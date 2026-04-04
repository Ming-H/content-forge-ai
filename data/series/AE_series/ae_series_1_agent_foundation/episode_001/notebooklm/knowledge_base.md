# 知识库：Agent Engineering 全景：从 Chatbot 到自主智能体的范式转变

生成时间: 2026-04-03 08:53
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "根据提供的来源，Agent Engineering 的全景展示了从简单 Chatbot 到自主智能体（Autonomous Agents）的深刻范式转变。其核心架构已从单一的“提示-响应”模式演变为高度复杂、具备自我迭代和环境交互能力的**智能体系统** [1, 2]。\n\n以下是核心技术架构和关键组件的概述：\n\n### 1. 技术演进路线\n智能体工程的演进经历了从“无状态对话”到“有状态自主操作”的过程：\n*   **零样本 LLM (Zero-shot LLM)**：早期的 Chatbot 主要以单次 pass 模式运行，不支持修正，类似于要求人类一口气写完文章而不允许回退 [2]。\n*   **增强型 LLM (Augmented LLM)**：在 LLM 基础上集成**检索（RAG）、工具（Tools）和记忆（Memory）**，使其能主动生成查询、选择工具并决定保留哪些信息 [3]。\n*   **代理流/工作流 (Workflows)**：通过预定义的代码路径编排 LLM 和工具，追求任务的**可预测性和一致性** [4, 5]。\n*   **自主智能体 (Autonomous Agents)**：模型能够根据任务目标**动态指导**自身流程和工具使用，在环境中通过反馈循环（Agent Loop）独立运行 [4, 6, 7]。\n*   **多智能体协作 (Multi-agent Collaboration)**：多个智能体通过角色扮演、任务拆分、讨论和辩论来解决单智能体难以处理的复杂任务 [8-10]。\n\n### 2. 核心算法与设计模式名称\n根据 Andrew Ng 和 Anthropic 的总结，核心模式包括：\n*   **反思 (Reflection)**：LLM 检查自身工作并寻找改进方法 [8]。\n*   **规划 (Planning)**：智能体制定并执行多步计划以实现目标（如撰写大纲、调研、初稿、修订） [8, 11]。\n*   **提示词链 (Prompt Chaining)**：将任务分解为序列步骤，每一步处理上一步的输出，并可加入程序化检查 [12]。\n*   **路由 (Routing)**：对输入进行分类，并将其导向专门的下游任务或特定模型（如将简单问题导向 Haiku，复杂问题导向 Sonnet） [13, 14]。\n*   **并行化 (Parallelization)**：包括**分段 (Sectioning)**（并行运行独立子任务）和**投票 (Voting)**（多次运行同一任务以获得更高置信度的输出） [15]。\n*   **编排器-工人 (Orchestrator-workers)**：中心 LLM 动态拆解任务并分发给工人 LLM，最后综合结果 [16]。\n*   **评估器-优化器 (Evaluator-optimizer)**：一个 LLM 生成响应，另一个提供反馈，在循环中不断改进 [17]。\n\n### 3. 主要架构模式\n*   **智能体循环 (Agent Loop)**：这是自主智能体的核心。智能体决定调用工具，执行后将结果返回给 LLM，如此循环直到任务完成 [7, 18, 19]。\n*   **智能体-计算机接口 (ACI, Agent-Computer Interface)**：专门为智能体设计的环境接口（如 SWE-agent），显著提升了智能体导航仓库、编辑代码和执行测试的能力 [20]。\n*   **从 Threads 到 Conversations**：OpenAI 的架构演进中，将仅存储消息的 Thread 替换为存储**消息、工具调用、工具输出**等多种数据项（Items）的 Conversation 对象 [21, 22]。\n*   **分层设计 (Layered Design)**：如 AutoGen 的架构，分为 Core API（事件驱动的底层通信）、AgentChat API（高级模式编排）和 Extensions API（功能扩展） [23, 24]。\n\n### 4. 关键技术指标\n*   **Pass@1 准确率**：在 HumanEval 或 SWE-bench 等基准测试上的表现。例如，在 Agent 循环包裹下的 GPT-3.5 准确率可从 48.1% 提升至 95.1% [19, 20]。\n*   **延迟 (Latency)**：智能体系统通常通过牺牲延迟和成本来换取更高的性能，特别是在多轮交互中 [4, 25]。\n*   **成本效率 (Cost Optimization)**：包括 Token 消耗管理（如 Prompt Caching、批处理 Batch）以及根据任务复杂降级使用小模型的策略 [14, 26, 27]。\n*   **安全性与防御 (Safety & Guardrails)**：针对提示词注入（Prompt Injection）的分类器防御、沙箱隔离环境（如 Docker/VM）以及人类在环（Human-in-the-loop）的确认机制 [25, 28-30]。\n*   **透明度 (Transparency)**：是否能够明确展示智能体的规划步骤和中间思维过程 [31]。",
    "conversation_id": "c94ba068-f426-48eb-9569-cc9a0af35cc2",
    "sources_used": [
      "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "6176a1b8-0474-4827-be67-b6301d4a008b",
      "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "b0d9e504-25f3-44f1-a768-fbe9b7d63724"
    ],
    "citations": {
      "1": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "2": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "3": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "4": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "5": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "6": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "7": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "8": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "9": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "10": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "11": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "12": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "13": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "14": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "15": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "16": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "17": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "18": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "19": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "20": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "21": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "22": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "23": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "24": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "25": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "26": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "27": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "28": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "29": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "30": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "31": "8cf581f7-6f33-4b8b-8200-3056fa939a92"
    },
    "references": [
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 1,
        "cited_text": "In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents. What are agents? \"Agent\" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems , but draw an important architectural distinction between workflows and agents :"
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 2,
        "cited_text": "Today, we mostly use LLMs in zero-shot mode, prompting a model to generate final output token by token without revising its work. This is akin to asking someone to compose an essay from start to finish, typing straight through with no backspacing allowed, and expecting a high-quality result. Despite the difficulty, LLMs do amazingly well at this task! With an agent workflow, however, we can ask the LLM to iterate over a document many times. For example, it might take a sequence of steps such as:"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 3,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 4,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 5,
        "cited_text": "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough. When and how to use frameworks There are many frameworks that make agentic systems easier to implement, including: The Claude Agent SDK ; Strands Agents SDK by AWS ; Rivet , a drag and drop GUI LLM workflow builder; and Vellum , another GUI tool for building and testing complex workflows."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 6,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 7,
        "cited_text": "4 Claude continues calling computer use tools until it's completed the task Claude analyzes the tool results to determine if more tool use is needed or the task has been completed. If Claude decides it needs another tool, it responds with another  tool_use   stop_reason  and you should return to step 3. Otherwise, it crafts a text response to the user. The repetition of steps 3 and 4 without user input is referred to as the \"agent loop\" (that is, Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request)."
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 8,
        "cited_text": "Reflection: The LLM examines its own work to come up with ways to improve it. Tool Use: The LLM is given tools such as web search, code execution, or any other function to help it gather information, take action, or process data. Planning: The LLM comes up with, and executes, a multistep plan to achieve a goal (for example, writing an outline for an essay, then doing online research, then writing a draft, and so on). Multi-agent collaboration: More than one AI agent work together, splitting up tasks and discussing and debating ideas, to come up with better solutions than a single agent would."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 9,
        "cited_text": "CrewAI offers two powerful, complementary approaches that work seamlessly together to build sophisticated AI applications: Crews : Teams of AI agents with true autonomy and agency, working together to accomplish complex tasks through role-based collaboration. Crews enable: Natural, autonomous decision-making between agents Dynamic task delegation and collaboration Specialized roles with defined goals and expertise Flexible problem-solving approaches Flows : Production-ready, event-driven workflows that deliver precise control over complex automations. Flows provide:"
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 10,
        "cited_text": "Warning : Only connect to trusted MCP servers as they may execute commands in your local environment or expose sensitive information. Multi-Agent Orchestration You can use  AgentTool  to create a basic multi-agent orchestration setup. import   asyncio   from   autogen_agentchat . agents   import   AssistantAgent   from   autogen_agentchat . tools   import   AgentTool   from   autogen_agentchat . ui   import   Console   from   autogen_ext . models . openai   import   OpenAIChatCompletionClient   async   def   main ()  ->   None :  model_client   =   OpenAIChatCompletionClient ( model = \"gpt-4.1\" )  math_agent   =   AssistantAgent (  \"math_expert\" ,  model_client = model_client ,  system_message = \"You are a math expert.\" ,  description = \"A math expert assistant.\" ,  model_client_stream = True , )  math_agent_tool   =   AgentTool ( math_agent ,  return_value_as_last_message = True )  chemistry_agent   =   AssistantAgent (  \"chemistry_expert\" ,  model_client = model_client ,  system_message = \"You are a chemistry expert.\" ,  description = \"A chemistry expert assistant.\" ,  model_client_stream = True , )  chemistry_agent_tool   =   AgentTool ( chemistry_agent ,  return_value_as_last_message = True )  agent   =   AssistantAgent (  \"assistant\" ,  system_message = \"You are a general assistant. Use expert tools when needed.\" ,  model_client = model_client ,  model_client_stream = True ,  tools = [ math_agent_tool ,  chemistry_agent_tool ],  max_tool_iterations = 10 , )  await   Console ( agent . run_stream ( task = \"What is the integral of x^2?\" ))  await   Console ( agent . run_stream ( task = \"What is the molecular weight of water?\" ))  asyncio . run ( main ())"
      },
      {
        "source_id": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
        "citation_number": 11,
        "cited_text": "Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangGraph ecosystem While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with: Deep Agents (new!) – Build agents that can plan, use subagents, and leverage file systems for complex tasks. LangChain – Provides integrations and composable components to streamline LLM application development. LangSmith – Helpful for agent evals and observability. Debug poor-performing LLM app runs, evaluate agent trajectories, gain visibility in production, and improve performance over time. LangSmith Deployment – Deploy and scale agents effortlessly with a purpose-built deployment platform for long-running, stateful workflows. Discover, reuse, configure, and share agents across teams – and iterate quickly with visual prototyping in LangSmith Studio ."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 12,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 13,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 14,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 15,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 16,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 17,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 18,
        "cited_text": "Start with the reference implementation A reference implementation is available that includes everything you need to get started quickly with computer use: A containerized environment suitable for computer use with Claude Implementations of the computer use tools An agent loop that interacts with the Claude API and executes the computer use tools A web interface to interact with the container, agent loop, and tools. Understanding the agentic loop The core of computer use is the \"agent loop\" - a cycle where Claude requests tool actions, your application executes them, and returns results to Claude. Here's a simplified example:"
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 19,
        "cited_text": "GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%. Open source agent tools and the academic literature on agents are proliferating, making this an exciting time but also a confusing one. To help put this work into perspective, I’d like to share a framework for categorizing design patterns for building agents. My team AI Fund is successfully using these patterns in many applications, and I hope you find them useful."
      },
      {
        "source_id": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
        "citation_number": 20,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2405.15793 Help | Advanced Search Computer Science > Software Engineering arXiv:2405.15793 (cs)   [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.  Comments:   Code, data, and demo available at this https URL Subjects:   Software Engineering (cs.SE) ; Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Human-Computer Interaction (cs.HC); Machine Learning (cs.LG)   Cite as: arXiv:2405.15793 [cs.SE]   (or arXiv:2405.15793v3 [cs.SE]  for this version) https://doi.org/10.48550/arXiv.2405.15793 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 21,
        "cited_text": "Events Meetups Hackathon Support Forum Discord API Dashboard Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We’re moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back  previous_response_id ."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 22,
        "cited_text": "A thread was a collection of messages stored server-side. Threads could only store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data. Request example Thread object 1  2  3  4  thread = openai.beta.threads.create(   messages=[{ \"role\" :  \"user\" ,  \"content\" :  \"what are the 5 Ds of dodgeball?\" }],   metadata={ \"user_id\" :  \"peter_le_fleur\" },  ) Conversation object 1  2  3  4  conversation = openai.conversations.create(   items=[{ \"role\" :  \"user\" ,  \"content\" :  \"what are the 5 Ds of dodgeball?\" }],   metadata={ \"user_id\" :  \"peter_le_fleur\" },  )"
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 23,
        "cited_text": "#  Run AutoGen Studio on http://localhost:8080  autogenstudio ui --port 8080 --appdir ./my-app Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components."
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 24,
        "cited_text": "Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 25,
        "cited_text": "Follow implementation best practices Understand computer use limitations The computer use functionality is in beta. While Claude's capabilities are cutting edge, developers should be aware of its limitations: Latency : the current computer use latency for human-AI interactions may be too slow compared to regular human-directed computer actions. Focus on use cases where speed isn't critical (for example, background information gathering, automated software testing) in trusted environments. Computer vision accuracy and reliability : Claude may make mistakes or hallucinate when outputting specific coordinates while generating actions. Claude Sonnet 3.7 introduces the thinking capability that can help you understand the model's reasoning and identify potential issues. Tool selection accuracy and reliability : Claude may make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability may be lower when interacting with niche applications or multiple applications at once. Prompt the model carefully when requesting complex tasks. Scrolling reliability : Claude Sonnet 3.7 introduced dedicated scroll actions with direction control that improves reliability. The model can now explicitly scroll in any direction (up/down/left/right) by a specified amount. Spreadsheet interaction : Mouse clicks for spreadsheet interaction have improved in Claude Sonnet 3.7 with the addition of more precise mouse control actions like  left_mouse_down ,  left_mouse_up , and new modifier key support. Cell selection can be more reliable by using these fine-grained controls and combining modifier keys with clicks. Account creation and content generation on social and communications platforms : While Claude will visit websites, Claude's ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms is limited. This capability may be updated in the future. Vulnerabilities : Vulnerabilities like jailbreaking or prompt injection may persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even in conflict with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. Consider the following: a. Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges b. Avoiding giving computer use access to sensitive accounts or data without strict oversight c. Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications Inappropriate or illegal actions : Per Anthropic's terms of service, you must not employ computer use to violate any laws or the Acceptable Use Policy."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 26,
        "cited_text": "Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 27,
        "cited_text": "Because your application controls where and how computer use data is stored, computer use is ZDR eligible. For ZDR eligibility across all features, see API and data retention . Pricing Computer use follows the standard tool use pricing . When using the computer use tool: System prompt overhead : The computer use beta adds 466-499 tokens to the system prompt Computer use tool token usage : Model Input tokens per tool definition Claude 4.x models 735 tokens Claude Sonnet 3.7 ( deprecated ) 735 tokens Additional token consumption :"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 28,
        "cited_text": "Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents. Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft. Limiting internet access to an allowlist of domains to reduce exposure to malicious content. Asking a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 29,
        "cited_text": "In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. Take precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection. The model has been trained to resist these prompt injections, and an extra layer of defense has been added. If you use the computer use tools, classifiers will automatically run on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, please contact support ."
      },
      {
        "source_id": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
        "citation_number": 30,
        "cited_text": "Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 31,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「Agent Engineering 全景」揭示了从静态对话（Chatbot）向动态、有状态、且具备环境交互能力的**自主智能体（Autonomous Agents）**的重大范式转变 [1, 2]。这种转变的核心在于从“单次提示词响应”转向“持续的、闭环的推理与行动” [3]。\n\n以下是基于来源的实现细节解析：\n\n### 1. 核心算法流程\n智能体的运作不再依赖于单一的 LLM 调用，而是由**智能体循环（Agent Loop）**驱动，主要包含以下模式：\n*   **智能体循环（Agent Loop）**：LLM 评估用户需求，决定调用工具，提取输入并在沙箱中执行，随后将结果（如截图、控制台输出）返回给 LLM。此过程循环往复，直至任务完成或达到最大迭代限制（如 10 次）以控制成本 [4, 5]。\n*   **规划与反思（Planning & Reflection）**：\n    *   **规划**：模型制定多步计划（如撰写大纲、调研、起草），并根据环境反馈动态调整 [6, 7]。\n    *   **反思**：LLM 检查自身工作并寻找改进点。例如，在代码生成中，通过运行测试并根据报错信息迭代 [7, 8]。\n*   **五大工作流模式**：\n    1.  **提示词链（Chaining）**：将任务分解为序列，每步处理上一步的输出 [9]。\n    2.  **路由（Routing）**：根据输入类别将其引导至专门的下游任务或特定模型 [10, 11]。\n    3.  **并行化（Parallelization）**：分为分段运行（Sectioning）和多次投票（Voting） [12]。\n    4.  **编排器-工人（Orchestrator-Workers）**：中心 LLM 动态拆解任务并分发给工人，最后进行汇总 [13]。\n    5.  **评估器-优化器（Evaluator-Optimizer）**：通过反馈循环不断精炼输出结果 [14]。\n\n### 2. 关键代码架构\n架构层面的演进体现在数据模型和环境接口的优化：\n*   **从 Threads 到 Conversations**：OpenAI 弃用了仅能存储消息的 Threads API，转向 **Conversations API**。新架构支持存储**消息、工具调用、工具输出**等多种类型的“Item”对象，增强了灵活性 [15, 16]。\n*   **智能体-计算机接口（ACI）**：这是自主智能体的关键组件（如 SWE-agent），通过为智能体定制的 Shell、编辑器和文件查找工具，提升其在代码库中的操作效率 [17]。\n*   **分层设计（Layered Design）**：\n    *   **Core API**：实现消息传递、事件驱动和分布式运行 [18]。\n    *   **AgentChat API**：提供更简单的、意见明确的 API，用于快速原型设计和多智能体模式 [18]。\n    *   **Extensions API**：允许扩展 LLM 客户端和执行能力 [18]。\n*   **Crews 与 Flows**：CrewAI 区分了**Crews（具备自主决策权的代理团队）**和 **Flows（基于事件的、精确控制的工作流）**，允许开发者平衡自主性与生产环境的可预测性 [19, 20]。\n\n### 3. 性能优化策略\n*   **推理性能（Pass@1）**：通过智能体循环封装，即使是 GPT-3.5，其 HumanEval 基准表现也能从 48.1% 提升至 **95.1%** [21]。\n*   **延迟与成本优化**：\n    *   **提示词缓存（Prompt Caching）**：减少重复指令的计算成本 [22, 23]。\n    *   **路由分流**：将简单任务分配给 Claude Haiku 等廉价模型，复杂任务分配给 Sonnet 或 Opus [11]。\n    *   **批处理（Batch）**：针对非实时任务降低成本 [24]。\n*   **精确度优化**：使用 ACI 代替标准控制台。例如，SWE-agent 要求智能体使用绝对路径而非相对路径，以解决其在移动目录后出现的定位错误 [17, 25]。\n\n### 4. 竞品技术对比\n| 特性 | CrewAI | LangGraph | AutoGen |\n| :--- | :--- | :--- | :--- |\n| **底层依赖** | 独立框架，不依赖 LangChain [26, 27] | 深度耦合 LangChain 生态 [28] | 微软主导，支持多语言 [18] |\n| **执行速度** | 特定 QA 任务中比 LangGraph **快 5.76 倍** [29] | 包含较多样板代码，相对较慢 [20] | 灵活，但大规模任务编排复杂 [29] |\n| **控制机制** | **Crews + Flows**（平衡自主与精确） [20] | 基于图的低级编排，需复杂状态管理 [20] | 主要是会话代理协作，缺乏原生“流程”概念 [29] |\n| **适用场景** | 生产级多智能体自动化 [26] | 长期运行的有状态、复杂工作流 [30] | 快速原型设计、多代理对话 [18] |\n\n### 5. 具体技术参数\n*   **SWE-agent 表现**：在 SWE-bench 上达到 **12.5%** 的 pass@1 率，远超非交互式 LM [17]。\n*   **计算机使用（Computer Use）成本**：\n    *   系统提示词额外消耗：466-499 token [31]。\n    *   每个工具定义的输入成本：**735 token** [31]。\n*   **坐标转换**：由于 API 会对截图进行缩放（最大 1568 像素），架构中必须包含坐标缩放因子计算（Scale Factor），以确保智能体点击的准确性 [32, 33]。",
    "conversation_id": "c94ba068-f426-48eb-9569-cc9a0af35cc2",
    "sources_used": [
      "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "6176a1b8-0474-4827-be67-b6301d4a008b",
      "0280f766-e8bf-4c6f-980d-03c5782fbdb2"
    ],
    "citations": {
      "1": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "2": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "3": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "4": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "5": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "6": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "7": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "8": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "9": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "10": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "11": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "12": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "13": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "14": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "15": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "16": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "17": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "18": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "19": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "20": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "21": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "22": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "23": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "24": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "25": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "26": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "27": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "28": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "29": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "30": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "31": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "32": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "33": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9"
    },
    "references": [
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 1,
        "cited_text": "In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents. What are agents? \"Agent\" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems , but draw an important architectural distinction between workflows and agents :"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 2,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 3,
        "cited_text": "Today, we mostly use LLMs in zero-shot mode, prompting a model to generate final output token by token without revising its work. This is akin to asking someone to compose an essay from start to finish, typing straight through with no backspacing allowed, and expecting a high-quality result. Despite the difficulty, LLMs do amazingly well at this task! With an agent workflow, however, we can ask the LLM to iterate over a document many times. For example, it might take a sequence of steps such as:"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 4,
        "cited_text": "4 Claude continues calling computer use tools until it's completed the task Claude analyzes the tool results to determine if more tool use is needed or the task has been completed. If Claude decides it needs another tool, it responds with another  tool_use   stop_reason  and you should return to step 3. Otherwise, it crafts a text response to the user. The repetition of steps 3 and 4 without user input is referred to as the \"agent loop\" (that is, Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request)."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 5,
        "cited_text": "async  def  sampling_loop (    * ,    model :  str ,    messages : list[ dict ],    api_key :  str ,    max_tokens :  int  =  4096 ,    tool_version :  str ,    thinking_budget :  int  |  None  =  None ,    max_iterations :  int  =  10 ,  # Add iteration limit to prevent infinite loops   ):    \"\"\"    A simple agent loop for Claude computer use interactions.    This function handles the back-and-forth between:    1. Sending user messages to Claude    2. Claude requesting to use tools    3. Your app executing those tools    4. Sending tool results back to Claude    \"\"\"    # Set up tools and API parameters    client  =  Anthropic( api_key = api_key)    beta_flag  =  (    \"computer-use-2025-11-24\"    if  \"20251124\"  in  tool_version    else  \"computer-use-2025-01-24\"    )    text_editor_type  =  (    \"text_editor_20250728\"    if  \"20251124\"  in  tool_version    else  f \"text_editor_ { tool_version } \"    )    # Configure tools - you should already have these initialized elsewhere    tools  =  [    {    \"type\" :  f \"computer_ { tool_version } \" ,    \"name\" :  \"computer\" ,    \"display_width_px\" :  1024 ,    \"display_height_px\" :  768 ,    },    { \"type\" : text_editor_type,  \"name\" :  \"str_replace_based_edit_tool\" },    { \"type\" :  \"bash_20250124\" ,  \"name\" :  \"bash\" },    ]    # Main agent loop (with iteration limit to prevent runaway API costs)    iterations  =  0    while  True  and  iterations  <  max_iterations:    iterations  +=  1    # Set up optional thinking parameter (for Claude Sonnet 3.7)    thinking  =  None    if  thinking_budget:    thinking  =  { \"type\" :  \"enabled\" ,  \"budget_tokens\" : thinking_budget}    # Call the Claude API    response  =  client.beta.messages.create(    model = model,    max_tokens = max_tokens,    messages = messages,    tools = tools,    betas = [beta_flag],    thinking = thinking,    )    # Add Claude's response to the conversation history    response_content  =  response.content    messages.append({ \"role\" :  \"assistant\" ,  \"content\" : response_content})    # Check if Claude used any tools    tool_results  =  []    for  block  in  response_content:    if  block.type  ==  \"tool_use\" :    # In a real app, you would execute the tool here    # For example: result = run_tool(block.name, block.input)    result  =  { \"result\" :  \"Tool executed successfully\" }    # Format the result for Claude    tool_results.append(    { \"type\" :  \"tool_result\" ,  \"tool_use_id\" : block.id,  \"content\" : result}    )    # If no tools were used, Claude is done - return the final messages    if  not  tool_results:    return  messages    # Add tool results to messages for the next iteration with Claude    messages.append({ \"role\" :  \"user\" ,  \"content\" : tool_results})"
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 6,
        "cited_text": "Plan an outline. Decide what, if any, web searches are needed to gather more information. Write a first draft. Read over the first draft to spot unjustified arguments or extraneous information. Revise the draft taking into account any weaknesses spotted. And so on. This iterative process is critical for most human writers to write good text. With AI, such an iterative workflow yields much better results than writing in a single pass. Devin ’s splashy demo recently received a lot of social media buzz. My team has been closely following the evolution of AI that writes code. We analyzed results from a number of research teams, focusing on an algorithm’s ability to do well on the widely used HumanEval coding benchmark. You can see our findings in the diagram below."
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 7,
        "cited_text": "Reflection: The LLM examines its own work to come up with ways to improve it. Tool Use: The LLM is given tools such as web search, code execution, or any other function to help it gather information, take action, or process data. Planning: The LLM comes up with, and executes, a multistep plan to achieve a goal (for example, writing an outline for an essay, then doing online research, then writing a draft, and so on). Multi-agent collaboration: More than one AI agent work together, splitting up tasks and discussing and debating ideas, to come up with better solutions than a single agent would."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 8,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 9,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 10,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 11,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 12,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 13,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 14,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 15,
        "cited_text": "Events Meetups Hackathon Support Forum Discord API Dashboard Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We’re moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back  previous_response_id ."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 16,
        "cited_text": "A thread was a collection of messages stored server-side. Threads could only store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data. Request example Thread object 1  2  3  4  thread = openai.beta.threads.create(   messages=[{ \"role\" :  \"user\" ,  \"content\" :  \"what are the 5 Ds of dodgeball?\" }],   metadata={ \"user_id\" :  \"peter_le_fleur\" },  ) Conversation object 1  2  3  4  conversation = openai.conversations.create(   items=[{ \"role\" :  \"user\" ,  \"content\" :  \"what are the 5 Ds of dodgeball?\" }],   metadata={ \"user_id\" :  \"peter_le_fleur\" },  )"
      },
      {
        "source_id": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
        "citation_number": 17,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2405.15793 Help | Advanced Search Computer Science > Software Engineering arXiv:2405.15793 (cs)   [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.  Comments:   Code, data, and demo available at this https URL Subjects:   Software Engineering (cs.SE) ; Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Human-Computer Interaction (cs.HC); Machine Learning (cs.LG)   Cite as: arXiv:2405.15793 [cs.SE]   (or arXiv:2405.15793v3 [cs.SE]  for this version) https://doi.org/10.48550/arXiv.2405.15793 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 18,
        "cited_text": "Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 19,
        "cited_text": "CrewAI offers two powerful, complementary approaches that work seamlessly together to build sophisticated AI applications: Crews : Teams of AI agents with true autonomy and agency, working together to accomplish complex tasks through role-based collaboration. Crews enable: Natural, autonomous decision-making between agents Dynamic task delegation and collaboration Specialized roles with defined goals and expertise Flexible problem-solving approaches Flows : Production-ready, event-driven workflows that deliver precise control over complex automations. Flows provide:"
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 20,
        "cited_text": "Please refer to the Connect CrewAI to LLMs page for details on configuring your agents' connections to models. How CrewAI Compares CrewAI's Advantage : CrewAI combines autonomous agent intelligence with precise workflow control through its unique Crews and Flows architecture. The framework excels at both high-level orchestration and low-level customization, enabling complex, production-grade systems with granular control. LangGraph : While LangGraph provides a foundation for building agent workflows, its approach requires significant boilerplate code and complex state management patterns. The framework's tight coupling with LangChain can limit flexibility when implementing custom agent behaviors or integrating with external systems."
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 21,
        "cited_text": "GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%. Open source agent tools and the academic literature on agents are proliferating, making this an exciting time but also a confusing one. To help put this work into perspective, I’d like to share a framework for categorizing design patterns for building agents. My team AI Fund is successfully using these patterns in many applications, and I hope you find them useful."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 22,
        "cited_text": "Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting"
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 23,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 24,
        "cited_text": "Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 25,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 26,
        "cited_text": "Homepage · Docs · Start Cloud Trial · Blog · Forum Fast and Flexible Multi-Agent Automation Framework CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks . It empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario. CrewAI Crews : Optimize for autonomy and collaborative intelligence. CrewAI Flows : The enterprise and production architecture for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively"
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 27,
        "cited_text": "Q: What exactly is CrewAI? A: CrewAI is a standalone, lean, and fast Python framework built specifically for orchestrating autonomous AI agents. Unlike frameworks like LangChain, CrewAI does not rely on external dependencies, making it leaner, faster, and simpler. Q: How do I install CrewAI? A: Install CrewAI using pip: uv pip install crewai For additional tools, use: uv pip install  ' crewai[tools] ' Q: Does CrewAI depend on LangChain? A: No. CrewAI is built entirely from the ground up, with no dependencies on LangChain or other agent frameworks. This ensures a lean, fast, and flexible experience."
      },
      {
        "source_id": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
        "citation_number": 28,
        "cited_text": "Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangGraph ecosystem While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with: Deep Agents (new!) – Build agents that can plan, use subagents, and leverage file systems for complex tasks. LangChain – Provides integrations and composable components to streamline LLM application development. LangSmith – Helpful for agent evals and observability. Debug poor-performing LLM app runs, evaluate agent trajectories, gain visibility in production, and improve performance over time. LangSmith Deployment – Deploy and scale agents effortlessly with a purpose-built deployment platform for long-running, stateful workflows. Discover, reuse, configure, and share agents across teams – and iterate quickly with visual prototyping in LangSmith Studio ."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 29,
        "cited_text": "P.S. CrewAI demonstrates significant performance advantages over LangGraph, executing 5.76x faster in certain cases like this QA task example ( see comparison ) while achieving higher evaluation scores with faster completion times in certain coding tasks, like in this example ( detailed analysis ). Autogen : While Autogen excels at creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows. ChatDev : ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications."
      },
      {
        "source_id": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
        "citation_number": 30,
        "cited_text": "Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. pip install -U langgraph If you're looking to quickly build agents with LangChain's  create_agent  (built on LangGraph), check out the LangChain Agents documentation . Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs ."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 31,
        "cited_text": "Because your application controls where and how computer use data is stored, computer use is ZDR eligible. For ZDR eligibility across all features, see API and data retention . Pricing Computer use follows the standard tool use pricing . When using the computer use tool: System prompt overhead : The computer use beta adds 466-499 tokens to the system prompt Computer use tool token usage : Model Input tokens per tool definition Claude 4.x models 735 tokens Claude Sonnet 3.7 ( deprecated ) 735 tokens Additional token consumption :"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 32,
        "cited_text": "Handle errors When implementing the computer use tool, various errors may occur. Here's how to handle them: Handle coordinate scaling for higher resolutions The API constrains images to a maximum of 1568 pixels on the longest edge and approximately 1.15 megapixels total (see image resizing for details). For example, a 1512x982 screen gets downsampled to approximately 1330x864. Claude analyzes this smaller image and returns coordinates in that space, but your tool executes clicks in the original screen space."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 33,
        "cited_text": "This can cause Claude's click coordinates to miss their targets unless you handle the coordinate transformation. To fix this, resize screenshots yourself and scale Claude's coordinates back up: import  math   def  get_scale_factor ( width ,  height ):    \"\"\"Calculate scale factor to meet API constraints.\"\"\"    long_edge  =  max (width, height)    total_pixels  =  width  *  height    long_edge_scale  =  1568  /  long_edge    total_pixels_scale  =  math.sqrt( 1_150_000  /  total_pixels)    return  min ( 1.0 , long_edge_scale, total_pixels_scale)   # When capturing screenshot   scale  =  get_scale_factor(screen_width, screen_height)   scaled_width  =  int (screen_width  *  scale)   scaled_height  =  int (screen_height  *  scale)   # Resize image to scaled dimensions before sending to Claude   screenshot  =  capture_and_resize(scaled_width, scaled_height)   # When handling Claude's coordinates, scale them back up   def  execute_click ( x ,  y ):    screen_x  =  x  /  scale    screen_y  =  y  /  scale    perform_click(screen_x, screen_y)"
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「Agent Engineering 全景」展现了从简单的无状态对话到具备自主规划、工具使用和自我迭代能力的智能体系统的跨越。以下是基于来源的真实应用场景、工业方案、性能数据及实践经验的详细列举：\n\n### 1. 真实应用场景与案例\n*   **客户支持（Customer Support）**：将聊天界面与工具集成，智能体可执行提取客户数据、查询订单历史、**自动办理退款**或更新工单等操作 [1, 2]。\n*   **编程智能体（Coding Agents）**：从简单的代码补全演进为自主解决问题。例如，智能体可以根据 GitHub 的 Issue 描述，自主导航仓库、编辑多个文件、运行测试并**解决真实的软件缺陷** [3-5]。\n*   **复杂搜索与调研**：在涉及多个来源的信息提取任务中，编排器（Orchestrator）智能体动态拆解任务，分发给工人智能体进行并发搜索和分析 [6, 7]。\n*   **桌面与 Web 自动化**：利用“计算机使用（Computer Use）”功能，智能体能像人类一样操作浏览器、填写表单、操作 Excel 等桌面软件，完成跨应用的端到端任务 [8, 9]。\n\n### 2. 工业级部署方案\n*   **OpenAI Responses API**：弃用了 Assistants API，转向更灵活的 **Responses API**。其工业架构核心在于将“Prompts”作为版本化的行为配置文件，并引入 **Conversations 对象**来存储消息、工具调用及其输出的完整流 [10-12]。\n*   **Anthropic 参考实现**：提供基于 **Docker 容器**的沙箱环境。该方案通过虚拟显示器（Xvfb）和轻量级 UI（Mutter）构建智能体操作环境，确保智能体在隔离的 Linux 环境中运行 Firefox 或 LibreOffice [13-15]。\n*   **CrewAI AMP Suite**：专为企业设计的方案，包含**统一控制平面（Unified Control Plane）**，提供实时可观测性、日志追踪和 24/7 企业级支持，支持云端及本地化部署 [16, 17]。\n*   **E2B Sandbox**：提供安全隔离的**云端沙箱基础设施**，专门用于运行智能体生成的代码，支持 JavaScript 和 Python SDK [18, 19]。\n\n### 3. 开源项目实战案例\n*   **SWE-agent**：由普林斯顿大学开发，引入了**智能体-计算机接口（ACI）**，使 LLM 能够通过专门设计的 Shell 和编辑器操作代码仓库 [20]。\n*   **CrewAI**：独立的 Python 框架，支持**角色扮演型多智能体协作**。它区分了具备自主权的 Crews（团队）和具备精确事件控制的 Flows（流） [21, 22]。\n*   **LangGraph**：由 LangChain 推出，用于构建**有状态的图结构智能体**，支持持久化存储、断点续传和人类在环（Human-in-the-loop）模式 [23, 24]。\n*   **AutoGen**：微软推出的框架，支持多智能体对话编排，具备分层设计，涵盖 Core API（分布式运行）和 AgentChat API（快速原型） [25-27]。\n\n### 4. 性能基准数据\n*   **HumanEval 编码基准**：\n    *   GPT-3.5（零样本）：48.1% 正确率。\n    *   **GPT-3.5（包裹在智能体循环中）**：正确率飙升至 **95.1%** [28]。\n*   **SWE-bench（软件工程基准）**：SWE-agent 的 **pass@1 成功率达到 12.5%**，远超传统的非交互式语言模型 [20]。\n*   **WebArena**：Claude 在该自主网页导航基准测试上取得了单智能体系统的 SOTA 结果 [8]。\n*   **执行速度**：在特定 QA 任务中，CrewAI 的执行速度比 LangGraph **快 5.76 倍** [29]。\n\n### 5. 开发者最佳实践\n*   **坚持简约原则**：优先使用简单的、可组合的模式，只有在简单 Prompt 无法解决问题时才增加 agentic 系统的复杂度 [30, 31]。\n*   **重视 ACI 设计**：像设计人机交互（HCI）一样设计**智能体-计算机接口（ACI）**。例如，为智能体提供清晰的工具文档、示例用法和边缘情况说明 [32, 33]。\n*   **透明化规划**：显式展示智能体的思考和规划步骤，这有助于调试并建立用户信任 [31, 34]。\n*   **安全加固**：在虚拟化环境（VM 或容器）中运行智能体，并针对敏感操作（如财务交易、接受条款）引入**人类确认机制** [35, 36]。\n\n### 6. 常见踩坑经验\n*   **路径定位失败**：智能体在移动目录后常因使用相对路径而迷失。**解决方案**：强制要求工具始终使用**绝对路径** [37]。\n*   **坐标偏移**：API 会对截图进行缩放，若不进行**坐标缩放因子（Scale Factor）**转换，智能体点击的位置会产生偏移 [38, 39]。\n*   **幻觉与失控**：智能体有时会假装检查了结果而直接跳到下一步。**对策**：在 Prompt 中明确要求“每一步后截图并评估结果，显式输出‘我已评估第 X 步...’” [34]。\n*   **格式开销过大**：要求模型生成包含大量转义字符的 JSON 或计算数千行代码的行号会显著降低成功率。**建议**：保持格式接近互联网自然文本，减少格式化负担 [32, 40]。",
    "conversation_id": "c94ba068-f426-48eb-9569-cc9a0af35cc2",
    "sources_used": [
      "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "6176a1b8-0474-4827-be67-b6301d4a008b",
      "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
      "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "9a88e940-c700-42af-92b9-58cbd7d63b86"
    ],
    "citations": {
      "1": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "2": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "3": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "4": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "5": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "6": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "7": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "8": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "9": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "10": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "11": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "12": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "13": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "14": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "15": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "16": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "17": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "18": "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
      "19": "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
      "20": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "21": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "22": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "23": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "24": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
      "25": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "26": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "27": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "28": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "29": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "30": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "31": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "32": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "33": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "34": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "35": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "36": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "37": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "38": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "39": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "40": "8cf581f7-6f33-4b8b-8200-3056fa939a92"
    },
    "references": [
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 1,
        "cited_text": "Acknowledgements Written by Erik Schluntz and Barry Zhang. This work draws upon our experiences building agents at Anthropic and the valuable insights shared by our customers, for which we're deeply grateful. Appendix 1: Agents in practice Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 2,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 3,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 4,
        "cited_text": "Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness. B. Coding agents The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because: Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 5,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 6,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 7,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 8,
        "cited_text": "Tools Computer use tool Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction. On WebArena , a benchmark for autonomous web navigation across real websites, Claude achieves state-of-the-art results among single-agent systems, demonstrating strong ability to complete multi-step browser tasks end to end. Computer use is in beta and requires a beta header : \"computer-use-2025-11-24\"  for Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5 \"computer-use-2025-01-24\"  for Sonnet 4.5, Haiku 4.5, Opus 4.1, Sonnet 4, Opus 4, and Sonnet 3.7 ( deprecated )"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 9,
        "cited_text": "Reach out through the feedback form to share your feedback on this feature. This feature is eligible for Zero Data Retention (ZDR) . When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned. Overview Computer use is a beta feature that enables Claude to interact with desktop environments. This tool provides: Screenshot capture : See what's currently displayed on screen Mouse control : Click, drag, and move the cursor Keyboard input : Type text and use keyboard shortcuts Desktop automation : Interact with any application or interface"
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 10,
        "cited_text": "Events Meetups Hackathon Support Forum Discord API Dashboard Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We’re moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back  previous_response_id ."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 11,
        "cited_text": "What’s changed? Before Now Why? Assistants Prompts Prompts hold configuration (model, tools, instructions) and are easier to version and update Threads Conversations Streams of items instead of just messages Runs Responses Responses send input items or use a conversation object and receive output items; tool call loops are explicitly managed Run steps Items Generalized objects—can be messages, tool calls, outputs, and more From assistants to prompts Assistants were persistent API objects that bundled model choice, instructions, and tool declarations—created and managed entirely through the API. Their replacement, prompts, can only be created in the dashboard, where you can version them as you develop your product."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 12,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 13,
        "cited_text": "These precautions remain important even with the classifier defense layer in place. Inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products. Computer use reference implementation Get started quickly with the computer use reference implementation that includes a web interface, Docker container, example tool implementations, and an agent loop. Note: The implementation has been updated to include new tools for both Claude 4 models and Claude Sonnet 3.7. Be sure to pull the latest version of the repo to access these new features."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 14,
        "cited_text": "The computing environment Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes: Virtual display : A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions. Desktop environment : A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 15,
        "cited_text": "Applications : Pre-installed Linux applications like Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks. Tool implementations : Integration code that translates Claude's abstract tool requests (like \"move mouse\" or \"take screenshot\") into actual operations in the virtual environment. Agent loop : A program that handles communication between Claude and the environment, sending Claude's actions to the environment and returning the results (screenshots, command outputs) back to Claude."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 16,
        "cited_text": "With over 100,000 developers certified through our community courses at learn.crewai.com , CrewAI is rapidly becoming the standard for enterprise-ready AI automation. CrewAI AMP Suite CrewAI AMP Suite is a comprehensive bundle tailored for organizations that require secure, scalable, and easy-to-manage agent-driven automation. You can try one part of the suite the Crew Control Plane for free Crew Control Plane Key Features: Tracing & Observability : Monitor and track your AI agents and workflows in real-time, including metrics, logs, and traces. Unified Control Plane : A centralized platform for managing, monitoring, and scaling your AI agents and workflows. Seamless Integrations : Easily connect with existing enterprise systems, data sources, and cloud infrastructure. Advanced Security : Built-in robust security and compliance measures ensuring safe deployment and management. Actionable Insights : Real-time analytics and reporting to optimize performance and decision-making. 24/7 Support : Dedicated enterprise support to ensure uninterrupted operation and quick resolution of issues. On-premise and Cloud Deployment Options : Deploy CrewAI AMP on-premise or in the cloud, depending on your security and compliance requirements."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 17,
        "cited_text": "Q: How can I contribute to CrewAI? A: Contributions are warmly welcomed! Fork the repository, create your branch, implement your changes, and submit a pull request. See the Contribution section of the README for detailed guidelines. Q: What additional features does CrewAI AMP offer? A: CrewAI AMP provides advanced features such as a unified control plane, real-time observability, secure integrations, advanced security, actionable insights, and dedicated 24/7 enterprise support. Q: Is CrewAI AMP available for cloud and on-premise deployments?"
      },
      {
        "source_id": "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
        "citation_number": 18,
        "cited_text": "What is E2B? E2B is an open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud. To start and control sandboxes, use our JavaScript SDK or Python SDK . Run your first Sandbox 1. Install SDK JavaScript / TypeScript npm i e2b Python pip install e2b 2. Get your E2B API key Sign up to E2B here . Get your API key here . Set environment variable with your API key E2B_API_KEY=e2b_*** 3. Start a sandbox and run commands JavaScript / TypeScript import   Sandbox   from   'e2b'   const   sandbox   =   await   Sandbox . create ( )   const   result   =   await   sandbox . commands . run ( 'echo \"Hello from E2B!\"' )   console . log ( result . stdout )   // Hello from E2B!"
      },
      {
        "source_id": "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
        "citation_number": 19,
        "cited_text": "5. Check docs Visit E2B documentation . 6. E2B cookbook Visit our Cookbook to get inspired by examples with different LLMs and AI frameworks. Self-hosting Read the self-hosting guide to learn how to set up the E2B infrastructure on your own. The infrastructure is deployed using Terraform. Supported cloud providers: 🟢 AWS 🟢 Google Cloud (GCP) Azure General Linux machine About Open-source, secure environment with real-world tools for enterprise-grade agents. e2b.dev/docs Topics react javascript python agent development typescript ai nextjs devtools openai software gpt copilot ai-agents ai-agent gpt-4 llm code-interpreter Resources"
      },
      {
        "source_id": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
        "citation_number": 20,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2405.15793 Help | Advanced Search Computer Science > Software Engineering arXiv:2405.15793 (cs)   [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.  Comments:   Code, data, and demo available at this https URL Subjects:   Software Engineering (cs.SE) ; Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Human-Computer Interaction (cs.HC); Machine Learning (cs.LG)   Cite as: arXiv:2405.15793 [cs.SE]   (or arXiv:2405.15793v3 [cs.SE]  for this version) https://doi.org/10.48550/arXiv.2405.15793 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 21,
        "cited_text": "Homepage · Docs · Start Cloud Trial · Blog · Forum Fast and Flexible Multi-Agent Automation Framework CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks . It empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario. CrewAI Crews : Optimize for autonomy and collaborative intelligence. CrewAI Flows : The enterprise and production architecture for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively"
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 22,
        "cited_text": "CrewAI offers two powerful, complementary approaches that work seamlessly together to build sophisticated AI applications: Crews : Teams of AI agents with true autonomy and agency, working together to accomplish complex tasks through role-based collaboration. Crews enable: Natural, autonomous decision-making between agents Dynamic task delegation and collaboration Specialized roles with defined goals and expertise Flexible problem-solving approaches Flows : Production-ready, event-driven workflows that deliver precise control over complex automations. Flows provide:"
      },
      {
        "source_id": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
        "citation_number": 23,
        "cited_text": "Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. pip install -U langgraph If you're looking to quickly build agents with LangChain's  create_agent  (built on LangGraph), check out the LangChain Agents documentation . Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs ."
      },
      {
        "source_id": "0280f766-e8bf-4c6f-980d-03c5782fbdb2",
        "citation_number": 24,
        "cited_text": "Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 25,
        "cited_text": "AutoGen AutoGen is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans. Important: if you are new to AutoGen, please checkout Microsoft Agent Framework . AutoGen will still be maintained and continue to receive bug fixes and critical security patches. Read our announcement . Installation AutoGen requires Python 3.10 or later . #  Install AgentChat and OpenAI client from Extensions  pip install -U  \" autogen-agentchat \"   \" autogen-ext[openai] \" The current stable version can be found in the releases . If you are upgrading from AutoGen v0.2, please refer to the Migration Guide for detailed instructions on how to update your code and configurations."
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 26,
        "cited_text": "#  Run AutoGen Studio on http://localhost:8080  autogenstudio ui --port 8080 --appdir ./my-app Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components."
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 27,
        "cited_text": "Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 28,
        "cited_text": "GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%. Open source agent tools and the academic literature on agents are proliferating, making this an exciting time but also a confusing one. To help put this work into perspective, I’d like to share a framework for categorizing design patterns for building agents. My team AI Fund is successfully using these patterns in many applications, and I hope you find them useful."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 29,
        "cited_text": "P.S. CrewAI demonstrates significant performance advantages over LangGraph, executing 5.76x faster in certain cases like this QA task example ( see comparison ) while achieving higher evaluation scores with faster completion times in certain coding tasks, like in this example ( detailed analysis ). Autogen : While Autogen excels at creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows. ChatDev : ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 30,
        "cited_text": "Skip to main content Skip to footer News Try Claude Engineering at Anthropic Building effective agents Published  Dec 19, 2024 We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks. Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 31,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 32,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 33,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 34,
        "cited_text": "The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs. Try the reference implementation out before reading the rest of this documentation. Optimize model performance with prompting Here are some tips on how to get the best quality outputs: Specify simple, well-defined tasks and provide explicit instructions for each step. Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with  After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: \"I have evaluated step X...\" If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one. Some UI elements (like dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts. For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt. If you need the model to log in, provide it with the username and password in your prompt inside xml tags like  <robot_credentials> . Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Review the guide on mitigating prompt injections before providing the model with login credentials."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 35,
        "cited_text": "Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents. Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft. Limiting internet access to an allowlist of domains to reduce exposure to malicious content. Asking a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 36,
        "cited_text": "Follow implementation best practices Understand computer use limitations The computer use functionality is in beta. While Claude's capabilities are cutting edge, developers should be aware of its limitations: Latency : the current computer use latency for human-AI interactions may be too slow compared to regular human-directed computer actions. Focus on use cases where speed isn't critical (for example, background information gathering, automated software testing) in trusted environments. Computer vision accuracy and reliability : Claude may make mistakes or hallucinate when outputting specific coordinates while generating actions. Claude Sonnet 3.7 introduces the thinking capability that can help you understand the model's reasoning and identify potential issues. Tool selection accuracy and reliability : Claude may make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability may be lower when interacting with niche applications or multiple applications at once. Prompt the model carefully when requesting complex tasks. Scrolling reliability : Claude Sonnet 3.7 introduced dedicated scroll actions with direction control that improves reliability. The model can now explicitly scroll in any direction (up/down/left/right) by a specified amount. Spreadsheet interaction : Mouse clicks for spreadsheet interaction have improved in Claude Sonnet 3.7 with the addition of more precise mouse control actions like  left_mouse_down ,  left_mouse_up , and new modifier key support. Cell selection can be more reliable by using these fine-grained controls and combining modifier keys with clicks. Account creation and content generation on social and communications platforms : While Claude will visit websites, Claude's ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms is limited. This capability may be updated in the future. Vulnerabilities : Vulnerabilities like jailbreaking or prompt injection may persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even in conflict with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. Consider the following: a. Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges b. Avoiding giving computer use access to sensitive accounts or data without strict oversight c. Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications Inappropriate or illegal actions : Per Anthropic's terms of service, you must not employ computer use to violate any laws or the Acceptable Use Policy."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 37,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 38,
        "cited_text": "Handle errors When implementing the computer use tool, various errors may occur. Here's how to handle them: Handle coordinate scaling for higher resolutions The API constrains images to a maximum of 1568 pixels on the longest edge and approximately 1.15 megapixels total (see image resizing for details). For example, a 1512x982 screen gets downsampled to approximately 1330x864. Claude analyzes this smaller image and returns coordinates in that space, but your tool executes clicks in the original screen space."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 39,
        "cited_text": "This can cause Claude's click coordinates to miss their targets unless you handle the coordinate transformation. To fix this, resize screenshots yourself and scale Claude's coordinates back up: import  math   def  get_scale_factor ( width ,  height ):    \"\"\"Calculate scale factor to meet API constraints.\"\"\"    long_edge  =  max (width, height)    total_pixels  =  width  *  height    long_edge_scale  =  1568  /  long_edge    total_pixels_scale  =  math.sqrt( 1_150_000  /  total_pixels)    return  min ( 1.0 , long_edge_scale, total_pixels_scale)   # When capturing screenshot   scale  =  get_scale_factor(screen_width, screen_height)   scaled_width  =  int (screen_width  *  scale)   scaled_height  =  int (screen_height  *  scale)   # Resize image to scaled dimensions before sending to Claude   screenshot  =  capture_and_resize(scaled_width, scaled_height)   # When handling Claude's coordinates, scale them back up   def  execute_click ( x ,  y ):    screen_x  =  x  /  scale    screen_y  =  y  /  scale    perform_click(screen_x, screen_y)"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 40,
        "cited_text": "There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「Agent Engineering 全景：从 Chatbot 到自主智能体的范式转变」领域，2025-2026 年标志着从“无状态对话助手”向“有状态、具备环境交互能力的自主智能体”全面迁移的关键期。以下是根据最新来源总结的研究突破、技术趋势及挑战：\n\n### 1. 2025-2026 年核心技术趋势与重要论文\n*   **API 范式转型：从 Assistants 到 Responses/Prompts**：\n    *   **OpenAI** 已宣布 Assistants API 计划于 **2026 年 8 月 26 日**关闭，全面转向 **Responses API** [1]。\n    *   **核心转变**：将传统的“线程（Threads）”升级为“对话（Conversations）”，后者不仅能存储消息，还能存储工具调用、输出项等多种数据对象 [2, 3]。同时，引入了**“Prompt 对象”**作为版本化的行为配置文件，实现了业务逻辑与模型配置的解耦 [4, 5]。\n*   **智能体-计算机接口 (ACI) 的崛起**：\n    *   **关键论文**：*《SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering》*（2024 年发表，2025 年持续演进）指出，智能体不仅需要强大的模型，更需要专门为其设计的软件界面（ACI） [6]。\n    *   **突破点**：通过 ACI，SWE-agent 在 SWE-bench 上取得了 **12.5%** 的通过率，远超非交互式模型 [6]。\n*   **计算机使用 (Computer Use) 的标准化**：\n    *   **Claude 4.x 系列**（如 4.6 版本）引入了原生“计算机使用”工具，使智能体能直接观察截图、控制鼠标点击和键盘输入，实现在真实桌面上完成端到端任务 [7-9]。\n*   **工作流与代理模式的融合**：\n    *   **Anthropic** 总结了五大核心模式：**提示词链 (Chaining)**、**路由 (Routing)**、**并行化 (Parallelization)**、**编排器-工人 (Orchestrator-workers)** 及 **评估器-优化器 (Evaluator-optimizer)** [10-14]。\n    *   **CrewAI** 进一步区分了具备自主权的 **Crews**（代理团队）和具备精确事件控制的 **Flows**（生产级流控架构），支持逻辑运算符（如 `or_`, `and_`）进行复杂任务编排 [15, 16]。\n\n### 2. 重要技术指标与性能突破\n*   **Agent 循环的增益**：Andrew Ng 指出，GPT-3.5 在零样本模式下 HumanEval 准确率仅为 48.1%，但包裹在 **Agent 循环**（反思、规划、工具使用、协作）中后，其表现可大幅提升至 **95.1%** [17, 18]。\n*   **执行效率**：CrewAI 在特定任务中的执行速度据称比 LangGraph **快 5.76 倍**，且在复杂编码任务中表现出更高的评估得分 [19]。\n\n### 3. 未解决的挑战\n*   **安全性与风险管理**：\n    *   **提示词注入 (Prompt Injection)**：智能体在浏览网页或查看图像时，可能会受到攻击者嵌入的恶意指令干扰 [20, 21]。\n    *   **权限与隔离**：自主智能体执行代码或操作真实系统存在巨大风险，需要极度安全的沙箱环境（如 **E2B Sandboxes** 或专用 Docker 容器）进行物理隔离 [22-24]。\n*   **交互精度与延迟**：\n    *   **视觉幻觉**：智能体在输出点击坐标时可能出现偏移，或由于截图缩放导致点击失败 [21, 25]。\n    *   **延迟成本**：Agent 循环通常以牺牲**延迟和成本**为代价来换取性能，这在实时人机交互中仍是一个瓶颈 [21, 26]。\n*   **可观测性不足**：复杂的多智能体系统中，调试“黑盒”逻辑和跨代理的状态同步依然困难 [27, 28]。\n\n### 4. 未来可能的突破点\n*   **统一集成协议 (MCP)**：**Model Context Protocol (MCP)** 正在成为连接智能体与第三方工具、服务器及连接器的全球标准，有望解决工具定义的碎片化问题 [29-31]。\n*   **扩展思考 (Extended Thinking)**：如 Claude 4.6 引入的 **Thinking Budget**，允许模型在执行动作前进行更深度的内部推理，这能显著降低视觉定位错误和逻辑幻觉 [21, 30, 32]。\n*   **自主迭代的 ACI**：未来研究方向可能包括让智能体自行优化其操作工具的界面（如自定义 Shell 或 API），以达到超越人类操作的效率 [6]。\n*   **端到端验证机制**：针对长程运行的智能体，引入类似 **Browser-based checks** 的端到端回归测试方案，以捕捉代码审查无法发现的交互错误 [33]。",
    "conversation_id": "c94ba068-f426-48eb-9569-cc9a0af35cc2",
    "sources_used": [
      "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "6176a1b8-0474-4827-be67-b6301d4a008b",
      "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
      "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e"
    ],
    "citations": {
      "1": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "2": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "3": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "4": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "5": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
      "6": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
      "7": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "8": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "9": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "10": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "11": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "12": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "13": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "14": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "15": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "16": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "17": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "18": "9a88e940-c700-42af-92b9-58cbd7d63b86",
      "19": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "20": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "21": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "22": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "23": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "24": "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
      "25": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "26": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "27": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "28": "6176a1b8-0474-4827-be67-b6301d4a008b",
      "29": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
      "30": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "31": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
      "32": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
      "33": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9"
    },
    "references": [
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 1,
        "cited_text": "Events Meetups Hackathon Support Forum Discord API Dashboard Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We’re moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back  previous_response_id ."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 2,
        "cited_text": "What’s changed? Before Now Why? Assistants Prompts Prompts hold configuration (model, tools, instructions) and are easier to version and update Threads Conversations Streams of items instead of just messages Runs Responses Responses send input items or use a conversation object and receive output items; tool call loops are explicitly managed Run steps Items Generalized objects—can be messages, tool calls, outputs, and more From assistants to prompts Assistants were persistent API objects that bundled model choice, instructions, and tool declarations—created and managed entirely through the API. Their replacement, prompts, can only be created in the dashboard, where you can version them as you develop your product."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 3,
        "cited_text": "A thread was a collection of messages stored server-side. Threads could only store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data. Request example Thread object 1  2  3  4  thread = openai.beta.threads.create(   messages=[{ \"role\" :  \"user\" ,  \"content\" :  \"what are the 5 Ds of dodgeball?\" }],   metadata={ \"user_id\" :  \"peter_le_fleur\" },  ) Conversation object 1  2  3  4  conversation = openai.conversations.create(   items=[{ \"role\" :  \"user\" ,  \"content\" :  \"what are the 5 Ds of dodgeball?\" }],   metadata={ \"user_id\" :  \"peter_le_fleur\" },  )"
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 4,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "b0d9e504-25f3-44f1-a768-fbe9b7d63724",
        "citation_number": 5,
        "cited_text": "Practical migration steps Identify each existing Assistant’s instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      },
      {
        "source_id": "653ffd39-507b-4d0a-a61a-40f5bafcbf6e",
        "citation_number": 6,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2405.15793 Help | Advanced Search Computer Science > Software Engineering arXiv:2405.15793 (cs)   [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.  Comments:   Code, data, and demo available at this https URL Subjects:   Software Engineering (cs.SE) ; Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Human-Computer Interaction (cs.HC); Machine Learning (cs.LG)   Cite as: arXiv:2405.15793 [cs.SE]   (or arXiv:2405.15793v3 [cs.SE]  for this version) https://doi.org/10.48550/arXiv.2405.15793 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 7,
        "cited_text": "Tools Computer use tool Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction. On WebArena , a benchmark for autonomous web navigation across real websites, Claude achieves state-of-the-art results among single-agent systems, demonstrating strong ability to complete multi-step browser tasks end to end. Computer use is in beta and requires a beta header : \"computer-use-2025-11-24\"  for Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5 \"computer-use-2025-01-24\"  for Sonnet 4.5, Haiku 4.5, Opus 4.1, Sonnet 4, Opus 4, and Sonnet 3.7 ( deprecated )"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 8,
        "cited_text": "Reach out through the feedback form to share your feedback on this feature. This feature is eligible for Zero Data Retention (ZDR) . When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned. Overview Computer use is a beta feature that enables Claude to interact with desktop environments. This tool provides: Screenshot capture : See what's currently displayed on screen Mouse control : Click, drag, and move the cursor Keyboard input : Type text and use keyboard shortcuts Desktop automation : Interact with any application or interface"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 9,
        "cited_text": "Enhanced actions ( computer_20251124 ) Available in Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5: All actions from  computer_20250124 zoom - View a specific region of the screen at full resolution. Requires  enable_zoom: true  in tool definition. Takes a  region  parameter with coordinates  [x1, y1, x2, y2]  defining top-left and bottom-right corners of the area to inspect. Tool parameters Parameter Required Description type Yes Tool version ( computer_20251124  or  computer_20250124 ) name Yes Must be \"computer\" display_width_px Yes Display width in pixels display_height_px Yes Display height in pixels display_number No Display number for X11 environments enable_zoom No Enable zoom action ( computer_20251124  only). Set to  true  to allow Claude to zoom into specific screen regions. Default:  false"
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 10,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 11,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 12,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 13,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 14,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 15,
        "cited_text": "Homepage · Docs · Start Cloud Trial · Blog · Forum Fast and Flexible Multi-Agent Automation Framework CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks . It empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario. CrewAI Crews : Optimize for autonomy and collaborative intelligence. CrewAI Flows : The enterprise and production architecture for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively"
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 16,
        "cited_text": "CrewAI's power truly shines when combining Crews with Flows to create sophisticated automation pipelines. CrewAI flows support logical operators like  or_  and  and_  to combine multiple conditions. This can be used with  @start ,  @listen , or  @router  decorators to create complex triggering conditions. or_ : Triggers when any of the specified conditions are met. and_ Triggers when all of the specified conditions are met. Here's how you can orchestrate multiple Crews within a Flow: from   crewai . flow . flow   import   Flow ,  listen ,  start ,  router ,  or_   from   crewai   import   Crew ,  Agent ,  Task ,  Process   from   pydantic   import   BaseModel   # Define structured state for precise control   class   MarketState ( BaseModel ):  sentiment :  str   =   \"neutral\"   confidence :  float   =   0.0   recommendations :  list   =  []  class   AdvancedAnalysisFlow ( Flow [ MarketState ]):  @ start ()   def   fetch_market_data ( self ):  # Demonstrate low-level control with structured state   self . state . sentiment   =   \"analyzing\"   return  { \"sector\" :  \"tech\" ,  \"timeframe\" :  \"1W\" }  # These parameters match the task description template   @ listen ( fetch_market_data )   def   analyze_with_crew ( self ,  market_data ):  # Show crew agency through specialized roles   analyst   =   Agent (  role = \"Senior Market Analyst\" ,  goal = \"Conduct deep market analysis with expert insight\" ,  backstory = \"You're a veteran analyst known for identifying subtle market patterns\"  )  researcher   =   Agent (  role = \"Data Researcher\" ,  goal = \"Gather and validate supporting market data\" ,  backstory = \"You excel at finding and correlating multiple data sources\"  )  analysis_task   =   Task (  description = \"Analyze {sector} sector data for the past {timeframe}\" ,  expected_output = \"Detailed market analysis with confidence score\" ,  agent = analyst  )  research_task   =   Task (  description = \"Find supporting data to validate the analysis\" ,  expected_output = \"Corroborating evidence and potential contradictions\" ,  agent = researcher  )  # Demonstrate crew autonomy   analysis_crew   =   Crew (  agents = [ analyst ,  researcher ],  tasks = [ analysis_task ,  research_task ],  process = Process . sequential ,  verbose = True  )  return   analysis_crew . kickoff ( inputs = market_data )  # Pass market_data as named inputs   @ router ( analyze_with_crew )   def   determine_next_steps ( self ):  # Show flow control with conditional routing   if   self . state . confidence   >   0.8 :  return   \"high_confidence\"   elif   self . state . confidence   >   0.5 :  return   \"medium_confidence\"   return   \"low_confidence\"   @ listen ( \"high_confidence\" )   def   execute_strategy ( self ):  # Demonstrate complex decision making   strategy_crew   =   Crew (  agents = [  Agent ( role = \"Strategy Expert\" ,  goal = \"Develop optimal market strategy\" ) ],  tasks = [  Task ( description = \"Create detailed strategy based on analysis\" ,  expected_output = \"Step-by-step action plan\" ) ] )  return   strategy_crew . kickoff ()  @ listen ( or_ ( \"medium_confidence\" ,  \"low_confidence\" ))   def   request_additional_analysis ( self ):  self . state . recommendations . append ( \"Gather more data\" )  return   \"Additional analysis required\""
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 17,
        "cited_text": "GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%. Open source agent tools and the academic literature on agents are proliferating, making this an exciting time but also a confusing one. To help put this work into perspective, I’d like to share a framework for categorizing design patterns for building agents. My team AI Fund is successfully using these patterns in many applications, and I hope you find them useful."
      },
      {
        "source_id": "9a88e940-c700-42af-92b9-58cbd7d63b86",
        "citation_number": 18,
        "cited_text": "Reflection: The LLM examines its own work to come up with ways to improve it. Tool Use: The LLM is given tools such as web search, code execution, or any other function to help it gather information, take action, or process data. Planning: The LLM comes up with, and executes, a multistep plan to achieve a goal (for example, writing an outline for an essay, then doing online research, then writing a draft, and so on). Multi-agent collaboration: More than one AI agent work together, splitting up tasks and discussing and debating ideas, to come up with better solutions than a single agent would."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 19,
        "cited_text": "P.S. CrewAI demonstrates significant performance advantages over LangGraph, executing 5.76x faster in certain cases like this QA task example ( see comparison ) while achieving higher evaluation scores with faster completion times in certain coding tasks, like in this example ( detailed analysis ). Autogen : While Autogen excels at creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows. ChatDev : ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 20,
        "cited_text": "In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. Take precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection. The model has been trained to resist these prompt injections, and an extra layer of defense has been added. If you use the computer use tools, classifiers will automatically run on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, please contact support ."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 21,
        "cited_text": "Follow implementation best practices Understand computer use limitations The computer use functionality is in beta. While Claude's capabilities are cutting edge, developers should be aware of its limitations: Latency : the current computer use latency for human-AI interactions may be too slow compared to regular human-directed computer actions. Focus on use cases where speed isn't critical (for example, background information gathering, automated software testing) in trusted environments. Computer vision accuracy and reliability : Claude may make mistakes or hallucinate when outputting specific coordinates while generating actions. Claude Sonnet 3.7 introduces the thinking capability that can help you understand the model's reasoning and identify potential issues. Tool selection accuracy and reliability : Claude may make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability may be lower when interacting with niche applications or multiple applications at once. Prompt the model carefully when requesting complex tasks. Scrolling reliability : Claude Sonnet 3.7 introduced dedicated scroll actions with direction control that improves reliability. The model can now explicitly scroll in any direction (up/down/left/right) by a specified amount. Spreadsheet interaction : Mouse clicks for spreadsheet interaction have improved in Claude Sonnet 3.7 with the addition of more precise mouse control actions like  left_mouse_down ,  left_mouse_up , and new modifier key support. Cell selection can be more reliable by using these fine-grained controls and combining modifier keys with clicks. Account creation and content generation on social and communications platforms : While Claude will visit websites, Claude's ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms is limited. This capability may be updated in the future. Vulnerabilities : Vulnerabilities like jailbreaking or prompt injection may persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even in conflict with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. Consider the following: a. Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges b. Avoiding giving computer use access to sensitive accounts or data without strict oversight c. Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications Inappropriate or illegal actions : Per Anthropic's terms of service, you must not employ computer use to violate any laws or the Acceptable Use Policy."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 22,
        "cited_text": "Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents. Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft. Limiting internet access to an allowlist of domains to reduce exposure to malicious content. Asking a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 23,
        "cited_text": "When you use computer use, Claude doesn't directly connect to this environment. Instead, your application: Receives Claude's tool use requests Translates them into actions in your computing environment Captures the results (screenshots, command outputs, etc.) Returns these results to Claude For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment. How to implement computer use"
      },
      {
        "source_id": "64b3ad68-0a22-4be0-91d9-d90cd6b7a37f",
        "citation_number": 24,
        "cited_text": "What is E2B? E2B is an open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud. To start and control sandboxes, use our JavaScript SDK or Python SDK . Run your first Sandbox 1. Install SDK JavaScript / TypeScript npm i e2b Python pip install e2b 2. Get your E2B API key Sign up to E2B here . Get your API key here . Set environment variable with your API key E2B_API_KEY=e2b_*** 3. Start a sandbox and run commands JavaScript / TypeScript import   Sandbox   from   'e2b'   const   sandbox   =   await   Sandbox . create ( )   const   result   =   await   sandbox . commands . run ( 'echo \"Hello from E2B!\"' )   console . log ( result . stdout )   // Hello from E2B!"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 25,
        "cited_text": "Handle errors When implementing the computer use tool, various errors may occur. Here's how to handle them: Handle coordinate scaling for higher resolutions The API constrains images to a maximum of 1568 pixels on the longest edge and approximately 1.15 megapixels total (see image resizing for details). For example, a 1512x982 screen gets downsampled to approximately 1330x864. Claude analyzes this smaller image and returns coordinates in that space, but your tool executes clicks in the original screen space."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 26,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 27,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "6176a1b8-0474-4827-be67-b6301d4a008b",
        "citation_number": 28,
        "cited_text": "With over 100,000 developers certified through our community courses at learn.crewai.com , CrewAI is rapidly becoming the standard for enterprise-ready AI automation. CrewAI AMP Suite CrewAI AMP Suite is a comprehensive bundle tailored for organizations that require secure, scalable, and easy-to-manage agent-driven automation. You can try one part of the suite the Crew Control Plane for free Crew Control Plane Key Features: Tracing & Observability : Monitor and track your AI agents and workflows in real-time, including metrics, logs, and traces. Unified Control Plane : A centralized platform for managing, monitoring, and scaling your AI agents and workflows. Seamless Integrations : Easily connect with existing enterprise systems, data sources, and cloud infrastructure. Advanced Security : Built-in robust security and compliance measures ensuring safe deployment and management. Actionable Insights : Real-time analytics and reporting to optimize performance and decision-making. 24/7 Support : Dedicated enterprise support to ensure uninterrupted operation and quick resolution of issues. On-premise and Cloud Deployment Options : Deploy CrewAI AMP on-premise or in the cloud, depending on your security and compliance requirements."
      },
      {
        "source_id": "8cf581f7-6f33-4b8b-8200-3056fa939a92",
        "citation_number": 29,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 30,
        "cited_text": "Loading... Search... ⌘K First steps Intro to Claude Quickstart Models & pricing Models overview Choosing a model What's new in Claude 4.6 Migration guide Model deprecations Pricing Build with Claude Features overview Using the Messages API Handling stop reasons Prompting best practices Model capabilities Extended thinking Adaptive thinking Effort Fast mode (beta: research preview) Structured outputs Citations Streaming Messages Batch processing PDF support Search results Multilingual support Embeddings Vision Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting Files & assets Files API Agent Skills Overview Quickstart Best practices Skills for enterprise Claude API skill Using Skills with the API Agent SDK Overview Quickstart How the agent loop works MCP in the API MCP connector Remote MCP servers Claude on 3rd-party platforms Amazon Bedrock Microsoft Foundry Vertex AI Prompt engineering Overview Console prompting tools Test & evaluate Define success and build evaluations Using the Evaluation Tool Reducing latency Strengthen guardrails Reduce hallucinations Increase output consistency Mitigate jailbreaks Streaming refusals Reduce prompt leak Administration and monitoring Admin API overview Data residency Workspaces Usage and Cost API Claude Code Analytics API API and data retention Console Log in Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading..."
      },
      {
        "source_id": "80d6a03e-cb3c-4bbb-b2d5-ed38249aca8e",
        "citation_number": 31,
        "cited_text": "MCP Server Create a web browsing assistant agent that uses the Playwright MCP server. # First run `npm install -g @playwright/mcp@latest` to install the MCP server.   import   asyncio   from   autogen_agentchat . agents   import   AssistantAgent   from   autogen_agentchat . ui   import   Console   from   autogen_ext . models . openai   import   OpenAIChatCompletionClient   from   autogen_ext . tools . mcp   import   McpWorkbench ,  StdioServerParams   async   def   main ()  ->   None :  model_client   =   OpenAIChatCompletionClient ( model = \"gpt-4.1\" )  server_params   =   StdioServerParams (  command = \"npx\" ,  args = [  \"@playwright/mcp@latest\" ,  \"--headless\" , ], )  async   with   McpWorkbench ( server_params )  as   mcp :  agent   =   AssistantAgent (  \"web_browsing_assistant\" ,  model_client = model_client ,  workbench = mcp ,  # For multiple MCP servers, put them in a list.   model_client_stream = True ,  max_tool_iterations = 10 , )  await   Console ( agent . run_stream ( task = \"Find out how many contributors for the microsoft/autogen repository\" ))  asyncio . run ( main ())"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 32,
        "cited_text": "async  def  sampling_loop (    * ,    model :  str ,    messages : list[ dict ],    api_key :  str ,    max_tokens :  int  =  4096 ,    tool_version :  str ,    thinking_budget :  int  |  None  =  None ,    max_iterations :  int  =  10 ,  # Add iteration limit to prevent infinite loops   ):    \"\"\"    A simple agent loop for Claude computer use interactions.    This function handles the back-and-forth between:    1. Sending user messages to Claude    2. Claude requesting to use tools    3. Your app executing those tools    4. Sending tool results back to Claude    \"\"\"    # Set up tools and API parameters    client  =  Anthropic( api_key = api_key)    beta_flag  =  (    \"computer-use-2025-11-24\"    if  \"20251124\"  in  tool_version    else  \"computer-use-2025-01-24\"    )    text_editor_type  =  (    \"text_editor_20250728\"    if  \"20251124\"  in  tool_version    else  f \"text_editor_ { tool_version } \"    )    # Configure tools - you should already have these initialized elsewhere    tools  =  [    {    \"type\" :  f \"computer_ { tool_version } \" ,    \"name\" :  \"computer\" ,    \"display_width_px\" :  1024 ,    \"display_height_px\" :  768 ,    },    { \"type\" : text_editor_type,  \"name\" :  \"str_replace_based_edit_tool\" },    { \"type\" :  \"bash_20250124\" ,  \"name\" :  \"bash\" },    ]    # Main agent loop (with iteration limit to prevent runaway API costs)    iterations  =  0    while  True  and  iterations  <  max_iterations:    iterations  +=  1    # Set up optional thinking parameter (for Claude Sonnet 3.7)    thinking  =  None    if  thinking_budget:    thinking  =  { \"type\" :  \"enabled\" ,  \"budget_tokens\" : thinking_budget}    # Call the Claude API    response  =  client.beta.messages.create(    model = model,    max_tokens = max_tokens,    messages = messages,    tools = tools,    betas = [beta_flag],    thinking = thinking,    )    # Add Claude's response to the conversation history    response_content  =  response.content    messages.append({ \"role\" :  \"assistant\" ,  \"content\" : response_content})    # Check if Claude used any tools    tool_results  =  []    for  block  in  response_content:    if  block.type  ==  \"tool_use\" :    # In a real app, you would execute the tool here    # For example: result = run_tool(block.name, block.input)    result  =  { \"result\" :  \"Tool executed successfully\" }    # Format the result for Claude    tool_results.append(    { \"type\" :  \"tool_result\" ,  \"tool_use_id\" : block.id,  \"content\" : result}    )    # If no tools were used, Claude is done - return the final messages    if  not  tool_results:    return  messages    # Add tool results to messages for the next iteration with Claude    messages.append({ \"role\" :  \"user\" ,  \"content\" : tool_results})"
      },
      {
        "source_id": "855d0ad7-2f3d-4147-bc2c-83d8e1e66be9",
        "citation_number": 33,
        "cited_text": "If you repeatedly encounter a clear set of issues or know in advance the tasks Claude will need to complete, use the system prompt to provide Claude with explicit tips or instructions on how to do the tasks successfully. For agents that span multiple sessions, run end-to-end verification at the start of each session, not only after implementation. Browser-based checks catch regressions from prior sessions that code-level review alone misses. See Effective harnesses for long-running agents for details."
      }
    ]
  }
}
