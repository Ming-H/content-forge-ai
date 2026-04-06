# 知识库：基础综合实战：构建一个多模式研究助手

生成时间: 2026-04-06 17:47
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "构建一个多模式研究助手的核心技术架构遵循“**以大型语言模型（LLM）为核心控制器**”的通用框架，其关键组件通常被划分为：**规划（Planning）、记忆（Memory）、工具使用（Tool Use）以及感知（Perception）** [1, 2]。\n\n以下是基于来源提取的核心架构和技术要点：\n\n### 1. 技术演进路线\n智能体系统的技术演进经历了从简单到复杂、从预定义到自主的转变：\n*   **基础构建模块**：从最初的单一模型调用，演进为**增强型LLM**，即集成检索（RAG）、工具和记忆能力的模型 [3, 4]。\n*   **工作流编排（Workflows）**：通过预定义的代码路径（如**提示词链条**、**路由**、**并行化**）来协调LLM和工具 [5-8]。\n*   **自主智能体（Agents）**：模型开始能够动态地指导自己的流程和工具使用。例如，从简单的 **Chain of Thought (CoT)** 演进到 **ReAct**（协同推理与行动）[6, 9-11]。\n*   **多模式集成**：感知能力的演进使得助手能处理视觉和音频输入。如 **JARVIS-1** 和 **HOLMES** 框架，实现了多模态信息收集与决策的结合 [12, 13]。\n\n### 2. 核心算法名称\n在规划、记忆和优化方面，主要涉及以下核心算法：\n*   **推理与规划算法**：\n    *   **Chain of Thought (CoT)**：通过“分步思考”分解复杂任务 [9]。\n    *   **Tree of Thoughts (ToT)**：在每一步探索多种推理可能性，形成树状结构 [14]。\n    *   **ReAct**：结合推理踪迹和特定任务动作（如搜索API）的协同算法 [10, 11]。\n    *   **Plan-and-Solve (PS)**：先制定计划再执行子任务，以减少步骤缺失错误 [15]。\n*   **记忆检索算法 (MIPS)**：用于从外部向量数据库快速检索信息，包括 **HNSW**（分层导航小世界）、**FAISS**（聚类量化检索）、**ScaNN**（各向异性向量量化）等 [16, 17]。\n*   **自我修正算法**：**Reflexion**（通过动态记忆和自我反思改进推理）以及 **Chain of Hindsight (CoH)**（利用历史反馈序列进行微调）[18, 19]。\n\n### 3. 主要架构模式\n*   **大脑-感知-动作架构**：这是LLM智能体的通用概念框架 [20, 21]。\n*   **编排器-工人模式 (Orchestrator-Workers)**：中央LLM动态分解任务并委派给专用工人模型，适用于复杂的搜索或编码任务 [22, 23]。\n*   **评估器-优化器模式 (Evaluator-Optimizer)**：一个模型生成响应，另一个模型提供反馈循环，类似于人类的写作打磨过程 [23]。\n*   **多代理协同模式**：如 **HOLMES** 框架，允许LLM利用多模态模型（MLLM）和API共同收集信息 [13]。\n\n### 4. 关键技术指标\n评估多模式研究助手的性能通常关注以下维度：\n*   **感知与动作水平**：\n    *   **Level-1 (调用)**：正确调用给定API并响应结果的能力 [24]。\n    *   **Level-2 (检索)**：搜索、阅读文档并学习使用新API的能力 [24]。\n    *   **Level-3 (规划)**：在模糊请求下进行多次API调用解决复杂问题的能力 [24]。\n*   **检索精度**：在向量搜索中常用的 **Recall@10**（前10名结果的召回率）[25]。\n*   **限制性指标**：\n    *   **有限上下文长度**：模型处理历史信息、指令和API上下文的带宽限制 [26]。\n    *   **成功率 (Success Rate)**：例如 ReAct 在交互式决策基准测试中，相较于纯动作或纯推理方法有显著的成功率提升 [11]。\n*   **可靠性指标**：包括格式解析的准确性（避免LLM生成错误的JSON格式）以及针对意外错误的计划调整鲁棒性 [26, 27]。\n\n**注：** 来源中并未直接提及名为“基础综合实战：构建一个多模式研究助手”的特定课程或书籍标题，以上内容是根据来源中关于“多模态研究智能体”和“LLM助手架构”的通用技术描述总结而成。",
    "conversation_id": "54ddd743-e565-4f91-b37e-54224c545793",
    "sources_used": [
      "5cc6ca32-64da-4942-8f57-268afe35e163",
      "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "fbb19078-5a5c-4b0e-be0d-148af878ed49",
      "cee20c76-4ec0-4596-a7db-5532200f330f",
      "cc526314-9bbb-47bc-a346-aff4b1f54a3d"
    ],
    "citations": {
      "1": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "2": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "3": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "4": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "5": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "6": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "7": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "8": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "9": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "10": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "11": "fbb19078-5a5c-4b0e-be0d-148af878ed49",
      "12": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "13": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "14": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "15": "cc526314-9bbb-47bc-a346-aff4b1f54a3d",
      "16": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "17": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "18": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "19": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "20": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "21": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "22": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "23": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "24": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "25": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "26": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "27": "5cc6ca32-64da-4942-8f57-268afe35e163"
    },
    "references": [
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 1,
        "cited_text": "LLM Powered Autonomous Agents | Lil'Log Lil'Log | Posts Archive Search Tags FAQ LLM Powered Autonomous Agents Date: June 23, 2023 | Estimated Reading Time: 31 min | Author: Lilian Weng Table of Contents Agent System Overview Component One: Planning Task Decomposition Self-Reflection Component Two: Memory Types of Memory Maximum Inner Product Search (MIPS) Component Three: Tool Use Case Studies Scientific Discovery Agent Generative Agents Simulation Proof-of-Concept Examples Challenges Citation References"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 2,
        "cited_text": "Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT , GPT-Engineer and BabyAGI , serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver. Agent System Overview # In a LLM-powered autonomous agent system, LLM functions as the agent's brain, complemented by several key components: Planning Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks. Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results. Memory Short-term memory: I would consider all the in-context learning (See Prompt Engineering ) as utilizing short-term memory of the model to learn. Long-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, often by leveraging an external vector store and fast retrieval. Tool use The agent learns to call external APIs for extra information that is missing from the model weights (often hard to change after pre-training), including current information, code execution capability, access to proprietary information sources and more."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 3,
        "cited_text": "See our cookbook for some sample implementations. Building blocks, workflows, and agents In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents. Building block: The augmented LLM The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 4,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 5,
        "cited_text": "In this post, we share what we've learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents. What are agents? \"Agent\" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems , but draw an important architectural distinction between workflows and ** agents**:"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 6,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 7,
        "cited_text": "Workflow: Prompt chaining Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see \"gate” in the diagram below) on any intermediate steps to ensure that the process is still on track. The prompt chaining workflow When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 8,
        "cited_text": "Examples where prompt chaining is useful: Generating Marketing copy, then translating it into a different language. Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline. Workflow: Routing Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 9,
        "cited_text": "Overview of a LLM-powered autonomous agent system. Component One: Planning # A complicated task usually involves many steps. An agent needs to know what they are and plan ahead. Task Decomposition # Chain of thought (CoT; Wei et al. 2022 ) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model's thinking process."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 10,
        "cited_text": "Self-Reflection # Self-reflection is a vital aspect that allows autonomous agents to improve iteratively by refining past action decisions and correcting previous mistakes. It plays a crucial role in real-world tasks where trial and error are inevitable. ReAct ( Yao et al. 2023 ) integrates reasoning and acting within LLM by extending the action space to be a combination of task-specific discrete actions and the language space. The former enables LLM to interact with the environment (e.g. use Wikipedia search API), while the latter prompting LLM to generate reasoning traces in natural language."
      },
      {
        "source_id": "fbb19078-5a5c-4b0e-be0d-148af878ed49",
        "citation_number": 11,
        "cited_text": "arXiv:2210.03629 (cs) [Submitted on 6 Oct 2022 ( v1 ), last revised 10 Mar 2023 (this version, v3)] Title: ReAct: Synergizing Reasoning and Acting in Language Models Authors: Shunyu Yao , Jeffrey Zhao , Dian Yu , Nan Du , Izhak Shafran , Karthik Narasimhan , Yuan Cao View a PDF of the paper titled ReAct: Synergizing Reasoning and Acting in Language Models, by Shunyu Yao and 6 other authors View PDF Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: this https URL"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 12,
        "cited_text": "Planning Plan formulation [2023/11] JARVIS-1: Open-world Multi-task Agents with Memory-Augmented Multimodal Language Models. ZiHao Wang (Peking University) et al. arXiv. [ paper ] [ code ] [2023/10] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models. Andy Zhou (University of Illinois Urbana-Champaign) et al. arXiv. [ paper ] [ project page ] [ code ] [2023/05] Tree of Thoughts: Deliberate Problem Solving with Large Language Models. Shunyu Yao (Princeton University) et al. arXiv. [ paper ] [ code ] [2023/05] Plan, Eliminate, and Track -- Language Models are Good Teachers for Embodied Agents. Yue Wu (Carnegie Mellon University) et al. arXiv. [ paper ] [2023/05] Reasoning with Language Model is Planning with World Model. Shibo Hao (UC San Diego) et al. arXiv. [ paper ] [ code ] [2023/05] SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks. Bill Yuchen Lin (Allen Institute for Artificial Intelligence) et al. arXiv. [ paper ] [ code ] [2023/04] LLM+P: Empowering Large Language Models with Optimal Planning Proficiency. Bo Liu (University of Texas at Austin) et al. arXiv. [ paper ] [ code ] [2023/03] HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. Yongliang Shen (Microsoft Research Asia) et al. arXiv. [ paper ] [ code ] [2023/02] Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents. ZiHao Wang (Peking University) et al. arXiv. [ paper ] [ code ] [2022/05] Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. Denny Zhou (Google Research) et al. arXiv. [ paper ] [2022/05] MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning. Ehud Karpas (AI21 Labs) et al. arXiv. [ paper ] [2022/04] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances. Michael Ahn (Robotics at Google) et al. arXiv. [ paper ] [2023/05] Agents: An Open-source Framework for Autonomous Language Agents. Wangchunshu Zhou (AIWaves) et al. arXiv. [ paper ] [ code ] [2022/12] Don't Generate, Discriminate: A Proposal for Grounding Language Models to Real-World Environments. Yu Gu (The Ohio State University) et al. ACL. [ paper ] [ code ]"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 13,
        "cited_text": "1.3 Action: Expand Action Space of LLM-based Agents 1.3.1 Tool Using [2024/02] Towards Uncertainty-Aware Language Agent. Jiuzhou Han (Monash University) et al. arXiv. [ paper ] [ project page ] [ code ] [2023/10] OpenAgents: An Open Platform for Language Agents in the Wild. XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ demo ] [2023/10] Lemur: Harmonizing Natural Language and Code for Language Agents Yiheng Xu (University of Hong Kong) et al. arXiv. [ paper ] [ code ] [2023/10] Towards End-to-End Embodied Decision Making via Multi-modal Large Language Model: Explorations with GPT4-Vision and Beyond Liang Chen (Peking University) et al. arXiv. [ paper ] [ code ] HOLMES is a multi-agent cooperation framework that allows LLMs to leverage MLLMs and APIs to gather multimodal information for informed decision-making. [2023/07] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] [ dataset ] ToolLLM is a general tool-use framework encompassing data construction, model training and evaluation. [2023/05] Large Language Models as Tool Makers. Tianle Cai (Princeton University) et al. arXiv. [ paper ] [ code ] LATM is a closed-loop framework that takes an initial step towards removing the dependency on the availability of existing tools. [2023/05] CREATOR: Disentangling Abstract and Concrete Reasonings of Large Language Models through Tool Creation. Cheng Qian (Tsinghua University) et al. arXiv. [ paper ] CREATOR is a novel framework that empowers LLMs to create their own tools through documentation and code realization. [2023/04] Tool Learning with Foundation Models. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] This survey primarily introduces a new paradigm called \"tool learning based on foundational models\", which combines the advantages of specialized tools and foundational models, achieving higher precision, efficiency, and automation in problem-solving. [2023/04] ChemCrow: Augmenting large-language models with chemistry tools. Andres M Bran (Laboratory of Artificial Chemical Intelligence, ISIC, EPFL) et al. arXiv. [ paper ] [ code ] ChemCrow is an LLM chemistry agent that integrates 13 expert-designed tools and augments the LLM performance in chemistry and emerge new capabilities. [2023/04] GeneGPT: Augmenting Large Language Models with Domain Tools for Improved Access to Biomedical Information. Qiao Jin (National Institutes of Health), Yifan Yang, Qingyu Chen, Zhiyong Lu. arXiv. [ paper ] [ code ] GeneGPT is a model that answer genomics questions. It introduces a novel method for handling challenges with hallucinations by teaching LLMs to use the Web APIs. [2023/04] OpenAGI: When LLM Meets Domain Experts. Yingqiang Ge (Rutgers University) et al. arXiv. [ paper ] [ code ] OpenAGI is an open-source AGI research platform. It introduces a paradigm of LLMs operating various expert models for complex task-solving and proposes an RLTF mechanism to improve the LLM's task-solving ability. [2023/03] HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. Yongliang Shen (Zhejiang University) et al. arXiv. [ paper ] [ code ] HuggingGPT is a system that leverages LLMs to connect various and multimodal AI models in machine learning communities to solve AI tasks. [2023/03] Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models. Chenfei Wu (Microsoft Research Asia) et al. arXiv. [ paper ] [ code ] Visual ChatGPT is a system that opens the door to investigating the visual roles of ChatGPT with the help of Visual Foundation Models. [2023/02] Augmented Language Models: a Survey. Grégoire Mialon (Meta AI) et al. TMLR. [ paper ] This survey reviews works in which LMs are augmented with the ability to use tools. Augmented LMs can use external modules to expand their context processing ability. [2023/02] Toolformer: Language Models Can Teach Themselves to Use Tools. Timo Schick (Meta AI) et al. arXiv. [ paper ]"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 14,
        "cited_text": "Tree of Thoughts ( Yao et al. 2023 ) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote. Task decomposition can be done (1) by LLM with simple prompting like \"Steps for XYZ.\\n1.\" , \"What are the subgoals for achieving XYZ?\" , (2) by using task-specific instructions; e.g. \"Write a story outline.\" for writing a novel, or (3) with human inputs."
      },
      {
        "source_id": "cc526314-9bbb-47bc-a346-aff4b1f54a3d",
        "citation_number": 15,
        "cited_text": "Abstract: Large language models (LLMs) have recently been shown to deliver impressive performance in various NLP tasks. To tackle multi-step reasoning tasks, few-shot chain-of-thought (CoT) prompting includes a few manually crafted step-by-step reasoning demonstrations which enable LLMs to explicitly generate reasoning steps and improve their reasoning task accuracy. To eliminate the manual effort, Zero-shot-CoT concatenates the target problem statement with \"Let's think step by step\" as an input prompt to LLMs. Despite the success of Zero-shot-CoT, it still suffers from three pitfalls: calculation errors, missing-step errors, and semantic misunderstanding errors. To address the missing-step errors, we propose Plan-and-Solve (PS) Prompting. It consists of two components: first, devising a plan to divide the entire task into smaller subtasks, and then carrying out the subtasks according to the plan. To address the calculation errors and improve the quality of generated reasoning steps, we extend PS prompting with more detailed instructions and derive PS+ prompting. We evaluate our proposed prompting strategy on ten datasets across three reasoning problems. The experimental results over GPT-3 show that our proposed zero-shot prompting consistently outperforms Zero-shot-CoT across all datasets by a large margin, is comparable to or exceeds Zero-shot-Program-of-Thought Prompting, and has comparable performance with 8-shot CoT prompting on the math reasoning problem. The code can be found at this https URL ."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 16,
        "cited_text": "Categorization of human memory. We can roughly consider the following mappings: Sensory memory as learning embedding representations for raw inputs, including text, image or other modalities; Short-term memory as in-context learning. It is short and finite, as it is restricted by the finite context window length of Transformer. Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval. Maximum Inner Product Search (MIPS) # The external memory can alleviate the restriction of finite attention span. A standard practice is to save the embedding representation of information into a vector store database that can support fast maximum inner-product search ( MIPS ). To optimize the retrieval speed, the common choice is the approximate nearest neighbors (ANN) algorithm to return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 17,
        "cited_text": "A couple common choices of ANN algorithms for fast MIPS: LSH (Locality-Sensitive Hashing): It introduces a hashing function such that similar input items are mapped to the same buckets with high probability, where the number of buckets is much smaller than the number of inputs. ANNOY (Approximate Nearest Neighbors Oh Yeah): The core data structure are random projection trees , a set of binary trees where each non-leaf node represents a hyperplane splitting the input space into half and each leaf stores one data point. Trees are built independently and at random, so to some extent, it mimics a hashing function. ANNOY search happens in all the trees to iteratively search through the half that is closest to the query and then aggregates the results. The idea is quite related to KD tree but a lot more scalable. HNSW (Hierarchical Navigable Small World): It is inspired by the idea of small world networks where most nodes can be reached by any other nodes within a small number of steps; e.g. “six degrees of separation” feature of social networks. HNSW builds hierarchical layers of these small-world graphs, where the bottom layers contain the actual data points. The layers in the middle create shortcuts to speed up search. When performing a search, HNSW starts from a random node in the top layer and navigates towards the target. When it can't get any closer, it moves down to the next layer, until it reaches the bottom layer. Each move in the upper layers can potentially cover a large distance in the data space, and each move in the lower layers refines the search quality. FAISS (Facebook AI Similarity Search): It operates on the assumption that in high dimensional space, distances between nodes follow a Gaussian distribution and thus there should exist clustering of data points. FAISS applies vector quantization by partitioning the vector space into clusters and then refining the quantization within clusters. Search first looks for cluster candidates with coarse quantization and then further looks into each cluster with finer quantization. ScaNN (Scalable Nearest Neighbors): The main innovation in ScaNN is anisotropic vector quantization . It quantizes a data point x i to x ~ i such that the inner product ⟨ q , x i ⟩ is as similar to the original distance of ∠ q , x ~ i as possible, instead of picking the closet quantization centroid points."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 18,
        "cited_text": "The ReAct prompt template incorporates explicit steps for LLM to think, roughly formatted as: Examples of reasoning trajectories for knowledge-intensive tasks (e.g. HotpotQA, FEVER) and decision-making tasks (e.g. AlfWorld Env, WebShop). (Image source: Yao et al. 2023 ). In both experiments on knowledge-intensive tasks and decision-making tasks, ReAct works better than the Act -only baseline where Thought: … step is removed. Reflexion ( Shinn & Labash 2023 ) is a framework to equip agents with dynamic memory and self-reflection capabilities to improve reasoning skills. Reflexion has a standard RL setup, in which the reward model provides a simple binary reward and the action space follows the setup in ReAct where the task-specific action space is augmented with language to enable complex reasoning steps. After each action a t , the agent computes a heuristic h t and optionally may decide to reset the environment to start a new trial depending on the self-reflection results."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 19,
        "cited_text": "Experiments on AlfWorld Env and HotpotQA. Hallucination is a more common failure than inefficient planning in AlfWorld. (Image source: Shinn & Labash, 2023 ) Chain of Hindsight (CoH; Liu et al. 2023 ) encourages the model to improve on its own outputs by explicitly presenting it with a sequence of past outputs, each annotated with feedback. Human feedback data is a collection of D h = { ( x , y i , r i , z i ) } i = 1 n , where x is the prompt, each y i is a model completion, r i is the human rating of y i , and z i is the corresponding human-provided hindsight feedback. Assume the feedback tuples are ranked by reward, r n ≥ r n − 1 ≥ ⋯ ≥ r 1 The process is supervised fine-tuning where the data is a sequence in the form of τ h = ( x , z i , y i , z j , y j , … , z n , y n ) , where ≤ i ≤ j ≤ n . The model is finetuned to only predict y n where conditioned on the sequence prefix, such that the model can self-reflect to produce better output based on the feedback sequence. The model can optionally receive multiple rounds of instructions with human annotators at test time."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 20,
        "cited_text": "In this repository, we provide a systematic and comprehensive survey on LLM-based agents, and list some must-read papers. Specifically, we start by the general conceptual framework for LLM-based agents: comprising three main components: brain, perception, and action, and the framework can be tailored to suit different applications. Subsequently, we explore the extensive applications of LLM-based agents in three aspects: single-agent scenarios, multi-agent scenarios, and human-agent cooperation. Following this, we delve into agent societies, exploring the behavior and personality of LLM-based agents, the social phenomena that emerge when they form societies, and the insights they offer for human society. Finally, we discuss a range of key topics and open problems within the field."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 21,
        "cited_text": "We greatly appreciate any contributions via PRs, issues, emails, or other methods. Table of Content (ToC) The Rise and Potential of Large Language Model Based Agents: A Survey 🔔 News 🌟 Introduction Table of Content (ToC) 1. The Birth of An Agent: Construction of LLM-based Agents 1.1 Brain: Primarily Composed of An LLM 1.1.1 Natural Language Interaction High-quality generation Deep understanding 1.1.2 Knowledge Pretrain model Linguistic knowledge Commonsense knowledge Actionable knowledge Potential issues of knowledge 1.1.3 Memory Memory capability Raising the length limit of Transformers Summarizing memory Compressing memories with vectors or data structures Memory retrieval 1.1.4 Reasoning & Planning Reasoning Planning Plan formulation Plan reflection 1.1.5 Transferability and Generalization Unseen task generalization In-context learning Continual learning 1.2 Perception: Multimodal Inputs for LLM-based Agents 1.2.1 Visual 1.2.2 Audio 1.3 Action: Expand Action Space of LLM-based Agents 1.3.1 Tool Using 1.3.2 Embodied Action 2. Agents in Practice: Applications of LLM-based Agents 2.1 General Ability of Single Agent 2.1.1 Task-oriented Deployment 2.1.2 Innovation-oriented Deployment 2.1.3 Lifecycle-oriented Deployment 2.2 Coordinating Potential of Multiple Agents 2.2.1 Cooperative Interaction for Complementarity 2.2.2 Adversarial Interaction for Advancement 2.3 Interactive Engagement between Human and Agent 2.3.1 Instructor-Executor Paradigm Education Health Other Application 2.3.2 Equal Partnership Paradigm Empathetic Communicator Human-Level Participant 3. Agent Society: From Individuality to Sociality 3.1 Behavior and Personality of LLM-based Agents 3.1.1 Social Behavior Individual behaviors Group behaviors 3.1.2 Personality Cognition Emotion Character 3.2 Environment for Agent Society 3.2.1 Text-based Environment 3.2.2 Virtual Sandbox Environment 3.2.3 Physical Environment 3.3 Society Simulation with LLM-based Agents 4. Other Topics 4.1 Benchmarks for LLM-based Agents 4.2 Training and Optimizing LLM-based Agents Citation Project Maintainers & Contributors Contact Star History"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 22,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 23,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 24,
        "cited_text": "This benchmark evaluates the agent's tool use capabilities at three levels: Level-1 evaluates the ability to call the API . Given an API's description, the model needs to determine whether to call a given API, call it correctly, and respond properly to API returns. Level-2 examines the ability to retrieve the API . The model needs to search for possible APIs that may solve the user's requirement and learn how to use them by reading documentation. Level-3 assesses the ability to plan API beyond retrieve and call . Given unclear user requests (e.g. schedule group meetings, book flight/hotel/restaurant for a trip), the model may have to conduct multiple API calls to solve it."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 25,
        "cited_text": "Comparison of MIPS algorithms, measured in recall@10. (Image source: Google Blog, 2020 ) Check more MIPS algorithms and performance comparison in ann-benchmarks.com . Component Three: Tool Use # Tool use is a remarkable and distinguishing characteristic of human beings. We create, modify and utilize external objects to do things that go beyond our physical and cognitive limits. Equipping LLMs with external tools can significantly extend the model capabilities. A picture of a sea otter using rock to crack open a seashell, while floating in the water. While some other animals can use tools, the complexity is not comparable with humans. (Image source: Animals using tools )"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 26,
        "cited_text": "pytest dataclasses Conversatin samples: Challenges # After going through key ideas and demos of building LLM-centered agents, I start to see a couple common limitations: Finite context length : The restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses. The design of the system has to work with this limited communication bandwidth, while mechanisms like self-reflection to learn from past mistakes would benefit a lot from long or infinite context windows. Although vector stores and retrieval can provide access to a larger knowledge pool, their representation power is not as powerful as full attention. Challenges in long-term planning and task decomposition : Planning over a lengthy history and effectively exploring the solution space remain challenging. LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error. Reliability of natural language interface : Current agent system relies on natural language as an interface between LLMs and external components such as memory and tools. However, the reliability of model outputs is questionable, as LLMs may make formatting errors and occasionally exhibit rebellious behavior (e.g. refuse to follow an instruction). Consequently, much of the agent demo code focuses on parsing model output."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 27,
        "cited_text": "The generative agent architecture. (Image source: Park et al. 2023 ) This fun simulation results in emergent social behavior, such as information diffusion, relationship memory (e.g. two agents continuing the conversation topic) and coordination of social events (e.g. host a party and invite many others). Proof-of-Concept Examples # AutoGPT has drawn a lot of attention into the possibility of setting up autonomous agents with LLM as the main controller. It has quite a lot of reliability issues given the natural language interface, but nevertheless a cool proof-of-concept demo. A lot of code in AutoGPT is about format parsing."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "构建一个多模式（多模态）研究助手是一个复杂的工程，其实现细节涉及从底层算法到上层架构的多重优化。根据提供的来源，该系统的实现细节可解析如下：\n\n### 1. 核心算法流程\n多模式研究助手的核心在于**“感知-规划-行动”**的闭环 [1]。\n*   **规划（Planning）与推理**：\n    *   **ReAct 算法**：这是最核心的推理模式。系统交替生成“推理轨迹（Thought）”和“任务特定操作（Action）” [2, 3]。这种交错方式允许模型在执行过程中（如调用搜索 API）根据环境反馈更新其搜索计划 [3]。\n    *   **Plan-and-Solve (PS) 提示**：为了解决研究任务中常见的“漏步骤”问题，该算法首先将复杂研究课题分解为子任务清单，再按计划执行 [4]。\n    *   **Tree of Thoughts (ToT)**：在研究方案设计阶段，通过探索多种推理路径并利用分类器或投票机制评估每条路径的优劣，形成树状决策结构 [5]。\n*   **多模态感知循环**：\n    *   **HOLMES 框架**：这是一个典型的多模式实现模式，允许核心 LLM 利用多模态模型（MLLM）和 API 协同收集视觉或音频等非文字信息 [6]。\n*   **自我修正**：\n    *   **Evaluator-Optimizer 模式**：一个模型负责生成报告草稿，另一个模型依据预设的研究标准提供反馈并驱动循环优化 [7]。\n\n### 2. 关键代码架构模式\n研究助手的实现通常采用**简单、可组合的模式**而非重度框架 [8]。\n*   **大脑与工具接口**：LLM 作为核心控制器，通过 **JSON Schema** 定义的函数工具（Function Tools）与外部环境交互 [9, 10]。\n*   **Orchestrator-Workers（编排器-工人）模式**：中央 LLM（如 GPT-5.4 或 Claude 3.5）动态分解研究任务，并将其分发给专门处理特定领域（如检索、代码分析）的“工人”模型 [11]。\n*   **MCP（模型上下文协议）集成**：通过 MCP 协议标准化连接外部数据库和研究工具，消除不同 API 间的集成复杂性 [12, 13]。\n*   **Handoffs（接力）架构**：在多代理协同中（如 OpenAI Swarm），使用“Agent”和“Handoff”原语，允许研究助手在不同能力的代理间转移任务控制权（例如从“搜索代理”转移给“论文撰写代理”） [14, 15]。\n\n### 3. 性能优化策略\n*   **延迟与效率优化**：\n    *   **并行化（Parallelization）**：在搜索环节采用“分段（Sectioning）”策略，同时并行调用多个搜索流以降低总时耗 [16, 17]。\n    *   **路由（Routing）**：将简单的查询分配给低延迟模型（如 Claude Haiku），而将复杂的综合分析任务分配给高性能模型（如 Claude Sonnet），平衡性能与成本 [18]。\n*   **上下文与精度优化**：\n    *   **Tool Search（工具搜索）**：当助手拥有数万个潜在 API 时，不一次性加载所有工具，而是先通过工具搜索功能按需加载相关函数，以节省 Context Window（上下文窗口）并减少 Token 消耗 [19, 20]。\n    *   **Prompt Caching（提示词缓存）**：对常用的系统指令和大型工具定义进行缓存，以优化长对话场景下的推理速度 [20, 21]。\n    *   **Strict Mode（严格模式）**：强制模型输出遵循 JSON 模式，确保工具调用的参数 100% 准确，避免解析错误导致的系统崩溃 [22]。\n\n### 4. 竞品技术对比与参数数据\n| 维度 | 主流系统实现 (如 OpenAI Agents SDK/Swarm) | 传统 Workflow 模式 (如早期 Dify/LangChain) |\n| :--- | :--- | :--- |\n| **控制逻辑** | **动态规划**：LLM 自主决定步骤 [23, 24] | **预定义路径**：代码硬编码流程 [23, 25] |\n| **状态管理** | **轻量/无状态**：在客户端运行，易于调试 [26, 27] | **重度/托管**：通常由服务端管理线程状态 [27] |\n| **技术指标** | **ReAct 成功率提升**：在决策测试中比基准提高 **34%** [3] | 受限于固定逻辑，应对模糊请求能力较弱 |\n| **工具容量** | **ToolLLM** 可支持 **16,000+** 真实 API [6] | 初始建议启动函数少于 **20** 个以维持精度 [28] |\n| **记忆性能** | **Recall@10**：通过 HNSW 或 ScaNN 算法实现极高召回率 [29] | 通常仅依赖简单的向量检索，缺乏多层级记忆调度 |\n\n**具体技术参数示例**：\n*   **记忆容量**：人类大脑短期记忆约包含 **7 个项目**，持续 **20-30 秒**；而研究助手的 STM（短期记忆）受限于 Transformer 的上下文窗口，LTM（长期记忆）则依托外部向量数据库实现无限存储 [30, 31]。\n*   **效率数据**：在企业级应用中，类似 Dify 这种集成工作流的系统据估算每年可为部门减少约 **18,000 小时** 的人工，每月节省 **300 人时** [32]。",
    "conversation_id": "54ddd743-e565-4f91-b37e-54224c545793",
    "sources_used": [
      "5cc6ca32-64da-4942-8f57-268afe35e163",
      "fbb19078-5a5c-4b0e-be0d-148af878ed49",
      "cc526314-9bbb-47bc-a346-aff4b1f54a3d",
      "cee20c76-4ec0-4596-a7db-5532200f330f",
      "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "2484c347-745f-4aa1-83ae-aa1196f51e74"
    ],
    "citations": {
      "1": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "2": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "3": "fbb19078-5a5c-4b0e-be0d-148af878ed49",
      "4": "cc526314-9bbb-47bc-a346-aff4b1f54a3d",
      "5": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "6": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "7": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "8": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "9": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "10": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "11": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "12": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "13": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "14": "2484c347-745f-4aa1-83ae-aa1196f51e74",
      "15": "2484c347-745f-4aa1-83ae-aa1196f51e74",
      "16": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "17": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "18": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "19": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "20": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "21": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "22": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "23": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "24": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "25": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "26": "2484c347-745f-4aa1-83ae-aa1196f51e74",
      "27": "2484c347-745f-4aa1-83ae-aa1196f51e74",
      "28": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "29": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "30": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "31": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "32": "16dd388d-10a3-4174-a924-f4aeb7a3e800"
    },
    "references": [
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 1,
        "cited_text": "LLM Powered Autonomous Agents | Lil'Log Lil'Log | Posts Archive Search Tags FAQ LLM Powered Autonomous Agents Date: June 23, 2023 | Estimated Reading Time: 31 min | Author: Lilian Weng Table of Contents Agent System Overview Component One: Planning Task Decomposition Self-Reflection Component Two: Memory Types of Memory Maximum Inner Product Search (MIPS) Component Three: Tool Use Case Studies Scientific Discovery Agent Generative Agents Simulation Proof-of-Concept Examples Challenges Citation References"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 2,
        "cited_text": "Self-Reflection # Self-reflection is a vital aspect that allows autonomous agents to improve iteratively by refining past action decisions and correcting previous mistakes. It plays a crucial role in real-world tasks where trial and error are inevitable. ReAct ( Yao et al. 2023 ) integrates reasoning and acting within LLM by extending the action space to be a combination of task-specific discrete actions and the language space. The former enables LLM to interact with the environment (e.g. use Wikipedia search API), while the latter prompting LLM to generate reasoning traces in natural language."
      },
      {
        "source_id": "fbb19078-5a5c-4b0e-be0d-148af878ed49",
        "citation_number": 3,
        "cited_text": "arXiv:2210.03629 (cs) [Submitted on 6 Oct 2022 ( v1 ), last revised 10 Mar 2023 (this version, v3)] Title: ReAct: Synergizing Reasoning and Acting in Language Models Authors: Shunyu Yao , Jeffrey Zhao , Dian Yu , Nan Du , Izhak Shafran , Karthik Narasimhan , Yuan Cao View a PDF of the paper titled ReAct: Synergizing Reasoning and Acting in Language Models, by Shunyu Yao and 6 other authors View PDF Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: this https URL"
      },
      {
        "source_id": "cc526314-9bbb-47bc-a346-aff4b1f54a3d",
        "citation_number": 4,
        "cited_text": "Abstract: Large language models (LLMs) have recently been shown to deliver impressive performance in various NLP tasks. To tackle multi-step reasoning tasks, few-shot chain-of-thought (CoT) prompting includes a few manually crafted step-by-step reasoning demonstrations which enable LLMs to explicitly generate reasoning steps and improve their reasoning task accuracy. To eliminate the manual effort, Zero-shot-CoT concatenates the target problem statement with \"Let's think step by step\" as an input prompt to LLMs. Despite the success of Zero-shot-CoT, it still suffers from three pitfalls: calculation errors, missing-step errors, and semantic misunderstanding errors. To address the missing-step errors, we propose Plan-and-Solve (PS) Prompting. It consists of two components: first, devising a plan to divide the entire task into smaller subtasks, and then carrying out the subtasks according to the plan. To address the calculation errors and improve the quality of generated reasoning steps, we extend PS prompting with more detailed instructions and derive PS+ prompting. We evaluate our proposed prompting strategy on ten datasets across three reasoning problems. The experimental results over GPT-3 show that our proposed zero-shot prompting consistently outperforms Zero-shot-CoT across all datasets by a large margin, is comparable to or exceeds Zero-shot-Program-of-Thought Prompting, and has comparable performance with 8-shot CoT prompting on the math reasoning problem. The code can be found at this https URL ."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 5,
        "cited_text": "Tree of Thoughts ( Yao et al. 2023 ) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote. Task decomposition can be done (1) by LLM with simple prompting like \"Steps for XYZ.\\n1.\" , \"What are the subgoals for achieving XYZ?\" , (2) by using task-specific instructions; e.g. \"Write a story outline.\" for writing a novel, or (3) with human inputs."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 6,
        "cited_text": "1.3 Action: Expand Action Space of LLM-based Agents 1.3.1 Tool Using [2024/02] Towards Uncertainty-Aware Language Agent. Jiuzhou Han (Monash University) et al. arXiv. [ paper ] [ project page ] [ code ] [2023/10] OpenAgents: An Open Platform for Language Agents in the Wild. XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ demo ] [2023/10] Lemur: Harmonizing Natural Language and Code for Language Agents Yiheng Xu (University of Hong Kong) et al. arXiv. [ paper ] [ code ] [2023/10] Towards End-to-End Embodied Decision Making via Multi-modal Large Language Model: Explorations with GPT4-Vision and Beyond Liang Chen (Peking University) et al. arXiv. [ paper ] [ code ] HOLMES is a multi-agent cooperation framework that allows LLMs to leverage MLLMs and APIs to gather multimodal information for informed decision-making. [2023/07] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] [ dataset ] ToolLLM is a general tool-use framework encompassing data construction, model training and evaluation. [2023/05] Large Language Models as Tool Makers. Tianle Cai (Princeton University) et al. arXiv. [ paper ] [ code ] LATM is a closed-loop framework that takes an initial step towards removing the dependency on the availability of existing tools. [2023/05] CREATOR: Disentangling Abstract and Concrete Reasonings of Large Language Models through Tool Creation. Cheng Qian (Tsinghua University) et al. arXiv. [ paper ] CREATOR is a novel framework that empowers LLMs to create their own tools through documentation and code realization. [2023/04] Tool Learning with Foundation Models. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] This survey primarily introduces a new paradigm called \"tool learning based on foundational models\", which combines the advantages of specialized tools and foundational models, achieving higher precision, efficiency, and automation in problem-solving. [2023/04] ChemCrow: Augmenting large-language models with chemistry tools. Andres M Bran (Laboratory of Artificial Chemical Intelligence, ISIC, EPFL) et al. arXiv. [ paper ] [ code ] ChemCrow is an LLM chemistry agent that integrates 13 expert-designed tools and augments the LLM performance in chemistry and emerge new capabilities. [2023/04] GeneGPT: Augmenting Large Language Models with Domain Tools for Improved Access to Biomedical Information. Qiao Jin (National Institutes of Health), Yifan Yang, Qingyu Chen, Zhiyong Lu. arXiv. [ paper ] [ code ] GeneGPT is a model that answer genomics questions. It introduces a novel method for handling challenges with hallucinations by teaching LLMs to use the Web APIs. [2023/04] OpenAGI: When LLM Meets Domain Experts. Yingqiang Ge (Rutgers University) et al. arXiv. [ paper ] [ code ] OpenAGI is an open-source AGI research platform. It introduces a paradigm of LLMs operating various expert models for complex task-solving and proposes an RLTF mechanism to improve the LLM's task-solving ability. [2023/03] HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. Yongliang Shen (Zhejiang University) et al. arXiv. [ paper ] [ code ] HuggingGPT is a system that leverages LLMs to connect various and multimodal AI models in machine learning communities to solve AI tasks. [2023/03] Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models. Chenfei Wu (Microsoft Research Asia) et al. arXiv. [ paper ] [ code ] Visual ChatGPT is a system that opens the door to investigating the visual roles of ChatGPT with the help of Visual Foundation Models. [2023/02] Augmented Language Models: a Survey. Grégoire Mialon (Meta AI) et al. TMLR. [ paper ] This survey reviews works in which LMs are augmented with the ability to use tools. Augmented LMs can use external modules to expand their context processing ability. [2023/02] Toolformer: Language Models Can Teach Themselves to Use Tools. Timo Schick (Meta AI) et al. arXiv. [ paper ]"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 7,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 8,
        "cited_text": "Building Effective AI Agents \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Building effective agents Published Dec 19, 2024 We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks. Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 9,
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
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 10,
        "cited_text": "Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT , GPT-Engineer and BabyAGI , serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver. Agent System Overview # In a LLM-powered autonomous agent system, LLM functions as the agent's brain, complemented by several key components: Planning Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks. Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results. Memory Short-term memory: I would consider all the in-context learning (See Prompt Engineering ) as utilizing short-term memory of the model to learn. Long-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, often by leveraging an external vector store and fast retrieval. Tool use The agent learns to call external APIs for extra information that is missing from the model weights (often hard to change after pre-training), including current information, code execution capability, access to proprietary information sources and more."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 11,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 12,
        "cited_text": "[ Connect ](https://dify.ai/#connect) Supercharge AI applications with global LLMs, RAG pipelines, tools, agent strategies, and more. Add Wings with Tools Expand capabilities of your AI application with powerful plugins. Bridge Your Systems / Platforms with Native MCP Integration Access external APIs, databases, and services through standardized MCP protocols, eliminating integration complexity and maintenance overhead. Support HTTP-based MCP services (protocol 2025-03-26) with pre-authorized and auth-free modes."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 13,
        "cited_text": "Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Responses How it works Function tool example Defining functions Defining namespaces Tool search Handling function calls Additional configurations Streaming Custom tools Copy Page More page actions"
      },
      {
        "source_id": "2484c347-745f-4aa1-83ae-aa1196f51e74",
        "citation_number": 14,
        "cited_text": "Overview Swarm focuses on making agent coordination and execution lightweight, highly controllable, and easily testable. It accomplishes this through two primitive abstractions: Agent s and handoffs . An Agent encompasses instructions and tools , and can at any point choose to hand off a conversation to another Agent . These primitives are powerful enough to express rich dynamics between tools and networks of agents, allowing you to build scalable, real-world solutions while avoiding a steep learning curve."
      },
      {
        "source_id": "2484c347-745f-4aa1-83ae-aa1196f51e74",
        "citation_number": 15,
        "cited_text": "Response Fields <cited_table> Agents An Agent simply encapsulates a set of instructions with a set of functions (plus some additional settings below), and has the capability to hand off execution to another Agent .",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Field",
              "Type",
              "Description"
            ],
            [
              "messages",
              "List",
              "A list of message objects generated during the conversation. Very similar to"
            ],
            [
              "agent",
              "Agent",
              "The last agent to handle a message."
            ],
            [
              "context_variables",
              "dict",
              "The same as the input variables, plus any changes."
            ]
          ]
        }
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 16,
        "cited_text": "Workflow: Parallelization LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning : Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs. The parallelization workflow When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 17,
        "cited_text": "Examples where parallelization is useful: Sectioning : Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response. Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model's performance on a given prompt. Voting : Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem. Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 18,
        "cited_text": "The routing workflow When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm. Examples where routing is useful: Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools. Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 19,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 20,
        "cited_text": "When to use allowed_tools You might want to configure an allowed_tools list in case you want to make only a subset of tools available across model requests, but not modify the list of tools you pass in, so you can maximize savings from prompt caching . You can also set tool_choice to \"none\" to imitate the behavior of passing no functions. When you use tool search, tool_choice still applies to the tools that are currently callable in the turn. This is most useful after you load a subset of tools and want to constrain the model to that subset."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 21,
        "cited_text": "Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents"
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 22,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 23,
        "cited_text": "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents , on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems. When (and when not) to use agents When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 24,
        "cited_text": "Examples where evaluator-optimizer is useful: Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques. Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted. Agents Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 25,
        "cited_text": "In this post, we share what we've learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents. What are agents? \"Agent\" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as agentic systems , but draw an important architectural distinction between workflows and ** agents**:"
      },
      {
        "source_id": "2484c347-745f-4aa1-83ae-aa1196f51e74",
        "citation_number": 26,
        "cited_text": "Note Swarm Agents are not related to Assistants in the Assistants API. They are named similarly for convenience, but are otherwise completely unrelated. Swarm is entirely powered by the Chat Completions API and is hence stateless between calls. Why Swarm Swarm explores patterns that are lightweight, scalable, and highly customizable by design. Approaches similar to Swarm are best suited for situations dealing with a large number of independent capabilities and instructions that are difficult to encode into a single prompt."
      },
      {
        "source_id": "2484c347-745f-4aa1-83ae-aa1196f51e74",
        "citation_number": 27,
        "cited_text": "The Assistants API is a great option for developers looking for fully-hosted threads and built in memory management and retrieval. However, Swarm is an educational resource for developers curious to learn about multi-agent orchestration. Swarm runs (almost) entirely on the client and, much like the Chat Completions API, does not store state between calls. Examples Check out /examples for inspiration! Learn more about each one in its README. basic : Simple examples of fundamentals like setup, function calling, handoffs, and context variables triage_agent : Simple example of setting up a basic triage step to hand off to the right agent weather_agent : Simple example of function calling airline : A multi-agent setup for handling different customer service requests in an airline context. support_bot : A customer service bot which includes a user interface agent and a help center agent with several tools personal_shopper : A personal shopping agent that can help with making sales and refunding orders"
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 28,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 29,
        "cited_text": "Comparison of MIPS algorithms, measured in recall@10. (Image source: Google Blog, 2020 ) Check more MIPS algorithms and performance comparison in ann-benchmarks.com . Component Three: Tool Use # Tool use is a remarkable and distinguishing characteristic of human beings. We create, modify and utilize external objects to do things that go beyond our physical and cognitive limits. Equipping LLMs with external tools can significantly extend the model capabilities. A picture of a sea otter using rock to crack open a seashell, while floating in the water. While some other animals can use tools, the complexity is not comparable with humans. (Image source: Animals using tools )"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 30,
        "cited_text": "Sensory Memory : This is the earliest stage of memory, providing the ability to retain impressions of sensory information (visual, auditory, etc) after the original stimuli have ended. Sensory memory typically only lasts for up to a few seconds. Subcategories include iconic memory (visual), echoic memory (auditory), and haptic memory (touch). Short-Term Memory (STM) or Working Memory : It stores information that we are currently aware of and needed to carry out complex cognitive tasks such as learning and reasoning. Short-term memory is believed to have the capacity of about 7 items ( Miller 1956 ) and lasts for 20-30 seconds. Long-Term Memory (LTM): Long-term memory can store information for a remarkably long time, ranging from a few days to decades, with an essentially unlimited storage capacity. There are two subtypes of LTM: Explicit / declarative memory: This is memory of facts and events, and refers to those memories that can be consciously recalled, including episodic memory (events and experiences) and semantic memory (facts and concepts). Implicit / procedural memory: This type of memory is unconscious and involves skills and routines that are performed automatically, like riding a bike or typing on a keyboard."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 31,
        "cited_text": "Categorization of human memory. We can roughly consider the following mappings: Sensory memory as learning embedding representations for raw inputs, including text, image or other modalities; Short-term memory as in-context learning. It is short and finite, as it is restricted by the finite context window length of Transformer. Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval. Maximum Inner Product Search (MIPS) # The external memory can alleviate the restriction of finite attention span. A standard practice is to save the embedding representation of information into a vector store database that can support fast maximum inner-product search ( MIPS ). To optimize the retrieval speed, the common choice is the approximate nearest neighbors (ANN) algorithm to return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup."
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 32,
        "cited_text": "Yoshiaki Umezu Division General Manager, Ricoh Estimated an annual reduction of 18,000 hours. Save 300 man-hours each month. Enterprise Q&A Bot: Serve 19,000+ employees across 20+ departments. G e t s t a r t e d [ Startup ](https://dify.ai/) Unlock Your Potential with AI From AI idea validation to seek growth, Dify offers everything you need to make a real impact. Enjoy everything out of the box and hit MVP with speed and agility in record time. G e t S t a r t e d Go to Market at Velocity 01 Focus on your idea and validate your idea in record time without complex settings."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "根据提供的来源，构建一个多模式（多模态）研究助手的真实应用场景、部署方案及实战经验总结如下：\n\n### 1. 真实应用场景与案例\n多模式助手正广泛应用于从科研创新到日常办公的多个领域：\n*   **科学研究与发现**：\n    *   **化学研究 (ChemCrow)**：集成 13 种专家设计的工具，辅助完成有机合成、药物发现和材料设计 [1, 2]。\n    *   **医学应用**：利用可操作知识处理医疗领域的专业查询 [3]。\n*   **软件开发与编码**：\n    *   **自主解决 GitHub 问题**：研究助手通过 **SWE-bench** 验证，能够仅根据拉取请求描述解决真实的 GitHub issue [4]。\n    *   **自动化测试与程序分析**：用于自主测试代理和辅助程序分析 [5]。\n*   **企业实务场景**：\n    *   **客户支持**：处理退款申请、技术支持等开放式任务，并能根据用户定义的解决方案衡量成功率 [6]。\n    *   **教育与辅导**：如 **Dona** 虚拟语音助手协助学生注册课程，或通过链式调用 LLM 增强私人辅导能力 [7, 8]。\n*   **社会仿真与模拟**：\n    *   **Generative Agents**：在沙盒环境中模拟 25 个虚拟角色的社交行为，实现信息扩散和社交事件协调 [9, 10]。\n\n### 2. 工业级部署方案\n*   **基础设施平台**：**Dify** 提供生产级的 AI 基础设施，支持 RAG 管道、可观察性和 native MCP（模型上下文协议）集成 [11, 12]。\n*   **企业级案例**：\n    *   **沃尔沃 (Volvo Cars)**：利用 Dify 进行快速原型验证，提高 frontier AI 领域的导航能力 [13]。\n    *   **理光 (Ricoh)**：通过无代码平台加速“公民开发者”开发，其企业问答机器人服务于 1.9 万名员工，涵盖 20 多个部门 [14, 15]。\n*   **生产化建议**：\n    *   **OpenAI Agents SDK**：作为 Swarm 的演进版本，是目前推荐的生产级多代理编排工具 [16]。\n    *   **架构模式**：倾向于使用简单、可组合的模式（如路由、并行化），而非复杂的重度框架 [17, 18]。\n\n### 3. 开源项目实战案例\n*   **LangChain**：用于构建代理和 LLM 驱动应用的平台，支持深度代理（Deep Agents）和复杂的编排框架 LangGraph [19, 20]。\n*   **Dify**：开源的智能体工作流构建器（GitHub 8k+ Stars），支持可视化拖拽构建复杂任务流 [21, 22]。\n*   **OpenAgents**：香港大学开发的开放平台，用于在野外环境（Wild）部署和评估语言智能体 [1, 22]。\n*   **概念验证 (PoC) 案例**：如 **AutoGPT**、**GPT-Engineer** 和 **BabyAGI**，展示了 LLM 作为核心控制器在文件操作和代码生成中的潜力 [23, 24]。\n\n### 4. 性能基准数据\n*   **效率指标**：\n    *   在企业部署中，预计每年减少约 **18,000 小时** 的人工工作量，每月节省 **300 人时** [15]。\n*   **任务成功率**：\n    *   **ReAct 算法**：在 ALFWorld 和 WebShop 基准测试中，相较于纯行动（Act-only）基线，成功率分别提升了 **34%** 和 **10%** [25]。\n    *   **MAgIC 基准**：在多智能体设置中，通过概率图形建模实现了平均 **50%** 的性能提升 [26]。\n*   **召回性能**：**Recall@10** 是衡量 MIPS（最大内积搜索）算法（如 HNSW、FAISS）性能的关键指标，用于评估内存检索的精准度 [27]。\n\n### 5. 开发者最佳实践\n*   **三大核心原则**：保持设计**简单**；确立**透明度**（展示规划步骤）；通过详尽的工具文档和测试优化**代理-计算机接口 (ACI)** [28]。\n*   **工具设计 (ACI)**：\n    *   将工具描述写得像给初级开发人员的文档一样清晰 [29]。\n    *   **Poka-yoke（防错）**：修改参数设计以减少模型犯错的可能性 [29]。\n*   **提升准确度**：\n    *   使用**严格模式 (Strict Mode)**，确保函数调用 100% 遵循 JSON Schema [30]。\n    *   将初始可用的函数数量控制在 **20 个以下**，以获得更高的准确率，不常用的工具通过“工具搜索”延迟加载 [31]。\n\n### 6. 常见踩坑经验\n*   **框架过度抽象**：复杂的框架可能隐藏底层的 Prompt 和响应，导致调试极其困难，建议从直接调用 API 开始构建 [32]。\n*   **路径与环境依赖**：在构建 **SWE-bench** 代理时，发现模型在移动目录后会因相对路径而出错，改为**强制使用绝对路径**后问题得以解决 [33]。\n*   **有限的上下文窗口**：由于上下文容量限制，系统设计必须权衡历史信息、指令和 API 调用上下文的带宽 [34]。\n*   **自然语言接口的不可靠性**：模型可能会产生格式错误或拒绝执行指令，因此代码中通常需要大量的逻辑来解析和纠正模型输出 [24, 34]。",
    "conversation_id": "54ddd743-e565-4f91-b37e-54224c545793",
    "sources_used": [
      "cee20c76-4ec0-4596-a7db-5532200f330f",
      "5cc6ca32-64da-4942-8f57-268afe35e163",
      "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "2484c347-745f-4aa1-83ae-aa1196f51e74",
      "15477146-e56c-444c-b116-190a187047b7",
      "fbb19078-5a5c-4b0e-be0d-148af878ed49",
      "b1502d82-776c-44c7-8886-a172bf69e0f5"
    ],
    "citations": {
      "1": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "2": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "3": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "4": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "5": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "6": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "7": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "8": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "9": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "10": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "11": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "12": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "13": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "14": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "15": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "16": "2484c347-745f-4aa1-83ae-aa1196f51e74",
      "17": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "18": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "19": "15477146-e56c-444c-b116-190a187047b7",
      "20": "15477146-e56c-444c-b116-190a187047b7",
      "21": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "22": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "23": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "24": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "25": "fbb19078-5a5c-4b0e-be0d-148af878ed49",
      "26": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "27": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "28": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "29": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "30": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "31": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "32": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "33": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "34": "5cc6ca32-64da-4942-8f57-268afe35e163"
    },
    "references": [
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 1,
        "cited_text": "1.3 Action: Expand Action Space of LLM-based Agents 1.3.1 Tool Using [2024/02] Towards Uncertainty-Aware Language Agent. Jiuzhou Han (Monash University) et al. arXiv. [ paper ] [ project page ] [ code ] [2023/10] OpenAgents: An Open Platform for Language Agents in the Wild. XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ demo ] [2023/10] Lemur: Harmonizing Natural Language and Code for Language Agents Yiheng Xu (University of Hong Kong) et al. arXiv. [ paper ] [ code ] [2023/10] Towards End-to-End Embodied Decision Making via Multi-modal Large Language Model: Explorations with GPT4-Vision and Beyond Liang Chen (Peking University) et al. arXiv. [ paper ] [ code ] HOLMES is a multi-agent cooperation framework that allows LLMs to leverage MLLMs and APIs to gather multimodal information for informed decision-making. [2023/07] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] [ dataset ] ToolLLM is a general tool-use framework encompassing data construction, model training and evaluation. [2023/05] Large Language Models as Tool Makers. Tianle Cai (Princeton University) et al. arXiv. [ paper ] [ code ] LATM is a closed-loop framework that takes an initial step towards removing the dependency on the availability of existing tools. [2023/05] CREATOR: Disentangling Abstract and Concrete Reasonings of Large Language Models through Tool Creation. Cheng Qian (Tsinghua University) et al. arXiv. [ paper ] CREATOR is a novel framework that empowers LLMs to create their own tools through documentation and code realization. [2023/04] Tool Learning with Foundation Models. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] This survey primarily introduces a new paradigm called \"tool learning based on foundational models\", which combines the advantages of specialized tools and foundational models, achieving higher precision, efficiency, and automation in problem-solving. [2023/04] ChemCrow: Augmenting large-language models with chemistry tools. Andres M Bran (Laboratory of Artificial Chemical Intelligence, ISIC, EPFL) et al. arXiv. [ paper ] [ code ] ChemCrow is an LLM chemistry agent that integrates 13 expert-designed tools and augments the LLM performance in chemistry and emerge new capabilities. [2023/04] GeneGPT: Augmenting Large Language Models with Domain Tools for Improved Access to Biomedical Information. Qiao Jin (National Institutes of Health), Yifan Yang, Qingyu Chen, Zhiyong Lu. arXiv. [ paper ] [ code ] GeneGPT is a model that answer genomics questions. It introduces a novel method for handling challenges with hallucinations by teaching LLMs to use the Web APIs. [2023/04] OpenAGI: When LLM Meets Domain Experts. Yingqiang Ge (Rutgers University) et al. arXiv. [ paper ] [ code ] OpenAGI is an open-source AGI research platform. It introduces a paradigm of LLMs operating various expert models for complex task-solving and proposes an RLTF mechanism to improve the LLM's task-solving ability. [2023/03] HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. Yongliang Shen (Zhejiang University) et al. arXiv. [ paper ] [ code ] HuggingGPT is a system that leverages LLMs to connect various and multimodal AI models in machine learning communities to solve AI tasks. [2023/03] Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models. Chenfei Wu (Microsoft Research Asia) et al. arXiv. [ paper ] [ code ] Visual ChatGPT is a system that opens the door to investigating the visual roles of ChatGPT with the help of Visual Foundation Models. [2023/02] Augmented Language Models: a Survey. Grégoire Mialon (Meta AI) et al. TMLR. [ paper ] This survey reviews works in which LMs are augmented with the ability to use tools. Augmented LMs can use external modules to expand their context processing ability. [2023/02] Toolformer: Language Models Can Teach Themselves to Use Tools. Timo Schick (Meta AI) et al. arXiv. [ paper ]"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 2,
        "cited_text": "Case Studies # Scientific Discovery Agent # ChemCrow ( Bran et al. 2023 ) is a domain-specific example in which LLM is augmented with 13 expert-designed tools to accomplish tasks across organic synthesis, drug discovery, and materials design. The workflow, implemented in LangChain , reflects what was previously described in the ReAct and MRKLs and combines CoT reasoning with tools relevant to the tasks: The LLM is provided with a list of tool names, descriptions of their utility, and details about the expected input/output. It is then instructed to answer a user-given prompt using the tools provided when necessary. The instruction suggests the model to follow the ReAct format - Thought, Action, Action Input, Observation ."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 3,
        "cited_text": "Commonsense knowledge [2022/10] Language Models of Code are Few-Shot Commonsense Learners. Aman Madaan et al.arXiv. [ paper ] [2021/04] Relational World Knowledge Representation in Contextual Language Models: A Review. Tara Safavi et al. arXiv. [ paper ] [2019/11] How Can We Know What Language Models Know? Zhengbao Jiang et al.arXiv. [ paper ] Actionable knowledge [2023/07] Large language models in medicine. Arun James Thirunavukarasu et al. nature. [ paper ] [2023/06] DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation. Yuhang Lai et al. ICML. [ paper ] [2022/10] Language Models of Code are Few-Shot Commonsense Learners. Aman Madaan et al. arXiv. [ paper ] [2022/02] A Systematic Evaluation of Large Language Models of Code. Frank F. Xu et al.arXiv. [ paper ] [2021/10] Training Verifiers to Solve Math Word Problems. Karl Cobbe et al. arXiv. [ paper ]"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 4,
        "cited_text": "In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements. Appendix 2: Prompt engineering your tools No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 5,
        "cited_text": "2.1.2 Innovation-oriented Deployment [2023/10] OpenAgents: An Open Platform for Language Agents in the Wild. XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ demo ] [2023/08] The Hitchhiker's Guide to Program Analysis: A Journey with Large Language Models. Haonan Li (UC Riverside) et al. arXiv. [ paper ] [2023/08] ChatMOF: An Autonomous AI System for Predicting and Generating Metal-Organic Frameworks. Yeonghun Kang (Korea Advanced Institute of Science and Technology) et al. arXiv. [ paper ] [2023/07] Math Agents: Computational Infrastructure, Mathematical Embedding, and Genomics. Melanie Swan (University College London) et al. arXiv. [ paper ] [2023/06] Towards Autonomous Testing Agents via Conversational Large Language Models. Robert Feldt (Chalmers University of Technology) et al. arXiv. [ paper ] [2023/04] Emergent autonomous scientific research capabilities of large language models. Daniil A. Boiko (CMU) et al. arXiv. [ paper ] [2023/04] ChemCrow: Augmenting large-language models with chemistry tools. Andres M Bran (Laboratory of Artificial Chemical Intelligence, ISIC, EPFL) et al. arXiv. [ paper ] [ code ] [2022/03] ScienceWorld: Is your Agent Smarter than a 5th Grader? Ruoyao Wang (University of Arizona) et al. arXiv. [ paper ] [ code ]"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 6,
        "cited_text": "A. Customer support Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because: Support interactions naturally follow a conversation flow while requiring access to external information and actions; Tools can be integrated to pull customer data, order history, and knowledge base articles; Actions such as issuing refunds or updating tickets can be handled programmatically; and Success can be clearly measured through user-defined resolutions."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 7,
        "cited_text": "Summarizing memory [2023/10] Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading Howard Chen (Princeton University) et al. arXiv. [ paper ] [2023/09] Empowering Private Tutoring by Chaining Large Language Models Yulin Chen (Tsinghua University) et al. arXiv. [ paper ] [2023/08] ExpeL: LLM Agents Are Experiential Learners. Andrew Zhao (Tsinghua University) et al. arXiv. [ paper ] [ code ] [2023/08] ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate. Chi-Min Chan (Tsinghua University) et al. arXiv. [ paper ] [ code ] [2023/05] MemoryBank: Enhancing Large Language Models with Long-Term Memory. Wanjun Zhong (Harbin Institute of Technology) et al. arXiv. [ paper ] [ code ] [2023/04] Generative Agents: Interactive Simulacra of Human Behavior. Joon Sung Park (Stanford University) et al. arXiv. [ paper ] [ code ] [2023/04] Unleashing Infinite-Length Input Capacity for Large-scale Language Models with Self-Controlled Memory System. Xinnian Liang (Beihang University) et al. arXiv. [ paper ] [ code ] [2023/03] Reflexion: Language Agents with Verbal Reinforcement Learning. Noah Shinn (Northeastern University) et al. arXiv. [ paper ] [ code ] [2023/05] RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text. Wangchunshu Zhou (AIWaves) et al. arXiv. [ paper ] [ code ]"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 8,
        "cited_text": "2.3 Interactive Engagement between Human and Agent 2.3.1 Instructor-Executor Paradigm Education [2023/07] Math Agents: Computational Infrastructure, Mathematical Embedding, and Genomics. Melanie Swan (UCL) et al. arXiv. [ paper ] Communicate with humans to help them understand and use mathematics. [2023/03] Hey Dona! Can you help me with student course registration? Vishesh Kalvakurthi (MSU) et al. arXiv. [ paper ] This is a developed application called Dona that offers virtual voice assistance in student course registration, where humans provide instructions."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 9,
        "cited_text": "LLM Powered Autonomous Agents | Lil'Log Lil'Log | Posts Archive Search Tags FAQ LLM Powered Autonomous Agents Date: June 23, 2023 | Estimated Reading Time: 31 min | Author: Lilian Weng Table of Contents Agent System Overview Component One: Planning Task Decomposition Self-Reflection Component Two: Memory Types of Memory Maximum Inner Product Search (MIPS) Component Three: Tool Use Case Studies Scientific Discovery Agent Generative Agents Simulation Proof-of-Concept Examples Challenges Citation References"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 10,
        "cited_text": "Generative Agents ( Park, et al. 2023 ) is super fun experiment where 25 virtual characters, each controlled by a LLM-powered agent, are living and interacting in a sandbox environment, inspired by The Sims. Generative agents create believable simulacra of human behavior for interactive applications. The design of generative agents combines LLM with memory, planning and reflection mechanisms to enable agents to behave conditioned on past experience, as well as to interact with other agents. Memory stream: is a long-term memory module (external database) that records a comprehensive list of agents' experience in natural language. Each element is an observation , an event directly provided by the agent. - Inter-agent communication can trigger new natural language statements. Retrieval model: surfaces the context to inform the agent's behavior, according to relevance, recency and importance. Recency: recent events have higher scores Importance: distinguish mundane from core memories. Ask LM directly. Relevance: based on how related it is to the current situation / query. Reflection mechanism: synthesizes memories into higher level inferences over time and guides the agent's future behavior. They are higher-level summaries of past events (<- note that this is a bit different from self-reflection above) Prompt LM with 100 most recent observations and to generate 3 most salient high-level questions given a set of observations/statements. Then ask LM to answer those questions. Planning & Reacting : translate the reflections and the environment information into actions Planning is essentially in order to optimize believability at the moment vs in time. Prompt template: {Intro of an agent X}. Here is X's plan today in broad strokes: 1) Relationships between agents and observations of one agent by another are all taken into consideration for planning and reacting. Environment information is present in a tree structure."
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 11,
        "cited_text": "Build Production-Ready Agentic Workflow G e t S t a r t e d Build Production-Ready Agentic Workflow Build Production-Ready AI Agent GitHub stars on GitHub Dify offers everything you need — agentic workflows, RAG pipelines, integrations, and observability — all in one place, putting AI power into your hands. Forum Now Live Join discussions, share insights, and explore how others are building with Dify. [ BUILD ](https://dify.ai/) From sketch to live, bring your AI vision to life and beyond. Amplify with Any Global Large Language Models"
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 12,
        "cited_text": "[ Connect ](https://dify.ai/#connect) Supercharge AI applications with global LLMs, RAG pipelines, tools, agent strategies, and more. Add Wings with Tools Expand capabilities of your AI application with powerful plugins. Bridge Your Systems / Platforms with Native MCP Integration Access external APIs, databases, and services through standardized MCP protocols, eliminating integration complexity and maintenance overhead. Support HTTP-based MCP services (protocol 2025-03-26) with pre-authorized and auth-free modes."
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 13,
        "cited_text": "Secure 03 Enterprise-grade security for your critical data assets. [ Enterprise ](https://dify.ai/) Solid AI Infrastructure for Enterprise Success The AI transformation for enterprise requires not just tools, but grounded infrastructure. Dify offers a reliable platform to distribute AI capabilities across multiple departments for unparalleled efficiency. L e a r n M o r e a b o u t D i f y E n t e r p r i s e IMPACT 10 K+ Teams 60 Industries 150 Countries 1 M+ Applications In this climate of perpetual beta, tools enabling rapid validation aren't just helpful, they're existential. For Volvo Cars, strategically navigating this AI frontier, this is where Dify delivers indispensable value."
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 14,
        "cited_text": "Ewen Wang Head of AI & Data APAC Dify's intuitive interface allows our teams to rapidly design and deploy complex natural language processing pipelines, enabling us to improve the quality of our assessment products while reducing cost and time to market. Gary Feng Director of AI What makes Dify stands out is its ability to democratize AI agent development. By combining powerful AI/ML capabilities on a no-code platform, its rapid deployment and intuitive interface make it highly accessible even for beginners, significantly accelerating citizen development."
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 15,
        "cited_text": "Yoshiaki Umezu Division General Manager, Ricoh Estimated an annual reduction of 18,000 hours. Save 300 man-hours each month. Enterprise Q&A Bot: Serve 19,000+ employees across 20+ departments. G e t s t a r t e d [ Startup ](https://dify.ai/) Unlock Your Potential with AI From AI idea validation to seek growth, Dify offers everything you need to make a real impact. Enjoy everything out of the box and hit MVP with speed and agility in record time. G e t S t a r t e d Go to Market at Velocity 01 Focus on your idea and validate your idea in record time without complex settings."
      },
      {
        "source_id": "2484c347-745f-4aa1-83ae-aa1196f51e74",
        "citation_number": 16,
        "cited_text": "Repository files navigation README MIT license Security Swarm (experimental, educational) Important Swarm is now replaced by the OpenAI Agents SDK , which is a production-ready evolution of Swarm. The Agents SDK features key improvements and will be actively maintained by the OpenAI team. We recommend migrating to the Agents SDK for all production use cases. Install Requires Python 3.10+ or Usage Table of Contents Overview Examples Documentation Running Swarm Agents Functions Streaming Evaluations Utils"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 17,
        "cited_text": "Building Effective AI Agents \\ Anthropic Skip to main content Skip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Building effective agents Published Dec 19, 2024 We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks. Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 18,
        "cited_text": "Combining and customizing these patterns These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity only when it demonstrably improves outcomes. Summary Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."
      },
      {
        "source_id": "15477146-e56c-444c-b116-190a187047b7",
        "citation_number": 19,
        "cited_text": "README Code of conduct More Repository files items Contributing MIT license Security The agent engineering platform. LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves. Note Looking for the JS/TS library? Check out LangChain.js . Quickstart If you're looking for more advanced customization or agent orchestration, check out LangGraph , our framework for building controllable agent workflows."
      },
      {
        "source_id": "15477146-e56c-444c-b116-190a187047b7",
        "citation_number": 20,
        "cited_text": "Tip For developing, debugging, and deploying AI agents and LLM applications, see LangSmith . LangChain ecosystem While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. Deep Agents — Build agents that can plan, use subagents, and leverage file systems for complex tasks LangGraph — Build agents that can reliably handle complex tasks with our low-level agent orchestration framework Integrations — Chat & embedding models, tools & toolkits, and more LangSmith — Agent evals, observability, and debugging for LLM apps LangSmith Deployment — Deploy and scale agents with a purpose-built platform for long-running, stateful workflows"
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 21,
        "cited_text": "Tommy Falkowski @TommyFalkowski Just tried out @dify_ai for the first time and I'm blown away. This is one of the most polished LLM-centric application I have used so far! Also includes support for local models through @ollama and any OpenAI-like API. 9:05 PM · Jun 26, 2024 Chris @BamChrisI Wait, with @dify_ai you can build an no-code workflow to generate an AI podcast like notebooklm. Mindblowing. 7:29 AM · Oct 22, 2024 Raj Mehta @rajmehta If you are building AI applications it might be worth checking out the workflow feature by @dify_ai . It allows developers to build complex LLM flows using a simple drag-and-drop interface. And the whole thing is open source too. Link to repo: https://github.com/langgenius/dify"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 22,
        "cited_text": "2. Agents in Practice: Applications of LLM-based Agents 2.1 General Ability of Single Agent 2.1.1 Task-oriented Deployment In web scenarios [2023/10] OpenAgents: An Open Platform for Language Agents in the Wild. XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ demo ] [2023/07] WebArena: A Realistic Web Environment for Building Autonomous Agents. Shuyan Zhou (CMU) et al. arXiv. [ paper ] [ code ] [2023/07] A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis. Izzeddin Gur (DeepMind) et al. arXiv. [ paper ] [2023/06] SYNAPSE: Leveraging Few-Shot Exemplars for Human-Level Computer Control. Longtao Zheng (Nanyang Technological University) et al. arXiv. [ paper ] [ code ] [2023/06] Mind2Web: Towards a Generalist Agent for the Web. Xiang Deng (The Ohio State University) et al. arXiv. [ paper ] [ code ] [2023/05] Multimodal Web Navigation with Instruction-Finetuned Foundation Models. Hiroki Furuta (The University of Tokyo) et al. arXiv. [ paper ] [2023/03] Language Models can Solve Computer Tasks. Geunwoo Kim (University of California) et al. arXiv. [ paper ] [ code ] [2022/07] WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents. Shunyu Yao (Princeton University) et al. arXiv. [ paper ] [ code ] [2021/12] WebGPT: Browser-assisted question-answering with human feedback. Reiichiro Nakano (OpenAI) et al. arXiv. [ paper ] [2023/05] Agents: An Open-source Framework for Autonomous Language Agents. Wangchunshu Zhou (AIWaves) et al. arXiv. [ paper ] [ code ] [2024/04] OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments. XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ data viewer ]"
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 23,
        "cited_text": "Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT , GPT-Engineer and BabyAGI , serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver. Agent System Overview # In a LLM-powered autonomous agent system, LLM functions as the agent's brain, complemented by several key components: Planning Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks. Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results. Memory Short-term memory: I would consider all the in-context learning (See Prompt Engineering ) as utilizing short-term memory of the model to learn. Long-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, often by leveraging an external vector store and fast retrieval. Tool use The agent learns to call external APIs for extra information that is missing from the model weights (often hard to change after pre-training), including current information, code execution capability, access to proprietary information sources and more."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 24,
        "cited_text": "The generative agent architecture. (Image source: Park et al. 2023 ) This fun simulation results in emergent social behavior, such as information diffusion, relationship memory (e.g. two agents continuing the conversation topic) and coordination of social events (e.g. host a party and invite many others). Proof-of-Concept Examples # AutoGPT has drawn a lot of attention into the possibility of setting up autonomous agents with LLM as the main controller. It has quite a lot of reliability issues given the natural language interface, but nevertheless a cool proof-of-concept demo. A lot of code in AutoGPT is about format parsing."
      },
      {
        "source_id": "fbb19078-5a5c-4b0e-be0d-148af878ed49",
        "citation_number": 25,
        "cited_text": "arXiv:2210.03629 (cs) [Submitted on 6 Oct 2022 ( v1 ), last revised 10 Mar 2023 (this version, v3)] Title: ReAct: Synergizing Reasoning and Acting in Language Models Authors: Shunyu Yao , Jeffrey Zhao , Dian Yu , Nan Du , Izhak Shafran , Karthik Narasimhan , Yuan Cao View a PDF of the paper titled ReAct: Synergizing Reasoning and Acting in Language Models, by Shunyu Yao and 6 other authors View PDF Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: this https URL"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 26,
        "cited_text": "4. Other Topics 4.1 Benchmarks for LLM-based Agents [2023/11] \"MAgIC: Investigation of Large Language Model Powered Multi-Agent in Cognition, Adaptability, Rationality and Collaboration.\" Lin Xu et al. (NUS, ByteDance, Stanford & UC Berkeley) arXiv. [ paper ] [ Project Page ] [ Code ] The work presents a benchmarking framework for evaluating LLMs in multi-agent settings, showing a 50% average improvement using Probabilistic Graphical Modeling. [2023/10] \"Benchmarking Large Language Models As AI Research Agents.\" Qian Huang (Stanford) et al. arXiv. [ paper ] [ code ] [2023/08] \"AgentBench: Evaluating LLMs as Agents.\" Xiao Liu (THU) et al. arXiv. [ paper ] [ code ] [ project page ] AGENTBENCH, a benchmark for assessing LLMs as agents, shows a performance gap between top commercial and open-source models. [2023/10] \"SmartPlay : A Benchmark for LLMs as Intelligent Agents.\" Yue Wu (CMU & Microsoft) et al. arXiv. [ paper ] [ code ] SmartPlay is a benchmark and methodology for evaluating LLMs as intelligent agents, featuring six diverse games to assess key capabilities, providing a roadmap for identifying gaps in current methodologie [2024/04] \"OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments.\" XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ data viewer ] OSWorld🖥 is a unified, real computer environment for multimodal agents to benchmark open-ended computer tasks with arbitrary apps and interfaces on Ubuntu, Windows, & macOS."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 27,
        "cited_text": "Comparison of MIPS algorithms, measured in recall@10. (Image source: Google Blog, 2020 ) Check more MIPS algorithms and performance comparison in ann-benchmarks.com . Component Three: Tool Use # Tool use is a remarkable and distinguishing characteristic of human beings. We create, modify and utilize external objects to do things that go beyond our physical and cognitive limits. Equipping LLMs with external tools can significantly extend the model capabilities. A picture of a sea otter using rock to crack open a seashell, while floating in the water. While some other animals can use tools, the complexity is not comparable with humans. (Image source: Animals using tools )"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 28,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 29,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 30,
        "cited_text": "Strict mode Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode. Under the hood, strict mode works by leveraging our structured outputs feature and therefore introduces a couple requirements: additionalProperties must be set to false for each object in the parameters . All fields in properties must be marked as required . You can denote optional fields by adding null as a type option (see example below)."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 31,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 32,
        "cited_text": "These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice. We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 33,
        "cited_text": "While building our agent for SWE-bench , we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly. Get the developer newsletter Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 34,
        "cited_text": "pytest dataclasses Conversatin samples: Challenges # After going through key ideas and demos of building LLM-centered agents, I start to see a couple common limitations: Finite context length : The restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses. The design of the system has to work with this limited communication bandwidth, while mechanisms like self-reflection to learn from past mistakes would benefit a lot from long or infinite context windows. Although vector stores and retrieval can provide access to a larger knowledge pool, their representation power is not as powerful as full attention. Challenges in long-term planning and task decomposition : Planning over a lengthy history and effectively exploring the solution space remain challenging. LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error. Reliability of natural language interface : Current agent system relies on natural language as an interface between LLMs and external components such as memory and tools. However, the reliability of model outputs is questionable, as LLMs may make formatting errors and occasionally exhibit rebellious behavior (e.g. refuse to follow an instruction). Consequently, much of the agent demo code focuses on parsing model output."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「基础综合实战：构建一个多模式研究助手」这一领域，2025-2026年的研究重点已从简单的“提示词工程”转向**生产级智能体架构**、**标准化协议**以及**基于强化学习的自主进化**。\n\n以下是基于最新来源的核心技术趋势与突破解析：\n\n### 1. 2025-2026年重要趋势与技术演进\n*   **从“工具调用”转向“工具搜索（Tool Search）”**：最新的模型（如 **GPT-5.4**）开始支持 `tool_search` 功能 [1, 2]。这解决了助手拥有数万个 API 时上下文窗口过载的问题，模型可以根据需求动态搜索并加载相关工具，而非在初始阶段加载所有模式 [2, 3]。\n*   **标准化 ACI 与 MCP 协议**：**模型上下文协议（MCP）** 已成为 2025-2026 年的标准（如 2025-03-26 协议版本），它消除了不同数据库和 API 之间的集成复杂性，使研究助手能够无缝连接全球 LLM 和 RAG 管道 [4, 5]。\n*   **长程决策的强化学习（AgentGym-RL）**：2025 年 9 月发布的 **AgentGym-RL** 框架标志着重大突破，通过**多轮强化学习**训练智能体处理长路径（Long-Horizon）决策，使其能在交互环境中直接学习而非仅仅依赖静态指令 [6]。\n*   **架构模式的精简化**：领先的研发团队（如 Anthropic）发现，最成功的实现并非依赖复杂框架，而是使用**简单、可组合的模式**，如：\n    *   **编排器-工人模式（Orchestrator-Workers）**：用于分解无法预测的复杂研究任务 [7, 8]。\n    *   **评估器-优化器模式（Evaluator-Optimizer）**：通过闭环反馈迭代提升研究报告的质量 [8]。\n\n### 2. 未解决的关键挑战\n尽管技术飞速发展，多模式助手仍面临以下核心局限：\n*   **有限的上下文窗口带宽**：尽管有向量检索，但其表达能力仍不如完全注意力（Full Attention）[9]。在处理涉及大量历史信息、详细指令和复杂 API 上下文的研究任务时，系统设计必须在通信带宽内进行艰难权衡 [9]。\n*   **长程规划的鲁棒性不足**：LLM 在面对意外错误时调整计划的能力依然薄弱，相比人类通过“试错”学习的弹性，模型在复杂任务分解中容易因一步错误导致整体崩溃 [9]。\n*   **自然语言接口的不可靠性**：当前系统仍重度依赖解析逻辑来处理模型输出的格式错误或指令拒绝行为（Rebellious Behavior） [9]。\n\n### 3. 未来可能的突破点\n*   **端到端多模态决策（End-to-End MLLM）**：如 **HOLMES** 框架和 **JARVIS-1**，未来的研究点在于让模型直接通过视觉感知（如 GPT-4-Vision 或更高版本）进行决策，而非将视觉信息转化为文字后再处理 [10-12]。\n*   **自主进化的智能体社会**：研究已开始探索 **LLM 智能体社会中的社会规范演化**（2024-2025 年研究），未来助手可能通过多智能体协作（Multi-Agent Debate）自主产生更优的研究范式 [13, 14]。\n*   **从 HCI 转向 ACI（代理-计算机接口）**：未来的突破将集中在优化**智能体专用接口**上，通过严格的文档编写、示例注入和“防错（Poka-yoke）”设计，使工具更易于被 AI 逻辑理解而非仅仅适配人类操作 [15-17]。\n*   **深度研究（Deep Research）模型**：专门针对长程研究任务优化的模型（如 OpenAI 的 **Deep Research** 系列）将整合联网搜索、代码解释器和 MCP 服务，实现高度自动化的科学探索 [18, 19]。",
    "conversation_id": "54ddd743-e565-4f91-b37e-54224c545793",
    "sources_used": [
      "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "cee20c76-4ec0-4596-a7db-5532200f330f",
      "5cc6ca32-64da-4942-8f57-268afe35e163"
    ],
    "citations": {
      "1": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "2": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "3": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "4": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
      "5": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "6": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "7": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "8": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "9": "5cc6ca32-64da-4942-8f57-268afe35e163",
      "10": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "11": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "12": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "13": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "14": "cee20c76-4ec0-4596-a7db-5532200f330f",
      "15": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "16": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "17": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
      "18": "b1502d82-776c-44c7-8886-a172bf69e0f5",
      "19": "b1502d82-776c-44c7-8886-a172bf69e0f5"
    },
    "references": [
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 1,
        "cited_text": "If your application has many functions or large schemas, you can pair function calling with tool search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and later models support tool_search . How it works Let's begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we'll show you how it's done with some practical examples. Tools - functionality we give the model A function or tool refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt's instructions."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 2,
        "cited_text": "Defining namespaces Use namespaces to group related tools by domain, such as crm , billing , or shipping . Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system. Tool search If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with tool_search . The tool_search tool lets the model search for relevant tools, add them to the model context, and then use them. Only gpt-5.4 and later models support it. Read the tool search guide to learn more."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 3,
        "cited_text": "(Optional) Function calling wth pydantic and zod While we encourage you to define your function schemas directly, our SDKs have helpers to convert pydantic and zod objects into schemas. Not all pydantic and zod features are supported. Define objects to represent function schema python Best practices for defining functions Write clear and detailed function names, parameter descriptions, and instructions. Explicitly describe the purpose of the function and each parameter (and its format), and what the output represents. Use the system prompt to describe when (and when not) to use each function. Generally, tell the model exactly what to do. Include examples and edge cases , especially to rectify any recurring failures. ( Note: Adding examples may hurt performance for reasoning models .) For deferred tools, put detailed guidance in the function description and keep the namespace description concise. The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly. Apply software engineering best practices. Make the functions obvious and intuitive . ( principle of least surprise ) Use enums and object structure to make invalid states unrepresentable. (e.g. toggle_light(on: bool, off: bool) allows for invalid calls) Pass the intern test. Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.) Offload the burden from the model and use code where possible. Don't make the model fill arguments you already know. For example, if you already have an order_id based on a previous menu, don't have an order_id param – instead, have no params submit_refund() and pass the order_id with code. Combine functions that are always called in sequence. For example, if you always call mark_location() after query_location() , just move the marking logic into the query function call. Keep the number of initially available functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions available at the start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer large or infrequently used parts of your tool surface instead of exposing everything up front. Leverage OpenAI resources. Generate and iterate on function schemas in the Playground . Consider fine-tuning to increase function calling accuracy for large numbers of functions or difficult tasks. ( cookbook )"
      },
      {
        "source_id": "16dd388d-10a3-4174-a924-f4aeb7a3e800",
        "citation_number": 4,
        "cited_text": "[ Connect ](https://dify.ai/#connect) Supercharge AI applications with global LLMs, RAG pipelines, tools, agent strategies, and more. Add Wings with Tools Expand capabilities of your AI application with powerful plugins. Bridge Your Systems / Platforms with Native MCP Integration Access external APIs, databases, and services through standardized MCP protocols, eliminating integration complexity and maintenance overhead. Support HTTP-based MCP services (protocol 2025-03-26) with pre-authorized and auth-free modes."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 5,
        "cited_text": "The augmented LLM We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol , which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation . For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 6,
        "cited_text": "Repository files navigation README The Rise and Potential of Large Language Model Based Agents: A Survey 🔥 Must-read papers for LLM-based agents. 🏃 Coming soon: Add one-sentence intro to each paper. 🔔 News 🎉 [2025-09-10] Note！You can develop your custom environment to AgentGym and perform RL on it! The tutorial is here . 🍺 [2025-09-10] New paper is released on arXiv: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning . 🚀 [2025-09-10] AgentGym-RL Framework released! We introduce the reinforcement learning (RL) version of AgentGym, enabling agents to learn directly from interactive environments: AgentGym-RL . 👀 [2025/09/03] AgentGym now provides an interactive frontend for visualization. Researchers can replay and inspect full trajectories, step through agent decision-making, and analyze model behaviors more easily. ☄ [2024/06/07] AgentGym has been released for developing and evolving LLM-based agents across diverse environments! Paper: AgentGym . Project page: https://agentgym.github.io/ . Codes: Platform and Implementations . Huggingface resources: AgentTraj-L , AgentEval , AgentEvol-7B . 🎉 [2024/05/02] R3 ( Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning ) was accepted by ICML 2024! 💫 [2024/02/08] New paper R3 on RL for LLM agent reasoning has been released! Paper: Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning . Codes: LLM-Reverse-Curriculum-RL . 🥳 [2023/09/20] This project has been listed on GitHub Trendings ! It is a great honor! 💥 [2023/09/15] Our survey is released! See The Rise and Potential of Large Language Model Based Agents: A Survey for the paper! ✨ [2023/09/14] We create this repository to maintain a paper list on LLM-based agents. More papers are coming soon!"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 7,
        "cited_text": "Workflow: Orchestrator-workers In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. The orchestrator-workers workflow When to use this workflow: This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 8,
        "cited_text": "Example where orchestrator-workers is useful: Coding products that make complex changes to multiple files each time. Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information. Workflow: Evaluator-optimizer In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. The evaluator-optimizer workflow When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document."
      },
      {
        "source_id": "5cc6ca32-64da-4942-8f57-268afe35e163",
        "citation_number": 9,
        "cited_text": "pytest dataclasses Conversatin samples: Challenges # After going through key ideas and demos of building LLM-centered agents, I start to see a couple common limitations: Finite context length : The restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses. The design of the system has to work with this limited communication bandwidth, while mechanisms like self-reflection to learn from past mistakes would benefit a lot from long or infinite context windows. Although vector stores and retrieval can provide access to a larger knowledge pool, their representation power is not as powerful as full attention. Challenges in long-term planning and task decomposition : Planning over a lengthy history and effectively exploring the solution space remain challenging. LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error. Reliability of natural language interface : Current agent system relies on natural language as an interface between LLMs and external components such as memory and tools. However, the reliability of model outputs is questionable, as LLMs may make formatting errors and occasionally exhibit rebellious behavior (e.g. refuse to follow an instruction). Consequently, much of the agent demo code focuses on parsing model output."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 10,
        "cited_text": "1. The Birth of An Agent: Construction of LLM-based Agents 1.1 Brain: Primarily Composed of An LLM 1.1.1 Natural Language Interaction High-quality generation [2023/10] Towards End-to-End Embodied Decision Making via Multi-modal Large Language Model: Explorations with GPT4-Vision and Beyond Liang Chen et al. arXiv. [ paper ] [ code ] This work proposes PCA-EVAL, which benchmarks embodied decision making via MLLM-based End-to-End method and LLM-based Tool-Using methods from Perception, Cognition and Action Levels. [2023/08] A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity. Yejin Bang et al. arXiv. [ paper ] This work evaluates the multitask, multilingual and multimodal aspects of ChatGPT using 21 data sets covering 8 different common NLP application tasks. [2023/06] LLM-Eval: Unified Multi-Dimensional Automatic Evaluation for Open-Domain Conversations with Large Language Models. Yen-Ting Lin et al. arXiv. [ paper ] The LLM-EVAL method evaluates multiple dimensions of evaluation, such as content, grammar, relevance, and appropriateness. [2023/04] Is ChatGPT a Highly Fluent Grammatical Error Correction System? A Comprehensive Evaluation. Tao Fang et al. arXiv. [ paper ] The results of evaluation demonstrate that ChatGPT has excellent error detection capabilities and can freely correct errors to make the corrected sentences very fluent. Additionally, its performance in non-English and low-resource settings highlights its potential in multilingual GEC tasks."
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 11,
        "cited_text": "Planning Plan formulation [2023/11] JARVIS-1: Open-world Multi-task Agents with Memory-Augmented Multimodal Language Models. ZiHao Wang (Peking University) et al. arXiv. [ paper ] [ code ] [2023/10] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models. Andy Zhou (University of Illinois Urbana-Champaign) et al. arXiv. [ paper ] [ project page ] [ code ] [2023/05] Tree of Thoughts: Deliberate Problem Solving with Large Language Models. Shunyu Yao (Princeton University) et al. arXiv. [ paper ] [ code ] [2023/05] Plan, Eliminate, and Track -- Language Models are Good Teachers for Embodied Agents. Yue Wu (Carnegie Mellon University) et al. arXiv. [ paper ] [2023/05] Reasoning with Language Model is Planning with World Model. Shibo Hao (UC San Diego) et al. arXiv. [ paper ] [ code ] [2023/05] SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks. Bill Yuchen Lin (Allen Institute for Artificial Intelligence) et al. arXiv. [ paper ] [ code ] [2023/04] LLM+P: Empowering Large Language Models with Optimal Planning Proficiency. Bo Liu (University of Texas at Austin) et al. arXiv. [ paper ] [ code ] [2023/03] HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. Yongliang Shen (Microsoft Research Asia) et al. arXiv. [ paper ] [ code ] [2023/02] Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents. ZiHao Wang (Peking University) et al. arXiv. [ paper ] [ code ] [2022/05] Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. Denny Zhou (Google Research) et al. arXiv. [ paper ] [2022/05] MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning. Ehud Karpas (AI21 Labs) et al. arXiv. [ paper ] [2022/04] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances. Michael Ahn (Robotics at Google) et al. arXiv. [ paper ] [2023/05] Agents: An Open-source Framework for Autonomous Language Agents. Wangchunshu Zhou (AIWaves) et al. arXiv. [ paper ] [ code ] [2022/12] Don't Generate, Discriminate: A Proposal for Grounding Language Models to Real-World Environments. Yu Gu (The Ohio State University) et al. ACL. [ paper ] [ code ]"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 12,
        "cited_text": "1.3 Action: Expand Action Space of LLM-based Agents 1.3.1 Tool Using [2024/02] Towards Uncertainty-Aware Language Agent. Jiuzhou Han (Monash University) et al. arXiv. [ paper ] [ project page ] [ code ] [2023/10] OpenAgents: An Open Platform for Language Agents in the Wild. XLang Lab (The University of Hong Kong) arXiv. [ paper ] [ project page ] [ code ] [ demo ] [2023/10] Lemur: Harmonizing Natural Language and Code for Language Agents Yiheng Xu (University of Hong Kong) et al. arXiv. [ paper ] [ code ] [2023/10] Towards End-to-End Embodied Decision Making via Multi-modal Large Language Model: Explorations with GPT4-Vision and Beyond Liang Chen (Peking University) et al. arXiv. [ paper ] [ code ] HOLMES is a multi-agent cooperation framework that allows LLMs to leverage MLLMs and APIs to gather multimodal information for informed decision-making. [2023/07] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] [ dataset ] ToolLLM is a general tool-use framework encompassing data construction, model training and evaluation. [2023/05] Large Language Models as Tool Makers. Tianle Cai (Princeton University) et al. arXiv. [ paper ] [ code ] LATM is a closed-loop framework that takes an initial step towards removing the dependency on the availability of existing tools. [2023/05] CREATOR: Disentangling Abstract and Concrete Reasonings of Large Language Models through Tool Creation. Cheng Qian (Tsinghua University) et al. arXiv. [ paper ] CREATOR is a novel framework that empowers LLMs to create their own tools through documentation and code realization. [2023/04] Tool Learning with Foundation Models. Yujia Qin (Tsinghua University) et al. arXiv. [ paper ] [ code ] This survey primarily introduces a new paradigm called \"tool learning based on foundational models\", which combines the advantages of specialized tools and foundational models, achieving higher precision, efficiency, and automation in problem-solving. [2023/04] ChemCrow: Augmenting large-language models with chemistry tools. Andres M Bran (Laboratory of Artificial Chemical Intelligence, ISIC, EPFL) et al. arXiv. [ paper ] [ code ] ChemCrow is an LLM chemistry agent that integrates 13 expert-designed tools and augments the LLM performance in chemistry and emerge new capabilities. [2023/04] GeneGPT: Augmenting Large Language Models with Domain Tools for Improved Access to Biomedical Information. Qiao Jin (National Institutes of Health), Yifan Yang, Qingyu Chen, Zhiyong Lu. arXiv. [ paper ] [ code ] GeneGPT is a model that answer genomics questions. It introduces a novel method for handling challenges with hallucinations by teaching LLMs to use the Web APIs. [2023/04] OpenAGI: When LLM Meets Domain Experts. Yingqiang Ge (Rutgers University) et al. arXiv. [ paper ] [ code ] OpenAGI is an open-source AGI research platform. It introduces a paradigm of LLMs operating various expert models for complex task-solving and proposes an RLTF mechanism to improve the LLM's task-solving ability. [2023/03] HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. Yongliang Shen (Zhejiang University) et al. arXiv. [ paper ] [ code ] HuggingGPT is a system that leverages LLMs to connect various and multimodal AI models in machine learning communities to solve AI tasks. [2023/03] Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models. Chenfei Wu (Microsoft Research Asia) et al. arXiv. [ paper ] [ code ] Visual ChatGPT is a system that opens the door to investigating the visual roles of ChatGPT with the help of Visual Foundation Models. [2023/02] Augmented Language Models: a Survey. Grégoire Mialon (Meta AI) et al. TMLR. [ paper ] This survey reviews works in which LMs are augmented with the ability to use tools. Augmented LMs can use external modules to expand their context processing ability. [2023/02] Toolformer: Language Models Can Teach Themselves to Use Tools. Timo Schick (Meta AI) et al. arXiv. [ paper ]"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 13,
        "cited_text": "2.2.2 Adversarial Interaction for Advancement [2023/08] ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate. Chi-Min Chan (Tsinghua University) et al. arXiv. [ paper ] [ code ] [2023/05] Improving Factuality and Reasoning in Language Models through Multiagent Debate. Yilun Du (MIT CSAIL) et al. arXiv. [ paper ] [ code ] [2023/05] Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback. Yao Fu (University of Edinburgh) et al. arXiv. [ paper ] [ code ] [2023/05] Examining the Inter-Consistency of Large Language Models: An In-depth Analysis via Debate. Kai Xiong (Harbin Institute of Technology) et al. arXiv. [ paper ] [2023/05] Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. Tian Liang (Tsinghua University) et al. arXiv. [ paper ] [ code ]"
      },
      {
        "source_id": "cee20c76-4ec0-4596-a7db-5532200f330f",
        "citation_number": 14,
        "cited_text": "3.3 Society Simulation with LLM-based Agents [2024/03] Emergence of Social Norms in Large Language Model-based Agent Societies. Siyue Ren et al. arXiv. [ paper ] [ code ] [2023/08] AgentSims: An Open-Source Sandbox for Large Language Model Evaluation. Jiaju Lin (PTA Studio) et al. arXiv. [ paper ] [ project page ] [ code ] [2023/07] S 3: Social-network Simulation System with Large Language Model-Empowered Agents. Chen Gao (Tsinghua University) et al. arXiv. [ paper ] [2023/07] Epidemic Modeling with Generative Agents. Ross Williams (Virginia Tech) et al. arXiv. [ paper ] [ code ] [2023/06] RecAgent: A Novel Simulation Paradigm for Recommender Systems. Lei Wang (Renmin University of China) et al. arXiv. [ paper ] [2023/05] Training Socially Aligned Language Models in Simulated Human Society. Ruibo Liu (Dartmouth College) et al. arXiv. [ paper ] [ code ] [2023/04] Generative Agents: Interactive Simulacra of Human Behavior. Joon Sung Park (Stanford University) et al. arXiv. [ paper ] [ code ] [2022/08] Social Simulacra: Creating Populated Prototypes for Social Computing Systems. Joon Sung Park (Stanford University) et al. UIST. [ paper ]"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 15,
        "cited_text": "When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent's planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing . Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users."
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 16,
        "cited_text": "Our suggestions for deciding on tool formats are the following: Give the model enough tokens to \"think\" before it writes itself into a corner. Keep the format close to what the model has seen naturally occurring in text on the internet. Make sure there's no formatting \"overhead\" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes. One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent -computer interfaces (ACI). Here are some thoughts on how to do so:"
      },
      {
        "source_id": "e53d3ec2-9aeb-4e11-b865-9e91b57dab7b",
        "citation_number": 17,
        "cited_text": "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools. How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools. Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate. Poka-yoke your tools. Change the arguments so that it is harder to make mistakes."
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 18,
        "cited_text": "Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance"
      },
      {
        "source_id": "b1502d82-776c-44c7-8886-a172bf69e0f5",
        "citation_number": 19,
        "cited_text": "Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Responses How it works Function tool example Defining functions Defining namespaces Tool search Handling function calls Additional configurations Streaming Custom tools Copy Page More page actions"
      }
    ]
  }
}
