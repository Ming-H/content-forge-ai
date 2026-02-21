#!/usr/bin/env python3
"""
验证 Daily 简报是否满足发布约束：
1. 5条编辑精选 + 30条分类热点 = 35条
2. 35条新闻全局不重复（按 URL，回退标题）
3. metadata 与 markdown 头部统计一致
4. markdown 关键区块存在（编辑精选、分类热点）
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


HEADER_PATTERN = re.compile(r"\*\*精选\*\*:\s*(\d+)条（(\d+)条编辑精选 \+ (\d+)条分类热点）")


def normalize_title(title: str) -> str:
    if not title:
        return ""
    title = title.lower().strip()
    title = re.sub(r"\s+", " ", title)
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", title)


def build_item_key(item: Dict) -> str:
    url = (item.get("url", "") or "").strip().lower()
    if url:
        return f"url::{url}"

    title = item.get("title_cn") or item.get("title") or ""
    normalized_title = normalize_title(title)
    if normalized_title:
        return f"title::{normalized_title}"

    source = (item.get("source", "") or "").strip().lower()
    published_at = (item.get("published_at") or item.get("timestamp") or "").strip().lower()
    return f"fallback::{source}::{published_at}"


def find_latest_digest() -> Path:
    candidates = sorted(Path("data/daily").glob("*/digest/digest_*.json"))
    if not candidates:
        raise FileNotFoundError("未找到任何 digest JSON 文件")
    return candidates[-1]


def validate_digest_file(
    digest_path: Path,
    expected_editors_pick: int = 5,
    expected_category_items: int = 30
) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    with digest_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    editors_pick = data.get("editors_pick", [])
    categories = data.get("categories", [])
    category_items = [item for category in categories for item in category.get("items", [])]

    expected_total = expected_editors_pick + expected_category_items
    actual_total = len(editors_pick) + len(category_items)

    # 1) 条数校验
    if len(editors_pick) != expected_editors_pick:
        errors.append(f"编辑精选数量错误: 期望{expected_editors_pick}，实际{len(editors_pick)}")
    if len(category_items) != expected_category_items:
        errors.append(f"分类热点数量错误: 期望{expected_category_items}，实际{len(category_items)}")
    if actual_total != expected_total:
        errors.append(f"总条数错误: 期望{expected_total}，实际{actual_total}")

    # 2) 元数据校验
    metadata = data.get("metadata", {})
    metadata_total = metadata.get("total_items")
    if metadata_total != expected_total:
        errors.append(f"metadata.total_items错误: 期望{expected_total}，实际{metadata_total}")

    # 3) markdown 头部与关键区块校验
    markdown_content = data.get("markdown_content", "") or ""
    if "## ⭐ 编辑精选 (Editor's Picks)" not in markdown_content:
        errors.append("Markdown缺少“编辑精选”区块")
    if "## 🔍 分类热点" not in markdown_content:
        errors.append("Markdown缺少“分类热点”区块")

    header_match = HEADER_PATTERN.search(markdown_content)
    if not header_match:
        errors.append("Markdown头部未找到“精选: X条（Y条编辑精选 + Z条分类热点）”统计行")
    else:
        header_total = int(header_match.group(1))
        header_editors = int(header_match.group(2))
        header_category = int(header_match.group(3))

        if header_total != expected_total:
            errors.append(f"Markdown头部总数错误: 期望{expected_total}，实际{header_total}")
        if header_editors != expected_editors_pick:
            errors.append(
                f"Markdown头部编辑精选数量错误: 期望{expected_editors_pick}，实际{header_editors}"
            )
        if header_category != expected_category_items:
            errors.append(
                f"Markdown头部分类型热点数量错误: 期望{expected_category_items}，实际{header_category}"
            )

    # 4) 去重校验（编辑精选+分类热点）
    all_items = editors_pick + category_items
    seen_keys = {}
    duplicate_samples = []

    for idx, item in enumerate(all_items, start=1):
        key = build_item_key(item)
        if key in seen_keys:
            duplicate_samples.append((seen_keys[key], idx, item.get("title_cn") or item.get("title", "")))
        else:
            seen_keys[key] = idx

    if duplicate_samples:
        errors.append(f"检测到重复新闻: {len(duplicate_samples)} 处")
        for first_idx, second_idx, title in duplicate_samples[:5]:
            warnings.append(f"重复样例 #{first_idx} 与 #{second_idx}: {title}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="验证 Daily 简报产物质量")
    parser.add_argument(
        "--file",
        type=str,
        default="",
        help="digest json 文件路径（默认自动选择最新）"
    )
    parser.add_argument("--editors-pick", type=int, default=5, help="编辑精选期望条数")
    parser.add_argument("--category-items", type=int, default=30, help="分类热点期望条数")
    args = parser.parse_args()

    digest_path = Path(args.file) if args.file else find_latest_digest()

    if not digest_path.exists():
        print(f"❌ 文件不存在: {digest_path}")
        return 1

    errors, warnings = validate_digest_file(
        digest_path,
        expected_editors_pick=args.editors_pick,
        expected_category_items=args.category_items
    )

    print(f"📄 检查文件: {digest_path}")

    for warning in warnings:
        print(f"⚠️  {warning}")

    if errors:
        print("\n❌ 校验失败:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("✅ 校验通过: 条数、去重、统计文案、关键区块均符合预期")
    return 0


if __name__ == "__main__":
    sys.exit(main())
