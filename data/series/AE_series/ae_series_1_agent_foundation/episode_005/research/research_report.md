# 调研报告

本次调研围绕Anthropic提出的Agent-Computer Interface (ACI) 设计理念展开。调研发现，业界正经历从“优化提示词”到“优化工具接口”的范式转移。通过引入Poka-yoke防错机制（如强制绝对路径、精简报错信息）、优化API的JSON Schema描述，开发者能大幅降低Agent的幻觉和试错成本。前沿基准（如SWE-bench）及学术论文证明，构建对LLM友好的周边工具生态已成为提升Agent任务成功率最关键的抓手。