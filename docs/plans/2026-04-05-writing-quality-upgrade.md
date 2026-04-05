# Writing Quality Upgrade Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Upgrade the series mode pipeline with 5 quality improvements: section summary context, coherence pass, self-refine loop, technical De-AI, and quality gate with retry.

**Architecture:** Add 3 new agents (CoherencePassAgent, TechnicalDeAIAgent, QualityGateAgent) and modify the existing LongFormGeneratorAgent to pass section summaries between sections. The SeriesOrchestrator pipeline extends from 4-stage to 7-stage: DeepResearch -> NotebookLM -> LongForm(enhanced) -> CoherencePass -> DeAI -> QualityGate -> [Retry if needed] -> Save.

**Tech Stack:** Python 3.x, ZhipuAI GLM API, existing BaseAgent framework, regex-based analysis.

---

## Task 1: Add Section Summary Tracking to LongFormGeneratorAgent

**Why:** Sections are generated independently with only title-level context. Passing 2-3 sentence summaries between sections will dramatically improve logical coherence.

**Files:**
- Modify: `src/agents/longform_generator.py:106-190` (the `_generate_article_stages` method and related methods)

**Step 1: Add `_summarize_section` method to LongFormGeneratorAgent**

Add this new method after `_extract_relevant_kb` (around line 1278):

```python
def _summarize_section(self, section_content: str, max_chars: int = 150) -> str:
    """
    Generate a brief summary of a section for passing as context to the next section.

    Uses a fast, low-token LLM call to extract key points.

    Args:
        section_content: The full text of the completed section.
        max_chars: Maximum characters for the summary.

    Returns:
        A 2-3 sentence summary string.
    """
    # Strip markdown headers and code blocks for a cleaner summary input
    clean = re.sub(r'```.*?```', '[代码块]', section_content, flags=re.DOTALL)
    clean = re.sub(r'#{1,6}\s+', '', clean)
    # Truncate to avoid excessive tokens
    if len(clean) > 1500:
        clean = clean[:1500]

    prompt = f"""用2-3句话总结以下章节的核心内容和关键结论。只输出总结，不要加前缀：

{clean}"""

    try:
        response = self._call_llm(prompt)
        summary = response.strip()
        # Hard truncate if LLM ignores instructions
        if len(summary) > max_chars:
            summary = summary[:max_chars] + "..."
        return summary
    except Exception:
        # Fallback: use first 100 chars
        text = section_content.replace('\n', ' ')[:max_chars]
        return text + "..." if len(text) == max_chars else text
```

**Step 2: Modify `_generate_article_stages` to track section summaries**

Change the section generation loop (lines 131-158) to build a `section_summaries` dict alongside `sections_content`:

```python
# REPLACE the existing loop block (lines 131-158) with:
full_content = ""
sections_content = {}
section_summaries = {}  # NEW: track summaries for context
previous_sections = []  # track section titles

generator_config = self.config.get("agents", {}).get("longform_generator", {})
enable_context = generator_config.get("enable_context_window", True)

for idx, section in enumerate(outline.get('sections', []), 1):
    self.log(f"  正在生成第 {idx}/{len(outline.get('sections', []))} 节: {section.get('title', '')}")

    if enable_context:
        section_content = self._expand_section(
            section, research_data, topic_data,
            previous_sections, knowledge_base,
            section_summaries  # NEW: pass summaries
        )
    else:
        section_content = self._expand_section(
            section, research_data, topic_data,
            previous_sections=None, knowledge_base=knowledge_base,
            section_summaries=None
        )

    section_content = self._normalize_section_headers(section_content, section.get('title'))
    full_content += f"{section_content}\n\n"
    sections_content[section.get('title')] = section_content

    # NEW: Generate summary for next section's context
    try:
        summary = self._summarize_section(section_content)
        section_summaries[section.get('title')] = summary
        self.log(f"    Section summary: {summary[:80]}...")
    except Exception:
        section_summaries[section.get('title')] = ""

    previous_sections.append(section.get('title'))
```

**Step 3: Modify `_expand_section` signature to accept `section_summaries`**

Change the method signature (line 307) and body:

```python
def _expand_section(self, section: Dict[str, Any], research_data: Dict[str, Any],
                   topic_data: Dict[str, Any], previous_sections: list = None,
                   knowledge_base: str = "", section_summaries: dict = None) -> str:
```

**Step 4: Modify `_build_section_context` to include summaries**

Change the signature (line 814) to accept `section_summaries`:

```python
def _build_section_context(self, current_title: str, previous_sections: list,
                          topic_data: Dict[str, Any],
                          section_summaries: dict = None) -> str:
```

Then update the method body to inject summaries into context. After the existing `previous_sections` block (around line 836), add:

```python
# Inject section summaries for coherence
if section_summaries and previous_sections:
    context_parts.append(f"\n**前面章节的核心内容摘要**：")
    for prev_title in previous_sections:
        summary = section_summaries.get(prev_title, "")
        if summary:
            context_parts.append(f"- {prev_title}：{summary}")
```

**Step 5: Update the call to `_build_section_context` inside `_expand_section`**

In `_expand_section` (line 330), update the call:

```python
context = self._build_section_context(
    section_title, previous_sections, topic_data,
    section_summaries  # NEW
)
```

**Step 6: Verify existing tests still pass**

Run: `cd /Users/z/Documents/work/content-forge-ai/test && PYTHONPATH=/Users/z/Documents/work/content-forge-ai python test_storage.py`
Expected: PASS (no changes to storage layer)

**Step 7: Commit**

```bash
git add src/agents/longform_generator.py
git commit -m "feat: pass section summaries between sections for logical coherence"
```

---

## Task 2: Create CoherencePassAgent (Full-Article Review)

**Why:** Sections generated independently have disjointed transitions, repetitive content, and inconsistent terminology. A coherence pass over the assembled article fixes this.

**Files:**
- Create: `src/agents/coherence_pass_agent.py`
- Modify: `src/agents/__init__.py` (register the new agent)
- Modify: `src/series_orchestrator.py` (add stage 4b)

**Step 1: Create `src/agents/coherence_pass_agent.py`**

```python
"""
Coherence Pass Agent - Full-article coherence review and fix.

Runs after all sections are assembled. Uses a single LLM call to:
1. Fix repetitive phrases across sections
2. Smooth transitions between independently-generated sections
3. Ensure consistent terminology throughout
4. Remove redundant content covered in multiple sections
"""

import re
from typing import Dict, Any
from src.agents.base import BaseAgent


class CoherencePassAgent(BaseAgent):
    """Full-article coherence pass agent."""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        self.max_review_tokens = 4000  # Max tokens for the review prompt

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute coherence pass on the full article.

        Args:
            state: Workflow state containing longform_article.

        Returns:
            Updated state with coherent article content.
        """
        self.log("开始全文一致性检查（Coherence Pass）...")

        article = state.get("longform_article", {})
        content = article.get("full_content", "")

        if not content:
            self.log("未找到文章内容，跳过一致性检查", "WARNING")
            return state

        # If article is very long, process in chunks with overlap
        if len(content) > 20000:
            improved = self._coherence_pass_chunked(content)
        else:
            improved = self._coherence_pass_single(content)

        # Update the article
        article["full_content"] = improved
        article["word_count"] = len(improved)

        self.log(f"一致性检查完成，文章长度: {len(content)} -> {len(improved)}")

        return {
            **state,
            "longform_article": article,
            "coherence_pass_applied": True,
            "current_step": "coherence_pass_completed"
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
            # Validate the response is reasonable
            if len(improved) < len(content) * 0.7:
                self.log("一致性检查结果过短，可能丢失内容，保留原文", "WARNING")
                return content
            return improved
        except Exception as e:
            self.log(f"一致性检查失败: {e}，保留原文", "WARNING")
            return content

    def _coherence_pass_chunked(self, content: str) -> str:
        """
        Chunked coherence review for long articles (>20k chars).
        Process each major section boundary (## headers) with overlap.
        """
        sections = re.split(r'\n(?=## )', content)
        if len(sections) <= 1:
            return self._coherence_pass_single(content)

        improved_sections = []
        overlap_context = ""

        for i, section in enumerate(sections):
            # Include previous section's tail for transition context
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
                    improved = section  # Keep original if result is too short
                improved_sections.append(improved)
            except Exception:
                improved_sections.append(section)

            # Store tail of current section for next iteration's context
            overlap_context = section[-500:] if len(section) > 500 else section

        return "\n".join(improved_sections)
```

**Step 2: Register in `src/agents/__init__.py`**

Add the import and registry entry:

```python
from src.agents.coherence_pass_agent import CoherencePassAgent

# In AGENT_REGISTRY, add:
"coherence_pass_agent": CoherencePassAgent,
```

**Step 3: Add to SeriesOrchestrator pipeline**

In `src/series_orchestrator.py`, modify `_init_agents` to add the new agent:

```python
# Add import at top of _init_agents method
from src.agents.coherence_pass_agent import CoherencePassAgent

# Add after longform_generator initialization:
if agents_config.get("coherence_pass_agent", {}).get("enabled", True):
    try:
        agents["coherence_pass_agent"] = CoherencePassAgent(
            config=full_config,
            prompts=self.prompts
        )
        logger.info("Initialized agent: coherence_pass_agent")
    except Exception as e:
        logger.warning(f"Failed to initialize coherence_pass_agent: {e}")
```

In `_execute_workflow`, add stage 3.5 after longform generation (after line 337):

```python
# ========== 阶段3.5：全文一致性检查 ==========
if "coherence_pass_agent" in self.agents:
    logger.info("===== 阶段3.5：全文一致性检查（Coherence Pass）=====")
    state = _call_agent_safely("coherence_pass_agent", state)
```

**Step 4: Add config entry in `config/config.yaml`**

Under `agents:`, add:

```yaml
  # 全文一致性检查Agent（新增）
  coherence_pass_agent:
    enabled: true
    max_review_tokens: 4000
```

**Step 5: Commit**

```bash
git add src/agents/coherence_pass_agent.py src/agents/__init__.py src/series_orchestrator.py config/config.yaml
git commit -m "feat: add CoherencePassAgent for full-article coherence review"
```

---

## Task 3: Create Self-Refine Loop (Actor-Critic Pattern)

**Why:** A single-pass generation often has quality issues. A critic-revise cycle catches and fixes problems before moving on.

**Files:**
- Create: `src/agents/self_refine_agent.py`
- Modify: `src/agents/__init__.py` (register)
- Modify: `src/series_orchestrator.py` (add stage 3.7)

**Step 1: Create `src/agents/self_refine_agent.py`**

```python
"""
Self-Refine Agent - Actor-Critic pattern for section-level quality improvement.

After each section is generated, a critic LLM call evaluates it against specific
criteria. If issues are found, a revision call is made. Max 2 iterations.
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
        """
        Execute self-refine on the article.

        Reviews the article section by section, identifies weak sections,
        and revises them.

        Args:
            state: Workflow state with longform_article.

        Returns:
            Updated state with refined article.
        """
        self.log("开始自审自改（Self-Refine）...")

        article = state.get("longform_article", {})
        content = article.get("full_content", "")

        if not content:
            self.log("未找到文章内容，跳过自审", "WARNING")
            return state

        # Split into sections by ## headers
        sections = self._split_sections(content)

        refined_sections = []
        refinement_log = []

        for i, section in enumerate(sections):
            if len(section) < 200:  # Skip very short sections
                refined_sections.append(section)
                continue

            self.log(f"  审查第 {i+1}/{len(sections)} 个章节...")

            # Critic phase
            critique = self._critique_section(section)

            if critique.get("score", 10) >= self.min_score:
                refined_sections.append(section)
                refinement_log.append({
                    "section_index": i,
                    "score": critique["score"],
                    "action": "kept"
                })
                continue

            # Revise phase (up to max_iterations)
            revised = section
            for iteration in range(self.max_iterations):
                self.log(f"    修订第 {iteration+1} 次（分数: {critique.get('score', 'N/A')}）")
                revised = self._revise_section(revised, critique)

                # Re-critique
                critique = self._critique_section(revised)
                if critique.get("score", 0) >= self.min_score:
                    break

            refined_sections.append(revised)
            refinement_log.append({
                "section_index": i,
                "final_score": critique.get("score", 0),
                "action": "revised",
                "iterations": iteration + 1
            })

        # Reassemble
        improved = "\n\n".join(refined_sections)
        article["full_content"] = improved
        article["word_count"] = len(improved)

        self.log(f"自审完成，修订了 {sum(1 for r in refinement_log if r['action'] == 'revised')} 个章节")

        return {
            **state,
            "longform_article": article,
            "self_refine_log": refinement_log,
            "current_step": "self_refine_completed"
        }

    def _split_sections(self, content: str) -> List[str]:
        """Split article into sections by ## headers."""
        parts = re.split(r'\n(?=## )', content)
        return [p for p in parts if p.strip()]

    def _critique_section(self, section: str) -> Dict[str, Any]:
        """
        Critic: evaluate a section and return structured feedback.

        Returns JSON with score (0-10) and specific issues.
        """
        # Truncate very long sections for the critic
        if len(section) > 3000:
            section_for_review = section[:3000] + "\n...(内容已截断)"
        else:
            section_for_review = section

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
            # Parse JSON from response
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return {"score": 7.0}  # Default: assume OK if parsing fails
        except Exception as e:
            self.log(f"Critic调用失败: {e}", "WARNING")
            return {"score": 7.0}  # Assume OK on failure

    def _revise_section(self, section: str, critique: Dict[str, Any]) -> str:
        """
        Revise a section based on critic feedback.
        """
        issues = critique.get("issues", [])
        suggestions = critique.get("suggestions", [])

        prompt = f"""你是一位资深科技编辑，请根据审稿意见修订以下章节。

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
```

**Step 2: Register in `src/agents/__init__.py`**

```python
from src.agents.self_refine_agent import SelfRefineAgent

# In AGENT_REGISTRY:
"self_refine_agent": SelfRefineAgent,
```

**Step 3: Add to SeriesOrchestrator pipeline**

In `_init_agents`:
```python
from src.agents.self_refine_agent import SelfRefineAgent

# Add after coherence_pass_agent:
if agents_config.get("self_refine_agent", {}).get("enabled", True):
    try:
        agents["self_refine_agent"] = SelfRefineAgent(
            config=full_config,
            prompts=self.prompts
        )
        logger.info("Initialized agent: self_refine_agent")
    except Exception as e:
        logger.warning(f"Failed to initialize self_refine_agent: {e}")
```

In `_execute_workflow`, add after coherence pass:
```python
# ========== 阶段3.7：自审自改 ==========
if "self_refine_agent" in self.agents:
    logger.info("===== 阶段3.7：自审自改（Self-Refine）=====")
    state = _call_agent_safely("self_refine_agent", state)
```

**Step 4: Add config entry in `config/config.yaml`**

```yaml
  # 自审自改Agent（新增）
  self_refine_agent:
    enabled: true
    max_iterations: 2
    min_score: 7.0
```

**Step 5: Commit**

```bash
git add src/agents/self_refine_agent.py src/agents/__init__.py src/series_orchestrator.py config/config.yaml
git commit -m "feat: add SelfRefineAgent with actor-critic pattern for section-level quality"
```

---

## Task 4: Create TechnicalDeAIAgent

**Why:** Existing De-AI skill targets social media (adds particles, colloquialisms). Technical long-form needs different treatment: pattern detection, sentence variety, and specificity enforcement.

**Files:**
- Create: `src/agents/technical_deai_agent.py`
- Modify: `src/agents/__init__.py` (register)
- Modify: `src/series_orchestrator.py` (add stage 4)

**Step 1: Create `src/agents/technical_deai_agent.py`**

```python
"""
Technical De-AI Agent - Remove AI patterns from technical long-form articles.

Unlike social media De-AI (which adds colloquialisms), this agent:
1. Detects 30+ common AI pattern phrases
2. Checks sentence length variance (AI text has uniform lengths)
3. Measures paragraph uniformity (AI writes perfectly parallel paragraphs)
4. Enforces specificity (every claim needs data/name/date)
5. Restructures AI-typical endings ("综上所述" -> forward-looking statement)

Pipeline:
  Regex scan -> Statistical analysis -> LLM rewrite of flagged sections
"""

import re
from typing import Dict, Any, List, Tuple
from src.agents.base import BaseAgent


# AI pattern phrases to detect and replace
AI_PATTERNS = {
    # Chinese AI cliches
    "值得注意的是": "但关键在于",
    "综上所述": "",
    "深入探讨": "拆解",
    "在当今的": "在",
    "在当今": "在",
    "毫无疑问": "",
    "众所周知": "",
    "不可或缺": "关键",
    "发挥着重要作用": "至关重要",
    "具有重要意义": "很重要",
    "日益增长": "不断增长",
    "蓬勃发展": "快速发展",
    "方兴未艾": "快速发展",
    "如火如荼": "大规模推进",
    "引发广泛关注": "受到开发者关注",
    "掀起了热潮": "被大量采用",
    "赋能": "帮助",
    "助力": "帮助",
    "深度赋能": "帮助",
    "一站式": "一体化",
    "全方位": "多维度",
    "多维度": "多个方面",
    "全链路": "端到端",
    "闭环": "完整流程",
    "底层逻辑": "核心原理",
    "抓手": "切入点",
    "组合拳": "方法",
    "矩阵": "体系",
    "生态体系": "生态",
    "赛道": "领域",
    "头部": "领先",
    "玩家": "参与者",
    "护城河": "竞争优势",
    "降本增效": "减少成本、提高效率",
    "方法论": "方法",
    "落地": "实施",
    "对齐": "统一",
    "拉齐": "同步",
    "颗粒度": "精度",
    "心路历程": "过程",
}


class TechnicalDeAIAgent(BaseAgent):
    """Technical De-AI agent for long-form articles."""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        deai_config = config.get("agents", {}).get("technical_deai_agent", {})
        self.max_ai_patterns = deai_config.get("max_ai_patterns", 5)
        self.min_sentence_variance = deai_config.get("min_sentence_variance", 8.0)

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute technical De-AI processing.

        Args:
            state: Workflow state with longform_article.

        Returns:
            Updated state with de-AI'd article.
        """
        self.log("开始技术长文去AI化处理...")

        article = state.get("longform_article", {})
        content = article.get("full_content", "")

        if not content:
            self.log("未找到文章内容，跳过去AI化", "WARNING")
            return state

        # Phase 1: Regex-based pattern detection and replacement
        content, pattern_report = self._replace_ai_patterns(content)

        # Phase 2: Statistical analysis
        stats_report = self._analyze_statistics(content)

        # Phase 3: LLM-based rewrite of flagged sections (if needed)
        if stats_report.get("needs_llm_rewrite", False):
            content = self._llm_rewrite(content, pattern_report, stats_report)

        # Update article
        article["full_content"] = content
        article["word_count"] = len(content)

        self.log(f"去AI化完成: 发现 {pattern_report['total_found']} 个AI模式, "
                 f"替换 {pattern_report['replaced']} 个")

        return {
            **state,
            "longform_article": article,
            "deai_report": {
                "patterns": pattern_report,
                "statistics": stats_report
            },
            "current_step": "technical_deai_completed"
        }

    def _replace_ai_patterns(self, content: str) -> Tuple[str, Dict[str, Any]]:
        """Phase 1: Find and replace AI pattern phrases."""
        found_patterns = []
        replaced_count = 0

        for pattern, replacement in AI_PATTERNS.items():
            count = content.count(pattern)
            if count > 0:
                found_patterns.append({
                    "pattern": pattern,
                    "count": count,
                    "replacement": replacement
                })
                if replacement:  # Only replace if we have a replacement
                    content = content.replace(pattern, replacement)
                    replaced_count += count
                elif not replacement:  # Remove filler words
                    content = content.replace(pattern, "")
                    replaced_count += count

        # Clean up double spaces left by removals
        content = re.sub(r'  +', ' ', content)
        content = re.sub(r'\n\n\n+', '\n\n', content)

        report = {
            "total_found": sum(p["count"] for p in found_patterns),
            "replaced": replaced_count,
            "details": found_patterns[:20]  # Top 20
        }

        return content, report

    def _analyze_statistics(self, content: str) -> Dict[str, Any]:
        """Phase 2: Statistical analysis of sentence/paragraph patterns."""
        # Remove code blocks for analysis
        text_only = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        text_only = re.sub(r'#{1,6}\s+.*\n', '', text_only)

        # Sentence analysis
        sentences = re.split(r'[。！？\n]', text_only)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 5]

        if not sentences:
            return {"needs_llm_rewrite": False, "sentence_variance": 0}

        lengths = [len(s) for s in sentences]
        avg_length = sum(lengths) / len(lengths)
        variance = (sum((l - avg_length) ** 2 for l in lengths) / len(lengths)) ** 0.5

        # Paragraph analysis
        paragraphs = [p.strip() for p in text_only.split('\n\n') if p.strip() and len(p.strip()) > 20]
        if paragraphs:
            para_lengths = [len(p) for p in paragraphs]
            para_avg = sum(para_lengths) / len(para_lengths)
            # Check if >60% of paragraphs follow same pattern (similar length)
            similar_count = sum(1 for l in para_lengths if abs(l - para_avg) < para_avg * 0.3)
            para_uniformity = similar_count / len(paragraphs)
        else:
            para_uniformity = 0

        needs_rewrite = (
            variance < self.min_sentence_variance or
            para_uniformity > 0.6
        )

        return {
            "sentence_variance": round(variance, 2),
            "avg_sentence_length": round(avg_length, 2),
            "total_sentences": len(sentences),
            "paragraph_uniformity": round(para_uniformity, 2),
            "needs_llm_rewrite": needs_rewrite,
            "issues": []
        }

    def _llm_rewrite(self, content: str, pattern_report: Dict[str, Any],
                     stats_report: Dict[str, Any]) -> str:
        """Phase 3: LLM-based rewrite for flagged issues."""
        issues = []

        if stats_report.get("sentence_variance", 0) < self.min_sentence_variance:
            issues.append(f"- 句子长度方差过低({stats_report['sentence_variance']})，句式过于均匀。"
                         "请混合使用短句（10-20字）和长句（40-60字），增加节奏变化。")

        if stats_report.get("paragraph_uniformity", 0) > 0.6:
            issues.append("- 段落结构过于统一。请适当调整段落长度，偶尔使用一句段或设问段。")

        if pattern_report.get("total_found", 0) > 10:
            issues.append(f"- 仍有 {pattern_report['total_found']} 处AI模式表达，需要更自然的表述。")

        if not issues:
            return content

        # Truncate for LLM if needed
        if len(content) > 15000:
            content_for_llm = content[:15000]
            tail = content[15000:]
        else:
            content_for_llm = content
            tail = ""

        prompt = f"""你是一位资深科技编辑，请对以下技术文章进行去AI化润色。

**发现的问题**：
{chr(10).join(issues)}

**润色要求**：
1. 混合使用不同长度的句子：有些5-10字的短句，有些30-50字的长句
2. 段落长度要有变化：偶尔用1-2句的短段落打破节奏
3. 替换所有"值得注意的是"、"综上所述"、"深入探讨"等AI套话
4. 在适当位置加入设问句或反问句
5. 保持技术准确性，不要改变技术描述
6. 保持Markdown格式不变

**文章**：
{content_for_llm}

请输出润色后的完整文章："""

        try:
            response = self._call_llm(prompt)
            improved = response.strip()
            if len(improved) < len(content_for_llm) * 0.7:
                self.log("去AI化结果过短，保留原文", "WARNING")
                return content
            return improved + tail
        except Exception as e:
            self.log(f"LLM去AI化失败: {e}，使用regex替换结果", "WARNING")
            return content
```

**Step 2: Register in `src/agents/__init__.py`**

```python
from src.agents.technical_deai_agent import TechnicalDeAIAgent

# In AGENT_REGISTRY:
"technical_deai_agent": TechnicalDeAIAgent,
```

**Step 3: Add to SeriesOrchestrator pipeline**

In `_init_agents`:
```python
from src.agents.technical_deai_agent import TechnicalDeAIAgent

if agents_config.get("technical_deai_agent", {}).get("enabled", True):
    try:
        agents["technical_deai_agent"] = TechnicalDeAIAgent(
            config=full_config,
            prompts=self.prompts
        )
        logger.info("Initialized agent: technical_deai_agent")
    except Exception as e:
        logger.warning(f"Failed to initialize technical_deai_agent: {e}")
```

In `_execute_workflow`, after self-refine:
```python
# ========== 阶段4：技术长文去AI化 ==========
if "technical_deai_agent" in self.agents:
    logger.info("===== 阶段4：技术长文去AI化（De-AI）=====")
    state = _call_agent_safely("technical_deai_agent", state)
```

**Step 4: Add config entry in `config/config.yaml`**

```yaml
  # 技术长文去AI化Agent（新增）
  technical_deai_agent:
    enabled: true
    max_ai_patterns: 5
    min_sentence_variance: 8.0
```

**Step 5: Commit**

```bash
git add src/agents/technical_deai_agent.py src/agents/__init__.py src/series_orchestrator.py config/config.yaml
git commit -m "feat: add TechnicalDeAIAgent for long-form article naturalization"
```

---

## Task 5: Create QualityGateAgent with Targeted Revision

**Why:** Quality scores exist but aren't enforced. A quality gate after all processing ensures only articles meeting the threshold are saved. Below-threshold articles get targeted revision instead of full regeneration.

**Files:**
- Create: `src/agents/quality_gate_agent.py`
- Modify: `src/agents/__init__.py` (register)
- Modify: `src/series_orchestrator.py` (add stage 5, update save logic)

**Step 1: Create `src/agents/quality_gate_agent.py`**

```python
"""
Quality Gate Agent - Unified quality scoring with targeted revision.

Replaces the disconnected QualityEvaluatorAgent and ContentQualityScorer
with a unified framework that:
1. Scores on 6 dimensions (content depth, logical coherence, factual accuracy,
   De-AI score, readability, practical value)
2. If score < threshold, performs TARGETED revision of weakest dimensions
3. Max 2 revision cycles before accepting
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

        # Unified quality dimensions
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
        Execute quality gate: score -> revise if needed -> score again.

        Args:
            state: Workflow state with longform_article.

        Returns:
            Updated state with quality_report and possibly revised article.
        """
        self.log("开始质量门禁检查...")

        article = state.get("longform_article", {})
        content = article.get("full_content", "")

        if not content:
            self.log("未找到文章内容，跳过质量门禁", "WARNING")
            return {**state, "quality_gate_passed": False}

        # Scoring + revision loop
        for cycle in range(self.max_revision_cycles + 1):
            self.log(f"质量评估第 {cycle + 1} 轮...")

            # Score using LLM-as-judge
            scores = self._score_with_llm(content)

            # Calculate weighted total
            total = sum(
                scores.get(dim, 0) * info["weight"]
                for dim, info in self.dimensions.items()
            )
            total = round(total, 1)

            self.log(f"  总分: {total}/{self.min_score}")

            if total >= self.min_score:
                self.log(f"✅ 质量门禁通过（{total}分）")

                report = {
                    "total_score": total,
                    "dimension_scores": scores,
                    "passed": True,
                    "revision_cycles": cycle,
                    "evaluated_at": datetime.now().isoformat()
                }

                return {
                    **state,
                    "quality_gate_report": report,
                    "quality_gate_passed": True
                }

            # Need revision
            self.log(f"⚠️ 质量不达标（{total}<{self.min_score}），进行第 {cycle+1} 轮修订")

            # Find weakest dimensions
            weakest = self._find_weakest(scores, n=2)
            self.log(f"  最弱维度: {weakest}")

            # Targeted revision
            content = self._targeted_revision(content, weakest, scores)
            article["full_content"] = content
            article["word_count"] = len(content)

        # Final attempt failed - save anyway with warning
        self.log(f"⚠️ 质量门禁未通过（{total}分），但保存文章")

        report = {
            "total_score": total,
            "dimension_scores": scores,
            "passed": False,
            "revision_cycles": self.max_revision_cycles,
            "evaluated_at": datetime.now().isoformat(),
            "note": "Quality below threshold after max revisions"
        }

        return {
            **state,
            "longform_article": article,
            "quality_gate_report": report,
            "quality_gate_passed": False
        }

    def _score_with_llm(self, content: str) -> Dict[str, float]:
        """
        Use LLM as judge to score the article on all dimensions.

        Returns dict of dimension -> score (0-100).
        """
        # For long articles, score a representative sample
        if len(content) > 10000:
            # Take first 3000 + middle 3000 + last 3000
            sample = content[:3000] + "\n...(中间部分省略)...\n" + \
                     content[len(content)//2 - 1500:len(content)//2 + 1500] + \
                     "\n...(省略)...\n" + content[-3000:]
        else:
            sample = content

        prompt = f"""你是资深科技编辑，请对以下文章进行多维度质量评分。

**评分维度**（每项0-100分）：
1. **内容深度**（20%）：技术细节是否充分？是否有深度分析？还是停留在表面描述？
2. **逻辑连贯**（20%）：章节之间是否有逻辑递进？过渡是否自然？是否有重复或跳跃？
3. **事实准确性**（20%）：技术描述是否准确？数据是否具体？引用是否可靠？
4. **去AI化程度**（15%）：是否避免了AI套话？语言是否自然？句子长度是否有变化？
5. **可读性**（15%）：段落是否适中？是否有列表/表格？标题是否清晰？
6. **实践价值**（10%）：是否有代码示例？是否有可操作建议？是否有避坑指南？

**文章内容**：
{sample}

请输出JSON格式评分：
{{
  "content_depth": <0-100>,
  "logical_coherence": <0-100>,
  "factual_accuracy": <0-100>,
  "deai_score": <0-100>,
  "readability": <0-100>,
  "practical_value": <0-100>,
  "brief_comment": "<一句话总评>"
}}"""

        try:
            response = self._call_llm(prompt)
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                scores = json.loads(json_match.group())
                # Validate all dimensions present
                for dim in self.dimensions:
                    if dim not in scores:
                        scores[dim] = 70  # Default
                return scores
        except Exception as e:
            self.log(f"LLM评分失败: {e}，使用默认分数", "WARNING")

        # Default scores if LLM fails
        return {dim: 70 for dim in self.dimensions}

    def _find_weakest(self, scores: Dict[str, float], n: int = 2) -> List[str]:
        """Find the n weakest dimensions."""
        sorted_dims = sorted(scores.items(), key=lambda x: x[1])
        return [dim for dim, score in sorted_dims[:n]]

    def _targeted_revision(self, content: str, weak_dims: List[str],
                          scores: Dict[str, float]) -> str:
        """
        Revise only the aspects related to weak dimensions.
        """
        dim_names = [self.dimensions[d]["name"] for d in weak_dims]
        dim_scores = {self.dimensions[d]["name"]: scores.get(d, 0) for d in weak_dims}

        prompt = f"""你是资深科技编辑，请对以下文章进行针对性改进。

**需要改进的维度**：
{chr(10).join(f"- {name}: {score}分" for name, score in dim_scores.items())}

**针对每个弱项的改进策略**：

如果是"内容深度"不足：
- 补充具体的技术实现细节
- 添加性能数据或基准测试结果
- 增加代码示例（如适用）

如果是"逻辑连贯"不足：
- 在章节间添加过渡句
- 消除重复论述
- 确保逻辑递进（背景->原理->实践->展望）

如果是"事实准确性"不足：
- 检查技术描述是否准确
- 补充具体版本号、发布日期
- 添加数据来源

如果是"去AI化程度"不足：
- 替换"值得注意的是"、"综上所述"等AI套话
- 调整句式，混合长短句
- 增加设问句或个人观点

如果是"可读性"不足：
- 拆分过长段落
- 增加列表或表格
- 优化标题层级

如果是"实践价值"不足：
- 添加可操作的步骤指南
- 补充工具推荐
- 增加避坑建议

**重要**：只改进指定维度相关的内容，不要改动其他部分。

**文章**：
{content[:12000]}

请输出改进后的完整文章（保持Markdown格式）："""

        try:
            response = self._call_llm(prompt)
            improved = response.strip()
            if len(improved) < len(content) * 0.6:
                self.log("修订结果过短，保留原文", "WARNING")
                return content
            # Keep the tail if content was truncated
            if len(content) > 12000:
                improved = improved + content[12000:]
            return improved
        except Exception as e:
            self.log(f"目标修订失败: {e}，保留原文", "WARNING")
            return content
```

**Step 2: Register in `src/agents/__init__.py`**

```python
from src.agents.quality_gate_agent import QualityGateAgent

# In AGENT_REGISTRY:
"quality_gate_agent": QualityGateAgent,
```

**Step 3: Add to SeriesOrchestrator pipeline**

In `_init_agents`:
```python
from src.agents.quality_gate_agent import QualityGateAgent

if agents_config.get("quality_gate_agent", {}).get("enabled", True):
    try:
        agents["quality_gate_agent"] = QualityGateAgent(
            config=full_config,
            prompts=self.prompts
        )
        logger.info("Initialized agent: quality_gate_agent")
    except Exception as e:
        logger.warning(f"Failed to initialize quality_gate_agent: {e}")
```

In `_execute_workflow`, after De-AI:
```python
# ========== 阶段5：质量门禁 ==========
if "quality_gate_agent" in self.agents:
    logger.info("===== 阶段5：质量门禁（Quality Gate）=====")
    state = _call_agent_safely("quality_gate_agent", state)
```

Also update the save section to include quality gate info:

```python
# In the save section, update md_content to include quality info:
quality_report = state.get("quality_gate_report", {})
quality_score = quality_report.get("total_score", "N/A")
quality_passed = quality_report.get("passed", False)

md_content = f"""# {article['title']}

{article.get('full_content', '')}

---
**元数据**:
- 字数: {article.get('word_count', 0)}
- 阅读时间: {article.get('reading_time', 'N/A')}
- 标签: {', '.join(article.get('tags', []))}
- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 知识库来源: {'NotebookLM' if state.get('knowledge_base') else 'LLM only'}
- 质量评分: {quality_score}/100 ({'✅ 通过' if quality_passed else '⚠️ 待改进'})
"""
```

**Step 4: Add config entry in `config/config.yaml`**

```yaml
  # 质量门禁Agent（新增）
  quality_gate_agent:
    enabled: true
    min_score: 75
    max_revision_cycles: 2
```

**Step 5: Commit**

```bash
git add src/agents/quality_gate_agent.py src/agents/__init__.py src/series_orchestrator.py config/config.yaml
git commit -m "feat: add QualityGateAgent with targeted revision for quality enforcement"
```

---

## Task 6: End-to-End Integration Test

**Why:** All 5 improvements are integrated into the pipeline. Need to verify the full flow works with a single episode before scaling.

**Files:**
- Modify: `config/config.yaml` (verify all new agent configs are present)

**Step 1: Verify all agents are registered**

Run: `PYTHONPATH=/Users/z/Documents/work/content-forge-ai python -c "from src.agents import AGENT_REGISTRY; print([k for k in AGENT_REGISTRY if k in ['coherence_pass_agent', 'self_refine_agent', 'technical_deai_agent', 'quality_gate_agent']])"`
Expected: `['coherence_pass_agent', 'self_refine_agent', 'technical_deai_agent', 'quality_gate_agent']`

**Step 2: Run a single episode to test the full pipeline**

Run: `PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --episode 1 --series-config config/voice_assistant_topics_40.json`
Expected: Full pipeline runs through all stages without errors

**Step 3: Verify the output contains quality metadata**

Check the generated article file for quality score in metadata section.

**Step 4: Commit any fixes**

```bash
git add -A
git commit -m "fix: integration fixes for writing quality upgrade pipeline"
```

---

## Pipeline Flow Summary (After All Tasks)

```
Before (4 stages):
  DeepResearch → NotebookLM → LongForm(Outline→Sections→Summary) → Save

After (7 stages):
  DeepResearch → NotebookLM → LongForm(Outline→Sections[with summaries]→Summary)
    → CoherencePass (full-article review)
    → SelfRefine (actor-critic section review)
    → TechnicalDeAI (pattern removal + naturalization)
    → QualityGate (score + targeted revision if needed)
    → Save (with quality metadata)
```

## Config Summary

Add to `config/config.yaml` under `agents:`:

```yaml
  coherence_pass_agent:
    enabled: true
    max_review_tokens: 4000

  self_refine_agent:
    enabled: true
    max_iterations: 2
    min_score: 7.0

  technical_deai_agent:
    enabled: true
    max_ai_patterns: 5
    min_sentence_variance: 8.0

  quality_gate_agent:
    enabled: true
    min_score: 75
    max_revision_cycles: 2
```

## File Changes Summary

| File | Action | Description |
|------|--------|-------------|
| `src/agents/longform_generator.py` | Modify | Add section summary tracking + context passing |
| `src/agents/coherence_pass_agent.py` | Create | Full-article coherence review agent |
| `src/agents/self_refine_agent.py` | Create | Actor-critic section refinement agent |
| `src/agents/technical_deai_agent.py` | Create | Technical De-AI processing agent |
| `src/agents/quality_gate_agent.py` | Create | Unified quality scoring + targeted revision |
| `src/agents/__init__.py` | Modify | Register 4 new agents |
| `src/series_orchestrator.py` | Modify | Add 4 new stages to pipeline |
| `config/config.yaml` | Modify | Add config for 4 new agents |
