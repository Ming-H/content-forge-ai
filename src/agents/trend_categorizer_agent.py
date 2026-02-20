"""
热点分类Agent v9.4 - 将按数据源组织的热点按6大分类重新组织

v9.0 更新:
- 5分类 → 6分类重构
- 新增: 🦾 AI Agent 分类
- 实现Top5截取逻辑（宁缺毋滥策略）
- 24小时严格过滤
- 30个数据源分类映射

v9.1 更新:
- 严格24小时时间过滤（时间解析失败或超过24h直接排除）
- 增强时间格式支持（RSS/Atom/HTTP Date等）

v9.2 更新:
- 去除24小时时间限制
- 优先最新数据（按时间戳排序，最新的在前）
- 确保每个分类Top5填满（6×5=30条）
- 只过滤掉没有时间戳的内容

v9.3 更新:
- 新增全局去重逻辑，确保30条新闻内部不重复
- 基于URL和标题相似度去重
- 相似度阈值60%（同一事件的报道视为重复）

v9.4 更新:
- 新增AI相关性过滤，确保30条新闻都与AI相关
- 通用数据源（如Hacker News）改为基于内容关键词分类
- 修复数据源映射冲突问题
"""

from typing import Dict, Any, List
from difflib import SequenceMatcher
import re
from src.agents.base import BaseAgent
from src.utils.time_filter import TimeFilter


# v9.4: AI相关性关键词 - 用于判断新闻是否与AI相关
AI_RELEVANCE_KEYWORDS = [
    # 核心AI技术
    "artificial intelligence", "machine learning", "deep learning",
    "neural network", "LLM", "GPT", "ChatGPT", "Claude", "Gemini",
    "Transformer", "NLP", "computer vision", "speech recognition",
    "reinforcement learning", "RLHF", "fine-tuning",

    # AI公司/产品
    "OpenAI", "Anthropic", "DeepMind", "Meta AI", "Microsoft AI",
    "Hugging Face", "Stability AI", "Midjourney", "DALL-E", "Sora",
    "LangChain", "Llama", "Mistral", "Qwen", "GLM", "通义千问", "文心一言",
    "AlphaFold", "AlphaGo", "AlphaCode", "Copilot",

    # AI应用/概念
    "autonomous agent", "RAG", "embedding", "inference",
    "benchmark", "AGI", "alignment", "multimodal", "generative",
    "diffusion model", "vector database", "chatbot", "language model",
    "text generation", "image generation", "AI agent", "AI model",

    # AI中文关键词
    "人工智能", "机器学习", "深度学习", "大模型", "智能体", "自然语言处理",
    "计算机视觉", "强化学习", "神经网络", "推理", "训练", "微调"
]

# 需要精确匹配的AI关键词（使用单词边界）
AI_EXACT_KEYWORDS = ["AI", "RL", "CV", "agent", "model", "token", "prompt"]

# v9.4: 需要基于内容分类的通用数据源（不固定到特定分类）
CONTENT_BASED_SOURCES = {
    "Hacker News", "Reddit", "Product Hunt", "NewsAPI"
}


class TrendCategorizerAgent(BaseAgent):
    """热点分类Agent v9.5 - 按6大分类组织热点，AI相关性过滤，优先最新数据，为NewsScoringAgent提供足够候选"""

    def __init__(self, config: Dict[str, Any], prompts: Dict[str, Any]):
        super().__init__(config, prompts)
        # 获取配置
        agent_config = config.get("agents", {}).get("trend_categorizer", {})
        self.max_per_category = agent_config.get("max_per_category", 10)  # v12.1: 每个分类10条候选
        self.final_per_category = agent_config.get("final_per_category", 5)  # 最终每个分类5条
        self.similarity_threshold = agent_config.get("similarity_threshold", 0.6)  # 相似度阈值60%

    def _is_ai_relevant(self, item: Dict[str, Any]) -> bool:
        """
        v9.4: 判断新闻是否与AI相关

        基于标题和描述中的AI关键词判断相关性
        使用精确匹配检测短关键词（如AI），子字符串匹配长关键词
        """
        title = item.get("title", "")
        description = item.get("description", "")
        text = f"{title} {description}"

        # 检查需要精确匹配的关键词（使用单词边界）
        text_lower = text.lower()
        for keyword in AI_EXACT_KEYWORDS:
            # 使用正则表达式进行单词边界匹配
            pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
            if re.search(pattern, text_lower):
                return True

        # 检查普通关键词（子字符串匹配）
        for keyword in AI_RELEVANCE_KEYWORDS:
            if keyword.lower() in text_lower:
                return True

        return False

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行热点分类 (v9.4: 6分类 + AI相关性过滤 + 优先最新 + Top5截取 + 全局去重)

        Args:
            state: 包含 trends_by_source 的状态

        Returns:
            Dict[str, Any]: 更新后的状态，包含 categorized_trends
        """
        self.log("开始按6大分类组织热点 (v9.4: AI相关性过滤，全局去重，优先最新)...")

        try:
            trends_by_source = state.get("trends_by_source", {})
            if not trends_by_source:
                self.log("未找到 trends_by_source，跳过分类")
                return state

            # ========== v9.0: 6大分类定义 ==========
            categories = {
                "📚 学术前沿": {
                    "icon": "📚",
                    "keywords": [
                        "paper", "research", "study", "arxiv", "publication", "publish",
                        "university", "institute", "lab", "professor", "scientist", "researcher",
                        "conference", "journal", "peer-reviewed", "dataset", "breakthrough",
                        "novel", "state-of-the-art", "sota", "semantic scholar", "openalex",
                        "papers with code", "openreview", "dblp", "citation", "theorem",
                        "algorithm", "machine learning", "deep learning", "neural network"
                    ],
                    "items": []
                },
                "🛠️ 开发工具": {
                    "icon": "🛠️",
                    "keywords": [
                        "library", "framework", "package", "sdk", "api", "tool",
                        "hugging face", "model", "dataset", "pypi", "npm", "github release",
                        "python", "javascript", "typescript", "langchain", "pytorch",
                        "tensorflow", "keras", "scikit-learn", "pandas", "numpy"
                    ],
                    "items": []
                },
                "🦾 AI Agent": {
                    "icon": "🦾",
                    "keywords": [
                        "agent", "autonomous", "multi-agent", "autogpt", "babyagi", "agentgpt",
                        "copilot", "assistant", "chatbot", "langchain agent", "ai agent",
                        "autonomous agent", "workflow", "task", "planning", "reasoning",
                        "tool use", "function calling", "openai function", "claude agent"
                    ],
                    "items": []
                },
                "💼 企业应用": {
                    "icon": "💼",
                    "keywords": [
                        "enterprise", "b2b", "business", "solution", "deployment",
                        "implementation", "integration", "workflow", "automation",
                        "industry", "sector", "startup", "funding", "investment",
                        "acquisition", "merger", "partnership", "collaboration"
                    ],
                    "items": []
                },
                "🌐 消费产品": {
                    "icon": "🌐",
                    "keywords": [
                        "product", "app", "service", "launch", "release", "update",
                        "consumer", "user", "mobile", "web", "desktop", "extension",
                        "plugin", "saas", "platform", "tool", "application",
                        "product hunt", "show hn", "startup", "app store", "google play"
                    ],
                    "items": []
                },
                "📰 行业资讯": {
                    "icon": "📰",
                    "keywords": [
                        "news", "report", "analysis", "trend", "forecast", "prediction",
                        "industry", "market", "regulation", "policy", "law", "ethics",
                        "safety", "alignment", "interpretability", "governance",
                        "mit technology review", "stanford hai", "accenture"
                    ],
                    "items": []
                }
            }

            # ========== v9.4: 数据源到分类的映射（30个数据源） ==========
            # 注意: Hacker News, Reddit, Product Hunt, NewsAPI 等通用数据源不固定分类
            # 它们会基于内容关键词自动分类
            source_category_map = {
                # 学术前沿
                "arXiv": "📚 学术前沿",
                "Semantic Scholar": "📚 学术前沿",
                "OpenAlex": "📚 学术前沿",
                "Papers with Code": "📚 学术前沿",
                "OpenReview": "📚 学术前沿",
                "DBLP": "📚 学术前沿",

                # 开发工具
                "Hugging Face": "🛠️ 开发工具",
                "PyPI": "🛠️ 开发工具",
                "npm": "🛠️ 开发工具",
                "GitHub Releases": "🛠️ 开发工具",
                "PyTorch": "🛠️ 开发工具",
                "TensorFlow": "🛠️ 开发工具",

                # AI Agent (专用AI Agent数据源)
                "GitHub Trending": "🦾 AI Agent",

                # 企业应用
                "TechCrunch AI": "💼 企业应用",
                "VentureBeat AI": "💼 企业应用",
                "AI Business": "💼 企业应用",
                "InfoQ AI": "💼 企业应用",

                # 消费产品
                "a16z": "🌐 消费产品",
                "App Store": "🌐 消费产品",
                "Google Play": "🌐 消费产品",

                # 行业资讯
                "MIT Tech Review": "📰 行业资讯",
                "The Gradient": "📰 行业资讯",
                "MarkTechPost": "📰 行业资讯",
                "Stanford HAI": "📰 行业资讯",
                "Accenture": "📰 行业资讯",

                # v9.4: 通用数据源 - 不固定分类，基于内容自动分类
                # Hacker News, Reddit, Product Hunt, NewsAPI 将基于关键词匹配
            }

            total_items = 0
            non_ai_count = 0

            # ========== v9.4: 第一步 - 收集所有新闻并格式化 + AI相关性过滤 ==========
            all_formatted_items = []
            for source_name, trends in trends_by_source.items():
                if not trends:
                    continue
                for trend in trends:
                    formatted_item = self._format_trend_item(trend, source_name)
                    # 记录原始数据源，用于后续分类
                    formatted_item["_source_name"] = source_name

                    # v9.4: AI相关性过滤 - 通用数据源必须检查AI相关性
                    if source_name in CONTENT_BASED_SOURCES:
                        if not self._is_ai_relevant(formatted_item):
                            non_ai_count += 1
                            continue  # 跳过非AI相关内容

                    all_formatted_items.append(formatted_item)
                    total_items += 1

            self.log(f"收集到 {total_items} 条AI相关新闻 (过滤掉 {non_ai_count} 条非AI内容)")

            # ========== v9.3: 第二步 - 全局去重 ==========
            unique_items = self._deduplicate_all_items(all_formatted_items)
            self.log(f"全局去重: {total_items}条 → {len(unique_items)}条 (移除{total_items - len(unique_items)}条重复)")

            # ========== v9.3: 第三步 - 分类去重后的新闻 ==========
            for item in unique_items:
                source_name = item.pop("_source_name", "")
                # 获取该数据源的默认分类
                default_category = source_category_map.get(source_name)

                # 确定分类
                category = self._determine_category(
                    item,
                    default_category,
                    categories
                )

                # 添加到对应分类
                categories[category]["items"].append(item)

            # ========== v9.5: 优先最新数据 + 保留更多候选（每分类10条） ==========
            # NewsScoringAgent 将从中选出 5条编辑精选 + 30条分类热点 = 35条
            categorized_trends = {}
            total_candidates = 0
            total_no_timestamp = 0

            for cat_name, cat_data in categories.items():
                items = cat_data["items"]

                # ========== 第一步: 只过滤掉没有时间戳的内容 ==========
                valid_items = []
                no_ts_count = 0

                for item in items:
                    timestamp = item.get("timestamp", "")
                    if not timestamp:
                        # v9.2: 没有时间戳的直接过滤掉（无法排序）
                        no_ts_count += 1
                        continue
                    # v9.2: 所有的有时间的都保留，不限制24小时
                    valid_items.append(item)

                if no_ts_count > 0:
                    self.log(f"  {cat_name}: 过滤掉{no_ts_count}条无时间戳内容")

                # ========== 第二步: 按时间戳排序（最新的在前）+ 热度作为次要排序 ==========
                sorted_items = sorted(
                    valid_items,
                    key=lambda x: (x.get("timestamp", ""), x.get("heat_score", 0)),
                    reverse=True
                )

                # ========== v9.5: 截取更多候选（每分类10条）供 NewsScoringAgent 选择 ==========
                # NewsScoringAgent 将从中选出 5条编辑精选 + 30条分类热点
                top_items = sorted_items[:self.max_per_category]

                categorized_trends[cat_name] = {
                    "icon": cat_data["icon"],
                    "items": top_items,
                    "count": len(top_items)
                }
                total_candidates += len(top_items)
                total_no_timestamp += no_ts_count

            self.log(f"分类完成(优先最新): 原始{total_items}条 -> 无时间戳{total_no_timestamp}条 -> 保留{total_candidates}条候选")

            # 统计每个分类的数量
            for cat_name, cat_data in categorized_trends.items():
                if cat_data["count"] > 0:
                    self.log(f"  {cat_name}: {cat_data['count']}条")

            return {
                **state,
                "categorized_trends": categorized_trends,
                "total_trends_count": total_candidates,
                "current_step": "trend_categorized"
            }

        except Exception as e:
            self.log(f"分类失败: {e}", "ERROR")
            return {
                **state,
                "error_message": f"分类失败: {e}",
                "current_step": "trend_categorizer_failed"
            }

    def _format_trend_item(self, trend: Dict[str, Any], source_name: str) -> Dict[str, Any]:
        """格式化热点条目，添加来源链接等信息"""
        title = trend.get("title", "")
        description = trend.get("description", "")
        url = trend.get("url", "")
        source = trend.get("source", source_name)
        heat_score = trend.get("heat_score", 0)
        tags = trend.get("tags", [])
        timestamp = trend.get("timestamp", "")

        # 提取数据源名称（去掉括号内容）
        if "NewsAPI" in source:
            # 格式: "NewsAPI (TechCrunch)" -> "NewsAPI"
            clean_source = "NewsAPI"
        elif "GitHub" in source:
            clean_source = "GitHub"
        else:
            clean_source = source

        return {
            "title": title,
            "description": description,
            "url": url,
            "source": clean_source,
            "full_source": source,  # 保留完整来源信息
            "heat_score": heat_score,
            "tags": tags,
            "timestamp": timestamp
        }

    def _determine_category(
        self,
        item: Dict[str, Any],
        default_category: str,
        categories: Dict[str, Dict]
    ) -> str:
        """
        确定热点条目的分类 (v9.0: 6分类系统)

        优先级:
        1. 基于数据源的默认分类
        2. 基于关键词匹配
        3. 兜底分类 (行业资讯)
        """
        title = item.get("title", "").lower()
        description = item.get("description", "").lower()
        text = f"{title} {description}"

        # 如果有默认分类且该分类不是None，优先使用
        if default_category and default_category in categories:
            return default_category

        # 基于关键词计算每个分类的匹配度
        category_scores = {}
        for cat_name, cat_data in categories.items():
            keywords = cat_data["keywords"]
            score = sum(1 for kw in keywords if kw.lower() in text)
            category_scores[cat_name] = score

        # 选择得分最高的分类
        if category_scores:
            best_category = max(category_scores, key=category_scores.get)
            if category_scores[best_category] > 0:
                return best_category

        # v9.0: 兜底分类 - 行业资讯（最通用）
        return "📰 行业资讯"

    def _deduplicate_all_items(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        全局去重 - 基于URL和标题相似度 (v9.3新增)

        去重策略:
        1. URL完全相同 → 必然重复
        2. 标题相似度 > 60% → 视为同一事件的报道

        Args:
            items: 所有格式化后的新闻条目

        Returns:
            去重后的新闻列表
        """
        if not items:
            return []

        unique_items = []
        seen_urls = set()
        seen_titles = []  # 保存已见过的标题，用于相似度比较

        # 按热度排序，优先保留高分新闻
        sorted_items = sorted(items, key=lambda x: x.get("heat_score", 0), reverse=True)

        for item in sorted_items:
            url = item.get("url", "")
            title = item.get("title", "")

            # 1. URL去重（最准确）
            if url and url in seen_urls:
                continue

            # 2. 标题相似度去重
            is_duplicate = False
            title_lower = title.lower()

            for seen_title in seen_titles:
                # 计算标题相似度
                similarity = SequenceMatcher(None, title_lower, seen_title.lower()).ratio()
                if similarity >= self.similarity_threshold:
                    is_duplicate = True
                    break

            if is_duplicate:
                continue

            # 通过去重检查，添加到结果
            unique_items.append(item)
            if url:
                seen_urls.add(url)
            seen_titles.append(title)

        return unique_items
