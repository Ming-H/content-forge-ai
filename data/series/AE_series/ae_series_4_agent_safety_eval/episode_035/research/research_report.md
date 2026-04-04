# 调研报告

本次调研深入剖析了当前大模型智能体安全防护的三大主流实战方案：NVIDIA NeMo Guardrails（擅长通过 Colang 控制复杂对话流边界）、Guardrails AI（基于 Pydantic 实现输入输出结构化验证与修复）以及 OpenAI Agents SDK 内置的 Input/Output/Tool 拦截机制。调研发现，面对日益复杂的越狱攻击和幻觉问题，企业级客服智能体需采用多层洋葱防御架构。尽管组合不同框架的防护栏能极大提升安全性，但开发者必须关注多重拦截带来的系统延迟，并建议在未来探索并行处理和 LLM-as-a-Judge 等前沿自治防护策略。