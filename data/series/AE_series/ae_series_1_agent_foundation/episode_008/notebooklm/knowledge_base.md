# 知识库：Parallelization 与 Orchestrator-Workers：并行与动态分工

生成时间: 2026-04-06 15:23
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "「Parallelization（并行）」与「Orchestrator-Workers（协调者-工作者）」是构建高效 AI Agent 系统（Agentic Systems）的核心架构模式。以下是基于来源文件的详细技术概述：\n\n### 1. 技术演进路线\nAI Agent 的架构演进遵循从简单到复杂、从静态到动态的逻辑：\n*   **基础阶段：增强型 LLM (Augmented LLM)**：最基本的构建块，即在 LLM 基础上增加检索（Retrieval）、工具（Tools）和记忆（Memory）能力 [1]。\n*   **线性流：提示词链 (Prompt Chaining)**：将任务分解为固定的顺序步骤，前一步的输出作为后一步的输入 [2]。\n*   **路由流 (Routing)**：根据输入对任务进行分类，并引导至专门的后续任务或模型（如将简单问题引导至小型模型 Claude Haiku） [3, 4]。\n*   **并行阶段 (Parallelization)**：LLM 同时处理任务，通过**并行化**来降低延迟并提高精度 [5]。\n*   **动态分工阶段 (Orchestrator-Workers)**：引入中央协调者动态分解任务，这是应对复杂、不可预测任务的关键演进 [6]。\n*   **高级阶段：自主智能体 (Autonomous Agents)**：智能体在循环中独立规划、使用工具并根据环境反馈进行推理，迈向自主完成任务 [7, 8]。\n\n### 2. 核心算法与机制名称\n*   **Agent Forest（智能体森林）**：一种核心的采样与投票（sampling-and-voting）方法，研究表明 LLM 的性能会随实例化智能体数量的增加而扩展 [9]。\n*   **Pregel & Apache Beam**：虽然不是直接的 AI 算法，但它们是现代 Agent 编排框架（如 LangGraph）的底层灵感来源，用于处理大规模状态计算 [10, 11]。\n*   **RAG (检索增强生成)**：用于在并行或协调任务中为 Agent 提供准确的外部知识背景 [12, 13]。\n*   **Sectioning（分段）与 Voting（投票）**：并行化模式下的两大核心逻辑：前者将任务拆分为独立子任务运行，后者通过多次运行同一任务以获取多样化结果或增强信心 [5]。\n\n### 3. 主要架构模式\n#### **并行化模式 (Parallelization)**\n*   **架构定义**：多个模型实例同时工作，输出结果由程序化聚合 [5]。\n*   **子模式**：\n    *   **分段 (Sectioning)**：如一个模型处理用户查询，另一个模型同步进行安全审计（Guardrails），这比单一模型处理多项任务性能更好 [14]。\n    *   **投票 (Voting)**：如在代码审计中，使用多个不同提示词的实例共同检查漏洞，通过投票决定最终反馈 [14]。\n\n#### **协调者-工作者模式 (Orchestrator-Workers)**\n*   **架构定义**：由一个中心 LLM（协调者）动态分解任务，委派给多个工作者 LLM（Worker），最后汇总结果 [6]。\n*   **关键特征**：与并行化的主要区别在于其**灵活性**。子任务不是预定义的，而是由协调者根据具体输入实时决定的（例如在复杂的代码修改任务中，涉及的文件数量是不确定的） [6, 15]。\n\n### 4. 关键技术指标\n*   **延迟与成本优化**：\n    *   **提示词缓存 (Prompt Caching)**：可将延迟降低 **>2 倍**，对于重复性任务，成本最高可降低 **90%** [16]。\n    *   **批量处理 (Batch Processing)**：Message Batches API 处理大量异步请求时，可降低 **50%** 的成本 [17]。\n*   **吞吐量与扩展性**：\n    *   **批处理限制**：单个消息批次上限为 **100,000 条请求** 或 **256 MB** [18]。\n    *   **扩展输出 (Extended Output)**：在批处理模式下，单次生成支持高达 **300,000 tokens** 的长文本 [19]。\n*   **性能基准**：\n    *   **执行速度**：高效框架（如 CrewAI）在某些 QA 任务中比传统框架快 **5.76 倍** [20]。\n    *   **缓存阈值**：最小可缓存长度通常为 **1,024**（Sonnet）至 **4,096**（Opus）tokens [21]。\n\n### 5. 关键组件\n*   **Orchestrator (协调者)**：负责任务分解、委派及结果综合 [6]。\n*   **Specialized Workers (专业工作者)**：专注于特定领域的智能体，如库存管理 Agent、索赔审核 Agent 等 [12, 13]。\n*   **Memory Retention (记忆保存)**：跨交互保留历史信息，确保多步骤任务的连续性和个性化体验 [22, 23]。\n*   **Guardrails (安全护栏)**：内置的安全与可靠性组件，用于在并行处理中实时拦截违规内容 [24, 25]。\n*   **Code Interpretation (代码解释器)**：允许 Agent 动态生成并执行代码，以处理复杂的数学或数据分析问题 [22]。",
    "conversation_id": "c20d4856-4d53-4d6c-9c16-9b0f8c2f5238",
    "sources_used": [
      "f50c5498-80ef-498e-b316-77915c2391a1",
      "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
      "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
      "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "f71e0184-ceb9-46da-913f-35250c96dc34"
    ],
    "citations": {
      "1": "f50c5498-80ef-498e-b316-77915c2391a1",
      "2": "f50c5498-80ef-498e-b316-77915c2391a1",
      "3": "f50c5498-80ef-498e-b316-77915c2391a1",
      "4": "f50c5498-80ef-498e-b316-77915c2391a1",
      "5": "f50c5498-80ef-498e-b316-77915c2391a1",
      "6": "f50c5498-80ef-498e-b316-77915c2391a1",
      "7": "f50c5498-80ef-498e-b316-77915c2391a1",
      "8": "f50c5498-80ef-498e-b316-77915c2391a1",
      "9": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
      "10": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "11": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
      "12": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "13": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "14": "f50c5498-80ef-498e-b316-77915c2391a1",
      "15": "f50c5498-80ef-498e-b316-77915c2391a1",
      "16": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "17": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "18": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "19": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "20": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "21": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "22": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "23": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "24": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "25": "f71e0184-ceb9-46da-913f-35250c96dc34"
    },
    "references": [
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 1,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 2,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 3,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 4,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 5,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 6,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 7,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 8,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      },
      {
        "source_id": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
        "citation_number": 9,
        "cited_text": "arXiv:2402.05120 (cs) [Submitted on 3 Feb 2024 ( v1 ), last revised 11 Oct 2024 (this version, v2)] Title: More Agents Is All You Need Authors: Junyou Li , Qin Zhang , Yangbin Yu , Qiang Fu , Deheng Ye View a PDF of the paper titled More Agents Is All You Need, by Junyou Li and 4 other authors View PDF HTML (experimental) Abstract: We find that, simply via a sampling-and-voting method, the performance of large language models (LLMs) scales with the number of agents instantiated. Also, this method, termed as Agent Forest, is orthogonal to existing complicated methods to further enhance LLMs, while the degree of enhancement is correlated to the task difficulty. We conduct comprehensive experiments on a wide range of LLM benchmarks to verify the presence of our finding, and to study the properties that can facilitate its occurrence. Our code is publicly available at: this https URL"
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 10,
        "cited_text": "Acknowledgements LangGraph is inspired by Pregel and Apache Beam . The public interface draws inspiration from NetworkX . LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain. About Build resilient language agents as graphs. docs.langchain.com/oss/python/langgraph/ Topics python open-source enterprise framework ai gemini openai multiagent agents ai-agents rag pydantic llm generative-ai chatgpt langchain langgraph deepagents Resources Readme License MIT license Code of conduct"
      },
      {
        "source_id": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
        "citation_number": 11,
        "cited_text": "Acknowledgements LangGraph is inspired by Pregel and Apache Beam . The public interface draws inspiration from NetworkX . LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain. Edit this page on GitHub or file an issue . Connect these docs to Claude, VSCode, and more via MCP for real-time answers. Was this page helpful? Yes No Install LangGraph Next Ctrl+I Docs by LangChain home page github x linkedin youtube Resources Forum Changelog LangChain Academy Trust Center"
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 12,
        "cited_text": "End of dialog window. Features Multi-agent collaboration Retrieval augmented generation Orchestrate and execute Memory retention Code interpretation Multi-agent collaboration Amazon Bedrock multi-agent collaboration allows developers to build, deploy, and manage multiple specialized agents seamlessly working together to address increasingly complex business workflows. Each agent focuses on specific tasks under the coordination of a supervisor agent, which breaks down intricate processes into manageable steps to ensure precision and reliability. By automating these complex operational processes, businesses can free their teams from operational burdens, allowing them to focus on innovation and deliver real business value."
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 13,
        "cited_text": "Retrieval augmented generation Agents securely connects to your company's data sources and augments the user requests with the right information to generate an accurate response. For example, if the user asks about claims eligibility, the RAG agent will look up information from the knowledge base and reconcile between the submitted claims and the eligibility policy response: “You need to turn in your driver's license, pictures of the damaged car, and an accident report.” Orchestrate and execute Customers can create an agent in Amazon Bedrock in just a few quick steps, accelerating the time it takes to build generative AI applications. Customers first select a model and write a few instructions in natural language. For example, “you are an inventory management agent that determines product availability in the inventory system.” Agents orchestrates and analyzes the task and breaks it down into the correct logical sequence using the FM's reasoning abilities. Agents automatically calls the necessary APIs to transact with the company systems and processes to fulfill the request, determining along the way if they can proceed or if they need to gather more information."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 14,
        "cited_text": "Examples where parallelization is useful: Sectioning : Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response. Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model's performance on a given prompt. Voting : Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem. Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 15,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 16,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 17,
        "cited_text": "You need to process large volumes of data Immediate responses are not required You want to optimize for cost efficiency You're running large-scale evaluations or analyses The Message Batches API is Anthropic's first implementation of this pattern. This feature is not eligible for Zero Data Retention (ZDR) . Data is retained according to the feature's standard retention policy. Message Batches API The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 18,
        "cited_text": "Large-scale evaluations: Process thousands of test cases efficiently. Content moderation: Analyze large volumes of user-generated content asynchronously. Data analysis: Generate insights or summaries for large datasets. Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries). Batch limitations A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first. The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours. Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download. Batches are scoped to a Workspace . You may view all batches (and their results) that were created within the Workspace that your API key belongs to. Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See Message Batches API rate limits . Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours. Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured spend limit ."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 19,
        "cited_text": "Extended output (beta) The output-300k-2026-03-24 beta header raises the max_tokens cap to 300,000 for batch requests using Claude Opus 4.6 or Claude Sonnet 4.6. Include the header to generate outputs far longer than the standard limit (64k to 128k depending on model) in a single turn. Extended output is available on the Message Batches API only, not the synchronous Messages API. It is supported on the Claude API and is not available on Amazon Bedrock, Vertex AI, or Microsoft Foundry. Use extended output for long-form generation such as book-length drafts and technical documentation, exhaustive structured data extraction, large code-generation scaffolds, and long reasoning chains."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 20,
        "cited_text": "P.S. CrewAI demonstrates significant performance advantages over LangGraph, executing 5.76x faster in certain cases like this QA task example ( see comparison) while achieving higher evaluation scores with faster completion times in certain coding tasks, like in this example ( detailed analysis). Autogen : While Autogen excels at creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows. ChatDev : ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 21,
        "cited_text": "Start with automatic caching. It covers the majority of use cases with minimal effort. Switch to explicit breakpoints only when you need fine-grained control. Key details ¶ Minimum cacheable length: 1,024 tokens for Sonnet; 4,096 tokens for Opus and Haiku 4.5 Cache TTL: 5 minutes by default (refreshed on each hit). A 1-hour TTL is available at 2x base input price. Pricing: Cache writes cost 1.25x base input price. Cache reads cost 0.1x base input price. Breakpoint limit: Up to 4 explicit breakpoints per request. Automatic caching uses one slot."
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 22,
        "cited_text": "Memory retention Agents has the ability to retain memory across interactions, offering more personalized and seamless user experiences. This feature allows an agent to remember historical interactions and improves the accuracy of multistep tasks. Users benefit from improved recommendations and recall of prior context when required, ensuring a more cohesive and efficient interaction with the agent. Code interpretation Agents supports the ability to dynamically generate and execute code in a secure environment. This feature automates complex analytical queries that were previously hard to answer solely through model reasoning. Use this capability to address a wide range of sophisticated use cases, such as data analysis, data visualization, and mathematical problem solving."
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 23,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 24,
        "cited_text": "Amazon Bedrock Generative AI Amazon Bedrock Agents Amazon Bedrock Agents Enable generative AI applications to automate multistep tasks by seamlessly connecting with company systems, APIs, and data sources What is Amazon Bedrock Agents? Amazon Bedrock Agents uses the reasoning of foundation models (FMs), APIs, and data to break down user requests, gathers relevant information, and efficiently completes tasks—freeing teams to focus on high-value work. Building an agent is straightforward and fast, with setup in just a few steps. Agents now includes memory retention for seamless task continuity and Amazon Bedrock Guardrails for built-in security and reliability. For more advanced needs, Amazon Bedrock supports multi-agent collaboration, allowing multiple specialized agents to work together on complex business challenges."
      },
      {
        "source_id": "f71e0184-ceb9-46da-913f-35250c96dc34",
        "citation_number": 25,
        "cited_text": "Middleware Overview Prebuilt middleware Custom middleware Frontend Overview Patterns Integrations Advanced usage Guardrails Runtime Context engineering Model Context Protocol (MCP) Human-in-the-loop Multi-agent Retrieval Long-term memory Agent development LangSmith Studio Test Agent Chat UI Deploy with LangSmith Deployment Observability On this page Create an agent Core benefits LangChain overview Copy page LangChain is an open source framework with a prebuilt agent architecture and integrations for any model or tool—so you can build agents that adapt as fast as the ecosystem evolves"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「Parallelization（并行）」与「Orchestrator-Workers（协调者-工作者）」是构建高效 AI Agent 系统的两种进阶架构模式，其实现细节涉及任务拆解逻辑、动态调度算法及针对大规模处理的性能优化策略。\n\n### 1. 核心算法流程\n\n#### **Parallelization (并行模式)**\n并行化通过同时运行多个模型实例来降低延迟或提高结果的可信度，主要包含两种算法逻辑：\n*   **分段逻辑 (Sectioning)**：将大任务拆分为独立的子任务并行执行。例如，在处理用户请求时，一个实例生成回答，另一个实例同步执行**安全护栏 (Guardrails)** 检查 [1, 2]。\n*   **投票逻辑 (Voting)**：对同一任务运行多次（使用不同提示词或参数），通过**采样与投票 (Sampling-and-voting)** 算法（如 **Agent Forest**）合并结果 [1, 3]。研究显示，LLM 的性能随并行智能体数量的增加而提升，且与任务难度正相关 [3]。\n\n#### **Orchestrator-Workers (协调者-工作者模式)**\n该模式的核心在于**动态分工**，流程如下：\n1.  **任务分解 (Breakdown)**：中央协调者 LLM 接收复杂输入，根据需求动态决定所需的子任务 [4]。\n2.  **动态委派 (Delegation)**：协调者将任务分配给专业工作者（Specialized Workers）。其灵活性体现在子任务并非预定义，而是实时生成的（例如根据代码修改任务动态决定涉及的文件数量）[4, 5]。\n3.  **结果综合 (Synthesis)**：协调者收集所有工作者的输出，并将其合成最终响应 [4]。\n\n### 2. 关键代码架构\n\n各主流框架对这两种模式提供了不同的架构实现：\n*   **LangGraph**：采用基于图的低层次编排，受 **Pregel 和 Apache Beam** 启发。它支持**持久化 (Persistence)** 和**中断恢复 (Durable execution)**，允许在并行任务失败时从断点重新开始 [6-8]。\n*   **CrewAI**：通过 **Crews**（自主角色协作）和 **Flows**（事件驱动控制）实现。其架构支持通过 `@start`、`@listen` 和 `@router` 等装饰器实现条件分支和并行触发逻辑（如 `or_` 和 `and_` 操作符） [9, 10]。\n*   **Amazon Bedrock Agents**：提供**多智能体协作 (Multi-agent collaboration)** 架构，由一个主管智能体（Supervisor Agent）负责任务分解和对专业智能体的协调 [11]。\n\n### 3. 性能优化策略\n\n为应对并行化带来的成本和延迟压力，系统通常采用以下策略：\n*   **提示词缓存 (Prompt Caching)**：\n    *   **效果**：降低延迟 **>2 倍**，对于重复任务成本降低高达 **90%** [12]。\n    *   **参数**：最小缓存阈值为 **1,024**（Sonnet）或 **4,096**（Opus）tokens。缓存 TTL 默认为 **5 分钟**，提供 **1 小时** TTL 选项（需 2 倍基础价格） [13]。\n*   **批量处理 (Batch Processing)**：\n    *   **效果**：成本降低 **50%**，大幅提升吞吐量 [14, 15]。\n    *   **限制**：单个批次上限为 **100,000 条请求** 或 **256 MB** [16]。\n*   **超长输出支持**：在批处理模式下，通过特定 beta 标头可将单次生成的 `max_tokens` 限制提升至 **300,000 tokens** [17]。\n\n### 4. 竞品技术对比与参数\n\n| 指标 | CrewAI | LangGraph | AutoGen |\n| :--- | :--- | :--- | :--- |\n| **核心理念** | 角色驱动与协同智能 [9] | 低层次状态机/图编排 [6] | 层级化设计 (Core/AgentChat) [18] |\n| **性能表现** | 在 QA 任务中执行速度比 LangGraph 快 **5.76 倍** [19] | 侧重长时运行的弹性与持久化 [7] | 侧重多智能体对话，但缺乏原生“过程”概念 [19] |\n| **易用性** | 支持 YAML 配置和精简 Python 代码 [20, 21] | 需要较多样板代码和复杂状态管理 [22] | 提供 AutoGen Studio 免代码 GUI [23, 24] |\n| **灵活性** | 高，支持 Crew 与 Flow 混合编排 [10] | 极高，完全控制状态转移路径 [25] | 较高，支持跨语言 (.NET/Python) [18] |\n\n**数据总结**：在处理大规模并行任务时，采用 **Message Batches API** 可节省一半成本 [15]，而通过 **Prompt Caching** 配合 **Automatic Caching** 机制，可使多轮对话中近 **100%** 的输入 token 实现缓存读取 [26]，显著优化了 Orchestrator 与 Workers 之间高频交互的效率。",
    "conversation_id": "c20d4856-4d53-4d6c-9c16-9b0f8c2f5238",
    "sources_used": [
      "f50c5498-80ef-498e-b316-77915c2391a1",
      "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
      "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "c877cdef-fbbf-470c-9a87-fed63356dc22",
      "48e31493-8f04-4ad6-a03c-e4ec9040a9bd"
    ],
    "citations": {
      "1": "f50c5498-80ef-498e-b316-77915c2391a1",
      "2": "f50c5498-80ef-498e-b316-77915c2391a1",
      "3": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
      "4": "f50c5498-80ef-498e-b316-77915c2391a1",
      "5": "f50c5498-80ef-498e-b316-77915c2391a1",
      "6": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "7": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "8": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "9": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "10": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "11": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "12": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "13": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "14": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "15": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "16": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "17": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "18": "c877cdef-fbbf-470c-9a87-fed63356dc22",
      "19": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "20": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "21": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "22": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "23": "c877cdef-fbbf-470c-9a87-fed63356dc22",
      "24": "c877cdef-fbbf-470c-9a87-fed63356dc22",
      "25": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
      "26": "6231d975-9d20-48b0-aa77-26ea25afbd9d"
    },
    "references": [
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 1,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 2,
        "cited_text": "Examples where parallelization is useful: Sectioning : Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response. Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model's performance on a given prompt. Voting : Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem. Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives."
      },
      {
        "source_id": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
        "citation_number": 3,
        "cited_text": "arXiv:2402.05120 (cs) [Submitted on 3 Feb 2024 ( v1 ), last revised 11 Oct 2024 (this version, v2)] Title: More Agents Is All You Need Authors: Junyou Li , Qin Zhang , Yangbin Yu , Qiang Fu , Deheng Ye View a PDF of the paper titled More Agents Is All You Need, by Junyou Li and 4 other authors View PDF HTML (experimental) Abstract: We find that, simply via a sampling-and-voting method, the performance of large language models (LLMs) scales with the number of agents instantiated. Also, this method, termed as Agent Forest, is orthogonal to existing complicated methods to further enhance LLMs, while the degree of enhancement is correlated to the task difficulty. We conduct comprehensive experiments on a wide range of LLM benchmarks to verify the presence of our finding, and to study the properties that can facilitate its occurrence. Our code is publicly available at: this https URL"
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 4,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 5,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 6,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. If you're looking to quickly build agents with LangChain's create_agent (built on LangGraph), check out the LangChain Agents documentation ."
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 7,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 8,
        "cited_text": "Acknowledgements LangGraph is inspired by Pregel and Apache Beam . The public interface draws inspiration from NetworkX . LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain. About Build resilient language agents as graphs. docs.langchain.com/oss/python/langgraph/ Topics python open-source enterprise framework ai gemini openai multiagent agents ai-agents rag pydantic llm generative-ai chatgpt langchain langgraph deepagents Resources Readme License MIT license Code of conduct"
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 9,
        "cited_text": "CrewAI Crews : Optimize for autonomy and collaborative intelligence. CrewAI Flows : The enterprise and production architecture for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively With over 100,000 developers certified through our community courses at learn.crewai.com , CrewAI is rapidly becoming the standard for enterprise-ready AI automation. CrewAI AMP Suite CrewAI AMP Suite is a comprehensive bundle tailored for organizations that require secure, scalable, and easy-to-manage agent-driven automation."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 10,
        "cited_text": "Using Crews and Flows Together CrewAI's power truly shines when combining Crews with Flows to create sophisticated automation pipelines. CrewAI flows support logical operators like or_ and and_ to combine multiple conditions. This can be used with @start , @listen , or @router decorators to create complex triggering conditions. or_ : Triggers when any of the specified conditions are met. and_ Triggers when all of the specified conditions are met. Here's how you can orchestrate multiple Crews within a Flow:"
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 11,
        "cited_text": "End of dialog window. Features Multi-agent collaboration Retrieval augmented generation Orchestrate and execute Memory retention Code interpretation Multi-agent collaboration Amazon Bedrock multi-agent collaboration allows developers to build, deploy, and manage multiple specialized agents seamlessly working together to address increasingly complex business workflows. Each agent focuses on specific tasks under the coordination of a supervisor agent, which breaks down intricate processes into manageable steps to ensure precision and reliability. By automating these complex operational processes, businesses can free their teams from operational burdens, allowing them to focus on innovation and deliver real business value."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 12,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 13,
        "cited_text": "Start with automatic caching. It covers the majority of use cases with minimal effort. Switch to explicit breakpoints only when you need fine-grained control. Key details ¶ Minimum cacheable length: 1,024 tokens for Sonnet; 4,096 tokens for Opus and Haiku 4.5 Cache TTL: 5 minutes by default (refreshed on each hit). A 1-hour TTL is available at 2x base input price. Pricing: Cache writes cost 1.25x base input price. Cache reads cost 0.1x base input price. Breakpoint limit: Up to 4 explicit breakpoints per request. Automatic caching uses one slot."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 14,
        "cited_text": "You need to process large volumes of data Immediate responses are not required You want to optimize for cost efficiency You're running large-scale evaluations or analyses The Message Batches API is Anthropic's first implementation of this pattern. This feature is not eligible for Zero Data Retention (ZDR) . Data is retained according to the feature's standard retention policy. Message Batches API The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 15,
        "cited_text": "Pricing The Batches API offers significant cost savings. All usage is charged at 50% of the standard API prices. <cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Model",
              "Batch input",
              "Batch output"
            ],
            [
              "Claude Opus 4.6",
              "$2.50 / MTok",
              "$12.50 / MTok"
            ],
            [
              "Claude Opus 4.5",
              "$2.50 / MTok",
              "$12.50 / MTok"
            ],
            [
              "Claude Opus 4.1",
              "$7.50 / MTok",
              "$37.50 / MTok"
            ],
            [
              "Claude Opus 4",
              "$7.50 / MTok",
              "$37.50 / MTok"
            ],
            [
              "Claude Sonnet 4.6",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Sonnet 4.5",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Sonnet 4",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Sonnet 3.7 (",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Haiku 4.5",
              "$0.50 / MTok",
              "$2.50 / MTok"
            ],
            [
              "Claude Haiku 3.5",
              "$0.40 / MTok",
              "$2 / MTok"
            ],
            [
              "Claude Opus 3 (",
              "$7.50 / MTok",
              "$37.50 / MTok"
            ],
            [
              "Claude Haiku 3",
              "$0.125 / MTok",
              "$0.625 / MTok"
            ]
          ]
        }
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 16,
        "cited_text": "Large-scale evaluations: Process thousands of test cases efficiently. Content moderation: Analyze large volumes of user-generated content asynchronously. Data analysis: Generate insights or summaries for large datasets. Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries). Batch limitations A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first. The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours. Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download. Batches are scoped to a Workspace . You may view all batches (and their results) that were created within the Workspace that your API key belongs to. Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See Message Batches API rate limits . Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours. Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured spend limit ."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 17,
        "cited_text": "Extended output (beta) The output-300k-2026-03-24 beta header raises the max_tokens cap to 300,000 for batch requests using Claude Opus 4.6 or Claude Sonnet 4.6. Include the header to generate outputs far longer than the standard limit (64k to 128k depending on model) in a single turn. Extended output is available on the Message Batches API only, not the synchronous Messages API. It is supported on the Claude API and is not available on Amazon Bedrock, Vertex AI, or Microsoft Foundry. Use extended output for long-form generation such as book-length drafts and technical documentation, exhaustive structured data extraction, large code-generation scaffolds, and long reasoning chains."
      },
      {
        "source_id": "c877cdef-fbbf-470c-9a87-fed63356dc22",
        "citation_number": 18,
        "cited_text": "Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components. Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 19,
        "cited_text": "P.S. CrewAI demonstrates significant performance advantages over LangGraph, executing 5.76x faster in certain cases like this QA task example ( see comparison) while achieving higher evaluation scores with faster completion times in certain coding tasks, like in this example ( detailed analysis). Autogen : While Autogen excels at creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows. ChatDev : ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 20,
        "cited_text": "2. Setting Up Your Crew with the YAML Configuration To create a new CrewAI project, run the following CLI (Command Line Interface) command: This command creates a new project folder with the following structure: You can now start developing your crew by editing the files in the src/my_project folder. The main.py file is the entry point of the project, the crew.py file is where you define your crew, the agents.yaml file is where you define your agents, and the tasks.yaml file is where you define your tasks."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 21,
        "cited_text": "To customize your project, you can: Modify src/my_project/config/agents.yaml to define your agents. Modify src/my_project/config/tasks.yaml to define your tasks. Modify src/my_project/crew.py to add your own logic, tools, and specific arguments. Modify src/my_project/main.py to add custom inputs for your agents and tasks. Add your environment variables into the .env file. Example of a simple crew with a sequential process: Instantiate your crew: Modify the files as needed to fit your use case:"
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 22,
        "cited_text": "Please refer to the Connect CrewAI to LLMs page for details on configuring your agents' connections to models. How CrewAI Compares CrewAI's Advantage : CrewAI combines autonomous agent intelligence with precise workflow control through its unique Crews and Flows architecture. The framework excels at both high-level orchestration and low-level customization, enabling complex, production-grade systems with granular control. LangGraph : While LangGraph provides a foundation for building agent workflows, its approach requires significant boilerplate code and complex state management patterns. The framework's tight coupling with LangChain can limit flexibility when implementing custom agent behaviors or integrating with external systems."
      },
      {
        "source_id": "c877cdef-fbbf-470c-9a87-fed63356dc22",
        "citation_number": 23,
        "cited_text": "Warning : Only connect to trusted MCP servers as they may execute commands in your local environment or expose sensitive information. Multi-Agent Orchestration You can use AgentTool to create a basic multi-agent orchestration setup. For more advanced multi-agent orchestrations and workflows, read AgentChat documentation . AutoGen Studio Use AutoGen Studio to prototype and run multi-agent workflows without writing code. Caution : AutoGen Studio is meant to help you rapidly prototype multi-agent workflows and demonstrate an example of end user interfaces built with AutoGen. It is not meant to be a production-ready app . Developers are encouraged to use the AutoGen framework to build their own applications, implementing authentication, security and other features required for deployed applications. See the security note for more details."
      },
      {
        "source_id": "c877cdef-fbbf-470c-9a87-fed63356dc22",
        "citation_number": 24,
        "cited_text": "The ecosystem also supports two essential developer tools : AutoGen Studio provides a no-code GUI for building multi-agent applications. AutoGen Bench provides a benchmarking suite for evaluating agent performance. You can use the AutoGen framework and developer tools to create applications for your domain. For example, Magentic-One is a state-of-the-art multi-agent team built using AgentChat API and Extensions API that can handle a variety of tasks that require web browsing, code execution, and file handling."
      },
      {
        "source_id": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
        "citation_number": 25,
        "cited_text": "Copy page Trusted by companies shaping the future of agents— including Klarna, Uber, J.P. Morgan, and more— LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents. LangGraph is very low-level, and focused entirely on agent orchestration . Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with models and tools . We will commonly use LangChain components throughout the documentation to integrate models and tools, but you don't need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain's agents that provide prebuilt architectures for common LLM and tool-calling loops. LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 26,
        "cited_text": "<cited_table> In [8]: After the first turn, nearly 100% of input tokens are read from cache on every subsequent turn. The conversation code is just a plain list of messages — no special cache_control markers needed on individual blocks. Example 3: Explicit cache breakpoints ¶ For more control, you can place cache_control directly on individual content blocks. This is useful when:",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Request",
              "Cache behavior"
            ],
            [
              "Request 1",
              "System + User:A cached (write)"
            ],
            [
              "Request 2",
              "System + User:A read from cache; Asst:B + User:C written to cache"
            ],
            [
              "Request 3",
              "System through User:C read from cache; Asst:D + User:E written to cache"
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
    "answer": "基于提供的来源，以下是关于「Parallelization（并行）」与「Orchestrator-Workers（协调者-工作者）」架构的真实应用场景、工业级方案、性能数据及最佳实践的详细分析。\n\n### 1. 真实应用场景与案例\n\n#### **并行模式 (Parallelization)**\n该模式适用于任务可独立拆解或需要多重验证的场景：\n*   **安全护栏 (Guardrails)**：在处理用户查询时，一个模型实例生成响应，另一个实例同步筛查不当内容。这种并行处理比单一调用处理所有任务性能更好 [1, 2]。\n*   **代码审计与漏洞扫描**：采用 **Voting（投票）** 逻辑，通过多个不同的提示词（Prompts）运行同一任务，如果多个实例都标记了某个漏洞，则提高置信度 [2]。\n*   **自动化评估 (Evals)**：在评估 LLM 性能时，让多个并行调用分别评估模型输出的不同维度 [2]。\n*   **大规模内容处理**：利用 **Batch Processing** 并行处理数千个测试用例、审核海量用户生成内容或为大数据集生成摘要 [3, 4]。\n\n#### **协调者-工作者模式 (Orchestrator-Workers)**\n该模式适用于子任务无法预测、需要动态决策的复杂流程：\n*   **自主编程 (Coding Agents)**：处理如 **SWE-bench** 任务，协调者根据需求动态决定修改哪些文件、修改多少个文件，并委派 Worker 执行具体编辑 [5-7]。\n*   **复杂搜索与调研**：协调者判断是否需要多轮搜索，指挥 Worker 从不同来源搜集、分析信息，并由协调者汇总 [5, 8]。\n*   **客户服务与事务处理**：协调者接收复杂请求（如退款），调用 Worker 查询历史记录、验证政策并执行 API 操作 [9, 10]。\n\n### 2. 工业级部署方案与开源实战\n\n*   **Amazon Bedrock Agents**：提供多智能体协作架构，由主管智能体（Supervisor Agent）协调多个专业智能体。内置记忆持久化、安全护栏和代码解释器，适合企业级规模化部署 [9, 11-13]。\n*   **CrewAI AMP Suite**：针对企业级自动化提供的套件，包含**控制平面 (Control Plane)**、实时可观测性（Tracing & Observability）以及支持本地/云端部署的安全方案 [14-16]。\n*   **LangGraph**：基于图的编排框架，支持**持久化 (Persistence)** 和**中断恢复 (Durable execution)**，能够处理运行时间极长的状态化 Agent 任务 [17-19]。\n*   **OpenAI Responses API**：取代了 Assistants API，通过「Prompts」和「Conversations」的概念简化了编排逻辑，支持 Deep Research 和工具调用循环的显式管理 [20-22]。\n\n### 3. 性能基准数据\n\n*   **成本优化**：\n    *   **Message Batches API**：异步处理请求可降低 **50%** 的成本 [23, 24]。\n    *   **Prompt Caching（提示词缓存）**：对于重复性任务，成本最高可降低 **90%** [25]。\n*   **延迟与效率**：\n    *   **缓存加速**：提示词缓存可将延迟降低 **>2 倍** [25]。\n    *   **多轮对话**：在多轮对话中使用自动缓存，首轮之后的输入 Token 缓存命中率接近 **100%** [26]。\n    *   **执行速度**：CrewAI 在某些 QA 任务中表现出比 LangGraph 快 **5.76 倍** 的速度 [27]。\n*   **可扩展性**：\n    *   **Agent Forest**：研究表明 LLM 的性能会随着实例化的智能体数量增加而扩展，且增强程度与任务难度正相关 [28]。\n\n### 4. 开发者最佳实践\n\n*   **保持简洁 (Simplicity)**：从简单的提示词开始，只有在简单方案失效时才增加并行或编排的复杂性 [29, 30]。\n*   **优先考虑透明度**：在设计时应显式展示 Agent 的规划步骤，便于调试和用户信任 [30]。\n*   **优化 Agent-Computer Interface (ACI)**：\n    *   像为初级开发人员编写文档一样详细地描述工具接口 [31, 32]。\n    *   **Poka-yoke（防错设计）**：通过更改参数设计使模型难以出错（例如：强制要求绝对路径而非相对路径） [32, 33]。\n*   **缓存策略**：在批量处理时，为每个请求包含相同的 `cache_control` 块，以最大化缓存命中率（命中率通常在 30%-98% 之间） [34, 35]。\n\n### 5. 常见踩坑经验\n\n*   **过度抽象**：使用复杂的框架可能导致底层提示词和响应被掩盖，增加调试难度。建议直接使用 API 或深入理解框架底层代码 [30, 36]。\n*   **工具格式陷阱**：避免让 LLM 编写复杂的格式，例如在 JSON 中转义代码，这会增加模型负担。应选择模型在互联网数据中自然见到的格式 [31, 37]。\n*   **缺乏环境反馈**：Agent 在执行每一步时必须获取环境的“地面真理（Ground Truth）”（如工具调用结果），否则错误会迅速累积 [6, 8]。\n*   **批处理顺序误区**：批量处理的结果返回顺序与输入不一定一致，开发者**必须使用 `custom_id`** 来匹配请求和响应，而不是依赖列表顺序 [38, 39]。",
    "conversation_id": "c20d4856-4d53-4d6c-9c16-9b0f8c2f5238",
    "sources_used": [
      "f50c5498-80ef-498e-b316-77915c2391a1",
      "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
      "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1"
    ],
    "citations": {
      "1": "f50c5498-80ef-498e-b316-77915c2391a1",
      "2": "f50c5498-80ef-498e-b316-77915c2391a1",
      "3": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "4": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "5": "f50c5498-80ef-498e-b316-77915c2391a1",
      "6": "f50c5498-80ef-498e-b316-77915c2391a1",
      "7": "f50c5498-80ef-498e-b316-77915c2391a1",
      "8": "f50c5498-80ef-498e-b316-77915c2391a1",
      "9": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "10": "f50c5498-80ef-498e-b316-77915c2391a1",
      "11": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "12": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "13": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
      "14": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "15": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "16": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "17": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "18": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "19": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
      "20": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "21": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "22": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "23": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "24": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "25": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "26": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "27": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "28": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
      "29": "f50c5498-80ef-498e-b316-77915c2391a1",
      "30": "f50c5498-80ef-498e-b316-77915c2391a1",
      "31": "f50c5498-80ef-498e-b316-77915c2391a1",
      "32": "f50c5498-80ef-498e-b316-77915c2391a1",
      "33": "f50c5498-80ef-498e-b316-77915c2391a1",
      "34": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "35": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "36": "f50c5498-80ef-498e-b316-77915c2391a1",
      "37": "f50c5498-80ef-498e-b316-77915c2391a1",
      "38": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "39": "6e752a1e-fc64-412c-bc11-e6bb1794244f"
    },
    "references": [
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 1,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 2,
        "cited_text": "Examples where parallelization is useful: Sectioning : Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response. Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model's performance on a given prompt. Voting : Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem. Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 3,
        "cited_text": "You can explore the API reference directly , in addition to this guide. How the Message Batches API works When you send a request to the Message Batches API: The system creates a new Message Batch with the provided Messages requests. The batch is then processed asynchronously, with each request handled independently. You can poll for the status of the batch and retrieve results when processing has ended for all requests. This is especially useful for bulk operations that don't require immediate results, such as:"
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 4,
        "cited_text": "Large-scale evaluations: Process thousands of test cases efficiently. Content moderation: Analyze large volumes of user-generated content asynchronously. Data analysis: Generate insights or summaries for large datasets. Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries). Batch limitations A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first. The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours. Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download. Batches are scoped to a Workspace . You may view all batches (and their results) that were created within the Workspace that your API key belongs to. Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See Message Batches API rate limits . Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours. Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured spend limit ."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 5,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 6,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 7,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 8,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 9,
        "cited_text": "Retrieval augmented generation Agents securely connects to your company's data sources and augments the user requests with the right information to generate an accurate response. For example, if the user asks about claims eligibility, the RAG agent will look up information from the knowledge base and reconcile between the submitted claims and the eligibility policy response: “You need to turn in your driver's license, pictures of the damaged car, and an accident report.” Orchestrate and execute Customers can create an agent in Amazon Bedrock in just a few quick steps, accelerating the time it takes to build generative AI applications. Customers first select a model and write a few instructions in natural language. For example, “you are an inventory management agent that determines product availability in the inventory system.” Agents orchestrates and analyzes the task and breaks it down into the correct logical sequence using the FM's reasoning abilities. Agents automatically calls the necessary APIs to transact with the company systems and processes to fulfill the request, determining along the way if they can proceed or if they need to gather more information."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 10,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 11,
        "cited_text": "Amazon Bedrock Generative AI Amazon Bedrock Agents Amazon Bedrock Agents Enable generative AI applications to automate multistep tasks by seamlessly connecting with company systems, APIs, and data sources What is Amazon Bedrock Agents? Amazon Bedrock Agents uses the reasoning of foundation models (FMs), APIs, and data to break down user requests, gathers relevant information, and efficiently completes tasks—freeing teams to focus on high-value work. Building an agent is straightforward and fast, with setup in just a few steps. Agents now includes memory retention for seamless task continuity and Amazon Bedrock Guardrails for built-in security and reliability. For more advanced needs, Amazon Bedrock supports multi-agent collaboration, allowing multiple specialized agents to work together on complex business challenges."
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 12,
        "cited_text": "End of dialog window. Features Multi-agent collaboration Retrieval augmented generation Orchestrate and execute Memory retention Code interpretation Multi-agent collaboration Amazon Bedrock multi-agent collaboration allows developers to build, deploy, and manage multiple specialized agents seamlessly working together to address increasingly complex business workflows. Each agent focuses on specific tasks under the coordination of a supervisor agent, which breaks down intricate processes into manageable steps to ensure precision and reliability. By automating these complex operational processes, businesses can free their teams from operational burdens, allowing them to focus on innovation and deliver real business value."
      },
      {
        "source_id": "c953db1b-12c2-4a28-afbe-7b9324f70aef",
        "citation_number": 13,
        "cited_text": "Memory retention Agents has the ability to retain memory across interactions, offering more personalized and seamless user experiences. This feature allows an agent to remember historical interactions and improves the accuracy of multistep tasks. Users benefit from improved recommendations and recall of prior context when required, ensuring a more cohesive and efficient interaction with the agent. Code interpretation Agents supports the ability to dynamically generate and execute code in a secure environment. This feature automates complex analytical queries that were previously hard to answer solely through model reasoning. Use this capability to address a wide range of sophisticated use cases, such as data analysis, data visualization, and mathematical problem solving."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 14,
        "cited_text": "CrewAI Crews : Optimize for autonomy and collaborative intelligence. CrewAI Flows : The enterprise and production architecture for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively With over 100,000 developers certified through our community courses at learn.crewai.com , CrewAI is rapidly becoming the standard for enterprise-ready AI automation. CrewAI AMP Suite CrewAI AMP Suite is a comprehensive bundle tailored for organizations that require secure, scalable, and easy-to-manage agent-driven automation."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 15,
        "cited_text": "You can try one part of the suite the Crew Control Plane for free Crew Control Plane Key Features: Tracing & Observability : Monitor and track your AI agents and workflows in real-time, including metrics, logs, and traces. Unified Control Plane : A centralized platform for managing, monitoring, and scaling your AI agents and workflows. Seamless Integrations : Easily connect with existing enterprise systems, data sources, and cloud infrastructure. Advanced Security : Built-in robust security and compliance measures ensuring safe deployment and management. Actionable Insights : Real-time analytics and reporting to optimize performance and decision-making. 24/7 Support : Dedicated enterprise support to ensure uninterrupted operation and quick resolution of issues. On-premise and Cloud Deployment Options : Deploy CrewAI AMP on-premise or in the cloud, depending on your security and compliance requirements."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 16,
        "cited_text": "Q: How can I contribute to CrewAI? A: Contributions are warmly welcomed! Fork the repository, create your branch, implement your changes, and submit a pull request. See the Contribution section of the README for detailed guidelines. Q: What additional features does CrewAI AMP offer? A: CrewAI AMP provides advanced features such as a unified control plane, real-time observability, secure integrations, advanced security, actionable insights, and dedicated 24/7 enterprise support. Q: Is CrewAI AMP available for cloud and on-premise deployments?"
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 17,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. If you're looking to quickly build agents with LangChain's create_agent (built on LangGraph), check out the LangChain Agents documentation ."
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 18,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
        "citation_number": 19,
        "cited_text": "Install pip uv Then, create a simple hello world example: Use LangSmith to trace requests, debug agent behavior, and evaluate outputs. Set LANGSMITH_TRACING=true and your API key to get started. Core benefits LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits: Durable execution : Build agents that persist through failures and can run for extended periods, resuming from where they left off. Human-in-the-loop : Incorporate human oversight by inspecting and modifying agent state at any point. Comprehensive memory : Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions. Debugging with LangSmith : Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment : Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
        "citation_number": 20,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
        "citation_number": 21,
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
        "source_id": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
        "citation_number": 22,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 23,
        "cited_text": "You need to process large volumes of data Immediate responses are not required You want to optimize for cost efficiency You're running large-scale evaluations or analyses The Message Batches API is Anthropic's first implementation of this pattern. This feature is not eligible for Zero Data Retention (ZDR) . Data is retained according to the feature's standard retention policy. Message Batches API The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 24,
        "cited_text": "Pricing The Batches API offers significant cost savings. All usage is charged at 50% of the standard API prices. <cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Model",
              "Batch input",
              "Batch output"
            ],
            [
              "Claude Opus 4.6",
              "$2.50 / MTok",
              "$12.50 / MTok"
            ],
            [
              "Claude Opus 4.5",
              "$2.50 / MTok",
              "$12.50 / MTok"
            ],
            [
              "Claude Opus 4.1",
              "$7.50 / MTok",
              "$37.50 / MTok"
            ],
            [
              "Claude Opus 4",
              "$7.50 / MTok",
              "$37.50 / MTok"
            ],
            [
              "Claude Sonnet 4.6",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Sonnet 4.5",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Sonnet 4",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Sonnet 3.7 (",
              "$1.50 / MTok",
              "$7.50 / MTok"
            ],
            [
              "Claude Haiku 4.5",
              "$0.50 / MTok",
              "$2.50 / MTok"
            ],
            [
              "Claude Haiku 3.5",
              "$0.40 / MTok",
              "$2 / MTok"
            ],
            [
              "Claude Opus 3 (",
              "$7.50 / MTok",
              "$37.50 / MTok"
            ],
            [
              "Claude Haiku 3",
              "$0.125 / MTok",
              "$0.625 / MTok"
            ]
          ]
        }
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 25,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 26,
        "cited_text": "<cited_table> In [8]: After the first turn, nearly 100% of input tokens are read from cache on every subsequent turn. The conversation code is just a plain list of messages — no special cache_control markers needed on individual blocks. Example 3: Explicit cache breakpoints ¶ For more control, you can place cache_control directly on individual content blocks. This is useful when:",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Request",
              "Cache behavior"
            ],
            [
              "Request 1",
              "System + User:A cached (write)"
            ],
            [
              "Request 2",
              "System + User:A read from cache; Asst:B + User:C written to cache"
            ],
            [
              "Request 3",
              "System through User:C read from cache; Asst:D + User:E written to cache"
            ]
          ]
        }
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 27,
        "cited_text": "P.S. CrewAI demonstrates significant performance advantages over LangGraph, executing 5.76x faster in certain cases like this QA task example ( see comparison) while achieving higher evaluation scores with faster completion times in certain coding tasks, like in this example ( detailed analysis). Autogen : While Autogen excels at creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows. ChatDev : ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications."
      },
      {
        "source_id": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
        "citation_number": 28,
        "cited_text": "arXiv:2402.05120 (cs) [Submitted on 3 Feb 2024 ( v1 ), last revised 11 Oct 2024 (this version, v2)] Title: More Agents Is All You Need Authors: Junyou Li , Qin Zhang , Yangbin Yu , Qiang Fu , Deheng Ye View a PDF of the paper titled More Agents Is All You Need, by Junyou Li and 4 other authors View PDF HTML (experimental) Abstract: We find that, simply via a sampling-and-voting method, the performance of large language models (LLMs) scales with the number of agents instantiated. Also, this method, termed as Agent Forest, is orthogonal to existing complicated methods to further enhance LLMs, while the degree of enhancement is correlated to the task difficulty. We conduct comprehensive experiments on a wide range of LLM benchmarks to verify the presence of our finding, and to study the properties that can facilitate its occurrence. Our code is publicly available at: this https URL"
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 29,
        "cited_text": "Combining and customizing these patterns These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity only when it demonstrably improves outcomes. Summary Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 30,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 31,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 32,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 33,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 34,
        "cited_text": "Shell The response will show the batch in a canceling state: JSON Using prompt caching with Message Batches The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, since batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 35,
        "cited_text": "To maximize the likelihood of cache hits in your batch requests: Include identical cache_control blocks in every Message request within your batch Maintain a steady stream of requests to prevent cache entries from expiring after their 5-minute lifetime Structure your requests to share as much cached content as possible Example of implementing prompt caching in a batch: Shell In this example, both requests in the batch include identical system messages and the full text of Pride and Prejudice marked with cache_control to increase the likelihood of cache hits."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 36,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 37,
        "cited_text": "There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 38,
        "cited_text": ".jsonl file If your result has an error, its result.error will be set to the standard error shape . Batch results may not match input order Batch results can be returned in any order, and may not match the ordering of requests when the batch was created. In the above example, the result for the second batch request is returned before the first. To correctly match results with their corresponding requests, always use the custom_id field. Canceling a Message Batch You can cancel a Message Batch that is currently processing using the cancel endpoint . Immediately after cancellation, a batch's processing_status will be canceling . You can use the same polling technique described above to wait until cancellation is finalized. Canceled batches end up with a status of ended and may contain partial results for requests that were processed before cancellation."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 39,
        "cited_text": "A single 300k-token generation can take over an hour to complete, so plan your batch submissions with the 24-hour processing window in mind. Standard batch pricing (50% of standard API prices) applies. Shell Best practices for effective batching To get the most out of the Batches API: Monitor batch processing status regularly and implement appropriate retry logic for failed requests. Use meaningful custom_id values to easily match results with requests, since order is not guaranteed. Consider breaking very large datasets into multiple batches for better manageability. Dry run a single request shape with the Messages API to avoid validation errors."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「Parallelization（并行）」与「Orchestrator-Workers（协调者-工作者）」领域，2025-2026年的技术格局正经历从“静态工作流”向“动态自主系统”的重大范式转移。以下是基于最新来源的深度解析：\n\n### 1. 重要研究突破与论文 (2024-2026)\n\n*   **智能体规模效应 (Scaling Law of Agents)**：\n    *   **核心发现**：研究论文《More Agents Is All You Need》(2024) 提出，LLM 的性能可以通过简单的“采样与投票”方法，随实例化的智能体数量增加而线性扩展 [1]。\n    *   **关键机制：Agent Forest（智能体森林）**：该研究证明了增加并行智能体数量对复杂任务的增强程度与任务难度呈正相关 [1]。这种方法与现有的复杂增强方法正交，提供了性能提升的新维度。\n*   **长程推理演进 (Evolution of Reasoning)**：\n    *   **技术趋势**：2025-2026年，模型开始集成“扩展思维（Extended Thinking）”和“自适应思维（Adaptive Thinking）” [2]。例如，Claude 4.6 等模型支持在生成前进行长达一小时的内部推理链 [3]。\n\n### 2. 核心技术趋势 (2025-2026)\n\n*   **API 范式转型：从 Assistants 到 Responses**：\n    *   OpenAI 已宣布弃用 Assistants API（将于2026年8月关闭），全面转向 **Responses API** [4]。\n    *   **转变核心**：从“持久化服务器端对象”转向“更简单的输入/输出项”，并将**编排逻辑（Orchestration）**（如工具循环、历史剪枝）交还给应用代码，以换取更高的灵活性和实时兼容性 [5, 6]。\n*   **低层编排架构的成熟**：\n    *   **图控架构 (LangGraph)**：受 Pregel 和 Apache Beam 启发，侧重于构建具有**持久性（Persistence）**和**中断恢复（Durable execution）**能力的 stateful 智能体 [7, 8]。\n    *   **事件驱动流 (CrewAI Flows)**：CrewAI 引入了 `Crews`（自主性）与 `Flows`（精确控制）的协同架构，支持 `or_` 和 `and_` 等逻辑操作符进行复杂触发 [9, 10]。\n*   **极长文本输出突破**：\n    *   **Extended Output (Beta)**：通过特定标头，并行批处理任务现在支持单次生成高达 **300,000 tokens** 的超长内容（如整本书的草稿或大规模代码脚手架） [11]。\n\n### 3. 性能优化与经济性指标\n\n*   **提示词缓存 (Prompt Caching)**：已成为标准配置，可减少 **>2x** 的延迟并降低高达 **90%** 的成本 [12]。系统支持自动缓存和显式断点（最多 4 个） [13, 14]。\n*   **批量处理 (Message Batches API)**：支持在大规模并行评估中将成本降低 **50%**，单次批处理上限达 **10万个请求** [15, 16]。\n*   **执行速度基准**：在特定 QA 任务中，优化后的多智能体框架（如 CrewAI）执行速度可比传统框架快 **5.76倍** [17]。\n\n### 4. 未解决的挑战\n\n*   **错误累积与复合风险**：自主智能体在多轮操作中面临**复合错误（Compounding Errors）**的风险，每一步的细微偏差可能导致最终结果完全偏离 [18]。\n*   **透明度与抽象层之争**：复杂框架虽然简化了入门，但往往会掩盖底层的 Prompt 和响应，导致在生产环境中**难以调试** [19, 20]。\n*   **环境真理性获取**：智能体在执行每一步时，如何从物理或软件环境中实时获取准确的“地面真理（Ground Truth）”以修正计划，仍是核心难点 [21]。\n\n### 5. 未来可能的突破点\n\n*   **ACI（智能体-计算机接口）标准化**：通过 **Model Context Protocol (MCP)** 等协议实现工具集、API 和数据源的即插即用，类似于 HCI（人机交互）对计算普及的推动作用 [22, 23]。\n*   **Human-in-the-loop (HITL) 的深度集成**：不再是简单的确认，而是支持在长程运行中随时对智能体状态进行“时间旅行（Time Travel）”式的检查与修改 [8, 24]。\n*   **自修复推理循环 (Evaluator-Optimizer)**：一种闭环模式，其中一个 LLM 生成响应，另一个 LLM 提供反馈并在循环中进行迭代修正，模仿人类的润色过程 [25]。",
    "conversation_id": "c20d4856-4d53-4d6c-9c16-9b0f8c2f5238",
    "sources_used": [
      "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
      "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "f50c5498-80ef-498e-b316-77915c2391a1",
      "48e31493-8f04-4ad6-a03c-e4ec9040a9bd"
    ],
    "citations": {
      "1": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
      "2": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "3": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "4": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "5": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "6": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
      "7": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "8": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
      "9": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "10": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "11": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "12": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "13": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "14": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
      "15": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "16": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
      "17": "cb4cda73-8778-475b-950b-ac5be119f2a6",
      "18": "f50c5498-80ef-498e-b316-77915c2391a1",
      "19": "f50c5498-80ef-498e-b316-77915c2391a1",
      "20": "f50c5498-80ef-498e-b316-77915c2391a1",
      "21": "f50c5498-80ef-498e-b316-77915c2391a1",
      "22": "f50c5498-80ef-498e-b316-77915c2391a1",
      "23": "f50c5498-80ef-498e-b316-77915c2391a1",
      "24": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
      "25": "f50c5498-80ef-498e-b316-77915c2391a1"
    },
    "references": [
      {
        "source_id": "8e228bdf-7d1f-4f00-a177-fa0d9d0fd1b1",
        "citation_number": 1,
        "cited_text": "arXiv:2402.05120 (cs) [Submitted on 3 Feb 2024 ( v1 ), last revised 11 Oct 2024 (this version, v2)] Title: More Agents Is All You Need Authors: Junyou Li , Qin Zhang , Yangbin Yu , Qiang Fu , Deheng Ye View a PDF of the paper titled More Agents Is All You Need, by Junyou Li and 4 other authors View PDF HTML (experimental) Abstract: We find that, simply via a sampling-and-voting method, the performance of large language models (LLMs) scales with the number of agents instantiated. Also, this method, termed as Agent Forest, is orthogonal to existing complicated methods to further enhance LLMs, while the degree of enhancement is correlated to the task difficulty. We conduct comprehensive experiments on a wide range of LLM benchmarks to verify the presence of our finding, and to study the properties that can facilitate its occurrence. Our code is publicly available at: this https URL"
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 2,
        "cited_text": "Batch processing - Claude API Docs Loading... Developer Guide API Reference MCP Resources Release Notes English Log in Search... ⌘K First steps Intro to Claude Quickstart Models & pricing Models overview Choosing a model What's new in Claude 4.6 Migration guide Model deprecations Pricing Build with Claude Features overview Using the Messages API Handling stop reasons Prompting best practices Model capabilities Extended thinking Adaptive thinking Effort Fast mode (beta: research preview) Structured outputs Citations Streaming Messages Batch processing PDF support Search results Multilingual support Embeddings Vision"
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 3,
        "cited_text": "A single 300k-token generation can take over an hour to complete, so plan your batch submissions with the 24-hour processing window in mind. Standard batch pricing (50% of standard API prices) applies. Shell Best practices for effective batching To get the most out of the Batches API: Monitor batch processing status regularly and implement appropriate retry logic for failed requests. Use meaningful custom_id values to easily match results with requests, since order is not guaranteed. Consider breaking very large datasets into multiple batches for better manageability. Dry run a single request shape with the Messages API to avoid validation errors."
      },
      {
        "source_id": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
        "citation_number": 4,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
        "citation_number": 5,
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
        "source_id": "507c30e0-dd04-4b09-9487-bc6f6e1ce6a7",
        "citation_number": 6,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 7,
        "cited_text": "GitHub - langchain-ai/langgraph: Build resilient language agents as graphs. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "8a82cd74-9212-43e5-8cf9-d150b9c38f34",
        "citation_number": 8,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 9,
        "cited_text": "CrewAI Crews : Optimize for autonomy and collaborative intelligence. CrewAI Flows : The enterprise and production architecture for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively With over 100,000 developers certified through our community courses at learn.crewai.com , CrewAI is rapidly becoming the standard for enterprise-ready AI automation. CrewAI AMP Suite CrewAI AMP Suite is a comprehensive bundle tailored for organizations that require secure, scalable, and easy-to-manage agent-driven automation."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 10,
        "cited_text": "Using Crews and Flows Together CrewAI's power truly shines when combining Crews with Flows to create sophisticated automation pipelines. CrewAI flows support logical operators like or_ and and_ to combine multiple conditions. This can be used with @start , @listen , or @router decorators to create complex triggering conditions. or_ : Triggers when any of the specified conditions are met. and_ Triggers when all of the specified conditions are met. Here's how you can orchestrate multiple Crews within a Flow:"
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 11,
        "cited_text": "Extended output (beta) The output-300k-2026-03-24 beta header raises the max_tokens cap to 300,000 for batch requests using Claude Opus 4.6 or Claude Sonnet 4.6. Include the header to generate outputs far longer than the standard limit (64k to 128k depending on model) in a single turn. Extended output is available on the Message Batches API only, not the synchronous Messages API. It is supported on the Claude API and is not available on Amazon Bedrock, Vertex AI, or Microsoft Foundry. Use extended output for long-form generation such as book-length drafts and technical documentation, exhaustive structured data extraction, large code-generation scaffolds, and long reasoning chains."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 12,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 13,
        "cited_text": "You want to cache different sections with different TTLs You need to cache a system prompt independently from message content You want fine-grained control over what gets cached You can also combine both approaches: use explicit breakpoints for your system prompt while automatic caching handles the conversation. Below, we place cache_control directly on the book content block and manually move the breakpoint forward on each turn. In [9]: Choosing an approach ¶ <cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "",
              "Automatic caching",
              "Explicit breakpoints"
            ],
            [
              "Ease of use",
              "One-line change",
              "Must place and move"
            ],
            [
              "Multi-turn",
              "Breakpoint moves forward automatically",
              "You manage breakpoint placement"
            ],
            [
              "Fine-grained control",
              "No",
              "Up to 4 independent breakpoints"
            ],
            [
              "Mixed TTLs",
              "Single TTL for auto breakpoint",
              "Different TTLs per breakpoint"
            ],
            [
              "Combinable",
              "Yes — automatic + explicit together",
              "Yes"
            ]
          ]
        }
      },
      {
        "source_id": "6231d975-9d20-48b0-aa77-26ea25afbd9d",
        "citation_number": 14,
        "cited_text": "Start with automatic caching. It covers the majority of use cases with minimal effort. Switch to explicit breakpoints only when you need fine-grained control. Key details ¶ Minimum cacheable length: 1,024 tokens for Sonnet; 4,096 tokens for Opus and Haiku 4.5 Cache TTL: 5 minutes by default (refreshed on each hit). A 1-hour TTL is available at 2x base input price. Pricing: Cache writes cost 1.25x base input price. Cache reads cost 0.1x base input price. Breakpoint limit: Up to 4 explicit breakpoints per request. Automatic caching uses one slot."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 15,
        "cited_text": "You need to process large volumes of data Immediate responses are not required You want to optimize for cost efficiency You're running large-scale evaluations or analyses The Message Batches API is Anthropic's first implementation of this pattern. This feature is not eligible for Zero Data Retention (ZDR) . Data is retained according to the feature's standard retention policy. Message Batches API The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput."
      },
      {
        "source_id": "6e752a1e-fc64-412c-bc11-e6bb1794244f",
        "citation_number": 16,
        "cited_text": "Large-scale evaluations: Process thousands of test cases efficiently. Content moderation: Analyze large volumes of user-generated content asynchronously. Data analysis: Generate insights or summaries for large datasets. Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries). Batch limitations A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first. The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours. Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download. Batches are scoped to a Workspace . You may view all batches (and their results) that were created within the Workspace that your API key belongs to. Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See Message Batches API rate limits . Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours. Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured spend limit ."
      },
      {
        "source_id": "cb4cda73-8778-475b-950b-ac5be119f2a6",
        "citation_number": 17,
        "cited_text": "P.S. CrewAI demonstrates significant performance advantages over LangGraph, executing 5.76x faster in certain cases like this QA task example ( see comparison) while achieving higher evaluation scores with faster completion times in certain coding tasks, like in this example ( detailed analysis). Autogen : While Autogen excels at creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows. ChatDev : ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 18,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 19,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 20,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 21,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 22,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 23,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "48e31493-8f04-4ad6-a03c-e4ec9040a9bd",
        "citation_number": 24,
        "cited_text": "Persistence Durable execution Streaming Interrupts Time travel Memory Subgraphs Production Application structure Test LangSmith Studio Agent Chat UI LangSmith Deployment LangSmith Observability Frontend Overview Graph execution LangGraph APIs Graph API Functional API Runtime On this page Install Core benefits LangGraph ecosystem Acknowledgements LangGraph overview Copy page Gain control with LangGraph to design agents that reliably handle complex tasks"
      },
      {
        "source_id": "f50c5498-80ef-498e-b316-77915c2391a1",
        "citation_number": 25,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      }
    ]
  }
}
