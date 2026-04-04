# 知识库：神经网络 TTS 深度对比：VITS、Bark、XTTS

生成时间: 2026-04-02 21:21
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "基于提供的源代码，以下是对 **VITS**、**Bark** 和 **XTTS** 三种神经网络 TTS 技术的深度对比分析，涵盖了从核心架构到关键指标的技术概览。\n\n### 1. VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech)\n\nVITS 是一种具有代表性的**单阶段端到端**模型，其主要贡献在于打破了传统 TTS 系统需要分步生成（如先生成梅尔频谱，再通过声码器转换）的局限 [1, 2]。\n\n*   **技术演进路线：** 从传统的两阶段（Two-stage）TTS 系统演进为**单阶段（Single-stage）并行采样**系统，旨在解决两阶段系统训练不连贯和采样质量不及预期的问题 [1, 2]。\n*   **核心算法名称：** 采用**变分推理（Variational Inference）**，并辅以**标准化流（Normalizing Flows）**和**对抗性训练（Adversarial Training）**过程 [1, 2]。\n*   **主要架构模式：** \n    *   **条件变分自编码器（Conditional VAE）：** 作为核心骨架 [1, 2]。\n    *   **随机时长预测器（Stochastic Duration Predictor）：** 用于模拟输入文本在不同语境下表现出的多样节奏和音高（一对多关系）[1, 2]。\n    *   **单阶段架构：** 允许在一个模型中直接实现文本到波形的转换 [1]。\n*   **关键技术指标：** \n    *   **平均意见得分（MOS）：** 在单人数据集（LJ Speech）上，其表现优于当时市面上最佳的 TTS 系统，并达到了可与原始音频（Ground Truth）媲美的水准 [1, 2]。\n    *   **采样方式：** 支持高效的并行采样 [1]。\n\n### 2. Bark\n\nBark 是由 Suno 开发的一款基于 **Transformer** 的全生成式文本转语音（及音频）模型，其设计理念更接近于现代的大语言模型 [3, 4]。\n\n*   **技术演进路线：** 受到 **AudioLM** 和 **Vall-E** 等生成式音频模型的启发，舍弃了中间环节的音素（Phonemes），直接将输入文本转换为音频 [4, 5]。\n*   **核心算法名称：** **GPT 风格的 Transformer 模型（GPT-style architecture）** [4]。\n*   **主要架构模式：** 采用分层级联的三个 Transformer 模型完成从文本到音频的量化表示转换 [6, 7]：\n    1.  **文本到语义令牌（Text to semantic tokens）：** 使用 BERT 分词器处理输入 [6]。\n    2.  **语义到粗略令牌（Semantic to coarse tokens）：** 转换出 EnCodec 的前两层码本（Codebooks）[6]。\n    3.  **粗略到精细令牌（Coarse to fine tokens）：** 最终生成 EnCodec 的 8 层码本以还原音频 [7]。\n*   **关键技术指标：** \n    *   **多功能性：** 不仅支持语音，还能生成音乐、环境噪音及**非语言交流（如笑声 [laughs]、叹气 [sighs]）** [3, 8]。\n    *   **语种支持：** 开箱即用支持 13+ 种语言 [8]。\n    *   **局限性：** 默认输出长度优化为 **13-14 秒**左右 [9]；全量版约需 **12GB 显存** [9]。\n\n### 3. XTTS (v2)\n\nXTTS 是由 Coqui 开发的针对快速克隆和多语言场景优化的语音生成模型，旨在实现极低门槛的零样本或少量样本语音克隆 [10]。\n\n*   **技术演进路线：** 从 XTTS-v1 演进而来，v2 版本改进了说话人条件调节（Speaker Conditioning）的架构，增加了稳定性并提升了韵律表现 [11]。\n*   **核心算法名称：** 基于参考音频提取特征进行**说话人条件调节（Speaker Conditioning）**，支持说话人插值（Interpolation）[10, 11]。\n*   **主要架构模式：**\n    *   **零样本克隆（Zero-shot cloning）：** 仅需短音频即可捕捉音色 [10]。\n    *   **跨语言克隆（Cross-language cloning）：** 使用一种语言的参考音频生成另一种语言的语音 [10, 11]。\n*   **关键技术指标：** \n    *   **克隆效率：** 仅需 **6 秒**参考音频即可完成声音克隆 [10, 11]。\n    *   **多语言能力：** 支持 **17 种语言**（包括中文、日文、韩文、印地语等）[11]。\n    *   **采样率：** 采样率为 **24kHz** [11]。\n\n### 技术对比总结\n\n| 特性指标 | VITS | Bark | XTTS (v2) |\n| :--- | :--- | :--- | :--- |\n| **技术核心** | CVAE + 标准化流 + 对抗学习 [1, 2] | GPT 风格 Transformer [4] | 说话人条件调节模型 [10, 11] |\n| **主要模式** | 端到端并行采样 [1] | 文本到语义令牌的分层生成 [6] | 快速语音克隆与跨语言迁移 [10, 11] |\n| **演进背景** | 追求更高 MOS 分的单阶段系统 [1] | 追求包含非言语信息的全生成音频 [3] | 追求多语言普适性与快速克隆 [11] |\n| **特色功能** | 随机时长预测、韵律多样化 [1, 2] | 能唱歌、发笑、生成环境音 [3, 8] | 6秒克隆、17种语种支持 [10, 11] |\n| **采样率** | 未明示（通常取决于配置） | 24kHz [12] | 24kHz [11] |",
    "conversation_id": "86674cd6-e082-45ea-acd4-9e41134ebd11",
    "sources_used": [
      "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "01cd196f-8e66-427c-a23c-273246e938e0",
      "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "64bbccb9-1477-4b71-973e-92976cf467e4",
      "bab69d19-3140-457c-a75a-12b45648b450"
    ],
    "citations": {
      "1": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "2": "01cd196f-8e66-427c-a23c-273246e938e0",
      "3": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "4": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "5": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "6": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "7": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "8": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "9": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "10": "bab69d19-3140-457c-a75a-12b45648b450",
      "11": "bab69d19-3140-457c-a75a-12b45648b450",
      "12": "64bbccb9-1477-4b71-973e-92976cf467e4"
    },
    "references": [
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 1,
        "cited_text": "VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech Jaehyeon Kim, Jungil Kong, and Juhee Son In our recent paper , we propose VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech. Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text. With the uncertainty modeling over latent variables and the stochastic duration predictor, our method expresses the natural one-to-many relationship in which a text input can be spoken in multiple ways with different pitches and rhythms. A subjective human evaluation (mean opinion score, or MOS) on the LJ Speech, a single speaker dataset, shows that our method outperforms the best publicly available TTS systems and achieves a MOS comparable to ground truth."
      },
      {
        "source_id": "01cd196f-8e66-427c-a23c-273246e938e0",
        "citation_number": 2,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2106.06103 Help | Advanced Search Computer Science > Sound arXiv:2106.06103 (cs)   [Submitted on 11 Jun 2021] Title: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech Authors: Jaehyeon Kim , Jungil Kong , Juhee Son View a PDF of the paper titled Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech, by Jaehyeon Kim and 2 other authors View PDF Abstract: Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text. With the uncertainty modeling over latent variables and the stochastic duration predictor, our method expresses the natural one-to-many relationship in which a text input can be spoken in multiple ways with different pitches and rhythms. A subjective human evaluation (mean opinion score, or MOS) on the LJ Speech, a single speaker dataset, shows that our method outperforms the best publicly available TTS systems and achieves a MOS comparable to ground truth.  Comments:   ICML 2021   Subjects:   Sound (cs.SD) ; Audio and Speech Processing (eess.AS)   Cite as: arXiv:2106.06103 [cs.SD]   (or arXiv:2106.06103v1 [cs.SD]  for this version) https://doi.org/10.48550/arXiv.2106.06103 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 3,
        "cited_text": "Notice: Bark is Suno's open-source text-to-speech+ model. If you are looking for our text-to-music models, please visit us on our web page and join our community on Discord . 🐶 Bark 🔗 Examples • Suno Studio Waitlist • Updates • How to Use • Installation • FAQ Bark is a transformer-based text-to-audio model created by Suno . Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. The model can also produce nonverbal communications like laughing, sighing and crying. To support the research community, we are providing access to pretrained model checkpoints, which are ready for inference and available for commercial use."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 4,
        "cited_text": "If you don't have hardware available or if you want to play with bigger versions of our models, you can also sign up for early access to our model playground here . ⚙️ Details Bark is fully generative text-to-audio model devolved for research and demo purposes. It follows a GPT style architecture similar to AudioLM and Vall-E and a quantized Audio representation from EnCodec . It is not a conventional TTS model, but instead a fully generative text-to-audio model capable of deviating in unexpected ways from any given script. Different to previous approaches, the input text prompt is converted directly to audio without the intermediate use of phonemes. It can therefore generalize to arbitrary instructions beyond speech such as music lyrics, sound effects or other non-speech sounds."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 5,
        "cited_text": "Requests for future language support here or in the #forums channel on Discord . 🙏 Appreciation nanoGPT for a dead-simple and blazing fast implementation of GPT-style models EnCodec for a state-of-the-art implementation of a fantastic audio codec AudioLM for related training and inference code Vall-E , AudioLM and many other ground-breaking papers that enabled the development of Bark © License Bark is licensed under the MIT License. 📱 Community Twitter Discord 🎧 Suno Studio (Early Access) We’re developing a playground for our models, including Bark."
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 6,
        "cited_text": "pizza.webm To save  audio_array  as a WAV file: from  scipy.io.wavfile  import  write  as  write_wav write_wav( \"/path/to/audio.wav\" , SAMPLE_RATE, audio_array) Model Details The following is additional information about the models released here. Bark is a series of three transformer models that turn text into audio. Text to semantic tokens Input: text, tokenized with BERT tokenizer from Hugging Face Output: semantic tokens that encode the audio to be generated Semantic to coarse tokens Input: semantic tokens Output: tokens from the first two codebooks of the EnCodec Codec from facebook"
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 7,
        "cited_text": "Coarse to fine tokens Input: the first two codebooks from EnCodec Output: 8 codebooks from EnCodec Architecture Model   Parameters   Attention   Output Vocab size   Text to semantic tokens   80/300 M   Causal   10,000   Semantic to coarse tokens   80/300 M   Causal   2x 1,024   Coarse to fine tokens   80/300 M   Non-causal   6x 1,024 Release date April 2023 Broader Implications We anticipate that this model's text to audio capabilities can be used to improve accessbility tools in a variety of languages."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 8,
        "cited_text": "Below is a list of some known non-speech sounds, but we are finding more every day. Please let us know if you find patterns that work particularly well on Discord ! [laughter] [laughs] [sighs] [music] [gasps] [clears throat] —  or  ...  for hesitations ♪  for song lyrics CAPITALIZATION for emphasis of a word [MAN]  and  [WOMAN]  to bias Bark toward male and female speakers, respectively Supported Languages Language   Status   English (en)   ✅   German (de)   ✅   Spanish (es)   ✅   French (fr)   ✅   Hindi (hi)   ✅   Italian (it)   ✅   Japanese (ja)   ✅   Korean (ko)   ✅   Polish (pl)   ✅   Portuguese (pt)   ✅   Russian (ru)   ✅   Turkish (tr)   ✅   Chinese, simplified (zh)   ✅"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 9,
        "cited_text": "Why is the output limited to ~13-14 seconds? Bark is a GPT-style model, and its architecture/context window is optimized to output generations with roughly this length. How much VRAM do I need? The full version of Bark requires around 12Gb of memory to hold everything on GPU at the same time. However, even smaller cards down to ~2Gb work with some additional settings. Simply add the following code snippet before your generation: import   os   os . environ [ \"SUNO_OFFLOAD_CPU\" ]  =   \"True\"   os . environ [ \"SUNO_USE_SMALL_MODELS\" ]  =   \"True\""
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 10,
        "cited_text": "Hugging Face Log In Sign Up coqui / XTTS-v2 Coqui.ai Text-to-Speech coqui Model card Files   Files and versions   xet Community   143 Configuration Parsing Warning: Invalid JSON for config file config.json ⓍTTS ⓍTTS is a Voice generation model that lets you clone voices into different languages by using just a quick 6-second audio clip. There is no need for an excessive amount of training data that spans countless hours. This is the same or similar model to what powers Coqui Studio and Coqui API ."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 11,
        "cited_text": "Features Supports 17 languages. Voice cloning with just a 6-second audio clip. Emotion and style transfer by cloning. Cross-language voice cloning. Multi-lingual speech generation. 24khz sampling rate. Updates over XTTS-v1 2 new languages; Hungarian and Korean Architectural improvements for speaker conditioning. Enables the use of multiple speaker references and interpolation between speakers. Stability improvements. Better prosody and audio quality across the board. Languages XTTS-v2 supports 17 languages: English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi) ."
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 12,
        "cited_text": "Run inference via the Transformers modelling code. You can use the processor + generate code to convert text into a mono 24 kHz speech waveform for more fine-grained control. from  transformers  import  AutoProcessor, AutoModel processor = AutoProcessor.from_pretrained( \"suno/bark\" ) model = AutoModel.from_pretrained( \"suno/bark\" ) inputs = processor( text=[ \"Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe.\" ], return_tensors= \"pt\" , ) speech_values = model.generate(**inputs, do_sample= True )"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "以下是对 VITS、Bark 和 XTTS（以 v2 为主）三种神经网络 TTS 技术的深度解析，涵盖实现细节、核心算法及性能对比。\n\n### 1. VITS (Variational Inference with adversarial learning for End-to-End TTS)\n\nVITS 标志着 TTS 从“两阶段生成”向**“单阶段端到端”**的跨越。\n\n*   **核心算法流程：** \n    *   采用**条件变分自编码器 (Conditional VAE)** 架构 [1, 2]。\n    *   通过**标准化流 (Normalizing Flows)** 增强生成建模的表现力 [1, 2]。\n    *   引入**随机时长预测器 (Stochastic Duration Predictor)**，用于模拟输入文本在音高和节奏上的“一对多”自然变化 [1, 2]。\n    *   利用**单调对齐搜索 (Monotonic Alignment Search)** 解决文本与音频的自动对齐问题 [3, 4]。\n*   **关键代码架构：** \n    *   包含 `models.py` (核心模型定义)、`attentions.py` (注意力机制) 及由 Cython 编写的 `monotonic_align` (高效对齐模块) [4-6]。\n*   **性能优化策略：** \n    *   支持**并行采样**，生成速度极快 [1]。\n    *   **快速微调：** 优化的管线（如 VITS-fast-fine-tuning）可在 **20 分钟至 2 小时**内完成新角色声音的适配 [7]。\n*   **技术指标：** \n    *   在单人数据集（LJ Speech）上的 **MOS（平均意见得分）** 可与原始音频媲美 [1, 2]。\n\n### 2. Bark (Text-Prompted Generative Audio Model)\n\nBark 是由 Suno 开发的**全生成式 Transformer 模型**，其逻辑更接近大语言模型而非传统 TTS。\n\n*   **核心算法流程（三阶段级联）：** \n    1.  **文本到语义令牌 (Text to Semantic)：** 使用 **BERT 分词器**处理文本，生成编码音频信息的语义令牌 [8]。\n    2.  **语义到粗略令牌 (Semantic to Coarse)：** 将语义信息转换为 **EnCodec** 编解码器的前两层码本 [8]。\n    3.  **粗略到精细令牌 (Coarse to Fine)：** 最终生成全部 8 层码本以还原高质量波形 [9]。\n*   **关键代码架构：** \n    *   基于 **GPT 风格架构**，融合了 nanoGPT 的实现方式及 EnCodec 音频压缩技术 [10, 11]。\n*   **性能优化策略：** \n    *   **VRAM 控制：** 完整版需约 **12GB 显存**；通过设置 `SUNO_USE_SMALL_MODELS` 可在 **8GB 显存**下运行 [12, 13]。\n    *   **多功能性：** 原生支持**非言语交流**（如 `[laughs]`、`[sighs]`）和**音乐生成**（使用 `♪` 符号） [14, 15]。\n*   **技术指标：** \n    *   **采样率：** 24kHz [16]。\n    *   **长度限制：** 针对 **13-14 秒** 的音频生成进行了优化 [13, 17]。\n\n### 3. XTTS (v2)\n\nXTTS-v2 是 Coqui 推出的专为**快速声音克隆**设计的跨语言模型。\n\n*   **核心算法流程：** \n    *   基于改进的**说话人条件调节 (Speaker Conditioning)** 架构 [18]。\n    *   支持**零样本 (Zero-shot)** 克隆，即直接通过参考音频提取特征进行语音合成 [19, 20]。\n*   **关键代码架构：** \n    *   通过 `XttsConfig` 和 `Xtts` 类进行初始化，支持说话人插值（Interpolation）以混合不同音色 [18, 21]。\n*   **性能优化策略：** \n    *   **极简数据：** 仅需 **6 秒** 的参考音频即可完成高质量克隆，无需长达数小时的训练 [18, 19]。\n    *   **跨语言迁移：** 允许用一种语言的样本生成另一种语言的语音 [19]。\n*   **技术指标：** \n    *   **采样率：** 24kHz [18]。\n    *   **语言支持：** 开箱即用支持 **17 种语言**（含中文、日文、韩文等） [18]。\n\n### 技术参数与竞品对比总结\n\n| 特性指标 | VITS | Bark | XTTS (v2) | GPT-SoVITS (竞品参考) |\n| :--- | :--- | :--- | :--- | :--- |\n| **基础架构** | CVAE + Flow | GPT-style Transformer | Conditioning Model | GPT + SoVITS [22] |\n| **推理速度** | 极快（并行） | 视硬件而定（实时需企业级 GPU） | 较快 | **RTF: 0.014** (4090) [23] |\n| **硬件要求** | 较低 | 较高 (**12GB VRAM**) [12] | 中等 | **VRAM 略高于 v2** [24] |\n| **克隆成本** | 需微调（~1小时）[7] | 不支持自定义克隆 [25] | **6秒音频** (零样本) [19] | **5秒(零样本)/1分钟(微调)** [22] |\n| **特殊能力** | 节奏随机性、高自然度 | 非言语信息、音乐 [14] | 跨语言能力、插值 [18] | 高情感表达、高稳定性 [26] |\n| **输出质量** | 接近真人（单人） | 变化较大（似 80 年代通话或完美语音）[27] | 24kHz 高保真 | 可达 **48k 原生输出** (v4) [28] |\n\n**总结：** \n*   如果你追求**单人极致音质**和推理效率，**VITS** 是首选。\n*   如果你需要**极简克隆**和多语言支持，**XTTS** 最具优势。\n*   如果你需要音频中包含**非语言情感（笑声、叹气）**或环境音，**Bark** 表现最强。\n*   对于兼顾速度与相似度的场景，**GPT-SoVITS** 在 RTX 4090 上可实现高达 **0.014** 的实时频率比 (RTF) [23]。",
    "conversation_id": "86674cd6-e082-45ea-acd4-9e41134ebd11",
    "sources_used": [
      "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "01cd196f-8e66-427c-a23c-273246e938e0",
      "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "64bbccb9-1477-4b71-973e-92976cf467e4",
      "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "bab69d19-3140-457c-a75a-12b45648b450",
      "62f3466b-587f-45a7-b032-540895b3f1c5"
    ],
    "citations": {
      "1": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "2": "01cd196f-8e66-427c-a23c-273246e938e0",
      "3": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "4": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "5": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "6": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "7": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "8": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "9": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "10": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "11": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "12": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "13": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "14": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "15": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "16": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "17": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "18": "bab69d19-3140-457c-a75a-12b45648b450",
      "19": "bab69d19-3140-457c-a75a-12b45648b450",
      "20": "bab69d19-3140-457c-a75a-12b45648b450",
      "21": "bab69d19-3140-457c-a75a-12b45648b450",
      "22": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "23": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "24": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "25": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "26": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "27": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "28": "62f3466b-587f-45a7-b032-540895b3f1c5"
    },
    "references": [
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 1,
        "cited_text": "VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech Jaehyeon Kim, Jungil Kong, and Juhee Son In our recent paper , we propose VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech. Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text. With the uncertainty modeling over latent variables and the stochastic duration predictor, our method expresses the natural one-to-many relationship in which a text input can be spoken in multiple ways with different pitches and rhythms. A subjective human evaluation (mean opinion score, or MOS) on the LJ Speech, a single speaker dataset, shows that our method outperforms the best publicly available TTS systems and achieves a MOS comparable to ground truth."
      },
      {
        "source_id": "01cd196f-8e66-427c-a23c-273246e938e0",
        "citation_number": 2,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2106.06103 Help | Advanced Search Computer Science > Sound arXiv:2106.06103 (cs)   [Submitted on 11 Jun 2021] Title: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech Authors: Jaehyeon Kim , Jungil Kong , Juhee Son View a PDF of the paper titled Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech, by Jaehyeon Kim and 2 other authors View PDF Abstract: Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text. With the uncertainty modeling over latent variables and the stochastic duration predictor, our method expresses the natural one-to-many relationship in which a text input can be spoken in multiple ways with different pitches and rhythms. A subjective human evaluation (mean opinion score, or MOS) on the LJ Speech, a single speaker dataset, shows that our method outperforms the best publicly available TTS systems and achieves a MOS comparable to ground truth.  Comments:   ICML 2021   Subjects:   Sound (cs.SD) ; Audio and Speech Processing (eess.AS)   Cite as: arXiv:2106.06103 [cs.SD]   (or arXiv:2106.06103v1 [cs.SD]  for this version) https://doi.org/10.48550/arXiv.2106.06103 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 3,
        "cited_text": "Visit our demo for audio samples. We also provide the pretrained models . ** Update note: Thanks to Rishikesh (ऋषिकेश) , our interactive TTS demo is now available on Colab Notebook . VITS at training   VITS at inference Pre-requisites Python >= 3.6 Clone this repository Install python requirements. Please refer requirements.txt You may need to install espeak first:  apt-get install espeak Download datasets Download and extract the LJ Speech dataset, then rename or create a link to the dataset folder:  ln -s /path/to/LJSpeech-1.1/wavs DUMMY1 For mult-speaker setting, download and extract the VCTK dataset, and downsample wav files to 22050 Hz. Then rename or create a link to the dataset folder:  ln -s /path/to/VCTK-Corpus/downsampled_wavs DUMMY2 Build Monotonic Alignment Search and run preprocessing if you use your own datasets."
      },
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 4,
        "cited_text": "#  Cython-version Monotonoic Alignment Search   cd  monotonic_align python setup.py build_ext --inplace  #  Preprocessing (g2p) for your own datasets. Preprocessed phonemes for LJ Speech and VCTK have been already provided.   #  python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_train_filelist.txt filelists/ljs_audio_text_val_filelist.txt filelists/ljs_audio_text_test_filelist.txt  #  python preprocess.py --text_index 2 --filelists filelists/vctk_audio_sid_text_train_filelist.txt filelists/vctk_audio_sid_text_val_filelist.txt filelists/vctk_audio_sid_text_test_filelist.txt"
      },
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 5,
        "cited_text": "Notifications You must be signed in to change notification settings Fork  736 Star  5k Additional navigation options Code Issues Pull requests Actions Projects Security and quality Insights Plachtaa/VITS-fast-fine-tuning Branches Tags Open more actions menu Folders and files Name Name Last commit message Last commit date Latest commit History 263 Commits 263 Commits .idea .idea configs configs monotonic_align monotonic_align scripts scripts text text DATA.MD DATA.MD DATA_EN.MD DATA_EN.MD LICENSE LICENSE LOCAL.md LOCAL.md README.md README.md README_ZH.md README_ZH.md VC_inference.py VC_inference.py attentions.py attentions.py cmd_inference.py cmd_inference.py commons.py commons.py data_utils.py data_utils.py finetune_speaker_v2.py finetune_speaker_v2.py losses.py losses.py mel_processing.py mel_processing.py models.py models.py models_infer.py models_infer.py modules.py modules.py preprocess_v2.py preprocess_v2.py requirements.txt requirements.txt transforms.py transforms.py utils.py utils.py Repository files navigation"
      },
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 6,
        "cited_text": "Notifications You must be signed in to change notification settings Fork  1.4k Star  7.8k Additional navigation options Code Issues Pull requests Actions Projects Security and quality Insights jaywalnut310/vits Branches Tags Open more actions menu Folders and files Name Name Last commit message Last commit date Latest commit History 12 Commits 12 Commits configs configs filelists filelists monotonic_align monotonic_align resources resources text text .gitignore .gitignore LICENSE LICENSE README.md README.md attentions.py attentions.py commons.py commons.py data_utils.py data_utils.py inference.ipynb inference.ipynb losses.py losses.py mel_processing.py mel_processing.py models.py models.py modules.py modules.py preprocess.py preprocess.py requirements.txt requirements.txt train.py train.py train_ms.py train_ms.py transforms.py transforms.py utils.py utils.py Repository files navigation"
      },
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 7,
        "cited_text": "Fine-tuning See LOCAL.md for local training guide. \n  Alternatively, you can perform fine-tuning on Google Colab How long does it take? Install dependencies (3 min) Choose pretrained model to start. The detailed differences between them are described in Colab Notebook Upload the voice samples of the characters you wish to add，see DATA.MD for detailed uploading options. Start fine-tuning. Time taken varies from 20 minutes ~ 2 hours, depending on the number of voices you uploaded. Inference or Usage (Currently support Windows only)"
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 8,
        "cited_text": "pizza.webm To save  audio_array  as a WAV file: from  scipy.io.wavfile  import  write  as  write_wav write_wav( \"/path/to/audio.wav\" , SAMPLE_RATE, audio_array) Model Details The following is additional information about the models released here. Bark is a series of three transformer models that turn text into audio. Text to semantic tokens Input: text, tokenized with BERT tokenizer from Hugging Face Output: semantic tokens that encode the audio to be generated Semantic to coarse tokens Input: semantic tokens Output: tokens from the first two codebooks of the EnCodec Codec from facebook"
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 9,
        "cited_text": "Coarse to fine tokens Input: the first two codebooks from EnCodec Output: 8 codebooks from EnCodec Architecture Model   Parameters   Attention   Output Vocab size   Text to semantic tokens   80/300 M   Causal   10,000   Semantic to coarse tokens   80/300 M   Causal   2x 1,024   Coarse to fine tokens   80/300 M   Non-causal   6x 1,024 Release date April 2023 Broader Implications We anticipate that this model's text to audio capabilities can be used to improve accessbility tools in a variety of languages."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 10,
        "cited_text": "If you don't have hardware available or if you want to play with bigger versions of our models, you can also sign up for early access to our model playground here . ⚙️ Details Bark is fully generative text-to-audio model devolved for research and demo purposes. It follows a GPT style architecture similar to AudioLM and Vall-E and a quantized Audio representation from EnCodec . It is not a conventional TTS model, but instead a fully generative text-to-audio model capable of deviating in unexpected ways from any given script. Different to previous approaches, the input text prompt is converted directly to audio without the intermediate use of phonemes. It can therefore generalize to arbitrary instructions beyond speech such as music lyrics, sound effects or other non-speech sounds."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 11,
        "cited_text": "Requests for future language support here or in the #forums channel on Discord . 🙏 Appreciation nanoGPT for a dead-simple and blazing fast implementation of GPT-style models EnCodec for a state-of-the-art implementation of a fantastic audio codec AudioLM for related training and inference code Vall-E , AudioLM and many other ground-breaking papers that enabled the development of Bark © License Bark is licensed under the MIT License. 📱 Community Twitter Discord 🎧 Suno Studio (Early Access) We’re developing a playground for our models, including Bark."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 12,
        "cited_text": "🛠️ Hardware and Inference Speed Bark has been tested and works on both CPU and GPU ( pytorch 2.0+ , CUDA 11.7 and CUDA 12.0). On enterprise GPUs and PyTorch nightly, Bark can generate audio in roughly real-time. On older GPUs, default colab, or CPU, inference time might be significantly slower. For older GPUs or CPU you might want to consider using smaller models. Details can be found in out tutorial sections here. The full version of Bark requires around 12GB of VRAM to hold everything on GPU at the same time. To use a smaller version of the models, which should fit into 8GB VRAM, set the environment flag  SUNO_USE_SMALL_MODELS=True ."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 13,
        "cited_text": "Why is the output limited to ~13-14 seconds? Bark is a GPT-style model, and its architecture/context window is optimized to output generations with roughly this length. How much VRAM do I need? The full version of Bark requires around 12Gb of memory to hold everything on GPU at the same time. However, even smaller cards down to ~2Gb work with some additional settings. Simply add the following code snippet before your generation: import   os   os . environ [ \"SUNO_OFFLOAD_CPU\" ]  =   \"True\"   os . environ [ \"SUNO_USE_SMALL_MODELS\" ]  =   \"True\""
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 14,
        "cited_text": "Notice: Bark is Suno's open-source text-to-speech+ model. If you are looking for our text-to-music models, please visit us on our web page and join our community on Discord . 🐶 Bark 🔗 Examples • Suno Studio Waitlist • Updates • How to Use • Installation • FAQ Bark is a transformer-based text-to-audio model created by Suno . Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. The model can also produce nonverbal communications like laughing, sighing and crying. To support the research community, we are providing access to pretrained model checkpoints, which are ready for inference and available for commercial use."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 15,
        "cited_text": "Below is a list of some known non-speech sounds, but we are finding more every day. Please let us know if you find patterns that work particularly well on Discord ! [laughter] [laughs] [sighs] [music] [gasps] [clears throat] —  or  ...  for hesitations ♪  for song lyrics CAPITALIZATION for emphasis of a word [MAN]  and  [WOMAN]  to bias Bark toward male and female speakers, respectively Supported Languages Language   Status   English (en)   ✅   German (de)   ✅   Spanish (es)   ✅   French (fr)   ✅   Hindi (hi)   ✅   Italian (it)   ✅   Japanese (ja)   ✅   Korean (ko)   ✅   Polish (pl)   ✅   Portuguese (pt)   ✅   Russian (ru)   ✅   Turkish (tr)   ✅   Chinese, simplified (zh)   ✅"
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 16,
        "cited_text": "Run inference via the Transformers modelling code. You can use the processor + generate code to convert text into a mono 24 kHz speech waveform for more fine-grained control. from  transformers  import  AutoProcessor, AutoModel processor = AutoProcessor.from_pretrained( \"suno/bark\" ) model = AutoModel.from_pretrained( \"suno/bark\" ) inputs = processor( text=[ \"Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe.\" ], return_tensors= \"pt\" , ) speech_values = model.generate(**inputs, do_sample= True )"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 17,
        "cited_text": "Bark tries to match the tone, pitch, emotion and prosody of a given preset, but does not currently support custom voice cloning. The model also attempts to preserve music, ambient noise, etc. text_prompt   =   \"\"\"    I have a silky smooth voice, and today I will tell you about   the exercise regimen of the common sloth.   \"\"\"   audio_array   =   generate_audio ( text_prompt ,  history_prompt = \"v2/en_speaker_1\" )   sloth.webm 📃 Generating Longer Audio By default,  generate_audio  works well with around 13 seconds of spoken text. For an example of how to do long-form generation, see 👉 Notebook 👈"
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 18,
        "cited_text": "Features Supports 17 languages. Voice cloning with just a 6-second audio clip. Emotion and style transfer by cloning. Cross-language voice cloning. Multi-lingual speech generation. 24khz sampling rate. Updates over XTTS-v1 2 new languages; Hungarian and Korean Architectural improvements for speaker conditioning. Enables the use of multiple speaker references and interpolation between speakers. Stability improvements. Better prosody and audio quality across the board. Languages XTTS-v2 supports 17 languages: English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi) ."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 19,
        "cited_text": "Hugging Face Log In Sign Up coqui / XTTS-v2 Coqui.ai Text-to-Speech coqui Model card Files   Files and versions   xet Community   143 Configuration Parsing Warning: Invalid JSON for config file config.json ⓍTTS ⓍTTS is a Voice generation model that lets you clone voices into different languages by using just a quick 6-second audio clip. There is no need for an excessive amount of training data that spans countless hours. This is the same or similar model to what powers Coqui Studio and Coqui API ."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 20,
        "cited_text": "This model is licensed under Coqui Public Model License . There's a lot that goes into a license for generative models, and you can read more of the origin story of CPML here . Contact Come and join in our 🐸Community. We're active on Discord and Twitter . You can also mail us at info@coqui.ai . Using 🐸TTS API: from  TTS.api  import  TTS tts = TTS( \"tts_models/multilingual/multi-dataset/xtts_v2\" , gpu= True )  # generate speech by cloning a voice using default settings  tts.tts_to_file(text= \"It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.\" , file_path= \"output.wav\" , speaker_wav= \"/path/to/target/speaker.wav\" , language= \"en\" )"
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 21,
        "cited_text": "Using 🐸TTS Command line: tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \\ --text \"Bugün okula gitmek istemiyorum.\" \\ --speaker_wav /path/to/target/speaker.wav \\ --language_idx tr \\ --use_cuda true Using the model directly: from  TTS.tts.configs.xtts_config  import  XttsConfig  from  TTS.tts.models.xtts  import  Xtts config = XttsConfig() config.load_json( \"/path/to/xtts/config.json\" ) model = Xtts.init_from_config(config) model.load_checkpoint(config, checkpoint_dir= \"/path/to/xtts/\" ,  eval = True ) model.cuda() outputs = model.synthesize(  \"It took me quite a long time to develop a voice and now that I have it I am not going to be silent.\" , config, speaker_wav= \"/data/TTS-public/_refclips/3.wav\" , gpt_cond_len= 3 , language= \"en\" , )  Downloads last month   6,270,396 Model tree for  coqui/XTTS-v2"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 22,
        "cited_text": "GPT-SoVITS-WebUI A Powerful Few-shot Voice Conversion and Text-to-Speech WebUI. English | 中文简体 | 日本語 | 한국어 | Türkçe Features: Zero-shot TTS: Input a 5-second vocal sample and experience instant text-to-speech conversion. Few-shot TTS: Fine-tune the model with just 1 minute of training data for improved voice similarity and realism. Cross-lingual Support: Inference in languages different from the training dataset, currently supporting English, Japanese, Korean, Cantonese and Chinese. WebUI Tools: Integrated tools include voice accompaniment separation, automatic training set segmentation, Chinese ASR, and text labeling, assisting beginners in creating training datasets and GPT/SoVITS models."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 23,
        "cited_text": "Check out our demo video here! Unseen speakers few-shot fine-tuning demo: few.shot.fine.tuning.demo.mp4 RTF(inference speed) of GPT-SoVITS v2 ProPlus : 0.028 tested in 4060Ti, 0.014 tested in 4090 (1400words~=4min, inference time is 3.36s), 0.526 in M4 CPU. You can test our huggingface demo (half H200) to experience high-speed inference . 请不要尬黑GPT-SoVITS推理速度慢，谢谢！ User guide: 简体中文 | English Installation For users in China, you can click here to use AutoDL Cloud Docker to experience the full functionality online."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 24,
        "cited_text": "V2Pro Release Notes New Features: Slightly higher VRAM usage than v2, surpassing v4's performance, with v2's hardware cost and speed. more details 2.v1/v2 and the v2Pro series share the same characteristics, while v3/v4 have similar features. For training sets with average audio quality, v1/v2/v2Pro can deliver decent results, but v3/v4 cannot. Additionally, the synthesized tone and timebre of v3/v4 lean more toward the reference audio rather than the overall training set. Use v2Pro from v1/v2/v3/v4 environment:"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 25,
        "cited_text": "If you are interested, you can sign up for early access here . ❓ FAQ How do I specify where models are downloaded and cached? Bark uses Hugging Face to download and store models. You can see find more info here . Bark's generations sometimes differ from my prompts. What's happening? Bark is a GPT-style model. As such, it may take some creative liberties in its generations, resulting in higher-variance model outputs than traditional text-to-speech approaches. What voices are supported by Bark? Bark supports 100+ speaker presets across supported languages . You can browse the library of speaker presets here . The community also shares presets in Discord . Bark also supports generating unique random voices that fit the input text. Bark does not currently support custom voice cloning."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 26,
        "cited_text": "GPT model is more stable, with fewer repetitions and omissions, and it is easier to generate speech with richer emotional expression. more details Use v3 from v2 environment: pip install -r requirements.txt  to update some packages Clone the latest codes from github. Download v3 pretrained models (s1v3.ckpt, s2Gv3.pth and models--nvidia--bigvgan_v2_24khz_100band_256x folder) from huggingface and put them into  GPT_SoVITS/pretrained_models . additional: for Audio Super Resolution model, you can read how to download"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 27,
        "cited_text": "My generated audio sounds like a 1980s phone call. What's happening? Bark generates audio from scratch. It is not meant to create only high-fidelity, studio-quality speech. Rather, outputs could be anything from perfect speech to multiple people arguing at a baseball game recorded with bad microphones. About 🔊 Text-Prompted Generative Audio Model Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 39.1k stars Watchers"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 28,
        "cited_text": "V4 Release Notes New Features: Version 4 fixes the issue of metallic artifacts in Version 3 caused by non-integer multiple upsampling, and natively outputs 48k audio to prevent muffled sound (whereas Version 3 only natively outputs 24k audio). The author considers Version 4 a direct replacement for Version 3, though further testing is still needed. more details Use v4 from v1/v2/v3 environment: pip install -r requirements.txt  to update some packages Clone the latest codes from github. Download v4 pretrained models (gsv-v4-pretrained/s2v4.pth, and gsv-v4-pretrained/vocoder.pth) from huggingface and put them into  GPT_SoVITS/pretrained_models ."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "基于提供的源文件，以下是关于 **VITS**、**Bark** 和 **XTTS**（以及相关改进型如 **GPT-SoVITS**）的真实应用场景、部署方案、性能数据及实战经验的深度对比：\n\n### 1. 真实应用场景与案例\n\n*   **VITS (及其变体 VITS-fast-fine-tuning):**\n    *   **快速角色适配：** 适用于在短时间内（小于1小时）将特定角色声音（如游戏角色、个人声音）接入 TTS 系统 [1]。\n    *   **多语种切换：** 广泛用于中、英、日三语的语音合成和**多对多语音转换 (VC)** [1, 2]。\n    *   **高自然度需求场景：** 适用于追求接近真人听感（MOS 分与原始音频相当）的单人或多人语音合成 [3, 4]。\n*   **Bark:**\n    *   **创意音频生成：** 除语音外，可生成**背景噪音、简单音效及音乐**（通过 `♪` 符号触发） [5, 6]。\n    *   **非语言交流：** 能够模拟人类的**笑声 [laughs]、叹气 [sighs]、哭泣 [crying]** 等情感表达 [5, 7]。\n    *   **无障碍工具：** 用于开发多语言的辅助交流工具 [8]。\n*   **XTTS (v2):**\n    *   **即时语音克隆：** 仅需 **6 秒音频** 即可完成克隆，适用于需要快速生成特定说话人声音的场景 [9, 10]。\n    *   **跨语言语音克隆：** 例如用中文参考音频生成该音色的英文语音 [10]。\n    *   **实时交互：** 配合 Mistral 或 Zephyr 等大模型实现**流式语音聊天** [11]。\n\n### 2. 工业级部署与开源实战\n\n*   **工业级/商业化方案：**\n    *   **XTTS** 技术直接支持了 **Coqui Studio** 和 **Coqui API**，具备成熟的商业服务架构 [9]。\n    *   **Bark** 提供针对企业级 GPU 优化的推理，并有小型化模型（Small models）支持低显存部署 [12, 13]。\n*   **开源项目案例：**\n    *   **GPT-SoVITS：** 提供集成的 WebUI 工具，支持从音频分离、自动切分、ASR（语音识别）到模型训练的全流程，极大降低了新手门槛 [14]。\n    *   **Bert-VITS2：** 将多语言 BERT 骨干网络与 VITS2 结合，是目前社区活跃的替代方案之一 [15, 16]。\n\n### 3. 性能基准数据\n\n| 维度 | VITS / VITS-fast | Bark | XTTS (v2) | GPT-SoVITS (v2 ProPlus) |\n| :--- | :--- | :--- | :--- | :--- |\n| **推理速度 (RTF)** | 极快 (并行采样) [3] | 实时 (企业级 GPU) [12] | 较快 | **4090: 0.014** / M4 CPU: 0.526 [17] |\n| **显存要求** | 较低 | **12GB (完整)** / 8GB (小型) [12] | 中等 | v2 硬件成本水平 [18] |\n| **音频采样率** | 通常为 22.05kHz [19] | **24kHz** [20] | **24kHz** [10] | **48k (原生输出, v4)** [21] |\n| **克隆所需数据** | 10+ 短音频或 3min+ 长音频 [22] | 不支持自定义克隆 [23] | **6 秒** [9] | **5 秒 (零样本)** / 1 分钟 (微调) [14] |\n\n### 4. 开发者最佳实践与踩坑经验\n\n#### **最佳实践：**\n*   **Bark 环境优化：** \n    *   显存不足（<4GB）时，设置环境标志 `SUNO_OFFLOAD_CPU=True` 和 `SUNO_USE_SMALL_MODELS=True` [24]。\n    *   使用 `pip install git+https://github.com/suno-ai/bark.git` 避免安装错误的同名包 [25]。\n*   **VITS 训练细节：** \n    *   必须安装 `ffmpeg` 以启用语音转换功能 [26]。\n    *   需手动构建 `monotonic_align` 的 Cython 版本以提升性能 [27, 28]。\n*   **GPT-SoVITS 部署：** \n    *   在 Windows Docker 部署时，务必增加 **共享内存 (shm_size)**（如设为 16g）以防止非预期行为 [29]。\n\n#### **常见踩坑经验：**\n*   **音频质量问题：** \n    *   Bark 的生成具有高度随机性，有时听起来像 **1980 年代的电话通话** 并非系统错误，而是其全生成架构导致的输出差异 [23, 30]。\n    *   XTTS 在参考音频质量较低时，合成效果会受影响，GPT-SoVITS v2 在这方面做了专项优化 [31]。\n*   **硬件限制：** \n    *   **macOS 用户注意：** 在 Mac 上使用 GPU 训练的模型质量显著低于其他设备，建议暂时使用 CPU 进行训练 [32]。\n    *   **输出长度：** Bark 的架构针对 **13-14 秒** 的音频进行了优化，超长生成需参考专门的 Notebook 处理技巧 [24, 33]。",
    "conversation_id": "86674cd6-e082-45ea-acd4-9e41134ebd11",
    "sources_used": [
      "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "01cd196f-8e66-427c-a23c-273246e938e0",
      "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "64bbccb9-1477-4b71-973e-92976cf467e4",
      "bab69d19-3140-457c-a75a-12b45648b450",
      "62f3466b-587f-45a7-b032-540895b3f1c5",
      "dfdfcb84-b50d-4200-8c8a-118595cc5f04"
    ],
    "citations": {
      "1": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "2": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "3": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "4": "01cd196f-8e66-427c-a23c-273246e938e0",
      "5": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "6": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "7": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "8": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "9": "bab69d19-3140-457c-a75a-12b45648b450",
      "10": "bab69d19-3140-457c-a75a-12b45648b450",
      "11": "bab69d19-3140-457c-a75a-12b45648b450",
      "12": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "13": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "14": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "15": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
      "16": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
      "17": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "18": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "19": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "20": "64bbccb9-1477-4b71-973e-92976cf467e4",
      "21": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "22": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "23": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "24": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "25": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "26": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "27": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "28": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
      "29": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "30": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "31": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "32": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "33": "3e1586be-d28d-4c1f-b308-124ac3ed7669"
    },
    "references": [
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 1,
        "cited_text": "中文文档请点击这里 VITS Fast Fine-tuning This repo will guide you to add your own character voices, or even your own voice, into existing VITS TTS model to make it able to do the following tasks in less than 1 hour: Many-to-many voice conversion between any characters you added & preset characters in the model. English, Japanese & Chinese Text-to-Speech synthesis with the characters you added & preset characters Welcome to play around with the base models! \n  Chinese & English & Japanese： Author: Me Chinese & Japanese： Author: SayaSS"
      },
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 2,
        "cited_text": "Use in MoeGoe Prepare downloaded model & config file, which are named  G_latest.pth  and  moegoe_config.json , respectively. Follow MoeGoe page instructions to install, configure path, and use. Looking for help? If you have any questions, please feel free to open an issue or join our Discord server. About This repo is a pipeline of VITS finetuning for fast speaker adaptation TTS, and many-to-many voice conversion Resources Readme License Apache-2.0 license Uh oh! There was an error while loading. Please reload this page ."
      },
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 3,
        "cited_text": "VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech Jaehyeon Kim, Jungil Kong, and Juhee Son In our recent paper , we propose VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech. Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text. With the uncertainty modeling over latent variables and the stochastic duration predictor, our method expresses the natural one-to-many relationship in which a text input can be spoken in multiple ways with different pitches and rhythms. A subjective human evaluation (mean opinion score, or MOS) on the LJ Speech, a single speaker dataset, shows that our method outperforms the best publicly available TTS systems and achieves a MOS comparable to ground truth."
      },
      {
        "source_id": "01cd196f-8e66-427c-a23c-273246e938e0",
        "citation_number": 4,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2106.06103 Help | Advanced Search Computer Science > Sound arXiv:2106.06103 (cs)   [Submitted on 11 Jun 2021] Title: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech Authors: Jaehyeon Kim , Jungil Kong , Juhee Son View a PDF of the paper titled Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech, by Jaehyeon Kim and 2 other authors View PDF Abstract: Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text. With the uncertainty modeling over latent variables and the stochastic duration predictor, our method expresses the natural one-to-many relationship in which a text input can be spoken in multiple ways with different pitches and rhythms. A subjective human evaluation (mean opinion score, or MOS) on the LJ Speech, a single speaker dataset, shows that our method outperforms the best publicly available TTS systems and achieves a MOS comparable to ground truth.  Comments:   ICML 2021   Subjects:   Sound (cs.SD) ; Audio and Speech Processing (eess.AS)   Cite as: arXiv:2106.06103 [cs.SD]   (or arXiv:2106.06103v1 [cs.SD]  for this version) https://doi.org/10.48550/arXiv.2106.06103 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 5,
        "cited_text": "Notice: Bark is Suno's open-source text-to-speech+ model. If you are looking for our text-to-music models, please visit us on our web page and join our community on Discord . 🐶 Bark 🔗 Examples • Suno Studio Waitlist • Updates • How to Use • Installation • FAQ Bark is a transformer-based text-to-audio model created by Suno . Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. The model can also produce nonverbal communications like laughing, sighing and crying. To support the research community, we are providing access to pretrained model checkpoints, which are ready for inference and available for commercial use."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 6,
        "cited_text": "Bark can generate all types of audio, and, in principle, doesn't see a difference between speech and music. Sometimes Bark chooses to generate text as music, but you can help it out by adding music notes around your lyrics.  text_prompt   =   \"\"\"    ♪ In the jungle, the mighty jungle, the lion barks tonight ♪   \"\"\"   audio_array   =   generate_audio ( text_prompt )   lion.webm 🎤 Voice Presets Bark supports 100+ speaker presets across supported languages . You can browse the library of supported voice presets HERE , or in the code . The community also often shares presets in Discord ."
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 7,
        "cited_text": "Hugging Face Log In Sign Up suno / bark Suno Text-to-Speech Transformers PyTorch bark text-to-audio audio Model card Files   Files and versions   xet Community   61 Bark Bark is a transformer-based text-to-audio model created by Suno . Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. The model can also produce nonverbal communications like laughing, sighing and crying. To support the research community, we are providing access to pretrained model checkpoints ready for inference."
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 8,
        "cited_text": "Coarse to fine tokens Input: the first two codebooks from EnCodec Output: 8 codebooks from EnCodec Architecture Model   Parameters   Attention   Output Vocab size   Text to semantic tokens   80/300 M   Causal   10,000   Semantic to coarse tokens   80/300 M   Causal   2x 1,024   Coarse to fine tokens   80/300 M   Non-causal   6x 1,024 Release date April 2023 Broader Implications We anticipate that this model's text to audio capabilities can be used to improve accessbility tools in a variety of languages."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 9,
        "cited_text": "Hugging Face Log In Sign Up coqui / XTTS-v2 Coqui.ai Text-to-Speech coqui Model card Files   Files and versions   xet Community   143 Configuration Parsing Warning: Invalid JSON for config file config.json ⓍTTS ⓍTTS is a Voice generation model that lets you clone voices into different languages by using just a quick 6-second audio clip. There is no need for an excessive amount of training data that spans countless hours. This is the same or similar model to what powers Coqui Studio and Coqui API ."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 10,
        "cited_text": "Features Supports 17 languages. Voice cloning with just a 6-second audio clip. Emotion and style transfer by cloning. Cross-language voice cloning. Multi-lingual speech generation. 24khz sampling rate. Updates over XTTS-v1 2 new languages; Hungarian and Korean Architectural improvements for speaker conditioning. Enables the use of multiple speaker references and interpolation between speakers. Stability improvements. Better prosody and audio quality across the board. Languages XTTS-v2 supports 17 languages: English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi) ."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 11,
        "cited_text": "Stay tuned as we continue to add support for more languages. If you have any language requests, feel free to reach out! Code The code-base supports inference and fine-tuning . Demo Spaces XTTS Space : You can see how model performs on supported languages, and try with your own reference or microphone input XTTS Voice Chat with Mistral or Zephyr : You can experience streaming voice chat with Mistral 7B Instruct or Zephyr 7B Beta 🐸💬 CoquiTTS coqui/TTS on Github 💼 Documentation ReadTheDocs 👩‍💻 Questions GitHub Discussions 🗯 Community Discord License"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 12,
        "cited_text": "🛠️ Hardware and Inference Speed Bark has been tested and works on both CPU and GPU ( pytorch 2.0+ , CUDA 11.7 and CUDA 12.0). On enterprise GPUs and PyTorch nightly, Bark can generate audio in roughly real-time. On older GPUs, default colab, or CPU, inference time might be significantly slower. For older GPUs or CPU you might want to consider using smaller models. Details can be found in out tutorial sections here. The full version of Bark requires around 12GB of VRAM to hold everything on GPU at the same time. To use a smaller version of the models, which should fit into 8GB VRAM, set the environment flag  SUNO_USE_SMALL_MODELS=True ."
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 13,
        "cited_text": "The original github repo and model card can be found here . This model is meant for research purposes only. The model output is not censored and the authors do not endorse the opinions in the generated content. Use at your own risk. Two checkpoints are released: small large (this checkpoint) Example Try out Bark yourself! Bark Colab: Hugging Face Colab: Hugging Face Demo: 🤗 Transformers Usage You can run Bark locally with the 🤗 Transformers library from version 4.31.0 onwards. First install the 🤗 Transformers library and scipy:"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 14,
        "cited_text": "GPT-SoVITS-WebUI A Powerful Few-shot Voice Conversion and Text-to-Speech WebUI. English | 中文简体 | 日本語 | 한국어 | Türkçe Features: Zero-shot TTS: Input a 5-second vocal sample and experience instant text-to-speech conversion. Few-shot TTS: Fine-tune the model with just 1 minute of training data for improved voice similarity and realism. Cross-lingual Support: Inference in languages different from the training dataset, currently supporting English, Japanese, Korean, Cantonese and Chinese. WebUI Tools: Integrated tools include voice accompaniment separation, automatic training set segmentation, Chinese ASR, and text labeling, assisting beginners in creating training datasets and GPT/SoVITS models."
      },
      {
        "source_id": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
        "citation_number": 15,
        "cited_text": "Bert-VITS2 VITS2 Backbone with multilingual bert For quick guide, please refer to  webui_preprocess.py . 简易教程请参见  webui_preprocess.py 。 【项目推介】 FishAudio下的全新自回归TTS Fish-Speech 现已可用，效果为目前开源SOTA水准，且在持续维护，推荐使用该项目作为BV2/GSV的替代。本项目短期内不再进行维护。 Demo Video: https://www.bilibili.com/video/BV18E421371Q Tech slides Video: https://www.bilibili.com/video/BV1zJ4m1K7cj 请注意，本项目核心思路来源于 anyvoiceai/MassTTS 一个非常好的tts项目 MassTTS的演示demo为 ai版峰哥锐评峰哥本人,并找回了在金三角失落的腰子 成熟的旅行者/开拓者/舰长/博士/sensei/猎魔人/喵喵露/V应当参阅代码自己学习如何训练。 严禁将此项目用于一切违反《中华人民共和国宪法》，《中华人民共和国刑法》，《中华人民共和国治安管理处罚法》和《中华人民共和国民法典》之用途。"
      },
      {
        "source_id": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
        "citation_number": 16,
        "cited_text": "严禁用于任何政治相关用途。 Video: https://www.bilibili.com/video/BV1hp4y1K78E Demo: https://www.bilibili.com/video/BV1TF411k78w References anyvoiceai/MassTTS jaywalnut310/vits p0p4k/vits2_pytorch svc-develop-team/so-vits-svc PaddlePaddle/PaddleSpeech emotional-vits fish-speech Bert-VITS2-UI 感谢所有贡献者作出的努力 About vits2 backbone with multilingual-bert Topics agent fish tts bert vocoder vits llm vits2 bert-vits bert-vits2 fish-speech Resources Readme License AGPL-3.0 license Uh oh! There was an error while loading. Please reload this page ."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 17,
        "cited_text": "Check out our demo video here! Unseen speakers few-shot fine-tuning demo: few.shot.fine.tuning.demo.mp4 RTF(inference speed) of GPT-SoVITS v2 ProPlus : 0.028 tested in 4060Ti, 0.014 tested in 4090 (1400words~=4min, inference time is 3.36s), 0.526 in M4 CPU. You can test our huggingface demo (half H200) to experience high-speed inference . 请不要尬黑GPT-SoVITS推理速度慢，谢谢！ User guide: 简体中文 | English Installation For users in China, you can click here to use AutoDL Cloud Docker to experience the full functionality online."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 18,
        "cited_text": "V2Pro Release Notes New Features: Slightly higher VRAM usage than v2, surpassing v4's performance, with v2's hardware cost and speed. more details 2.v1/v2 and the v2Pro series share the same characteristics, while v3/v4 have similar features. For training sets with average audio quality, v1/v2/v2Pro can deliver decent results, but v3/v4 cannot. Additionally, the synthesized tone and timebre of v3/v4 lean more toward the reference audio rather than the overall training set. Use v2Pro from v1/v2/v3/v4 environment:"
      },
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 19,
        "cited_text": "Visit our demo for audio samples. We also provide the pretrained models . ** Update note: Thanks to Rishikesh (ऋषिकेश) , our interactive TTS demo is now available on Colab Notebook . VITS at training   VITS at inference Pre-requisites Python >= 3.6 Clone this repository Install python requirements. Please refer requirements.txt You may need to install espeak first:  apt-get install espeak Download datasets Download and extract the LJ Speech dataset, then rename or create a link to the dataset folder:  ln -s /path/to/LJSpeech-1.1/wavs DUMMY1 For mult-speaker setting, download and extract the VCTK dataset, and downsample wav files to 22050 Hz. Then rename or create a link to the dataset folder:  ln -s /path/to/VCTK-Corpus/downsampled_wavs DUMMY2 Build Monotonic Alignment Search and run preprocessing if you use your own datasets."
      },
      {
        "source_id": "64bbccb9-1477-4b71-973e-92976cf467e4",
        "citation_number": 20,
        "cited_text": "Run inference via the Transformers modelling code. You can use the processor + generate code to convert text into a mono 24 kHz speech waveform for more fine-grained control. from  transformers  import  AutoProcessor, AutoModel processor = AutoProcessor.from_pretrained( \"suno/bark\" ) model = AutoModel.from_pretrained( \"suno/bark\" ) inputs = processor( text=[ \"Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe.\" ], return_tensors= \"pt\" , ) speech_values = model.generate(**inputs, do_sample= True )"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 21,
        "cited_text": "V4 Release Notes New Features: Version 4 fixes the issue of metallic artifacts in Version 3 caused by non-integer multiple upsampling, and natively outputs 48k audio to prevent muffled sound (whereas Version 3 only natively outputs 24k audio). The author considers Version 4 a direct replacement for Version 3, though further testing is still needed. more details Use v4 from v1/v2/v3 environment: pip install -r requirements.txt  to update some packages Clone the latest codes from github. Download v4 pretrained models (gsv-v4-pretrained/s2v4.pth, and gsv-v4-pretrained/vocoder.pth) from huggingface and put them into  GPT_SoVITS/pretrained_models ."
      },
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 22,
        "cited_text": "Chinese only：(No running huggingface spaces) Author: Wwwwhy230825 Currently Supported Tasks: Clone character voice from 10+ short audios Clone character voice from long audio(s) >= 3 minutes (one audio should contain single speaker only) Clone character voice from videos(s) >= 3 minutes (one video should contain single speaker only) Clone character voice from BILIBILI video links (one video should contain single speaker only) Currently Supported Characters for TTS & VC: Any character you wish as long as you have their voices! (Note that voice conversion can only be conducted between any two speakers in the model)"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 23,
        "cited_text": "If you are interested, you can sign up for early access here . ❓ FAQ How do I specify where models are downloaded and cached? Bark uses Hugging Face to download and store models. You can see find more info here . Bark's generations sometimes differ from my prompts. What's happening? Bark is a GPT-style model. As such, it may take some creative liberties in its generations, resulting in higher-variance model outputs than traditional text-to-speech approaches. What voices are supported by Bark? Bark supports 100+ speaker presets across supported languages . You can browse the library of speaker presets here . The community also shares presets in Discord . Bark also supports generating unique random voices that fit the input text. Bark does not currently support custom voice cloning."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 24,
        "cited_text": "Why is the output limited to ~13-14 seconds? Bark is a GPT-style model, and its architecture/context window is optimized to output generations with roughly this length. How much VRAM do I need? The full version of Bark requires around 12Gb of memory to hold everything on GPU at the same time. However, even smaller cards down to ~2Gb work with some additional settings. Simply add the following code snippet before your generation: import   os   os . environ [ \"SUNO_OFFLOAD_CPU\" ]  =   \"True\"   os . environ [ \"SUNO_USE_SMALL_MODELS\" ]  =   \"True\""
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 25,
        "cited_text": "Click to toggle example long-form generations (from the example notebook)   dialog.webm   longform_advanced.webm   longform_basic.webm Command line python -m bark --text \"Hello, my name is Suno.\" --output_filename \"example.wav\" 💻 Installation ‼️  CAUTION  ‼️  Do NOT use  pip install bark . It installs a different package, which is not managed by Suno. pip install git+https://github.com/suno-ai/bark.git or git clone https://github.com/suno-ai/bark  cd  bark  &&  pip install  . 🤗 Transformers Usage"
      },
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 26,
        "cited_text": "Remember to download your fine-tuned model! Download the latest release Put your model & config file into the folder  inference , which are named  G_latest.pth  and  finetune_speaker.json , respectively. The file structure should be as follows: inference ├───inference.exe ├───... ├───finetune_speaker.json └───G_latest.pth run  inference.exe , the browser should pop up automatically. Note: you must install  ffmpeg  to enable voice conversion feature. Inference with CLI In this example, we will show how to run inference with the default pretrained model. We are now in the main repository directory."
      },
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 27,
        "cited_text": "Create the necessary folders and download the necessary files. cd monotonic_align/ mkdir monotonic_align python setup.py build_ext --inplace cd .. mkdir pretrained_models # download data for fine-tuning wget https://huggingface.co/datasets/Plachta/sampled_audio4ft/resolve/main/sampled_audio4ft_v2.zip unzip sampled_audio4ft_v2.zip For your finetuned model you may need to create additional directories: mkdir video_data mkdir raw_audio mkdir denoised_audio mkdir custom_character_voice mkdir segmented_character_voice"
      },
      {
        "source_id": "e0e55458-0cc9-4b17-a01b-69b8a6fc2ee5",
        "citation_number": 28,
        "cited_text": "#  Cython-version Monotonoic Alignment Search   cd  monotonic_align python setup.py build_ext --inplace  #  Preprocessing (g2p) for your own datasets. Preprocessed phonemes for LJ Speech and VCTK have been already provided.   #  python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_train_filelist.txt filelists/ljs_audio_text_val_filelist.txt filelists/ljs_audio_text_test_filelist.txt  #  python preprocess.py --text_index 2 --filelists filelists/vctk_audio_sid_text_train_filelist.txt filelists/vctk_audio_sid_text_val_filelist.txt filelists/vctk_audio_sid_text_test_filelist.txt"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 29,
        "cited_text": "Environment Variables is_half : Controls whether half-precision (fp16) is enabled. Set to  true  if your GPU supports it to reduce memory usage. Shared Memory Configuration On Windows (Docker Desktop), the default shared memory size is small and may cause unexpected behavior. Increase  shm_size  (e.g., to  16g ) in your Docker Compose file based on your available system memory. Choosing a Service The  docker-compose.yaml  defines two services: GPT-SoVITS-CU126  &  GPT-SoVITS-CU128 : Full version with all features. GPT-SoVITS-CU126-Lite  &  GPT-SoVITS-CU128-Lite : Lightweight version with reduced dependencies and functionality."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 30,
        "cited_text": "My generated audio sounds like a 1980s phone call. What's happening? Bark generates audio from scratch. It is not meant to create only high-fidelity, studio-quality speech. Rather, outputs could be anything from perfect speech to multiple people arguing at a baseball game recorded with bad microphones. About 🔊 Text-Prompted Generative Audio Model Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 39.1k stars Watchers"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 31,
        "cited_text": "Open Inference WebUI Integrated Package Users Double-click  go-webui-v2.bat  or use  go-webui-v2.ps1  ,then open the inference webui at  1-GPT-SoVITS-TTS/1C-inference Others python GPT_SoVITS/inference_webui.py  < language(optional) > OR python webui.py then open the inference webui at  1-GPT-SoVITS-TTS/1C-inference V2 Release Notes New Features: Support Korean and Cantonese An optimized text frontend Pre-trained model extended from 2k hours to 5k hours Improved synthesis quality for low-quality reference audio"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 32,
        "cited_text": "Users in China can download the package here . Install the program by running the following commands: conda create  - n GPTSoVits python = 3.10  conda activate GPTSoVits pwsh  -F  install.ps1  -- Device  < CU126 | CU128 | CPU >   -- Source  < HF | HF - Mirror | ModelScope >  [ -- DownloadUVR5 ] Linux conda create -n GPTSoVits python=3.10 conda activate GPTSoVits bash install.sh --device  < CU126 | CU128 | ROCM | CPU >  --source  < HF | HF-Mirror | ModelScope >  [--download-uvr5] macOS Note: The models trained with GPUs on Macs result in significantly lower quality compared to those trained on other devices, so we are temporarily using CPUs instead."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 33,
        "cited_text": "Bark tries to match the tone, pitch, emotion and prosody of a given preset, but does not currently support custom voice cloning. The model also attempts to preserve music, ambient noise, etc. text_prompt   =   \"\"\"    I have a silky smooth voice, and today I will tell you about   the exercise regimen of the common sloth.   \"\"\"   audio_array   =   generate_audio ( text_prompt ,  history_prompt = \"v2/en_speaker_1\" )   sloth.webm 📃 Generating Longer Audio By default,  generate_audio  works well with around 13 seconds of spoken text. For an example of how to do long-form generation, see 👉 Notebook 👈"
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "根据提供的源代码和当前的行业技术动态，2025-2026年「神经网络 TTS」领域正经历从经典的端到端架构向**自回归 (AR) 模型**与**流匹配 (Flow Matching)** 架构的深度转型。以下是该领域的最新研究突破、技术趋势及未来方向：\n\n### 1. 2025-2026年重要技术演进与论文趋势\n\n*   **从 VITS 到自回归 SOTA 的演进：** \n    *   传统的 VITS 框架（如 VITS-fast-fine-tuning）已逐渐进入维护后期，该项目于 **2025年11月21日正式归档** [1]。\n    *   **Fish-Speech** 被视为 Bert-VITS2 和 GPT-SoVITS 的强力替代者，代表了目前开源界的 **SOTA（尖端）水平**，其核心采用了全新的**自回归 TTS 架构** [2, 3]。\n*   **架构融合与流匹配技术：** \n    *   **GPT-SoVITS v4** 及后续版本的理论研究开始转向 **F5-TTS** 和 **Shortcut Flow Matching**（快捷流匹配） [4]。这种趋势旨在结合 GPT 的生成稳定性与流匹配的高效采样能力。\n    *   **Bert-VITS2** 成功将 **Multilingual BERT** 骨干网络引入 VITS2，提升了模型对多语言语义的理解能力 [2, 5]。\n*   **高保真与原生高采样率：** \n    *   技术重心正从 24kHz 向原生 **48kHz** 采样率转移。例如 **GPT-SoVITS v4** 通过修复非整数倍上采样导致的金属伪影，实现了原生 48k 音频输出，解决了以往声音“闷”的问题 [6]。\n\n### 2. 最新研究突破\n\n*   **零样本 (Zero-shot) 克隆的极致化：**\n    *   **XTTS-v2** 实现了仅需 **6 秒** 音频即可完成包含情感和风格迁移的跨语言克隆 [7, 8]。\n    *   **GPT-SoVITS v3/v4** 在不进行微调的情况下，其**音色相似度**显著提升，且模型稳定性更高，减少了语音重复和漏字现象 [9, 10]。\n*   **硬件效能优化 (V2Pro)：**\n    *   **GPT-SoVITS V2Pro** 系列在 2025 年 6 月发布，旨在以 **V2 级别的硬件成本和速度**，实现超越 V4 的性能表现，解决了高性能模型显存占用过高的问题 [11, 12]。\n*   **交互式流式部署：**\n    *   XTTS 已实现与 **Mistral** 或 **Zephyr** 等大模型集成，支持**流式语音聊天**，这标志着 TTS 正从单纯的工具向交互式 AI 代理 (Agent) 演进 [13, 14]。\n\n### 3. 未解决的挑战\n\n*   **长文本生成的连贯性：** 即使是像 **Bark** 这样强大的生成式模型，其架构和上下文窗口仍主要针对 **13-14 秒** 的音频进行了优化，超长文本的自然过渡仍需复杂的技术手段（如 Notebook 处理技巧） [15, 16]。\n*   **情感控制的精细度：** 虽然 XTTS 支持情感迁移，但**增强型 TTS 情感控制**（如通过预训练 GPT 模型实现更丰富的表情）仍被列为开发者的高优先级待办事项 [17]。\n*   **跨设备质量一致性：** 在不同平台上（如 **macOS 的 GPU 训练**）生成的模型质量仍显著低于传统 NVIDIA 环境，导致开发者目前在 Mac 上被迫退回到 CPU 训练 [18]。\n\n### 4. 未来可能的突破点与发展方向\n\n*   **超大规模数据集扩展：** 训练数据集规模正计划从目前的 2k-5k 小时扩展至 **10k 小时及以上**，以追求更强的通用性 [17]。\n*   **非言语信息深度集成：** 继 Bark 之后，未来的突破点在于更自然地集成**呼吸声、犹豫感、甚至环境音**，使 TTS 输出不再仅仅是“完美的语音”，而是“真实的音频生成” [19-21]。\n*   **模型混合与蒸馏：** **模型融合 (Model Mix)** 和开发更小尺寸 (Tiny-sized) 但保持高性能的 TTS 模型将成为端侧部署的关键 [17]。\n*   **从文本到潜空间映射：** 探索将 SoVITS 的令牌输入改为 **GPT 词表的概率分布（Transformer Latent）**，以获取更深层的语义表达 [17]。\n\n**总结：** 2025-2026 年的 TTS 领域正处于从“模拟真人说话”向“全生成式音频艺术”的跨越期，**自回归架构**和**原生 48k 高保真**已成为新的行业标准。",
    "conversation_id": "86674cd6-e082-45ea-acd4-9e41134ebd11",
    "sources_used": [
      "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
      "62f3466b-587f-45a7-b032-540895b3f1c5",
      "bab69d19-3140-457c-a75a-12b45648b450",
      "390b1831-3526-4bdb-8e81-8cdf46daf14e",
      "3e1586be-d28d-4c1f-b308-124ac3ed7669"
    ],
    "citations": {
      "1": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
      "2": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
      "3": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
      "4": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "5": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
      "6": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "7": "bab69d19-3140-457c-a75a-12b45648b450",
      "8": "bab69d19-3140-457c-a75a-12b45648b450",
      "9": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "10": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "11": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "12": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "13": "390b1831-3526-4bdb-8e81-8cdf46daf14e",
      "14": "bab69d19-3140-457c-a75a-12b45648b450",
      "15": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "16": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "17": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "18": "62f3466b-587f-45a7-b032-540895b3f1c5",
      "19": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "20": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
      "21": "3e1586be-d28d-4c1f-b308-124ac3ed7669"
    },
    "references": [
      {
        "source_id": "749c8a26-7b6e-437b-81e7-4fd7e8b26639",
        "citation_number": 1,
        "cited_text": "Search code, repositories, users, issues, pull requests... Clear Search syntax tips Provide feedback We read every piece of feedback, and take your input very seriously. Saved searches Use saved searches to filter your results more quickly To see all available qualifiers, see our documentation . Sign in Sign up Appearance settings   You signed in with another tab or window. Reload to refresh your session.   You signed out in another tab or window. Reload to refresh your session.   You switched accounts on another tab or window. Reload to refresh your session.   Dismiss alert   {{ message }}    This repository was archived by the owner on Nov 21, 2025. It is now read-only. Plachtaa / VITS-fast-fine-tuning Public archive"
      },
      {
        "source_id": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
        "citation_number": 2,
        "cited_text": "Bert-VITS2 VITS2 Backbone with multilingual bert For quick guide, please refer to  webui_preprocess.py . 简易教程请参见  webui_preprocess.py 。 【项目推介】 FishAudio下的全新自回归TTS Fish-Speech 现已可用，效果为目前开源SOTA水准，且在持续维护，推荐使用该项目作为BV2/GSV的替代。本项目短期内不再进行维护。 Demo Video: https://www.bilibili.com/video/BV18E421371Q Tech slides Video: https://www.bilibili.com/video/BV1zJ4m1K7cj 请注意，本项目核心思路来源于 anyvoiceai/MassTTS 一个非常好的tts项目 MassTTS的演示demo为 ai版峰哥锐评峰哥本人,并找回了在金三角失落的腰子 成熟的旅行者/开拓者/舰长/博士/sensei/猎魔人/喵喵露/V应当参阅代码自己学习如何训练。 严禁将此项目用于一切违反《中华人民共和国宪法》，《中华人民共和国刑法》，《中华人民共和国治安管理处罚法》和《中华人民共和国民法典》之用途。"
      },
      {
        "source_id": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
        "citation_number": 3,
        "cited_text": "严禁用于任何政治相关用途。 Video: https://www.bilibili.com/video/BV1hp4y1K78E Demo: https://www.bilibili.com/video/BV1TF411k78w References anyvoiceai/MassTTS jaywalnut310/vits p0p4k/vits2_pytorch svc-develop-team/so-vits-svc PaddlePaddle/PaddleSpeech emotional-vits fish-speech Bert-VITS2-UI 感谢所有贡献者作出的努力 About vits2 backbone with multilingual-bert Topics agent fish tts bert vocoder vits llm vits2 bert-vits bert-vits2 fish-speech Resources Readme License AGPL-3.0 license Uh oh! There was an error while loading. Please reload this page ."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 4,
        "cited_text": "ar-vits SoundStorm vits TransferTTS contentvec hifi-gan fish-speech f5-TTS shortcut flow matching Pretrained Models Chinese Speech Pretrain Chinese-Roberta-WWM-Ext-Large BigVGAN eresnetv2 Text Frontend for Inference paddlespeech zh_normalization split-lang g2pW pypinyin-g2pW paddlespeech g2pw WebUI Tools ultimatevocalremovergui audio-slicer SubFix FFmpeg gradio faster-whisper FunASR AP-BWE Thankful to @Naozumi520 for providing the Cantonese training set and for the guidance on Cantonese-related knowledge."
      },
      {
        "source_id": "dfdfcb84-b50d-4200-8c8a-118595cc5f04",
        "citation_number": 5,
        "cited_text": "Skip to content Navigation Menu Sign in Appearance settings AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 6,
        "cited_text": "V4 Release Notes New Features: Version 4 fixes the issue of metallic artifacts in Version 3 caused by non-integer multiple upsampling, and natively outputs 48k audio to prevent muffled sound (whereas Version 3 only natively outputs 24k audio). The author considers Version 4 a direct replacement for Version 3, though further testing is still needed. more details Use v4 from v1/v2/v3 environment: pip install -r requirements.txt  to update some packages Clone the latest codes from github. Download v4 pretrained models (gsv-v4-pretrained/s2v4.pth, and gsv-v4-pretrained/vocoder.pth) from huggingface and put them into  GPT_SoVITS/pretrained_models ."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 7,
        "cited_text": "Hugging Face Log In Sign Up coqui / XTTS-v2 Coqui.ai Text-to-Speech coqui Model card Files   Files and versions   xet Community   143 Configuration Parsing Warning: Invalid JSON for config file config.json ⓍTTS ⓍTTS is a Voice generation model that lets you clone voices into different languages by using just a quick 6-second audio clip. There is no need for an excessive amount of training data that spans countless hours. This is the same or similar model to what powers Coqui Studio and Coqui API ."
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 8,
        "cited_text": "Features Supports 17 languages. Voice cloning with just a 6-second audio clip. Emotion and style transfer by cloning. Cross-language voice cloning. Multi-lingual speech generation. 24khz sampling rate. Updates over XTTS-v1 2 new languages; Hungarian and Korean Architectural improvements for speaker conditioning. Enables the use of multiple speaker references and interpolation between speakers. Stability improvements. Better prosody and audio quality across the board. Languages XTTS-v2 supports 17 languages: English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi) ."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 9,
        "cited_text": "more details Use v2 from v1 environment: pip install -r requirements.txt  to update some packages Clone the latest codes from github. Download v2 pretrained models from huggingface and put them into  GPT_SoVITS/pretrained_models/gsv-v2final-pretrained . Chinese v2 additional: G2PWModel.zip(HF) | G2PWModel.zip(ModelScope) (Download G2PW models, unzip and rename to  G2PWModel , and then place them in  GPT_SoVITS/text .) V3 Release Notes New Features: The timbre similarity is higher, requiring less training data to approximate the target speaker (the timbre similarity is significantly improved using the base model directly without fine-tuning)."
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 10,
        "cited_text": "GPT model is more stable, with fewer repetitions and omissions, and it is easier to generate speech with richer emotional expression. more details Use v3 from v2 environment: pip install -r requirements.txt  to update some packages Clone the latest codes from github. Download v3 pretrained models (s1v3.ckpt, s2Gv3.pth and models--nvidia--bigvgan_v2_24khz_100band_256x folder) from huggingface and put them into  GPT_SoVITS/pretrained_models . additional: for Audio Super Resolution model, you can read how to download"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 11,
        "cited_text": "V2Pro Release Notes New Features: Slightly higher VRAM usage than v2, surpassing v4's performance, with v2's hardware cost and speed. more details 2.v1/v2 and the v2Pro series share the same characteristics, while v3/v4 have similar features. For training sets with average audio quality, v1/v2/v2Pro can deliver decent results, but v3/v4 cannot. Additionally, the synthesized tone and timebre of v3/v4 lean more toward the reference audio rather than the overall training set. Use v2Pro from v1/v2/v3/v4 environment:"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 12,
        "cited_text": "Thanks to all contributors for their efforts About 1 min voice data can also be used to train a good TTS model! (few shot voice cloning) Topics text-to-speech tts voice-cloning vits voice-clone voice-cloneai Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page . Activity Stars 56.3k stars Watchers 267 watching Forks 6.2k forks Report repository Releases  4 20250606v2pro    Latest  Jun 6, 2025 + 3 releases Packages  0 Uh oh! There was an error while loading. Please reload this page ."
      },
      {
        "source_id": "390b1831-3526-4bdb-8e81-8cdf46daf14e",
        "citation_number": 13,
        "cited_text": "Hugging Face Log In Sign Up Coqui.ai company    Verified https://coqui.ai coqui_ai coqui-ai Activity Feed Request to join this org 989 AI & ML interests None defined yet. spaces   3 Runtime error  Featured   2.77k XTTS 🐸 Generate speech from text using a reference voice coqui   Jan 15, 2024 Paused  Featured   267 Coqui XTTS Voice Chat With Mistral or Zephyr 🐸 coqui   Nov 18, 2023 Runtime error  172 CoquiTTS (Official) 🐸 coqui   Sep 26, 2023 models   2 coqui/XTTS-v2 Text-to-Speech  •   Updated  Dec 11, 2023   •    6.27M   •    3.45k coqui/XTTS-v1"
      },
      {
        "source_id": "bab69d19-3140-457c-a75a-12b45648b450",
        "citation_number": 14,
        "cited_text": "Stay tuned as we continue to add support for more languages. If you have any language requests, feel free to reach out! Code The code-base supports inference and fine-tuning . Demo Spaces XTTS Space : You can see how model performs on supported languages, and try with your own reference or microphone input XTTS Voice Chat with Mistral or Zephyr : You can experience streaming voice chat with Mistral 7B Instruct or Zephyr 7B Beta 🐸💬 CoquiTTS coqui/TTS on Github 💼 Documentation ReadTheDocs 👩‍💻 Questions GitHub Discussions 🗯 Community Discord License"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 15,
        "cited_text": "Bark tries to match the tone, pitch, emotion and prosody of a given preset, but does not currently support custom voice cloning. The model also attempts to preserve music, ambient noise, etc. text_prompt   =   \"\"\"    I have a silky smooth voice, and today I will tell you about   the exercise regimen of the common sloth.   \"\"\"   audio_array   =   generate_audio ( text_prompt ,  history_prompt = \"v2/en_speaker_1\" )   sloth.webm 📃 Generating Longer Audio By default,  generate_audio  works well with around 13 seconds of spoken text. For an example of how to do long-form generation, see 👉 Notebook 👈"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 16,
        "cited_text": "Why is the output limited to ~13-14 seconds? Bark is a GPT-style model, and its architecture/context window is optimized to output generations with roughly this length. How much VRAM do I need? The full version of Bark requires around 12Gb of memory to hold everything on GPU at the same time. However, even smaller cards down to ~2Gb work with some additional settings. Simply add the following code snippet before your generation: import   os   os . environ [ \"SUNO_OFFLOAD_CPU\" ]  =   \"True\"   os . environ [ \"SUNO_USE_SMALL_MODELS\" ]  =   \"True\""
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 17,
        "cited_text": "pip install -r requirements.txt  to update some packages Clone the latest codes from github. Download v2Pro pretrained models (v2Pro/s2Dv2Pro.pth, v2Pro/s2Gv2Pro.pth, v2Pro/s2Dv2ProPlus.pth, v2Pro/s2Gv2ProPlus.pth, and sv/pretrained_eres2netv2w24s4ep4.ckpt) from huggingface and put them into  GPT_SoVITS/pretrained_models . Todo List High Priority: Localization in Japanese and English. User guide. Japanese and English dataset fine tune training. Features: Zero-shot voice conversion (5s) / few-shot voice conversion (1min). TTS speaking speed control. Enhanced TTS emotion control. Maybe use pretrained finetuned preset GPT models for better emotion. Experiment with changing SoVITS token inputs to probability distribution of GPT vocabs (transformer latent). Improve English and Japanese text frontend. Develop tiny and larger-sized TTS models. Colab scripts. Try expand training dataset (2k hours -> 10k hours). better sovits base model (enhanced audio quality) model mix"
      },
      {
        "source_id": "62f3466b-587f-45a7-b032-540895b3f1c5",
        "citation_number": 18,
        "cited_text": "Users in China can download the package here . Install the program by running the following commands: conda create  - n GPTSoVits python = 3.10  conda activate GPTSoVits pwsh  -F  install.ps1  -- Device  < CU126 | CU128 | CPU >   -- Source  < HF | HF - Mirror | ModelScope >  [ -- DownloadUVR5 ] Linux conda create -n GPTSoVits python=3.10 conda activate GPTSoVits bash install.sh --device  < CU126 | CU128 | ROCM | CPU >  --source  < HF | HF-Mirror | ModelScope >  [--download-uvr5] macOS Note: The models trained with GPUs on Macs result in significantly lower quality compared to those trained on other devices, so we are temporarily using CPUs instead."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 19,
        "cited_text": "Notice: Bark is Suno's open-source text-to-speech+ model. If you are looking for our text-to-music models, please visit us on our web page and join our community on Discord . 🐶 Bark 🔗 Examples • Suno Studio Waitlist • Updates • How to Use • Installation • FAQ Bark is a transformer-based text-to-audio model created by Suno . Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. The model can also produce nonverbal communications like laughing, sighing and crying. To support the research community, we are providing access to pretrained model checkpoints, which are ready for inference and available for commercial use."
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 20,
        "cited_text": "Below is a list of some known non-speech sounds, but we are finding more every day. Please let us know if you find patterns that work particularly well on Discord ! [laughter] [laughs] [sighs] [music] [gasps] [clears throat] —  or  ...  for hesitations ♪  for song lyrics CAPITALIZATION for emphasis of a word [MAN]  and  [WOMAN]  to bias Bark toward male and female speakers, respectively Supported Languages Language   Status   English (en)   ✅   German (de)   ✅   Spanish (es)   ✅   French (fr)   ✅   Hindi (hi)   ✅   Italian (it)   ✅   Japanese (ja)   ✅   Korean (ko)   ✅   Polish (pl)   ✅   Portuguese (pt)   ✅   Russian (ru)   ✅   Turkish (tr)   ✅   Chinese, simplified (zh)   ✅"
      },
      {
        "source_id": "3e1586be-d28d-4c1f-b308-124ac3ed7669",
        "citation_number": 21,
        "cited_text": "My generated audio sounds like a 1980s phone call. What's happening? Bark generates audio from scratch. It is not meant to create only high-fidelity, studio-quality speech. Rather, outputs could be anything from perfect speech to multiple people arguing at a baseball game recorded with bad microphones. About 🔊 Text-Prompted Generative Audio Model Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 39.1k stars Watchers"
      }
    ]
  }
}
