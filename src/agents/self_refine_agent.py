"""
Self-Refine Agent - Actor-Critic pattern for section-level quality improvement.

Splits the article into sections, scores each on 5 dimensions,
and revises weak sections with targeted feedback.
"""

import json
import re
from typing import Dict, Any, List
from src.agents.base import BaseAgent


class SelfRefineAgent(BaseAgent):
    """Self-refine agent using actor-critic pattern."""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        refine_config = config.get("agents", {}).get("self_refine_agent", {})
        self.max_iterations = refine_config.get("max_iterations", 2)
        self.min_score = refine_config.get("min_score", 7.0)

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        self.log("开始自审自改（Self-Refine）...")

        article = state.get("longform_article", {})
        content = article.get("full_content", "")

        if not content:
            self.log("未找到文章内容，跳过自审", "WARNING")
            return state

        sections = self._split_sections(content)
        refined_sections = []
        refinement_log = []

        for i, section in enumerate(sections):
            if len(section) < 200:
                refined_sections.append(section)
                continue

            self.log(f"  审查第 {i+1}/{len(sections)} 个章节...")

            critique = self._critique_section(section)
            score = critique.get("score", 10)

            if score >= self.min_score:
                refined_sections.append(section)
                refinement_log.append({
                    "section_index": i, "score": score, "action": "kept"
                })
                continue

            revised = section
            for iteration in range(self.max_iterations):
                self.log(f"    修订第 {iteration+1} 次（分数: {score}）")
                revised = self._revise_section(revised, critique)

                critique = self._critique_section(revised)
                score = critique.get("score", 0)
                if score >= self.min_score:
                    break

            refined_sections.append(revised)
            refinement_log.append({
                "section_index": i,
                "final_score": score,
                "action": "revised",
                "iterations": iteration + 1
            })

        improved = "\n".join(refined_sections)
        article["full_content"] = improved
        article["word_count"] = len(improved)

        revised_count = sum(1 for r in refinement_log if r["action"] == "revised")
        self.log(f"自审完成，修订了 {revised_count} 个章节")

        return {
            **state,
            "longform_article": article,
            "self_refine_log": refinement_log,
            "current_step": "self_refine_completed"
        }

    def _split_sections(self, content: str) -> List[str]:
        parts = re.split(r'\n(?=## )', content)
        return [p for p in parts if p.strip()]

    def _critique_section(self, section: str) -> Dict[str, Any]:
        section_for_review = section[:3000] + "\n...(内容已截断)" if len(section) > 3000 else section

        prompt = f"""你是资深科技编辑，审查以下文章章节的质量。

**评分标准**（每项0-2分，总分10分）：
1. **逻辑连贯**：段落间是否有清晰逻辑，是否突兀跳转
2. **深度充分**：是否有实质性技术内容，而非空泛描述
3. **证据支撑**：论断是否有数据、案例或代码支撑
4. **AI痕迹**：是否过多使用AI套话（"值得注意的是"、"综上所述"等）
5. **可读性**：句子是否清晰，段落长度是否适中

**章节内容**：
{section_for_review}

请输出JSON格式的评分结果：
{{
  "score": <总分0-10>,
  "logic": <0-2>,
  "depth": <0-2>,
  "evidence": <0-2>,
  "ai_pattern": <0-2, 2=无AI痕迹>,
  "readability": <0-2>,
  "issues": ["具体问题1", "具体问题2"],
  "suggestions": ["具体建议1", "具体建议2"]
}}"""

        try:
            response = self._call_llm(prompt)
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return {"score": 7.0}
        except Exception as e:
            self.log(f"Critic调用失败: {e}", "WARNING")
            return {"score": 7.0}

    def _revise_section(self, section: str, critique: Dict[str, Any]) -> str:
        issues = critique.get("issues", [])
        suggestions = critique.get("suggestions", [])

        prompt = f"""你是资深科技编辑，请根据审稿意见修订以下章节。

**审稿意见**：
问题：
{chr(10).join(f"- {issue}" for issue in issues)}

建议：
{chr(10).join(f"- {s}" for s in suggestions)}

**修订要求**：
1. 只修改有问题的地方，保留原有优质内容
2. 保持Markdown格式
3. 保持原有章节标题
4. 不要添加新的章节
5. 替换AI套话为自然表达

**原文章节**：
{section}

请输出修订后的完整章节："""

        try:
            response = self._call_llm(prompt)
            revised = response.strip()
            if len(revised) < len(section) * 0.5:
                self.log("修订结果过短，保留原文", "WARNING")
                return section
            return revised
        except Exception as e:
            self.log(f"修订失败: {e}，保留原文", "WARNING")
            return section
