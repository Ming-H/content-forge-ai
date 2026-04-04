# 知识库：Function Calling 深度解析：让 LLM 连接外部世界

生成时间: 2026-04-03 12:37
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "关于「Function Calling（函数调用）深度解析：让 LLM 连接外部世界」的核心技术架构与组件，根据现有资料可以从以下维度进行概述：\n\n### 一、 技术演进路线\nFunction Calling 的技术演进经历了从早期的简单提示工程到深度微调，再到如今原生支持和协议标准化的过程：\n1.  **提示工程阶段（Prompt-based Reasoning）**：早期模型主要依靠 **CoT（思维链）** 或 **ReAct** 等提示策略来尝试调用工具，但准确率较低且难以生成稳定的结构化参数 [1, 2]。\n2.  **指令微调阶段（Instruction Tuning）**：通过大规模 API 数据集（如 **APIBench** 或 **ToolBench**）对模型进行监督微调（SFT），使其具备理解复杂 API 文档并生成精确调用的能力，代表作包括 **Gorilla** 和 **ToolLLaMA** [3-5]。\n3.  **原生 API 支持阶段**：OpenAI、Gemini 和 Claude 等主流厂商在模型底层内置了对函数调用的支持，引入了独特的 **ID 映射机制** 和 **思维特征（Thought Signatures）**，以确保多轮对话中的上下文一致性 [6-8]。\n4.  **生态标准化阶段**：出现了如 **MCP（Model Context Protocol）** 这样的开放标准，旨在通过统一协议连接 AI 应用与外部工具及数据 [9, 10]。\n\n### 二、 核心算法与关键组件\n核心技术架构依赖于以下关键算法和组件：\n*   **DFSDT（基于深度优先搜索的决策树）**：用于 ToolLLM 框架中，显著增强了 LLM 的规划和推理能力，使其能处理包含多个 API 调用的复杂指令，并能在推理过程中评估多条路径 [1, 5]。\n*   **RAFT（检索增强微调）**：由 Gorilla 提出，通过在微调中加入检索到的文档（包含正确和干扰信息），提高模型对 API 文档变化的适应性并减少幻觉 [11-13]。\n*   **神经 API 检索器（Neural API Retriever）**：在面对数万个 API 的大规模场景时，该组件负责根据用户指令推荐最相关的工具，实现“开域”工具使用 [1, 5]。\n*   **思维特征（Thought Signatures）**：Gemini 3 等模型利用内部推理过程来决定何时调用函数。通过在多轮对话中传递这些特征，模型能保持推理的一致性 [14-16]。\n\n### 三、 主要架构模式\nFunction Calling 遵循一个循环的代理逻辑模式（Agentic Loop）：\n1.  **定义与声明**：开发者使用 **JSON Schema**（通常是 OpenAPI 的子集）在应用层定义函数名称、描述及参数约束 [17-20]。\n2.  **意图识别与参数生成**：模型分析用户输入，决定是否需要调用工具，并输出符合 Schema 的结构化 JSON（包含函数名和参数）[21-23]。\n3.  **执行侧差异化**：\n    *   **客户端工具（Client Tools）**：在开发者环境执行，模型仅返回指令（stop_reason: \"tool_use\"），安全性由开发者控制 [24]。\n    *   **服务器端工具（Server Tools）**：在模型厂商基础设施（如 Anthropic 的环境）上直接运行并返回结果 [24]。\n4.  **结果反馈与整合**：应用将执行结果回传给模型，模型结合结果生成最终的自然语言回复 [21, 25, 26]。\n\n### 四、 关键技术指标\n评估 Function Calling 性能的核心指标包括：\n*   **成功率/通过率（Pass Rate）**：在限定的 API 调用次数内成功完成指令的比例 [2, 27, 28]。\n*   **幻觉率（Hallucination Rate）**：模型生成错误 API 调用（如虚构参数或不存在的函数）的频率。Gorilla 等模型通过微调可将其显著降低 [4, 11, 13]。\n*   **端到端延迟（Latency）**：如 LiteLLM 代理服务器在 1k RPS 下的 P95 延迟可达到 **8ms** 左右 [29]。\n*   **工具容量（Tool Capacity）**：模型能同时处理或通过检索访问的 API 规模，从早期的几十个演进到支持 **16,000+** 个真实世界 API [3, 5, 13, 30]。\n*   **Schema 遵循度（Strict Mode Accuracy）**：开启 **Strict Mode** 后，模型输出完全符合 JSON Schema 定义的概率 [31, 32]。\n\n若您需要更深入的针对某一特定模型（如 Gemini 或 OpenAI）的架构分析，我可以为您创建一份**深度研究报告**。",
    "conversation_id": "6644b4c8-4688-4d87-b7ac-5f06f7119a94",
    "sources_used": [
      "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "7c52ee01-0056-43bb-9fc9-a17792878206",
      "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "2be6827b-3272-4f52-af8e-e3daa4204826",
      "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "c996bde3-6773-40e5-8860-77bf34569653"
    ],
    "citations": {
      "1": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "2": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "3": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "4": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "5": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "6": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "7": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "8": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "9": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "10": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "11": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "12": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "13": "2be6827b-3272-4f52-af8e-e3daa4204826",
      "14": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "15": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "16": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "17": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "18": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "19": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "20": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "21": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "22": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "23": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "24": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "25": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "26": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "27": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "28": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "29": "c996bde3-6773-40e5-8860-77bf34569653",
      "30": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "31": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "32": "dc281e96-2bed-443d-a0b9-d44e12d990e1"
    },
    "references": [
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 1,
        "cited_text": "✨Here is an overview of the dataset construction, training, and evaluation. ✨✨Features: API Collection : we gather 16464 representational state transfer (REST) APIs from RapidAPI , a platform that hosts massive real-world APIs provided by developers. Instruction Generation : we curate instructions that involve both single-tool and multi-tool scenarios. Answer Annotation : we develop a novel depth-first search based decision tree (DFSDT) to bolster the planning and reasoning ability of LLMs, which significantly improves the annotation efficiency and successfully annotates those complex instructions that cannot be answered with CoT or ReACT. We provide responses that not only include the final answer but also incorporate the model's reasoning process, tool execution, and tool execution results . API Retriver : we incorporate API retrieval to equip ToolLLaMA with open-domain tool-using abilities. All the data is automatically generated by OpenAI API and filtered by us, the whole data creation process is easy to scale up."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 2,
        "cited_text": "Web UI The app will be available on http://localhost:3000/ Backend server This server will be available on http://localhost:5000/ . To start a request, call http://localhost:5000/stream with a GET or POST request containing a JSON object with the following fields: ToolEval By fine-tuning LLaMA on ToolBench, we obtain ToolLLaMA . Considering that human evaluation can be time-consuming, we follow AlpacaEval to develop an efficient machine evaluator ToolEval , which incorporates two evaluation metrics: Pass Rate : Calculates the proportion of successfully completing an instruction within limited OpenAI API calls. Preference : Measured by comparing two answers (action sequences) for a given instruction. We pre-define a set of criteria for a better answer, which are organized as prompts for ChatGPT. We provide the test instruction and two candidate answers to the evaluator and obtain its preference. We evaluate each answer pair multiple times to improve the reliability of our system. Then we calculate the Win Rate (percentage of being preferred by the evaluator). More details can be found in our paper."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 3,
        "cited_text": "Repository files navigation README Apache-2.0 license 🛠ToolBench🤖 Model • Data Release • Web Demo • Tool Eval • Paper • Citation 🔨This project (ToolLLM) aims to construct open-source, large-scale, high-quality instruction tuning SFT data to facilitate the construction of powerful LLMs with general tool-use capability. We aim to empower open-source LLMs to master thousands of diverse real-world APIs. We achieve this by collecting a high-quality instruction-tuning dataset. It is constructed automatically using the latest ChatGPT (gpt-3.5-turbo-16k), which is upgraded with enhanced function call capabilities. We provide the dataset, the corresponding training and evaluation scripts, and a capable model ToolLLaMA fine-tuned on ToolBench."
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 4,
        "cited_text": "About Gorilla enables LLMs to use tools by invoking APIs. Given a natural language query, Gorilla comes up with the semantically- and syntactically- correct API to invoke. With Gorilla, we are the first to demonstrate how to use LLMs to invoke 1,600+ (and growing) API calls accurately while reducing hallucination. This repository contains inference code for running Gorilla finetuned models, evaluation code for reproducing results from our paper, and APIBench - the largest collection of APIs, curated and easy to be trained on!"
      },
      {
        "source_id": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
        "citation_number": 5,
        "cited_text": "View PDF Abstract: Despite the advancements of open-source large language models (LLMs), e.g., LLaMA, they remain significantly limited in tool-use capabilities, i.e., using external tools (APIs) to fulfill human instructions. The reason is that current instruction tuning largely focuses on basic language tasks but ignores the tool-use domain. This is in contrast to the excellent tool-use capabilities of state-of-the-art (SOTA) closed-source LLMs, e.g., ChatGPT. To bridge this gap, we introduce ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation. We first present ToolBench, an instruction-tuning dataset for tool use, which is constructed automatically using ChatGPT. Specifically, the construction can be divided into three stages: (i) API collection: we collect 16,464 real-world RESTful APIs spanning 49 categories from RapidAPI Hub; (ii) instruction generation: we prompt ChatGPT to generate diverse instructions involving these APIs, covering both single-tool and multi-tool scenarios; (iii) solution path annotation: we use ChatGPT to search for a valid solution path (chain of API calls) for each instruction. To enhance the reasoning capabilities of LLMs, we develop a novel depth-first search-based decision tree algorithm. It enables LLMs to evaluate multiple reasoning traces and expand the search space. Moreover, to evaluate the tool-use capabilities of LLMs, we develop an automatic evaluator: ToolEval. Based on ToolBench, we fine-tune LLaMA to obtain an LLM ToolLLaMA, and equip it with a neural API retriever to recommend appropriate APIs for each instruction. Experiments show that ToolLLaMA demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, and exhibits comparable performance to ChatGPT. Our ToolLLaMA also demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 6,
        "cited_text": "Important: Gemini 3 model APIs now generate a unique id for every function call. If you are manually constructing the conversation history or using the REST API, when returning the result of your executed function to the model we recommend passing the matching id in your functionResponse . If you are using the standard Python or Node.js SDKs, this is handled automatically. Get Weather Schedule Meeting Create Chart Python JavaScript REST More How function calling works Function calling involves a structured interaction between your application, the model, and external functions. Here's a breakdown of the process:"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 7,
        "cited_text": "Responses Copy Page More page actions Function calling Give models access to new functionality and data they can use to follow instructions and respond to prompts. Function calling (also known as tool calling ) provides a powerful and flexible way for OpenAI models to interface with external systems and access data outside their training data. This guide shows how you can connect a model to data and actions provided by your application. We'll show how to use function tools (defined by a JSON schema) and custom tools which work with free form text inputs and outputs."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 8,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 9,
        "cited_text": "Model context protocol (MCP) Model Context Protocol (MCP) is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts. The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 10,
        "cited_text": "Here, you can find an example of how to use a local MCP server with Gemini and mcp SDK. Python JavaScript More Make sure the latest version of the mcp SDK is installed on your platform of choice. Note: Python supports automatic tool calling by passing in the ClientSession into the tools parameters. If you want to disable it, you can provide automatic_function_calling with disabled True . Make sure the latest version of the mcp SDK is installed on your platform of choice. Note: JavaScript supports automatic tool calling by wrapping the client with mcpToTool . If you want to disable it, you can provide automaticFunctionCalling with disabled true ."
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 11,
        "cited_text": "Repository files navigation README Apache-2.0 license Gorilla: Large Language Model Connected with Massive APIs Latest Updates 📢 Check out our detailed Berkeley Function Calling Leaderboard changelog (Last updated: ) for the latest dataset / model updates to the Berkeley Function Calling Leaderboard! 🤖 [07/17/2025] Announcing BFCL V4 Agentic! As function-calling forms the bedrock of Agentic systems, BFCL V4 Agentic benchmark focuses on tool-calling in real-world agentic settings, featuring web search with multi-hop reasoning and error recovery, agent memory management, and format sensitivity evaluation. [ Web-search Blog ] [ Memory Blog ] [ Format Sensitivity Blog ] [ PR ] [ Tweet ] 🎯 [10/04/2024] Introducing the Agent Arena by Gorilla X LMSYS Chatbot Arena! Compare different agents in tasks like search, finance, RAG, and beyond. Explore which models and tools work best for specific tasks through our novel ranking system and community-driven prompt hub. [ Blog ] [ Arena ] [ Leaderboard ] [ Dataset ] [ Tweet ] 📣 [09/21/2024] Announcing BFCL V3 - Evaluating multi-turn and multi-step function calling capabilities! New state-based evaluation system tests models on handling complex workflows, sequential functions, and service states. [ Blog ] [ Leaderboard ] [ Code ] [ Tweet ] 🚀 [08/20/2024] Released BFCL V2 • Live! The Berkeley Function-Calling Leaderboard now features enterprise-contributed data and real-world scenarios. [ Blog ] [ Live Leaderboard ] [ V2 Categories Leaderboard ] [ Tweet ] ⚡ [04/12/2024] Excited to release GoEx - a runtime for LLM-generated actions like code, API calls, and more. Featuring \"post-facto validation\" for assessing LLM actions after execution, \"undo\" and \"damage confinement\" abstractions to manage unintended actions & risks. This paves the way for fully autonomous LLM agents, enhancing interaction between apps & services with human-out-of-loop. [ Blog ] [ Code ] [ Paper ] [ Tweet ] ⏰ [04/01/2024] Introducing cost and latency metrics into Berkeley function calling leaderboard ! 🚀 [03/15/2024] RAFT: Adapting Language Model to Domain Specific RAG is live! [ MSFT-Meta blog ] [ Berkeley Blog ] 🏆 [02/26/2024] Berkeley Function Calling Leaderboard is live! 🎯 [02/25/2024] OpenFunctions v2 sets new SoTA for open-source LLMs! 🔥 [11/16/2023] Excited to release Gorilla OpenFunctions 💻 [06/29/2023] Released gorilla-cli , LLMs for your CLI! 🟢 [06/06/2023] Released Commercially usable, Apache 2.0 licensed Gorilla models 🚀 [05/30/2023] Provided the CLI interface to chat with Gorilla! 🚀 [05/28/2023] Released Torch Hub and TensorFlow Hub Models! 🚀 [05/27/2023] Released the first Gorilla model! or 🤗 ! 🔥 [05/27/2023] We released the APIZoo contribution guide for community API contributions! 🔥 [05/25/2023] We release the APIBench dataset and the evaluation code of Gorilla!"
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 12,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "2be6827b-3272-4f52-af8e-e3daa4204826",
        "citation_number": 13,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 14,
        "cited_text": "You can also construct FunctionDeclarations from Python functions directly using types.FunctionDeclaration.from_callable(client=client, callable=your_function) . Function calling with thinking models Gemini 3 and 2.5 series models use an internal \"thinking\" process to reason through requests. This significantly improves function calling performance, allowing the model to better determine when to call a function and which parameters to use. Because the Gemini API is stateless, models use thought signatures to maintain context across multi-turn conversations."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 15,
        "cited_text": "This section covers advanced management of thought signatures and is only necessary if you're manually constructing API requests (e.g., via REST) or manipulating conversation history. If you're using the Google GenAI SDKs (our official libraries), you don't need to manage this process . The SDKs automatically handle the necessary steps, as shown in the earlier example . Managing conversation history manually If you modify the conversation history manually, instead of sending the complete previous response you must correctly handle the thought_signature included in the model's turn."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 16,
        "cited_text": "In Gemini 3, any Part of a model response may contain a thought signature. While we generally recommend returning signatures from all Part types, passing back thought signatures is mandatory for function calling. Unless you are manipulating conversation history manually, the Google GenAI SDK will handle thought signatures automatically. If you are manipulating conversation history manually, refer to the Thoughts Signatures page for complete guidance and details on handling thought signatures for Gemini 3."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 17,
        "cited_text": "Finally, send the result of the function execution back to the model so it can incorporate this information into its final response to the user. Python JavaScript More This completes the function calling flow. The model successfully used the set_light_values function to perform the request action of the user. Function declarations When you implement function calling in a prompt, you create a tools object, which contains one or more function declarations . You define functions using JSON, specifically with a select subset of the OpenAPI schema format. A single function declaration can include the following parameters:"
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 18,
        "cited_text": "name (string): A unique name for the function ( get_weather_forecast , send_email ). Use descriptive names without spaces or special characters (use underscores or camelCase). description (string): A clear and detailed explanation of the function's purpose and capabilities. This is crucial for the model to understand when to use the function. Be specific and provide examples if helpful (\"Finds theaters based on location and optionally movie title which is currently playing in theaters.\"). parameters (object): Defines the input parameters the function expects. type (string): Specifies the overall data type, such as object . properties (object): Lists individual parameters, each with: type (string): The data type of the parameter, such as string , integer , boolean, array . description (string): A description of the parameter's purpose and format. Provide examples and constraints (\"The city and state, e.g., 'San Francisco, CA' or a zip code e.g., '95616'.\"). enum (array, optional): If the parameter values are from a fixed set, use \"enum\" to list the allowed values instead of just describing them in the description. This improves accuracy (\"enum\": [\"daylight\", \"cool\", \"warm\"]). required (array): An array of strings listing the parameter names that are mandatory for the function to operate."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 19,
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
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 20,
        "cited_text": "This notebook covers how to use the Chat Completions API in combination with external functions to extend the capabilities of GPT models. tools is an optional parameter in the Chat Completion API which can be used to provide function specifications. The purpose of this is to enable models to generate function arguments which adhere to the provided specifications. Note that the API will not actually execute any function calls. It is up to developers to execute function calls using model outputs. Within the tools parameter, if the functions parameter is provided then by default the model will decide when it is appropriate to use one of the functions. The API can be forced to use a specific function by setting the tool_choice parameter to {\"type\": \"function\", \"function\": {\"name\": \"my_function\"}} . The API can also be forced to not use any function by setting the tool_choice parameter to \"none\" . If a function is used, the output will contain \"finish_reason\": \"tool_calls\" in the response, as well as a tool_calls object that has the name of the function and the generated function arguments."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 21,
        "cited_text": "Define function declaration: Define the function declaration in your application code. Function Declarations describe the function's name, parameters, and purpose to the model. Call API with function declarations: Send user prompt along with the function declaration(s) to the model. It analyzes the request and determines if a function call would be helpful. If so, it responds with a structured JSON object containing the function name, arguments, and a unique id (this id is now always returned by the API for Gemini 3 models * ). Execute function code (your responsibility): The Model doesn't execute the function itself. It's your application's responsibility to process the response and check for a function call. If Yes : Extract the name, args, and id of the function and execute the corresponding function in your application. No: The model has provided a direct text response to the prompt (this flow is less emphasized in the example but is a possible outcome). Create user friendly response: If a function was executed, capture the result and send it back to the model, ensuring you include the matching id , in a subsequent turn of the conversation. It will use the result to generate a final, user-friendly response that incorporates the information from the function call."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 22,
        "cited_text": "Tool calls - requests from the model to use tools A function call or tool call refers to a special kind of response we can get from the model if it examines a prompt, and then determines that in order to follow the instructions in the prompt, it needs to call one of the tools we made available to it. If the model receives a prompt like “what is the weather in Paris?” in an API request, it could respond to that prompt with a tool call for the get_weather tool, with Paris as the location argument. Tool call outputs - output we generate for the model"
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 23,
        "cited_text": "Steps to invoke a function call using Chat Completions API: Step 1 : Prompt the model with content that may result in model selecting a tool to use. The description of the tools such as a function name and signature is defined in the 'Tools' list and passed to the model in API call. If selected, the function name and parameters are included in the response. Step 2 : Check programmatically if model wanted to call a function. If true, proceed to step 3. Step 3 : Extract the function name and parameters from response, call the function with parameters. Append the result to messages."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 24,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 25,
        "cited_text": "For functions that return images or files, you can pass an array of image or file objects instead of a string. If your function has no return value (e.g. send_email ), simply return a string that indicates success or failure. (e.g. \"success\" ) Incorporating results into response After appending the results to your messages , you can send them back to the model to get a final response. Send results back to model python After appending the results to your input , you can send them back to the model to get a final response."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 26,
        "cited_text": "Step 4 : Invoke the chat completions API with the message list to get the response. Next Steps See our other notebook that demonstrates how to use the Chat Completions API and functions for knowledge retrieval to interact conversationally with a knowledge base."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 27,
        "cited_text": "Win rate. The below example take ChatGPT-ReACT as reference model and GPT4-ReACT as candidate model. Notice that you need to get both model's pass rate results first, then run the following commands to evaluate the preference result of GPT4-ReACT: The result files will be stored under the ${SAVE_PATH}. Please refer to ToolEval for more details. 📊 Model Experiments Results In our main experiments, ToolLLaMA(v2) demonstrates a compelling capability to handle both single-tool and complex multi-tool instructions, which on a par with ChatGPT. Below are the main results. Win rate for each model is compared with ChatGPT-ReACT."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 28,
        "cited_text": "Pass Rate: <cited_table> Win Rate: (Reference model: ChatGPT-ReACT) <cited_table>",
        "cited_table": {
          "num_columns": 9,
          "rows": [
            [
              "Method",
              "Model",
              "I1-Inst.",
              "I1-Tool",
              "I1-Cate.",
              "I2-Inst.",
              "I2-Cate.",
              "I3-Inst.",
              "Average"
            ],
            [
              "ReACT",
              "Claude-2",
              "5.5",
              "3.5",
              "5.5",
              "6",
              "6",
              "14",
              "6.8"
            ],
            [
              "",
              "Text-Davinci-003",
              "12",
              "20",
              "20",
              "8.5",
              "14.5",
              "24",
              "16.5"
            ],
            [
              "",
              "ChatGPT",
              "41.5",
              "44",
              "44.5",
              "42.5",
              "46.5",
              "22",
              "40.2"
            ],
            [
              "",
              "ToolLLaMA",
              "25",
              "29",
              "33",
              "30.5",
              "31.5",
              "25",
              "29"
            ],
            [
              "",
              "GPT4",
              "53.5",
              "50.0",
              "53.5",
              "67.0",
              "72.0",
              "47.0",
              "57.2"
            ],
            [
              "DFSDT",
              "Claude-2",
              "20.5",
              "31",
              "18.5",
              "17",
              "20.5",
              "28",
              "22.6"
            ],
            [
              "",
              "Text-Davinci-003",
              "43.5",
              "44",
              "46",
              "37",
              "42",
              "46",
              "43.1"
            ],
            [
              "",
              "ChatGPT",
              "54.5",
              "65",
              "60.5",
              "75",
              "71.5",
              "62",
              "64.8"
            ],
            [
              "",
              "ToolLLaMA",
              "57",
              "61",
              "62",
              "77",
              "77",
              "66",
              "66.7"
            ],
            [
              "",
              "ToolLLaMA-Retreiver",
              "64",
              "64",
              "60.5",
              "81.5",
              "68.5",
              "65",
              "67.3"
            ],
            [
              "",
              "GPT4",
              "60",
              "71.5",
              "67",
              "79.5",
              "77.5",
              "71",
              "71.1"
            ]
          ]
        }
      },
      {
        "source_id": "c996bde3-6773-40e5-8860-77bf34569653",
        "citation_number": 29,
        "cited_text": "Direct Python library integration in your codebase, Router with retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - Router , application-level load balancing and cost tracking, exception handling with OpenAI-compatible errors, observability callbacks (Lunary, MLflow, Langfuse, etc.) LiteLLM Performance: 8ms P95 latency at 1k RPS (See benchmarks here ) Jump to LiteLLM Proxy (LLM Gateway) Docs Jump to Supported LLM Providers Stable Release: Use docker images with the -stable tag. These have undergone 12 hour load tests, before being published. More information about the release cycle here"
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 30,
        "cited_text": "<cited_table> We crawl 16000+ real-world APIs from RapidAPI , and curate realistic human instructions that involve them. Below we present a hierarchy of RapidAPI and our instruction generation process. ToolBench contains both single-tool and multi-tool scenarios. The multi-tool scenarios can be further categorized into intra-category multi-tool and intra-collection multi-tool. We utilize DFSDT method for all scenarios to our data creation. Here is an illustration for the data creation process using DFSDT method:",
        "cited_table": {
          "num_columns": 5,
          "rows": [
            [
              "Tool Nums",
              "API Nums",
              "Instance Nums",
              "Real API Call",
              "Reasoning Traces"
            ],
            [
              "3451",
              "16464",
              "126486",
              "469585",
              "4.0"
            ]
          ]
        }
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 31,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 32,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「Function Calling（函数调用）」是实现大语言模型（LLM）从“对话框”走向“操作系统”的核心技术。以下是基于源文件的深度解析，涵盖实现细节、架构、优化策略及竞品对比。\n\n### 一、 核心算法流程\nFunction Calling 的本质是一个**多阶段的结构化交互循环**，主要包含以下算法逻辑：\n\n1.  **定义与意图识别（JSON Schema-based Selection）**：\n    *   开发者通过 **JSON Schema**（OpenAPI 子集）定义函数名称、描述和参数约束 [1, 2]。\n    *   模型分析用户提示词，判断是否需要调用工具。如果需要，模型不再生成自然语言，而是生成符合 Schema 的结构化 JSON 对象，包含函数名和提取的参数 [3-5]。\n2.  **DFSDT（基于深度优先搜索的决策树）算法**：\n    *   **ToolLLM** 框架引入的核心算法。相比传统的 ReAct 或 CoT，**DFSDT** 允许模型评估多个推理轨迹并扩大搜索空间 [6, 7]。\n    *   这显著提升了处理复杂、多步骤指令的能力，特别是在单次尝试失败时能进行**错误恢复和路径回溯** [6, 7]。\n3.  **RAFT（检索增强微调）算法**：\n    *   由 **Gorilla** 提出，通过在微调过程中加入包含“oracle（正确文档）”和“distractor（干扰文档）”的数据集，训练模型不仅能记住 API 用法，还能根据实时检索到的文档调整调用逻辑，大幅减少幻觉 [8, 9]。\n4.  **思维特征（Thought Signatures）维护**：\n    *   在 **Gemini 3** 等模型中，由于 API 是无状态的，系统通过 `thought_signature` 在多轮对话中传递模型的内部推理过程，确保复杂任务在多次调用间的一致性 [10-12]。\n\n### 二、 关键代码架构\n目前主流的实现架构分为**应用侧执行**与**原生协议化**两类：\n\n*   **客户端执行模式（Client-side Tools）**：\n    *   模型返回 `stop_reason: \"tool_use\"` 或 `finish_reason: \"tool_calls\"` [13, 14]。\n    *   应用程序提取 `call_id`、函数名及参数，在本地环境执行代码（如 SQL 查询、发邮件），并将结果回传给模型 [4, 15]。\n*   **服务器端执行模式（Server-side Tools）**：\n    *   Anthropic 等厂商提供的模式，如 `web_search`、`code_execution` 直接在厂商基础设施上运行，开发者直接获取结果，无需处理执行环境 [14, 16]。\n*   **标准化架构：MCP（Model Context Protocol）**：\n    *   一种开放标准，旨在统一 AI 应用与外部工具（如本地 Shell、数据库）的连接协议，减少重复代码量 [17, 18]。\n*   **自动化 SDK 封装**：\n    *   Python SDK（如 Gemini 和 OpenAI）支持通过 **Pydantic** 或 **Python type hints** 自动生成函数声明，并处理执行循环 [19-21]。\n\n### 三、 性能优化策略\n1.  **并行与组合调用（Parallel & Compositional Calling）**：\n    *   **并行调用**：在单轮中同时发起多个互不依赖的请求（如同时查询三个城市的温度），提高任务效率 [22-24]。\n    *   **组合调用**：模型自动将一个函数的输出作为另一个函数的输入（如 `get_location` -> `get_weather`），形成调用链 [25, 26]。\n2.  **严格模式（Strict Mode）**：\n    *   通过将 `strict` 参数设为 `true`，利用结构化输出技术强制模型生成的 JSON 完全符合 Schema，减少解析错误 [27, 28]。\n3.  **提示词缓存（Prompt Caching）**：\n    *   由于函数定义通常较长且重复，Claude 和 OpenAI 支持对 `tools` 参数进行缓存，从而**显著降低延迟并减少输入 token 的成本** [29-31]。\n4.  **低延迟网关优化**：\n    *   使用如 **LiteLLM** 等代理服务器，在 1k RPS（每秒请求数）压力下，P95 延迟可优化至约 **8ms** [32]。\n\n### 四、 竞品技术对比与参数\n下表综合了来源中的关键技术指标：\n\n| 维度 | Gemini 3 系列 | OpenAI GPT-5.4/o4-mini | Claude 4.6 (Anthropic) | ToolLLaMA (OpenBMB) |\n| :--- | :--- | :--- | :--- | :--- |\n| **核心算法/机制** | 思维特征 (Thought Signatures) [10] | 结构化输出/Strict Mode [27] | 代理循环 (Agentic Loop) [14] | DFSDT (决策树搜索) [7] |\n| **工具搜索能力** | 内置 Multi-tool use [33] | `tool_search` 延迟加载 [34, 35] | 系统自动选择 [16] | 神经 API 检索器 [6] |\n| **API 覆盖规模** | 支持 16,000+ APIs (ToolBench 体系) [6] | 广泛的插件与内置工具 [18] | 侧重企业级工具链 [36] | 涵盖 16,464 个真实 API [6, 37] |\n| **Token 消耗** | 自动处理不计额外系统开销 [11] | 计入 Context Limit [38] | 系统提示词消耗约 313-346 tokens [39] | 与 SFT 模型一致 |\n| **主要优势** | 推理一致性强，支持多模态响应 [40] | 严格的 Schema 遵循，支持 CFG 语法约束 [27, 41] | 区分客户端/服务器工具，安全性高 [14] | 在复杂多步任务中胜过 ChatGPT (Win Rate) [42] |\n\n### 五、 具体技术参数与数据\n*   **评估指标（ToolEval）**：在对 ChatGPT+DFSDT 和 ToolLLaMA+DFSDT 的测试中，模型评估结果与人类评价的一致性在**通过率（Pass Rate）上达到 87.1%**，在**胜率（Win Rate）上达到 80.3%** [43]。\n*   **数据规模**：**ToolBench** 数据集包含 **126,486 个实例**，涉及来自 RapidAPI 的 **16,464 个 API** [37]。\n*   **成本/延迟参数**：\n    *   **Claude Opus 4.6** 开启自动工具选择时，系统提示词消耗为 **346 tokens** [39]。\n    *   **LiteLLM** 网关性能：**8ms P95 延迟** [32]。\n*   **推荐配置**：为了获得最稳定的调用结果，官方通常建议将 **Temperature 设为 0**（Gemini 3 除外，其建议保持 1.0 以维持推理性能） [44]。对于工具集规模，建议初次调用的活跃工具数保持在 **20 个以内**，更多工具应使用工具检索机制 [21, 44]。",
    "conversation_id": "6644b4c8-4688-4d87-b7ac-5f06f7119a94",
    "sources_used": [
      "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "7c52ee01-0056-43bb-9fc9-a17792878206",
      "2be6827b-3272-4f52-af8e-e3daa4204826",
      "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "c996bde3-6773-40e5-8860-77bf34569653"
    ],
    "citations": {
      "1": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "2": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "3": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "4": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "5": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "6": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "7": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "8": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "9": "2be6827b-3272-4f52-af8e-e3daa4204826",
      "10": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "11": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "12": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "13": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "14": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "15": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "16": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "17": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "18": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "19": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "20": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "21": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "22": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "23": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "24": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "25": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "26": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "27": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "28": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "29": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "30": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "31": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "32": "c996bde3-6773-40e5-8860-77bf34569653",
      "33": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "34": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "35": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "36": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "37": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "38": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "39": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "40": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "41": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "42": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "43": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "44": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd"
    },
    "references": [
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 1,
        "cited_text": "Finally, send the result of the function execution back to the model so it can incorporate this information into its final response to the user. Python JavaScript More This completes the function calling flow. The model successfully used the set_light_values function to perform the request action of the user. Function declarations When you implement function calling in a prompt, you create a tools object, which contains one or more function declarations . You define functions using JSON, specifically with a select subset of the OpenAPI schema format. A single function declaration can include the following parameters:"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 2,
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
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 3,
        "cited_text": "Function calling lets you connect models to external tools and APIs. Instead of generating text responses, the model determines when to call specific functions and provides the necessary parameters to execute real-world actions. This allows the model to act as a bridge between natural language and real-world actions and data. Function calling has 3 primary use cases: Augment Knowledge: Access information from external sources like databases, APIs, and knowledge bases. Extend Capabilities: Use external tools to perform computations and extend the limitations of the model, such as using a calculator or creating charts. Take Actions: Interact with external systems using APIs, such as scheduling appointments, creating invoices, sending emails, or controlling smart home devices."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 4,
        "cited_text": "Define function declaration: Define the function declaration in your application code. Function Declarations describe the function's name, parameters, and purpose to the model. Call API with function declarations: Send user prompt along with the function declaration(s) to the model. It analyzes the request and determines if a function call would be helpful. If so, it responds with a structured JSON object containing the function name, arguments, and a unique id (this id is now always returned by the API for Gemini 3 models * ). Execute function code (your responsibility): The Model doesn't execute the function itself. It's your application's responsibility to process the response and check for a function call. If Yes : Extract the name, args, and id of the function and execute the corresponding function in your application. No: The model has provided a direct text response to the prompt (this flow is less emphasized in the example but is a possible outcome). Create user friendly response: If a function was executed, capture the result and send it back to the model, ensuring you include the matching id , in a subsequent turn of the conversation. It will use the result to generate a final, user-friendly response that incorporates the information from the function call."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 5,
        "cited_text": "Tool calls - requests from the model to use tools A function call or tool call refers to a special kind of response we can get from the model if it examines a prompt, and then determines that in order to follow the instructions in the prompt, it needs to call one of the tools we made available to it. If the model receives a prompt like “what is the weather in Paris?” in an API request, it could respond to that prompt with a tool call for the get_weather tool, with Paris as the location argument. Tool call outputs - output we generate for the model"
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 6,
        "cited_text": "✨Here is an overview of the dataset construction, training, and evaluation. ✨✨Features: API Collection : we gather 16464 representational state transfer (REST) APIs from RapidAPI , a platform that hosts massive real-world APIs provided by developers. Instruction Generation : we curate instructions that involve both single-tool and multi-tool scenarios. Answer Annotation : we develop a novel depth-first search based decision tree (DFSDT) to bolster the planning and reasoning ability of LLMs, which significantly improves the annotation efficiency and successfully annotates those complex instructions that cannot be answered with CoT or ReACT. We provide responses that not only include the final answer but also incorporate the model's reasoning process, tool execution, and tool execution results . API Retriver : we incorporate API retrieval to equip ToolLLaMA with open-domain tool-using abilities. All the data is automatically generated by OpenAI API and filtered by us, the whole data creation process is easy to scale up."
      },
      {
        "source_id": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
        "citation_number": 7,
        "cited_text": "View PDF Abstract: Despite the advancements of open-source large language models (LLMs), e.g., LLaMA, they remain significantly limited in tool-use capabilities, i.e., using external tools (APIs) to fulfill human instructions. The reason is that current instruction tuning largely focuses on basic language tasks but ignores the tool-use domain. This is in contrast to the excellent tool-use capabilities of state-of-the-art (SOTA) closed-source LLMs, e.g., ChatGPT. To bridge this gap, we introduce ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation. We first present ToolBench, an instruction-tuning dataset for tool use, which is constructed automatically using ChatGPT. Specifically, the construction can be divided into three stages: (i) API collection: we collect 16,464 real-world RESTful APIs spanning 49 categories from RapidAPI Hub; (ii) instruction generation: we prompt ChatGPT to generate diverse instructions involving these APIs, covering both single-tool and multi-tool scenarios; (iii) solution path annotation: we use ChatGPT to search for a valid solution path (chain of API calls) for each instruction. To enhance the reasoning capabilities of LLMs, we develop a novel depth-first search-based decision tree algorithm. It enables LLMs to evaluate multiple reasoning traces and expand the search space. Moreover, to evaluate the tool-use capabilities of LLMs, we develop an automatic evaluator: ToolEval. Based on ToolBench, we fine-tune LLaMA to obtain an LLM ToolLLaMA, and equip it with a neural API retriever to recommend appropriate APIs for each instruction. Experiments show that ToolLLaMA demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, and exhibits comparable performance to ChatGPT. Our ToolLLaMA also demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench."
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 8,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "2be6827b-3272-4f52-af8e-e3daa4204826",
        "citation_number": 9,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 10,
        "cited_text": "You can also construct FunctionDeclarations from Python functions directly using types.FunctionDeclaration.from_callable(client=client, callable=your_function) . Function calling with thinking models Gemini 3 and 2.5 series models use an internal \"thinking\" process to reason through requests. This significantly improves function calling performance, allowing the model to better determine when to call a function and which parameters to use. Because the Gemini API is stateless, models use thought signatures to maintain context across multi-turn conversations."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 11,
        "cited_text": "This section covers advanced management of thought signatures and is only necessary if you're manually constructing API requests (e.g., via REST) or manipulating conversation history. If you're using the Google GenAI SDKs (our official libraries), you don't need to manage this process . The SDKs automatically handle the necessary steps, as shown in the earlier example . Managing conversation history manually If you modify the conversation history manually, instead of sending the complete previous response you must correctly handle the thought_signature included in the model's turn."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 12,
        "cited_text": "In Gemini 3, any Part of a model response may contain a thought signature. While we generally recommend returning signatures from all Part types, passing back thought signatures is mandatory for function calling. Unless you are manipulating conversation history manually, the Google GenAI SDK will handle thought signatures automatically. If you are manipulating conversation history manually, refer to the Thoughts Signatures page for complete guidance and details on handling thought signatures for Gemini 3."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 13,
        "cited_text": "This notebook covers how to use the Chat Completions API in combination with external functions to extend the capabilities of GPT models. tools is an optional parameter in the Chat Completion API which can be used to provide function specifications. The purpose of this is to enable models to generate function arguments which adhere to the provided specifications. Note that the API will not actually execute any function calls. It is up to developers to execute function calls using model outputs. Within the tools parameter, if the functions parameter is provided then by default the model will decide when it is appropriate to use one of the functions. The API can be forced to use a specific function by setting the tool_choice parameter to {\"type\": \"function\", \"function\": {\"name\": \"my_function\"}} . The API can also be forced to not use any function by setting the tool_choice parameter to \"none\" . If a function is used, the output will contain \"finish_reason\": \"tool_calls\" in the response, as well as a tool_calls object that has the name of the function and the generated function arguments."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 14,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 15,
        "cited_text": "Steps to invoke a function call using Chat Completions API: Step 1 : Prompt the model with content that may result in model selecting a tool to use. The description of the tools such as a function name and signature is defined in the 'Tools' list and passed to the model in API call. If selected, the function name and parameters are included in the response. Step 2 : Check programmatically if model wanted to call a function. If true, proceed to step 3. Step 3 : Extract the function name and parameters from response, call the function with parameters. Append the result to messages."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 16,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 17,
        "cited_text": "Model context protocol (MCP) Model Context Protocol (MCP) is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts. The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 18,
        "cited_text": "We then send all of the tool definition, the original prompt, the model's tool call, and the tool call output back to the model to finally receive a text response like: Functions versus tools A function is a specific kind of tool, defined by a JSON schema. A function definition allows the model to pass data to your application, where your code can access data or take actions suggested by the model. In addition to function tools, there are custom tools (described in this guide) that work with free text inputs and outputs. There are also built-in tools that are part of the OpenAI platform. These tools enable the model to search the web , execute code , access the functionality of an MCP server , and more."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 19,
        "cited_text": "Python JavaScript More Each of the printed results reflects a single function call that the model has requested. To send the results back, include the responses in the same order as they were requested. The Python SDK supports automatic function calling , which automatically converts Python functions to declarations, handles the function call execution and response cycle for you. Following is an example for the disco use case. Note: Automatic Function Calling is a Python SDK only feature at the moment."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 20,
        "cited_text": "Python JavaScript More Automatic function calling (Python only) When using the Python SDK, you can provide Python functions directly as tools. The SDK converts these functions into declarations, manages the function call execution, and handles the response cycle for you. Define your function with type hints and a docstring. For optimal results, it is recommended to use Google-style docstrings. The SDK will then automatically: Detect function call responses from the model. Call the corresponding Python function in your code. Send the function's response back to the model. Return the model's final text response."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 21,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 22,
        "cited_text": "Inspecting thought signatures While not necessary for implementation, you can inspect the response to see the thought_signature for debugging or educational purposes. Python JavaScript More Learn more about limitations and usage of thought signatures, and about thinking models in general, on the Thinking page. Parallel function calling In addition to single turn function calling, you can also call multiple functions at once. Parallel function calling lets you execute multiple functions at once and is used when the functions are not dependent on each other. This is useful in scenarios like gathering data from multiple independent sources, such as retrieving customer details from different databases or checking inventory levels across various warehouses or performing multiple actions such as converting your apartment into a disco."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 23,
        "cited_text": "Parallel function calling Parallel function calling is not possible when using built-in tools . The model may choose to call multiple functions in a single turn. You can prevent this by setting parallel_tool_calls to false , which ensures exactly zero or one tool is called. Note: Currently, if you are using a fine tuned model and the model calls multiple functions in one turn then strict mode will be disabled for those calls. Note for gpt-4.1-nano-2025-04-14 : This snapshot of gpt-4.1-nano can sometimes include multiple tools calls for the same tool if parallel tool calls are enabled. It is recommended to disable this feature when using this nano snapshot."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 24,
        "cited_text": "Parallel Function Calling Newer models such as gpt-5, gpt-4.1 or gpt-4o can call multiple functions in one turn. How to call functions with model generated arguments In our next example, we'll demonstrate how to execute functions whose inputs are model-generated, and use this to implement an agent that can answer questions for us about a database. For simplicity we'll use the Chinook sample database . Note: SQL generation can be high-risk in a production environment since models are not perfectly reliable at generating correct SQL."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 25,
        "cited_text": "Python More Compositional function calling Compositional or sequential function calling allows Gemini to chain multiple function calls together to fulfill a complex request. For example, to answer \"Get the temperature in my current location\", the Gemini API might first invoke a get_current_location() function followed by a get_weather() function that takes the location as a parameter. The following example demonstrates how to implement compositional function calling using the Python SDK and automatic function calling."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 26,
        "cited_text": "This example shows how to use JavaScript/TypeScript SDK to do comopositional function calling using a manual execution loop. Expected Output When you run the code, you will see the SDK orchestrating the function calls. The model first calls get_weather_forecast , receives the temperature, and then calls set_thermostat_temperature with the correct value based on the logic in the prompt. Compositional function calling is a native Live API feature. This means Live API can handle the function calling similar to the Python SDK."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 27,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 28,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 29,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 30,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 31,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "c996bde3-6773-40e5-8860-77bf34569653",
        "citation_number": 32,
        "cited_text": "Direct Python library integration in your codebase, Router with retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - Router , application-level load balancing and cost tracking, exception handling with OpenAI-compatible errors, observability callbacks (Lunary, MLflow, Langfuse, etc.) LiteLLM Performance: 8ms P95 latency at 1k RPS (See benchmarks here ) Jump to LiteLLM Proxy (LLM Gateway) Docs Jump to Supported LLM Providers Stable Release: Use docker images with the -stable tag. These have undergone 12 hour load tests, before being published. More information about the release cycle here"
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 33,
        "cited_text": "Python More To see what the inferred schema looks like, you can convert it using from_callable : Python More Multi-tool use: Combine built-in tools with function calling You can enable multiple tools, combining built-in tools with function calling in the same request. Gemini 3 models can combine built-in tools with function calling out-of-the-box, thanks to the tool context circulation feature. Read the page on Combining built-in tools and function calling to learn more. Preview: Combining built-in tools with function calling and tool context circulation features are in Preview in Gemini 3 models."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 34,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 35,
        "cited_text": "When to use allowed_tools You might want to configure an allowed_tools list in case you want to make only a subset of tools available across model requests, but not modify the list of tools you pass in, so you can maximize savings from prompt caching . You can also set tool_choice to \"none\" to imitate the behavior of passing no functions. When you use tool search, tool_choice still applies to the tools that are currently callable in the turn. This is most useful after you load a subset of tools and want to constrain the model to that subset."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 36,
        "cited_text": "Files & assets Files API Agent Skills Overview Quickstart Best practices Skills for enterprise Claude API skill Using Skills with the API Agent SDK Overview Quickstart How the agent loop works Core concepts Guides SDK references MCP in the API MCP connector Remote MCP servers Claude on 3rd-party platforms Amazon Bedrock Microsoft Foundry Vertex AI Prompt engineering Overview Console prompting tools Test & evaluate Define success and build evaluations Using the Evaluation Tool Reducing latency Strengthen guardrails"
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 37,
        "cited_text": "<cited_table> We crawl 16000+ real-world APIs from RapidAPI , and curate realistic human instructions that involve them. Below we present a hierarchy of RapidAPI and our instruction generation process. ToolBench contains both single-tool and multi-tool scenarios. The multi-tool scenarios can be further categorized into intra-category multi-tool and intra-collection multi-tool. We utilize DFSDT method for all scenarios to our data creation. Here is an illustration for the data creation process using DFSDT method:",
        "cited_table": {
          "num_columns": 5,
          "rows": [
            [
              "Tool Nums",
              "API Nums",
              "Instance Nums",
              "Real API Call",
              "Reasoning Traces"
            ],
            [
              "3451",
              "16464",
              "126486",
              "469585",
              "4.0"
            ]
          ]
        }
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 38,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 39,
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
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 40,
        "cited_text": "Python Javascript More For models before the Gemini 3 series, use the Live API . Multimodal function responses Note: This feature is available for Gemini 3 series models. For Gemini 3 series models, you can include multimodal content in the function response parts that you send to the model. The model can process this multimodal content in its next turn to produce a more informed response. The following MIME types are supported for multimodal content in function responses: Images : image/png , image/jpeg , image/webp Documents : application/pdf , text/plain"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 41,
        "cited_text": "Custom tool calling example python Just as before, the output array will contain a tool call generated by the model. Except this time, the tool call input is given as plain text. Context-free grammars A context-free grammar (CFG) is a set of rules that define how to produce valid text in a given format. For custom tools, you can provide a CFG that will constrain the model's text input for a custom tool. You can provide a custom CFG using the grammar parameter when configuring a custom tool. Currently, we support two CFG syntaxes when defining grammars: lark and regex ."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 42,
        "cited_text": "Pass Rate: <cited_table> Win Rate: (Reference model: ChatGPT-ReACT) <cited_table>",
        "cited_table": {
          "num_columns": 9,
          "rows": [
            [
              "Method",
              "Model",
              "I1-Inst.",
              "I1-Tool",
              "I1-Cate.",
              "I2-Inst.",
              "I2-Cate.",
              "I3-Inst.",
              "Average"
            ],
            [
              "ReACT",
              "Claude-2",
              "5.5",
              "3.5",
              "5.5",
              "6",
              "6",
              "14",
              "6.8"
            ],
            [
              "",
              "Text-Davinci-003",
              "12",
              "20",
              "20",
              "8.5",
              "14.5",
              "24",
              "16.5"
            ],
            [
              "",
              "ChatGPT",
              "41.5",
              "44",
              "44.5",
              "42.5",
              "46.5",
              "22",
              "40.2"
            ],
            [
              "",
              "ToolLLaMA",
              "25",
              "29",
              "33",
              "30.5",
              "31.5",
              "25",
              "29"
            ],
            [
              "",
              "GPT4",
              "53.5",
              "50.0",
              "53.5",
              "67.0",
              "72.0",
              "47.0",
              "57.2"
            ],
            [
              "DFSDT",
              "Claude-2",
              "20.5",
              "31",
              "18.5",
              "17",
              "20.5",
              "28",
              "22.6"
            ],
            [
              "",
              "Text-Davinci-003",
              "43.5",
              "44",
              "46",
              "37",
              "42",
              "46",
              "43.1"
            ],
            [
              "",
              "ChatGPT",
              "54.5",
              "65",
              "60.5",
              "75",
              "71.5",
              "62",
              "64.8"
            ],
            [
              "",
              "ToolLLaMA",
              "57",
              "61",
              "62",
              "77",
              "77",
              "66",
              "66.7"
            ],
            [
              "",
              "ToolLLaMA-Retreiver",
              "64",
              "64",
              "60.5",
              "81.5",
              "68.5",
              "65",
              "67.3"
            ],
            [
              "",
              "GPT4",
              "60",
              "71.5",
              "67",
              "79.5",
              "77.5",
              "71",
              "71.1"
            ]
          ]
        }
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 43,
        "cited_text": "To validate the reliability of ChatGPT evaluator in both pass rate and win rate, we sample among four different methods (ChatGPT+ReACT, ChatGPT+DFSDT, ToolLLaMA+DFSDT and GPT4+DFSDT) to obtain solution pairs for 300 test instructions for each method. Then we engage humans to annotate the pass rate for ChatGPT+DFSDT, ToolLLaMA+DFSDT and GPT4+DFSDT, and the win rate among ChatGPT+ReACT and ChatGPT+DFSDT. Our ChatGPT evaluator demonstrates a high agreement of 87.1% in pass rate and 80.3% in win rate with human annotators. This result shows that our evaluator generates highly similar evaluation results to humans and can be viewed as a credible evaluator who simulates human evaluation on pass rate and win rate."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 44,
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
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「Function Calling（函数调用）」作为连接大语言模型（LLM）与现实世界的桥梁，其应用已从简单的信息查询演进为复杂的代理任务。以下根据来源资料，对其真实应用场景、工业方案、基准数据及实践经验进行深度解析：\n\n### 一、 真实应用场景与案例\n函数调用主要有三大类核心用途 [1]：\n*   **知识增强（Augment Knowledge）**：访问数据库、API 或知识库中的外部实时信息 [1]。例如，查询当前天气预报 [2, 3]、获取特定用户 ID 的账户详细信息 [2] 或通过 SQL 查询分析 Chinook 示例数据库 [4, 5]。\n*   **能力扩展（Extend Capabilities）**：利用外部工具进行模型无法胜任的计算或可视化 [1]。例如，使用计算器进行精确数学运算或调用工具生成图表 [1, 6]。\n*   **执行动作（Take Actions）**：通过 API 与外部系统交互 [1]。典型案例包括：\n    *   **商业流程**：自动处理退款（针对丢失订单）[2, 7]、创建发票、发送电子邮件 [1, 8]。\n    *   **日程与控制**：预约会议 [6]、控制智能家居设备（如调节灯光亮度或空调温度）[9, 10]。\n    *   **开发辅助**：**Gorilla CLI** 通过自然语言生成并执行 1500+ 种命令行操作（如 AWS、GCP 命令）[11, 12]。\n\n### 二、 工业级部署方案\n*   **网关架构（LiteLLM Proxy Server）**：提供统一的 AI 网关，支持 100 多个 LLM API。其工业特性包括：**多租户成本跟踪**、基于项目的 spend 管理、虚拟密钥访问控制、身份验证（SSO）及 P95 延迟仅 **8ms** 的高性能路由 [13-15]。\n*   **执行模式选择**：\n    *   **客户端执行（Client Tools）**：模型返回调用指令，由开发者应用在本地执行，适用于私有数据处理 [16]。\n    *   **服务器端执行（Server Tools）**：Anthropic 等平台直接在其基础设施上执行工具（如 `web_search`、`code_execution`）并返回结果，降低了应用侧的维护负担 [16]。\n*   **标准化协议（MCP）**：**Model Context Protocol** 是一种开放标准，旨在统一 AI 应用与数据源、工具之间的连接，减少集成不同工具时的重复代码 [17, 18]。\n\n### 三、 开源项目实战案例\n*   **ToolLLM / ToolBench**：一个大规模开源平台，通过 **DFSDT（基于深度优先搜索的决策树）** 算法增强模型的推理规划能力，涵盖来自 RapidAPI 的 **16,464 个真实 API** [19-21]。其训练出的 **ToolLLaMA** 在处理复杂指令方面表现出色 [20, 22]。\n*   **Gorilla**：通过 **RAFT（检索增强微调）** 技术，使模型能准确调用 1,600+ API，显著减少了 API 参数生成中的幻觉问题 [11, 23, 24]。\n*   **LangChain / LangGraph**：用于构建复杂代理流程的框架，通过低层级的编排支持构建具有长期规划和子代理协作能力的深层代理 [25, 26]。\n\n### 四、 性能基准数据\n*   **评估指标**：**ToolEval** 引入了**通过率（Pass Rate）**和**胜率（Win Rate）** [27]。在实验中，ChatGPT 评估器与人类标注者在通过率上的达成度为 **87.1%**，胜率达成度为 **80.3%** [28]。\n*   **模型表现**：**GPT-4** 在 DFSDT 模式下平均通过率达到 **71.1%**，而经过微调的 **ToolLLaMA-Retriever** 达到 **67.3%**，在部分任务中表现与顶级闭源模型相当 [29]。\n*   **数据规模**：**APIBench** 数据集包含了来自 HuggingFace、TorchHub 和 TensorHub 的大量 API 指令，用于验证模型在快速更新文档中的适应能力 [24]。\n\n### 五、 开发者最佳实践与常见踩坑经验\n#### 1. 最佳实践\n*   **精准描述**：函数名和参数描述必须清晰准确。模型完全依赖这些描述来决定何时调用及如何填充参数 [7, 30]。\n*   **强类型约束**：优先使用 **Enum（枚举）** 和特定的数据类型（如 integer、boolean）而非 open-ended 字符串，以消除无效状态 [7, 30]。\n*   **启用严格模式（Strict Mode）**：建议始终开启 `strict: true`，利用结构化输出技术强制模型生成的 JSON 完全符合 Schema 约束 [31, 32]。\n*   **控制工具规模**：单次对话中活跃工具数建议维持在 **10-20 个以内**。若工具集庞大，应配合 **Tool Search（工具检索）** 动态加载 [7, 30]。\n*   **温度设置**：常规模型建议将 Temperature 设为 **0** 以保证确定性；但 **Gemini 3** 强烈建议保持默认的 **1.0**，否则可能导致逻辑死循环或性能下降 [30]。\n\n#### 2. 常见踩坑经验（坑点）\n*   **Token 限制**：所有函数定义都会计入 Input Token 成本并占用上下文窗口。过长的描述会导致成本上升并限制有效历史记录长度 [30, 33]。\n*   **参数“脑补”**：不要让模型填充应用侧已知的参数（如 order_id），应直接在后台通过代码注入，以减少模型出错机率 [7]。\n*   **解析位置假设**：不要假设 `functionCall` 总是在响应部分的最后位。在并行调用或多模态响应中，必须遍历 parts 数组而非依赖固定位置索引 [34]。\n*   **Intern Test（实习生测试）**：如果一个人类实习生只看你的函数定义无法正确执行任务，模型也大概率会出错；此时应补充系统提示词或优化描述 [7]。\n*   **结果整合幻觉**：模型可能会忽略工具返回的错误信息而编造结果。建议在重要操作（如支付）前通过对话确认 [30]。",
    "conversation_id": "6644b4c8-4688-4d87-b7ac-5f06f7119a94",
    "sources_used": [
      "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "7c52ee01-0056-43bb-9fc9-a17792878206",
      "c996bde3-6773-40e5-8860-77bf34569653",
      "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "2be6827b-3272-4f52-af8e-e3daa4204826",
      "cb9e9864-d0db-416a-9b2b-79a804a1c933"
    ],
    "citations": {
      "1": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "2": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "3": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "4": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "5": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "6": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "7": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "8": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "9": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "10": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "11": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "12": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "13": "c996bde3-6773-40e5-8860-77bf34569653",
      "14": "c996bde3-6773-40e5-8860-77bf34569653",
      "15": "c996bde3-6773-40e5-8860-77bf34569653",
      "16": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "17": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "18": "c996bde3-6773-40e5-8860-77bf34569653",
      "19": "c996bde3-6773-40e5-8860-77bf34569653",
      "20": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "21": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "22": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "23": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "24": "2be6827b-3272-4f52-af8e-e3daa4204826",
      "25": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "26": "cb9e9864-d0db-416a-9b2b-79a804a1c933",
      "27": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "28": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "29": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "30": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "31": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "32": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "33": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "34": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd"
    },
    "references": [
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 1,
        "cited_text": "Function calling lets you connect models to external tools and APIs. Instead of generating text responses, the model determines when to call specific functions and provides the necessary parameters to execute real-world actions. This allows the model to act as a bridge between natural language and real-world actions and data. Function calling has 3 primary use cases: Augment Knowledge: Access information from external sources like databases, APIs, and knowledge bases. Extend Capabilities: Use external tools to perform computations and extend the limitations of the model, such as using a calculator or creating charts. Take Actions: Interact with external systems using APIs, such as scheduling appointments, creating invoices, sending emails, or controlling smart home devices."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 2,
        "cited_text": "You could give the model access to tools that: Get today's weather for a location Access account details for a given user ID Issue refunds for a lost order Or anything else you'd like the model to be able to know or do as it responds to a prompt. When we make an API request to the model with a prompt, we can include a list of tools the model could consider using. For example, if we wanted the model to be able to answer questions about the current weather somewhere in the world, we might give it access to a get_weather tool that takes location as an argument."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 3,
        "cited_text": "Let's create some function specifications to interface with a hypothetical weather API. We'll pass these function specification to the Chat Completions API in order to generate function arguments that adhere to the specification. If we prompt the model about the current weather, it will respond with some clarifying questions. Once we provide the missing information, it will generate the appropriate function arguments for us. By prompting it differently, we can get it to target the other function we've told it about."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 4,
        "cited_text": "Parallel Function Calling Newer models such as gpt-5, gpt-4.1 or gpt-4o can call multiple functions in one turn. How to call functions with model generated arguments In our next example, we'll demonstrate how to execute functions whose inputs are model-generated, and use this to implement an agent that can answer questions for us about a database. For simplicity we'll use the Chinook sample database . Note: SQL generation can be high-risk in a production environment since models are not perfectly reliable at generating correct SQL."
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 5,
        "cited_text": "Specifying a function to execute SQL queries First let's define some helpful utility functions to extract data from a SQLite database. Now we can use these utility functions to extract a representation of the database schema. As before, we'll define a function specification for the function we'd like the API to generate arguments for. Notice that we are inserting the database schema into the function specification. This will be important for the model to know about. Executing SQL queries Now let's implement the function that will actually excute queries against the database."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 6,
        "cited_text": "Important: Gemini 3 model APIs now generate a unique id for every function call. If you are manually constructing the conversation history or using the REST API, when returning the result of your executed function to the model we recommend passing the matching id in your functionResponse . If you are using the standard Python or Node.js SDKs, this is handled automatically. Get Weather Schedule Meeting Create Chart Python JavaScript REST More How function calling works Function calling involves a structured interaction between your application, the model, and external functions. Here's a breakdown of the process:"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 7,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 8,
        "cited_text": "For functions that return images or files, you can pass an array of image or file objects instead of a string. If your function has no return value (e.g. send_email ), simply return a string that indicates success or failure. (e.g. \"success\" ) Incorporating results into response After appending the results to your messages , you can send them back to the model to get a final response. Send results back to model python After appending the results to your input , you can send them back to the model to get a final response."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 9,
        "cited_text": "Step 1: Define a function declaration Define a function and its declaration within your application code that allows users to set light values and make an API request. This function could call external services or APIs. Python JavaScript More Step 2: Call the model with function declarations Once you have defined your function declarations, you can prompt the model to use them. It analyzes the prompt and function declarations and decides whether to respond directly or to call a function. If a function is called, the response object will contain a function call suggestion."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 10,
        "cited_text": "Python JavaScript More This example uses the automatic function calling feature of the google-genai Python SDK. The SDK automatically converts the Python functions to the required schema, executes the function calls when requested by the model, and sends the results back to the model to complete the task. Expected Output When you run the code, you will see the SDK orchestrating the function calls. The model first calls get_weather_forecast , receives the temperature, and then calls set_thermostat_temperature with the correct value based on the logic in the prompt."
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 11,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 12,
        "cited_text": "• Natural language command generation with multi-LLM fusion • Privacy-focused with explicit execution approval • Command history and interactive selection interface Gorilla API Zoo 📚 Dataset A community-maintained repository of up-to-date API documentation • Centralized, searchable index of APIs across domains • Structured documentation format with arguments, versioning, and examples • Community-driven updates to keep pace with API changes • Rich data source for model training and fine-tuning • Enables retrieval-augmented training and inference"
      },
      {
        "source_id": "c996bde3-6773-40e5-8860-77bf34569653",
        "citation_number": 13,
        "cited_text": "Repository files navigation README Contributing License Security 🚅 LiteLLM Call 100+ LLMs in OpenAI format. [Bedrock, Azure, OpenAI, VertexAI, Anthropic, Groq, etc.] LiteLLM Proxy Server (AI Gateway) | Hosted Proxy | Enterprise Tier Use LiteLLM for LLMs - Call 100+ LLMs (Python SDK + AI Gateway) All Supported Endpoints - /chat/completions , /responses , /embeddings , /images , /audio , /batches , /rerank , /a2a , /messages and more. Python SDK AI Gateway (Proxy Server) Getting Started - E2E Tutorial - Setup virtual keys, make your first request"
      },
      {
        "source_id": "c996bde3-6773-40e5-8860-77bf34569653",
        "citation_number": 14,
        "cited_text": "Use with Cursor IDE Docs: MCP Gateway How to use LiteLLM You can use LiteLLM through either the Proxy Server or Python SDK. Both gives you a unified interface to access multiple LLMs (100+ LLMs). Choose the option that best fits your needs: LiteLLM AI Gateway LiteLLM Python SDK Use Case Central service (LLM Gateway) to access multiple LLMs Use LiteLLM directly in your Python code Who Uses It? Gen AI Enablement / ML Platform Teams Developers building LLM projects Key Features Centralized API gateway with authentication and authorization, multi-tenant cost tracking and spend management per project/user, per-project customization (logging, guardrails, caching), virtual keys for secure access control, admin dashboard UI for monitoring and management"
      },
      {
        "source_id": "c996bde3-6773-40e5-8860-77bf34569653",
        "citation_number": 15,
        "cited_text": "Direct Python library integration in your codebase, Router with retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - Router , application-level load balancing and cost tracking, exception handling with OpenAI-compatible errors, observability callbacks (Lunary, MLflow, Langfuse, etc.) LiteLLM Performance: 8ms P95 latency at 1k RPS (See benchmarks here ) Jump to LiteLLM Proxy (LLM Gateway) Docs Jump to Supported LLM Providers Stable Release: Use docker images with the -stable tag. These have undergone 12 hour load tests, before being published. More information about the release cycle here"
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 16,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 17,
        "cited_text": "Model context protocol (MCP) Model Context Protocol (MCP) is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts. The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model."
      },
      {
        "source_id": "c996bde3-6773-40e5-8860-77bf34569653",
        "citation_number": 18,
        "cited_text": "Docs: LLM Providers Agents - Invoke A2A Agents (Python SDK + AI Gateway) Supported Providers - LangGraph, Vertex AI Agent Engine, Azure AI Foundry, Bedrock AgentCore, Pydantic AI Python SDK - A2A Protocol AI Gateway (Proxy Server) Step 1. Add your Agent to the AI Gateway Step 2. Call Agent via A2A SDK Docs: A2A Agent Gateway MCP Tools - Connect MCP servers to any LLM (Python SDK + AI Gateway) Python SDK - MCP Bridge AI Gateway - MCP Gateway Step 1. Add your MCP Server to the AI Gateway Step 2. Call MCP tools via /chat/completions"
      },
      {
        "source_id": "c996bde3-6773-40e5-8860-77bf34569653",
        "citation_number": 19,
        "cited_text": "Contributors 1,384 + 1,370 contributors Languages Python 82.5% TypeScript 15.7% HTML 1.3% JavaScript 0.4% Shell 0.1% Makefile 0.0% Footer © 2026 GitHub, Inc. Footer navigation Terms Privacy Security Status Community Docs Contact Manage cookies Do not share my personal information You can't perform that action at this time."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 20,
        "cited_text": "Repository files navigation README Apache-2.0 license 🛠ToolBench🤖 Model • Data Release • Web Demo • Tool Eval • Paper • Citation 🔨This project (ToolLLM) aims to construct open-source, large-scale, high-quality instruction tuning SFT data to facilitate the construction of powerful LLMs with general tool-use capability. We aim to empower open-source LLMs to master thousands of diverse real-world APIs. We achieve this by collecting a high-quality instruction-tuning dataset. It is constructed automatically using the latest ChatGPT (gpt-3.5-turbo-16k), which is upgraded with enhanced function call capabilities. We provide the dataset, the corresponding training and evaluation scripts, and a capable model ToolLLaMA fine-tuned on ToolBench."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 21,
        "cited_text": "✨Here is an overview of the dataset construction, training, and evaluation. ✨✨Features: API Collection : we gather 16464 representational state transfer (REST) APIs from RapidAPI , a platform that hosts massive real-world APIs provided by developers. Instruction Generation : we curate instructions that involve both single-tool and multi-tool scenarios. Answer Annotation : we develop a novel depth-first search based decision tree (DFSDT) to bolster the planning and reasoning ability of LLMs, which significantly improves the annotation efficiency and successfully annotates those complex instructions that cannot be answered with CoT or ReACT. We provide responses that not only include the final answer but also incorporate the model's reasoning process, tool execution, and tool execution results . API Retriver : we incorporate API retrieval to equip ToolLLaMA with open-domain tool-using abilities. All the data is automatically generated by OpenAI API and filtered by us, the whole data creation process is easy to scale up."
      },
      {
        "source_id": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
        "citation_number": 22,
        "cited_text": "View PDF Abstract: Despite the advancements of open-source large language models (LLMs), e.g., LLaMA, they remain significantly limited in tool-use capabilities, i.e., using external tools (APIs) to fulfill human instructions. The reason is that current instruction tuning largely focuses on basic language tasks but ignores the tool-use domain. This is in contrast to the excellent tool-use capabilities of state-of-the-art (SOTA) closed-source LLMs, e.g., ChatGPT. To bridge this gap, we introduce ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation. We first present ToolBench, an instruction-tuning dataset for tool use, which is constructed automatically using ChatGPT. Specifically, the construction can be divided into three stages: (i) API collection: we collect 16,464 real-world RESTful APIs spanning 49 categories from RapidAPI Hub; (ii) instruction generation: we prompt ChatGPT to generate diverse instructions involving these APIs, covering both single-tool and multi-tool scenarios; (iii) solution path annotation: we use ChatGPT to search for a valid solution path (chain of API calls) for each instruction. To enhance the reasoning capabilities of LLMs, we develop a novel depth-first search-based decision tree algorithm. It enables LLMs to evaluate multiple reasoning traces and expand the search space. Moreover, to evaluate the tool-use capabilities of LLMs, we develop an automatic evaluator: ToolEval. Based on ToolBench, we fine-tune LLaMA to obtain an LLM ToolLLaMA, and equip it with a neural API retriever to recommend appropriate APIs for each instruction. Experiments show that ToolLLaMA demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, and exhibits comparable performance to ChatGPT. Our ToolLLaMA also demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 23,
        "cited_text": "You can't perform that action at this time."
      },
      {
        "source_id": "2be6827b-3272-4f52-af8e-e3daa4204826",
        "citation_number": 24,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 25,
        "cited_text": "You can't perform that action at this time."
      },
      {
        "source_id": "cb9e9864-d0db-416a-9b2b-79a804a1c933",
        "citation_number": 26,
        "cited_text": "If you're looking for more advanced customization or agent orchestration, check out LangGraph , our framework for building controllable agent workflows. Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangChain ecosystem While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. Deep Agents — Build agents that can plan, use subagents, and leverage file systems for complex tasks LangGraph — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework Integrations — Chat & embedding models, tools & toolkits, and more LangSmith — Agent evals, observability, and debugging for LLM apps LangSmith Deployment — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows"
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 27,
        "cited_text": "Web UI The app will be available on http://localhost:3000/ Backend server This server will be available on http://localhost:5000/ . To start a request, call http://localhost:5000/stream with a GET or POST request containing a JSON object with the following fields: ToolEval By fine-tuning LLaMA on ToolBench, we obtain ToolLLaMA . Considering that human evaluation can be time-consuming, we follow AlpacaEval to develop an efficient machine evaluator ToolEval , which incorporates two evaluation metrics: Pass Rate : Calculates the proportion of successfully completing an instruction within limited OpenAI API calls. Preference : Measured by comparing two answers (action sequences) for a given instruction. We pre-define a set of criteria for a better answer, which are organized as prompts for ChatGPT. We provide the test instruction and two candidate answers to the evaluator and obtain its preference. We evaluate each answer pair multiple times to improve the reliability of our system. Then we calculate the Win Rate (percentage of being preferred by the evaluator). More details can be found in our paper."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 28,
        "cited_text": "To validate the reliability of ChatGPT evaluator in both pass rate and win rate, we sample among four different methods (ChatGPT+ReACT, ChatGPT+DFSDT, ToolLLaMA+DFSDT and GPT4+DFSDT) to obtain solution pairs for 300 test instructions for each method. Then we engage humans to annotate the pass rate for ChatGPT+DFSDT, ToolLLaMA+DFSDT and GPT4+DFSDT, and the win rate among ChatGPT+ReACT and ChatGPT+DFSDT. Our ChatGPT evaluator demonstrates a high agreement of 87.1% in pass rate and 80.3% in win rate with human annotators. This result shows that our evaluator generates highly similar evaluation results to humans and can be viewed as a credible evaluator who simulates human evaluation on pass rate and win rate."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 29,
        "cited_text": "Pass Rate: <cited_table> Win Rate: (Reference model: ChatGPT-ReACT) <cited_table>",
        "cited_table": {
          "num_columns": 9,
          "rows": [
            [
              "Method",
              "Model",
              "I1-Inst.",
              "I1-Tool",
              "I1-Cate.",
              "I2-Inst.",
              "I2-Cate.",
              "I3-Inst.",
              "Average"
            ],
            [
              "ReACT",
              "Claude-2",
              "5.5",
              "3.5",
              "5.5",
              "6",
              "6",
              "14",
              "6.8"
            ],
            [
              "",
              "Text-Davinci-003",
              "12",
              "20",
              "20",
              "8.5",
              "14.5",
              "24",
              "16.5"
            ],
            [
              "",
              "ChatGPT",
              "41.5",
              "44",
              "44.5",
              "42.5",
              "46.5",
              "22",
              "40.2"
            ],
            [
              "",
              "ToolLLaMA",
              "25",
              "29",
              "33",
              "30.5",
              "31.5",
              "25",
              "29"
            ],
            [
              "",
              "GPT4",
              "53.5",
              "50.0",
              "53.5",
              "67.0",
              "72.0",
              "47.0",
              "57.2"
            ],
            [
              "DFSDT",
              "Claude-2",
              "20.5",
              "31",
              "18.5",
              "17",
              "20.5",
              "28",
              "22.6"
            ],
            [
              "",
              "Text-Davinci-003",
              "43.5",
              "44",
              "46",
              "37",
              "42",
              "46",
              "43.1"
            ],
            [
              "",
              "ChatGPT",
              "54.5",
              "65",
              "60.5",
              "75",
              "71.5",
              "62",
              "64.8"
            ],
            [
              "",
              "ToolLLaMA",
              "57",
              "61",
              "62",
              "77",
              "77",
              "66",
              "66.7"
            ],
            [
              "",
              "ToolLLaMA-Retreiver",
              "64",
              "64",
              "60.5",
              "81.5",
              "68.5",
              "65",
              "67.3"
            ],
            [
              "",
              "GPT4",
              "60",
              "71.5",
              "67",
              "79.5",
              "77.5",
              "71",
              "71.1"
            ]
          ]
        }
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 30,
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
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 31,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 32,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 33,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 34,
        "cited_text": "Notes and limitations Positioning of function call parts: When using custom function declarations alongside built-in tools (like Google Search), the model may return a mix of functionCall , toolCall , and toolResponse parts in a single turn. Because of this, don't assume the functionCall will always be the last item in the parts array. If you are manually parsing the JSON response, always iterate through the parts array rather than relying on position. Only a subset of the OpenAPI schema is supported. For ANY mode, the API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your function parameter and response schemas by shortening property names, reducing nesting, or limiting the number of function declarations. Supported parameter types in Python are limited. Automatic function calling is a Python SDK feature only."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "根据提供的源文件，关于「Function Calling（函数调用）」领域的最新研究突破、2025-2026年的技术趋势以及未来挑战的深度解析如下：\n\n### 一、 2025-2026年重要趋势与技术突破\n\n1.  **大规模工具生态的动态管理 (Tool Search)**\n    *   **技术趋势**：最新的模型如 **GPT-5.4** 引入了 **Tool Search（工具检索）** 功能。当应用拥有成千上万个 API 时，不再需要一次性将所有 Schema 塞入上下文，而是允许模型根据需求动态搜索并加载相关工具，显著解决了 Token 限制问题 [1-3]。\n    *   **架构演进**：OpenAI 的 **Deferred Loading（延迟加载）** 机制允许模型在交互过程中发现并集成之前未定义的工具 [2, 4]。\n\n2.  **推理过程的显式化与一致性 (Thought Signatures)**\n    *   **技术突破**：**Gemini 3** 系列模型引入了 **Thought Signatures（思维特征）**。由于 API 调用是无状态的，思维特征允许模型在多轮对话中传递其内部推理逻辑，确保复杂任务在多次函数调用间保持上下文一致性 [5-7]。\n    *   **推理模型集成**：在 **GPT-5** 或 **o4-mini** 等推理模型中，工具调用生成的推理项（Reasoning items）必须随工具输出一并回传，以维持模型的思考链条 [8]。\n\n3.  **协议标准化与互操作性 (MCP)**\n    *   **行业标准**：**Model Context Protocol (MCP)** 已成为连接 AI 应用与外部工具（如本地 Shell、数据库、MCP 服务器）的开放标准 [9, 10]。Google、OpenAI 和 Anthropic 的 SDK 均已内置或实验性支持 MCP，大幅降低了跨平台集成的 boilerplate 代码 [9, 11, 12]。\n\n4.  **执行环境的云端化 (Server-side Tools)**\n    *   **能力跃迁**：**Claude 4.6** 等模型开始区分 **Client tools（客户端工具）** 和 **Server tools（服务器工具）**。后者（如 web_search, code_execution）直接在厂商的基础设施上运行，开发者无需维护复杂的执行环境，且具备更高的安全隔离性 [13]。\n\n---\n\n### 二、 重要论文与算法模型\n\n*   **BFCL V4 Agentic (Berkeley Function Calling Leaderboard)**：\n    2025年7月发布的最新基准，标志着研究重心从单轮调用转向**智能体场景（Agentic settings）**，重点评估多跳推理、错误恢复（Error recovery）及智能体记忆管理 [14]。\n*   **Gorilla & RAFT (Retrieval-Augmented Fine-Tuning)**：\n    通过检索增强微调，模型在面对频繁更新的 API 文档时表现出极强的适应性，并利用 **GoEx 引擎** 实现了具备“撤销（Undo）”和“损害限制（Damage confinement）”能力的动作执行环境 [14-16]。\n*   **ToolBench & DFSDT (Depth-First Search Decision Tree)**：\n    **ToolLLaMA-2-v2** 利用深度优先搜索决策树算法，使模型能够评估多条推理轨迹并扩大搜索空间，在复杂多步任务中的表现已可与 ChatGPT 媲美 [17-19]。\n\n---\n\n### 三、 未解决的挑战\n\n1.  **幻觉与幻觉检测 (Hallucination)**：\n    尽管引入了 **Strict Mode（严格模式）** [20, 21] 和 **Function relevance detection** [22]，模型仍可能生成不存在的参数或虚构 API 调用。如何在大规模（16,000+ API）场景下完全消除幻觉仍是难题 [18, 23]。\n2.  **安全性与风险控制**：\n    LLM 生成的动作（如 SQL 注入风险、文件系统操作）在生产环境中具有高风险。目前的解决方案如 **GoEx** 提供的沙箱和事后验证仍处于早期阶段 [15, 24]。\n3.  **长链调用的性能退化**：\n    随着调用步骤增加，Token 消耗呈指数增长，且容易出现逻辑漂移。目前的 **Prompt Caching（提示词缓存）** 技术虽降低了成本，但未完全解决长序列推理的稳定性问题 [3, 25]。\n\n---\n\n### 四、 未来可能的突破点\n\n1.  **原生多模态函数响应 (Multimodal Responses)**：\n    **Gemini 3** 已开始支持在函数响应中包含图像（PNG/JPEG）和文档（PDF），未来模型将能直接通过工具获取并“理解”非文本数据，实现更高维度的交互 [26, 27]。\n2.  **自主计算机使用 (Computer Use)**：\n    研究方向正从调用单一 API 转向直接控制计算机（Computer Use），模型将具备操作 UI、移动鼠标和管理文件系统的综合能力，成为真正的数字代理 [28]。\n3.  **自定义约束语法 (Context-Free Grammars)**：\n    通过 **Lark** 或 **Regex** 等上下文无关文法（CFG）约束非 JSON 格式的输出，使 LLM 能精准对接具有特殊格式要求的工业协议 [29, 30]。\n\n**开发者建议**：鉴于技术的快速演进，建议优先采用支持 **MCP** 的架构以保证未来的兼容性，并在复杂任务中开启 **Strict Mode** 以确保 Schema 的 100% 遵循 [9, 10, 20]。",
    "conversation_id": "6644b4c8-4688-4d87-b7ac-5f06f7119a94",
    "sources_used": [
      "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "7c52ee01-0056-43bb-9fc9-a17792878206",
      "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "2be6827b-3272-4f52-af8e-e3daa4204826",
      "50c5c72e-5468-4953-88a0-4c5e847594a1"
    ],
    "citations": {
      "1": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "2": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "3": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "4": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "5": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "6": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "7": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "8": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "9": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "10": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "11": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "12": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "13": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "14": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "15": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "16": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "17": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "18": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
      "19": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
      "20": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "21": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "22": "7c52ee01-0056-43bb-9fc9-a17792878206",
      "23": "2be6827b-3272-4f52-af8e-e3daa4204826",
      "24": "50c5c72e-5468-4953-88a0-4c5e847594a1",
      "25": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "26": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "27": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
      "28": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
      "29": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
      "30": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e"
    },
    "references": [
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 1,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 2,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 3,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 4,
        "cited_text": "Sample response with multiple function calls If you are using tool search , you may also see tool_search_call and tool_search_output items before a function_call . Once the function is loaded, handle the function call in the same way shown here. Execute function calls and append results python In the example above, we have a hypothetical call_function to route each call. Here's a possible implementation: Execute function calls and append results python Formatting results The result you pass in the function_call_output message should typically be a string, where the format is up to you (JSON, error codes, plain text, etc.). The model will interpret that string as needed."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 5,
        "cited_text": "You can also construct FunctionDeclarations from Python functions directly using types.FunctionDeclaration.from_callable(client=client, callable=your_function) . Function calling with thinking models Gemini 3 and 2.5 series models use an internal \"thinking\" process to reason through requests. This significantly improves function calling performance, allowing the model to better determine when to call a function and which parameters to use. Because the Gemini API is stateless, models use thought signatures to maintain context across multi-turn conversations."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 6,
        "cited_text": "This section covers advanced management of thought signatures and is only necessary if you're manually constructing API requests (e.g., via REST) or manipulating conversation history. If you're using the Google GenAI SDKs (our official libraries), you don't need to manage this process . The SDKs automatically handle the necessary steps, as shown in the earlier example . Managing conversation history manually If you modify the conversation history manually, instead of sending the complete previous response you must correctly handle the thought_signature included in the model's turn."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 7,
        "cited_text": "Follow these rules to ensure the model's context is preserved: Always send the thought_signature back to the model inside its original Part . Always include the exact id from the function_call in your function_response so the API can map the result to the correct request. Don't merge a Part containing a signature with one that does not. This breaks the positional context of the thought. Don't combine two Parts that both contain signatures, as the signature strings cannot be merged. Gemini 3 thought signatures"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 8,
        "cited_text": "Complete tool calling example python Complete tool calling example python Note that for reasoning models like GPT-5 or o4-mini, any reasoning items returned in model responses with tool calls must also be passed back with tool call outputs. Defining functions Functions are usually declared in the tools parameter of each API request. With tool search , your application can also load deferred functions later in the interaction. Either way, each callable function uses the same schema shape. A function definition has the following properties:"
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 9,
        "cited_text": "Model context protocol (MCP) Model Context Protocol (MCP) is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts. The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 10,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 11,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 12,
        "cited_text": "Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting"
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 13,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 14,
        "cited_text": "Repository files navigation README Apache-2.0 license Gorilla: Large Language Model Connected with Massive APIs Latest Updates 📢 Check out our detailed Berkeley Function Calling Leaderboard changelog (Last updated: ) for the latest dataset / model updates to the Berkeley Function Calling Leaderboard! 🤖 [07/17/2025] Announcing BFCL V4 Agentic! As function-calling forms the bedrock of Agentic systems, BFCL V4 Agentic benchmark focuses on tool-calling in real-world agentic settings, featuring web search with multi-hop reasoning and error recovery, agent memory management, and format sensitivity evaluation. [ Web-search Blog ] [ Memory Blog ] [ Format Sensitivity Blog ] [ PR ] [ Tweet ] 🎯 [10/04/2024] Introducing the Agent Arena by Gorilla X LMSYS Chatbot Arena! Compare different agents in tasks like search, finance, RAG, and beyond. Explore which models and tools work best for specific tasks through our novel ranking system and community-driven prompt hub. [ Blog ] [ Arena ] [ Leaderboard ] [ Dataset ] [ Tweet ] 📣 [09/21/2024] Announcing BFCL V3 - Evaluating multi-turn and multi-step function calling capabilities! New state-based evaluation system tests models on handling complex workflows, sequential functions, and service states. [ Blog ] [ Leaderboard ] [ Code ] [ Tweet ] 🚀 [08/20/2024] Released BFCL V2 • Live! The Berkeley Function-Calling Leaderboard now features enterprise-contributed data and real-world scenarios. [ Blog ] [ Live Leaderboard ] [ V2 Categories Leaderboard ] [ Tweet ] ⚡ [04/12/2024] Excited to release GoEx - a runtime for LLM-generated actions like code, API calls, and more. Featuring \"post-facto validation\" for assessing LLM actions after execution, \"undo\" and \"damage confinement\" abstractions to manage unintended actions & risks. This paves the way for fully autonomous LLM agents, enhancing interaction between apps & services with human-out-of-loop. [ Blog ] [ Code ] [ Paper ] [ Tweet ] ⏰ [04/01/2024] Introducing cost and latency metrics into Berkeley function calling leaderboard ! 🚀 [03/15/2024] RAFT: Adapting Language Model to Domain Specific RAG is live! [ MSFT-Meta blog ] [ Berkeley Blog ] 🏆 [02/26/2024] Berkeley Function Calling Leaderboard is live! 🎯 [02/25/2024] OpenFunctions v2 sets new SoTA for open-source LLMs! 🔥 [11/16/2023] Excited to release Gorilla OpenFunctions 💻 [06/29/2023] Released gorilla-cli , LLMs for your CLI! 🟢 [06/06/2023] Released Commercially usable, Apache 2.0 licensed Gorilla models 🚀 [05/30/2023] Provided the CLI interface to chat with Gorilla! 🚀 [05/28/2023] Released Torch Hub and TensorFlow Hub Models! 🚀 [05/27/2023] Released the first Gorilla model! or 🤗 ! 🔥 [05/27/2023] We released the APIZoo contribution guide for community API contributions! 🔥 [05/25/2023] We release the APIBench dataset and the evaluation code of Gorilla!"
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 15,
        "cited_text": "• Head-to-head agent comparisons with ELO rating system • Framework compatibility testing (LangChain, AutoGPT) • Community-driven evaluation platform • Real-world task performance metrics Gorilla Execution Engine (GoEx) 🔧 Infra Runtime for executing LLM-generated actions with safety guarantees • Post-facto validation for verifying LLM actions after execution • Undo capabilities and damage confinement for risk mitigation • OAuth2 and API key authentication for multiple services • Support for RESTful APIs, databases, and filesystem operations"
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 16,
        "cited_text": "• Docker-based sandboxed execution environment Retrieval-Augmented Fine-tuning (RAFT) 📝 Fine-tuning 🤖 Model Fine-tuning LLMs for robust domain-specific retrieval • Novel fine-tuning recipe for domain-specific RAG • Chain-of-thought answers with direct document quotes • Training with oracle and distractor documents • Improved performance on PubMed, HotpotQA, and Gorilla benchmarks • Efficient adaptation of smaller models for domain QA Gorilla CLI 🤖 Model 🔧 Local CLI Infra LLMs for your command-line interface • User-friendly CLI tool supporting ~1500 APIs (Kubernetes, AWS, GCP, etc.)"
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 17,
        "cited_text": "2024.8 Update We have updated the RapidAPI server with a new IP, please make sure you get the latest code. You can also build it locally using codes here . 💁♂💁💁♀ Join Us on Discord! Read this in 中文. What's New [2024/3/17] Welcome to StableToolBench : A stable and reliable local toolbench server based on API response simulation. Dive deeper into the tech behind StableToolBench with paper here and explore more on the project homepage . Codes are available here . [2023/9/29] A new version ToolEval which is more stable and covers more models including GPT4! Please refer to ToolEval for more details. Besides, ToolLLaMA-2-7b-v2 is released with stronger tool-use capabilities. Please use the ToolLLaMA-2-7b-v2 model to reproduce our latest experimental results with the new version ToolEval. [2023/8/30] Data updation, with more than 120,000 solution path annotations and intact reasoning thoughts ! Please find data.zip on Google Drive . [2023/8/8] No more hallucination! ToolLLaMA-2-7b-v1 (fine-tuned from LLaMA-2-7b) is released with lower API hallucination than ChatGPT. [2023/8/4] We provide RapidAPI backend service to free you from using your own RapidAPI key and subscribing the APIs. Please fill out our form . We will review it as soon as possible and send you the ToolBench key to get start on it! [2023/8/1] Our paper is released. [2023/7/27] New version ToolBench is released."
      },
      {
        "source_id": "97ffa2c2-553f-4548-a73b-5ae4d9df557e",
        "citation_number": 18,
        "cited_text": "✨Here is an overview of the dataset construction, training, and evaluation. ✨✨Features: API Collection : we gather 16464 representational state transfer (REST) APIs from RapidAPI , a platform that hosts massive real-world APIs provided by developers. Instruction Generation : we curate instructions that involve both single-tool and multi-tool scenarios. Answer Annotation : we develop a novel depth-first search based decision tree (DFSDT) to bolster the planning and reasoning ability of LLMs, which significantly improves the annotation efficiency and successfully annotates those complex instructions that cannot be answered with CoT or ReACT. We provide responses that not only include the final answer but also incorporate the model's reasoning process, tool execution, and tool execution results . API Retriver : we incorporate API retrieval to equip ToolLLaMA with open-domain tool-using abilities. All the data is automatically generated by OpenAI API and filtered by us, the whole data creation process is easy to scale up."
      },
      {
        "source_id": "cc5d08c8-45bb-46aa-b1d8-643f0b07a957",
        "citation_number": 19,
        "cited_text": "View PDF Abstract: Despite the advancements of open-source large language models (LLMs), e.g., LLaMA, they remain significantly limited in tool-use capabilities, i.e., using external tools (APIs) to fulfill human instructions. The reason is that current instruction tuning largely focuses on basic language tasks but ignores the tool-use domain. This is in contrast to the excellent tool-use capabilities of state-of-the-art (SOTA) closed-source LLMs, e.g., ChatGPT. To bridge this gap, we introduce ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation. We first present ToolBench, an instruction-tuning dataset for tool use, which is constructed automatically using ChatGPT. Specifically, the construction can be divided into three stages: (i) API collection: we collect 16,464 real-world RESTful APIs spanning 49 categories from RapidAPI Hub; (ii) instruction generation: we prompt ChatGPT to generate diverse instructions involving these APIs, covering both single-tool and multi-tool scenarios; (iii) solution path annotation: we use ChatGPT to search for a valid solution path (chain of API calls) for each instruction. To enhance the reasoning capabilities of LLMs, we develop a novel depth-first search-based decision tree algorithm. It enables LLMs to evaluate multiple reasoning traces and expand the search space. Moreover, to evaluate the tool-use capabilities of LLMs, we develop an automatic evaluator: ToolEval. Based on ToolBench, we fine-tune LLaMA to obtain an LLM ToolLLaMA, and equip it with a neural API retriever to recommend appropriate APIs for each instruction. Experiments show that ToolLLaMA demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, and exhibits comparable performance to ChatGPT. Our ToolLLaMA also demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 20,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 21,
        "cited_text": "If you send strict: true and your schema does not meet the requirements above, the request will be rejected with details about the missing constraints. If you omit strict , the default depends on the API: Responses requests will normalize your schema into strict mode (for example, by setting additionalProperties: false and marking all fields as required), which can make previously optional fields mandatory, while Chat Completions requests remain non-strict by default. To opt out of strict mode in Responses and keep non-strict, best-effort function calling, explicitly set strict: false ."
      },
      {
        "source_id": "7c52ee01-0056-43bb-9fc9-a17792878206",
        "citation_number": 22,
        "cited_text": "• Retrieval-augmented training for test-time adaptation Gorilla OpenFunctions-V2 🤖 Model Drop-in alternative for function calling, supporting multiple complex data types and parallel execution • Multiple & parallel function execution with OpenAI-compatible endpoints • Native support for Python, Java, JavaScript, and REST APIs with expanded data types • Function relevance detection to reduce hallucinations • Enhanced RESTful API formatting capabilities • State-of-the-art performance among open-source models Berkeley Function Calling Leaderboard (BFCL)"
      },
      {
        "source_id": "2be6827b-3272-4f52-af8e-e3daa4204826",
        "citation_number": 23,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "50c5c72e-5468-4953-88a0-4c5e847594a1",
        "citation_number": 24,
        "cited_text": "Parallel Function Calling Newer models such as gpt-5, gpt-4.1 or gpt-4o can call multiple functions in one turn. How to call functions with model generated arguments In our next example, we'll demonstrate how to execute functions whose inputs are model-generated, and use this to implement an agent that can answer questions for us about a database. For simplicity we'll use the Chinook sample database . Note: SQL generation can be high-risk in a production environment since models are not perfectly reliable at generating correct SQL."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 25,
        "cited_text": "Tool use examples For a complete hands-on walkthrough, see the tutorial . For reference examples of individual concepts, see Define tools and Handle tool calls . What happens when Claude needs more information Pricing Tool use requests are priced based on: The total number of input tokens sent to the model (including in the tools parameter) The number of output tokens generated For server-side tools, additional usage-based pricing (e.g., web search charges per search performed) Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage."
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 26,
        "cited_text": "Python Javascript More For models before the Gemini 3 series, use the Live API . Multimodal function responses Note: This feature is available for Gemini 3 series models. For Gemini 3 series models, you can include multimodal content in the function response parts that you send to the model. The model can process this multimodal content in its next turn to produce a more informed response. The following MIME types are supported for multimodal content in function responses: Images : image/png , image/jpeg , image/webp Documents : application/pdf , text/plain"
      },
      {
        "source_id": "3389f9e7-2282-4ce6-a509-8bb1abdd99bd",
        "citation_number": 27,
        "cited_text": "To include multimodal data in a function response, include it as one or more parts nested within the functionResponse part. Each multimodal part must contain inlineData . If you reference a multimodal part from within the structured response field, it must contain a unique displayName . You can also reference a multimodal part from within the structured response field of the functionResponse part by using the JSON reference format {\"$ref\": \"<displayName>\"} . The model substitutes the reference with the multimodal content when processing the response. Each displayName can only be referenced once in the structured response field."
      },
      {
        "source_id": "dc281e96-2bed-443d-a0b9-d44e12d990e1",
        "citation_number": 28,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 29,
        "cited_text": "Custom tool calling example python Just as before, the output array will contain a tool call generated by the model. Except this time, the tool call input is given as plain text. Context-free grammars A context-free grammar (CFG) is a set of rules that define how to produce valid text in a given format. For custom tools, you can provide a CFG that will constrain the model's text input for a custom tool. You can provide a custom CFG using the grammar parameter when configuring a custom tool. Currently, we support two CFG syntaxes when defining grammars: lark and regex ."
      },
      {
        "source_id": "d5ba7ff3-a3f5-4ec2-baf0-7ba603566f2e",
        "citation_number": 30,
        "cited_text": "Lark CFG Lark context free grammar example python The output from the tool should then conform to the Lark CFG that you defined: Grammars are specified using a variation of Lark . Model sampling is constrained using LLGuidance . Some features of Lark are not supported: Lookarounds in lexer regexes Lazy modifiers ( *? , +? , ?? ) in lexer regexes Priorities of terminals Templates Imports (other than built-in %import common) %declare s We recommend using the Lark IDE to experiment with custom grammars."
      }
    ]
  }
}
