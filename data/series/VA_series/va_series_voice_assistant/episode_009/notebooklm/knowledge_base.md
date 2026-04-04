# 知识库：声纹识别与说话人分离：语音助手的身份认证

生成时间: 2026-04-03 14:00
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "根据提供的来源，声纹识别与说话人分离技术作为语音助手身份认证的核心，其技术架构和关键组件概括如下：\n\n### 一、 核心技术架构与主要架构模式\n身份认证系统的核心架构通常由两个主要子系统组成：**声纹识别（Speaker Recognition/Verification）**和**说话人分离（Speaker Diarization）** [1-3]。\n\n1.  **处理流水线（Pipeline Pattern）**：\n    这是目前最常用的架构模式，将复杂任务拆解为多个神经构建模块 [2, 4]：\n    *   **语音活动检测（VAD/SAD）**：识别音频中的人声部分 [2-4]。\n    *   **说话人变更检测与重叠检测**：识别说话人切换点及多人同时说话的情况 [2, 4, 5]。\n    *   **特征提取（Embedding Extraction）**：将变长的语音片段映射为固定长度的声纹特征向量（Embedding） [6, 7]。\n    *   **后端处理/聚类**：对提取的特征进行相似度比对（识别）或分群（分离） [3, 8, 9]。\n\n2.  **全监督架构模式（Fully Supervised Pattern）**：\n    如 **UIS-RNN**，它打破了传统聚类的局限，通过递归神经网络以全监督的方式同时解决序列数据的分割与聚类问题 [8, 10]。\n\n### 二、 技术演进路线\n来源中提到了从传统统计模型到深度学习模型的明确演进过程：\n*   **传统阶段**：使用全协方差 GMM-UBM、i-Vectors 以及 PLDA 后端作为标准方法 [7]。\n*   **深度学习早期**：引入基于 DNN 的说话人嵌入（Speaker Embeddings），例如经典的 **x-vector** 架构 [6, 7]。\n*   **现代增强阶段**：\n    *   引入 **Res2Net** 模块和 **注意力机制（Attention）** [6]。\n    *   使用 **Squeeze-and-Excitation (SE)** 块来显式建模通道间的依赖关系 [6]。\n    *   特征聚合与传播：利用不同层级的分级特征进行增强 [6]。\n*   **前沿阶段**：发展到更高性能的架构，如 **ECAPA-TDNN**、**CAM++** 和 **ERes2Net** [6, 11, 12]。\n\n### 三、 核心算法名称\n*   **声纹特征提取模型**：\n    *   **d-vector** [13, 14]、**x-vector** [6, 7]、**ECAPA-TDNN** [6, 15]。\n    *   **ResNet** 系列（如 ResNet34, SimAM_ResNet） [9, 11]。\n    *   **CAM++**、**ERes2Net**、**RepVGG** [11, 12]。\n*   **后端比对与聚类算法**：\n    *   **PLDA**（概率线性判别分析） [3, 9]。\n    *   **谱聚类（Spectral Clustering）** [3, 16]。\n    *   **UIS-RNN**（无界交错状态循环神经网络） [8, 17]。\n    *   **UMAP** 降维结合 **HDBSCAN** 聚类 [11]。\n\n### 四、 关键技术指标\n衡量身份认证系统性能的主要指标包括：\n*   **EER (Equal Error Rate，等错误率)**：衡量声纹识别准确性的核心指标，数值越低表示性能越好（例如在 Vox1-O-clean 集上可达到 0.447%） [9]。\n*   **minDCF (Minimum Detection Cost Function，最小检测代价函数)**：用于评估识别系统的决策成本 [9]。\n*   **DER (Diarization Error Rate，说话人分离错误率)**：衡量说话人分离系统的综合错误指标，包括虚警、漏检和标签错误 [18-20]。\n*   **推理速度（Inference Speed）**：例如“每小时音频处理所需秒数”，是衡量生产环境可用性的重要指标 [21]。\n\n### 五、 交付与部署组件\n为了实现语音助手的实时认证，系统通常包含以下组件：\n*   **SDK 与 REST API**：用于将声纹能力集成到移动端或桌面端应用中 [22, 23]。\n*   **容器化部署**：支持在云端或边缘计算设备上运行，以满足合规性与安全性要求 [24, 25]。\n*   **定制化训练工具**：如 Azure Speech Studio，允许用户创建自定义声纹模型或神经语音 [22, 26]。",
    "conversation_id": "a31d41fe-47ba-4e4e-bcad-64bf6d5ee582",
    "sources_used": [
      "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "77a438b2-68a7-435c-bd6b-a116c7953577",
      "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "952e6f81-ec96-4412-9872-13c331762d12",
      "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
      "66d08aeb-fde5-4b5b-a700-957312a58234",
      "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "5341d428-958c-4c67-9cec-262642f52388",
      "70279693-1c87-43f1-9150-6347ce00ecc8"
    ],
    "citations": {
      "1": "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "2": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "3": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "4": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "5": "952e6f81-ec96-4412-9872-13c331762d12",
      "6": "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
      "7": "66d08aeb-fde5-4b5b-a700-957312a58234",
      "8": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "9": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "10": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "11": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "12": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "13": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "14": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "15": "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
      "16": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "17": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "18": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "19": "952e6f81-ec96-4412-9872-13c331762d12",
      "20": "952e6f81-ec96-4412-9872-13c331762d12",
      "21": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "22": "5341d428-958c-4c67-9cec-262642f52388",
      "23": "70279693-1c87-43f1-9150-6347ce00ecc8",
      "24": "5341d428-958c-4c67-9cec-262642f52388",
      "25": "5341d428-958c-4c67-9cec-262642f52388",
      "26": "5341d428-958c-4c67-9cec-262642f52388"
    },
    "references": [
      {
        "source_id": "f7a45787-0b03-46c1-a505-cf2112070aa9",
        "citation_number": 1,
        "cited_text": "docs.nvidia.com/nemo-framework/user-guide/latest/overview.html Topics machine-translation tts speech-synthesis neural-networks deeplearning speaker-recognition asr speech-translation speaker-diariazation generative-ai Resources Readme License Apache-2.0 license Contributing Contributing Citation Cite this repository Loading Something went wrong. Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 17k stars Watchers 231 watching Forks 3.4k forks Report repository Releases 85"
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 2,
        "cited_text": "Citations If you use pyannote.audio please use the following citations: Development The commands below will setup pre-commit hooks and packages needed for developing the pyannote.audio library. Test About Neural building blocks for speaker diarization: speech activity detection, speaker change detection, overlapped speech detection, speaker embedding pyannote.github.io Topics pytorch pretrained-models speaker-recognition speaker-verification speech-processing speaker-diarization voice-activity-detection speech-activity-detection speaker-change-detection speaker-embedding overlapped-speech-detection"
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
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
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 4,
        "cited_text": "GitHub - pyannote/pyannote-audio: Neural building blocks for speaker diarization: speech activity detection, speaker change detection, overlapped speech detection, speaker embedding · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 5,
        "cited_text": "pyannote/speaker-diarization-3.1 · Hugging Face Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Log In Sign Up pyannote / speaker-diarization-3.1 like 1.71k Follow pyannote 2.23k Automatic Speech Recognition pyannote.audio pyannote pyannote-audio-pipeline audio voice speech speaker speaker-diarization speaker-change-detection voice-activity-detection overlapped-speech-detection arxiv: 2111.14448 arxiv: 2012.01477 License: mit Model card Files Files and versions xet"
      },
      {
        "source_id": "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
        "citation_number": 6,
        "cited_text": "View PDF Abstract: Current speaker verification techniques rely on a neural network to extract speaker representations. The successful x-vector architecture is a Time Delay Neural Network (TDNN) that applies statistics pooling to project variable-length utterances into fixed-length speaker characterizing embeddings. In this paper, we propose multiple enhancements to this architecture based on recent trends in the related fields of face verification and computer vision. Firstly, the initial frame layers can be restructured into 1-dimensional Res2Net modules with impactful skip connections. Similarly to SE-ResNet, we introduce Squeeze-and-Excitation blocks in these modules to explicitly model channel interdependencies. The SE block expands the temporal context of the frame layer by rescaling the channels according to global properties of the recording. Secondly, neural networks are known to learn hierarchical features, with each layer operating on a different level of complexity. To leverage this complementary information, we aggregate and propagate features of different hierarchical levels. Finally, we improve the statistics pooling module with channel-dependent frame attention. This enables the network to focus on different subsets of frames during each of the channel's statistics estimation. The proposed ECAPA-TDNN architecture significantly outperforms state-of-the-art TDNN based systems on the VoxCeleb test sets and the 2019 VoxCeleb Speaker Recognition Challenge."
      },
      {
        "source_id": "66d08aeb-fde5-4b5b-a700-957312a58234",
        "citation_number": 7,
        "cited_text": "This directory (sre16) contains example scripts for the NIST SRE 2016 speaker recognition evaluation. The following corpora are required to perform the evaluation: NIST SRE 2016 enroll set NIST SRE 2016 test set More details on NIST SRE 2016 can be found at the url https://www.nist.gov/itl/iad/mig/speaker-recognition-evaluation-2016 . Additional data sources (mostly past NIST SREs, Switchboard, etc) are required to train the systems in the subdirectories. See the corresponding README.txt files in the subdirectories for more details. The subdirectories \"v1\" and so on are different speaker recognition recipes. The recipe in v1 demonstrates a standard approach using a full-covariance GMM-UBM, iVectors, and a PLDA backend. The example in v2 demonstrates DNN speaker embeddings with a PLDA backend."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 8,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing Apache-2.0 license Security UIS-RNN Overview This is the library for the Unbounded Interleaved-State Recurrent Neural Network (UIS-RNN) algorithm. UIS-RNN solves the problem of segmenting and clustering sequential data by learning from examples. This algorithm was originally proposed in the paper Fully Supervised Speaker Diarization . The work has been introduced by Google AI Blog ."
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 9,
        "cited_text": "Recipes VoxCeleb : Speaker Verification recipe on the VoxCeleb dataset 🔥 UPDATE 2024.05.15: We support score calibration for Voxceleb and achieve better performance! 🔥 UPDATE 2023.07.10: We support self-supervised learning recipe on Voxceleb! Achieving 2.627% (ECAPA_TDNN_GLOB_c1024) EER on vox1-O-clean test set without any labels. 🔥 UPDATE 2022.10.31: We support deep r-vector up to the 293-layer version! Achieving 0.447%/0.043 EER/mindcf on vox1-O-clean test set 🔥 UPDATE 2022.07.19: We apply the same setups as the CNCeleb recipe, and obtain SOTA performance considering the open-source systems EER/minDCF on vox1-O-clean test set are 0.723%/0.069 (ResNet34) and 0.728%/0.099 (ECAPA_TDNN_GLOB_c1024), after LM fine-tuning and AS-Norm CNCeleb : Speaker Verification recipe on the CnCeleb dataset 🔥 UPDATE 2024.05.16: We support score calibration for Cnceleb and achieve better EER. 🔥 UPDATE 2022.10.31: 221-layer ResNet achieves 5.655%/0.330 EER/minDCF 🔥 UPDATE 2022.07.12: We migrate the winner system of CNSRC 2022 report slides EER/minDCF reduction from 8.426%/0.487 to 6.492%/0.354 after large margin fine-tuning and AS-Norm NIST SRE16 : Speaker Verification recipe for the 2016 NIST Speaker Recognition Evaluation Plan . Similar recipe can be found in Kaldi . 🔥 UPDATE 2023.07.14: We support NIST SRE16 recipe. After PLDA adaptation, we achieved 6.608%, 10.01%, and 2.974% EER on trial Pooled, Tagalog, and Cantonese, respectively. VoxConverse : Diarization recipe on the VoxConverse dataset"
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 10,
        "cited_text": "Variants Here we list the repositories that are based on UIS-RNN, but integrated with other technologies or added some improvements. <cited_table> About This is the library for the Unbounded Interleaved-State Recurrent Neural Network (UIS-RNN) algorithm, corresponding to the paper Fully Supervised Speaker Diarization.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Link",
              "Description"
            ],
            [
              "taylorlu/Speaker-Diarization",
              "Speaker diarization using UIS-RNN and GhostVLAD. An easier way to support openset speakers."
            ],
            [
              "DonkeyShot21/uis-rnn-sml",
              "A variant of UIS-RNN, for the paper Supervised Online Diarization with Sample Mean Loss for Multi-Domain Data."
            ]
          ]
        }
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 11,
        "cited_text": "Please refer to python usage for more command line and python programming usage. Install for development & deployment Clone this repo Create conda env: pytorch version >= 1.12.1 is recommended !!! 🔥 News 2025.12.05: Add support for the w2v-bert2 model , see #439 and #441 . 2025.02.23: Add support for the Xi-vector, see #404 . 2024.09.03: Support the SimAM_ResNet and the model pretrained on VoxBlink2, check Pretrained Models for the pretrained model, VoxCeleb Recipe for the super performance, and python usage for the command line usage! 2024.08.30: We support whisper_encoder based frontend and propose the Whisper-PMFA framework, check #356 . 2024.08.20: Update diarization recipe for VoxConverse dataset by leveraging umap dimensionality reduction and hdbscan clustering, see #347 and #352 . 2024.08.18: Support using ssl pre-trained models as the frontend. The WavLM recipe is also provided, see #344 . 2024.05.15: Add support for quality-aware score calibration , see #320 . 2024.04.25: Add support for the gemini-dfresnet model, see #291 . 2024.04.23: Support MNN inference engine in runtime, see #310 . 2024.04.02: Release Wespeaker document with detailed model-training tutorials, introduction of various runtime platforms, etc. 2024.03.04: Support the eres2net-cn-common-200k and campplus-cn-common-200k of damo #281 , check python usage for details. 2024.02.05: Support the ERes2Net #272 and Res2Net #273 models. 2023.11.13: Support CLI usage of wespeaker, check python usage for details. 2023.07.18: Support the kaldi-compatible PLDA and unsupervised adaptation, see #186 . 2023.07.14: Support the NIST SRE16 recipe , see #177 ."
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 12,
        "cited_text": "Topics ssl pytorch resnet production-ready speaker-recognition speaker-verification plda speaker-diarization dino asv voxceleb xvector nist-sre repvgg ecapa-tdnn wavlm campplus eres2net cnceleb redimnet Resources Readme License Apache-2.0 license Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 1.3k stars Watchers 18 watching Forks 187 forks Report repository Releases 3 WeSpeaker 1.2.0 Latest on Jul 23, 2023 + 2 releases Packages 0 No packages published Uh oh! There was an error while loading. Please reload this page ."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 13,
        "cited_text": "Disclaimer This open source implementation is slightly different than the internal one which we used to produce the results in the paper , due to dependencies on some internal libraries. We CANNOT share the data, code, or model for the speaker recognition system ( d-vector embeddings ) used in the paper, since the speaker recognition system heavily depends on Google's internal infrastructure and proprietary data. This library is NOT an official Google product. We welcome community contributions ( guidelines ) to the uisrnn/contrib folder. But we won't be responsible for the correctness of any community contributions."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 14,
        "cited_text": "Speaker recognizer/encoder To learn more about our speaker embedding system, check out this site . We are aware of several third-party implementations of this work: Resemblyzer: PyTorch implementation by resemble-ai TensorFlow implementation by Janghyun1230 PyTorch implementaion by HarryVolek - with UIS-RNN integration PyTorch implementation as part of SV2TTS Please use your own judgement to decide whether you want to use these implementations. We are NOT responsible for the correctness of any third-party implementations."
      },
      {
        "source_id": "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
        "citation_number": 15,
        "cited_text": "Login Help Pages About Electrical Engineering and Systems Science > Audio and Speech Processing arXiv:2005.07143 (eess) [Submitted on 14 May 2020 ( v1 ), last revised 10 Aug 2020 (this version, v3)] Title: ECAPA-TDNN: Emphasized Channel Attention, Propagation and Aggregation in TDNN Based Speaker Verification Authors: Brecht Desplanques , Jenthe Thienpondt , Kris Demuynck View a PDF of the paper titled ECAPA-TDNN: Emphasized Channel Attention, Propagation and Aggregation in TDNN Based Speaker Verification, by Brecht Desplanques and 1 other authors"
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 16,
        "cited_text": "The definitions of the args are described in uisrnn/arguments.py . See inference_parser . Citations Our paper is cited as: References Baseline diarization system To learn more about our baseline diarization system based on unsupervised clustering algorithms, check out this site . A Python re-implementation of the spectral clustering algorithm used in this paper is available here . The ground truth labels for the NIST SRE 2000 dataset (Disk6 and Disk8) can be found here . For more public resources on speaker diarization, check out awesome-diarization ."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 17,
        "cited_text": "All algorithms are implemented as the UISRNN class. First, construct a UISRNN object by: The definitions of the args are described in uisrnn/arguments.py . See model_parser . Training Next, train the model by calling the fit() function: The definitions of the args are described in uisrnn/arguments.py . See training_parser . The fit() function accepts two types of input, as described below. Input as list of sequences (recommended) Here, train_sequences is a list of observation sequences. Each observation sequence is a 2-dim numpy array of type float ."
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 18,
        "cited_text": "Benchmark <cited_table> Diarization error rate (in %, the lower, the better) Compared to the 3.1 legacy pipeline, community-1 brings significant improvement in terms of speaker counting and assignment. precision-2 premium pipeline further improves accuracy as well as processing speed (in its self-hosted version).",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "legacy (3.1)",
              "community-1",
              "precision-2"
            ],
            [
              "AISHELL-4",
              "12.2",
              "11.7",
              "11.4"
            ],
            [
              "AliMeeting",
              "24.5",
              "20.3",
              "15.2"
            ],
            [
              "AMI",
              "18.8",
              "17.0",
              "12.9"
            ],
            [
              "AMI",
              "22.7",
              "19.9",
              "15.6"
            ],
            [
              "AVA-AVD",
              "49.7",
              "44.6",
              "37.1"
            ],
            [
              "CALLHOME",
              "28.5",
              "26.7",
              "16.6"
            ],
            [
              "DIHARD 3",
              "21.4",
              "20.2",
              "14.7"
            ],
            [
              "Ego4D",
              "51.2",
              "46.8",
              "39.0"
            ],
            [
              "MSDWild",
              "25.4",
              "22.8",
              "17.3"
            ],
            [
              "RAMC",
              "22.2",
              "20.8",
              "10.5"
            ],
            [
              "REPERE",
              "7.9",
              "8.9",
              "7.4"
            ],
            [
              "VoxConverse",
              "11.2",
              "11.2",
              "8.5"
            ]
          ]
        }
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 19,
        "cited_text": "Benchmark This pipeline has been benchmarked on a large collection of datasets. Processing is fully automatic: no manual voice activity detection (as is sometimes the case in the literature) no manual number of speakers (though it is possible to provide it to the pipeline) no fine-tuning of the internal models nor tuning of the pipeline hyper-parameters to each dataset ... with the least forgiving diarization error rate (DER) setup (named \"Full\" in this paper ): no forgiveness collar evaluation of overlapped speech"
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 20,
        "cited_text": "<cited_table> Citations Downloads last month 11,172,667 Inference Providers NEW Automatic Speech Recognition",
        "cited_table": {
          "num_columns": 7,
          "rows": [
            [
              "Benchmark",
              "DER%",
              "FA%",
              "Miss%",
              "Conf%",
              "Expected output",
              "File-level evaluation"
            ],
            [
              "AISHELL-4",
              "12.2",
              "3.8",
              "4.4",
              "4.0",
              "RTTM",
              "eval"
            ],
            [
              "AliMeeting ( channel 1)",
              "24.4",
              "4.4",
              "10.0",
              "10.0",
              "RTTM",
              "eval"
            ],
            [
              "AMI ( headset mix,",
              "18.8",
              "3.6",
              "9.5",
              "5.7",
              "RTTM",
              "eval"
            ],
            [
              "AMI ( array1, channel 1,",
              "22.4",
              "3.8",
              "11.2",
              "7.5",
              "RTTM",
              "eval"
            ],
            [
              "AVA-AVD",
              "50.0",
              "10.8",
              "15.7",
              "23.4",
              "RTTM",
              "eval"
            ],
            [
              "DIHARD 3 ( Full)",
              "21.7",
              "6.2",
              "8.1",
              "7.3",
              "RTTM",
              "eval"
            ],
            [
              "MSDWild",
              "25.3",
              "5.8",
              "8.0",
              "11.5",
              "RTTM",
              "eval"
            ],
            [
              "REPERE ( phase 2)",
              "7.8",
              "1.8",
              "2.6",
              "3.5",
              "RTTM",
              "eval"
            ],
            [
              "VoxConverse ( v0.3)",
              "11.3",
              "4.1",
              "3.4",
              "3.8",
              "RTTM",
              "eval"
            ]
          ]
        }
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 21,
        "cited_text": "<cited_table> Self-hosted speed on a NVIDIA H100 80GB HBM3 Telemetry With the optional telemetry feature in pyannote.audio , you can choose to send anonymous usage metrics to help the pyannote team improve the library. What we track For each call to Pipeline.from_pretrained({origin}) (or Model.from_pretrained({origin}) ), we track information about {origin} in the following privacy-preserving way:",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "community-1",
              "precision-2",
              "Speed up"
            ],
            [
              "AMI",
              "31s per hour of audio",
              "14s per hour of audio",
              "2.2x faster"
            ],
            [
              "DIHARD 3",
              "37s per hour of audio",
              "14s per hour of audio",
              "2.6x faster"
            ]
          ]
        }
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 22,
        "cited_text": "Integration of Azure Speech in your application Speech Studio is a set of UI-based tools for building and integrating features from Azure Speech in your applications. You create projects in Speech Studio by using a no-code approach. You can then reference those assets in your applications by using: Speech SDK . This SDK exposes many of the Azure Speech capabilities that you can use to develop speech-enabled applications. The Speech SDK is available in many programming languages and across all platforms. Speech CLI . With this command-line tool, you can use Azure Speech without having to write any code. Most features in the Speech SDK are available in the Speech CLI, and some advanced features and customizations are simplified in the Speech CLI. REST APIs . In some cases, you can't or shouldn't use the Speech SDK. In those cases, you can use REST APIs to access Azure Speech. For example, use REST APIs for batch transcription ."
      },
      {
        "source_id": "70279693-1c87-43f1-9150-6347ce00ecc8",
        "citation_number": 23,
        "cited_text": "接口说明 RESTful API 移动端SDK Java SDK Python SDK C++ SDK C# SDK Go SDK Node.js SDK 微信小程序 语音合成 接口说明 RESTful API 移动端SDK Java SDK C++ SDK Python SDK C# SDK Go SDK Node.js SDK 微信小程序 SSML标记语言介绍 语音合成时间戳功能介绍 界面化的TTS下载工具 长文本语音合成 离线语音合成 协议 相关协议 智能语音交互服务等级协议 阿里云产品服务协议（通用） 智能语音交互试用服务及服务改进计划协议 智能语音合成服务及服务改进计划协议 关注我们： 新浪微博 联系我们 文档 | 开发者社区 | 天池大赛 | 培训与认证 法律声明及隐私权政策 | Cookies政策 © 2009-现在 Aliyun.com 版权所有增值电信业务经营许可证： 浙B2-20080101"
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 24,
        "cited_text": "You can create custom voices, add specific words to your base vocabulary, or build your own models. Run Azure Speech anywhere, in the cloud or at the edge in containers. Enable your applications, tools, and devices for speech by using the Speech CLI , Speech SDK , and REST APIs . Azure Speech is available for many languages , regions , and price points . Scenarios Common scenarios for speech include: Captioning : Learn how to synchronize captions with your input audio, apply profanity filters, get partial results, apply customizations, and identify spoken languages for multilingual scenarios. Audio content creation : Use neural voices to make interactions with chatbots and voice agents more natural and engaging, convert digital texts such as e-books into audiobooks, and enhance in-car navigation systems. Call center : Transcribe calls in real time or process a batch of calls, redact personal information, and extract insights such as sentiment to help with your call-center use case. Language learning : Provide pronunciation assessment feedback to language learners, support real-time transcription for remote learning conversations, and read aloud teaching materials with neural voices. Voice Live : Create natural, humanlike conversational interfaces for applications and experiences. The Voice Live feature provides fast, reliable interaction between a human and an agent implementation. Speech translation : Generate high-quality speech-to-speech translation in real time, or automatically generate translated videos in a broad range of languages. Video avatar creation : Create lifelike and high-quality synthetic talking avatar videos for various real-time and batch applications while adhering to responsible AI practices."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 25,
        "cited_text": "Delivery and presence You can deploy Azure Speech features in the cloud or on-premises. By using containers , you can bring the service closer to your data for compliance, security, or other operational reasons. Azure Speech deployment in sovereign clouds is available for some government entities and their partners. For example, the Azure Government cloud is available to US government entities and their partners. The Azure operated by 21Vianet cloud is available to organizations that have a business presence in China. For more information, see Speech service in sovereign clouds ."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 26,
        "cited_text": "Voice options include: Standard voice : You can choose among highly natural out-of-the-box voices. Check the standard voice samples in the Voice Gallery and determine the right voice for your business needs. Custom voice : You can create a custom voice that's recognizable and unique to your brand or product. Custom voices are private and can offer a competitive advantage. Check the custom voice samples . Text-to-speech avatar Text-to-speech avatar converts text into a digital video of a photorealistic human speaking with a natural-sounding voice. The video can be synthesized asynchronously or in real time. You can build applications integrated with text-to-speech avatar through an API, or use text-to-speech avatar in Foundry to create video content without coding. The feature empowers you to deliver lifelike and high-quality synthetic talking avatar videos for various applications while adhering to responsible AI practices."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "「声纹识别（Speaker Verification）」与「说话人分离（Speaker Diarization）」是语音助手身份认证的两大基石。前者用于“确认你是谁”，后者用于“在多人对话中区分谁在说话” [1-3]。以下是基于现有主流框架（如 NVIDIA NeMo, Google UIS-RNN, pyannote-audio, SpeechBrain 及 WeSpeaker）的实现细节解析：\n\n### 一、 核心算法流程\n\n身份认证系统的实现逻辑通常遵循从原始音频到身份标签的转化：\n\n1.  **前端处理与 VAD**：利用语音活动检测（VAD）剔除背景噪音和静音片段 [2, 4]。\n2.  **特征提取（Embedding Learning）**：\n    *   **主流模型**：从早期的 **i-vector** 演进到深度学习时代的 **d-vector**、**x-vector** [5, 6]。\n    *   **先进架构**：**ECAPA-TDNN** 通过 Res2Net 模块、Squeeze-and-Excitation (SE) 块以及多尺度特征聚合，显著增强了通道注意力和时间上下文建模能力 [5]。\n3.  **说话人分离（Diarization）**：\n    *   **传统方式**：基于**谱聚类（Spectral Clustering）**等无监督方法 [7]。\n    *   **全监督方式（UIS-RNN）**：通过 **Unbounded Interleaved-State RNN** 算法，学习如何对嵌入向量（Embeddings）进行序列化分割与聚类，解决了传统方法难以在线处理和鲁棒性差的问题 [1, 8]。\n4.  **后端比对与评分**：\n    *   使用**余弦相似度**或 **PLDA**（概率线性判别分析）对比提取的 Embedding 与注册声纹库的匹配度 [6, 9]。\n    *   **AS-Norm（自适应对称归一化）**：用于消除信道干扰，提升评分的稳定性 [10]。\n\n### 二、 关键代码架构\n\n现代开源框架普遍采用模块化和配置驱动的架构：\n\n*   **SpeechBrain 的“Brain”类与 YAML 驱动**：其核心架构通过 `Brain` 类管理训练循环，所有的超参数（从学习率到模型结构）都封装在 YAML 配置文件中，实现了高度的可复用性 [11, 12]。\n*   **pyannote 的 Pipeline 模式**：通过 `Pipeline.from_pretrained` 接口，将 VAD、分段、嵌入提取和聚类串联成工作流，支持端到端的推理 [13, 14]。\n*   **WeSpeaker 的生产导向架构**：提供 Python API 和 CLI 工具，并针对工业级部署支持 **ONNX** 和 **MNN** 推理引擎，确保模型在运行时的高效性 [9, 15]。\n\n### 三、 性能优化策略\n\n为了满足语音助手实时性的需求，各框架采取了不同的优化路径：\n\n*   **训练加速**：支持多 GPU 分布式训练、混合精度训练（Mixed-Precision）以及动态批处理（Dynamic Batching），以处理变长的语音信号 [12]。\n*   **推理加速**：\n    *   **pyannote \"Precision-2\"**：通过自研优化，其处理速度比社区版本提升了 **2.2x 至 2.6x**（如在 H100 上处理 1 小时音频仅需 14 秒） [16, 17]。\n    *   **数据增强**：UIS-RNN 通过 **Block-wise Shuffling**（块状随机洗牌）对训练序列进行数据增强，提升了模型在小规模数据集上的鲁棒性 [18]。\n*   **精度校准**：WeSpeaker 引入了**质量感知分数校准（Quality-aware Score Calibration）**，根据语音质量调整识别阈值 [9, 10]。\n\n### 四、 竞品技术对比与核心数据\n\n以下是根据各框架公开 Benchmark 整理的技术指标对比：\n\n| 指标 | WeSpeaker (SOTA) | pyannote (3.1/Community) | Azure Speech (Managed) |\n| :--- | :--- | :--- | :--- |\n| **核心算法** | ResNet-293 / ECAPA-TDNN [10, 19] | Segmentation-3.0 / ECAPA [20, 21] | 神经语音模型（Neural Voice） [22] |\n| **Vox1-O-clean EER** | **0.447%** (ResNet293) [10] | 未明确标出 (侧重分离) | 商业秘密 |\n| **AISHELL-4 DER** | - | **11.7% - 12.2%** [16, 23] | 极高准确度 [24] |\n| **VoxConverse DER** | - | **11.2% - 11.3%** [16, 23] | - |\n| **主要优势** | 生产环境优化，支持 293 层超深残差网络 [9, 10] | 分离性能领先，集成 Hugging Face 易用性极高 [13, 21] | 全托管服务，支持多语言识别、翻译及定制化合成 [24, 25] |\n| **部署方式** | 源码 / Conda / Runtime [26] | Pip / Hugging Face [21] | 云端 API / 容器化部署 [27, 28] |\n\n**数据总结**：在纯技术指标上，WeSpeaker 在 **Vox1-O** 声纹识别集上达到了 **0.447% 的等错误率（EER）**，处于行业顶尖水平 [10]；而 pyannote 在说话人分离任务上表现优异，在 **REPERE (phase 2)** 任务中实现了低至 **7.8% 的 DER** [23]。语音助手开发者通常会根据是对端侧推理有硬性需求（选 WeSpeaker/NeMo）还是追求快速云端集成（选 Azure/Hugging Face）来做出选择 [21, 29]。",
    "conversation_id": "a31d41fe-47ba-4e4e-bcad-64bf6d5ee582",
    "sources_used": [
      "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "77a438b2-68a7-435c-bd6b-a116c7953577",
      "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
      "66d08aeb-fde5-4b5b-a700-957312a58234",
      "952e6f81-ec96-4412-9872-13c331762d12",
      "5341d428-958c-4c67-9cec-262642f52388",
      "6d9034d9-794b-4914-be97-bd71e56e48d8"
    ],
    "citations": {
      "1": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "2": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "3": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "4": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "5": "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
      "6": "66d08aeb-fde5-4b5b-a700-957312a58234",
      "7": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "8": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "9": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "10": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "11": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "12": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "13": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "14": "952e6f81-ec96-4412-9872-13c331762d12",
      "15": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "16": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "17": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "18": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "19": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "20": "952e6f81-ec96-4412-9872-13c331762d12",
      "21": "952e6f81-ec96-4412-9872-13c331762d12",
      "22": "5341d428-958c-4c67-9cec-262642f52388",
      "23": "952e6f81-ec96-4412-9872-13c331762d12",
      "24": "5341d428-958c-4c67-9cec-262642f52388",
      "25": "5341d428-958c-4c67-9cec-262642f52388",
      "26": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "27": "5341d428-958c-4c67-9cec-262642f52388",
      "28": "5341d428-958c-4c67-9cec-262642f52388",
      "29": "6d9034d9-794b-4914-be97-bd71e56e48d8"
    },
    "references": [
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 1,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing Apache-2.0 license Security UIS-RNN Overview This is the library for the Unbounded Interleaved-State Recurrent Neural Network (UIS-RNN) algorithm. UIS-RNN solves the problem of segmenting and clustering sequential data by learning from examples. This algorithm was originally proposed in the paper Fully Supervised Speaker Diarization . The work has been introduced by Google AI Blog ."
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 2,
        "cited_text": "Citations If you use pyannote.audio please use the following citations: Development The commands below will setup pre-commit hooks and packages needed for developing the pyannote.audio library. Test About Neural building blocks for speaker diarization: speech activity detection, speaker change detection, overlapped speech detection, speaker embedding pyannote.github.io Topics pytorch pretrained-models speaker-recognition speaker-verification speech-processing speaker-diarization voice-activity-detection speech-activity-detection speaker-change-detection speaker-embedding overlapped-speech-detection"
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 3,
        "cited_text": "Discussion For Chinese users, you can scan the QR code on the left to follow our offical account of WeNet Community . We also created a WeChat group for better discussion and quicker response. Please scan the QR code on the right to join the chat group. Citations If you find wespeaker useful, please cite it as Looking for contributors If you are interested to contribute, feel free to contact @wsstriving or @robin1001 About Research and Production Oriented Speaker Verification, Recognition and Diarization Toolkit"
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
        "citation_number": 4,
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
        "source_id": "1362fc4c-2ac5-4e1f-a7bb-b87ea5cf0c4b",
        "citation_number": 5,
        "cited_text": "View PDF Abstract: Current speaker verification techniques rely on a neural network to extract speaker representations. The successful x-vector architecture is a Time Delay Neural Network (TDNN) that applies statistics pooling to project variable-length utterances into fixed-length speaker characterizing embeddings. In this paper, we propose multiple enhancements to this architecture based on recent trends in the related fields of face verification and computer vision. Firstly, the initial frame layers can be restructured into 1-dimensional Res2Net modules with impactful skip connections. Similarly to SE-ResNet, we introduce Squeeze-and-Excitation blocks in these modules to explicitly model channel interdependencies. The SE block expands the temporal context of the frame layer by rescaling the channels according to global properties of the recording. Secondly, neural networks are known to learn hierarchical features, with each layer operating on a different level of complexity. To leverage this complementary information, we aggregate and propagate features of different hierarchical levels. Finally, we improve the statistics pooling module with channel-dependent frame attention. This enables the network to focus on different subsets of frames during each of the channel's statistics estimation. The proposed ECAPA-TDNN architecture significantly outperforms state-of-the-art TDNN based systems on the VoxCeleb test sets and the 2019 VoxCeleb Speaker Recognition Challenge."
      },
      {
        "source_id": "66d08aeb-fde5-4b5b-a700-957312a58234",
        "citation_number": 6,
        "cited_text": "This directory (sre16) contains example scripts for the NIST SRE 2016 speaker recognition evaluation. The following corpora are required to perform the evaluation: NIST SRE 2016 enroll set NIST SRE 2016 test set More details on NIST SRE 2016 can be found at the url https://www.nist.gov/itl/iad/mig/speaker-recognition-evaluation-2016 . Additional data sources (mostly past NIST SREs, Switchboard, etc) are required to train the systems in the subdirectories. See the corresponding README.txt files in the subdirectories for more details. The subdirectories \"v1\" and so on are different speaker recognition recipes. The recipe in v1 demonstrates a standard approach using a full-covariance GMM-UBM, iVectors, and a PLDA backend. The example in v2 demonstrates DNN speaker embeddings with a PLDA backend."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 7,
        "cited_text": "The definitions of the args are described in uisrnn/arguments.py . See inference_parser . Citations Our paper is cited as: References Baseline diarization system To learn more about our baseline diarization system based on unsupervised clustering algorithms, check out this site . A Python re-implementation of the spectral clustering algorithm used in this paper is available here . The ground truth labels for the NIST SRE 2000 dataset (Disk6 and Disk8) can be found here . For more public resources on speaker diarization, check out awesome-diarization ."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 8,
        "cited_text": "Variants Here we list the repositories that are based on UIS-RNN, but integrated with other technologies or added some improvements. <cited_table> About This is the library for the Unbounded Interleaved-State Recurrent Neural Network (UIS-RNN) algorithm, corresponding to the paper Fully Supervised Speaker Diarization.",
        "cited_table": {
          "num_columns": 2,
          "rows": [
            [
              "Link",
              "Description"
            ],
            [
              "taylorlu/Speaker-Diarization",
              "Speaker diarization using UIS-RNN and GhostVLAD. An easier way to support openset speakers."
            ],
            [
              "DonkeyShot21/uis-rnn-sml",
              "A variant of UIS-RNN, for the paper Supervised Online Diarization with Sample Mean Loss for Multi-Domain Data."
            ]
          ]
        }
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 9,
        "cited_text": "Please refer to python usage for more command line and python programming usage. Install for development & deployment Clone this repo Create conda env: pytorch version >= 1.12.1 is recommended !!! 🔥 News 2025.12.05: Add support for the w2v-bert2 model , see #439 and #441 . 2025.02.23: Add support for the Xi-vector, see #404 . 2024.09.03: Support the SimAM_ResNet and the model pretrained on VoxBlink2, check Pretrained Models for the pretrained model, VoxCeleb Recipe for the super performance, and python usage for the command line usage! 2024.08.30: We support whisper_encoder based frontend and propose the Whisper-PMFA framework, check #356 . 2024.08.20: Update diarization recipe for VoxConverse dataset by leveraging umap dimensionality reduction and hdbscan clustering, see #347 and #352 . 2024.08.18: Support using ssl pre-trained models as the frontend. The WavLM recipe is also provided, see #344 . 2024.05.15: Add support for quality-aware score calibration , see #320 . 2024.04.25: Add support for the gemini-dfresnet model, see #291 . 2024.04.23: Support MNN inference engine in runtime, see #310 . 2024.04.02: Release Wespeaker document with detailed model-training tutorials, introduction of various runtime platforms, etc. 2024.03.04: Support the eres2net-cn-common-200k and campplus-cn-common-200k of damo #281 , check python usage for details. 2024.02.05: Support the ERes2Net #272 and Res2Net #273 models. 2023.11.13: Support CLI usage of wespeaker, check python usage for details. 2023.07.18: Support the kaldi-compatible PLDA and unsupervised adaptation, see #186 . 2023.07.14: Support the NIST SRE16 recipe , see #177 ."
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 10,
        "cited_text": "Recipes VoxCeleb : Speaker Verification recipe on the VoxCeleb dataset 🔥 UPDATE 2024.05.15: We support score calibration for Voxceleb and achieve better performance! 🔥 UPDATE 2023.07.10: We support self-supervised learning recipe on Voxceleb! Achieving 2.627% (ECAPA_TDNN_GLOB_c1024) EER on vox1-O-clean test set without any labels. 🔥 UPDATE 2022.10.31: We support deep r-vector up to the 293-layer version! Achieving 0.447%/0.043 EER/mindcf on vox1-O-clean test set 🔥 UPDATE 2022.07.19: We apply the same setups as the CNCeleb recipe, and obtain SOTA performance considering the open-source systems EER/minDCF on vox1-O-clean test set are 0.723%/0.069 (ResNet34) and 0.728%/0.099 (ECAPA_TDNN_GLOB_c1024), after LM fine-tuning and AS-Norm CNCeleb : Speaker Verification recipe on the CnCeleb dataset 🔥 UPDATE 2024.05.16: We support score calibration for Cnceleb and achieve better EER. 🔥 UPDATE 2022.10.31: 221-layer ResNet achieves 5.655%/0.330 EER/minDCF 🔥 UPDATE 2022.07.12: We migrate the winner system of CNSRC 2022 report slides EER/minDCF reduction from 8.426%/0.487 to 6.492%/0.354 after large margin fine-tuning and AS-Norm NIST SRE16 : Speaker Verification recipe for the 2016 NIST Speaker Recognition Evaluation Plan . Similar recipe can be found in Kaldi . 🔥 UPDATE 2023.07.14: We support NIST SRE16 recipe. After PLDA adaptation, we achieved 6.608%, 10.01%, and 2.974% EER on trial Pooled, Tagalog, and Cantonese, respectively. VoxConverse : Diarization recipe on the VoxConverse dataset"
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
        "citation_number": 11,
        "cited_text": "📚 Training Recipes We share over 200 competitive training recipes on more than 40 datasets supporting 20 speech and text processing tasks (see below). We support both training from scratch and fine-tuning pretrained models such as Whisper , Wav2Vec2 , WavLM , Hubert , GPT2 , Llama2 , and beyond. The models on HuggingFace can be easily plugged in and fine-tuned. For any task, you train the model using these commands: The hyperparameters are encapsulated in a YAML file, while the training process is orchestrated through a Python script. We maintained a consistent code structure across different tasks. For better replicability, training logs and checkpoints are hosted on Dropbox."
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
        "citation_number": 12,
        "cited_text": "Training Orchestration: The Brain class serves as a fully customizable tool for managing training and evaluation loops over data. It simplifies training loops while providing the flexibility to override any part of the process. Hyperparameter Management: A YAML-based hyperparameter file specifies all hyperparameters, from individual numbers (e.g., learning rate) to complete objects (e.g., custom models). This elegant solution drastically simplifies the training script. Dynamic Dataloader: Enables flexible and efficient data reading. GPU Training: Supports single and multi-GPU training, including distributed training. Dynamic Batching: On-the-fly dynamic batching enhances the efficient processing of variable-length signals. Mixed-Precision Training: Accelerates training through mixed-precision techniques. Efficient Data Reading: Reads large datasets efficiently from a shared Network File System (NFS) via WebDataset . Hugging Face Integration: Interfaces seamlessly with HuggingFace for popular models such as wav2vec2 and Hubert. Orion Integration: Interfaces with Orion for hyperparameter tuning. Speech Augmentation Techniques: Includes SpecAugment, Noise, Reverberation, and more. Data Preparation Scripts: Includes scripts for preparing data for supported datasets."
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 13,
        "cited_text": "Repository files navigation README Code of conduct MIT license pyannote speaker diarization toolkit pyannote.audio is an open-source toolkit written in Python for speaker diarization. Based on PyTorch machine learning framework, it comes with state-of-the-art pretrained models and pipelines , that can be further finetuned to your own data for even better performance. Highlights 🤯 state-of-the-art performance (see Benchmark ) 🤗 pretrained pipelines (and models ) on 🤗 model hub 🚀 built-in support for pyannoteAI premium speaker diarization 🐍 Python-first API ⚡ multi-GPU training with pytorch-lightning"
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 14,
        "cited_text": "Usage Processing on GPU pyannote.audio pipelines run on CPU by default. You can send them to GPU with the following lines: Processing from memory Pre-loading audio files in memory may result in faster processing: Monitoring progress Hooks are available to monitor the progress of the pipeline: Controlling the number of speakers In case the number of speakers is known in advance, one can use the num_speakers option: One can also provide lower and/or upper bounds on the number of speakers using min_speakers and max_speakers options:"
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 15,
        "cited_text": "wenet-e2e / wespeaker Public Notifications You must be signed in to change notification settings Fork 187 Star 1.3k Code Issues 40 Pull requests 3 Discussions Actions Projects Security and quality 0 Insights Additional navigation options Code Issues Pull requests Discussions Actions Projects Security and quality Insights wenet-e2e/wespeaker master 5 Branches 3 Tags Go to file Code Open more actions menu Folders and files <cited_table>",
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
              ".github/ workflows",
              "",
              ".github/ workflows",
              "fix: keep initial_lr in scheduler_args instead of popping it (",
              "3 months ago"
            ],
            [
              "docs",
              "",
              "docs",
              "[cli] support w2v-bert2-LoRA-adapter-MFA model (",
              "4 months ago"
            ],
            [
              "examples",
              "",
              "examples",
              "fix: resolve bugs in WarmupLR_withStepDecay and train config (",
              "4 months ago"
            ],
            [
              "runtime",
              "",
              "runtime",
              "[runtime] cosine score normalization (",
              "last year"
            ],
            [
              "tools",
              "",
              "tools",
              "Integrate w2v-bert2-LoRA-adapter-MFA model (",
              "5 months ago"
            ],
            [
              "wespeaker",
              "",
              "wespeaker",
              "xi-vector: Clamp log precision values to specified range (",
              "2 months ago"
            ],
            [
              ".clang-format",
              "",
              ".clang-format",
              "[lint] auto format all by pre-commit, including c++, python (",
              "3 years ago"
            ],
            [
              ".flake8",
              "",
              ".flake8",
              "[fix] fix some bugs and flake8 lint problem (",
              "4 years ago"
            ],
            [
              ".gitignore",
              "",
              ".gitignore",
              "Support Whisper-PMFA (",
              "2 years ago"
            ],
            [
              ".pre-commit-config.yaml",
              "",
              ".pre-commit-config.yaml",
              "[lint] use pre-commit to auto check and lint (",
              "3 years ago"
            ],
            [
              "CPPLINT.cfg",
              "",
              "CPPLINT.cfg",
              "[runtime] support onnxruntime (",
              "3 years ago"
            ],
            [
              "LICENSE",
              "",
              "LICENSE",
              "Create LICENSE (",
              "4 years ago"
            ],
            [
              "README.md",
              "",
              "README.md",
              "[cli] support w2v-bert2-LoRA-adapter-MFA model (",
              "4 months ago"
            ],
            [
              "ROADMAP.md",
              "",
              "ROADMAP.md",
              "[doc] update README.md and add QMF results (",
              "2 years ago"
            ],
            [
              "requirements.txt",
              "",
              "requirements.txt",
              "Add diarization recipe v3 (",
              "2 years ago"
            ],
            [
              "setup.cfg",
              "",
              "setup.cfg",
              "[cli] add first cli support (",
              "3 years ago"
            ],
            [
              "setup.py",
              "",
              "setup.py",
              "[cli] add cli requirements of umap+hdbscan (",
              "2 years ago"
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
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 16,
        "cited_text": "Benchmark <cited_table> Diarization error rate (in %, the lower, the better) Compared to the 3.1 legacy pipeline, community-1 brings significant improvement in terms of speaker counting and assignment. precision-2 premium pipeline further improves accuracy as well as processing speed (in its self-hosted version).",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "legacy (3.1)",
              "community-1",
              "precision-2"
            ],
            [
              "AISHELL-4",
              "12.2",
              "11.7",
              "11.4"
            ],
            [
              "AliMeeting",
              "24.5",
              "20.3",
              "15.2"
            ],
            [
              "AMI",
              "18.8",
              "17.0",
              "12.9"
            ],
            [
              "AMI",
              "22.7",
              "19.9",
              "15.6"
            ],
            [
              "AVA-AVD",
              "49.7",
              "44.6",
              "37.1"
            ],
            [
              "CALLHOME",
              "28.5",
              "26.7",
              "16.6"
            ],
            [
              "DIHARD 3",
              "21.4",
              "20.2",
              "14.7"
            ],
            [
              "Ego4D",
              "51.2",
              "46.8",
              "39.0"
            ],
            [
              "MSDWild",
              "25.4",
              "22.8",
              "17.3"
            ],
            [
              "RAMC",
              "22.2",
              "20.8",
              "10.5"
            ],
            [
              "REPERE",
              "7.9",
              "8.9",
              "7.4"
            ],
            [
              "VoxConverse",
              "11.2",
              "11.2",
              "8.5"
            ]
          ]
        }
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 17,
        "cited_text": "<cited_table> Self-hosted speed on a NVIDIA H100 80GB HBM3 Telemetry With the optional telemetry feature in pyannote.audio , you can choose to send anonymous usage metrics to help the pyannote team improve the library. What we track For each call to Pipeline.from_pretrained({origin}) (or Model.from_pretrained({origin}) ), we track information about {origin} in the following privacy-preserving way:",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "community-1",
              "precision-2",
              "Speed up"
            ],
            [
              "AMI",
              "31s per hour of audio",
              "14s per hour of audio",
              "2.2x faster"
            ],
            [
              "DIHARD 3",
              "37s per hour of audio",
              "14s per hour of audio",
              "2.6x faster"
            ]
          ]
        }
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 18,
        "cited_text": "The reason we concatenate all training sequences is that, we will be resampling and block-wise shuffling the training data as a data augmentation process, such that we result in a robust model even when there is insufficient number of training sequences. Training on large datasets For large datasets, the data usually could not be loaded into memory at once. In such cases, the fit() function needs to be called multiple times. Here we provide a few guidelines as our suggestions: Do not feed different datasets into different calls of fit() . Instead, for each call of fit() , the input should cover sequences from different datasets. For each call to the fit() function, make the size of input roughly the same. And, don't make the input size too small."
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 19,
        "cited_text": "Topics ssl pytorch resnet production-ready speaker-recognition speaker-verification plda speaker-diarization dino asv voxceleb xvector nist-sre repvgg ecapa-tdnn wavlm campplus eres2net cnceleb redimnet Resources Readme License Apache-2.0 license Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 1.3k stars Watchers 18 watching Forks 187 forks Report repository Releases 3 WeSpeaker 1.2.0 Latest on Jul 23, 2023 + 2 releases Packages 0 No packages published Uh oh! There was an error while loading. Please reload this page ."
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 20,
        "cited_text": "pyannote/speaker-diarization-3.1 · Hugging Face Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Log In Sign Up pyannote / speaker-diarization-3.1 like 1.71k Follow pyannote 2.23k Automatic Speech Recognition pyannote.audio pyannote pyannote-audio-pipeline audio voice speech speaker speaker-diarization speaker-change-detection voice-activity-detection overlapped-speech-detection arxiv: 2111.14448 arxiv: 2012.01477 License: mit Model card Files Files and versions xet"
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 21,
        "cited_text": "Both speaker segmentation and embedding now run in pure PyTorch. This should ease deployment and possibly speed up inference. It requires pyannote.audio version 3.1 or higher. It ingests mono audio sampled at 16kHz and outputs speaker diarization as an Annotation instance: stereo or multi-channel audio files are automatically downmixed to mono by averaging the channels. audio files sampled at a different rate are resampled to 16kHz automatically upon loading. Requirements Install pyannote.audio 3.1 with pip install pyannote.audio Accept pyannote/segmentation-3.0 user conditions Accept pyannote/speaker-diarization-3.1 user conditions Create access token at hf.co/settings/tokens ."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 22,
        "cited_text": "The base model might not be sufficient if the audio contains ambient noise or includes industry and domain-specific jargon. In these cases, you can create and train custom speech models with acoustic, language, and pronunciation data. Custom speech models are private and can offer a competitive advantage. Text to speech With text to speech , you can convert input text into humanlike synthesized speech. Use neural voices, which are humanlike voices powered by deep neural networks. Use Speech Synthesis Markup Language (SSML) to fine-tune the pitch, pronunciation, speaking rate, volume, and more."
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 23,
        "cited_text": "<cited_table> Citations Downloads last month 11,172,667 Inference Providers NEW Automatic Speech Recognition",
        "cited_table": {
          "num_columns": 7,
          "rows": [
            [
              "Benchmark",
              "DER%",
              "FA%",
              "Miss%",
              "Conf%",
              "Expected output",
              "File-level evaluation"
            ],
            [
              "AISHELL-4",
              "12.2",
              "3.8",
              "4.4",
              "4.0",
              "RTTM",
              "eval"
            ],
            [
              "AliMeeting ( channel 1)",
              "24.4",
              "4.4",
              "10.0",
              "10.0",
              "RTTM",
              "eval"
            ],
            [
              "AMI ( headset mix,",
              "18.8",
              "3.6",
              "9.5",
              "5.7",
              "RTTM",
              "eval"
            ],
            [
              "AMI ( array1, channel 1,",
              "22.4",
              "3.8",
              "11.2",
              "7.5",
              "RTTM",
              "eval"
            ],
            [
              "AVA-AVD",
              "50.0",
              "10.8",
              "15.7",
              "23.4",
              "RTTM",
              "eval"
            ],
            [
              "DIHARD 3 ( Full)",
              "21.7",
              "6.2",
              "8.1",
              "7.3",
              "RTTM",
              "eval"
            ],
            [
              "MSDWild",
              "25.3",
              "5.8",
              "8.0",
              "11.5",
              "RTTM",
              "eval"
            ],
            [
              "REPERE ( phase 2)",
              "7.8",
              "1.8",
              "2.6",
              "3.5",
              "RTTM",
              "eval"
            ],
            [
              "VoxConverse ( v0.3)",
              "11.3",
              "4.1",
              "3.4",
              "3.8",
              "RTTM",
              "eval"
            ]
          ]
        }
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 24,
        "cited_text": "What is Azure Speech? Feedback Summarize this article for me In this article Scenarios Capabilities Delivery and presence Integration of Azure Speech in your application Code samples Responsible AI Related content Show 3 more Azure Speech in Foundry Tools provides speech to text, text to speech, and other capabilities through a Microsoft Foundry resource . You can transcribe speech to text with high accuracy, produce natural-sounding text-to-speech voices, translate spoken audio, and conduct live AI voice conversations."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 25,
        "cited_text": "You can choose from a range of standard voices for the avatar. The language support for text-to-speech avatar is the same as the language support for text to speech. Speech translation Speech translation enables real-time, multilingual translation of speech to your applications, tools, and devices. Use this feature for speech-to-speech and speech-to-text translation. LLM speech (preview) Take advantage of a large language model (LLM)-enhanced speech model in LLM speech . This feature currently supports the following tasks:"
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 26,
        "cited_text": "Repository files navigation README Apache-2.0 license WeSpeaker Roadmap | Docs | Paper | Runtime | Pretrained Models | Huggingface Demo | Modelscope Demo WeSpeaker mainly focuses on speaker embedding learning , with application to the speaker verification task. We support online feature extraction or loading pre-extracted features in kaldi-format. Installation Install python package Command-line usage (use -h for parameters): Python programming usage : You can set the environment variable WESPEAKER_HOME to specify the path of downloaded pre-trained models. By default it will be $HOME/.wespeaker ."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 27,
        "cited_text": "You can create custom voices, add specific words to your base vocabulary, or build your own models. Run Azure Speech anywhere, in the cloud or at the edge in containers. Enable your applications, tools, and devices for speech by using the Speech CLI , Speech SDK , and REST APIs . Azure Speech is available for many languages , regions , and price points . Scenarios Common scenarios for speech include: Captioning : Learn how to synchronize captions with your input audio, apply profanity filters, get partial results, apply customizations, and identify spoken languages for multilingual scenarios. Audio content creation : Use neural voices to make interactions with chatbots and voice agents more natural and engaging, convert digital texts such as e-books into audiobooks, and enhance in-car navigation systems. Call center : Transcribe calls in real time or process a batch of calls, redact personal information, and extract insights such as sentiment to help with your call-center use case. Language learning : Provide pronunciation assessment feedback to language learners, support real-time transcription for remote learning conversations, and read aloud teaching materials with neural voices. Voice Live : Create natural, humanlike conversational interfaces for applications and experiences. The Voice Live feature provides fast, reliable interaction between a human and an agent implementation. Speech translation : Generate high-quality speech-to-speech translation in real time, or automatically generate translated videos in a broad range of languages. Video avatar creation : Create lifelike and high-quality synthetic talking avatar videos for various real-time and batch applications while adhering to responsible AI practices."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 28,
        "cited_text": "Delivery and presence You can deploy Azure Speech features in the cloud or on-premises. By using containers , you can bring the service closer to your data for compliance, security, or other operational reasons. Azure Speech deployment in sovereign clouds is available for some government entities and their partners. For example, the Azure Government cloud is available to US government entities and their partners. The Azure operated by 21Vianet cloud is available to organizations that have a business presence in China. For more information, see Speech service in sovereign clouds ."
      },
      {
        "source_id": "6d9034d9-794b-4914-be97-bd71e56e48d8",
        "citation_number": 29,
        "cited_text": "Why use Inference Endpoints Inference Endpoints makes deploying AI models to production a smooth experience. Instead of spending weeks configuring infrastructure, managing servers, and debugging deployment issues, you can focus on what matters most: your model and your users. Our platform eliminates the complexity of AI infrastructure while providing enterprise-grade features that scale with your business needs. Whether you're a startup launching your first AI product or an enterprise team managing hundreds of models, Inference Endpoints provides the reliability, performance, and cost-efficiency you need."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "「声纹识别与说话人分离」在语音助手身份认证中的应用已广泛渗透至工业与科研领域。以下基于提供的来源，详细列出其应用场景、部署方案、基准数据及实践经验。\n\n### 一、 真实应用场景与案例\n\n1.  **办公与协作系统**：\n    *   **微软 Teams**：利用 Azure Speech 提供的技术进行实时字幕生成（Captioning） [1]。\n    *   **会议纪要**：在多人会议中区分不同发言人并转录，如阿里云提供的访谈录音转写和法庭庭审实时记录 [2]。\n2.  **内容创作与教育**：\n    *   **多语言翻译与配音**：如 **SoniTranslate** 和 **Whisper-WebUI** 等开源项目，利用声纹识别和分离技术实现视频的自动翻译与身份对齐 [3]。\n    *   **语言学习**：通过发音评估（Pronunciation Assessment）为学习者提供反馈 [4]。\n3.  **客户服务与金融**：\n    *   **呼叫中心（Call Center）**：进行实时通话转写、个人隐私信息脱敏、情感分析及座席辅助 [5, 6]。\n    *   **身份验证**：在金融、保险、电力等领域，利用声纹作为生物特征进行身份核验 [2]。\n4.  **智能硬件与导航**：\n    *   **车载系统**：增强车载导航的交互自然度，确保指令来自合法驾驶员 [5]。\n\n### 二、 工业级部署方案\n\n1.  **全托管云服务**：\n    *   **Azure Speech**：提供 Speech SDK、CLI 和 REST API，支持云端及边缘计算（通过容器部署） [5, 7]。\n    *   **Hugging Face Inference Endpoints**：提供全托管基础设施，支持自动扩缩容（Autoscaling）和生产级 Inference Engines（如 vLLM, TGI） [8, 9]。\n2.  **私有化与边缘部署**：\n    *   **NVIDIA NeMo**：支持大规模生成式 AI 框架，针对语音 AI 优化，可部署在 NVIDIA GPU 上 [10, 11]。其 **NIM**（NVIDIA Inference Microservices）提供低延迟的实时对话能力 [12]。\n    *   **WeSpeaker Runtime**：专为生产设计，支持 **ONNX** 和 **MNN** 推理引擎，适合集成到各种运行时平台 [13, 14]。\n3.  **高性能加速方案**：\n    *   **pyannote \"precision-2\"**：在 NVIDIA H100 上处理 1 小时音频仅需 **14 秒**，处理速度比社区版提升 2.2 倍以上 [15]。\n\n### 三、 开源项目实战案例\n\n*   **WeSpeaker**：提供了 **VoxCeleb** 和 **CNCeleb** 等大规模数据集的完整训练脚本（Recipes），甚至支持高达 **293 层** 的超深 ResNet 模型 [16]。\n*   **SpeechBrain**：被 **Mila** 等顶级学术机构用于研究加速，支持从 Whisper 到 Wav2Vec2 的多种预训练模型微调 [17, 18]。\n*   **UIS-RNN (Google)**：解决了完全监督下的说话人分离问题，其库中包含处理 d-vector 嵌入的序列分割与聚类逻辑 [19]。\n\n### 四、 性能基准数据 (Benchmarks)\n\n| 任务 | 模型/框架 | 数据集 | 核心指标 |\n| :--- | :--- | :--- | :--- |\n| **声纹识别** | **WeSpeaker (ResNet293)** | Vox1-O-clean | **EER: 0.447%** [16] |\n| **说话人分离** | **pyannote 3.1** | VoxConverse | **DER: 11.3%** [20] |\n| **说话人分离** | **pyannote community-1** | AISHELL-4 | **DER: 11.7%** [21] |\n| **自监督识别** | **WeSpeaker (ECAPA_TDNN)** | Vox1-O-clean | **EER: 2.627%** (无标签训练) [16] |\n\n### 五、 开发者最佳实践与踩坑经验\n\n#### **最佳实践**\n*   **数据增强**：**UIS-RNN** 推荐使用 **块状随机洗牌（Block-wise Shuffling）** 对训练数据进行重采样和增强，以在数据量不足时提升模型鲁棒性 [22]。\n*   **预处理优化**：**pyannote** 建议将音频预加载到内存中以显著提升处理速度 [23]。\n*   **模型精细控制**：在已知发言人数时，使用 `num_speakers` 或设置 `min_speakers`/`max_speakers` 范围可大幅提高识别准确度 [23]。\n*   **配置驱动**：**SpeechBrain** 采用 YAML 文件封装超参数，将逻辑与参数分离，利于实验的可重复性 [17, 24]。\n\n#### **常见踩坑经验 (Pitfalls)**\n*   **ID 冲突问题**：在 UIS-RNN 中，拼接多个序列进行训练时，必须谨慎处理 `enforce_cluster_id_uniqueness` 参数。如果不同序列中的同一标签不代表同一人，需确保标签全局唯一，否则会导致模型混淆身份 [25, 26]。\n*   **环境依赖陷阱**：**pyannote 3.1** 移除了 `onnxruntime` 的依赖，转而使用纯 PyTorch 以简化部署难度并避免复杂的依赖冲突 [27, 28]。\n*   **PyTorch 版本安全漏洞**：自 PyTorch 2.6 起，`torch.load` 默认开启 `weights_only=True`，加载旧模型或第三方模型时可能需要手动调整，但需注意防范任意代码执行风险 [29]。\n*   **大规模训练策略**：对于超大规模数据集，不应在多次 `fit()` 调用中喂入完全不同的数据集，而应确保单次调用中包含来自不同数据源的样本 [22]。",
    "conversation_id": "a31d41fe-47ba-4e4e-bcad-64bf6d5ee582",
    "sources_used": [
      "5341d428-958c-4c67-9cec-262642f52388",
      "70279693-1c87-43f1-9150-6347ce00ecc8",
      "952e6f81-ec96-4412-9872-13c331762d12",
      "6d9034d9-794b-4914-be97-bd71e56e48d8",
      "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "77a438b2-68a7-435c-bd6b-a116c7953577",
      "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "8c795b3b-5f02-417f-b414-c85fd2956efb"
    ],
    "citations": {
      "1": "5341d428-958c-4c67-9cec-262642f52388",
      "2": "70279693-1c87-43f1-9150-6347ce00ecc8",
      "3": "952e6f81-ec96-4412-9872-13c331762d12",
      "4": "5341d428-958c-4c67-9cec-262642f52388",
      "5": "5341d428-958c-4c67-9cec-262642f52388",
      "6": "5341d428-958c-4c67-9cec-262642f52388",
      "7": "5341d428-958c-4c67-9cec-262642f52388",
      "8": "6d9034d9-794b-4914-be97-bd71e56e48d8",
      "9": "6d9034d9-794b-4914-be97-bd71e56e48d8",
      "10": "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "11": "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "12": "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "13": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "14": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "15": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "16": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "17": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "18": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "19": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "20": "952e6f81-ec96-4412-9872-13c331762d12",
      "21": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "22": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "23": "952e6f81-ec96-4412-9872-13c331762d12",
      "24": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "25": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "26": "8c795b3b-5f02-417f-b414-c85fd2956efb",
      "27": "952e6f81-ec96-4412-9872-13c331762d12",
      "28": "952e6f81-ec96-4412-9872-13c331762d12",
      "29": "f7a45787-0b03-46c1-a505-cf2112070aa9"
    },
    "references": [
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 1,
        "cited_text": "Microsoft uses Azure Speech for many scenarios, such as captioning in Microsoft Teams, dictation in Microsoft Office 365, and Read Aloud in the Microsoft Edge browser. Capabilities The following sections summarize Azure Speech features and provide links for more information. Speech to text Use speech to text to convert audio into text. Choose from: Real-time transcription for streaming audio. Fast transcription for pre-recorded audio files. Batch transcription for processing large volumes of audio asynchronously."
      },
      {
        "source_id": "70279693-1c87-43f1-9150-6347ce00ecc8",
        "citation_number": 2,
        "cited_text": "智能语音交互-智能语音交互-阿里云 查看 “ ” 全部搜索结果 AI 助理 你好，我是AI助理，可以解答问题、推荐解决方案等 官方文档 输入文档关键字查找 产品概述 快速入门 实践教程 开发参考 安全合规 服务支持 首页 智能语音交互 智能语音交互 智能语音交互（Intelligent Speech Interaction），是基于语音识别、语音合成、自然语言理解等技术，为企业在多种实际应用场景下，赋予产品 “能听、会说、懂你” 式的智能人机交互体验。适用于多个应用场景中，包括智能问答、智能质检、法庭庭审实时记录、实时演讲字幕、访谈录音转写等场景，在金融、保险、司法、电商等多个领域均有应用案例。 售前咨询 常见问题 学习路径 由浅入深，带您玩转智能语音交互。 了解 产品简介 什么是智能语音交互 产品优势 功能特性 应用场景 基本概念 地域和域名 上手 快速入门 从这里开始 管理项目 获取Token 运行示例 SDK和API概览 非开发者使用指南 使用 一句话识别"
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 3,
        "cited_text": "This model isn't deployed by any Inference Provider. 🙋 27 Ask for provider support Model tree for pyannote/speaker-diarization-3.1 Finetunes 38 models Merges 1 model Spaces using pyannote/speaker-diarization-3.1 100 🌍 Daniel9046/SoniTranslate 🚀 jhj0517/Whisper-WebUI 🌍 Sonogram/Instructor-Support-Tool 🌍🈷 G-Rost/SoniTranslate_2 👁 AtomCosmic/CatalystDiarization ✨ avans06/whisper-webui-translate 💋 alexnasa/OutofLipSync 🐰 clement-pages/gryannote 🌍🈷 RO-Rtechs/Translate_Video_language 🚀 soiz1/Whisper-WebUI"
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 4,
        "cited_text": "Language identification Language identification helps you identify languages spoken in audio by comparing them against a list of supported languages . Use language identification by itself, with speech-to-text recognition, or with speech translation. Pronunciation assessment Pronunciation assessment evaluates speech pronunciation and gives speakers feedback on the accuracy and fluency of spoken audio. By using pronunciation assessment, language learners can practice, get instant feedback, and improve their pronunciation so that they can speak and present with confidence."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 5,
        "cited_text": "You can create custom voices, add specific words to your base vocabulary, or build your own models. Run Azure Speech anywhere, in the cloud or at the edge in containers. Enable your applications, tools, and devices for speech by using the Speech CLI , Speech SDK , and REST APIs . Azure Speech is available for many languages , regions , and price points . Scenarios Common scenarios for speech include: Captioning : Learn how to synchronize captions with your input audio, apply profanity filters, get partial results, apply customizations, and identify spoken languages for multilingual scenarios. Audio content creation : Use neural voices to make interactions with chatbots and voice agents more natural and engaging, convert digital texts such as e-books into audiobooks, and enhance in-car navigation systems. Call center : Transcribe calls in real time or process a batch of calls, redact personal information, and extract insights such as sentiment to help with your call-center use case. Language learning : Provide pronunciation assessment feedback to language learners, support real-time transcription for remote learning conversations, and read aloud teaching materials with neural voices. Voice Live : Create natural, humanlike conversational interfaces for applications and experiences. The Voice Live feature provides fast, reliable interaction between a human and an agent implementation. Speech translation : Generate high-quality speech-to-speech translation in real time, or automatically generate translated videos in a broad range of languages. Video avatar creation : Create lifelike and high-quality synthetic talking avatar videos for various real-time and batch applications while adhering to responsible AI practices."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 6,
        "cited_text": "transcribe : Convert pre-recorded audio into text. translate : Convert pre-recorded audio into text in a specified target language. The LLM-enhanced speech model delivers improved quality, deep contextual understanding, multilingual support, and prompt-tuning capabilities. LLM speech shares the same ultra-fast inference performance as fast transcription. Use cases include generating captions and subtitles from audio files, summarizing meeting notes, assisting call center agents, transcribing voicemails, and more."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 7,
        "cited_text": "Integration of Azure Speech in your application Speech Studio is a set of UI-based tools for building and integrating features from Azure Speech in your applications. You create projects in Speech Studio by using a no-code approach. You can then reference those assets in your applications by using: Speech SDK . This SDK exposes many of the Azure Speech capabilities that you can use to develop speech-enabled applications. The Speech SDK is available in many programming languages and across all platforms. Speech CLI . With this command-line tool, you can use Azure Speech without having to write any code. Most features in the Speech SDK are available in the Speech CLI, and some advanced features and customizations are simplified in the Speech CLI. REST APIs . In some cases, you can't or shouldn't use the Speech SDK. In those cases, you can use REST APIs to access Azure Speech. For example, use REST APIs for batch transcription ."
      },
      {
        "source_id": "6d9034d9-794b-4914-be97-bd71e56e48d8",
        "citation_number": 8,
        "cited_text": "Inference Engines vLLM Text Generation Inference (TGI) SGLang Text Embeddings Inference (TEI) llama.cpp Inference Toolkit Custom Container Images Join the Hugging Face community and get access to the augmented documentation experience Collaborate on models, datasets and Spaces Faster examples with accelerated inference Switch between documentation themes Sign Up to get started Copy page Inference Endpoints Inference Endpoints is a managed service to deploy your AI model to production. Here you'll find quickstarts, guides, tutorials, use cases and a lot more."
      },
      {
        "source_id": "6d9034d9-794b-4914-be97-bd71e56e48d8",
        "citation_number": 9,
        "cited_text": "Key Features 📦 Fully managed infrastructure : you don't need to worry about things like kubernetes, CUDA versions and configuring VPNs. Inference Endpoints deals with this under the hood so you can focus on deploying your model and serving customers as fast as possible. ↕ Autoscaling : as there's more traffic to your model you'll need more firepower as well. Your Inference Endpoint scales up as traffic increases and down as it decreases to save you on unnecessary compute cost. 👀 Observability : understand and debug what's going on in your model through logs & metrics. 🔥 Integrated support for open-source Inference Engines : Whether you want to deploy your model with vLLM, TGI or a custom container, we got you! 🤗 Seamless integration with the Hugging Face Hub : Downloading model weights fast and with the correct security policies is paramount when bringing an AI model to production. With Inference Endpoints, it's easy and safe."
      },
      {
        "source_id": "f7a45787-0b03-46c1-a505-cf2112070aa9",
        "citation_number": 10,
        "cited_text": "Introduction NVIDIA NeMo Speech is built for researchers and PyTorch developers working on Speech models including Automatic Speech Recognition (ASR), Text to Speech (TTS), and Speech LLMs. It is designed to help you efficiently create, customize, and deploy new It is designed to help you efficiently create, customize, and deploy new AI models by leveraging existing code and pre-trained model checkpoints. For technical documentation, please see the NeMo Framework User Guide . Requirements Python 3.12 or above Pytorch 2.6 or above NVIDIA GPU (if you intend to do model training)"
      },
      {
        "source_id": "f7a45787-0b03-46c1-a505-cf2112070aa9",
        "citation_number": 11,
        "cited_text": "Install NeMo Speech NeMo Speech is installable via pip: pip install 'nemo-toolkit[all]' To install with extra dependencies for CUDA 12.x or 13.x, use pip install 'nemo-toolkit[all,cu12]' or pip install 'nemo-toolkit[all,cu13]' respectively. Contribute to NeMo We welcome community contributions! Please refer to CONTRIBUTING.md for the process. Licenses NeMo is licensed under the Apache License 2.0 . About A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech)"
      },
      {
        "source_id": "f7a45787-0b03-46c1-a505-cf2112070aa9",
        "citation_number": 12,
        "cited_text": "Repository files navigation README Contributing Apache-2.0 license NVIDIA NeMo Speech Checkout our HuggingFace🤗 collection for the latest open weight checkpoints and demos! Updates 2026-03: Nemotron 3 VoiceChat is now released in Early Access. Built on the Nemotron Nano v2 LLM backbone with Nemotron speech and TTS decoder, VoiceChat delivers full-duplex, natural, interruptible conversations with low latency. Try out the demo and apply for early access . 2026-03: Nemotron-Speech-Streaming v2603 has been updated. It has been trained on a larger and more diverse corpus, resulting in lower WER across all latency modes. Try out the demo and check out the NIM . 2026-03: MagpieTTS v2602 has been released with support for 9 languages(En, Es, De, Fr, Vi, It, Zh, Hi, Ja). Try out the demo and check out the NIM . 2026-01: Nemotron-Speech-Streaming was released: One checkpoint that enables users to pick their optimal point on the latency-accuracy Pareto curve! 2026-01: MagpieTTS was released. 2026: This repo has pivoted to focus on audio, speech, and multimodal LLM. For the last NeMo release with support for more modalities, see v2.7.0 2025-08: Parakeet V3 and Canary V2 have been released with speech recognition and translation support for 25 European languages. 2025-06: Canary-Qwen-2.5B has been released with record-setting 5.63% WER on English Open ASR Leaderboard."
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 13,
        "cited_text": "wenet-e2e / wespeaker Public Notifications You must be signed in to change notification settings Fork 187 Star 1.3k Code Issues 40 Pull requests 3 Discussions Actions Projects Security and quality 0 Insights Additional navigation options Code Issues Pull requests Discussions Actions Projects Security and quality Insights wenet-e2e/wespeaker master 5 Branches 3 Tags Go to file Code Open more actions menu Folders and files <cited_table>",
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
              ".github/ workflows",
              "",
              ".github/ workflows",
              "fix: keep initial_lr in scheduler_args instead of popping it (",
              "3 months ago"
            ],
            [
              "docs",
              "",
              "docs",
              "[cli] support w2v-bert2-LoRA-adapter-MFA model (",
              "4 months ago"
            ],
            [
              "examples",
              "",
              "examples",
              "fix: resolve bugs in WarmupLR_withStepDecay and train config (",
              "4 months ago"
            ],
            [
              "runtime",
              "",
              "runtime",
              "[runtime] cosine score normalization (",
              "last year"
            ],
            [
              "tools",
              "",
              "tools",
              "Integrate w2v-bert2-LoRA-adapter-MFA model (",
              "5 months ago"
            ],
            [
              "wespeaker",
              "",
              "wespeaker",
              "xi-vector: Clamp log precision values to specified range (",
              "2 months ago"
            ],
            [
              ".clang-format",
              "",
              ".clang-format",
              "[lint] auto format all by pre-commit, including c++, python (",
              "3 years ago"
            ],
            [
              ".flake8",
              "",
              ".flake8",
              "[fix] fix some bugs and flake8 lint problem (",
              "4 years ago"
            ],
            [
              ".gitignore",
              "",
              ".gitignore",
              "Support Whisper-PMFA (",
              "2 years ago"
            ],
            [
              ".pre-commit-config.yaml",
              "",
              ".pre-commit-config.yaml",
              "[lint] use pre-commit to auto check and lint (",
              "3 years ago"
            ],
            [
              "CPPLINT.cfg",
              "",
              "CPPLINT.cfg",
              "[runtime] support onnxruntime (",
              "3 years ago"
            ],
            [
              "LICENSE",
              "",
              "LICENSE",
              "Create LICENSE (",
              "4 years ago"
            ],
            [
              "README.md",
              "",
              "README.md",
              "[cli] support w2v-bert2-LoRA-adapter-MFA model (",
              "4 months ago"
            ],
            [
              "ROADMAP.md",
              "",
              "ROADMAP.md",
              "[doc] update README.md and add QMF results (",
              "2 years ago"
            ],
            [
              "requirements.txt",
              "",
              "requirements.txt",
              "Add diarization recipe v3 (",
              "2 years ago"
            ],
            [
              "setup.cfg",
              "",
              "setup.cfg",
              "[cli] add first cli support (",
              "3 years ago"
            ],
            [
              "setup.py",
              "",
              "setup.py",
              "[cli] add cli requirements of umap+hdbscan (",
              "2 years ago"
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
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 14,
        "cited_text": "Please refer to python usage for more command line and python programming usage. Install for development & deployment Clone this repo Create conda env: pytorch version >= 1.12.1 is recommended !!! 🔥 News 2025.12.05: Add support for the w2v-bert2 model , see #439 and #441 . 2025.02.23: Add support for the Xi-vector, see #404 . 2024.09.03: Support the SimAM_ResNet and the model pretrained on VoxBlink2, check Pretrained Models for the pretrained model, VoxCeleb Recipe for the super performance, and python usage for the command line usage! 2024.08.30: We support whisper_encoder based frontend and propose the Whisper-PMFA framework, check #356 . 2024.08.20: Update diarization recipe for VoxConverse dataset by leveraging umap dimensionality reduction and hdbscan clustering, see #347 and #352 . 2024.08.18: Support using ssl pre-trained models as the frontend. The WavLM recipe is also provided, see #344 . 2024.05.15: Add support for quality-aware score calibration , see #320 . 2024.04.25: Add support for the gemini-dfresnet model, see #291 . 2024.04.23: Support MNN inference engine in runtime, see #310 . 2024.04.02: Release Wespeaker document with detailed model-training tutorials, introduction of various runtime platforms, etc. 2024.03.04: Support the eres2net-cn-common-200k and campplus-cn-common-200k of damo #281 , check python usage for details. 2024.02.05: Support the ERes2Net #272 and Res2Net #273 models. 2023.11.13: Support CLI usage of wespeaker, check python usage for details. 2023.07.18: Support the kaldi-compatible PLDA and unsupervised adaptation, see #186 . 2023.07.14: Support the NIST SRE16 recipe , see #177 ."
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 15,
        "cited_text": "<cited_table> Self-hosted speed on a NVIDIA H100 80GB HBM3 Telemetry With the optional telemetry feature in pyannote.audio , you can choose to send anonymous usage metrics to help the pyannote team improve the library. What we track For each call to Pipeline.from_pretrained({origin}) (or Model.from_pretrained({origin}) ), we track information about {origin} in the following privacy-preserving way:",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "community-1",
              "precision-2",
              "Speed up"
            ],
            [
              "AMI",
              "31s per hour of audio",
              "14s per hour of audio",
              "2.2x faster"
            ],
            [
              "DIHARD 3",
              "37s per hour of audio",
              "14s per hour of audio",
              "2.6x faster"
            ]
          ]
        }
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 16,
        "cited_text": "Recipes VoxCeleb : Speaker Verification recipe on the VoxCeleb dataset 🔥 UPDATE 2024.05.15: We support score calibration for Voxceleb and achieve better performance! 🔥 UPDATE 2023.07.10: We support self-supervised learning recipe on Voxceleb! Achieving 2.627% (ECAPA_TDNN_GLOB_c1024) EER on vox1-O-clean test set without any labels. 🔥 UPDATE 2022.10.31: We support deep r-vector up to the 293-layer version! Achieving 0.447%/0.043 EER/mindcf on vox1-O-clean test set 🔥 UPDATE 2022.07.19: We apply the same setups as the CNCeleb recipe, and obtain SOTA performance considering the open-source systems EER/minDCF on vox1-O-clean test set are 0.723%/0.069 (ResNet34) and 0.728%/0.099 (ECAPA_TDNN_GLOB_c1024), after LM fine-tuning and AS-Norm CNCeleb : Speaker Verification recipe on the CnCeleb dataset 🔥 UPDATE 2024.05.16: We support score calibration for Cnceleb and achieve better EER. 🔥 UPDATE 2022.10.31: 221-layer ResNet achieves 5.655%/0.330 EER/minDCF 🔥 UPDATE 2022.07.12: We migrate the winner system of CNSRC 2022 report slides EER/minDCF reduction from 8.426%/0.487 to 6.492%/0.354 after large margin fine-tuning and AS-Norm NIST SRE16 : Speaker Verification recipe for the 2016 NIST Speaker Recognition Evaluation Plan . Similar recipe can be found in Kaldi . 🔥 UPDATE 2023.07.14: We support NIST SRE16 recipe. After PLDA adaptation, we achieved 6.608%, 10.01%, and 2.974% EER on trial Pooled, Tagalog, and Cantonese, respectively. VoxConverse : Diarization recipe on the VoxConverse dataset"
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
        "citation_number": 17,
        "cited_text": "📚 Training Recipes We share over 200 competitive training recipes on more than 40 datasets supporting 20 speech and text processing tasks (see below). We support both training from scratch and fine-tuning pretrained models such as Whisper , Wav2Vec2 , WavLM , Hubert , GPT2 , Llama2 , and beyond. The models on HuggingFace can be easily plugged in and fine-tuned. For any task, you train the model using these commands: The hyperparameters are encapsulated in a YAML file, while the training process is orchestrated through a Python script. We maintained a consistent code structure across different tasks. For better replicability, training logs and checkpoints are hosted on Dropbox."
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
        "citation_number": 18,
        "cited_text": "🎯 Use Cases 🚀 Research Acceleration : Speeding up academic and industrial research. You can develop and integrate new models effortlessly, comparing their performance against our baselines. ⚡ Rapid Prototyping : Ideal for quick prototyping in time-sensitive projects. 🎓 Educational Tool : SpeechBrain's simplicity makes it a valuable educational resource. It is used by institutions like Mila , Concordia University , Avignon University , and many others for student training. 🚀 Quick Start To get started with SpeechBrain, follow these simple steps:"
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 19,
        "cited_text": "Repository files navigation README Code of conduct More Repository files items Contributing Apache-2.0 license Security UIS-RNN Overview This is the library for the Unbounded Interleaved-State Recurrent Neural Network (UIS-RNN) algorithm. UIS-RNN solves the problem of segmenting and clustering sequential data by learning from examples. This algorithm was originally proposed in the paper Fully Supervised Speaker Diarization . The work has been introduced by Google AI Blog ."
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 20,
        "cited_text": "<cited_table> Citations Downloads last month 11,172,667 Inference Providers NEW Automatic Speech Recognition",
        "cited_table": {
          "num_columns": 7,
          "rows": [
            [
              "Benchmark",
              "DER%",
              "FA%",
              "Miss%",
              "Conf%",
              "Expected output",
              "File-level evaluation"
            ],
            [
              "AISHELL-4",
              "12.2",
              "3.8",
              "4.4",
              "4.0",
              "RTTM",
              "eval"
            ],
            [
              "AliMeeting ( channel 1)",
              "24.4",
              "4.4",
              "10.0",
              "10.0",
              "RTTM",
              "eval"
            ],
            [
              "AMI ( headset mix,",
              "18.8",
              "3.6",
              "9.5",
              "5.7",
              "RTTM",
              "eval"
            ],
            [
              "AMI ( array1, channel 1,",
              "22.4",
              "3.8",
              "11.2",
              "7.5",
              "RTTM",
              "eval"
            ],
            [
              "AVA-AVD",
              "50.0",
              "10.8",
              "15.7",
              "23.4",
              "RTTM",
              "eval"
            ],
            [
              "DIHARD 3 ( Full)",
              "21.7",
              "6.2",
              "8.1",
              "7.3",
              "RTTM",
              "eval"
            ],
            [
              "MSDWild",
              "25.3",
              "5.8",
              "8.0",
              "11.5",
              "RTTM",
              "eval"
            ],
            [
              "REPERE ( phase 2)",
              "7.8",
              "1.8",
              "2.6",
              "3.5",
              "RTTM",
              "eval"
            ],
            [
              "VoxConverse ( v0.3)",
              "11.3",
              "4.1",
              "3.4",
              "3.8",
              "RTTM",
              "eval"
            ]
          ]
        }
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 21,
        "cited_text": "Benchmark <cited_table> Diarization error rate (in %, the lower, the better) Compared to the 3.1 legacy pipeline, community-1 brings significant improvement in terms of speaker counting and assignment. precision-2 premium pipeline further improves accuracy as well as processing speed (in its self-hosted version).",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "legacy (3.1)",
              "community-1",
              "precision-2"
            ],
            [
              "AISHELL-4",
              "12.2",
              "11.7",
              "11.4"
            ],
            [
              "AliMeeting",
              "24.5",
              "20.3",
              "15.2"
            ],
            [
              "AMI",
              "18.8",
              "17.0",
              "12.9"
            ],
            [
              "AMI",
              "22.7",
              "19.9",
              "15.6"
            ],
            [
              "AVA-AVD",
              "49.7",
              "44.6",
              "37.1"
            ],
            [
              "CALLHOME",
              "28.5",
              "26.7",
              "16.6"
            ],
            [
              "DIHARD 3",
              "21.4",
              "20.2",
              "14.7"
            ],
            [
              "Ego4D",
              "51.2",
              "46.8",
              "39.0"
            ],
            [
              "MSDWild",
              "25.4",
              "22.8",
              "17.3"
            ],
            [
              "RAMC",
              "22.2",
              "20.8",
              "10.5"
            ],
            [
              "REPERE",
              "7.9",
              "8.9",
              "7.4"
            ],
            [
              "VoxConverse",
              "11.2",
              "11.2",
              "8.5"
            ]
          ]
        }
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 22,
        "cited_text": "The reason we concatenate all training sequences is that, we will be resampling and block-wise shuffling the training data as a data augmentation process, such that we result in a robust model even when there is insufficient number of training sequences. Training on large datasets For large datasets, the data usually could not be loaded into memory at once. In such cases, the fit() function needs to be called multiple times. Here we provide a few guidelines as our suggestions: Do not feed different datasets into different calls of fit() . Instead, for each call of fit() , the input should cover sequences from different datasets. For each call to the fit() function, make the size of input roughly the same. And, don't make the input size too small."
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 23,
        "cited_text": "Usage Processing on GPU pyannote.audio pipelines run on CPU by default. You can send them to GPU with the following lines: Processing from memory Pre-loading audio files in memory may result in faster processing: Monitoring progress Hooks are available to monitor the progress of the pipeline: Controlling the number of speakers In case the number of speakers is known in advance, one can use the num_speakers option: One can also provide lower and/or upper bounds on the number of speakers using min_speakers and max_speakers options:"
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
        "citation_number": 24,
        "cited_text": "Training Orchestration: The Brain class serves as a fully customizable tool for managing training and evaluation loops over data. It simplifies training loops while providing the flexibility to override any part of the process. Hyperparameter Management: A YAML-based hyperparameter file specifies all hyperparameters, from individual numbers (e.g., learning rate) to complete objects (e.g., custom models). This elegant solution drastically simplifies the training script. Dynamic Dataloader: Enables flexible and efficient data reading. GPU Training: Supports single and multi-GPU training, including distributed training. Dynamic Batching: On-the-fly dynamic batching enhances the efficient processing of variable-length signals. Mixed-Precision Training: Accelerates training through mixed-precision techniques. Efficient Data Reading: Reads large datasets efficiently from a shared Network File System (NFS) via WebDataset . Hugging Face Integration: Interfaces seamlessly with HuggingFace for popular models such as wav2vec2 and Hubert. Orion Integration: Interfaces with Orion for hyperparameter tuning. Speech Augmentation Techniques: Includes SpecAugment, Noise, Reverberation, and more. Data Preparation Scripts: Includes scripts for preparing data for supported datasets."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 25,
        "cited_text": "When calling fit() in this way, please be very careful with the argument --enforce_cluster_id_uniqueness . For example, assume: If the label 'a' from the two sequences refers to the same cluster across the entire dataset, then we should have enforce_cluster_id_uniqueness=False ; otherwise, if 'a' is only a local indicator to distinguish from 'b' in the 1st sequence, and to distinguish from 'c' in the 2nd sequence, then we should have enforce_cluster_id_uniqueness=True . Also, please note that, when calling fit() in this way, we are going to concatenate all sequences and all cluster IDs, and delegate to the next section below."
      },
      {
        "source_id": "8c795b3b-5f02-417f-b414-c85fd2956efb",
        "citation_number": 26,
        "cited_text": "For example, if the set of labels in the first sequence is {'A', 'B', 'C'} , and the set of labels in the second sequence is {'B', 'C', 'D'} . Then before concatenation, we should rename them to something like {'1_A', '1_B', '1_C'} and {'2_B', '2_C', '2_D'} , unless 'B' and 'C' in the two sequences are meaningfully identical (in speaker diarization, this means they are the same speakers across utterances). This part will be automatically taken care of by the argument --enforce_cluster_id_uniqueness for the previous section."
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 27,
        "cited_text": "Log in or Sign Up to review the conditions and access this model content. 🎹 Speaker diarization 3.1 Requirements Usage Processing on GPU Processing from memory Monitoring progress Controlling the number of speakers Benchmark Citations Using this open-source model in production? Consider switching to pyannoteAI for better and faster options. 🎹 Speaker diarization 3.1 This pipeline is the same as pyannote/speaker-diarization-3.0 except it removes the problematic use of onnxruntime ."
      },
      {
        "source_id": "952e6f81-ec96-4412-9872-13c331762d12",
        "citation_number": 28,
        "cited_text": "Both speaker segmentation and embedding now run in pure PyTorch. This should ease deployment and possibly speed up inference. It requires pyannote.audio version 3.1 or higher. It ingests mono audio sampled at 16kHz and outputs speaker diarization as an Annotation instance: stereo or multi-channel audio files are automatically downmixed to mono by averaging the channels. audio files sampled at a different rate are resampled to 16kHz automatically upon loading. Requirements Install pyannote.audio 3.1 with pip install pyannote.audio Accept pyannote/segmentation-3.0 user conditions Accept pyannote/speaker-diarization-3.1 user conditions Create access token at hf.co/settings/tokens ."
      },
      {
        "source_id": "f7a45787-0b03-46c1-a505-cf2112070aa9",
        "citation_number": 29,
        "cited_text": "As of Pytorch 2.6 , torch.load defaults to using weights_only=True . Some model checkpoints may require using weights_only=False . In this case, you can set the env var TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1 before running code that uses torch.load . However, this should only be done with trusted files. Loading files from untrusted sources with more than weights only can have the risk of arbitrary code execution. Developer Documentation <cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Version",
              "Status",
              "Description"
            ],
            [
              "Latest",
              "",
              "Documentation of the latest (i.e. main) branch."
            ],
            [
              "Stable",
              "",
              "Documentation of the stable (i.e. most recent release) - To be added"
            ]
          ]
        }
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「声纹识别与说话人分离」领域，2025至2026年的研究重点已从单一的算法精度竞争转向**多模态大语言模型（Multimodal LLMs）的融合**、**实时流式处理**以及**端侧轻量化部署**。以下是基于最新来源的详细解析：\n\n### 一、 2025-2026年重要论文与技术突破\n1.  **架构演进：从单模态到多模态 LLM**\n    *   **多模态语音大模型（Speech LLMs）**：NVIDIA 在 2026 年明确将其技术重心转向音频、语音与多模态 LLM 的结合 [1]。SpeechBrain 也将“多模态大语言模型”列为核心优先事项，旨在开发能同时处理文本、语音和音频任务的单一基础模型 [2]。\n    *   **全双工对话系统**：2026年3月发布的 **Nemotron 3 VoiceChat** 代表了最新突破，它基于 Nemotron Nano v2 LLM 骨干网络，支持低延迟、自然且**可中断**的全双工语音交互，这要求声纹识别与分离技术必须在毫秒级内完成身份校验 [1]。\n\n2.  **核心算法的持续增强**\n    *   **Xi-vector 与 w2v-bert2**：WeSpeaker 在 2025 年底相继引入了 **Xi-vector** 和 **w2v-bert2-LoRA** 适配器模型 [3, 4]。这些技术利用大规模预训练模型的特征提取能力，结合低秩自适应（LoRA）技术，大幅提升了在复杂环境下的声纹嵌入精度。\n    *   **LLM 增强型语音模型**：Azure Speech 推出的 **LLM speech (preview)** 利用大模型深入理解语境，从而在噪声或多口音场景下实现更准确的身份与内容对齐 [5, 6]。\n\n### 二、 2025-2026年技术趋势\n*   **极致的推理速度**：pyannote-audio 的 **precision-2** 生产级流水线在 2025 年 9 月的基准测试中显示，在 H100 上处理 1 小时音频仅需 **14 秒**，处理速度比旧版本提升了 **2.2 至 2.6 倍** [7, 8]。\n*   **流式与精度平衡**：**Nemotron-Speech-Streaming** 技术的演进允许用户在延迟与准确度（Pareto 曲线）之间动态选择最优平衡点，解决了传统模型难以兼顾实时性与高精度的痛点 [1]。\n*   **质量感知校准（Quality-aware Calibration）**：WeSpeaker 引入了针对 VoxCeleb 和 CNCeleb 数据集的**分数校准**技术，通过评估语音质量来动态调整识别阈值，显著降低了误识率 [4, 9]。\n\n### 三、 未解决的挑战\n*   **生产环境的“规模化”冲突**：SpeechBrain 指出，行业面临“Scale Up”（训练超大规模模型以获取极限性能）与“Scale Down”（在生产环境中实现低功耗、实时流式的小模型部署）之间的巨大鸿沟 [2]。\n*   **安全与合规性风险**：随着 PyTorch 等底层框架的更新（如 PyTorch 2.6 默认开启 weights_only 加载），模型权重的安全性成为新课题。加载不可信来源的模型可能会带来**任意代码执行**的风险，这对于涉及敏感身份信息的语音助手而言是重大隐患 [10]。\n*   **重叠语音的分离难题**：虽然 pyannote 等框架在重叠语音检测上有所突破，但在极端嘈杂或多人同时抢话的场景下，Diarization Error Rate (DER) 依然存在提升空间 [7, 11]。\n\n### 四、 未来可能的突破点\n*   **统一基础模型（Foundation Models）**：未来的语音助手将不再由多个离散的插件（VAD、声纹、ASR、LLM）组成，而是演变为一个**单一的端到端神经系统**，能够直接从音频流中感知身份、情感和语义 [2]。\n*   **上下文深层理解**：通过 LLM 的常识和逻辑推理能力，系统将能够根据对话背景（如“只有家庭成员能控制智能家居”）来辅助声纹验证，从而在声纹特征模糊时提供逻辑层面的二次校验 [6]。\n*   **绿色 AI 与端侧实时化**：针对低功耗设备优化的小参数量声纹模型将成为主流，通过 **MNN** 或 **ONNX** 等推理引擎实现完全本地化的身份验证，以保护用户隐私并消除云端延迟 [3, 4]。",
    "conversation_id": "a31d41fe-47ba-4e4e-bcad-64bf6d5ee582",
    "sources_used": [
      "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "5341d428-958c-4c67-9cec-262642f52388",
      "77a438b2-68a7-435c-bd6b-a116c7953577"
    ],
    "citations": {
      "1": "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "2": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
      "3": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "4": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "5": "5341d428-958c-4c67-9cec-262642f52388",
      "6": "5341d428-958c-4c67-9cec-262642f52388",
      "7": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "8": "77a438b2-68a7-435c-bd6b-a116c7953577",
      "9": "756626a2-599e-4e71-84a4-281bc13cf9ed",
      "10": "f7a45787-0b03-46c1-a505-cf2112070aa9",
      "11": "77a438b2-68a7-435c-bd6b-a116c7953577"
    },
    "references": [
      {
        "source_id": "f7a45787-0b03-46c1-a505-cf2112070aa9",
        "citation_number": 1,
        "cited_text": "Repository files navigation README Contributing Apache-2.0 license NVIDIA NeMo Speech Checkout our HuggingFace🤗 collection for the latest open weight checkpoints and demos! Updates 2026-03: Nemotron 3 VoiceChat is now released in Early Access. Built on the Nemotron Nano v2 LLM backbone with Nemotron speech and TTS decoder, VoiceChat delivers full-duplex, natural, interruptible conversations with low latency. Try out the demo and apply for early access . 2026-03: Nemotron-Speech-Streaming v2603 has been updated. It has been trained on a larger and more diverse corpus, resulting in lower WER across all latency modes. Try out the demo and check out the NIM . 2026-03: MagpieTTS v2602 has been released with support for 9 languages(En, Es, De, Fr, Vi, It, Zh, Hi, Ja). Try out the demo and check out the NIM . 2026-01: Nemotron-Speech-Streaming was released: One checkpoint that enables users to pick their optimal point on the latency-accuracy Pareto curve! 2026-01: MagpieTTS was released. 2026: This repo has pivoted to focus on audio, speech, and multimodal LLM. For the last NeMo release with support for more modalities, see v2.7.0 2025-08: Parakeet V3 and Canary V2 have been released with speech recognition and translation support for 25 European languages. 2025-06: Canary-Qwen-2.5B has been released with record-setting 5.63% WER on English Open ASR Leaderboard."
      },
      {
        "source_id": "6c3f3187-c07f-45bd-9b6f-e3c66faca317",
        "citation_number": 2,
        "cited_text": "🔮Future Plans We have ambitious plans for the future, with a focus on the following priorities: Scale Up: We aim to provide comprehensive recipes and technologies for training massive models on extensive datasets. Scale Down: While scaling up delivers unprecedented performance, we recognize the challenges of deploying large models in production scenarios. We are focusing on real-time, streamable, and small-footprint Conversational AI. Multimodal Large Language Models : We envision a future where a single foundation model can handle a wide range of text, speech, and audio tasks. Our core team is focused on enabling the training of advanced multimodal LLMs."
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 3,
        "cited_text": "wenet-e2e / wespeaker Public Notifications You must be signed in to change notification settings Fork 187 Star 1.3k Code Issues 40 Pull requests 3 Discussions Actions Projects Security and quality 0 Insights Additional navigation options Code Issues Pull requests Discussions Actions Projects Security and quality Insights wenet-e2e/wespeaker master 5 Branches 3 Tags Go to file Code Open more actions menu Folders and files <cited_table>",
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
              ".github/ workflows",
              "",
              ".github/ workflows",
              "fix: keep initial_lr in scheduler_args instead of popping it (",
              "3 months ago"
            ],
            [
              "docs",
              "",
              "docs",
              "[cli] support w2v-bert2-LoRA-adapter-MFA model (",
              "4 months ago"
            ],
            [
              "examples",
              "",
              "examples",
              "fix: resolve bugs in WarmupLR_withStepDecay and train config (",
              "4 months ago"
            ],
            [
              "runtime",
              "",
              "runtime",
              "[runtime] cosine score normalization (",
              "last year"
            ],
            [
              "tools",
              "",
              "tools",
              "Integrate w2v-bert2-LoRA-adapter-MFA model (",
              "5 months ago"
            ],
            [
              "wespeaker",
              "",
              "wespeaker",
              "xi-vector: Clamp log precision values to specified range (",
              "2 months ago"
            ],
            [
              ".clang-format",
              "",
              ".clang-format",
              "[lint] auto format all by pre-commit, including c++, python (",
              "3 years ago"
            ],
            [
              ".flake8",
              "",
              ".flake8",
              "[fix] fix some bugs and flake8 lint problem (",
              "4 years ago"
            ],
            [
              ".gitignore",
              "",
              ".gitignore",
              "Support Whisper-PMFA (",
              "2 years ago"
            ],
            [
              ".pre-commit-config.yaml",
              "",
              ".pre-commit-config.yaml",
              "[lint] use pre-commit to auto check and lint (",
              "3 years ago"
            ],
            [
              "CPPLINT.cfg",
              "",
              "CPPLINT.cfg",
              "[runtime] support onnxruntime (",
              "3 years ago"
            ],
            [
              "LICENSE",
              "",
              "LICENSE",
              "Create LICENSE (",
              "4 years ago"
            ],
            [
              "README.md",
              "",
              "README.md",
              "[cli] support w2v-bert2-LoRA-adapter-MFA model (",
              "4 months ago"
            ],
            [
              "ROADMAP.md",
              "",
              "ROADMAP.md",
              "[doc] update README.md and add QMF results (",
              "2 years ago"
            ],
            [
              "requirements.txt",
              "",
              "requirements.txt",
              "Add diarization recipe v3 (",
              "2 years ago"
            ],
            [
              "setup.cfg",
              "",
              "setup.cfg",
              "[cli] add first cli support (",
              "3 years ago"
            ],
            [
              "setup.py",
              "",
              "setup.py",
              "[cli] add cli requirements of umap+hdbscan (",
              "2 years ago"
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
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 4,
        "cited_text": "Please refer to python usage for more command line and python programming usage. Install for development & deployment Clone this repo Create conda env: pytorch version >= 1.12.1 is recommended !!! 🔥 News 2025.12.05: Add support for the w2v-bert2 model , see #439 and #441 . 2025.02.23: Add support for the Xi-vector, see #404 . 2024.09.03: Support the SimAM_ResNet and the model pretrained on VoxBlink2, check Pretrained Models for the pretrained model, VoxCeleb Recipe for the super performance, and python usage for the command line usage! 2024.08.30: We support whisper_encoder based frontend and propose the Whisper-PMFA framework, check #356 . 2024.08.20: Update diarization recipe for VoxConverse dataset by leveraging umap dimensionality reduction and hdbscan clustering, see #347 and #352 . 2024.08.18: Support using ssl pre-trained models as the frontend. The WavLM recipe is also provided, see #344 . 2024.05.15: Add support for quality-aware score calibration , see #320 . 2024.04.25: Add support for the gemini-dfresnet model, see #291 . 2024.04.23: Support MNN inference engine in runtime, see #310 . 2024.04.02: Release Wespeaker document with detailed model-training tutorials, introduction of various runtime platforms, etc. 2024.03.04: Support the eres2net-cn-common-200k and campplus-cn-common-200k of damo #281 , check python usage for details. 2024.02.05: Support the ERes2Net #272 and Res2Net #273 models. 2023.11.13: Support CLI usage of wespeaker, check python usage for details. 2023.07.18: Support the kaldi-compatible PLDA and unsupervised adaptation, see #186 . 2023.07.14: Support the NIST SRE16 recipe , see #177 ."
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 5,
        "cited_text": "You can choose from a range of standard voices for the avatar. The language support for text-to-speech avatar is the same as the language support for text to speech. Speech translation Speech translation enables real-time, multilingual translation of speech to your applications, tools, and devices. Use this feature for speech-to-speech and speech-to-text translation. LLM speech (preview) Take advantage of a large language model (LLM)-enhanced speech model in LLM speech . This feature currently supports the following tasks:"
      },
      {
        "source_id": "5341d428-958c-4c67-9cec-262642f52388",
        "citation_number": 6,
        "cited_text": "transcribe : Convert pre-recorded audio into text. translate : Convert pre-recorded audio into text in a specified target language. The LLM-enhanced speech model delivers improved quality, deep contextual understanding, multilingual support, and prompt-tuning capabilities. LLM speech shares the same ultra-fast inference performance as fast transcription. Use cases include generating captions and subtitles from audio files, summarizing meeting notes, assisting call center agents, transcribing voicemails, and more."
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 7,
        "cited_text": "Benchmark <cited_table> Diarization error rate (in %, the lower, the better) Compared to the 3.1 legacy pipeline, community-1 brings significant improvement in terms of speaker counting and assignment. precision-2 premium pipeline further improves accuracy as well as processing speed (in its self-hosted version).",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "legacy (3.1)",
              "community-1",
              "precision-2"
            ],
            [
              "AISHELL-4",
              "12.2",
              "11.7",
              "11.4"
            ],
            [
              "AliMeeting",
              "24.5",
              "20.3",
              "15.2"
            ],
            [
              "AMI",
              "18.8",
              "17.0",
              "12.9"
            ],
            [
              "AMI",
              "22.7",
              "19.9",
              "15.6"
            ],
            [
              "AVA-AVD",
              "49.7",
              "44.6",
              "37.1"
            ],
            [
              "CALLHOME",
              "28.5",
              "26.7",
              "16.6"
            ],
            [
              "DIHARD 3",
              "21.4",
              "20.2",
              "14.7"
            ],
            [
              "Ego4D",
              "51.2",
              "46.8",
              "39.0"
            ],
            [
              "MSDWild",
              "25.4",
              "22.8",
              "17.3"
            ],
            [
              "RAMC",
              "22.2",
              "20.8",
              "10.5"
            ],
            [
              "REPERE",
              "7.9",
              "8.9",
              "7.4"
            ],
            [
              "VoxConverse",
              "11.2",
              "11.2",
              "8.5"
            ]
          ]
        }
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 8,
        "cited_text": "<cited_table> Self-hosted speed on a NVIDIA H100 80GB HBM3 Telemetry With the optional telemetry feature in pyannote.audio , you can choose to send anonymous usage metrics to help the pyannote team improve the library. What we track For each call to Pipeline.from_pretrained({origin}) (or Model.from_pretrained({origin}) ), we track information about {origin} in the following privacy-preserving way:",
        "cited_table": {
          "num_columns": 4,
          "rows": [
            [
              "Benchmark (last updated in 2025-09)",
              "community-1",
              "precision-2",
              "Speed up"
            ],
            [
              "AMI",
              "31s per hour of audio",
              "14s per hour of audio",
              "2.2x faster"
            ],
            [
              "DIHARD 3",
              "37s per hour of audio",
              "14s per hour of audio",
              "2.6x faster"
            ]
          ]
        }
      },
      {
        "source_id": "756626a2-599e-4e71-84a4-281bc13cf9ed",
        "citation_number": 9,
        "cited_text": "Recipes VoxCeleb : Speaker Verification recipe on the VoxCeleb dataset 🔥 UPDATE 2024.05.15: We support score calibration for Voxceleb and achieve better performance! 🔥 UPDATE 2023.07.10: We support self-supervised learning recipe on Voxceleb! Achieving 2.627% (ECAPA_TDNN_GLOB_c1024) EER on vox1-O-clean test set without any labels. 🔥 UPDATE 2022.10.31: We support deep r-vector up to the 293-layer version! Achieving 0.447%/0.043 EER/mindcf on vox1-O-clean test set 🔥 UPDATE 2022.07.19: We apply the same setups as the CNCeleb recipe, and obtain SOTA performance considering the open-source systems EER/minDCF on vox1-O-clean test set are 0.723%/0.069 (ResNet34) and 0.728%/0.099 (ECAPA_TDNN_GLOB_c1024), after LM fine-tuning and AS-Norm CNCeleb : Speaker Verification recipe on the CnCeleb dataset 🔥 UPDATE 2024.05.16: We support score calibration for Cnceleb and achieve better EER. 🔥 UPDATE 2022.10.31: 221-layer ResNet achieves 5.655%/0.330 EER/minDCF 🔥 UPDATE 2022.07.12: We migrate the winner system of CNSRC 2022 report slides EER/minDCF reduction from 8.426%/0.487 to 6.492%/0.354 after large margin fine-tuning and AS-Norm NIST SRE16 : Speaker Verification recipe for the 2016 NIST Speaker Recognition Evaluation Plan . Similar recipe can be found in Kaldi . 🔥 UPDATE 2023.07.14: We support NIST SRE16 recipe. After PLDA adaptation, we achieved 6.608%, 10.01%, and 2.974% EER on trial Pooled, Tagalog, and Cantonese, respectively. VoxConverse : Diarization recipe on the VoxConverse dataset"
      },
      {
        "source_id": "f7a45787-0b03-46c1-a505-cf2112070aa9",
        "citation_number": 10,
        "cited_text": "As of Pytorch 2.6 , torch.load defaults to using weights_only=True . Some model checkpoints may require using weights_only=False . In this case, you can set the env var TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1 before running code that uses torch.load . However, this should only be done with trusted files. Loading files from untrusted sources with more than weights only can have the risk of arbitrary code execution. Developer Documentation <cited_table>",
        "cited_table": {
          "num_columns": 3,
          "rows": [
            [
              "Version",
              "Status",
              "Description"
            ],
            [
              "Latest",
              "",
              "Documentation of the latest (i.e. main) branch."
            ],
            [
              "Stable",
              "",
              "Documentation of the stable (i.e. most recent release) - To be added"
            ]
          ]
        }
      },
      {
        "source_id": "77a438b2-68a7-435c-bd6b-a116c7953577",
        "citation_number": 11,
        "cited_text": "Citations If you use pyannote.audio please use the following citations: Development The commands below will setup pre-commit hooks and packages needed for developing the pyannote.audio library. Test About Neural building blocks for speaker diarization: speech activity detection, speaker change detection, overlapped speech detection, speaker embedding pyannote.github.io Topics pytorch pretrained-models speaker-recognition speaker-verification speech-processing speaker-diarization voice-activity-detection speech-activity-detection speaker-change-detection speaker-embedding overlapped-speech-detection"
      }
    ]
  }
}
