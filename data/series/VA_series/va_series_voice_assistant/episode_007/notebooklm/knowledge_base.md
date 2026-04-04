# 知识库：语音活动检测 (VAD)：让机器知道何时该听

生成时间: 2026-04-03 09:31
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "语音活动检测 (VAD) 的核心任务是将音频信号分类为**有声 (voiced)**或**无声 (unvoiced)**片段，旨在提升语音识别的效率和准确性 [1, 2]。以下是根据来源整理的技术架构与核心组件概述：\n\n### 1. 技术演进路线\nVAD 技术经历了从基于规则的轻量化工具到深度学习模型的演进，并进一步向语义理解方向发展：\n*   **传统模型阶段**：以 **WebRTC VAD** 为代表。这是由 Google 为 WebRTC 项目开发的 VAD，被公认为最快、最现代且免费的工具之一，广泛应用于电信和语音识别 [1]。\n*   **深度学习模型阶段**：现代 VAD 如 **Silero VAD** 和 **RNNoise** 采用了神经网络架构（如 RNN） [3, 4]。这些模型在处理超过 6000 种语言的大型语料库上进行训练，能够更好地应对背景噪音和多种音频域 [3]。\n*   **语义分割阶段 (Semantic Segmentation)**：最新的演进方向是超越单纯的静音检测，采用语义分割策略。它不仅依赖静音超时，还通过检测句末标点（如“.”或“?”）来切分语音，从而解决长难句的“欠分割”或短停顿导致的“过分割”问题 [5, 6]。\n\n### 2. 核心算法与模型名称\n*   **WebRTC VAD**：行业标准的规则/统计模型，提供 0 到 3 四种“攻击性（aggressiveness）”模式，用于调节过滤非语音信号的强度 [1]。\n*   **Silero VAD**：企业级预训练模型，基于 **PyTorch** 和 **ONNX**，具有极高的可移植性 [3, 7]。\n*   **RNN/Cobra VAD**：如 **RNNoise** 使用循环神经网络 (RNN) 进行降噪与语音识别 [4]；**Cobra** 是 Picovoice 提供的专用端侧 VAD 引擎 [8]。\n\n### 3. 主要架构模式\n*   **帧处理模式 (Frame-based Processing)**：VAD 将音频流切分为短小的“帧”。WebRTC VAD 接受 10、20 或 30 毫秒的帧 [2]；在实时流式识别中，100 毫秒的帧大小被认为是效率与延迟之间的最佳折中 [9]。\n*   **端侧部署模式 (On-device)**：为了实现**零延迟 (Zero-latency)**和隐私保护，VAD 引擎（如 Picovoice 或 Silero）常被设计为直接在移动端、Web 或嵌入式设备上运行，避免网络波动影响 [10, 11]。\n*   **超时控制机制 (Timeout Mechanisms)**：\n    *   **分割静音超时 (Segmentation silence timeout)**：调整在认为一句话结束前允许的停顿长度 [12]。\n    *   **初始静音超时 (Initial silence timeout)**：调整在识别尝试结束并返回“无匹配”前允许的起始静音长度 [12]。\n\n### 4. 关键技术指标\n*   **处理速度**：高性能模型处理一个 30 毫秒的音频块耗时**不到 1 毫秒** (单 CPU 线程) [3]。\n*   **模型体积**：轻量化 JIT 模型通常仅约 **2 MB** 左右 [3]。\n*   **采样率支持**：通用标准支持 **8,000 Hz** 和 **16,000 Hz**，部分可扩展至 48,000 Hz [2, 3]。\n*   **配置参数**：\n    *   分割静音超时通常设置在 **100 到 5,000 毫秒**之间，默认值常为 500 毫秒 [12]。\n    *   音频格式要求通常为 **16 位单声道 PCM** [2, 13]。",
    "conversation_id": "9ae38e85-cc2f-4a00-b3da-5ed5b388db02",
    "sources_used": [
      "56261f9d-2dda-41b7-b09a-89037041a489",
      "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "fe87bf45-9360-4f03-bc56-1753511d18ec",
      "cdaedc5e-2096-454d-941b-60772bff17a6",
      "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2"
    ],
    "citations": {
      "1": "56261f9d-2dda-41b7-b09a-89037041a489",
      "2": "56261f9d-2dda-41b7-b09a-89037041a489",
      "3": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "4": "fe87bf45-9360-4f03-bc56-1753511d18ec",
      "5": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "6": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "7": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "8": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "9": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "10": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "11": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "12": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "13": "cdaedc5e-2096-454d-941b-60772bff17a6"
    },
    "references": [
      {
        "source_id": "56261f9d-2dda-41b7-b09a-89037041a489",
        "citation_number": 1,
        "cited_text": "Repository files navigation README License py-webrtcvad This is a python interface to the WebRTC Voice Activity Detector (VAD). It is compatible with Python 2 and Python 3. A VAD classifies a piece of audio data as being voiced or unvoiced. It can be useful for telephony and speech recognition. The VAD that Google developed for the WebRTC project is reportedly one of the best available, being fast, modern and free. How to use it Install the webrtcvad module: Create a Vad object: Optionally, set its aggressiveness mode, which is an integer between 0 and 3. 0 is the least aggressive about filtering out non-speech, 3 is the most aggressive. (You can also set the mode when you create the VAD, e.g. vad = webrtcvad.Vad(3) ):"
      },
      {
        "source_id": "56261f9d-2dda-41b7-b09a-89037041a489",
        "citation_number": 2,
        "cited_text": "Give it a short segment (\"frame\") of audio. The WebRTC VAD only accepts 16-bit mono PCM audio, sampled at 8000, 16000, 32000 or 48000 Hz. A frame must be either 10, 20, or 30 ms in duration: See example.py for a more detailed example that will process a .wav file, find the voiced segments, and write each one as a separate .wav. How to run unit tests To run unit tests: History 2.0.10 Fixed memory leak. Thank you, bond005 ! 2.0.9 Improved example code. Added WebRTC license. 2.0.8 Fixed Windows compilation errors. Thank you, xiongyihui !"
      },
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 3,
        "cited_text": "You will have to implement the I/O; You will have to adapt the existing wrappers / examples / post-processing for your use-case. Using pip : pip install silero-vad Using torch.hub : Key Features Stellar accuracy Silero VAD has excellent results on speech detection tasks. Fast One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x faster. Lightweight JIT model is around two megabytes in size. General Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from different domains with various background noise and quality levels. Flexible sampling rate Silero VAD supports 8000 Hz and 16000 Hz sampling rates . Highly Portable Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere where these runtimes are available. No Strings Attached Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock."
      },
      {
        "source_id": "fe87bf45-9360-4f03-bc56-1753511d18ec",
        "citation_number": 4,
        "cited_text": "GitHub - xiph/rnnoise: Recurrent neural network for audio noise reduction · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 5,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 6,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 7,
        "cited_text": "Repository files navigation README Code of conduct MIT license Silero VAD Silero VAD - pre-trained enterprise-grade Voice Activity Detector (also see our STT models ). Real Time Example real-time-example.mp4 Please note, that video loads only if you are logged in your GitHub account. Fast start Dependencies System requirements to run python examples on x86-64 systems: python 3.8+ ; 1G+ RAM; A modern CPU with AVX, AVX2, AVX-512 or AMX instruction sets. Dependencies: torch>=1.12.0 ; torchaudio>=0.12.0 (for I/O only); onnxruntime>=1.16.1 (for ONNX model usage)."
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 8,
        "cited_text": "Voice AI picoLLM On-Device LLM Leopard Speech-to-Text Cheetah Streaming Speech-to-Text Orca Text-to-Speech Koala Noise Suppression Eagle Speaker Recognition Falcon Speaker Diarization Porcupine Wake Word Rhino Speech-to-Intent Cobra Voice Activity Detection Resources Docs Console Blog Use Cases Playground Contact Contact Sales Company About us Careers Follow Picovoice Subscribe to our newsletter Terms of Use Privacy Policy © 2019-2026 Picovoice Inc. This website uses cookies to enhance the user experience."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 9,
        "cited_text": "For codecs with a header, use the auto_decoding_config setting in RecognitionConfig to automatically choose the correct sampling rate. Frame size Streaming recognition recognizes live audio as it is captured from a microphone or other audio source. The audio stream is split into frames and sent in consecutive StreamingRecognizeRequest messages. Any frame size is acceptable. Larger frames are more efficient, but add latency. A 100-millisecond frame size is recommended as a good tradeoff between latency and efficiency."
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 10,
        "cited_text": "On-device Voice AI and local LLM platforms for Enterprises Platform Use Cases Blog Docs Contact Sales Start Free The only all-in-one on-device voice AI already deployed at scale Wake word, speech-to-text, LLM, text-to-speech, and more. All on-device. Runs across mobile, web, desktop, and embedded. Built for forward-thinking enterprises ready to deploy, not just experiment. Start Free Contact Sales Loved by developers, trusted by enterprises Voice AI Agents Across Platforms Picovoice's modular voice AI platform is engineered for on-device deployment, empowering enterprises to deliver customized, cross-platform voice solutions without sacrificing performance, latency, or privacy."
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 11,
        "cited_text": "Zero-latency Predictable and consistent response time with no network latency. Cloud Unbounded Response Time On-Device Guaranteed Response Time End-to-End Optimization Complete technological ownership enables fine-tuning at every layer rather than being constrained by third-party frameworks and pre-trained models. Learn More Accurate Outperforms alternatives with high margins, proven by open-source benchmarks. 2026-03-13T11:28:00.272749 image/svg+xml Matplotlib v3.10.8, https://matplotlib.org/ Hyper customizable"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 12,
        "cited_text": "These problems can be addressed by setting one of two timeout properties on the SpeechConfig instance used to create a SpeechRecognizer : Segmentation silence timeout adjusts how much nonspeech audio is allowed within a phrase that's currently being spoken before that phrase is considered \"done.\" Higher values generally make results longer and allow longer pauses from the speaker within a phrase but make results take longer to arrive. They can also combine separate phrases into a single result when set too high. Lower values generally make results shorter and ensure more prompt and frequent breaks between phrases, but can also cause single phrases to separate into multiple results when set too low. This timeout can be set to integer values between 100 and 5000, in milliseconds, with 500 a typical default. Initial silence timeout adjusts how much nonspeech audio is allowed before a phrase before the recognition attempt ends in a \"no match\" result. Higher values give speakers more time to react and start speaking, but can also result in slow responsiveness when nothing is spoken. Lower values ensure a prompt \"no match\" for faster user experience and more controlled audio handling, but might cut a speaker off too quickly when set too low. Because continuous recognition generates many results, this value determines how often \"no match\" results arrive but doesn't otherwise affect the content of recognition results. This timeout can be set to any non-negative integer value, in milliseconds, or set to 0 to disable it entirely. 5000 is a typical default for single-shot recognition while 15000 is a typical default for continuous recognition."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 13,
        "cited_text": "For many use cases, it's likely that your audio data comes from Azure Blob Storage, or it's otherwise already in memory as a byte[] instance or a similar raw data structure. The following example uses PushAudioInputStream to recognize speech, which is essentially an abstracted memory stream. The sample code does the following actions: Writes raw audio data to PushAudioInputStream by using the Write() function, which accepts a byte[] instance. Reads a .wav file by using FileReader for demonstration purposes. If you already have audio data in a byte[] instance, you can skip directly to writing the content to the input stream. The default format is 16-bit, 16-kHz mono pulse-code modulation (PCM) data. To customize the format, you can pass an AudioStreamFormat object to CreatePushStream() by using the static function AudioStreamFormat.GetWaveFormatPCM(sampleRate, (byte)bitRate, (byte)channels) ."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "语音活动检测 (VAD) 的实现细节涵盖了从底层的信号处理到高层的语义理解。以下是基于来源对 VAD 实现细节的深入解析：\n\n### 1. 核心算法流程\nVAD 的基本逻辑是将连续音频流切分为离散的“有声”或“无声”片段：\n*   **帧切分 (Framing)**：音频被划分为极短的帧。**WebRTC VAD** 接受 10、20 或 30 毫秒的帧 [1]；而对于一般的实时流式识别，**100 毫秒**的帧大小被认为是延迟与效率之间的理想平衡点 [2]。\n*   **分类检测**：\n    *   **统计/规则法**：如 WebRTC 使用统计模型来分类。它提供 0-3 四种**攻击性 (aggressiveness) 模式**，数值越高对非语音信号的过滤越严厉 [3]。\n    *   **神经网络法**：**Silero VAD** 或 **RNNoise** 使用预训练的神经网络（如 RNN）在海量语料（如 6000+ 语言）上进行特征提取，判断当前帧是否包含人类语音 [4, 5]。\n*   **状态控制 (Timeout Management)**：\n    *   **起始超时**：判断在返回“无匹配”结果前允许的起始静音时长（如默认 5,000 毫秒） [6]。\n    *   **分割超时**：在当前语句结束前允许的非语音停顿（可调范围 100-5,000 毫秒） [6, 7]。\n\n### 2. 关键代码架构\n现代 VAD 引擎通常采用高度可移植且模块化的架构：\n*   **包装器与接口**：如 `py-webrtcvad` 提供 C 语言内核的 Python 接口，支持 **16 位单声道 PCM** 音频 [1, 3, 8]。\n*   **配置类架构**：在 Azure 架构中，通过 `SpeechConfig` 实例设置超参数（如 `set_property`），并由 `SpeechRecognizer` 执行实际的实时检测逻辑 [9, 10]。\n*   **内存流处理**：高性能实现支持从**内存字节流 (PushAudioInputStream)** 直接读取数据，跳过文件头处理，实现无缝对接 [11, 12]。\n\n### 3. 性能优化策略\n*   **零延迟 (Zero-latency) 部署**：将 VAD 引擎（如 **Picovoice Cobra** 或 **Silero**）部署在**端侧 (On-device)**，避免网络传输产生的波动，确保响应时间的确定性 [13]。\n*   **计算加速**：\n    *   **轻量化模型**：Silero 的 JIT 模型体积仅约 **2 MB** [4, 14]。\n    *   **极速处理**：单个 30ms 音频块在单 CPU 线程上的处理时间**小于 1 毫秒** [4]。\n*   **采样率与格式适配**：优先使用音源的原始采样率（如电话系统的 **8,000 Hz** 或高清语音的 **16,000 Hz**），避免重采样带来的性能开销 [15, 16]。建议使用 **FLAC** 或 **LINEAR16** 等无损格式以保证识别精度 [15]。\n\n### 4. 竞品技术对比与具体参数\n\n| 技术维度 | WebRTC VAD | Silero VAD | Azure Speech (语义分割) |\n| :--- | :--- | :--- | :--- |\n| **核心算法** | 统计模型 [3] | 深度神经网络 (PyTorch/ONNX) [4] | 基于语义标点识别 [17] |\n| **主要优势** | 速度极快、开源标准、免费 [3] | 企业级精度、支持 6000+ 语言、极小体积 [4] | 解决“长难句”或“短停顿”的误分割 [17] |\n| **处理帧长** | 10, 20, 30 ms [1] | 30+ ms [4] | 动态 (基于语义完整性) [17] |\n| **关键参数** | 4 种攻击性模式 (0-3) [3] | 模型大小 ~2 MB [4] | 停顿超时 100-5,000 ms [6] |\n| **采样率支持** | 8k, 16k, 32k, 48k Hz [1] | 8k, 16k Hz [4] | 8k, 16k Hz (推荐) [16] |\n\n**补充：性能优化进阶**\n在处理高并发或长语音时，**语义分割 (Semantic Segmentation)** 策略优于传统的静音检测，因为它通过识别句末标点（如“.”或“?”）来触发分割，有效解决了用户长谈时的“墙状文本 (wall of text)”问题 [17, 18]。同时，在实时场景下，禁用自动增益控制 (AGC) 和第三方降噪处理通常能获得更好的识别精度，因为 VAD 引擎通常自带针对噪音的鲁棒性设计 [19]。",
    "conversation_id": "9ae38e85-cc2f-4a00-b3da-5ed5b388db02",
    "sources_used": [
      "56261f9d-2dda-41b7-b09a-89037041a489",
      "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "0ee7d21b-a3a9-46d4-b565-208755247738",
      "fe87bf45-9360-4f03-bc56-1753511d18ec",
      "cdaedc5e-2096-454d-941b-60772bff17a6",
      "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "6043cfb1-b0b3-4d52-9e90-2757f5d284ce"
    ],
    "citations": {
      "1": "56261f9d-2dda-41b7-b09a-89037041a489",
      "2": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "3": "56261f9d-2dda-41b7-b09a-89037041a489",
      "4": "0ee7d21b-a3a9-46d4-b565-208755247738",
      "5": "fe87bf45-9360-4f03-bc56-1753511d18ec",
      "6": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "7": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "8": "56261f9d-2dda-41b7-b09a-89037041a489",
      "9": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "10": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "11": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "12": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "13": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "14": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "15": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "16": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "17": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "18": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "19": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2"
    },
    "references": [
      {
        "source_id": "56261f9d-2dda-41b7-b09a-89037041a489",
        "citation_number": 1,
        "cited_text": "Give it a short segment (\"frame\") of audio. The WebRTC VAD only accepts 16-bit mono PCM audio, sampled at 8000, 16000, 32000 or 48000 Hz. A frame must be either 10, 20, or 30 ms in duration: See example.py for a more detailed example that will process a .wav file, find the voiced segments, and write each one as a separate .wav. How to run unit tests To run unit tests: History 2.0.10 Fixed memory leak. Thank you, bond005 ! 2.0.9 Improved example code. Added WebRTC license. 2.0.8 Fixed Windows compilation errors. Thank you, xiongyihui !"
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 2,
        "cited_text": "For codecs with a header, use the auto_decoding_config setting in RecognitionConfig to automatically choose the correct sampling rate. Frame size Streaming recognition recognizes live audio as it is captured from a microphone or other audio source. The audio stream is split into frames and sent in consecutive StreamingRecognizeRequest messages. Any frame size is acceptable. Larger frames are more efficient, but add latency. A 100-millisecond frame size is recommended as a good tradeoff between latency and efficiency."
      },
      {
        "source_id": "56261f9d-2dda-41b7-b09a-89037041a489",
        "citation_number": 3,
        "cited_text": "Repository files navigation README License py-webrtcvad This is a python interface to the WebRTC Voice Activity Detector (VAD). It is compatible with Python 2 and Python 3. A VAD classifies a piece of audio data as being voiced or unvoiced. It can be useful for telephony and speech recognition. The VAD that Google developed for the WebRTC project is reportedly one of the best available, being fast, modern and free. How to use it Install the webrtcvad module: Create a Vad object: Optionally, set its aggressiveness mode, which is an integer between 0 and 3. 0 is the least aggressive about filtering out non-speech, 3 is the most aggressive. (You can also set the mode when you create the VAD, e.g. vad = webrtcvad.Vad(3) ):"
      },
      {
        "source_id": "0ee7d21b-a3a9-46d4-b565-208755247738",
        "citation_number": 4,
        "cited_text": "You will have to implement the I/O; You will have to adapt the existing wrappers / examples / post-processing for your use-case. Using pip : pip install silero-vad Using torch.hub : Key Features Stellar accuracy Silero VAD has excellent results on speech detection tasks. Fast One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x faster. Lightweight JIT model is around two megabytes in size. General Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from different domains with various background noise and quality levels. Flexible sampling rate Silero VAD supports 8000 Hz and 16000 Hz sampling rates . Highly Portable Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere where these runtimes are available. No Strings Attached Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock."
      },
      {
        "source_id": "fe87bf45-9360-4f03-bc56-1753511d18ec",
        "citation_number": 5,
        "cited_text": "Repository files navigation README BSD-3-Clause license About Recurrent neural network for audio noise reduction Topics audio c rnn noise-reduction Resources Readme License BSD-3-Clause license Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars 5.5k stars Watchers 154 watching Forks 1k forks Report repository Releases 1 RNNoise 0.2 Latest on Apr 14, 2024 Packages 0 No packages published Uh oh! There was an error while loading. Please reload this page . Contributors 13 Languages"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 6,
        "cited_text": "These problems can be addressed by setting one of two timeout properties on the SpeechConfig instance used to create a SpeechRecognizer : Segmentation silence timeout adjusts how much nonspeech audio is allowed within a phrase that's currently being spoken before that phrase is considered \"done.\" Higher values generally make results longer and allow longer pauses from the speaker within a phrase but make results take longer to arrive. They can also combine separate phrases into a single result when set too high. Lower values generally make results shorter and ensure more prompt and frequent breaks between phrases, but can also cause single phrases to separate into multiple results when set too low. This timeout can be set to integer values between 100 and 5000, in milliseconds, with 500 a typical default. Initial silence timeout adjusts how much nonspeech audio is allowed before a phrase before the recognition attempt ends in a \"no match\" result. Higher values give speakers more time to react and start speaking, but can also result in slow responsiveness when nothing is spoken. Lower values ensure a prompt \"no match\" for faster user experience and more controlled audio handling, but might cut a speaker off too quickly when set too low. Because continuous recognition generates many results, this value determines how often \"no match\" results arrive but doesn't otherwise affect the content of recognition results. This timeout can be set to any non-negative integer value, in milliseconds, or set to 0 to disable it entirely. 5000 is a typical default for single-shot recognition while 15000 is a typical default for continuous recognition."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 7,
        "cited_text": "Since there are tradeoffs when modifying these timeouts, you should only change the settings when you have a problem related to silence handling. Default values optimally handle most spoken audio and only uncommon scenarios should encounter problems. Example: Users speaking a serial number like \"ABC-123-4567\" might pause between character groups long enough for the serial number to be broken into multiple results. In this case, try a higher value like 2000 milliseconds for the segmentation silence timeout:"
      },
      {
        "source_id": "56261f9d-2dda-41b7-b09a-89037041a489",
        "citation_number": 8,
        "cited_text": "About Python interface to the WebRTC Voice Activity Detector Resources Readme License View license Uh oh! There was an error while loading. Please reload this page . Activity Stars 2.5k stars Watchers 48 watching Forks 428 forks Report repository Releases 12 tags Packages 0 No packages published Uh oh! There was an error while loading. Please reload this page . Contributors 7 Languages C 79.4% C++ 12.7% Python 4.7% Objective-C 3.2% Footer © 2026 GitHub, Inc. Footer navigation Terms Privacy Security Status Community Docs Contact Manage cookies Do not share my personal information"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 9,
        "cited_text": "To learn how to set up the environment for a sample application, see Quickstart: Recognize and convert speech to text . Create a speech configuration instance To call the Speech service by using the Speech SDK, you need to create a SpeechConfig instance. This class includes information about your Speech resource, like your speech key and associated region, endpoint, host, or authorization token. Create a Foundry resource for Speech in the Azure portal . Get the Speech resource key and region. Create a SpeechConfig instance by using the following code. Replace YourSpeechKey and YourSpeechRegion with your Speech resource key and region."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 10,
        "cited_text": "To use semantic segmentation, you need to set the following property on the SpeechConfig instance used to create a SpeechRecognizer : Python Copy Some of the limitations of semantic segmentation are as follows: You need the Speech SDK version 1.41 or later to use semantic segmentation. Semantic segmentation is only intended for use in continuous recognition . This includes scenarios such as dictation and captioning. It shouldn't be used in the single recognition mode or interactive scenarios. Semantic segmentation isn't available for all languages and locales. Semantic segmentation doesn't yet support confidence scores and NBest lists. As such, we don't recommend semantic segmentation if you're using confidence scores or NBest lists."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 11,
        "cited_text": "For many use cases, it's likely that your audio data comes from Azure Blob Storage, or it's otherwise already in memory as a byte[] instance or a similar raw data structure. The following example uses PushAudioInputStream to recognize speech, which is essentially an abstracted memory stream. The sample code does the following actions: Writes raw audio data to PushAudioInputStream by using the Write() function, which accepts a byte[] instance. Reads a .wav file by using FileReader for demonstration purposes. If you already have audio data in a byte[] instance, you can skip directly to writing the content to the input stream. The default format is 16-bit, 16-kHz mono pulse-code modulation (PCM) data. To customize the format, you can pass an AudioStreamFormat object to CreatePushStream() by using the static function AudioStreamFormat.GetWaveFormatPCM(sampleRate, (byte)bitRate, (byte)channels) ."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 12,
        "cited_text": "Creates a push stream by using createPushStream() . Reads a .wav file by using fs.createReadStream for demonstration purposes. If you already have audio data in the ArrayBuffer , you can skip directly to writing the content to the input stream. Creates an audio configuration by using the push stream. JavaScript Copy Using a push stream as input assumes that the audio data is raw pulse-code modulation (PCM) data that skips any headers. The API still works in certain cases if the header isn't skipped. For the best results, consider implementing logic to read off the headers so that fs begins at the start of the audio data ."
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 13,
        "cited_text": "Zero-latency Predictable and consistent response time with no network latency. Cloud Unbounded Response Time On-Device Guaranteed Response Time End-to-End Optimization Complete technological ownership enables fine-tuning at every layer rather than being constrained by third-party frameworks and pre-trained models. Learn More Accurate Outperforms alternatives with high margins, proven by open-source benchmarks. 2026-03-13T11:28:00.272749 image/svg+xml Matplotlib v3.10.8, https://matplotlib.org/ Hyper customizable"
      },
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 14,
        "cited_text": "You will have to implement the I/O; You will have to adapt the existing wrappers / examples / post-processing for your use-case. Using pip : pip install silero-vad Using torch.hub : Key Features Stellar accuracy Silero VAD has excellent results on speech detection tasks. Fast One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x faster. Lightweight JIT model is around two megabytes in size. General Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from different domains with various background noise and quality levels. Flexible sampling rate Silero VAD supports 8000 Hz and 16000 Hz sampling rates . Highly Portable Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere where these runtimes are available. No Strings Attached Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 15,
        "cited_text": "If you follow these guidelines and don't get the results you expect from the API, see Troubleshooting & Support . For optimal results... If possible, avoid... Capture audio with a sampling rate of 16,000 Hz or higher. Lower sampling rates may reduce accuracy. However, avoid re-sampling. For example, in telephony the native rate is commonly 8000 Hz, which is the rate that should be sent to the service. Use a lossless codec to record and transmit audio. FLAC or LINEAR16 is recommended. Using mp3, mp4, m4a, mu-law, a-law or other lossy codecs during recording or transmission may reduce accuracy. If your audio is already in an encoding not supported by the API, transcode it to lossless FLAC or LINEAR16 . If your application must use a lossy codec to conserve bandwidth, we recommend the AMR_WB or OGG_OPUS codecs, in that preferred order."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 16,
        "cited_text": "Multiple people talking at the same time, or at different volumes may be interpreted as background noise and ignored. Use word and phrase hints to add names and terms to the vocabulary and to boost the accuracy for specific words and phrases. The recognizer has a very large vocabulary, however terms and proper names that are out-of-vocabulary will not be recognized. Sampling rate If possible, set the sampling rate of the audio source to 16000 Hz. For headerless codecs, use the explicit_decoding_config setting in RecognitionConfig to set sample_rate_hertz to match the native sample rate of the audio source (instead of re-sampling)."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 17,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 18,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 19,
        "cited_text": "Audio preprocessing It's best to provide audio that is as clean as possible by using a good quality and well-positioned microphone. However, applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy. The service is designed to handle noisy audio. For best results: Position the microphone as close as possible to the person that is speaking, particularly when background noise is present. Avoid audio clipping. Do not use automatic gain control (AGC). All noise reduction processing should be disabled. Listen to some sample audio. It should sound clear, without distortion or unexpected noise."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "语音活动检测 (VAD) 技术在工业界和开源社区中已有广泛的成熟应用，其核心价值在于优化语音交互的响应速度与处理效率。以下是基于来源整理的真实应用场景、部署方案、性能基准及实战经验：\n\n### 1. 真实应用场景与案例\nVAD 是现代语音 AI 系统的基础设施，其应用涵盖了从云端服务到边缘设备的各个领域：\n*   **工业级应用**：\n    *   **呼叫中心自动化与语音机器人**：用于检测用户何时开始或停止说话，实现自然的轮次切换 [1, 2]。\n    *   **实时转写与会议字幕**：在直播会议或听写场景中，通过 VAD 触发实时语音转文字 [3, 4]。\n    *   **车载与 IoT 控制**：作为唤醒词检测后的延续，判断用户指令的边界 [1, 5]。\n*   **开源与社区案例**：\n    *   **Silero VAD**：被广泛用于数据清洗（从海量音频中提取有人声的片段）和移动端应用部署 [1, 6]。\n    *   **WebRTC VAD**：电信级标准，常集成在各类 VoIP 软件中用于节省带宽 [7]。\n    *   **Whisper 增强**：在 GitHub 社区中，开发者常结合 VAD 解决 Whisper 模型在流式任务中的幻觉与断句问题 [8, 9]。\n\n### 2. 工业级部署方案\n*   **端侧部署 (On-device)**：\n    *   **Picovoice Cobra**：专为实时性设计的端侧 VAD 引擎，支持 Android、iOS、Web 以及树莓派等嵌入式平台，强调**零延迟**和隐私保护 [2, 5, 10]。\n    *   **Silero JIT 模型**：利用 PyTorch JIT 或 ONNX Runtime，在不依赖复杂后端的情况下实现跨平台运行 [11, 12]。\n*   **云端与容器化部署**：\n    *   **Azure Speech 容器**：支持通过 Docker 部署带有 VAD 功能的 Websocket 端点，适用于私有云或数据合规要求高的场景 [13-15]。\n    *   **内存流处理**：在 C# 或 Java 环境下，通过 `PushAudioInputStream` 模式直接将原始 PCM 字节流推入识别引擎，跳过文件 I/O 以降低延迟 [16, 17]。\n\n### 3. 性能基准数据\n根据 **Silero VAD** 等企业级开源项目提供的数据，现代 VAD 已达到极高性能：\n*   **处理延迟**：在单个 CPU 线程上，处理一个 30 毫秒以上的音频块耗时**不到 1 毫秒** [11, 12]。\n*   **资源占用**：Silero 的 JIT 模型体积仅约 **2 MB**，运行示例通常仅需 1GB 以上内存及支持 AVX/AMX 指令集的现代 CPU [11, 18]。\n*   **采样率与格式**：标准支持 **8,000 Hz 和 16,000 Hz**，通常要求 **16 位单声道 PCM** 格式 [11, 12]。\n*   **超时控制**：\n    *   **分割静音超时**：默认通常为 500ms，可在 100-5,000ms 间调节 [19]。\n    *   **初始静音超时**：单次识别默认为 5,000ms，连续识别模式可达 15,000ms [19]。\n\n### 4. 开发者最佳实践与踩坑经验\n#### 最佳实践\n*   **采样率一致性**：首选原始采样率（如电话用 8k，高清语音用 16k），**严禁进行不必要的重采样**以防精度损失 [20, 21]。\n*   **编码格式**：优先使用 **FLAC 或 LINEAR16** 等无损编解码器；若需节省带宽，推荐按 AMR_WB 或 OGG_OPUS 顺序选择 [20]。\n*   **禁用多余处理**：**必须禁用自动增益控制 (AGC)** 和第三方降噪处理，因为这些处理往往会干扰现代 VAD 引擎的内部算法逻辑 [22]。\n\n#### 常见踩坑与对策\n*   **欠分割与“文本墙” (Wall of Text)**：当用户持续讲话不间断时，传统 VAD 可能无法切分，导致可读性极差。**对策**：引入**语义分割 (Semantic Segmentation)** 策略，结合标点符号（如“.”或“?”）识别进行强制切分 [23, 24]。\n*   **过分割与语速适配**：\n    *   **快速语音**：容易将多句话连在一起。**解决**：将分割静音超时调低（如 300ms） [25]。\n    *   **慢速语音/读序列号**：如“ABC-123”中间的停顿常导致识别过早结束。**解决**：将分割静音超时调高（如 2000ms） [26]。\n*   **字节流偏置**：在使用内存流 (Push Stream) 时，如果直接发送带文件头的 byte 数组，可能导致识别失败。**解决**：确保发送的 byte[] 从**音频数据的起始位置**开始（跳过 WAV 头等） [17, 27]。",
    "conversation_id": "9ae38e85-cc2f-4a00-b3da-5ed5b388db02",
    "sources_used": [
      "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "cdaedc5e-2096-454d-941b-60772bff17a6",
      "0ee7d21b-a3a9-46d4-b565-208755247738",
      "56261f9d-2dda-41b7-b09a-89037041a489",
      "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2",
      "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2"
    ],
    "citations": {
      "1": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "2": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "3": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "4": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "5": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "6": "0ee7d21b-a3a9-46d4-b565-208755247738",
      "7": "56261f9d-2dda-41b7-b09a-89037041a489",
      "8": "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2",
      "9": "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2",
      "10": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "11": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "12": "0ee7d21b-a3a9-46d4-b565-208755247738",
      "13": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "14": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "15": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "16": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "17": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "18": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "19": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "20": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "21": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "22": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "23": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "24": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "25": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "26": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "27": "cdaedc5e-2096-454d-941b-60772bff17a6"
    },
    "references": [
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 1,
        "cited_text": "Typical Use Cases Voice activity detection for IOT / edge / mobile use cases Data cleaning and preparation, voice detection in general Telephony and call-center automation, voice bots Voice interfaces Links Examples and Dependencies Quality Metrics Performance Metrics Versions and Available Models Further reading FAQ Get In Touch Try our models, create an issue , start a discussion , join our telegram chat , email us, read our news . Please see our wiki for relevant information and email us directly."
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 2,
        "cited_text": "Voice AI picoLLM On-Device LLM Leopard Speech-to-Text Cheetah Streaming Speech-to-Text Orca Text-to-Speech Koala Noise Suppression Eagle Speaker Recognition Falcon Speaker Diarization Porcupine Wake Word Rhino Speech-to-Intent Cobra Voice Activity Detection Resources Docs Console Blog Use Cases Playground Contact Contact Sales Company About us Careers Follow Picovoice Subscribe to our newsletter Terms of Use Privacy Policy © 2019-2026 Picovoice Inc. This website uses cookies to enhance the user experience."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 3,
        "cited_text": "Speech to text REST API reference | Speech to text REST API for short audio reference | Additional samples on GitHub In this how-to guide, you learn how to use Azure Speech in Foundry Tools for real-time speech to text conversion. Real-time speech recognition is ideal for applications requiring immediate transcription, such as dictation, call center assistance, and captioning for live meetings. To learn how to set up the environment for a sample application, see Quickstart: Recognize and convert speech to text ."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 4,
        "cited_text": "Reference documentation | Package (NuGet) | Additional samples on GitHub In this how-to guide, you learn how to use Azure Speech in Foundry Tools for real-time speech to text conversion. Real-time speech recognition is ideal for applications requiring immediate transcription, such as dictation, call center assistance, and captioning for live meetings. To learn how to set up the environment for a sample application, see Quickstart: Recognize and convert speech to text . Create a speech configuration instance"
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 5,
        "cited_text": "On-device Voice AI and local LLM platforms for Enterprises Platform Use Cases Blog Docs Contact Sales Start Free The only all-in-one on-device voice AI already deployed at scale Wake word, speech-to-text, LLM, text-to-speech, and more. All on-device. Runs across mobile, web, desktop, and embedded. Built for forward-thinking enterprises ready to deploy, not just experiment. Start Free Contact Sales Loved by developers, trusted by enterprises Voice AI Agents Across Platforms Picovoice's modular voice AI platform is engineered for on-device deployment, empowering enterprises to deliver customized, cross-platform voice solutions without sacrificing performance, latency, or privacy."
      },
      {
        "source_id": "0ee7d21b-a3a9-46d4-b565-208755247738",
        "citation_number": 6,
        "cited_text": "Typical Use Cases Voice activity detection for IOT / edge / mobile use cases Data cleaning and preparation, voice detection in general Telephony and call-center automation, voice bots Voice interfaces Links Examples and Dependencies Quality Metrics Performance Metrics Versions and Available Models Further reading FAQ Get In Touch Try our models, create an issue , start a discussion , join our telegram chat , email us, read our news . Please see our wiki for relevant information and email us directly."
      },
      {
        "source_id": "56261f9d-2dda-41b7-b09a-89037041a489",
        "citation_number": 7,
        "cited_text": "Repository files navigation README License py-webrtcvad This is a python interface to the WebRTC Voice Activity Detector (VAD). It is compatible with Python 2 and Python 3. A VAD classifies a piece of audio data as being voiced or unvoiced. It can be useful for telephony and speech recognition. The VAD that Google developed for the WebRTC project is reportedly one of the best available, being fast, modern and free. How to use it Install the webrtcvad module: Create a Vad object: Optionally, set its aggressiveness mode, which is an integer between 0 and 3. 0 is the least aggressive about filtering out non-speech, 3 is the most aggressive. (You can also set the mode when you create the VAD, e.g. vad = webrtcvad.Vad(3) ):"
      },
      {
        "source_id": "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2",
        "citation_number": 8,
        "cited_text": "openai / whisper Public Notifications You must be signed in to change notification settings Fork 12k Star 97.1k Code Pull requests 118 Discussions Actions Security and quality 0 Insights Additional navigation options Code Pull requests Discussions Actions Security and quality Insights openai whisper Discussions Pinned Discussions Possible to use for real-time / streaming tasks? 🙏 Q&A · davidhariri Search all discussions is:open is:open is:open Clear Sort by: Latest activity"
      },
      {
        "source_id": "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2",
        "citation_number": 9,
        "cited_text": "stephnangue started 3 weeks ago in Show and tell 0 2 You must be logged in to vote 🙌 Is this Suitable for real time websocket streaming? Sriharan-VJ started last month in Show and tell 2 66 You must be logged in to vote 🙌 Install Whisper in one click with WhisperScript, a Windows and MacOS desktop app GUI for Whisper with Speaker Diarization, Recording and Video Player jonathgh started on Mar 4, 2023 in Show and tell 76 Previous 1 2 3 4 5 … 39 40 Next Footer © 2026 GitHub, Inc. Footer navigation"
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 10,
        "cited_text": "Android iOS Mac Raspberry Pi Chrome Firefox Safari Windows ⚡ Live Demo Your browser does not support the video tag. OnePlus BE2028 2020, Android 11, 6GB RAM Your browser does not support the video tag. iPhone 15 Pro 2023, iOS 18.5, 8GB RAM Your browser does not support the video tag. MacBook Air M1 2020, macOS 15.5, 8GB RAM Your browser does not support the video tag. Raspberry Pi 4 2021, OS Lite (64-bit), 8GB RAM Your browser does not support the video tag. MacBook Air M1 2020, macOS 15.5, 8GB RAM Your browser does not support the video tag."
      },
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 11,
        "cited_text": "You will have to implement the I/O; You will have to adapt the existing wrappers / examples / post-processing for your use-case. Using pip : pip install silero-vad Using torch.hub : Key Features Stellar accuracy Silero VAD has excellent results on speech detection tasks. Fast One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x faster. Lightweight JIT model is around two megabytes in size. General Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from different domains with various background noise and quality levels. Flexible sampling rate Silero VAD supports 8000 Hz and 16000 Hz sampling rates . Highly Portable Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere where these runtimes are available. No Strings Attached Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock."
      },
      {
        "source_id": "0ee7d21b-a3a9-46d4-b565-208755247738",
        "citation_number": 12,
        "cited_text": "You will have to implement the I/O; You will have to adapt the existing wrappers / examples / post-processing for your use-case. Using pip : pip install silero-vad Using torch.hub : Key Features Stellar accuracy Silero VAD has excellent results on speech detection tasks. Fast One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x faster. Lightweight JIT model is around two megabytes in size. General Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from different domains with various background noise and quality levels. Flexible sampling rate Silero VAD supports 8000 Hz and 16000 Hz sampling rates . Highly Portable Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere where these runtimes are available. No Strings Attached Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 13,
        "cited_text": "Speech containers provide websocket-based query endpoint APIs that are accessed through the Speech SDK and Speech CLI. By default, the Speech SDK and Speech CLI use the public Speech service. To use the container, you need to change the initialization method. Use a container host URL instead of key and region. For more information about containers, see Host URLs in Install and run Speech containers with Docker . Semantic segmentation Semantic segmentation is a speech recognition segmentation strategy that's designed to mitigate issues associated with silence-based segmentation:"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 14,
        "cited_text": "Language identification You can use language identification with speech to text recognition when you need to identify the language in an audio source and then transcribe it to text. For a complete code sample, see Language identification . Use a custom endpoint With custom speech , you can upload your own data, test and train a custom model, compare accuracy between models, and deploy a model to a custom endpoint. The following example shows how to set a custom endpoint. C# Copy Run and use a container Speech containers provide websocket-based query endpoint APIs that are accessed through the Speech SDK and Speech CLI. By default, the Speech SDK and Speech CLI use the public Speech service. To use the container, you need to change the initialization method. Use a container host URL instead of key and region."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 15,
        "cited_text": "JavaScript Copy Run and use a container Speech containers provide websocket-based query endpoint APIs that are accessed through the Speech SDK and Speech CLI. By default, the Speech SDK and Speech CLI use the public Speech service. To use the container, you need to change the initialization method. Use a container host URL instead of key and region. For more information about containers, see Host URLs in Install and run Speech containers with Docker . Reference documentation | Additional samples on GitHub"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 16,
        "cited_text": "For many use cases, it's likely that your audio data comes from Azure Blob Storage, or it's otherwise already in memory as a byte[] instance or a similar raw data structure. The following example uses PushAudioInputStream to recognize speech, which is essentially an abstracted memory stream. The sample code does the following actions: Writes raw audio data to PushAudioInputStream by using the Write() function, which accepts a byte[] instance. Reads a .wav file by using FileReader for demonstration purposes. If you already have audio data in a byte[] instance, you can skip directly to writing the content to the input stream. The default format is 16-bit, 16-kHz mono pulse-code modulation (PCM) data. To customize the format, you can pass an AudioStreamFormat object to CreatePushStream() by using the static function AudioStreamFormat.GetWaveFormatPCM(sampleRate, (byte)bitRate, (byte)channels) ."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 17,
        "cited_text": "Creates a push stream by using createPushStream() . Reads a .wav file by using fs.createReadStream for demonstration purposes. If you already have audio data in the ArrayBuffer , you can skip directly to writing the content to the input stream. Creates an audio configuration by using the push stream. JavaScript Copy Using a push stream as input assumes that the audio data is raw pulse-code modulation (PCM) data that skips any headers. The API still works in certain cases if the header isn't skipped. For the best results, consider implementing logic to read off the headers so that fs begins at the start of the audio data ."
      },
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 18,
        "cited_text": "Repository files navigation README Code of conduct MIT license Silero VAD Silero VAD - pre-trained enterprise-grade Voice Activity Detector (also see our STT models ). Real Time Example real-time-example.mp4 Please note, that video loads only if you are logged in your GitHub account. Fast start Dependencies System requirements to run python examples on x86-64 systems: python 3.8+ ; 1G+ RAM; A modern CPU with AVX, AVX2, AVX-512 or AMX instruction sets. Dependencies: torch>=1.12.0 ; torchaudio>=0.12.0 (for I/O only); onnxruntime>=1.16.1 (for ONNX model usage)."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 19,
        "cited_text": "These problems can be addressed by setting one of two timeout properties on the SpeechConfig instance used to create a SpeechRecognizer : Segmentation silence timeout adjusts how much nonspeech audio is allowed within a phrase that's currently being spoken before that phrase is considered \"done.\" Higher values generally make results longer and allow longer pauses from the speaker within a phrase but make results take longer to arrive. They can also combine separate phrases into a single result when set too high. Lower values generally make results shorter and ensure more prompt and frequent breaks between phrases, but can also cause single phrases to separate into multiple results when set too low. This timeout can be set to integer values between 100 and 5000, in milliseconds, with 500 a typical default. Initial silence timeout adjusts how much nonspeech audio is allowed before a phrase before the recognition attempt ends in a \"no match\" result. Higher values give speakers more time to react and start speaking, but can also result in slow responsiveness when nothing is spoken. Lower values ensure a prompt \"no match\" for faster user experience and more controlled audio handling, but might cut a speaker off too quickly when set too low. Because continuous recognition generates many results, this value determines how often \"no match\" results arrive but doesn't otherwise affect the content of recognition results. This timeout can be set to any non-negative integer value, in milliseconds, or set to 0 to disable it entirely. 5000 is a typical default for single-shot recognition while 15000 is a typical default for continuous recognition."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 20,
        "cited_text": "If you follow these guidelines and don't get the results you expect from the API, see Troubleshooting & Support . For optimal results... If possible, avoid... Capture audio with a sampling rate of 16,000 Hz or higher. Lower sampling rates may reduce accuracy. However, avoid re-sampling. For example, in telephony the native rate is commonly 8000 Hz, which is the rate that should be sent to the service. Use a lossless codec to record and transmit audio. FLAC or LINEAR16 is recommended. Using mp3, mp4, m4a, mu-law, a-law or other lossy codecs during recording or transmission may reduce accuracy. If your audio is already in an encoding not supported by the API, transcode it to lossless FLAC or LINEAR16 . If your application must use a lossy codec to conserve bandwidth, we recommend the AMR_WB or OGG_OPUS codecs, in that preferred order."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 21,
        "cited_text": "Multiple people talking at the same time, or at different volumes may be interpreted as background noise and ignored. Use word and phrase hints to add names and terms to the vocabulary and to boost the accuracy for specific words and phrases. The recognizer has a very large vocabulary, however terms and proper names that are out-of-vocabulary will not be recognized. Sampling rate If possible, set the sampling rate of the audio source to 16000 Hz. For headerless codecs, use the explicit_decoding_config setting in RecognitionConfig to set sample_rate_hertz to match the native sample rate of the audio source (instead of re-sampling)."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 22,
        "cited_text": "Audio preprocessing It's best to provide audio that is as clean as possible by using a good quality and well-positioned microphone. However, applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy. The service is designed to handle noisy audio. For best results: Position the microphone as close as possible to the person that is speaking, particularly when background noise is present. Avoid audio clipping. Do not use automatic gain control (AGC). All noise reduction processing should be disabled. Listen to some sample audio. It should sound clear, without distortion or unexpected noise."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 23,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 24,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 25,
        "cited_text": "C# Copy Example: A recorded presenter's speech might be fast enough that several sentences in a row get combined, with large recognition results only arriving once or twice per minute. In this case, set the segmentation silence timeout to a lower value like 300 ms: C# Copy Example: A single-shot recognition asking a speaker to find and read a serial number ends too quickly while the number is being found. In this case, try a longer initial silence timeout like 10,000 ms: C# Copy Semantic segmentation Semantic segmentation is a speech recognition segmentation strategy that's designed to mitigate issues associated with silence-based segmentation :"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 26,
        "cited_text": "Since there are tradeoffs when modifying these timeouts, you should only change the settings when you have a problem related to silence handling. Default values optimally handle most spoken audio and only uncommon scenarios should encounter problems. Example: Users speaking a serial number like \"ABC-123-4567\" might pause between character groups long enough for the serial number to be broken into multiple results. In this case, try a higher value like 2000 milliseconds for the segmentation silence timeout:"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 27,
        "cited_text": "C# Copy Using a push stream as input assumes that the audio data is raw PCM and skips any headers. The API still works in certain cases if the header isn't skipped. For the best results, consider implementing logic to read off the headers so that byte[] begins at the start of the audio data . Handle errors The previous examples only get the recognized text from the speechRecognitionResult.Text property. To handle errors and other responses, you need to write some code to handle the result. The following code evaluates the speechRecognitionResult.Reason property and:"
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「语音活动检测 (VAD)」领域，根据 2026 年最新的技术文档与行业实践，核心研究突破与发展方向正从传统的“静音检测”向“语义深度理解”与“端侧极致优化”演进。以下是核心趋势、挑战与突破点的详细解析：\n\n### 1. 2025-2026 年关键技术趋势\n基于来源中 2026 年最新的更新，VAD 的技术趋势呈现出以下特征：\n\n*   **从静音分割转向语义分割 (Semantic Segmentation)**：这是目前最显著的突破。传统 VAD 仅依赖静音超时（Silence Timeouts）来切分音频，而最新的策略（如 Azure Speech SDK 1.41+ 版本中提出的方案）通过检测**句末标点符号**（如“.”或“?”）来触发分割 [1-3]。这种方法能生成语义更完整的文本片段，显著提升了长语音任务的可读性 [4-6]。\n*   **企业级大规模多语言模型**：如 **Silero VAD** 等预训练模型已实现在超过 **6000 种语言**的超大规模语料库上进行训练 [7, 8]。这使得 VAD 在不同语种、多种背景噪音和音频质量下具有极强的泛化能力 [7]。\n*   **提示词驱动的检测与识别 (Prompting-based Control)**：新一代模型（如 AssemblyAI 的 **Universal-3 Pro**）开始支持通过提示词（Prompting）进行微调和定制化，使得 VAD 与下游转写任务的衔接更加紧密和精确 [9, 10]。\n*   **端侧 (On-device) 与零延迟架构**：为了满足隐私（如 GDPR/HIPAA 合规）和实时性需求，VAD 引擎（如 Picovoice Cobra）正全面转向端侧运行，旨在消除网络波动带来的不确定延迟，实现**零延迟 (Zero-latency)** 响应 [11-13]。\n\n### 2. 未解决的挑战\n尽管技术在进步，但 sources 中也指出了当前 VAD 领域仍面临的瓶颈：\n\n*   **欠分割与“文本墙” (Under-segmentation)**：当用户持续讲话且停顿极短时，传统机制无法有效断句，导致输出长串难以阅读的文本 [4, 5, 14]。\n*   **过分割 (Over-segmentation)**：用户在思考时的短暂微弱停顿常被误判为语音结束，导致单句话被碎裂成多个片段 [4, 14]。\n*   **噪声环境下的鲁棒性**：虽然现代 VAD 被设计为能忽略背景噪声 [15]，但在极端噪音或回声环境下，识别精度仍会受损 [16]。\n*   **处理重复与幻觉**：在流式处理中，如何识别并过滤掉语音中的重复片段仍是开发者社区讨论的热点 [17]。\n\n### 3. 未来可能的突破点\n*   **语义分割的全面普及**：随着语义分割解决“停顿误判”问题的能力被证实，它有望取代单纯的静音超时成为行业标准，特别是在听写和实时字幕场景中 [2, 3, 18]。\n*   **极致轻量化与专用指令集加速**：目前的 JIT 模型已能压缩至 **2 MB** 左右，且在单核 CPU 上处理 30ms 音频仅需**不足 1ms** [7, 8]。未来突破点在于更深度的端到端优化，直接利用现代 CPU 的 AVX-512 或 AMX 指令集实现更低功耗的常驻监听 [19, 20]。\n*   **LLM 与 VAD 的深度融合**：来源提到将端侧 LLM（如 picoLLM）与 VAD 引擎结合，这暗示未来的 VAD 可能不再是独立的模块，而是作为感知层直接与大模型集成，通过语义上下文实时判断“倾听”的边界 [21, 22]。\n\n**特别提示**：关于 2025-2026 年的**具体学术论文名称**，由于所提供的来源主要为技术手册、GitHub 项目说明及 2026 年更新的官方文档，并未包含特定学术期刊的论文全文或引用列表。上述趋势是基于 2026 年 1 月至 4 月间更新的技术文档总结出的行业演进方向 [23-25]。",
    "conversation_id": "9ae38e85-cc2f-4a00-b3da-5ed5b388db02",
    "sources_used": [
      "cdaedc5e-2096-454d-941b-60772bff17a6",
      "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "0ee7d21b-a3a9-46d4-b565-208755247738",
      "7477fd7a-c13d-40ac-b442-14a8bf526ceb",
      "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2"
    ],
    "citations": {
      "1": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "2": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "3": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "4": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "5": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "6": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "7": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "8": "0ee7d21b-a3a9-46d4-b565-208755247738",
      "9": "7477fd7a-c13d-40ac-b442-14a8bf526ceb",
      "10": "7477fd7a-c13d-40ac-b442-14a8bf526ceb",
      "11": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "12": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "13": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "14": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "15": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "16": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "17": "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2",
      "18": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "19": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
      "20": "0ee7d21b-a3a9-46d4-b565-208755247738",
      "21": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "22": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
      "23": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
      "24": "cdaedc5e-2096-454d-941b-60772bff17a6",
      "25": "cdaedc5e-2096-454d-941b-60772bff17a6"
    },
    "references": [
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 1,
        "cited_text": "Speech containers provide websocket-based query endpoint APIs that are accessed through the Speech SDK and Speech CLI. By default, the Speech SDK and Speech CLI use the public Speech service. To use the container, you need to change the initialization method. Use a container host URL instead of key and region. For more information about containers, see Host URLs in Install and run Speech containers with Docker . Semantic segmentation Semantic segmentation is a speech recognition segmentation strategy that's designed to mitigate issues associated with silence-based segmentation:"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 2,
        "cited_text": "To use semantic segmentation, you need to set the following property on the SpeechConfig instance used to create a SpeechRecognizer : Python Copy Some of the limitations of semantic segmentation are as follows: You need the Speech SDK version 1.41 or later to use semantic segmentation. Semantic segmentation is only intended for use in continuous recognition . This includes scenarios such as dictation and captioning. It shouldn't be used in the single recognition mode or interactive scenarios. Semantic segmentation isn't available for all languages and locales. Semantic segmentation doesn't yet support confidence scores and NBest lists. As such, we don't recommend semantic segmentation if you're using confidence scores or NBest lists."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 3,
        "cited_text": "You need the Speech SDK version 1.41 or later to use semantic segmentation. Semantic segmentation is only intended for use in continuous recognition . This includes scenarios such as dictation and captioning. It shouldn't be used in the single recognition mode or interactive scenarios. Semantic segmentation isn't available for all languages and locales. Semantic segmentation doesn't yet support confidence scores and NBest lists. As such, we don't recommend semantic segmentation if you're using confidence scores or NBest lists."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 4,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 5,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 6,
        "cited_text": "Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly. Instead of only relying on silence timeouts, semantic segmentation mostly segments and returns final results when it detects sentence-ending punctuation (such as '.' or '?'). This improves the user experience with higher-quality, semantically complete segments and prevents long intermediate results."
      },
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 7,
        "cited_text": "You will have to implement the I/O; You will have to adapt the existing wrappers / examples / post-processing for your use-case. Using pip : pip install silero-vad Using torch.hub : Key Features Stellar accuracy Silero VAD has excellent results on speech detection tasks. Fast One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x faster. Lightweight JIT model is around two megabytes in size. General Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from different domains with various background noise and quality levels. Flexible sampling rate Silero VAD supports 8000 Hz and 16000 Hz sampling rates . Highly Portable Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere where these runtimes are available. No Strings Attached Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock."
      },
      {
        "source_id": "0ee7d21b-a3a9-46d4-b565-208755247738",
        "citation_number": 8,
        "cited_text": "You will have to implement the I/O; You will have to adapt the existing wrappers / examples / post-processing for your use-case. Using pip : pip install silero-vad Using torch.hub : Key Features Stellar accuracy Silero VAD has excellent results on speech detection tasks. Fast One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x faster. Lightweight JIT model is around two megabytes in size. General Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from different domains with various background noise and quality levels. Flexible sampling rate Silero VAD supports 8000 Hz and 16000 Hz sampling rates . Highly Portable Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere where these runtimes are available. No Strings Attached Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock."
      },
      {
        "source_id": "7477fd7a-c13d-40ac-b442-14a8bf526ceb",
        "citation_number": 9,
        "cited_text": "Recommended model We recommend Universal-3 Pro for pre-recorded audio transcription. It delivers the highest accuracy with support for fine-tuning and customization via prompting. For the broadest language coverage (99 languages), use [\"universal-3-pro\", \"universal-2\"] to automatically fall back to Universal-2 for unsupported languages. Prerequisites Before you begin, make sure you have: Python Python SDK JavaScript JavaScript SDK An AssemblyAI API key (get one by signing up at assemblyai.com ) Python 3.6 or later installed The requests library ( pip install requests )"
      },
      {
        "source_id": "7477fd7a-c13d-40ac-b442-14a8bf526ceb",
        "citation_number": 10,
        "cited_text": "Step 5: Access speaker diarization (optional) If you enabled speaker labels, you can access the speaker-separated utterances: Python Python SDK JavaScript JavaScript SDK Complete example Here is the full working code: Python Python SDK JavaScript JavaScript SDK Next steps Now that you have transcribed your first audio file: Learn how you can do even more with Universal-3 Pro with prompting Explore our Speech Understanding features for more ways to analyze your audio data Learn more about searching, summarizing, or asking questions on your transcript with our LLM Gateway feature Find out how to use webhooks to get notified when your transcripts are ready"
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 11,
        "cited_text": "Zero-latency Predictable and consistent response time with no network latency. Cloud Unbounded Response Time On-Device Guaranteed Response Time End-to-End Optimization Complete technological ownership enables fine-tuning at every layer rather than being constrained by third-party frameworks and pre-trained models. Learn More Accurate Outperforms alternatives with high margins, proven by open-source benchmarks. 2026-03-13T11:28:00.272749 image/svg+xml Matplotlib v3.10.8, https://matplotlib.org/ Hyper customizable"
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 12,
        "cited_text": "Custom wake words, voice commands, speech-to-text and small language models. ![](data:image/svg+xml;charset=utf-8,%3Csvg height='681' width='772' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E) Private All voice data is processed on-device. Intrinsically HIPAA and GDPR compliant. Lightweight Lightweight, edge-first architecture developed by Picovoice researchers. Enterprise Support Industry leading support for building innovative and complex AI-powered apps. Serious AI built for real-world scale"
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 13,
        "cited_text": "Voice AI picoLLM On-Device LLM Leopard Speech-to-Text Cheetah Streaming Speech-to-Text Orca Text-to-Speech Koala Noise Suppression Eagle Speaker Recognition Falcon Speaker Diarization Porcupine Wake Word Rhino Speech-to-Intent Cobra Voice Activity Detection Resources Docs Console Blog Use Cases Playground Contact Contact Sales Company About us Careers Follow Picovoice Subscribe to our newsletter Terms of Use Privacy Policy © 2019-2026 Picovoice Inc. This website uses cookies to enhance the user experience."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 14,
        "cited_text": "For more information about containers, see Host URLs in Install and run Speech containers with Docker . Semantic segmentation Semantic segmentation is a speech recognition segmentation strategy that's designed to mitigate issues associated with silence-based segmentation: Under-segmentation: When users speak for a long time without pauses, they can see a long sequence of text without breaks (\"wall of text\"), which severely degrades their readability experience. Over-segmentation: When a user pauses for a short time, the silence detection mechanism can segment incorrectly."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 15,
        "cited_text": "The recognizer is designed to ignore background voices and noise without additional noise-canceling. However, for optimal results, position the microphone as close to the user as possible, particularly when background noise is present. Excessive background noise and echoes may reduce accuracy, especially if a lossy codec is also used. If you are capturing audio from more than one person, and each person is recorded on a separate channel, send each channel separately to get the best recognition results. However, if all speakers are mixed in a single channel recording, send the recording as is."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 16,
        "cited_text": "Audio preprocessing It's best to provide audio that is as clean as possible by using a good quality and well-positioned microphone. However, applying noise-reduction signal processing to the audio before sending it to the service typically reduces recognition accuracy. The service is designed to handle noisy audio. For best results: Position the microphone as close as possible to the person that is speaking, particularly when background noise is present. Avoid audio clipping. Do not use automatic gain control (AGC). All noise reduction processing should be disabled. Listen to some sample audio. It should sound clear, without distortion or unexpected noise."
      },
      {
        "source_id": "b9e20ba3-0b46-4d84-8902-7aea8bbf68e2",
        "citation_number": 17,
        "cited_text": "1 You must be logged in to vote 💬 Problem with repetitions lukasc-ubc started on Nov 17, 2024 in General 6 1 You must be logged in to vote 🙌 StarWhisper - Windows desktop app with local transcription PeakProductivity started 3 weeks ago in Show and tell 0 6 You must be logged in to vote 🙌 MacWhisper - Full featured native Whisper for Mac jordibruin started on Mar 14, 2023 in Show and tell 1 1 You must be logged in to vote 🙌 AI Agents call OpenAI API without an touching an API key"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 18,
        "cited_text": "To use semantic segmentation, you need to set the following property on the SpeechConfig instance used to create a SpeechRecognizer : Java Copy Some of the limitations of semantic segmentation are as follows: You need the Speech SDK version 1.41 or later to use semantic segmentation. Semantic segmentation is only intended for use in continuous recognition . This includes scenarios such as dictation and captioning. It shouldn't be used in the single recognition mode or interactive scenarios. Semantic segmentation isn't available for all languages and locales. Semantic segmentation doesn't yet support confidence scores and NBest lists. As such, we don't recommend semantic segmentation if you're using confidence scores or NBest lists."
      },
      {
        "source_id": "6043cfb1-b0b3-4d52-9e90-2757f5d284ce",
        "citation_number": 19,
        "cited_text": "Repository files navigation README Code of conduct MIT license Silero VAD Silero VAD - pre-trained enterprise-grade Voice Activity Detector (also see our STT models ). Real Time Example real-time-example.mp4 Please note, that video loads only if you are logged in your GitHub account. Fast start Dependencies System requirements to run python examples on x86-64 systems: python 3.8+ ; 1G+ RAM; A modern CPU with AVX, AVX2, AVX-512 or AMX instruction sets. Dependencies: torch>=1.12.0 ; torchaudio>=0.12.0 (for I/O only); onnxruntime>=1.16.1 (for ONNX model usage)."
      },
      {
        "source_id": "0ee7d21b-a3a9-46d4-b565-208755247738",
        "citation_number": 20,
        "cited_text": "Repository files navigation README Code of conduct MIT license Silero VAD Silero VAD - pre-trained enterprise-grade Voice Activity Detector (also see our STT models ). Real Time Example real-time-example.mp4 Please note, that video loads only if you are logged in your GitHub account. Fast start Dependencies System requirements to run python examples on x86-64 systems: python 3.8+ ; 1G+ RAM; A modern CPU with AVX, AVX2, AVX-512 or AMX instruction sets. Dependencies: torch>=1.12.0 ; torchaudio>=0.12.0 (for I/O only); onnxruntime>=1.16.1 (for ONNX model usage)."
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 21,
        "cited_text": "MacBook Air M1 2020, macOS 15.5, 8GB RAM Your browser does not support the video tag. MacBook Air M1 2020, macOS 15.5, 8GB RAM Your browser does not support the video tag. Microsoft Surface Laptop Studio 2 2023, Windows 11, 16GB RAM Learn more about the products used in this demo: Porcupine Wake Word Cheetah Streaming Speech-to-Text picoLLM On-Device LLM Orca Streaming Text-to-Speech Start building with the open-source demo: pico-cookbook Develop smarter products with no compromises Accurate and lightweight on-device AI engines at your fingertips."
      },
      {
        "source_id": "b9f52407-3959-4c1c-b32c-71e63e64ae1a",
        "citation_number": 22,
        "cited_text": "On-Device LLM Speech-to-Text Streaming STT Noise Suppression Speaker Recognition Speaker Diarization Wake Word Speech-to-Intent Voice Activity Detection Text-to-Speech picoLLM On-Device LLM End-to-end platform that compresses any LLM without sacrificing accuracy and runs across web, mobile, desktop, and embedded devices. Start Building Learn More Model used: Llama 3.2 Hello, Llama! Hello! Start the demo to begin a conversation. Start Demo Why Picovoice? Bringing cloud performance and convenience to the edge with no compromises."
      },
      {
        "source_id": "dff21c3f-f3ec-44d5-8ef7-81a6cdc5f1b2",
        "citation_number": 23,
        "cited_text": "Was this helpful? Send feedback Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-04-01 UTC. Products and pricing See all products Google Cloud pricing Google Cloud Marketplace Contact sales Support Community forums Support Release Notes System status"
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 24,
        "cited_text": "Feedback Was this page helpful? Yes No No Need help with this topic? Want to try using Ask Learn to clarify or guide you through this topic? Ask Learn Ask Learn Suggest a fix? Additional resources Last updated on 01/30/2026 In this article Convert speech to text Related content Was this page helpful? Yes No No Need help with this topic? Want to try using Ask Learn to clarify or guide you through this topic? Ask Learn Ask Learn Suggest a fix? Ask Learn Preview Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation."
      },
      {
        "source_id": "cdaedc5e-2096-454d-941b-60772bff17a6",
        "citation_number": 25,
        "cited_text": "Please sign in to use Ask Learn. Sign in English (United States) Your Privacy Choices Theme Light Dark High contrast AI Disclaimer Previous Versions Blog Contribute Privacy Consumer Health Privacy Terms of Use Trademarks © Microsoft 2026"
      }
    ]
  }
}
