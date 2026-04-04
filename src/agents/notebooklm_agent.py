"""
NotebookLM 知识提取 Agent

自动化 nlm CLI 流程:
1. 创建笔记本（命名格式：VA_EP{XXX}_{主题}）
2. 批量添加 URL 作为资料源
3. 执行 3-5 轮结构化查询
4. 合成 knowledge_base.md

配额: 3-5 次查询/期，50 次/天
"""

import json
import subprocess
import time
import re
from datetime import datetime
from typing import Dict, Any, List, Optional
from src.agents.base import BaseAgent


class NotebookLMAgent(BaseAgent):
    """NotebookLM 知识提取 Agent"""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        nb_config = config.get("agents", {}).get("notebooklm_agent", {})
        if not nb_config:
            nb_config = config
        self.max_sources = nb_config.get("max_sources", 15)
        self.query_rounds = nb_config.get("query_rounds", 4)
        self.query_timeout = nb_config.get("query_timeout", 120)
        self.mock_mode = nb_config.get("mock_mode", False)
        self.notebook_prefix = nb_config.get("notebook_prefix", "VA_EP")

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行 NotebookLM 知识提取

        Args:
            state: 需要包含 collected_urls（阶段1产出）和 selected_ai_topic

        Returns:
            更新后的状态，包含 knowledge_base 和 notebooklm_metadata
        """
        self.log("开始 NotebookLM 知识提取...")

        selected_topic = state.get("selected_ai_topic", {})
        episode_number = state.get("episode_number", 0)
        topic_title = selected_topic.get("title", "unknown")
        collected_urls = state.get("collected_urls", [])

        self.log(f"主题: {topic_title}")
        self.log(f"可用 URL: {len(collected_urls)}")

        if self.mock_mode:
            result = self._mock_execute(episode_number, topic_title, collected_urls)
        else:
            result = self._real_execute(episode_number, topic_title, collected_urls)

        return {
            **state,
            "knowledge_base": result["knowledge_base"],
            "notebooklm_metadata": result["metadata"],
            "current_step": "notebooklm_completed",
        }

    def _real_execute(
        self,
        episode_number: int,
        topic_title: str,
        collected_urls: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        """真实执行 NotebookLM 流程"""

        # Step 1: 检查 nlm CLI
        if not self._check_nlm_cli():
            raise RuntimeError("nlm CLI 不可用，NotebookLM 是必须阶段。请先安装 nlm CLI 工具")

        # Step 2: 检查认证
        if not self._check_auth():
            raise RuntimeError("NotebookLM 未认证。请先运行 'nlm login' 完成认证")

        # Step 3: 创建笔记本
        topic_short = re.sub(r'[^\w\u4e00-\u9fff]', '_', topic_title)[:30]
        notebook_name = f"{self.notebook_prefix}{episode_number:03d}_{topic_short}"
        notebook_id = self._create_notebook(notebook_name)

        if not notebook_id:
            raise RuntimeError(f"创建 NotebookLM 笔记本失败: {notebook_name}")

        self.log(f"笔记本已创建: {notebook_name} (ID: {notebook_id})")

        # Step 4: 添加资料源
        sources_added = self._add_sources(notebook_id, collected_urls[:self.max_sources])
        self.log(f"已添加 {sources_added} 个资料源")

        # Step 5: 等待资料处理完成
        time.sleep(10)

        # Step 6: 结构化查询
        answers = self._run_queries(notebook_id, topic_title)

        # Step 7: 合成知识库
        knowledge_base = self._synthesize_knowledge_base(topic_title, answers)

        metadata = {
            "notebook_id": notebook_id,
            "notebook_name": notebook_name,
            "source_count": sources_added,
            "query_count": len(answers),
            "created_at": datetime.now().isoformat(),
            "sources": [u.get("url", "") for u in collected_urls[:self.max_sources]],
        }

        return {"knowledge_base": knowledge_base, "metadata": metadata}

    # ---- nlm CLI 操作 ----

    def _check_nlm_cli(self) -> bool:
        """检查 nlm CLI 是否可用"""
        try:
            result = subprocess.run(
                ["nlm", "--version"],
                capture_output=True, text=True, timeout=10,
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def _check_auth(self) -> bool:
        """检查 NotebookLM 认证状态"""
        try:
            result = subprocess.run(
                ["nlm", "login", "--check"],
                capture_output=True, text=True, timeout=30,
            )
            return "Authentication valid" in result.stdout or "✓" in result.stdout
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def _create_notebook(self, name: str) -> Optional[str]:
        """创建 NotebookLM 笔记本"""
        try:
            result = subprocess.run(
                ["nlm", "notebook", "create", name],
                capture_output=True, text=True, timeout=60,
            )
            # 从输出中提取 notebook_id
            match = re.search(r'[\w-]{8,}[\w-]*', result.stdout.strip().split('\n')[-1] if result.stdout.strip() else "")
            if match:
                return match.group()
            # 尝试 JSON 解析
            try:
                data = json.loads(result.stdout)
                return data.get("id") or data.get("notebook_id")
            except (json.JSONDecodeError, AttributeError):
                pass
            self.log(f"创建笔记本输出: {result.stdout[:200]}", "DEBUG")
            return None
        except subprocess.TimeoutExpired:
            self.log("创建笔记本超时", "ERROR")
            return None

    def _add_sources(self, notebook_id: str, urls: List[Dict[str, str]]) -> int:
        """批量添加 URL 资料源"""
        added = 0
        for url_info in urls:
            url = url_info.get("url", "")
            if not url.startswith("http"):
                continue
            try:
                result = subprocess.run(
                    ["nlm", "source", "add", notebook_id, "--url", url, "--wait"],
                    capture_output=True, text=True, timeout=120,
                )
                if result.returncode == 0:
                    added += 1
                    self.log(f"  已添加: {url[:60]}...")
                else:
                    self.log(f"  添加失败: {url[:60]}... - {result.stderr[:100]}", "WARNING")
            except subprocess.TimeoutExpired:
                self.log(f"  添加超时: {url[:60]}...", "WARNING")
        return added

    def _run_queries(self, notebook_id: str, topic: str) -> List[Dict[str, str]]:
        """执行结构化查询"""
        queries = self._build_queries(topic)
        answers = []

        for i, q in enumerate(queries[:self.query_rounds], 1):
            self.log(f"  查询 {i}/{min(len(queries), self.query_rounds)}: {q['name']}")
            answer = self._query_notebook(notebook_id, q["prompt"])
            if answer:
                answers.append({
                    "name": q["name"],
                    "question": q["prompt"],
                    "answer": answer,
                })
                self.log(f"  回答长度: {len(answer)} 字符")
            else:
                self.log(f"  查询无结果", "WARNING")

        return answers

    def _query_notebook(self, notebook_id: str, question: str) -> Optional[str]:
        """查询单个问题"""
        try:
            result = subprocess.run(
                ["nlm", "query", "notebook", notebook_id, question,
                 "--timeout", str(self.query_timeout)],
                capture_output=True, text=True, timeout=self.query_timeout + 30,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
            return None
        except subprocess.TimeoutExpired:
            self.log("查询超时", "WARNING")
            return None

    def _build_queries(self, topic: str) -> List[Dict[str, str]]:
        """构建结构化查询列表"""
        return [
            {
                "name": "技术全景",
                "prompt": (
                    f"请概述「{topic}」的核心技术架构和关键组件。"
                    "重点提取：技术演进路线、核心算法名称、主要架构模式、"
                    "关键技术指标。请引用具体来源。"
                ),
            },
            {
                "name": "深度实现",
                "prompt": (
                    f"详细解析「{topic}」的实现细节，包括："
                    "核心算法流程、关键代码架构、性能优化策略、"
                    "与竞品的技术对比。请提供具体的技术参数和数据。"
                ),
            },
            {
                "name": "实战应用",
                "prompt": (
                    f"列出「{topic}」的真实应用场景和案例："
                    "工业级部署方案、开源项目实战案例、性能基准数据、"
                    "开发者最佳实践和常见踩坑经验。"
                ),
            },
            {
                "name": "前沿趋势",
                "prompt": (
                    f"「{topic}」领域的最新研究突破和发展方向："
                    "2025-2026年重要论文和技术趋势、未解决的挑战、"
                    "未来可能的突破点。"
                ),
            },
            {
                "name": "对比分析",
                "prompt": (
                    f"对比「{topic}」领域的主要技术方案："
                    "各方案的优缺点、适用场景、性能数据、选型建议。"
                    "请用具体数据支撑对比结论。"
                ),
            },
        ]

    def _synthesize_knowledge_base(self, topic: str, answers: List[Dict[str, str]]) -> str:
        """合成结构化知识库文档"""
        sections = []
        sections.append(f"# 知识库：{topic}\n")
        sections.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        sections.append(f"查询轮数: {len(answers)}\n")

        for ans in answers:
            sections.append(f"## {ans['name']}\n")
            sections.append(ans["answer"])
            sections.append("")

        return "\n".join(sections)

    # ---- Mock 模式 ----

    def _mock_execute(
        self,
        episode_number: int,
        topic_title: str,
        collected_urls: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        """Mock 模式：不调用 nlm CLI，返回模拟数据"""
        self.log("使用 mock 模式生成模拟知识库")

        knowledge_base = self._generate_mock_knowledge_base(topic_title)

        metadata = {
            "notebook_id": "mock_notebook_id",
            "notebook_name": f"{self.notebook_prefix}{episode_number:03d}_mock",
            "source_count": len(collected_urls),
            "query_count": 4,
            "created_at": datetime.now().isoformat(),
            "mock": True,
        }

        return {"knowledge_base": knowledge_base, "metadata": metadata}

    def _generate_mock_knowledge_base(self, topic: str) -> str:
        """生成 mock 知识库"""
        return f"""# 知识库：{topic}

生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}
模式: Mock（用于测试）

## 技术全景

{topic}的核心技术架构包括以下关键组件：
- 核心算法: 基于深度学习的端到端架构
- 关键指标: 在标准基准测试中达到SOTA性能
- 演进路线: 从传统方法到神经网络，再到大模型范式

## 深度实现

实现细节：
- 模型架构: Transformer-based，约1B参数
- 训练数据: 超过10000小时标注数据
- 优化策略: 混合精度训练、梯度累积、分布式训练
- 性能: 推理延迟<200ms (GPU), <500ms (CPU)

## 实战应用

真实应用案例：
1. 实时语音助手: 集成到智能设备中，支持自然语言交互
2. 会议转录: 自动将会议录音转为文字，准确率>95%
3. 客服系统: 智能语音客服，处理常见问题

## 前沿趋势

最新研究方向：
- 端到端语音大模型: 统一理解与生成
- 全双工对话: 同时听和说
- 多语言统一: 单一模型支持100+语言
- 边缘部署: 量化到4-bit，在手机上实时运行
"""
