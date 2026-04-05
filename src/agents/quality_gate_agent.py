"""
Quality Gate Agent - Unified quality scoring with targeted revision.

Scores on 6 dimensions using LLM-as-judge. If below threshold,
performs targeted revision of weakest dimensions. Max 2 cycles.

Dimensions and weights:
- content_depth (20%): technical detail, data support, depth of analysis
- logical_coherence (20%): section transitions, logical progression, no redundancy
- factual_accuracy (20%): verifiable claims, data specificity, references
- deai_score (15%): absence of AI patterns, sentence variety, natural language
- readability (15%): paragraph balance, formatting, heading clarity
- practical_value (10%): code examples, actionable advice, tool recommendations
"""

import re
import json
from typing import Dict, Any, List
from datetime import datetime

from src.agents.base import BaseAgent


class QualityGateAgent(BaseAgent):
    """Quality gate with targeted revision."""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        gate_config = config.get("agents", {}).get("quality_gate_agent", {})
        self.min_score = gate_config.get("min_score", 75)
        self.max_revision_cycles = gate_config.get("max_revision_cycles", 2)
        self.dimensions = {
            "content_depth": {"weight": 0.20, "name": "内容深度"},
            "logical_coherence": {"weight": 0.20, "name": "逻辑连贯"},
            "factual_accuracy": {"weight": 0.20, "name": "事实准确性"},
            "deai_score": {"weight": 0.15, "name": "去AI化程度"},
            "readability": {"weight": 0.15, "name": "可读性"},
            "practical_value": {"weight": 0.10, "name": "实践价值"},
        }

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute quality gate evaluation and targeted revision.

        Args:
            state: Workflow state containing longform_article

        Returns:
            Updated state with quality_gate_report and quality_gate_passed
        """
        self.log("开始质量门禁检查...")

        article = state.get("longform_article", {})
        if isinstance(article, str):
            content = article
            article = {"full_content": article}
        elif isinstance(article, dict):
            content = article.get("full_content", "")
        else:
            self.log("未找到文章内容，跳过质量门禁", "WARNING")
            return {**state, "quality_gate_passed": False}

        if not content:
            self.log("文章内容为空，跳过质量门禁", "WARNING")
            return {**state, "quality_gate_passed": False}

        for cycle in range(self.max_revision_cycles + 1):
            self.log(f"质量评估第 {cycle} 轮...")
            scores = self._score_with_llm(content)
            total = round(
                sum(scores.get(dim, 0) * info["weight"]
                    for dim, info in self.dimensions.items()),
                1
            )

            # Log dimension scores
            dim_log = ", ".join(
                f"{self.dimensions[d]['name']}={scores.get(d, 0)}"
                for d in self.dimensions
            )
            self.log(f"  总分: {total}/{self.min_score} | {dim_log}")

            if total >= self.min_score:
                self.log(f"质量门禁通过（{total}分）")
                report = {
                    "total_score": total,
                    "dimension_scores": scores,
                    "passed": True,
                    "revision_cycles": cycle,
                    "evaluated_at": datetime.now().isoformat(),
                }
                return {
                    **state,
                    "longform_article": article,
                    "quality_gate_report": report,
                    "quality_gate_passed": True,
                    "current_step": "quality_gate_completed",
                }

            # Need revision
            if cycle < self.max_revision_cycles:
                self.log(f"质量不达标（{total}<{self.min_score}），进行第 {cycle + 1} 轮修订")
                weakest = self._find_weakest(scores, n=2)
                weak_names = [self.dimensions[d]["name"] for d in weakest]
                self.log(f"  最弱维度: {weak_names}")

                content = self._targeted_revision(content, weakest, scores)
                article["full_content"] = content
                article["word_count"] = len(content)

        # Final attempt - did not pass after all revisions
        self.log(f"质量门禁未通过（{total}分），保存文章", "WARNING")

        report = {
            "total_score": total,
            "dimension_scores": scores,
            "passed": False,
            "revision_cycles": self.max_revision_cycles,
            "evaluated_at": datetime.now().isoformat(),
            "note": "Quality below threshold after max revisions",
        }
        return {
            **state,
            "longform_article": article,
            "quality_gate_report": report,
            "quality_gate_passed": False,
            "current_step": "quality_gate_completed",
        }

    def _score_with_llm(self, content: str) -> Dict[str, float]:
        """
        Use LLM as judge to score article on 6 dimensions (0-100).

        For long articles, uses a sampled representation to stay within
        context limits.
        """
        if len(content) > 10000:
            sample = (
                content[:3000]
                + "\n...(中间部分省略)...\n"
                + content[len(content) // 2 - 1500:len(content) // 2 + 1500]
                + "\n...(省略)...\n"
                + content[-3000:]
            )
        else:
            sample = content

        prompt = f"""你是资深科技编辑，请对以下文章进行多维度质量评分。评分维度（每项0-100分）：

1. **内容深度**（20%）：技术细节是否充分？是否有深度分析？还是表面描述？
2. **逻辑连贯**（20%）：章节之间逻辑递进是否自然？过渡是否流畅？是否有重复或跳跃？
3. **事实准确性**（20%）：技术描述是否准确？数据是否具体？引用是否可靠？
4. **去AI化程度**（15%）：是否避免了AI套话？语言是否自然？句子长度是否有变化？
5. **可读性**（15%）：段落是否适中？格式是否丰富？标题是否清晰？
6. **实践价值**（10%）：是否有代码示例？是否有可操作建议？是否有避坑指南？

文章内容：
{sample}

请输出JSON格式评分：
{{"content_depth": <0-100>, "logical_coherence": <0-100>, "factual_accuracy": <0-100>, "deai_score": <0-100>, "readability": <0-100>, "practical_value": <0-100>, "brief_comment": "<一句话总评>"}}"""

        try:
            response = self._call_llm(prompt)
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                scores = json.loads(json_match.group())
                # Ensure all dimensions present with default fallback
                for dim in self.dimensions:
                    if dim not in scores:
                        scores[dim] = 70
                return scores
            else:
                self.log("LLM评分返回格式异常，使用默认分数", "WARNING")
                return {dim: 70 for dim in self.dimensions}
        except Exception as e:
            self.log(f"LLM评分失败: {e}，使用默认分数", "WARNING")
            return {dim: 70 for dim in self.dimensions}

    def _find_weakest(self, scores: Dict[str, float], n: int = 2) -> List[str]:
        """Find the n weakest dimensions by score."""
        return [dim for dim, _ in sorted(scores.items(), key=lambda x: x[1])[:n]]

    def _targeted_revision(
        self,
        content: str,
        weak_dims: List[str],
        scores: Dict[str, float]
    ) -> str:
        """
        Perform targeted revision focusing on the weakest dimensions.

        Uses LLM to revise only the aspects that scored lowest,
        preserving the rest of the content.
        """
        dim_scores = {
            self.dimensions[d]["name"]: scores.get(d, 0)
            for d in weak_dims
        }

        dim_list = "\n".join(
            f"- {name}: {score}分"
            for name, score in dim_scores.items()
        )

        strategy_map = {
            "内容深度": "- 补充技术细节和性能数据和基准测试结果\n- 添加代码示例（如适用）\n- 增加对比分析和具体案例",
            "逻辑连贯": "- 在章节间添加过渡句\n- 消除重复论述\n- 确保逻辑递进（背景->原理->实践->展望）",
            "事实准确性": "- 检查技术描述准确性\n- 补充具体版本号、发布日期\n- 添加数据来源",
            "去AI化程度": '- 替换"值得注意的是"、"综上所述"等AI套话\n- 调整句式，混合长短句\n- 增加设问句或个人观点',
            "可读性": "- 拆分过长段落\n- 增加列表或表格\n- 优化标题层级",
            "实践价值": "- 添加可操作的步骤指南\n- 补充工具推荐\n- 增加避坑建议",
        }

        strategies = "\n".join(
            strategy_map.get(name, "")
            for name in dim_scores.keys()
        )

        # For long articles, only send the first portion for revision
        if len(content) > 12000:
            content_for_llm = content[:12000]
            tail = content[12000:]
        else:
            content_for_llm = content
            tail = ""

        prompt = f"""你是资深科技编辑，请对以下文章进行针对性改进。

需要改进的维度:
{dim_list}

针对每个弱项的改进策略:
{strategies}

**重要**: 只改进指定维度相关的内容，不要改动其他部分。保持原有Markdown格式和文章结构不变。

文章:
{content_for_llm}

请输出改进后的完整文章（保持Markdown格式）："""

        try:
            response = self._call_llm(prompt)
            improved = response.strip()

            # Validate: reject if too short (content loss)
            if len(improved) < len(content_for_llm) * 0.6:
                self.log("修订结果过短，保留原文", "WARNING")
                return content

            # Reattach tail for long articles
            if tail:
                improved = improved + tail

            return improved

        except Exception as e:
            self.log(f"目标修订失败: {e}，保留原文", "WARNING")
            return content
