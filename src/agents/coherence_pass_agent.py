"""
Coherence Pass Agent - Full-article coherence review and fix.
"""

import re
from typing import Dict, Any
from src.agents.base import BaseAgent


class CoherencePassAgent(BaseAgent):
    """Full-article coherence pass agent."""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        self.log("开始全文一致性检查（Coherence Pass）...")

        article = state.get("longform_article", {})
        content = article.get("full_content", "")

        if not content:
            self.log("未找到文章内容，跳过一致性检查", "WARNING")
            return state

        if len(content) > 20000:
            improved = self._coherence_pass_chunked(content)
        else:
            improved = self._coherence_pass_single(content)

        article["full_content"] = improved
        article["word_count"] = len(improved)

        self.log(f"一致性检查完成，文章长度: {len(content)} -> {len(improved)}")

        return {
            **state,
            "longform_article": article,
            "coherence_pass_applied": True,
        }

    def _coherence_pass_single(self, content: str) -> str:
        """Single-pass coherence review for articles under 20k chars."""
        prompt = f"""你是一位资深科技编辑，正在审查一篇由多个章节拼接而成的技术文章。
请对以下全文进行一致性审查和润色，只修改需要改进的地方，保留原有优秀内容。

**审查重点**：
1. **过渡衔接**：章节之间的过渡是否自然？如果出现突兀跳转，添加1-2句过渡语
2. **重复内容**：是否有多个章节重复讨论同一个论点？如有，保留最详细的版本，其余用简短引用替代
3. **术语一致**：同一技术概念是否使用了不同叫法？统一为首次使用的术语
4. **AI痕迹**：是否出现"值得注意的是"、"综上所述"、"深入探讨"、"在当今的XX领域"等AI常见套话？替换为更自然的表达
5. **结尾重复**：总结部分是否只是前面内容的简单复述？如果是，改为前瞻性建议或行动号召

**重要规则**：
- 不要删除任何实质性内容
- 不要改变文章结构
- 只修改表述问题，不改变技术描述
- 保持专业但自然的写作风格

**原文**：
{content}

请输出修改后的完整文章（保持Markdown格式）："""

        try:
            response = self._call_llm(prompt)
            improved = response.strip()
            if len(improved) < len(content) * 0.7:
                self.log("一致性检查结果过短，可能丢失内容，保留原文", "WARNING")
                return content
            return improved
        except Exception as e:
            self.log(f"一致性检查失败: {e}，保留原文", "WARNING")
            return content

    def _coherence_pass_chunked(self, content: str) -> str:
        """Chunked coherence review for long articles (>20k chars)."""
        sections = re.split(r'\n(?=## )', content)
        if len(sections) <= 1:
            return self._coherence_pass_single(content)

        improved_sections = []
        overlap_context = ""

        for i, section in enumerate(sections):
            if overlap_context:
                section_with_context = f"[上一节末尾]: ...{overlap_context}\n\n[当前节]:\n{section}"
            else:
                section_with_context = section

            prompt = f"""你是一位资深科技编辑，审查文章的一个章节，确保它与上下文衔接自然。

**审查重点**：
1. 与上一节的过渡是否自然？如有突兀跳转，在开头添加1-2句过渡
2. 是否有AI套话（"值得注意的是"、"综上所述"等）？替换为自然表达
3. 是否与上一节内容重复？如有，简化重复部分

只输出修改后的当前章节内容（保持Markdown格式），不要输出上一节：

{section_with_context}"""

            try:
                response = self._call_llm(prompt)
                improved = response.strip()
                if len(improved) < len(section) * 0.5:
                    improved = section
                improved_sections.append(improved)
            except Exception:
                improved_sections.append(section)

            overlap_context = section[-500:] if len(section) > 500 else section

        return "\n".join(improved_sections)
