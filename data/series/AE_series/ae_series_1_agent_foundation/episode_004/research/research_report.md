# 调研报告

本次调研深入解析了 Function Calling 连接大模型与外部世界的核心机制，梳理了 OpenAI 与 Anthropic 在 JSON Schema 定义、并行调用 及 tool_choice 控制上的技术差异。通过结合开源框架、主流云服务、开发者实战反馈及最新学术前沿，揭示了构建生产级 Agent 的关键路径：即通过严谨的 JSON Schema 设计、结构化输出生成以及闭环的错误处理/自我纠正策略，解决 LLM 在意图路由与 API 调用中的幻觉与不稳定性痛点。