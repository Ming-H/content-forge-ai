# 知识库：神经音频编解码器：语音数字化的基础设施

生成时间: 2026-04-03 13:15
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "神经音频编解码器（Neural Audio Codecs）作为语音和音频数字化的核心基础设施，其技术架构正从传统的信号处理向基于深度学习的生成式架构演进。以下是基于来源内容的详细概述：\n\n### 一、 技术演进路线\n1.  **从单一压缩到语义-声学统一**：早期的神经编解码器如 **EnCodec** 主要关注高保真音频压缩 [1]。随后的演进方向（如 **SpeechTokenizer**）开始尝试将**语义信息（Semantic tokens）**与**声学信息（Acoustic tokens）**统一在同一个框架下，通过分层处理实现信息的解耦 [2, 3]。\n2.  **从时域建模到频域优化**：如 **Vocos** 所示，技术路线正从直接在时域建模波形，转向生成谱系数（Spectral coefficients）并结合逆傅里叶变换，以实现更快的推理速度和更高的合成质量 [4]。\n3.  **大语言模型（LLM）的离散化基石**：编解码器产出的离散标记（Tokens）已成为 **VALL-E**、**Bark** 和 **MusicGen** 等音频语言模型的核心输入，使其能够像处理文本一样处理音频 [5, 6]。\n\n### 二、 核心算法名称\n*   **RVQ (Residual Vector Quantization)**：残差向量量化，是几乎所有主流神经音频编解码器（EnCodec, DAC, SpeechTokenizer）实现高倍率压缩的核心算法 [2, 3, 7, 8]。\n*   **RVQGAN**：一种结合了生成对抗网络（GAN）的改进型 RVQ 架构，旨在通过对抗训练提升重构音频的逼真度 [7]。\n*   **MS-STFT Discriminator**：多尺度短时傅里叶变换判别器，用于在训练过程中捕捉不同尺度的频谱特征 [9]。\n*   **Snake Activation**：一种特殊的激活函数，被应用于某些高性能编解码器模型（如 SpeechTokenizer 的特定版本）以增强序列建模能力 [10, 11]。\n*   **DVAE (Discrete Variational Autoencoder)**：离散变分自编码器，常用于将连续音频信号编码为离散的隐变量 [12]。\n\n### 三、 主要架构模式\n*   **Encoder-Decoder（自编码器）架构**：这是最基础的模式。编码器将原始波形转换为压缩的潜在表示，经过量化层后，解码器负责将其重构回波形 [1-3]。\n*   **分层解耦模式（Hierarchical Disentanglement）**：以 **SpeechTokenizer** 为代表，利用 RVQ 的层级特性。其**第一层量化器（Quantizer）**捕捉语义信息，而剩余的层则捕捉音色、环境等声学细节 [2]。\n*   **多带宽/多尺度模式**：如 **EnCodec**，通过单一模型支持多种目标比特率（如 1.5, 3, 6, 12, 24 kbps），并提供因果（Causal）与非因果（Non-causal）两种架构以适应实时或非实时场景 [1, 9]。\n*   **模块化 Artisan 层**：在 ASR 等扩展应用中，通过替换 Transformer 的线性层为 **Artisan Layer**，实现多语言或多任务的自适应处理 [13, 14]。\n\n### 四、 关键技术指标\n*   **压缩率（Compression Factor）**：**Descript Audio Codec (DAC)** 实现了高达 **90倍** 的压缩比，能将 44.1kHz 的音频压缩至仅 **8 kbps** 而保持卓越保真度 [7, 15]。\n*   **比特率（Bitrate）**：常见的神经编解码器支持 **1.5 kbps 到 24 kbps** 的极低带宽传输 [9]。\n*   **采样率支持（Sampling Rates）**：主流模型已覆盖 **16kHz、24kHz、32kHz、44.1kHz 至 48kHz**，涵盖了从窄带语音到高保真立体声音乐的各种场景 [1, 6, 15]。\n*   **实时因子（RTF）**：例如 **ChatTTS** 在 4090 GPU 上生成的实时因子约为 **0.3**，体现了现代架构的高效推理能力 [16]。\n*   **保真度与伪影控制**：通过对抗训练最小化感知伪影，确保在极低带宽下仍具有极高的音频重建质量 [1, 15]。",
    "conversation_id": "5562ecf7-edc8-4f82-b295-2bc59caca5c3",
    "sources_used": [
      "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "af1e46df-4b1a-4450-9956-448602e4058b",
      "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "991304f6-07e9-4590-b3b7-a19eb3523975",
      "0044fd5e-16c9-4441-bcc3-2a21ed2917e3"
    ],
    "citations": {
      "1": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "2": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "3": "af1e46df-4b1a-4450-9956-448602e4058b",
      "4": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "5": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "6": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "7": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "8": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "9": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "10": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "11": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "12": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "13": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "14": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "15": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "16": "8686cc45-6701-4d28-8d44-6c8bf25c5609"
    },
    "references": [
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 1,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security EnCodec: High Fidelity Neural Audio Compression This is the code for the EnCodec neural codec presented in the High Fidelity Neural Audio Compression [abs] . paper. We provide our two multi-bandwidth models: A causal model operating at 24 kHz on monophonic audio trained on a variety of audio data. A non-causal model operating at 48 kHz on stereophonic audio trained on music-only data."
      },
      {
        "source_id": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
        "citation_number": 2,
        "cited_text": "Repository files navigation README Apache-2.0 license SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models Introduction This is the code for the SpeechTokenizer presented in the SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models . SpeechTokenizer is a unified speech tokenizer for speech language models, which adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Specifically, the code indices that the first quantizer of RVQ outputs can be considered as semantic tokens and the output of the remaining quantizers mainly contain timbre info, which serve as supplements for the information lost by the first quantizer. We provide our models:"
      },
      {
        "source_id": "af1e46df-4b1a-4450-9956-448602e4058b",
        "citation_number": 3,
        "cited_text": "Computer Science > Computation and Language arXiv:2308.16692 (cs) [Submitted on 31 Aug 2023 ( v1 ), last revised 23 Jan 2024 (this version, v2)] Title: SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models Authors: Xin Zhang , Dong Zhang , Shimin Li , Yaqian Zhou , Xipeng Qiu View a PDF of the paper titled SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models, by Xin Zhang and 4 other authors View PDF HTML (experimental) Abstract: Current speech large language models build upon discrete speech representations, which can be categorized into semantic tokens and acoustic tokens. However, existing speech tokens are not specifically designed for speech language modeling. To assess the suitability of speech tokens for building speech language models, we established the first benchmark, SLMTokBench. Our results indicate that neither semantic nor acoustic tokens are ideal for this purpose. Therefore, we propose SpeechTokenizer, a unified speech tokenizer for speech large language models. SpeechTokenizer adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Furthermore, We construct a Unified Speech Language Model (USLM) leveraging SpeechTokenizer. Experiments show that SpeechTokenizer performs comparably to EnCodec in speech reconstruction and demonstrates strong performance on the SLMTokBench benchmark. Also, USLM outperforms VALL-E in zero-shot Text-to-Speech tasks. Code and models are available at this https URL ."
      },
      {
        "source_id": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
        "citation_number": 4,
        "cited_text": "Repository files navigation README MIT license Vocos: Closing the gap between time-domain and Fourier-based neural vocoders for high-quality audio synthesis Audio samples | Paper [abs] [pdf] Vocos is a fast neural vocoder designed to synthesize audio waveforms from acoustic features. Trained using a Generative Adversarial Network (GAN) objective, Vocos can generate waveforms in a single forward pass. Unlike other typical GAN-based vocoders, Vocos does not model audio samples in the time domain. Instead, it generates spectral coefficients, facilitating rapid audio reconstruction through inverse Fourier transform."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 5,
        "cited_text": "Acknowledgements bark , XTTSv2 and valle demonstrate a remarkable TTS result by an autoregressive-style system. fish-speech reveals capability of GVQ as audio tokenizer for LLM modeling. vocos which is used as a pretrained vocoder. Special Appreciation wlu-audio lab for early algorithm experiments. Thanks to all contributors for their efforts About A generative speech model for daily dialogue. 2noise.com Topics python chat agent text-to-speech torch tts english chinese gpt natural-language-inference english-language chinese-language torchaudio llm chatgpt llm-agent chattts"
      },
      {
        "source_id": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
        "citation_number": 6,
        "cited_text": "JadeCopet Update MusicGen citation 3 years ago 62201d6 · 3 years ago History History Open commit details History 419 lines (304 loc) · 18.9 KB main Breadcrumbs audiocraft / docs / MUSICGEN.md Top File metadata and controls Preview Code Blame 419 lines (304 loc) · 18.9 KB Raw Copy raw file Download raw file Outline Edit and raw actions MusicGen: Simple and Controllable Music Generation AudioCraft provides the code and models for MusicGen, a simple and controllable model for music generation . MusicGen is a single stage auto-regressive Transformer model trained over a 32kHz EnCodec tokenizer with 4 codebooks sampled at 50 Hz. Unlike existing methods like MusicLM , MusicGen doesn't require a self-supervised semantic representation, and it generates all 4 codebooks in one pass. By introducing a small delay between the codebooks, we show we can predict them in parallel, thus having only 50 auto-regressive steps per second of audio. Check out our sample page or test the available demo!"
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 7,
        "cited_text": "Repository files navigation README MIT license Descript Audio Codec (.dac): High-Fidelity Audio Compression with Improved RVQGAN This repository contains training and inference scripts for the Descript Audio Codec (.dac), a high fidelity general neural audio codec, introduced in the paper titled High-Fidelity Audio Compression with Improved RVQGAN . arXiv Paper: High-Fidelity Audio Compression with Improved RVQGAN 📈 Demo Site ⚙ Model Weights 👉 With Descript Audio Codec, you can compress 44.1 KHz audio into discrete codes at a low 8 kbps bitrate ."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 8,
        "cited_text": "Bad interactions between DistributedDataParallel and the RVQ code We do not use DDP, instead we recommend using the routines in encodec/distrib.py , in particular encodec.distrib.sync_buffer and encodec.distrib.sync_grad . Citation If you use this code or results in your paper, please cite our work as: License The code in this repository is released under the MIT license as found in the LICENSE file. About State-of-the-art deep learning based audio codec supporting both mono 24 kHz audio and stereo 48 kHz audio."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 9,
        "cited_text": "The 24 kHz model can compress to 1.5, 3, 6, 12 or 24 kbps, while the 48 kHz model support 3, 6, 12 and 24 kbps. We also provide a pre-trained language model for each of the models, that can further compress the representation by up to 40% without any further loss of quality. For reference, we also provide the code for our novel MS-STFT discriminator and the balancer . Samples Samples including baselines are provided on our sample page . You can also have a quick demo of what we achieve for 48 kHz music with EnCodec, along with entropy coding, by clicking the thumbnail (original tracks provided by Lucille Crew and Voyageur I )."
      },
      {
        "source_id": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
        "citation_number": 10,
        "cited_text": "A model operated at 16khz on monophonic speech trained on Librispeech with average representation across all HuBERT layers as semantic teacher. A model with Snake activation operated at 16khz on monophonic speech trained on Librispeech and Common Voice with average representation across all HuBERT layers as semantic teacher. Overview The SpeechTokenizer framework. Welcome to try our SLMTokBench and we will also open source our USLM ! Qick Link Relase Samples Installation Model List Usage Train SpeechTokenizer Data Preprocess Train Quick Start Citation License"
      },
      {
        "source_id": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
        "citation_number": 11,
        "cited_text": "Model List <cited_table> Usage load model Extracting discrete representations Decoding discrete representations Train SpeechTokenizer In the following section, we describe how to train a SpeechTokenizer model by using our trainer. Data Preprocess To train the SpeechTokenizer, the first step is to extract semantic teacher representations from raw audio waveforms. We provide an example of how to extract HuBERT representations in scripts/hubert_rep_extract.sh . We explain the arguments in the following:",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Model",
              "Dataset",
              "Discription"
            ],
            [
              "speechtokenizer_hubert_avg",
              "LibriSpeech",
              "Adopt average representation across all HuBERT layers as semantic teacher"
            ],
            [
              "speechtokenizer_snake",
              "LibriSpeech + Common Voice",
              "Snake activation, average representation across all HuBERT layers"
            ]
          ]
        }
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 12,
        "cited_text": "Dataset & Model Important The released model is for academic purposes only. The main model is trained with Chinese and English audio data of 100,000+ hours. The open-source version on HuggingFace is a 40,000 hours pre-trained model without SFT. Roadmap [x] Open-source the 40k-hours-base model and spk_stats file. [x] Streaming audio generation. [x] Open-source DVAE encoder and zero shot inferring code. [-] Multi-emotion controlling. [-] ChatTTS.cpp (new repo in 2noise org is welcomed) Licenses The Code"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 13,
        "cited_text": "Motivated by the observations above, we aim to investigate if we can leverage such similarities (i.e., modular similarity and linguistic similarity) to adaptively share certain parts of an ASR model across languages. Specifically, our hy-pothesis is that there is a potential to first construct a set of generalizable sub-modules and then select a different combination of these sub-modules for different languages. 3.3. Master-ASR: Overview Inspired by the aforementioned intriguing hypothesis, we de-velop our Master-ASR framework that can adaptively share certain sub-modules across different languages. As shown in Fig. 1, we replace the QKV and Projection layers in self-attention modules of a vanilla transformer with our pro-posed Artisan Layer (see Fig. 2 and Sec. 3.4). The purpose of the Artisan Layer is to learn shared weights across all the languages in the tuning dataset L, while allowing different"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 14,
        "cited_text": "3 Master-ASR : Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning A set of Specialist Scores Binary Mask Artisan QKV/Projection Weights (b) QKV/Projection Weights Artisan QKV/Projection Weights QKV/Projection Weights Binary Mask Learnable Params Frozen Params English Chinese Spanish (a) French Expanded Mapping Matrix Top-k Selection A set of Specialist Scores English Chinese Spanish Mapping Matrix Top-k Selection Figure 2. Block diagram of the proposed Artisan Layer and our proposed two-stage training pipeline: (a) Training Artisan Layer for scalable multilingual ASR, where we aim to learn (1) a mapping matrix T and (2) a set of Specialist Scores {Mk}(k ∈ [K]), where K = 4 in this example, and tune (3) the corresponding pretrained weights of the QKV or Projection layer; (b) Tuning Artisan Layer for low-resource ASR, where we aim to support a new language by only inserting and tuning a new row in the mapping matrix while freezing all other parameters in the Artisan Layer."
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 15,
        "cited_text": "🤌 That's approximately 90x compression while maintaining exceptional fidelity and minimizing artifacts. 💪 Our universal model works on all domains (speech, environment, music, etc.), making it widely applicable to generative modeling of all audio. 👌 It can be used as a drop-in replacement for EnCodec for all audio language modeling applications (such as AudioLMs, MusicLMs, MusicGen, etc.) Usage Installation OR Weights Weights are released as part of this repo under MIT license. We release weights for models that can natively support 16 kHz, 24kHz, and 44.1kHz sampling rates. Weights are automatically downloaded when you first run encode or decode command. You can cache them using one of the following commands"
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 16,
        "cited_text": "Quick Start Make sure you are under the project root directory when you execute these commands below. 1. Launch WebUI 2. Infer by Command Line It will save audio to ./output_audio_n.mp3 Installation Install the stable version from PyPI Install the latest version from GitHub Install from local directory in dev mode Basic Usage Advanced Usage Example: self introduction <cited_table> FAQ 1. How much VRAM do I need? How about infer speed? For a 30-second audio clip, at least 4GB of GPU memory is required. For the 4090 GPU, it can generate audio corresponding to approximately 7 semantic tokens per second. The Real-Time Factor (RTF) is around 0.3.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "male speaker",
              "female speaker"
            ],
            [
              "intro_en_m.webm",
              "intro_en_f.webm"
            ]
          ]
        }
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "神经音频编解码器作为语音数字化的基础设施，其核心在于将连续的音频波形转化为高度压缩的离散标记（Tokens），并在保证高保真度的前提下实现极低带宽传输。以下是基于来源的实现细节解析：\n\n### 一、 核心算法流程\n神经音频编解码器主要基于**自编码器（Encoder-Decoder）**架构，结合**残差向量量化（RVQ）**和**生成对抗网络（GAN）**技术 [1-3]。\n\n1.  **编码阶段 (Encoding)**：\n    *   **特征提取**：编码器通过多层卷积或 Transformer 结构将原始波形（如 44.1kHz 或 24kHz）映射到低维潜空间 [2, 3]。\n    *   **分层量化 (RVQ)**：核心算法 **RVQ (Residual Vector Quantization)** 将潜空间向量通过多个量化器进行逐级近似 [1, 2]。例如，**EnCodec** 支持 1.5 到 24 kbps 的多带宽量化，**DAC** 则能实现 **90倍** 的压缩率（将 44.1kHz 音频压缩至 **8 kbps**） [2, 4]。\n2.  **语义与声学解耦 (Disentanglement)**：\n    *   **SpeechTokenizer** 创新性地在 RVQ 层级上实现信息分离：其**第一层量化器**输出定义为**语义标记（Semantic tokens）**，其余层捕捉**音色和环境（Acoustic tokens）**，从而统一了语音建模的两个维度 [1, 5]。\n3.  **解码与重构 (Decoding/Synthesis)**：\n    *   **时域/频域重构**：传统解码器（如 EnCodec）在时域重建波形 [3]。而 **Vocos** 采用不同策略，不直接建模时间样本，而是生成**频谱系数（Spectral coefficients）**，通过**逆傅里叶变换（IFT）**快速重构音频，显著提升合成速度 [6]。\n\n### 二、 关键代码架构\n现代架构倾向于**模块化**和**可扩展性**设计：\n\n*   **Artisan Layer (工匠层)**：在 **Master-ASR** 框架中，传统的 QKV 或投影层被替换为 Artisan Layer [7, 8]。该层包含：\n    *   **Specialist Scores (专家得分)**：一组与权重形状相同的参数，可组合生成二进制掩码 [9, 10]。\n    *   **Mapping Matrix (映射矩阵)**：指导不同语言自适应地选择和组合子模块，实现多语言扩展 [10, 11]。\n*   **分阶段训练管线**：Master-ASR 采用两阶段训练。第一阶段通过操作学习率（$\\alpha=10$）和更新频率（$\\beta=5$）来训练映射矩阵 $T$，防止模式坍塌；第二阶段针对低资源语言进行微调 [12-14]。\n*   **端到端集成**：如 **ChatTTS** 整合了 DVAE 编码器和零样本推理代码，支持流式音频生成 [15, 16]。\n\n### 三、 性能优化策略\n1.  **推理加速**：\n    *   **并行预测**：**MusicGen** 通过在不同码本（Codebooks）之间引入微小延迟，实现并行预测，每秒音频仅需 50 个自回归步骤 [17]。\n    *   **频域转换**：Vocos 通过 IFT 代替复杂的时域卷积，在保持高保真度的同时大幅降低计算开销 [6]。\n2.  **计算效率与正则化**：\n    *   **稀疏化处理**：通过 **Top-K 选择策略** 生成二进制掩码。实验表明，当稀疏率 $t=0.3$ 时，能在推理效率与表达能力间取得最佳平衡 [18, 19]。\n    *   **参数共享**：Master-ASR 通过共享通用的子模块，使推理开销比现有 SOTA 方案降低了 **30%** [20, 21]。\n3.  **显存优化**：\n    *   **分片加载 (FSDP)**：在处理 1.5B 级别的大模型时，支持 FSDP 显存分片，以释放激活层所需的显存空间 [22]。\n\n### 四、 技术指标与竞品对比\n\n| 指标项目 | EnCodec [3, 4] | Descript Audio Codec (DAC) [2, 23] | Vocos [24] | Master-ASR [20, 25] |\n| :--- | :--- | :--- | :--- | :--- |\n| **压缩能力** | 1.5 - 24 kbps | **8 kbps (90x 压缩)** | N/A (Vocoder) | 比 SOTA 降低 30% 推理开销 |\n| **采样率支持** | 24kHz (单声道), 48kHz (立体声) | 16kHz, 24kHz, **44.1kHz** | 24kHz | 基于 16kHz/24kHz 预训练模型 |\n| **核心算法** | RVQ + MS-STFT 判别器 | 改进型 RVQGAN | 频域生成 + IFT | Artisan Layer + 模块化学习 |\n| **可扩展性** | 多带宽模型 | 通用模型（语音/音乐/环境） | 兼容 EnCodec tokens | **51+ 语言** 支持，低资源微调参数少 50 倍 |\n| **主要优势** | Meta 官方支持，Transformer 集成 | 极高压缩比下的保真度 | 极高的合成速度 | 卓越的多语言扩展与低资源适应性 |\n\n**具体数据支持**：\n*   **ChatTTS 推理性能**：在 4090 GPU 上，实时因子 (RTF) 约为 **0.3**，每秒可生成约 7 个语义标记 [26]。\n*   **微调效率**：Master-ASR 在进行低资源微调时，其可训练参数仅为 0.62M，比传统全量微调（301M）减少了近 **500倍**，且 CER（字符错误率）优于常规 Adapter 方法 [27, 28]。\n*   **模型规模**：Vocos-mel-24khz 模型参数量约为 **13.5M**，而 Vocos-encodec-24khz 仅为 **7.9M** [24]。",
    "conversation_id": "5562ecf7-edc8-4f82-b295-2bc59caca5c3",
    "sources_used": [
      "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "991304f6-07e9-4590-b3b7-a19eb3523975",
      "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "af1e46df-4b1a-4450-9956-448602e4058b",
      "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "57ce82e8-4ab3-41b1-af30-4ccc379f7edb"
    ],
    "citations": {
      "1": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "2": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "3": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "4": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "5": "af1e46df-4b1a-4450-9956-448602e4058b",
      "6": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "7": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "8": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "9": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "10": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "11": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "12": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "13": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "14": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "15": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "16": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "17": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "18": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "19": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "20": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "21": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "22": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "23": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "24": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "25": "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
      "26": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "27": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "28": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3"
    },
    "references": [
      {
        "source_id": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
        "citation_number": 1,
        "cited_text": "Repository files navigation README Apache-2.0 license SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models Introduction This is the code for the SpeechTokenizer presented in the SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models . SpeechTokenizer is a unified speech tokenizer for speech language models, which adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Specifically, the code indices that the first quantizer of RVQ outputs can be considered as semantic tokens and the output of the remaining quantizers mainly contain timbre info, which serve as supplements for the information lost by the first quantizer. We provide our models:"
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 2,
        "cited_text": "Repository files navigation README MIT license Descript Audio Codec (.dac): High-Fidelity Audio Compression with Improved RVQGAN This repository contains training and inference scripts for the Descript Audio Codec (.dac), a high fidelity general neural audio codec, introduced in the paper titled High-Fidelity Audio Compression with Improved RVQGAN . arXiv Paper: High-Fidelity Audio Compression with Improved RVQGAN 📈 Demo Site ⚙ Model Weights 👉 With Descript Audio Codec, you can compress 44.1 KHz audio into discrete codes at a low 8 kbps bitrate ."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 3,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security EnCodec: High Fidelity Neural Audio Compression This is the code for the EnCodec neural codec presented in the High Fidelity Neural Audio Compression [abs] . paper. We provide our two multi-bandwidth models: A causal model operating at 24 kHz on monophonic audio trained on a variety of audio data. A non-causal model operating at 48 kHz on stereophonic audio trained on music-only data."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 4,
        "cited_text": "The 24 kHz model can compress to 1.5, 3, 6, 12 or 24 kbps, while the 48 kHz model support 3, 6, 12 and 24 kbps. We also provide a pre-trained language model for each of the models, that can further compress the representation by up to 40% without any further loss of quality. For reference, we also provide the code for our novel MS-STFT discriminator and the balancer . Samples Samples including baselines are provided on our sample page . You can also have a quick demo of what we achieve for 48 kHz music with EnCodec, along with entropy coding, by clicking the thumbnail (original tracks provided by Lucille Crew and Voyageur I )."
      },
      {
        "source_id": "af1e46df-4b1a-4450-9956-448602e4058b",
        "citation_number": 5,
        "cited_text": "Computer Science > Computation and Language arXiv:2308.16692 (cs) [Submitted on 31 Aug 2023 ( v1 ), last revised 23 Jan 2024 (this version, v2)] Title: SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models Authors: Xin Zhang , Dong Zhang , Shimin Li , Yaqian Zhou , Xipeng Qiu View a PDF of the paper titled SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models, by Xin Zhang and 4 other authors View PDF HTML (experimental) Abstract: Current speech large language models build upon discrete speech representations, which can be categorized into semantic tokens and acoustic tokens. However, existing speech tokens are not specifically designed for speech language modeling. To assess the suitability of speech tokens for building speech language models, we established the first benchmark, SLMTokBench. Our results indicate that neither semantic nor acoustic tokens are ideal for this purpose. Therefore, we propose SpeechTokenizer, a unified speech tokenizer for speech large language models. SpeechTokenizer adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Furthermore, We construct a Unified Speech Language Model (USLM) leveraging SpeechTokenizer. Experiments show that SpeechTokenizer performs comparably to EnCodec in speech reconstruction and demonstrates strong performance on the SLMTokBench benchmark. Also, USLM outperforms VALL-E in zero-shot Text-to-Speech tasks. Code and models are available at this https URL ."
      },
      {
        "source_id": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
        "citation_number": 6,
        "cited_text": "Repository files navigation README MIT license Vocos: Closing the gap between time-domain and Fourier-based neural vocoders for high-quality audio synthesis Audio samples | Paper [abs] [pdf] Vocos is a fast neural vocoder designed to synthesize audio waveforms from acoustic features. Trained using a Generative Adversarial Network (GAN) objective, Vocos can generate waveforms in a single forward pass. Unlike other typical GAN-based vocoders, Vocos does not model audio samples in the time domain. Instead, it generates spectral coefficients, facilitating rapid audio reconstruction through inverse Fourier transform."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 7,
        "cited_text": "Motivated by the observations above, we aim to investigate if we can leverage such similarities (i.e., modular similarity and linguistic similarity) to adaptively share certain parts of an ASR model across languages. Specifically, our hy-pothesis is that there is a potential to first construct a set of generalizable sub-modules and then select a different combination of these sub-modules for different languages. 3.3. Master-ASR: Overview Inspired by the aforementioned intriguing hypothesis, we de-velop our Master-ASR framework that can adaptively share certain sub-modules across different languages. As shown in Fig. 1, we replace the QKV and Projection layers in self-attention modules of a vanilla transformer with our pro-posed Artisan Layer (see Fig. 2 and Sec. 3.4). The purpose of the Artisan Layer is to learn shared weights across all the languages in the tuning dataset L, while allowing different"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 8,
        "cited_text": "3 Master-ASR : Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning A set of Specialist Scores Binary Mask Artisan QKV/Projection Weights (b) QKV/Projection Weights Artisan QKV/Projection Weights QKV/Projection Weights Binary Mask Learnable Params Frozen Params English Chinese Spanish (a) French Expanded Mapping Matrix Top-k Selection A set of Specialist Scores English Chinese Spanish Mapping Matrix Top-k Selection Figure 2. Block diagram of the proposed Artisan Layer and our proposed two-stage training pipeline: (a) Training Artisan Layer for scalable multilingual ASR, where we aim to learn (1) a mapping matrix T and (2) a set of Specialist Scores {Mk}(k ∈ [K]), where K = 4 in this example, and tune (3) the corresponding pretrained weights of the QKV or Projection layer; (b) Tuning Artisan Layer for low-resource ASR, where we aim to support a new language by only inserting and tuning a new row in the mapping matrix while freezing all other parameters in the Artisan Layer."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 9,
        "cited_text": "3.4. Master-ASR: The Artisan Layer In this subsection, we introduce the key building block, the Artisan Layer, in Master-ASR. As discussed in Sec. 3.2, we aim to design the Artisan Layer to fulfill two criteria: (1) It incorporates efficient sub-modules capable of adapting the outputs of the designed ASR model to different languages; (2) It can share these sub-modules adaptively across differ- ent languages based on their characteristics. In particular, the above two criteria are implemented on top of a vanilla QKV or Projection layer. As shown in Fig. 2 (a), the Artisan Layer first uses a mapping matrix T to guide the adaptive summation of Specialist Scores to generate a distinct set of binary masks for different target languages. After that, Artisan Layer applies these generated binary masks to the pretrained weights of the corresponding QKV or Projection layer, adapting the model to different target languages."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 10,
        "cited_text": "Formally, the design of the Artisan Layer can be described as follows: Given a QKV or Projection layer with a weight tensor W ∈ Rcin×cout , where cin and cout are the num-ber of input and output channels, respectively, the Ar-tisan Layer introduces two additional components: (1) A set of K Specialist Scores with each Specialist Score Mk ∈ Rcin×cout(k ∈ [K]; K is a hyperparameter in Master-ASR); (2) A mapping matrix T ∈ RL×K , where the non-zero elements in T indicate which Specialist Scores to use for the corresponding target language in L. For a given language l, the Artisan Layer first generates the correspond-ing mask score Sl by summing over a selected subset of the Specialist Scores, i.e.,"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 11,
        "cited_text": "4 Master-ASR : Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning While the above objective in Eq. 4 can be optimized in an end-to-end manner, effectively training the Artisan Layer towards its maximum potential is still a non-trivial task. In particular, there are two challenges: (1) Collapse of T : A recent work shows that training a modular model with a mapping matrix can be problematic, as certain T ∈ T may collapse into a high entropy or non-sparse distribution (Ponti et al., 2022). This issue hinders the model from learning distinct features across different modules (e.g., Specialist Scores in Fig. 2), and thus, its capability to generate suffi-ciently different outputs for different languages; (2) Mask convergence: Recent works indicate that mask tuning re-quires a low-noise condition (Lai et al., 2021; Fu et al., 2022), thus making it difficult to learn an optimal set of masks when the mapping matrix T undergoes rapid changes during training. To tackle the two challenges above, Master-ASR integrates the following techniques."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 12,
        "cited_text": "languages to select different sub-modules. Specifically, each Artisan Layer consists of three sets of parameters: (1) The pretrained weights inherited from the corresponding original QKV and Projection layer; (2) A set of Specialist Scores, each of which is of the same shape as the corresponding pre-trained weights and can be adaptively combined to generate binary masks applied on top of the pretrained weights; (3) A language-Specialist Score mapping matrix, of which the non-zero elements indicate the Specialist Scores (i.e., the corresponding mask scores) for a target language. Further-more, to effectively train the above modules and matrices, Master-ASR integrates a two-stage training pipeline to (1) achieve multilingual ASR on dataset L, i.e., the multilingual scalability (see Fig. 2 (a) and Sec. 3.5) and then (2) tune the trained multilingual ASR model on the newly added low-resource language l′, i.e., the low-resource adaptation ability. In this way, Master-ASR enables the trained model to extend the learned languages from multilingual dataset L to the joint set L ∪ l′ with minimal training, inference, and storage overhead (see Fig. 2 (b) and Sec. 3.6)."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 13,
        "cited_text": "To tackle (1) collapse of T , we manipulate the learning rate and the update frequency of all elements in T . Specifically, we increase the learning rate of all T ∈ T to be larger than all other parameters in Master-ASR (see Fig. 2) by α times, and only update T ∈ T every β iterations while all the other parameters are updated in each iteration. With a higher learning rate for T , we aim to facilitate decisive selection of Specialist Scores during training, e.g., given a Specialist Score Mk and a target language l, σ(T [l, k]) ≈ 0 or σ(T [l, k]) ≈ 1. We empirically observe that doing so can avoid Master-ASR from frequently alternating between se-lecting and deselecting a specific Specialist Score for a given language in consecutive updates, as shown in Table 8. Such frequent switching could prevent the corresponding Spe-cialist Score from effectively learning a language-specific representation. On the other hand, the lower update fre-quency for T can enable the selected Specialist Scores to undergo several updates before updating T . Our observation is that it can increase the standard deviation of T , suggesting T can better determine the optimal selection of Specialist Scores for each language, as shown in Table 8."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 14,
        "cited_text": "Master-ASR 0.7x 0.57x 0.04x 16.31 23.53 10.14 10.67 15.98 10.84 15.49 11.08 20.54 25.52 14.24 without using a language model, such as a 4-gram language model (Heafield et al., 2013), to ensure a fair comparison. XLSR-53 is pretrained on 53 languages in an SSL manner. It is worth noting that the six-language low-resource tun-ing dataset we collected does not overlap with the dataset used for XLSR-53 pretraining or the collected 51-language multilingual dataset. Multilingual ASR training settings: We design our train-ing recipe following the training schedule used in Baevski et al. (2020). Specifically, we train models for 100k itera-tions on 36 GPUs using an Adam optimizer with an initial learning rate of 5e-5 and a tri-stage schedule for all modules except T . Unless stated otherwise, we set t = 0.3, α = 10, β = 5, and γ = 5, 000."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 15,
        "cited_text": "Dataset & Model Important The released model is for academic purposes only. The main model is trained with Chinese and English audio data of 100,000+ hours. The open-source version on HuggingFace is a 40,000 hours pre-trained model without SFT. Roadmap [x] Open-source the 40k-hours-base model and spk_stats file. [x] Streaming audio generation. [x] Open-source DVAE encoder and zero shot inferring code. [-] Multi-emotion controlling. [-] ChatTTS.cpp (new repo in 2noise org is welcomed) Licenses The Code"
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 16,
        "cited_text": "Acknowledgements bark , XTTSv2 and valle demonstrate a remarkable TTS result by an autoregressive-style system. fish-speech reveals capability of GVQ as audio tokenizer for LLM modeling. vocos which is used as a pretrained vocoder. Special Appreciation wlu-audio lab for early algorithm experiments. Thanks to all contributors for their efforts About A generative speech model for daily dialogue. 2noise.com Topics python chat agent text-to-speech torch tts english chinese gpt natural-language-inference english-language chinese-language torchaudio llm chatgpt llm-agent chattts"
      },
      {
        "source_id": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
        "citation_number": 17,
        "cited_text": "JadeCopet Update MusicGen citation 3 years ago 62201d6 · 3 years ago History History Open commit details History 419 lines (304 loc) · 18.9 KB main Breadcrumbs audiocraft / docs / MUSICGEN.md Top File metadata and controls Preview Code Blame 419 lines (304 loc) · 18.9 KB Raw Copy raw file Download raw file Outline Edit and raw actions MusicGen: Simple and Controllable Music Generation AudioCraft provides the code and models for MusicGen, a simple and controllable model for music generation . MusicGen is a single stage auto-regressive Transformer model trained over a 32kHz EnCodec tokenizer with 4 codebooks sampled at 50 Hz. Unlike existing methods like MusicLM , MusicGen doesn't require a self-supervised semantic representation, and it generates all 4 codebooks in one pass. By introducing a small delay between the codebooks, we show we can predict them in parallel, thus having only 50 auto-regressive steps per second of audio. Check out our sample page or test the available demo!"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 18,
        "cited_text": "Sl = K∑ k=1 Mk × 1σ(T [l,k])>0.5, (1) where 1f(.) is an indicator function conditioned on f(.) and σ(.) is the Sigmoid function. Then for a target language l, given a preset sparsity ratio t (e.g., t = 30%, which is a hyperparameter in Master-ASR), the corresponding binary mask Bl ∈ {0, 1}cin×cout is generated as follows. Bl = 1Sl>r, (2) where r is the ⌈(1− t)× cin × cout⌉-th largest element in Sl and ⌈.⌉ is the ceiling operator. Finally, the weight tensor Wl of the corresponding Artisan Layer is generated with"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 19,
        "cited_text": "4.6. Ablation Studies Ablate on sparsity ratio. The sparsity ratio t plays a criti-cal role in Master-ASR’s achievable performance. A higher value of t improves inference efficiency but may result in a larger gap in expressive power compared to a dense layer. On the other hand, a smaller value of t incurs higher in-ference overhead but better preserves the pretrained repre-sentation. To this end, we ablate on the impact of t on the achievable CER. As shown in Fig. 4 (a), we observe that the optimal t is around 0.3, which minimizes the CER across all languages. As compared to the observation in (Fu et al., 2022), where the optimal sparsity is around 0.1, we con-jecture that the increase in the optimal sparsity is because Master-ASR requires more diverse masks to encode general-izable features across different languages, thus necessitating a higher sparsity ratio."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 20,
        "cited_text": "Master-ASR: Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning Zhongzhi Yu 1 Yang Zhang 2 Kaizhi Qian 2 Yonggan Fu 1 Yingyan (Celine) Lin 1 Abstract Despite the impressive performance recently achieved by automatic speech recognition (ASR), we observe two primary challenges that hinder its broader applications: (1) The difficulty of intro-ducing scalability into the model to support more languages with limited training, inference, and storage overhead; (2) The low-resource adaptation ability that enables effective low-resource adapta-tion while avoiding over-fitting and catastrophic forgetting issues. Inspired by recent findings, we hypothesize that we can address the above chal-lenges with modules widely shared across lan-guages. To this end, we propose an ASR frame-work, dubbed Master-ASR, that, for the first time, simultaneously achieves strong multilingual scal-ability and low-resource adaptation ability thanks to its modularize-then-assemble strategy. Specifi-cally, Master-ASR learns a small set of generaliz-able sub-modules and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experi-ments and visualizations demonstrate that Master-ASR can effectively discover language similarity and improve multilingual and low-resource ASR performance over state-of-the-art (SOTA) meth-ods, e.g., under multilingual-ASR, our framework achieves a 0.13∼2.41 lower character error rate (CER) with 30% smaller inference overhead over SOTA solutions on multilingual ASR and a com-parable CER, with nearly 50 times fewer trainable parameters over SOTA solutions on low-resource tuning, respectively."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 21,
        "cited_text": "We propose an ASR framework, dubbed Master-ASR, which addresses the aforementioned bottleneck challenges in multilingual ASR through a modularize-then-assemble approach. Specifically, Master-ASR learns (1) a set of generalizable sub-modules, with each sub-module spe-cializing in a different sub-task; (2) an assembly strategy that maps each supported language to the corresponding generalizable sub-modules in an end-to-end manner. We propose an efficient and effective low-resource adap-tation approach in our Master-ASR framework by only learning a new reassembly strategy for pretrained sub-modules without changing the sub-modules themselves. This approach avoids the catastrophic forgetting issue by preserving the pretrained sub-modules during adaptation and avoids the over-fitting issue by reassembling the sub-modules, which enforces strong regularization. Extensive experiments and visualizations validate that Master-ASR can effectively alleviate the aforementioned bottleneck challenge in ASR. In particular, Master-ASR can discover language similarity and improve multilingual and low-resource ASR performance over state-of-the-art (SOTA) methods, e.g., a 0.13∼2.41 lower character er-ror rate (CER) with 30% less inference overhead over SOTA solutions on multilingual ASR and a comparable CER with nearly 50 times fewer trainable parameters over SOTA solutions on low-resource tuning, respectively."
      },
      {
        "source_id": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
        "citation_number": 22,
        "cited_text": "Now you can load your custom model with: Learn more Learn more about AudioCraft training pipelines in the dedicated section . FAQ I need help on Windows @FurkanGozukara made a complete tutorial for AudioCraft/MusicGen on Windows I need help for running the demo on Colab Check @camenduru tutorial on YouTube . What are top-k, top-p, temperature and classifier-free guidance? Check out @FurkanGozukara tutorial . Should I use FSDP or autocast ? The two are mutually exclusive (because FSDP does autocast on its own). You can use autocast up to 1.5B (medium), if you have enough RAM on your GPU. FSDP makes everything more complex but will free up some memory for the actual activations by sharding the optimizer state."
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 23,
        "cited_text": "🤌 That's approximately 90x compression while maintaining exceptional fidelity and minimizing artifacts. 💪 Our universal model works on all domains (speech, environment, music, etc.), making it widely applicable to generative modeling of all audio. 👌 It can be used as a drop-in replacement for EnCodec for all audio language modeling applications (such as AudioLMs, MusicLMs, MusicGen, etc.) Usage Installation OR Weights Weights are released as part of this repo under MIT license. We release weights for models that can natively support 16 kHz, 24kHz, and 44.1kHz sampling rates. Weights are automatically downloaded when you first run encode or decode command. You can cache them using one of the following commands"
      },
      {
        "source_id": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
        "citation_number": 24,
        "cited_text": "Integrate with 🐶 Bark text-to-audio model See example notebook . Pre-trained models <cited_table> Training Prepare a filelist of audio files for the training and validation set: Fill a config file, e.g. vocos.yaml , with your filelist paths and start training with: Refer to Pytorch Lightning documentation for details about customizing the training pipeline. Citation If this code contributes to your research, please cite our work:",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Model Name",
              "Dataset",
              "Training Iterations",
              "Parameters"
            ],
            [
              "charactr/vocos-mel-24khz",
              "LibriTTS",
              "1M",
              "13.5M"
            ],
            [
              "charactr/vocos-encodec-24khz",
              "DNS Challenge",
              "2M",
              "7.9M"
            ]
          ]
        }
      },
      {
        "source_id": "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
        "citation_number": 25,
        "cited_text": "View PDF Abstract: Despite the impressive performance recently achieved by automatic speech recognition (ASR), we observe two primary challenges that hinder its broader applications: (1) The difficulty of introducing scalability into the model to support more languages with limited training, inference, and storage overhead; (2) The low-resource adaptation ability that enables effective low-resource adaptation while avoiding over-fitting and catastrophic forgetting issues. Inspired by recent findings, we hypothesize that we can address the above challenges with modules widely shared across languages. To this end, we propose an ASR framework, dubbed \\METHODNS, that, \\textit{for the first time}, simultaneously achieves strong multilingual scalability and low-resource adaptation ability thanks to its modularize-then-assemble strategy. Specifically, \\METHOD learns a small set of generalizable sub-modules and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experiments and visualizations demonstrate that \\METHOD can effectively discover language similarity and improve multilingual and low-resource ASR performance over state-of-the-art (SOTA) methods, e.g., under multilingual-ASR, our framework achieves a 0.13\\sim 2.41 lower character error rate (CER) with 30% smaller inference overhead over SOTA solutions on multilingual ASR and a comparable CER, with nearly 50 times fewer trainable parameters over SOTA solutions on low-resource tuning, respectively."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 26,
        "cited_text": "Quick Start Make sure you are under the project root directory when you execute these commands below. 1. Launch WebUI 2. Infer by Command Line It will save audio to ./output_audio_n.mp3 Installation Install the stable version from PyPI Install the latest version from GitHub Install from local directory in dev mode Basic Usage Advanced Usage Example: self introduction <cited_table> FAQ 1. How much VRAM do I need? How about infer speed? For a 30-second audio clip, at least 4GB of GPU memory is required. For the 4090 GPU, it can generate audio corresponding to approximately 7 semantic tokens per second. The Real-Time Factor (RTF) is around 0.3.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "male speaker",
              "female speaker"
            ],
            [
              "intro_en_m.webm",
              "intro_en_f.webm"
            ]
          ]
        }
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 27,
        "cited_text": "Table 2. Benchmarking our Master-ASR on low-resource tuning with SOTA solutions. Each language is trained with only 10-min data. “Param.” indicates the number of trainable parameters. Method Param. sr gn ha pa or myv Avg. Weight Tuning 301M 29.37 22.14 31.05 25.28 30.17 28.35 27.52 Mask Tuning (Fu et al., 2022) 301M 25.14 20.31 27.62 22.83 26.72 25.99 24.77 Adapter Tuning (Le et al., 2021) 25M 26.37 21.16 28.74 23.69 27.52 27.31 25.80 Ours 0.62M 26.01 20.72 28.36 22.97 27.04 26.48 25.26 Ours + ft 301M 25.23 20.28 27.51 22.75 26.64 25.86 24.71"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 28,
        "cited_text": "6. Conclusion This work presents an ASR framework, dubbed Master-ASR. To the best of our knowledge, Master-ASR is the first that can simultaneously achieve strong multilingual scala-bility and low-resource adaptation ability in ASR thanks to its modularize-then-assemble strategy. Specifically, Master-ASR learns a set of generalizable Specialist Scores and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experiments consistently validate the effectiveness of Master-ASR in boosting the scalability and low-resource adaptation capa-bility of ASR models. For example, (1) in multilingual ASR, Master-ASR achieves a 0.13∼2.41 lower CER with 30% smaller inference overhead over SOTA ASR methods; (2) in low-resource tuning, Master-ASR achieves a comparable CER with nearly 50 times fewer trainable parameters over SOTA ASR methods."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「神经音频编解码器」（Neural Audio Codecs）作为现代语音数字化的底层基石，其应用已从简单的文件压缩扩展到生成式 AI 和大规模多语言交互。以下根据来源提供其真实应用场景、工业部署、性能数据及实战经验的详细分析：\n\n### 一、 真实应用场景与案例\n\n1.  **大语言模型（LLM）对话助手**：\n    *   **ChatTTS** 专门针对对话场景优化，作为 LLM 助手的后端，提供自然且富有表现力的语音合成 [1]。它支持**细粒度控制**，可在合成语音中插入笑声、停顿和语气词 [2]。\n2.  **生成式音频与音乐创作**：\n    *   **MusicGen** 利用 EnCodec 提取的离散 Token，在单阶段 Transformer 架构下实现了可控的音乐生成 [3]。\n    *   **Descript Audio Codec (DAC)** 可作为通用音频语言建模（如 AudioLMs、MusicGen）的即插即用替代方案 [4]。\n3.  **极低带宽通信与存储**：\n    *   **EnCodec** 和 **DAC** 被用于高保真音频压缩。例如，DAC 能将 **44.1kHz 音频**压缩至仅 **8kbps**，实现约 **90倍** 的压缩率，同时保持极高的保真度 [4, 5]。\n4.  **多语言自动语音识别 (ASR)**：\n    *   **Master-ASR** 采用模块化学习，通过共享子模块支持 **51 种以上语言**，并显著降低了在低资源语言上的适配成本 [6, 7]。\n5.  **商业级 API 服务**：\n    *   **ElevenLabs** 提供包括 TTS、语音转换（Voice Changer）和配音（Dubbing）在内的全套 API 服务，支持多种语言和专业级音频隔离 [8]。\n\n### 二、 工业级部署方案\n\n*   **容器化部署**：DAC 提供 **Dockerfile**，将默认模型权重缓存至镜像中，支持无网络环境下的 CPU/GPU 推理 [9, 10]。\n*   **库集成方案**：\n    *   **EnCodec** 和 **MusicGen** 已被集成进 **🤗 Transformers** 库，支持通过 Python 代码大规模调用 [11, 12]。\n    *   **ElevenLabs** 提供官方 Python 和 Node.js 绑定，通过 HTTP 或 Websocket 实现流式音频传输 [13]。\n*   **硬件优化方案**：ChatTTS 建议使用 **vLLM** (Linux) 或 NVIDIA GPU 上的加速工具（虽目前部分存在稳定性限制）[14, 15]。\n\n### 三、 性能基准数据\n\n| 维度 | 指标数据 | 来源 |\n| :--- | :--- | :--- |\n| **压缩性能** | DAC 在 8kbps 下实现 **90x 压缩率** | [4, 5] |\n| **推理效率** | ChatTTS 在 4090 GPU 上的 **实时因子 (RTF)** 约为 **0.3** | [16] |\n| **生成速度** | ChatTTS 每秒可生成约 **7 个语义标记 (Tokens)** | [16] |\n| **显存占用** | 30 秒音频至少需 **4GB 显存**；MusicGen 1.5B 模型建议 **16GB 显存** | [16, 17] |\n| **ASR 精度** | Master-ASR 比 SOTA 方案 CER 降低 **0.13~2.41**，推理开销减少 **30%** | [18, 19] |\n| **采样率支持** | 覆盖 16kHz, 24kHz, 32kHz, 44.1kHz, 48kHz | [3, 5, 20] |\n\n### 四、 开发者最佳实践\n\n1.  **分层解耦模型选择**：在构建语音语言模型时，推荐使用 **SpeechTokenizer**，因为它能将**语义（Semantic）**和**声学（Acoustic）**信息分层解耦，第一层量化器专门捕捉语义 [21, 22]。\n2.  **两阶段训练策略**：在多语言扩展时，参考 Master-ASR 的做法：第一阶段学习通用的“工匠层”（Artisan Layer）子模块，第二阶段仅针对新语言调整重组策略（映射矩阵），以避免**灾难性遗忘** [23, 24]。\n3.  **快速重构选择**：如果追求合成速度，建议使用 **Vocos** 作为声码器，它通过生成谱系数并应用**逆傅里叶变换 (IFT)**，比传统的时域 GAN 建模更快 [25, 26]。\n\n### 五、 常见踩坑经验与解决建议\n\n*   **长音频内存溢出 (OOM)**：EnCodec 等模型在处理长文件时可能一次性应用模型，导致大量显存占用而进程崩溃 [27]。\n    *   *建议*：采用 **分片推理 (Chunked inference)** [28]。\n*   **自回归模型不稳定性**：ChatTTS 等自回归系统常遇到多说话人混淆或音质突然下降的问题 [29]。\n    *   *建议*：尝试多次采样以筛选最佳结果 [29]。\n*   **分布式训练兼容性**：EnCodec 在使用 `DistributedDataParallel` 时存在潜在 bug。\n    *   *建议*：使用其自定义的 `encodec.distrib` 例程进行同步处理 [30]。\n*   **模型训练塌陷**：在训练带映射矩阵的模块化模型（如 Master-ASR）时，矩阵 $T$ 容易塌陷为非稀疏分布 [31]。\n    *   *建议*：显著**提高 $T$ 的学习率**（如其他参数的 10 倍），并**降低其更新频率**（如每 5 次迭代更新一次），以确保子模块能有效学习特定特征 [32]。\n*   **不成熟的加速库**：目前部分项目对 **FlashAttention-2** 或 **TransformerEngine** 的适配不完善，安装后可能反而导致速度变慢 [15]。",
    "conversation_id": "5562ecf7-edc8-4f82-b295-2bc59caca5c3",
    "sources_used": [
      "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "991304f6-07e9-4590-b3b7-a19eb3523975",
      "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
      "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "a2043b0a-f5ad-43e6-9c79-79f958543a53",
      "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "af1e46df-4b1a-4450-9956-448602e4058b",
      "1e89191e-6f28-4dac-8e18-fffa0a38cadc"
    ],
    "citations": {
      "1": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "2": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "3": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "4": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "5": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "6": "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
      "7": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "8": "a2043b0a-f5ad-43e6-9c79-79f958543a53",
      "9": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "10": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "11": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "12": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "13": "a2043b0a-f5ad-43e6-9c79-79f958543a53",
      "14": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "15": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "16": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "17": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "18": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "19": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "20": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "21": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "22": "af1e46df-4b1a-4450-9956-448602e4058b",
      "23": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "24": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "25": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "26": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "27": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "28": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "29": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "30": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "31": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "32": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3"
    },
    "references": [
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 1,
        "cited_text": "Repository files navigation README AGPL-3.0 license ChatTTS A generative speech model for daily dialogue. English | 简体中文 | 日本語 | Русский | Español | Français | 한국어 Introduction Note This repo contains the algorithm infrastructure and some simple examples. Tip For the extended end-user products, please refer to the index repo Awesome-ChatTTS maintained by the community. You can find a diagram visualization of the codebase here . ChatTTS is a text-to-speech model designed specifically for dialogue scenarios such as LLM assistant."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 2,
        "cited_text": "Supported Languages [x] English [x] Chinese [-] Coming Soon... Highlights You can refer to this video on Bilibili for the detailed description. Conversational TTS : ChatTTS is optimized for dialogue-based tasks, enabling natural and expressive speech synthesis. It supports multiple speakers, facilitating interactive conversations. Fine-grained Control : The model could predict and control fine-grained prosodic features, including laughter, pauses, and interjections. Better Prosody : ChatTTS surpasses most of open-source TTS models in terms of prosody. We provide pretrained models to support further research and development."
      },
      {
        "source_id": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
        "citation_number": 3,
        "cited_text": "JadeCopet Update MusicGen citation 3 years ago 62201d6 · 3 years ago History History Open commit details History 419 lines (304 loc) · 18.9 KB main Breadcrumbs audiocraft / docs / MUSICGEN.md Top File metadata and controls Preview Code Blame 419 lines (304 loc) · 18.9 KB Raw Copy raw file Download raw file Outline Edit and raw actions MusicGen: Simple and Controllable Music Generation AudioCraft provides the code and models for MusicGen, a simple and controllable model for music generation . MusicGen is a single stage auto-regressive Transformer model trained over a 32kHz EnCodec tokenizer with 4 codebooks sampled at 50 Hz. Unlike existing methods like MusicLM , MusicGen doesn't require a self-supervised semantic representation, and it generates all 4 codebooks in one pass. By introducing a small delay between the codebooks, we show we can predict them in parallel, thus having only 50 auto-regressive steps per second of audio. Check out our sample page or test the available demo!"
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 4,
        "cited_text": "🤌 That's approximately 90x compression while maintaining exceptional fidelity and minimizing artifacts. 💪 Our universal model works on all domains (speech, environment, music, etc.), making it widely applicable to generative modeling of all audio. 👌 It can be used as a drop-in replacement for EnCodec for all audio language modeling applications (such as AudioLMs, MusicLMs, MusicGen, etc.) Usage Installation OR Weights Weights are released as part of this repo under MIT license. We release weights for models that can natively support 16 kHz, 24kHz, and 44.1kHz sampling rates. Weights are automatically downloaded when you first run encode or decode command. You can cache them using one of the following commands"
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 5,
        "cited_text": "Repository files navigation README MIT license Descript Audio Codec (.dac): High-Fidelity Audio Compression with Improved RVQGAN This repository contains training and inference scripts for the Descript Audio Codec (.dac), a high fidelity general neural audio codec, introduced in the paper titled High-Fidelity Audio Compression with Improved RVQGAN . arXiv Paper: High-Fidelity Audio Compression with Improved RVQGAN 📈 Demo Site ⚙ Model Weights 👉 With Descript Audio Codec, you can compress 44.1 KHz audio into discrete codes at a low 8 kbps bitrate ."
      },
      {
        "source_id": "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
        "citation_number": 6,
        "cited_text": "View PDF Abstract: Despite the impressive performance recently achieved by automatic speech recognition (ASR), we observe two primary challenges that hinder its broader applications: (1) The difficulty of introducing scalability into the model to support more languages with limited training, inference, and storage overhead; (2) The low-resource adaptation ability that enables effective low-resource adaptation while avoiding over-fitting and catastrophic forgetting issues. Inspired by recent findings, we hypothesize that we can address the above challenges with modules widely shared across languages. To this end, we propose an ASR framework, dubbed \\METHODNS, that, \\textit{for the first time}, simultaneously achieves strong multilingual scalability and low-resource adaptation ability thanks to its modularize-then-assemble strategy. Specifically, \\METHOD learns a small set of generalizable sub-modules and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experiments and visualizations demonstrate that \\METHOD can effectively discover language similarity and improve multilingual and low-resource ASR performance over state-of-the-art (SOTA) methods, e.g., under multilingual-ASR, our framework achieves a 0.13\\sim 2.41 lower character error rate (CER) with 30% smaller inference overhead over SOTA solutions on multilingual ASR and a comparable CER, with nearly 50 times fewer trainable parameters over SOTA solutions on low-resource tuning, respectively."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 7,
        "cited_text": "and T ′ is the total set of extended mapping matrices. Given the training dataset D′ corresponding to language l′, we aim to optimize the following object in this stage, min T ′,W ′ cls ∑ (x,y)∈D′ J (f(x;W ∪ {W ′ cls}, T ′,M), y). (5) Thanks to our Artisan Layer design, the low resource tun-ing in Master-ASR (i.e., the optimization of Eq. 5) can be differentiably updated in an end-to-end manner. 4. Experiments 4.1. Experiment Settings Datasets and models: Datasets. We evaluate Master-ASR using a subset of the widely used large-scale CommonVoice dataset (Ardila et al., 2019). Specifically, this subset com-prises 51 languages, each of which contains one hour of training data and one hour of validation data, to train our multilingual ASR model as described in Sec. 3.5. Further-more, we collect an additional dataset consisting of six languages, with 10 minutes of training data and 10 minutes of validation data for each language, to evaluate the per-formance of low-resource tuning as discussed in Sec.3.6. Models. We implement Master-ASR and baseline meth-ods on a pretrained XLSR-53 (Conneau et al., 2020) model"
      },
      {
        "source_id": "a2043b0a-f5ad-43e6-9c79-79f958543a53",
        "citation_number": 8,
        "cited_text": "Introduction | ElevenLabs Documentation Scribe v2 is now available. Learn more about the model here . Search / Community Blog Help Center API Pricing Sign up Login Overview ElevenCreative ElevenAgents ElevenAPI API reference Changelog Login Overview ElevenCreative ElevenAgents ElevenAPI API reference Changelog API reference Introduction Authentication Streaming ElevenAgents Agents Conversations Users Tools Knowledge Base Tests Phone Numbers Widget Workspace SIP Trunk Twilio WhatsApp Batch Calling LLM MCP Analytics Environment Variables ElevenAPI Text to Speech Speech to Text Music Voices Text to Dialogue Voice Changer Voice Design Sound Effects Audio Isolation Dubbing Forced Alignment Pronunciation Dictionaries Audio Native ElevenCreative Studio Core Resources History Models Tokens Workspace Usage User Service Accounts Workspace Webhooks Legacy Voices Knowledge Base Dubbing"
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 9,
        "cited_text": "We provide a Dockerfile that installs all required dependencies for encoding and decoding. The build process caches the default model weights inside the image. This allows the image to be used without an internet connection. Please refer to instructions below. Compress audio This command will create .dac files with the same name as the input files. It will also preserve the directory structure relative to input root and re-create it in the output directory. Please use python -m dac encode --help for more options."
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 10,
        "cited_text": "Reconstruct audio from compressed codes This command will create .wav files with the same name as the input files. It will also preserve the directory structure relative to input root and re-create it in the output directory. Please use python -m dac decode --help for more options. Programmatic Usage Docker image We provide a dockerfile to build a docker image with all the necessary dependencies. Building the image. Using the image. Usage on CPU: Usage on GPU: <command> can be one of the compression and reconstruction commands listed above. For example, if you want to run compression,"
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 11,
        "cited_text": "🤗 Transformers Encodec has now been added to Transformers. For more information, please refer to Transformers' Encodec docs . You can find both the 24KHz and 48KHz checkpoints on the 🤗 Hub. Using 🤗 Transformers, you can leverage Encodec at scale along with all the other supported models and datasets. ⚡ Alternatively you can also directly use the encodec package, as detailed in the Usage section. To use first you'd need to set up your development environment! Then, start embedding your audio datasets at scale!"
      },
      {
        "source_id": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
        "citation_number": 12,
        "cited_text": "We observe the best trade-off between quality and compute with the facebook/musicgen-medium or facebook/musicgen-melody model. In order to use MusicGen locally you must have a GPU . We recommend 16GB of memory, but smaller GPUs will be able to generate short sequences, or longer sequences with the facebook/musicgen-small model. See after a quick example for using the API. 🤗 Transformers Usage MusicGen is available in the 🤗 Transformers library from version 4.31.0 onwards, requiring minimal dependencies and additional packages. Steps to get started:"
      },
      {
        "source_id": "a2043b0a-f5ad-43e6-9c79-79f958543a53",
        "citation_number": 13,
        "cited_text": "Community Blog Help Center API Pricing Sign up System On this page Installation Tracking generation costs API reference Introduction Copy page Explore the ElevenLabs API reference with comprehensive guides, code examples, and endpoint documentation Installation You can interact with the API through HTTP or Websocket requests from any language, via our official Python bindings or our official Node.js libraries. To install the official Python bindings, run the following command: To install the official Node.js library, run the following command in your Node.js project directory:"
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 14,
        "cited_text": "Contact GitHub issues/PRs are always welcomed. Formal Inquiries For formal inquiries about the model and roadmap, please contact us at open-source@2noise.com . Online Chat 1. QQ Group (Chinese Social APP) Group 1 , 808364215 Group 2 , 230696694 Group 3 , 933639842 Group 4 , 608667975 2. Discord Server Join by clicking here . Get Started Clone Repo Install requirements 1. Install Directly 2. Install from conda Optional: Install vLLM (Linux only) Unrecommended Optional: Install TransformerEngine if using NVIDIA GPU (Linux only)"
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 15,
        "cited_text": "Warning DO NOT INSTALL! The adaptation of TransformerEngine is currently under development and CANNOT run properly now. Only install it on developing purpose. See more details on at #672 #676 Note The installation process is very slow. Unrecommended Optional: Install FlashAttention-2 (mainly NVIDIA GPU) Warning DO NOT INSTALL! Currently the FlashAttention-2 will slow down the generating speed according to this issue . Only install it on developing purpose. Note See supported devices at the Hugging Face Doc ."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 16,
        "cited_text": "Quick Start Make sure you are under the project root directory when you execute these commands below. 1. Launch WebUI 2. Infer by Command Line It will save audio to ./output_audio_n.mp3 Installation Install the stable version from PyPI Install the latest version from GitHub Install from local directory in dev mode Basic Usage Advanced Usage Example: self introduction <cited_table> FAQ 1. How much VRAM do I need? How about infer speed? For a 30-second audio clip, at least 4GB of GPU memory is required. For the 4090 GPU, it can generate audio corresponding to approximately 7 semantic tokens per second. The Real-Time Factor (RTF) is around 0.3.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "male speaker",
              "female speaker"
            ],
            [
              "intro_en_m.webm",
              "intro_en_f.webm"
            ]
          ]
        }
      },
      {
        "source_id": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
        "citation_number": 17,
        "cited_text": "We use 20K hours of licensed music to train MusicGen. Specifically, we rely on an internal dataset of 10K high-quality music tracks, and on the ShutterStock and Pond5 music data. Model Card See the model card . Installation Please follow the AudioCraft installation instructions from the README . AudioCraft requires a GPU with at least 16 GB of memory for running inference with the medium-sized models (~1.5B parameters). Usage We offer a number of way to interact with MusicGen: A demo is also available on the facebook/MusicGen Hugging Face Space (huge thanks to all the HF team for their support). You can run the extended demo on a Colab: colab notebook You can use the gradio demo locally by running python -m demos.musicgen_app --share . You can play with MusicGen by running the jupyter notebook at demos/musicgen_demo.ipynb locally (if you have a GPU). Finally, checkout @camenduru Colab page which is regularly updated with contributions from @camenduru and the community."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 18,
        "cited_text": "Master-ASR: Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning Zhongzhi Yu 1 Yang Zhang 2 Kaizhi Qian 2 Yonggan Fu 1 Yingyan (Celine) Lin 1 Abstract Despite the impressive performance recently achieved by automatic speech recognition (ASR), we observe two primary challenges that hinder its broader applications: (1) The difficulty of intro-ducing scalability into the model to support more languages with limited training, inference, and storage overhead; (2) The low-resource adaptation ability that enables effective low-resource adapta-tion while avoiding over-fitting and catastrophic forgetting issues. Inspired by recent findings, we hypothesize that we can address the above chal-lenges with modules widely shared across lan-guages. To this end, we propose an ASR frame-work, dubbed Master-ASR, that, for the first time, simultaneously achieves strong multilingual scal-ability and low-resource adaptation ability thanks to its modularize-then-assemble strategy. Specifi-cally, Master-ASR learns a small set of generaliz-able sub-modules and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experi-ments and visualizations demonstrate that Master-ASR can effectively discover language similarity and improve multilingual and low-resource ASR performance over state-of-the-art (SOTA) meth-ods, e.g., under multilingual-ASR, our framework achieves a 0.13∼2.41 lower character error rate (CER) with 30% smaller inference overhead over SOTA solutions on multilingual ASR and a com-parable CER, with nearly 50 times fewer trainable parameters over SOTA solutions on low-resource tuning, respectively."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 19,
        "cited_text": "6. Conclusion This work presents an ASR framework, dubbed Master-ASR. To the best of our knowledge, Master-ASR is the first that can simultaneously achieve strong multilingual scala-bility and low-resource adaptation ability in ASR thanks to its modularize-then-assemble strategy. Specifically, Master-ASR learns a set of generalizable Specialist Scores and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experiments consistently validate the effectiveness of Master-ASR in boosting the scalability and low-resource adaptation capa-bility of ASR models. For example, (1) in multilingual ASR, Master-ASR achieves a 0.13∼2.41 lower CER with 30% smaller inference overhead over SOTA ASR methods; (2) in low-resource tuning, Master-ASR achieves a comparable CER with nearly 50 times fewer trainable parameters over SOTA ASR methods."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 20,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license Security EnCodec: High Fidelity Neural Audio Compression This is the code for the EnCodec neural codec presented in the High Fidelity Neural Audio Compression [abs] . paper. We provide our two multi-bandwidth models: A causal model operating at 24 kHz on monophonic audio trained on a variety of audio data. A non-causal model operating at 48 kHz on stereophonic audio trained on music-only data."
      },
      {
        "source_id": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
        "citation_number": 21,
        "cited_text": "Repository files navigation README Apache-2.0 license SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models Introduction This is the code for the SpeechTokenizer presented in the SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models . SpeechTokenizer is a unified speech tokenizer for speech language models, which adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Specifically, the code indices that the first quantizer of RVQ outputs can be considered as semantic tokens and the output of the remaining quantizers mainly contain timbre info, which serve as supplements for the information lost by the first quantizer. We provide our models:"
      },
      {
        "source_id": "af1e46df-4b1a-4450-9956-448602e4058b",
        "citation_number": 22,
        "cited_text": "Computer Science > Computation and Language arXiv:2308.16692 (cs) [Submitted on 31 Aug 2023 ( v1 ), last revised 23 Jan 2024 (this version, v2)] Title: SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models Authors: Xin Zhang , Dong Zhang , Shimin Li , Yaqian Zhou , Xipeng Qiu View a PDF of the paper titled SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models, by Xin Zhang and 4 other authors View PDF HTML (experimental) Abstract: Current speech large language models build upon discrete speech representations, which can be categorized into semantic tokens and acoustic tokens. However, existing speech tokens are not specifically designed for speech language modeling. To assess the suitability of speech tokens for building speech language models, we established the first benchmark, SLMTokBench. Our results indicate that neither semantic nor acoustic tokens are ideal for this purpose. Therefore, we propose SpeechTokenizer, a unified speech tokenizer for speech large language models. SpeechTokenizer adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Furthermore, We construct a Unified Speech Language Model (USLM) leveraging SpeechTokenizer. Experiments show that SpeechTokenizer performs comparably to EnCodec in speech reconstruction and demonstrates strong performance on the SLMTokBench benchmark. Also, USLM outperforms VALL-E in zero-shot Text-to-Speech tasks. Code and models are available at this https URL ."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 23,
        "cited_text": "languages to select different sub-modules. Specifically, each Artisan Layer consists of three sets of parameters: (1) The pretrained weights inherited from the corresponding original QKV and Projection layer; (2) A set of Specialist Scores, each of which is of the same shape as the corresponding pre-trained weights and can be adaptively combined to generate binary masks applied on top of the pretrained weights; (3) A language-Specialist Score mapping matrix, of which the non-zero elements indicate the Specialist Scores (i.e., the corresponding mask scores) for a target language. Further-more, to effectively train the above modules and matrices, Master-ASR integrates a two-stage training pipeline to (1) achieve multilingual ASR on dataset L, i.e., the multilingual scalability (see Fig. 2 (a) and Sec. 3.5) and then (2) tune the trained multilingual ASR model on the newly added low-resource language l′, i.e., the low-resource adaptation ability. In this way, Master-ASR enables the trained model to extend the learned languages from multilingual dataset L to the joint set L ∪ l′ with minimal training, inference, and storage overhead (see Fig. 2 (b) and Sec. 3.6)."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 24,
        "cited_text": "nate between updating W and M every γ iterations. This strategy can not only train M to produce effective binary masks for different languages, but also adjust W to better accommodate the binary masks generated by M, as shown in Table 9. 3.6. Master-ASR: Tuning on Low-resource Languages In this section, we elaborate on how to leverage the trained multilingual Master-ASR model above in a low-resource tuning scenario. As mentioned in Sec. 2.2, existing works need to either tune a full model (Baevski et al., 2020; Babu et al., 2021) or train language-specific modules from scratch (Fu et al., 2022; Hou et al., 2021) to support a new low-resource language l′. Both have been shown to eas-ily suffer from over-fitting and catastrophic forgetting is-sues (Hou et al., 2021; Cai et al., 2014; Winata et al., 2020; Kessler et al., 2021). In contrast, in Master-ASR, the learned Specialist Scores in each Artisan Layer (see Sec. 3.5) pro-vide a novel design knob to support l′. Specifically, this is achieved by learning a new combination of Specialist Scores in each Artisan Layer, i.e., inserting and optimizing an additional row in each mapping matrix T ∈ T ."
      },
      {
        "source_id": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
        "citation_number": 25,
        "cited_text": "Repository files navigation README MIT license Vocos: Closing the gap between time-domain and Fourier-based neural vocoders for high-quality audio synthesis Audio samples | Paper [abs] [pdf] Vocos is a fast neural vocoder designed to synthesize audio waveforms from acoustic features. Trained using a Generative Adversarial Network (GAN) objective, Vocos can generate waveforms in a single forward pass. Unlike other typical GAN-based vocoders, Vocos does not model audio samples in the time domain. Instead, it generates spectral coefficients, facilitating rapid audio reconstruction through inverse Fourier transform."
      },
      {
        "source_id": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
        "citation_number": 26,
        "cited_text": "Installation To use Vocos only in inference mode, install it using: If you wish to train the model, install it with additional dependencies: Usage Reconstruct audio from mel-spectrogram Copy-synthesis from a file: Reconstruct audio from EnCodec tokens Additionally, you need to provide a bandwidth_id which corresponds to the embedding for bandwidth from the list: [1.5, 3.0, 6.0, 12.0] . Copy-synthesis from a file: It extracts and quantizes features with EnCodec, then reconstructs them with Vocos in a single forward pass."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 27,
        "cited_text": "Installation for development This will install the dependencies and a encodec in developer mode (changes to the files will directly reflect), along with the dependencies to run unit tests. Test You can run the unit tests with FAQ Please check this section before opening an issue. Out of memory errors with long files We do not try to be smart about long files, and we apply the model at once on the entire file. This can lead to a large memory usage and result in the process being killed. At the moment we will not support this use case."
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 28,
        "cited_text": "descriptinc / descript-audio-codec Public Notifications You must be signed in to change notification settings Fork 176 Star 1.8k Code Issues 63 Pull requests 11 Security and quality 0 Insights Additional navigation options Code Issues Pull requests Security and quality Insights descriptinc/descript-audio-codec main 15 Branches 6 Tags Go to file Code Open more actions menu Folders and files <cited_table>",
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
              "assets",
              "",
              "assets",
              "add image assets",
              "3 years ago"
            ],
            [
              "conf",
              "",
              "conf",
              "Chunked inference for codec (",
              "3 years ago"
            ],
            [
              "dac",
              "",
              "dac",
              "Chunked inference for codec (",
              "3 years ago"
            ],
            [
              "scripts",
              "",
              "scripts",
              "Chunked inference for codec (",
              "3 years ago"
            ],
            [
              "tests",
              "",
              "tests",
              "Fix test + fix doc-string (",
              "3 years ago"
            ],
            [
              ".dockerignore",
              "",
              ".dockerignore",
              "Prepare code for public release",
              "3 years ago"
            ],
            [
              ".gitattributes",
              "",
              ".gitattributes",
              "Prepare code for public release",
              "3 years ago"
            ],
            [
              ".gitignore",
              "",
              ".gitignore",
              "Prepare for pypi release (",
              "3 years ago"
            ],
            [
              ".pre-commit-config.yaml",
              "",
              ".pre-commit-config.yaml",
              "Prepare code for public release",
              "3 years ago"
            ],
            [
              "Dockerfile",
              "",
              "Dockerfile",
              "Prepare code for public release",
              "3 years ago"
            ],
            [
              "Dockerfile.dev",
              "",
              "Dockerfile.dev",
              "Chunked inference for codec (",
              "3 years ago"
            ],
            [
              "LICENSE",
              "",
              "LICENSE",
              "Prepare code for public release",
              "3 years ago"
            ],
            [
              "README.md",
              "",
              "README.md",
              "Chunked inference for codec (",
              "3 years ago"
            ],
            [
              "docker-compose.yml",
              "",
              "docker-compose.yml",
              "Chunked inference for codec (",
              "3 years ago"
            ],
            [
              "requirements.txt",
              "",
              "requirements.txt",
              "Chunked inference for codec (",
              "3 years ago"
            ],
            [
              "setup.py",
              "",
              "setup.py",
              "Chunked inference for codec (",
              "3 years ago"
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
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 29,
        "cited_text": "2. Model stability is not good enough, with issues such as multi speakers or poor audio quality. This is a problem that typically occurs with autoregressive models (for bark and valle). It's generally difficult to avoid. One can try multiple samples to find a suitable result. 3. Besides laughter, can we control anything else? Can we control other emotions? In the current released model, the only token-level control units are [laugh] , [uv_break] , and [lbreak] . In future versions, we may open-source models with additional emotional control capabilities."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 30,
        "cited_text": "Bad interactions between DistributedDataParallel and the RVQ code We do not use DDP, instead we recommend using the routines in encodec/distrib.py , in particular encodec.distrib.sync_buffer and encodec.distrib.sync_grad . Citation If you use this code or results in your paper, please cite our work as: License The code in this repository is released under the MIT license as found in the LICENSE file. About State-of-the-art deep learning based audio codec supporting both mono 24 kHz audio and stereo 48 kHz audio."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 31,
        "cited_text": "4 Master-ASR : Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning While the above objective in Eq. 4 can be optimized in an end-to-end manner, effectively training the Artisan Layer towards its maximum potential is still a non-trivial task. In particular, there are two challenges: (1) Collapse of T : A recent work shows that training a modular model with a mapping matrix can be problematic, as certain T ∈ T may collapse into a high entropy or non-sparse distribution (Ponti et al., 2022). This issue hinders the model from learning distinct features across different modules (e.g., Specialist Scores in Fig. 2), and thus, its capability to generate suffi-ciently different outputs for different languages; (2) Mask convergence: Recent works indicate that mask tuning re-quires a low-noise condition (Lai et al., 2021; Fu et al., 2022), thus making it difficult to learn an optimal set of masks when the mapping matrix T undergoes rapid changes during training. To tackle the two challenges above, Master-ASR integrates the following techniques."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 32,
        "cited_text": "To tackle (1) collapse of T , we manipulate the learning rate and the update frequency of all elements in T . Specifically, we increase the learning rate of all T ∈ T to be larger than all other parameters in Master-ASR (see Fig. 2) by α times, and only update T ∈ T every β iterations while all the other parameters are updated in each iteration. With a higher learning rate for T , we aim to facilitate decisive selection of Specialist Scores during training, e.g., given a Specialist Score Mk and a target language l, σ(T [l, k]) ≈ 0 or σ(T [l, k]) ≈ 1. We empirically observe that doing so can avoid Master-ASR from frequently alternating between se-lecting and deselecting a specific Specialist Score for a given language in consecutive updates, as shown in Table 8. Such frequent switching could prevent the corresponding Spe-cialist Score from effectively learning a language-specific representation. On the other hand, the lower update fre-quency for T can enable the selected Specialist Scores to undergo several updates before updating T . Our observation is that it can increase the standard deviation of T , suggesting T can better determine the optimal selection of Specialist Scores for each language, as shown in Table 8."
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "基于提供的来源，以下是关于「神经音频编解码器：语音数字化的基础设施」领域的最新研究突破、技术趋势、挑战及未来方向的深度分析：\n\n### 一、 2025-2026年最新研究突破与技术趋势\n\n当前的神经音频编解码器正从单纯的“压缩工具”演变为“语音大模型的语义基础”。\n\n1.  **语义与声学信息的层级解耦（Unified Tokenization）**\n    *   **代表性论文/技术**：**SpeechTokenizer** (ICLR 2024) [1, 2]。\n    *   **突破点**：传统编解码器（如 EnCodec）产生的离散标记（Tokens）往往混杂了语义和声学特征 [1]。SpeechTokenizer 提出了一种**统一的解耦架构**，利用残差向量量化（RVQ）的分层特性：其**第一层量化器**输出语义标记（Semantic tokens），其余层补充音色、环境等声学信息（Acoustic tokens） [1, 3]。这使得大语言模型可以像处理文本一样，直接在语音编解码器的第一层进行建模 [1]。\n\n2.  **模块化学习与跨语言可扩展性（Modular Scalability）**\n    *   **代表性论文/技术**：**Master-ASR** (ICML 2023) [4, 5]。\n    *   **趋势**：为了支持全球数千种语言，研究方向正从“单一模型适配所有语言”转向“**模块化组装**” [4, 6]。Master-ASR 引入了 **Artisan Layer（工匠层）**，通过学习一小组通用的“专家得分（Specialist Scores）”并为不同语言生成映射矩阵，实现了极低成本的跨语言扩展 [7, 8]。\n\n3.  **极致压缩比与高保真度（High-Fidelity Compression）**\n    *   **代表性技术**：**Descript Audio Codec (DAC)** [9, 10]。\n    *   **突破点**：DAC 在 8 kbps 的极低比特率下实现了对 **44.1 kHz 音频**的 90 倍压缩，且重构音频几乎无损，成为 AudioLM 和 MusicGen 等生成式模型的新一代基础组件 [9-11]。\n\n4.  **从时域到频域的重构加速（Spectral-based Synthesis）**\n    *   **代表性技术**：**Vocos** [12]。\n    *   **趋势**：Vocos 摒弃了传统的时域建模，转而生成**频谱系数**并通过逆傅里叶变换（IFT）快速重构，显著提升了推理速度并解决了时域 GAN 建模的性能瓶颈 [12]。\n\n### 二、 未解决的挑战\n\n尽管技术进步显著，但在实际应用中仍面临核心难题：\n\n1.  **自回归模型的不稳定性**：如 **ChatTTS** 等基于编解码器的自回归生成系统，常面临多说话人混淆、音质突然下降或幻觉问题，这在生成式架构中极难完全避免 [13]。\n2.  **长音频处理的显存压力**：当前的编解码模型（如 EnCodec）在处理长音频文件时，往往需要一次性应用模型，导致显存占用极高，甚至引发 OOM（内存溢出）错误 [14]。\n3.  **低资源语言的泛化瓶颈**：尽管 Master-ASR 等方案减少了参数量，但在语言分布极度偏移（Distribution Shift）时，现有的通用模块仍难以捕捉到足够精准的特征 [15, 16]。\n4.  **实时性与复杂度的权衡**：在移动端或实时对话场景中，复杂的 RVQ 架构和多层 Transformer 的推理延迟仍是部署障碍 [17]。\n\n### 三、 未来可能的突破点\n\n1.  **引入对比学习增强特征泛化**：未来可能会将对比学习（Contrastive Learning）集成到编解码器的训练中，以生成更具代表性和鲁棒性的“专家模块”，提升对未见语言的适应能力 [15, 16]。\n2.  **基于先验知识的引导调整**：利用语言学定义的**语言家族（Language Families）**先验知识，指导编解码器的模块组装策略，有望在无需微调的情况下实现新语言的零样本支持 [16]。\n3.  **动态可扩展架构**：当目标语言与预训练数据存在显著差异时，模型能够**动态引入新的子模块**（New Specialist Scores），而非仅仅重组现有模块，以应对复杂的分布变化 [16]。\n4.  **细粒度的 prosody 控制集成**：未来的编解码器将不仅压缩波形，还会将笑声、语气、情感等**细粒度韵律特征**直接编码为可控的 Token，实现更自然的交互式语音合成 [13, 18]。\n\n**技术参数总结**：目前 SOTA 模型已实现每秒处理约 7 个语义标记（ChatTTS） [19]，在 4090 GPU 上的实时因子达到 0.3 左右 [19]，预示着编解码技术正向着更高效、更语义化的方向全速前进。",
    "conversation_id": "5562ecf7-edc8-4f82-b295-2bc59caca5c3",
    "sources_used": [
      "af1e46df-4b1a-4450-9956-448602e4058b",
      "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
      "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "991304f6-07e9-4590-b3b7-a19eb3523975",
      "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "be02e9a7-4bd9-4164-bb0f-9dea56be5142"
    ],
    "citations": {
      "1": "af1e46df-4b1a-4450-9956-448602e4058b",
      "2": "af1e46df-4b1a-4450-9956-448602e4058b",
      "3": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
      "4": "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
      "5": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "6": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "7": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "8": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "9": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "10": "991304f6-07e9-4590-b3b7-a19eb3523975",
      "11": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
      "12": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
      "13": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "14": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "15": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "16": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
      "17": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
      "18": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
      "19": "8686cc45-6701-4d28-8d44-6c8bf25c5609"
    },
    "references": [
      {
        "source_id": "af1e46df-4b1a-4450-9956-448602e4058b",
        "citation_number": 1,
        "cited_text": "Computer Science > Computation and Language arXiv:2308.16692 (cs) [Submitted on 31 Aug 2023 ( v1 ), last revised 23 Jan 2024 (this version, v2)] Title: SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models Authors: Xin Zhang , Dong Zhang , Shimin Li , Yaqian Zhou , Xipeng Qiu View a PDF of the paper titled SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models, by Xin Zhang and 4 other authors View PDF HTML (experimental) Abstract: Current speech large language models build upon discrete speech representations, which can be categorized into semantic tokens and acoustic tokens. However, existing speech tokens are not specifically designed for speech language modeling. To assess the suitability of speech tokens for building speech language models, we established the first benchmark, SLMTokBench. Our results indicate that neither semantic nor acoustic tokens are ideal for this purpose. Therefore, we propose SpeechTokenizer, a unified speech tokenizer for speech large language models. SpeechTokenizer adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Furthermore, We construct a Unified Speech Language Model (USLM) leveraging SpeechTokenizer. Experiments show that SpeechTokenizer performs comparably to EnCodec in speech reconstruction and demonstrates strong performance on the SLMTokBench benchmark. Also, USLM outperforms VALL-E in zero-shot Text-to-Speech tasks. Code and models are available at this https URL ."
      },
      {
        "source_id": "af1e46df-4b1a-4450-9956-448602e4058b",
        "citation_number": 2,
        "cited_text": "<cited_table> Submission history From: Dong Zhang [ view email ] [v1] Thu, 31 Aug 2023 12:53:09 UTC (1,912 KB) [v2] Tue, 23 Jan 2024 01:56:57 UTC (1,926 KB) Full-text links: Access Paper: View a PDF of the paper titled SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models, by Xin Zhang and 4 other authors",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Comments:",
              "Accepted by ICLR 2024. Project page is at"
            ],
            [
              "Subjects:",
              "Computation and Language (cs.CL); Sound (cs.SD); Audio and Speech Processing (eess.AS)"
            ],
            [
              "Cite as:",
              "arXiv:2308.16692"
            ],
            [
              "",
              "(or"
            ],
            [
              "",
              "https://doi.org/10.48550/arXiv.2308.16692"
            ]
          ]
        }
      },
      {
        "source_id": "689407d8-905a-4b85-b579-eb1a5bb6f30a",
        "citation_number": 3,
        "cited_text": "Repository files navigation README Apache-2.0 license SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models Introduction This is the code for the SpeechTokenizer presented in the SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models . SpeechTokenizer is a unified speech tokenizer for speech language models, which adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. Specifically, the code indices that the first quantizer of RVQ outputs can be considered as semantic tokens and the output of the remaining quantizers mainly contain timbre info, which serve as supplements for the information lost by the first quantizer. We provide our models:"
      },
      {
        "source_id": "57ce82e8-4ab3-41b1-af30-4ccc379f7edb",
        "citation_number": 4,
        "cited_text": "View PDF Abstract: Despite the impressive performance recently achieved by automatic speech recognition (ASR), we observe two primary challenges that hinder its broader applications: (1) The difficulty of introducing scalability into the model to support more languages with limited training, inference, and storage overhead; (2) The low-resource adaptation ability that enables effective low-resource adaptation while avoiding over-fitting and catastrophic forgetting issues. Inspired by recent findings, we hypothesize that we can address the above challenges with modules widely shared across languages. To this end, we propose an ASR framework, dubbed \\METHODNS, that, \\textit{for the first time}, simultaneously achieves strong multilingual scalability and low-resource adaptation ability thanks to its modularize-then-assemble strategy. Specifically, \\METHOD learns a small set of generalizable sub-modules and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experiments and visualizations demonstrate that \\METHOD can effectively discover language similarity and improve multilingual and low-resource ASR performance over state-of-the-art (SOTA) methods, e.g., under multilingual-ASR, our framework achieves a 0.13\\sim 2.41 lower character error rate (CER) with 30% smaller inference overhead over SOTA solutions on multilingual ASR and a comparable CER, with nearly 50 times fewer trainable parameters over SOTA solutions on low-resource tuning, respectively."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 5,
        "cited_text": "1. Introduction Recent breakthroughs in deep neural networks (DNNs) have significantly advanced the performance of automatic speech 1School of Computer Science, Georgia Institute of Technology, Atlanta, USA 2MIT-IBM Watson AI Lab, Boston, USA. Corre-spondence to: Yingyan (Celine) Lin <celine.lin@gatech.edu>. Proceedings of the 40 th International Conference on Machine Learning, Honolulu, Hawaii, USA. PMLR 202, 2023. Copyright 2023 by the author(s). recognition (ASR) in various applications under monolin-gual scenarios equipped with sufficient resources (i.e., suffi-cient labeled training data) (Hsu et al., 2021; Baevski et al., 2020; Ao et al., 2021; Babu et al., 2021; Conneau et al., 2020). However, how to achieve comparable performance under more practical situations where there are fewer re-sources available, and multiple target languages need to be simultaneously supported, still remains an open ques-tion (Babu et al., 2021; Yadav & Sitaram, 2022). Specifi-cally, there are two critical challenges: The multilingual scalability: An ideal ASR system should be able to support multiple languages, while avoiding excessive overhead in terms of the training, inference, or model storage cost when the number of supported languages increases (Yadav & Sitaram, 2022). To avoid the need for training completely different models for different lan-guages (Babu et al., 2021; Conneau et al., 2020), the major-ity of existing works either introduce an adapter-like module to adapt the pretrained model to different languages with fewer additional model parameters (Le et al., 2021; Hou et al., 2021; Fu et al., 2022), or use a much larger model with a dedicated training recipe to increase the model capac-ity and cater to more complex multilingual ASR tasks (Li et al., 2021; 2022; Pratap et al., 2020). However, these approaches either require the model to be tuned for each language separately, resulting in high training costs (Le et al., 2021; Hou et al., 2021; Fu et al., 2022), or result in a significant increase in inference cost due to the larger model size (Li et al., 2021; 2022; Pratap et al., 2020). The low-resource adaptation ability: Given the limited training data from low-resource languages (e.g., less than one hour per language as in (Fu et al., 2022)), effectively adapting the ASR model to target low-resource languages has been a long-lasting challenge in ASR. Existing attempts to address this challenge involve leveraging learned knowl-edge from pretrained models. In addition to directly tun-ing a pretrained model to low-resource languages (Hsu et al., 2021; Baevski et al., 2020; Conneau et al., 2020), techniques such as utilizing more data from other modali-ties (Zheng et al., 2021; Du et al., 2022; Liang et al., 2020), meta-learning (Hsu et al., 2020), and parameter-efficient tuning (Fu et al., 2022; Hou et al., 2021) are also used to further improve low-resource adaptation ability. However, how to better utilize the learned knowledge and avoid the issues of over-fitting (Hou et al., 2021; Cai et al., 2014) and"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 6,
        "cited_text": "2.3. Modular Models Modular models learn a set of modules and a mapping strategy during training. This enables them to flexibly adopt appropriate modules for different input data or target tasks (Kirsch et al., 2018; Ponti et al., 2022; Crawshaw, 2020; Pan & Rajan, 2020). For example, (Kirsch et al., 2018) proposes a training method to effectively train a large model consisting of multiple modules and adaptively select-ing different modules based on different given inputs and (Ponti et al., 2022) proposes a novel model architecture to learn a set of LoRA adapters (Hu et al., 2021) in a language model to simultaneously support multiple neural language processing tasks by adaptively selecting different combi-nations of LoRA adapters for different tasks. The merits of such models are two-fold: (1) They improve model ca-pacity without increasing inference cost; (2) They help to decompose difficult tasks into simple sub-tasks, alleviating the learning difficulty and thus improving the achievable task accuracy (Kirsch et al., 2018; Ponti et al., 2022). Mo-tivated by this, we hypothesize that such principles can be leveraged to improve both the multilingual scalability and low-resource adaptability of ASR systems. To the best of our knowledge, we are the first to explore the leveraging of the concept of modular models in designing scalable and data-efficient multilingual ASR models."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 7,
        "cited_text": "Master-ASR: Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning Zhongzhi Yu 1 Yang Zhang 2 Kaizhi Qian 2 Yonggan Fu 1 Yingyan (Celine) Lin 1 Abstract Despite the impressive performance recently achieved by automatic speech recognition (ASR), we observe two primary challenges that hinder its broader applications: (1) The difficulty of intro-ducing scalability into the model to support more languages with limited training, inference, and storage overhead; (2) The low-resource adaptation ability that enables effective low-resource adapta-tion while avoiding over-fitting and catastrophic forgetting issues. Inspired by recent findings, we hypothesize that we can address the above chal-lenges with modules widely shared across lan-guages. To this end, we propose an ASR frame-work, dubbed Master-ASR, that, for the first time, simultaneously achieves strong multilingual scal-ability and low-resource adaptation ability thanks to its modularize-then-assemble strategy. Specifi-cally, Master-ASR learns a small set of generaliz-able sub-modules and adaptively assembles them for different languages to reduce the multilingual overhead and enable effective knowledge transfer for low-resource adaptation. Extensive experi-ments and visualizations demonstrate that Master-ASR can effectively discover language similarity and improve multilingual and low-resource ASR performance over state-of-the-art (SOTA) meth-ods, e.g., under multilingual-ASR, our framework achieves a 0.13∼2.41 lower character error rate (CER) with 30% smaller inference overhead over SOTA solutions on multilingual ASR and a com-parable CER, with nearly 50 times fewer trainable parameters over SOTA solutions on low-resource tuning, respectively."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 8,
        "cited_text": "Formally, the design of the Artisan Layer can be described as follows: Given a QKV or Projection layer with a weight tensor W ∈ Rcin×cout , where cin and cout are the num-ber of input and output channels, respectively, the Ar-tisan Layer introduces two additional components: (1) A set of K Specialist Scores with each Specialist Score Mk ∈ Rcin×cout(k ∈ [K]; K is a hyperparameter in Master-ASR); (2) A mapping matrix T ∈ RL×K , where the non-zero elements in T indicate which Specialist Scores to use for the corresponding target language in L. For a given language l, the Artisan Layer first generates the correspond-ing mask score Sl by summing over a selected subset of the Specialist Scores, i.e.,"
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 9,
        "cited_text": "Repository files navigation README MIT license Descript Audio Codec (.dac): High-Fidelity Audio Compression with Improved RVQGAN This repository contains training and inference scripts for the Descript Audio Codec (.dac), a high fidelity general neural audio codec, introduced in the paper titled High-Fidelity Audio Compression with Improved RVQGAN . arXiv Paper: High-Fidelity Audio Compression with Improved RVQGAN 📈 Demo Site ⚙ Model Weights 👉 With Descript Audio Codec, you can compress 44.1 KHz audio into discrete codes at a low 8 kbps bitrate ."
      },
      {
        "source_id": "991304f6-07e9-4590-b3b7-a19eb3523975",
        "citation_number": 10,
        "cited_text": "🤌 That's approximately 90x compression while maintaining exceptional fidelity and minimizing artifacts. 💪 Our universal model works on all domains (speech, environment, music, etc.), making it widely applicable to generative modeling of all audio. 👌 It can be used as a drop-in replacement for EnCodec for all audio language modeling applications (such as AudioLMs, MusicLMs, MusicGen, etc.) Usage Installation OR Weights Weights are released as part of this repo under MIT license. We release weights for models that can natively support 16 kHz, 24kHz, and 44.1kHz sampling rates. Weights are automatically downloaded when you first run encode or decode command. You can cache them using one of the following commands"
      },
      {
        "source_id": "ee9623df-4cd5-4ff1-b308-0ad00aaedf4c",
        "citation_number": 11,
        "cited_text": "JadeCopet Update MusicGen citation 3 years ago 62201d6 · 3 years ago History History Open commit details History 419 lines (304 loc) · 18.9 KB main Breadcrumbs audiocraft / docs / MUSICGEN.md Top File metadata and controls Preview Code Blame 419 lines (304 loc) · 18.9 KB Raw Copy raw file Download raw file Outline Edit and raw actions MusicGen: Simple and Controllable Music Generation AudioCraft provides the code and models for MusicGen, a simple and controllable model for music generation . MusicGen is a single stage auto-regressive Transformer model trained over a 32kHz EnCodec tokenizer with 4 codebooks sampled at 50 Hz. Unlike existing methods like MusicLM , MusicGen doesn't require a self-supervised semantic representation, and it generates all 4 codebooks in one pass. By introducing a small delay between the codebooks, we show we can predict them in parallel, thus having only 50 auto-regressive steps per second of audio. Check out our sample page or test the available demo!"
      },
      {
        "source_id": "1e89191e-6f28-4dac-8e18-fffa0a38cadc",
        "citation_number": 12,
        "cited_text": "Repository files navigation README MIT license Vocos: Closing the gap between time-domain and Fourier-based neural vocoders for high-quality audio synthesis Audio samples | Paper [abs] [pdf] Vocos is a fast neural vocoder designed to synthesize audio waveforms from acoustic features. Trained using a Generative Adversarial Network (GAN) objective, Vocos can generate waveforms in a single forward pass. Unlike other typical GAN-based vocoders, Vocos does not model audio samples in the time domain. Instead, it generates spectral coefficients, facilitating rapid audio reconstruction through inverse Fourier transform."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 13,
        "cited_text": "2. Model stability is not good enough, with issues such as multi speakers or poor audio quality. This is a problem that typically occurs with autoregressive models (for bark and valle). It's generally difficult to avoid. One can try multiple samples to find a suitable result. 3. Besides laughter, can we control anything else? Can we control other emotions? In the current released model, the only token-level control units are [laugh] , [uv_break] , and [lbreak] . In future versions, we may open-source models with additional emotional control capabilities."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 14,
        "cited_text": "Installation for development This will install the dependencies and a encodec in developer mode (changes to the files will directly reflect), along with the dependencies to run unit tests. Test You can run the unit tests with FAQ Please check this section before opening an issue. Out of memory errors with long files We do not try to be smart about long files, and we apply the model at once on the entire file. This can lead to a large memory usage and result in the process being killed. At the moment we will not support this use case."
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 15,
        "cited_text": "5. Limitations and Future Directions Despite the promising performance achieved by our pro-posed Master-ASR, there are still several directions that can further improve Master-ASR’s multilingual and low-resource performance that are worth further exploration. Here, we list a few of them: Learning a set of more representative and general-izable Specialist Scores. While we observe promising performance on multilingual and low-resource ASR by Table 6. Ablate on the weight update strategy. Method Freeze Random Iter"
      },
      {
        "source_id": "0044fd5e-16c9-4441-bcc3-2a21ed2917e3",
        "citation_number": 16,
        "cited_text": "CER 18.47 14.41 14.24 simply learning a set of Specialist Scores in Master-ASR, these modules may not provide sufficiently gen-eralizable features for better tuning low-resource lan-guages. One potential solution is integrating tech-niques like contrastive learning to help Master-ASR learn a more generalizable set of Specialist Scores. Adaptively introducing new Specialist Scores dur-ing tuning. When the targeting low-resource language has a significant distribution shift with the training lan-guages, the commonly used generalizable Specialist Scores may not sufficiently fit the new distribution. Thus, adaptively introducing a new Specialist Score in the model to better accommodate the significant dis-tribution shift, in this case, may further improve the performance. Guide tuning with prior knowledge. Some existing works (Zhao et al., 2020; Li et al., 2020) show that using prior knowledge about languages can help the model to make better decisions. Master-ASR may also benefit from incorporating prior knowledge to guide the tuning process, especially under the low-resource scenario. Specifically, it is worth exploring whether human-defined language families can help to generate a combination strategy for Specialist Scores, even without the need to further tune the model."
      },
      {
        "source_id": "be02e9a7-4bd9-4164-bb0f-9dea56be5142",
        "citation_number": 17,
        "cited_text": "What's up? See the changelog for details on releases. Installation EnCodec requires Python 3.8, and a reasonably recent version of PyTorch (1.11.0 ideally). To install EnCodec, you can run from this repository: Supported platforms: we officially support only Mac OS X (you might need XCode installed if running on a non Intel Mac), and recent versions of mainstream Linux distributions. We will try to help out on Windows but cannot provide strong support. Any other platform (iOS / Android / onboard ARM) are not supported."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 18,
        "cited_text": "Supported Languages [x] English [x] Chinese [-] Coming Soon... Highlights You can refer to this video on Bilibili for the detailed description. Conversational TTS : ChatTTS is optimized for dialogue-based tasks, enabling natural and expressive speech synthesis. It supports multiple speakers, facilitating interactive conversations. Fine-grained Control : The model could predict and control fine-grained prosodic features, including laughter, pauses, and interjections. Better Prosody : ChatTTS surpasses most of open-source TTS models in terms of prosody. We provide pretrained models to support further research and development."
      },
      {
        "source_id": "8686cc45-6701-4d28-8d44-6c8bf25c5609",
        "citation_number": 19,
        "cited_text": "Quick Start Make sure you are under the project root directory when you execute these commands below. 1. Launch WebUI 2. Infer by Command Line It will save audio to ./output_audio_n.mp3 Installation Install the stable version from PyPI Install the latest version from GitHub Install from local directory in dev mode Basic Usage Advanced Usage Example: self introduction <cited_table> FAQ 1. How much VRAM do I need? How about infer speed? For a 30-second audio clip, at least 4GB of GPU memory is required. For the 4090 GPU, it can generate audio corresponding to approximately 7 semantic tokens per second. The Real-Time Factor (RTF) is around 0.3.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "male speaker",
              "female speaker"
            ],
            [
              "intro_en_m.webm",
              "intro_en_f.webm"
            ]
          ]
        }
      }
    ]
  }
}
