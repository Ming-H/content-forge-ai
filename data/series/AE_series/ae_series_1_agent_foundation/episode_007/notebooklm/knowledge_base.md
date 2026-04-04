# 知识库：Prompt Chaining 与 Routing：可预测的工作流

生成时间: 2026-04-03 15:56
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "「Prompt Chaining（提示词链）」与「Routing（路由）」是构建**可预测生成式 AI 工作流**的核心模式。根据提供的来源，其技术架构与组件概述如下：\n\n### 1. 技术演进路线\n技术演进遵循从简单到复杂、从无序到受控的路径：\n*   **基础阶段：增强型 LLM**。通过检索（RAG）、工具和内存增强单个 LLM 调用 [1]。\n*   **初级工作流阶段：工作流（Workflows）**。LLM 与工具通过**预定义的代码路径**进行编排，侧重于**可预测性**和一致性 [2, 3]。\n*   **高级编排阶段：状态驱动与学习路由**。引入如 **StateFlow**（状态机模型）来增强对复杂过程的控制，或使用 **RouteLLM**（基于偏好数据的学习路由）来优化成本与性能平衡 [4, 5]。\n*   **最终形态：自主智能体（Agents）**。LLM 动态指导自身进程和工具使用，具有更高的灵活性但牺牲了部分可预测性 [2, 6, 7]。\n\n### 2. 核心算法与技术名称\n*   **Prompt Chaining（提示词链）**：将任务分解为一系列步骤，每个 LLM 调用处理上一个调用的输出 [8]。通常包含**程序化检查（Gate）**以确保流程在轨 [8]。\n*   **Routing（路由）**：对输入进行分类并定向到专门的下游任务 [9]。\n    *   **RouteLLM**：一种高效的路由模型，利用**人类偏好数据**和数据增强技术训练，在推理时动态选择强模型或弱模型 [5]。\n*   **StateFlow**：一种基于**有限状态机（State Machine）**的范式。它区分了“**过程接地（Process Grounding）**”（通过状态转换）和“**子任务解决（Sub-task Solving）**”（通过状态内的行动），显著提升了可解释性 [4]。\n*   **Parallelization（并行化）**：分为 **Sectioning**（拆分任务并行运行）和 **Voting**（多次运行取多样化结果）[10]。\n\n### 3. 主要架构模式\n*   **线性链式架构（Linear Chaining）**：固定子任务的顺序执行，适用于可清晰分解的任务（如：撰写大纲 -> 检查大纲 -> 撰写正文）[8, 9]。\n*   **分发式路由架构（Hub-and-Spoke Routing）**：分类器作为核心，将不同类别的请求（如：退款申请 vs 技术支持）导向不同的提示词和工具 [11]。\n*   **编排者-工作者架构（Orchestrator-Workers）**：中央 LLM 动态拆解任务并分发给工作者 LLM，最后综合结果，适用于无法预知子任务数量的复杂场景 [12]。\n*   **评估者-优化者架构（Evaluator-Optimizer）**：一个 LLM 生成响应，另一个提供反馈循环，适用于有明确评价标准且需迭代改进的任务 [13]。\n*   **视觉化编排（Visual Builder）**：如 **Amazon Bedrock Flows**，允许通过拖拽提示词、智能体、知识库和 Lambda 等组件构建工作流 [14]。\n\n### 4. 关键技术指标\n*   **准确率与成功率**：**StateFlow** 在 SQL 任务中比 ReAct 成功率高出 **13%**，在 ALFWorld 基准测试中高出 **28%** [4]。\n*   **成本优化**：\n    *   **RouteLLM** 可将成本降低 **2 倍以上**且不损害响应质量 [5]。\n    *   **Prompt Caching（提示词缓存）** 可将重复任务的成本降低高达 **90%** [15]。\n    *   **StateFlow** 的成本比 ReAct 低 **3 到 5 倍** [4]。\n*   **延迟（Latency）**：\n    *   提示词链通过简化单个调用任务来换取更高的准确率，但可能增加整体延迟 [8]。\n    *   **提示词缓存**可将延迟降低 **2 倍以上** [15]。\n*   **缓存阈值**：缓存触发的最小长度通常为 **1,024 标记**（Sonnet）或 **4,096 标记**（Opus）[16]。\n*   **版本控制与回滚**：工作流支持版本化，以便进行 **A/B 测试**和快速回滚 [17, 18]。",
    "conversation_id": "f129feb2-3053-49b6-bd5d-2ff2e38f1d4b",
    "sources_used": [
      "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "faeba007-37d1-42b6-a99e-847af50d9857",
      "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
      "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12"
    ],
    "citations": {
      "1": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "2": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "3": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "4": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "5": "faeba007-37d1-42b6-a99e-847af50d9857",
      "6": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "7": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "8": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "9": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "10": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "11": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "12": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "13": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "14": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "15": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
      "16": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
      "17": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "18": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12"
    },
    "references": [
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 1,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 2,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 3,
        "cited_text": "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough. When and how to use frameworks There are many frameworks that make agentic systems easier to implement, including: The Claude Agent SDK ; Strands Agents SDK by AWS ; Rivet , a drag and drop GUI LLM workflow builder; and Vellum , another GUI tool for building and testing complex workflows."
      },
      {
        "source_id": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
        "citation_number": 4,
        "cited_text": "arXiv:2403.11322 (cs) [Submitted on 17 Mar 2024 ( v1 ), last revised 14 Sep 2024 (this version, v5)] Title: StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows Authors: Yiran Wu , Tianwei Yue , Shaokun Zhang , Chi Wang , Qingyun Wu View a PDF of the paper titled StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows, by Yiran Wu and 4 other authors View PDF HTML (experimental) Abstract: It is a notable trend to use Large Language Models (LLMs) to tackle complex tasks, e.g., tasks that require a sequence of actions and dynamic interaction with tools and external environments. In this paper, we propose StateFlow, a novel LLM-based task-solving paradigm that conceptualizes complex task-solving processes as state machines. In StateFlow, we distinguish between \"process grounding\" (via state and state transitions) and \"sub-task solving\" (through actions within a state), enhancing control and interpretability of the task-solving procedure. A state represents the status of a running process. The transitions between states are controlled by heuristic rules or decisions made by the LLM, allowing for a dynamic and adaptive progression. Upon entering a state, a series of actions is executed, involving not only calling LLMs guided by different prompts, but also the utilization of external tools as needed. Our results show that StateFlow significantly enhances LLMs' efficiency. For instance, StateFlow achieves 13% and 28% higher success rates compared to ReAct in InterCode SQL and ALFWorld benchmark, with 5x and 3x less cost respectively. We also show that StateFlow can be combined with iterative refining methods like Reflexion to further improve performance."
      },
      {
        "source_id": "faeba007-37d1-42b6-a99e-847af50d9857",
        "citation_number": 5,
        "cited_text": "arXiv:2406.18665 (cs) [Submitted on 26 Jun 2024 ( v1 ), last revised 23 Feb 2025 (this version, v4)] Title: RouteLLM: Learning to Route LLMs with Preference Data Authors: Isaac Ong , Amjad Almahairi , Vincent Wu , Wei-Lin Chiang , Tianhao Wu , Joseph E. Gonzalez , M Waleed Kadous , Ion Stoica View a PDF of the paper titled RouteLLM: Learning to Route LLMs with Preference Data, by Isaac Ong and 7 other authors View PDF HTML (experimental) Abstract: Large language models (LLMs) exhibit impressive capabilities across a wide range of tasks, yet the choice of which model to use often involves a trade-off between performance and cost. More powerful models, though effective, come with higher expenses, while less capable models are more cost-effective. To address this dilemma, we propose several efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality. We develop a training framework for these routers leveraging human preference data and data augmentation techniques to enhance performance. Our evaluation on widely-recognized benchmarks shows that our approach significantly reduces costs-by over 2 times in certain cases-without compromising the quality of responses. Interestingly, our router models also demonstrate significant transfer learning capabilities, maintaining their performance even when the strong and weak models are changed at test time. This highlights the potential of these routers to provide a cost-effective yet high-performance solution for deploying LLMs."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 6,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 7,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 8,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 9,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 10,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 11,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 12,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 13,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 14,
        "cited_text": "Black White Red Green Blue Yellow Magenta Cyan Opacity Transparent Semi-Transparent Opaque Font Size 50% 75% 100% 125% 150% 175% 200% 300% 400% Text Edge Style None Raised Depressed Uniform Drop shadow Font Family Proportional Sans-Serif Monospace Sans-Serif Proportional Serif Monospace Serif Casual Script Small Caps Reset Done Close Modal Dialog End of dialog window. Quickly build generative AI workflows visually Bedrock Flows accelerates the creation, testing, and deployment of user-defined workflows for generative AI applications through an intuitive visual builder. You can seamlessly drag, drop and link Prompts, Agents, Knowledge bases, Guardrails, Lex, Lambda, other AWS services, with business logic to create a workflow. This removes the need to write code and offers easy customization of the business logic. You can also create and updates flows using APIs or AWS Cloud Development Kit."
      },
      {
        "source_id": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
        "citation_number": 15,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      },
      {
        "source_id": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
        "citation_number": 16,
        "cited_text": "Start with automatic caching. It covers the majority of use cases with minimal effort. Switch to explicit breakpoints only when you need fine-grained control. Key details ¶ Minimum cacheable length: 1,024 tokens for Sonnet; 4,096 tokens for Opus and Haiku 4.5 Cache TTL: 5 minutes by default (refreshed on each hit). A 1-hour TTL is available at 2x base input price. Pricing: Cache writes cost 1.25x base input price. Cache reads cost 0.1x base input price. Breakpoint limit: Up to 4 explicit breakpoints per request. Automatic caching uses one slot."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 17,
        "cited_text": "Test and deploy faster with serverless infrastructure You can test your flows directly in the console for faster iteration with built-in traceability of inputs and outputs. Once a flow is ready, you can version the flow and integrate it into your generative AI application. The versioning capability on flows enables an easy rollback mechanism, and A/B testing. You can invoke the flow via an API call to integrate with your application without the need to deploy and manage your own infrastructure. Collaborate on workflow creation"
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 18,
        "cited_text": "Practical migration steps Identify each existing Assistant's instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「Prompt Chaining（提示词链）」与「Routing（路由）」是构建可预测生成式 AI 工作流的核心模式。以下是基于来源资料的深度解析：\n\n### 1. 核心算法流程与工作模式\n\n这些模式将复杂的任务拆解为可控的组件，确保输出的一致性：\n\n*   **Prompt Chaining（提示词链）流程**：\n    *   **任务分解**：将一个复杂任务分解为一系列固定子任务 [1]。\n    *   **顺序执行**：每个 LLM 调用处理前一个调用的输出 [1]。\n    *   **程序化检查（Gates）**：在中间步骤引入逻辑检查，若输出不符合预期则触发重试或报错，确保流程在轨 [1]。\n    *   **典型应用**：生成文档大纲 $\\rightarrow$ 逻辑检查 $\\rightarrow$ 根据大纲撰写正文 [2]。\n\n*   **Routing（路由）算法流程**：\n    *   **分类器（Router）**：对输入进行识别，确定其所属类别（如：退款申请 vs 技术支持）[2, 3]。\n    *   **定向分发**：根据分类结果将请求导向专门的下游提示词、工具或模型 [2, 3]。\n    *   **RouteLLM 优化**：利用**人类偏好数据**和数据增强技术训练路由模型，在推理时动态选择强模型（如 Opus）或弱模型（如 Haiku），以平衡质量与成本 [4]。\n\n*   **StateFlow（状态驱动）**：\n    *   **有限状态机（FSM）建模**：将任务解决过程建模为状态机 [5]。\n    *   **过程接地（Process Grounding）**：通过状态转换维持流程控制 [5]。\n    *   **子任务解决**：在每个状态内执行特定的 LLM 动作或工具调用 [5]。\n\n### 2. 关键代码架构\n\n现代 AI 开发正从“黑盒 API”转向更具透明度和可测试性的架构：\n\n*   **解耦式架构 (OpenAI Responses API)**：\n    *   **Prompts（提示词）**：取代了持久化的 Assistant 对象，成为可在仪表板中版本化管理的“行为配置文件” [6, 7]。\n    *   **Conversations（对话）**：存储消息、工具调用及输出的流式集合 [8, 9]。\n    *   **Responses（响应）**：简单的输入-输出执行单元，应用代码显式处理工具循环（Tool Loops）和重试逻辑 [6, 10]。\n*   **可视化编排架构 (Amazon Bedrock Flows)**：\n    *   **节点化组件**：通过拖拽 Prompts、Agents、知识库、Guardrails、Lambda 等节点构建逻辑链条 [11]。\n    *   **版本与回滚**：支持流程的版本化，便于 A/B 测试和生产环境快速回滚 [12]。\n*   **底层框架 (LangGraph)**：\n    *   相比于高层的 LangChain，**LangGraph** 提供了低级编排框架，用于构建需要**持久化**、**循环逻辑**和**人机交互（Human-in-the-loop）**的可控工作流 [13, 14]。\n\n### 3. 性能优化策略与具体参数\n\n优化策略侧重于降低延迟、成本并提高准确率：\n\n*   **提示词缓存 (Prompt Caching)**：\n    *   **数据效果**：可将重复任务的**成本降低高达 90%**，**延迟缩短 2 倍以上** [15]。\n    *   **触发阈值**：**Sonnet** 模型的最小缓存长度为 **1,024 标记**；**Opus** 和 **Haiku 4.5** 为 **4,096 标记** [16]。\n    *   **定价机制**：缓存写入成本通常为基础输入价的 **1.25 倍**，缓存命中读取仅为 **0.1 倍** [16]。\n    *   **管理模式**：支持“自动缓存”（系统自动管理断点）和“显式断点”（手动设置，每个请求最多 4 个）[16, 17]。\n*   **并行化 (Parallelization)**：\n    *   **Sectioning（切片）**：将任务拆分为独立子任务并行运行以降低延迟 [18]。\n    *   **Voting（投票）**：多次运行同一任务并汇总，以提高结果的置信度 [18]。\n*   **模型路由优化**：**RouteLLM** 可在不损害响应质量的前提下，将整体成本**降低 2 倍以上** [4]。\n\n### 4. 技术对比：StateFlow vs. ReAct 范式\n\n根据相关论文研究，状态驱动的工作流在复杂任务中表现优于传统的推理路径：\n\n| 指标 | StateFlow (状态驱动) | ReAct (传统推理循环) |\n| :--- | :--- | :--- |\n| **SQL 任务成功率** | **高出 13%** [5] | 基准水平 |\n| **ALFWorld 任务成功率** | **高出 28%** [5] | 基准水平 |\n| **SQL 任务成本** | **低 5 倍** [5] | 较高 |\n| **ALFWorld 任务成本** | **低 3 倍** [5] | 较高 |\n| **流程控制** | 基于预定义的 FSM，高度可预测 [5] | 由 LLM 动态驱动，具有不可预测性 [19] |\n\n**总结建议**：开发者应从直接使用 LLM API 开始，优先构建简单的组合模式 [20]。只有在任务可以被清晰分解时才使用 **Prompt Chaining**；在需要优化成本性能比时引入 **Routing**；而在需要极端稳定性的复杂任务中，应考虑 **StateFlow** 或 **LangGraph** 等状态机架构 [5, 13, 21]。",
    "conversation_id": "f129feb2-3053-49b6-bd5d-2ff2e38f1d4b",
    "sources_used": [
      "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "faeba007-37d1-42b6-a99e-847af50d9857",
      "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "59f38c05-3e11-42a4-8f0b-33e2e4587d3d"
    ],
    "citations": {
      "1": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "2": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "3": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "4": "faeba007-37d1-42b6-a99e-847af50d9857",
      "5": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "6": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "7": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "8": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "9": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "10": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "11": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "12": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "13": "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "14": "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "15": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
      "16": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
      "17": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
      "18": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "19": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "20": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "21": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705"
    },
    "references": [
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 1,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 2,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 3,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "faeba007-37d1-42b6-a99e-847af50d9857",
        "citation_number": 4,
        "cited_text": "arXiv:2406.18665 (cs) [Submitted on 26 Jun 2024 ( v1 ), last revised 23 Feb 2025 (this version, v4)] Title: RouteLLM: Learning to Route LLMs with Preference Data Authors: Isaac Ong , Amjad Almahairi , Vincent Wu , Wei-Lin Chiang , Tianhao Wu , Joseph E. Gonzalez , M Waleed Kadous , Ion Stoica View a PDF of the paper titled RouteLLM: Learning to Route LLMs with Preference Data, by Isaac Ong and 7 other authors View PDF HTML (experimental) Abstract: Large language models (LLMs) exhibit impressive capabilities across a wide range of tasks, yet the choice of which model to use often involves a trade-off between performance and cost. More powerful models, though effective, come with higher expenses, while less capable models are more cost-effective. To address this dilemma, we propose several efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality. We develop a training framework for these routers leveraging human preference data and data augmentation techniques to enhance performance. Our evaluation on widely-recognized benchmarks shows that our approach significantly reduces costs-by over 2 times in certain cases-without compromising the quality of responses. Interestingly, our router models also demonstrate significant transfer learning capabilities, maintaining their performance even when the strong and weak models are changed at test time. This highlights the potential of these routers to provide a cost-effective yet high-performance solution for deploying LLMs."
      },
      {
        "source_id": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
        "citation_number": 5,
        "cited_text": "arXiv:2403.11322 (cs) [Submitted on 17 Mar 2024 ( v1 ), last revised 14 Sep 2024 (this version, v5)] Title: StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows Authors: Yiran Wu , Tianwei Yue , Shaokun Zhang , Chi Wang , Qingyun Wu View a PDF of the paper titled StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows, by Yiran Wu and 4 other authors View PDF HTML (experimental) Abstract: It is a notable trend to use Large Language Models (LLMs) to tackle complex tasks, e.g., tasks that require a sequence of actions and dynamic interaction with tools and external environments. In this paper, we propose StateFlow, a novel LLM-based task-solving paradigm that conceptualizes complex task-solving processes as state machines. In StateFlow, we distinguish between \"process grounding\" (via state and state transitions) and \"sub-task solving\" (through actions within a state), enhancing control and interpretability of the task-solving procedure. A state represents the status of a running process. The transitions between states are controlled by heuristic rules or decisions made by the LLM, allowing for a dynamic and adaptive progression. Upon entering a state, a series of actions is executed, involving not only calling LLMs guided by different prompts, but also the utilization of external tools as needed. Our results show that StateFlow significantly enhances LLMs' efficiency. For instance, StateFlow achieves 13% and 28% higher success rates compared to ReAct in InterCode SQL and ALFWorld benchmark, with 5x and 3x less cost respectively. We also show that StateFlow can be combined with iterative refining methods like Reflexion to further improve performance."
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 6,
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
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 7,
        "cited_text": "Practical migration steps Identify each existing Assistant's instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 8,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 9,
        "cited_text": "A thread was a collection of messages stored server-side. Threads could only store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data. Request example Thread object Conversation object Response example Thread object Conversation object From runs to responses Runs were asynchronous processes that executed against threads. See the example below. Responses are simpler: provide a set of input items to execute, and get a list of output items back. Responses are designed to be used alone, but you can also use them with prompt and conversation objects for storing context and configuration."
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 10,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 11,
        "cited_text": "Black White Red Green Blue Yellow Magenta Cyan Opacity Transparent Semi-Transparent Opaque Font Size 50% 75% 100% 125% 150% 175% 200% 300% 400% Text Edge Style None Raised Depressed Uniform Drop shadow Font Family Proportional Sans-Serif Monospace Sans-Serif Proportional Serif Monospace Serif Casual Script Small Caps Reset Done Close Modal Dialog End of dialog window. Quickly build generative AI workflows visually Bedrock Flows accelerates the creation, testing, and deployment of user-defined workflows for generative AI applications through an intuitive visual builder. You can seamlessly drag, drop and link Prompts, Agents, Knowledge bases, Guardrails, Lex, Lambda, other AWS services, with business logic to create a workflow. This removes the need to write code and offers easy customization of the business logic. You can also create and updates flows using APIs or AWS Cloud Development Kit."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 12,
        "cited_text": "Test and deploy faster with serverless infrastructure You can test your flows directly in the console for faster iteration with built-in traceability of inputs and outputs. Once a flow is ready, you can version the flow and integrate it into your generative AI application. The versioning capability on flows enables an easy rollback mechanism, and A/B testing. You can invoke the flow via an API call to integrate with your application without the need to deploy and manage your own infrastructure. Collaborate on workflow creation"
      },
      {
        "source_id": "b6977b92-cd06-4e01-a91b-930eed06e01b",
        "citation_number": 13,
        "cited_text": "Copy page LangChain is the easy way to start building completely custom agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and more . LangChain provides a prebuilt agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications. LangChain vs. LangGraph vs. Deep Agents If you are looking to build an agent, we recommend you start with Deep Agents which comes “batteries-included”, with modern features like automatic compression of long conversations, a virtual filesystem, and subagent-spawning for managing and isolating context. Deep Agents are implementations of LangChain agents . If you don't need these capabilities or would like to customize your own for your agents and autonomous applications, start with LangChain. Use LangGraph , our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows and heavy customization."
      },
      {
        "source_id": "b6977b92-cd06-4e01-a91b-930eed06e01b",
        "citation_number": 14,
        "cited_text": "[ Built on top of LangGraph LangChain's agents are built on top of LangGraph. This allows us to take advantage of LangGraph's durable execution, human-in-the-loop support, persistence, and more. Learn more](https://python.langchain.com/oss/python/langgraph/overview) [ Debug with LangSmith Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Learn more](https://python.langchain.com/langsmith/observability)"
      },
      {
        "source_id": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
        "citation_number": 15,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      },
      {
        "source_id": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
        "citation_number": 16,
        "cited_text": "Start with automatic caching. It covers the majority of use cases with minimal effort. Switch to explicit breakpoints only when you need fine-grained control. Key details ¶ Minimum cacheable length: 1,024 tokens for Sonnet; 4,096 tokens for Opus and Haiku 4.5 Cache TTL: 5 minutes by default (refreshed on each hit). A 1-hour TTL is available at 2x base input price. Pricing: Cache writes cost 1.25x base input price. Cache reads cost 0.1x base input price. Breakpoint limit: Up to 4 explicit breakpoints per request. Automatic caching uses one slot."
      },
      {
        "source_id": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
        "citation_number": 17,
        "cited_text": "There are two ways to enable prompt caching: Automatic caching (recommended): Add a single cache_control field at the top level of your request. The system automatically manages cache breakpoints for you. Explicit cache breakpoints : Place cache_control on individual content blocks for fine-grained control over exactly what gets cached. This cookbook demonstrates both approaches, starting with the simpler automatic method. Setup ¶ In [1]: In [2]: Let's fetch the full text of Pride and Prejudice (~187k tokens) to use as our large context."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 18,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 19,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 20,
        "cited_text": "Building Effective AI Agents \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Building effective agents Published Dec 19, 2024 We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks. Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 21,
        "cited_text": "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough. When and how to use frameworks There are many frameworks that make agentic systems easier to implement, including: The Claude Agent SDK ; Strands Agents SDK by AWS ; Rivet , a drag and drop GUI LLM workflow builder; and Vellum , another GUI tool for building and testing complex workflows."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「Prompt Chaining（提示词链）」与「Routing（路由）」是构建**可预测、工业级**生成式 AI 系统的基石。以下是基于来源资料的真实应用场景、部署方案、性能基准及开发者实战经验的详细列举：\n\n### 1. 真实应用场景与案例\n这些工作流模式已在多个行业领域得到验证：\n\n*   **客户支持（Customer Support）**：\n    *   **应用案例**：**Dentsu Creative** 利用 Amazon Bedrock Flows 将客户服务解决方案与 Claude Haiku 连接，处理常见查询，节省了大量人力成本 [1]。\n    *   **Routing 模式**：将输入分类为“一般问题”、“退款申请”或“技术支持”，分别导向专门的提示词、工具和下游流程 [2, 3]。\n*   **代码开发与软件工程（Coding Agents）**：\n    *   **应用案例**：Anthropic 开发了专门的编码 Agent 来解决 **SWE-bench** 任务（基于 PR 描述自动修改多个文件并修复 GitHub 问题）[4, 5]。\n    *   **Orchestrator-Workers 模式**：中央 LLM 动态分解复杂的代码修改任务，分发给多个工作者模型执行，最后汇总结果 [6, 7]。\n*   **文档创作与内容转化**：\n    *   **应用案例**：**Thomson Reuters** 使用多提示词工作流（Multi-prompt workflows）来构建复杂的生成式 AI 功能，实现法律或商业文档的精准处理 [8, 9]。\n    *   **Prompt Chaining 模式**：先生成大纲 $\\rightarrow$ 检查大纲逻辑 $\\rightarrow$ 最终根据大纲撰写正文 [10]。\n\n### 2. 工业级部署方案与开源实战\n企业级部署侧重于**可观测性、版本控制和无服务器架构**：\n\n*   **可视化编排（Amazon Bedrock Flows）**：提供直观的视觉构建器，允许开发者通过拖拽 Prompts、Agents、知识库和 Lambda 函数来创建流程，无需编写编排代码 [11]。\n*   **API 驱动的解耦架构（OpenAI Responses API）**：将传统的 Assistant 对象迁移为版本化的 **Prompts**。这种模式实现了“关注点分离”：应用代码负责任务编排（如工具循环、重试），而 Prompt 负责高层行为和约束 [12, 13]。\n*   **受控工作流框架（LangGraph）**：相比于简单的链式调用，LangGraph 支持构建具有**持久性（Persistence）**、**循环逻辑**和**人机交互（Human-in-the-loop）**的复杂状态机工作流 [14-16]。\n\n### 3. 性能基准数据\n可预测的工作流通过牺牲部分灵活性换取了极高的效率和准确率：\n\n*   **StateFlow（状态驱动工作流）**：\n    *   在 InterCode SQL 任务中，成功率比 ReAct 模式高出 **13%**，成本降低 **5 倍** [17]。\n    *   在 ALFWorld 任务中，成功率高出 **28%**，成本降低 **3 倍** [17]。\n*   **RouteLLM（学习路由）**：\n    *   在不牺牲响应质量的前提下，通过动态选择强/弱模型，可将推理**成本降低 2 倍以上** [18]。\n*   **提示词缓存（Prompt Caching）**：\n    *   对于重复性任务，可将**成本降低高达 90%**，**延迟缩短 2 倍以上** [19]。\n\n### 4. 开发者最佳实践\n成功构建 AI 工作流的核心原则包括：\n\n*   **保持简洁（Simplicity First）**：不要过度设计。优先尝试优化单个提示词或简单的 RAG，只有在简单方案失效时才引入复杂的工作流或 Agent [20-22]。\n*   **代理-计算机接口（ACI）优化**：\n    *   **文档化与示例**：像为初级开发人员写文档一样编写工具定义，包括边界情况和示例用法 [23]。\n    *   **绝对路径**：在开发文件处理 Agent 时，使用**绝对路径**而非相对路径，以避免 Agent 在切换工作目录后出错 [24]。\n*   **透明化规划**：明确显示 Agent 的规划步骤，以便于调试和用户信任 [25]。\n*   **版本化行为配置文件**：将提示词作为可追溯、可回滚的版本化对象管理，支持 A/B 测试 [13, 26, 27]。\n\n### 5. 常见踩坑经验与反思\n*   **过度抽象的框架陷阱**：一些高层框架会隐藏底层的提示词和响应细节，导致**难以调试**。建议直接使用 API 或确保理解框架底层的逻辑 [28]。\n*   **输出格式负担**：要求模型生成复杂的 diff 格式或带转义的 JSON 会显著增加出错率。应选择模型在互联网文本中更常见的自然格式（如 Markdown 内部的代码块）[29, 30]。\n*   **忽略环境反馈**：Agent 如果不能从环境（如工具调用结果或测试运行器）中获得“地面的真相（Ground Truth）”，容易产生幻觉并不断累积错误 [4, 31]。",
    "conversation_id": "f129feb2-3053-49b6-bd5d-2ff2e38f1d4b",
    "sources_used": [
      "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "0a874637-027e-4994-9598-74d590bf14b9",
      "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "faeba007-37d1-42b6-a99e-847af50d9857",
      "59f38c05-3e11-42a4-8f0b-33e2e4587d3d"
    ],
    "citations": {
      "1": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "2": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "3": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "4": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "5": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "6": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "7": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "8": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "9": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "10": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "11": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "12": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "13": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "14": "0a874637-027e-4994-9598-74d590bf14b9",
      "15": "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "16": "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "17": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "18": "faeba007-37d1-42b6-a99e-847af50d9857",
      "19": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
      "20": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "21": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "22": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "23": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "24": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "25": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "26": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
      "27": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "28": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "29": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "30": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "31": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705"
    },
    "references": [
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 1,
        "cited_text": "— Laura Skylaki, VP of Artificial Intelligence, Business Intelligence and Data Platforms at Thomson Reuters Dentsu Creative Dentsu Creative is a global creative agency network designed to create meaningful connection between brands and consumers. \"We have successfully leveraged Amazon Bedrock Flows to transform customer experiences. Using Bedrock Flows, we accelerated the process of reshaping books into an easy-to-read format for readers with learning disabilities. Bedrock Flows also enabled us to easily connect customer service solutions with foundation models like Claude Haiku to address common inquiries, saving hours and allowing customer support team to focus on more complex requests. By empowering non-technical users to understand how AI and business logic are applied with the intuitive visual interface, Bedrock Flows has driven transparency and visibility for generative AI solutions in our organization. Whether reaching new audiences or scaling customer requests, Dentsu continues to innovate with cutting-edge generative AI technology powered by Amazon Bedrock Flows.\""
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 2,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 3,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 4,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 5,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 6,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 7,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 8,
        "cited_text": "Prompt Flows is available in Amazon Bedrock Studio, an SSO-enabled web interface that provides the easiest way for developers across an organization to experiment and collaborate with access to FMs. You can collaborate directly with your teammates to create, evaluate and deploy the right prompt flows for your use case. Customer Quotes Thomson Reuters Dentsu Creative Thomson Reuters ThomsonReuterstransforms **** the way professionals work by delivering innovative tech and GenAI powered by trusted expertise and industry-leading insights."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 9,
        "cited_text": "\"The mandate of the Thomson Reuters Enterprise AI Platform is to enable our subject-matter experts, engineers, and AI researchers to co-create Gen-AI capabilities that bring cutting-edge, trusted technology in the hands of our customers and shape the way professionals work. Bedrock Flows will enable us to create complex, flexible, multi-prompt workflows which we can easily evaluate, compare and version. We can also quickly integrate flows with our applications using the SDK APIs for serverless flow execution — without wasting time in deployment and infrastructure management. We are excited about the potential productivity gain and acceleration for generative-AI application development with Bedrock Flows.\""
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 10,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 11,
        "cited_text": "Black White Red Green Blue Yellow Magenta Cyan Opacity Transparent Semi-Transparent Opaque Font Size 50% 75% 100% 125% 150% 175% 200% 300% 400% Text Edge Style None Raised Depressed Uniform Drop shadow Font Family Proportional Sans-Serif Monospace Sans-Serif Proportional Serif Monospace Serif Casual Script Small Caps Reset Done Close Modal Dialog End of dialog window. Quickly build generative AI workflows visually Bedrock Flows accelerates the creation, testing, and deployment of user-defined workflows for generative AI applications through an intuitive visual builder. You can seamlessly drag, drop and link Prompts, Agents, Knowledge bases, Guardrails, Lex, Lambda, other AWS services, with business logic to create a workflow. This removes the need to write code and offers easy customization of the business logic. You can also create and updates flows using APIs or AWS Cloud Development Kit."
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 12,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 13,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "0a874637-027e-4994-9598-74d590bf14b9",
        "citation_number": 14,
        "cited_text": "If you're looking for more advanced customization or agent orchestration, check out LangGraph , our framework for building controllable agent workflows. Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangChain ecosystem While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. Deep Agents — Build agents that can plan, use subagents, and leverage file systems for complex tasks LangGraph — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework Integrations — Chat & embedding models, tools & toolkits, and more LangSmith — Agent evals, observability, and debugging for LLM apps LangSmith Deployment — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows"
      },
      {
        "source_id": "b6977b92-cd06-4e01-a91b-930eed06e01b",
        "citation_number": 15,
        "cited_text": "Copy page LangChain is the easy way to start building completely custom agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and more . LangChain provides a prebuilt agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications. LangChain vs. LangGraph vs. Deep Agents If you are looking to build an agent, we recommend you start with Deep Agents which comes “batteries-included”, with modern features like automatic compression of long conversations, a virtual filesystem, and subagent-spawning for managing and isolating context. Deep Agents are implementations of LangChain agents . If you don't need these capabilities or would like to customize your own for your agents and autonomous applications, start with LangChain. Use LangGraph , our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows and heavy customization."
      },
      {
        "source_id": "b6977b92-cd06-4e01-a91b-930eed06e01b",
        "citation_number": 16,
        "cited_text": "[ Built on top of LangGraph LangChain's agents are built on top of LangGraph. This allows us to take advantage of LangGraph's durable execution, human-in-the-loop support, persistence, and more. Learn more](https://python.langchain.com/oss/python/langgraph/overview) [ Debug with LangSmith Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Learn more](https://python.langchain.com/langsmith/observability)"
      },
      {
        "source_id": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
        "citation_number": 17,
        "cited_text": "arXiv:2403.11322 (cs) [Submitted on 17 Mar 2024 ( v1 ), last revised 14 Sep 2024 (this version, v5)] Title: StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows Authors: Yiran Wu , Tianwei Yue , Shaokun Zhang , Chi Wang , Qingyun Wu View a PDF of the paper titled StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows, by Yiran Wu and 4 other authors View PDF HTML (experimental) Abstract: It is a notable trend to use Large Language Models (LLMs) to tackle complex tasks, e.g., tasks that require a sequence of actions and dynamic interaction with tools and external environments. In this paper, we propose StateFlow, a novel LLM-based task-solving paradigm that conceptualizes complex task-solving processes as state machines. In StateFlow, we distinguish between \"process grounding\" (via state and state transitions) and \"sub-task solving\" (through actions within a state), enhancing control and interpretability of the task-solving procedure. A state represents the status of a running process. The transitions between states are controlled by heuristic rules or decisions made by the LLM, allowing for a dynamic and adaptive progression. Upon entering a state, a series of actions is executed, involving not only calling LLMs guided by different prompts, but also the utilization of external tools as needed. Our results show that StateFlow significantly enhances LLMs' efficiency. For instance, StateFlow achieves 13% and 28% higher success rates compared to ReAct in InterCode SQL and ALFWorld benchmark, with 5x and 3x less cost respectively. We also show that StateFlow can be combined with iterative refining methods like Reflexion to further improve performance."
      },
      {
        "source_id": "faeba007-37d1-42b6-a99e-847af50d9857",
        "citation_number": 18,
        "cited_text": "arXiv:2406.18665 (cs) [Submitted on 26 Jun 2024 ( v1 ), last revised 23 Feb 2025 (this version, v4)] Title: RouteLLM: Learning to Route LLMs with Preference Data Authors: Isaac Ong , Amjad Almahairi , Vincent Wu , Wei-Lin Chiang , Tianhao Wu , Joseph E. Gonzalez , M Waleed Kadous , Ion Stoica View a PDF of the paper titled RouteLLM: Learning to Route LLMs with Preference Data, by Isaac Ong and 7 other authors View PDF HTML (experimental) Abstract: Large language models (LLMs) exhibit impressive capabilities across a wide range of tasks, yet the choice of which model to use often involves a trade-off between performance and cost. More powerful models, though effective, come with higher expenses, while less capable models are more cost-effective. To address this dilemma, we propose several efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality. We develop a training framework for these routers leveraging human preference data and data augmentation techniques to enhance performance. Our evaluation on widely-recognized benchmarks shows that our approach significantly reduces costs-by over 2 times in certain cases-without compromising the quality of responses. Interestingly, our router models also demonstrate significant transfer learning capabilities, maintaining their performance even when the strong and weak models are changed at test time. This highlights the potential of these routers to provide a cost-effective yet high-performance solution for deploying LLMs."
      },
      {
        "source_id": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
        "citation_number": 19,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 20,
        "cited_text": "Building Effective AI Agents \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Building effective agents Published Dec 19, 2024 We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks. Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 21,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 22,
        "cited_text": "Combining and customizing these patterns These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity only when it demonstrably improves outcomes. Summary Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 23,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 24,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 25,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "b7531ab7-492c-41fe-a54f-482fe5d6ae42",
        "citation_number": 26,
        "cited_text": "Test and deploy faster with serverless infrastructure You can test your flows directly in the console for faster iteration with built-in traceability of inputs and outputs. Once a flow is ready, you can version the flow and integrate it into your generative AI application. The versioning capability on flows enables an easy rollback mechanism, and A/B testing. You can invoke the flow via an API call to integrate with your application without the need to deploy and manage your own infrastructure. Collaborate on workflow creation"
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 27,
        "cited_text": "Practical migration steps Identify each existing Assistant's instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 28,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 29,
        "cited_text": "There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 30,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 31,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「Prompt Chaining（提示词链）」与「Routing（路由）」领域，2025-2026 年的技术演进正从简单的线性逻辑转向**高度受控的状态驱动架构**与**动态成本性能优化**。以下是根据最新资料整理的研究突破、技术趋势及未来方向：\n\n### 一、 2025-2026 年重要技术趋势与论文突破\n\n1.  **从「无状态链」转向「状态驱动工作流」（State-Driven Workflows）**\n    *   **核心突破**：**StateFlow**（2024年发布，2025年持续演进）提出了将复杂任务建模为**有限状态机（FSM）**的范式 [1]。它区分了“过程接地”（通过状态转换控制流程）和“子任务解决”（在状态内执行行动），显著提升了任务的**可解释性与控制力** [1]。\n    *   **性能提升**：在 ALFWorld 等基准测试中，StateFlow 的成功率比传统的 ReAct 模式高出 **28%**，且成本降低了 **3 倍** [1]。\n\n2.  **基于偏好学习的智能路由（Learning to Route）**\n    *   **重要论文**：**RouteLLM**（2025年2月最新修订版）展示了如何利用**人类偏好数据**训练高效的路由模型 [2, 3]。\n    *   **关键技术**：路由模型可以动态地在强模型（如 GPT-5.4 或 Claude 4.6）与轻量化模型（如 Haiku 4.5）之间切换 [2, 4-6]。这使得在不牺牲响应质量的前提下，**推理成本可降低 2 倍以上** [2]。\n\n3.  **从「持久化助手」转向「版本化行为配置文件」**\n    *   **行业趋势**：OpenAI 宣布将于 2026 年 8 月关闭 Assistants API，全面转向 **Responses API** [7]。\n    *   **技术架构演进**：核心逻辑从“黑盒 API 对象”转变为**可版本化、可差异比对（Diff）且可回滚**的「Prompt（提示词）」对象 [8, 9]。这种模式实现了“关注点分离”：应用代码负责任务编排（如工具循环、重试），而 Prompt 负责高层行为约束 [9]。\n\n### 二、 未解决的挑战\n\n尽管工作流预测性有所提升，但仍面临以下核心挑战：\n*   **错误累积（Compounding Errors）**：在长链条或多步 Agent 任务中，前一步的微小偏差可能导致后续步骤的剧烈偏离，且自主 Agent 的运行成本极高 [10, 11]。\n*   **抽象层负担**：现有的编排框架往往增加了抽象层，**掩盖了底层的提示词和响应细节**，导致开发者难以调试复杂的生成行为 [12]。\n*   **环境接地（Environmental Grounding）不足**：Agent 在执行过程中往往缺乏来自真实环境（如代码执行结果）的即时“地面真相”反馈，容易产生幻觉 [13]。\n*   **延迟与性能的权衡**：多步骤的工作流通常需要牺牲**响应延迟**来换取更高的任务成功率 [14, 15]。\n\n### 三、 未来可能的突破点\n\n1.  **深度智能体（Deep Agents）与子代理生成**\n    *   未来的架构（如 LangChain 推出的 Deep Agents）将具备“自带电池”的特性，包括**长对话的自动压缩**、虚拟文件系统以及**动态衍生子代理（Subagent-spawning）**以隔离任务上下文 [16]。\n\n2.  **统一的实时交互架构**\n    *   未来的 Prompt 配置将实现**跨模式一致性**。同一套行为定义（Prompt）可以无缝应用于普通聊天、流式传输以及低延迟的 **Realtime API** 交互会话，确保在不同交互场景下模型行为的统一 [9, 17]。\n\n3.  **标准化工具集成协议（MCP）**\n    *   **Model Context Protocol（MCP）** 正成为连接 LLM 与第三方工具、API 的标准，这将简化 Prompt Chaining 中工具调用部分的开发难度，实现工具定义的生态互通 [18, 19]。\n\n4.  **大规模提示词缓存（Prompt Caching）的普及**\n    *   随着缓存技术的成熟，重复性工作流的成本将降低 **90%**，延迟缩短 **2 倍**以上。这将使得极其复杂、多步迭代的「评估者-优化者（Evaluator-Optimizer）」模式在经济上变得可行 [20, 21]。",
    "conversation_id": "f129feb2-3053-49b6-bd5d-2ff2e38f1d4b",
    "sources_used": [
      "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "faeba007-37d1-42b6-a99e-847af50d9857",
      "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "dde5fd27-737e-4d07-8a22-8de415da04b4",
      "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "3b1278e6-700e-4d61-9a57-916d05dc052b",
      "59f38c05-3e11-42a4-8f0b-33e2e4587d3d"
    ],
    "citations": {
      "1": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
      "2": "faeba007-37d1-42b6-a99e-847af50d9857",
      "3": "faeba007-37d1-42b6-a99e-847af50d9857",
      "4": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "5": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "6": "dde5fd27-737e-4d07-8a22-8de415da04b4",
      "7": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "8": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "9": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "10": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "11": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "12": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "13": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "14": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "15": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "16": "b6977b92-cd06-4e01-a91b-930eed06e01b",
      "17": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
      "18": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "19": "3b1278e6-700e-4d61-9a57-916d05dc052b",
      "20": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
      "21": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d"
    },
    "references": [
      {
        "source_id": "bad0105a-e3a0-47bd-9b5a-57e511d44831",
        "citation_number": 1,
        "cited_text": "arXiv:2403.11322 (cs) [Submitted on 17 Mar 2024 ( v1 ), last revised 14 Sep 2024 (this version, v5)] Title: StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows Authors: Yiran Wu , Tianwei Yue , Shaokun Zhang , Chi Wang , Qingyun Wu View a PDF of the paper titled StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows, by Yiran Wu and 4 other authors View PDF HTML (experimental) Abstract: It is a notable trend to use Large Language Models (LLMs) to tackle complex tasks, e.g., tasks that require a sequence of actions and dynamic interaction with tools and external environments. In this paper, we propose StateFlow, a novel LLM-based task-solving paradigm that conceptualizes complex task-solving processes as state machines. In StateFlow, we distinguish between \"process grounding\" (via state and state transitions) and \"sub-task solving\" (through actions within a state), enhancing control and interpretability of the task-solving procedure. A state represents the status of a running process. The transitions between states are controlled by heuristic rules or decisions made by the LLM, allowing for a dynamic and adaptive progression. Upon entering a state, a series of actions is executed, involving not only calling LLMs guided by different prompts, but also the utilization of external tools as needed. Our results show that StateFlow significantly enhances LLMs' efficiency. For instance, StateFlow achieves 13% and 28% higher success rates compared to ReAct in InterCode SQL and ALFWorld benchmark, with 5x and 3x less cost respectively. We also show that StateFlow can be combined with iterative refining methods like Reflexion to further improve performance."
      },
      {
        "source_id": "faeba007-37d1-42b6-a99e-847af50d9857",
        "citation_number": 2,
        "cited_text": "arXiv:2406.18665 (cs) [Submitted on 26 Jun 2024 ( v1 ), last revised 23 Feb 2025 (this version, v4)] Title: RouteLLM: Learning to Route LLMs with Preference Data Authors: Isaac Ong , Amjad Almahairi , Vincent Wu , Wei-Lin Chiang , Tianhao Wu , Joseph E. Gonzalez , M Waleed Kadous , Ion Stoica View a PDF of the paper titled RouteLLM: Learning to Route LLMs with Preference Data, by Isaac Ong and 7 other authors View PDF HTML (experimental) Abstract: Large language models (LLMs) exhibit impressive capabilities across a wide range of tasks, yet the choice of which model to use often involves a trade-off between performance and cost. More powerful models, though effective, come with higher expenses, while less capable models are more cost-effective. To address this dilemma, we propose several efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality. We develop a training framework for these routers leveraging human preference data and data augmentation techniques to enhance performance. Our evaluation on widely-recognized benchmarks shows that our approach significantly reduces costs-by over 2 times in certain cases-without compromising the quality of responses. Interestingly, our router models also demonstrate significant transfer learning capabilities, maintaining their performance even when the strong and weak models are changed at test time. This highlights the potential of these routers to provide a cost-effective yet high-performance solution for deploying LLMs."
      },
      {
        "source_id": "faeba007-37d1-42b6-a99e-847af50d9857",
        "citation_number": 3,
        "cited_text": "<cited_table> Submission history From: Isaac Ong [ view email ] [v1] Wed, 26 Jun 2024 18:10:22 UTC (580 KB) [v2] Mon, 1 Jul 2024 05:38:08 UTC (623 KB) [v3] Sun, 21 Jul 2024 10:33:08 UTC (623 KB) [v4] Sun, 23 Feb 2025 08:50:33 UTC (782 KB) Full-text links:",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Subjects:",
              "Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)"
            ],
            [
              "Cite as:",
              "arXiv:2406.18665"
            ],
            [
              "",
              "(or"
            ],
            [
              "",
              "https://doi.org/10.48550/arXiv.2406.18665"
            ]
          ]
        }
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 4,
        "cited_text": "Community Programs, meetups, and support for builders Start searching API Dashboard Search the API docs Search docs Suggested response_format reasoning_effort streaming tools Primary navigation API API Reference Codex ChatGPT Resources Search docs Suggested response_format reasoning_effort streaming tools Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API"
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 5,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "dde5fd27-737e-4d07-8a22-8de415da04b4",
        "citation_number": 6,
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
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 7,
        "cited_text": "Assistants migration guide Migrate from the Assistants API to the Responses API. After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the migration guide to update your integration. Learn more . We're moving from the Assistants API to the new Responses API for a simpler and more flexible mental model. Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like deep research , MCP , and computer use . This change also lets you manage conversations instead of passing back previous_response_id ."
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
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
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 9,
        "cited_text": "Why this is helpful Portability and versioning : You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version. Separation of concerns : Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults). Realtime compatibility : The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions. Tool and output consistency : Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 10,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 11,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 12,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 13,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 14,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 15,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "b6977b92-cd06-4e01-a91b-930eed06e01b",
        "citation_number": 16,
        "cited_text": "Copy page LangChain is the easy way to start building completely custom agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and more . LangChain provides a prebuilt agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications. LangChain vs. LangGraph vs. Deep Agents If you are looking to build an agent, we recommend you start with Deep Agents which comes “batteries-included”, with modern features like automatic compression of long conversations, a virtual filesystem, and subagent-spawning for managing and isolating context. Deep Agents are implementations of LangChain agents . If you don't need these capabilities or would like to customize your own for your agents and autonomous applications, start with LangChain. Use LangGraph , our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows and heavy customization."
      },
      {
        "source_id": "89aa4ae2-1b44-4a1c-9a79-ea98ee693e12",
        "citation_number": 17,
        "cited_text": "Practical migration steps Identify each existing Assistant's instruction + tool bundle. In the dashboard, recreate that bundle as a named prompt. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically. Think of a prompt as a versioned behavioral profile to plug into either Responses or Realtime API. From threads to conversations"
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 18,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "3b1278e6-700e-4d61-9a57-916d05dc052b",
        "citation_number": 19,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "338b2d7e-87d9-4cef-9ae3-9b9dcca0a705",
        "citation_number": 20,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "59f38c05-3e11-42a4-8f0b-33e2e4587d3d",
        "citation_number": 21,
        "cited_text": "Latest commit PedramNavid docs(misc): update prompt caching cookbook with automatic caching ( #387 ) success 2 months ago 419ce35 · 2 months ago History History Open commit details History 640 lines (640 loc) · 22.4 KB main Breadcrumbs claude-cookbooks / misc / prompt_caching.ipynb Top File metadata and controls Preview Code Blame 640 lines (640 loc) · 22.4 KB Raw Copy raw file Download raw file Edit and raw actions Prompt caching with the Claude API ¶ Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks."
      }
    ]
  }
}
