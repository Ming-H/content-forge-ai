# 知识库：Agent-Computer Interface 设计：工具即提示工程

生成时间: 2026-04-03 13:14
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "「Agent-Computer Interface（ACI）设计：工具即提示工程」的核心理念在于，**工具的定义、文档和接口设计应被视为提示工程的一个分支**，旨在通过优化智能体与计算机交互的界面，提升大型语言模型（LLM）调用工具的准确性和效率 [1-3]。\n\n以下是基于提供的来源对该技术的架构与关键组件的概述：\n\n### 1. 核心技术架构与关键组件\nACI 的设计架构建立在**增强型大语言模型（Augmented LLM）**这一基础构建块之上，通过集成检索、工具和记忆功能，使模型能够主动生成查询并选择工具 [4, 5]。\n\n*   **智能体-计算机界面 (ACI)**：这是为智能体量身定制的软件接口（如 SWE-agent），允许智能体自主创建、编辑代码文件、导航仓库以及执行程序 [6]。\n*   **工具定义与文档 (Tool Documentation)**：工具的结构定义（如 JSON 架构）和详细描述是 ACI 的核心。良好的定义应包括示例用法、输入格式要求和边界说明，其重要性等同于整体提示词设计 [2, 7, 8]。\n*   **模型上下文协议 (MCP)**：一种通用的客户端实现方式，允许开发者通过简单的接口将智能体与第三方工具生态系统集成 [5, 9]。\n*   **智能体循环 (Agentic Loop)**：智能体在交互中获取环境的“地面真值”（如工具返回结果或代码执行输出），并基于反馈进行推理、规划和错误修复的闭环过程 [10, 11]。\n\n### 2. 技术演进路线\n智能体系统的复杂性呈现出阶梯式的演进 [4]：\n1.  **单次 LLM 调用**：通过检索（Retrieval）和上下文示例优化性能 [12]。\n2.  **简单工作流 (Workflows)**：通过预定义的代码路径编排 LLM 任务，如**提示链 (Prompt Chaining)**、**路由 (Routing)** 和**并行化 (Parallelization)** [13-16]。\n3.  **复杂工作流**：引入动态分配任务的模式，如**编排者-工作者 (Orchestrator-Workers)** 和循环迭代的**评估者-优化者 (Evaluator-Optimizer)** [17, 18]。\n4.  **自主智能体 (Autonomous Agents)**：模型能够动态指挥自身进程和工具使用，处理无法预设固定路径的开放式问题 [13, 19]。\n\n### 3. 核心算法与方法名称\n*   **DFSDT (Depth-First Search based Decision Tree)**：一种基于深度优先搜索的决策树方法，用于提升模型在复杂指令下的规划和推理能力，显著优于传统的 CoT 或 ReACT [20, 21]。\n*   **Chain of Hindsight (CoH)**：用于训练 **Agentic Transformer (AT)**，通过将轨迹经验按奖励排序并重新标记目标回报，使模型能够从亚优数据中学习改进 [22]。\n*   **ReACT**：一种经典的推理与行动结合的方法，常作为智能体性能评估的基准（Baseline）[20, 23]。\n*   **工具搜索 (Tool Search)**：当工具集过大时，模型先搜索相关工具再加载到上下文中的一种动态加载技术 [24, 25]。\n\n### 4. 主要架构模式\n*   **提示链模式**：将任务分解为固定序列，每一步的输出作为下一步的输入，并辅以编程检查点（Gate）[14]。\n*   **评估者-优化者模式**：一个 LLM 生成响应，另一个 LLM 提供反馈循环，类似人类的润色过程 [18]。\n*   **Poka-yoke 设计原则**：在 ACI 设计中应用“防错”理念，通过修改工具参数使模型难以犯错（例如要求使用绝对路径而非相对路径）[7, 26]。\n*   **客户端与服务端执行 (Client/Server-side execution)**：工具既可以在本地应用中运行（如 bash），也可以在智能体平台的基础设施上运行（如 web\\_search）[27]。\n\n### 5. 关键技术指标\n*   **解决率 (Pass Rate / % Resolved)**：衡量智能体成功完成任务（如 SWE-bench 漏洞修复）的比例。例如，SWE-agent 在 SWE-bench 上的 pass@1 达到 12.5% [6, 28]。\n*   **胜率 (Win Rate)**：通过比较两个模型的动作序列，衡量一个模型相对于基准模型（如 ChatGPT-ReACT）被评价者偏好的程度 [23, 28, 29]。\n*   **系统提示令牌开销 (System Prompt Tokens)**：启用工具使用功能所需的额外令牌数。例如，Claude Opus 4.6 在开启工具选择时的系统提示约为 313-346 个令牌 [30, 31]。\n*   **延迟与成本 (Latency & Cost)**：智能体系统通常会以更高的延迟和成本为代价，换取更强的任务性能 [13, 32, 33]。",
    "conversation_id": "80460170-aa1a-41b8-843e-a16c9f82f508",
    "sources_used": [
      "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "d14c795c-08d1-41ad-9059-b803289a27fb",
      "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "33d910bb-570b-4cd3-b789-6b75c097af26"
    ],
    "citations": {
      "1": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "2": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "3": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "4": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "5": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "6": "d14c795c-08d1-41ad-9059-b803289a27fb",
      "7": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "8": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "9": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "10": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "11": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "12": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "13": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "14": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "15": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "16": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "17": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "18": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "19": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "20": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "21": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "22": "33d910bb-570b-4cd3-b789-6b75c097af26",
      "23": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "24": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "25": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "26": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "27": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "28": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "29": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "30": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "31": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "32": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "33": "7efb95f7-fe12-45e9-b579-5dc7e858777d"
    },
    "references": [
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 1,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 2,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 3,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 4,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 5,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "d14c795c-08d1-41ad-9059-b803289a27fb",
        "citation_number": 6,
        "cited_text": "Computer Science > Software Engineering arXiv:2405.15793 (cs) [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 7,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 8,
        "cited_text": "Responses Copy Page More page actions Function calling Give models access to new functionality and data they can use to follow instructions and respond to prompts. Function calling (also known as tool calling ) provides a powerful and flexible way for OpenAI models to interface with external systems and access data outside their training data. This guide shows how you can connect a model to data and actions provided by your application. We'll show how to use function tools (defined by a JSON schema) and custom tools which work with free form text inputs and outputs."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 9,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 10,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 11,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 12,
        "cited_text": "When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough. When and how to use frameworks There are many frameworks that make agentic systems easier to implement, including: The Claude Agent SDK ; Strands Agents SDK by AWS ; Rivet , a drag and drop GUI LLM workflow builder; and Vellum , another GUI tool for building and testing complex workflows."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 13,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 14,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 15,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 16,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 17,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 18,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 19,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 20,
        "cited_text": "✨Here is an overview of the dataset construction, training, and evaluation. ✨✨Features: API Collection : we gather 16464 representational state transfer (REST) APIs from RapidAPI , a platform that hosts massive real-world APIs provided by developers. Instruction Generation : we curate instructions that involve both single-tool and multi-tool scenarios. Answer Annotation : we develop a novel depth-first search based decision tree (DFSDT) to bolster the planning and reasoning ability of LLMs, which significantly improves the annotation efficiency and successfully annotates those complex instructions that cannot be answered with CoT or ReACT. We provide responses that not only include the final answer but also incorporate the model's reasoning process, tool execution, and tool execution results . API Retriver : we incorporate API retrieval to equip ToolLLaMA with open-domain tool-using abilities. All the data is automatically generated by OpenAI API and filtered by us, the whole data creation process is easy to scale up."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 21,
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
        "source_id": "33d910bb-570b-4cd3-b789-6b75c097af26",
        "citation_number": 22,
        "cited_text": "arXiv:2305.16554 (cs) [Submitted on 26 May 2023] Title: Emergent Agentic Transformer from Chain of Hindsight Experience Authors: Hao Liu , Pieter Abbeel View a PDF of the paper titled Emergent Agentic Transformer from Chain of Hindsight Experience, by Hao Liu and Pieter Abbeel View PDF Abstract: Large transformer models powered by diverse data and model scale have dominated natural language modeling and computer vision and pushed the frontier of multiple AI areas. In reinforcement learning (RL), despite many efforts into transformer-based policies, a key limitation, however, is that current transformer-based policies cannot learn by directly combining information from multiple sub-optimal trials. In this work, we address this issue using recently proposed chain of hindsight to relabel experience, where we train a transformer on a sequence of trajectory experience ascending sorted according to their total rewards. Our method consists of relabelling target return of each trajectory to the maximum total reward among in sequence of trajectories and training an autoregressive model to predict actions conditioning on past states, actions, rewards, target returns, and task completion tokens, the resulting model, Agentic Transformer (AT), can learn to improve upon itself both at training and test time. As we show on D4RL and ExoRL benchmarks, to the best our knowledge, this is the first time that a simple transformer-based model performs competitively with both temporal-difference and imitation-learning-based approaches, even from sub-optimal data. Our Agentic Transformer also shows a promising scaling trend that bigger models consistently improve results."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 23,
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
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 24,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 25,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 26,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 27,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 28,
        "cited_text": "Web UI The app will be available on http://localhost:3000/ Backend server This server will be available on http://localhost:5000/ . To start a request, call http://localhost:5000/stream with a GET or POST request containing a JSON object with the following fields: ToolEval By fine-tuning LLaMA on ToolBench, we obtain ToolLLaMA . Considering that human evaluation can be time-consuming, we follow AlpacaEval to develop an efficient machine evaluator ToolEval , which incorporates two evaluation metrics: Pass Rate : Calculates the proportion of successfully completing an instruction within limited OpenAI API calls. Preference : Measured by comparing two answers (action sequences) for a given instruction. We pre-define a set of criteria for a better answer, which are organized as prompts for ChatGPT. We provide the test instruction and two candidate answers to the evaluator and obtain its preference. We evaluate each answer pair multiple times to improve the reliability of our system. Then we calculate the Win Rate (percentage of being preferred by the evaluator). More details can be found in our paper."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 29,
        "cited_text": "Win rate. The below example take ChatGPT-ReACT as reference model and GPT4-ReACT as candidate model. Notice that you need to get both model's pass rate results first, then run the following commands to evaluate the preference result of GPT4-ReACT: The result files will be stored under the ${SAVE_PATH}. Please refer to ToolEval for more details. 📊 Model Experiments Results In our main experiments, ToolLLaMA(v2) demonstrates a compelling capability to handle both single-tool and complex multi-tool instructions, which on a par with ChatGPT. Below are the main results. Win rate for each model is compared with ChatGPT-ReACT."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 30,
        "cited_text": "The additional tokens from tool use come from: The tools parameter in API requests (tool names, descriptions, and schemas) tool_use content blocks in API requests and responses tool_result content blocks in API requests When you use tools , we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 31,
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
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 32,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 33,
        "cited_text": "Tool use examples For a complete hands-on walkthrough, see the tutorial . For reference examples of individual concepts, see Define tools and Handle tool calls . What happens when Claude needs more information Pricing Tool use requests are priced based on: The total number of input tokens sent to the model (including in the tools parameter) The number of output tokens generated For server-side tools, additional usage-based pricing (e.g., web search charges per search performed) Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「Agent-Computer Interface（ACI）设计：工具即提示工程」的核心理念是将**工具的设计、文档描述及接口规范**视为提示工程的关键组成部分，通过为大型语言模型（LLM）量身定制交互界面，显著提升智能体在复杂环境（如软件工程、网络搜索）中的自主执行能力 [1, 2]。\n\n以下是该设计的实现细节：\n\n### 1. 核心算法流程\nACI 设计并不依赖单一算法，而是多种策略的组合，其核心流程通常遵循**智能体循环（Agentic Loop）** [3, 4]：\n*   **DFSDT（基于深度优先搜索的决策树）**：在 ToolBench 中被用于加强 LLM 的规划和推理。它能自动标注复杂的指令路径，成功解决传统 CoT（思维链）或 ReACT 无法处理的任务 [5, 6]。\n*   **Chain of Hindsight（事后链）经验学习**：用于训练 **Agentic Transformer (AT)**。该方法将轨迹经验按奖励排序，让模型从亚优数据中学习如何逐步改进动作序列 [7]。\n*   **反馈驱动的迭代**：智能体通过工具获取环境的“地面真值”（Ground Truth），如代码执行结果或 API 返回值，并基于此反馈进行推理、规划和错误修复 [3, 8]。\n\n### 2. 关键代码架构\nACI 强调将 LLM 与外部增强功能集成的结构化方式：\n*   **增强型 LLM 架构**：以 LLM 为核心，集成**检索（Retrieval）、工具（Tools）和记忆（Memory）**三大组件 [9]。\n*   **模型上下文协议 (MCP)**：一种通用的客户端/服务器架构模式，允许开发者通过简单的接口将智能体与第三方工具生态系统集成，无需为每个工具编写复杂的封装代码 [10, 11]。\n*   **结构化输出与 Strict Mode**：利用 JSON Schema 定义函数工具。开启 **Strict Mode**（严格模式）可强制模型输出必须 100% 符合预定义的 Schema，通过结构化输出降低解析错误 [12, 13]。\n*   **自定义语法约束（CFG）**：使用 Lark 或 Regex 等上下文无关语法来约束模型对自定义工具的输入，确保生成的代码或指令在语法上绝对正确 [14, 15]。\n\n### 3. 性能优化策略\nACI 的核心在于通过“防错”设计和资源管理提升效率：\n*   **Poka-yoke（防错）设计**：在设计工具参数时消除歧义。例如，SWE-agent 将工具修改为**仅接受绝对路径**而非相对路径，彻底解决了模型在切换工作目录后出现的定位错误 [16, 17]。\n*   **工具搜索 (Tool Search)**：当工具集庞大时，不一次性加载所有定义，而是让模型先搜索相关工具再按需加载。这在 **GPT-5.4** 及更高版本中被用于节省上下文窗口空间并降低干扰 [18, 19]。\n*   **Prompt Caching（提示词缓存）**：对于频繁使用的工具定义和系统提示，利用缓存机制减少重复计算的延迟并降低令牌成本 [20, 21]。\n*   **预留“思考空间”**：在生成最终工具调用前，允许模型输出思考过程（Thinking Tokens），避免因缺乏推理步骤而直接输出错误的参数 [22, 23]。\n\n### 4. 竞品技术对比与数据\n下表总结了基于 ACI 设计的代表性系统及其技术指标：\n\n| 指标维度 | SWE-agent [2] | ToolLLaMA (DFSDT) [24] | Claude 4.5/4.6 (Native) [25] |\n| :--- | :--- | :--- | :--- |\n| **核心优势** | 专门为软件工程定制的命令行界面 ACI | 使用 DFSDT 自动生成的 12.6w+ 指令数据微调 | 原生集成高推理能力与 ACI 最佳实践 |\n| **SWE-bench 解决率** | **12.5%** (Pass@1) | 29% - 66.7% (视数据集版本) | **75.6% - 76.8%** (Verified 版本) |\n| **系统提示开销** | 未明确 (取决于 CLI 工具数) | 依赖于检索到的工具数量 | 开启工具功能需 **313 - 346 tokens** [26] |\n| **实现复杂度** | 中等 (需配置 Sandbox 环境) | 高 (涉及复杂的微调流程) | 低 (直接调用 API 即可使用) |\n\n**关键结论：**\n*   **数据驱动的效率**：Mini-SWE-agent 仅用 **100 行 Python 代码**结合优化的 ACI 设计，就在 SWE-bench Verified 上达到了高达 **74%** 的解决率，证明了界面设计比复杂框架更重要 [27]。\n*   **工具数量的影响**：研究建议初始可用工具应少于 **20 个** 以保持高准确度，超量时应采用工具搜索技术 [28]。\n*   **成本权衡**：智能体系统通过增加调用次数和令牌开销（如 Claude Haiku 4.5 开启工具需额外 313 tokens）来换取复杂任务的成功解决 [26, 29]。",
    "conversation_id": "80460170-aa1a-41b8-843e-a16c9f82f508",
    "sources_used": [
      "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "d14c795c-08d1-41ad-9059-b803289a27fb",
      "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "33d910bb-570b-4cd3-b789-6b75c097af26",
      "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "e32e9ece-5360-4b79-8fc4-e87c0aa239e7"
    ],
    "citations": {
      "1": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "2": "d14c795c-08d1-41ad-9059-b803289a27fb",
      "3": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "4": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "5": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "6": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "7": "33d910bb-570b-4cd3-b789-6b75c097af26",
      "8": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "9": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "10": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "11": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "12": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "13": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "14": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "15": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "16": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "17": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "18": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "19": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "20": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "21": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "22": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "23": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "24": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "25": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
      "26": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "27": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
      "28": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "29": "277e2bdc-ca16-497e-b84e-106ac473c89e"
    },
    "references": [
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 1,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "d14c795c-08d1-41ad-9059-b803289a27fb",
        "citation_number": 2,
        "cited_text": "Computer Science > Software Engineering arXiv:2405.15793 (cs) [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 3,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 4,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 5,
        "cited_text": "✨Here is an overview of the dataset construction, training, and evaluation. ✨✨Features: API Collection : we gather 16464 representational state transfer (REST) APIs from RapidAPI , a platform that hosts massive real-world APIs provided by developers. Instruction Generation : we curate instructions that involve both single-tool and multi-tool scenarios. Answer Annotation : we develop a novel depth-first search based decision tree (DFSDT) to bolster the planning and reasoning ability of LLMs, which significantly improves the annotation efficiency and successfully annotates those complex instructions that cannot be answered with CoT or ReACT. We provide responses that not only include the final answer but also incorporate the model's reasoning process, tool execution, and tool execution results . API Retriver : we incorporate API retrieval to equip ToolLLaMA with open-domain tool-using abilities. All the data is automatically generated by OpenAI API and filtered by us, the whole data creation process is easy to scale up."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 6,
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
        "source_id": "33d910bb-570b-4cd3-b789-6b75c097af26",
        "citation_number": 7,
        "cited_text": "arXiv:2305.16554 (cs) [Submitted on 26 May 2023] Title: Emergent Agentic Transformer from Chain of Hindsight Experience Authors: Hao Liu , Pieter Abbeel View a PDF of the paper titled Emergent Agentic Transformer from Chain of Hindsight Experience, by Hao Liu and Pieter Abbeel View PDF Abstract: Large transformer models powered by diverse data and model scale have dominated natural language modeling and computer vision and pushed the frontier of multiple AI areas. In reinforcement learning (RL), despite many efforts into transformer-based policies, a key limitation, however, is that current transformer-based policies cannot learn by directly combining information from multiple sub-optimal trials. In this work, we address this issue using recently proposed chain of hindsight to relabel experience, where we train a transformer on a sequence of trajectory experience ascending sorted according to their total rewards. Our method consists of relabelling target return of each trajectory to the maximum total reward among in sequence of trajectories and training an autoregressive model to predict actions conditioning on past states, actions, rewards, target returns, and task completion tokens, the resulting model, Agentic Transformer (AT), can learn to improve upon itself both at training and test time. As we show on D4RL and ExoRL benchmarks, to the best our knowledge, this is the first time that a simple transformer-based model performs competitively with both temporal-difference and imitation-learning-based approaches, even from sub-optimal data. Our Agentic Transformer also shows a promising scaling trend that bigger models consistently improve results."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 8,
        "cited_text": "Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness. B. Coding agents The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because: Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 9,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 10,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 11,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 12,
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
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 13,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 14,
        "cited_text": "Custom tool calling example python Just as before, the output array will contain a tool call generated by the model. Except this time, the tool call input is given as plain text. Context-free grammars A context-free grammar (CFG) is a set of rules that define how to produce valid text in a given format. For custom tools, you can provide a CFG that will constrain the model's text input for a custom tool. You can provide a custom CFG using the grammar parameter when configuring a custom tool. Currently, we support two CFG syntaxes when defining grammars: lark and regex ."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 15,
        "cited_text": "Lark CFG Lark context free grammar example python The output from the tool should then conform to the Lark CFG that you defined: Grammars are specified using a variation of Lark . Model sampling is constrained using LLGuidance . Some features of Lark are not supported: Lookarounds in lexer regexes Lazy modifiers ( *? , +? , ?? ) in lexer regexes Priorities of terminals Templates Imports (other than built-in %import common) %declare s We recommend using the Lark IDE to experiment with custom grammars."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 16,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 17,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 18,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 19,
        "cited_text": "Token Usage Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using tool search so deferred tools are loaded only when needed. It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 20,
        "cited_text": "When to use allowed_tools You might want to configure an allowed_tools list in case you want to make only a subset of tools available across model requests, but not modify the list of tools you pass in, so you can maximize savings from prompt caching . You can also set tool_choice to \"none\" to imitate the behavior of passing no functions. When you use tool search, tool_choice still applies to the tools that are currently callable in the turn. This is most useful after you load a subset of tools and want to constrain the model to that subset."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 21,
        "cited_text": "Tools Overview How tool use works Tutorial: Build a tool-using agent Define tools Handle tool calls Parallel tool use Tool Runner (SDK) Strict tool use Tool use with prompt caching Server tools Troubleshooting Tool reference Web search tool Web fetch tool Code execution tool Memory tool Bash tool Computer use tool Text editor tool Tool infrastructure Manage tool context Tool combinations Tool search Programmatic tool calling Fine-grained tool streaming Context management Context windows Compaction Context editing Prompt caching Token counting"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 22,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 23,
        "cited_text": "Tool use with Claude - Claude API Docs Loading... Developer Guide API Reference MCP Resources Release Notes English Log in Search... ⌘K First steps Intro to Claude Quickstart Models & pricing Models overview Choosing a model What's new in Claude 4.6 Migration guide Model deprecations Pricing Build with Claude Features overview Using the Messages API Handling stop reasons Prompting best practices Model capabilities Extended thinking Adaptive thinking Effort Fast mode (beta: research preview) Structured outputs Citations Streaming Messages Batch processing PDF support Search results Multilingual support Embeddings Vision"
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 24,
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
        "source_id": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
        "citation_number": 25,
        "cited_text": "2.0.0 [-] 🆕 MiniMax M2.5 (high reasoning) 75.80 $0.07 2026-02-17 2.0.0 [-] 🆕 Claude Opus 4.6 75.60 $0.55 2026-02-17 2.0.0 [-] 🆕 GPT-5-2 Codex 72.80 $0.45 2026-02-19 2.0.0 [-] 🆕 GLM-5 (high reasoning) 72.80 $0.53 2026-02-17 2.0.0 [-] 🆕 GPT-5-2 (high reasoning) 72.80 $0.47 2026-02-17 2.0.0 [-] 🆕 GPT 5.2 Codex 72.80 $0.45 2026-02-19 2.0.0 [-] 🆕 Claude 4.5 Sonnet (high reasoning) 71.40 $0.66 2026-02-17 2.0.0 [-] 🆕 Kimi K2.5 (high reasoning) 70.80 $0.15 2026-02-17 2.0.0 [-] 🆕 DeepSeek V3.2 (high reasoning) 70.00 $0.45 2026-02-17"
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
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
        "source_id": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
        "citation_number": 27,
        "cited_text": "SWE-bench Leaderboards SWE-bench SWE-bench Leaderboards Benchmarks SWE-bench SWE-bench Verified SWE-bench Multilingual SWE-bench Multimodal SWE-bench Lite About Paper Docs Blog Contact Citations Press Submit SWE-bench Family mini-SWE-agent SWE-smith CodeClash SWE-ReX SWE-bench CLI SWE-agent (legacy) Official Leaderboards mini-SWE-agent scores up to 74% on SWE-bench Verified in 100 lines of Python code. Click here to learn more."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 28,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 29,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「Agent-Computer Interface（ACI）设计：工具即提示工程」的核心观点是，**为智能体设计的工具接口应当与提示词（Prompt）同等对待**，通过优化交互界面来提升大模型的任务成功率。以下是根据来源整理的真实应用场景、部署方案、案例、数据及实践经验：\n\n### 1. 真实应用场景\n*   **软件工程自动化**：智能体自主定位 GitHub 问题、阅读代码、创建和编辑文件、执行测试并修复漏洞 [1-3]。\n*   **智能客户支持**：结合对话与行动，执行查询订单、下发退款、更新工单等操作 [4]。\n*   **进攻性网络安全**：用于寻找网络安全漏洞或参加 CTF（夺旗赛）挑战 [5, 6]。\n*   **文档与营销自动化**：例如生成营销文案并翻译，或基于大纲自动撰写完整文档 [7]。\n*   **科学研究协助**：解析科学图表（FigQA）和进行复杂的跨源信息搜索与分析 [8]。\n\n### 2. 工业级部署方案\n*   **执行架构：客户端与服务端执行**\n    *   **客户端工具（Client-side Tools）**：由开发者的应用程序在本地执行（如 Bash、文件编辑器），Claude 等模型返回 `tool_use` 块，由应用执行后回传结果 [9, 10]。\n    *   **服务端工具（Server-side Tools）**：由模型供应商直接在基础设施上运行（如网络搜索、代码解释器、Tool Search），开发者直接接收结果 [9, 10]。\n*   **基础设施集成**：主要通过 **Model Context Protocol (MCP)** 协议，允许智能体无缝集成第三方工具生态系统 [11, 12]。工业级部署通常依托于 Amazon Bedrock、Google Cloud Vertex AI 等平台 [13, 14]。\n*   **治理与安全性**：在沙盒环境（Sandboxed Environments）中运行智能体，并使用托管配置、身份验证和防护栏（Guardrails）来确保安全 [1, 15]。\n\n### 3. 开源项目实战案例\n*   **SWE-agent**：由普林斯顿和斯坦福研究人员开发，通过定制的 ACI 让模型能像人类工程师一样操作文件系统 [16, 17]。\n*   **ToolBench / ToolLLaMA**：开源平台，收集了超过 1.6 万个真实 REST API，用于训练 LLM 的通用工具使用能力 [18, 19]。\n*   **Gorilla**：通过微调让 LLaMA 模型在调用庞大 API 库时超越 GPT-4 的性能，有效减少幻觉 [20]。\n*   **Mini-SWE-agent**：仅用 **100 行 Python 代码**实现的极简 Agent，在性能上却能与复杂框架竞争 [21, 22]。\n\n### 4. 性能基准数据\n*   **SWE-bench Verified（漏洞修复成功率）**：\n    *   **Claude 4.5 Opus (high reasoning)**：76.8% [23]。\n    *   **Gemini 3 Flash (high reasoning)**：75.8% [23]。\n    *   **Mini-SWE-agent**：最高可达 74% [22]。\n*   **ToolEval（综合工具使用能力）**：\n    *   **ToolLLaMA (DFSDT)**：在平均通过率（Pass Rate）上达到 66.7% [24]。\n    *   **GPT-4 (DFSDT)**：达到 71.1% [24]。\n*   **成本与令牌消耗**：启用工具功能会产生额外的**系统提示令牌（System Prompt Tokens）**，Claude Opus/Sonnet 4 系列模型通常需要约 **313-346 个令牌** [25]。\n\n### 5. 开发者最佳实践\n*   **Poka-yoke（防错设计）**：通过修改工具参数使模型难以犯错。例如，将文件路径工具从相对路径改为**强制要求绝对路径**，解决了模型在切换工作目录后出现的定位错误 [26, 27]。\n*   **保持界面简洁**：建议初始可用工具**少于 20 个**以确保准确性。对于庞大的工具集，应使用 **Tool Search** 功能按需加载 [28]。\n*   **提供“思考空间”**：在模型输出工具指令前，给予其足够的 Token 进行推理规划（Thinking Tokens），防止直接输出错误参数 [29]。\n*   **启用严格模式（Strict Mode）**：使用 JSON Schema 强制模型输出 100% 符合预定义的结构，确保证书调用的可靠性 [8, 30]。\n*   **透明性设计**：显式展示智能体的规划步骤，以便于人类监控和调试 [31]。\n\n### 6. 常见踩坑经验\n*   **路径跟踪失败**：模型在使用相对路径时，常因为忘记之前执行过 `cd` 命令而导致后续操作失败 [27]。\n*   **复杂框架陷阱**：使用过于复杂的智能体框架会增加抽象层，导致底层的提示词和响应变得难以调试 [32]。\n*   **格式开销过大**：强制模型在输出 JSON 时进行繁琐的转义，或要求其计算代码行数，会极大地增加模型出错的概率 [29, 33]。\n*   **CFG 语法越界**：在使用自定义语法约束（CFG）时，如果规则过于碎片化（Lexer/Parser 分离不当），模型可能会产生语义正确但语法无效的输出（Out-of-distribution） [34, 35]。",
    "conversation_id": "80460170-aa1a-41b8-843e-a16c9f82f508",
    "sources_used": [
      "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "dc1427a5-b141-49e5-8f16-691613af11bc",
      "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "d14c795c-08d1-41ad-9059-b803289a27fb",
      "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "46632339-03c7-4c09-84ea-24187d7b7682",
      "e32e9ece-5360-4b79-8fc4-e87c0aa239e7"
    ],
    "citations": {
      "1": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "2": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "3": "dc1427a5-b141-49e5-8f16-691613af11bc",
      "4": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "5": "dc1427a5-b141-49e5-8f16-691613af11bc",
      "6": "dc1427a5-b141-49e5-8f16-691613af11bc",
      "7": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "8": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "9": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "10": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "11": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "12": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "13": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "14": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "15": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "16": "dc1427a5-b141-49e5-8f16-691613af11bc",
      "17": "d14c795c-08d1-41ad-9059-b803289a27fb",
      "18": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "19": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "20": "46632339-03c7-4c09-84ea-24187d7b7682",
      "21": "dc1427a5-b141-49e5-8f16-691613af11bc",
      "22": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
      "23": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
      "24": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "25": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "26": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "27": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "28": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "29": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "30": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "31": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "32": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "33": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "34": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "35": "a99d8ccb-e95b-455a-8f69-eff33fad0319"
    },
    "references": [
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 1,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 2,
        "cited_text": "Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness. B. Coding agents The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because: Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
      },
      {
        "source_id": "dc1427a5-b141-49e5-8f16-691613af11bc",
        "citation_number": 3,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Warning Most of our current development effort is on mini-swe-agent , which has superseded SWE-agent. It matches the performance performance of SWE-agent, while being much simpler. See the FAQ for more details about the differences. Our general recommendation is to use mini-SWE-agent instead of SWE-agent going forward. SWE-agent enables your language model of choice (e.g. GPT-4o or Claude Sonnet 4) to autonomously use tools to fix issues in real GitHub repositories , find cybersecurity vulnerabilities , or perform any custom task ."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 4,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "dc1427a5-b141-49e5-8f16-691613af11bc",
        "citation_number": 5,
        "cited_text": "🚀 Get started! 👉 Try SWE-agent in your browser: ( more information ) Read our documentation to learn more: Installation Hello world from the command line Benchmarking on SWE-bench Frequently Asked Questions SWE-agent for offensive cybersecurity (EnIGMA) SWE-agent: EnIGMA is a mode for solving offensive cybersecurity (capture the flag) challenges. EnIGMA achieves state-of-the-art results on multiple cybersecurity benchmarks (see leaderboard ). Please use SWE-agent 0.7 while we update EnIGMA for 1.0."
      },
      {
        "source_id": "dc1427a5-b141-49e5-8f16-691613af11bc",
        "citation_number": 6,
        "cited_text": "If you found this work helpful, please consider citing it using the following: SWE-agent citation If you used the summarizer, interactive commands or the offensive cybersecurity capabilities in SWE-agent, please also consider citing: EnIGMA citation 🪪 License MIT. Check LICENSE . About SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] swe-agent.com Topics agent ai cybersecurity lms developer-tools agent-based-model llm"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 7,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 8,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 9,
        "cited_text": "Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Tools Tool use with Claude Copy page Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works. Copy page Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools)."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 10,
        "cited_text": "Here's the simplest example using a server tool, where Anthropic handles execution: Python How tool use works Tools differ primarily by where the code executes. Client tools (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with stop_reason: \"tool_use\" and one or more tool_use blocks, your code executes the operation, and you send back a tool_result . Server tools (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 11,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 12,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 13,
        "cited_text": "Claude Platform Overview Developer docs Pricing Marketplace Regional compliance Amazon Bedrock Google Cloud's Vertex AI Microsoft Foundry Console login Resources Blog Claude partner network Community Connectors Courses Customer stories Engineering at Anthropic Events Inside Claude Code Inside Cowork Plugins Powered by Claude Service partners Startups program Tutorials Use cases Company Anthropic Careers Economic Futures Research News Claude's Constitution Responsible Scaling Policy Security and compliance Transparency"
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 14,
        "cited_text": "Files & assets Files API Agent Skills Overview Quickstart Best practices Skills for enterprise Claude API skill Using Skills with the API Agent SDK Overview Quickstart How the agent loop works Core concepts Guides SDK references MCP in the API MCP connector Remote MCP servers Claude on 3rd-party platforms Amazon Bedrock Microsoft Foundry Vertex AI Prompt engineering Overview Console prompting tools Test & evaluate Define success and build evaluations Using the Evaluation Tool Reducing latency Strengthen guardrails"
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 15,
        "cited_text": "Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams"
      },
      {
        "source_id": "dc1427a5-b141-49e5-8f16-691613af11bc",
        "citation_number": 16,
        "cited_text": "GitHub - SWE-agent/SWE-agent: SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "d14c795c-08d1-41ad-9059-b803289a27fb",
        "citation_number": 17,
        "cited_text": "Computer Science > Software Engineering arXiv:2405.15793 (cs) [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 18,
        "cited_text": "GitHub - OpenBMB/ToolBench: [ICLR'24 spotlight] An open platform for training, serving, and evaluating large language model for tool learning. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 19,
        "cited_text": "Repository files navigation README Apache-2.0 license 🛠ToolBench🤖 Model • Data Release • Web Demo • Tool Eval • Paper • Citation 🔨This project (ToolLLM) aims to construct open-source, large-scale, high-quality instruction tuning SFT data to facilitate the construction of powerful LLMs with general tool-use capability. We aim to empower open-source LLMs to master thousands of diverse real-world APIs. We achieve this by collecting a high-quality instruction-tuning dataset. It is constructed automatically using the latest ChatGPT (gpt-3.5-turbo-16k), which is upgraded with enhanced function call capabilities. We provide the dataset, the corresponding training and evaluation scripts, and a capable model ToolLLaMA fine-tuned on ToolBench."
      },
      {
        "source_id": "46632339-03c7-4c09-84ea-24187d7b7682",
        "citation_number": 20,
        "cited_text": "arXiv:2305.15334 (cs) [Submitted on 24 May 2023] Title: Gorilla: Large Language Model Connected with Massive APIs Authors: Shishir G. Patil , Tianjun Zhang , Xin Wang , Joseph E. Gonzalez View a PDF of the paper titled Gorilla: Large Language Model Connected with Massive APIs, by Shishir G. Patil and 3 other authors View PDF Abstract: Large Language Models (LLMs) have seen an impressive wave of advances recently, with models now excelling in a variety of tasks, such as mathematical reasoning and program synthesis. However, their potential to effectively use tools via API calls remains unfulfilled. This is a challenging task even for today's state-of-the-art LLMs such as GPT-4, largely due to their inability to generate accurate input arguments and their tendency to hallucinate the wrong usage of an API call. We release Gorilla, a finetuned LLaMA-based model that surpasses the performance of GPT-4 on writing API calls. When combined with a document retriever, Gorilla demonstrates a strong capability to adapt to test-time document changes, enabling flexible user updates or version changes. It also substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model's ability, we introduce APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs. Gorilla's code, model, data, and demo are available at this https URL"
      },
      {
        "source_id": "dc1427a5-b141-49e5-8f16-691613af11bc",
        "citation_number": 21,
        "cited_text": "✅ State of the art on SWE-bench among open-source projects ✅ Free-flowing & generalizable : Leaves maximal agency to the LM ✅ Configurable & fully documented : Governed by a single yaml file ✅ Made for research : Simple & hackable by design SWE-agent is built and maintained by researchers from Princeton University and Stanford University. 📣 News July 24: Mini-SWE-Agent achieves 65% on SWE-bench verified in 100 lines of python! May 2: SWE-agent-LM-32b achieves open-weights SOTA on SWE-bench Feb 28: SWE-agent 1.0 + Claude 3.7 is SoTA on SWE-Bench full Feb 25: SWE-agent 1.0 + Claude 3.7 is SoTA on SWE-bench verified Feb 13: Releasing SWE-agent 1.0: SoTA on SWE-bench light & tons of new features Dec 7: An interview with the SWE-agent & SWE-bench team"
      },
      {
        "source_id": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
        "citation_number": 22,
        "cited_text": "SWE-bench Leaderboards SWE-bench SWE-bench Leaderboards Benchmarks SWE-bench SWE-bench Verified SWE-bench Multilingual SWE-bench Multimodal SWE-bench Lite About Paper Docs Blog Contact Citations Press Submit SWE-bench Family mini-SWE-agent SWE-smith CodeClash SWE-ReX SWE-bench CLI SWE-agent (legacy) Official Leaderboards mini-SWE-agent scores up to 74% on SWE-bench Verified in 100 lines of Python code. Click here to learn more."
      },
      {
        "source_id": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
        "citation_number": 23,
        "cited_text": "Org: UIUC [x] Org: Warp Org: Warp [x] Org: Z-AI Org: Z-AI [x] Org: Z.ai Org: Z.ai [x] Org: deepseek Org: deepseek [x] Org: devlo Org: devlo [x] Org: mistral Org: mistral [x] System: Attempts - 1 System: Attempts - 1 [x] System: Attempts - 2 System: Attempts - 2 [x] System: Attempts - 2+ System: Attempts - 2+ [-] Show results from older agent versions [-] Model % Resolved Avg. $ Trajs Org Date Agent [-] 🆕 Claude 4.5 Opus (high reasoning) 76.80 $0.75 2026-02-17 2.0.0 [-] 🆕 Gemini 3 Flash (high reasoning) 75.80 $0.36 2026-02-17"
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 24,
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
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 25,
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
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 26,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 27,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 28,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 29,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 30,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 31,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 32,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 33,
        "cited_text": "There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 34,
        "cited_text": "The regex syntax used by terminals is the Rust regex crate syntax , not Python's re module . Key ideas and best practices Lexer runs before the parser Terminals are matched by the lexer (greedily / longest match wins) before any CFG rule logic is applied. If you try to “shape” a terminal by splitting it across several rules, the lexer cannot be guided by those rules—only by terminal regexes. Prefer one terminal when you're carving text out of freeform spans If you need to recognize a pattern embedded in arbitrary text (e.g., natural language with “anything” between anchors), express that as a single terminal. Do not try to interleave free‑text terminals with parser rules; the greedy lexer will not respect your intended boundaries and it is highly likely the model will go out of distribution."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 35,
        "cited_text": "Use rules to combine tokens, not to steer regex internals Good rule usage example: Treat whitespace explicitly Don't rely on open-ended %ignore directives. Using unbounded ignore directives may cause the grammar to be too complex and/or may cause the model to go out of distribution. Prefer threading explicit terminals wherever whitespace is allowed. Troubleshooting If the API rejects the grammar because it is too complex, simplify the rules and terminals and remove unbounded %ignore s. If custom tools are called with unexpected tokens, confirm terminals aren't overlapping; check greedy lexer. When the model drifts “out‑of‑distribution” (shows up as the model producing excessively long or repetitive outputs, it is syntactically valid but is semantically wrong): Tighten the grammar. Iterate on the prompt (add few-shot examples) and tool description (explain the grammar and instruct the model to reason and conform to it). Experiment with a higher reasoning effort (e.g, bump from medium to high)."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「Agent-Computer Interface（ACI）设计：工具即提示工程」领域，2025-2026年的研究焦点已从单纯的“模型调用工具”演进为**将工具界面视为一种专为 AI 智能体设计的语言系统** [1, 2]。以下是该领域的最新突破、技术趋势及未来方向：\n\n### 1. 2025-2026 年关键技术趋势与重要研究\n随着 **GPT-5.4** 和 **Claude 4.6** 等高推理模型的发布，ACI 设计进入了标准化与深度集成阶段 [3, 4]：\n\n*   **Model Context Protocol (MCP) 的标准化**：MCP 已成为连接智能体与第三方工具生态系统的通用标准 [5, 6]。它允许智能体通过简单的客户端实现，动态接入复杂的外部服务，降低了 ACI 开发的准入门槛 [5, 6]。\n*   **工具搜索 (Tool Search) 技术**：针对“大规模工具集”问题，**GPT-5.4** 等模型引入了工具搜索机制 [3, 7]。当工具数量庞大（通常建议初始可见少于 20 个）时，模型先通过搜索加载相关工具定义，再进行调用，从而节省上下文空间并减少干扰 [7, 8]。\n*   **严格模式与语法约束 (Strict Mode & CFG)**：为了确保 100% 的架构遵从性，**Strict Mode** 强制模型输出符合 JSON Schema [6, 9]。同时，**上下文无关语法 (CFG)**（如使用 Lark 或 Regex）被用于约束自定义工具的文本输入，解决了模型在生成复杂格式时常见的转义错误 [10, 11]。\n*   **极简主义的崛起 (mini-SWE-agent)**：最新的研究显示，复杂的框架反而可能掩盖底层响应 [12]。**mini-SWE-agent** 仅用约 100 行 Python 代码结合优化的 ACI，就在 SWE-bench Verified 基准测试中达到了 **74%** 的解决率，证明了界面设计的价值高于框架复杂性 [13, 14]。\n\n### 2. 重要论文与项目成果\n*   **《SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering》**：该基础研究确立了 ACI 的核心地位，提出智能体是不同于人类的新型终端用户，需要专属的软件界面（如强制使用绝对路径、简化文件导航工具）[2, 15]。\n*   **《Emergent Agentic Transformer from Chain of Hindsight Experience》**：提出 **Agentic Transformer (AT)**，通过 **事后链 (Chain of Hindsight)** 将经验按奖励排序训练，使模型能从亚优轨迹中学习自我改进，标志着智能体具备了在测试时自我优化的能力 [16]。\n*   **ToolBench (ICLR 2024 Spotlight)**：引入了基于**深度优先搜索决策树 (DFSDT)** 的标注方法，极大提升了模型在处理 ReACT 无法完成的复杂多工具任务时的规划能力 [17, 18]。\n\n### 3. 未解决的挑战\n尽管性能在提升（如 Claude 4.5 Opus 在 SWE-bench 上达到 76.8%），该领域仍面临严峻挑战 [19]：\n*   **错误复合效应 (Compounding Errors)**：在自主智能体长时间运行的过程中，单次工具调用的微小偏差可能导致后续规划彻底偏离，且模型难以在多轮迭代中始终保持“地面真值” [20, 21]。\n*   **格式开销 (Formatting Overhead)**：要求模型计算代码行数或在 JSON 中进行大量的字符转义，会显著增加推理负担并诱发幻觉 [1, 22]。\n*   **延迟与成本的权衡**：智能体系统通常通过牺牲延迟和成本来换取准确率 [23]。例如，启用工具调用需额外消耗 **313-346 个系统令牌**，且复杂的推理模式（High Reasoning）费用昂贵 [19, 24]。\n\n### 4. 未来可能的突破点\n*   **可验证的闭环系统**：未来的智能体将更加依赖于**环境反馈作为“推理锚点”**。例如，在代码领域，利用自动化测试结果作为强制反馈循环（Evaluator-Optimizer 模式），实现无需人工干预的自我修复 [25, 26]。\n*   **高推理努力 (High Reasoning Effort)**：通过增加预留的“思考空间”（Thinking Tokens），让模型在输出工具指令前进行大规模搜索和推演，这将进一步刷新科学研究（FigQA）和软件维护的性能上限 [1, 27]。\n*   **ACI 防错设计 (Poka-yoke)**：未来将研究如何通过 API 层的结构性调整（如强制枚举、不可代表的错误状态设计），从根本上使模型“无法犯错”，实现更稳健的智能体协作 [8, 28]。",
    "conversation_id": "80460170-aa1a-41b8-843e-a16c9f82f508",
    "sources_used": [
      "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "d14c795c-08d1-41ad-9059-b803289a27fb",
      "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "dc1427a5-b141-49e5-8f16-691613af11bc",
      "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
      "33d910bb-570b-4cd3-b789-6b75c097af26",
      "44100584-1e5a-4486-a6a7-c928cf13c6a2"
    ],
    "citations": {
      "1": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "2": "d14c795c-08d1-41ad-9059-b803289a27fb",
      "3": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "4": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "5": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "6": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "7": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "8": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "9": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "10": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "11": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "12": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "13": "dc1427a5-b141-49e5-8f16-691613af11bc",
      "14": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
      "15": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "16": "33d910bb-570b-4cd3-b789-6b75c097af26",
      "17": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "18": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
      "19": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
      "20": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "21": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "22": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "23": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "24": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
      "25": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "26": "277e2bdc-ca16-497e-b84e-106ac473c89e",
      "27": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
      "28": "277e2bdc-ca16-497e-b84e-106ac473c89e"
    },
    "references": [
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 1,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "d14c795c-08d1-41ad-9059-b803289a27fb",
        "citation_number": 2,
        "cited_text": "Computer Science > Software Engineering arXiv:2405.15793 (cs) [Submitted on 6 May 2024 ( v1 ), last revised 11 Nov 2024 (this version, v3)] Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering Authors: John Yang , Carlos E. Jimenez , Alexander Wettig , Kilian Lieret , Shunyu Yao , Karthik Narasimhan , Ofir Press View a PDF of the paper titled SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering, by John Yang and 6 other authors View PDF Abstract: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 3,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 4,
        "cited_text": "Tool use with Claude - Claude API Docs Loading... Developer Guide API Reference MCP Resources Release Notes English Log in Search... ⌘K First steps Intro to Claude Quickstart Models & pricing Models overview Choosing a model What's new in Claude 4.6 Migration guide Model deprecations Pricing Build with Claude Features overview Using the Messages API Handling stop reasons Prompting best practices Model capabilities Extended thinking Adaptive thinking Effort Fast mode (beta: research preview) Structured outputs Citations Streaming Messages Batch processing PDF support Search results Multilingual support Embeddings Vision"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 5,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 6,
        "cited_text": "For the full conceptual model including the agentic loop and when to choose each approach, see How tool use works . For connecting to MCP servers, see the MCP connector . For building your own MCP client, see modelcontextprotocol.io . Guarantee schema conformance with strict tool use Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly. See Strict tool use . Tool access is one of the highest-leverage primitives you can give an agent. On benchmarks like LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), adding even basic tools produces outsized capability gains, often surpassing human expert baselines."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 7,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 8,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 9,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 10,
        "cited_text": "Custom tools Custom tools work in much the same way as JSON schema-driven function tools. But rather than providing the model explicit instructions on what input your tool requires, the model can pass an arbitrary string back to your tool as input. This is useful to avoid unnecessarily wrapping a response in JSON, or to apply a custom grammar to the response (more on this below). The following code sample shows creating a custom tool that expects to receive a string of text containing Python code as a response."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 11,
        "cited_text": "Custom tool calling example python Just as before, the output array will contain a tool call generated by the model. Except this time, the tool call input is given as plain text. Context-free grammars A context-free grammar (CFG) is a set of rules that define how to produce valid text in a given format. For custom tools, you can provide a CFG that will constrain the model's text input for a custom tool. You can provide a custom CFG using the grammar parameter when configuring a custom tool. Currently, we support two CFG syntaxes when defining grammars: lark and regex ."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 12,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "dc1427a5-b141-49e5-8f16-691613af11bc",
        "citation_number": 13,
        "cited_text": "✅ State of the art on SWE-bench among open-source projects ✅ Free-flowing & generalizable : Leaves maximal agency to the LM ✅ Configurable & fully documented : Governed by a single yaml file ✅ Made for research : Simple & hackable by design SWE-agent is built and maintained by researchers from Princeton University and Stanford University. 📣 News July 24: Mini-SWE-Agent achieves 65% on SWE-bench verified in 100 lines of python! May 2: SWE-agent-LM-32b achieves open-weights SOTA on SWE-bench Feb 28: SWE-agent 1.0 + Claude 3.7 is SoTA on SWE-Bench full Feb 25: SWE-agent 1.0 + Claude 3.7 is SoTA on SWE-bench verified Feb 13: Releasing SWE-agent 1.0: SoTA on SWE-bench light & tons of new features Dec 7: An interview with the SWE-agent & SWE-bench team"
      },
      {
        "source_id": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
        "citation_number": 14,
        "cited_text": "SWE-bench Leaderboards SWE-bench SWE-bench Leaderboards Benchmarks SWE-bench SWE-bench Verified SWE-bench Multilingual SWE-bench Multimodal SWE-bench Lite About Paper Docs Blog Contact Citations Press Submit SWE-bench Family mini-SWE-agent SWE-smith CodeClash SWE-ReX SWE-bench CLI SWE-agent (legacy) Official Leaderboards mini-SWE-agent scores up to 74% on SWE-bench Verified in 100 lines of Python code. Click here to learn more."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 15,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "33d910bb-570b-4cd3-b789-6b75c097af26",
        "citation_number": 16,
        "cited_text": "arXiv:2305.16554 (cs) [Submitted on 26 May 2023] Title: Emergent Agentic Transformer from Chain of Hindsight Experience Authors: Hao Liu , Pieter Abbeel View a PDF of the paper titled Emergent Agentic Transformer from Chain of Hindsight Experience, by Hao Liu and Pieter Abbeel View PDF Abstract: Large transformer models powered by diverse data and model scale have dominated natural language modeling and computer vision and pushed the frontier of multiple AI areas. In reinforcement learning (RL), despite many efforts into transformer-based policies, a key limitation, however, is that current transformer-based policies cannot learn by directly combining information from multiple sub-optimal trials. In this work, we address this issue using recently proposed chain of hindsight to relabel experience, where we train a transformer on a sequence of trajectory experience ascending sorted according to their total rewards. Our method consists of relabelling target return of each trajectory to the maximum total reward among in sequence of trajectories and training an autoregressive model to predict actions conditioning on past states, actions, rewards, target returns, and task completion tokens, the resulting model, Agentic Transformer (AT), can learn to improve upon itself both at training and test time. As we show on D4RL and ExoRL benchmarks, to the best our knowledge, this is the first time that a simple transformer-based model performs competitively with both temporal-difference and imitation-learning-based approaches, even from sub-optimal data. Our Agentic Transformer also shows a promising scaling trend that bigger models consistently improve results."
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 17,
        "cited_text": "GitHub - OpenBMB/ToolBench: [ICLR'24 spotlight] An open platform for training, serving, and evaluating large language model for tool learning. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "44100584-1e5a-4486-a6a7-c928cf13c6a2",
        "citation_number": 18,
        "cited_text": "✨Here is an overview of the dataset construction, training, and evaluation. ✨✨Features: API Collection : we gather 16464 representational state transfer (REST) APIs from RapidAPI , a platform that hosts massive real-world APIs provided by developers. Instruction Generation : we curate instructions that involve both single-tool and multi-tool scenarios. Answer Annotation : we develop a novel depth-first search based decision tree (DFSDT) to bolster the planning and reasoning ability of LLMs, which significantly improves the annotation efficiency and successfully annotates those complex instructions that cannot be answered with CoT or ReACT. We provide responses that not only include the final answer but also incorporate the model's reasoning process, tool execution, and tool execution results . API Retriver : we incorporate API retrieval to equip ToolLLaMA with open-domain tool-using abilities. All the data is automatically generated by OpenAI API and filtered by us, the whole data creation process is easy to scale up."
      },
      {
        "source_id": "e32e9ece-5360-4b79-8fc4-e87c0aa239e7",
        "citation_number": 19,
        "cited_text": "Org: UIUC [x] Org: Warp Org: Warp [x] Org: Z-AI Org: Z-AI [x] Org: Z.ai Org: Z.ai [x] Org: deepseek Org: deepseek [x] Org: devlo Org: devlo [x] Org: mistral Org: mistral [x] System: Attempts - 1 System: Attempts - 1 [x] System: Attempts - 2 System: Attempts - 2 [x] System: Attempts - 2+ System: Attempts - 2+ [-] Show results from older agent versions [-] Model % Resolved Avg. $ Trajs Org Date Agent [-] 🆕 Claude 4.5 Opus (high reasoning) 76.80 $0.75 2026-02-17 2.0.0 [-] 🆕 Gemini 3 Flash (high reasoning) 75.80 $0.36 2026-02-17"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 20,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 21,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 22,
        "cited_text": "There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 23,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "7efb95f7-fe12-45e9-b579-5dc7e858777d",
        "citation_number": 24,
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
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 25,
        "cited_text": "Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness. B. Coding agents The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because: Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 26,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "a99d8ccb-e95b-455a-8f69-eff33fad0319",
        "citation_number": 27,
        "cited_text": "Use rules to combine tokens, not to steer regex internals Good rule usage example: Treat whitespace explicitly Don't rely on open-ended %ignore directives. Using unbounded ignore directives may cause the grammar to be too complex and/or may cause the model to go out of distribution. Prefer threading explicit terminals wherever whitespace is allowed. Troubleshooting If the API rejects the grammar because it is too complex, simplify the rules and terminals and remove unbounded %ignore s. If custom tools are called with unexpected tokens, confirm terminals aren't overlapping; check greedy lexer. When the model drifts “out‑of‑distribution” (shows up as the model producing excessively long or repetitive outputs, it is syntactically valid but is semantically wrong): Tighten the grammar. Iterate on the prompt (add few-shot examples) and tool description (explain the grammar and instruct the model to reason and conform to it). Experiment with a higher reasoning effort (e.g, bump from medium to high)."
      },
      {
        "source_id": "277e2bdc-ca16-497e-b84e-106ac473c89e",
        "citation_number": 28,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      }
    ]
  }
}
