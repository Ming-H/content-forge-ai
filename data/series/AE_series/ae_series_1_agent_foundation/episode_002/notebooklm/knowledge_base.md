# 知识库：LLM 作为 Agent 大脑：模型能力边界与选型策略

生成时间: 2026-04-03 09:34
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "根据提供的来源，关于「LLM 作为 Agent 大脑：模型能力边界与选型策略」的核心技术架构和关键组件，可以概述如下：\n\n### 1. 核心技术架构与关键组件\nAI Agent 被定义为一种**自动化推理和决策引擎** [1]。其核心架构通常被视为以 LLM 作为“大脑”，通过以下关键组件协同工作：\n*   **规划 (Planning)**：将复杂问题拆解为更小的子问题，并制定任务执行路径 [1, 2]。\n*   **记忆 (Memory)**：存储已完成的任务和历史交互信息，以便维持长期上下文和状态管理 [1, 3]。\n*   **工具使用/执行 (Tool Use/Execution)**：选择并调用外部 API 或工具（如搜索、计算、代码执行等）来获取实时数据或执行现实动作 [1, 4, 5]。\n*   **架构模式**：包括**单智能体 (Single-Agent)** 和**多智能体 (Multi-Agent)** 模式，后者通过编排多个专家智能体协作来处理复杂任务 [6, 7]。\n\n### 2. 技术演进路线\n技术演进呈现出从单一工具调用向全面智能体化发展的趋势：\n*   **从工具增强到智能体导向**：早期研究侧重于**工具增强型学习**（Tool-augmented），即工具辅助模型；现在转向**工具导向型学习**（Tool-oriented），模型自主学习如何分解任务、推理规划并选择工具 [2]。\n*   **评测标准演进**：以 Berkeley Function Calling Leaderboard (BFCL) 为例，演进路线为：**V1 (AST 评测)** -> **V2 (企业与开源工具)** -> **V3 (多轮交互)** -> **V4 (全面智能体化评估)**，增加了对 Web 搜索、记忆管理和格式敏感度的考核 [3, 8]。\n\n### 3. 核心算法与机制名称\n*   **函数调用 (Function Calling/Tool Calling)**：LLM 接口的核心机制，使模型能返回结构化 JSON 建议以驱动外部功能 [9, 10]。\n*   **ReAct (Reason + Act)**：一种经典的智能体工作流，通过结合推理和行动来解决复杂任务 [11, 12]。\n*   **思维链 (CoT, Chain-of-Thought)**：在推理模型（如 GPT-5 或 o3 系列）中广泛应用，用于增强规划和解决复杂逻辑问题的能力 [13, 14]。\n*   **RAFT (Retrieval-Augmented Fine-Tuning)**：用于增强模型在特定领域内 RAG 和 API 调用的准确性，减少幻觉 [3, 15]。\n*   **结构化输出 (Structured Outputs)**：确保模型生成的响应严格遵循 JSON Schema，提高类型安全性和系统可靠性 [16, 17]。\n\n### 4. 主要架构模式\n*   **响应-执行循环 (Agentic Loop)**：模型确定调用工具 -> 应用执行操作 -> 结果反馈给模型 -> 模型生成最终响应 [5, 18]。\n*   **分层与可扩展设计**：如 AutoGen 的架构，分为 Core API（事件驱动、消息传递）、AgentChat API（快速原型开发）和 Extensions API（集成特定 LLM 客户端） [19]。\n*   **多智能体编排 (Multi-Agent Orchestration)**：利用专家分工模式，例如由一个“研究员”智能体和一个“写作”智能体协作生成报告 [6, 20]。\n\n### 5. 关键技术指标 (选型策略依据)\n在进行模型选型时，通常依据以下指标：\n*   **总体准确率 (Overall Accuracy)**：反映模型在单轮、多轮及各类工具调用场景下的综合表现 [21, 22]。\n*   **幻觉率 (Hallucination Measurement)**：衡量模型在面对无法处理的请求时是否会错误地“捏造”工具调用 [21, 23]。\n*   **上下文窗口 (Context Window)**：模型在一次对话中能处理的最大 Token 数量，限制了智能体可调用的工具描述和记忆长度 [24, 25]。\n*   **延迟与成本 (Latency & Cost)**：在生产环境中，每 1000 个 Token 的费用以及推理速度是选型的决定性因素 [3, 21, 26]。\n*   **格式敏感度 (Format Sensitivity)**：模型对不同输入格式（如 JSON、Pydantic、Zod）的一致性表现 [21, 27]。",
    "conversation_id": "f97c9bd5-b5bd-40d9-b4c7-5f7173fd585f",
    "sources_used": [
      "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "f3cba5cb-ea4c-4dcb-90b0-8a28817ee32c",
      "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "e9400d2f-22c2-476b-8bfa-292662063768",
      "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "9bc01691-b449-4949-a89a-dbfdc4896811",
      "23d4ae25-c078-4c24-825f-676b34bd530d",
      "5d860664-3c42-434c-85d9-52ba7b008def",
      "2db39851-e74c-4170-ac46-8b20063363d5",
      "f1862034-f162-453c-bd4e-28a714de736c",
      "3a08567b-3003-4501-94a1-7a0d3b200873"
    ],
    "citations": {
      "1": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "2": "f3cba5cb-ea4c-4dcb-90b0-8a28817ee32c",
      "3": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "4": "e9400d2f-22c2-476b-8bfa-292662063768",
      "5": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "6": "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "7": "9bc01691-b449-4949-a89a-dbfdc4896811",
      "8": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "9": "e9400d2f-22c2-476b-8bfa-292662063768",
      "10": "5d860664-3c42-434c-85d9-52ba7b008def",
      "11": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "12": "2db39851-e74c-4170-ac46-8b20063363d5",
      "13": "5d860664-3c42-434c-85d9-52ba7b008def",
      "14": "f1862034-f162-453c-bd4e-28a714de736c",
      "15": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "16": "f1862034-f162-453c-bd4e-28a714de736c",
      "17": "f1862034-f162-453c-bd4e-28a714de736c",
      "18": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "19": "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "20": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "21": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "22": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "23": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "24": "3a08567b-3003-4501-94a1-7a0d3b200873",
      "25": "3a08567b-3003-4501-94a1-7a0d3b200873",
      "26": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "27": "f1862034-f162-453c-bd4e-28a714de736c"
    },
    "references": [
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 1,
        "cited_text": "Install MCP Server MCP Docs Copy MCP URL Install in Cursor Copy Claude Code command Copy Codex config LlamaIndex Framework Use Cases Agents Copy Markdown Open in Claude Open in ChatGPT Open in Cursor Copy Markdown View as Markdown Agents An “agent” is an automated reasoning and decision engine. It takes in a user input/query and can make internal decisions for executing that query in order to return the correct result. The key agent components can include, but are not limited to: Breaking down a complex question into smaller ones Choosing an external Tool to use + coming up with parameters for calling the Tool Planning out a set of tasks Storing previously completed tasks in a memory module"
      },
      {
        "source_id": "f3cba5cb-ea4c-4dcb-90b0-8a28817ee32c",
        "citation_number": 2,
        "cited_text": "View a PDF of the paper titled Tool Learning with Foundation Models, by Yujia Qin and 40 other authors View PDF HTML (experimental) Abstract: Humans possess an extraordinary ability to create and utilize tools, allowing them to overcome physical limitations and explore new frontiers. With the advent of foundation models, AI systems have the potential to be equally adept in tool use as humans. This paradigm, i.e., tool learning with foundation models, combines the strengths of specialized tools and foundation models to achieve enhanced accuracy, efficiency, and automation in problem-solving. Despite its immense potential, there is still a lack of a comprehensive understanding of key challenges, opportunities, and future endeavors in this field. To this end, we present a systematic investigation of tool learning in this paper. We first introduce the background of tool learning, including its cognitive origins, the paradigm shift of foundation models, and the complementary roles of tools and models. Then we recapitulate existing tool learning research into tool-augmented and tool-oriented learning. We formulate a general tool learning framework: starting from understanding the user instruction, models should learn to decompose a complex task into several subtasks, dynamically adjust their plan through reasoning, and effectively conquer each sub-task by selecting appropriate tools. We also discuss how to train models for improved tool-use capabilities and facilitate the generalization in tool learning. Considering the lack of a systematic tool learning evaluation in prior works, we experiment with 18 representative tools and show the potential of current foundation models in skillfully utilizing tools. Finally, we discuss several open problems that require further investigation for tool learning. In general, we hope this paper could inspire future research in integrating tools with foundation models."
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 3,
        "cited_text": "Repository files navigation README Apache-2.0 license Gorilla: Large Language Model Connected with Massive APIs Latest Updates 📢 Check out our detailed Berkeley Function Calling Leaderboard changelog (Last updated: ) for the latest dataset / model updates to the Berkeley Function Calling Leaderboard! 🤖 [07/17/2025] Announcing BFCL V4 Agentic! As function-calling forms the bedrock of Agentic systems, BFCL V4 Agentic benchmark focuses on tool-calling in real-world agentic settings, featuring web search with multi-hop reasoning and error recovery, agent memory management, and format sensitivity evaluation. [ Web-search Blog ] [ Memory Blog ] [ Format Sensitivity Blog ] [ PR ] [ Tweet ] 🎯 [10/04/2024] Introducing the Agent Arena by Gorilla X LMSYS Chatbot Arena! Compare different agents in tasks like search, finance, RAG, and beyond. Explore which models and tools work best for specific tasks through our novel ranking system and community-driven prompt hub. [ Blog ] [ Arena ] [ Leaderboard ] [ Dataset ] [ Tweet ] 📣 [09/21/2024] Announcing BFCL V3 - Evaluating multi-turn and multi-step function calling capabilities! New state-based evaluation system tests models on handling complex workflows, sequential functions, and service states. [ Blog ] [ Leaderboard ] [ Code ] [ Tweet ] 🚀 [08/20/2024] Released BFCL V2 • Live! The Berkeley Function-Calling Leaderboard now features enterprise-contributed data and real-world scenarios. [ Blog ] [ Live Leaderboard ] [ V2 Categories Leaderboard ] [ Tweet ] ⚡ [04/12/2024] Excited to release GoEx - a runtime for LLM-generated actions like code, API calls, and more. Featuring \"post-facto validation\" for assessing LLM actions after execution, \"undo\" and \"damage confinement\" abstractions to manage unintended actions & risks. This paves the way for fully autonomous LLM agents, enhancing interaction between apps & services with human-out-of-loop. [ Blog ] [ Code ] [ Paper ] [ Tweet ] ⏰ [04/01/2024] Introducing cost and latency metrics into Berkeley function calling leaderboard ! 🚀 [03/15/2024] RAFT: Adapting Language Model to Domain Specific RAG is live! [ MSFT-Meta blog ] [ Berkeley Blog ] 🏆 [02/26/2024] Berkeley Function Calling Leaderboard is live! 🎯 [02/25/2024] OpenFunctions v2 sets new SoTA for open-source LLMs! 🔥 [11/16/2023] Excited to release Gorilla OpenFunctions 💻 [06/29/2023] Released gorilla-cli , LLMs for your CLI! 🟢 [06/06/2023] Released Commercially usable, Apache 2.0 licensed Gorilla models 🚀 [05/30/2023] Provided the CLI interface to chat with Gorilla! 🚀 [05/28/2023] Released Torch Hub and TensorFlow Hub Models! 🚀 [05/27/2023] Released the first Gorilla model! or 🤗 ! 🔥 [05/27/2023] We released the APIZoo contribution guide for community API contributions! 🔥 [05/25/2023] We release the APIBench dataset and the evaluation code of Gorilla!"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 4,
        "cited_text": "Function calling lets you connect models to external tools and APIs. Instead of generating text responses, the model determines when to call specific functions and provides the necessary parameters to execute real-world actions. This allows the model to act as a bridge between natural language and real-world actions and data. Function calling has 3 primary use cases: Augment Knowledge: Access information from external sources like databases, APIs, and knowledge bases. Extend Capabilities: Use external tools to perform computations and extend the limitations of the model, such as using a calculator or creating charts. Take Actions: Interact with external systems using APIs, such as scheduling appointments, creating invoices, sending emails, or controlling smart home devices."
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 5,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "b717658c-57b7-4b5b-9367-7bd1fd456082",
        "citation_number": 6,
        "cited_text": "Warning : Only connect to trusted MCP servers as they may execute commands in your local environment or expose sensitive information. Multi-Agent Orchestration You can use AgentTool to create a basic multi-agent orchestration setup. For more advanced multi-agent orchestrations and workflows, read AgentChat documentation . AutoGen Studio Use AutoGen Studio to prototype and run multi-agent workflows without writing code. Caution : AutoGen Studio is meant to help you rapidly prototype multi-agent workflows and demonstrate an example of end user interfaces built with AutoGen. It is not meant to be a production-ready app . Developers are encouraged to use the AutoGen framework to build their own applications, implementing authentication, security and other features required for deployed applications. See the security note for more details."
      },
      {
        "source_id": "9bc01691-b449-4949-a89a-dbfdc4896811",
        "citation_number": 7,
        "cited_text": "Computer Science > Artificial Intelligence arXiv:2404.11584 (cs) [Submitted on 17 Apr 2024] Title: The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey Authors: Tula Masterman , Sandi Besen , Mason Sawtell , Alex Chao View a PDF of the paper titled The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey, by Tula Masterman and 3 other authors View PDF HTML (experimental) Abstract: This survey paper examines the recent advancements in AI agent implementations, with a focus on their ability to achieve complex goals that require enhanced reasoning, planning, and tool execution capabilities. The primary objectives of this work are to a) communicate the current capabilities and limitations of existing AI agent implementations, b) share insights gained from our observations of these systems in action, and c) suggest important considerations for future developments in AI agent design. We achieve this by providing overviews of single-agent and multi-agent architectures, identifying key patterns and divergences in design choices, and evaluating their overall impact on accomplishing a provided goal. Our contribution outlines key themes when selecting an agentic architecture, the impact of leadership on agent systems, agent communication styles, and key phases for planning, execution, and reflection that enable robust AI agent systems."
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 8,
        "cited_text": "Berkeley Function Calling Leaderboard (BFCL) V4 Home Blog Try it Out! Leaderboard Berkeley Function-Calling Leaderboard BFCL: From Tool Use to Agentic Evaluation of Large Language Models The Berkeley Function Calling Leaderboard (BFCL) V4 evaluates the LLM's ability to call functions (aka tools) accurately. This leaderboard consists of real-world data and will be updated periodically. For more information on the evaluation dataset and methodology, please refer to our blogs: BFCL-v1 introducing AST as an evaluation metric, BFCL-v2 introducing enterprise and OSS-contributed functions, BFCL-v3 introducing multi-turn interactions, and BFCL-v4 introducing holistic agentic evaluation. Checkout code and data ."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 9,
        "cited_text": "Define function declaration: Define the function declaration in your application code. Function Declarations describe the function's name, parameters, and purpose to the model. Call API with function declarations: Send user prompt along with the function declaration(s) to the model. It analyzes the request and determines if a function call would be helpful. If so, it responds with a structured JSON object containing the function name, arguments, and a unique id (this id is now always returned by the API for Gemini 3 models * ). Execute function code (your responsibility): The Model doesn't execute the function itself. It's your application's responsibility to process the response and check for a function call. If Yes : Extract the name, args, and id of the function and execute the corresponding function in your application. No: The model has provided a direct text response to the prompt (this flow is less emphasized in the example but is a possible outcome). Create user friendly response: If a function was executed, capture the result and send it back to the model, ensuring you include the matching id , in a subsequent turn of the conversation. It will use the result to generate a final, user-friendly response that incorporates the information from the function call."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 10,
        "cited_text": "Responses Copy Page More page actions Function calling Give models access to new functionality and data they can use to follow instructions and respond to prompts. Function calling (also known as tool calling ) provides a powerful and flexible way for OpenAI models to interface with external systems and access data outside their training data. This guide shows how you can connect a model to data and actions provided by your application. We'll show how to use function tools (defined by a JSON schema) and custom tools which work with free form text inputs and outputs."
      },
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 11,
        "cited_text": "Resources Section titled “Resources” Prebuilt Agents and Tools The following component guides are the central hubs for getting started in building with agents: Agents Tools Custom Agentic Workflows LlamaIndex Workflows allow you to build very custom, agentic workflows through a core event-driven orchestration foundation. Workflows Documentation Building a ReAct agent workflow Deploying Workflows Building with Agentic Ingredients If you want to leverage core agentic ingredients in your workflow, LlamaIndex has robust abstractions for every agent sub-ingredient."
      },
      {
        "source_id": "2db39851-e74c-4170-ac46-8b20063363d5",
        "citation_number": 12,
        "cited_text": "3. Prompt IDE : Intuitive interface for crafting prompts, comparing model performance, and adding additional features such as text-to-speech to a chat-based app. 4. RAG Pipeline : Extensive RAG capabilities that cover everything from document ingestion to retrieval, with out-of-box support for text extraction from PDFs, PPTs, and other common document formats. 5. Agent capabilities : You can define agents based on LLM Function Calling or ReAct, and add pre-built or custom tools for the agent. Dify provides 50+ built-in tools for AI agents, such as Google Search, DALL· E, Stable Diffusion and WolframAlpha."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 13,
        "cited_text": "Complete tool calling example python Complete tool calling example python Note that for reasoning models like GPT-5 or o4-mini, any reasoning items returned in model responses with tool calls must also be passed back with tool call outputs. Defining functions Functions are usually declared in the tools parameter of each API request. With tool search , your application can also load deferred functions later in the interaction. Either way, each callable function uses the same schema shape. A function definition has the following properties:"
      },
      {
        "source_id": "f1862034-f162-453c-bd4e-28a714de736c",
        "citation_number": 14,
        "cited_text": "<cited_table> Examples Chain of thought Structured data extraction UI generation Moderation Chain of thought Chain of thought You can ask the model to output an answer in a structured, step-by-step way, to guide the user through the solution.",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "",
              "Structured Outputs",
              "JSON Mode"
            ],
            [
              "Outputs valid JSON",
              "Yes",
              "Yes"
            ],
            [
              "Adheres to schema",
              "Yes (see",
              "No"
            ],
            [
              "Compatible models",
              "gpt-4o-mini",
              "gpt-3.5-turbo"
            ],
            [
              "Enabling",
              "text: { format: { type: \"json_schema\", \"strict\": true, \"schema\": ... } }",
              "text: { format: { type: \"json_object\" } }"
            ]
          ]
        }
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 15,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "f1862034-f162-453c-bd4e-28a714de736c",
        "citation_number": 16,
        "cited_text": "Copy Page More page actions Responses Copy Page More page actions Structured model outputs Ensure text responses from the model adhere to a JSON schema you define. JSON is one of the most widely used formats in the world for applications to exchange data. Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema , so you don't need to worry about the model omitting a required key, or hallucinating an invalid enum value. Some benefits of Structured Outputs include:"
      },
      {
        "source_id": "f1862034-f162-453c-bd4e-28a714de736c",
        "citation_number": 17,
        "cited_text": "The remainder of this guide will focus on non-function calling use cases in the Chat Completions API. To learn more about how to use Structured Outputs with function calling, check out the Function Calling guide. The remainder of this guide will focus on non-function calling use cases in the Responses API. To learn more about how to use Structured Outputs with function calling, check out the Function Calling guide. Structured Outputs vs JSON mode Structured Outputs is the evolution of JSON mode . While both ensure valid JSON is produced, only Structured Outputs ensure schema adherence. Both Structured Outputs and JSON mode are supported in the Responses API, Chat Completions API, Assistants API, Fine-tuning API and Batch API."
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 18,
        "cited_text": "These token counts are added to your normal input and output tokens to calculate the total cost of a request. Refer to the models overview table for current per-model prices. When you send a tool use prompt, just like any other API request, the response will output both input and output token counts as part of the reported usage metrics. Next steps Choose your path Understand the concepts Where tools run, how the loop works, and when to use tools. Build step by step The tutorial: from a single tool call to production."
      },
      {
        "source_id": "b717658c-57b7-4b5b-9367-7bd1fd456082",
        "citation_number": 19,
        "cited_text": "Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components. Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 20,
        "cited_text": "Agentic RAG : Build a context-augmented research assistant over your data that not only answers simple questions, but complex research tasks. Our getting started guide is a great place to start. Report Generation : Generate a multimodal report using a multi-agent researcher + writer workflow + LlamaParse. Notebook . Customer Support : Check out starter template for building a multi-agent concierge with workflows . Others: Productivity Assistant : Build an agent that can operate over common workflow tools like email, calendar. Check out our GSuite agent tutorial . Coding Assistant : Build an agent that can operate over code. Check out our code interpreter tutorial ."
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 21,
        "cited_text": "| ||| | Agentic || Multi Turn | Single Turn || Hallucination Measurement || Format Sensitivity || | || | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | ||| | Web Search | Memory | Multi turn | Non-live (AST) | Live (AST) | || || Latency (s) | || | Rank 🔼 | Overall Acc | Model | Cost ($) | Overall Acc | Base | No Snippet | Overall Acc | KV | Vector | Recursive Sum | Overall Acc | Base | Miss Func | Miss Param | Long Context | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Relevance | Irrelevance | Max Delta | SD | Mean | SD | P95 | Organization | License | | 1 | 77.47 | Claude-Opus-4-5-20251101 (FC) | 86.55 | 84.5 | 84 | 85 | 73.76 | 70.97 | 72.9 | 77.42 | 68.38 | 81 | 64 | 58 | 70.5 | 88.58 | 76.83 | 95.5 | 93.5 | 88.5 | 79.79 | 86.43 | 78.16 | 87.5 | 75 | 62.5 | 84.72 | N/A | N/A | 4.38 | 3.13 | 7.56 | Anthropic | Proprietary | | 2 | 73.24 | Claude-Sonnet-4-5-20250929 (FC) | 43.73 | 81 | 82 | 80 | 64.95 | 54.19 | 57.42 | 83.23 | 61.37 | 69 | 65 | 52.5 | 59 | 88.65 | 72.58 | 95.5 | 94.5 | 92 | 81.13 | 89.53 | 78.92 | 87.5 | 83.33 | 68.75 | 86.61 | N/A | N/A | 4.31 | 4.43 | 7.27 | Anthropic | Proprietary | | 3 | 72.51 | Gemini-3-Pro-Preview (Prompt) | 298.47 | 80 | 78 | 82 | 61.72 | 59.35 | 62.58 | 63.23 | 60.75 | 64.5 | 60 | 54.5 | 64 | 90.65 | 79.58 | 96 | 95 | 92 | 83.12 | 87.6 | 81.77 | 93.75 | 87.5 | 68.75 | 85.59 | 8.5 | 1.7 | 12.08 | 21.3 | 32.73 | Google | Proprietary | | 4 | 72.38 | GLM-4.6 (FC thinking) | 4.64 | 77.5 | 79 | 76 | 55.7 | 43.87 | 56.13 | 67.1 | 68 | 74.5 | 68 | 63 | 66.5 | 87.56 | 74.25 | 95 | 91.5 | 89.5 | 80.9 | 89.53 | 78.92 | 81.25 | 75 | 75 | 84.96 | N/A | N/A | 4.34 | 7.22 | 13.5 | Zhipu AI | MIT | | 5 | 69.57 | Grok-4-1-fast-reasoning (FC) | 17.26 | 82.5 | 82 | 83 | 53.98 | 41.29 | 57.42 | 63.23 | 58.87 | 70.5 | 59.5 | 43 | 62.5 | 88.27 | 77.58 | 93 | 92.5 | 90 | 78.46 | 84.11 | 77.3 | 75 | 70.83 | 81.25 | 79.43 | N/A | N/A | 6.74 | 12.78 | 17.57 | xAI | Proprietary | | 6 | 68.7 | Claude-Haiku-4-5-20251001 (FC) | 14.23 | 83.5 | 86 | 81 | 54.41 | 51.61 | 55.48 | 56.13 | 53.62 | 63.5 | 42.5 | 52.5 | 56 | 86.5 | 71 | 94 | 92.5 | 88.5 | 78.68 | 83.72 | 77.59 | 75 | 75 | 62.5 | 85.11 | N/A | N/A | 1.68 | 3.92 | 3.15 | Anthropic | Proprietary | | 7 | 68.14 | Gemini-3-Pro-Preview (FC) | 224.69 | 68.5 | 63 | 74 | 54.84 | 50.32 | 63.23 | 50.97 | 63.12 | 69 | 63 | 56.5 | 64 | 85.75 | 75.5 | 94 | 91 | 82.5 | 81.72 | 87.6 | 80.44 | 75 | 79.17 | 75 | 77.85 | N/A | N/A | 15.87 | 41.41 | 58.48 | Google | Proprietary | | 8 | 63.05 | o3-2025-04-16 (Prompt) | 234.64 | 50.5 | 51 | 50 | 51.83 | 33.55 | 50.32 | 71.61 | 62.25 | 68 | 63.5 | 54.5 | 63 | 81.94 | 74.25 | 89 | 86.5 | 78 | 73.21 | 83.33 | 70.75 | 75 | 70.83 | 93.75 | 83.98 | 8.5 | 2.75 | 4.83 | 7.01 | 11.7 | OpenAI | Proprietary | | 9 | 62.97 | Grok-4-0709 (Prompt) | 348.19 | 74 | 74 | 74 | 50.54 | 43.87 | 59.35 | 48.39 | 47 | 55.5 | 46 | 36 | 50.5 | 82.75 | 67 | 93.5 | 89 | 81.5 | 72.54 | 81.78 | 70.18 | 81.25 | 70.83 | 81.25 | 84.3 | 13.0 | 2.88 | 30.38 | 36.19 | 101.54 | xAI | Proprietary | | 10 | 61.38 | Grok-4-0709 (FC) | 355.17 | 82 | 80 | 84 | 55.91 | 57.42 | 58.71 | 51.61 | 33.88 | 44 | 19 | 28.5 | 44 | 85.38 | 73.5 | 92.5 | 88.5 | 87 | 75.57 | 82.17 | 73.88 | 75 | 79.17 | 87.5 | 75.4 | N/A | N/A | 15.49 | 26.22 | 44.28 | xAI | Proprietary | | 11 | 59.06 | Moonshotai-Kimi-K2-Instruct (FC) | 6.19 | 66.5 | 72 | 61 | 29.03 | 21.94 | 20 | 45.16 | 50.63 | 62 | 41 | 44.5 | 55 | 81.6 | 69.42 | 92 | 82 | 83 | 78.68 | 81.78 | 78.06 | 87.5 | 66.67 | 75 | 87.34 | N/A | N/A | 6.4 | 9.38 | 13.78 | MoonshotAI | modified-mit | | 12 | 58.29 | Grok-4-1-fast-non-reasoning (FC)"
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 22,
        "cited_text": "FC = native support for function/tool calling. Prompt = walk-around for function calling, using model's normal text generation capability. Cost is calculated as an estimate of the cost for the entire benchmark, in USD. Latency is measured in seconds. Overall Accuracy is the unweighted average of all the sub-categories. For details on score composition, please refer to our blog . Format sensitivity test cases are only supported for prompt (non-FC) models. Click on column header to sort. If you would like to add your model or contribute test-cases, please contact us via discord ."
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 23,
        "cited_text": "• Retrieval-augmented training for test-time adaptation Gorilla OpenFunctions-V2 🤖 Model Drop-in alternative for function calling, supporting multiple complex data types and parallel execution • Multiple & parallel function execution with OpenAI-compatible endpoints • Native support for Python, Java, JavaScript, and REST APIs with expanded data types • Function relevance detection to reduce hallucinations • Enhanced RESTful API formatting capabilities • State-of-the-art performance among open-source models Berkeley Function Calling Leaderboard (BFCL)"
      },
      {
        "source_id": "3a08567b-3003-4501-94a1-7a0d3b200873",
        "citation_number": 24,
        "cited_text": "官方 Java SDK 企业级 Java 开发工具包，支持高并发和高可用性 OpenAI SDK 兼容 兼容 OpenAI SDK，零学习成本快速迁移现有应用 LangChain 集成 集成 LangChain 框架，构建复杂的 AI 应用和智能代理 核心概念 GLM Token 上下文窗口 GLM - General Language Model GLM 是一款基于自回归填空的预训练语言模型。ChatGLM 系列模型，支持相对复杂的自然语言指令，并且能够解决困难的推理类问题。该模型配备了易于使用的 API 接口，允许开发者轻松将其融入各类应用，广泛应用于智能客服、虚拟主播、聊天机器人等诸多领域。 Token - 文本处理单位 Token 是模型用来表示自然语言文本的基本单位，可以直观的理解为“字”或“词”；通常 1 个中文词语、1 个英文单词、1 个数字或 1 个符号计为 1 个 token。 GLM 系列模型中 token 和字数的换算比例约为 1:1.6 ，但因为不同模型的分词不同，所以换算比例也存在差异，每一次实际处理 token 数量以模型返回为准，您可以从返回结果的 usage 中查看。"
      },
      {
        "source_id": "3a08567b-3003-4501-94a1-7a0d3b200873",
        "citation_number": 25,
        "cited_text": "Context Window - 上下文窗口 上下文窗口是指模型在一次对话中能够处理的最大长度。包括： 用户输入的内容 模型生成的回复 模型在生成回复过程中进行推理或调用工具时产生的中间内容（如：GLM-4-AllTools ） 如果超出上下文窗口限制，会发生什么？ 超出部分被截断： 如果总文本量超过了上下文窗口的限制，超出的部分将被自动丢弃，无法被处理。 影响对话内容： 你可能看不到被丢弃的部分，从而影响模型的回答质量或上下文的连贯性。"
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 26,
        "cited_text": "Tool use examples For a complete hands-on walkthrough, see the tutorial . For reference examples of individual concepts, see Define tools and Handle tool calls . What happens when Claude needs more information Pricing Tool use requests are priced based on: The total number of input tokens sent to the model (including in the tools parameter) The number of output tokens generated For server-side tools, additional usage-based pricing (e.g., web search charges per search performed) Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage."
      },
      {
        "source_id": "f1862034-f162-453c-bd4e-28a714de736c",
        "citation_number": 27,
        "cited_text": "Reliable type-safety: No need to validate or retry incorrectly formatted responses Explicit refusals: Safety-based model refusals are now programmatically detectable Simpler prompting: No need for strongly worded prompts to achieve consistent formatting In addition to supporting JSON Schema in the REST API, the OpenAI SDKs for Python and JavaScript also make it easy to define object schemas using Pydantic and Zod respectively. Below, you can see how to extract information from unstructured text that conforms to a schema defined in code."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「LLM 作为 Agent 大脑」的实现逻辑是基于将模型从简单的文本生成器转变为**自动化推理与决策引擎** [1]。其核心在于模型如何感知用户需求、规划路径并调度外部工具 [1, 2]。\n\n以下是基于来源的详细技术实现细节：\n\n### 1. 核心算法流程\nAgent 的运作遵循一个结构化的**响应-执行循环 (Agentic Loop)** [3, 4]：\n*   **规划与拆解 (Planning)**：Agent 接收复杂指令，将其拆解为子任务或规划任务集 [1]。\n*   **工具发现与调用 (Tool Calling)**：\n    *   **步骤1：定义声明**：开发者在应用中定义函数名、参数 schema（通常符合 OpenAPI 规范）和详细描述 [5-7]。\n    *   **步骤2：模型决策**：LLM 分析 prompt，决定是否需要调用工具。若需要，它会返回一个包含函数名和结构化参数的 JSON 对象（及唯一 `call_id`）[5, 8, 9]。\n    *   **步骤3：客户端执行**：应用程序提取 LLM 建议，执行实际代码逻辑，并获取结果 [5, 10]。\n*   **结果反馈与迭代**：将工具执行结果发回模型。模型据此生成最终回复，或启动下一轮工具调用（如**组合式/顺序调用**）[3, 5, 11]。\n*   **推理模式**：现代模型（如 Gemini 3, GPT-5 系列）集成了**思维链 (CoT)** 或**深度思考 (Thinking)** 机制，利用内部推理过程来提高决策的准确性 [12-14]。\n\n### 2. 关键代码架构模式\n目前主流框架（如 AutoGen, LlamaIndex, LangChain）采用分层设计：\n*   **事件驱动层 (Core API)**：实现智能体间的消息传递、状态管理和分布式运行环境 [15]。\n*   **编排层 (AgentChat/Workflows)**：提供高级 API 用于快速原型开发，支持多智能体协作（如研究员+写作者工作流）[15, 16]。\n*   **扩展层 (Extensions/Tools)**：集成特定的 LLM 客户端、外部 API、代码解释器或 MCP（模型上下文协议）服务器 [15, 17]。\n*   **记忆管理**：包含短期对话历史和长期向量存储（Memory Module），确保跨任务的上下文连贯性 [1, 18]。\n\n### 3. 性能优化策略\n为解决延迟、成本和准确性问题，业界采用了以下策略：\n*   **Prompt Caching（提示词缓存）**：Anthropic 等厂商支持缓存重复的系统提示或工具定义，大幅降低推理延迟和 token 成本 [19, 20]。\n*   **Tool Search（工具搜索）**：当 API 数量极其庞大时，不将所有 schema 塞入上下文，而是使用工具搜索（如 `tool_search` 机制）根据需要动态加载相关工具，节省 token [21-23]。\n*   **RAFT (Retrieval-Augmented Fine-Tuning)**：针对特定领域 API 进行微调，使模型学会从干扰文档中提取正确参数，减少幻觉并提升 RAG 任务的可靠性 [24, 25]。\n*   **严格模式 (Strict Mode)**：通过 `strict: true` 强制模型输出严格遵循 JSON Schema，提高类型安全性并降低因格式错误导致的任务失败 [26-28]。\n\n### 4. 竞品技术对比与性能参数 (BFCL V4 数据)\n根据 **Berkeley Function Calling Leaderboard (BFCL) V4** 的最新评测，各家模型在 Agent 能力边界上的表现存在差异 [18, 29]：\n\n| 模型 | 总体准确率 (%) | 延迟 (s, Mean) | 成本 (Benchmark 估算 $) | 幻觉率测算 (%) |\n| :--- | :--- | :--- | :--- | :--- |\n| **Claude-Opus-4-5** (FC) | **77.47** | 4.38 | 86.55 | 84.72 |\n| **Gemini-3-Pro-Preview** | 72.51 | 12.08 | 298.47 | 85.59 |\n| **GLM-4.6** (Zhipu AI) | 72.38 | 4.34 | **4.64** | **84.96** |\n| **Grok-4-1-fast-reasoning**| 69.57 | 6.74 | 17.26 | 79.43 |\n| **o3-2025-04-16** (Prompt)| 63.05 | 4.83 | 234.64 | 83.98 |\n| **DeepSeek-V3.2-Exp** | 56.73 | 37.89 | 57.75 | 67.00 |\n\n**关键发现：**\n*   **能力阶梯**：Claude-Opus 4.5 在总体准确率、单轮及多轮调用场景中位居榜首 [18]。\n*   **性价比分化**：**GLM-4.6** 以极低的成本（$4.64）实现了与顶级 Proprietary 模型相近的准确率（72.38%）和优秀的幻觉控制 [18]。\n*   **推理权衡**：具有深度思考能力的推理模型（如 o3, Gemini-3, GLM-4.6 thinking）在处理复杂逻辑和参数提取时更稳健，但部分模型（如 DeepSeek）的平均延迟显著更高 [18, 30]。\n*   **格式敏感度**：模型在处理 JSON、Pydantic 等不同格式时的性能也不同，Claude 系列在此项测试中通常表现较优 [18]。",
    "conversation_id": "f97c9bd5-b5bd-40d9-b4c7-5f7173fd585f",
    "sources_used": [
      "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "e9400d2f-22c2-476b-8bfa-292662063768",
      "5d860664-3c42-434c-85d9-52ba7b008def",
      "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "23d4ae25-c078-4c24-825f-676b34bd530d",
      "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
      "f1862034-f162-453c-bd4e-28a714de736c"
    ],
    "citations": {
      "1": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "2": "e9400d2f-22c2-476b-8bfa-292662063768",
      "3": "5d860664-3c42-434c-85d9-52ba7b008def",
      "4": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "5": "e9400d2f-22c2-476b-8bfa-292662063768",
      "6": "e9400d2f-22c2-476b-8bfa-292662063768",
      "7": "5d860664-3c42-434c-85d9-52ba7b008def",
      "8": "5d860664-3c42-434c-85d9-52ba7b008def",
      "9": "5d860664-3c42-434c-85d9-52ba7b008def",
      "10": "e9400d2f-22c2-476b-8bfa-292662063768",
      "11": "e9400d2f-22c2-476b-8bfa-292662063768",
      "12": "e9400d2f-22c2-476b-8bfa-292662063768",
      "13": "5d860664-3c42-434c-85d9-52ba7b008def",
      "14": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "15": "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "16": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "17": "e9400d2f-22c2-476b-8bfa-292662063768",
      "18": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "19": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "20": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "21": "5d860664-3c42-434c-85d9-52ba7b008def",
      "22": "5d860664-3c42-434c-85d9-52ba7b008def",
      "23": "5d860664-3c42-434c-85d9-52ba7b008def",
      "24": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "25": "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
      "26": "5d860664-3c42-434c-85d9-52ba7b008def",
      "27": "f1862034-f162-453c-bd4e-28a714de736c",
      "28": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "29": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "30": "23d4ae25-c078-4c24-825f-676b34bd530d"
    },
    "references": [
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 1,
        "cited_text": "Install MCP Server MCP Docs Copy MCP URL Install in Cursor Copy Claude Code command Copy Codex config LlamaIndex Framework Use Cases Agents Copy Markdown Open in Claude Open in ChatGPT Open in Cursor Copy Markdown View as Markdown Agents An “agent” is an automated reasoning and decision engine. It takes in a user input/query and can make internal decisions for executing that query in order to return the correct result. The key agent components can include, but are not limited to: Breaking down a complex question into smaller ones Choosing an external Tool to use + coming up with parameters for calling the Tool Planning out a set of tasks Storing previously completed tasks in a memory module"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 2,
        "cited_text": "Function calling lets you connect models to external tools and APIs. Instead of generating text responses, the model determines when to call specific functions and provides the necessary parameters to execute real-world actions. This allows the model to act as a bridge between natural language and real-world actions and data. Function calling has 3 primary use cases: Augment Knowledge: Access information from external sources like databases, APIs, and knowledge bases. Extend Capabilities: Use external tools to perform computations and extend the limitations of the model, such as using a calculator or creating charts. Take Actions: Interact with external systems using APIs, such as scheduling appointments, creating invoices, sending emails, or controlling smart home devices."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 3,
        "cited_text": "The tool calling flow Tool calling is a multi-step conversation between your application and a model via the OpenAI API. The tool calling flow has five high level steps: Make a request to the model with tools it could call Receive a tool call from the model Execute code on the application side with input from the tool call Make a second request to the model with the tool output Receive a final response from the model (or more tool calls) Function tool example Let's look at an end-to-end tool calling flow for a get_horoscope function that gets a daily horoscope for an astrological sign."
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 4,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 5,
        "cited_text": "Define function declaration: Define the function declaration in your application code. Function Declarations describe the function's name, parameters, and purpose to the model. Call API with function declarations: Send user prompt along with the function declaration(s) to the model. It analyzes the request and determines if a function call would be helpful. If so, it responds with a structured JSON object containing the function name, arguments, and a unique id (this id is now always returned by the API for Gemini 3 models * ). Execute function code (your responsibility): The Model doesn't execute the function itself. It's your application's responsibility to process the response and check for a function call. If Yes : Extract the name, args, and id of the function and execute the corresponding function in your application. No: The model has provided a direct text response to the prompt (this flow is less emphasized in the example but is a possible outcome). Create user friendly response: If a function was executed, capture the result and send it back to the model, ensuring you include the matching id , in a subsequent turn of the conversation. It will use the result to generate a final, user-friendly response that incorporates the information from the function call."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 6,
        "cited_text": "name (string): A unique name for the function ( get_weather_forecast , send_email ). Use descriptive names without spaces or special characters (use underscores or camelCase). description (string): A clear and detailed explanation of the function's purpose and capabilities. This is crucial for the model to understand when to use the function. Be specific and provide examples if helpful (\"Finds theaters based on location and optionally movie title which is currently playing in theaters.\"). parameters (object): Defines the input parameters the function expects. type (string): Specifies the overall data type, such as object . properties (object): Lists individual parameters, each with: type (string): The data type of the parameter, such as string , integer , boolean, array . description (string): A description of the parameter's purpose and format. Provide examples and constraints (\"The city and state, e.g., 'San Francisco, CA' or a zip code e.g., '95616'.\"). enum (array, optional): If the parameter values are from a fixed set, use \"enum\" to list the allowed values instead of just describing them in the description. This improves accuracy (\"enum\": [\"daylight\", \"cool\", \"warm\"]). required (array): An array of strings listing the parameter names that are mandatory for the function to operate."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 7,
        "cited_text": "<cited_table> Here is an example function definition for a get_weather function Because the parameters are defined by a JSON schema , you can leverage many of its rich features like property types, enums, descriptions, nested objects, and, recursive objects.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Field",
              "Description"
            ],
            [
              "type",
              "This should always be"
            ],
            [
              "name",
              "The function's name (e.g."
            ],
            [
              "description",
              "Details on when and how to use the function"
            ],
            [
              "parameters",
              "JSON schema"
            ],
            [
              "strict",
              "Whether to enforce strict mode for the function call"
            ]
          ]
        }
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 8,
        "cited_text": "Tool calls - requests from the model to use tools A function call or tool call refers to a special kind of response we can get from the model if it examines a prompt, and then determines that in order to follow the instructions in the prompt, it needs to call one of the tools we made available to it. If the model receives a prompt like “what is the weather in Paris?” in an API request, it could respond to that prompt with a tool call for the get_weather tool, with Paris as the location argument. Tool call outputs - output we generate for the model"
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 9,
        "cited_text": "Handling function calls When the model calls a function, you must execute it and return the result. Since model responses can include zero, one, or multiple calls, it is best practice to assume there are several. The response has an array of tool_calls , each with an id (used later to submit the function result) and a function containing a name and JSON-encoded arguments . Sample response with multiple function calls Execute function calls and append results python The response output array contains an entry with the type having a value of function_call . Each entry with a call_id (used later to submit the function result), name , and JSON-encoded arguments ."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 10,
        "cited_text": "Python JavaScript More The model then returns a functionCall object in an OpenAPI compatible schema specifying how to call one or more of the declared functions in order to respond to the user's question. Python JavaScript More Step 3: Execute set_light_values function code Extract the function call details from the model's response, parse the arguments , and execute the set_light_values function. Python JavaScript More Step 4: Create user friendly response with function result and call the model again"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 11,
        "cited_text": "Python More Compositional function calling Compositional or sequential function calling allows Gemini to chain multiple function calls together to fulfill a complex request. For example, to answer \"Get the temperature in my current location\", the Gemini API might first invoke a get_current_location() function followed by a get_weather() function that takes the location as a parameter. The following example demonstrates how to implement compositional function calling using the Python SDK and automatic function calling."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 12,
        "cited_text": "You can also construct FunctionDeclarations from Python functions directly using types.FunctionDeclaration.from_callable(client=client, callable=your_function) . Function calling with thinking models Gemini 3 and 2.5 series models use an internal \"thinking\" process to reason through requests. This significantly improves function calling performance, allowing the model to better determine when to call a function and which parameters to use. Because the Gemini API is stateless, models use thought signatures to maintain context across multi-turn conversations."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 13,
        "cited_text": "Complete tool calling example python Complete tool calling example python Note that for reasoning models like GPT-5 or o4-mini, any reasoning items returned in model responses with tool calls must also be passed back with tool call outputs. Defining functions Functions are usually declared in the tools parameter of each API request. With tool search , your application can also load deferred functions later in the interaction. Either way, each callable function uses the same schema shape. A function definition has the following properties:"
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 14,
        "cited_text": "Tool use with Claude - Claude API Docs Loading... Developer Guide API Reference MCP Resources Release Notes English Log in Search... ⌘K First steps Intro to Claude Quickstart Models & pricing Models overview Choosing a model What's new in Claude 4.6 Migration guide Model deprecations Pricing Build with Claude Features overview Using the Messages API Handling stop reasons Prompting best practices Model capabilities Extended thinking Adaptive thinking Effort Fast mode (beta: research preview) Structured outputs Citations Streaming Messages Batch processing PDF support Search results Multilingual support Embeddings Vision"
      },
      {
        "source_id": "b717658c-57b7-4b5b-9367-7bd1fd456082",
        "citation_number": 15,
        "cited_text": "Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components. Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 16,
        "cited_text": "Agentic RAG : Build a context-augmented research assistant over your data that not only answers simple questions, but complex research tasks. Our getting started guide is a great place to start. Report Generation : Generate a multimodal report using a multi-agent researcher + writer workflow + LlamaParse. Notebook . Customer Support : Check out starter template for building a multi-agent concierge with workflows . Others: Productivity Assistant : Build an agent that can operate over common workflow tools like email, calendar. Check out our GSuite agent tutorial . Coding Assistant : Build an agent that can operate over code. Check out our code interpreter tutorial ."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 17,
        "cited_text": "Model context protocol (MCP) Model Context Protocol (MCP) is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts. The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model."
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 18,
        "cited_text": "| ||| | Agentic || Multi Turn | Single Turn || Hallucination Measurement || Format Sensitivity || | || | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | ||| | Web Search | Memory | Multi turn | Non-live (AST) | Live (AST) | || || Latency (s) | || | Rank 🔼 | Overall Acc | Model | Cost ($) | Overall Acc | Base | No Snippet | Overall Acc | KV | Vector | Recursive Sum | Overall Acc | Base | Miss Func | Miss Param | Long Context | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Relevance | Irrelevance | Max Delta | SD | Mean | SD | P95 | Organization | License | | 1 | 77.47 | Claude-Opus-4-5-20251101 (FC) | 86.55 | 84.5 | 84 | 85 | 73.76 | 70.97 | 72.9 | 77.42 | 68.38 | 81 | 64 | 58 | 70.5 | 88.58 | 76.83 | 95.5 | 93.5 | 88.5 | 79.79 | 86.43 | 78.16 | 87.5 | 75 | 62.5 | 84.72 | N/A | N/A | 4.38 | 3.13 | 7.56 | Anthropic | Proprietary | | 2 | 73.24 | Claude-Sonnet-4-5-20250929 (FC) | 43.73 | 81 | 82 | 80 | 64.95 | 54.19 | 57.42 | 83.23 | 61.37 | 69 | 65 | 52.5 | 59 | 88.65 | 72.58 | 95.5 | 94.5 | 92 | 81.13 | 89.53 | 78.92 | 87.5 | 83.33 | 68.75 | 86.61 | N/A | N/A | 4.31 | 4.43 | 7.27 | Anthropic | Proprietary | | 3 | 72.51 | Gemini-3-Pro-Preview (Prompt) | 298.47 | 80 | 78 | 82 | 61.72 | 59.35 | 62.58 | 63.23 | 60.75 | 64.5 | 60 | 54.5 | 64 | 90.65 | 79.58 | 96 | 95 | 92 | 83.12 | 87.6 | 81.77 | 93.75 | 87.5 | 68.75 | 85.59 | 8.5 | 1.7 | 12.08 | 21.3 | 32.73 | Google | Proprietary | | 4 | 72.38 | GLM-4.6 (FC thinking) | 4.64 | 77.5 | 79 | 76 | 55.7 | 43.87 | 56.13 | 67.1 | 68 | 74.5 | 68 | 63 | 66.5 | 87.56 | 74.25 | 95 | 91.5 | 89.5 | 80.9 | 89.53 | 78.92 | 81.25 | 75 | 75 | 84.96 | N/A | N/A | 4.34 | 7.22 | 13.5 | Zhipu AI | MIT | | 5 | 69.57 | Grok-4-1-fast-reasoning (FC) | 17.26 | 82.5 | 82 | 83 | 53.98 | 41.29 | 57.42 | 63.23 | 58.87 | 70.5 | 59.5 | 43 | 62.5 | 88.27 | 77.58 | 93 | 92.5 | 90 | 78.46 | 84.11 | 77.3 | 75 | 70.83 | 81.25 | 79.43 | N/A | N/A | 6.74 | 12.78 | 17.57 | xAI | Proprietary | | 6 | 68.7 | Claude-Haiku-4-5-20251001 (FC) | 14.23 | 83.5 | 86 | 81 | 54.41 | 51.61 | 55.48 | 56.13 | 53.62 | 63.5 | 42.5 | 52.5 | 56 | 86.5 | 71 | 94 | 92.5 | 88.5 | 78.68 | 83.72 | 77.59 | 75 | 75 | 62.5 | 85.11 | N/A | N/A | 1.68 | 3.92 | 3.15 | Anthropic | Proprietary | | 7 | 68.14 | Gemini-3-Pro-Preview (FC) | 224.69 | 68.5 | 63 | 74 | 54.84 | 50.32 | 63.23 | 50.97 | 63.12 | 69 | 63 | 56.5 | 64 | 85.75 | 75.5 | 94 | 91 | 82.5 | 81.72 | 87.6 | 80.44 | 75 | 79.17 | 75 | 77.85 | N/A | N/A | 15.87 | 41.41 | 58.48 | Google | Proprietary | | 8 | 63.05 | o3-2025-04-16 (Prompt) | 234.64 | 50.5 | 51 | 50 | 51.83 | 33.55 | 50.32 | 71.61 | 62.25 | 68 | 63.5 | 54.5 | 63 | 81.94 | 74.25 | 89 | 86.5 | 78 | 73.21 | 83.33 | 70.75 | 75 | 70.83 | 93.75 | 83.98 | 8.5 | 2.75 | 4.83 | 7.01 | 11.7 | OpenAI | Proprietary | | 9 | 62.97 | Grok-4-0709 (Prompt) | 348.19 | 74 | 74 | 74 | 50.54 | 43.87 | 59.35 | 48.39 | 47 | 55.5 | 46 | 36 | 50.5 | 82.75 | 67 | 93.5 | 89 | 81.5 | 72.54 | 81.78 | 70.18 | 81.25 | 70.83 | 81.25 | 84.3 | 13.0 | 2.88 | 30.38 | 36.19 | 101.54 | xAI | Proprietary | | 10 | 61.38 | Grok-4-0709 (FC) | 355.17 | 82 | 80 | 84 | 55.91 | 57.42 | 58.71 | 51.61 | 33.88 | 44 | 19 | 28.5 | 44 | 85.38 | 73.5 | 92.5 | 88.5 | 87 | 75.57 | 82.17 | 73.88 | 75 | 79.17 | 87.5 | 75.4 | N/A | N/A | 15.49 | 26.22 | 44.28 | xAI | Proprietary | | 11 | 59.06 | Moonshotai-Kimi-K2-Instruct (FC) | 6.19 | 66.5 | 72 | 61 | 29.03 | 21.94 | 20 | 45.16 | 50.63 | 62 | 41 | 44.5 | 55 | 81.6 | 69.42 | 92 | 82 | 83 | 78.68 | 81.78 | 78.06 | 87.5 | 66.67 | 75 | 87.34 | N/A | N/A | 6.4 | 9.38 | 13.78 | MoonshotAI | modified-mit | | 12 | 58.29 | Grok-4-1-fast-non-reasoning (FC)"
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 19,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 20,
        "cited_text": "Tool use examples For a complete hands-on walkthrough, see the tutorial . For reference examples of individual concepts, see Define tools and Handle tool calls . What happens when Claude needs more information Pricing Tool use requests are priced based on: The total number of input tokens sent to the model (including in the tools parameter) The number of output tokens generated For server-side tools, additional usage-based pricing (e.g., web search charges per search performed) Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 21,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 22,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 23,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 24,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
        "citation_number": 25,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 26,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "f1862034-f162-453c-bd4e-28a714de736c",
        "citation_number": 27,
        "cited_text": "Copy Page More page actions Responses Copy Page More page actions Structured model outputs Ensure text responses from the model adhere to a JSON schema you define. JSON is one of the most widely used formats in the world for applications to exchange data. Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema , so you don't need to worry about the model omitting a required key, or hallucinating an invalid enum value. Some benefits of Structured Outputs include:"
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 28,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 29,
        "cited_text": "Berkeley Function Calling Leaderboard (BFCL) V4 Home Blog Try it Out! Leaderboard Berkeley Function-Calling Leaderboard BFCL: From Tool Use to Agentic Evaluation of Large Language Models The Berkeley Function Calling Leaderboard (BFCL) V4 evaluates the LLM's ability to call functions (aka tools) accurately. This leaderboard consists of real-world data and will be updated periodically. For more information on the evaluation dataset and methodology, please refer to our blogs: BFCL-v1 introducing AST as an evaluation metric, BFCL-v2 introducing enterprise and OSS-contributed functions, BFCL-v3 introducing multi-turn interactions, and BFCL-v4 introducing holistic agentic evaluation. Checkout code and data ."
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 30,
        "cited_text": "| 16.27 | 75 | 74 | 76 | 26.24 | 20.65 | 20 | 38.06 | 46.75 | 58 | 39.5 | 37.5 | 52 | 88.13 | 76 | 93 | 93 | 90.5 | 77.94 | 82.95 | 76.92 | 75 | 70.83 | 81.25 | 74.09 | N/A | N/A | 2.29 | 7.31 | 5.34 | xAI | Proprietary | | 13 | 57.06 | Command A Reasoning (FC) | 3.04 | 55.5 | 65 | 46 | 28.82 | 16.13 | 23.87 | 46.45 | 50.12 | 61.5 | 41 | 49.5 | 48.5 | 86.27 | 73.58 | 93.5 | 89.5 | 88.5 | 78.61 | 80.23 | 78.35 | 75 | 75 | 68.75 | 86.75 | N/A | N/A | 3.44 | 4.91 | 8.39 | Cohere | CC-BY-NC 4.0 License (w/ Acceptable Use Addendum) | | 14 | 56.73 | DeepSeek-V3.2-Exp (Prompt + Thinking) | 57.75 | 58 | 64 | 52 | 44.09 | 46.45 | 46.45 | 39.35 | 44.88 | 55 | 49 | 27 | 48.5 | 85.52 | 74.08 | 92 | 89.5 | 86.5 | 76.02 | 82.56 | 74.74 | 87.5 | 54.17 | 93.75 | 67 | 10.0 | 2.77 | 37.89 | 49.56 | 102.09 | DeepSeek | MIT | | 15 | 56.24 | Gemini-2.5-Flash (FC) | 26.36 | 59 | 59 | 59 | 41.29 | 19.35 | 50.32 | 54.19 | 36.25 | 41.5 | 36 | 32 | 35.5 | 84.96 | 74.33 | 92 | 94 | 79.5 | 74.39 | 85.27 | 71.7 | 81.25 | 70.83 | 75 | 93.67 | N/A | N/A | 2.99 | 9.22 | 5.62 | Google | Proprietary | | 16 | 55.87 | GPT-5.2-2025-12-11 (FC) | 85.65 | 75.5 | 78 | 73 | 45.81 | 33.55 | 43.23 | 60.65 | 28.12 | 36.5 | 18 | 27.5 | 30.5 | 81.85 | 72.92 | 88 | 89 | 77.5 | 70.39 | 71.71 | 70.37 | 68.75 | 58.33 | 75 | 79.42 | N/A | N/A | 2.23 | 9.75 | 5.26 | OpenAI | Proprietary | | 17 | 55.46 | GPT-5-mini-2025-08-07 (FC) | 22.18 | 82 | 87 | 77 | 44.3 | 36.77 | 43.87 | 52.26 | 27.5 | 36.5 | 17 | 23.5 | 33 | 69.85 | 59.92 | 69 | 80 | 70.5 | 58.62 | 62.02 | 58.02 | 62.5 | 45.83 | 62.5 | 91.01 | N/A | N/A | 8.32 | 17.35 | 19.8 | OpenAI | Proprietary | | 18 | 54.66 | xLAM-2-32b-fc-r (FC) | 6.0 | 25.5 | 37 | 14 | 20.86 | 6.45 | 10.32 | 45.81 | 69.5 | 81.5 | 72.5 | 67.5 | 56.5 | 89.6 | 80.42 | 94 | 93 | 91 | 75.5 | 82.17 | 74.64 | 50 | 58.33 | 81.25 | 80.23 | N/A | N/A | 6.94 | 8.21 | 17.66 | Salesforce | cc-by-nc-4.0 | | 19 | 54.12 | DeepSeek-V3.2-Exp (FC) | 6.71 | 69.5 | 80 | 59 | 54.19 | 41.94 | 61.29 | 59.35 | 37.38 | 41.5 | 39.5 | 33.5 | 35 | 34.85 | 37.92 | 74 | 15 | 12.5 | 53.66 | 66.28 | 51.66 | 25 | 25 | 37.5 | 93.18 | N/A | N/A | 5.83 | 11.71 | 10.59 | DeepSeek | MIT | | 20 | 53.96 | GPT-4.1-2025-04-14 (FC) | 100.75 | 68 | 67 | 69 | 23.87 | 16.13 | 18.06 | 37.42 | 38.88 | 47.5 | 32.5 | 32.5 | 43 | 82.79 | 72.67 | 89 | 88 | 81.5 | 69.95 | 69.38 | 70.28 | 56.25 | 70.83 | 87.5 | 86.52 | N/A | N/A | 1.63 | 3.05 | 4.01 | OpenAI | Proprietary | | 21 | 53.24 | o4-mini-2025-04-16 (FC) | 81.91 | 75.5 | 75 | 76 | 34.19 | 19.35 | 24.52 | 58.71 | 41.75 | 51 | 30 | 40.5 | 45.5 | 37.73 | 66.92 | 84 | 0 | 0 | 66.1 | 69.38 | 67.81 | 0 | 0 | 81.25 | 83.91 | N/A | N/A | 3.71 | 7.18 | 9.33 | OpenAI | Proprietary | | 22 | 53.07 | xLAM-2-70b-fc-r (FC) | 25.1 | 15 | 17 | 13 | 14.41 | 2.58 | 10.97 | 29.68 | 77.38 | 82.5 | 77 | 74 | 76 | 88.44 | 78.25 | 94 | 92 | 89.5 | 72.17 | 77.91 | 71.13 | 68.75 | 58.33 | 75 | 79.11 | N/A | N/A | 28.06 | 68.77 | 91.21 | Salesforce | cc-by-nc-4.0 | | 23 | 52.15 | Qwen3-235B-A22B-Instruct-2507 (Prompt) | 3.12 | 50.5 | 56 | 45 | 19.35 | 12.9 | 11.61 | 33.55 | 44.62 | 54 | 42.5 | 31.5 | 50.5 | 90.33 | 79.83 | 95 | 95.5 | 91 | 78.68 | 82.95 | 77.78 | 81.25 | 70.83 | 93.75 | 78.89 | 8.0 | 1.95 | 2.56 | 2.75 | 7.61 | Qwen | apache-2.0 | | 24 | 51.45 | GPT-5-nano-2025-08-07 (FC) | 8.79 | 72.5 | 74 | 71 | 24.73 | 18.06 | 27.1 | 29.03 | 34.5 | 44 | 23.5 | 32.5 | 38 | 68 | 57 | 64.5 | 79 | 71.5 | 59.44 | 58.91 | 59.83 | 50 | 54.17 | 75 | 89.1 | N/A | N/A | 10.36 | 10.37 | 23.56 | OpenAI | Proprietary | | 25 | 51.4 | Nanbeige4-3B-Thinking-2511 (FC) | 14.14 | 21.5 | 31 | 12 | 36.77 | 31.61 | 34.19 | 44.52 | 51.12 | 58.5 | 54 | 45 | 47 | 81.58 | 63.83 | 93.5 | 84.5 | 84.5 | 79.42 | 86.05 | 78.06 | 75 | 70.83 | 75 | 83.09 | N/A | N/A | 13.46 | 26.41 | 37.45 | Nanbeige | apache-2.0 | | 26 | 50.9 | Gemini-2.5-Flash (Prompt)"
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "基于提供的来源，以下是关于「LLM 作为 Agent 大脑：模型能力边界与选型策略」的真实应用场景、部署方案、基准数据及实践经验的详细汇总：\n\n### 1. 真实应用场景与案例\nAgent 通过将复杂问题拆解、选择工具并规划任务，在多个领域展现了即时价值：\n*   **智能辅助研发与办公**：\n    *   **代码助手 (Coding Assistant)**：构建能够操作代码库、利用代码解释器执行逻辑的智能体 [1]。\n    *   **生产力助手 (Productivity Assistant)**：操作电子邮件、日历等常用工作流工具（如 GSuite 智能体） [1]。\n*   **企业级服务**：\n    *   **智能客服 (Customer Support)**：通过多智能体礼宾工作流处理用户咨询，实现自动化的客户引导 [1]。\n    *   **报告自动生成 (Report Generation)**：结合 LlamaParse，利用“研究员+撰写者”的多智能体协作模式生成多模态报告 [1]。\n*   **知识管理**：\n    *   **智能体 RAG (Agentic RAG)**：构建上下文增强的研究助手，不仅回答简单问题，还能处理复杂的深度研究任务 [1]。\n    *   **垂直领域应用**：如通过 API 调用实现自动排期、创建发票、发送邮件或控制智能家居设备 [2]。\n\n### 2. 工业级部署方案\n为了将 Agent 推向生产环境，业界已形成了一套成熟的工具链和基础设施：\n*   **云原生与容器化部署**：\n    *   **Docker 隔离环境**：利用 **Gorilla Execution Engine (GoEx)** 在沙盒化的 Docker 环境中执行 LLM 生成的动作，以确保安全 [3, 4]。\n    *   **Kubernetes (K8s)**：通过 Helm Chart、YAML 文件在 K8s 上配置高可用集群，支持大规模部署 [5]。\n*   **基础设施即代码 (IaC)**：\n    *   支持使用 **Terraform** 或 **AWS CDK** 一键部署到 AWS、Google Cloud、Azure 等主流云平台 [5, 6]。\n    *   **Azure DevOps Pipeline**：利用 Helm Chart 实现自动化流水线部署 [6]。\n*   **一站式平台**：\n    *   **Dify**：提供生产级智能体开发平台，集成 AI 工作流、RAG 流水线、模型管理及监控（如 Grafana 仪表板） [7, 8]。\n    *   **智谱 AI (bigmodel.cn)**：提供包括模型精调、推理、评测及 API 服务的一站式 MaaS 开发范式 [9]。\n\n### 3. 开源项目实战案例\n*   **LlamaIndex**：提供预构建的智能体架构和自定义工作流（Workflows），支持从简单的 ReAct 智能体到复杂的多智能体模式 [10, 11]。\n*   **AutoGen (Microsoft)**：侧重于多智能体编排，支持事件驱动的通信模式，并提供分布式运行时环境 [12, 13]。\n*   **Gorilla**：通过微调 LLaMA 模型，在调用 1600+ API 时表现出色，显著降低了幻觉率，并能适应文档的频繁更新 [14, 15]。\n*   **LangChain**：标准化的接口框架，支持快速原型开发，并集成了大量的工具包、向量数据库和评估工具 [16, 17]。\n\n### 4. 性能基准数据 (基于 BFCL V4)\n根据 **Berkeley Function Calling Leaderboard (BFCL) V4**，各主流模型在 Agent 核心能力上的表现如下 [18, 19]：\n\n| 指标 | Claude-Opus-4.5 (FC) | Gemini-3-Pro-Preview | GLM-4.6 (Thinking) | DeepSeek-V3.2 (Thinking) |\n| :--- | :--- | :--- | :--- | :--- |\n| **总体准确率** | **77.47%** | 72.51% | 72.38% | 56.73% |\n| **平均延迟** | 4.38s | 12.08s | 4.34s | 37.89s |\n| **测试总成本** | $86.55 | $298.47 | **$4.64** | $57.75 |\n| **幻觉控制率** | 84.72% | 85.59% | 84.96% | 67.00% |\n\n*注：GLM-4.6 在保持高准确率的同时，成本仅为头部模型的数十分之一，具有极高的工业性价比 [18]。*\n\n### 5. 开发者最佳实践与踩坑经验\n#### 最佳实践：\n*   **精简工具集**：虽然模型能处理大量工具，但建议将当前激活的工具集控制在 **10-20 个**以内，以降低误选风险 [20, 21]。\n*   **严格类型约束 (Strict Mode)**：启用 `strict: true` 强制模型输出完全符合 JSON Schema，减少格式校验失败 [22, 23]。\n*   **高质量描述**：函数名和参数描述必须清晰、无歧义，模型极其依赖这些自然语言指令来理解工具意图 [20, 21]。\n*   **提示词工程**：使用系统提示词明确 Agent 的角色和工具使用边界（例如：“不要猜测日期，必须调用获取日期工具”） [20]。\n*   **温度设置**：通常建议将 **Temperature 设为 0** 以获得确定的工具调用结果；但对于 Gemini 3，建议保持 **默认值 1.0** 以避免推理循环异常 [20]。\n\n#### 踩坑经验 (Pitfalls)：\n*   **Token 限制风险**：工具描述和参数 Schema 会消耗大量输入 Token，过长的描述可能导致模型达到上下文极限 [20, 24]。\n*   **数组位置假设**：在处理 JSON 响应时，不要假设 `functionCall` 总是在数组的末尾，必须遍历 `parts` 数组以处理混合返回的情况 [25]。\n*   **幻觉处理不当**：如果用户请求超出了工具能力，模型可能会捏造参数；建议在 Prompt 中指示模型在无法处理时主动询问或返回特定错误信息 [26]。\n*   **忽略 finishReason**：必须检查响应中的 `finishReason`，以处理因模型无法生成有效工具调用而导致的异常流程 [20]。\n*   **并行调用冲突**：虽然并行调用能提高效率，但需注意某些工具之间是否存在时序依赖或竞态条件 [27, 28]。",
    "conversation_id": "f97c9bd5-b5bd-40d9-b4c7-5f7173fd585f",
    "sources_used": [
      "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "e9400d2f-22c2-476b-8bfa-292662063768",
      "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "2db39851-e74c-4170-ac46-8b20063363d5",
      "3a08567b-3003-4501-94a1-7a0d3b200873",
      "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
      "a48d217e-2c80-405c-90aa-3213a16edf40",
      "23d4ae25-c078-4c24-825f-676b34bd530d",
      "5d860664-3c42-434c-85d9-52ba7b008def",
      "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "f1862034-f162-453c-bd4e-28a714de736c"
    ],
    "citations": {
      "1": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "2": "e9400d2f-22c2-476b-8bfa-292662063768",
      "3": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "4": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "5": "2db39851-e74c-4170-ac46-8b20063363d5",
      "6": "2db39851-e74c-4170-ac46-8b20063363d5",
      "7": "2db39851-e74c-4170-ac46-8b20063363d5",
      "8": "2db39851-e74c-4170-ac46-8b20063363d5",
      "9": "3a08567b-3003-4501-94a1-7a0d3b200873",
      "10": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "11": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "12": "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "13": "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "14": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "15": "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
      "16": "a48d217e-2c80-405c-90aa-3213a16edf40",
      "17": "a48d217e-2c80-405c-90aa-3213a16edf40",
      "18": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "19": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "20": "e9400d2f-22c2-476b-8bfa-292662063768",
      "21": "5d860664-3c42-434c-85d9-52ba7b008def",
      "22": "5d860664-3c42-434c-85d9-52ba7b008def",
      "23": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
      "24": "5d860664-3c42-434c-85d9-52ba7b008def",
      "25": "e9400d2f-22c2-476b-8bfa-292662063768",
      "26": "f1862034-f162-453c-bd4e-28a714de736c",
      "27": "e9400d2f-22c2-476b-8bfa-292662063768",
      "28": "5d860664-3c42-434c-85d9-52ba7b008def"
    },
    "references": [
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 1,
        "cited_text": "Agentic RAG : Build a context-augmented research assistant over your data that not only answers simple questions, but complex research tasks. Our getting started guide is a great place to start. Report Generation : Generate a multimodal report using a multi-agent researcher + writer workflow + LlamaParse. Notebook . Customer Support : Check out starter template for building a multi-agent concierge with workflows . Others: Productivity Assistant : Build an agent that can operate over common workflow tools like email, calendar. Check out our GSuite agent tutorial . Coding Assistant : Build an agent that can operate over code. Check out our code interpreter tutorial ."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 2,
        "cited_text": "Function calling lets you connect models to external tools and APIs. Instead of generating text responses, the model determines when to call specific functions and provides the necessary parameters to execute real-world actions. This allows the model to act as a bridge between natural language and real-world actions and data. Function calling has 3 primary use cases: Augment Knowledge: Access information from external sources like databases, APIs, and knowledge bases. Extend Capabilities: Use external tools to perform computations and extend the limitations of the model, such as using a calculator or creating charts. Take Actions: Interact with external systems using APIs, such as scheduling appointments, creating invoices, sending emails, or controlling smart home devices."
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 3,
        "cited_text": "• Head-to-head agent comparisons with ELO rating system • Framework compatibility testing (LangChain, AutoGPT) • Community-driven evaluation platform • Real-world task performance metrics Gorilla Execution Engine (GoEx) 🔧 Infra Runtime for executing LLM-generated actions with safety guarantees • Post-facto validation for verifying LLM actions after execution • Undo capabilities and damage confinement for risk mitigation • OAuth2 and API key authentication for multiple services • Support for RESTful APIs, databases, and filesystem operations"
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 4,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "2db39851-e74c-4170-ac46-8b20063363d5",
        "citation_number": 5,
        "cited_text": "Deployment with Kubernetes If you'd like to configure a highly-available setup, there are community-contributed Helm Charts and YAML files which allow Dify to be deployed on Kubernetes. Helm Chart by @LeoQuote Helm Chart by @BorisPolonsky Helm Chart by @magicsong YAML file by @Winson-030 YAML file by @wyy-holding 🚀 NEW! YAML files (Supports Dify v1.6.0) by @Zhoneym Using Terraform for Deployment Deploy Dify to Cloud Platform with a single click using terraform Azure Global Azure Terraform by @nikawang"
      },
      {
        "source_id": "2db39851-e74c-4170-ac46-8b20063363d5",
        "citation_number": 6,
        "cited_text": "Google Cloud Google Cloud Terraform by @sotazum Using AWS CDK for Deployment Deploy Dify to AWS with CDK AWS AWS CDK by @KevinZhao (EKS based) AWS CDK by @tmokmss (ECS based) Using Alibaba Cloud Computing Nest Quickly deploy Dify to Alibaba cloud with Alibaba Cloud Computing Nest Using Alibaba Cloud Data Management One-Click deploy Dify to Alibaba Cloud with Alibaba Cloud Data Management Deploy to AKS with Azure Devops Pipeline One-Click deploy Dify to AKS with Azure Devops Pipeline Helm Chart by @LeoZhang"
      },
      {
        "source_id": "2db39851-e74c-4170-ac46-8b20063363d5",
        "citation_number": 7,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing License Dify Cloud · Self-hosting · Documentation · Dify edition overview Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features (including Opik , Langfuse , and Arize Phoenix ) and more, letting you quickly go from prototype to production. Here's a list of the core features:"
      },
      {
        "source_id": "2db39851-e74c-4170-ac46-8b20063363d5",
        "citation_number": 8,
        "cited_text": "Customizing Suggested Questions You can now customize the \"Suggested Questions After Answer\" feature to better fit your use case. For example, to generate longer, more technical questions: See the Suggested Questions Configuration Guide for detailed examples and usage instructions. Metrics Monitoring with Grafana Import the dashboard to Grafana, using Dify's PostgreSQL database as data source, to monitor metrics in granularity of apps, tenants, messages, and more. Grafana Dashboard by @bowenliang123"
      },
      {
        "source_id": "3a08567b-3003-4501-94a1-7a0d3b200873",
        "citation_number": 9,
        "cited_text": "Skip to main content 智谱AI开放文档  home page 使用指南 API 文档 场景示例 编码套餐 更新日志 条款与协议 常见问题 开始使用 平台介绍 模型概览 快速开始 核心参数 迁移至 GLM-5 模型介绍 模型能力 深度思考 思考模式 流式消息 工具流式输出 工具调用 上下文缓存 结构化输出 模型工具 GLM in Excel（Beta） 联网搜索 模型部署 模型微调 模型评测 批量处理 OCR 服务 GLM 全模态知识库 知识处理及检索 知识库服务计费 上下文增强技术报告 对话调用知识库 智能体 平台服务 智能体开发平台 提示词工程 内容安全 模型迁移 用户权益 模型备案 平台定位 平台优势 查看模型 极速体验 快速开始 开发指南 核心概念 开始使用 平台介绍 Z智谱·一站式大模型开发平台 平台定位 智谱大模型开放平台 bigmodel.cn ，提供功能丰富、灵活易用、高性价比的大模型 API 服务，支持智能体开发与模型精调、推理、评测等，致力于构建高效通用的“一站式模型即服务” AI 开发新范式。 平台优势 模型矩阵"
      },
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 10,
        "cited_text": "LlamaIndex provides a comprehensive framework for building agentic systems with varying degrees of complexity: If you want to build agents quickly : Use our prebuilt agent and tool architectures to rapidly setup agentic systems. If you want full control over your agentic system : Build and deploy custom agentic workflows from scratch using our Workflows . Use Cases Section titled “Use Cases” The scope of possible use cases for agents is vast and ever-expanding. That said, here are some practical use cases that can deliver immediate value."
      },
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 11,
        "cited_text": "Resources Section titled “Resources” Prebuilt Agents and Tools The following component guides are the central hubs for getting started in building with agents: Agents Tools Custom Agentic Workflows LlamaIndex Workflows allow you to build very custom, agentic workflows through a core event-driven orchestration foundation. Workflows Documentation Building a ReAct agent workflow Deploying Workflows Building with Agentic Ingredients If you want to leverage core agentic ingredients in your workflow, LlamaIndex has robust abstractions for every agent sub-ingredient."
      },
      {
        "source_id": "b717658c-57b7-4b5b-9367-7bd1fd456082",
        "citation_number": 12,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing CC-BY-4.0 license MIT license Security AutoGen AutoGen is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans. Important: if you are new to AutoGen, please checkout Microsoft Agent Framework . AutoGen will still be maintained and continue to receive bug fixes and critical security patches. Read our announcement . Installation AutoGen requires Python 3.10 or later ."
      },
      {
        "source_id": "b717658c-57b7-4b5b-9367-7bd1fd456082",
        "citation_number": 13,
        "cited_text": "Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components. Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 14,
        "cited_text": "About Gorilla enables LLMs to use tools by invoking APIs. Given a natural language query, Gorilla comes up with the semantically- and syntactically- correct API to invoke. With Gorilla, we are the first to demonstrate how to use LLMs to invoke 1,600+ (and growing) API calls accurately while reducing hallucination. This repository contains inference code for running Gorilla finetuned models, evaluation code for reproducing results from our paper, and APIBench - the largest collection of APIs, curated and easy to be trained on!"
      },
      {
        "source_id": "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
        "citation_number": 15,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "a48d217e-2c80-405c-90aa-3213a16edf40",
        "citation_number": 16,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security The agent engineering platform. LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves. Note Looking for the JS/TS library? Check out LangChain.js . Quickstart"
      },
      {
        "source_id": "a48d217e-2c80-405c-90aa-3213a16edf40",
        "citation_number": 17,
        "cited_text": "Why use LangChain? LangChain helps developers build applications powered by LLMs through a standard interface for models, embeddings, vector stores, and more. Real-time data augmentation — Easily connect LLMs to diverse data sources and external/internal systems, drawing from LangChain's vast library of integrations with model providers, tools, vector stores, retrievers, and more Model interoperability — Swap models in and out as your engineering team experiments to find the best choice for your application's needs. As the industry frontier evolves, adapt quickly — LangChain's abstractions keep you moving without losing momentum Rapid prototyping — Quickly build and iterate on LLM applications with LangChain's modular, component-based architecture. Test different approaches and workflows without rebuilding from scratch, accelerating your development cycle Production-ready features — Deploy reliable applications with built-in support for monitoring, evaluation, and debugging through integrations like LangSmith. Scale with confidence using battle-tested patterns and best practices Vibrant community and ecosystem — Leverage a rich ecosystem of integrations, templates, and community-contributed components. Benefit from continuous improvements and stay up-to-date with the latest AI developments through an active open-source community Flexible abstraction layers — Work at the level of abstraction that suits your needs — from high-level chains for quick starts to low-level components for fine-grained control. LangChain grows with your application's complexity"
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 18,
        "cited_text": "| ||| | Agentic || Multi Turn | Single Turn || Hallucination Measurement || Format Sensitivity || | || | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | ||| | Web Search | Memory | Multi turn | Non-live (AST) | Live (AST) | || || Latency (s) | || | Rank 🔼 | Overall Acc | Model | Cost ($) | Overall Acc | Base | No Snippet | Overall Acc | KV | Vector | Recursive Sum | Overall Acc | Base | Miss Func | Miss Param | Long Context | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Relevance | Irrelevance | Max Delta | SD | Mean | SD | P95 | Organization | License | | 1 | 77.47 | Claude-Opus-4-5-20251101 (FC) | 86.55 | 84.5 | 84 | 85 | 73.76 | 70.97 | 72.9 | 77.42 | 68.38 | 81 | 64 | 58 | 70.5 | 88.58 | 76.83 | 95.5 | 93.5 | 88.5 | 79.79 | 86.43 | 78.16 | 87.5 | 75 | 62.5 | 84.72 | N/A | N/A | 4.38 | 3.13 | 7.56 | Anthropic | Proprietary | | 2 | 73.24 | Claude-Sonnet-4-5-20250929 (FC) | 43.73 | 81 | 82 | 80 | 64.95 | 54.19 | 57.42 | 83.23 | 61.37 | 69 | 65 | 52.5 | 59 | 88.65 | 72.58 | 95.5 | 94.5 | 92 | 81.13 | 89.53 | 78.92 | 87.5 | 83.33 | 68.75 | 86.61 | N/A | N/A | 4.31 | 4.43 | 7.27 | Anthropic | Proprietary | | 3 | 72.51 | Gemini-3-Pro-Preview (Prompt) | 298.47 | 80 | 78 | 82 | 61.72 | 59.35 | 62.58 | 63.23 | 60.75 | 64.5 | 60 | 54.5 | 64 | 90.65 | 79.58 | 96 | 95 | 92 | 83.12 | 87.6 | 81.77 | 93.75 | 87.5 | 68.75 | 85.59 | 8.5 | 1.7 | 12.08 | 21.3 | 32.73 | Google | Proprietary | | 4 | 72.38 | GLM-4.6 (FC thinking) | 4.64 | 77.5 | 79 | 76 | 55.7 | 43.87 | 56.13 | 67.1 | 68 | 74.5 | 68 | 63 | 66.5 | 87.56 | 74.25 | 95 | 91.5 | 89.5 | 80.9 | 89.53 | 78.92 | 81.25 | 75 | 75 | 84.96 | N/A | N/A | 4.34 | 7.22 | 13.5 | Zhipu AI | MIT | | 5 | 69.57 | Grok-4-1-fast-reasoning (FC) | 17.26 | 82.5 | 82 | 83 | 53.98 | 41.29 | 57.42 | 63.23 | 58.87 | 70.5 | 59.5 | 43 | 62.5 | 88.27 | 77.58 | 93 | 92.5 | 90 | 78.46 | 84.11 | 77.3 | 75 | 70.83 | 81.25 | 79.43 | N/A | N/A | 6.74 | 12.78 | 17.57 | xAI | Proprietary | | 6 | 68.7 | Claude-Haiku-4-5-20251001 (FC) | 14.23 | 83.5 | 86 | 81 | 54.41 | 51.61 | 55.48 | 56.13 | 53.62 | 63.5 | 42.5 | 52.5 | 56 | 86.5 | 71 | 94 | 92.5 | 88.5 | 78.68 | 83.72 | 77.59 | 75 | 75 | 62.5 | 85.11 | N/A | N/A | 1.68 | 3.92 | 3.15 | Anthropic | Proprietary | | 7 | 68.14 | Gemini-3-Pro-Preview (FC) | 224.69 | 68.5 | 63 | 74 | 54.84 | 50.32 | 63.23 | 50.97 | 63.12 | 69 | 63 | 56.5 | 64 | 85.75 | 75.5 | 94 | 91 | 82.5 | 81.72 | 87.6 | 80.44 | 75 | 79.17 | 75 | 77.85 | N/A | N/A | 15.87 | 41.41 | 58.48 | Google | Proprietary | | 8 | 63.05 | o3-2025-04-16 (Prompt) | 234.64 | 50.5 | 51 | 50 | 51.83 | 33.55 | 50.32 | 71.61 | 62.25 | 68 | 63.5 | 54.5 | 63 | 81.94 | 74.25 | 89 | 86.5 | 78 | 73.21 | 83.33 | 70.75 | 75 | 70.83 | 93.75 | 83.98 | 8.5 | 2.75 | 4.83 | 7.01 | 11.7 | OpenAI | Proprietary | | 9 | 62.97 | Grok-4-0709 (Prompt) | 348.19 | 74 | 74 | 74 | 50.54 | 43.87 | 59.35 | 48.39 | 47 | 55.5 | 46 | 36 | 50.5 | 82.75 | 67 | 93.5 | 89 | 81.5 | 72.54 | 81.78 | 70.18 | 81.25 | 70.83 | 81.25 | 84.3 | 13.0 | 2.88 | 30.38 | 36.19 | 101.54 | xAI | Proprietary | | 10 | 61.38 | Grok-4-0709 (FC) | 355.17 | 82 | 80 | 84 | 55.91 | 57.42 | 58.71 | 51.61 | 33.88 | 44 | 19 | 28.5 | 44 | 85.38 | 73.5 | 92.5 | 88.5 | 87 | 75.57 | 82.17 | 73.88 | 75 | 79.17 | 87.5 | 75.4 | N/A | N/A | 15.49 | 26.22 | 44.28 | xAI | Proprietary | | 11 | 59.06 | Moonshotai-Kimi-K2-Instruct (FC) | 6.19 | 66.5 | 72 | 61 | 29.03 | 21.94 | 20 | 45.16 | 50.63 | 62 | 41 | 44.5 | 55 | 81.6 | 69.42 | 92 | 82 | 83 | 78.68 | 81.78 | 78.06 | 87.5 | 66.67 | 75 | 87.34 | N/A | N/A | 6.4 | 9.38 | 13.78 | MoonshotAI | modified-mit | | 12 | 58.29 | Grok-4-1-fast-non-reasoning (FC)"
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 19,
        "cited_text": "| 16.27 | 75 | 74 | 76 | 26.24 | 20.65 | 20 | 38.06 | 46.75 | 58 | 39.5 | 37.5 | 52 | 88.13 | 76 | 93 | 93 | 90.5 | 77.94 | 82.95 | 76.92 | 75 | 70.83 | 81.25 | 74.09 | N/A | N/A | 2.29 | 7.31 | 5.34 | xAI | Proprietary | | 13 | 57.06 | Command A Reasoning (FC) | 3.04 | 55.5 | 65 | 46 | 28.82 | 16.13 | 23.87 | 46.45 | 50.12 | 61.5 | 41 | 49.5 | 48.5 | 86.27 | 73.58 | 93.5 | 89.5 | 88.5 | 78.61 | 80.23 | 78.35 | 75 | 75 | 68.75 | 86.75 | N/A | N/A | 3.44 | 4.91 | 8.39 | Cohere | CC-BY-NC 4.0 License (w/ Acceptable Use Addendum) | | 14 | 56.73 | DeepSeek-V3.2-Exp (Prompt + Thinking) | 57.75 | 58 | 64 | 52 | 44.09 | 46.45 | 46.45 | 39.35 | 44.88 | 55 | 49 | 27 | 48.5 | 85.52 | 74.08 | 92 | 89.5 | 86.5 | 76.02 | 82.56 | 74.74 | 87.5 | 54.17 | 93.75 | 67 | 10.0 | 2.77 | 37.89 | 49.56 | 102.09 | DeepSeek | MIT | | 15 | 56.24 | Gemini-2.5-Flash (FC) | 26.36 | 59 | 59 | 59 | 41.29 | 19.35 | 50.32 | 54.19 | 36.25 | 41.5 | 36 | 32 | 35.5 | 84.96 | 74.33 | 92 | 94 | 79.5 | 74.39 | 85.27 | 71.7 | 81.25 | 70.83 | 75 | 93.67 | N/A | N/A | 2.99 | 9.22 | 5.62 | Google | Proprietary | | 16 | 55.87 | GPT-5.2-2025-12-11 (FC) | 85.65 | 75.5 | 78 | 73 | 45.81 | 33.55 | 43.23 | 60.65 | 28.12 | 36.5 | 18 | 27.5 | 30.5 | 81.85 | 72.92 | 88 | 89 | 77.5 | 70.39 | 71.71 | 70.37 | 68.75 | 58.33 | 75 | 79.42 | N/A | N/A | 2.23 | 9.75 | 5.26 | OpenAI | Proprietary | | 17 | 55.46 | GPT-5-mini-2025-08-07 (FC) | 22.18 | 82 | 87 | 77 | 44.3 | 36.77 | 43.87 | 52.26 | 27.5 | 36.5 | 17 | 23.5 | 33 | 69.85 | 59.92 | 69 | 80 | 70.5 | 58.62 | 62.02 | 58.02 | 62.5 | 45.83 | 62.5 | 91.01 | N/A | N/A | 8.32 | 17.35 | 19.8 | OpenAI | Proprietary | | 18 | 54.66 | xLAM-2-32b-fc-r (FC) | 6.0 | 25.5 | 37 | 14 | 20.86 | 6.45 | 10.32 | 45.81 | 69.5 | 81.5 | 72.5 | 67.5 | 56.5 | 89.6 | 80.42 | 94 | 93 | 91 | 75.5 | 82.17 | 74.64 | 50 | 58.33 | 81.25 | 80.23 | N/A | N/A | 6.94 | 8.21 | 17.66 | Salesforce | cc-by-nc-4.0 | | 19 | 54.12 | DeepSeek-V3.2-Exp (FC) | 6.71 | 69.5 | 80 | 59 | 54.19 | 41.94 | 61.29 | 59.35 | 37.38 | 41.5 | 39.5 | 33.5 | 35 | 34.85 | 37.92 | 74 | 15 | 12.5 | 53.66 | 66.28 | 51.66 | 25 | 25 | 37.5 | 93.18 | N/A | N/A | 5.83 | 11.71 | 10.59 | DeepSeek | MIT | | 20 | 53.96 | GPT-4.1-2025-04-14 (FC) | 100.75 | 68 | 67 | 69 | 23.87 | 16.13 | 18.06 | 37.42 | 38.88 | 47.5 | 32.5 | 32.5 | 43 | 82.79 | 72.67 | 89 | 88 | 81.5 | 69.95 | 69.38 | 70.28 | 56.25 | 70.83 | 87.5 | 86.52 | N/A | N/A | 1.63 | 3.05 | 4.01 | OpenAI | Proprietary | | 21 | 53.24 | o4-mini-2025-04-16 (FC) | 81.91 | 75.5 | 75 | 76 | 34.19 | 19.35 | 24.52 | 58.71 | 41.75 | 51 | 30 | 40.5 | 45.5 | 37.73 | 66.92 | 84 | 0 | 0 | 66.1 | 69.38 | 67.81 | 0 | 0 | 81.25 | 83.91 | N/A | N/A | 3.71 | 7.18 | 9.33 | OpenAI | Proprietary | | 22 | 53.07 | xLAM-2-70b-fc-r (FC) | 25.1 | 15 | 17 | 13 | 14.41 | 2.58 | 10.97 | 29.68 | 77.38 | 82.5 | 77 | 74 | 76 | 88.44 | 78.25 | 94 | 92 | 89.5 | 72.17 | 77.91 | 71.13 | 68.75 | 58.33 | 75 | 79.11 | N/A | N/A | 28.06 | 68.77 | 91.21 | Salesforce | cc-by-nc-4.0 | | 23 | 52.15 | Qwen3-235B-A22B-Instruct-2507 (Prompt) | 3.12 | 50.5 | 56 | 45 | 19.35 | 12.9 | 11.61 | 33.55 | 44.62 | 54 | 42.5 | 31.5 | 50.5 | 90.33 | 79.83 | 95 | 95.5 | 91 | 78.68 | 82.95 | 77.78 | 81.25 | 70.83 | 93.75 | 78.89 | 8.0 | 1.95 | 2.56 | 2.75 | 7.61 | Qwen | apache-2.0 | | 24 | 51.45 | GPT-5-nano-2025-08-07 (FC) | 8.79 | 72.5 | 74 | 71 | 24.73 | 18.06 | 27.1 | 29.03 | 34.5 | 44 | 23.5 | 32.5 | 38 | 68 | 57 | 64.5 | 79 | 71.5 | 59.44 | 58.91 | 59.83 | 50 | 54.17 | 75 | 89.1 | N/A | N/A | 10.36 | 10.37 | 23.56 | OpenAI | Proprietary | | 25 | 51.4 | Nanbeige4-3B-Thinking-2511 (FC) | 14.14 | 21.5 | 31 | 12 | 36.77 | 31.61 | 34.19 | 44.52 | 51.12 | 58.5 | 54 | 45 | 47 | 81.58 | 63.83 | 93.5 | 84.5 | 84.5 | 79.42 | 86.05 | 78.06 | 75 | 70.83 | 75 | 83.09 | N/A | N/A | 13.46 | 26.41 | 37.45 | Nanbeige | apache-2.0 | | 26 | 50.9 | Gemini-2.5-Flash (Prompt)"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 20,
        "cited_text": "<cited_table> Best practices Function and Parameter Descriptions: Be extremely clear and specific in your descriptions. The model relies on these to choose the correct function and provide appropriate arguments. Naming: Use descriptive function names (without spaces, periods, or dashes). Strong Typing: Use specific types (integer, string, enum) for parameters to reduce errors. If a parameter has a limited set of valid values, use an enum. Tool Selection: While the model can use an arbitrary number of tools, providing too many can increase the risk of selecting an incorrect or suboptimal tool. For best results, aim to provide only the relevant tools for the context or task, ideally keeping the active set to a maximum of 10-20. Consider dynamic tool selection based on conversation context if you have a large total number of tools. Prompt Engineering: Provide context: Tell the model its role (e.g., \"You are a helpful weather assistant.\"). Give instructions: Specify how and when to use functions (e.g., \"Don't guess dates; always use a future date for forecasts.\"). Encourage clarification: Instruct the model to ask clarifying questions if needed. See Agentic workflows for further strategies on designing these prompts. Here is an example of a tested system instruction . Temperature: Use a low temperature (e.g., 0) for more deterministic and reliable function calls. When using Gemini 3 models, we strongly recommend keeping the temperature at its default value of 1.0. Changing the temperature (setting it below 1.0) may lead to unexpected behavior, such as looping or degraded performance, particularly in complex mathematical or reasoning tasks. Validation: If a function call has significant consequences (e.g., placing an order), validate the call with the user before executing it. Check Finish Reason: Always check the finishReason in the model's response to handle cases where the model failed to generate a valid function call. Error Handling : Implement robust error handling in your functions to gracefully handle unexpected inputs or API failures. Return informative error messages that the model can use to generate helpful responses to the user. Security: Be mindful of security when calling external APIs. Use appropriate authentication and authorization mechanisms. Avoid exposing sensitive data in function calls. Token Limits: Function descriptions and parameters count towards your input token limit. If you're hitting token limits, consider limiting the number of functions or the length of the descriptions, break down complex tasks into smaller, more focused function sets. Mix of bash and custom tools For those building with a mix of bash and custom tools, Gemini 3.1 Pro Preview comes with a separate endpoint available via the API called gemini-3.1-pro-preview-customtools .",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Model",
              "Function Calling",
              "Parallel Function Calling",
              "Compositional Function Calling"
            ],
            [
              "Gemini 3.1 Pro Preview",
              "✔",
              "✔",
              "✔"
            ],
            [
              "Gemini 3 Flash Preview",
              "✔",
              "✔",
              "✔"
            ],
            [
              "Gemini 2.5 Pro",
              "✔",
              "✔",
              "✔"
            ],
            [
              "Gemini 2.5 Flash",
              "✔",
              "✔",
              "✔"
            ],
            [
              "Gemini 2.5 Flash-Lite",
              "✔",
              "✔",
              "✔"
            ],
            [
              "Gemini 2.0 Flash",
              "✔",
              "✔",
              "✔"
            ],
            [
              "Gemini 2.0 Flash-Lite",
              "X",
              "X",
              "X"
            ]
          ]
        }
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 21,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 22,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "4968e567-8cd8-4c38-96ba-637b9e667a0e",
        "citation_number": 23,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 24,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 25,
        "cited_text": "Notes and limitations Positioning of function call parts: When using custom function declarations alongside built-in tools (like Google Search), the model may return a mix of functionCall , toolCall , and toolResponse parts in a single turn. Because of this, don't assume the functionCall will always be the last item in the parts array. If you are manually parsing the JSON response, always iterate through the parts array rather than relying on position. Only a subset of the OpenAPI schema is supported. For ANY mode, the API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your function parameter and response schemas by shortening property names, reducing nesting, or limiting the number of function declarations. Supported parameter types in Python are limited. Automatic function calling is a Python SDK feature only."
      },
      {
        "source_id": "f1862034-f162-453c-bd4e-28a714de736c",
        "citation_number": 26,
        "cited_text": "The model will always try to adhere to the provided schema, which can result in hallucinations if the input is completely unrelated to the schema. You could include language in your prompt to specify that you want to return empty parameters, or a specific sentence, if the model detects that the input is incompatible with the task. Handling mistakes Structured Outputs can still contain mistakes. If you see mistakes, try adjusting your instructions, providing examples in the system instructions, or splitting tasks into simpler subtasks. Refer to the prompt engineering guide for more guidance on how to tweak your inputs."
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 27,
        "cited_text": "Inspecting thought signatures While not necessary for implementation, you can inspect the response to see the thought_signature for debugging or educational purposes. Python JavaScript More Learn more about limitations and usage of thought signatures, and about thinking models in general, on the Thinking page. Parallel function calling In addition to single turn function calling, you can also call multiple functions at once. Parallel function calling lets you execute multiple functions at once and is used when the functions are not dependent on each other. This is useful in scenarios like gathering data from multiple independent sources, such as retrieving customer details from different databases or checking inventory levels across various warehouses or performing multiple actions such as converting your apartment into a disco."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 28,
        "cited_text": "Parallel function calling Parallel function calling is not possible when using built-in tools . The model may choose to call multiple functions in a single turn. You can prevent this by setting parallel_tool_calls to false , which ensures exactly zero or one tool is called. Note: Currently, if you are using a fine tuned model and the model calls multiple functions in one turn then strict mode will be disabled for those calls. Note for gpt-4.1-nano-2025-04-14 : This snapshot of gpt-4.1-nano can sometimes include multiple tools calls for the same tool if parallel tool calls are enabled. It is recommended to disable this feature when using this nano snapshot."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在 2025-2026 年的时间框架内，「LLM 作为 Agent 大脑」领域已从简单的工具调用演变为**复杂的自动化推理与决策引擎** [1]。根据 Berkeley Function Calling Leaderboard (BFCL) V4 的最新发布以及 OpenAI、Google 和智谱 AI 等头部厂商的技术路线，该领域的核心研究突破和未来方向可以总结如下：\n\n### 1. 2025-2026 年重要技术趋势与研究进展\n\n*   **推理模型与 Agent 的深度融合 (Reasoning-integrated Agents)**：\n    *   **核心进展**：新一代模型（如 **GPT-5 系列、Gemini 3、GLM-4.6**）引入了**内部“思维链”或“思维签名 (Thought Signatures)”**机制 [2, 3]。这种机制允许模型在执行工具调用前进行深度思考，显著提升了处理复杂逻辑、多步规划和参数提取的准确性 [2, 4]。\n    *   **技术表现**：在 BFCL V4 评测中，具备“Thinking”模式的模型在处理复杂任务时的鲁棒性远超传统模型 [5]。\n\n*   **工具搜索与动态上下文管理 (Tool Search & Dynamic Loading)**：\n    *   **技术突破**：针对拥有上千个 API 的大规模系统，**Tool Search (工具搜索)** 技术（由 GPT-5.4 等支持）允许模型不再预加载所有工具定义，而是根据需求动态搜索并加载相关工具 [6, 7]。\n    *   **意义**：这解决了工具描述过多导致 Token 溢出和准确率下降的难题，使 Agent 能够连接到包含 1600+ API 的“API Zoo”中 [8-10]。\n\n*   **标准化的互操作协议 (MCP)**：\n    *   **行业趋势**：**模型上下文协议 (Model Context Protocol, MCP)** 成为连接 AI 应用与外部数据源（如 Playwright、Slack、GitHub）的开放标准 [11, 12]。这一标准极大降低了开发者为不同模型构建工具适配器的成本 [11, 13]。\n\n*   **全模态 Agentic 循环**：\n    *   **新能力**：Gemini 3 等模型已支持**多模态函数响应 (Multimodal Function Responses)**，模型可以调用工具获取图像或 PDF 文档，并在下一轮对话中直接基于这些多模态内容进行推理 [14, 15]。\n\n### 2. 重要论文与技术框架\n\n*   **BFCL V4 Agentic 评估体系**：研究重点从单轮函数调用转向**整体智能体评估 (Holistic Agentic Evaluation)**。该研究引入了对**网页搜索、多跳推理 (Multi-hop Reasoning)、错误恢复及 Agent 记忆管理**的深度考核 [16, 17]。\n*   **RAFT (Retrieval-Augmented Fine-Tuning)**：该论文提出了一种针对特定领域微调 LLM 的新范式，通过训练模型从干扰文档中提取正确 API 信息，有效解决了 Agent 在特定业务场景下的幻觉问题 [18, 19]。\n*   **GoEx (Gorilla Execution Engine)**：提出了 **LLM 生成动作的运行时环境**，具备“事后验证 (Post-facto Validation)”、“撤销 (Undo)”和“伤害约束 (Damage Confinement)”等安全机制，为全自动 Agent 的落地提供了安全保障 [17, 20]。\n\n### 3. 未解决的挑战\n\n*   **参数幻觉与高精度要求**：即使是顶级模型，在生成复杂工具的输入参数时仍存在幻觉风险，这在金融或生产控制场景下是不可接受的 [19]。\n*   **状态管理与长期记忆的复杂性**：在长周期的任务中，如何有效地维持和更新 Agent 的内部状态及记忆模块（Memory Module），并确保跨多轮交互的一致性，依然是一个难题 [1, 16, 21]。\n*   **推理延迟与成本的博弈**：虽然“深度思考”提高了准确性，但导致了显著的延迟增加（如某些模型延迟超过 30 秒），这限制了 Agent 在实时交互场景的应用 [5, 22]。\n\n### 4. 未来可能的突破点\n\n*   **自主纠错与自我进化**：未来的突破点在于 Agent 是否能通过 GoEx 类的运行时反馈进行**在线学习和自主纠错**，从而在无需人工干预的情况下完成任务 [17]。\n*   **多智能体编排 (Multi-Agent Orchestration) 的普及**：从单智能体转向多智能体（如研究员、写作者、审核员）协作模式。通过事件驱动的底层架构（如 AutoGen Core 或 LangGraph），实现更复杂、更受控的业务流程 [23, 24]。\n*   **从“工具增强”到“工具导向”的范式转变**：模型将不再是仅仅被工具增强，而是作为**原生的工具导向型大脑**，能够自主学习如何通过组合各种原子化的 API 来创造新的工作流 [25]。",
    "conversation_id": "f97c9bd5-b5bd-40d9-b4c7-5f7173fd585f",
    "sources_used": [
      "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "e9400d2f-22c2-476b-8bfa-292662063768",
      "3a08567b-3003-4501-94a1-7a0d3b200873",
      "5d860664-3c42-434c-85d9-52ba7b008def",
      "23d4ae25-c078-4c24-825f-676b34bd530d",
      "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
      "a48d217e-2c80-405c-90aa-3213a16edf40",
      "f3cba5cb-ea4c-4dcb-90b0-8a28817ee32c"
    ],
    "citations": {
      "1": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
      "2": "e9400d2f-22c2-476b-8bfa-292662063768",
      "3": "3a08567b-3003-4501-94a1-7a0d3b200873",
      "4": "5d860664-3c42-434c-85d9-52ba7b008def",
      "5": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "6": "5d860664-3c42-434c-85d9-52ba7b008def",
      "7": "5d860664-3c42-434c-85d9-52ba7b008def",
      "8": "5d860664-3c42-434c-85d9-52ba7b008def",
      "9": "5d860664-3c42-434c-85d9-52ba7b008def",
      "10": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "11": "e9400d2f-22c2-476b-8bfa-292662063768",
      "12": "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "13": "5d860664-3c42-434c-85d9-52ba7b008def",
      "14": "e9400d2f-22c2-476b-8bfa-292662063768",
      "15": "e9400d2f-22c2-476b-8bfa-292662063768",
      "16": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "17": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "18": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "19": "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
      "20": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "21": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
      "22": "23d4ae25-c078-4c24-825f-676b34bd530d",
      "23": "a48d217e-2c80-405c-90aa-3213a16edf40",
      "24": "b717658c-57b7-4b5b-9367-7bd1fd456082",
      "25": "f3cba5cb-ea4c-4dcb-90b0-8a28817ee32c"
    },
    "references": [
      {
        "source_id": "1d71ee39-c97f-4f65-b54c-2c46e9aac93e",
        "citation_number": 1,
        "cited_text": "Install MCP Server MCP Docs Copy MCP URL Install in Cursor Copy Claude Code command Copy Codex config LlamaIndex Framework Use Cases Agents Copy Markdown Open in Claude Open in ChatGPT Open in Cursor Copy Markdown View as Markdown Agents An “agent” is an automated reasoning and decision engine. It takes in a user input/query and can make internal decisions for executing that query in order to return the correct result. The key agent components can include, but are not limited to: Breaking down a complex question into smaller ones Choosing an external Tool to use + coming up with parameters for calling the Tool Planning out a set of tasks Storing previously completed tasks in a memory module"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 2,
        "cited_text": "You can also construct FunctionDeclarations from Python functions directly using types.FunctionDeclaration.from_callable(client=client, callable=your_function) . Function calling with thinking models Gemini 3 and 2.5 series models use an internal \"thinking\" process to reason through requests. This significantly improves function calling performance, allowing the model to better determine when to call a function and which parameters to use. Because the Gemini API is stateless, models use thought signatures to maintain context across multi-turn conversations."
      },
      {
        "source_id": "3a08567b-3003-4501-94a1-7a0d3b200873",
        "citation_number": 3,
        "cited_text": "Skip to main content 智谱AI开放文档  home page 使用指南 API 文档 场景示例 编码套餐 更新日志 条款与协议 常见问题 开始使用 平台介绍 模型概览 快速开始 核心参数 迁移至 GLM-5 模型介绍 模型能力 深度思考 思考模式 流式消息 工具流式输出 工具调用 上下文缓存 结构化输出 模型工具 GLM in Excel（Beta） 联网搜索 模型部署 模型微调 模型评测 批量处理 OCR 服务 GLM 全模态知识库 知识处理及检索 知识库服务计费 上下文增强技术报告 对话调用知识库 智能体 平台服务 智能体开发平台 提示词工程 内容安全 模型迁移 用户权益 模型备案 平台定位 平台优势 查看模型 极速体验 快速开始 开发指南 核心概念 开始使用 平台介绍 Z智谱·一站式大模型开发平台 平台定位 智谱大模型开放平台 bigmodel.cn ，提供功能丰富、灵活易用、高性价比的大模型 API 服务，支持智能体开发与模型精调、推理、评测等，致力于构建高效通用的“一站式模型即服务” AI 开发新范式。 平台优势 模型矩阵"
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 4,
        "cited_text": "Complete tool calling example python Complete tool calling example python Note that for reasoning models like GPT-5 or o4-mini, any reasoning items returned in model responses with tool calls must also be passed back with tool call outputs. Defining functions Functions are usually declared in the tools parameter of each API request. With tool search , your application can also load deferred functions later in the interaction. Either way, each callable function uses the same schema shape. A function definition has the following properties:"
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 5,
        "cited_text": "| ||| | Agentic || Multi Turn | Single Turn || Hallucination Measurement || Format Sensitivity || | || | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | ||| | Web Search | Memory | Multi turn | Non-live (AST) | Live (AST) | || || Latency (s) | || | Rank 🔼 | Overall Acc | Model | Cost ($) | Overall Acc | Base | No Snippet | Overall Acc | KV | Vector | Recursive Sum | Overall Acc | Base | Miss Func | Miss Param | Long Context | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Overall Acc | Simple | Multiple | Parallel | Multiple Parallel | Relevance | Irrelevance | Max Delta | SD | Mean | SD | P95 | Organization | License | | 1 | 77.47 | Claude-Opus-4-5-20251101 (FC) | 86.55 | 84.5 | 84 | 85 | 73.76 | 70.97 | 72.9 | 77.42 | 68.38 | 81 | 64 | 58 | 70.5 | 88.58 | 76.83 | 95.5 | 93.5 | 88.5 | 79.79 | 86.43 | 78.16 | 87.5 | 75 | 62.5 | 84.72 | N/A | N/A | 4.38 | 3.13 | 7.56 | Anthropic | Proprietary | | 2 | 73.24 | Claude-Sonnet-4-5-20250929 (FC) | 43.73 | 81 | 82 | 80 | 64.95 | 54.19 | 57.42 | 83.23 | 61.37 | 69 | 65 | 52.5 | 59 | 88.65 | 72.58 | 95.5 | 94.5 | 92 | 81.13 | 89.53 | 78.92 | 87.5 | 83.33 | 68.75 | 86.61 | N/A | N/A | 4.31 | 4.43 | 7.27 | Anthropic | Proprietary | | 3 | 72.51 | Gemini-3-Pro-Preview (Prompt) | 298.47 | 80 | 78 | 82 | 61.72 | 59.35 | 62.58 | 63.23 | 60.75 | 64.5 | 60 | 54.5 | 64 | 90.65 | 79.58 | 96 | 95 | 92 | 83.12 | 87.6 | 81.77 | 93.75 | 87.5 | 68.75 | 85.59 | 8.5 | 1.7 | 12.08 | 21.3 | 32.73 | Google | Proprietary | | 4 | 72.38 | GLM-4.6 (FC thinking) | 4.64 | 77.5 | 79 | 76 | 55.7 | 43.87 | 56.13 | 67.1 | 68 | 74.5 | 68 | 63 | 66.5 | 87.56 | 74.25 | 95 | 91.5 | 89.5 | 80.9 | 89.53 | 78.92 | 81.25 | 75 | 75 | 84.96 | N/A | N/A | 4.34 | 7.22 | 13.5 | Zhipu AI | MIT | | 5 | 69.57 | Grok-4-1-fast-reasoning (FC) | 17.26 | 82.5 | 82 | 83 | 53.98 | 41.29 | 57.42 | 63.23 | 58.87 | 70.5 | 59.5 | 43 | 62.5 | 88.27 | 77.58 | 93 | 92.5 | 90 | 78.46 | 84.11 | 77.3 | 75 | 70.83 | 81.25 | 79.43 | N/A | N/A | 6.74 | 12.78 | 17.57 | xAI | Proprietary | | 6 | 68.7 | Claude-Haiku-4-5-20251001 (FC) | 14.23 | 83.5 | 86 | 81 | 54.41 | 51.61 | 55.48 | 56.13 | 53.62 | 63.5 | 42.5 | 52.5 | 56 | 86.5 | 71 | 94 | 92.5 | 88.5 | 78.68 | 83.72 | 77.59 | 75 | 75 | 62.5 | 85.11 | N/A | N/A | 1.68 | 3.92 | 3.15 | Anthropic | Proprietary | | 7 | 68.14 | Gemini-3-Pro-Preview (FC) | 224.69 | 68.5 | 63 | 74 | 54.84 | 50.32 | 63.23 | 50.97 | 63.12 | 69 | 63 | 56.5 | 64 | 85.75 | 75.5 | 94 | 91 | 82.5 | 81.72 | 87.6 | 80.44 | 75 | 79.17 | 75 | 77.85 | N/A | N/A | 15.87 | 41.41 | 58.48 | Google | Proprietary | | 8 | 63.05 | o3-2025-04-16 (Prompt) | 234.64 | 50.5 | 51 | 50 | 51.83 | 33.55 | 50.32 | 71.61 | 62.25 | 68 | 63.5 | 54.5 | 63 | 81.94 | 74.25 | 89 | 86.5 | 78 | 73.21 | 83.33 | 70.75 | 75 | 70.83 | 93.75 | 83.98 | 8.5 | 2.75 | 4.83 | 7.01 | 11.7 | OpenAI | Proprietary | | 9 | 62.97 | Grok-4-0709 (Prompt) | 348.19 | 74 | 74 | 74 | 50.54 | 43.87 | 59.35 | 48.39 | 47 | 55.5 | 46 | 36 | 50.5 | 82.75 | 67 | 93.5 | 89 | 81.5 | 72.54 | 81.78 | 70.18 | 81.25 | 70.83 | 81.25 | 84.3 | 13.0 | 2.88 | 30.38 | 36.19 | 101.54 | xAI | Proprietary | | 10 | 61.38 | Grok-4-0709 (FC) | 355.17 | 82 | 80 | 84 | 55.91 | 57.42 | 58.71 | 51.61 | 33.88 | 44 | 19 | 28.5 | 44 | 85.38 | 73.5 | 92.5 | 88.5 | 87 | 75.57 | 82.17 | 73.88 | 75 | 79.17 | 87.5 | 75.4 | N/A | N/A | 15.49 | 26.22 | 44.28 | xAI | Proprietary | | 11 | 59.06 | Moonshotai-Kimi-K2-Instruct (FC) | 6.19 | 66.5 | 72 | 61 | 29.03 | 21.94 | 20 | 45.16 | 50.63 | 62 | 41 | 44.5 | 55 | 81.6 | 69.42 | 92 | 82 | 83 | 78.68 | 81.78 | 78.06 | 87.5 | 66.67 | 75 | 87.34 | N/A | N/A | 6.4 | 9.38 | 13.78 | MoonshotAI | modified-mit | | 12 | 58.29 | Grok-4-1-fast-non-reasoning (FC)"
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 6,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 7,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 8,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 9,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 10,
        "cited_text": "• Natural language command generation with multi-LLM fusion • Privacy-focused with explicit execution approval • Command history and interactive selection interface Gorilla API Zoo 📚 Dataset A community-maintained repository of up-to-date API documentation • Centralized, searchable index of APIs across domains • Structured documentation format with arguments, versioning, and examples • Community-driven updates to keep pace with API changes • Rich data source for model training and fine-tuning • Enables retrieval-augmented training and inference"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 11,
        "cited_text": "Model context protocol (MCP) Model Context Protocol (MCP) is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts. The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model."
      },
      {
        "source_id": "b717658c-57b7-4b5b-9367-7bd1fd456082",
        "citation_number": 12,
        "cited_text": "The current stable version can be found in the releases . If you are upgrading from AutoGen v0.2, please refer to the Migration Guide for detailed instructions on how to update your code and configurations. Quickstart The following samples call OpenAI API, so you first need to create an account and export your key as export OPENAI_API_KEY=\"sk-...\" . Hello World Create an assistant agent using OpenAI's GPT-4o model. See other supported models . MCP Server Create a web browsing assistant agent that uses the Playwright MCP server."
      },
      {
        "source_id": "5d860664-3c42-434c-85d9-52ba7b008def",
        "citation_number": 13,
        "cited_text": "Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 14,
        "cited_text": "Python Javascript More For models before the Gemini 3 series, use the Live API . Multimodal function responses Note: This feature is available for Gemini 3 series models. For Gemini 3 series models, you can include multimodal content in the function response parts that you send to the model. The model can process this multimodal content in its next turn to produce a more informed response. The following MIME types are supported for multimodal content in function responses: Images : image/png , image/jpeg , image/webp Documents : application/pdf , text/plain"
      },
      {
        "source_id": "e9400d2f-22c2-476b-8bfa-292662063768",
        "citation_number": 15,
        "cited_text": "To include multimodal data in a function response, include it as one or more parts nested within the functionResponse part. Each multimodal part must contain inlineData . If you reference a multimodal part from within the structured response field, it must contain a unique displayName . You can also reference a multimodal part from within the structured response field of the functionResponse part by using the JSON reference format {\"$ref\": \"<displayName>\"} . The model substitutes the reference with the multimodal content when processing the response. Each displayName can only be referenced once in the structured response field."
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 16,
        "cited_text": "Berkeley Function Calling Leaderboard (BFCL) V4 Home Blog Try it Out! Leaderboard Berkeley Function-Calling Leaderboard BFCL: From Tool Use to Agentic Evaluation of Large Language Models The Berkeley Function Calling Leaderboard (BFCL) V4 evaluates the LLM's ability to call functions (aka tools) accurately. This leaderboard consists of real-world data and will be updated periodically. For more information on the evaluation dataset and methodology, please refer to our blogs: BFCL-v1 introducing AST as an evaluation metric, BFCL-v2 introducing enterprise and OSS-contributed functions, BFCL-v3 introducing multi-turn interactions, and BFCL-v4 introducing holistic agentic evaluation. Checkout code and data ."
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 17,
        "cited_text": "Repository files navigation README Apache-2.0 license Gorilla: Large Language Model Connected with Massive APIs Latest Updates 📢 Check out our detailed Berkeley Function Calling Leaderboard changelog (Last updated: ) for the latest dataset / model updates to the Berkeley Function Calling Leaderboard! 🤖 [07/17/2025] Announcing BFCL V4 Agentic! As function-calling forms the bedrock of Agentic systems, BFCL V4 Agentic benchmark focuses on tool-calling in real-world agentic settings, featuring web search with multi-hop reasoning and error recovery, agent memory management, and format sensitivity evaluation. [ Web-search Blog ] [ Memory Blog ] [ Format Sensitivity Blog ] [ PR ] [ Tweet ] 🎯 [10/04/2024] Introducing the Agent Arena by Gorilla X LMSYS Chatbot Arena! Compare different agents in tasks like search, finance, RAG, and beyond. Explore which models and tools work best for specific tasks through our novel ranking system and community-driven prompt hub. [ Blog ] [ Arena ] [ Leaderboard ] [ Dataset ] [ Tweet ] 📣 [09/21/2024] Announcing BFCL V3 - Evaluating multi-turn and multi-step function calling capabilities! New state-based evaluation system tests models on handling complex workflows, sequential functions, and service states. [ Blog ] [ Leaderboard ] [ Code ] [ Tweet ] 🚀 [08/20/2024] Released BFCL V2 • Live! The Berkeley Function-Calling Leaderboard now features enterprise-contributed data and real-world scenarios. [ Blog ] [ Live Leaderboard ] [ V2 Categories Leaderboard ] [ Tweet ] ⚡ [04/12/2024] Excited to release GoEx - a runtime for LLM-generated actions like code, API calls, and more. Featuring \"post-facto validation\" for assessing LLM actions after execution, \"undo\" and \"damage confinement\" abstractions to manage unintended actions & risks. This paves the way for fully autonomous LLM agents, enhancing interaction between apps & services with human-out-of-loop. [ Blog ] [ Code ] [ Paper ] [ Tweet ] ⏰ [04/01/2024] Introducing cost and latency metrics into Berkeley function calling leaderboard ! 🚀 [03/15/2024] RAFT: Adapting Language Model to Domain Specific RAG is live! [ MSFT-Meta blog ] [ Berkeley Blog ] 🏆 [02/26/2024] Berkeley Function Calling Leaderboard is live! 🎯 [02/25/2024] OpenFunctions v2 sets new SoTA for open-source LLMs! 🔥 [11/16/2023] Excited to release Gorilla OpenFunctions 💻 [06/29/2023] Released gorilla-cli , LLMs for your CLI! 🟢 [06/06/2023] Released Commercially usable, Apache 2.0 licensed Gorilla models 🚀 [05/30/2023] Provided the CLI interface to chat with Gorilla! 🚀 [05/28/2023] Released Torch Hub and TensorFlow Hub Models! 🚀 [05/27/2023] Released the first Gorilla model! or 🤗 ! 🔥 [05/27/2023] We released the APIZoo contribution guide for community API contributions! 🔥 [05/25/2023] We release the APIBench dataset and the evaluation code of Gorilla!"
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 18,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "4f8b26f8-c4a2-4c3d-8c61-0d7e99bdbbec",
        "citation_number": 19,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 20,
        "cited_text": "• Head-to-head agent comparisons with ELO rating system • Framework compatibility testing (LangChain, AutoGPT) • Community-driven evaluation platform • Real-world task performance metrics Gorilla Execution Engine (GoEx) 🔧 Infra Runtime for executing LLM-generated actions with safety guarantees • Post-facto validation for verifying LLM actions after execution • Undo capabilities and damage confinement for risk mitigation • OAuth2 and API key authentication for multiple services • Support for RESTful APIs, databases, and filesystem operations"
      },
      {
        "source_id": "74a766c3-b4e3-4798-9f63-d7190ea4e195",
        "citation_number": 21,
        "cited_text": "📊 Evaluation 🏆 Leaderboard 🔧 Function Calling Infra 📚 Dataset Comprehensive evaluation of function-calling capabilities • V1: Expert-curated dataset for evaluating single-turn function calling • V2: Enterprise-contributed data for real-world scenarios • V3: Multi-turn & multi-step function calling evaluation • Cost and latency metrics for all models • Interactive API explorer for testing • Community-driven benchmarking platform Agent Arena 📊 Evaluation 🏆 Leaderboard Compare LLM agents across models, tools, and frameworks"
      },
      {
        "source_id": "23d4ae25-c078-4c24-825f-676b34bd530d",
        "citation_number": 22,
        "cited_text": "| 16.27 | 75 | 74 | 76 | 26.24 | 20.65 | 20 | 38.06 | 46.75 | 58 | 39.5 | 37.5 | 52 | 88.13 | 76 | 93 | 93 | 90.5 | 77.94 | 82.95 | 76.92 | 75 | 70.83 | 81.25 | 74.09 | N/A | N/A | 2.29 | 7.31 | 5.34 | xAI | Proprietary | | 13 | 57.06 | Command A Reasoning (FC) | 3.04 | 55.5 | 65 | 46 | 28.82 | 16.13 | 23.87 | 46.45 | 50.12 | 61.5 | 41 | 49.5 | 48.5 | 86.27 | 73.58 | 93.5 | 89.5 | 88.5 | 78.61 | 80.23 | 78.35 | 75 | 75 | 68.75 | 86.75 | N/A | N/A | 3.44 | 4.91 | 8.39 | Cohere | CC-BY-NC 4.0 License (w/ Acceptable Use Addendum) | | 14 | 56.73 | DeepSeek-V3.2-Exp (Prompt + Thinking) | 57.75 | 58 | 64 | 52 | 44.09 | 46.45 | 46.45 | 39.35 | 44.88 | 55 | 49 | 27 | 48.5 | 85.52 | 74.08 | 92 | 89.5 | 86.5 | 76.02 | 82.56 | 74.74 | 87.5 | 54.17 | 93.75 | 67 | 10.0 | 2.77 | 37.89 | 49.56 | 102.09 | DeepSeek | MIT | | 15 | 56.24 | Gemini-2.5-Flash (FC) | 26.36 | 59 | 59 | 59 | 41.29 | 19.35 | 50.32 | 54.19 | 36.25 | 41.5 | 36 | 32 | 35.5 | 84.96 | 74.33 | 92 | 94 | 79.5 | 74.39 | 85.27 | 71.7 | 81.25 | 70.83 | 75 | 93.67 | N/A | N/A | 2.99 | 9.22 | 5.62 | Google | Proprietary | | 16 | 55.87 | GPT-5.2-2025-12-11 (FC) | 85.65 | 75.5 | 78 | 73 | 45.81 | 33.55 | 43.23 | 60.65 | 28.12 | 36.5 | 18 | 27.5 | 30.5 | 81.85 | 72.92 | 88 | 89 | 77.5 | 70.39 | 71.71 | 70.37 | 68.75 | 58.33 | 75 | 79.42 | N/A | N/A | 2.23 | 9.75 | 5.26 | OpenAI | Proprietary | | 17 | 55.46 | GPT-5-mini-2025-08-07 (FC) | 22.18 | 82 | 87 | 77 | 44.3 | 36.77 | 43.87 | 52.26 | 27.5 | 36.5 | 17 | 23.5 | 33 | 69.85 | 59.92 | 69 | 80 | 70.5 | 58.62 | 62.02 | 58.02 | 62.5 | 45.83 | 62.5 | 91.01 | N/A | N/A | 8.32 | 17.35 | 19.8 | OpenAI | Proprietary | | 18 | 54.66 | xLAM-2-32b-fc-r (FC) | 6.0 | 25.5 | 37 | 14 | 20.86 | 6.45 | 10.32 | 45.81 | 69.5 | 81.5 | 72.5 | 67.5 | 56.5 | 89.6 | 80.42 | 94 | 93 | 91 | 75.5 | 82.17 | 74.64 | 50 | 58.33 | 81.25 | 80.23 | N/A | N/A | 6.94 | 8.21 | 17.66 | Salesforce | cc-by-nc-4.0 | | 19 | 54.12 | DeepSeek-V3.2-Exp (FC) | 6.71 | 69.5 | 80 | 59 | 54.19 | 41.94 | 61.29 | 59.35 | 37.38 | 41.5 | 39.5 | 33.5 | 35 | 34.85 | 37.92 | 74 | 15 | 12.5 | 53.66 | 66.28 | 51.66 | 25 | 25 | 37.5 | 93.18 | N/A | N/A | 5.83 | 11.71 | 10.59 | DeepSeek | MIT | | 20 | 53.96 | GPT-4.1-2025-04-14 (FC) | 100.75 | 68 | 67 | 69 | 23.87 | 16.13 | 18.06 | 37.42 | 38.88 | 47.5 | 32.5 | 32.5 | 43 | 82.79 | 72.67 | 89 | 88 | 81.5 | 69.95 | 69.38 | 70.28 | 56.25 | 70.83 | 87.5 | 86.52 | N/A | N/A | 1.63 | 3.05 | 4.01 | OpenAI | Proprietary | | 21 | 53.24 | o4-mini-2025-04-16 (FC) | 81.91 | 75.5 | 75 | 76 | 34.19 | 19.35 | 24.52 | 58.71 | 41.75 | 51 | 30 | 40.5 | 45.5 | 37.73 | 66.92 | 84 | 0 | 0 | 66.1 | 69.38 | 67.81 | 0 | 0 | 81.25 | 83.91 | N/A | N/A | 3.71 | 7.18 | 9.33 | OpenAI | Proprietary | | 22 | 53.07 | xLAM-2-70b-fc-r (FC) | 25.1 | 15 | 17 | 13 | 14.41 | 2.58 | 10.97 | 29.68 | 77.38 | 82.5 | 77 | 74 | 76 | 88.44 | 78.25 | 94 | 92 | 89.5 | 72.17 | 77.91 | 71.13 | 68.75 | 58.33 | 75 | 79.11 | N/A | N/A | 28.06 | 68.77 | 91.21 | Salesforce | cc-by-nc-4.0 | | 23 | 52.15 | Qwen3-235B-A22B-Instruct-2507 (Prompt) | 3.12 | 50.5 | 56 | 45 | 19.35 | 12.9 | 11.61 | 33.55 | 44.62 | 54 | 42.5 | 31.5 | 50.5 | 90.33 | 79.83 | 95 | 95.5 | 91 | 78.68 | 82.95 | 77.78 | 81.25 | 70.83 | 93.75 | 78.89 | 8.0 | 1.95 | 2.56 | 2.75 | 7.61 | Qwen | apache-2.0 | | 24 | 51.45 | GPT-5-nano-2025-08-07 (FC) | 8.79 | 72.5 | 74 | 71 | 24.73 | 18.06 | 27.1 | 29.03 | 34.5 | 44 | 23.5 | 32.5 | 38 | 68 | 57 | 64.5 | 79 | 71.5 | 59.44 | 58.91 | 59.83 | 50 | 54.17 | 75 | 89.1 | N/A | N/A | 10.36 | 10.37 | 23.56 | OpenAI | Proprietary | | 25 | 51.4 | Nanbeige4-3B-Thinking-2511 (FC) | 14.14 | 21.5 | 31 | 12 | 36.77 | 31.61 | 34.19 | 44.52 | 51.12 | 58.5 | 54 | 45 | 47 | 81.58 | 63.83 | 93.5 | 84.5 | 84.5 | 79.42 | 86.05 | 78.06 | 75 | 70.83 | 75 | 83.09 | N/A | N/A | 13.46 | 26.41 | 37.45 | Nanbeige | apache-2.0 | | 26 | 50.9 | Gemini-2.5-Flash (Prompt)"
      },
      {
        "source_id": "a48d217e-2c80-405c-90aa-3213a16edf40",
        "citation_number": 23,
        "cited_text": "If you're looking for more advanced customization or agent orchestration, check out LangGraph , our framework for building controllable agent workflows. Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangChain ecosystem While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. Deep Agents — Build agents that can plan, use subagents, and leverage file systems for complex tasks LangGraph — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework Integrations — Chat & embedding models, tools & toolkits, and more LangSmith — Agent evals, observability, and debugging for LLM apps LangSmith Deployment — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows"
      },
      {
        "source_id": "b717658c-57b7-4b5b-9367-7bd1fd456082",
        "citation_number": 24,
        "cited_text": "Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components. Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "f3cba5cb-ea4c-4dcb-90b0-8a28817ee32c",
        "citation_number": 25,
        "cited_text": "View a PDF of the paper titled Tool Learning with Foundation Models, by Yujia Qin and 40 other authors View PDF HTML (experimental) Abstract: Humans possess an extraordinary ability to create and utilize tools, allowing them to overcome physical limitations and explore new frontiers. With the advent of foundation models, AI systems have the potential to be equally adept in tool use as humans. This paradigm, i.e., tool learning with foundation models, combines the strengths of specialized tools and foundation models to achieve enhanced accuracy, efficiency, and automation in problem-solving. Despite its immense potential, there is still a lack of a comprehensive understanding of key challenges, opportunities, and future endeavors in this field. To this end, we present a systematic investigation of tool learning in this paper. We first introduce the background of tool learning, including its cognitive origins, the paradigm shift of foundation models, and the complementary roles of tools and models. Then we recapitulate existing tool learning research into tool-augmented and tool-oriented learning. We formulate a general tool learning framework: starting from understanding the user instruction, models should learn to decompose a complex task into several subtasks, dynamically adjust their plan through reasoning, and effectively conquer each sub-task by selecting appropriate tools. We also discuss how to train models for improved tool-use capabilities and facilitate the generalization in tool learning. Considering the lack of a systematic tool learning evaluation in prior works, we experiment with 18 representative tools and show the potential of current foundation models in skillfully utilizing tools. Finally, we discuss several open problems that require further investigation for tool learning. In general, we hope this paper could inspire future research in integrating tools with foundation models."
      }
    ]
  }
}
