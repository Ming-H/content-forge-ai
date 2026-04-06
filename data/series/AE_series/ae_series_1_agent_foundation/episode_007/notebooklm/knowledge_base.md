# 知识库：Prompt Chaining 与 Routing：可预测的工作流

生成时间: 2026-04-06 13:44
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "「Prompt Chaining（提示链）」与「Routing（路由）」是构建**可预测生成式 AI 工作流**的核心模式，旨在通过**预定义的代码路径**实现 LLM 与工具的编排 [1, 2]。以下是其核心技术架构与关键组件的概述：\n\n### 1. 技术演进路线\n在构建 agentic 系统时，技术演进通常遵循从简单到复杂的阶梯：\n*   **基础构建块 (Augmented LLM)**：通过检索（RAG）、工具（Tools）和存储（Memory）增强的单一 LLM 调用 [3, 4]。\n*   **工作流 (Workflows)**：通过**预定义代码路径**编排 LLM 和工具。**Prompt Chaining** 和 **Routing** 是此阶段的核心模式，提供高度的**可预测性和一致性** [1, 5]。\n*   **自主智能体 (Agents)**：LLM 动态引导自身流程，具有更高灵活性，但牺牲了部分可预测性，且增加了延迟和成本 [1, 6]。\n\n### 2. 主要架构模式\n*   **Prompt Chaining（提示链）架构**：\n    *   **线性编排**：将复杂任务分解为一系列步骤，每个 LLM 调用的输出作为下一个调用的输入 [2]。\n    *   **编程检查点 (Gate)**：在中间步骤加入程序化逻辑（如状态检查或格式验证），确保流程不偏离轨道 [2]。\n    *   **适用场景**：任务可被清晰拆分为固定子任务的情况（如：生成营销文案 $\\rightarrow$ 翻译 $\\rightarrow$ 格式检查） [2, 7]。\n*   **Routing（路由）架构**：\n    *   **分类器层 (Classifier)**：首先对输入进行分类。\n    *   **专业化处理器**：根据分类结果将请求导向专门的下游任务、提示词或工具 [7, 8]。\n    *   **关注点分离**：避免单个提示词因需要处理过多异构输入而导致性能下降 [7]。\n\n### 3. 核心算法与组件名称\n*   **智能提示词路由 (Intelligent Prompt Routing)**：一种自动化服务，根据请求复杂度动态分配模型，以平衡质量与成本 [9]。\n*   **语义路由器 (Semantic Router)**：利用**语义向量空间 (Semantic Vector Space)** 进行决策。它通过 embedding/encoder 模型（如 OpenAI 或 Cohere 编码器）将查询转化为向量，通过余弦相似度等算法快速匹配预定义的路由决策路径（RouteLayer），避免了缓慢的 LLM 文本生成 [10, 11]。\n*   **程序化栅栏 (Programmatic Gates)**：用于 Prompt Chaining 中间的验证逻辑，确保数据一致性 [2]。\n*   **自动化推理检查 (Automated Reasoning checks)**：用于识别模型响应的准确性并减少幻觉 [12]。\n\n### 4. 关键技术指标\n*   **成本优化**：使用智能路由（Intelligent Prompt Routing）可**降低高达 30% 的成本** [9]。\n*   **性能提升**：相比通用模型，经过蒸馏（Distillation）的专业化模型运行速度可提升 **500%**，成本降低 **75%**，且精度损失极小 [9]。\n*   **安全性与准确率**：Bedrock Guardrails 配合自动化推理检查，能以高达 **99% 的准确率** 识别正确的响应，并拦截多达 88% 的有害内容 [12]。\n*   **响应延迟**：语义路由决策层（如 Semantic Router）的决策速度可达 **10ms** 级别，远快于 LLM 的推理生成 [13]。\n*   **权衡指标**：智能体系统通常是以增加**延迟（Latency）**和**成本（Cost）**为代价，来换取更高的**任务表现（Task Performance）** [1]。\n\n综上所述，Prompt Chaining 与 Routing 的核心在于通过**结构化的设计**将非确定性的 LLM 能力转化为**可控的工业化工作流**。",
    "conversation_id": "57d6e6db-2415-4df0-8859-2d371dcde5b7",
    "sources_used": [
      "38eac028-33e1-461a-94fe-bd31488694f8",
      "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "62ec4664-8c3b-4f49-8649-0a7815f98bf1"
    ],
    "citations": {
      "1": "38eac028-33e1-461a-94fe-bd31488694f8",
      "2": "38eac028-33e1-461a-94fe-bd31488694f8",
      "3": "38eac028-33e1-461a-94fe-bd31488694f8",
      "4": "38eac028-33e1-461a-94fe-bd31488694f8",
      "5": "38eac028-33e1-461a-94fe-bd31488694f8",
      "6": "38eac028-33e1-461a-94fe-bd31488694f8",
      "7": "38eac028-33e1-461a-94fe-bd31488694f8",
      "8": "38eac028-33e1-461a-94fe-bd31488694f8",
      "9": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "10": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "11": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "12": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "13": "62ec4664-8c3b-4f49-8649-0a7815f98bf1"
    },
    "references": [
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 1,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 2,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 3,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 4,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 5,
        "cited_text": "In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents. What are agents? \"Agent\" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems , but draw an important architectural distinction between workflows and agents :"
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 6,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 7,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 8,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 9,
        "cited_text": "Learn more about safety and guardrails Optimize for cost, latency, and accuracy Ensure your AI applications are optimized for the perfect balance of cost, speed, and accuracy. Features like Model Distillation, Prompt caching, and Intelligent Prompt Routing can reduce expenses while maintaining performance. For example, distilled models run up to 500% faster and cost up to 75% less, with minimal impact on accuracy. Intelligent Prompt Routing can cut costs by up to 30% while maintaining quality. With flexible options for both real-time and batch processing, Bedrock helps you build smart, efficient, and cost-effective AI systems."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 10,
        "cited_text": "Repository files navigation README Contributing MIT license Semantic Router is a superfast decision-making layer for your LLMs and agents. Rather than waiting for slow LLM generations to make tool-use decisions, we use the magic of semantic vector space to make those decisions — routing our requests using semantic meaning. Read the Docs Quickstart To get started with semantic-router we install it like so: ❗ If wanting to use a fully local version of semantic router you can use HuggingFaceEncoder and LlamaCppLLM ( pip install -qU \"semantic-router[local]\" , see here). To use the HybridRouteLayer you must pip install -qU \"semantic-router[hybrid]\" ."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 11,
        "cited_text": "We begin by defining a set of Route objects. These are the decision paths that the semantic router can decide to use, let's try two simple routes for now — one for talk on politics and another for chitchat : We have our routes ready, now we initialize an embedding / encoder model. We currently support a CohereEncoder and OpenAIEncoder — more encoders will be added soon. To initialize them we do: With our routes and encoder defined we now create a RouteLayer . The route layer handles our semantic decision making."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 12,
        "cited_text": "Securely customize with your data Move from generic AI to AI that knows your customer and your business by customizing models with your data. By combining multiple data customization tools—Knowledge Bases, Bedrock Data Automation, prompt engineering, and fine-tuning—you can optimize your AI applications to your business, while ensuring you're always in control of sensitive information. Learn more about customization Apply security, privacy, and responsible AI checks Amazon Bedrock provides industry-leading security, privacy, and compliance for generative AI applications. Bedrock Guardrails can help block up to 88% of harmful content and identify correct model responses with up to 99% accuracy to minimize hallucinations and data ambiguity using Automated Reasoning checks. Bedrock never stores or uses your data to train models, ensuring complete security and privacy, with encryption of data in transit and at rest, as well as identity-based policies for managing data access. Bedrock provides comprehensive monitoring and logging capabilities that can support your governance and audit requirements. Finally, Bedrock is in scope for common compliance standards including ISO, SOC, CSA STAR Level 2, GDPR, FedRAMP High, and is HIPAA eligible."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 13,
        "cited_text": "Online Course Community Dimitrios Manias, Ali Chouman, Abdallah Shami, Semantic Routing for Enhanced Performance of LLM-Assisted Intent-Based 5G Core Network Management and Orchestration , IEEE GlobeCom 2024 Julian Horsey, Semantic Router superfast decision layer for LLMs and AI agents , Geeky Gadgets azhar, Beyond Basic Chatbots: How Semantic Router is Changing the Game , AI Insights @ Medium Daniel Avila, Semantic Router: Enhancing Control in LLM Conversations , CodeGPT @ Medium Yogendra Sisodia, Stop Chat-GPT From Going Rogue In Production With Semantic Router , Medium Aniket Hingane, LLM Apps: Why you Must Know Semantic Router in 2024: Part 1 , Medium Adrien Sales, 🔀 Semantic Router w. ollama/gemma2 : real life 10ms hotline challenge 🤯 Adrien Sales, Kaggle Notebook 🔀 Semantic Router: ollama / gemma2:9b hotline"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「Prompt Chaining（提示链）」与「Routing（路由）」是构建生产级、可预测 AI 应用的核心工作流模式。与完全依赖 LLM 自主决策的「智能体（Agents）」不同，这两者通过**预定义的代码路径**实现更高的确定性和一致性 [1, 2]。\n\n### 1. 核心算法流程\n*   **Prompt Chaining（串行执行流程）**：\n    1.  **分解**：将复杂任务拆分为固定的子任务序列（如：生成文案 $\\rightarrow$ 翻译 $\\rightarrow$ 格式检查）[3, 4]。\n    2.  **传递**：上一个 LLM 调用的输出作为下一个调用的输入 [3]。\n    3.  **验证（Gate 机制）**：在步骤间引入**编程检查点（Gate）**。如果输出不符合预定义标准，流程将触发重试或报错，防止错误累积 [3]。\n*   **Routing（分类转发流程）**：\n    1.  **分类（Classifier）**：输入首先经过分类器（可以是小型 LLM、传统算法或语义匹配模型）[5, 6]。\n    2.  **分配**：根据类别将任务导向专门的下游提示词、工具或特定模型（如：简单问题分发给 Claude Haiku，复杂问题分发给 Opus）[5]。\n    3.  **语义路由（Semantic Routing）**：利用**语义向量空间**。系统将查询转化为向量，通过余弦相似度与预设路径（RouteLayer）匹配，无需等待 LLM 生成文本即可做出决定 [6, 7]。\n\n### 2. 关键代码架构\n*   **低抽象架构（API 模式）**：Anthropic 建议开发者直接调用 LLM API 编写逻辑，认为这比复杂的框架更易于调试且透明度更高 [8]。\n*   **状态图架构（LangGraph）**：作为低层级编排框架，它将工作流构建为**状态图**，支持持久化存储、断点调试（Human-in-the-loop）和自动恢复 [9, 10]。\n*   **可视化编排（Flowise）**：采用可视化节点连接方式构建 Agentic Workflows，适合快速原型开发 [11, 12]。\n*   **生产级组件（Amazon Bedrock AgentCore）**：提供 Runtime（安全部署）、Gateway（统一工具访问）和 Memory（跨会话上下文保留）等组件来支撑规模化运行 [13]。\n\n### 3. 性能优化策略\n*   **智能路由（Intelligent Prompt Routing）**：自动根据请求复杂度分配模型，可实现**成本降低高达 30%** [14]。\n*   **模型蒸馏（Model Distillation）**：通过大模型训练小模型。蒸馏后的专用模型运行速度可提升 **500%**，成本降低 **75%**，且精度损失微乎其微 [14]。\n*   **响应延迟优化**：语义路由器（Semantic Router）的决策延迟仅为 **10ms 级别**，远快于 LLM 的推理生成 [15]。\n*   **提示词缓存（Prompt Caching）**：通过缓存重复的上下文或系统提示，显著降低首 token 延迟并节约成本 [14, 16]。\n\n### 4. 技术对比分析\n根据来源提供的信息，我们将工作流（Chaining/Routing）与自主智能体（Agents）进行对比：\n\n| 维度 | 工作流 (Chaining/Routing) | 自主智能体 (Autonomous Agents) |\n| :--- | :--- | :--- |\n| **控制力** | **预定义代码路径**，高度可控 [2] | LLM 动态指导流程，具有不确定性 [2] |\n| **适用场景** | 任务可分解、有固定标准（如客服自动回复）[3, 17] | 任务不可预测、需要多轮推理（如软件工程、复杂搜索）[18, 19] |\n| **性能表现** | 较低延迟，高可预测性 [20] | 以**延迟和成本**换取灵活性 [2, 21] |\n| **安全性** | 易于实施 Programmatic Gates [3] | 需在沙盒环境运行，依赖 Guardrails [21] |\n\n**关键数据总结**：\n*   **准确率指标**：利用 Bedrock Guardrails 配合自动化推理检查，识别模型响应的准确率可达 **99%**，并能拦截 **88%** 的有害内容 [22]。\n*   **模型参数**：Claude 4.6 系列模型中，Opus 支持最高 **100 万 token** 的上下文窗口（Beta 版），而 Haiku 是定位最快、最具成本效益的模型 [23, 24]。",
    "conversation_id": "57d6e6db-2415-4df0-8859-2d371dcde5b7",
    "sources_used": [
      "38eac028-33e1-461a-94fe-bd31488694f8",
      "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "9ef49dad-e363-44c5-ba53-bdf1c865b105",
      "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "9332d1d6-aff5-4ee1-8612-f929310f9838",
      "7709ccdf-b76e-4326-967c-bf2d038a4abd"
    ],
    "citations": {
      "1": "38eac028-33e1-461a-94fe-bd31488694f8",
      "2": "38eac028-33e1-461a-94fe-bd31488694f8",
      "3": "38eac028-33e1-461a-94fe-bd31488694f8",
      "4": "38eac028-33e1-461a-94fe-bd31488694f8",
      "5": "38eac028-33e1-461a-94fe-bd31488694f8",
      "6": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "7": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "8": "38eac028-33e1-461a-94fe-bd31488694f8",
      "9": "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "10": "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "11": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
      "12": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
      "13": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "14": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "15": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "16": "9332d1d6-aff5-4ee1-8612-f929310f9838",
      "17": "38eac028-33e1-461a-94fe-bd31488694f8",
      "18": "38eac028-33e1-461a-94fe-bd31488694f8",
      "19": "38eac028-33e1-461a-94fe-bd31488694f8",
      "20": "38eac028-33e1-461a-94fe-bd31488694f8",
      "21": "38eac028-33e1-461a-94fe-bd31488694f8",
      "22": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "23": "7709ccdf-b76e-4326-967c-bf2d038a4abd",
      "24": "7709ccdf-b76e-4326-967c-bf2d038a4abd"
    },
    "references": [
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 1,
        "cited_text": "In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents. What are agents? \"Agent\" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems , but draw an important architectural distinction between workflows and agents :"
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 2,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 3,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 4,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 5,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 6,
        "cited_text": "We begin by defining a set of Route objects. These are the decision paths that the semantic router can decide to use, let's try two simple routes for now — one for talk on politics and another for chitchat : We have our routes ready, now we initialize an embedding / encoder model. We currently support a CohereEncoder and OpenAIEncoder — more encoders will be added soon. To initialize them we do: With our routes and encoder defined we now create a RouteLayer . The route layer handles our semantic decision making."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 7,
        "cited_text": "Repository files navigation README Contributing MIT license Semantic Router is a superfast decision-making layer for your LLMs and agents. Rather than waiting for slow LLM generations to make tool-use decisions, we use the magic of semantic vector space to make those decisions — routing our requests using semantic meaning. Read the Docs Quickstart To get started with semantic-router we install it like so: ❗ If wanting to use a fully local version of semantic router you can use HuggingFaceEncoder and LlamaCppLLM ( pip install -qU \"semantic-router[local]\" , see here). To use the HybridRouteLayer you must pip install -qU \"semantic-router[hybrid]\" ."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 8,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "141802c7-ba51-4375-a7a4-2814284bfbb9",
        "citation_number": 9,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. If you're looking to quickly build agents with LangChain's create_agent (built on LangGraph), check out the LangChain Agents documentation ."
      },
      {
        "source_id": "141802c7-ba51-4375-a7a4-2814284bfbb9",
        "citation_number": 10,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
        "citation_number": 11,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing License Security English | 繁體中文 | 简体中文 | 日本語 | 한국어 Build AI Agents, Visually 📚 Table of Contents ⚡ Quick Start 🐳 Docker 👨💻 Developers 🌱 Env Variables 📖 Documentation 🌐 Self Host ☁ Flowise Cloud 🙋 Support 🙌 Contributing 📄 License ⚡Quick Start Download and Install NodeJS >= 18.15.0 Install Flowise Start Flowise Open http://localhost:3000"
      },
      {
        "source_id": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
        "citation_number": 12,
        "cited_text": "☁ Flowise Cloud Get Started with Flowise Cloud . 🙋 Support Feel free to ask any questions, raise problems, and request new features in Discussion . 🙌 Contributing Thanks go to these awesome contributors See Contributing Guide . Reach out to us at Discord if you have any questions or issues. 📄 License Source code in this repository is made available under the Apache License Version 2.0 . About Build AI Agents, Visually flowiseai.com Topics react javascript typescript chatbot artificial-intelligence openai multiagent-systems agents workflow-automation low-code no-code rag large-language-models chatgpt langchain agentic-workflow agentic-ai"
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 13,
        "cited_text": "Learn more about cost optimization Accelerate agents to production with composable services With Amazon Bedrock AgentCore enable agents to take actions across tools and data with the right permissions and controls, run agents securely at scale, and monitor agent performance and quality in production - all without any infrastructure management. AgentCore services and capabilities work together or independently: Runtime for secure, serverless deployment; Gateway for unified tool access and connections; Memory for intelligent context retention across sessions; Identity for seamless authentication across AWS and third-party services; Browser and Code Interpreter for enhanced agent capabilities; Observability for comprehensive monitoring and debugging; Evaluations for continuous quality scoring; and Policy for fine-grained control over agent actions."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 14,
        "cited_text": "Learn more about safety and guardrails Optimize for cost, latency, and accuracy Ensure your AI applications are optimized for the perfect balance of cost, speed, and accuracy. Features like Model Distillation, Prompt caching, and Intelligent Prompt Routing can reduce expenses while maintaining performance. For example, distilled models run up to 500% faster and cost up to 75% less, with minimal impact on accuracy. Intelligent Prompt Routing can cut costs by up to 30% while maintaining quality. With flexible options for both real-time and batch processing, Bedrock helps you build smart, efficient, and cost-effective AI systems."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 15,
        "cited_text": "Online Course Community Dimitrios Manias, Ali Chouman, Abdallah Shami, Semantic Routing for Enhanced Performance of LLM-Assisted Intent-Based 5G Core Network Management and Orchestration , IEEE GlobeCom 2024 Julian Horsey, Semantic Router superfast decision layer for LLMs and AI agents , Geeky Gadgets azhar, Beyond Basic Chatbots: How Semantic Router is Changing the Game , AI Insights @ Medium Daniel Avila, Semantic Router: Enhancing Control in LLM Conversations , CodeGPT @ Medium Yogendra Sisodia, Stop Chat-GPT From Going Rogue In Production With Semantic Router , Medium Aniket Hingane, LLM Apps: Why you Must Know Semantic Router in 2024: Part 1 , Medium Adrien Sales, 🔀 Semantic Router w. ollama/gemma2 : real life 10ms hotline challenge 🤯 Adrien Sales, Kaggle Notebook 🔀 Semantic Router: ollama / gemma2:9b hotline"
      },
      {
        "source_id": "9332d1d6-aff5-4ee1-8612-f929310f9838",
        "citation_number": 16,
        "cited_text": "Advanced Techniques Sub-agents : Learn how to use Haiku as a sub-agent in combination with Opus. Upload PDFs to Claude : Parse and pass PDFs as text to Claude. Automated evaluations : Use Claude to automate the prompt evaluation process. Enable JSON mode : Ensure consistent JSON output from Claude. Create a moderation filter : Use Claude to create a content moderation filter for your application. Prompt caching : Learn techniques for efficient prompt caching with Claude. Additional Resources"
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 17,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 18,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 19,
        "cited_text": "Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness. B. Coding agents The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because: Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 20,
        "cited_text": "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough. When and how to use frameworks There are many frameworks that make agentic systems easier to implement, including: The Claude Agent SDK ; Strands Agents SDK by AWS ; Rivet , a drag and drop GUI LLM workflow builder; and Vellum , another GUI tool for building and testing complex workflows."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 21,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 22,
        "cited_text": "Securely customize with your data Move from generic AI to AI that knows your customer and your business by customizing models with your data. By combining multiple data customization tools—Knowledge Bases, Bedrock Data Automation, prompt engineering, and fine-tuning—you can optimize your AI applications to your business, while ensuring you're always in control of sensitive information. Learn more about customization Apply security, privacy, and responsible AI checks Amazon Bedrock provides industry-leading security, privacy, and compliance for generative AI applications. Bedrock Guardrails can help block up to 88% of harmful content and identify correct model responses with up to 99% accuracy to minimize hallucinations and data ambiguity using Automated Reasoning checks. Bedrock never stores or uses your data to train models, ensuring complete security and privacy, with encryption of data in transit and at rest, as well as identity-based policies for managing data access. Bedrock provides comprehensive monitoring and logging capabilities that can support your governance and audit requirements. Finally, Bedrock is in scope for common compliance standards including ISO, SOC, CSA STAR Level 2, GDPR, FedRAMP High, and is HIPAA eligible."
      },
      {
        "source_id": "7709ccdf-b76e-4326-967c-bf2d038a4abd",
        "citation_number": 23,
        "cited_text": "所有当前的 Claude 模型都支持文本和图像输入、文本输出、多语言能力和视觉功能。模型可通过 Anthropic API、AWS Bedrock 和 Google Vertex AI 使用。 选择模型后， 了解如何进行首次 API 调用 。 最新模型对比 <cited_table>",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "特性",
              "Claude Opus 4.6",
              "Claude Sonnet 4.5",
              "Claude Haiku 4.5"
            ],
            [
              "描述",
              "我们最智能的模型，适用于构建智能体和编码",
              "速度与智能的最佳组合",
              "我们最快的模型，具有接近前沿的智能"
            ],
            [
              "Claude API ID",
              "claude-opus-4-6",
              "claude-sonnet-4-5-20250929",
              "claude-haiku-4-5-20251001"
            ],
            [
              "Claude API 别名",
              "claude-opus-4-6",
              "claude-sonnet-4-5",
              "claude-haiku-4-5"
            ],
            [
              "AWS Bedrock ID",
              "anthropic.claude-opus-4-6-v1:0",
              "anthropic.claude-sonnet-4-5-20250929-v1:0",
              "anthropic.claude-haiku-4-5-20251001-v1:0"
            ],
            [
              "GCP Vertex AI ID",
              "claude-opus-4-6",
              "claude-sonnet-4-5@20250929",
              "claude-haiku-4-5@20251001"
            ],
            [
              "定价",
              "$5 / 输入 MTok $25 / 输出 MTok",
              "$3 / 输入 MTok $15 / 输出 MTok",
              "$1 / 输入 MTok $5 / 输出 MTok"
            ],
            [
              "扩展思考",
              "是",
              "是",
              "是"
            ],
            [
              "自适应思考",
              "是",
              "否",
              "否"
            ],
            [
              "优先级层",
              "是",
              "是",
              "是"
            ],
            [
              "相对延迟",
              "中等",
              "快",
              "最快"
            ],
            [
              "上下文窗口",
              "200K tokens / 1M tokens (beta)",
              "200K tokens / 1M tokens (beta)",
              "200K tokens"
            ],
            [
              "最大输出",
              "128K tokens",
              "64K tokens",
              "64K tokens"
            ],
            [
              "可靠知识截止日期",
              "2025 年 5 月",
              "2025 年 1 月",
              "2025 年 2 月"
            ],
            [
              "训练数据截止日期",
              "2025 年 8 月",
              "2025 年 7 月",
              "2025 年 7 月"
            ]
          ]
        }
      },
      {
        "source_id": "7709ccdf-b76e-4326-967c-bf2d038a4abd",
        "citation_number": 24,
        "cited_text": "1-请参阅我们的 定价页面 了解完整的定价信息，包括批量API折扣、提示缓存费率、扩展思考成本和视觉处理费用。 * 2- 可靠知识截止日期 表示模型知识最为广泛和可靠的截止日期。 训练数据截止日期 是所使用训练数据的更广泛日期范围。更多信息请参阅 Anthropic透明度中心 。 * 3-ClaudeOpus4.6和Sonnet4.5在使用 context-1m-2025-08-07 beta头时支持 1Mtoken上下文窗口 。超过200Ktokens的请求适用 长上下文定价 。 * 具有相同快照日期（例如 20240620）的模型在所有平台上都是相同的，不会发生变化。模型名称中的快照日期确保了一致性，使开发者能够在不同环境中依赖稳定的性能。 从 ** Claude Sonnet 4.5 及所有后续模型 开始，AWS Bedrock 和 Google Vertex AI 提供两种端点类型： 全局端点（动态路由以实现最大可用性）和 区域端点**（通过特定地理区域保证数据路由）。更多信息请参阅 第三方平台定价部分 。 旧版模型 提示和输出性能 Claude 4 模型在以下方面表现出色： 性能 ：在推理、编码、多语言任务、长上下文处理、诚实性和图像处理方面取得顶级成果。更多信息请参阅 Claude 4 博客文章 。 引人入胜的回复 ：Claude 模型非常适合需要丰富、类人交互的应用。 如果您偏好更简洁的回复，可以调整提示来引导模型生成所需的输出长度。详情请参阅我们的 提示工程指南 。 有关提示最佳实践，请参阅我们的 提示最佳实践指南 。 输出质量 ：从之前的模型代际迁移到 Claude 4 时，您可能会注意到整体性能的显著提升。"
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "基于提供的源文件，以下是「Prompt Chaining（提示链）与 Routing（路由）」在构建可预测工作流中的真实应用场景、工业方案及实践经验总结：\n\n### 1. 工业级部署方案与真实案例\n工业级应用强调**安全性、成本优化和可扩展性**。\n*   **Amazon Bedrock AgentCore**：这是典型的工业级部署架构，提供 Runtime（无服务器部署）、Gateway（统一工具访问）、Memory（跨会话上下文保留）和 Observability（监控与调试）等核心组件 [1, 2]。\n*   **Robinhood（金融创新）**：通过在 Amazon Bedrock 上部署可预测工作流，在 6 个月内将 token 处理量从每日 5 亿提升至 **50 亿**，同时将 AI 成本降低了 **80%**，并将开发时间缩短了一半 [3]。\n*   **Epsilon（营销自动化）**：利用提示链与路由技术自动化复杂的营销活动工作流。通过预定义路径，将原本需要数月的开发周期缩短至**数周**，并在保持企业级安全性的同时实现了个性化体验 [4]。\n*   **客户服务（通用场景）**：将路由用于分类查询（如：一般问题、退款申请、技术支持），将简单请求路由至轻量级模型（如 Claude Haiku），而将复杂请求导向专业化工具或强力模型（如 Claude Opus） [5, 6]。\n\n### 2. 开源项目实战案例\n开发者可以利用成熟的开源框架快速实现这些模式：\n*   **LangGraph**：一个低层级的编排框架，支持构建**状态化**的提示链。它被 Klarna 和 Replit 等公司用于构建具有「人机回环」（Human-in-the-loop）功能的复杂工作流 [7, 8]。\n*   **Semantic Router**：专注于极速决策的路由层。它不依赖缓慢的 LLM 生成，而是通过向量空间匹配进行决策，延迟仅为 **10ms 级别** [9, 10]。\n*   **Flowise**：一个可视化编排工具，允许开发者通过拖拽节点的方式构建提示链和 Agent 工作流，支持在 AWS、Azure 等云端自托管部署 [11-13]。\n*   **Claude Cookbooks**：提供了实战「食谱」，例如将 Haiku 作为子智能体（Sub-agent）与 Opus 链式配合，以及如何实现高效的提示词缓存（Prompt Caching） [14]。\n\n### 3. 性能基准数据\n*   **成本与速度优化**：\n    *   **模型蒸馏（Distillation）**：专用的小型模型运行速度可提升 **500%**，成本降低 **75%**，而精度损失极小 [15]。\n    *   **智能路由**：根据任务复杂度自动路由模型，可降低高达 **30% 的成本** [15]。\n*   **安全性与准确率**：\n    *   **Bedrock Guardrails**：在自动化推理检查的配合下，识别正确响应的准确率可达 **99%**，并能拦截多达 **88%** 的有害内容 [16]。\n*   **推理任务表现**：\n    *   **GeM-CoT**：一种通用的思维链（CoT）路由机制，在 10 个公共推理任务和 23 个 BBH 任务中展现了卓越的泛化性能 [17]。\n\n### 4. 开发者最佳实践\n*   **从简单开始**：始终先尝试简单的提示词和 RAG，仅在必要时增加提示链或路由的复杂度 [18, 19]。\n*   **保持透明度**：在设计智能体时，应显式展示其规划步骤，以便于调试和用户信任 [20]。\n*   **专注于 ACI（Agent-Computer Interface）**：为智能体使用的工具编写精细的文档（如同为初级开发人员编写 docstring），包含示例、边界情况和输入格式要求 [21, 22]。\n*   **引入编程栅栏 (Programmatic Gates)**：在提示链的中间步骤加入代码检查，确保输出符合预期后再进入下一步 [23]。\n\n### 5. 常见踩坑经验与解决方案\n*   **过度抽象风险**：过度依赖框架可能导致底层提示词和响应被遮蔽，使调试变得困难。建议开发者从直接调用 LLM API 开始构建 [20, 24]。\n*   **格式开销过大**：要求 LLM 输出复杂的 JSON（涉及大量转义）比 Markdown 更具挑战性。应尽量减少格式开销，给模型留出「思考」的 token 空间 [21, 25]。\n*   **文件路径问题**：在构建编码智能体时，相对路径容易在切换目录后出错。**实战经验**表明，强制要求模型使用**绝对路径**可显著提升成功率 [26]。\n*   **随机性与蝴蝶效应**：在全自动构建（如本体构建）中，响应的随机性可能引发后续步骤的偏差。**最佳实践**是引入人类早期干预和监督，以提高效率和产出质量 [27]。",
    "conversation_id": "57d6e6db-2415-4df0-8859-2d371dcde5b7",
    "sources_used": [
      "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "38eac028-33e1-461a-94fe-bd31488694f8",
      "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "9ef49dad-e363-44c5-ba53-bdf1c865b105",
      "9332d1d6-aff5-4ee1-8612-f929310f9838",
      "9b244d49-e214-4724-9d67-318f5cdad25c",
      "3454bfd3-bc2c-45d1-9e33-715a54b1c0ff"
    ],
    "citations": {
      "1": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "2": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "3": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "4": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "5": "38eac028-33e1-461a-94fe-bd31488694f8",
      "6": "38eac028-33e1-461a-94fe-bd31488694f8",
      "7": "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "8": "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "9": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "10": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "11": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
      "12": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
      "13": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
      "14": "9332d1d6-aff5-4ee1-8612-f929310f9838",
      "15": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "16": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "17": "9b244d49-e214-4724-9d67-318f5cdad25c",
      "18": "38eac028-33e1-461a-94fe-bd31488694f8",
      "19": "38eac028-33e1-461a-94fe-bd31488694f8",
      "20": "38eac028-33e1-461a-94fe-bd31488694f8",
      "21": "38eac028-33e1-461a-94fe-bd31488694f8",
      "22": "38eac028-33e1-461a-94fe-bd31488694f8",
      "23": "38eac028-33e1-461a-94fe-bd31488694f8",
      "24": "38eac028-33e1-461a-94fe-bd31488694f8",
      "25": "38eac028-33e1-461a-94fe-bd31488694f8",
      "26": "38eac028-33e1-461a-94fe-bd31488694f8",
      "27": "3454bfd3-bc2c-45d1-9e33-715a54b1c0ff"
    },
    "references": [
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 1,
        "cited_text": "Amazon Bedrock gives you access to hundreds of FMs from leading AI companies along with evaluation tools to pick the best model based on your unique performance and cost needs. Future-proof your AI strategy as your needs evolve and new models emerge. Learn more about model choice Build and deploy agents Accelerate agents to production with Amazon Bedrock AgentCore , an agentic platform to build, deploy and operate highly capable agents securely, at scale using any framework and model – no infrastructure management required. Or you can orchestrate agents using Amazon Bedrock Agents for guided agent building."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 2,
        "cited_text": "Learn more about cost optimization Accelerate agents to production with composable services With Amazon Bedrock AgentCore enable agents to take actions across tools and data with the right permissions and controls, run agents securely at scale, and monitor agent performance and quality in production - all without any infrastructure management. AgentCore services and capabilities work together or independently: Runtime for secure, serverless deployment; Gateway for unified tool access and connections; Memory for intelligent context retention across sessions; Identity for seamless authentication across AWS and third-party services; Browser and Code Interpreter for enhanced agent capabilities; Observability for comprehensive monitoring and debugging; Evaluations for continuous quality scoring; and Policy for fine-grained control over agent actions."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 3,
        "cited_text": "Explore frontier agents Meet AWS frontier agents Announcing general availability of AWS Security & DevOps Agents—changing the way we secure and operate software at scale. Explore frontier agents Real results, real customers Robinhood Robinhood transformed into an AI-first financial innovator using Amazon Bedrock, scaling from 500 million to 5 billion tokens daily in just six months—while slashing AI costs by 80% and cutting development time in half. According to Dev Tagare, Robinhood's Head of AI, Amazon Bedrock's model diversity, security, and compliance features are purpose-built for regulated industries. Robinhood's success demonstrates how fintech leaders can use Amazon Bedrock to democratize finance with cutting-edge AI while maintaining enterprise-grade security and compliance."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 4,
        "cited_text": "Opaque Semi-Transparent Text Background Color Black White Red Green Blue Yellow Magenta Cyan Opacity Opaque Semi-Transparent Transparent Caption Area Background Color Black White Red Green Blue Yellow Magenta Cyan Opacity Transparent Semi-Transparent Opaque Font Size 50% 75% 100% 125% 150% 175% 200% 300% 400% Text Edge Style None Raised Depressed Uniform Drop shadow Font Family Proportional Sans-Serif Monospace Sans-Serif Proportional Serif Monospace Serif Casual Script Small Caps Reset Done Close Modal Dialog End of dialog window. Epsilon Epsilon used Amazon Bedrock AgentCore to transform their marketing operations, enabling intelligent agents to automate complex campaign workflows while maintaining enterprise-grade security and compliance. Epsilon accelerated their agent development from months to weeks, delivering personalized marketing experiences at scale while reducing operational overhead."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 5,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 6,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "141802c7-ba51-4375-a7a4-2814284bfbb9",
        "citation_number": 7,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. If you're looking to quickly build agents with LangChain's create_agent (built on LangGraph), check out the LangChain Agents documentation ."
      },
      {
        "source_id": "141802c7-ba51-4375-a7a4-2814284bfbb9",
        "citation_number": 8,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 9,
        "cited_text": "Repository files navigation README Contributing MIT license Semantic Router is a superfast decision-making layer for your LLMs and agents. Rather than waiting for slow LLM generations to make tool-use decisions, we use the magic of semantic vector space to make those decisions — routing our requests using semantic meaning. Read the Docs Quickstart To get started with semantic-router we install it like so: ❗ If wanting to use a fully local version of semantic router you can use HuggingFaceEncoder and LlamaCppLLM ( pip install -qU \"semantic-router[local]\" , see here). To use the HybridRouteLayer you must pip install -qU \"semantic-router[hybrid]\" ."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 10,
        "cited_text": "Online Course Community Dimitrios Manias, Ali Chouman, Abdallah Shami, Semantic Routing for Enhanced Performance of LLM-Assisted Intent-Based 5G Core Network Management and Orchestration , IEEE GlobeCom 2024 Julian Horsey, Semantic Router superfast decision layer for LLMs and AI agents , Geeky Gadgets azhar, Beyond Basic Chatbots: How Semantic Router is Changing the Game , AI Insights @ Medium Daniel Avila, Semantic Router: Enhancing Control in LLM Conversations , CodeGPT @ Medium Yogendra Sisodia, Stop Chat-GPT From Going Rogue In Production With Semantic Router , Medium Aniket Hingane, LLM Apps: Why you Must Know Semantic Router in 2024: Part 1 , Medium Adrien Sales, 🔀 Semantic Router w. ollama/gemma2 : real life 10ms hotline challenge 🤯 Adrien Sales, Kaggle Notebook 🔀 Semantic Router: ollama / gemma2:9b hotline"
      },
      {
        "source_id": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
        "citation_number": 11,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing License Security English | 繁體中文 | 简体中文 | 日本語 | 한국어 Build AI Agents, Visually 📚 Table of Contents ⚡ Quick Start 🐳 Docker 👨💻 Developers 🌱 Env Variables 📖 Documentation 🌐 Self Host ☁ Flowise Cloud 🙋 Support 🙌 Contributing 📄 License ⚡Quick Start Download and Install NodeJS >= 18.15.0 Install Flowise Start Flowise Open http://localhost:3000"
      },
      {
        "source_id": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
        "citation_number": 12,
        "cited_text": "Any code changes will reload the app automatically on http://localhost:8080 🌱 Env Variables Flowise supports different environment variables to configure your instance. You can specify the following variables in the .env file inside packages/server folder. Read more 📖 Documentation You can view the Flowise Docs here 🌐 Self Host Deploy Flowise self-hosted in your existing infrastructure, we support various deployments AWS Azure Digital Ocean GCP Alibaba Cloud Others Railway Northflank Render HuggingFace Spaces Elestio Sealos RepoCloud"
      },
      {
        "source_id": "9ef49dad-e363-44c5-ba53-bdf1c865b105",
        "citation_number": 13,
        "cited_text": "☁ Flowise Cloud Get Started with Flowise Cloud . 🙋 Support Feel free to ask any questions, raise problems, and request new features in Discussion . 🙌 Contributing Thanks go to these awesome contributors See Contributing Guide . Reach out to us at Discord if you have any questions or issues. 📄 License Source code in this repository is made available under the Apache License Version 2.0 . About Build AI Agents, Visually flowiseai.com Topics react javascript typescript chatbot artificial-intelligence openai multiagent-systems agents workflow-automation low-code no-code rag large-language-models chatgpt langchain agentic-workflow agentic-ai"
      },
      {
        "source_id": "9332d1d6-aff5-4ee1-8612-f929310f9838",
        "citation_number": 14,
        "cited_text": "Advanced Techniques Sub-agents : Learn how to use Haiku as a sub-agent in combination with Opus. Upload PDFs to Claude : Parse and pass PDFs as text to Claude. Automated evaluations : Use Claude to automate the prompt evaluation process. Enable JSON mode : Ensure consistent JSON output from Claude. Create a moderation filter : Use Claude to create a content moderation filter for your application. Prompt caching : Learn techniques for efficient prompt caching with Claude. Additional Resources"
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 15,
        "cited_text": "Learn more about safety and guardrails Optimize for cost, latency, and accuracy Ensure your AI applications are optimized for the perfect balance of cost, speed, and accuracy. Features like Model Distillation, Prompt caching, and Intelligent Prompt Routing can reduce expenses while maintaining performance. For example, distilled models run up to 500% faster and cost up to 75% less, with minimal impact on accuracy. Intelligent Prompt Routing can cut costs by up to 30% while maintaining quality. With flexible options for both real-time and batch processing, Bedrock helps you build smart, efficient, and cost-effective AI systems."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 16,
        "cited_text": "Securely customize with your data Move from generic AI to AI that knows your customer and your business by customizing models with your data. By combining multiple data customization tools—Knowledge Bases, Bedrock Data Automation, prompt engineering, and fine-tuning—you can optimize your AI applications to your business, while ensuring you're always in control of sensitive information. Learn more about customization Apply security, privacy, and responsible AI checks Amazon Bedrock provides industry-leading security, privacy, and compliance for generative AI applications. Bedrock Guardrails can help block up to 88% of harmful content and identify correct model responses with up to 99% accuracy to minimize hallucinations and data ambiguity using Automated Reasoning checks. Bedrock never stores or uses your data to train models, ensuring complete security and privacy, with encryption of data in transit and at rest, as well as identity-based policies for managing data access. Bedrock provides comprehensive monitoring and logging capabilities that can support your governance and audit requirements. Finally, Bedrock is in scope for common compliance standards including ISO, SOC, CSA STAR Level 2, GDPR, FedRAMP High, and is HIPAA eligible."
      },
      {
        "source_id": "9b244d49-e214-4724-9d67-318f5cdad25c",
        "citation_number": 17,
        "cited_text": "Computer Science > Computation and Language arXiv:2310.06692 (cs) [Submitted on 10 Oct 2023 ( v1 ), last revised 20 Feb 2024 (this version, v3)] Title: Generalizable Chain-of-Thought Prompting in Mixed-task Scenarios with Large Language Models Authors: Anni Zou , Zhuosheng Zhang , Hai Zhao , Xiangru Tang View a PDF of the paper titled Generalizable Chain-of-Thought Prompting in Mixed-task Scenarios with Large Language Models, by Anni Zou and 3 other authors View PDF Abstract: Large language models (LLMs) have unveiled remarkable reasoning capabilities by exploiting chain-of-thought (CoT) prompting, which generates intermediate reasoning chains to serve as the rationale for deriving the answer. However, current CoT methods either simply employ general prompts such as Let's think step by step, or heavily rely on pre-defined task-specific demonstrations to attain preferable performances, thereby engendering an inescapable gap between performance and generalization. To bridge this gap, we propose GeM-CoT, a Generalizable CoT prompting mechanism in Mixed-task scenarios where the type of input questions is unknown. GeM-CoT first categorizes the question type and subsequently samples or constructs demonstrations from the corresponding data pool in an automatic pattern. With this technical design, GeM-CoT simultaneously enjoys superior generalization capabilities and remarkable performances on 10 public reasoning tasks and 23 BBH tasks."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 18,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 19,
        "cited_text": "Combining and customizing these patterns These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity only when it demonstrably improves outcomes. Summary Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 20,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 21,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 22,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 23,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 24,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 25,
        "cited_text": "There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 26,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "3454bfd3-bc2c-45d1-9e33-715a54b1c0ff",
        "citation_number": 27,
        "cited_text": "View PDF Abstract: Engineering knowledge-based (or expert) systems require extensive manual effort and domain knowledge. As Large Language Models (LLMs) are trained using an enormous amount of cross-domain knowledge, it becomes possible to automate such engineering processes. This paper presents an empirical automation and semi-automation framework for domain knowledge distillation using prompt engineering and the LLM ChatGPT. We assess the framework empirically in the autonomous driving domain and present our key observations. In our implementation, we construct the domain knowledge ontology by \"chatting\" with ChatGPT. The key finding is that while fully automated domain ontology construction is possible, human supervision and early intervention typically improve efficiency and output quality as they lessen the effects of response randomness and the butterfly effect. We, therefore, also develop a web-based distillation assistant enabling supervision and flexible intervention at runtime. We hope our findings and tools could inspire future research toward revolutionizing the engineering of knowledge-based systems across application domains."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「Prompt Chaining（提示链）」与「Routing（路由）」构建的可预测工作流领域，2025-2026年的研究与技术趋势正从单一的模型调用转向**高度工程化的系统编排**。\n\n以下是基于来源的详细分析：\n\n### 1. 2025-2026 重要技术趋势与研究突破\n*   **模型能力的代际跃迁 (Claude 4.6 & Opus)**：最新一代模型（如 Claude Opus 4.6）引入了**扩展思考 (Extended Thinking)** 和 **自适应思考 (Adaptive Thinking)** 模式，使模型在进入提示链之前能进行更深度的内部推理 [1]。这显著增强了复杂逻辑链条的稳定性 [2]。\n*   **GeM-CoT（通用化思维链路由）**：研究提出了一种名为 **GeM-CoT** 的新机制，专门解决混合任务场景下的路由问题 [3]。它能自动识别输入问题的类型，并从动态数据池中构建相应的示例（Demonstrations），实现了在 10 个公共推理任务和 23 个 BBH 任务上的性能与泛化能力的平衡 [3]。\n*   **极速语义路由 (Semantic Router)**：技术重心正转向基于**语义向量空间**的决策层，例如 Semantic Router 项目 [4]。它通过余弦相似度匹配预设路径，将决策延迟降低至 **10ms 级别**，从而避免了等待 LLM 文本生成带来的高延迟 [5]。\n*   **智能提示词路由 (Intelligent Prompt Routing)**：工业界（如 Amazon Bedrock）开始大规模应用自动路由技术，根据任务复杂度动态分配模型（如将简单任务分发给 Haiku 4.5，复杂任务分发给 Opus 4.6），在保持质量的同时可**降低 30% 的成本** [1, 6]。\n\n### 2. 核心架构演进：从「智能体」回归「工作流」\n*   **确定性路径的回归**：Anthropic 明确区分了「工作流（Workflows）」与「智能体（Agents）」：工作流通过**预定义代码路径**编排 LLM 和工具，而智能体则由 LLM 动态驱动 [7, 8]。目前的趋势是**优先使用工作流以换取可预测性和一致性**，仅在极具灵活性的场景下使用自主智能体 [8, 9]。\n*   **状态化编排框架**：以 **LangGraph** 为代表的低层级框架正成为主流，它提供**持久化存储（Persistence）**、**持久执行（Durable Execution）**和**断点调试**能力，允许工作流在失败后从精确位置恢复 [10, 11]。\n\n### 3. 未解决的挑战\n*   **错误的复合效应 (Compounding Errors)**：在长提示链或自主智能体中，细微的步骤偏差会随着迭代增加而累积，导致最终输出完全偏离轨道 [12]。\n*   **ACI (Agent-Computer Interface) 的标准缺失**：工具的文档定义（ACI）往往不够严谨，导致模型在调用 API 时出现格式错误或路径引用错误（如相对路径导致的混乱） [13, 14]。\n*   **响应随机性与「蝴蝶效应」**：在全自动化的领域知识蒸馏（Domain Knowledge Distillation）中，LLM 响应的随机性可能引发后续链条的连锁反应，影响本体构建的质量 [15]。\n\n### 4. 未来可能的突破点\n*   **超长上下文的高效路由**：随着 Claude 4.6 等模型支持高达 **100 万 token** 的上下文窗口（Beta 版），如何在该窗口内精准定位并路由关键信息将成为核心课题 [1]。\n*   **人机回环 (HITL) 的深度集成**：未来的突破点在于如何更自然地在提示链的「编程栅栏 (Programmatic Gates)」中引入人类干预 [16]。研究表明，**早期的人类监督和干预**能显著提升自动化流程的效率和产出质量 [15]。\n*   **多模态路由与验证**：目前的路由多集中于文本，未来将扩展到**多模态路由**（如识别图像内容并分发给特定视觉模型）以及自动化推理检查（Automated Reasoning checks）的普及，目前这类检查已能达到 **99% 的准确率** [17, 18]。\n\n**总结建议**：开发者应遵循**「简单性、透明性、精细 ACI」**三大原则，优先构建简单的提示链，仅在复杂性确实能带来结果提升时才引入多级路由和自主智能体架构 [19, 20]。",
    "conversation_id": "57d6e6db-2415-4df0-8859-2d371dcde5b7",
    "sources_used": [
      "7709ccdf-b76e-4326-967c-bf2d038a4abd",
      "9b244d49-e214-4724-9d67-318f5cdad25c",
      "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "38eac028-33e1-461a-94fe-bd31488694f8",
      "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "3454bfd3-bc2c-45d1-9e33-715a54b1c0ff"
    ],
    "citations": {
      "1": "7709ccdf-b76e-4326-967c-bf2d038a4abd",
      "2": "7709ccdf-b76e-4326-967c-bf2d038a4abd",
      "3": "9b244d49-e214-4724-9d67-318f5cdad25c",
      "4": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "5": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "6": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "7": "38eac028-33e1-461a-94fe-bd31488694f8",
      "8": "38eac028-33e1-461a-94fe-bd31488694f8",
      "9": "38eac028-33e1-461a-94fe-bd31488694f8",
      "10": "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "11": "141802c7-ba51-4375-a7a4-2814284bfbb9",
      "12": "38eac028-33e1-461a-94fe-bd31488694f8",
      "13": "38eac028-33e1-461a-94fe-bd31488694f8",
      "14": "38eac028-33e1-461a-94fe-bd31488694f8",
      "15": "3454bfd3-bc2c-45d1-9e33-715a54b1c0ff",
      "16": "38eac028-33e1-461a-94fe-bd31488694f8",
      "17": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
      "18": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
      "19": "38eac028-33e1-461a-94fe-bd31488694f8",
      "20": "38eac028-33e1-461a-94fe-bd31488694f8"
    },
    "references": [
      {
        "source_id": "7709ccdf-b76e-4326-967c-bf2d038a4abd",
        "citation_number": 1,
        "cited_text": "所有当前的 Claude 模型都支持文本和图像输入、文本输出、多语言能力和视觉功能。模型可通过 Anthropic API、AWS Bedrock 和 Google Vertex AI 使用。 选择模型后， 了解如何进行首次 API 调用 。 最新模型对比 <cited_table>",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "特性",
              "Claude Opus 4.6",
              "Claude Sonnet 4.5",
              "Claude Haiku 4.5"
            ],
            [
              "描述",
              "我们最智能的模型，适用于构建智能体和编码",
              "速度与智能的最佳组合",
              "我们最快的模型，具有接近前沿的智能"
            ],
            [
              "Claude API ID",
              "claude-opus-4-6",
              "claude-sonnet-4-5-20250929",
              "claude-haiku-4-5-20251001"
            ],
            [
              "Claude API 别名",
              "claude-opus-4-6",
              "claude-sonnet-4-5",
              "claude-haiku-4-5"
            ],
            [
              "AWS Bedrock ID",
              "anthropic.claude-opus-4-6-v1:0",
              "anthropic.claude-sonnet-4-5-20250929-v1:0",
              "anthropic.claude-haiku-4-5-20251001-v1:0"
            ],
            [
              "GCP Vertex AI ID",
              "claude-opus-4-6",
              "claude-sonnet-4-5@20250929",
              "claude-haiku-4-5@20251001"
            ],
            [
              "定价",
              "$5 / 输入 MTok $25 / 输出 MTok",
              "$3 / 输入 MTok $15 / 输出 MTok",
              "$1 / 输入 MTok $5 / 输出 MTok"
            ],
            [
              "扩展思考",
              "是",
              "是",
              "是"
            ],
            [
              "自适应思考",
              "是",
              "否",
              "否"
            ],
            [
              "优先级层",
              "是",
              "是",
              "是"
            ],
            [
              "相对延迟",
              "中等",
              "快",
              "最快"
            ],
            [
              "上下文窗口",
              "200K tokens / 1M tokens (beta)",
              "200K tokens / 1M tokens (beta)",
              "200K tokens"
            ],
            [
              "最大输出",
              "128K tokens",
              "64K tokens",
              "64K tokens"
            ],
            [
              "可靠知识截止日期",
              "2025 年 5 月",
              "2025 年 1 月",
              "2025 年 2 月"
            ],
            [
              "训练数据截止日期",
              "2025 年 8 月",
              "2025 年 7 月",
              "2025 年 7 月"
            ]
          ]
        }
      },
      {
        "source_id": "7709ccdf-b76e-4326-967c-bf2d038a4abd",
        "citation_number": 2,
        "cited_text": "1-请参阅我们的 定价页面 了解完整的定价信息，包括批量API折扣、提示缓存费率、扩展思考成本和视觉处理费用。 * 2- 可靠知识截止日期 表示模型知识最为广泛和可靠的截止日期。 训练数据截止日期 是所使用训练数据的更广泛日期范围。更多信息请参阅 Anthropic透明度中心 。 * 3-ClaudeOpus4.6和Sonnet4.5在使用 context-1m-2025-08-07 beta头时支持 1Mtoken上下文窗口 。超过200Ktokens的请求适用 长上下文定价 。 * 具有相同快照日期（例如 20240620）的模型在所有平台上都是相同的，不会发生变化。模型名称中的快照日期确保了一致性，使开发者能够在不同环境中依赖稳定的性能。 从 ** Claude Sonnet 4.5 及所有后续模型 开始，AWS Bedrock 和 Google Vertex AI 提供两种端点类型： 全局端点（动态路由以实现最大可用性）和 区域端点**（通过特定地理区域保证数据路由）。更多信息请参阅 第三方平台定价部分 。 旧版模型 提示和输出性能 Claude 4 模型在以下方面表现出色： 性能 ：在推理、编码、多语言任务、长上下文处理、诚实性和图像处理方面取得顶级成果。更多信息请参阅 Claude 4 博客文章 。 引人入胜的回复 ：Claude 模型非常适合需要丰富、类人交互的应用。 如果您偏好更简洁的回复，可以调整提示来引导模型生成所需的输出长度。详情请参阅我们的 提示工程指南 。 有关提示最佳实践，请参阅我们的 提示最佳实践指南 。 输出质量 ：从之前的模型代际迁移到 Claude 4 时，您可能会注意到整体性能的显著提升。"
      },
      {
        "source_id": "9b244d49-e214-4724-9d67-318f5cdad25c",
        "citation_number": 3,
        "cited_text": "Computer Science > Computation and Language arXiv:2310.06692 (cs) [Submitted on 10 Oct 2023 ( v1 ), last revised 20 Feb 2024 (this version, v3)] Title: Generalizable Chain-of-Thought Prompting in Mixed-task Scenarios with Large Language Models Authors: Anni Zou , Zhuosheng Zhang , Hai Zhao , Xiangru Tang View a PDF of the paper titled Generalizable Chain-of-Thought Prompting in Mixed-task Scenarios with Large Language Models, by Anni Zou and 3 other authors View PDF Abstract: Large language models (LLMs) have unveiled remarkable reasoning capabilities by exploiting chain-of-thought (CoT) prompting, which generates intermediate reasoning chains to serve as the rationale for deriving the answer. However, current CoT methods either simply employ general prompts such as Let's think step by step, or heavily rely on pre-defined task-specific demonstrations to attain preferable performances, thereby engendering an inescapable gap between performance and generalization. To bridge this gap, we propose GeM-CoT, a Generalizable CoT prompting mechanism in Mixed-task scenarios where the type of input questions is unknown. GeM-CoT first categorizes the question type and subsequently samples or constructs demonstrations from the corresponding data pool in an automatic pattern. With this technical design, GeM-CoT simultaneously enjoys superior generalization capabilities and remarkable performances on 10 public reasoning tasks and 23 BBH tasks."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 4,
        "cited_text": "Repository files navigation README Contributing MIT license Semantic Router is a superfast decision-making layer for your LLMs and agents. Rather than waiting for slow LLM generations to make tool-use decisions, we use the magic of semantic vector space to make those decisions — routing our requests using semantic meaning. Read the Docs Quickstart To get started with semantic-router we install it like so: ❗ If wanting to use a fully local version of semantic router you can use HuggingFaceEncoder and LlamaCppLLM ( pip install -qU \"semantic-router[local]\" , see here). To use the HybridRouteLayer you must pip install -qU \"semantic-router[hybrid]\" ."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 5,
        "cited_text": "Online Course Community Dimitrios Manias, Ali Chouman, Abdallah Shami, Semantic Routing for Enhanced Performance of LLM-Assisted Intent-Based 5G Core Network Management and Orchestration , IEEE GlobeCom 2024 Julian Horsey, Semantic Router superfast decision layer for LLMs and AI agents , Geeky Gadgets azhar, Beyond Basic Chatbots: How Semantic Router is Changing the Game , AI Insights @ Medium Daniel Avila, Semantic Router: Enhancing Control in LLM Conversations , CodeGPT @ Medium Yogendra Sisodia, Stop Chat-GPT From Going Rogue In Production With Semantic Router , Medium Aniket Hingane, LLM Apps: Why you Must Know Semantic Router in 2024: Part 1 , Medium Adrien Sales, 🔀 Semantic Router w. ollama/gemma2 : real life 10ms hotline challenge 🤯 Adrien Sales, Kaggle Notebook 🔀 Semantic Router: ollama / gemma2:9b hotline"
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 6,
        "cited_text": "Learn more about safety and guardrails Optimize for cost, latency, and accuracy Ensure your AI applications are optimized for the perfect balance of cost, speed, and accuracy. Features like Model Distillation, Prompt caching, and Intelligent Prompt Routing can reduce expenses while maintaining performance. For example, distilled models run up to 500% faster and cost up to 75% less, with minimal impact on accuracy. Intelligent Prompt Routing can cut costs by up to 30% while maintaining quality. With flexible options for both real-time and batch processing, Bedrock helps you build smart, efficient, and cost-effective AI systems."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 7,
        "cited_text": "In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents. What are agents? \"Agent\" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems , but draw an important architectural distinction between workflows and agents :"
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 8,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 9,
        "cited_text": "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough. When and how to use frameworks There are many frameworks that make agentic systems easier to implement, including: The Claude Agent SDK ; Strands Agents SDK by AWS ; Rivet , a drag and drop GUI LLM workflow builder; and Vellum , another GUI tool for building and testing complex workflows."
      },
      {
        "source_id": "141802c7-ba51-4375-a7a4-2814284bfbb9",
        "citation_number": 10,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. If you're looking to quickly build agents with LangChain's create_agent (built on LangGraph), check out the LangChain Agents documentation ."
      },
      {
        "source_id": "141802c7-ba51-4375-a7a4-2814284bfbb9",
        "citation_number": 11,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 12,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 13,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 14,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "3454bfd3-bc2c-45d1-9e33-715a54b1c0ff",
        "citation_number": 15,
        "cited_text": "View PDF Abstract: Engineering knowledge-based (or expert) systems require extensive manual effort and domain knowledge. As Large Language Models (LLMs) are trained using an enormous amount of cross-domain knowledge, it becomes possible to automate such engineering processes. This paper presents an empirical automation and semi-automation framework for domain knowledge distillation using prompt engineering and the LLM ChatGPT. We assess the framework empirically in the autonomous driving domain and present our key observations. In our implementation, we construct the domain knowledge ontology by \"chatting\" with ChatGPT. The key finding is that while fully automated domain ontology construction is possible, human supervision and early intervention typically improve efficiency and output quality as they lessen the effects of response randomness and the butterfly effect. We, therefore, also develop a web-based distillation assistant enabling supervision and flexible intervention at runtime. We hope our findings and tools could inspire future research toward revolutionizing the engineering of knowledge-based systems across application domains."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 16,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "2b834573-7bf4-47b0-a389-bbd63ac12b5a",
        "citation_number": 17,
        "cited_text": "Securely customize with your data Move from generic AI to AI that knows your customer and your business by customizing models with your data. By combining multiple data customization tools—Knowledge Bases, Bedrock Data Automation, prompt engineering, and fine-tuning—you can optimize your AI applications to your business, while ensuring you're always in control of sensitive information. Learn more about customization Apply security, privacy, and responsible AI checks Amazon Bedrock provides industry-leading security, privacy, and compliance for generative AI applications. Bedrock Guardrails can help block up to 88% of harmful content and identify correct model responses with up to 99% accuracy to minimize hallucinations and data ambiguity using Automated Reasoning checks. Bedrock never stores or uses your data to train models, ensuring complete security and privacy, with encryption of data in transit and at rest, as well as identity-based policies for managing data access. Bedrock provides comprehensive monitoring and logging capabilities that can support your governance and audit requirements. Finally, Bedrock is in scope for common compliance standards including ISO, SOC, CSA STAR Level 2, GDPR, FedRAMP High, and is HIPAA eligible."
      },
      {
        "source_id": "62ec4664-8c3b-4f49-8649-0a7815f98bf1",
        "citation_number": 18,
        "cited_text": "Our utterance vector space also integrates with Pinecone and Qdrant ! 📚 Resources Docs <cited_table>",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Notebook",
              "Description"
            ],
            [
              "Introduction",
              "Introduction to Semantic Router and static routes"
            ],
            [
              "Dynamic Routes",
              "Dynamic routes for parameter generation and functionc calls"
            ],
            [
              "Save/Load Layers",
              "How to save and load"
            ],
            [
              "LangChain Integration",
              "How to integrate Semantic Router with LangChain Agents"
            ],
            [
              "Local Execution",
              "Fully local Semantic Router with dynamic routes —"
            ],
            [
              "Route Optimization",
              "How to train route layer thresholds to optimize performance"
            ],
            [
              "Multi-Modal Routes",
              "Using multi-modal routes to identify Shrek vs. not-Shrek pictures"
            ]
          ]
        }
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 19,
        "cited_text": "Combining and customizing these patterns These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity only when it demonstrably improves outcomes. Summary Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."
      },
      {
        "source_id": "38eac028-33e1-461a-94fe-bd31488694f8",
        "citation_number": 20,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      }
    ]
  }
}
