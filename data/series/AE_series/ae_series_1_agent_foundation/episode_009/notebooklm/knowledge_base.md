# 知识库：Evaluator-Optimizer 与 Reflection：自我纠错的 Agent

生成时间: 2026-04-06 16:36
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "「Evaluator-Optimizer（评估者-优化者）」与「Reflection（反思/自省）」是构建具备自我纠错能力的 AI Agent 的核心架构模式。其核心目标是通过**迭代反馈循环**来提升 LLM 的输出质量，使其能够突破单次推理的局限。\n\n以下是根据来源总结的技术架构与关键组件：\n\n### 1. 技术演进路线\nAI Agent 的自我纠错技术经历了从简单到复杂的演进过程：\n*   **基础增强层**：最初是增强型 LLM（Augmented LLM），通过检索、工具和记忆来扩展模型能力 [1, 2]。\n*   **线性工作流层**：演进为**提示链（Prompt Chaining）**和**路由（Routing）**，将复杂任务分解为固定步骤 [3, 4]。\n*   **循环迭代层**：引入 **Evaluator-Optimizer 模式**，通过专门的评估步骤进入迭代优化循环 [5]。\n*   **自主强化层**：发展出 **Reflexion（言语强化学习）** 和 **STaR（自教推理者）**，Agent 开始具备维护短期记忆（情节记忆）、自我评估并在多次尝试中学习的能力 [6, 7]。\n\n### 2. 核心算法与概念\n*   **Evaluator-Optimizer**：一个 LLM 调用负责生成响应，另一个 LLM 调用负责根据预设标准提供评估和反馈，两者循环协作 [5]。\n*   **Reflexion (Verbal Reinforcement Learning)**：一种通过**语言反馈**而非权重更新来强化 Agent 的框架。Agent 会对任务反馈信号进行言语反思，并将反思文本存储在**情节记忆（Episodic Memory）**缓冲区中，以指导后续尝试 [7]。\n*   **STaR (Self-Taught Reasoner)**：一种引导（Bootstrapping）技术。模型为问题生成推理链（Rationales），如果答案错误，则在给定正确答案的情况下重新尝试生成推理，并最终在所有产生正确答案的推理链上进行微调 [6]。\n*   **Chain-of-Thought (CoT)**：在上述迭代过程中，作为基础的推理生成方式，帮助模型逐步处理复杂逻辑 [6, 7]。\n\n### 3. 主要架构模式\n*   **生成-评估循环 (Generator-Evaluator Loop)**：\n    *   **生成器（Optimizer）**：接收原始输入及（可选的）反馈，输出改进后的结果 [5]。\n    *   **评估器（Evaluator）**：根据明确的成功标准评估输出，提供结构化反馈或判断是否达到终止条件 [5, 8]。\n*   **自主 Agent 循环 (Reflexion 架构)**：\n    1.  **尝试 (Trial)**：Agent 执行操作或生成代码。\n    2.  **评估 (Evaluation)**：从环境（如编译器或测试用例）获得反馈信号（标量或语言反馈） [7]。\n    3.  **反思 (Reflection)**：Agent 分析失败原因，生成反思摘要 [7]。\n    4.  **存储 (Memory)**：将反思存入记忆库，在下一次循环中作为上下文输入 [7]。\n\n### 4. 关键技术指标\n*   **任务准确率提升**：**Reflexion** 在 HumanEval 编码基准测试中达到了 **91% 的 pass@1 准确率**，超过了 GPT-4 初始的 80% [7]。\n*   **推理效率**：**STaR** 算法能让模型通过自我学习，在特定任务上表现出与比其大 30 倍的模型相当的性能 [6]。\n*   **时延与成本权衡**：这类模式通常会以增加时延和调用成本为代价，换取更高的任务成功率 [9, 10]。\n*   **反馈质量**：系统的有效性高度依赖于 LLM 是否能提供可执行的、类似于人类水平的反馈 [5]。\n*   **控制指标**：通常需要设置**最大迭代次数（Stopping Conditions）**以防止无限循环 [11]。\n\n### 5. 关键组件总结\n*   **情节记忆缓冲区 (Episodic Memory Buffer)**：用于跨尝试保留反思信息 [7]。\n*   **反馈信号 (Feedback Signals)**：可以是外部环境给出的（如代码执行错误、搜索结果），也可以是内部模拟生成的 [7, 11]。\n*   **工具集 (Toolsets/ACI)**：Agent 与环境交互的接口，其文档和定义的清晰度直接影响纠错效率 [12, 13]。",
    "conversation_id": "76fa4855-9011-4940-a25f-ed7a56c07636",
    "sources_used": [
      "745524b2-c668-4b93-9251-2d15be28d983",
      "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
      "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b"
    ],
    "citations": {
      "1": "745524b2-c668-4b93-9251-2d15be28d983",
      "2": "745524b2-c668-4b93-9251-2d15be28d983",
      "3": "745524b2-c668-4b93-9251-2d15be28d983",
      "4": "745524b2-c668-4b93-9251-2d15be28d983",
      "5": "745524b2-c668-4b93-9251-2d15be28d983",
      "6": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
      "7": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
      "8": "745524b2-c668-4b93-9251-2d15be28d983",
      "9": "745524b2-c668-4b93-9251-2d15be28d983",
      "10": "745524b2-c668-4b93-9251-2d15be28d983",
      "11": "745524b2-c668-4b93-9251-2d15be28d983",
      "12": "745524b2-c668-4b93-9251-2d15be28d983",
      "13": "745524b2-c668-4b93-9251-2d15be28d983"
    },
    "references": [
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 1,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 2,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 3,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 4,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 5,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
        "citation_number": 6,
        "cited_text": "arXiv:2203.14465 (cs) [Submitted on 28 Mar 2022 ( v1 ), last revised 20 May 2022 (this version, v2)] Title: STaR: Bootstrapping Reasoning With Reasoning Authors: Eric Zelikman , Yuhuai Wu , Jesse Mu , Noah D. Goodman View a PDF of the paper titled STaR: Bootstrapping Reasoning With Reasoning, by Eric Zelikman and 3 other authors View PDF Abstract: Generating step-by-step \"chain-of-thought\" rationales improves language model performance on complex reasoning tasks like mathematics or commonsense question-answering. However, inducing language model rationale generation currently requires either constructing massive rationale datasets or sacrificing accuracy by using only few-shot inference. We propose a technique to iteratively leverage a small number of rationale examples and a large dataset without rationales, to bootstrap the ability to perform successively more complex reasoning. This technique, the \"Self-Taught Reasoner\" (STaR), relies on a simple loop: generate rationales to answer many questions, prompted with a few rationale examples; if the generated answers are wrong, try again to generate a rationale given the correct answer; fine-tune on all the rationales that ultimately yielded correct answers; repeat. We show that STaR significantly improves performance on multiple datasets compared to a model fine-tuned to directly predict final answers, and performs comparably to fine-tuning a 30\\times larger state-of-the-art language model on CommensenseQA. Thus, STaR lets a model improve itself by learning from its own generated reasoning."
      },
      {
        "source_id": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
        "citation_number": 7,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 8,
        "cited_text": "Acknowledgements Written by Erik Schluntz and Barry Zhang. This work draws upon our experiences building agents at Anthropic and the valuable insights shared by our customers, for which we're deeply grateful. Appendix 1: Agents in practice Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 9,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 10,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 11,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 12,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 13,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「Evaluator-Optimizer（评估者-优化者）」与「Reflection（反思/自省）」是构建具备自我纠错能力的智能体（Agent）的两大支柱。其核心逻辑在于通过**闭环反馈**而非单次推理来提升输出质量。以下是基于来源的详细技术解析：\n\n### 1. 核心算法流程\n\n*   **Evaluator-Optimizer 模式**：\n    这是一个双角色循环系统。**优化器（Optimizer）**根据原始输入生成响应，**评估器（Evaluator）**根据预设标准提供反馈[1]。流程为：\n    1.  **生成**：优化器输出初步方案。\n    2.  **评估**：评估器检查输出并生成结构化反馈（如“此处逻辑有误”或“缺少 X 维度信息”）[1]。\n    3.  **循环**：优化器根据反馈重新生成响应，直到达到终止条件（如评估通过或达到最大尝试次数）[2]。\n\n*   **Reflection (Reflexion) 算法**：\n    这是一种通过**言语强化学习（Verbal Reinforcement Learning）**实现的技术[3]。它不更新模型权重，而是维护一个**情节记忆（Episodic Memory）**缓冲池[3]。\n    1.  **尝试 (Trial)**：Agent 执行任务或生成代码[3]。\n    2.  **获取信号**：从环境（如编译器或测试集）获取标量（分数）或自由文本反馈[3]。\n    3.  **反思 (Self-Reflection)**：Agent 对失败原因进行文字总结，分析为何之前的尝试未成功[3]。\n    4.  **记忆存储**：将反思文本存入记忆缓冲区，在下一次迭代中作为上下文提示，指导决策[3]。\n\n*   **STaR (Self-Taught Reasoner)**：\n    一种引导技术，要求模型为问题生成推理链（Rationales）[4]。如果结果错误，模型在已知正确答案的情况下重新推理，并最终在产生正确答案的推理路径上进行微调[4]。\n\n### 2. 关键代码架构\n\n实现这些模式通常依赖于以下架构模式：\n*   **状态化图架构 (Stateful Graphs)**：如 **LangGraph**，将 Agent 逻辑表示为有向图，每个节点代表一个 LLM 调用或工具操作，能够持久化存储状态并支持失败重试[5, 6]。\n*   **多智能体协作 (Orchestrator-Workers)**：一个中心 LLM 作为协调者，将复杂任务拆解并分发给专门的子智能体执行[7]。\n*   **智能体-计算机接口 (ACI)**：比起 prompt 优化，**工具定义（Tool Definition）**的优化往往更关键[8]。例如，强制要求工具使用**绝对路径**而非相对路径，可以显著降低 Agent 在复杂文件系统中的报错率[9]。\n\n### 3. 性能优化策略\n\n*   **提示缓存 (Prompt Caching)**：在迭代循环中，由于大量上下文（如系统指令、参考资料）保持不变，使用提示缓存可减少延迟并降低成本[10]。其**缓存命中率通常在 30% 到 98% 之间**[10]。\n*   **批量处理 (Batch Processing)**：对于非实时的大规模评估任务，使用 Batch API 可以将**成本降低 50%**，并提供更高的吞吐量[11, 12]。\n*   **超长输出支持 (Extended Output)**：在需要长链推理（Chain-of-Thought）或大规模代码生成的场景中，利用 beta 版本的长输出功能可单次生成高达 **300,000 个 token** 的内容[13]。\n*   **情节记忆缓冲区**：通过存储过去的错误和反思，防止 Agent 在循环中陷入相同的错误陷阱[3]。\n\n### 4. 竞品技术对比与数据指标\n\n| 维度 | Reflexion (强化 Agent) | 基础 GPT-4 / 其它 LLM | STaR 引导技术 |\n| :--- | :--- | :--- | :--- |\n| **核心数据** | 在 HumanEval 编码基准上达到 **91% pass@1 准确率**[3]。 | GPT-4 初始准确率为 **80%**[3]。 | 使较小模型表现可比拟 **30 倍规模**的大型模型[4]。 |\n| **反馈机制** | 言语反馈（文本形式的反思）[3]。 | 无反馈或仅有简单的重试 prompt。 | 给定正确答案后的反思与微调[4]。 |\n| **学习方式** | 情节记忆、非权重更新[3]。 | 无在线学习能力。 | 迭代微调（权重更新）[4]。 |\n| **主要框架** | LangGraph (Graph-based)[5] / AutoGen (Message-based)[14]。 | 单次调用或简单 Chaining。 | 内部训练流程。 |\n\n### 5. 具体技术参数总结\n\n*   **数据留存**：使用批量处理 API 时，结果在服务器端最长留存 **29 天**[15, 16]。\n*   **处理窗口**：大多数批处理任务可在 **1 小时内**完成，最长处理窗口为 24 小时[11, 15]。\n*   **批处理容量**：单个批处理包上限为 **100,000 个请求**或 **256 MB**[15]。\n*   **成本效率**：通过 Evaluator-Optimizer 这种 agentic 模式，虽然增加了调用次数，但可以通过 **50% 的批处理折扣**和**提示缓存**来抵消增加的成本[10, 12]。",
    "conversation_id": "76fa4855-9011-4940-a25f-ed7a56c07636",
    "sources_used": [
      "745524b2-c668-4b93-9251-2d15be28d983",
      "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
      "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
      "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "df15d832-193b-4372-af9f-767ed0195559",
      "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c"
    ],
    "citations": {
      "1": "745524b2-c668-4b93-9251-2d15be28d983",
      "2": "745524b2-c668-4b93-9251-2d15be28d983",
      "3": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
      "4": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
      "5": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "6": "df15d832-193b-4372-af9f-767ed0195559",
      "7": "745524b2-c668-4b93-9251-2d15be28d983",
      "8": "745524b2-c668-4b93-9251-2d15be28d983",
      "9": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "10": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "11": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "12": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "13": "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c",
      "14": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "15": "7dd4077b-dce0-4435-b440-736c0c9d0c89"
    },
    "references": [
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 1,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 2,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
        "citation_number": 3,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
        "citation_number": 4,
        "cited_text": "arXiv:2203.14465 (cs) [Submitted on 28 Mar 2022 ( v1 ), last revised 20 May 2022 (this version, v2)] Title: STaR: Bootstrapping Reasoning With Reasoning Authors: Eric Zelikman , Yuhuai Wu , Jesse Mu , Noah D. Goodman View a PDF of the paper titled STaR: Bootstrapping Reasoning With Reasoning, by Eric Zelikman and 3 other authors View PDF Abstract: Generating step-by-step \"chain-of-thought\" rationales improves language model performance on complex reasoning tasks like mathematics or commonsense question-answering. However, inducing language model rationale generation currently requires either constructing massive rationale datasets or sacrificing accuracy by using only few-shot inference. We propose a technique to iteratively leverage a small number of rationale examples and a large dataset without rationales, to bootstrap the ability to perform successively more complex reasoning. This technique, the \"Self-Taught Reasoner\" (STaR), relies on a simple loop: generate rationales to answer many questions, prompted with a few rationale examples; if the generated answers are wrong, try again to generate a rationale given the correct answer; fine-tune on all the rationales that ultimately yielded correct answers; repeat. We show that STaR significantly improves performance on multiple datasets compared to a model fine-tuned to directly predict final answers, and performs comparably to fine-tuning a 30\\times larger state-of-the-art language model on CommensenseQA. Thus, STaR lets a model improve itself by learning from its own generated reasoning."
      },
      {
        "source_id": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
        "citation_number": 5,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. If you're looking to quickly build agents with LangChain's create_agent (built on LangGraph), check out the LangChain Agents documentation ."
      },
      {
        "source_id": "df15d832-193b-4372-af9f-767ed0195559",
        "citation_number": 6,
        "cited_text": "Copy page Trusted by companies shaping the future of agents— including Klarna, Uber, J.P. Morgan, and more— LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents. LangGraph is very low-level, and focused entirely on agent orchestration . Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with models and tools . We will commonly use LangChain components throughout the documentation to integrate models and tools, but you don't need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain's agents that provide prebuilt architectures for common LLM and tool-calling loops. LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 7,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 8,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 9,
        "cited_text": "Shell The response will show the batch in a canceling state: JSON Using prompt caching with Message Batches The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, since batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 10,
        "cited_text": "You need to process large volumes of data Immediate responses are not required You want to optimize for cost efficiency You're running large-scale evaluations or analyses The Message Batches API is Anthropic's first implementation of this pattern. This feature is not eligible for Zero Data Retention (ZDR) . Data is retained according to the feature's standard retention policy. Message Batches API The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 11,
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
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 12,
        "cited_text": "Extended output (beta) The output-300k-2026-03-24 beta header raises the max_tokens cap to 300,000 for batch requests using Claude Opus 4.6 or Claude Sonnet 4.6. Include the header to generate outputs far longer than the standard limit (64k to 128k depending on model) in a single turn. Extended output is available on the Message Batches API only, not the synchronous Messages API. It is supported on the Claude API and is not available on Amazon Bedrock, Vertex AI, or Microsoft Foundry. Use extended output for long-form generation such as book-length drafts and technical documentation, exhaustive structured data extraction, large code-generation scaffolds, and long reasoning chains."
      },
      {
        "source_id": "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c",
        "citation_number": 13,
        "cited_text": "Why Use AutoGen? The AutoGen ecosystem provides everything you need to create AI agents, especially multi-agent workflows -- framework, developer tools, and applications. The framework uses a layered and extensible design. Layers have clearly divided responsibilities and build on top of layers below. This design enables you to use the framework at different levels of abstraction, from high-level APIs to low-level components. Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python. AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats. Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 14,
        "cited_text": "Large-scale evaluations: Process thousands of test cases efficiently. Content moderation: Analyze large volumes of user-generated content asynchronously. Data analysis: Generate insights or summaries for large datasets. Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries). Batch limitations A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first. The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours. Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download. Batches are scoped to a Workspace . You may view all batches (and their results) that were created within the Workspace that your API key belongs to. Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See Message Batches API rate limits . Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours. Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured spend limit ."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 15,
        "cited_text": "Batch processing stores request and response data for up to 29 days after batch creation. You can delete a message batch at any time after processing using the DELETE /v1/messages/batches/{batch_id} endpoint. To delete an in-progress batch, cancel it first. Asynchronous processing requires server-side storage of both inputs and outputs until batch completion and result retrieval. For ZDR eligibility across all features, see API and data retention . FAQ How long does it take for a batch to process? Is the Batches API available for all models?"
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「Evaluator-Optimizer」与「Reflection」是当前构建自主、高精度 AI Agent 的核心模式。以下是基于来源整理的真实应用场景、部署方案、性能数据及实战经验：\n\n### 1. 真实应用场景与案例\n*   **软件工程（Coding Agents）**：\n    *   **典型案例**：Anthropic 开发的编码 Agent 能独立解决 **SWE-bench Verified** 基准测试中的真实 GitHub 问题，仅凭拉取请求（PR）描述即可完成多文件修改 [1, 2]。\n    *   **应用逻辑**：Agent 利用测试结果作为反馈信号进行迭代。通过编译器报错或单元测试失败，触发自省流程，直至代码通过验证 [3, 4]。\n*   **客户支持（Customer Support）**：\n    *   **典型案例**：多家公司采用基于成功解决率（Success-based pricing）的计费模型部署 Agent [3]。\n    *   **应用逻辑**：Agent 结合外部工具（如订单查询、退款接口）与对话流程，在处理退款或技术支持请求时，通过评估步骤确保操作符合业务逻辑 [5]。\n*   **高精度内容生成**：\n    *   **文学翻译**：通过评估者模型捕获初次翻译中缺失的细微差别，提供批评意见引导优化器进行第二轮修正 [6]。\n    *   **复杂搜索**：在多轮信息采集任务中，评估者决定是否需要额外的搜索动作以完善信息覆盖度 [6]。\n\n### 2. 工业级部署方案\n*   **状态化图架构 (Stateful Graphs)**：\n    *   **LangGraph** 被 Klarna、Uber、J.P. Morgan 等公司用于部署长时运行（long-running）的 Agent [7, 8]。其核心在于提供**持久化存储**，使 Agent 在失败后能从断点自动恢复，并支持**人机协作（Human-in-the-loop）**，允许人工在关键节点检查或修改状态 [9, 10]。\n*   **大规模离线处理 (Batch Processing)**：\n    *   利用 **Message Batches API** 进行大规模评估。其优势在于提供 **50% 的价格折扣**，支持单次提交 10 万个请求，且缓存命中率可达 30%-98% [11-13]。\n*   **可观测性与监控**：\n    *   使用 **LangSmith** 进行追踪和评估，可视化 Agent 的执行路径、状态转换及运行指标 [9, 14, 15]。\n\n### 3. 开源项目实战案例\n*   **Reflexion**：一个通过言语反馈强化 Agent 的框架，开源了针对 **HotPotQA**（推理）、**AlfWorld**（决策）和 **HumanEval**（编程）的实验代码 [16, 17]。\n*   **AutoGen**：微软开发的框架，支持创建多智能体协作应用，其典型应用 **Magentic-One** 能处理复杂的网页浏览和代码执行任务 [18, 19]。\n*   **Claude Cookbooks**：提供了 **Evaluator-Optimizer** 和 **Orchestrator-Workers** 工作流的极简参考实现 [20, 21]。\n\n### 4. 性能基准数据\n*   **准确率提升**：**Reflexion** 在 HumanEval 编码基准测试中达到了 **91% 的 pass@1 准确率**，大幅超过 GPT-4 初始的 80% [4]。\n*   **模型效率**：**STaR** 算法通过自我学习推理链，使较小模型在 CommonsenseQA 等数据集上的表现能够比拟比其大 **30 倍** 的尖端模型 [22]。\n*   **吞吐与成本**：Batch API 虽然不提供即时响应（通常 1 小时内完成），但将**单位 token 成本降低了 50%** [11, 12]。\n\n### 5. 开发者最佳实践与踩坑经验\n*   **最佳实践**：\n    *   **保持简单**：优先使用简单的 **Prompt Chaining** 或 **Routing**，仅在必要时引入复杂的自主循环 [23, 24]。\n    *   **优化 Agent 计算机接口 (ACI)**：为模型提供极其清晰的工具文档（Docstrings）。例如，**强制要求使用绝对文件路径**而非相对路径，可显著解决 Agent 在目录切换后找不到文件的问题 [25-27]。\n    *   **透明化规划**：显式展示 Agent 的思考步骤（Reasoning traces），便于调试和建立用户信任 [10, 25]。\n*   **常见踩坑点**：\n    *   **过度抽象**：使用复杂的 Agent 框架可能掩盖底层的 prompt 逻辑，增加调试难度 [28]。\n    *   **格式障碍**：LLM 编写 Diff 格式或包含转义字符的 JSON 代码块非常吃力。建议提供更多 token 供模型在输出前进行“思考”，或选择更符合预训练分布的文本格式 [29, 30]。\n    *   **错误堆叠**：自主 Agent 容易产生**错误累积**。必须设置最大迭代次数（Stopping Conditions）作为兜底保护 [1, 31]。",
    "conversation_id": "76fa4855-9011-4940-a25f-ed7a56c07636",
    "sources_used": [
      "745524b2-c668-4b93-9251-2d15be28d983",
      "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
      "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "df15d832-193b-4372-af9f-767ed0195559",
      "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "ab884bf8-fdcf-4673-b2c3-74050c1cdda0",
      "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c",
      "58d56788-da63-44d1-8a77-1a315c11ac38",
      "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e"
    ],
    "citations": {
      "1": "745524b2-c668-4b93-9251-2d15be28d983",
      "2": "745524b2-c668-4b93-9251-2d15be28d983",
      "3": "745524b2-c668-4b93-9251-2d15be28d983",
      "4": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
      "5": "745524b2-c668-4b93-9251-2d15be28d983",
      "6": "745524b2-c668-4b93-9251-2d15be28d983",
      "7": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "8": "df15d832-193b-4372-af9f-767ed0195559",
      "9": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "10": "df15d832-193b-4372-af9f-767ed0195559",
      "11": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "12": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "13": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "14": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "15": "df15d832-193b-4372-af9f-767ed0195559",
      "16": "ab884bf8-fdcf-4673-b2c3-74050c1cdda0",
      "17": "ab884bf8-fdcf-4673-b2c3-74050c1cdda0",
      "18": "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c",
      "19": "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c",
      "20": "58d56788-da63-44d1-8a77-1a315c11ac38",
      "21": "58d56788-da63-44d1-8a77-1a315c11ac38",
      "22": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
      "23": "745524b2-c668-4b93-9251-2d15be28d983",
      "24": "745524b2-c668-4b93-9251-2d15be28d983",
      "25": "745524b2-c668-4b93-9251-2d15be28d983",
      "26": "745524b2-c668-4b93-9251-2d15be28d983",
      "27": "745524b2-c668-4b93-9251-2d15be28d983",
      "28": "745524b2-c668-4b93-9251-2d15be28d983",
      "29": "745524b2-c668-4b93-9251-2d15be28d983",
      "30": "745524b2-c668-4b93-9251-2d15be28d983",
      "31": "745524b2-c668-4b93-9251-2d15be28d983"
    },
    "references": [
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 1,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 2,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 3,
        "cited_text": "Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness. B. Coding agents The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because: Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
      },
      {
        "source_id": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
        "citation_number": 4,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 5,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 6,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
        "citation_number": 7,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security Low-level orchestration framework for building stateful agents. Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents. If you're looking to quickly build agents with LangChain's create_agent (built on LangGraph), check out the LangChain Agents documentation ."
      },
      {
        "source_id": "df15d832-193b-4372-af9f-767ed0195559",
        "citation_number": 8,
        "cited_text": "Copy page Trusted by companies shaping the future of agents— including Klarna, Uber, J.P. Morgan, and more— LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents. LangGraph is very low-level, and focused entirely on agent orchestration . Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with models and tools . We will commonly use LangChain components throughout the documentation to integrate models and tools, but you don't need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain's agents that provide prebuilt architectures for common LLM and tool-calling loops. LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more."
      },
      {
        "source_id": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
        "citation_number": 9,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "df15d832-193b-4372-af9f-767ed0195559",
        "citation_number": 10,
        "cited_text": "Install pip uv Then, create a simple hello world example: Use LangSmith to trace requests, debug agent behavior, and evaluate outputs. Set LANGSMITH_TRACING=true and your API key to get started. Core benefits LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits: Durable execution : Build agents that persist through failures and can run for extended periods, resuming from where they left off. Human-in-the-loop : Incorporate human oversight by inspecting and modifying agent state at any point. Comprehensive memory : Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions. Debugging with LangSmith : Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment : Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 11,
        "cited_text": "You need to process large volumes of data Immediate responses are not required You want to optimize for cost efficiency You're running large-scale evaluations or analyses The Message Batches API is Anthropic's first implementation of this pattern. This feature is not eligible for Zero Data Retention (ZDR) . Data is retained according to the feature's standard retention policy. Message Batches API The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 12,
        "cited_text": "Large-scale evaluations: Process thousands of test cases efficiently. Content moderation: Analyze large volumes of user-generated content asynchronously. Data analysis: Generate insights or summaries for large datasets. Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries). Batch limitations A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first. The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours. Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download. Batches are scoped to a Workspace . You may view all batches (and their results) that were created within the Workspace that your API key belongs to. Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See Message Batches API rate limits . Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours. Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured spend limit ."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 13,
        "cited_text": "Shell The response will show the batch in a canceling state: JSON Using prompt caching with Message Batches The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, since batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns."
      },
      {
        "source_id": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
        "citation_number": 14,
        "cited_text": "Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangGraph ecosystem While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with: Deep Agents (new!) – Build agents that can plan, use subagents, and leverage file systems for complex tasks. LangChain – Provides integrations and composable components to streamline LLM application development. LangSmith – Helpful for agent evals and observability. Debug poor-performing LLM app runs, evaluate agent trajectories, gain visibility in production, and improve performance over time. LangSmith Deployment – Deploy and scale agents effortlessly with a purpose-built deployment platform for long-running, stateful workflows. Discover, reuse, configure, and share agents across teams – and iterate quickly with visual prototyping in LangSmith Studio ."
      },
      {
        "source_id": "df15d832-193b-4372-af9f-767ed0195559",
        "citation_number": 15,
        "cited_text": "LangGraph ecosystem While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with: [ LangSmith Observability Trace requests, evaluate outputs, and monitor deployments in one place. Prototype locally with LangGraph, then move to production with integrated observability and evaluation to build more reliable agent systems. Learn more](https://langchain-ai.github.io/langsmith/observability)"
      },
      {
        "source_id": "ab884bf8-fdcf-4673-b2c3-74050c1cdda0",
        "citation_number": 16,
        "cited_text": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "ab884bf8-fdcf-4673-b2c3-74050c1cdda0",
        "citation_number": 17,
        "cited_text": "Repository files navigation README MIT license [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning This repo holds the code, demos, and log files for Reflexion: Language Agents with Verbal Reinforcement Learning by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao. We have released the LeetcodeHardGym here To Run: reasoning (HotPotQA) We have provided a set of notebooks to easily run, explore, and interact with the results of the reasoning experiments. Each experiment consists of a random sample of 100 questions from the HotPotQA distractor dataset. Each question in the sample is attempted by an agent with a specific type and reflexion strategy."
      },
      {
        "source_id": "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c",
        "citation_number": 18,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing CC-BY-4.0 license MIT license Security AutoGen AutoGen is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans. Important: if you are new to AutoGen, please checkout Microsoft Agent Framework . AutoGen will still be maintained and continue to receive bug fixes and critical security patches. Read our announcement . Installation AutoGen requires Python 3.10 or later ."
      },
      {
        "source_id": "7f53054f-3ccd-4ee2-9d91-fbb5445fbc6c",
        "citation_number": 19,
        "cited_text": "The ecosystem also supports two essential developer tools : AutoGen Studio provides a no-code GUI for building multi-agent applications. AutoGen Bench provides a benchmarking suite for evaluating agent performance. You can use the AutoGen framework and developer tools to create applications for your domain. For example, Magentic-One is a state-of-the-art multi-agent team built using AgentChat API and Extensions API that can handle a variety of tasks that require web browsing, code execution, and file handling."
      },
      {
        "source_id": "58d56788-da63-44d1-8a77-1a315c11ac38",
        "citation_number": 20,
        "cited_text": "More options More options Latest commit PedramNavid docs: update all model references from Claude 4.5 to Claude 4.6 ( #375 ) Open commit details success 2 months ago 944b94a · 2 months ago History History Open commit details History main Breadcrumbs claude-cookbooks / patterns / agents / Top Folders and files <cited_table>",
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
              "### parent directory",
              "",
              "",
              "",
              ""
            ],
            [
              "prompts",
              "",
              "prompts",
              "Update research_lead_agent.md",
              "9 months ago"
            ],
            [
              "README.md",
              "",
              "README.md",
              "cookbook for 'Building Effective Agents'",
              "2 years ago"
            ],
            [
              "basic_workflows.ipynb",
              "",
              "basic_workflows.ipynb",
              "Lint + Format all cookbooks/scripts (",
              "5 months ago"
            ],
            [
              "evaluator_optimizer.ipynb",
              "",
              "evaluator_optimizer.ipynb",
              "Lint + Format all cookbooks/scripts (",
              "5 months ago"
            ],
            [
              "orchestrator_workers.ipynb",
              "",
              "orchestrator_workers.ipynb",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
            ],
            [
              "util.py",
              "",
              "util.py",
              "docs: update all model references from Claude 4.5 to Claude 4.6 (",
              "2 months ago"
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
        "source_id": "58d56788-da63-44d1-8a77-1a315c11ac38",
        "citation_number": 21,
        "cited_text": "README.md Outline Building Effective Agents Cookbook Reference implementation for Building Effective Agents by Erik Schluntz and Barry Zhang. This repository contains example minimal implementations of common agent workflows discussed in the blog: Basic Building Blocks Prompt Chaining Routing Multi-LLM Parallelization Advanced Workflows Orchestrator-Subagents Evaluator-Optimizer Getting Started See the Jupyter notebooks for detailed examples: Basic Workflows Evaluator-Optimizer Workflow Orchestrator-Workers Workflow"
      },
      {
        "source_id": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
        "citation_number": 22,
        "cited_text": "arXiv:2203.14465 (cs) [Submitted on 28 Mar 2022 ( v1 ), last revised 20 May 2022 (this version, v2)] Title: STaR: Bootstrapping Reasoning With Reasoning Authors: Eric Zelikman , Yuhuai Wu , Jesse Mu , Noah D. Goodman View a PDF of the paper titled STaR: Bootstrapping Reasoning With Reasoning, by Eric Zelikman and 3 other authors View PDF Abstract: Generating step-by-step \"chain-of-thought\" rationales improves language model performance on complex reasoning tasks like mathematics or commonsense question-answering. However, inducing language model rationale generation currently requires either constructing massive rationale datasets or sacrificing accuracy by using only few-shot inference. We propose a technique to iteratively leverage a small number of rationale examples and a large dataset without rationales, to bootstrap the ability to perform successively more complex reasoning. This technique, the \"Self-Taught Reasoner\" (STaR), relies on a simple loop: generate rationales to answer many questions, prompted with a few rationale examples; if the generated answers are wrong, try again to generate a rationale given the correct answer; fine-tune on all the rationales that ultimately yielded correct answers; repeat. We show that STaR significantly improves performance on multiple datasets compared to a model fine-tuned to directly predict final answers, and performs comparably to fine-tuning a 30\\times larger state-of-the-art language model on CommensenseQA. Thus, STaR lets a model improve itself by learning from its own generated reasoning."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 23,
        "cited_text": "Building Effective AI Agents \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Building effective agents Published Dec 19, 2024 We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks. Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 24,
        "cited_text": "Combining and customizing these patterns These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity only when it demonstrably improves outcomes. Summary Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 25,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 26,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 27,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 28,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 29,
        "cited_text": "There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 30,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 31,
        "cited_text": "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 (\"Prompt Engineering your Tools\"). Autonomous agent When to use agents: Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在 2025-2026 年的背景下，「Evaluator-Optimizer 与 Reflection」领域的研究已从基础的提示工程演进为**深度集成模型原生能力**与**工程化模式**的高度融合。以下是基于来源对该领域最新研究突破、技术趋势及未来方向的解析：\n\n### 1. 2025-2026 年核心技术趋势与论文方向\n\n*   **模型原生思维能力（Native Reasoning）**：最新模型如 Claude 4.6 引入了**扩展思维（Extended Thinking）**和**自适应思维（Adaptive Thinking）**能力 [1, 2]。这标志着 Agent 的纠错不再仅依赖外部循环，而是可以在单次推理中进行更深层次的逻辑自检。\n*   **长链推理与超大输出（Extended Output）**：为了支持复杂任务的自我纠错，系统现在支持单次生成高达 **300,000 个 token** 的内容 [3]。这允许 Agent 记录极其详尽的推理链（Chain-of-Thought），用于解决需要大规模代码重构或长篇文档生成的纠错任务 [3, 4]。\n*   **言语强化学习（Verbal Reinforcement Learning）**：以 *Reflexion* 框架为代表的研究（NeurIPS 2023 的深度演进）依然是核心 [5]。该技术突破了权重更新的限制，通过在**情节记忆（Episodic Memory）**中维护反思文本，使 Agent 能够通过“言语反馈”在后续尝试中自我强化 [5]。\n*   **自教推理引导（STaR 模式）**：*STaR (Self-Taught Reasoner)* 技术通过让模型为问题生成推理链并进行迭代微调，实现了**自我提升循环** [4]。研究显示，这种方法能让较小规模的模型在特定任务上达到 30 倍规模模型的性能水平 [4]。\n\n### 2. 重要架构模式\n\n*   **简单组合模式取代复杂框架**：行业趋势正从过度抽象的框架转向**简单、可组合的模式（Composable Patterns）** [6]。核心模式包括：\n    *   **Evaluator-Optimizer**：通过一个模型生成，另一个模型根据明确标准提供迭代反馈，类似于人类的协作写作过程 [7, 8]。\n    *   **Orchestrator-Workers**：由协调者动态拆解任务并分发给专业子智能体，适用于无法预见子任务数量的复杂场景 [8, 9]。\n*   **状态化与持久化（Stateful Agents）**：利用 **LangGraph** 等框架将 Agent 逻辑表示为有向图，支持**中断（Interrupts）**、**时间旅行（Time Travel）**和**持久化存储**，使 Agent 能在失败后从精确断点恢复并进行人工干预 [10-12]。\n\n### 3. 未解决的挑战\n\n*   **错误累积与复合误差**：自主 Agent 在多轮循环中容易产生**错误堆叠（Compounding Errors）** [13]。如果初始规划出现偏差，后续的自我反思可能无法有效将其拉回正轨。\n*   **智能体-计算机接口（ACI）的脆弱性**：Agent 与工具交互时的微小歧义（如相对路径 vs 绝对路径）会导致纠错失败 [14]。目前仍需大量人工投入来优化工具文档和接口定义 [15, 16]。\n*   **成本与时延的权衡**：Agentic 系统（尤其是带有深层反思循环的系统）通常以显著增加的延迟和 token 成本为代价 [17]。虽然**批处理（Batch Processing）**能降低 50% 的成本，但牺牲了实时性 [2, 18]。\n*   **透明度与调试难度**：复杂的抽象层往往掩盖了底层的 prompt 逻辑，使得在多 Agent 协作中的故障排除变得极其困难 [19]。\n\n### 4. 未来可能的突破点\n\n*   **深度智能体（Deep Agents）**：新一代 Agent 将更深入地整合文件系统权限、子智能体调度和端到端规划能力，具备更强的环境适应性 [20]。\n*   **模型上下文协议（MCP）的普及**：通过 MCP 实现工具生态的标准化集成，减少 ACI 层的适配成本，使 Agent 能够无缝接入第三方专业工具进行纠错 [21, 22]。\n*   **可验证的反馈循环（Verifiable Feedback）**：特别是在编码 Agent 领域，利用**编译器**和**自动化测试**作为“地面真理（Ground Truth）”提供客观信号，将是实现完全自主纠错的关键 [23-25]。\n*   **自适应推理量**：未来的模型将能够根据任务难度自动调整推理步数（Reasoning Effort），在简单纠错与深度反思之间取得最优效率平衡 [26]。",
    "conversation_id": "76fa4855-9011-4940-a25f-ed7a56c07636",
    "sources_used": [
      "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
      "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
      "745524b2-c668-4b93-9251-2d15be28d983",
      "58d56788-da63-44d1-8a77-1a315c11ac38",
      "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "df15d832-193b-4372-af9f-767ed0195559",
      "b94aaa34-c224-4c3d-9654-3aa0d24c9852"
    ],
    "citations": {
      "1": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "2": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "3": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "4": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
      "5": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
      "6": "745524b2-c668-4b93-9251-2d15be28d983",
      "7": "745524b2-c668-4b93-9251-2d15be28d983",
      "8": "58d56788-da63-44d1-8a77-1a315c11ac38",
      "9": "745524b2-c668-4b93-9251-2d15be28d983",
      "10": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "11": "df15d832-193b-4372-af9f-767ed0195559",
      "12": "df15d832-193b-4372-af9f-767ed0195559",
      "13": "745524b2-c668-4b93-9251-2d15be28d983",
      "14": "745524b2-c668-4b93-9251-2d15be28d983",
      "15": "745524b2-c668-4b93-9251-2d15be28d983",
      "16": "745524b2-c668-4b93-9251-2d15be28d983",
      "17": "745524b2-c668-4b93-9251-2d15be28d983",
      "18": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
      "19": "745524b2-c668-4b93-9251-2d15be28d983",
      "20": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
      "21": "745524b2-c668-4b93-9251-2d15be28d983",
      "22": "b94aaa34-c224-4c3d-9654-3aa0d24c9852",
      "23": "745524b2-c668-4b93-9251-2d15be28d983",
      "24": "745524b2-c668-4b93-9251-2d15be28d983",
      "25": "745524b2-c668-4b93-9251-2d15be28d983",
      "26": "b94aaa34-c224-4c3d-9654-3aa0d24c9852"
    },
    "references": [
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 1,
        "cited_text": "Batch processing - Claude API Docs Loading... Developer Guide API Reference MCP Resources Release Notes English Log in Search... ⌘K First steps Intro to Claude Quickstart Models & pricing Models overview Choosing a model What's new in Claude 4.6 Migration guide Model deprecations Pricing Build with Claude Features overview Using the Messages API Handling stop reasons Prompting best practices Model capabilities Extended thinking Adaptive thinking Effort Fast mode (beta: research preview) Structured outputs Citations Streaming Messages Batch processing PDF support Search results Multilingual support Embeddings Vision"
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 2,
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
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 3,
        "cited_text": "Extended output (beta) The output-300k-2026-03-24 beta header raises the max_tokens cap to 300,000 for batch requests using Claude Opus 4.6 or Claude Sonnet 4.6. Include the header to generate outputs far longer than the standard limit (64k to 128k depending on model) in a single turn. Extended output is available on the Message Batches API only, not the synchronous Messages API. It is supported on the Claude API and is not available on Amazon Bedrock, Vertex AI, or Microsoft Foundry. Use extended output for long-form generation such as book-length drafts and technical documentation, exhaustive structured data extraction, large code-generation scaffolds, and long reasoning chains."
      },
      {
        "source_id": "01dc596f-d7fc-4a2a-93b2-f2927b62ee5e",
        "citation_number": 4,
        "cited_text": "arXiv:2203.14465 (cs) [Submitted on 28 Mar 2022 ( v1 ), last revised 20 May 2022 (this version, v2)] Title: STaR: Bootstrapping Reasoning With Reasoning Authors: Eric Zelikman , Yuhuai Wu , Jesse Mu , Noah D. Goodman View a PDF of the paper titled STaR: Bootstrapping Reasoning With Reasoning, by Eric Zelikman and 3 other authors View PDF Abstract: Generating step-by-step \"chain-of-thought\" rationales improves language model performance on complex reasoning tasks like mathematics or commonsense question-answering. However, inducing language model rationale generation currently requires either constructing massive rationale datasets or sacrificing accuracy by using only few-shot inference. We propose a technique to iteratively leverage a small number of rationale examples and a large dataset without rationales, to bootstrap the ability to perform successively more complex reasoning. This technique, the \"Self-Taught Reasoner\" (STaR), relies on a simple loop: generate rationales to answer many questions, prompted with a few rationale examples; if the generated answers are wrong, try again to generate a rationale given the correct answer; fine-tune on all the rationales that ultimately yielded correct answers; repeat. We show that STaR significantly improves performance on multiple datasets compared to a model fine-tuned to directly predict final answers, and performs comparably to fine-tuning a 30\\times larger state-of-the-art language model on CommensenseQA. Thus, STaR lets a model improve itself by learning from its own generated reasoning."
      },
      {
        "source_id": "4b8b8ebd-20c9-4737-bfd9-ffe40417c56b",
        "citation_number": 5,
        "cited_text": "arXiv:2303.11366 (cs) [Submitted on 20 Mar 2023 ( v1 ), last revised 10 Oct 2023 (this version, v4)] Title: Reflexion: Language Agents with Verbal Reinforcement Learning Authors: Noah Shinn , Federico Cassano , Edward Berman , Ashwin Gopinath , Karthik Narasimhan , Shunyu Yao View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors View PDF Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 6,
        "cited_text": "Building Effective AI Agents \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Building effective agents Published Dec 19, 2024 We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks. Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 7,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "58d56788-da63-44d1-8a77-1a315c11ac38",
        "citation_number": 8,
        "cited_text": "README.md Outline Building Effective Agents Cookbook Reference implementation for Building Effective Agents by Erik Schluntz and Barry Zhang. This repository contains example minimal implementations of common agent workflows discussed in the blog: Basic Building Blocks Prompt Chaining Routing Multi-LLM Parallelization Advanced Workflows Orchestrator-Subagents Evaluator-Optimizer Getting Started See the Jupyter notebooks for detailed examples: Basic Workflows Evaluator-Optimizer Workflow Orchestrator-Workers Workflow"
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 9,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
        "citation_number": 10,
        "cited_text": "Note Looking for the JS/TS library? Check out LangGraph.js and the JS docs . Why use LangGraph? LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent: Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off. Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution. Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions. Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "df15d832-193b-4372-af9f-767ed0195559",
        "citation_number": 11,
        "cited_text": "Persistence Durable execution Streaming Interrupts Time travel Memory Subgraphs Production Application structure Test LangSmith Studio Agent Chat UI LangSmith Deployment LangSmith Observability Frontend Overview Graph execution LangGraph APIs Graph API Functional API Runtime On this page Install Core benefits LangGraph ecosystem Acknowledgements LangGraph overview Copy page Gain control with LangGraph to design agents that reliably handle complex tasks"
      },
      {
        "source_id": "df15d832-193b-4372-af9f-767ed0195559",
        "citation_number": 12,
        "cited_text": "Install pip uv Then, create a simple hello world example: Use LangSmith to trace requests, debug agent behavior, and evaluate outputs. Set LANGSMITH_TRACING=true and your API key to get started. Core benefits LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits: Durable execution : Build agents that persist through failures and can run for extended periods, resuming from where they left off. Human-in-the-loop : Incorporate human oversight by inspecting and modifying agent state at any point. Comprehensive memory : Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions. Debugging with LangSmith : Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Production-ready deployment : Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 13,
        "cited_text": "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails. Examples where agents are useful: The following examples are from our own implementations: A coding Agent to resolve SWE-bench tasks , which involve edits to many files based on a task description; Our “computer use” reference implementation , where Claude uses a computer to accomplish tasks. High-level flow of a coding agent"
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 14,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 15,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 16,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 17,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "7dd4077b-dce0-4435-b440-736c0c9d0c89",
        "citation_number": 18,
        "cited_text": "You need to process large volumes of data Immediate responses are not required You want to optimize for cost efficiency You're running large-scale evaluations or analyses The Message Batches API is Anthropic's first implementation of this pattern. This feature is not eligible for Zero Data Retention (ZDR) . Data is retained according to the feature's standard retention policy. Message Batches API The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 19,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "ea79c0f9-6f80-4808-98ee-0263b2bfd65b",
        "citation_number": 20,
        "cited_text": "Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangGraph ecosystem While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with: Deep Agents (new!) – Build agents that can plan, use subagents, and leverage file systems for complex tasks. LangChain – Provides integrations and composable components to streamline LLM application development. LangSmith – Helpful for agent evals and observability. Debug poor-performing LLM app runs, evaluate agent trajectories, gain visibility in production, and improve performance over time. LangSmith Deployment – Deploy and scale agents effortlessly with a purpose-built deployment platform for long-running, stateful workflows. Discover, reuse, configure, and share agents across teams – and iterate quickly with visual prototyping in LangSmith Studio ."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 21,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "b94aaa34-c224-4c3d-9654-3aa0d24c9852",
        "citation_number": 22,
        "cited_text": "Agents Overview Build agents Agent Builder Node reference Safety in building agents Agents SDK Deploy in your product ChatKit Custom theming Widgets Actions Advanced integration Optimize Agent evals Trace grading Voice agents Tools Using tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter"
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 23,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 24,
        "cited_text": "Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness. B. Coding agents The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because: Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
      },
      {
        "source_id": "745524b2-c668-4b93-9251-2d15be28d983",
        "citation_number": 25,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "b94aaa34-c224-4c3d-9654-3aa0d24c9852",
        "citation_number": 26,
        "cited_text": "Community Programs, meetups, and support for builders Start searching API Dashboard Search the docs Search docs Suggested response_format reasoning_effort streaming tools Primary navigation API API Reference Codex ChatGPT Resources Search docs Suggested response_format reasoning_effort streaming tools Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API"
      }
    ]
  }
}
