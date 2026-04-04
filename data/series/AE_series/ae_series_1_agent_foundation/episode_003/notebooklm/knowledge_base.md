# 知识库：第一个 Agent：用纯 Python + API 从零构建

生成时间: 2026-04-03 10:16
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "基于您提供的来源，构建「第一个 Agent：用纯 Python + API 从零构建」的核心技术架构主要围绕**代理循环（Agentic Loop）**展开，旨在通过 Python 代码手动管理模型与外部工具之间的交互。\n\n以下是该架构的技术演进、核心组件及关键指标的概述：\n\n### 1. 技术演进路线\nAgent 技术经历了从单一任务生成到复杂环境交互的演变：\n*   **初期阶段：ReAct 范式。** 核心思想是协同「推理」（Reasoning）与「行动」（Acting）[1]。模型在生成文本时交替产生推理痕迹和特定任务的操作，利用外部 API（如 Wikipedia）获取实时信息以减少幻觉 [1]。\n*   **自学阶段：Toolformer。** 模型开始学习如何决定调用哪些 API、何时调用、传递什么参数以及如何整合结果 [2]。\n*   **平台化阶段：从 Assistants API 转向 Responses API。** 演进路线从由平台托管状态（Assistants API）转向由开发者在 Python 端手动控制编排逻辑（Responses API），从而获得更高的灵活性和可移植性 [3, 4]。\n*   **标准化阶段：MCP 协议。** 引入模型上下文协议（Model Context Protocol），为 AI 助手与数据源（如 GitHub、Slack）之间建立通用的、标准化的双向连接 [5, 6]。\n\n### 2. 核心算法名称\n*   **ReAct 算法：** 该架构的灵魂，通过在生成序列中嵌入思考（Thought）、行动（Action）和观察（Observation）的循环，使模型具备逻辑推理和环境反馈能力 [1]。\n*   **Toolformer：** 一种自监督训练方法，使模型能够自主学习 API 的调用时机和方式 [2]。\n*   **链式思考（Chain-of-Thought）：** 作为 ReAct 的前置基础，用于在执行行动前生成逻辑步骤 [1]。\n\n### 3. 主要架构模式：代理循环（Agentic Loop）\n纯 Python + API 构建的 Agent 通常采用**显式状态编排模式** [4, 7]：\n*   **编排器（Orchestrator）：** 由 Python 代码担任，负责管理对话历史（Conversation State）、修剪上下文（History Pruning）和处理重试逻辑（Retries） [4]。\n*   **提示词（Prompts）：** 被视为一种「版本化行为配置」，封装了模型选择、指令规范和工具声明 [8, 9]。\n*   **工具调用流程（The Tool Calling Flow）：**\n    1.  **初始请求：** Python 调用模型 API 并附带工具描述（JSON Schema） [7, 10]。\n    2.  **触发调用：** 模型判断需要外部信息，返回 `tool_calls` 对象而非普通文本 [11-13]。\n    3.  **本地执行：** Python 解析参数，在本地环境执行相应函数（如 SQL 查询、搜索） [7, 10, 12]。\n    4.  **结果反馈：** 将工具输出（Tool Output）通过 API 发回模型 [7, 10]。\n    5.  **生成最终响应：** 模型整合所有信息，给出用户答案 [7, 14]。\n\n### 4. 关键组件\n*   **工具（Tools/Functions）：** 通过 JSON Schema 定义，包含函数名、描述和参数约束（如 `strict: true` 确保模式一致性） [15, 16]。\n*   **对话（Conversations）：** 代替了旧版的「线程」，作为一种「项」（Items）的流，可以存储消息、工具调用及其输出 [8, 17]。\n*   **上下文管理（Context Management）：** 包含 Token 计数、提示词缓存（Prompt Caching）和上下文压缩（Compaction） [18, 19]。\n*   **传输层（Transports）：** 支持 stdio、SSE 或 Streamable HTTP 等标准化传输方式（尤其是 MCP 架构下） [20, 21]。\n\n### 5. 关键技术指标\n*   **模式一致性（Strict Mode）：** 通过设置 `strict: true`，确保模型生成的函数调用 100% 符合定义的 JSON Schema [16, 22]。\n*   **并发能力（Parallel Function Calling）：** 模型在单次交互中支持同时调用多个函数（如同时查询三个城市的天气） [23, 24]。\n*   **Token 成本：** 工具定义本身会被注入系统消息中，计入输入 Token；工具返回的结果同样计入输入 Token [25, 26]。\n*   **执行延迟：** 对于推理模型（Reasoning Models），可能需要更高的推理努力（Reasoning Effort）来确保复杂工具调用的准确性 [27, 28]。\n\n如果您希望深入了解如何实现特定功能的 Agent（例如基于数据库查询的 Agent），我可以为您演示具体的 Python 代码逻辑。",
    "conversation_id": "12473243-78e3-4528-809d-514057372f09",
    "sources_used": [
      "d5221585-f4ba-4631-aac4-933e154a5d24",
      "b4d8fc62-79c9-4866-9f3a-17d9234481dd",
      "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "f41ff146-4c65-4b00-8020-849dd93d6594",
      "846ddb0d-a14f-400c-997f-b253c39b7a2c"
    ],
    "citations": {
      "1": "d5221585-f4ba-4631-aac4-933e154a5d24",
      "2": "b4d8fc62-79c9-4866-9f3a-17d9234481dd",
      "3": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "4": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "5": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "6": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "7": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "8": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "9": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "10": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "11": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "12": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "13": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "14": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "15": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "16": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "17": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "18": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "19": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "20": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "21": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "22": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "23": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "24": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "25": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "26": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "27": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "28": "8176a84a-7bef-4f48-8b5a-dbed30dafe19"
    },
    "references": [
      {
        "source_id": "d5221585-f4ba-4631-aac4-933e154a5d24",
        "citation_number": 1,
        "cited_text": "arXiv:2210.03629 (cs) [Submitted on 6 Oct 2022 ( v1 ), last revised 10 Mar 2023 (this version, v3)] Title: ReAct: Synergizing Reasoning and Acting in Language Models Authors: Shunyu Yao , Jeffrey Zhao , Dian Yu , Nan Du , Izhak Shafran , Karthik Narasimhan , Yuan Cao View a PDF of the paper titled ReAct: Synergizing Reasoning and Acting in Language Models, by Shunyu Yao and 6 other authors View PDF Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: this https URL"
      },
      {
        "source_id": "b4d8fc62-79c9-4866-9f3a-17d9234481dd",
        "citation_number": 2,
        "cited_text": "arXiv:2302.04761 (cs) [Submitted on 9 Feb 2023] Title: Toolformer: Language Models Can Teach Themselves to Use Tools Authors: Timo Schick , Jane Dwivedi-Yu , Roberto Dessì , Roberta Raileanu , Maria Lomeli , Luke Zettlemoyer , Nicola Cancedda , Thomas Scialom View a PDF of the paper titled Toolformer: Language Models Can Teach Themselves to Use Tools, by Timo Schick and 7 other authors View PDF Abstract: Language models (LMs) exhibit remarkable abilities to solve new tasks from just a few examples or textual instructions, especially at scale. They also, paradoxically, struggle with basic functionality, such as arithmetic or factual lookup, where much simpler and smaller models excel. In this paper, we show that LMs can teach themselves to use external tools via simple APIs and achieve the best of both worlds. We introduce Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each API. We incorporate a range of tools, including a calculator, a Q&A system, two different search engines, a translation system, and a calendar. Toolformer achieves substantially improved zero-shot performance across a variety of downstream tasks, often competitive with much larger models, without sacrificing its core language modeling abilities."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 3,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 4,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 5,
        "cited_text": "Introducing the Model Context Protocol \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing the Model Context Protocol Nov 25, 2024 Today, we're open-sourcing the Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments. Its aim is to help frontier models produce better, more relevant responses."
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 6,
        "cited_text": "As AI assistants gain mainstream adoption, the industry has invested heavily in model capabilities, achieving rapid advances in reasoning and quality. Yet even the most sophisticated models are constrained by their isolation from data—trapped behind information silos and legacy systems. Every new data source requires its own custom implementation, making truly connected systems difficult to scale. MCP addresses this challenge. It provides a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol. The result is a simpler, more reliable way to give AI systems access to the data they need."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 7,
        "cited_text": "The tool calling flow Tool calling is a multi-step conversation between your application and a model via the OpenAI API. The tool calling flow has five high level steps: Make a request to the model with tools it could call Receive a tool call from the model Execute code on the application side with input from the tool call Make a second request to the model with the tool output Receive a final response from the model (or more tool calls) Function tool example Let's look at an end-to-end tool calling flow for a get_horoscope function that gets a daily horoscope for an astrological sign."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 8,
        "cited_text": "What's changed? <cited_table> From assistants to prompts Assistants were persistent API objects that bundled model choice, instructions, and tool declarations—created and managed entirely through the API. Their replacement, prompts, can only be created in the dashboard, where you can version them as you develop your product.",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Before",
              "Now",
              "Why?"
            ],
            [
              "Assistants",
              "Prompts",
              "Prompts hold configuration (model, tools, instructions) and are easier to version and update"
            ],
            [
              "Threads",
              "Conversations",
              "Streams of items instead of just messages"
            ],
            [
              "Runs",
              "Responses",
              "Responses send input items or use a conversation object and receive output items; tool call loops are explicitly managed"
            ],
            [
              "Run steps",
              "Items",
              "Generalized objects—can be messages, tool calls, outputs, and more"
            ]
          ]
        }
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 9,
        "cited_text": "Practical migration steps Identify each existing Assistant's instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 10,
        "cited_text": "Steps to invoke a function call using Chat Completions API: Step 1 : Prompt the model with content that may result in model selecting a tool to use. The description of the tools such as a function name and signature is defined in the 'Tools' list and passed to the model in API call. If selected, the function name and parameters are included in the response. Step 2 : Check programmatically if model wanted to call a function. If true, proceed to step 3. Step 3 : Extract the function name and parameters from response, call the function with parameters. Append the result to messages."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 11,
        "cited_text": "Tool calls - requests from the model to use tools A function call or tool call refers to a special kind of response we can get from the model if it examines a prompt, and then determines that in order to follow the instructions in the prompt, it needs to call one of the tools we made available to it. If the model receives a prompt like “what is the weather in Paris?” in an API request, it could respond to that prompt with a tool call for the get_weather tool, with Paris as the location argument. Tool call outputs - output we generate for the model"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 12,
        "cited_text": "Handling function calls When the model calls a function, you must execute it and return the result. Since model responses can include zero, one, or multiple calls, it is best practice to assume there are several. The response has an array of tool_calls , each with an id (used later to submit the function result) and a function containing a name and JSON-encoded arguments . Sample response with multiple function calls Execute function calls and append results python The response output array contains an entry with the type having a value of function_call . Each entry with a call_id (used later to submit the function result), name , and JSON-encoded arguments ."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 13,
        "cited_text": "This notebook covers how to use the Chat Completions API in combination with external functions to extend the capabilities of GPT models. tools is an optional parameter in the Chat Completion API which can be used to provide function specifications. The purpose of this is to enable models to generate function arguments which adhere to the provided specifications. Note that the API will not actually execute any function calls. It is up to developers to execute function calls using model outputs. Within the tools parameter, if the functions parameter is provided then by default the model will decide when it is appropriate to use one of the functions. The API can be forced to use a specific function by setting the tool_choice parameter to {\"type\": \"function\", \"function\": {\"name\": \"my_function\"}} . The API can also be forced to not use any function by setting the tool_choice parameter to \"none\" . If a function is used, the output will contain \"finish_reason\": \"tool_calls\" in the response, as well as a tool_calls object that has the name of the function and the generated function arguments."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 14,
        "cited_text": "For functions that return images or files, you can pass an array of image or file objects instead of a string. If your function has no return value (e.g. send_email ), simply return a string that indicates success or failure. (e.g. \"success\" ) Incorporating results into response After appending the results to your messages , you can send them back to the model to get a final response. Send results back to model python After appending the results to your input , you can send them back to the model to get a final response."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 15,
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
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 16,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 17,
        "cited_text": "A thread was a collection of messages stored server-side. Threads could only store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data. Request example Thread object Conversation object Response example Thread object Conversation object From runs to responses Runs were asynchronous processes that executed against threads. See the example below. Responses are simpler: provide a set of input items to execute, and get a list of output items back. Responses are designed to be used alone, but you can also use them with prompt and conversation objects for storing context and configuration."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 18,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 19,
        "cited_text": "Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices"
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 20,
        "cited_text": "Overview The Model Context Protocol allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction. This Python SDK implements the full MCP specification, making it easy to: Build MCP clients that can connect to any MCP server Create MCP servers that expose resources, prompts and tools Use standard transports like stdio, SSE, and Streamable HTTP Handle all MCP protocol messages and lifecycle events Installation"
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 21,
        "cited_text": "Streamable HTTP Transport Note : Streamable HTTP transport is the recommended transport for production deployments. Use stateless_http=True and json_response=True for optimal scalability. Full example: examples/snippets/servers/streamable_config.py You can mount multiple FastMCP servers in a Starlette application: Full example: examples/snippets/servers/streamable_starlette_mount.py For low level server with Streamable HTTP implementations, see: Stateful server: examples/servers/simple-streamablehttp/ Stateless server: examples/servers/simple-streamablehttp-stateless/"
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 22,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 23,
        "cited_text": "Parallel function calling Parallel function calling is not possible when using built-in tools . The model may choose to call multiple functions in a single turn. You can prevent this by setting parallel_tool_calls to false , which ensures exactly zero or one tool is called. Note: Currently, if you are using a fine tuned model and the model calls multiple functions in one turn then strict mode will be disabled for those calls. Note for gpt-4.1-nano-2025-04-14 : This snapshot of gpt-4.1-nano can sometimes include multiple tools calls for the same tool if parallel tool calls are enabled. It is recommended to disable this feature when using this nano snapshot."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 24,
        "cited_text": "Parallel Function Calling Newer models such as gpt-5, gpt-4.1 or gpt-4o can call multiple functions in one turn. How to call functions with model generated arguments In our next example, we'll demonstrate how to execute functions whose inputs are model-generated, and use this to implement an agent that can answer questions for us about a database. For simplicity we'll use the Chinook sample database . Note: SQL generation can be high-risk in a production environment since models are not perfectly reliable at generating correct SQL."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 25,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 26,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 27,
        "cited_text": "Use rules to combine tokens, not to steer regex internals Good rule usage example: Treat whitespace explicitly Don't rely on open-ended %ignore directives. Using unbounded ignore directives may cause the grammar to be too complex and/or may cause the model to go out of distribution. Prefer threading explicit terminals wherever whitespace is allowed. Troubleshooting If the API rejects the grammar because it is too complex, simplify the rules and terminals and remove unbounded %ignore s. If custom tools are called with unexpected tokens, confirm terminals aren't overlapping; check greedy lexer. When the model drifts “out‑of‑distribution” (shows up as the model producing excessively long or repetitive outputs, it is syntactically valid but is semantically wrong): Tighten the grammar. Iterate on the prompt (add few-shot examples) and tool description (explain the grammar and instruct the model to reason and conform to it). Experiment with a higher reasoning effort (e.g, bump from medium to high)."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 28,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "构建一个基于纯 Python 和 API 的 Agent，其核心在于**从「单次请求-响应模型」转向「具有状态和工具调用能力的循环系统」**。以下是根据来源对该系统的实现细节、架构及优化策略的深度解析。\n\n### 1. 核心算法流程：ReAct 范式与代理循环\nAgent 的底层逻辑由 **ReAct（Reasoning and Acting）算法** 驱动，它将推理和行动协同起来 [1]。\n\n*   **五步循环流程（The Tool Calling Flow）**：\n    1.  **初始请求**：Python 程序向模型发送 Prompt，并附带一组工具定义（JSON Schema）[2, 3]。\n    2.  **模型决策**：模型判断是否需要外部工具。若需要，它会生成一个 **`tool_calls`** 对象，其中包含 `call_id`、函数名及生成的 JSON 参数 [4, 5]。\n    3.  **本地执行（Action）**：Python 程序拦截该调用，解析参数，并在本地环境运行实际的函数（如 SQL 查询、文件读写）[2, 3]。\n    4.  **结果回传（Observation）**：将工具执行的输出（Tool Output）通过 `tool_result` 消息发回给模型，必须携带对应的 `call_id` 以维持上下文对应关系 [2, 6]。\n    5.  **最终推理（Thought）**：模型根据工具反馈的信息进行最后的推理，并给出用户答案，或者开启新一轮的工具调用循环 [1, 2]。\n\n### 2. 关键代码架构：解耦与编排\n在纯 Python 实现中，架构的核心是**编排器（Orchestrator）**，它负责管理状态，而非依赖平台托管 [7]。\n\n*   **工具定义层**：通过 JSON Schema 显式定义工具。关键参数包括 `name`（函数名）、`description`（模型判断何时调用的依据）和 `parameters`（参数约束）[8]。\n*   **状态管理层（Conversations vs. Threads）**：架构从旧版的「线程（Threads）」转向**「对话项流（Streams of Items）」**。这意味着 Python 代码需要手动维护 `messages` 列表，处理消息、工具调用、工具输出这三者的时序 [9, 10]。\n*   **Prompt 行为配置**：将 Prompt 视为**「版本化行为规范」**。Python 逻辑负责任务流转（如重试、历史修剪），而 Prompt 负责定义高层指令、工具可用性和输出结构 [7, 11]。\n\n### 3. 性能优化策略\n为确保 Agent 在生产环境中的可靠性，需要实施以下优化：\n\n*   **模式一致性保证（Strict Mode）**：在工具定义中开启 **`strict: true`**。这会强制模型生成的函数参数 100% 符合 JSON Schema，从而避免 Python 端在解析 JSON 时出错 [12, 13]。\n*   **并发执行（Parallel Function Calling）**：允许模型在单次交互中请求多个工具调用（例如同时查询三个城市的天气）。Python 端可以使用异步并发（如 `asyncio`）同时执行这些函数，大幅降低总延迟 [14, 15]。\n*   **上下文优化与缓存**：\n    *   **Prompt Caching（提示词缓存）**：将静态的系统指令和工具定义缓存，减少重复处理时间并降低成本 [7, 16]。\n    *   **工具数量控制**：建议初始可用的工具数量**少于 20 个**，以维持高准确率 [17]。\n*   **按需加载（Tool Search）**：对于拥有庞大工具库的系统，使用 **`tool_search`** 延迟加载工具。模型先搜索相关工具，再将其动态载入上下文，节省 Token 消耗 [18, 19]。\n\n### 4. 与竞品的技术对比及具体参数\n在构建 Agent 时，目前主要存在两种技术路线：**开发者自控（Responses API/SDK）**与**平台托管（Assistants API/Legacy）**。\n\n| 技术指标 | 纯 Python + API (Responses API) | 平台托管模式 (Assistants API) |\n| :--- | :--- | :--- |\n| **状态存储** | **开发者本地/数据库控制**，灵活性极高 [10, 20] | 服务器端持久化存储，黑盒化 [10, 20] |\n| **工具调用循环** | **显式管理（Explicitly Managed）**，代码可见 [9] | 隐式自动循环 [9] |\n| **启动成本（Token）** | **Claude 3.5/4.6 为 313-346 Tokens**（注入系统消息）[21] | 包含在平台基础服务费或 Token 中 [22] |\n| **架构协议** | **MCP (Model Context Protocol)** 标准化连接 [23] | 私有 API 协议 [20] |\n| **可移植性** | 高，同一套代码可用于 Chat 或 Realtime API [7] | 低，绑定特定 API 接口 [9] |\n\n**关键数据参考**：\n*   **ReAct 性能提升**：在 ALFWorld 决策基准测试中，ReAct 架构比单纯的强化学习方法在成功率上绝对提升了 **34%** [1]。\n*   **Token 消耗**：在 Claude 4.6 模型中，开启 `auto` 模式的工具调用会自动加载约 **346 个系统 Token** 用于启用 Agent 能力 [21]。\n*   **响应延迟优化**：通过使用 **Predicted Outputs（预测输出）** 和优先处理，可显著降低首字延迟 [24, 25]。\n\n这种纯 Python + API 的架构赋予了开发者对 Agent 执行细节的**绝对控制权**，使其能够自由实现复杂的重试逻辑、动态 Prompt 注入以及跨平台的状态同步 [7, 20]。",
    "conversation_id": "12473243-78e3-4528-809d-514057372f09",
    "sources_used": [
      "d5221585-f4ba-4631-aac4-933e154a5d24",
      "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
      "8a0e5adb-265f-4e62-9df5-79f354409a11"
    ],
    "citations": {
      "1": "d5221585-f4ba-4631-aac4-933e154a5d24",
      "2": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "3": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "4": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "5": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "6": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "7": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "8": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "9": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "10": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "11": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "12": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "13": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "14": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "15": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "16": "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
      "17": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "18": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "19": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "20": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "21": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "22": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "23": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "24": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "25": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98"
    },
    "references": [
      {
        "source_id": "d5221585-f4ba-4631-aac4-933e154a5d24",
        "citation_number": 1,
        "cited_text": "arXiv:2210.03629 (cs) [Submitted on 6 Oct 2022 ( v1 ), last revised 10 Mar 2023 (this version, v3)] Title: ReAct: Synergizing Reasoning and Acting in Language Models Authors: Shunyu Yao , Jeffrey Zhao , Dian Yu , Nan Du , Izhak Shafran , Karthik Narasimhan , Yuan Cao View a PDF of the paper titled ReAct: Synergizing Reasoning and Acting in Language Models, by Shunyu Yao and 6 other authors View PDF Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: this https URL"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 2,
        "cited_text": "The tool calling flow Tool calling is a multi-step conversation between your application and a model via the OpenAI API. The tool calling flow has five high level steps: Make a request to the model with tools it could call Receive a tool call from the model Execute code on the application side with input from the tool call Make a second request to the model with the tool output Receive a final response from the model (or more tool calls) Function tool example Let's look at an end-to-end tool calling flow for a get_horoscope function that gets a daily horoscope for an astrological sign."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 3,
        "cited_text": "Steps to invoke a function call using Chat Completions API: Step 1 : Prompt the model with content that may result in model selecting a tool to use. The description of the tools such as a function name and signature is defined in the 'Tools' list and passed to the model in API call. If selected, the function name and parameters are included in the response. Step 2 : Check programmatically if model wanted to call a function. If true, proceed to step 3. Step 3 : Extract the function name and parameters from response, call the function with parameters. Append the result to messages."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 4,
        "cited_text": "Tool calls - requests from the model to use tools A function call or tool call refers to a special kind of response we can get from the model if it examines a prompt, and then determines that in order to follow the instructions in the prompt, it needs to call one of the tools we made available to it. If the model receives a prompt like “what is the weather in Paris?” in an API request, it could respond to that prompt with a tool call for the get_weather tool, with Paris as the location argument. Tool call outputs - output we generate for the model"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 5,
        "cited_text": "Handling function calls When the model calls a function, you must execute it and return the result. Since model responses can include zero, one, or multiple calls, it is best practice to assume there are several. The response has an array of tool_calls , each with an id (used later to submit the function result) and a function containing a name and JSON-encoded arguments . Sample response with multiple function calls Execute function calls and append results python The response output array contains an entry with the type having a value of function_call . Each entry with a call_id (used later to submit the function result), name , and JSON-encoded arguments ."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 6,
        "cited_text": "A function call output or tool call output refers to the response a tool generates using the input from a model's tool call. The tool call output can either be structured JSON or plain text, and it should contain a reference to a specific model tool call (referenced by call_id in the examples to come). To complete our weather example: The model has access to a get_weather tool that takes location as an argument. In response to a prompt like “what's the weather in Paris?” the model returns a tool call that contains a location argument with a value of Paris The tool call output might return a JSON object (e.g., {\"temperature\": \"25\", \"unit\": \"C\"} , indicating a current temperature of 25 degrees), Image contents , or File contents ."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 7,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 8,
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
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 9,
        "cited_text": "What's changed? <cited_table> From assistants to prompts Assistants were persistent API objects that bundled model choice, instructions, and tool declarations—created and managed entirely through the API. Their replacement, prompts, can only be created in the dashboard, where you can version them as you develop your product.",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Before",
              "Now",
              "Why?"
            ],
            [
              "Assistants",
              "Prompts",
              "Prompts hold configuration (model, tools, instructions) and are easier to version and update"
            ],
            [
              "Threads",
              "Conversations",
              "Streams of items instead of just messages"
            ],
            [
              "Runs",
              "Responses",
              "Responses send input items or use a conversation object and receive output items; tool call loops are explicitly managed"
            ],
            [
              "Run steps",
              "Items",
              "Generalized objects—can be messages, tool calls, outputs, and more"
            ]
          ]
        }
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 10,
        "cited_text": "A thread was a collection of messages stored server-side. Threads could only store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data. Request example Thread object Conversation object Response example Thread object Conversation object From runs to responses Runs were asynchronous processes that executed against threads. See the example below. Responses are simpler: provide a set of input items to execute, and get a list of output items back. Responses are designed to be used alone, but you can also use them with prompt and conversation objects for storing context and configuration."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 11,
        "cited_text": "Practical migration steps Identify each existing Assistant's instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 12,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 13,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 14,
        "cited_text": "Parallel function calling Parallel function calling is not possible when using built-in tools . The model may choose to call multiple functions in a single turn. You can prevent this by setting parallel_tool_calls to false , which ensures exactly zero or one tool is called. Note: Currently, if you are using a fine tuned model and the model calls multiple functions in one turn then strict mode will be disabled for those calls. Note for gpt-4.1-nano-2025-04-14 : This snapshot of gpt-4.1-nano can sometimes include multiple tools calls for the same tool if parallel tool calls are enabled. It is recommended to disable this feature when using this nano snapshot."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 15,
        "cited_text": "Parallel Function Calling Newer models such as gpt-5, gpt-4.1 or gpt-4o can call multiple functions in one turn. How to call functions with model generated arguments In our next example, we'll demonstrate how to execute functions whose inputs are model-generated, and use this to implement an agent that can answer questions for us about a database. For simplicity we'll use the Chinook sample database . Note: SQL generation can be high-risk in a production environment since models are not perfectly reliable at generating correct SQL."
      },
      {
        "source_id": "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
        "citation_number": 16,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 17,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 18,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 19,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 20,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 21,
        "cited_text": "<cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Model",
              "Tool choice",
              "Tool use system prompt token count"
            ],
            [
              "Claude Opus 4.6",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4.1",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4.6",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 3.7 (",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Haiku 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Haiku 3.5",
              "auto",
              "264 tokens 340 tokens"
            ],
            [
              "Claude Opus 3 (",
              "auto",
              "530 tokens 281 tokens"
            ],
            [
              "Claude Sonnet 3",
              "auto",
              "159 tokens 235 tokens"
            ],
            [
              "Claude Haiku 3",
              "auto",
              "264 tokens 340 tokens"
            ]
          ]
        }
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 22,
        "cited_text": "Tool use examples For a complete hands-on walkthrough, see the tutorial . For reference examples of individual concepts, see Define tools and Handle tool calls . What happens when Claude needs more information Pricing Tool use requests are priced based on: The total number of input tokens sent to the model (including in the tools parameter) The number of output tokens generated For server-side tools, additional usage-based pricing (e.g., web search charges per search performed) Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage."
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 23,
        "cited_text": "Introducing the Model Context Protocol \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing the Model Context Protocol Nov 25, 2024 Today, we're open-sourcing the Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments. Its aim is to help frontier models produce better, more relevant responses."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 24,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 25,
        "cited_text": "Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools"
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "基于提供的来源，构建「第一个 Agent：用纯 Python + API 从零构建」不仅是技术实现，更涉及从实验到工业级部署的全生命周期。以下是其真实应用场景、部署方案、性能数据、实战案例及经验总结：\n\n### 1. 真实应用场景与案例\nAgent 通过将模型连接到外部数据和操作，在多个领域展现了实际价值：\n*   **企业自动化与数据处理：** 实现 **SQL 数据库查询**（如针对 Chinook 示例数据库的自然语言问答）、**客户服务代理**（处理退款、账户查询）以及 **PDF 内容提取与总结** [1-4]。\n*   **开发与系统集成：** 利用 **MCP（模型上下文协议）** 标准化连接 GitHub、Slack、Google Drive、Postgres 和 Puppeteer 等系统，进行代码维护、前端 UI 构建（配合 Figma）或跨工具的数据检索 [5-7]。\n*   **公共服务与信息检索：** 获取实时天气预报、星座查询、Web 搜索及文件检索 [8-10]。\n\n### 2. 工业级部署方案\n为了支持生产环境，架构演进至高可用与标准化的协议模式：\n*   **传输协议选择：** 推荐使用 **Streamable HTTP** 作为生产部署的首选，因为它具有良好的可扩展性，并支持**状态化（Stateful）**和**无状态（Stateless）**操作模式 [11, 12]。\n*   **标准化网关：** 采用 **MCP 服务器** 作为数据和功能的统一入口，支持通过标准 SDK 在不同 AI 平台间复用 Agent 逻辑 [13, 14]。\n*   **安全与合规：** 实现 **OAuth 2.1 认证**以保护敏感资源，并在部署时应用**网络安全检查（Cybersecurity checks）**和**安全防护栏（Guardrails）** [15-17]。\n*   **状态存储：** 工业级方案通常将对话状态（Conversation State）持久化在数据库中，并支持**上下文压缩（Compaction）**以节省存储空间和 Token 成本 [18, 19]。\n\n### 3. 开源项目实战案例\n*   **MCP Python SDK：** 官方提供的标准实现，展示了如何构建能够被 Claude 或其他 MCP 客户端调用的工具和资源 [20, 21]。\n*   **Claude Cookbooks：** 包含一系列 Jupyter Notebook 示例，涵盖了 **Haiku 子代理（Sub-agents）** 协作、自动化评估、Prompt 缓存等进阶实战技巧 [2, 22]。\n*   **OpenAI Cookbook：** 提供了基于 Chat Completions API 构建 Agent 的全套代码模板，包括 SQL 生成代理和知识库检索系统 [23, 24]。\n\n### 4. 性能基准数据\n*   **决策准确率提升：** 研究表明，**ReAct 架构**在 ALFWorld 和 WebShop 等决策任务中，相比传统的强化学习方法，其**绝对成功率提升了 10% 到 34%** [25]。\n*   **模型消耗（Token）：** 开启 Agent 能力会增加初始 Token 负担。例如，使用 Claude Opus 4.6 处理工具调用请求时，其系统 Prompt 约占 **313 至 346 Tokens** [26]。\n*   **成本与延迟：** 通过 **Prompt Caching（提示词缓存）**，开发者可以减少重复定义的工具 Schema 带来的费用，并结合 **Predicted Outputs** 优化首字生成延迟 [15, 27, 28]。\n\n### 5. 开发者最佳实践\n*   **工具定义：** 始终开启 **Strict Mode (`strict: true`)** 以确保模型生成的参数 100% 符合 JSON Schema，并为函数提供清晰、详细的描述 [29-31]。\n*   **复杂度控制：** 建议单轮对话开始时可用的工具数量**控制在 20 个以内**，对于大规模工具库应使用 **Tool Search** 进行按需加载 [31, 32]。\n*   **工程化原则：** 遵循“最少惊讶原则”，使用 **Enums** 枚举值防止非法状态，并确保函数接口简单到“能通过实习生测试” [32]。\n\n### 6. 常见踩坑经验\n*   **SQL 生成风险：** 在生产环境中直接执行模型生成的 SQL 具有高风险，必须进行严格的安全审计 [3]。\n*   **上下文溢出：** 大型工具定义（JSON Schema）会被注入系统消息，容易触及上下文限制。优化策略包括缩短描述或使用细粒度的工具流 [27]。\n*   **幻觉与错误传播：** 纯思考（CoT）模式容易产生逻辑幻觉。**ReAct 模式**通过引入外部工具反馈（Observation）能有效抑制这一问题 [25]。\n*   **解析失败：** 自定义语法（Custom Grammars）如果过于复杂，可能导致模型输出在语义上正确但在语法上偏移。应保持语法简单、明确，并在必要时增加少样本（Few-shot）示例 [33, 34]。",
    "conversation_id": "12473243-78e3-4528-809d-514057372f09",
    "sources_used": [
      "9522b537-6442-4d93-8322-7d7cd480d830",
      "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "f41ff146-4c65-4b00-8020-849dd93d6594",
      "d5221585-f4ba-4631-aac4-933e154a5d24",
      "846ddb0d-a14f-400c-997f-b253c39b7a2c"
    ],
    "citations": {
      "1": "9522b537-6442-4d93-8322-7d7cd480d830",
      "2": "9522b537-6442-4d93-8322-7d7cd480d830",
      "3": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "4": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "5": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "6": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "7": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "8": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "9": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "10": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "11": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "12": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "13": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "14": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "15": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "16": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "17": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "18": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "19": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "20": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "21": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "22": "9522b537-6442-4d93-8322-7d7cd480d830",
      "23": "f41ff146-4c65-4b00-8020-849dd93d6594",
      "24": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "25": "d5221585-f4ba-4631-aac4-933e154a5d24",
      "26": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "27": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "28": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "29": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "30": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "31": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "32": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "33": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "34": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98"
    },
    "references": [
      {
        "source_id": "9522b537-6442-4d93-8322-7d7cd480d830",
        "citation_number": 1,
        "cited_text": "Tool use : Learn how to integrate Claude with external tools and functions to extend its capabilities. Customer service agent Calculator integration SQL queries Third-Party Integrations Retrieval augmented generation : Supplement Claude's knowledge with external data sources. Vector databases (Pinecone) Wikipedia Web pages Embeddings with Voyage AI Multimodal Capabilities Vision with Claude : Getting started with images Best practices for vision Interpreting charts and graphs Extracting content from forms Generate images with Claude : Use Claude with Stable Diffusion for image generation."
      },
      {
        "source_id": "9522b537-6442-4d93-8322-7d7cd480d830",
        "citation_number": 2,
        "cited_text": "Advanced Techniques Sub-agents : Learn how to use Haiku as a sub-agent in combination with Opus. Upload PDFs to Claude : Parse and pass PDFs as text to Claude. Automated evaluations : Use Claude to automate the prompt evaluation process. Enable JSON mode : Ensure consistent JSON output from Claude. Create a moderation filter : Use Claude to create a content moderation filter for your application. Prompt caching : Learn techniques for efficient prompt caching with Claude. Additional Resources"
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 3,
        "cited_text": "Parallel Function Calling Newer models such as gpt-5, gpt-4.1 or gpt-4o can call multiple functions in one turn. How to call functions with model generated arguments In our next example, we'll demonstrate how to execute functions whose inputs are model-generated, and use this to implement an agent that can answer questions for us about a database. For simplicity we'll use the Chinook sample database . Note: SQL generation can be high-risk in a production environment since models are not perfectly reliable at generating correct SQL."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 4,
        "cited_text": "Specifying a function to execute SQL queries First let's define some helpful utility functions to extract data from a SQLite database. Now we can use these utility functions to extract a representation of the database schema. As before, we'll define a function specification for the function we'd like the API to generate arguments for. Notice that we are inserting the database schema into the function specification. This will be important for the model to know about. Executing SQL queries Now let's implement the function that will actually excute queries against the database."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 5,
        "cited_text": "Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma"
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 6,
        "cited_text": "Claude 3.5 Sonnet is adept at quickly building MCP server implementations, making it easy for organizations and individuals to rapidly connect their most important datasets with a range of AI-powered tools. To help developers start exploring, we're sharing pre-built MCP servers for popular enterprise systems like Google Drive, Slack, GitHub, Git, Postgres, and Puppeteer. Early adopters like Block and Apollo have integrated MCP into their systems, while development tools companies including Zed, Replit, Codeium, and Sourcegraph are working with MCP to enhance their platforms—enabling AI agents to better retrieve relevant information to further understand the context around a coding task and produce more nuanced and functional code with fewer attempts."
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 7,
        "cited_text": "Instead of maintaining separate connectors for each data source, developers can now build against a standard protocol. As the ecosystem matures, AI systems will maintain context as they move between different tools and datasets, replacing today's fragmented integrations with a more sustainable architecture. Getting started Developers can start building and testing MCP connectors today. All Claude.ai plans support connecting MCP servers to the Claude Desktop app. Claude for Work customers can begin testing MCP servers locally, connecting Claude to internal systems and datasets. We'll soon provide developer toolkits for deploying remote production MCP servers that can serve your entire Claude for Work organization."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 8,
        "cited_text": "You could give the model access to tools that: Get today's weather for a location Access account details for a given user ID Issue refunds for a lost order Or anything else you'd like the model to be able to know or do as it responds to a prompt. When we make an API request to the model with a prompt, we can include a list of tools the model could consider using. For example, if we wanted the model to be able to answer questions about the current weather somewhere in the world, we might give it access to a get_weather tool that takes location as an argument."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 9,
        "cited_text": "A function call output or tool call output refers to the response a tool generates using the input from a model's tool call. The tool call output can either be structured JSON or plain text, and it should contain a reference to a specific model tool call (referenced by call_id in the examples to come). To complete our weather example: The model has access to a get_weather tool that takes location as an argument. In response to a prompt like “what's the weather in Paris?” the model returns a tool call that contains a location argument with a value of Paris The tool call output might return a JSON object (e.g., {\"temperature\": \"25\", \"unit\": \"C\"} , indicating a current temperature of 25 degrees), Image contents , or File contents ."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 10,
        "cited_text": "The tool calling flow Tool calling is a multi-step conversation between your application and a model via the OpenAI API. The tool calling flow has five high level steps: Make a request to the model with tools it could call Receive a tool call from the model Execute code on the application side with input from the tool call Make a second request to the model with the tool output Receive a final response from the model (or more tool calls) Function tool example Let's look at an end-to-end tool calling flow for a get_horoscope function that gets a daily horoscope for an astrological sign."
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 11,
        "cited_text": "Streamable HTTP Transport Note : Streamable HTTP transport is the recommended transport for production deployments. Use stateless_http=True and json_response=True for optimal scalability. Full example: examples/snippets/servers/streamable_config.py You can mount multiple FastMCP servers in a Starlette application: Full example: examples/snippets/servers/streamable_starlette_mount.py For low level server with Streamable HTTP implementations, see: Stateful server: examples/servers/simple-streamablehttp/ Stateless server: examples/servers/simple-streamablehttp-stateless/"
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 12,
        "cited_text": "The streamable HTTP transport supports: Stateful and stateless operation modes Resumability with event stores JSON or SSE response formats Better scalability for multi-node deployments CORS Configuration for Browser-Based Clients If you'd like your server to be accessible by browser-based MCP clients, you'll need to configure CORS headers. The Mcp-Session-Id header must be exposed for browser clients to access it: This configuration is necessary because: The MCP streamable HTTP transport uses the Mcp-Session-Id header for session management Browsers restrict access to response headers unless explicitly exposed via CORS Without this configuration, browser-based clients won't be able to read the session ID from initialization responses"
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 13,
        "cited_text": "Overview The Model Context Protocol allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction. This Python SDK implements the full MCP specification, making it easy to: Build MCP clients that can connect to any MCP server Create MCP servers that expose resources, prompts and tools Use standard transports like stdio, SSE, and Streamable HTTP Handle all MCP protocol messages and lifecycle events Installation"
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 14,
        "cited_text": "Introducing the Model Context Protocol \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing the Model Context Protocol Nov 25, 2024 Today, we're open-sourcing the Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments. Its aim is to help frontier models produce better, more relevant responses."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 15,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 16,
        "cited_text": "The elicit() method returns an ElicitationResult with: action : \"accept\", \"decline\", or \"cancel\" data : The validated response (only when accepted) validation_error : Any validation error message Sampling Tools can interact with LLMs through sampling (generating text): Full example: examples/snippets/servers/sampling.py Logging and Notifications Tools can send logs and notifications through the context: Full example: examples/snippets/servers/notifications.py Authentication Authentication can be used by servers that want to expose tools accessing protected resources. mcp.server.auth implements OAuth 2.1 resource server functionality, where MCP servers act as Resource Servers (RS) that validate tokens issued by separate Authorization Servers (AS). This follows the MCP authorization specification and implements RFC 9728 (Protected Resource Metadata) for AS discovery."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 17,
        "cited_text": "Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events"
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 18,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 19,
        "cited_text": "Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices"
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 20,
        "cited_text": "GitHub - modelcontextprotocol/python-sdk: The official Python SDK for Model Context Protocol servers and clients · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 21,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security MCP Python SDK Python implementation of the Model Context Protocol (MCP) Note This README documents v1.x of the MCP Python SDK (the current stable release). For v1.x code and documentation, see the v1.x branch . For the upcoming v2 documentation (pre-alpha, in development on main ), see README.v2.md . Table of Contents MCP Python SDK Overview Installation Adding MCP to your python project Running the standalone MCP development tools Quickstart What is MCP? Core Concepts Server Resources Tools Structured Output Prompts Images Context Getting Context in Functions Context Properties and Methods Completions Elicitation Sampling Logging and Notifications Authentication FastMCP Properties Session Properties and Methods Request Context Properties Running Your Server Development Mode Claude Desktop Integration Direct Execution Streamable HTTP Transport CORS Configuration for Browser-Based Clients Mounting to an Existing ASGI Server StreamableHTTP servers Basic mounting Host-based routing Multiple servers with path configuration Path configuration at initialization SSE servers Advanced Usage Low-Level Server Structured Output Support Pagination (Advanced) Writing MCP Clients Client Display Utilities OAuth Authentication for Clients Parsing Tool Results MCP Primitives Server Capabilities Documentation Contributing License"
      },
      {
        "source_id": "9522b537-6442-4d93-8322-7d7cd480d830",
        "citation_number": 22,
        "cited_text": "anthropics / claude-cookbooks Public Notifications You must be signed in to change notification settings Fork 4.1k Star 37.2k Code Issues 12 Pull requests 80 Actions Projects Security and quality 0 Insights Additional navigation options Code Issues Pull requests Actions Projects Security and quality Insights anthropics/claude-cookbooks main 106 Branches 0 Tags Go to file Code Open more actions menu Folders and files <cited_table>",
        "cited_table": {
          "num_columns": 5,
          "rows": [
            [
              "Name",
              "",
              "Name",
              "Last commit message",
              "Last commit date"
            ],
            [
              "## Latest commit",
              "",
              "",
              "",
              ""
            ],
            [
              ".claude",
              "",
              ".claude",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              ".github",
              "",
              ".github",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "anthropic_cookbook",
              "",
              "anthropic_cookbook",
              "refactor: simplify notebook CI/CD by removing nbqa and papermill",
              "7 months ago"
            ],
            [
              "capabilities",
              "",
              "capabilities",
              "chore(knowledge_graph): regenerate notebook outputs with structured o…",
              "last week"
            ],
            [
              "claude_agent_sdk",
              "",
              "claude_agent_sdk",
              "address review: import SDKSessionInfo, explicit raise, return type, c…",
              "3 days ago"
            ],
            [
              "coding",
              "",
              "coding",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "extended_thinking",
              "",
              "extended_thinking",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "finetuning",
              "",
              "finetuning",
              "Lint + Format all cookbooks/scripts (",
              "5 months ago"
            ],
            [
              "images",
              "",
              "images",
              "Frontend Cookbook (",
              "6 months ago"
            ],
            [
              "misc",
              "",
              "misc",
              "docs(misc): update prompt caching cookbook with automatic caching (",
              "2 months ago"
            ],
            [
              "multimodal",
              "",
              "multimodal",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "observability",
              "",
              "observability",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "patterns/ agents",
              "",
              "patterns/ agents",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "scripts",
              "",
              "scripts",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "skills",
              "",
              "skills",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "tests",
              "",
              "tests",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "third_party",
              "",
              "third_party",
              "Lint + Format all cookbooks/scripts (",
              "5 months ago"
            ],
            [
              "tool_evaluation",
              "",
              "tool_evaluation",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "tool_use",
              "",
              "tool_use",
              "fix(tool_use): unwrap blockquote callouts in context engineering note…",
              "3 days ago"
            ],
            [
              ".env.example",
              "",
              ".env.example",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              ".gitignore",
              "",
              ".gitignore",
              "feat(claude_agent_sdk): add OpenAI migration guide + SRE README + min…",
              "2 weeks ago"
            ],
            [
              ".pre-commit-config.yaml",
              "",
              ".pre-commit-config.yaml",
              "add zh to memory cookbook (",
              "4 months ago"
            ],
            [
              "CLAUDE.md",
              "",
              "CLAUDE.md",
              "feat(claude_agent_sdk): add OpenAI migration guide + SRE README + min…",
              "2 weeks ago"
            ],
            [
              "CONTRIBUTING.md",
              "",
              "CONTRIBUTING.md",
              "remove 404ing link (",
              "3 weeks ago"
            ],
            [
              "LICENSE",
              "",
              "LICENSE",
              "launch stuff",
              "2 years ago"
            ],
            [
              "Makefile",
              "",
              "Makefile",
              "feat: add notebook testing scaffold with pytest and tox (",
              "4 months ago"
            ],
            [
              "README.md",
              "",
              "README.md",
              "docs: fix typos in README and CONTRIBUTING (",
              "4 months ago"
            ],
            [
              "authors.yaml",
              "",
              "authors.yaml",
              "Merge pull request",
              "2 days ago"
            ],
            [
              "lychee.toml",
              "",
              "lychee.toml",
              "feat(skills): add comprehensive style guide for cookbook audits (",
              "5 months ago"
            ],
            [
              "pyproject.toml",
              "",
              "pyproject.toml",
              "chore: bump anthropic SDK to >=0.77.0 for structured outputs",
              "last week"
            ],
            [
              "registry.yaml",
              "",
              "registry.yaml",
              "Merge pull request",
              "2 days ago"
            ],
            [
              "requirements-dev.txt",
              "",
              "requirements-dev.txt",
              "fix: remove nbstripout and preserve notebook outputs",
              "7 months ago"
            ],
            [
              "tox.ini",
              "",
              "tox.ini",
              "feat: add notebook testing scaffold with pytest and tox (",
              "4 months ago"
            ],
            [
              "uv.lock",
              "",
              "uv.lock",
              "chore: bump anthropic SDK to >=0.77.0 for structured outputs",
              "last week"
            ],
            [
              "uv.toml",
              "",
              "uv.toml",
              "fix: configure uv to use public PyPI",
              "7 months ago"
            ],
            [
              "View all files",
              "",
              "",
              "",
              ""
            ]
          ]
        }
      },
      {
        "source_id": "f41ff146-4c65-4b00-8020-849dd93d6594",
        "citation_number": 23,
        "cited_text": "You can't perform that action at this time."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 24,
        "cited_text": "This notebook covers how to use the Chat Completions API in combination with external functions to extend the capabilities of GPT models. tools is an optional parameter in the Chat Completion API which can be used to provide function specifications. The purpose of this is to enable models to generate function arguments which adhere to the provided specifications. Note that the API will not actually execute any function calls. It is up to developers to execute function calls using model outputs. Within the tools parameter, if the functions parameter is provided then by default the model will decide when it is appropriate to use one of the functions. The API can be forced to use a specific function by setting the tool_choice parameter to {\"type\": \"function\", \"function\": {\"name\": \"my_function\"}} . The API can also be forced to not use any function by setting the tool_choice parameter to \"none\" . If a function is used, the output will contain \"finish_reason\": \"tool_calls\" in the response, as well as a tool_calls object that has the name of the function and the generated function arguments."
      },
      {
        "source_id": "d5221585-f4ba-4631-aac4-933e154a5d24",
        "citation_number": 25,
        "cited_text": "arXiv:2210.03629 (cs) [Submitted on 6 Oct 2022 ( v1 ), last revised 10 Mar 2023 (this version, v3)] Title: ReAct: Synergizing Reasoning and Acting in Language Models Authors: Shunyu Yao , Jeffrey Zhao , Dian Yu , Nan Du , Izhak Shafran , Karthik Narasimhan , Yuan Cao View a PDF of the paper titled ReAct: Synergizing Reasoning and Acting in Language Models, by Shunyu Yao and 6 other authors View PDF Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: this https URL"
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 26,
        "cited_text": "<cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Model",
              "Tool choice",
              "Tool use system prompt token count"
            ],
            [
              "Claude Opus 4.6",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4.1",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4.6",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 3.7 (",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Haiku 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Haiku 3.5",
              "auto",
              "264 tokens 340 tokens"
            ],
            [
              "Claude Opus 3 (",
              "auto",
              "530 tokens 281 tokens"
            ],
            [
              "Claude Sonnet 3",
              "auto",
              "159 tokens 235 tokens"
            ],
            [
              "Claude Haiku 3",
              "auto",
              "264 tokens 340 tokens"
            ]
          ]
        }
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 27,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 28,
        "cited_text": "When to use allowed_tools You might want to configure an allowed_tools list in case you want to make only a subset of tools available across model requests, but not modify the list of tools you pass in, so you can maximize savings from prompt caching . You can also set tool_choice to \"none\" to imitate the behavior of passing no functions. When you use tool search, tool_choice still applies to the tools that are currently callable in the turn. This is most useful after you load a subset of tools and want to constrain the model to that subset."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 29,
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
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 30,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 31,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 32,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 33,
        "cited_text": "Keep grammars simple Try to make your grammar as simple as possible. The OpenAI API may return an error if the grammar is too complex, so you should ensure that your desired grammar is compatible before using it in the API. Lark grammars can be tricky to perfect. While simple grammars perform most reliably, complex grammars often require iteration on the grammar definition itself, the prompt, and the tool description to ensure that the model does not go out of distribution. Correct versus incorrect patterns"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 34,
        "cited_text": "Use rules to combine tokens, not to steer regex internals Good rule usage example: Treat whitespace explicitly Don't rely on open-ended %ignore directives. Using unbounded ignore directives may cause the grammar to be too complex and/or may cause the model to go out of distribution. Prefer threading explicit terminals wherever whitespace is allowed. Troubleshooting If the API rejects the grammar because it is too complex, simplify the rules and terminals and remove unbounded %ignore s. If custom tools are called with unexpected tokens, confirm terminals aren't overlapping; check greedy lexer. When the model drifts “out‑of‑distribution” (shows up as the model producing excessively long or repetitive outputs, it is syntactically valid but is semantically wrong): Tighten the grammar. Iterate on the prompt (add few-shot examples) and tool description (explain the grammar and instruct the model to reason and conform to it). Experiment with a higher reasoning effort (e.g, bump from medium to high)."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「第一个 Agent：用纯 Python + API 从零构建」这一领域，2025-2026 年的研究突破与技术趋势正从“简单的 API 调用”转向**“高度自治、标准化且由开发者完全掌控的系统编排”**。以下是基于来源的详细解析：\n\n### 1. 2025-2026 年重要技术趋势\n*   **从平台托管转向开发者编排 (Responses API)：** 行业正在经历从 Assistants API（平台托管状态）向 **Responses API** 的重大迁移 [1, 2]。这种趋势强调开发者在 Python 端手动管理对话历史（Conversation State）、修剪上下文和工具调用循环，以获得更高的灵活性和可移植性 [3, 4]。\n*   **MCP (Model Context Protocol) 的标准化：** MCP 已成为连接 AI 助手与数据源（如 GitHub、Slack、本地环境）的通用开放标准 [5, 6]。它解决了每增加一个数据源就需要自定义实现的痛点，实现了“一次构建，多处连接” [7, 8]。\n*   **动态工具加载 (Tool Search)：** 随着工具库的膨胀，最新的模型（如 GPT-5.4 及以后版本）开始支持 **Tool Search** [9, 10]。Agent 不再需要预先加载所有工具 Schema，而是由模型根据需求搜索并按需加载工具，有效绕过了上下文窗口限制并降低了 Token 消耗 [11, 12]。\n*   **推理模型 (Reasoning Models) 的深化：** 模型如 GPT-5 或 Claude 4.6 开始支持“推理努力”（Reasoning Effort）配置，允许 Agent 在执行复杂工具调用前进行更长时间的内部思考（Thought Traces），以减少逻辑错误 [13-15]。\n\n### 2. 核心研究与经典论文\n*   **ReAct 范式 (2022-2023)：** 虽非 2025 年产物，但其**推理与行动协同**的核心思想仍是所有现代 Agent 的基石 [16]。研究表明，ReAct 架构在交互式决策任务中比传统强化学习方法在成功率上提升了 **34%** [16]。\n*   **Toolformer (2023)：** 确立了语言模型通过 API 接口自学使用工具的路径，为现在模型自主决策调用哪些 API 奠定了理论基础 [17]。\n\n### 3. 未解决的挑战\n*   **高风险行动的安全边界：** 例如 **SQL 自动生成**在生产环境中仍被视为高风险，因为模型生成的查询可能存在不确定性 [18]。目前的解决方案仍处于“网络安全检查”和“人工审查”阶段 [19, 20]。\n*   **Token 成本与系统负担：** 启用 Agent 能力（工具定义）会带来额外的 Token 开销。例如，Claude 4.6 模型仅为了开启工具使用能力，就会自动加载约 **346 个系统 Token** [21, 22]。\n*   **幻觉与错误传播：** 尽管引入了观察（Observation）环节，但在复杂的多步推理中，模型仍可能产生逻辑幻觉，且错误会随着循环步数增加而传播 [16]。\n\n### 4. 未来可能的突破点\n*   **计算机操作能力 (Computer Use)：** Agent 将不再局限于调用 API，而是能够直接操作计算机界面（如浏览网页、编辑文件、执行 Shell 命令），这被视为 Agent 能力的终极形态之一 [23-25]。\n*   **严格模式与结构化输出：** 通过 **Strict Mode (`strict: true`)** 强制模型 100% 遵循 JSON Schema，这将消除 Python 端解析错误的风险，使 Agent 运行更加稳健 [26-28]。\n*   **实时交互 Agent：** 结合 **Realtime API** 和低延迟传输（如 WebRTC/WebSockets），未来的 Python Agent 将支持流式、低延迟的多模态交互 [29, 30]。\n\n**总结：** 2025-2026 年的发展方向是**“解耦与标准化”**。开发者正通过纯 Python 代码（配合 Responses API 和 MCP 协议）重新夺回对 Agent 逻辑的控制权，而不再依赖黑盒化的平台托管服务 [1, 3, 7]。",
    "conversation_id": "12473243-78e3-4528-809d-514057372f09",
    "sources_used": [
      "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
      "d5221585-f4ba-4631-aac4-933e154a5d24",
      "b4d8fc62-79c9-4866-9f3a-17d9234481dd",
      "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "846ddb0d-a14f-400c-997f-b253c39b7a2c"
    ],
    "citations": {
      "1": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "2": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "3": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "4": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "5": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "6": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "7": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "8": "8a0e5adb-265f-4e62-9df5-79f354409a11",
      "9": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "10": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "11": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "12": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "13": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "14": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "15": "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
      "16": "d5221585-f4ba-4631-aac4-933e154a5d24",
      "17": "b4d8fc62-79c9-4866-9f3a-17d9234481dd",
      "18": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "19": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "20": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
      "21": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "22": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "23": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "24": "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
      "25": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "26": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "27": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
      "28": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
      "29": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
      "30": "8176a84a-7bef-4f48-8b5a-dbed30dafe19"
    },
    "references": [
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 1,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 2,
        "cited_text": "What's changed? <cited_table> From assistants to prompts Assistants were persistent API objects that bundled model choice, instructions, and tool declarations—created and managed entirely through the API. Their replacement, prompts, can only be created in the dashboard, where you can version them as you develop your product.",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Before",
              "Now",
              "Why?"
            ],
            [
              "Assistants",
              "Prompts",
              "Prompts hold configuration (model, tools, instructions) and are easier to version and update"
            ],
            [
              "Threads",
              "Conversations",
              "Streams of items instead of just messages"
            ],
            [
              "Runs",
              "Responses",
              "Responses send input items or use a conversation object and receive output items; tool call loops are explicitly managed"
            ],
            [
              "Run steps",
              "Items",
              "Generalized objects—can be messages, tool calls, outputs, and more"
            ]
          ]
        }
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 3,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 4,
        "cited_text": "Practical migration steps Identify each existing Assistant's instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 5,
        "cited_text": "Introducing the Model Context Protocol \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Announcements Introducing the Model Context Protocol Nov 25, 2024 Today, we're open-sourcing the Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments. Its aim is to help frontier models produce better, more relevant responses."
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 6,
        "cited_text": "As AI assistants gain mainstream adoption, the industry has invested heavily in model capabilities, achieving rapid advances in reasoning and quality. Yet even the most sophisticated models are constrained by their isolation from data—trapped behind information silos and legacy systems. Every new data source requires its own custom implementation, making truly connected systems difficult to scale. MCP addresses this challenge. It provides a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol. The result is a simpler, more reliable way to give AI systems access to the data they need."
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 7,
        "cited_text": "Model Context Protocol The Model Context Protocol is an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools. The architecture is straightforward: developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers. Today, we're introducing three major components of the Model Context Protocol for developers: The Model Context Protocol specification and SDKs Local MCP server support in the Claude Desktop apps An open-source repository of MCP servers"
      },
      {
        "source_id": "8a0e5adb-265f-4e62-9df5-79f354409a11",
        "citation_number": 8,
        "cited_text": "Instead of maintaining separate connectors for each data source, developers can now build against a standard protocol. As the ecosystem matures, AI systems will maintain context as they move between different tools and datasets, replacing today's fragmented integrations with a more sustainable architecture. Getting started Developers can start building and testing MCP connectors today. All Claude.ai plans support connecting MCP servers to the Claude Desktop app. Claude for Work customers can begin testing MCP servers locally, connecting Claude to internal systems and datasets. We'll soon provide developer toolkits for deploying remote production MCP servers that can serve your entire Claude for Work organization."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 9,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 10,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 11,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 12,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 13,
        "cited_text": "Community Programs, meetups, and support for builders Start searching API Dashboard Search the API docs Search docs Suggested response_format reasoning_effort streaming tools Primary navigation API API Reference Codex ChatGPT Resources Search docs Suggested response_format reasoning_effort streaming tools Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API"
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 14,
        "cited_text": "Complete tool calling example python Complete tool calling example python Note that for reasoning models like GPT-5 or o4-mini, any reasoning items returned in model responses with tool calls must also be passed back with tool call outputs. Defining functions Functions are usually declared in the tools parameter of each API request. With tool search , your application can also load deferred functions later in the interaction. Either way, each callable function uses the same schema shape. A function definition has the following properties:"
      },
      {
        "source_id": "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
        "citation_number": 15,
        "cited_text": "Not Found - Claude API Docs Loading... Developer Guide API Reference MCP Resources Release Notes English Log in Search... ⌘K First steps Intro to Claude Quickstart Models & pricing Models overview Choosing a model What's new in Claude 4.6 Migration guide Model deprecations Pricing Build with Claude Features overview Using the Messages API Handling stop reasons Prompting best practices Model capabilities Extended thinking Adaptive thinking Effort Fast mode (beta: research preview) Structured outputs Citations Streaming Messages Batch processing PDF support Search results Multilingual support Embeddings Vision"
      },
      {
        "source_id": "d5221585-f4ba-4631-aac4-933e154a5d24",
        "citation_number": 16,
        "cited_text": "arXiv:2210.03629 (cs) [Submitted on 6 Oct 2022 ( v1 ), last revised 10 Mar 2023 (this version, v3)] Title: ReAct: Synergizing Reasoning and Acting in Language Models Authors: Shunyu Yao , Jeffrey Zhao , Dian Yu , Nan Du , Izhak Shafran , Karthik Narasimhan , Yuan Cao View a PDF of the paper titled ReAct: Synergizing Reasoning and Acting in Language Models, by Shunyu Yao and 6 other authors View PDF Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: this https URL"
      },
      {
        "source_id": "b4d8fc62-79c9-4866-9f3a-17d9234481dd",
        "citation_number": 17,
        "cited_text": "arXiv:2302.04761 (cs) [Submitted on 9 Feb 2023] Title: Toolformer: Language Models Can Teach Themselves to Use Tools Authors: Timo Schick , Jane Dwivedi-Yu , Roberto Dessì , Roberta Raileanu , Maria Lomeli , Luke Zettlemoyer , Nicola Cancedda , Thomas Scialom View a PDF of the paper titled Toolformer: Language Models Can Teach Themselves to Use Tools, by Timo Schick and 7 other authors View PDF Abstract: Language models (LMs) exhibit remarkable abilities to solve new tasks from just a few examples or textual instructions, especially at scale. They also, paradoxically, struggle with basic functionality, such as arithmetic or factual lookup, where much simpler and smaller models excel. In this paper, we show that LMs can teach themselves to use external tools via simple APIs and achieve the best of both worlds. We introduce Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each API. We incorporate a range of tools, including a calculator, a Q&A system, two different search engines, a translation system, and a calendar. Toolformer achieves substantially improved zero-shot performance across a variety of downstream tasks, often competitive with much larger models, without sacrificing its core language modeling abilities."
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 18,
        "cited_text": "Parallel Function Calling Newer models such as gpt-5, gpt-4.1 or gpt-4o can call multiple functions in one turn. How to call functions with model generated arguments In our next example, we'll demonstrate how to execute functions whose inputs are model-generated, and use this to implement an agent that can answer questions for us about a database. For simplicity we'll use the Chinook sample database . Note: SQL generation can be high-risk in a production environment since models are not perfectly reliable at generating correct SQL."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 19,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 20,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 21,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 22,
        "cited_text": "<cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Model",
              "Tool choice",
              "Tool use system prompt token count"
            ],
            [
              "Claude Opus 4.6",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4.1",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Opus 4",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4.6",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 4",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Sonnet 3.7 (",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Haiku 4.5",
              "auto",
              "346 tokens 313 tokens"
            ],
            [
              "Claude Haiku 3.5",
              "auto",
              "264 tokens 340 tokens"
            ],
            [
              "Claude Opus 3 (",
              "auto",
              "530 tokens 281 tokens"
            ],
            [
              "Claude Sonnet 3",
              "auto",
              "159 tokens 235 tokens"
            ],
            [
              "Claude Haiku 3",
              "auto",
              "264 tokens 340 tokens"
            ]
          ]
        }
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 23,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "a0c235b4-3089-4554-ac75-3b1f0c9a8760",
        "citation_number": 24,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 25,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 26,
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
        "source_id": "4e67fd0e-9f00-49fc-8c75-77ac9ca1bc98",
        "citation_number": 27,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "846ddb0d-a14f-400c-997f-b253c39b7a2c",
        "citation_number": 28,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "d667c5a6-859d-4613-a19b-9765ec6c22c0",
        "citation_number": 29,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      },
      {
        "source_id": "8176a84a-7bef-4f48-8b5a-dbed30dafe19",
        "citation_number": 30,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      }
    ]
  }
}
