# 调研报告

本次针对 AutoGen/AG2 多智能体模式的调研显示，框架正经历从微软主导的「ConversableAgent + GroupChatManager」经典群聊模式，向社区驱动、基于事件驱动与 Handoff 的 Swarm 模式演进。虽然 Auto 和 RoundRobin 编排在原型阶段极快，但 Swarm 和 Nested Chat 因其动态状态交接和任务解耦能力，正成为 2025 年企业级多智能体落地的最佳实践。开发者在享受多智能体涌现能力的同时，需重点关注 AG2 v1.0 架构升级带来的 API 变动，以及 Token 消耗优化等工程痛点。