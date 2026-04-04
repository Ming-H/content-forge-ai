# 调研报告

本次调研系统梳理了多模式研究助手背后的核心技术。当前业界已明确将工作流划分为 Prompt Chaining（线性低延迟）、ReAct（动态推理）和 Orchestrator-Workers（复杂规划）。实战证明，脱离重度框架，利用 OpenAI/Anthropic 原生 Function Calling API 纯 Python 手搓 Agent Loop，不仅能避开黑盒问题，还能精准控制多模式间的路由与状态切换，是通向高级 AI 工程师的必经之路。