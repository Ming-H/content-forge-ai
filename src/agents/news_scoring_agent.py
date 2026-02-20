"""
新闻重要性评分Agent v9.0 - 对分类后的新闻进行重要性评分和筛选

评分维度:
- source_authority: 来源权威度 (30%) - v9.0更新: 30个数据源评分
- engagement: 互动数据 (20%)
- freshness: 时效性 (15%) - v9.0更新: 严格24小时过滤
- category_balance: 分类平衡 (15%) - v9.0更新: 6分类平衡
- content_quality: 内容质量 (10%)
- diversity: 多样性 (10%)

v9.0 更新:
- 6分类系统权威度评分
- 30个数据源完整覆盖
- 严格24小时时效性过滤
- 宁缺毋滥策略
"""

from typing import Dict, Any, List
from datetime import datetime, timedelta
from collections import defaultdict
from src.agents.base import BaseAgent
import re


# v8.0: AI关键词列表 - 用于识别高价值内容
AI_KEYWORDS_HIGH_VALUE = [
    # 核心技术
    "GPT", "LLM", "Transformer", "Agent", "RAG", "Fine-tuning", "LoRA",
    "Multi-agent", "Chain of Thought", "Reasoning", "Embedding",
    # 前沿技术
    "Diffusion", "Stable Diffusion", "Midjourney", "DALL-E", "Sora",
    "Whisper", "CLIP", "GLM", "Qwen", "Llama", "Mistral",
    # 应用领域
    "Code generation", "Copilot", "GitHub Copilot", "ChatGPT",
    "OpenAI", "Anthropic", "Claude", "Gemini", "Hugging Face",
    # 技术概念
    "Prompt engineering", "In-context learning", "Zero-shot", "Few-shot",
    "Temperature", "Token", "Context window", "Inference",
]

# 新兴技术趋势 - 2024-2025
EMERGING_TECH_TRENDS = [
    "AI Agent", "Autonomous agent", "Multi-agent system",
    "Video generation", "Text-to-video", "Sora",
    "Real-time voice", "GPT-4o", "GPT-4o mini",
    "Local LLM", "On-device AI", "Edge AI",
    "Open source model", "Llama 3", "Gemma", "Mixtral",
    "AI safety", "Alignment", "Interpretability",
    "Multimodal", "Vision-language", "VLM",
]

# 数据源权威度评分 (0-100) - v9.0 更新: 30个数据源权威度评分
# 评分标准:
# - 95-100: 顶级官方/学术机构 (OpenAI, Google AI, MIT等)
# - 85-94: 权威学术/研究机构 (Microsoft Research, BAIR, Stanford HAI等)
# - 75-84: 知名学术预印本/数据库 (arXiv, Semantic Scholar, OpenAlex等)
# - 65-74: 顶级科技媒体/社区 (Hacker News, MIT Tech Review等)
# - 55-64: 行业媒体/资讯 (TechCrunch, VentureBeat, NewsAPI等)
# - 45-54: 专业媒体/博客 (MarkTechPost, KDnuggets, The Gradient等)
# - 35-44: 产品平台/社区 (Product Hunt, GitHub, Reddit等)
# - 25-34: 用户生成内容/榜单

SOURCE_AUTHORITY_SCORES = {
    # ========== 📚 学术前沿 (6个) ==========
    "arXiv": 80,                        # 学术预印本 - 最高权威
    "Semantic Scholar": 78,             # 论文元数据库 - 高权威
    "OpenAlex": 75,                     # 开放学术数据库 - 高权威
    "Papers with Code": 72,             # 论文+代码 - 高权威
    "OpenReview": 70,                   # 论文评审平台 - 中高权威
    "DBLP": 68,                         # 计算机科学文献库 - 中高权威

    # ========== 🛠️ 开发工具 (5个) ==========
    "Hugging Face": 60,                 # ML模型平台 - 中高权威
    "PyPI": 55,                         # Python包索引 - 中等权威
    "npm": 50,                          # JavaScript包 - 中等权威
    "GitHub Releases": 58,              # GitHub版本发布 - 中高权威
    "PyTorch": 75,                      # PyTorch官方 - 高权威
    "TensorFlow": 75,                   # TensorFlow官方 - 高权威

    # ========== 🦾 AI Agent (5个) ==========
    "GitHub Trending": 45,              # GitHub热门项目 - 中等权威
    "Product Hunt": 40,                 # 产品发布平台 - 中低权威
    "Reddit": 50,                       # Reddit社区 - 中等权威
    "Hacker News": 70,                  # Hacker News - 高权威
    "Awesome AI Agents": 55,            # 精选列表 - 中等权威

    # ========== 💼 企业应用 (4个) ==========
    "TechCrunch AI": 62,                # TechCrunch AI - 中高权威
    "VentureBeat AI": 58,               # VentureBeat AI - 中等权威
    "AI Business": 52,                  # AI Business - 中等权威
    "InfoQ AI": 55,                     # InfoQ AI - 中等权威

    # ========== 🌐 消费产品 (4个) ==========
    "Product Hunt": 40,                 # Product Hunt - 中低权威
    "a16z": 70,                         # a16z报告 - 高权威
    "Hacker News": 70,                  # Hacker News (Show HN) - 高权威
    "App Store": 45,                    # App Store - 中等权威
    "Google Play": 45,                  # Google Play - 中等权威

    # ========== 📰 行业资讯 (6个) ==========
    "NewsAPI": 55,                      # NewsAPI聚合 - 中等权威
    "MIT Tech Review": 72,              # MIT技术评论 - 高权威
    "The Gradient": 58,                 # The Gradient期刊 - 中高权威
    "MarkTechPost": 52,                 # MarkTechPost - 中等权威
    "Stanford HAI": 80,                 # Stanford HAI报告 - 高权威
    "Accenture": 65,                    # Accenture技术趋势 - 中高权威

    # ========== 其他已有数据源 ==========
    "OpenAI Blog": 95,                  # OpenAI官方 - 顶级权威
    "Anthropic": 95,                    # Anthropic官方 - 顶级权威
    "Google AI": 90,                    # Google AI官方 - 顶级权威
    "Microsoft Research": 85,           # 微软研究院 - 高权威
    "BAIR Blog": 85,                    # Berkeley AI Research - 高权威
    "MIT": 80,                          # MIT - 高权威
    "The Verge AI": 65,                 # The Verge AI - 中高权威
    "KDnuggets": 50,                    # KDnuggets - 中等权威
}


class NewsScoringAgent(BaseAgent):
    """新闻重要性评分Agent - 对新闻进行评分和筛选"""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        self.name = "news_scoring"

        # 获取配置
        agent_config = config.get("agents", {}).get("news_scoring", {})
        self.max_items = agent_config.get("max_items", 35)  # v12.1: 35条（5条编辑精选 + 30条分类热点）
        self.category_items = agent_config.get("category_items", 30)  # 分类热点数量
        self.min_per_category = agent_config.get("min_per_category", 5)  # v12.1: 每个分类至少5条
        self.max_per_category = agent_config.get("max_per_category", 5)  # v12.1: 每个分类最多5条
        self.editors_pick_count = agent_config.get("editors_pick_count", 5)  # 编辑精选数量

        # 评分权重
        weights = agent_config.get("scoring_weights", {})
        self.weight_source = weights.get("source_authority", 30)
        self.weight_engagement = weights.get("engagement", 20)
        self.weight_freshness = weights.get("freshness", 15)
        self.weight_balance = weights.get("category_balance", 15)
        self.weight_quality = weights.get("content_quality", 10)
        self.weight_diversity = weights.get("diversity", 10)

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行新闻评分和筛选

        v12.1: 编辑精选5条 + 分类热点30条 = 35条不重复

        Args:
            state: 包含 categorized_trends 的状态

        Returns:
            Dict[str, Any]: 更新后的状态，包含 scored_trends 和 editors_pick
        """
        self.log("开始对新闻进行重要性评分和筛选...")

        try:
            categorized_trends = state.get("categorized_trends", {})
            if not categorized_trends:
                self.log("未找到 categorized_trends，跳过评分")
                return state

            # 第一步: 为每条新闻计算综合评分
            scored_items = self._score_all_items(categorized_trends)
            self.log(f"完成 {len(scored_items)} 条新闻的评分")

            # v12.1: 第二步 - 先提取编辑精选（Top 5），从所有评分后的新闻中选
            editors_pick = self._extract_editors_pick_from_all(scored_items)
            editors_pick_urls = set(item.get("url", "") for item in editors_pick)
            self.log(f"编辑精选: {len(editors_pick)} 条")

            # v12.1: 第三步 - 从剩余候选中选30条用于分类热点（排除编辑精选）
            remaining_items = [
                item for item in scored_items
                if item.get("url", "") not in editors_pick_urls
            ]
            self.log(f"排除编辑精选后剩余候选: {len(remaining_items)} 条")

            # 第四步：每个分类选5条
            final_selection = self._select_top_items(remaining_items)

            # 第五步: 构建新的分类结构
            scored_trends = self._build_scored_structure(
                final_selection,
                categorized_trends
            )

            # 统计信息
            total_selected = sum(len(cat["items"]) for cat in scored_trends.values())
            total_unique = total_selected + len(editors_pick)
            self.log(f"评分完成: 编辑精选{len(editors_pick)}条 + 分类热点{total_selected}条 = {total_unique}条")

            # 统计每个分类的数量
            for cat_name, cat_data in scored_trends.items():
                if cat_data["count"] > 0:
                    self.log(f"  {cat_name}: {cat_data['count']}条")

            return {
                **state,
                "scored_trends": scored_trends,
                "editors_pick": editors_pick,
                "total_selected_count": total_unique,
                "current_step": "news_scored"
            }

        except Exception as e:
            self.log(f"评分失败: {e}", "ERROR")
            return {
                **state,
                "error_message": f"评分失败: {e}",
                "current_step": "news_scoring_failed"
            }

    def _score_all_items(self, categorized_trends: Dict) -> List[Dict]:
        """为所有新闻项计算综合评分"""
        scored_items = []
        current_time = datetime.now()

        for cat_name, cat_data in categorized_trends.items():
            items = cat_data.get("items", [])
            for item in items:
                # 计算各项得分
                source_score = self._score_source_authority(item)
                engagement_score = self._score_engagement(item)
                freshness_score = self._score_freshness(item, current_time)
                quality_score = self._score_content_quality(item)

                # 综合评分
                total_score = (
                    source_score * self.weight_source / 100 +
                    engagement_score * self.weight_engagement / 100 +
                    freshness_score * self.weight_freshness / 100 +
                    quality_score * self.weight_quality / 100
                )

                scored_item = {
                    **item,
                    "category": cat_name,
                    "importance_score": round(total_score, 2),
                    "score_breakdown": {
                        "source": source_score,
                        "engagement": engagement_score,
                        "freshness": freshness_score,
                        "quality": quality_score
                    }
                }
                scored_items.append(scored_item)

        return scored_items

    def _score_source_authority(self, item: Dict) -> float:
        """根据数据源权威度评分"""
        source = item.get("source", "")
        # 查找最匹配的数据源
        for known_source, score in SOURCE_AUTHORITY_SCORES.items():
            if known_source.lower() in source.lower():
                return float(score)
        return 50.0  # 默认中等分数

    def _score_engagement(self, item: Dict) -> float:
        """根据互动数据评分"""
        heat_score = item.get("heat_score", 0)

        # Hacker News 点数通常在 0-500+
        if heat_score >= 200:
            return 100.0
        elif heat_score >= 100:
            return 85.0
        elif heat_score >= 50:
            return 70.0
        elif heat_score >= 20:
            return 55.0
        elif heat_score >= 10:
            return 40.0
        else:
            # 没有互动数据也给基础分
            return 30.0

    def _score_freshness(self, item: Dict, current_time: datetime) -> float:
        """
        根据时效性评分 (v9.0: 严格24小时过滤)

        宁缺毋滥策略:
        - 24小时内: 70-100分
        - 超过24小时: 0-20分（基本被淘汰）
        """
        timestamp = item.get("timestamp", "")
        if not timestamp:
            return 30.0  # v9.0: 没有时间戳给低分（宁缺毋滥）

        try:
            # 尝试解析时间戳
            if isinstance(timestamp, str):
                # 尝试多种时间格式
                for fmt in ["%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]:
                    try:
                        pub_time = datetime.strptime(timestamp.split("+")[0].strip(), fmt)
                        break
                    except ValueError:
                        continue
                else:
                    return 30.0  # v9.0: 解析失败给低分
            else:
                return 30.0

            # 计算时间差
            time_diff = (current_time - pub_time).total_seconds() / 3600  # 小时

            # v9.0: 严格24小时过滤
            if time_diff <= 6:
                return 100.0
            elif time_diff <= 12:
                return 90.0
            elif time_diff <= 24:
                return 70.0
            elif time_diff <= 36:  # 超过24小时，大幅降分
                return 20.0
            elif time_diff <= 48:
                return 10.0
            else:
                return 5.0  # 超过48小时，基本淘汰

        except Exception:
            return 30.0

    def _score_content_quality(self, item: Dict) -> float:
        """根据内容质量评分（v8.0 - 增强版，包含AI关键词识别）"""
        title = item.get("title", "")
        description = item.get("description", "")

        score = 50.0  # 基础分

        # ========== 基础质量评分 ==========

        # 标题质量
        if len(title) >= 10 and len(title) <= 100:
            score += 15
        elif len(title) >= 5:
            score += 10

        # 描述质量
        if description:
            if len(description) >= 50 and len(description) <= 500:
                score += 20
            elif len(description) >= 20:
                score += 15
            elif len(description) >= 10:
                score += 10
        else:
            score -= 10

        # 标题是否包含数字（通常更具体）
        if any(char.isdigit() for char in title):
            score += 5

        # 标题是否全大写（可能质量较低）
        if title.isupper():
            score -= 10

        # ========== v8.0: AI关键词和技术趋势识别 ==========

        # 合并标题和描述进行关键词检测
        content = f"{title} {description}".lower()

        # 检测高价值AI关键词（每个+3分，最多+15分）
        ai_keyword_count = 0
        for keyword in AI_KEYWORDS_HIGH_VALUE:
            if keyword.lower() in content:
                ai_keyword_count += 1
                if ai_keyword_count >= 5:  # 最多计算5个
                    break
        score += min(15, ai_keyword_count * 3)

        # 检测新兴技术趋势（每个+5分，最多+10分）
        trend_count = 0
        for trend in EMERGING_TECH_TRENDS:
            if trend.lower() in content:
                trend_count += 1
                if trend_count >= 2:  # 最多计算2个
                    break
        score += min(10, trend_count * 5)

        # 检测专业术语（提升质量感）
        technical_terms = ["API", "SDK", "benchmark", "performance", "architecture",
                          "paper", "research", "model", "training", "inference"]
        tech_term_count = sum(1 for term in technical_terms if term.lower() in content)
        score += min(5, tech_term_count * 1)

        return min(100.0, max(0.0, score))

    def _balance_categories(
        self,
        scored_items: List[Dict],
        categorized_trends: Dict
    ) -> List[Dict]:
        """按分类平衡，确保每个分类至少有 min_per_category 条，保留最多 max_per_category 条作为候选"""
        # 按分类分组
        items_by_category = defaultdict(list)
        for item in scored_items:
            cat = item.get("category", "")
            items_by_category[cat].append(item)

        # 为每个分类保留候选（先保留最多 max_per_category 条）
        balanced_items = []

        for cat_name, items in items_by_category.items():
            # 按评分排序
            sorted_items = sorted(items, key=lambda x: x.get("importance_score", 0), reverse=True)

            # 保留最多 max_per_category 条作为候选（而不是只保留 min_per_category）
            max_count = min(len(sorted_items), self.max_per_category)
            balanced_items.extend(sorted_items[:max_count])

        return balanced_items

    def _select_top_items(self, scored_items: List[Dict], exclude_count: int = 0) -> List[Dict]:
        """
        选择评分最高的 N 条新闻，用于分类热点

        v12.1: 选择30条（6分类 × 5条），确保每个分类恰好5条
        """
        # v12.1: 目标是30条分类热点
        target_count = self.category_items  # 30条

        # 按分类分组
        items_by_category = defaultdict(list)
        for item in scored_items:
            cat = item.get("category", "")
            items_by_category[cat].append(item)

        # v12.1: 每个分类恰好选5条（如果有的话）
        selected_items = []
        for cat_name, items in items_by_category.items():
            sorted_items = sorted(items, key=lambda x: x.get("importance_score", 0), reverse=True)
            # 每个分类最多5条
            cat_items = sorted_items[:self.max_per_category]
            selected_items.extend(cat_items)

        return selected_items

    def _build_scored_structure(
        self,
        scored_items: List[Dict],
        original_categories: Dict
    ) -> Dict:
        """构建筛选后的分类结构"""
        # 按分类分组
        items_by_category = defaultdict(list)
        for item in scored_items:
            cat = item.get("category", "")
            items_by_category[cat].append(item)

        # 构建新的分类结构
        scored_trends = {}
        for cat_name, cat_data in original_categories.items():
            items = items_by_category.get(cat_name, [])
            scored_trends[cat_name] = {
                "icon": cat_data.get("icon", ""),
                "items": items,
                "count": len(items)
            }

        return scored_trends

    def _extract_editors_pick_from_all(self, scored_items: List[Dict]) -> List[Dict]:
        """
        v12.1: 从所有候选中提取编辑精选 (Top 5)
        编辑精选独立于分类热点，从全局最高分中选取
        """
        # 按评分排序，选取最高的N条
        sorted_items = sorted(
            scored_items,
            key=lambda x: x.get("importance_score", 0),
            reverse=True
        )[:self.editors_pick_count]

        # 为编辑精选添加序号
        editors_pick = []
        for i, item in enumerate(sorted_items, 1):
            editors_pick.append({
                **item,
                "pick_rank": i,
                "id": f"ep_{i:03d}"
            })

        return editors_pick

    def _extract_editors_pick(self, scored_items: List[Dict]) -> List[Dict]:
        """提取编辑精选 (Top 5) - 保留用于兼容性"""
        top_items = sorted(
            scored_items,
            key=lambda x: x.get("importance_score", 0),
            reverse=True
        )[:5]

        # 为编辑精选添加序号
        editors_pick = []
        for i, item in enumerate(top_items, 1):
            editors_pick.append({
                **item,
                "pick_rank": i,
                "id": f"ep_{i:03d}"
            })

        return editors_pick
