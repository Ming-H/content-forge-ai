"""
Daily 模式约束回归测试：
1. NewsScoringAgent 输出 5条编辑精选 + 30条分类热点，且互不重复
2. WorldClassDigestAgentV9 头部统计与实际条目一致
"""

import os
import sys
import unittest
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents.news_scoring_agent import NewsScoringAgent
from src.agents.world_class_digest_agent_v8 import WorldClassDigestAgentV9


def build_item(category: str, index: int) -> dict:
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "title": f"{category} 新闻 {index}",
        "description": f"{category} 相关描述 {index}",
        "url": f"https://example.com/{category}/{index}",
        "source": "TechCrunch AI",
        "heat_score": 100 - index,
        "timestamp": timestamp,
    }


class TestDailyDigestConstraints(unittest.TestCase):
    def setUp(self):
        self.config = {
            "agents": {
                "news_scoring": {
                    "max_items": 35,
                    "category_items": 30,
                    "min_per_category": 5,
                    "max_per_category": 5,
                    "editors_pick_count": 5,
                },
                "world_class_digest": {
                    "translate_enabled": False,
                    "batch_size": 5,
                },
            },
            "llm": {"provider": "zhipuai"},
        }
        self.prompts = {}

    def _build_categorized_trends(self) -> dict:
        categories = [
            ("📚 学术前沿", "📚"),
            ("🛠️ 开发工具", "🛠️"),
            ("🦾 AI Agent", "🦾"),
            ("💼 企业应用", "💼"),
            ("🌐 消费产品", "🌐"),
            ("📰 行业资讯", "📰"),
        ]
        return {
            cat: {
                "icon": icon,
                # 每个分类提供10条候选，确保剔除编辑精选后仍能补齐30条
                "items": [build_item(cat, i) for i in range(10)],
                "count": 10,
            }
            for cat, icon in categories
        }

    def test_news_scoring_must_output_35_unique_items(self):
        agent = NewsScoringAgent(self.config, self.prompts)
        state = {"categorized_trends": self._build_categorized_trends()}
        result = agent.execute(state)

        editors_pick = result.get("editors_pick", [])
        scored_trends = result.get("scored_trends", {})
        category_items = [item for cat in scored_trends.values() for item in cat.get("items", [])]

        self.assertEqual(len(editors_pick), 5)
        self.assertEqual(len(category_items), 30)

        all_urls = [item.get("url", "") for item in editors_pick + category_items]
        self.assertEqual(len(set(all_urls)), 35)

    def test_digest_header_counts_should_follow_actual_items(self):
        digest_agent = WorldClassDigestAgentV9(self.config, self.prompts)
        digest_agent.llm = None

        # 故意制造 count 字段不一致，验证会按 items 长度重算
        scored_trends = self._build_categorized_trends()
        for cat_data in scored_trends.values():
            cat_data["items"] = cat_data["items"][:5]
            cat_data["count"] = 0

        editors_pick = [build_item("editors", i) for i in range(5)]

        digest = digest_agent._generate_world_class_digest_v9(
            scored_trends=scored_trends,
            editors_pick=editors_pick,
            source_status={},
        )

        metadata = digest.get("metadata", {})
        markdown_content = digest.get("markdown_content", "")

        self.assertEqual(metadata.get("total_items"), 35)
        self.assertIn("**精选**: 35条（5条编辑精选 + 30条分类热点）", markdown_content)


if __name__ == "__main__":
    unittest.main()
