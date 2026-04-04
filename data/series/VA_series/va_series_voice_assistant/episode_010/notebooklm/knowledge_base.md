# 知识库：语音增强与降噪：嘈杂环境中的清晰对话

生成时间: 2026-04-03 15:58
查询轮数: 2

## 技术全景

{
  "value": {
    "answer": "根据所提供的资料，针对「语音增强与降噪：嘈杂环境中的清晰对话」这一主题，其核心技术架构、算法及演进路线概述如下：\n\n### 1. 技术演进路线\n语音增强技术经历了从传统方法到深度学习驱动的显著演进：\n*   **传统与基础深度学习阶段：** 早期采用**循环神经网络 (RNN)**（如 RNNoise [1, 2]）或简单的**频谱掩蔽 (Spectral Masking)** 方案 [3]。\n*   **低复杂度全频带框架：** 演进至支持 48kHz 全频带音频的低复杂度框架，如 **DeepFilterNet** 系列，其发展路径为：DeepFilterNet $\\rightarrow$ DeepFilterNet2（针对嵌入式设备优化） $\\rightarrow$ DeepFilterNet3（感知驱动的实时增强）[4, 5]。\n*   **端到端与模块化架构：** 出现了如 Asteroid 和 SpeechBrain 等工具包，支持从卷积时域模型（ConvTasNet）到双路径递归网络（DualPathRNN）的多种架构 [3, 6]。\n*   **多模态与个性化阶段：** 现代技术开始集成**个性化语音增强 (Personalized DNS)**、去混响以及针对特定说话人的提取技术（Target Speaker Extraction）[7, 8]。\n\n### 2. 核心算法名称\n资料中提及了多个代表性的核心算法：\n*   **基础与挑战赛基准：** **NSNet**（微软 DNS 挑战赛基准模型）[9]；**ECAPA-TDNN**（用于说话人嵌入/提取）[3, 10]。\n*   **高性能深度模型：** **FRCRN**（频率递归卷积递归网络，已在 ModelScope 上被广泛使用）[11, 12]；**MossFormer**（语音分离模型）[11, 12]；**SepFormer**（基于 Transformer 的增强模型）[3]。\n*   **其他关键算法：** **ConvTasNet**、**DCCRNet**、**DCUNet** [6]；**MetricGAN**（基于度量的对抗网络）和 **SEGAN**（语音增强生成对抗网络）[3]。\n\n### 3. 主要架构模式\n语音增强系统的架构通常遵循以下模式：\n*   **模块化构建块：** 包含 **滤波器组 (Filterbanks)**、**编码器 (Encoders)**、**分离器/掩蔽器 (Separators/Maskers)** 和 **解码器 (Decoders)** [13]。\n*   **域处理差异：**\n    *   **频域 (Frequency Domain)：** 处理频谱图，使用复数卷积或循环网络 [3, 12]。\n    *   **时域 (Time Domain)：** 直接对原始波形建模（如 TasNet 系列） [3, 6]。\n*   **部署模式：** 支持**云端/边缘容器化部署** [14] 或**设备端嵌入式 (Embedded Speech)** 处理，以应对网络不稳定的场景 [15, 16]。\n*   **硬件加速：** 利用特定的 GPU 性能（如 NVIDIA RTX 系列）进行 AI 降噪、回声消除和房间混响去除 [17, 18]。\n\n### 4. 关键技术组件\n*   **降噪与回声消除单元：** 专门用于消除键盘敲击声、风扇声和背景混响 [17, 19]。\n*   **说话人提取组件：** 通过参考语音、面部表情（唇语）或身体姿态等条件提取特定目标人的声音 [8]。\n*   **语音超分辨率/带宽扩展：** 将低分辨率音频（如 16kHz）转换为 48kHz 高清音频 [8, 11]。\n*   **口音转换与翻译：** 在增强语音的同时进行口音修正或实时语音转语音翻译 [19, 20]。\n\n### 5. 关键技术指标\n评估语音增强效果的主要指标包括：\n*   **客观评价指标：** \n    *   **PESQ**（语音质量知觉评估）[3, 21]。\n    *   **STOI**（短时客观可懂度）[21]。\n    *   **SNR**（信噪比）与 **SI-SDR**（尺度不变信号失真比）[21]。\n*   **主观与综合指标：** \n    *   **ITU-T P.835**：评估语音质量 (**SIG**)、背景噪声质量 (**BAK**) 和整体质量 (**OVRL**) [7, 22]。\n    *   **DNSMOS**：深度降噪平均意见得分 [9, 21]。\n*   **下游任务性能：** **词准确率 (WAcc)** 或单词错误率，用于衡量增强后音频对语音识别的影响 [7, 23]。\n*   **工程指标：** 处理**延迟 (Latency)**，确保实时通信需求 [7]。",
    "conversation_id": "93edd13d-32e9-467d-81ca-bf6b1f9a8045",
    "sources_used": [
      "c534c1bb-c4d6-44a5-aef5-e4e7fa3853fd",
      "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
      "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
      "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
      "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "d469b10c-9efc-4e9c-8e6d-cab16768e5ee",
      "7de04067-7886-4191-bee0-6da8e42f7a86",
      "b41cdd21-d04c-441e-b768-9543c9bbba07"
    ],
    "citations": {
      "1": "c534c1bb-c4d6-44a5-aef5-e4e7fa3853fd",
      "2": "c534c1bb-c4d6-44a5-aef5-e4e7fa3853fd",
      "3": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
      "4": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "5": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "6": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
      "7": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
      "8": "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "9": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
      "10": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
      "11": "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "12": "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "13": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
      "14": "d469b10c-9efc-4e9c-8e6d-cab16768e5ee",
      "15": "d469b10c-9efc-4e9c-8e6d-cab16768e5ee",
      "16": "d469b10c-9efc-4e9c-8e6d-cab16768e5ee",
      "17": "7de04067-7886-4191-bee0-6da8e42f7a86",
      "18": "7de04067-7886-4191-bee0-6da8e42f7a86",
      "19": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "20": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "21": "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "22": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
      "23": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119"
    },
    "references": [
      {
        "source_id": "c534c1bb-c4d6-44a5-aef5-e4e7fa3853fd",
        "citation_number": 1,
        "cited_text": "GitHub - xiph/rnnoise: Recurrent neural network for audio noise reduction · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "c534c1bb-c4d6-44a5-aef5-e4e7fa3853fd",
        "citation_number": 2,
        "cited_text": "Repository files navigation README BSD-3-Clause license About Recurrent neural network for audio noise reduction Topics audio c rnn noise-reduction Resources Readme License BSD-3-Clause license Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 5.5k stars Watchers 154 watching Forks 1k forks Report repository Releases 1 RNNoise 0.2 Latest on Apr 14, 2024 Packages 0 No packages published Uh oh! There was an error while loading. Please reload this page . Contributors 13 Languages"
      },
      {
        "source_id": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
        "citation_number": 3,
        "cited_text": "🔧 Supported Technologies SpeechBrain is a versatile framework designed for implementing a wide range of technologies within the field of Conversational AI. It excels not only in individual task implementations but also in combining various technologies into complex pipelines. 🎙 Speech/Audio Processing <cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Tasks",
              "Datasets",
              "Technologies/Models"
            ],
            [
              "Speech Recognition",
              "AISHELL-1",
              "CTC"
            ],
            [
              "Speaker Recognition",
              "VoxCeleb",
              "ECAPA-TDNN"
            ],
            [
              "Speech Separation",
              "WSJ0Mix",
              "SepFormer"
            ],
            [
              "Speech Enhancement",
              "DNS",
              "SepFormer"
            ],
            [
              "Interpretability",
              "ESC50",
              "Listenable Maps for Audio Classifiers (L-MAC)"
            ],
            [
              "Speech Generation",
              "AudioMNIST",
              "Diffusion"
            ],
            [
              "Text-to-Speech",
              "LJSpeech",
              "Tacotron2"
            ],
            [
              "Vocoding",
              "LJSpeech",
              "HiFiGAN"
            ],
            [
              "Spoken Language Understanding",
              "MEDIA",
              "Direct SLU"
            ],
            [
              "Speech-to-Speech Translation",
              "CVSS",
              "Discrete Hubert"
            ],
            [
              "Speech Translation",
              "Fisher CallHome (Spanish)",
              "wav2vec2"
            ],
            [
              "Emotion Classification",
              "IEMOCAP",
              "ECAPA-TDNN"
            ],
            [
              "Language Identification",
              "VoxLingua107",
              "ECAPA-TDNN"
            ],
            [
              "Voice Activity Detection",
              "LibriParty",
              "CRDNN"
            ],
            [
              "Sound Classification",
              "ESC50",
              "CNN14"
            ],
            [
              "Self-Supervised Learning",
              "CommonVoice",
              "wav2vec2"
            ],
            [
              "Metric Learning",
              "REAL-M",
              "Blind SNR-Estimation"
            ],
            [
              "Alignment",
              "TIMIT",
              "CTC"
            ],
            [
              "Diarization",
              "AMI",
              "ECAPA-TDNN"
            ]
          ]
        }
      },
      {
        "source_id": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
        "citation_number": 4,
        "cited_text": "Repository files navigation README License More Repository files items Apache-2.0 license MIT license DeepFilterNet A Low Complexity Speech Enhancement Framework for Full-Band Audio (48kHz) using on Deep Filtering. For PipeWire integration as a virtual noise suppression microphone look here . Demo DeepFilterNet-Demo-new.mp4 To run the demo (linux only) use: News New DeepFilterNet Demo: DeepFilterNet: Perceptually Motivated Real-Time Speech Enhancement Paper: https://arxiv.org/abs/2305.08227 Video: https://youtu.be/EO7n96YwnyE New Multi-Frame Filtering Paper: Deep Multi-Frame Filtering for Hearing Aids Paper: https://arxiv.org/abs/2305.08225 Real-time version and a LADSPA plugin Pre-compiled binary , no python dependencies. Usage: deep-filter audio-file.wav LADSPA plugin with pipewire filter-chain integration for real-time noise reduction on your mic. DeepFilterNet2 Paper: DeepFilterNet2: Towards Real-Time Speech Enhancement on Embedded Devices for Full-Band Audio Paper: https://arxiv.org/abs/2205.05474 Samples: https://rikorose.github.io/DeepFilterNet2-Samples/ Demo: https://huggingface.co/spaces/hshr/DeepFilterNet2 Original DeepFilterNet Paper: DeepFilterNet: A Low Complexity Speech Enhancement Framework for Full-Band Audio based on Deep Filtering Paper: https://arxiv.org/abs/2110.05588 Samples: https://rikorose.github.io/DeepFilterNet-Samples/ Demo: https://huggingface.co/spaces/hshr/DeepFilterNet Video Lecture: https://youtu.be/it90gBqkY6k"
      },
      {
        "source_id": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
        "citation_number": 5,
        "cited_text": "If you use the DeepFilterNet2 model, please cite: DeepFilterNet2: Towards Real-Time Speech Enhancement on Embedded Devices for Full-Band Audio If you use the DeepFilterNet3 model, please cite: DeepFilterNet: Perceptually Motivated Real-Time Speech Enhancement If you use the multi-frame beamforming algorithms. please cite Deep Multi-Frame Filtering for Hearing Aids License DeepFilterNet is free and open source! All code in this repository is dual-licensed under either: MIT License ( LICENSE-MIT or http://opensource.org/licenses/MIT ) Apache License, Version 2.0 ( LICENSE-APACHE or http://www.apache.org/licenses/LICENSE-2.0 )"
      },
      {
        "source_id": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
        "citation_number": 6,
        "cited_text": "Getting started with Asteroid Introduction and Overview Filterbank API Permutation invariant training wrapper PITLossWrapper Process large wav files Running a recipe ( ↑up to contents ) Running the recipes requires additional packages in most cases, we recommend running : Then choose the recipe you want to run and run it! More information in egs/README.md . Available recipes ( ↑up to contents ) [x] ConvTasnet ( Luo et al. ) [x] Tasnet ( Luo et al. ) [x] Deep clustering ( Hershey et al. and Isik et al. ) [x] Chimera ++ ( Luo et al. and Wang et al. ) [x] DualPathRNN ( Luo et al. ) [x] Two step learning ( Tzinis et al. ) [x] SudoRMRFNet ( Tzinis et al. ) [x] DPTNet ( Chen et al. ) [x] DCCRNet ( Hu et al. ) [x] DCUNet ( Choi et al. ) [x] CrossNet-Open-Unmix ( Sawata et al. ) [x] Multi-Decoder DPRNN ( Zhu et al. ) [-] Open-Unmix (coming) ( Stöter et al. ) [-] Wavesplit (coming) ( Zeghidour et al. )"
      },
      {
        "source_id": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
        "citation_number": 7,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items CC-BY-4.0 license MIT license Security ICASSP 2023 Deep Noise Suppression Challenge Website: https://aka.ms/dns-challenge Git Repo: https://github.com/microsoft/DNS-Challenge Challenge Paper: Important features of this challenge Along with noise suppression, it includes de-reverberation and suppression of interfering talkers for headset and speakerphone scenarios. The challenge has two tracks: (i) Headset (wired/wireless headphone, earbuds such as airpods etc.) speech enhancement; (ii) Non-headset (speakerphone, built-in mic in laptop/desktop/mobile phone/other meeting devices etc.) speech enhancement. This challenge adopts the ITU-T P.835 subjective test framework to measure speech quality (SIG), background noise quality (BAK), and overall audio quality (OVRL). We modified the ITU-T P.835 to make it reliable for test clips with interfering (undesired neighboring) talkers. Along with P.835 scores, Word Accuracy (WAcc) is used to measure the performance of models. Please NOTE that the intellectual property (IP) is not transferred to the challenge organizers, i.e., if code is shared/submitted, the participants remain the owners of their code (when the code is made publicly available, an appropriate license should be added). There are new requirements for model related latency. Please check all requirements listed at https://www.microsoft.com/en-us/research/academic-program/deep-noise-suppression-challenge-icassp-2023/"
      },
      {
        "source_id": "abe2c06c-a51d-4549-b567-0ce3bb630961",
        "citation_number": 8,
        "cited_text": "2. Train For advanced researchers and developers, we provide model finetune and training scripts for all the tasks offerred in ClearVoice and more: Task 1: Speech enhancement (16kHz & 48kHz) Task 2: Speech separation (8kHz & 16kHz) Task 2: Speech super-resolution (48kHz) Task 4: Target speaker extraction Sub-Task 1: Audio-only Speaker Extraction Conditioned on a Reference Speech (8kHz) Sub-Task 2: Audio-visual Speaker Extraction Conditioned on Face (Lip) Recording (16kHz) Sub-Task 3: Audio-visual Speaker Extraction Conditioned on Body Gestures (16kHz) Sub-Task 4: Neuro-steered Speaker Extraction Conditioned on EEG Signals (16kHz)"
      },
      {
        "source_id": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
        "citation_number": 9,
        "cited_text": "The previous challenges were: The baseline NSNet noise suppression: The P.835 test framework: DNSMOS API: Contributing This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com . When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA."
      },
      {
        "source_id": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
        "citation_number": 10,
        "cited_text": "Baseline Speaker Embeddings This challenge adopted pretrained ECAPA-TDNN model available in SpeechBrain as baseline speaker embeddings models, available at https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb . Participants can use any other publically available speaker embeddings model or develop their own speaker embedding extractor. Participants are encourage to explore RawNet3 models available at https://github.com/jungjee/RawNet Previous DNS Challenge used RawNet2 speaker embeddings. So far, impact of different speaker embeddings for personalized speech enhancements is not studied in sufficient depth."
      },
      {
        "source_id": "abe2c06c-a51d-4549-b567-0ce3bb630961",
        "citation_number": 11,
        "cited_text": "Please leave your ⭐ on our GitHub to support this community project！ 记得点击右上角的星星⭐来支持我们一下，您的支持是我们更新模型的最大动力！ News 🔥 Upcoming: More tasks will be added to ClearVoice. [2025.6] Add an interface for ClearVoice that allows passing a Numpy array into the model and receiving its output as a NumPy array. It allows a more flexible call of the models during a training or inference pipeline. Please check out demo_Numpy2Numpy.py . [2025.5] Updated speechscore with more non-intrusive metrics: NISQA and DISTILL_MOS [2025.4] Updated pip installation for ClearVoice . Now you can simply type pip install clearvoice to use all the pretrained models in ClearVoice, see project description in PyPi link . [2025.4] Added a training script for speech super-resolution, supporting both retraining and fine-tuning of models. For details, refer to the documentation here . [2025.4] Added data generation scripts for training/finetuning speech enhancement models. The scripts generate either noisy speech or noisy-reverberant speech. Please check here . [2025.1] ClearVoice demo is ready for try on both HuggingFace and ModelScope . However, HuggingFace has limited GPU usage, and ModelScope has more GPU usage quota. [2025.1] ClearVoice now offers speech super-resolution , also known as bandwidth extension. This feature improves the perceptual quality of speech by converting low-resolution audio (with an effective sampling rate of at least 16,000 Hz) into high-resolution audio with a sampling rate of 48,000 Hz. A full upscaled LJSpeech-1.1-48kHz dataset can be downloaded from HuggingFace and ModelScope . [2025.1] ClearVoice now supports more audio formats including \"wav\", \"aac\", \"ac3\", \"aiff\", \"flac\", \"m4a\", \"mp3\", \"ogg\", \"opus\", \"wma\", \"webm\" , etc. It also supports both mono and stereo channels with 16-bit or 32-bit precisions. A latest version of ffmpeg is required for audio codecs. [2024.12] Upload pre-trained models on ModelScope. User now can download the models from either ModelScope or Huggingface [2024.11] Our FRCRN speech denoiser has been used over 3.0 million times on ModelScope [2024.11] Our MossFormer speech separator has been used over 2.5 million times on ModelScope [2024.11] Release of this repository"
      },
      {
        "source_id": "abe2c06c-a51d-4549-b567-0ce3bb630961",
        "citation_number": 12,
        "cited_text": "Contents of this repository This repository is organized into three main components: ClearVoice , Train , and SpeechScore . 1. ClearVoice [ Readme][ 文档] ClearVoice offers a user-friendly solution for speech processing tasks such as speech denoising, separation, super-resolution, audio-visual target speaker extraction, and more. It is designed as a unified inference platform leveraged pre-trained models (e.g., FRCRN , MossFormer ), all trained on extensive datasets. If you're looking for a tool to improve speech quality, ClearVoice is the perfect choice. Simply click on ClearVoice and follow our detailed instructions to get started."
      },
      {
        "source_id": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
        "citation_number": 13,
        "cited_text": "( ↑up to contents ) Modularity. Building blocks are thought and designed to be seamlessly plugged together. Filterbanks, encoders, maskers, decoders and losses are all common building blocks that can be combined in a flexible way to create new systems. Extensibility. Extending Asteroid with new features is simple. Add a new filterbank, separator architecture, dataset or even recipe very easily. Reproducibility. Recipes provide an easy way to reproduce results with data preparation, system design, training and evaluation in a single script. This is an essential tool for the community!"
      },
      {
        "source_id": "d469b10c-9efc-4e9c-8e6d-cab16768e5ee",
        "citation_number": 14,
        "cited_text": "Build voice-enabled, multilingual generative AI apps with fast transcriptions and natural-sounding voices. Explore Azure Speech Integrate voice with your AI agents Enable AI agents with end-to-end speech, including customized transcription, voice, and avatars. Explore Voice Live API Translate audio or text Enable real-time, multi-language speech-to-speech translation and speech-to-text transcription of audio streams. Learn more Deploy anywhere Run AI models wherever your data resides. Deploy your apps in the cloud or at the edge with containers. Develop with containers"
      },
      {
        "source_id": "d469b10c-9efc-4e9c-8e6d-cab16768e5ee",
        "citation_number": 15,
        "cited_text": "Learn more Enable multilingual communication Translate audio or video data from and into an ever-growing list of supported languages. Customize translations to your industry. Learn more Embed speech Use embedded speech to power on-device speech-to-text and text-to-speech scenarios where cloud connectivity is intermittent or unavailable. Learn more Security Embedded security and compliance 34,000 Full-time equivalent engineers dedicated to security initiatives at Microsoft. Learn more 15,000 Partners with specialized security expertise."
      },
      {
        "source_id": "d469b10c-9efc-4e9c-8e6d-cab16768e5ee",
        "citation_number": 16,
        "cited_text": "Azure Speech is part of Foundry Tools (formerly Azure AI Services) and provides APIs for speech-to-text, text-to-speech, translation, and speaker recognition. It was previously known as Azure AI Speech. 02/ I see that Azure AI Speech is now called Azure Speech in Foundry Tools. How does that change the service? Yes, we're rebranding many of our former Azure AI Services as Foundry Tools. This shift reflects a broader platform unification under Foundry, and signals that these services are now positioned as core tools for building agentic AI applications. Azure Speech in Foundry Tools still offers the same powerful capabilities—like speech recognition, text-to-speech, and translation—but is now part of a cohesive toolkit designed for developers building intelligent agents. The rebrand helps clarify how these APIs fit into the Foundry ecosystem and makes it easier to discover, orchestrate, and integrate them into modern AI workflows."
      },
      {
        "source_id": "7de04067-7886-4191-bee0-6da8e42f7a86",
        "citation_number": 17,
        "cited_text": "Download Now Download Now Please go to a desktop browser to download the NVIDIA Broadcast app. Close Version 2.0.0 System Requirements | Setup Guide See Broadcast in Action Get a taste of what the Broadcast app can do for you using the incredible performance of NVIDIA RTX™ GPUs. Noise and Echo Removal Rise Above the Noise Loud keyboard typing. Annoying microphone static. Bothersome PC fans. Nagging background reverb. Noise Removal and Room Echo Removal use AI to eliminate unwanted background noise at the touch of a button."
      },
      {
        "source_id": "7de04067-7886-4191-bee0-6da8e42f7a86",
        "citation_number": 18,
        "cited_text": "<cited_table> Support Setup Guide FAQ Help Feedback Release Notes Stream Like a Boss Steal the show with the best livestreaming quality, the highest gaming performance, and cutting-edge AI features. Powered by the 9th-gen NVIDIA Encoder (NVENC), GeForce RTX® 50 Series ushers in a new era of high-quality broadcasting with improved AV1 and HEVC encode quality. Plus, access exclusive optimizations and AI effects in your favorite broadcasting apps to transform any room into a home studio.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "System Requirements",
              ""
            ],
            [
              "GPU",
              "NVIDIA GeForce RTX™ 2060, Quadro RTX™ 3000, TITAN RTX™, or higher"
            ],
            [
              "RAM",
              "8GB RAM or higher"
            ],
            [
              "CPU",
              "Recommended: Intel Core i5 8600, AMD Ryzen r5 2600 or higher"
            ],
            [
              "Driver",
              "NVIDIA Studio Driver"
            ],
            [
              "Internet",
              "Internet connectivity during installation"
            ]
          ]
        }
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 19,
        "cited_text": "During Meeting After Meeting Before Meeting In-meeting superpowers. Stay focused with noise-free calls, instant transcripts, and action items Transcription & Recording Krisp's AI meeting assistant silently handles transcripts and recordings . demo Noise Cancellation #1 AI noise cancellation for any meeting removes noise, echo, and cross-talk. demo Accent Conversion AI accent conversion for clearer, more confident communication in every meeting. Your browser does not support the video tag. AI Noise Cancellation"
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 20,
        "cited_text": "Voice AI for Meetings: Noise Cancellation & AI Note Taker | Krisp Krisp AI Meeting Note Taker Voice Notes and Memo Recorder AI Meeting Assistant Back AI Meeting Assistant with #1 Noise Cancellation Explore AI Meeting Assistant AI Notetaker AI Note Taker Meeting Transcription Meeting Recording Meeting Summary Real Time Voice AI Noise Cancellation Accent Conversion - Speaker side Accent Conversion - Listener side Use cases IT Consulting MSP Call Center AI Back Call Center AI AI that boosts call center productivity Explore platform Speech Assist Accent Conversion Real-time accent conversion for call center agents. Voice Translation Real-time AI voice translation for call center agents. Noise Cancellation Remove background noises, voices & echoes. Agent Assist Agent Assist Real-time AI assistant for call center agents. Speech Analytics Speech Analytics Call scoring, Compliance monitoring and more. AI Voice SDK Back AI Voice SDK with #1 AI Voice Models Explore SDK For Voice AI Agents Voice Isolation Isolate the primary speaker's voice Turn-Taking Improving turn-taking for AI For Human-to-human Calls Accent Conversion Convert accents in calls Voice Translation Voice-to-voice translation of multilingual calls Noise Cancellation Noise removal in calls Customers Pricing"
      },
      {
        "source_id": "abe2c06c-a51d-4549-b567-0ce3bb630961",
        "citation_number": 21,
        "cited_text": "Contributors are welcomed to include more model architectures and tasks! 3. SpeechScore [ Readme][ 文档] SpeechScore is a speech quality assessment toolkit. We include it here to evaluate different model performance. SpeechScore includes many popular speech metrics: Signal-to-Noise Ratio (SNR) Perceptual Evaluation of Speech Quality (PESQ) Short-Time Objective Intelligibility (STOI) Deep Noise Suppression Mean Opinion Score (DNSMOS) Scale-Invariant Signal-to-Distortion Ratio (SI-SDR) and many more quality benchmarks"
      },
      {
        "source_id": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
        "citation_number": 22,
        "cited_text": "Install SpeechBrain with below command: pip install speechbrain #Compute Speaker Embeddings for your wav file with below command: import torchaudio from speechbrain.pretrained import EncoderClassifier classifier = EncoderClassifier.from_hparams(source=\"speechbrain/spkrec-ecapa-voxceleb\") signal, fs =torchaudio.load('tests/samples/ASR/spk1_snt1.wav') embeddings = classifier.encode_batch(signal) In this repository This repository contains the datasets and scripts required for 5th DNS Challenge at ICASSP 2023, aka DNS Challenge 5, or simply DNS5 . For more details about the challenge, please see our website and paper . For more details on the testing framework, please visit P.835 ."
      },
      {
        "source_id": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
        "citation_number": 23,
        "cited_text": "Datasets V5_dev_testset : directory containing dev testsets for both tracks. Each testclip has 10s duration and the corresponding enrollment clips with 30s duration. BLIND testset : WAcc script https://github.com/microsoft/DNS-Challenge/tree/master/WAcc Wacc ground-truth transcript Dev testset: available only for speakerphone track, see v5_dev_testset directory. For headset track, we are providing ASR output and list of prompts read during recording of testclips. Participants can help in correcting ASR output to generate the ground-truth transcripts. Blind testset:"
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「语音增强与降噪」旨在通过深度学习和数字信号处理技术，在嘈杂环境中提取清晰的人声。以下是基于资料的实现细节深度解析：\n\n### 1. 核心算法流程\n现代语音增强技术通常遵循以下两种核心工作流：\n*   **深度过滤（Deep Filtering）架构：** 如 **DeepFilterNet** 框架，其核心流程是针对全频带音频（48kHz）进行低复杂度的增强。该算法首先利用 **STFT（短时傅里叶变换）** 将音频转入频域，随后通过深度神经网络预测复数增益或掩蔽（Masking），对频谱进行实时过滤，最后通过 **ISTFT（逆短时傅里叶变换）** 还原时域信号 [1, 2]。\n*   **模块化构建块（Modular Blocks）：** 如 **Asteroid** 工具包采用的架构模式，流程包括：**滤波器组（Filterbanks）** $\\rightarrow$ **编码器（Encoders）** $\\rightarrow$ **分离器/掩蔽器（Separators/Maskers）** $\\rightarrow$ **解码器（Decoders）** [3]。这种模式允许灵活组合不同的模型架构，如时域的 **ConvTasNet** 或基于注意力机制的 **SepFormer** [4, 5]。\n\n### 2. 关键代码架构\n资料显示，高性能的降噪系统往往采用**混合语言架构**以平衡开发效率与运行性能：\n*   **混合驱动模式（以 DeepFilterNet 为例）：**\n    *   **libDF (Rust)：** 用于底层的高效数据加载、音频增强处理和实时流式计算，确保极低的端到端延迟 [2]。\n    *   **pyDF/Python 层：** 提供 Python 包装器，用于 PyTorch 模型的训练、评估以及与数据集（如 HDF5 格式）的交互 [2, 6]。\n*   **配置驱动架构（以 SpeechBrain 为例）：**\n    *   **YAML 封装：** 将所有超参数（学习率、模型结构、数据路径）封装在 YAML 文件中，实现模型定义的清晰化 [7, 8]。\n    *   **Brain 类编排：** 通过专门的 Python 基类处理训练循环、多 GPU 分布式训练及混合精度任务 [8]。\n\n### 3. 性能优化策略\n为了在嵌入式设备或高负载场景（如会议软件）中实现「清晰对话」，系统采用了以下优化：\n*   **硬件加速与推理优化：** **NVIDIA Broadcast** 利用 **RTX GPU** 的专用核心处理 AI 降噪、房间回声消除和空间音频增强 [9, 10]。**Krisp** 则通过**端侧（On-device）处理**技术，在本地完成 16 种语言的转录和增强，以确保隐私并减少网络带宽需求 [11, 12]。\n*   **模型精简与超分辨率：** **DeepFilterNet2** 专门针对嵌入式设备优化，通过感知动机的结构设计降低计算复杂度 [1]。**ClearerVoice-Studio** 提供**语音超分辨率（Bandwidth Extension）**功能，将 16kHz 音频实时扩展至 48kHz，在节省传输资源的同时保持高保真音质 [13]。\n*   **动态批处理（Dynamic Batching）：** 在训练阶段，通过对变长信号进行即时动态批处理，提升 GPU 利用率 [8]。\n\n### 4. 关键技术参数与数据\n*   **音频采样率：** 主流 SOTA 模型（如 DeepFilterNet, ClearVoice）普遍支持 **48kHz 全频带音频**处理 [1, 13]。\n*   **评估指标：** 采用 **ITU-T P.835** 主观测试框架，评估 **SIG**（语音质量）、**BAK**（背景噪声质量）和 **OVRL**（整体音频质量）；此外还包括 **PESQ**、**STOI** 和 **Word Accuracy (WAcc)** 词准确率 [14, 15]。\n*   **功能参数：**\n    *   **Krisp：** 支持 **750 个**工作区自定义词汇术语；支持 **16 种**语言的转录 [12, 16]。\n    *   **应用数据：** **FRCRN** 模型在 ModelScope 上的调用量已超过 **300 万次**，**MossFormer** 分离模型超过 **250 万次** [13]。\n*   **硬件门槛：** NVIDIA Broadcast 推荐配置为 **RTX 2060 GPU** 及以上，需 **8GB RAM** [10]。\n\n### 5. 竞品技术对比\n| 特性 | DeepFilterNet / Asteroid | NVIDIA Broadcast | Krisp |\n| :--- | :--- | :--- | :--- |\n| **核心优势** | 开源、模块化，支持极低复杂度嵌入式部署 [1, 3] | 深度集成 RTX 硬件，支持虚拟灯光、眼部校正等多模态 AI [10, 17] | 卓越的跨平台集成（Zoom/Teams/Meet），支持双向降噪（发言方与听众方） [18, 19] |\n| **主要功能** | 噪声抑制、波束成形 [1, 20] | 降噪、回声消除、背景替换 [9, 21] | 降噪、口音转换（Accent Conversion）、AI 纪要 [22, 23] |\n| **适用人群** | 研究员、嵌入式开发者 [2, 24] | 主播、视频会议专业人士 [25] | 企业团队、呼叫中心 [26] |",
    "conversation_id": "93edd13d-32e9-467d-81ca-bf6b1f9a8045",
    "sources_used": [
      "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
      "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
      "7de04067-7886-4191-bee0-6da8e42f7a86",
      "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "a21bb63c-b6cb-4d2f-918e-7ed6629c6119"
    ],
    "citations": {
      "1": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "2": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "3": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
      "4": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
      "5": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
      "6": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "7": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
      "8": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
      "9": "7de04067-7886-4191-bee0-6da8e42f7a86",
      "10": "7de04067-7886-4191-bee0-6da8e42f7a86",
      "11": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "12": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "13": "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "14": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
      "15": "abe2c06c-a51d-4549-b567-0ce3bb630961",
      "16": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "17": "7de04067-7886-4191-bee0-6da8e42f7a86",
      "18": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "19": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "20": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
      "21": "7de04067-7886-4191-bee0-6da8e42f7a86",
      "22": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "23": "b41cdd21-d04c-441e-b768-9543c9bbba07",
      "24": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
      "25": "7de04067-7886-4191-bee0-6da8e42f7a86",
      "26": "b41cdd21-d04c-441e-b768-9543c9bbba07"
    },
    "references": [
      {
        "source_id": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
        "citation_number": 1,
        "cited_text": "Repository files navigation README License More Repository files items Apache-2.0 license MIT license DeepFilterNet A Low Complexity Speech Enhancement Framework for Full-Band Audio (48kHz) using on Deep Filtering. For PipeWire integration as a virtual noise suppression microphone look here . Demo DeepFilterNet-Demo-new.mp4 To run the demo (linux only) use: News New DeepFilterNet Demo: DeepFilterNet: Perceptually Motivated Real-Time Speech Enhancement Paper: https://arxiv.org/abs/2305.08227 Video: https://youtu.be/EO7n96YwnyE New Multi-Frame Filtering Paper: Deep Multi-Frame Filtering for Hearing Aids Paper: https://arxiv.org/abs/2305.08225 Real-time version and a LADSPA plugin Pre-compiled binary , no python dependencies. Usage: deep-filter audio-file.wav LADSPA plugin with pipewire filter-chain integration for real-time noise reduction on your mic. DeepFilterNet2 Paper: DeepFilterNet2: Towards Real-Time Speech Enhancement on Embedded Devices for Full-Band Audio Paper: https://arxiv.org/abs/2205.05474 Samples: https://rikorose.github.io/DeepFilterNet2-Samples/ Demo: https://huggingface.co/spaces/hshr/DeepFilterNet2 Original DeepFilterNet Paper: DeepFilterNet: A Low Complexity Speech Enhancement Framework for Full-Band Audio based on Deep Filtering Paper: https://arxiv.org/abs/2110.05588 Samples: https://rikorose.github.io/DeepFilterNet-Samples/ Demo: https://huggingface.co/spaces/hshr/DeepFilterNet Video Lecture: https://youtu.be/it90gBqkY6k"
      },
      {
        "source_id": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
        "citation_number": 2,
        "cited_text": "Usage deep-filter Download a pre-compiled deep-filter binary from the release page . You can use deep-filter to suppress noise in noisy .wav audio files. Currently, only wav files with a sampling rate of 48kHz are supported. If you want to use the pytorch backend e.g. for GPU processing, see further below for the Python usage. DeepFilterNet Framework This framework supports Linux, MacOS and Windows. Training is only tested under Linux. The framework is structured as follows: libDF contains Rust code used for data loading and augmentation. DeepFilterNet contains DeepFilterNet code training, evaluation and visualization as well as pretrained model weights. pyDF contains a Python wrapper of libDF STFT/ISTFT processing loop. pyDF-data contains a Python wrapper of libDF dataset functionality and provides a pytorch data loader. ladspa contains a LADSPA plugin for real-time noise suppression. models contains pretrained for usage in DeepFilterNet (Python) or libDF/deep-filter (Rust)"
      },
      {
        "source_id": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
        "citation_number": 3,
        "cited_text": "( ↑up to contents ) Modularity. Building blocks are thought and designed to be seamlessly plugged together. Filterbanks, encoders, maskers, decoders and losses are all common building blocks that can be combined in a flexible way to create new systems. Extensibility. Extending Asteroid with new features is simple. Add a new filterbank, separator architecture, dataset or even recipe very easily. Reproducibility. Recipes provide an easy way to reproduce results with data preparation, system design, training and evaluation in a single script. This is an essential tool for the community!"
      },
      {
        "source_id": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
        "citation_number": 4,
        "cited_text": "Getting started with Asteroid Introduction and Overview Filterbank API Permutation invariant training wrapper PITLossWrapper Process large wav files Running a recipe ( ↑up to contents ) Running the recipes requires additional packages in most cases, we recommend running : Then choose the recipe you want to run and run it! More information in egs/README.md . Available recipes ( ↑up to contents ) [x] ConvTasnet ( Luo et al. ) [x] Tasnet ( Luo et al. ) [x] Deep clustering ( Hershey et al. and Isik et al. ) [x] Chimera ++ ( Luo et al. and Wang et al. ) [x] DualPathRNN ( Luo et al. ) [x] Two step learning ( Tzinis et al. ) [x] SudoRMRFNet ( Tzinis et al. ) [x] DPTNet ( Chen et al. ) [x] DCCRNet ( Hu et al. ) [x] DCUNet ( Choi et al. ) [x] CrossNet-Open-Unmix ( Sawata et al. ) [x] Multi-Decoder DPRNN ( Zhu et al. ) [-] Open-Unmix (coming) ( Stöter et al. ) [-] Wavesplit (coming) ( Zeghidour et al. )"
      },
      {
        "source_id": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
        "citation_number": 5,
        "cited_text": "🔧 Supported Technologies SpeechBrain is a versatile framework designed for implementing a wide range of technologies within the field of Conversational AI. It excels not only in individual task implementations but also in combining various technologies into complex pipelines. 🎙 Speech/Audio Processing <cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Tasks",
              "Datasets",
              "Technologies/Models"
            ],
            [
              "Speech Recognition",
              "AISHELL-1",
              "CTC"
            ],
            [
              "Speaker Recognition",
              "VoxCeleb",
              "ECAPA-TDNN"
            ],
            [
              "Speech Separation",
              "WSJ0Mix",
              "SepFormer"
            ],
            [
              "Speech Enhancement",
              "DNS",
              "SepFormer"
            ],
            [
              "Interpretability",
              "ESC50",
              "Listenable Maps for Audio Classifiers (L-MAC)"
            ],
            [
              "Speech Generation",
              "AudioMNIST",
              "Diffusion"
            ],
            [
              "Text-to-Speech",
              "LJSpeech",
              "Tacotron2"
            ],
            [
              "Vocoding",
              "LJSpeech",
              "HiFiGAN"
            ],
            [
              "Spoken Language Understanding",
              "MEDIA",
              "Direct SLU"
            ],
            [
              "Speech-to-Speech Translation",
              "CVSS",
              "Discrete Hubert"
            ],
            [
              "Speech Translation",
              "Fisher CallHome (Spanish)",
              "wav2vec2"
            ],
            [
              "Emotion Classification",
              "IEMOCAP",
              "ECAPA-TDNN"
            ],
            [
              "Language Identification",
              "VoxLingua107",
              "ECAPA-TDNN"
            ],
            [
              "Voice Activity Detection",
              "LibriParty",
              "CRDNN"
            ],
            [
              "Sound Classification",
              "ESC50",
              "CNN14"
            ],
            [
              "Self-Supervised Learning",
              "CommonVoice",
              "wav2vec2"
            ],
            [
              "Metric Learning",
              "REAL-M",
              "Blind SNR-Estimation"
            ],
            [
              "Alignment",
              "TIMIT",
              "CTC"
            ],
            [
              "Diarization",
              "AMI",
              "ECAPA-TDNN"
            ]
          ]
        }
      },
      {
        "source_id": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
        "citation_number": 6,
        "cited_text": "So, you first need to create your datasets in HDF5 format. Each dataset typically only holds training, validation, or test set of noise, speech or RIRs. All datasets should be made available in one dataset folder for the train script. The dataset configuration file should contain 3 entries: \"train\", \"valid\", \"test\". Each of those contains a list of datasets (e.g. a speech, noise and a RIR dataset). You can use multiple speech or noise dataset. Optionally, a sampling factor may be specified that can be used to over/under-sample the dataset. Say, you have a specific dataset with transient noises and want to increase the amount of non-stationary noises by oversampling. In most cases you want to set this factor to 1."
      },
      {
        "source_id": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
        "citation_number": 7,
        "cited_text": "📚 Training Recipes We share over 200 competitive training recipes on more than 40 datasets supporting 20 speech and text processing tasks (see below). We support both training from scratch and fine-tuning pretrained models such as Whisper , Wav2Vec2 , WavLM , Hubert , GPT2 , Llama2 , and beyond. The models on HuggingFace can be easily plugged in and fine-tuned. For any task, you train the model using these commands: The hyperparameters are encapsulated in a YAML file, while the training process is orchestrated through a Python script. We maintained a consistent code structure across different tasks. For better replicability, training logs and checkpoints are hosted on Dropbox."
      },
      {
        "source_id": "4fd34b4b-1c32-4c76-84d7-322c96dbd7e4",
        "citation_number": 8,
        "cited_text": "Training Orchestration: The Brain class serves as a fully customizable tool for managing training and evaluation loops over data. It simplifies training loops while providing the flexibility to override any part of the process. Hyperparameter Management: A YAML-based hyperparameter file specifies all hyperparameters, from individual numbers (e.g., learning rate) to complete objects (e.g., custom models). This elegant solution drastically simplifies the training script. Dynamic Dataloader: Enables flexible and efficient data reading. GPU Training: Supports single and multi-GPU training, including distributed training. Dynamic Batching: On-the-fly dynamic batching enhances the efficient processing of variable-length signals. Mixed-Precision Training: Accelerates training through mixed-precision techniques. Efficient Data Reading: Reads large datasets efficiently from a shared Network File System (NFS) via WebDataset . Hugging Face Integration: Interfaces seamlessly with HuggingFace for popular models such as wav2vec2 and Hubert. Orion Integration: Interfaces with Orion for hyperparameter tuning. Speech Augmentation Techniques: Includes SpecAugment, Noise, Reverberation, and more. Data Preparation Scripts: Includes scripts for preparing data for supported datasets."
      },
      {
        "source_id": "7de04067-7886-4191-bee0-6da8e42f7a86",
        "citation_number": 9,
        "cited_text": "Download Now Download Now Please go to a desktop browser to download the NVIDIA Broadcast app. Close Version 2.0.0 System Requirements | Setup Guide See Broadcast in Action Get a taste of what the Broadcast app can do for you using the incredible performance of NVIDIA RTX™ GPUs. Noise and Echo Removal Rise Above the Noise Loud keyboard typing. Annoying microphone static. Bothersome PC fans. Nagging background reverb. Noise Removal and Room Echo Removal use AI to eliminate unwanted background noise at the touch of a button."
      },
      {
        "source_id": "7de04067-7886-4191-bee0-6da8e42f7a86",
        "citation_number": 10,
        "cited_text": "<cited_table> Support Setup Guide FAQ Help Feedback Release Notes Stream Like a Boss Steal the show with the best livestreaming quality, the highest gaming performance, and cutting-edge AI features. Powered by the 9th-gen NVIDIA Encoder (NVENC), GeForce RTX® 50 Series ushers in a new era of high-quality broadcasting with improved AV1 and HEVC encode quality. Plus, access exclusive optimizations and AI effects in your favorite broadcasting apps to transform any room into a home studio.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "System Requirements",
              ""
            ],
            [
              "GPU",
              "NVIDIA GeForce RTX™ 2060, Quadro RTX™ 3000, TITAN RTX™, or higher"
            ],
            [
              "RAM",
              "8GB RAM or higher"
            ],
            [
              "CPU",
              "Recommended: Intel Core i5 8600, AMD Ryzen r5 2600 or higher"
            ],
            [
              "Driver",
              "NVIDIA Studio Driver"
            ],
            [
              "Internet",
              "Internet connectivity during installation"
            ]
          ]
        }
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 11,
        "cited_text": "Yes. Because Krisp works at the audio level, it integrates with every conferencing app such as Zoom, Google Meet, Microsoft Teams, Slack Huddles, and more. How accurate is Krisp transcription, and what affects quality? Krisp transcription is tuned for real-world meetings. Accuracy remains high even in noisy environments thanks to our Noise Cancellation. Quality depends mostly on the speaker's clarity and microphone, but because we filter out background distractions first, you will often see better results with Krisp than with standalone transcription tools. To make transcripts even more relevant, Krisp supports Custom Vocabulary with up to 750 words. This allows you to tailor transcription to your company or industry-specific language, ensuring names, acronyms, and technical terms are captured correctly."
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 12,
        "cited_text": "Which languages Krisp supports for transcription? Krisp supports on-device English transcription for maximum privacy and speed, plus server-based transcription in 15 additional languages including Spanish, French, German, Russian, Italian, Dutch, Polish, Portuguese, Hindi, Danish, Swedish, Norwegian, Czech, Ukrainian, and Korean. We continue to expand this list. Is there a Krisp mobile app, and what features does it include? Yes. The Krisp mobile app is built for on-the-go meetings. You can record and transcribe in-person conversations, capture hybrid sessions, or upload audio files for transcription. It works offline too. Today, mobile app does not include Noise Cancellation, but it is coming."
      },
      {
        "source_id": "abe2c06c-a51d-4549-b567-0ce3bb630961",
        "citation_number": 13,
        "cited_text": "Please leave your ⭐ on our GitHub to support this community project！ 记得点击右上角的星星⭐来支持我们一下，您的支持是我们更新模型的最大动力！ News 🔥 Upcoming: More tasks will be added to ClearVoice. [2025.6] Add an interface for ClearVoice that allows passing a Numpy array into the model and receiving its output as a NumPy array. It allows a more flexible call of the models during a training or inference pipeline. Please check out demo_Numpy2Numpy.py . [2025.5] Updated speechscore with more non-intrusive metrics: NISQA and DISTILL_MOS [2025.4] Updated pip installation for ClearVoice . Now you can simply type pip install clearvoice to use all the pretrained models in ClearVoice, see project description in PyPi link . [2025.4] Added a training script for speech super-resolution, supporting both retraining and fine-tuning of models. For details, refer to the documentation here . [2025.4] Added data generation scripts for training/finetuning speech enhancement models. The scripts generate either noisy speech or noisy-reverberant speech. Please check here . [2025.1] ClearVoice demo is ready for try on both HuggingFace and ModelScope . However, HuggingFace has limited GPU usage, and ModelScope has more GPU usage quota. [2025.1] ClearVoice now offers speech super-resolution , also known as bandwidth extension. This feature improves the perceptual quality of speech by converting low-resolution audio (with an effective sampling rate of at least 16,000 Hz) into high-resolution audio with a sampling rate of 48,000 Hz. A full upscaled LJSpeech-1.1-48kHz dataset can be downloaded from HuggingFace and ModelScope . [2025.1] ClearVoice now supports more audio formats including \"wav\", \"aac\", \"ac3\", \"aiff\", \"flac\", \"m4a\", \"mp3\", \"ogg\", \"opus\", \"wma\", \"webm\" , etc. It also supports both mono and stereo channels with 16-bit or 32-bit precisions. A latest version of ffmpeg is required for audio codecs. [2024.12] Upload pre-trained models on ModelScope. User now can download the models from either ModelScope or Huggingface [2024.11] Our FRCRN speech denoiser has been used over 3.0 million times on ModelScope [2024.11] Our MossFormer speech separator has been used over 2.5 million times on ModelScope [2024.11] Release of this repository"
      },
      {
        "source_id": "a21bb63c-b6cb-4d2f-918e-7ed6629c6119",
        "citation_number": 14,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items CC-BY-4.0 license MIT license Security ICASSP 2023 Deep Noise Suppression Challenge Website: https://aka.ms/dns-challenge Git Repo: https://github.com/microsoft/DNS-Challenge Challenge Paper: Important features of this challenge Along with noise suppression, it includes de-reverberation and suppression of interfering talkers for headset and speakerphone scenarios. The challenge has two tracks: (i) Headset (wired/wireless headphone, earbuds such as airpods etc.) speech enhancement; (ii) Non-headset (speakerphone, built-in mic in laptop/desktop/mobile phone/other meeting devices etc.) speech enhancement. This challenge adopts the ITU-T P.835 subjective test framework to measure speech quality (SIG), background noise quality (BAK), and overall audio quality (OVRL). We modified the ITU-T P.835 to make it reliable for test clips with interfering (undesired neighboring) talkers. Along with P.835 scores, Word Accuracy (WAcc) is used to measure the performance of models. Please NOTE that the intellectual property (IP) is not transferred to the challenge organizers, i.e., if code is shared/submitted, the participants remain the owners of their code (when the code is made publicly available, an appropriate license should be added). There are new requirements for model related latency. Please check all requirements listed at https://www.microsoft.com/en-us/research/academic-program/deep-noise-suppression-challenge-icassp-2023/"
      },
      {
        "source_id": "abe2c06c-a51d-4549-b567-0ce3bb630961",
        "citation_number": 15,
        "cited_text": "Contributors are welcomed to include more model architectures and tasks! 3. SpeechScore [ Readme][ 文档] SpeechScore is a speech quality assessment toolkit. We include it here to evaluate different model performance. SpeechScore includes many popular speech metrics: Signal-to-Noise Ratio (SNR) Perceptual Evaluation of Speech Quality (PESQ) Short-Time Objective Intelligibility (STOI) Deep Noise Suppression Mean Opinion Score (DNSMOS) Scale-Invariant Signal-to-Distortion Ratio (SI-SDR) and many more quality benchmarks"
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 16,
        "cited_text": "Install Mobile app Meetings on the go with the Krisp mobile app! Join & capture meetings from mobile Transcribe in-person meeting Easily access shared content Capture & customize meetings your way. Chrome Extension If using mostly conferencing apps inside chrome - like Google Meet. Get extension Audio/Video upload Upload and transcribe your meeting recordings. Custom Vocabulary 750 workspace-level terms and abbreviations, with industry-specific starter kits to get started easily. Record with bot"
      },
      {
        "source_id": "7de04067-7886-4191-bee0-6da8e42f7a86",
        "citation_number": 17,
        "cited_text": "Virtual Key Light Stay in the Spotlight Virtual Key Light helps you stay camera-ready with automatic face relighting that reduces shadows and keeps you evenly lit during your livestreams. Eye Contact See Eye to Eye Keep your eyes on the prize. Eye Contact uses AI to make it appear as if you're looking directly at the camera, even when glancing to the side or taking notes. Video Noise Removal Picture Perfect No light? No problem. Enhance the quality of your webcam, removing the visual noise that is present in low-light situations for a cleaner picture."
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 18,
        "cited_text": "Voice AI for Meetings: Noise Cancellation & AI Note Taker | Krisp Krisp AI Meeting Note Taker Voice Notes and Memo Recorder AI Meeting Assistant Back AI Meeting Assistant with #1 Noise Cancellation Explore AI Meeting Assistant AI Notetaker AI Note Taker Meeting Transcription Meeting Recording Meeting Summary Real Time Voice AI Noise Cancellation Accent Conversion - Speaker side Accent Conversion - Listener side Use cases IT Consulting MSP Call Center AI Back Call Center AI AI that boosts call center productivity Explore platform Speech Assist Accent Conversion Real-time accent conversion for call center agents. Voice Translation Real-time AI voice translation for call center agents. Noise Cancellation Remove background noises, voices & echoes. Agent Assist Agent Assist Real-time AI assistant for call center agents. Speech Analytics Speech Analytics Call scoring, Compliance monitoring and more. AI Voice SDK Back AI Voice SDK with #1 AI Voice Models Explore SDK For Voice AI Agents Voice Isolation Isolate the primary speaker's voice Turn-Taking Improving turn-taking for AI For Human-to-human Calls Accent Conversion Convert accents in calls Voice Translation Voice-to-voice translation of multilingual calls Noise Cancellation Noise removal in calls Customers Pricing"
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 19,
        "cited_text": "Our enterprise-grade protections keep your information safe, private, and in your control. Visit Trust center SOC 2 Certified Independently audited for top-tier security and privacy. GDPR Compliance Privacy built to meet EU regulations. HIPAA Compliant Complete protection for healthcare organizations. PCI-DSS Certified Certified to securely handle and process your payment information. Works with any calling app & integrates to your workflow From Google Calendar to Zoom, Slack, HubSpot, Salesforce, and Zapier - Krisp seamlessly fits into your workflow."
      },
      {
        "source_id": "ac12356d-b5d7-4e0b-ad44-68cac72153a8",
        "citation_number": 20,
        "cited_text": "If you use the DeepFilterNet2 model, please cite: DeepFilterNet2: Towards Real-Time Speech Enhancement on Embedded Devices for Full-Band Audio If you use the DeepFilterNet3 model, please cite: DeepFilterNet: Perceptually Motivated Real-Time Speech Enhancement If you use the multi-frame beamforming algorithms. please cite Deep Multi-Frame Filtering for Hearing Aids License DeepFilterNet is free and open source! All code in this repository is dual-licensed under either: MIT License ( LICENSE-MIT or http://opensource.org/licenses/MIT ) Apache License, Version 2.0 ( LICENSE-APACHE or http://www.apache.org/licenses/LICENSE-2.0 )"
      },
      {
        "source_id": "7de04067-7886-4191-bee0-6da8e42f7a86",
        "citation_number": 21,
        "cited_text": "Go live or attend a meeting remotely without worrying about finding a quiet place. NVIDIA Broadcast makes it fast and easy. Studio Voice Sound Your Best Upgrade your mic with the power of AI to deliver premium audio quality. With Studio Voice (beta) , you can sound your best and turn your room into a professional studio. Play Demo Virtual Background Set the Stage Experience instant creative control at your fingertips. Background Removal, Replacement, and Blur allow you to customize your background without the need for expensive equipment or complex lighting setups. Personalize your webcam feed using powerful AI greenscreen effects perfect for work and play, wherever you are. The possibilities are endless."
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 22,
        "cited_text": "During Meeting After Meeting Before Meeting In-meeting superpowers. Stay focused with noise-free calls, instant transcripts, and action items Transcription & Recording Krisp's AI meeting assistant silently handles transcripts and recordings . demo Noise Cancellation #1 AI noise cancellation for any meeting removes noise, echo, and cross-talk. demo Accent Conversion AI accent conversion for clearer, more confident communication in every meeting. Your browser does not support the video tag. AI Noise Cancellation"
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 23,
        "cited_text": "AI Noise Cancellation Play and toggle Krisp on and off 0 With Krisp Noise Cancellation Try out different noise types Multiple noises Barking dog Crying baby Keyboard clicks Fan noise Accent Conversion AI accent conversion for clearer, more confident communication in every meeting. Accent Conversion Play and toggle Krisp on and off 0 With Krisp AI Accent Conversion Try out different output voices Manoj Ishika Automate post-meeting everything. AI Note Taker handles meeting transcripts , summaries , and CRM updates. Focus on what matters."
      },
      {
        "source_id": "4e178ad6-0791-47d4-a1bc-2137f4fd707e",
        "citation_number": 24,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing MIT license The PyTorch-based audio source separation toolkit for researchers. Asteroid is a Pytorch-based audio source separation toolkit that enables fast experimentation on common datasets. It comes with a source code that supports a large range of datasets and architectures, and a set of recipes to reproduce some important papers. You use Asteroid or you want to? Please, if you have found a bug, open an issue , if you solved it, open a pull request ! Same goes for new features, tell us what you want or help us building it! Don't hesitate to join the slack and ask questions / suggest new features there as well! Asteroid is intended to be a community-based project so hop on and help us!"
      },
      {
        "source_id": "7de04067-7886-4191-bee0-6da8e42f7a86",
        "citation_number": 25,
        "cited_text": "Features System Requirements Support Download Now NVIDIA Broadcast Features System Requirements Support Download Now This site requires Javascript in order to view all its content. Please enable Javascript in order to access all the functionality of this web site. Here are the instructions how to enable JavaScript in your web browser. NVIDIA Broadcast App The NVIDIA Broadcast app transforms any room into a home studio. Take your livestreams, voice chats, and video conference calls to the next level with AI-enhanced voice and video."
      },
      {
        "source_id": "b41cdd21-d04c-441e-b768-9543c9bbba07",
        "citation_number": 26,
        "cited_text": "Sign in Book a demo Get Krisp [ AI Meeting Assistant For individuals and teams](https://app.krisp.ai/sign-up?tr_source=website&tr_button=navigation_button) [ Call Center AI For BPOs and call centers](https://krisp.ai/contact-center/) [ AI Voice SDK For developers](https://krisp.ai/developers/) AI Meeting Assistant Back AI Meeting Assistant with #1 Noise Cancellation Explore AI Meeting Assistant AI Notetaker AI Note Taker Meeting Transcription Meeting Recording Meeting Summary Real Time Voice AI Noise Cancellation Accent Conversion - Speaker side Accent Conversion - Listener side Use cases IT Consulting MSP Call Center AI Back Call Center AI AI that boosts call center productivity Explore platform Speech Assist Accent Conversion Real-time accent conversion for call center agents. Voice Translation Real-time AI voice translation for call center agents. Noise Cancellation Remove background noises, voices & echoes. Agent Assist Agent Assist Real-time AI assistant for call center agents. Speech Analytics Speech Analytics Call scoring, Compliance monitoring and more. AI Voice SDK Back AI Voice SDK with #1 AI Voice Models Explore SDK For Voice AI Agents Voice Isolation Isolate the primary speaker's voice Turn-Taking Improving turn-taking for AI For Human-to-human Calls Accent Conversion Convert accents in calls Voice Translation Voice-to-voice translation of multilingual calls Noise Cancellation Noise removal in calls Customers Pricing"
      }
    ]
  }
}
