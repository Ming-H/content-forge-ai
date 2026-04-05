"""
TechnicalDeAIAgent - 技术文章去AI化处理 Agent

3阶段流水线: regex scan -> statistical analysis -> LLM rewrite

与社交媒体去AI化不同，技术文章需要:
- 保持技术准确性，不改变技术描述
- 保持 Markdown 格式
- 保持文章结构不变，不添加新章节
- 每个论点需要有数据/名称/日期支撑
- 自然表达，避免AI套话

Phase 1: regex scan - 40+ AI pattern detection and replacement
Phase 2: statistical analysis - sentence length variance, paragraph uniformity
Phase 3: LLM rewrite - targeted rewrite of flagged sections only
"""

import re
import math
import statistics
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass, field

from src.agents.base import BaseAgent


# ============================================================================
# AI Pattern Constants - 40+ patterns for detection and replacement
# ============================================================================

AI_PATTERNS = {
    # --- 开头套话 ---
    "在当今的": "",
    "在当今": "",
    "随着.*?的发展": "",
    "随着.*?不断": "",
    "在.*?领域中": "",
    "在.*?领域中，": "",
    "作为.*?领域": "",

    # --- 连接词套话 ---
    "值得注意的是": "需要关注的是",
    "综上所述": "总的来说",
    "总而言之": "总的来说",
    "众所周知": "大家知道",
    "毋庸置疑": "毫无疑问",
    "毋庸置疑地": "",
    "毋庸置疑的": "",
    "不言而喻": "显然",
    "显而易见": "显然",
    "由此可见": "可以看出",
    "毋庸置疑的是": "",
    "需要指出的是": "需要说明的是",

    # --- 强调套话 ---
    "深入探讨": "详细分析",
    "深入剖析": "详细分析",
    "深入理解": "理解",
    "深入浅出": "",
    "全方位": "",
    "多维度": "多个角度",
    "从.*?角度来看": "",
    "从.*?层面": "",

    # --- 比较套话 ---
    "二者各有优劣": "各有利弊",
    "各有千秋": "各有利弊",
    "各有特色": "各有利弊",
    "各有侧重": "侧重点不同",

    # --- 总结套话 ---
    "通过以上分析": "根据分析",
    "通过上述分析": "根据分析",
    "通过.*?的分析": "根据分析",
    "希望本文能够": "",
    "希望能为": "",
    "本文将从": "下面从",
    "本文详细": "下面详细",

    # --- 过度修饰 ---
    "极大地": "显著地",
    "深刻地": "深入地",
    "充分地": "",
    "有效地": "",
    "高效地": "",
    "精准地": "精确地",
    "全面地": "",
    "系统地": "",

    # --- 空洞表达 ---
    "发挥着.*?的作用": "起到关键作用",
    "具有.*?的意义": "有重要意义",
    "提供了.*?的支撑": "提供了支撑",
    "具有重要的.*?价值": "有重要价值",
    "产生了.*?的影响": "产生了影响",
    "提供了.*?的可能": "使之成为可能",
    "带来了.*?的机遇": "带来了机遇",
    "面临.*?的挑战": "面临挑战",

    # --- 被动句式（AI偏好） ---
    "被广泛.*?于": "广泛用于",
    "被广泛应用于": "广泛用于",
    "被越来越多": "越来越多地",
    "被认为是": "是",
    "被称为": "叫做",

    # --- 冗余表达 ---
    "事实上，": "",
    "实际上，": "",
    "本质上，": "",
    "简而言之，": "",
    "换言之，": "",
    "换句话说，": "",
    "具体来说，": "",
    "详细来说，": "",
    "总体而言，": "",
    "整体而言，": "",
    "在一定程度上": "",

    # --- AI特有的过度结构化标记 ---
    "首先.*?其次.*?最后": "",  # 整体模式，不直接替换
    "一方面.*?另一方面": "",   # 整体模式，不直接替换
}

# Patterns that should be removed entirely (not replaced)
REMOVE_ONLY_PATTERNS = [
    r"在当今的?",
    r"在当今",
    r"随着[^。，,；]{2,15}的发展[，,]?",
    r"随着[^。，,；]{2,15}不断[^。，,；]{2,10}[，,]?",
    r"在[^。，,；]{2,15}领域中[，,]?",
    r"作为[^。，,；]{2,15}领域",
    r"事实上[，,]?",
    r"实际上[，,]?",
    r"本质上[，,]?",
    r"简而言之[，,]?",
    r"换言之[，,]?",
    r"换句话说[，,]?",
    r"具体来说[，,]?",
    r"详细来说[，,]?",
    r"总体而言[，,]?",
    r"整体而言[，,]?",
    r"在一定程度上[，,]?",
    r"毋庸置疑[地的是]*[，,]?",
    r"毋庸置疑地[，,]?",
]

# Simple word-level replacements (exact match)
WORD_REPLACEMENTS = {
    "值得注意的是": "需要关注的是",
    "综上所述": "总的来说",
    "总而言之": "总的来说",
    "众所周知": "大家知道",
    "不言而喻": "显然",
    "显而易见": "显然",
    "由此可见": "可以看出",
    "需要指出的是": "需要说明的是",
    "深入探讨": "详细分析",
    "深入剖析": "详细分析",
    "深入理解": "理解",
    "二者各有优劣": "各有利弊",
    "各有千秋": "各有利弊",
    "通过以上分析": "根据分析",
    "通过上述分析": "根据分析",
    "多维度": "多个角度",
    "极大地": "显著地",
    "深刻地": "深入地",
    "被广泛应用于": "广泛用于",
    "被认为是": "是",
    "被称为": "叫做",
    "被越来越多": "越来越多地",
    "发挥着重要的作用": "起到关键作用",
    "具有重要的参考价值": "有重要参考价值",
    "希望本文能够": "",
    "希望能为": "",
    "本文将从": "下面从",
    "本文详细": "下面详细",
}

# Patterns that indicate AI-generated content (for scoring)
AI_INDICATOR_PATTERNS = [
    r"在当今的?",
    r"随着[^。，,；]{2,15}的发展",
    r"值得注意的是",
    r"综上所述",
    r"总而言之",
    r"众所周知",
    r"毋庸置疑",
    r"不言而喻",
    r"显而易见",
    r"由此可见",
    r"需要指出的是",
    r"深入探讨",
    r"深入剖析",
    r"从[^。，,；]{2,10}角度来看",
    r"从[^。，,；]{2,10}层面",
    r"二者各有优劣",
    r"各有千秋",
    r"通过以上分析",
    r"通过上述分析",
    r"希望本文能够",
    r"本文将从",
    r"本文详细",
    r"事实上[，,]?",
    r"实际上[，,]?",
    r"本质上[，,]?",
    r"简而言之[，,]?",
    r"换言之[，,]?",
    r"具体来说[，,]?",
    r"总体而言[，,]?",
    r"整体而言[，,]?",
    r"在一定程度上",
    r"多维度",
    r"全方位",
    r"发挥着[^。，,；]{2,15}的作用",
    r"具有[^。，,；]{2,15}的意义",
    r"提供了[^。，,；]{2,15}的支撑",
    r"具有[^。，,；]{2,15}的价值",
    r"产生了[^。，,；]{2,15}的影响",
    r"带来了[^。，,；]{2,15}的机遇",
    r"面临[^。，,；]{2,15}的挑战",
    r"被广泛应用于",
    r"被认为是",
    r"极大地",
    r"深刻地",
    r"充分地",
    r"有效地",
    r"高效地",
    r"精准地",
    r"全面地",
    r"系统地",
    r"首先[^。，,；]{2,30}其次[^。，,；]{2,30}最后",
    r"一方面[^。，,；]{2,30}另一方面",
]


@dataclass
class DeAIStats:
    """去AI化统计报告"""
    ai_pattern_count: int = 0
    patterns_found: List[str] = field(default_factory=list)
    patterns_replaced: int = 0
    patterns_removed: int = 0
    sentence_variance: float = 0.0
    paragraph_uniformity: float = 0.0
    avg_sentence_length: float = 0.0
    total_sentences: int = 0
    total_paragraphs: int = 0
    needs_llm_rewrite: bool = False
    llm_rewrite_applied: bool = False
    issues: List[str] = field(default_factory=list)


class TechnicalDeAIAgent(BaseAgent):
    """
    技术文章去AI化处理 Agent

    3阶段流水线:
    1. regex scan - 检测和替换AI模式
    2. statistical analysis - 句子长度方差、段落均匀度分析
    3. LLM rewrite - 对有问题的部分进行定向LLM重写

    配置项:
        max_ai_patterns: int (default 5) - 超过此数量的AI模式触发LLM重写
        min_sentence_variance: float (default 8.0) - 最小句子长度方差
        max_paragraph_uniformity: float (default 0.6) - 最大段落均匀度
    """

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)

        deai_config = config.get("agents", {}).get("technical_deai_agent", {})
        self.max_ai_patterns = deai_config.get("max_ai_patterns", 5)
        self.min_sentence_variance = deai_config.get("min_sentence_variance", 8.0)
        self.max_paragraph_uniformity = deai_config.get("max_paragraph_uniformity", 0.6)

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行去AI化处理

        Args:
            state: 包含 longform_article 的状态

        Returns:
            更新后的状态，包含去AI化后的文章和统计报告
        """
        self.log("开始技术文章去AI化处理（3阶段流水线）...")

        article = state.get("longform_article", {})
        if isinstance(article, str):
            content = article
        elif isinstance(article, dict):
            content = article.get("full_content", "")
        else:
            self.log("未找到文章内容，跳过去AI化", "WARNING")
            return state

        if not content:
            self.log("文章内容为空，跳过去AI化", "WARNING")
            return state

        self.log(f"原文长度: {len(content)} 字符")

        # ========== Phase 1: Regex Scan ==========
        content, regex_stats = self._phase_regex_scan(content)
        self.log(f"Phase 1 (Regex Scan): 发现 {regex_stats['ai_pattern_count']} 个AI模式, "
                 f"替换 {regex_stats['patterns_replaced']} 个, "
                 f"移除 {regex_stats['patterns_removed']} 个")

        # ========== Phase 2: Statistical Analysis ==========
        stats = self._phase_statistical_analysis(content)
        self.log(f"Phase 2 (Statistical Analysis): "
                 f"句子方差={stats.sentence_variance:.1f} (阈值>={self.min_sentence_variance}), "
                 f"段落均匀度={stats.paragraph_uniformity:.2f} (阈值<={self.max_paragraph_uniformity}), "
                 f"AI模式={stats.ai_pattern_count} (阈值<={self.max_ai_patterns})")

        # Determine if LLM rewrite is needed
        needs_rewrite = (
            stats.ai_pattern_count > self.max_ai_patterns
            or stats.sentence_variance < self.min_sentence_variance
            or stats.paragraph_uniformity > self.max_paragraph_uniformity
        )
        stats.needs_llm_rewrite = needs_rewrite

        # ========== Phase 3: LLM Rewrite (if needed) ==========
        if needs_rewrite:
            self.log("Phase 3: 启动LLM定向重写...")
            content = self._phase_llm_rewrite(content, stats)
            stats.llm_rewrite_applied = True
            self.log("Phase 3: LLM重写完成")
        else:
            self.log("Phase 3: 文章质量达标，无需LLM重写")

        # Final cleanup
        content = self._final_cleanup(content)

        # Update article
        if isinstance(state.get("longform_article"), dict):
            article["full_content"] = content
            article["word_count"] = len(content)
        else:
            article = {"full_content": content, "word_count": len(content)}

        # Build stats report
        stats_report = {
            "ai_pattern_count": stats.ai_pattern_count,
            "patterns_found": stats.patterns_found[:20],  # limit to 20
            "patterns_replaced": regex_stats["patterns_replaced"],
            "patterns_removed": regex_stats["patterns_removed"],
            "sentence_variance": round(stats.sentence_variance, 2),
            "paragraph_uniformity": round(stats.paragraph_uniformity, 2),
            "avg_sentence_length": round(stats.avg_sentence_length, 1),
            "total_sentences": stats.total_sentences,
            "total_paragraphs": stats.total_paragraphs,
            "needs_llm_rewrite": stats.needs_llm_rewrite,
            "llm_rewrite_applied": stats.llm_rewrite_applied,
            "issues": stats.issues,
        }

        self.log(f"去AI化完成: AI模式={stats.ai_pattern_count}, "
                 f"需要LLM重写={needs_rewrite}, 实际重写={stats.llm_rewrite_applied}")

        return {
            **state,
            "longform_article": article,
            "deai_stats": stats_report,
            "deai_applied": True,
            "current_step": "technical_deai_completed",
        }

    # ========================================================================
    # Phase 1: Regex Scan
    # ========================================================================

    def _phase_regex_scan(self, content: str) -> Tuple[str, Dict[str, Any]]:
        """
        Phase 1: Regex-based AI pattern detection and replacement.

        Uses both simple word replacements and regex removal patterns.
        """
        original_content = content

        # Step 1: Simple word-level replacements (exact match)
        replacements_made = 0
        for old, new in WORD_REPLACEMENTS.items():
            count = content.count(old)
            if count > 0:
                content = content.replace(old, new)
                replacements_made += count

        # Step 2: Regex-based removal patterns
        removals_made = 0
        for pattern in REMOVE_ONLY_PATTERNS:
            matches = re.findall(pattern, content)
            removals_made += len(matches)
            content = re.sub(pattern, "", content)

        # Step 3: Clean up double spaces and artifacts from removals
        content = self._clean_whitespace(content)

        stats = {
            "ai_pattern_count": self._count_ai_patterns(original_content),
            "patterns_replaced": replacements_made,
            "patterns_removed": removals_made,
        }

        return content, stats

    def _replace_ai_patterns(self, content: str) -> str:
        """
        Strict pattern matching and replacement using AI_PATTERNS dict.

        For patterns with replacement text, substitute; for empty replacements,
        remove the pattern entirely.
        """
        for pattern, replacement in AI_PATTERNS.items():
            if not pattern:
                continue
            try:
                content = re.sub(pattern, replacement, content)
            except re.error:
                # Skip invalid regex patterns
                continue

        content = self._clean_whitespace(content)
        return content

    def _count_ai_patterns(self, content: str) -> int:
        """Count how many AI indicator patterns are found in the content."""
        count = 0
        for pattern in AI_INDICATOR_PATTERNS:
            try:
                matches = re.findall(pattern, content)
                count += len(matches)
            except re.error:
                continue
        return count

    def _find_ai_patterns(self, content: str) -> List[str]:
        """Find and return specific AI patterns found in the content."""
        found = []
        for pattern in AI_INDICATOR_PATTERNS:
            try:
                matches = re.findall(pattern, content)
                found.extend(matches)
            except re.error:
                continue
        return found

    def _clean_whitespace(self, content: str) -> str:
        """Clean up whitespace artifacts from pattern removal."""
        # Remove double/triple spaces
        content = re.sub(r" {2,}", " ", content)
        # Remove spaces before Chinese punctuation
        content = re.sub(r" ([，。；：！？、）】」])", r"\1", content)
        # Remove leading spaces on lines (but preserve code block indentation)
        lines = content.split("\n")
        cleaned = []
        in_code_block = False
        for line in lines:
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                cleaned.append(line)
                continue
            if not in_code_block and line.strip():
                # Only strip leading/trailing spaces for non-code, non-empty lines
                stripped = line.strip()
                # Preserve markdown list indentation
                if stripped.startswith(("- ", "* ", "+ ", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
                    cleaned.append(line.rstrip())
                else:
                    cleaned.append(stripped)
            else:
                cleaned.append(line)
        content = "\n".join(cleaned)
        # Collapse multiple blank lines to max 2
        content = re.sub(r"\n{3,}", "\n\n", content)
        return content

    # ========================================================================
    # Phase 2: Statistical Analysis
    # ========================================================================

    def _phase_statistical_analysis(self, content: str) -> DeAIStats:
        """
        Phase 2: Statistical analysis of sentence length variance,
        paragraph uniformity, and remaining AI patterns.
        """
        stats = DeAIStats()

        # Count AI patterns after regex cleanup
        stats.ai_pattern_count = self._count_ai_patterns(content)
        stats.patterns_found = self._find_ai_patterns(content)

        # Extract plain text (remove markdown syntax for analysis)
        plain_text = self._extract_plain_text(content)

        # Sentence analysis
        sentences = self._split_sentences(plain_text)
        stats.total_sentences = len(sentences)

        if sentences:
            sentence_lengths = [len(s) for s in sentences if len(s) > 0]
            if sentence_lengths:
                stats.avg_sentence_length = statistics.mean(sentence_lengths)
                if len(sentence_lengths) >= 2:
                    stats.sentence_variance = statistics.variance(sentence_lengths)
                else:
                    stats.sentence_variance = 0.0

        # Paragraph analysis
        paragraphs = self._split_paragraphs(content)
        stats.total_paragraphs = len(paragraphs)

        if len(paragraphs) >= 2:
            paragraph_lengths = [len(p) for p in paragraphs if len(p) > 0]
            if paragraph_lengths:
                mean_len = statistics.mean(paragraph_lengths)
                if mean_len > 0:
                    # Coefficient of variation (lower = more uniform = more AI-like)
                    if len(paragraph_lengths) >= 2:
                        std_len = statistics.stdev(paragraph_lengths)
                        stats.paragraph_uniformity = 1.0 - min(1.0, std_len / mean_len)
                    else:
                        stats.paragraph_uniformity = 1.0

        # Build issues list
        if stats.ai_pattern_count > self.max_ai_patterns:
            stats.issues.append(
                f"AI模式过多: 发现 {stats.ai_pattern_count} 个 (阈值 {self.max_ai_patterns})"
            )
        if stats.sentence_variance < self.min_sentence_variance:
            stats.issues.append(
                f"句子长度方差过低: {stats.sentence_variance:.1f} (阈值 >={self.min_sentence_variance}), "
                f"句子长度过于均匀，缺乏自然变化"
            )
        if stats.paragraph_uniformity > self.max_paragraph_uniformity:
            stats.issues.append(
                f"段落均匀度过高: {stats.paragraph_uniformity:.2f} (阈值 <={self.max_paragraph_uniformity}), "
                f"段落结构过于整齐，需要增加变化"
            )

        return stats

    def _extract_plain_text(self, content: str) -> str:
        """Extract plain text from markdown content for analysis."""
        # Remove code blocks
        text = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        # Remove inline code
        text = re.sub(r"`[^`]+`", "", text)
        # Remove markdown links (keep text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        # Remove images
        text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", "", text)
        # Remove headers markers
        text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
        # Remove bold/italic markers
        text = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text)
        # Remove horizontal rules
        text = re.sub(r"^---+$", "", text, flags=re.MULTILINE)
        # Remove list markers
        text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
        text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
        return text.strip()

    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences (Chinese-aware)."""
        # Split on Chinese and English sentence endings
        sentences = re.split(r"[。！？；\n]+", text)
        # Filter empty and very short sentences
        return [s.strip() for s in sentences if len(s.strip()) > 2]

    def _split_paragraphs(self, content: str) -> List[str]:
        """Split content into paragraphs (non-empty blocks separated by blank lines)."""
        # Split on double newlines
        paragraphs = re.split(r"\n\s*\n", content)
        # Filter out code blocks, headers, and very short fragments
        result = []
        for p in paragraphs:
            p = p.strip()
            if not p:
                continue
            # Skip pure headers
            if re.match(r"^#{1,6}\s+", p):
                continue
            # Skip code blocks
            if p.startswith("```"):
                continue
            # Skip very short fragments (likely metadata or separators)
            if len(p) < 20:
                continue
            result.append(p)
        return result

    # ========================================================================
    # Phase 3: LLM Rewrite (targeted sections only)
    # ========================================================================

    def _phase_llm_rewrite(self, content: str, stats: DeAIStats) -> str:
        """
        Phase 3: LLM-based rewrite of flagged sections.

        For long articles (>15000 chars), processes in chunks:
        - head (first 12000 chars) -> LLM rewrite
        - tail (remaining) -> appended as-is

        For shorter articles, processes the whole thing.
        """
        issues_text = "\n".join(f"- {issue}" for issue in stats.issues)

        if len(content) <= 15000:
            return self._llm_rewrite_full(content, issues_text)
        else:
            return self._llm_rewrite_chunked(content, issues_text)

    def _llm_rewrite_full(self, content: str, issues_text: str) -> str:
        """LLM rewrite for articles <= 15000 chars."""
        prompt = f"""你是一位资深科技编辑，请对以下技术文章进行去AI化润色。

**检测到的问题**：
{issues_text}

**改进策略**：
- 如果"AI模式过多"：将"综上所述"、"值得注意的是"、"在当今"等AI套话替换为更自然的表达
- 如果"句子方差过低"：交替使用长短句，有些句子20-30字，有些50-80字，增加节奏感
- 如果"段落均匀度过高"：调整段落长度，有的段落3-4句，有的段落1-2句，打破AI生成的均匀节奏

**严格要求**：
1. 只修改有问题的部分，保留原有优质内容，不要改动正确的技术描述
2. 不要改变文章结构和章节标题
3. 不要添加新的章节
4. 保持Markdown格式
5. 保持技术准确性，不改变技术描述中的术语、数据和代码
6. 结尾如果只是简单复述前面内容，改为前瞻性建议或行动号召
7. 使用自然表达，避免AI套话
8. 每个论点尽量有数据、名称或日期支撑

**原文**：
{content}

请输出修改后的完整文章（保持Markdown格式）："""

        try:
            response = self._call_llm(prompt)
            improved = response.strip()

            # Validate: reject if too short (content loss)
            if len(improved) < len(content) * 0.6:
                self.log(
                    f"去AI化结果过短 ({len(improved)} vs {len(content)}), "
                    f"可能丢失内容，保留原文",
                    "WARNING"
                )
                return content

            return improved

        except Exception as e:
            self.log(f"LLM去AI化失败: {e}", "WARNING")
            return content

    def _llm_rewrite_chunked(self, content: str, issues_text: str) -> str:
        """LLM rewrite for long articles (>15000 chars), processing in chunks."""
        head = content[:12000]
        tail = content[12000:]

        prompt = f"""你是一位资深科技编辑，请对以下技术文章的前半部分进行去AI化润色。

**检测到的问题**：
{issues_text}

**改进策略**：
- 如果"AI模式过多"：将"综上所述"、"值得注意的是"、"在当今"等AI套话替换为更自然的表达
- 如果"句子方差过低"：交替使用长短句，增加自然节奏感
- 如果"段落均匀度过高"：调整段落长度，打破均匀节奏

**严格要求**：
1. 只修改有问题的部分，保留原有优质内容
2. 不要改变文章结构和章节标题
3. 不要添加新的章节
4. 保持Markdown格式
5. 保持技术准确性
6. 使用自然表达

**原文（前半部分）**：
{head}

请输出修改后的完整前半部分（保持Markdown格式）："""

        try:
            response = self._call_llm(prompt)
            improved_head = response.strip()

            # Validate
            if len(improved_head) < len(head) * 0.6:
                self.log("前半部分去AI化结果过短，保留原文", "WARNING")
                return content

            return improved_head + tail

        except Exception as e:
            self.log(f"LLM去AI化失败: {e}", "WARNING")
            return content

    # ========================================================================
    # Final Cleanup
    # ========================================================================

    def _final_cleanup(self, content: str) -> str:
        """
        Final cleanup pass: remove any remaining double spaces and artifacts.
        """
        # Remove double spaces
        cleanup = content.split("  ")
        content = " ".join(cleanup)

        # Remove trailing whitespace on lines
        lines = content.split("\n")
        in_code = False
        cleaned_lines = []
        for line in lines:
            if line.strip().startswith("```"):
                in_code = not in_code
            if not in_code:
                line = line.rstrip()
            cleaned_lines.append(line)

        content = "\n".join(cleaned_lines)

        # Collapse multiple blank lines
        content = re.sub(r"\n{3,}", "\n\n", content)

        # Remove leading/trailing whitespace
        content = content.strip()

        return content
