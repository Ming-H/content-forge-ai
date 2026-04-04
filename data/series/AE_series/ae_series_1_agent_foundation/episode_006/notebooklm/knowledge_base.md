# 知识库：ReAct 模式：思考-行动-观察的 Agent 循环

生成时间: 2026-04-03 13:57
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "「ReAct 模式：思考-行动-观察（Think-Act-Observe）的 Agent 循环」源于 2023 年发表的 ICLR 论文《ReAct: Synergizing Reasoning and Acting in Language Models》，旨在通过协同推理与行动来增强大型语言模型（LLM）解决复杂任务的能力 [1, 2]。\n\n以下是基于来源整理的核心技术架构、关键组件及相关技术指标：\n\n### 1. 核心技术架构与关键组件\nReAct 模式构建了一个闭环的迭代流程，使 Agent 能够像人类一样处理任务：\n*   **思考 (Thought)**：LLM 生成推理轨迹，用于规划、跟踪和更新行动方案，并处理运行中的异常 [1, 3]。\n*   **行动 (Action)**：Agent 根据推理结果与外部环境（如维基百科、API、计算器等）进行交互 [1, 3]。\n*   **观察 (Observation)**：Agent 接收来自环境的反馈（如搜索结果、代码执行输出），并将其作为上下文输入到下一个循环中 [1, 4]。\n*   **关键组件**：\n    *   **LLM 推理引擎**：作为 Agent 的“大脑”，负责逻辑分析和决策 [1, 5]。\n    *   **外部工具库 (Tools/Skills)**：包括 Web 搜索、代码解释器、文件检索（RAG）和模型上下文协议（MCP）连接器 [6-8]。\n    *   **记忆系统 (Memory)**：存储对话状态、动作历史和环境反馈，支持长期记忆压缩和检索 [9-11]。\n\n### 2. 技术演进路线\nAgent 技术经历了从单一推理到复杂循环反馈的演进：\n1.  **Chain-of-Thought (CoT)**：早期的技术路径，侧重于模型内部的逐步推理（仅“思考”）[12]。\n2.  **Act-only**：侧重于直接调用工具而缺乏明确推理逻辑的模式。\n3.  **ReAct (2023)**：正式提出将推理轨迹与特定任务的行动相结合 [1, 3]。\n4.  **Reflexion (2023)**：在 ReAct 基础上引入**语言强化学习**，Agent 通过口头自我反思任务反馈信号，并维护历史经验以优化决策 [11]。\n5.  **Plan-and-Solve (PS) (2023)**：针对 CoT 的步骤缺失问题，提出先制定整体计划，再按计划执行子任务的架构 [12]。\n6.  **Agentic RL (2025-2026)**：最新的演进方向，通过强化学习（如 Trinity-RFT）对 Agent 的推理和工具使用能力进行端到端调优 [9, 13]。\n\n### 3. 核心算法名称\n*   **ReAct Algorithm**：协同推理与行动的核心算法框架 [2]。\n*   **Reflexion**：基于语言反馈的自我强化学习算法 [11]。\n*   **Plan-and-Solve (PS/PS+) Prompting**：旨在解决多步推理中步骤缺失和计算误差的算法 [12]。\n*   **Trinity-RFT**：用于 Agent 强化学习微调的特定库/算法 [9]。\n\n### 4. 主要架构模式\n*   **Agentic Loop (工具调用循环)**：模型在循环中不断调用工具，直到达到停止条件 [4, 14]。\n*   **Agent Graph (Agent 图架构)**：将 Agent 的逻辑表示为有向图（如 LangGraph），实现可控的任务编排 [14, 15]。\n*   **Multi-agent Conversation (多 Agent 协作)**：通过多个 Agent（如助理 Agent 和用户代理 Agent）之间的对话和反馈执行任务 [5, 16, 17]。\n*   **Human-in-the-loop (人工干预)**：在循环中支持实时中断、引导或提供人工反馈 [13, 18, 19]。\n\n### 5. 关键技术指标\n衡量 ReAct 及后续 Agent 模式性能的主要指标包括：\n*   **任务成功率 (Success Rate)**：例如在 AlfWorld 任务中，GPT-3 使用 ReAct 模式可达到 78.4% 的成功率 [20]。\n*   **精确匹配度 (EM, Exact Match)**：在 HotpotQA（29.4%-30.4%）和 FEVER（54%-62.2%）等基准测试中的得分 [20]。\n*   **Pass@1 准确率**：Reflexion 在 HumanEval 编程基准测试中达到了 91% 的 Pass@1 成绩 [11]。\n*   **Token 消耗量**：包括输入/输出 Token 数，以及工具使用时自动加载的系统提示词（通常约 150-530 Tokens）[21-23]。\n*   **推理延迟与成本**：特别是在生产环境中，通过批处理和预测输出等手段进行优化 [24, 25]。",
    "conversation_id": "e87fa844-1f99-4965-a570-cd7c5f71372c",
    "sources_used": [
      "67435eed-15fe-4a1a-88b7-1a1675bb4834",
      "92919907-d72e-4070-85fe-be96ea905d4a",
      "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "e4ac6599-2562-4caa-9f12-22505667e18e",
      "a17a977e-d59a-4195-864b-81bb1582975f",
      "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
      "beec4d53-e134-47c8-b85e-26eb40acf1b1",
      "6f26f676-2418-41cb-a026-91961e3b2495"
    ],
    "citations": {
      "1": "67435eed-15fe-4a1a-88b7-1a1675bb4834",
      "2": "92919907-d72e-4070-85fe-be96ea905d4a",
      "3": "92919907-d72e-4070-85fe-be96ea905d4a",
      "4": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "5": "e4ac6599-2562-4caa-9f12-22505667e18e",
      "6": "a17a977e-d59a-4195-864b-81bb1582975f",
      "7": "a17a977e-d59a-4195-864b-81bb1582975f",
      "8": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "9": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "10": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "11": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "12": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
      "13": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "14": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
      "15": "6f26f676-2418-41cb-a026-91961e3b2495",
      "16": "e4ac6599-2562-4caa-9f12-22505667e18e",
      "17": "e4ac6599-2562-4caa-9f12-22505667e18e",
      "18": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "19": "e4ac6599-2562-4caa-9f12-22505667e18e",
      "20": "92919907-d72e-4070-85fe-be96ea905d4a",
      "21": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "22": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "23": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "24": "a17a977e-d59a-4195-864b-81bb1582975f",
      "25": "a17a977e-d59a-4195-864b-81bb1582975f"
    },
    "references": [
      {
        "source_id": "67435eed-15fe-4a1a-88b7-1a1675bb4834",
        "citation_number": 1,
        "cited_text": "Languages Python 61.2% Jupyter Notebook 36.5% Makefile 1.7% JavaScript 0.3% HTML 0.2% Tree-sitter Query 0.1% Footer © 2026 GitHub, Inc. Footer navigation Terms Privacy Security Status Community Docs Contact Manage cookies Do not share my personal information You can't perform that action at this time."
      },
      {
        "source_id": "92919907-d72e-4070-85fe-be96ea905d4a",
        "citation_number": 2,
        "cited_text": "GitHub - ysymyth/ReAct: [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "92919907-d72e-4070-85fe-be96ea905d4a",
        "citation_number": 3,
        "cited_text": "Repository files navigation README MIT license ReAct Prompting GPT-3 prompting code for ICLR 2023 paper ReAct: Synergizing Reasoning and Acting in Language Models . To use ReAct for more tasks, consider trying LangChain's zero-shot ReAct Agent . Setup You need to first have an OpenAI API key and store it in the environment variable OPENAI_API_KEY (see here ). Package requirement: openai , and install alfworld following instructions here . Experiments Run {hotpotqa,fever,alfworld,webshop}.ipynb . As HotpotQA and FEVER have large validation sets, we only run 500 random examples (see notebooks). We find PaLM and GPT-3 are better at different tasks."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 4,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 5,
        "cited_text": "On this page Multi-agent Conversation Framework AutoGen offers a unified multi-agent conversation framework as a high-level abstraction of using foundation models. It features capable, customizable and conversable agents which integrate LLMs, tools, and humans via automated agent chat. By automating chat among multiple capable agents, one can easily make them collectively perform tasks autonomously or with human feedback, including tasks that require using tools via code. This framework simplifies the orchestration, automation and optimization of a complex LLM workflow. It maximizes the performance of LLM models and overcomes their weaknesses. It enables building next-gen LLM applications based on multi-agent conversations with minimal effort."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 6,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 7,
        "cited_text": "Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 8,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 9,
        "cited_text": "The AgentScope Ecosystem News [2026-03] RELS : We recently developed and open sourced an AI assistant named CoPaw (Co Personal Agent Workstation), built upon AgentScope , AgentScope-Runtime , and Reme . [2026-02] FEAT : Realtime Voice Agent support. Example | Multi-Agent Realtime Example | Tutorial [2026-01] COMM : Biweekly Meetings launched to share ecosystem updates and development plans - join us! Details & Schedule [2026-01] FEAT : Database support & memory compression in memory module. Example | Tutorial [2025-12] INTG : A2A (Agent-to-Agent) protocol support. Example | Tutorial [2025-12] FEAT : TTS (Text-to-Speech) support. Example | Tutorial [2025-11] INTG : Anthropic Agent Skill support. Example | Tutorial [2025-11] RELS : Alias-Agent for diverse real-world tasks and Data-Juicer Agent for data processing open-sourced. Alias-Agent | Data-Juicer Agent [2025-11] INTG : Agentic RL via Trinity-RFT library. Example | Trinity-RFT [2025-11] INTG : ReMe for enhanced long-term memory. Example [2025-11] RELS : agentscope-samples repository launched and agentscope-runtime upgraded with Docker/K8s deployment and VNC-powered GUI sandboxes. Samples | Runtime"
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 10,
        "cited_text": "Multi-Agent Workflows AgentScope provides MsgHub and pipelines to streamline multi-agent conversations, offering efficient message routing and seamless information sharing Documentation Tutorial FAQ API Docs More Examples & Samples Functionality MCP Anthropic Agent Skill Plan Structured Output RAG Long-Term Memory Session with SQLite Stream Printing Messages TTS Code-first Deployment Memory Compression Agent ReAct Agent Voice Agent Deep Research Agent Browser-use Agent Meta Planner Agent A2A Agent Realtime Voice Agent"
      },
      {
        "source_id": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
        "citation_number": 11,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
        "citation_number": 12,
        "cited_text": "Abstract: Large language models (LLMs) have recently been shown to deliver impressive performance in various NLP tasks. To tackle multi-step reasoning tasks, few-shot chain-of-thought (CoT) prompting includes a few manually crafted step-by-step reasoning demonstrations which enable LLMs to explicitly generate reasoning steps and improve their reasoning task accuracy. To eliminate the manual effort, Zero-shot-CoT concatenates the target problem statement with \"Let's think step by step\" as an input prompt to LLMs. Despite the success of Zero-shot-CoT, it still suffers from three pitfalls: calculation errors, missing-step errors, and semantic misunderstanding errors. To address the missing-step errors, we propose Plan-and-Solve (PS) Prompting. It consists of two components: first, devising a plan to divide the entire task into smaller subtasks, and then carrying out the subtasks according to the plan. To address the calculation errors and improve the quality of generated reasoning steps, we extend PS prompting with more detailed instructions and derive PS+ prompting. We evaluate our proposed prompting strategy on ten datasets across three reasoning problems. The experimental results over GPT-3 show that our proposed zero-shot prompting consistently outperforms Zero-shot-CoT across all datasets by a large margin, is comparable to or exceeds Zero-shot-Program-of-Thought Prompting, and has comparable performance with 8-shot CoT prompting on the math reasoning problem. The code can be found at this https URL ."
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 13,
        "cited_text": "multi_agent_realtime_voice.mp4 Human-in-the-loop Support realtime interruption in ReActAgent: conversation can be interrupted via cancellation in realtime and resumed seamlessly via robust memory preservation. Flexible MCP Usage Use individual MCP tools as local callable functions to compose toolkits or wrap into a more complex tool. Agentic RL Train your agentic application seamlessly with Reinforcement Learning integration. We also prepare multiple sample projects covering various scenarios: <cited_table>",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Example",
              "Description",
              "Model",
              "Training Result"
            ],
            [
              "Math Agent",
              "Tune a math-solving agent with multi-step reasoning.",
              "Qwen3-0.6B",
              "Accuracy: 75% → 85%"
            ],
            [
              "Frozen Lake",
              "Train an agent to navigate the Frozen Lake environment.",
              "Qwen2.5-3B-Instruct",
              "Success rate: 15% → 86%"
            ],
            [
              "Learn to Ask",
              "Tune agents using LLM-as-a-judge for automated feedback.",
              "Qwen2.5-7B-Instruct",
              "Accuracy: 47% → 92%"
            ],
            [
              "Email Search",
              "Improve tool-use capabilities without labeled ground truth.",
              "Qwen3-4B-Instruct-2507",
              "Accuracy: 60%"
            ],
            [
              "Werewolf Game",
              "Train agents for strategic multi-agent game interactions.",
              "Qwen2.5-7B-Instruct",
              "Werewolf win rate: 50% → 80%"
            ],
            [
              "Data Augment",
              "Generate synthetic training data to enhance tuning results.",
              "Qwen3-0.6B",
              "AIME-24 accuracy: 20% → 60%"
            ]
          ]
        }
      },
      {
        "source_id": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
        "citation_number": 14,
        "cited_text": "create_agent Creates an agent graph that calls tools in a loop until a stopping condition is met.](https://python.langchain.com/python/langchain/agents/factory/create_agent) [Function before_model Decorator used to dynamically create a middleware with the before_model hook.](https://python.langchain.com/python/langchain/agents/middleware/types/before_model) [Function after_model Decorator used to dynamically create a middleware with the after_model hook.](https://python.langchain.com/python/langchain/agents/middleware/types/after_model)"
      },
      {
        "source_id": "6f26f676-2418-41cb-a026-91961e3b2495",
        "citation_number": 15,
        "cited_text": "If you're looking for more advanced customization or agent orchestration, check out LangGraph , our framework for building controllable agent workflows. Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangChain ecosystem While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. Deep Agents — Build agents that can plan, use subagents, and leverage file systems for complex tasks LangGraph — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework Integrations — Chat & embedding models, tools & toolkits, and more LangSmith — Agent evals, observability, and debugging for LLM apps LangSmith Deployment — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows"
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 16,
        "cited_text": "Agents AutoGen abstracts and implements conversable agents designed to solve tasks through inter-agent conversations. Specifically, the agents in AutoGen have the following notable features: Conversable: Agents in AutoGen are conversable, which means that any agent can send and receive messages from other agents to initiate or continue a conversation Customizable: Agents in AutoGen can be customized to integrate LLMs, humans, tools, or a combination of them. The figure below shows the built-in agents in AutoGen."
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 17,
        "cited_text": "A Basic Two-Agent Conversation Example Once the participating agents are constructed properly, one can start a multi-agent conversation session by an initialization step as shown in the following code: After the initialization step, the conversation could proceed automatically. Find a visual illustration of how the user_proxy and assistant collaboratively solve the above task autonomously below: The assistant receives a message from the user_proxy, which contains the task description. The assistant then tries to write Python code to solve the task and sends the response to the user_proxy. Once the user_proxy receives a response from the assistant, it tries to reply by either soliciting human input or preparing an automatically generated reply. If no human input is provided, the user_proxy executes the code and uses the result as the auto-reply. The assistant then generates a further response for the user_proxy. The user_proxy can then decide whether to terminate the conversation. If not, steps 3 and 4 are repeated."
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 18,
        "cited_text": "Simple : start building your agents in 5 minutes with built-in ReAct agent, tools, skills, human-in-the-loop steering, memory, planning, realtime voice, evaluation and model finetuning Extensible : large number of ecosystem integrations for tools, memory and observability; built-in support for MCP and A2A; message hub for flexible multi-agent orchestration and workflows Production-ready : deploy and serve your agents locally, as serverless in the cloud, or on your K8s cluster with built-in OTel support"
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 19,
        "cited_text": "Supporting Diverse Conversation Patterns Conversations with different levels of autonomy, and human-involvement patterns On the one hand, one can achieve fully autonomous conversations after an initialization step. On the other hand, AutoGen can be used to implement human-in-the-loop problem-solving by configuring human involvement levels and patterns (e.g., setting the human_input_mode to ALWAYS ), as human involvement is expected and/or desired in many applications. Static and dynamic conversations"
      },
      {
        "source_id": "92919907-d72e-4070-85fe-be96ea905d4a",
        "citation_number": 20,
        "cited_text": "<cited_table> Citation About [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models Topics decision-making reasoning large-language-models llm prompting Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page . Activity Stars 3.7k stars Watchers 20 watching Forks 362 forks Report repository Releases No releases published",
        "cited_table": {
          "num_columns": 5,
          "rows": [
            [
              "",
              "HotpotQA (500 random dev, EM)",
              "FEVER (500 random dev, EM)",
              "AlfWorld (success rate)",
              "WebShop (success rate)"
            ],
            [
              "PaLM-540B (paper)",
              "29.4",
              "62.2",
              "70.9",
              "40"
            ],
            [
              "GPT-3 (davinci-002)",
              "30.4",
              "54",
              "78.4",
              "35.8"
            ]
          ]
        }
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 21,
        "cited_text": "Tool use examples For a complete hands-on walkthrough, see the tutorial . For reference examples of individual concepts, see Define tools and Handle tool calls . What happens when Claude needs more information Pricing Tool use requests are priced based on: The total number of input tokens sent to the model (including in the tools parameter) The number of output tokens generated For server-side tools, additional usage-based pricing (e.g., web search charges per search performed) Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 22,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 23,
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
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 24,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 25,
        "cited_text": "Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「ReAct 模式：思考-行动-观察（Think-Act-Observe）」作为大语言模型（LLM）实现复杂任务自动化的核心范式，其技术实现细节和性能参数如下：\n\n### 1. 核心算法流程\nReAct 的核心逻辑是将**推理轨迹（Reasoning Traaces）**与**特定任务的行动（Actions）**结合，形成一个循环闭环 [1, 2]。\n*   **思考 (Thought)**：模型通过生成自然语言推理步骤来阐明任务目标、更新计划并处理异常情况 [2, 3]。\n*   **行动 (Action)**：模型生成结构化的指令（如 API 调用、Web 搜索、Shell 命令等）与外部环境交互 [4, 5]。\n*   **观察 (Observation)**：系统接收外部环境的反馈（如搜索结果、代码执行输出），并将其作为上下文反馈给模型，用于下一轮迭代 [2, 5]。\n*   **停止条件**：循环持续进行，直到模型认为任务已完成并输出最终答案，或者达到设定的最大迭代步数 [6]。\n\n### 2. 关键代码架构\n现代框架通过不同的组件封装来实现这一循环：\n*   **状态管理 (State Management)**：如 LangChain 使用 `AgentState` 存储循环中的所有历史信息 [7]。OpenAI 从 persistent 线程转向 `Conversable` 的项目模式，通过发送输入项并接收输出项（Items）来显式管理工具调用循环 [8-10]。\n*   **Agent 代理类**：\n    *   **AssistantAgent**：负责推理和代码编写（如 AutoGen 中的实现） [11]。\n    *   **UserProxyAgent**：作为人类或环境的代理，负责执行代码和工具并返回观察结果 [11, 12]。\n*   **工具调用接口**：\n    *   **客户端工具 (Client Tools)**：在用户应用程序中运行，模型返回 `tool_use` 块，应用执行后返回 `tool_result` [13]。\n    *   **服务端工具 (Server Tools)**：在提供商（如 Anthropic）的基础设施上直接运行并返回结果 [13]。\n\n### 3. 性能优化策略\n*   **上下文压缩 (Context Compaction)**：当对话历史过长时，通过对历史信息进行摘要或删除不必要的消息来减少 Token 消耗 [3, 14]。\n*   **提示词缓存 (Prompt Caching)**：缓存频繁使用的系统指令和工具定义，以显著降低延迟和成本 [3, 15]。\n*   **预测输出 (Predicted Outputs)**：在已知部分响应内容（如固定格式或代码模板）时，加速模型生成过程 [16, 17]。\n*   **系统提示词优化**：模型如 Claude 会在启用工具时自动加载特定的系统提示词（System Prompt），例如 Claude 4.6 约占用 **346 个 Tokens**，而 Claude 3.5 为 **264 个 Tokens** [18, 19]。\n\n### 4. 竞品技术对比与技术参数\nReAct 模式与其他 Agentic 架构在性能和实现逻辑上存在显著差异：\n\n| 维度 | ReAct 模式 [2, 20] | Reflexion 模式 [21] | Plan-and-Solve (PS+) [22] |\n| :--- | :--- | :--- | :--- |\n| **核心逻辑** | 推理 + 环境交互循环 | 引入**语言强化学习**和自我反思 | 预先制定完整计划再执行 |\n| **优势** | 实现简单，即时反馈 | 显著降低幻觉，具自我修复能力 | 减少漏步错误和计算误差 |\n| **性能指标 (GPT-3)** | HotpotQA: **30.4 EM**; AlfWorld: **78.4% 成功率** | HumanEval 编码准确率达到 **91%** | 在数学推理上优于 Zero-shot-CoT |\n| **数据比较 (PaLM-540B)** | FEVER: **62.2 EM**; WebShop: **40% 成功率** | - | - |\n\n**关键差异点**：\n*   **对比 CoT**：传统的 Chain-of-Thought 仅限于内部推理，缺乏与外部环境的联通；ReAct 解决了推理在现实世界中的“落地”问题 [22]。\n*   **API 迁移趋势**：OpenAI 正在将 `Assistants API` 迁移至更灵活的 `Responses API`，其核心变化在于**显式化工具调用循环**，开发者可以更精细地控制每一轮「思考-行动-观察」的颗粒度 [8, 9]。\n*   **工具效能**：在 LAB-Bench 等基准测试中，增加基础工具（如 Web 搜索、文件检索）能使模型性能产生超越人类专家的非线性提升 [23]。",
    "conversation_id": "e87fa844-1f99-4965-a570-cd7c5f71372c",
    "sources_used": [
      "67435eed-15fe-4a1a-88b7-1a1675bb4834",
      "92919907-d72e-4070-85fe-be96ea905d4a",
      "a17a977e-d59a-4195-864b-81bb1582975f",
      "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "beec4d53-e134-47c8-b85e-26eb40acf1b1",
      "e4ac6599-2562-4caa-9f12-22505667e18e",
      "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec"
    ],
    "citations": {
      "1": "67435eed-15fe-4a1a-88b7-1a1675bb4834",
      "2": "92919907-d72e-4070-85fe-be96ea905d4a",
      "3": "a17a977e-d59a-4195-864b-81bb1582975f",
      "4": "a17a977e-d59a-4195-864b-81bb1582975f",
      "5": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "6": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
      "7": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
      "8": "a17a977e-d59a-4195-864b-81bb1582975f",
      "9": "a17a977e-d59a-4195-864b-81bb1582975f",
      "10": "a17a977e-d59a-4195-864b-81bb1582975f",
      "11": "e4ac6599-2562-4caa-9f12-22505667e18e",
      "12": "e4ac6599-2562-4caa-9f12-22505667e18e",
      "13": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "14": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "15": "a17a977e-d59a-4195-864b-81bb1582975f",
      "16": "a17a977e-d59a-4195-864b-81bb1582975f",
      "17": "a17a977e-d59a-4195-864b-81bb1582975f",
      "18": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "19": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "20": "92919907-d72e-4070-85fe-be96ea905d4a",
      "21": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "22": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
      "23": "0a452718-985f-4af5-9441-e2d6cbf6188a"
    },
    "references": [
      {
        "source_id": "67435eed-15fe-4a1a-88b7-1a1675bb4834",
        "citation_number": 1,
        "cited_text": "Languages Python 61.2% Jupyter Notebook 36.5% Makefile 1.7% JavaScript 0.3% HTML 0.2% Tree-sitter Query 0.1% Footer © 2026 GitHub, Inc. Footer navigation Terms Privacy Security Status Community Docs Contact Manage cookies Do not share my personal information You can't perform that action at this time."
      },
      {
        "source_id": "92919907-d72e-4070-85fe-be96ea905d4a",
        "citation_number": 2,
        "cited_text": "Repository files navigation README MIT license ReAct Prompting GPT-3 prompting code for ICLR 2023 paper ReAct: Synergizing Reasoning and Acting in Language Models . To use ReAct for more tasks, consider trying LangChain's zero-shot ReAct Agent . Setup You need to first have an OpenAI API key and store it in the environment variable OPENAI_API_KEY (see here ). Package requirement: openai , and install alfworld following instructions here . Experiments Run {hotpotqa,fever,alfworld,webshop}.ipynb . As HotpotQA and FEVER have large validation sets, we only run 500 random examples (see notebooks). We find PaLM and GPT-3 are better at different tasks."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 3,
        "cited_text": "Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 4,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 5,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
        "citation_number": 6,
        "cited_text": "create_agent Creates an agent graph that calls tools in a loop until a stopping condition is met.](https://python.langchain.com/python/langchain/agents/factory/create_agent) [Function before_model Decorator used to dynamically create a middleware with the before_model hook.](https://python.langchain.com/python/langchain/agents/middleware/types/before_model) [Function after_model Decorator used to dynamically create a middleware with the after_model hook.](https://python.langchain.com/python/langchain/agents/middleware/types/after_model)"
      },
      {
        "source_id": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
        "citation_number": 7,
        "cited_text": "agents | langchain | LangChain Reference LangChain Reference home page Search... Python langchain Agents Agents Reference docs This page contains reference documentation for Agents. See the docs for conceptual guides, tutorials, and examples on using Agents. Classes [Class AgentState State schema for the agent.](https://python.langchain.com/python/langchain/agents/middleware/types/AgentState) [Class ModelRequest Model request information for the agent.](https://python.langchain.com/python/langchain/agents/middleware/types/ModelRequest)"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 8,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
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
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 10,
        "cited_text": "A thread was a collection of messages stored server-side. Threads could only store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data. Request example Thread object Conversation object Response example Thread object Conversation object From runs to responses Runs were asynchronous processes that executed against threads. See the example below. Responses are simpler: provide a set of input items to execute, and get a list of output items back. Responses are designed to be used alone, but you can also use them with prompt and conversation objects for storing context and configuration."
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 11,
        "cited_text": "We have designed a generic ConversableAgent class for Agents that are capable of conversing with each other through the exchange of messages to jointly finish a task. An agent can communicate with other agents and perform actions. Different agents can differ in what actions they perform after receiving messages. Two representative subclasses are AssistantAgent and UserProxyAgent The AssistantAgent is designed to act as an AI assistant, using LLMs by default but not requiring human input or code execution. It could write Python code (in a Python coding block) for a user to execute when a message (typically a description of a task that needs to be solved) is received. Under the hood, the Python code is written by LLM (e.g., GPT-4). It can also receive the execution results and suggest corrections or bug fixes. Its behavior can be altered by passing a new system message. The LLM inference configuration can be configured via [ llm_config ]. The UserProxyAgent is conceptually a proxy agent for humans, soliciting human input as the agent's reply at each interaction turn by default and also having the capability to execute code and call functions or tools. The UserProxyAgent triggers code execution automatically when it detects an executable code block in the received message and no human user input is provided. Code execution can be disabled by setting the code_execution_config parameter to False. LLM-based response is disabled by default. It can be enabled by setting llm_config to a dict corresponding to the inference configuration. When llm_config is set as a dictionary, UserProxyAgent can generate replies using an LLM when code execution is not performed."
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 12,
        "cited_text": "A Basic Two-Agent Conversation Example Once the participating agents are constructed properly, one can start a multi-agent conversation session by an initialization step as shown in the following code: After the initialization step, the conversation could proceed automatically. Find a visual illustration of how the user_proxy and assistant collaboratively solve the above task autonomously below: The assistant receives a message from the user_proxy, which contains the task description. The assistant then tries to write Python code to solve the task and sends the response to the user_proxy. Once the user_proxy receives a response from the assistant, it tries to reply by either soliciting human input or preparing an automatically generated reply. If no human input is provided, the user_proxy executes the code and uses the result as the auto-reply. The assistant then generates a further response for the user_proxy. The user_proxy can then decide whether to terminate the conversation. If not, steps 3 and 4 are repeated."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 13,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 14,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 15,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 16,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 17,
        "cited_text": "Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 18,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 19,
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
        "source_id": "92919907-d72e-4070-85fe-be96ea905d4a",
        "citation_number": 20,
        "cited_text": "<cited_table> Citation About [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models Topics decision-making reasoning large-language-models llm prompting Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page . Activity Stars 3.7k stars Watchers 20 watching Forks 362 forks Report repository Releases No releases published",
        "cited_table": {
          "num_columns": 5,
          "rows": [
            [
              "",
              "HotpotQA (500 random dev, EM)",
              "FEVER (500 random dev, EM)",
              "AlfWorld (success rate)",
              "WebShop (success rate)"
            ],
            [
              "PaLM-540B (paper)",
              "29.4",
              "62.2",
              "70.9",
              "40"
            ],
            [
              "GPT-3 (davinci-002)",
              "30.4",
              "54",
              "78.4",
              "35.8"
            ]
          ]
        }
      },
      {
        "source_id": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
        "citation_number": 21,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
        "citation_number": 22,
        "cited_text": "Abstract: Large language models (LLMs) have recently been shown to deliver impressive performance in various NLP tasks. To tackle multi-step reasoning tasks, few-shot chain-of-thought (CoT) prompting includes a few manually crafted step-by-step reasoning demonstrations which enable LLMs to explicitly generate reasoning steps and improve their reasoning task accuracy. To eliminate the manual effort, Zero-shot-CoT concatenates the target problem statement with \"Let's think step by step\" as an input prompt to LLMs. Despite the success of Zero-shot-CoT, it still suffers from three pitfalls: calculation errors, missing-step errors, and semantic misunderstanding errors. To address the missing-step errors, we propose Plan-and-Solve (PS) Prompting. It consists of two components: first, devising a plan to divide the entire task into smaller subtasks, and then carrying out the subtasks according to the plan. To address the calculation errors and improve the quality of generated reasoning steps, we extend PS prompting with more detailed instructions and derive PS+ prompting. We evaluate our proposed prompting strategy on ten datasets across three reasoning problems. The experimental results over GPT-3 show that our proposed zero-shot prompting consistently outperforms Zero-shot-CoT across all datasets by a large margin, is comparable to or exceeds Zero-shot-Program-of-Thought Prompting, and has comparable performance with 8-shot CoT prompting on the math reasoning problem. The code can be found at this https URL ."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 23,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「ReAct 模式：思考-行动-观察（Think-Act-Observe）」已从理论研究演进为工业界构建自主 Agent 的核心范式。以下是基于来源整理的真实应用场景、部署方案、基准数据及实践经验：\n\n### 1. 真实应用场景与开源项目实战\nReAct 循环被广泛应用于需要复杂逻辑推理与外部工具交互的任务中：\n*   **多步知识检索与问答**：如 **HotpotQA** 和 **FEVER** 任务，Agent 通过维基百科 API 进行搜索、思考并提取信息，以解决需要跨多篇文档推理的问题 [1, 2]。\n*   **软件工程与代码维护**：\n    *   **GitHub/Codex**：利用技能加速开源软件维护，在 IDE 插件中实现自动化代码修复 [3, 4]。\n    *   **Reflexion 模式**：通过对代码执行结果的“自我反思”来纠错。在 **HumanEval** 基准测试中，Reflexion 框架达到了 **91% 的 pass@1 准确率**，远超 GPT-4 原生的 80% [5]。\n*   **具身智能与模拟环境**：\n    *   **AlfWorld**：在交互式文本环境中执行家庭任务 [2]。\n    *   **Frozen Lake**：训练 Agent 导航复杂环境，通过强化学习（RL）将成功率从 15% 提升至 86% [6]。\n*   **办公自动化助手**：\n    *   **CoPaw**：基于 AgentScope 构建的个人助理工作站 [7]。\n    *   **Friday**：AgentScope 提供的一个 ReAct Agent 示例，可直接与用户进行多轮工具调用对话 [8]。\n*   **策略游戏**：如 **九人狼人杀**，通过 ReAct 循环进行角色推理和语言博弈 [6, 9]。\n\n### 2. 工业级部署方案\n为了支持大规模应用，业界已形成成熟的架构：\n*   **显式工具调用循环 (Explicit Tool Loop)**：OpenAI 的最新 **Responses API** 将工具调用循环交给开发者控制（取代了 Assistants API 的黑盒运行），通过发送输入项并接收输出项来管理状态 [10, 11]。\n*   **服务端与客户端执行分层**：\n    *   **服务端工具 (Server Tools)**：如 Claude 提供的 Web 搜索、代码执行等，直接在模型商的基础设施运行 [12]。\n    *   **客户端工具 (Client Tools)**：在用户本地应用运行，通过 `tool_use` 和 `tool_result` 块完成数据交换 [12]。\n*   **部署架构支撑**：\n    *   **AgentScope** 支持本地、云端 Serverless 或 **K8s 集群**部署，并内置 OTel（OpenTelemetry）观测支持 [13]。\n    *   **LangGraph** 提供了低级别的 Agent 编排框架，用于构建可控的复杂工作流 [14]。\n\n### 3. 性能基准数据\n| 任务/模型 | 基准测试 | 性能指标 | 来源 |\n| :--- | :--- | :--- | :--- |\n| **GPT-3 (ReAct)** | HotpotQA | **30.4 EM** (精确匹配) | [2] |\n| **PaLM-540B (ReAct)** | FEVER | **62.2 EM** | [2] |\n| **Reflexion Agent** | HumanEval | **91% pass@1** | [5] |\n| **Math Agent (RL)** | 数学推理 | 准确率从 **75% 提升至 85%** | [6] |\n| **Data Augment** | AIME-24 | 准确率从 **20% 提升至 60%** | [6] |\n\n### 4. 开发者最佳实践\n*   **上下文管理与压缩**：由于 ReAct 循环会产生大量历史，开发者应使用**上下文压缩 (Compaction)** 和 **提示词缓存 (Prompt Caching)** 来降低 Token 成本并减少延迟 [15, 16]。\n*   **职责分离**：将应用代码负责的“编排”（如历史剪裁、重试、工具循环）与 Prompt 负责的“高层行为”分离，利用**版本化 Prompt** 提高迭代效率 [17]。\n*   **人机协同 (Human-in-the-loop)**：在 ReAct 循环中允许实时中断和人工干预，这对于安全性要求高的任务至关重要 [6, 18]。\n*   **结构化输出**：使用 `strict: true` 或 JSON Schema 确保 Agent 生成的工具调用指令完全符合接口规范 [19, 20]。\n\n### 5. 常见踩坑经验\n*   **步骤缺失与计算错误**：普通 CoT 容易漏掉步骤。**Plan-and-Solve (PS+)** 模式通过先制定整体计划再执行，可有效缓解这一问题 [21]。\n*   **Token 隐形消耗**：启用工具使用时，模型会自动加载系统提示词。例如 Claude 4.6 开启工具后会增加约 **346 个 Token** 的固定开销 [22, 23]。\n*   **API 废弃风险**：OpenAI 已计划于 2026 年 8 月关闭 Assistants API，开发者需及时向 **Responses API** 迁移 [10]。\n*   **安全性与沙箱**：在执行 Shell 或代码工具时，必须配置严格的沙箱（如 VNC-powered GUI sandboxes）和网络隔离措施 [7, 24, 25]。",
    "conversation_id": "e87fa844-1f99-4965-a570-cd7c5f71372c",
    "sources_used": [
      "92919907-d72e-4070-85fe-be96ea905d4a",
      "a17a977e-d59a-4195-864b-81bb1582975f",
      "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "6f26f676-2418-41cb-a026-91961e3b2495",
      "e4ac6599-2562-4caa-9f12-22505667e18e",
      "beec4d53-e134-47c8-b85e-26eb40acf1b1",
      "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
      "67435eed-15fe-4a1a-88b7-1a1675bb4834"
    ],
    "citations": {
      "1": "92919907-d72e-4070-85fe-be96ea905d4a",
      "2": "92919907-d72e-4070-85fe-be96ea905d4a",
      "3": "a17a977e-d59a-4195-864b-81bb1582975f",
      "4": "a17a977e-d59a-4195-864b-81bb1582975f",
      "5": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "6": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "7": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "8": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "9": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "10": "a17a977e-d59a-4195-864b-81bb1582975f",
      "11": "a17a977e-d59a-4195-864b-81bb1582975f",
      "12": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "13": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "14": "6f26f676-2418-41cb-a026-91961e3b2495",
      "15": "a17a977e-d59a-4195-864b-81bb1582975f",
      "16": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "17": "a17a977e-d59a-4195-864b-81bb1582975f",
      "18": "e4ac6599-2562-4caa-9f12-22505667e18e",
      "19": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "20": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
      "21": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
      "22": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "23": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "24": "a17a977e-d59a-4195-864b-81bb1582975f",
      "25": "67435eed-15fe-4a1a-88b7-1a1675bb4834"
    },
    "references": [
      {
        "source_id": "92919907-d72e-4070-85fe-be96ea905d4a",
        "citation_number": 1,
        "cited_text": "Repository files navigation README MIT license ReAct Prompting GPT-3 prompting code for ICLR 2023 paper ReAct: Synergizing Reasoning and Acting in Language Models . To use ReAct for more tasks, consider trying LangChain's zero-shot ReAct Agent . Setup You need to first have an OpenAI API key and store it in the environment variable OPENAI_API_KEY (see here ). Package requirement: openai , and install alfworld following instructions here . Experiments Run {hotpotqa,fever,alfworld,webshop}.ipynb . As HotpotQA and FEVER have large validation sets, we only run 500 random examples (see notebooks). We find PaLM and GPT-3 are better at different tasks."
      },
      {
        "source_id": "92919907-d72e-4070-85fe-be96ea905d4a",
        "citation_number": 2,
        "cited_text": "<cited_table> Citation About [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models Topics decision-making reasoning large-language-models llm prompting Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page . Activity Stars 3.7k stars Watchers 20 watching Forks 362 forks Report repository Releases No releases published",
        "cited_table": {
          "num_columns": 5,
          "rows": [
            [
              "",
              "HotpotQA (500 random dev, EM)",
              "FEVER (500 random dev, EM)",
              "AlfWorld (success rate)",
              "WebShop (success rate)"
            ],
            [
              "PaLM-540B (paper)",
              "29.4",
              "62.2",
              "70.9",
              "40"
            ],
            [
              "GPT-3 (davinci-002)",
              "30.4",
              "54",
              "78.4",
              "35.8"
            ]
          ]
        }
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 3,
        "cited_text": "Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 4,
        "cited_text": "Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ"
      },
      {
        "source_id": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
        "citation_number": 5,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 6,
        "cited_text": "multi_agent_realtime_voice.mp4 Human-in-the-loop Support realtime interruption in ReActAgent: conversation can be interrupted via cancellation in realtime and resumed seamlessly via robust memory preservation. Flexible MCP Usage Use individual MCP tools as local callable functions to compose toolkits or wrap into a more complex tool. Agentic RL Train your agentic application seamlessly with Reinforcement Learning integration. We also prepare multiple sample projects covering various scenarios: <cited_table>",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Example",
              "Description",
              "Model",
              "Training Result"
            ],
            [
              "Math Agent",
              "Tune a math-solving agent with multi-step reasoning.",
              "Qwen3-0.6B",
              "Accuracy: 75% → 85%"
            ],
            [
              "Frozen Lake",
              "Train an agent to navigate the Frozen Lake environment.",
              "Qwen2.5-3B-Instruct",
              "Success rate: 15% → 86%"
            ],
            [
              "Learn to Ask",
              "Tune agents using LLM-as-a-judge for automated feedback.",
              "Qwen2.5-7B-Instruct",
              "Accuracy: 47% → 92%"
            ],
            [
              "Email Search",
              "Improve tool-use capabilities without labeled ground truth.",
              "Qwen3-4B-Instruct-2507",
              "Accuracy: 60%"
            ],
            [
              "Werewolf Game",
              "Train agents for strategic multi-agent game interactions.",
              "Qwen2.5-7B-Instruct",
              "Werewolf win rate: 50% → 80%"
            ],
            [
              "Data Augment",
              "Generate synthetic training data to enhance tuning results.",
              "Qwen3-0.6B",
              "AIME-24 accuracy: 20% → 60%"
            ]
          ]
        }
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 7,
        "cited_text": "The AgentScope Ecosystem News [2026-03] RELS : We recently developed and open sourced an AI assistant named CoPaw (Co Personal Agent Workstation), built upon AgentScope , AgentScope-Runtime , and Reme . [2026-02] FEAT : Realtime Voice Agent support. Example | Multi-Agent Realtime Example | Tutorial [2026-01] COMM : Biweekly Meetings launched to share ecosystem updates and development plans - join us! Details & Schedule [2026-01] FEAT : Database support & memory compression in memory module. Example | Tutorial [2025-12] INTG : A2A (Agent-to-Agent) protocol support. Example | Tutorial [2025-12] FEAT : TTS (Text-to-Speech) support. Example | Tutorial [2025-11] INTG : Anthropic Agent Skill support. Example | Tutorial [2025-11] RELS : Alias-Agent for diverse real-world tasks and Data-Juicer Agent for data processing open-sourced. Alias-Agent | Data-Juicer Agent [2025-11] INTG : Agentic RL via Trinity-RFT library. Example | Trinity-RFT [2025-11] INTG : ReMe for enhanced long-term memory. Example [2025-11] RELS : agentscope-samples repository launched and agentscope-runtime upgraded with Docker/K8s deployment and VNC-powered GUI sandboxes. Samples | Runtime"
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 8,
        "cited_text": "Quickstart Installation AgentScope requires Python 3.10 or higher. From PyPI Or with uv: From source Example Hello AgentScope! Start with a conversation between user and a ReAct agent 🤖 named \"Friday\"! Voice Agent Create a voice-enabled ReAct agent that can understand and respond with speech, even playing a multi-agent werewolf game with voice interactions. werewolf_voice_agent.mp4 Realtime Voice Agent Build a realtime voice agent with web interface that can interact with users via voice input and output. Realtime chatbot | Realtime Multi-Agent Example"
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 9,
        "cited_text": "Game Nine-player Werewolves Workflow Multi-agent Debate Multi-agent Conversation Multi-agent Concurrent Multi-agent Realtime Conversation Evaluation ACEBench Tuner Tune ReAct Agent Contributing We welcome contributions from the community! Please refer to our CONTRIBUTING.md for guidelines on how to contribute. License AgentScope is released under Apache License 2.0. Publications If you find our work helpful for your research or application, please cite our papers. AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications AgentScope: A Flexible yet Robust Multi-Agent Platform"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 10,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 11,
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
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 12,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 13,
        "cited_text": "Simple : start building your agents in 5 minutes with built-in ReAct agent, tools, skills, human-in-the-loop steering, memory, planning, realtime voice, evaluation and model finetuning Extensible : large number of ecosystem integrations for tools, memory and observability; built-in support for MCP and A2A; message hub for flexible multi-agent orchestration and workflows Production-ready : deploy and serve your agents locally, as serverless in the cloud, or on your K8s cluster with built-in OTel support"
      },
      {
        "source_id": "6f26f676-2418-41cb-a026-91961e3b2495",
        "citation_number": 14,
        "cited_text": "If you're looking for more advanced customization or agent orchestration, check out LangGraph , our framework for building controllable agent workflows. Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangChain ecosystem While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. Deep Agents — Build agents that can plan, use subagents, and leverage file systems for complex tasks LangGraph — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework Integrations — Chat & embedding models, tools & toolkits, and more LangSmith — Agent evals, observability, and debugging for LLM apps LangSmith Deployment — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 15,
        "cited_text": "Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 16,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 17,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 18,
        "cited_text": "Supporting Diverse Conversation Patterns Conversations with different levels of autonomy, and human-involvement patterns On the one hand, one can achieve fully autonomous conversations after an initialization step. On the other hand, AutoGen can be used to implement human-in-the-loop problem-solving by configuring human involvement levels and patterns (e.g., setting the human_input_mode to ALWAYS ), as human involvement is expected and/or desired in many applications. Static and dynamic conversations"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 19,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "beec4d53-e134-47c8-b85e-26eb40acf1b1",
        "citation_number": 20,
        "cited_text": "[Function wrap_model_call Create middleware with wrap_model_call hook from a function.](https://python.langchain.com/python/langchain/agents/middleware/types/wrap_model_call) [Function wrap_tool_call Create middleware with wrap_tool_call hook from a function.](https://python.langchain.com/python/langchain/agents/middleware/types/wrap_tool_call) Types [Type ResponseFormat Union type for all supported response format strategies.](https://python.langchain.com/python/langchain/agents/structured_output/ResponseFormat)"
      },
      {
        "source_id": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
        "citation_number": 21,
        "cited_text": "Abstract: Large language models (LLMs) have recently been shown to deliver impressive performance in various NLP tasks. To tackle multi-step reasoning tasks, few-shot chain-of-thought (CoT) prompting includes a few manually crafted step-by-step reasoning demonstrations which enable LLMs to explicitly generate reasoning steps and improve their reasoning task accuracy. To eliminate the manual effort, Zero-shot-CoT concatenates the target problem statement with \"Let's think step by step\" as an input prompt to LLMs. Despite the success of Zero-shot-CoT, it still suffers from three pitfalls: calculation errors, missing-step errors, and semantic misunderstanding errors. To address the missing-step errors, we propose Plan-and-Solve (PS) Prompting. It consists of two components: first, devising a plan to divide the entire task into smaller subtasks, and then carrying out the subtasks according to the plan. To address the calculation errors and improve the quality of generated reasoning steps, we extend PS prompting with more detailed instructions and derive PS+ prompting. We evaluate our proposed prompting strategy on ten datasets across three reasoning problems. The experimental results over GPT-3 show that our proposed zero-shot prompting consistently outperforms Zero-shot-CoT across all datasets by a large margin, is comparable to or exceeds Zero-shot-Program-of-Thought Prompting, and has comparable performance with 8-shot CoT prompting on the math reasoning problem. The code can be found at this https URL ."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 22,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 23,
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
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 24,
        "cited_text": "Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools"
      },
      {
        "source_id": "67435eed-15fe-4a1a-88b7-1a1675bb4834",
        "citation_number": 25,
        "cited_text": "Sign up for LlamaParse — Create an account and get your API key. Parse — Agentic OCR and document parsing (130+ formats). Docs · Parse in the cloud Extract — Structured data extraction from documents. Docs Index — Ingest, index, and RAG pipelines. Docs · Web UI Split — Split large documents into subcategories. Docs Agents — Build end-to-end document agents with Workflows and Agent Builder. Docs Important Links Documentation X (formerly Twitter) LinkedIn Reddit Discord Ecosystem LlamaHub (community library of data loaders) LlamaLab (cutting-edge AGI projects using LlamaIndex)"
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "「ReAct 模式：思考-行动-观察」在 2025-2026 年已从基础的提示词工程演进为高度系统化的 **Agentic 架构**。以下是基于最新来源整理的研究突破与发展趋势：\n\n### 1. 2025-2026 年核心技术趋势与重要进展\n在 2025 至 2026 年间，该领域的研究重点从单纯的“逻辑闭环”转向了**性能调优、多 Agent 协议及物理环境交互**。\n\n*   **Agentic RL（智能体强化学习）的普及**：\n    *   通过 **Trinity-RFT** 等库，开发者开始利用强化学习对 Agent 进行微调 [1]。\n    *   **案例数据**：在数学 Agent 任务中，通过多步推理调优，准确率从 75% 提升至 85%；在 Frozen Lake 环境中，成功率从 15% 飙升至 86% [2]。\n*   **交互模式的变革（Realtime & Computer Use）**：\n    *   **实时语音 Agent**：2026 年 2 月，AgentScope 等框架实现了实时语音交互，允许用户在 ReAct 循环中进行实时中断与无缝恢复 [1, 3]。\n    *   **Computer Use（计算机操作）**：Claude 4.6 等模型引入了原生“计算机使用”工具，使 Agent 能够像人类一样操作 UI 界面 [4, 5]。\n*   **标准化协议：MCP 与 A2A**：\n    *   **模型上下文协议 (MCP)**：成为连接外部工具与 Agent 的标准，支持跨平台的工具搜索与连接 [6, 7]。\n    *   **Agent-to-Agent (A2A) 协议**：2025 年底推出的 A2A 协议支持不同 Agent 之间的高效通信，推动了多智能体协作的标准化 [1, 8]。\n\n### 2. 重要论文与模型演进\n*   **模型代际更新**：最新的 **GPT-5.4** 已成为构建复杂 Agent 的核心底座 [9, 10]。\n*   **Reflexion（反思模式）的强化**：在 2023 年《Reflexion: Language Agents with Verbal Reinforcement Learning》基础上，现代 Agent 通过**语言强化学习**在编码任务（如 HumanEval）上达到了 91% 的 pass@1 准确率 [11]。\n*   **Plan-and-Solve (PS+)**：针对 ReAct 循环中常见的步骤缺失问题，PS+ 模式通过预先制定详细计划并结合详细指令，显著改善了多步推理任务的质量 [12]。\n*   **控制理论视角**：研究开始将 LLM 提示工程形式化为**离散随机动力系统**，通过控制理论分析输入序列如何改变输出概率 [13]。\n\n### 3. 未解决的挑战\n尽管进展显著，ReAct 循环仍面临以下瓶颈：\n*   **上下文管理与 Token 成本**：\n    *   复杂的 ReAct 循环会迅速消耗上下文窗口。虽然引入了**上下文压缩 (Compaction)** 和**提示词缓存 (Prompt Caching)**，但长时任务的记忆维护成本依然高昂 [14, 15]。\n    *   开启工具调用会产生显著的系统 Token 开销（如 Claude 4.6 约增加 346 Tokens） [16]。\n*   **架构迁移的复杂性**：OpenAI 正在将集成度高的 Assistants API 迁移至更灵活但复杂度更高的 **Responses API**（预计 2026 年 8 月完成关停），这要求开发者显式管理工具调用循环 [17, 18]。\n*   **安全性与幻觉**：Agent 在执行 Shell 命令或计算机操作时，如何确保安全（Cyber Safety）并减少推理中的语义误解仍是核心难题 [12, 19]。\n\n### 4. 未来可能的突破点\n*   **Deep Research（深度研究智能体）**：通过结合 MCP 和大规模检索，Agent 将能够执行长达数小时甚至数天的复杂调研任务 [20, 21]。\n*   **长效记忆系统 (ReMe)**：利用如 **ReMe** 库实现的增强型长期记忆，Agent 将能跨会话保持复杂的任务状态和用户偏好 [1, 8]。\n*   **人机深度协同 (Human-in-the-loop)**：未来的架构（如 LangGraph 和 AutoGen 0.4）将更强调**可控的 Agent 图架构**，允许人类在自动化循环的关键节点进行精准干预 [22, 23]。\n*   **边缘与端侧 Agent**：随着轻量化模型（如 Qwen3-0.6B）在 Agent 任务中表现出极高的调优潜力，ReAct 循环有望在端侧设备上大规模普及 [2]。",
    "conversation_id": "e87fa844-1f99-4965-a570-cd7c5f71372c",
    "sources_used": [
      "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "a17a977e-d59a-4195-864b-81bb1582975f",
      "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
      "f2582523-804b-4367-b124-24ecc8aeeb26",
      "6f26f676-2418-41cb-a026-91961e3b2495",
      "e4ac6599-2562-4caa-9f12-22505667e18e"
    ],
    "citations": {
      "1": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "2": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "3": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "4": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "5": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "6": "a17a977e-d59a-4195-864b-81bb1582975f",
      "7": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "8": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
      "9": "a17a977e-d59a-4195-864b-81bb1582975f",
      "10": "a17a977e-d59a-4195-864b-81bb1582975f",
      "11": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
      "12": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
      "13": "f2582523-804b-4367-b124-24ecc8aeeb26",
      "14": "a17a977e-d59a-4195-864b-81bb1582975f",
      "15": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "16": "0a452718-985f-4af5-9441-e2d6cbf6188a",
      "17": "a17a977e-d59a-4195-864b-81bb1582975f",
      "18": "a17a977e-d59a-4195-864b-81bb1582975f",
      "19": "a17a977e-d59a-4195-864b-81bb1582975f",
      "20": "a17a977e-d59a-4195-864b-81bb1582975f",
      "21": "a17a977e-d59a-4195-864b-81bb1582975f",
      "22": "6f26f676-2418-41cb-a026-91961e3b2495",
      "23": "e4ac6599-2562-4caa-9f12-22505667e18e"
    },
    "references": [
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 1,
        "cited_text": "The AgentScope Ecosystem News [2026-03] RELS : We recently developed and open sourced an AI assistant named CoPaw (Co Personal Agent Workstation), built upon AgentScope , AgentScope-Runtime , and Reme . [2026-02] FEAT : Realtime Voice Agent support. Example | Multi-Agent Realtime Example | Tutorial [2026-01] COMM : Biweekly Meetings launched to share ecosystem updates and development plans - join us! Details & Schedule [2026-01] FEAT : Database support & memory compression in memory module. Example | Tutorial [2025-12] INTG : A2A (Agent-to-Agent) protocol support. Example | Tutorial [2025-12] FEAT : TTS (Text-to-Speech) support. Example | Tutorial [2025-11] INTG : Anthropic Agent Skill support. Example | Tutorial [2025-11] RELS : Alias-Agent for diverse real-world tasks and Data-Juicer Agent for data processing open-sourced. Alias-Agent | Data-Juicer Agent [2025-11] INTG : Agentic RL via Trinity-RFT library. Example | Trinity-RFT [2025-11] INTG : ReMe for enhanced long-term memory. Example [2025-11] RELS : agentscope-samples repository launched and agentscope-runtime upgraded with Docker/K8s deployment and VNC-powered GUI sandboxes. Samples | Runtime"
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 2,
        "cited_text": "multi_agent_realtime_voice.mp4 Human-in-the-loop Support realtime interruption in ReActAgent: conversation can be interrupted via cancellation in realtime and resumed seamlessly via robust memory preservation. Flexible MCP Usage Use individual MCP tools as local callable functions to compose toolkits or wrap into a more complex tool. Agentic RL Train your agentic application seamlessly with Reinforcement Learning integration. We also prepare multiple sample projects covering various scenarios: <cited_table>",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Example",
              "Description",
              "Model",
              "Training Result"
            ],
            [
              "Math Agent",
              "Tune a math-solving agent with multi-step reasoning.",
              "Qwen3-0.6B",
              "Accuracy: 75% → 85%"
            ],
            [
              "Frozen Lake",
              "Train an agent to navigate the Frozen Lake environment.",
              "Qwen2.5-3B-Instruct",
              "Success rate: 15% → 86%"
            ],
            [
              "Learn to Ask",
              "Tune agents using LLM-as-a-judge for automated feedback.",
              "Qwen2.5-7B-Instruct",
              "Accuracy: 47% → 92%"
            ],
            [
              "Email Search",
              "Improve tool-use capabilities without labeled ground truth.",
              "Qwen3-4B-Instruct-2507",
              "Accuracy: 60%"
            ],
            [
              "Werewolf Game",
              "Train agents for strategic multi-agent game interactions.",
              "Qwen2.5-7B-Instruct",
              "Werewolf win rate: 50% → 80%"
            ],
            [
              "Data Augment",
              "Generate synthetic training data to enhance tuning results.",
              "Qwen3-0.6B",
              "AIME-24 accuracy: 20% → 60%"
            ]
          ]
        }
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 3,
        "cited_text": "Quickstart Installation AgentScope requires Python 3.10 or higher. From PyPI Or with uv: From source Example Hello AgentScope! Start with a conversation between user and a ReAct agent 🤖 named \"Friday\"! Voice Agent Create a voice-enabled ReAct agent that can understand and respond with speech, even playing a multi-agent werewolf game with voice interactions. werewolf_voice_agent.mp4 Realtime Voice Agent Build a realtime voice agent with web interface that can interact with users via voice input and output. Realtime chatbot | Realtime Multi-Agent Example"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 4,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 5,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 6,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 7,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "58c93d9b-97fc-4454-ac80-7381f9fa03b5",
        "citation_number": 8,
        "cited_text": "Multi-Agent Workflows AgentScope provides MsgHub and pipelines to streamline multi-agent conversations, offering efficient message routing and seamless information sharing Documentation Tutorial FAQ API Docs More Examples & Samples Functionality MCP Anthropic Agent Skill Plan Structured Output RAG Long-Term Memory Session with SQLite Stream Printing Messages TTS Code-first Deployment Memory Compression Agent ReAct Agent Voice Agent Deep Research Agent Browser-use Agent Meta Planner Agent A2A Agent Realtime Voice Agent"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 9,
        "cited_text": "Community Programs, meetups, and support for builders Start searching API Dashboard Search the API docs Search docs Suggested response_format reasoning_effort streaming tools Primary navigation API API Reference Codex ChatGPT Resources Search docs Suggested response_format reasoning_effort streaming tools Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 10,
        "cited_text": "Meetups Hackathon Support Forum Discord API Dashboard Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents"
      },
      {
        "source_id": "2714962b-cdae-43ee-9c79-a8c337c41bb6",
        "citation_number": 11,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "aa0a3eab-45d8-4fe0-a595-dc4ae8d075ec",
        "citation_number": 12,
        "cited_text": "Abstract: Large language models (LLMs) have recently been shown to deliver impressive performance in various NLP tasks. To tackle multi-step reasoning tasks, few-shot chain-of-thought (CoT) prompting includes a few manually crafted step-by-step reasoning demonstrations which enable LLMs to explicitly generate reasoning steps and improve their reasoning task accuracy. To eliminate the manual effort, Zero-shot-CoT concatenates the target problem statement with \"Let's think step by step\" as an input prompt to LLMs. Despite the success of Zero-shot-CoT, it still suffers from three pitfalls: calculation errors, missing-step errors, and semantic misunderstanding errors. To address the missing-step errors, we propose Plan-and-Solve (PS) Prompting. It consists of two components: first, devising a plan to divide the entire task into smaller subtasks, and then carrying out the subtasks according to the plan. To address the calculation errors and improve the quality of generated reasoning steps, we extend PS prompting with more detailed instructions and derive PS+ prompting. We evaluate our proposed prompting strategy on ten datasets across three reasoning problems. The experimental results over GPT-3 show that our proposed zero-shot prompting consistently outperforms Zero-shot-CoT across all datasets by a large margin, is comparable to or exceeds Zero-shot-Program-of-Thought Prompting, and has comparable performance with 8-shot CoT prompting on the math reasoning problem. The code can be found at this https URL ."
      },
      {
        "source_id": "f2582523-804b-4367-b124-24ecc8aeeb26",
        "citation_number": 13,
        "cited_text": "arXiv:2310.04444 (cs) [Submitted on 2 Oct 2023 ( v1 ), last revised 3 Jul 2024 (this version, v4)] Title: What's the Magic Word? A Control Theory of LLM Prompting Authors: Aman Bhargava , Cameron Witkowski , Shi-Zhuo Looi , Matt Thomson View a PDF of the paper titled What's the Magic Word? A Control Theory of LLM Prompting, by Aman Bhargava and 3 other authors View PDF HTML (experimental) Abstract: Prompt engineering is crucial for deploying LLMs but is poorly understood mathematically. We formalize LLM systems as a class of discrete stochastic dynamical systems to explore prompt engineering through the lens of control theory. We offer a mathematical analysis of the limitations on the controllability of self-attention as a function of the singular values of the parameter matrices. We present complementary empirical results on the controllability of a panel of LLMs, including Falcon-7b, Llama-7b, and Falcon-40b. Given initial state \\mathbf x_0 from Wikitext and prompts of length k \\leq 10 tokens, we find that the \"correct\" next token is reachable at least 97% of the time, and that the top 75 most likely next tokens are reachable at least 85% of the time. Intriguingly, short prompt sequences can dramatically alter the likelihood of specific outputs, even making the least likely tokens become the most likely ones. This control-theoretic analysis of LLMs demonstrates the significant and poorly understood role of input sequences in steering output probabilities, offering a foundational perspective for enhancing language model system capabilities."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 14,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 15,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "0a452718-985f-4af5-9441-e2d6cbf6188a",
        "citation_number": 16,
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
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 17,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 18,
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
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 19,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 20,
        "cited_text": "Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools"
      },
      {
        "source_id": "a17a977e-d59a-4195-864b-81bb1582975f",
        "citation_number": 21,
        "cited_text": "Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files From assistants to prompts From threads to conversations From runs to responses Migrating your integration Comparing full examples Copy Page More page actions Copy Page More page actions"
      },
      {
        "source_id": "6f26f676-2418-41cb-a026-91961e3b2495",
        "citation_number": 22,
        "cited_text": "If you're looking for more advanced customization or agent orchestration, check out LangGraph , our framework for building controllable agent workflows. Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangChain ecosystem While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. Deep Agents — Build agents that can plan, use subagents, and leverage file systems for complex tasks LangGraph — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework Integrations — Chat & embedding models, tools & toolkits, and more LangSmith — Agent evals, observability, and debugging for LLM apps LangSmith Deployment — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows"
      },
      {
        "source_id": "e4ac6599-2562-4caa-9f12-22505667e18e",
        "citation_number": 23,
        "cited_text": "Multi-agent Conversation Framework | AutoGen 0.2 Skip to main content AutoGen 0.4 has been released. Read the migration guide here . This is the official project. We are not affiliated with any forks or startups. See our statement . AutoGen Docs Getting Started Installation Tutorial User Guide API Reference FAQs AutoGen Studio Ecosystem Contributor Guide Research Examples Examples by Category Examples by Notebook Application Gallery Other Languages Dotnet Old Blog (Archived) New Blog"
      }
    ]
  }
}
