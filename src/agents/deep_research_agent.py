"""
深度调研 Agent - 6维度多源调研

借鉴 DevFox Pulse 的 6-dimension research 方法：
1. 事实层：核心技术事实、数据、时间线
2. 开源层：GitHub 项目、开源工具
3. 闭源/商业层：官方文档、API、商业产品
4. 社区层：社区讨论、用户反馈
5. 实战层：教程、部署指南、性能基准
6. 前沿层：最新论文、研究突破
"""

import json
import re
from datetime import datetime
from typing import Dict, Any, List
from src.agents.base import BaseAgent


class DeepResearchAgent(BaseAgent):
    """深度调研 Agent - 6维度多源调研"""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        research_config = config.get("agents", {}).get("deep_research_agent", {})
        if not research_config:
            research_config = config
        self.max_urls = research_config.get("max_urls", 15)
        self.search_provider = research_config.get("search_provider", "zhipuai")
        self.mock_mode = research_config.get("mock_mode", False)

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行 6 维度深度调研

        Args:
            state: 工作流状态（需要 selected_ai_topic）

        Returns:
            更新后的状态，包含 research_data 和 collected_urls
        """
        self.log("开始 6 维度深度调研...")

        selected_topic = state.get("selected_ai_topic")
        if not selected_topic:
            raise ValueError("没有找到选中的话题")

        topic_title = selected_topic.get("title", "")
        topic_desc = selected_topic.get("description", "")
        keywords = selected_topic.get("tags", [])

        self.log(f"调研主题: {topic_title}")

        if self.mock_mode:
            research_data = self._mock_research(topic_title, topic_desc, keywords)
        else:
            research_data = self._do_research(topic_title, topic_desc, keywords)

        self.log(f"调研完成，收集到 {len(research_data.get('collected_urls', []))} 个 URL")

        return {
            **state,
            "research_data": research_data,
            "research_summary": self._generate_summary(research_data),
            "collected_urls": research_data.get("collected_urls", []),
            "current_step": "deep_research_completed",
        }

    def _do_research(self, title: str, desc: str, keywords: List[str]) -> Dict[str, Any]:
        """执行真实调研"""
        if self.search_provider == "zhipuai":
            return self._research_with_zhipuai(title, desc, keywords)
        else:
            self.log(f"搜索提供商 {self.search_provider} 未支持，使用 mock", "WARNING")
            return self._mock_research(title, desc, keywords)

    def _research_with_zhipuai(self, title: str, desc: str, keywords: List[str]) -> Dict[str, Any]:
        """通过智谱AI联网搜索进行 6 维度调研"""
        keyword_str = ", ".join(keywords[:5]) if keywords else ""

        prompt = f"""请对以下技术主题进行全面的 6 维度调研，并返回 JSON 格式结果。

**主题**: {title}
**描述**: {desc}
**关键词**: {keyword_str}

请按以下 6 个维度搜索并整理信息：

1. **事实层**: 核心技术事实、关键数据、发展时间线、涉及的主要项目/公司
2. **开源层**: GitHub 上的相关开源项目（给出仓库 URL）、awesome 列表、社区实现
3. **闭源/商业层**: 官方文档链接、商业产品、API 文档 URL、云服务方案
4. **社区层**: 技术社区讨论要点、用户真实反馈、优缺点评价
5. **实战层**: 教程链接、部署指南、性能基准数据、最佳实践
6. **前沿层**: 最新论文（arxiv 链接）、2025-2026 研究突破、未来趋势

**输出 JSON 格式**:
{{
  "dimensions": {{
    "facts": ["事实1", "事实2", ...],
    "opensource": [
      {{"name": "项目名", "url": "GitHub URL", "description": "简介"}}
    ],
    "commercial": [
      {{"name": "产品/文档名", "url": "链接", "description": "简介"}}
    ],
    "community": ["观点1", "观点2", ...],
    "practice": [
      {{"title": "教程/指南标题", "url": "链接", "description": "简介"}}
    ],
    "frontier": [
      {{"title": "论文/研究标题", "url": "链接", "description": "简介"}}
    ]
  }},
  "summary": "一段话总结调研发现"
}}

请确保所有 URL 都是真实可访问的链接。"""

        try:
            response = self._call_llm(prompt)
            research_data = self._parse_json_response(response)
        except Exception as e:
            self.log(f"调研查询失败: {e}", "ERROR")
            raise RuntimeError(f"深度调研 LLM 调用失败: {e}")

        # 提取所有 URL
        collected_urls = self._extract_urls(research_data)
        research_data["collected_urls"] = collected_urls[:self.max_urls]
        research_data["query"] = f"{title} {desc}"
        research_data["researched_at"] = datetime.now().isoformat()

        return research_data

    def _extract_urls(self, data: Dict[str, Any]) -> List[Dict[str, str]]:
        """从调研结果中提取所有 URL"""
        urls = []
        seen = set()
        dimensions = data.get("dimensions", {})

        for dim_name, items in dimensions.items():
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict):
                        url = item.get("url", "")
                        if url and url.startswith("http") and url not in seen:
                            seen.add(url)
                            urls.append({
                                "url": url,
                                "title": item.get("name", item.get("title", "")),
                                "type": dim_name,
                            })

        return urls

    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """解析 LLM 的 JSON 响应（带多重修复）"""
        # 尝试1: 直接解析
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            pass

        # 尝试2: 提取 JSON 块
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            json_str = json_match.group()
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass

            # 尝试3: 修复常见 JSON 错误
            try:
                # 修复尾随逗号（,} 或 ,]）
                fixed = re.sub(r',\s*([}\]])', r'\1', json_str)
                # 修复缺少逗号（"string"\n"string" → "string",\n"string"）
                fixed = re.sub(r'"\s*\n\s*"', '",\n"', fixed)
                # 修复缺少逗号（]\n[ → ],\n[）
                fixed = re.sub(r'\]\s*\n\s*\[', '],\n[', fixed)
                # 修复单引号
                fixed = fixed.replace("'", '"')
                return json.loads(fixed)
            except json.JSONDecodeError:
                pass

            # 尝试4: 逐步截断修复（从末尾去掉不完整的部分）
            for i in range(1, 5):
                try:
                    truncated = json_str[:-(i * 50)] + '}'
                    return json.loads(truncated)
                except json.JSONDecodeError:
                    continue

        raise ValueError("无法解析调研结果 JSON")

    def _mock_research(self, title: str, desc: str, keywords: List[str]) -> Dict[str, Any]:
        """生成 mock 调研数据（用于测试）"""
        return {
            "query": f"{title} {desc}",
            "dimensions": {
                "facts": [
                    f"{title}是当前AI领域的重要技术方向",
                    f"该技术在2024-2026年经历了快速发展",
                    "主要参与者包括OpenAI、Google、Meta等",
                ],
                "opensource": [
                    {"name": f"{title}-examples", "url": f"https://github.com/example/{title.replace(' ', '-')}", "description": "示例项目和代码"},
                ],
                "commercial": [
                    {"name": "Official Documentation", "url": "https://docs.example.com", "description": "官方技术文档"},
                ],
                "community": [
                    "社区普遍认为这项技术降低了开发门槛",
                    "性能方面仍有提升空间",
                ],
                "practice": [
                    {"title": f"{title} Best Practices", "url": "https://example.com/tutorial", "description": "最佳实践指南"},
                ],
                "frontier": [
                    {"title": f"Latest Advances in {title}", "url": "https://arxiv.org/abs/2501.00001", "description": "最新研究论文"},
                ],
            },
            "collected_urls": [
                {"url": "https://github.com/example/project", "title": "Example Project", "type": "opensource"},
                {"url": "https://docs.example.com", "title": "Official Docs", "type": "commercial"},
                {"url": "https://example.com/tutorial", "title": "Tutorial", "type": "practice"},
            ],
            "summary": f"{title}是一项快速发展的技术，在多个领域有广泛应用前景。",
            "researched_at": datetime.now().isoformat(),
            "mock": True,
        }

    def _generate_summary(self, research_data: Dict[str, Any]) -> str:
        """生成调研摘要"""
        dims = research_data.get("dimensions", {})
        url_count = len(research_data.get("collected_urls", []))
        summary = research_data.get("summary", "")

        return (
            f"**调研主题**: {research_data.get('query', '')}\n\n"
            f"**收集资料**: {url_count} 个 URL\n\n"
            f"**摘要**: {summary}\n\n"
            f"**维度覆盖**: "
            + ", ".join(dims.keys())
        )
