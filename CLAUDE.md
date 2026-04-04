# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**IMPORTANT**: Always run commands with PYTHONPATH set to the project root directory.

## Essential Commands

```bash
export PYTHONPATH=/Users/z/Documents/work/content-forge-ai

# Auto Mode - daily Chinese AI news digest
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode auto --once

# Series Mode - multi-series blog generation
# LLM series (default config)
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --progress
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --episode 1
# ML series
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --episode 1 --series-config config/ml_topics_100_complete.json
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --all --start 1 --end 10 --series-config config/ml_topics_100_complete.json
# Voice Assistant series
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --episode 1 --series-config config/voice_assistant_topics_40.json
# Agent Engineering series
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --episode 1 --series-config config/agent_engineering_topics_50.json
PYTHONPATH=/Users/z/Documents/work/content-forge-ai python src/main.py --mode series --progress --series-config config/agent_engineering_topics_50.json

# Batch ML generation (3 parallel processes)
./batch_generate_ml_series.sh

# Tests
cd test && PYTHONPATH=/Users/z/Documents/work/content-forge-ai python test_ai_trends.py --source hackernews
cd test && PYTHONPATH=/Users/z/Documents/work/content-forge-ai python test_storage.py
cd test && PYTHONPATH=/Users/z/Documents/work/content-forge-ai python test_digest.py
cd test && PYTHONPATH=/Users/z/Documents/work/content-forge-ai python test_v9_categorization.py
cd test && PYTHONPATH=/Users/z/Documents/work/content-forge-ai python test_daily_digest_constraints.py
cd test && PYTHONPATH=/Users/z/Documents/work/content-forge-ai python test_data_sources.py
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env - ZHIPUAI_API_KEY and TAVILY_API_KEY are required
# Optional: NEWSAPI_KEY, OPENAI_API_KEY, GEMINI_API_KEY, NEWSDATA_IO_API_KEY, REDDIT_*, STABILITY_API_KEY
```

## Architecture: Two-Mode System

```
src/main.py (--mode auto|series)
    |
    +-> AutoContentOrchestrator (src/auto_orchestrator.py)
    |   +-> LangGraph StateGraph workflow (dynamic agent chain)
    |
    +-> SeriesOrchestrator (src/series_orchestrator.py)
        +-> 4-stage: DeepResearch -> NotebookLM -> LongForm -> Save
        +-> Fallback: ResearchAgent (Tavily search)
```

**Only 2 modes exist.** Custom/Refine modes in config.yaml are NOT implemented.

### Auto Mode Workflow

LangGraph DAG built dynamically based on which agents are enabled in config:

```
concurrent_fetch -> time_weight -> trend_categorizer -> news_scoring
  -> auto_fact_check (disabled by default)
  -> content_enhancer (disabled by default)
  -> translation_refiner (disabled by default)
  -> world_class_digest -> END
```

Core agents (always enabled): `concurrent_fetch`, `time_weight`, `trend_categorizer`, `news_scoring`, `world_class_digest`
Quality agents (disabled by default, enable in config.yaml): `auto_fact_check`, `content_enhancer`, `translation_refiner`

State flow: `trends_by_source` -> `time_weighted_trends` -> `categorized_trends` -> `scored_trends` -> `news_digest`

### Series Mode Workflow

**4-stage pipeline** (DeepResearch → NotebookLM → LongForm → Save):
1. **DeepResearchAgent** - 6-dimension multi-source research (facts, open-source, commercial, community, practical, frontier)
2. **NotebookLM** (optional, enabled by default) - knowledge extraction via `nlm` CLI; creates notebook, adds URLs, runs structured queries
3. **ResearchAgent** - fallback web search via Tavily (used when DeepResearchAgent fails)
4. **LongFormGeneratorAgent** - staged generation (outline -> sections -> summary) producing 8000-13000 word articles with retry

The orchestrator tries DeepResearch first, falls back to ResearchAgent if it fails. NotebookLM is optional and skipped if unavailable.

Quality agents (CodeReview, FactCheck, QualityEvaluator, ConsistencyChecker, Visualization, Citation) exist in `src/agents/` but are NOT used in the current series pipeline.

**Available series configs:**
- `config/blog_topics_100_complete.json` - LLM 100-episode series (default)
- `config/ml_topics_100_complete.json` - ML 100-episode series
- `config/voice_assistant_topics_40.json` - Voice Assistant 40-episode series
- `config/agent_engineering_topics_50.json` - Agent Engineering 50-episode series

## Key Files

| File | Purpose |
|------|---------|
| `src/main.py` | CLI entry point (`--mode auto\|series`) |
| `src/auto_orchestrator.py` | LangGraph workflow for auto mode |
| `src/series_orchestrator.py` | Sequential workflow for series mode |
| `src/state.py` | WorkflowState TypedDict, state helpers |
| `src/agents/base.py` | BaseAgent base class with `_call_llm()`, `log()`, `with_retry` |
| `src/agents/__init__.py` | All agent exports + `AGENT_REGISTRY` dict + `get_agent_class()` |
| `src/agents/ai_trend_analyzer_real.py` | 42 data source integrations |
| `src/agents/deep_research_agent.py` | 6-dimension research (facts, open-source, commercial, community, practical, frontier) |
| `src/agents/notebooklm_agent.py` | NotebookLM knowledge extraction via `nlm` CLI |
| `src/data_sources/` | External data source modules (GitHub Trending, HuggingFace, ProductHunt, Reddit, arXiv, etc.) |
| `src/utils/storage_v2.py` | StorageFactory (DailyStorage, SeriesStorage) |
| `src/utils/series_manager.py` | SeriesMetadata, SeriesPathManager, TopicFormatter |
| `src/utils/api_config.py` | Unified API key/endpoint management |
| `src/utils/time_filter.py` | Time-based filtering utilities |
| `src/utils/github_publisher.py` | GitHub content publishing |
| `config/config.yaml` | Main config (LLM, agents, data sources) |
| `config/prompts.yaml` | Agent system prompt templates |
| `config/prompts_longform_v8.yaml` | Longform generation prompts |
| `config/blog_topics_100_complete.json` | LLM 100-episode plan |
| `config/ml_topics_100_complete.json` | ML 100-episode plan |
| `config/voice_assistant_topics_40.json` | Voice Assistant 40-episode plan |
| `config/agent_engineering_topics_50.json` | Agent Engineering 50-episode plan |

## Core Patterns

### Agent Pattern
All agents inherit `BaseAgent` (`src/agents/base.py`), implementing `execute(state: Dict) -> Dict`. Must return complete state using immutable pattern: `{**state, "new_field": value}`. Agents have built-in retry (`with_retry`), metrics collection (`AgentMetrics`), and status tracking (`AgentStatus`).

### Agent Registry
Agents are registered in `src/agents/__init__.py` via `AGENT_REGISTRY` dict. Access by name with `get_agent_class(name)`. Auto mode agents are registered separately from series mode agents.

### State Management
- Auto mode: `trends_by_source` -> `categorized_trends` -> `scored_trends` -> `news_digest`
- Series mode: `current_topic` + `selected_ai_topic` -> `research_data` + `collected_urls` -> `knowledge_base` + `notebooklm_metadata` -> `longform_article`
- Both `current_topic` and `selected_ai_topic` are set by the orchestrator for compatibility
- These state fields are NOT compatible between modes

### Storage
```
data/
├── daily/YYYYMMDD/          # Auto mode
│   ├── raw/                 # Per-source JSON
│   └── digest/              # Markdown + JSON digest
└── series/{series_id}/      # Series mode
    └── episode_{xxx}/longform/  # Article markdown
```

### LLM Configuration
Primary: ZhipuAI `glm-4.7` via `https://open.bigmodel.cn/api/coding/paas/v4/`
Fallback: OpenAI `gpt-4o`
Config in `config/config.yaml` under `llm.provider`.

### Series Path Management
Series use dual identifiers: `series_id` ("series_1") for internal use, `series_path` ("series_1_llm_foundation") for filesystem. Always use `SeriesPathManager` to convert. Category detection: `series_*` -> "LLM_series", `ml_series_*` -> "ML_series", `va_series_*` -> "VA_series".

## Data Sources

42 sources integrated in `RealAITrendAnalyzerAgent` (`src/agents/ai_trend_analyzer_real.py`). Additional modular sources in `src/data_sources/` (GitHub Trending, HuggingFace, ProductHunt, Reddit, Semantic Scholar, Papers With Code, PyPI RSS, NPM Registry, OpenAlex). Key categories:
- **RSS feeds**: TechCrunch, MIT Review, OpenAI, BAIR, Microsoft Research, arXiv, MarkTechPost, KDnuggets, AI Business, The Gradient, InfoQ, Hugging Face, AI News, The Decoder, Wired, VentureBeat, Google AI, DeepMind, Towards Data Science, 量子位, 机器之心
- **APIs**: NewsAPI.org, Hacker News, NewsData.io, Reddit, GitHub Trending
- **Academic**: arXiv CL/CV/LG RSS feeds

Config params in `config/config.yaml`: `max_trends: 20`, `min_heat_score: 60`, `cache_ttl: 3600`

## 6-Category System (Auto Mode)

📚 学术前沿, 🛠️ 开发工具, 🦾 AI Agent, 💼 企业应用, 🌬️ 消费产品, 📰 行业资讯

No 24h restriction - prioritizes by timestamp, Top5 per category, guarantees 30 items daily.

## Deployment

**GitHub Actions** (`.github/workflows/daily-digest.yml`): 3x daily at 06:00, 12:00, 18:00 Beijing Time.
**`run_and_commit.sh`**: Manual deploy script (auto-generate -> commit -> push).
Commit format: `feat: AI内容自动生成 - YYYY-MM-DD`

## Utility Scripts

| Script | Purpose |
|--------|---------|
| `scripts/daily_digest.py` | Standalone daily digest runner |
| `scripts/validate_daily_digest.py` | Validate generated digest files |
| `scripts/content_quality_checker.py` | Content quality analysis |
| `scripts/image_generator.py` | Standalone image generation |
| `scripts/add_references.py` | Add references to existing articles |

## Gotchas

1. **PYTHONPATH required** for all commands - imports will fail without it
2. **ZhipuAI base URL** is `https://open.bigmodel.cn/api/coding/paas/v4/` (coding endpoint, NOT standard API)
3. **`world_class_digest_agent_v8.py`** file name is legacy - it implements v9+ functionality (`WorldClassDigestAgentV9`)
4. **`config.yaml` header says v2.5** but implementation is v11.0 - ignore the header
5. **Series mode uses 4-stage pipeline** - DeepResearch → NotebookLM → LongForm → Save, with ResearchAgent as fallback
6. **v11.0 quality agents disabled by default** - enable `auto_fact_check`, `content_enhancer`, `translation_refiner` in config.yaml to activate
7. **Agent name != state field**: agent `ai_trend_analyzer` outputs `trends_by_source`, not `trending_topics`
8. **DailyStorage** only creates `raw/` and `digest/` subdirectories
9. **Series ID vs path**: use `SeriesPathManager` to convert between "series_1" and "series_1_llm_foundation"
10. **Data sources are split** across `src/agents/ai_trend_analyzer_real.py` (legacy inline) and `src/data_sources/` (newer modular sources)
11. **NotebookLM agent** requires `nlm` CLI tool and has quota limits (50 queries/day, 3-5 per episode); falls back gracefully if unavailable
12. **DeepResearchAgent** collects URLs via search, outputs `research_data` and `collected_urls` for NotebookLM to consume
