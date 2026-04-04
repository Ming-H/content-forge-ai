# 调研报告

本次调研发现，Agent CI/CD 正在经历从'手工作坊'向'现代软件工程'的范式跃迁。将 Prompt 视为代码并通过 Git 进行版本控制已成为行业共识（以微软 Promptflow 和 LangSmith 为代表）。为解决大模型的非确定性问题，开发者必须依赖基于'黄金测试集'的自动化回归测试和 LLM-as-a-Judge 机制。在部署阶段，结合 Feature Flag 的蓝绿发布和 A/B 测试是规避 Agent 幻觉和行为漂移风险的关键防线。未来，由 AI 自主编译和测试提示词（如 DSPy 框架）将成为 Agentic CI/CD 的前沿爆发点。