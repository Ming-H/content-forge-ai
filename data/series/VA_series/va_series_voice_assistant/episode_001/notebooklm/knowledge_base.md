# 知识库：语音识别全景：从 HMM 到端到端神经网络的演进

生成时间: 2026-04-02 09:29
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "根据您提供的来源，语音识别（ASR）技术已从传统的混合模型演进为端到端（End-to-End, E2E）神经网络架构。以下是核心技术架构与关键组件的概述：\n\n### 1. 技术演进路线\n语音识别经历了从模块化混合系统到高度集成化端到端系统的演进：\n*   **传统/混合阶段**：早期以 **DNN/HMM**（深度神经网络/隐马尔可夫模型）混合架构为主，将声学模型、语言模型和词典分开处理 [1, 2]。\n*   **端到端（E2E）起步阶段**：引入了 **CTC**（连接时序分类）和 **Attention-based**（基于注意力机制）模型，旨在通过单个神经网络取代传统流水线的多个阶段 [2, 3]。\n*   **高性能/流式演进阶段**：发展出 **Transducer**（传感器）架构，支持流式识别，并引入了 **Transformer** 和 **Conformer** 等先进编码器架构 [4, 5]。\n*   **大模型/多任务阶段**：出现了如 **OpenAI Whisper** 和 **Amazon Transcribe** 这样的下一代多参数基础模型，能够同时处理多语言识别、翻译和语种识别 [3, 6]。\n\n### 2. 主要架构模式与核心算法\n根据来源，主流的 E2E 架构分为以下几类：\n*   **混合 CTC/Attention 架构**：利用 CTC 进行快速训练并辅助对齐，同时结合 Attention 机制提升解码精度 [2]。\n*   **Transducer (RNN-T) 架构**：由 **Encoder**（编码器）、**Decoder/Predictor**（解码器/预测器）和 **Joint Network**（联合网络）三个模块组成，支持流式输出 [7, 8]。\n*   **序列到序列 (Seq2Seq) 架构**：如 Whisper 采用的 **Transformer 编码器-解码器** 结构，通过自回归方式预测标记序列 [3, 9]。\n*   **关键算法名称**：\n    *   **声学特征提取**：传统频谱特征、**Self-supervised Learning Representations** (如 HuBERT, Wav2Vec2.0) [5, 10, 11]。\n    *   **编码器算法**：VGG, CNN, BiRNN, **Transformer**, **Conformer**, **Branchformer**, **E-Branchformer** [2, 8]。\n    *   **解码/搜索算法**：**Beam Search**（束搜索）、**Time Synchronous Decoding** (TSD)、**Alignment-Length Synchronous Decoding** (ALSD) [4, 12]。\n\n### 3. 核心技术组件\n*   **前端 (Frontend)**：负责特征提取和文本预处理。现代框架（如 ESPnet2）支持“在线（On-the-fly）”提取 [13]。\n*   **编码器 (Encoder)**：将音频信号转换为高层抽象表示，常用 **Conformer** 结合了卷积和自注意力机制的优点 [8, 14]。\n*   **解码器 (Decoder)**：负责生成预测文本，支持 **RNN**, **Stateless**（无状态）, **MEGA**, **RWKV** 等不同实现 [4, 15]。\n*   **语言模型 (LM)**：虽然端到端模型内部集成了语言能力，但仍可引入外部的 **RNNLM**, **TransformerLM** 或 **N-gram** 进一步优化结果 [2, 16]。\n\n### 4. 关键技术指标\n衡量语音识别系统性能的核心指标包括：\n*   **准确率指标**：\n    *   **CER (Character Error Rate)**：字符错误率，常用于中文识别 [17, 18]。\n    *   **WER (Word Error Rate)**：词错误率，常用于英文识别 [17, 18]。\n*   **效率与实时性指标**：\n    *   **RTF (Real-Time Factor)**：实时因子，计算公式为“总解码时间 / 总音频时长” [19, 20]。\n    *   **Latency**：延迟，通常以“毫秒/句子”为单位衡量流式或非流式系统的响应速度 [19, 20]。\n*   **可扩展性**：支持的语言数量（如 Google Cloud 和 Amazon 支持 100+ 语言）及对噪声环境的鲁棒性 [21-23]。",
    "conversation_id": "1d51604e-53db-4bef-b2ff-c6744401b23d",
    "sources_used": [
      "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "b8469813-5d75-4eab-8fda-7f5cc2f5a49f"
    ],
    "citations": {
      "1": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "2": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "3": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "4": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "5": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "6": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "7": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "8": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "9": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "10": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "11": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "12": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "13": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "14": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "15": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "16": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "17": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "18": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "19": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "20": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "21": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "22": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "23": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f"
    },
    "references": [
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 1,
        "cited_text": "ESPnet: end-to-end speech processing toolkit system/pytorch ver.   2.5.1   2.7.1   2.8.0   2.9.1   ubuntu/python3.10/pip ubuntu/python3.12/pip ubuntu/python3.10/conda debian12/python3.10/conda windows/python3.10/pip macos/python3.10/pip macos/python3.10/conda Docs | Example (ESPnet2) | Docker | Notebook ESPnet is an end-to-end speech processing toolkit covering end-to-end speech recognition, text-to-speech, speech translation, speech enhancement, speaker diarization, spoken language understanding, and so on. ESPnet uses pytorch as a deep learning engine and also follows Kaldi style data processing, feature extraction/format, and recipes to provide a complete setup for various speech processing experiments."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 2,
        "cited_text": "ASR: Automatic Speech Recognition State-of-the-art performance in several ASR benchmarks (comparable/superior to hybrid DNN/HMM and CTC) Hybrid CTC/attention based end-to-end ASR Fast/accurate training with CTC/attention multitask training CTC/attention joint decoding to boost monotonic alignment decoding Encoder: VGG-like CNN + BiRNN (LSTM/GRU), sub-sampling BiRNN (LSTM/GRU), Transformer, Conformer, Branchformer , or E-Branchformer Decoder: RNN (LSTM/GRU), Transformer, or S4 Attention: Flash Attention , Dot product, location-aware attention, variants of multi-head Incorporate RNNLM/LSTMLM/TransformerLM/N-gram trained only with text data Batch GPU decoding Data augmentation"
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 3,
        "cited_text": "Whisper [Blog] [Paper] [Model card] [Colab example] Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification. Approach A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 4,
        "cited_text": "Transducer based end-to-end ASR Architecture: Custom encoder supporting RNNs, Conformer, Branchformer (w/ variants), 1D Conv / TDNN. Decoder w/ parameters shared across blocks supporting RNN, stateless w/ 1D Conv, MEGA , and RWKV . Pre-encoder: VGG2L or Conv2D available. Search algorithms: Greedy search constrained to one emission by timestep. Default beam search algorithm [Graves, 2012] without prefix search. Alignment-Length Synchronous decoding [Saon et al., 2020] . Time Synchronous Decoding [Saon et al., 2020] . N-step Constrained beam search modified from [Kim et al., 2020] . modified Adaptive Expansion Search based on [Kim et al., 2021] and NSC."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 5,
        "cited_text": "Self-supervised learning representations as features, using upstream models in S3PRL in frontend. Set  frontend  to  s3prl Select any upstream model by setting the  frontend_conf  to the corresponding name. Transfer Learning : easy usage and transfers from models previously trained by your group or models from ESPnet Hugging Face repository . Documentation and toy example runnable on colab . Streaming Transformer/Conformer ASR with blockwise synchronous beam search. Restricted Self-Attention based on Longformer as an encoder for long sequences OpenAI Whisper model, robust ASR based on large-scale, weakly-supervised multitask learning"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 6,
        "cited_text": "Skip to main content Contact us AWS Marketplace Sign in to console Create account Amazon Transcribe Overview Use Cases Features Pricing Getting Started More Products Artificial Intelligence Amazon Transcribe Amazon Transcribe Automatically convert speech to text and gain insights Get started with Amazon Transcribe Try Free Demo Why Amazon Transcribe? Amazon Transcribe is a fully managed, automatic speech recognition (ASR) service that makes it easy for developers to add speech to text capabilities to their applications. It is powered by a next-generation, multi-billion parameter speech foundation model that delivers high accuracy transcriptions for streaming and recorded speech. Thousands of customers across industries use it to automate manual tasks, unlock rich insights, increase accessibility, and boost discoverability of audio and video content."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 7,
        "cited_text": "Limitations Only non-streaming inference mode is supported currently The decoding stage 12 in  asr.sh  automatically runs the rtf & latency calculation if  \"asr_inference_tool == \"espnet2.bin.asr_inference\" ; other inference tools like k2 & maskctc are still left to do Transducer ASR Important : If you encounter any issue related to  warp-transducer , please open an issue in our forked repo . ESPnet2 supports models trained with the (RNN-)Tranducer loss, aka Transducer models. Currently, two versions of these models exist within ESPnet2: one under  asr  and the other under  asr_transducer . The first one is designed as a supplement of CTC-Attention ASR models while the second is designed independently and purely for the Transducer task. For that, we rely on  ESPnetASRTransducerModel  instead of  ESPnetASRModel  and a new task called  ASRTransducerTask  is used in place of  ASRTask ."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 8,
        "cited_text": "The architecture is composed of three modules: encoder, decoder and joint network. Each module has one (or three) config(s) with various parameters in order to configure the internal parts. The following sections describe the mandatory and optional parameters for each module. Encoder For the encoder, we propose a unique encoder type encapsulating the following blocks: Branchformer, Conformer, Conv 1D and E-Branchformer. It is similar to the custom encoder in ESPnet1, meaning we don't need to set the parameter  encoder: [type]  here. Instead, the encoder architecture is defined by three configurations passed to  encoder_conf :"
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 9,
        "cited_text": "Internally, the  transcribe()  method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window. Below is an example usage of  whisper.detect_language()  and  whisper.decode()  which provide lower-level access to the model. import   whisper   model   =   whisper . load_model ( \"turbo\" )  # load audio and pad/trim it to fit 30 seconds   audio   =   whisper . load_audio ( \"audio.mp3\" )  audio   =   whisper . pad_or_trim ( audio )  # make log-Mel spectrogram and move to the same device as the model   mel   =   whisper . log_mel_spectrogram ( audio ,  n_mels = model . dims . n_mels ). to ( model . device )  # detect the spoken language   _ ,  probs   =   model . detect_language ( mel )  print ( f\"Detected language:  { max ( probs ,  key = probs . get ) } \" )  # decode the audio   options   =   whisper . DecodingOptions ()  result   =   whisper . decode ( model ,  mel ,  options )  # print the recognized text   print ( result . text )"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 10,
        "cited_text": "The stage number differs according to the task. Please read the task-specific shell script (e.g.,  asr1/asr.sh ) to see the number to specify. The packed model can be uploaded to huggingface by setting the previously mentioned flags. Usage of Self-Supervised Learning Representations as feature ESPnet supports self-supervised learning representations (SSLR) to replace traditional spectrum features. In some cases, SSLRs can boost the performance. To use SSLRs in your task, you need to make several modifications."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 11,
        "cited_text": "Install S3PRL by  tools/installers/install_s3prl.sh . If HuBERT / Wav2Vec is needed, fairseq should be installed by  tools/installers/install_fairseq.sh . Here's various tips for using SSLRs. To reduce the time used in  collect_stats  step, please specify  --feats_normalize uttmvn  in  run.sh  and pass it as arguments to  asr.sh  or other task-specific scripts. (Recommended) In the configuration file, specify the  frontend  and  preencoder . Taking  HuBERT  as an example: The  upstream  name can be whatever supported in S3PRL.  multilayer-feature=True  means the final representation is a weighted-sum of all layers' hidden states from SSLR model. frontend: s3prl   frontend_conf:    frontend_conf:    upstream: hubert_large_ll60k # Note: If the upstream is changed, please change the input_size in the preencoder.    download_dir: ./hub    multilayer_feature: True Here the  preencoder  is to reduce the input dimension to the encoder, to reduce the memory cost. The  input_size  depends on the upstream model, while the  output_size  can be set to any values. preencoder: linear   preencoder_conf:    input_size: 1024 # Note: If the upstream is changed, please change this value accordingly.    output_size: 80 Because the shift sizes of different  upstream  models are different, e.g.  HuBERT  and  Wav2Vec2.0  have  20ms  frameshift. Sometimes, the downsampling rate ( input_layer ) in the  encoder  configuration need to be changed. For example, using  input_layer: conv2d2  will results in a total frameshift of  40ms , which is enough for some tasks."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 12,
        "cited_text": "Inference Various decoding algorithms are also available for Transducer by setting  search_type  parameter in your decode config: Beam search algorithm without prefix search [Graves, 2012] . ( search_type: default ) Time Synchronous Decoding [Saon et al., 2020] . ( search_type: tsd ) Alignment-Length Synchronous Decoding [Saon et al., 2020] . ( search_type: alsd ) modified Adaptive Expansion Search, based on [Kim et al., 2021] and [Boyer et al., 2021] . ( search_type: maes ) The algorithms share two parameters to control the beam size ( beam_size ) and the partial/final hypotheses normalization ( score_norm ). In addition, three algorithms have specific parameters:"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 13,
        "cited_text": "On the fly feature extraction & text preprocessing for training You don't need to create the feature file before training, but just input wave data directly. We support both raw wave input and extracted features. The preprocessing for text, tokenization to characters, or sentencepieces, can be also applied during training. Support self-supervised learning representations from s3prl Discarding the JSON format describing the training corpus. Why do we discard the JSON format? Because a dict object generated from a large JSON file requires much memory and it also takes much time to parse such a large JSON file."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 14,
        "cited_text": "(float, default = 0.0)    att_dropout_rate (optional) :  Dropout rate for the attention module. (float, default = 0.0)    # Conformer    -  block_type :  conformer    hidden_size :  Hidden (and output) dimension. (int)    linear_size :  Dimension of feed-forward module. (int)    conv_mod_kernel_size :  Size of the convolving kernel in the ConformerConvolution module. (int)    heads (optional) :  Number of heads in multi-head attention. (int, default = 4)    norm_eps (optional) :  Epsilon value for normalization module. (float, default = 1e-05 or 0.25 for BasicNorm)    norm_partial (optional) :  Partial value for the normalization module, if norm_type = 'rms_norm'. (float, default = -1.0)    conv_mod_norm_eps (optional) :  Epsilon value for Batchnorm1d in the ConformerConvolution module. (float, default = 1e-05)    conv_mod_norm_momentum (optional) :  Momentum value for Batchnorm1d in the ConformerConvolution module."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 15,
        "cited_text": "Decoder For the decoder, four types of blocks are available: stateless ('stateless'), RNN ('rnn'), MEGA ('mega') or RWKV ('rwkv'). Contrary to the encoder, the parameters are shared across the blocks, meaning we only define one block in the configuration. The type of the stack of blocks is defined by passing the corresponding type string to the parameter  decoder . The internal parts are defined through the field  decoder_conf  containing the following controlable parameters: decoder_conf :    embed_size :  Size of the embedding layer (int, default = 256).    num_blocks :  Number of decoder blocks/layers (int, default = 4 for MEGA or 1 for RNN).    rnn_type (RNN only) :  Type of RNN cells (int, default = \"lstm\").    hidden_size (RNN only) :  Size of the hidden layers (int, default = 256).    block_size (MEGA/RWKV only) :  Size of the block's input/output (int, default = 512).    linear_size (MEGA/RWKV only) :  Feed-Forward module hidden size (int, default = 1024).    attention_size (RWKV only) :  Hidden-size of the attention module. (int, default = None).    context_size (RWKV only) :  Context size for the WKV kernel module (int, default = 1024).    qk_size (MEGA only) :  Shared query and key size for attention module (int, default = 128).    v_size (MEGA only) :  Value size for attention module (int, default = 1024).    chunk_size (MEGA only) :  Chunk size for attention computation (int, default = -1, i.e. full context).    num_heads (MEGA only) :  Number of EMA heads (int, default = 4).    rel_pos_bias (MEGA only) :  Type of relative position bias in attention module (str, default = \"simple\").    max_positions (MEGA only) :  Maximum number of position for RelativePositionBias (int, default = 2048).    truncation_length (MEGA only) :  Maximum length for truncation in EMA module (int, default = None).    normalization_type (MEGA/RWKV only) :  Normalization layer type (str, default = \"layer_norm\").    normalization_args (MEGA/RKWV only) :  Normalization layer arguments (dict, default = {}).    activation_type (MEGA only) :  Activation function type (str, default = \"swish\").    activation_args (MEGA only) :  Activation function arguments (dict, default = {}).    rescale_every (RWKV only) :  Whether to rescale input every N blocks during inference (int, default = 0)    dropout_rate (excl. RWKV) :  Dropout rate for main block modules (float, default = 0.0).    embed_dropout_rate :  Dropout rate for embedding layer (float, default = 0.0).    att_dropout_rate (MEGA/RWKV only) :  Dropout rate for the attention module.    ema_dropout_rate (MEGA only) :  Dropout rate for the EMA module.    ffn_dropout_rate (MEGA/RWKV only) :  Dropout rate for the feed-forward module."
      },
      {
        "source_id": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
        "citation_number": 16,
        "cited_text": "For more information please see: streaming asr and streaming tts Model List PaddleSpeech supports a series of most popular models. They are summarized in released models and attached with available pretrained models. Speech-to-Text contains Acoustic Model , Language Model , and Speech Translation , with the following details: Speech-to-Text Module Type   Dataset   Model Type   Example   Speech Recogination   Aishell   DeepSpeech2 RNN + Conv based Models deepspeech2-aishell Transformer based Attention Models u2.transformer.conformer-aishell Librispeech   Transformer based Attention Models deepspeech2-librispeech / transformer.conformer.u2-librispeech / transformer.conformer.u2-kaldi-librispeech TIMIT   Unified Streaming & Non-streaming Two-pass u2-timit Alignment   THCHS30   MFA mfa-thchs30 Language Model   Ngram Language Model kenlm Speech Translation (English to Chinese)   TED En-Zh   Transformer + ASR MTL transformer-ted FAT + Transformer + ASR MTL fat-st-ted"
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 17,
        "cited_text": "ASR results expand We list the character error rate (CER) and word error rate (WER) of major ASR tasks. Task   CER (%)   WER (%)   Pre-trained model   Aishell dev/test   4.6/5.1   N/A link ESPnet2 Aishell dev/test   4.1/4.4   N/A link Common Voice dev/test   1.7/1.8   2.2/2.3 link CSJ eval1/eval2/eval3   5.7/3.8/4.2   N/A link ESPnet2 CSJ eval1/eval2/eval3   4.5/3.3/3.6   N/A link ESPnet2 GigaSpeech dev/test   N/A   10.6/10.5 link HKUST dev   23.5   N/A link ESPnet2 HKUST dev   21.2   N/A link Librispeech dev_clean/dev_other/test_clean/test_other   N/A   1.9/4.9/2.1/4.9 link ESPnet2 Librispeech dev_clean/dev_other/test_clean/test_other   0.6/1.5/0.6/1.4   1.7/3.4/1.8/3.6 link Switchboard (eval2000) callhm/swbd   N/A   14.0/6.8 link ESPnet2 Switchboard (eval2000) callhm/swbd   N/A   13.4/7.3 link TEDLIUM2 dev/test   N/A   8.6/7.2 link ESPnet2 TEDLIUM2 dev/test   N/A   7.3/7.1 link TEDLIUM3 dev/test   N/A   9.6/7.6 link WSJ dev93/eval92   3.2/2.1   7.0/4.7   N/A ESPnet2 WSJ dev93/eval92   1.1/0.8   2.8/1.8 link Note that the performance of the CSJ, HKUST, and Librispeech tasks was significantly improved by using the wide network (#units = 1024) and large subword units if necessary reported by RWTH ."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 18,
        "cited_text": "Whisper's performance varies widely depending on the language. The figure below shows a performance breakdown of  large-v3  and  large-v2  models by language, using WERs (word error rates) or CER (character error rates, shown in Italic ) evaluated on the Common Voice 15 and Fleurs datasets. Additional WER/CER metrics corresponding to the other models and datasets can be found in Appendix D.1, D.2, and D.4 of the paper , as well as the BLEU (Bilingual Evaluation Understudy) scores for translation in Appendix D.3."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 19,
        "cited_text": "In order to calculate real-time-factor and (non-streaming) latency the script  utils/calculate_rtf.py  has been reworked and can now be used for both ESPnet1 and ESPnet2. The script calculates inference times based on time markers in the decoding log files and reports the average real-time-factor (RTF) and average latency over all decoded utterances. For ESPnet2, the script will automatically be run (see Limitations section below) after the decoding stage has finished but can also be run as a stand-alone script:"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 20,
        "cited_text": "# ../../../utils/calculate_rtf.py --log-dir exp/byan/librispeech_asr_train_asr_conformer_raw_bpe_batch_bins30000000_accum_grad3_optim_conflr0.001_sp/decode_as   r_lm_lm_train_lm_transformer2_en_bpe5000_valid.loss.ave_asr_model_valid.acc.ave/test_clean/logdir  --log-name  asr_inference  --input-shift  0.0625  --start-times-   marker  \"speech length\"  --end-times-marker  \"best hypo\"   Total  audio  duration:  19452.481  [sec]   Total  decoding  time:  137762.231  [sec]   RTF:  7.082   Latency:  52581.004  [ms/sentence]"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 21,
        "cited_text": "Realize the value of your speech data today with Amazon Transcribe. Benefits of Amazon Transcribe Easily embed voice technologies in your applications with Amazon Transcribe, a fully managed, multi-billion parameter speech foundation model that instantly converts real-time or recorded speech into text. It is trained on millions of hours of audio data across a variety of languages. Amazon Transcribe accounts for different accents, noisy environments, and acoustic conditions that enables you to produce more accurate outputs."
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 22,
        "cited_text": "Use key features across 100+ languages that make it easy to use and customize. These include features such as automatic punctuation, custom vocabulary, automatic language identification, speaker diarization, word-level confidence scores, and vocabulary filters.   Access advanced features such as redaction of sensitive information, automatic language detection, content moderation, and custom language models. Extract key business insights from customer calls, video files, clinical conversations and more.   Automatically extracts insights such as sentiment, call categories, call characteristics, and generative AI-powered summaries with Amazon Transcribe Call Analytics."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 23,
        "cited_text": "Supports over 125 languages Use AI to caption videos How to use Speech-to-Text 02:26 mins Features Advanced speech AI Speech-to-Text can utilize Chirp 3 , Google Cloud’s foundation model for speech trained on millions of hours of audio data and billions of text sentences. This contrasts with traditional speech recognition techniques that focus on large amounts of language-specific supervised data. These techniques give users improved recognition and transcription for more spoken languages and accents."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "语音识别技术（ASR）的演进标志着从传统的模块化混合模型（如 DNN/HMM）转向了高度集成的**端到端（End-to-End, E2E）神经网络架构**。这种转变简化了训练流程，并在多个公开数据集上达到了 SOTA（前沿）性能 [1-3]。\n\n以下是核心实现细节、架构设计、优化策略及竞品对比的详细解析：\n\n### 1. 核心算法流程与实现细节\n\n现代端到端系统主要基于三种核心算法框架：**CTC**、**Attention-based Seq2Seq** 以及 **Transducer (RNN-T)**。\n\n*   **Hybrid CTC/Attention 架构**：\n    *   **流程**：结合了 CTC 的快速收敛与单调对齐特性，以及 Attention 机制对长序列特征的捕捉能力 [2]。\n    *   **实现**：在训练阶段采用多任务学习（Multitask Training），同时优化 CTC 损失和交叉熵（Attention 损失） [2]。在解码阶段，利用 CTC 进行联合解码以引导 Attention 的对齐 [2]。\n*   **Transducer (RNN-T) 架构**：\n    *   **组件**：由 **Encoder**（音频特征提取）、**Decoder/Predictor**（语言模型特征提取）和 **Joint Network**（信息融合）组成 [4-6]。\n    *   **优势**：天生支持流式识别，因为它不依赖于整句的全局注意力 [6, 7]。\n*   **Whisper (Large-Scale Seq2Seq)**：\n    *   **流程**：采用典型的 **Transformer 编码器-解码器** 结构，将音频切分为 30 秒的滑动窗口 [8, 9]。\n    *   **任务表示**：通过一组**特殊标记（Special Tokens）**定义任务（如识别、翻译、语种检测），实现多任务并行处理 [8]。\n\n### 2. 关键代码架构：以 ESPnet2 与 WeNet 为例\n\n*   **ESPnet2 的解耦架构**：\n    *   **核心特性**：摒弃了对 Kaldi 的强制依赖，实现了 **\"On-the-fly\"（在线）** 特征提取和文本预处理，这意味着在训练过程中直接输入原始波形即可 [10, 11]。\n    *   **代码结构**：采用 **Recipe（配方）** 模式，通过 `run.sh` 作为入口，涵盖数据准备、模型定义、训练及评估全流程 [12, 13]。\n*   **WeNet 的生产级设计**：\n    *   **架构理念**：**\"Production First\"**，专注于云端和边缘侧的部署 [3, 14]。\n    *   **跨平台支持**：支持 x86、x86_64 以及昇腾 NPU 等硬件环境，并提供 C++ 运行时环境用于高性能流式服务 [15, 16]。\n\n### 3. 性能优化策略\n\n*   **流式识别优化**：\n    *   **分块注意力**：引入 **Blockwise/Contextual Block Transformer/Conformer**，通过受限的注意力范围减少延迟 [17, 18]。\n    *   **动态分块训练**：在训练中随机调整分块大小，使模型能同时适应离线和在线识别场景 [19]。\n*   **正则化与损失增强**：\n    *   **FastEmit**：专门用于 Transducer 模型，通过鼓励模型尽早发射标记来降低延迟 [7, 20]。\n    *   **Pruned RNN-T**：在 k2 工具包中实现的剪枝损失函数，能够显着减少显存消耗并提升训练速度 [21]。\n*   **解码算法优化**：\n    *   除了传统的束搜索（Beam Search），还演进出 **时间同步解码 (TSD)**、**对齐长度同步解码 (ALSD)** 以及 **改进的自适应扩展搜索 (MAES)** 等，以平衡解码速度与精度 [6, 22, 23]。\n\n### 4. 竞品技术对比与具体参数\n\n语音识别领域目前形成了“公有云 API”与“开源基础模型”两大阵营：\n\n#### 技术参数对比表\n\n| 特性指标 | **OpenAI Whisper (Turbo)** | **Google Chirp 3 (V2 API)** | **Amazon Transcribe** | **ESPnet2 (Conformer)** |\n| :--- | :--- | :--- | :--- | :--- |\n| **参数规模** | ~809 M (Turbo 版) [24] | 数十亿参数 [25, 26] | 数十亿参数 [27] | 灵活 (常为 100M-300M) [28] |\n| **VRAM 占用** | ~6 GB [24] | 云端处理 (不适用) | 云端处理 (不适用) | 灵活 (取决于模型配置) |\n| **多语言支持** | 99+ 语种 [8, 29] | 100+ 语种 [26] | 100+ 语种 [30] | 依赖数据集 (支持 100+) [31] |\n| **价格** | 开源/MIT 协议 [32] | $0.016 / 分钟 [33] | 按使用量计费 [27] | 开源/Apache-2.0 [34] |\n| **主要特性** | 极强的鲁棒性、多任务 [8] | 自监督训练 (28B 文本句) [26] | 针对噪声、口音优化 [35] | 极致的可复现性、SOTA 精度 [1] |\n\n#### 性能表现数据\n*   **准确率 (WER/CER)**：\n    *   **ESPnet2** 在 **Aishell** 数据集上的 CER 达到 **4.1% (dev) / 4.4% (test)** [28]。\n    *   **ESPnet2** 在 **Librispeech** 干净数据集上的 WER 低至 **1.7%** [28]。\n*   **效率 (RTF)**：\n    *   Whisper **Turbo** 版相比 Large-v3 提升了约 **8倍** 的推理速度，且精度损失极小 [24]。\n    *   ESPnet2 提供的 Conformer 模型在 Librispeech 上的 RTF 约为 **7.082**（非流式单核解码） [36]。\n\n### 5. 总结\n语音识别的演进路径是从 **HMM 模块化设计** 逐步走向以 **Transformer/Conformer 为基座的基础模型 (Foundation Models)** [25, 27]。大型云服务商（如 Google、AWS、Azure）正通过数亿小时的音频进行自监督预训练，以提供更强的多语言适应能力 [26, 35]；而开源框架（如 ESPnet、WeNet、PaddleSpeech）则在模型结构的精细优化与生产级部署上持续发力 [3, 37, 38]。",
    "conversation_id": "1d51604e-53db-4bef-b2ff-c6744401b23d",
    "sources_used": [
      "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281"
    ],
    "citations": {
      "1": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "2": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "3": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "4": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "5": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "6": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "7": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "8": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "9": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "10": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "11": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "12": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "13": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "14": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "15": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "16": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "17": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "18": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "19": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "20": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "21": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "22": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "23": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "24": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "25": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "26": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "27": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "28": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "29": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "30": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "31": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "32": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "33": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "34": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "35": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "36": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "37": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "38": "3736b005-7a2c-452c-9caa-1183bb8c7a99"
    },
    "references": [
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 1,
        "cited_text": "ESPnet: end-to-end speech processing toolkit system/pytorch ver.   2.5.1   2.7.1   2.8.0   2.9.1   ubuntu/python3.10/pip ubuntu/python3.12/pip ubuntu/python3.10/conda debian12/python3.10/conda windows/python3.10/pip macos/python3.10/pip macos/python3.10/conda Docs | Example (ESPnet2) | Docker | Notebook ESPnet is an end-to-end speech processing toolkit covering end-to-end speech recognition, text-to-speech, speech translation, speech enhancement, speaker diarization, spoken language understanding, and so on. ESPnet uses pytorch as a deep learning engine and also follows Kaldi style data processing, feature extraction/format, and recipes to provide a complete setup for various speech processing experiments."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 2,
        "cited_text": "ASR: Automatic Speech Recognition State-of-the-art performance in several ASR benchmarks (comparable/superior to hybrid DNN/HMM and CTC) Hybrid CTC/attention based end-to-end ASR Fast/accurate training with CTC/attention multitask training CTC/attention joint decoding to boost monotonic alignment decoding Encoder: VGG-like CNN + BiRNN (LSTM/GRU), sub-sampling BiRNN (LSTM/GRU), Transformer, Conformer, Branchformer , or E-Branchformer Decoder: RNN (LSTM/GRU), Transformer, or S4 Attention: Flash Attention , Dot product, location-aware attention, variants of multi-head Incorporate RNNLM/LSTMLM/TransformerLM/N-gram trained only with text data Batch GPU decoding Data augmentation"
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 3,
        "cited_text": "WeNet Roadmap | Docs | Papers | Runtime | Pretrained Models | HuggingFace | Ask WeNet Guru We share Net together. Highlights Production first and production ready : The core design principle, WeNet provides full stack production solutions for speech recognition. Accurate : WeNet achieves SOTA results on a lot of public speech datasets. Light weight : WeNet is easy to install, easy to use, well designed, and well documented. Install Install python package pip install git+https://github.com/wenet-e2e/wenet.git"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 4,
        "cited_text": "Limitations Only non-streaming inference mode is supported currently The decoding stage 12 in  asr.sh  automatically runs the rtf & latency calculation if  \"asr_inference_tool == \"espnet2.bin.asr_inference\" ; other inference tools like k2 & maskctc are still left to do Transducer ASR Important : If you encounter any issue related to  warp-transducer , please open an issue in our forked repo . ESPnet2 supports models trained with the (RNN-)Tranducer loss, aka Transducer models. Currently, two versions of these models exist within ESPnet2: one under  asr  and the other under  asr_transducer . The first one is designed as a supplement of CTC-Attention ASR models while the second is designed independently and purely for the Transducer task. For that, we rely on  ESPnetASRTransducerModel  instead of  ESPnetASRModel  and a new task called  ASRTransducerTask  is used in place of  ASRTask ."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 5,
        "cited_text": "The architecture is composed of three modules: encoder, decoder and joint network. Each module has one (or three) config(s) with various parameters in order to configure the internal parts. The following sections describe the mandatory and optional parameters for each module. Encoder For the encoder, we propose a unique encoder type encapsulating the following blocks: Branchformer, Conformer, Conv 1D and E-Branchformer. It is similar to the custom encoder in ESPnet1, meaning we don't need to set the parameter  encoder: [type]  here. Instead, the encoder architecture is defined by three configurations passed to  encoder_conf :"
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 6,
        "cited_text": "Transducer based end-to-end ASR Architecture: Custom encoder supporting RNNs, Conformer, Branchformer (w/ variants), 1D Conv / TDNN. Decoder w/ parameters shared across blocks supporting RNN, stateless w/ 1D Conv, MEGA , and RWKV . Pre-encoder: VGG2L or Conv2D available. Search algorithms: Greedy search constrained to one emission by timestep. Default beam search algorithm [Graves, 2012] without prefix search. Alignment-Length Synchronous decoding [Saon et al., 2020] . Time Synchronous Decoding [Saon et al., 2020] . N-step Constrained beam search modified from [Kim et al., 2020] . modified Adaptive Expansion Search based on [Kim et al., 2021] and NSC."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 7,
        "cited_text": "Features: Unified interface for offline and streaming speech recognition. Multi-task learning with various auxiliary losses: Encoder: CTC, auxiliary Transducer and symmetric KL divergence. Decoder: cross-entropy w/ label smoothing. Transfer learning with an acoustic model and/or language model. Training with FastEmit regularization method [Yu et al., 2021] . Please refer to the tutorial page for complete documentation. CTC segmentation Non-autoregressive model based on Mask-CTC ASR examples for supporting endangered language documentation (Please refer to egs/puebla_nahuatl and egs/yoloxochitl_mixtec for details) Wav2Vec2.0 pre-trained model as Encoder, imported from FairSeq ."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 8,
        "cited_text": "Whisper [Blog] [Paper] [Model card] [Colab example] Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification. Approach A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 9,
        "cited_text": "Internally, the  transcribe()  method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window. Below is an example usage of  whisper.detect_language()  and  whisper.decode()  which provide lower-level access to the model. import   whisper   model   =   whisper . load_model ( \"turbo\" )  # load audio and pad/trim it to fit 30 seconds   audio   =   whisper . load_audio ( \"audio.mp3\" )  audio   =   whisper . pad_or_trim ( audio )  # make log-Mel spectrogram and move to the same device as the model   mel   =   whisper . log_mel_spectrogram ( audio ,  n_mels = model . dims . n_mels ). to ( model . device )  # detect the spoken language   _ ,  probs   =   model . detect_language ( mel )  print ( f\"Detected language:  { max ( probs ,  key = probs . get ) } \" )  # decode the audio   options   =   whisper . DecodingOptions ()  result   =   whisper . decode ( model ,  mel ,  options )  # print the recognized text   print ( result . text )"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 10,
        "cited_text": "Python API Shell API ESPnet2 About 18 min ESPnet2 Main changes from ESPnet1 Chainer free Discarding Chainer completely. The development of Chainer is stopped at v7: https://chainer.org/announcement/2019/12/05/released-v7.html Kaldi free It's not mandatory to compile Kaldi. If you find some recipes requiring Kaldi mandatory, please report it. It should be dealt with as a bug in ESPnet2. We still support the features made by Kaldi optionally. We still follow Kaldi style. i.e. depending on  utils/  of Kaldi."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 11,
        "cited_text": "On the fly feature extraction & text preprocessing for training You don't need to create the feature file before training, but just input wave data directly. We support both raw wave input and extracted features. The preprocessing for text, tokenization to characters, or sentencepieces, can be also applied during training. Support self-supervised learning representations from s3prl Discarding the JSON format describing the training corpus. Why do we discard the JSON format? Because a dict object generated from a large JSON file requires much memory and it also takes much time to parse such a large JSON file."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 12,
        "cited_text": "Support distributed data-parallel training (Not enough tested) Single node multi GPU training with  DistributedDataParallel  is also supported. Understanding ESPnet2 Recipes Recipe is a set of scripts that enables users to fully reproduce the experiment, such as data preparation, model definition, training, evaluation, and model release. You can find the new recipes in  egs2  (shorthand for Examples for ESPnet2 ): espnet2/ # Python modules of espnet2   espnet3/ # Python modules of espnet3   egs2/ # espnet2 recipes"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 13,
        "cited_text": "Keep in mind that all scripts should be ran at the level of  egs2/<dataset>/<task> . # Doesn't work   cd  egs2/an4/   ./asr1/run.sh   ./asr1/scripts/ <some-script>.sh   # Doesn't work   cd  egs2/an4/asr1/local/   ./data.sh   # Works   cd  egs2/an4/asr1   ./run.sh   ./scripts/ <some-script>.sh Directory structure of each recipe egs2/an4/asr1/    - conf/ # Configuration files for training, inference, etc.    - scripts/ # Bash utilities of espnet2    - pyscripts/ # Python utilities of espnet2    - steps/ # From Kaldi utilities    - utils/ # From Kaldi utilities    - db.sh # The directory path of each corpora    - path.sh # Setup script for environment variables    - cmd.sh # Configuration for your backend of job scheduler    - run.sh # Entry point    - asr.sh # Invoked by run.sh"
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 14,
        "cited_text": "Skip to content Navigation Menu Sign in Appearance settings AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start"
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 15,
        "cited_text": "Clone the repo git clone https://github.com/wenet-e2e/wenet.git Install Conda: please see https://docs.conda.io/en/latest/miniconda.html Create Conda env: conda create -n wenet python=3.10 conda activate wenet conda install conda-forge::sox Install CUDA: please follow this link , It's recommended to install CUDA 12.1 Install torch and torchaudio, It's recomended to use 2.2.2+cu121: pip install torch==2.2.2+cu121 torchaudio==2.2.2+cu121 -f https://download.pytorch.org/whl/torch_stable.html For Ascend NPU users: Install CANN: please follow this link to install CANN toolkit and kernels."
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 16,
        "cited_text": "Build for deployment Optionally, if you want to use x86 runtime or language model(LM), you have to build the runtime as follows. Otherwise, you can just ignore this step. #  runtime build requires cmake 3.14 or above   cd  runtime/libtorch mkdir build  &&   cd  build  &&  cmake -DGRAPH_TOOLS=ON ..  &&  cmake --build  . Please see doc for building runtime on more platforms and OS. Discussion & Communication You can directly discuss on Github Issues . For Chinese users, you can also scan the QR code on the left to follow our official account of WeNet. We created a WeChat group for better discussion and quicker response. Please scan the personal QR code on the right, and the guy is responsible for inviting you to the chat group."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 17,
        "cited_text": "Streaming ASR ESPnet supports streaming Transformer/Conformer ASR with blockwise synchronous beam search. For more details, please refer to the paper . Training To achieve streaming ASR, please employ blockwise Transformer/Conformer encoder in the configuration file. Taking  blockwise Transformer  as an example: The  encoder  name can be  contextual_block_transformer  or  contextual_block_conformer . encoder:  contextual_block_transformer   encoder_conf:    block_size:  40  # block size for block processing    hop_size:  16  # hop size for block processing    look_ahead:  16  # look-ahead size for block processing    init_average:  true  # whether to use average input as initial context    ctx_pos_enc:  true  # whether to use positional encoding for the context vectors"
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 18,
        "cited_text": "Self-supervised learning representations as features, using upstream models in S3PRL in frontend. Set  frontend  to  s3prl Select any upstream model by setting the  frontend_conf  to the corresponding name. Transfer Learning : easy usage and transfers from models previously trained by your group or models from ESPnet Hugging Face repository . Documentation and toy example runnable on colab . Streaming Transformer/Conformer ASR with blockwise synchronous beam search. Restricted Self-Attention based on Longformer as an encoder for long sequences OpenAI Whisper model, robust ASR based on large-scale, weakly-supervised multitask learning"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 19,
        "cited_text": "Streaming To enable streaming capabilities for Transducer models, we support dynamic chunk training and chunk-by-chunk decoding as proposed in [Zhang et al., 2021] . Our implementation is based on the version proposed in Icefall , based itself on the original WeNet one. For a complete explanation on the different procedure and parameters, we refer the reader to the corresponding paper. Training To train a streaming model, the parameter  dynamic_chunk_training  should be set to  True  in  main_conf  (See section Encoder . From here, the user has access to two parameters in order to control the dynamic chunk selection ( short_chunk_threshold  and  short_chunk_size ) and another one to control the left context in the causal convolution and the attention module ( num_left_chunks )."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 20,
        "cited_text": "General usage To enable Transducer model training or decoding in your experiments, the following option should be supplied to  asr.sh  in your  run.sh : asr.sh  --asr_task  asr_transducer  [...] For Transducer loss computation during training, we rely by default on a fork of  warp-transducer . The installation procedure is described here . Note: We made available FastEmit regularization [Yu et al., 2021] during loss computation. To enable it,  fastemit_lambda  need to be set in  model_conf : model_conf :    fastemit_lambda :  Regularization parameter for FastEmit. (float, default = 0.0)"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 21,
        "cited_text": "Optionnaly, we also support training with the Pruned RNN-T loss [Kuang et al. 2022] made available in the k2 toolkit. To use it, the parameter  use_k2_pruned_loss  should be set to  True  in  model_conf . From here, the loss computation can be controlled by setting the following parameters through  k2_pruned_loss_args  in  model_conf : model_conf :    use_k2_pruned_loss :  True    k2_pruned_loss_args :    prune_range :  How many tokens by frame are used compute the pruned loss. (int, default = 5)    simple_loss_scaling :  The weight to scale the simple loss after warm-up. (float, default = 0.5)    lm_scale :  The scale factor to smooth the LM part. (float, default = 0.0)    am_scale :  The scale factor to smooth the AM part. (float, default = 0.0)    loss_type :  Define the type of path to take for loss computation, either 'regular', 'smoothed' or 'constrained'. (str, default = \"regular\")"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 22,
        "cited_text": "Inference Various decoding algorithms are also available for Transducer by setting  search_type  parameter in your decode config: Beam search algorithm without prefix search [Graves, 2012] . ( search_type: default ) Time Synchronous Decoding [Saon et al., 2020] . ( search_type: tsd ) Alignment-Length Synchronous Decoding [Saon et al., 2020] . ( search_type: alsd ) modified Adaptive Expansion Search, based on [Kim et al., 2021] and [Boyer et al., 2021] . ( search_type: maes ) The algorithms share two parameters to control the beam size ( beam_size ) and the partial/final hypotheses normalization ( score_norm ). In addition, three algorithms have specific parameters:"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 23,
        "cited_text": "Time-synchronous decoding search_type :  tsd   max_sym_exp  :  Number of maximum symbol expansions at each time step. (int > 1, default = 3) Alignement-Length Synchronous decoding search_type :  alsd   u_max :  Maximum expected target sequence length. (int, default = 50) Modified Adaptive Expansion Search search_type :  maes   nstep :  Number of maximum expansion steps at each time step (int, default = 2)   expansion_gamma :  Number of additional candidates in expanded hypotheses selection. (int, default = 2)   expansion_beta :  Allowed logp difference for prune-by-value method. (float, default = 2.3)"
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 24,
        "cited_text": "Size   Parameters   English-only model   Multilingual model   Required VRAM   Relative speed   tiny   39 M   tiny.en   tiny   ~1 GB   ~10x   base   74 M   base.en   base   ~1 GB   ~7x   small   244 M   small.en   small   ~2 GB   ~4x   medium   769 M   medium.en   medium   ~5 GB   ~2x   large   1550 M   N/A   large   ~10 GB   1x   turbo   809 M   N/A   turbo   ~6 GB   ~8x The  .en  models for English-only applications tend to perform better, especially for the  tiny.en  and  base.en  models. We observed that the difference becomes less significant for the  small.en  and  medium.en  models. Additionally, the  turbo  model is an optimized version of  large-v3  that offers faster transcription speed with a minimal degradation in accuracy."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 25,
        "cited_text": "Supports over 125 languages Use AI to caption videos How to use Speech-to-Text 02:26 mins Features Advanced speech AI Speech-to-Text can utilize Chirp 3 , Google Cloud’s foundation model for speech trained on millions of hours of audio data and billions of text sentences. This contrasts with traditional speech recognition techniques that focus on large amounts of language-specific supervised data. These techniques give users improved recognition and transcription for more spoken languages and accents."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 26,
        "cited_text": "Support for 85+ languages and variants Build for a global user base with extensive language support . Transcribe short, long, and even streaming audio data. Speech-to-Text also offers users more accurate and globe-spanning deployments for transcription with Chirp 3 , the next generation of universal speech models. Chirp 3: Transcription was built using self-supervised training on millions of hours of audio and 28 billion sentences of text spanning 100+ languages. Transcribe short, long, or streaming audio  View guide Streaming speech recognition"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 27,
        "cited_text": "Skip to main content Contact us AWS Marketplace Sign in to console Create account Amazon Transcribe Overview Use Cases Features Pricing Getting Started More Products Artificial Intelligence Amazon Transcribe Amazon Transcribe Automatically convert speech to text and gain insights Get started with Amazon Transcribe Try Free Demo Why Amazon Transcribe? Amazon Transcribe is a fully managed, automatic speech recognition (ASR) service that makes it easy for developers to add speech to text capabilities to their applications. It is powered by a next-generation, multi-billion parameter speech foundation model that delivers high accuracy transcriptions for streaming and recorded speech. Thousands of customers across industries use it to automate manual tasks, unlock rich insights, increase accessibility, and boost discoverability of audio and video content."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 28,
        "cited_text": "ASR results expand We list the character error rate (CER) and word error rate (WER) of major ASR tasks. Task   CER (%)   WER (%)   Pre-trained model   Aishell dev/test   4.6/5.1   N/A link ESPnet2 Aishell dev/test   4.1/4.4   N/A link Common Voice dev/test   1.7/1.8   2.2/2.3 link CSJ eval1/eval2/eval3   5.7/3.8/4.2   N/A link ESPnet2 CSJ eval1/eval2/eval3   4.5/3.3/3.6   N/A link ESPnet2 GigaSpeech dev/test   N/A   10.6/10.5 link HKUST dev   23.5   N/A link ESPnet2 HKUST dev   21.2   N/A link Librispeech dev_clean/dev_other/test_clean/test_other   N/A   1.9/4.9/2.1/4.9 link ESPnet2 Librispeech dev_clean/dev_other/test_clean/test_other   0.6/1.5/0.6/1.4   1.7/3.4/1.8/3.6 link Switchboard (eval2000) callhm/swbd   N/A   14.0/6.8 link ESPnet2 Switchboard (eval2000) callhm/swbd   N/A   13.4/7.3 link TEDLIUM2 dev/test   N/A   8.6/7.2 link ESPnet2 TEDLIUM2 dev/test   N/A   7.3/7.1 link TEDLIUM3 dev/test   N/A   9.6/7.6 link WSJ dev93/eval92   3.2/2.1   7.0/4.7   N/A ESPnet2 WSJ dev93/eval92   1.1/0.8   2.8/1.8 link Note that the performance of the CSJ, HKUST, and Librispeech tasks was significantly improved by using the wide network (#units = 1024) and large subword units if necessary reported by RWTH ."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 29,
        "cited_text": "Command-line usage The following command will transcribe speech in audio files, using the  turbo  model: whisper audio.flac audio.mp3 audio.wav --model turbo The default setting (which selects the  turbo  model) works well for transcribing English. However, the  turbo  model is not trained for translation tasks . If you need to translate non-English speech into English , use one of the multilingual models ( tiny ,  base ,  small ,  medium ,  large ) instead of  turbo . For example, to transcribe an audio file containing non-English speech, you can specify the language:"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 30,
        "cited_text": "Use key features across 100+ languages that make it easy to use and customize. These include features such as automatic punctuation, custom vocabulary, automatic language identification, speaker diarization, word-level confidence scores, and vocabulary filters.   Access advanced features such as redaction of sensitive information, automatic language detection, content moderation, and custom language models. Extract key business insights from customer calls, video files, clinical conversations and more.   Automatically extracts insights such as sentiment, call categories, call characteristics, and generative AI-powered summaries with Amazon Transcribe Call Analytics."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 31,
        "cited_text": "Tutorial Series 2019 Tutorial at Interspeech Material 2021 Tutorial at CMU Online video Material 2022 Tutorial at CMU Usage of ESPnet (ASR as an example) Online video Material Add new models/tasks to ESPnet Online video Material Key Features Kaldi-style complete recipe Support numbers of  ASR  recipes (WSJ, Switchboard, CHiME-4/5, Librispeech, TED, CSJ, AMI, HKUST, Voxforge, REVERB, Gigaspeech, etc.) Support numbers of  TTS  recipes in a similar manner to the ASR recipe (LJSpeech, LibriTTS, M-AILABS, etc.) Support numbers of  ST  recipes (Fisher-CallHome Spanish, Libri-trans, IWSLT'18, How2, Must-C, Mboshi-French, etc.) Support numbers of  MT  recipes (IWSLT'14, IWSLT'16, the above ST recipes etc.) Support numbers of  SLU  recipes (CATSLU-MAPS, FSC, Grabo, IEMOCAP, JDCINAL, SNIPS, SLURP, SWBD-DA, etc.) Support numbers of  SE/SS  recipes (DNS-IS2020, LibriMix, SMS-WSJ, VCTK-noisyreverb, WHAM!, WHAMR!, WSJ-2mix, etc.) Support voice conversion recipe (VCC2020 baseline) Support speaker diarization recipe (mini_librispeech, librimix) Support singing voice synthesis recipe (ofuton_p_utagoe_db, opencpop, m4singer, etc.)"
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 32,
        "cited_text": "More examples Please use the 🙌 Show and tell category in Discussions for sharing more example usages of Whisper and third-party extensions such as web demos, integrations with other tools, ports for different platforms, etc. License Whisper's code and model weights are released under the MIT License. See LICENSE for further details. About Robust Speech Recognition via Large-Scale Weak Supervision Resources Readme License MIT license Uh oh! There was an error while loading. Please reload this page ."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 33,
        "cited_text": "Speech-to-Text V2 API V2 offers data residency for multi and single region deployments of Chirp 3. V2 does include audit logging and support for customer managed encryption keys. $0.016 per min View pricing details for Speech-to-Text. How Speech-to-Text pricing works Speech-to-Text pricing is based on the API version, channels, batch methods, and any additional Google Cloud service costs like storage. Speech-to-Text V2 API Service and capability V2 offers data residency for multi and single region deployments of Chirp 3. V2 does include audit logging and support for customer managed encryption keys."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 34,
        "cited_text": "About End-to-End Speech Processing Toolkit espnet.github.io/espnet/ Topics text-to-speech deep-learning chainer end-to-end machine-translation pytorch speech-synthesis speech-recognition kaldi voice-conversion speaker-diarization speech-separation speech-enhancement spoken-language-understanding speech-translation singing-voice-synthesis Resources Readme License Apache-2.0 license Contributing Contributing Uh oh! There was an error while loading. Please reload this page . Activity Custom properties Stars"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 35,
        "cited_text": "Realize the value of your speech data today with Amazon Transcribe. Benefits of Amazon Transcribe Easily embed voice technologies in your applications with Amazon Transcribe, a fully managed, multi-billion parameter speech foundation model that instantly converts real-time or recorded speech into text. It is trained on millions of hours of audio data across a variety of languages. Amazon Transcribe accounts for different accents, noisy environments, and acoustic conditions that enables you to produce more accurate outputs."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 36,
        "cited_text": "# ../../../utils/calculate_rtf.py --log-dir exp/byan/librispeech_asr_train_asr_conformer_raw_bpe_batch_bins30000000_accum_grad3_optim_conflr0.001_sp/decode_as   r_lm_lm_train_lm_transformer2_en_bpe5000_valid.loss.ave_asr_model_valid.acc.ave/test_clean/logdir  --log-name  asr_inference  --input-shift  0.0625  --start-times-   marker  \"speech length\"  --end-times-marker  \"best hypo\"   Total  audio  duration:  19452.481  [sec]   Total  decoding  time:  137762.231  [sec]   RTF:  7.082   Latency:  52581.004  [ms/sentence]"
      },
      {
        "source_id": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
        "citation_number": 37,
        "cited_text": "Punctuation Restoration Input Text   Output Text  今天的天气真不错啊你下午有空吗我想约你一起去吃饭   今天的天气真不错啊！你下午有空吗？我想约你一起去吃饭。 Features Via the easy-to-use, efficient, flexible and scalable implementation, our vision is to empower both industrial application and academic research, including training, inference & testing modules, and deployment process. To be more specific, this toolkit features at: 📦 Ease of Use : low barriers to install, CLI , Server , and Streaming Server is available to quick-start your journey. 🏆 Align to the State-of-the-Art : we provide high-speed and ultra-lightweight models, and also cutting-edge technology. 🏆 Streaming ASR and TTS System : we provide production ready streaming asr and streaming tts system. 💯 Rule-based Chinese frontend : our frontend contains Text Normalization and Grapheme-to-Phoneme (G2P, including Polyphone and Tone Sandhi). Moreover, we use self-defined linguistic rules to adapt Chinese context."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 38,
        "cited_text": "Supports multiple tasks in a single model Multilingual speech recognition Any-to-any speech translation Language identification Utterance-level timestamp prediction (segmentation) DNN Framework Flexible network architecture thanks to Chainer and PyTorch Flexible front-end processing thanks to kaldiio and HDF5 support Tensorboard-based monitoring DeepSpeed -based large-scale training ESPnet2 See ESPnet2 . Independent from Kaldi/Chainer, unlike ESPnet1 On-the-fly feature extraction and text processing when training Supporting DistributedDataParallel and DaraParallel both Supporting multiple nodes training and integrated with Slurm or MPI Supporting Sharded Training provided by fairscale A template recipe that can be applied to all corpora Possible to train any size of corpus without CPU memory error ESPnet Model Zoo Integrated with wandb"
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "语音识别技术（ASR）从传统的 HMM 架构演进到现代端到端神经网络，不仅在算法上实现了突破，也在工业级部署和开源生态中积累了大量实践。根据提供的来源，以下是相关的真实应用场景、部署方案、性能数据及最佳实践的详细列举。\n\n### 1. 真实应用场景与案例\n语音识别技术已广泛渗透到各行各业，核心场景包括：\n*   **客服与呼叫中心分析**：自动提取业务洞察、分析客户情绪、通话自动分类以及生成基于生成式 AI 的摘要 [1-3]。\n*   **媒体与内容创作**：为点播和直播内容自动生成字幕，提升可访问性和搜索可见性 [2, 4]。\n*   **医疗临床记录**：Amazon Transcribe Medical 等服务支持将医生与患者的临床对话自动录入电子健康档案（EHR），并能识别专业医学术语 [5]。\n*   **实时语音助手与机器人**：构建具备自然语音交互能力的生成式 AI 应用，支持多语言实时对话 [6, 7]。\n*   **游戏与社交安全**：利用毒性检测（Toxicity Detection）识别并分类游戏场景或社交媒体中的不良语音，维护社区环境 [5]。\n\n### 2. 工业级部署方案\n针对不同的业务需求，目前存在三种主流部署模式：\n*   **全托管云 API 方案**：如 **Amazon Transcribe**、**Azure Speech** 和 **Google Cloud STT**，提供数十亿参数的基础模型，支持 100+ 语种，具备高扩展性和安全性 [6, 8-10]。\n*   **私有化部署与边缘计算**：\n    *   **Google Cloud Speech-to-Text On-Prem**：支持在私有数据中心运行谷歌的语音识别技术 [11]。\n    *   **容器化部署**：Azure 支持通过容器在云端或边缘侧部署 AI 模型，确保数据就近处理 [6]。\n*   **生产导向的开源框架 (Production-First)**：\n    *   **WeNet**：核心原则是“生产优先”，提供从训练到 C++ 运行时的全栈生产解决方案 [12, 13]。\n    *   **PaddleSpeech**：提供一键式 CLI、Server 和流式 Server 部署工具，支持 Linux、Windows 和 Mac 跨平台 [14, 15]。\n\n### 3. 开源项目实战案例\n*   **ESPnet2 实验复现**：通过 **Recipe（配方）** 系统，开发者可以完全复现 Aishell、Librispeech 和 WSJ 等经典数据集的实验流程 [16-18]。\n*   **PaddleSpeech 创意应用**：\n    *   **PaddleBoBo**：利用 TTS 生成虚拟人语音 [19]。\n    *   **VTuberTalk**：利用 ASR 和 TTS 从视频中克隆声音，辅助虚拟主播创作 [19, 20]。\n*   **OpenAI Whisper 实践**：支持多任务（识别、翻译、语种鉴定）的轻量化调用，通过简单的 Python API 即可处理大规模音频文件 [21, 22]。\n\n### 4. 性能基准数据\n| 指标分类 | 模型/项目 | 性能数据 |\n| :--- | :--- | :--- |\n| **准确率 (CER/WER)** | **ESPnet2 (Aishell)** | CER: 4.1% (dev) / 4.4% (test) [23] |\n| | **ESPnet2 (Librispeech)** | WER: 1.7% (clean) / 3.4% (other) [23] |\n| **推理效率 (RTF)** | **ESPnet2 (Conformer)** | RTF 约为 7.082 (Librispeech 非流式单核解码) [24] |\n| | **Whisper Turbo** | 推理速度约为 Large-v3 的 **8 倍** [25, 26] |\n| **经济成本** | **主流云厂商 (AWS/Azure/Google)** | 标准定价约为 **$0.016 / 分钟** [27, 28] |\n\n### 5. 开发者最佳实践与常见踩坑经验\n\n#### 最佳实践\n*   **使用 \"On-the-fly\" 特征提取**：在 ESPnet2 中，训练时直接输入原始波形（raw wave），由系统实时提取特征和预处理文本，无需预先生成庞大的特征文件 [29, 30]。\n*   **流式识别配置**：若需实现流式输出，应在编码器配置中使用 **Contextual Block Transformer/Conformer**，并设置合理的块大小（block size）和跳跃步长（hop size） [31]。\n*   **多任务学习增强**：在训练端到端模型时，引入 **CTC** 作为辅助损失函数，可以加速收敛并显着提升解码时的单调对齐能力 [32, 33]。\n\n#### 常见踩坑经验\n*   **多 GPU 训练时的 Batch Size**：在 ESPnet2 中，总的 batch size 不会随 GPU 数量增加而自动调整。如果增加 GPU 数量，**必须手动调大 batch size** 以维持训练效率 [34]。\n*   **内存优化**：避免使用大型 JSON 文件描述训练集，因为解析大 JSON 会消耗极高内存。建议采用 ESPnet2 的新数据输入系统 [29]。\n*   **Whisper 模型选择**：**Turbo 模型虽然速度快，但并未针对翻译任务进行训练**。如果需要将非英语翻译为英语，必须选择 small、medium 或 large 等多语言版本模型 [35]。\n*   **硬件依赖问题**：在国产硬件（如昇腾 NPU）上部署 WeNet 时，需要安装特定的 CANN 插件和 `torch-npu` 依赖 [36, 37]。\n*   **流式推理模式确认**：开发者成功训练模型后，若解码报错（如 'NoneType' 错误），通常是因为在推理阶段忘记指定 `--use_streaming true` [38]。",
    "conversation_id": "1d51604e-53db-4bef-b2ff-c6744401b23d",
    "sources_used": [
      "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "bb9688e5-48a8-411c-88d7-3b417e991873",
      "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
      "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "a4f4f597-f7ca-4372-9555-9af1d705c695"
    ],
    "citations": {
      "1": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "2": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "3": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "4": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "5": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "6": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "7": "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
      "8": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "9": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "10": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "11": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "12": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "13": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "14": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "15": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "16": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "17": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "18": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "19": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "20": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "21": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "22": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "23": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "24": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "25": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "26": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "27": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "28": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "29": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "30": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "31": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "32": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "33": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "34": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "35": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "36": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "37": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "38": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1"
    },
    "references": [
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 1,
        "cited_text": "Use key features across 100+ languages that make it easy to use and customize. These include features such as automatic punctuation, custom vocabulary, automatic language identification, speaker diarization, word-level confidence scores, and vocabulary filters.   Access advanced features such as redaction of sensitive information, automatic language detection, content moderation, and custom language models. Extract key business insights from customer calls, video files, clinical conversations and more.   Automatically extracts insights such as sentiment, call categories, call characteristics, and generative AI-powered summaries with Amazon Transcribe Call Analytics."
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 2,
        "cited_text": "Convert speech content into text and apply generative AI to automate routine tasks and unlock insights trapped in your audio and video content. Use Cases Use Amazon Transcribe Call Analytics and Amazon Connect Contact Lens to improve customer experience and boost agent productivity with real-time or post-call conversation insights and automate tasks like note-taking, call classification, and generative AI-powered summaries, With Amazon Transcribe, you can subtitle on-demand and broadcast content to increase accessibility and improve customer experience. Boost productivity by accurately capturing meetings and conversations that matter to you."
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 3,
        "cited_text": "USE CASES Develop multimodal generative AI apps with speech models Build voice-enabled agents Use foundation models along with customized audio-in and audio-out models to power agents with voice. Learn more Transcribe speech to text Transcribe call center or meeting conversations. Go global with audio captioning in more than 100 languages. Learn more Convert text to speech Build bots that speak naturally. Differentiate your brand with customized, realistic voices and speaking styles. Learn more Use post-call analytics"
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 4,
        "cited_text": "Analyze audio or video call recordings to gain deep insights using foundation models in Azure Content Understanding in Foundry Tools. Learn more Transcribe audio with OpenAI Whisper Transform your call centers using the latest OpenAI Whisper model in Azure Speech or Azure OpenAI in Foundry Models. Read the blog Build custom voices Build natural-sounding voices with custom neural voice. Learn more Build your avatars Bring your brand to life using prebuilt or custom avatars with natural-sounding voices. Learn more Enable multilingual communication"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 5,
        "cited_text": "Use Transcribe Toxicity Detection for gaming, social media and other peer to peer conversations. Detect and categorize toxic audio and foster a safe and inclusive online environment. Medical doctors and practitioners can use Amazon Transcribe Medical and AWS Healthscribe to quickly and efficiently document clinical conversations into electronic health record (EHR) systems for analysis. The service is HIPAA- eligible and trained to understand medical terminology. How to get started Demo Check out our differentiating features"
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 6,
        "cited_text": "Other Microsoft Rewards Free downloads & security Education Gift cards Licensing Unlocked stories View Sitemap No results Voice Live API is now integrated with the new Foundry Agent Service Read the blog Azure Speech in Foundry Tools Energize your apps and agents with prebuilt, customizable, multilingual speech AI models. Get started with Azure Create with Microsoft Foundry Get started with Azure Get started with Azure OVERVIEW Discover the latest Azure Speech capabilities Build voice-enabled, multilingual generative AI apps with fast transcriptions and natural-sounding voices. Explore Azure Speech Enable AI agents with end-to-end speech, including customized transcription, voice, and avatars. Explore Voice Live API Enable real-time, multi-language speech-to-speech translation and speech-to-text transcription of audio streams. Learn more Run AI models wherever your data resides. Deploy your apps in the cloud or at the edge with containers. Develop with containers"
      },
      {
        "source_id": "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
        "citation_number": 7,
        "cited_text": "Contact Us Log In Sign Up Free Virtual Event: Multilingual Strategies for Real-Time Voice Agents Watch Now The Voice AI Economy is   Powered by Deepgram Build with the most accurate and cost-effective real-time APIs for speech-to-text, text-to-speech, and voice agents. Available in real-time and batch, cloud and self-hosted. Sign Up Free Playground Speech to Text Text to Speech Voice Agent Audio Intelligence Your transcriptions will show here. Copy Download A single, unified  Voice Agent API Instead of stitching together separate components, Deepgram unifies speech-to-text, text-to-speech, and LLM orchestration into a single API, reducing complexity, latency, and cost."
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 8,
        "cited_text": "Skip to main content Contact us AWS Marketplace Sign in to console Create account Amazon Transcribe Overview Use Cases Features Pricing Getting Started More Products Artificial Intelligence Amazon Transcribe Amazon Transcribe Automatically convert speech to text and gain insights Get started with Amazon Transcribe Try Free Demo Why Amazon Transcribe? Amazon Transcribe is a fully managed, automatic speech recognition (ASR) service that makes it easy for developers to add speech to text capabilities to their applications. It is powered by a next-generation, multi-billion parameter speech foundation model that delivers high accuracy transcriptions for streaming and recorded speech. Thousands of customers across industries use it to automate manual tasks, unlock rich insights, increase accessibility, and boost discoverability of audio and video content."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 9,
        "cited_text": "Supports over 125 languages Use AI to caption videos How to use Speech-to-Text 02:26 mins Features Advanced speech AI Speech-to-Text can utilize Chirp 3 , Google Cloud’s foundation model for speech trained on millions of hours of audio data and billions of text sentences. This contrasts with traditional speech recognition techniques that focus on large amounts of language-specific supervised data. These techniques give users improved recognition and transcription for more spoken languages and accents."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 10,
        "cited_text": "Support for 85+ languages and variants Build for a global user base with extensive language support . Transcribe short, long, and even streaming audio data. Speech-to-Text also offers users more accurate and globe-spanning deployments for transcription with Chirp 3 , the next generation of universal speech models. Chirp 3: Transcription was built using self-supervised training on millions of hours of audio and 28 billion sentences of text spanning 100+ languages. Transcribe short, long, or streaming audio  View guide Streaming speech recognition"
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 11,
        "cited_text": "Speech adaptation Customize speech recognition to transcribe domain-specific terms and rare words by providing hints and boost your transcription accuracy of specific words or phrases. Automatically convert spoken numbers into addresses, years, currencies, and more using classes . Speech-to-Text On-Prem Have full control over your infrastructure and protected speech data while leveraging Google’s speech recognition technology on-premises , right in your own private data centers. Contact sales to get started."
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 12,
        "cited_text": "Skip to content Navigation Menu Sign in Appearance settings AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start"
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 13,
        "cited_text": "WeNet Roadmap | Docs | Papers | Runtime | Pretrained Models | HuggingFace | Ask WeNet Guru We share Net together. Highlights Production first and production ready : The core design principle, WeNet provides full stack production solutions for speech recognition. Accurate : WeNet achieves SOTA results on a lot of public speech datasets. Light weight : WeNet is easy to install, easy to use, well designed, and well documented. Install Install python package pip install git+https://github.com/wenet-e2e/wenet.git"
      },
      {
        "source_id": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
        "citation_number": 14,
        "cited_text": "Punctuation Restoration Input Text   Output Text  今天的天气真不错啊你下午有空吗我想约你一起去吃饭   今天的天气真不错啊！你下午有空吗？我想约你一起去吃饭。 Features Via the easy-to-use, efficient, flexible and scalable implementation, our vision is to empower both industrial application and academic research, including training, inference & testing modules, and deployment process. To be more specific, this toolkit features at: 📦 Ease of Use : low barriers to install, CLI , Server , and Streaming Server is available to quick-start your journey. 🏆 Align to the State-of-the-Art : we provide high-speed and ultra-lightweight models, and also cutting-edge technology. 🏆 Streaming ASR and TTS System : we provide production ready streaming asr and streaming tts system. 💯 Rule-based Chinese frontend : our frontend contains Text Normalization and Grapheme-to-Phoneme (G2P, including Polyphone and Tone Sandhi). Moreover, we use self-defined linguistic rules to adapt Chinese context."
      },
      {
        "source_id": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
        "citation_number": 15,
        "cited_text": "Community Scan the QR code below with your Wechat, you can access to official technical exchange group and get the bonus ( more than 20GB learning materials, such as papers, codes and videos ) and the live link of the lessons. Look forward to your participation. Installation We strongly recommend our users to install PaddleSpeech in Linux with python>=3.8 . Dependency Introduction gcc >= 4.8.5 paddlepaddle python >= 3.8 OS support: Linux(recommend), Windows, Mac OSX PaddleSpeech depends on paddlepaddle. For installation, please refer to the official website of paddlepaddle and choose according to your own machine. Here is an example of the cpu version."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 16,
        "cited_text": "Support distributed data-parallel training (Not enough tested) Single node multi GPU training with  DistributedDataParallel  is also supported. Understanding ESPnet2 Recipes Recipe is a set of scripts that enables users to fully reproduce the experiment, such as data preparation, model definition, training, evaluation, and model release. You can find the new recipes in  egs2  (shorthand for Examples for ESPnet2 ): espnet2/ # Python modules of espnet2   espnet3/ # Python modules of espnet3   egs2/ # espnet2 recipes"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 17,
        "cited_text": "The  egs2  recipes are always structured by  egs2/<dataset>/<task> . So, for example, the user should be able to fully reproduce the experiment by the following: # Dataset: an4, Task: ASR   cd egs2/an4/asr1/   # Run the full experiment   ./run.sh Note that the usage of recipes is almost the same as that of ESPnet1. Now, let's go step-by-step on how exactly the recipes work. Change directory to the base directory # e.g.   cd  egs2/an4/asr1/ an4  is a tiny corpus and can be freely obtained, so it might be suitable for this tutorial. You can perform any other recipes as the same way. e.g.  wsj ,  librispeech , and etc."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 18,
        "cited_text": "Tutorial Series 2019 Tutorial at Interspeech Material 2021 Tutorial at CMU Online video Material 2022 Tutorial at CMU Usage of ESPnet (ASR as an example) Online video Material Add new models/tasks to ESPnet Online video Material Key Features Kaldi-style complete recipe Support numbers of  ASR  recipes (WSJ, Switchboard, CHiME-4/5, Librispeech, TED, CSJ, AMI, HKUST, Voxforge, REVERB, Gigaspeech, etc.) Support numbers of  TTS  recipes in a similar manner to the ASR recipe (LJSpeech, LibriTTS, M-AILABS, etc.) Support numbers of  ST  recipes (Fisher-CallHome Spanish, Libri-trans, IWSLT'18, How2, Must-C, Mboshi-French, etc.) Support numbers of  MT  recipes (IWSLT'14, IWSLT'16, the above ST recipes etc.) Support numbers of  SLU  recipes (CATSLU-MAPS, FSC, Grabo, IEMOCAP, JDCINAL, SNIPS, SLURP, SWBD-DA, etc.) Support numbers of  SE/SS  recipes (DNS-IS2020, LibriMix, SMS-WSJ, VCTK-noisyreverb, WHAM!, WHAMR!, WSJ-2mix, etc.) Support voice conversion recipe (VCC2020 baseline) Support speaker diarization recipe (mini_librispeech, librimix) Support singing voice synthesis recipe (ofuton_p_utagoe_db, opencpop, m4singer, etc.)"
      },
      {
        "source_id": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
        "citation_number": 19,
        "cited_text": "The Text-to-Speech module is originally called Parakeet , and now merged with this repository. If you are interested in academic research about this task, please see TTS research overview . Also, this document is a good guideline for the pipeline components. ⭐ Examples PaddleBoBo : Use PaddleSpeech TTS to generate virtual human voice. PaddleSpeech Demo Video VTuberTalk : Use PaddleSpeech TTS and ASR to clone voice from videos. Citation To cite PaddleSpeech for research, please use the following format. @inproceedings{zhang2022paddlespeech, title = {PaddleSpeech: An Easy-to-Use All-in-One Speech Toolkit}, author = {Hui Zhang, Tian Yuan, Junkun Chen, Xintong Li, Renjie Zheng, Yuxin Huang, Xiaojie Chen, Enlei Gong, Zeyu Chen, Xiaoguang Hu, dianhai yu, Yanjun Ma, Liang Huang}, booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Demonstrations}, year = {2022}, publisher = {Association for Computational Linguistics}, } @InProceedings{pmlr-v162-bai22d, title = {{A}$^3${T}: Alignment-Aware Acoustic and Text Pretraining for Speech Synthesis and Editing}, author = {Bai, He and Zheng, Renjie and Chen, Junkun and Ma, Mingbo and Li, Xintong and Huang, Liang}, booktitle = {Proceedings of the 39th International Conference on Machine Learning}, pages = {1399--1411}, year = {2022}, volume = {162}, series = {Proceedings of Machine Learning Research}, month = {17--23 Jul}, publisher = {PMLR}, pdf = {https://proceedings.mlr.press/v162/bai22d/bai22d.pdf}, url = {https://proceedings.mlr.press/v162/bai22d.html}, } @inproceedings{zheng2021fused, title={Fused acoustic and text encoding for multimodal bilingual pretraining and speech translation}, author={Zheng, Renjie and Chen, Junkun and Ma, Mingbo and Huang, Liang}, booktitle={International Conference on Machine Learning}, pages={12736--12746}, year={2021}, organization={PMLR} }"
      },
      {
        "source_id": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
        "citation_number": 20,
        "cited_text": "Contribute to PaddleSpeech You are warmly welcome to submit questions in discussions and bug reports in issues ! Also, we highly appreciate if you are willing to contribute to this project! Contributors Acknowledgement Many thanks to HighCWu for adding VITS-aishell3 and VITS-VC examples. Many thanks to david-95 for fixing multi-punctuation bug、contributing to multiple program and data, and adding SSML for TTS Chinese Text Frontend. Many thanks to BarryKCL for improving TTS Chinses Frontend based on G2PW . Many thanks to yeyupiaoling / PPASR / PaddlePaddle-DeepSpeech / VoiceprintRecognition-PaddlePaddle / AudioClassification-PaddlePaddle for years of attention, constructive advice and great help. Many thanks to mymagicpower for the Java implementation of ASR upon short and long audio files. Many thanks to JiehangXie / PaddleBoBo for developing Virtual Uploader(VUP)/Virtual YouTuber(VTuber) with PaddleSpeech TTS function. Many thanks to 745165806 / PaddleSpeechTask for contributing Punctuation Restoration model. Many thanks to kslz for supplementary Chinese documents. Many thanks to awmmmm for contributing fastspeech2 aishell3 conformer pretrained model. Many thanks to phecda-xu / PaddleDubbing for developing a dubbing tool with GUI based on PaddleSpeech TTS model. Many thanks to jerryuhoo / VTuberTalk for developing a GUI tool based on PaddleSpeech TTS and code for making datasets from videos based on PaddleSpeech ASR. Many thanks to vpegasus / xuesebot for developing a rasa chatbot,which is able to speak and listen thanks to PaddleSpeech. Many thanks to chenkui164 / FastASR for the C++ inference implementation of PaddleSpeech ASR. Many thanks to heyudage / VoiceTyping for the real-time voice typing tool implementation of PaddleSpeech ASR streaming services. Many thanks to EscaticZheng / ps3.9wheel-install for the python3.9 prebuilt wheel for PaddleSpeech installation in Windows without Visual Studio. Besides, PaddleSpeech depends on a lot of open source repositories. See references for more information. Many thanks to chinobing / FastAPI-PaddleSpeech-Audio-To-Text for converting audio to text based on FastAPI and PaddleSpeech. Many thanks to MistEO / Pallas-Bot for QQ bot based on PaddleSpeech TTS."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 21,
        "cited_text": "Whisper [Blog] [Paper] [Model card] [Colab example] Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification. Approach A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 22,
        "cited_text": "whisper japanese.wav --language Japanese To translate speech into English, use: whisper japanese.wav --model medium --language Japanese --task translate Note: The  turbo  model will return the original language even if  --task translate  is specified. Use  medium  or  large  for the best translation results. Run the following to view all available options: whisper --help See tokenizer.py for the list of all available languages. Python usage Transcription can also be performed within Python: import   whisper   model   =   whisper . load_model ( \"turbo\" )  result   =   model . transcribe ( \"audio.mp3\" )  print ( result [ \"text\" ])"
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 23,
        "cited_text": "ASR results expand We list the character error rate (CER) and word error rate (WER) of major ASR tasks. Task   CER (%)   WER (%)   Pre-trained model   Aishell dev/test   4.6/5.1   N/A link ESPnet2 Aishell dev/test   4.1/4.4   N/A link Common Voice dev/test   1.7/1.8   2.2/2.3 link CSJ eval1/eval2/eval3   5.7/3.8/4.2   N/A link ESPnet2 CSJ eval1/eval2/eval3   4.5/3.3/3.6   N/A link ESPnet2 GigaSpeech dev/test   N/A   10.6/10.5 link HKUST dev   23.5   N/A link ESPnet2 HKUST dev   21.2   N/A link Librispeech dev_clean/dev_other/test_clean/test_other   N/A   1.9/4.9/2.1/4.9 link ESPnet2 Librispeech dev_clean/dev_other/test_clean/test_other   0.6/1.5/0.6/1.4   1.7/3.4/1.8/3.6 link Switchboard (eval2000) callhm/swbd   N/A   14.0/6.8 link ESPnet2 Switchboard (eval2000) callhm/swbd   N/A   13.4/7.3 link TEDLIUM2 dev/test   N/A   8.6/7.2 link ESPnet2 TEDLIUM2 dev/test   N/A   7.3/7.1 link TEDLIUM3 dev/test   N/A   9.6/7.6 link WSJ dev93/eval92   3.2/2.1   7.0/4.7   N/A ESPnet2 WSJ dev93/eval92   1.1/0.8   2.8/1.8 link Note that the performance of the CSJ, HKUST, and Librispeech tasks was significantly improved by using the wide network (#units = 1024) and large subword units if necessary reported by RWTH ."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 24,
        "cited_text": "# ../../../utils/calculate_rtf.py --log-dir exp/byan/librispeech_asr_train_asr_conformer_raw_bpe_batch_bins30000000_accum_grad3_optim_conflr0.001_sp/decode_as   r_lm_lm_train_lm_transformer2_en_bpe5000_valid.loss.ave_asr_model_valid.acc.ave/test_clean/logdir  --log-name  asr_inference  --input-shift  0.0625  --start-times-   marker  \"speech length\"  --end-times-marker  \"best hypo\"   Total  audio  duration:  19452.481  [sec]   Total  decoding  time:  137762.231  [sec]   RTF:  7.082   Latency:  52581.004  [ms/sentence]"
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 25,
        "cited_text": "pip install setuptools-rust Available models and languages There are six model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and inference speed relative to the large model. The relative speeds below are measured by transcribing English speech on a A100, and the real-world speed may vary significantly depending on many factors including the language, the speaking speed, and the available hardware."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 26,
        "cited_text": "Size   Parameters   English-only model   Multilingual model   Required VRAM   Relative speed   tiny   39 M   tiny.en   tiny   ~1 GB   ~10x   base   74 M   base.en   base   ~1 GB   ~7x   small   244 M   small.en   small   ~2 GB   ~4x   medium   769 M   medium.en   medium   ~5 GB   ~2x   large   1550 M   N/A   large   ~10 GB   1x   turbo   809 M   N/A   turbo   ~6 GB   ~8x The  .en  models for English-only applications tend to perform better, especially for the  tiny.en  and  base.en  models. We observed that the difference becomes less significant for the  small.en  and  medium.en  models. Additionally, the  turbo  model is an optimized version of  large-v3  that offers faster transcription speed with a minimal degradation in accuracy."
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 27,
        "cited_text": "Flexible pricing to meet your needs Pay for only what you use—no upfront costs. Azure Speech pay-as-you-go pricing is based on: The number of hours of audio you transcribe or translate for speech to text and speech translation. The number of characters you convert to audio for text to speech. The number of transactions for speaker recognition. Azure Speech pricing RELATED PRODUCTS Azure products work better together Build comprehensive solutions using Azure Speech and other Azure AI products."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 28,
        "cited_text": "Speech-to-Text V2 API V2 offers data residency for multi and single region deployments of Chirp 3. V2 does include audit logging and support for customer managed encryption keys. $0.016 per min View pricing details for Speech-to-Text. How Speech-to-Text pricing works Speech-to-Text pricing is based on the API version, channels, batch methods, and any additional Google Cloud service costs like storage. Speech-to-Text V2 API Service and capability V2 offers data residency for multi and single region deployments of Chirp 3. V2 does include audit logging and support for customer managed encryption keys."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 29,
        "cited_text": "On the fly feature extraction & text preprocessing for training You don't need to create the feature file before training, but just input wave data directly. We support both raw wave input and extracted features. The preprocessing for text, tokenization to characters, or sentencepieces, can be also applied during training. Support self-supervised learning representations from s3prl Discarding the JSON format describing the training corpus. Why do we discard the JSON format? Because a dict object generated from a large JSON file requires much memory and it also takes much time to parse such a large JSON file."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 30,
        "cited_text": "Supports multiple tasks in a single model Multilingual speech recognition Any-to-any speech translation Language identification Utterance-level timestamp prediction (segmentation) DNN Framework Flexible network architecture thanks to Chainer and PyTorch Flexible front-end processing thanks to kaldiio and HDF5 support Tensorboard-based monitoring DeepSpeed -based large-scale training ESPnet2 See ESPnet2 . Independent from Kaldi/Chainer, unlike ESPnet1 On-the-fly feature extraction and text processing when training Supporting DistributedDataParallel and DaraParallel both Supporting multiple nodes training and integrated with Slurm or MPI Supporting Sharded Training provided by fairscale A template recipe that can be applied to all corpora Possible to train any size of corpus without CPU memory error ESPnet Model Zoo Integrated with wandb"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 31,
        "cited_text": "Streaming ASR ESPnet supports streaming Transformer/Conformer ASR with blockwise synchronous beam search. For more details, please refer to the paper . Training To achieve streaming ASR, please employ blockwise Transformer/Conformer encoder in the configuration file. Taking  blockwise Transformer  as an example: The  encoder  name can be  contextual_block_transformer  or  contextual_block_conformer . encoder:  contextual_block_transformer   encoder_conf:    block_size:  40  # block size for block processing    hop_size:  16  # hop size for block processing    look_ahead:  16  # look-ahead size for block processing    init_average:  true  # whether to use average input as initial context    ctx_pos_enc:  true  # whether to use positional encoding for the context vectors"
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 32,
        "cited_text": "ASR: Automatic Speech Recognition State-of-the-art performance in several ASR benchmarks (comparable/superior to hybrid DNN/HMM and CTC) Hybrid CTC/attention based end-to-end ASR Fast/accurate training with CTC/attention multitask training CTC/attention joint decoding to boost monotonic alignment decoding Encoder: VGG-like CNN + BiRNN (LSTM/GRU), sub-sampling BiRNN (LSTM/GRU), Transformer, Conformer, Branchformer , or E-Branchformer Decoder: RNN (LSTM/GRU), Transformer, or S4 Attention: Flash Attention , Dot product, location-aware attention, variants of multi-head Incorporate RNNLM/LSTMLM/TransformerLM/N-gram trained only with text data Batch GPU decoding Data augmentation"
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 33,
        "cited_text": "Features: Unified interface for offline and streaming speech recognition. Multi-task learning with various auxiliary losses: Encoder: CTC, auxiliary Transducer and symmetric KL divergence. Decoder: cross-entropy w/ label smoothing. Transfer learning with an acoustic model and/or language model. Training with FastEmit regularization method [Yu et al., 2021] . Please refer to the tutorial page for complete documentation. CTC segmentation Non-autoregressive model based on Mask-CTC ASR examples for supporting endangered language documentation (Please refer to egs/puebla_nahuatl and egs/yoloxochitl_mixtec for details) Wav2Vec2.0 pre-trained model as Encoder, imported from FairSeq ."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 34,
        "cited_text": "Distributed training Using Job scheduling system Various tips Relationship between mini-batch size and number of GPUs The behavior of batch size in ESPnet2 during multi-GPU training is different from that in ESPnet1. In ESPnet2, the total batch size is not changed regardless of the number of GPUs. Therefore, you need to manually increase the batch size if you increase the number of GPUs. Please refer to this doc for more information. Use specified experiment directory for evaluation If you already have trained a model, you may wonder how to give it to run.sh when you'll evaluate it later. By default the directory name is determined according to given options,  asr_args ,  lm_args , or etc. You can overwrite it by  --asr_exp  and  --lm_exp ."
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 35,
        "cited_text": "Command-line usage The following command will transcribe speech in audio files, using the  turbo  model: whisper audio.flac audio.mp3 audio.wav --model turbo The default setting (which selects the  turbo  model) works well for transcribing English. However, the  turbo  model is not trained for translation tasks . If you need to translate non-English speech into English , use one of the multilingual models ( tiny ,  base ,  small ,  medium ,  large ) instead of  turbo . For example, to transcribe an audio file containing non-English speech, you can specify the language:"
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 36,
        "cited_text": "Clone the repo git clone https://github.com/wenet-e2e/wenet.git Install Conda: please see https://docs.conda.io/en/latest/miniconda.html Create Conda env: conda create -n wenet python=3.10 conda activate wenet conda install conda-forge::sox Install CUDA: please follow this link , It's recommended to install CUDA 12.1 Install torch and torchaudio, It's recomended to use 2.2.2+cu121: pip install torch==2.2.2+cu121 torchaudio==2.2.2+cu121 -f https://download.pytorch.org/whl/torch_stable.html For Ascend NPU users: Install CANN: please follow this link to install CANN toolkit and kernels."
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 37,
        "cited_text": "Install WeNet with torch-npu dependencies: pip install -e .[torch-npu] Related version control table: Requirement   Minimum   Recommend   CANN   8.0.RC2.alpha003   latest   torch   2.1.0   2.2.0   torch-npu   2.1.0   2.2.0   torchaudio   2.1.0   2.2.0   deepspeed   0.13.2   latest Install other python packages pip install -r requirements.txt pre-commit install  #  for clean and tidy code Frequently Asked Questions (FAQs) #  If you encounter sox compatibility issues  RuntimeError: set_buffer_size requires sox extension which is not available.  #  ubuntu  sudo apt-get install sox libsox-dev  #  centos  sudo yum install sox sox-devel  #  conda env  conda install conda-forge::sox"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 38,
        "cited_text": "Decoding To enable online decoding, the argument  --use_streaming true  should be added to  run.sh . ./run.sh  --stage  12  --use_streaming  true FAQ Issue about  'NoneType' object has no attribute 'max'  during training: Please make sure you employ  forward_train  function during traininig, check more details here . I successfully trained the model, but encountered the above issue during decoding: You may forget to specify  --use_streaming true  to select streaming inference. Real-Time-Factor and Latency"
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "在「语音识别（ASR）全景」演进中，2025-2026 年的技术突破标志着该领域已从“特定任务模型”全面跨入**“语音基础大模型（Speech Foundation Models）”**与**“智能体原生（Agent-native）”**的新时代。\n\n以下是基于来源的最新研究突破、技术趋势及未来方向的深度解析：\n\n### 一、 2025-2026 年核心技术趋势与重要成果\n\n这一时期的核心特征是**模型参数规模的爆发式增长**与**多任务能力的极度集成**。\n\n1.  **语音基础模型（Speech Foundation Models）的统治**：\n    *   **Amazon Transcribe** 推出了新一代**数十亿参数**的语音基础模型，通过数百万小时的多语言音频数据训练，极大提升了对不同口音、噪声环境的鲁棒性 [1, 2]。\n    *   **Google Chirp 3** 作为通用语音模型，利用自监督学习（SSL）在 100 多种语言上进行了 280 亿文本句和数百万小时音频的预处理，实现了跨语言的通用识别能力 [3, 4]。\n2.  **Whisper 系列及其开源复现（OWSM）**：\n    *   **OpenAI Whisper Turbo**（2025 年发布）成为性能平衡的标杆，其推理速度达到 Large-v3 的 **8 倍**，且准确率下降极小 [5]。\n    *   **ESPnet 的 OWSM 项目**：致力于利用公开数据复现 Whisper 风格的大规模弱监督多任务训练，支持识别、翻译、时间戳预测和语种鉴定 [6, 7]。\n3.  **从“工具”向“智能体（Agent）”转型**：\n    *   **Azure AI Speech 品牌重塑**：2025-2026 年间，Azure 将其语音服务整合进 **Foundry Tools**，强调其作为构建**智能体 AI（Agentic AI）**核心工具的地位，支持端到端语音交互、数字人（Avatar）和实时翻译 [8, 9]。\n    *   **Deepgram Voice Agent API**：推出了统一的语音智能体 API，将 STT、TTS 和 **LLM 编排（Orchestration）**集成在单一接口中，大幅降低了交互延迟 [10, 11]。\n\n### 二、 重要论文与技术演进路径\n\n根据开源框架（如 ESPnet2, PaddleSpeech）的最新引用与更新，技术路线呈现以下特征：\n\n*   **架构演进**：主流编码器已从 Transformer 进化到 **Branchformer**、**E-Branchformer** 和 **Squeezeformer** [12-14]。这些架构在捕捉局部卷积特征与全局上下文注意力之间取得了更好的平衡。\n*   **训练范式**：**自监督学习表示（SSLR）**如 HuBERT 和 Wav2Vec2.0 已成为前端特征的标准配置，能够取代传统频谱特征以提升识别精度 [15-17]。\n*   **推理优化**：为了支持流式应用，**分块注意力机制（Blockwise/Contextual Block）**和改进的搜索算法（如 **MAES** - 改进的自适应扩展搜索）被广泛采用 [18, 19]。\n\n### 三、 未解决的挑战\n\n尽管基础模型表现强劲，但领域内仍存在以下痛点：\n\n1.  **语境切换（Code-switching）**：虽然 PaddleSpeech 等框架在 2025 年新增了在线中英混读模型，但在极其频繁的语种切换场景下，识别精度仍有提升空间 [13]。\n2.  **特定任务的局限性**：例如 **Whisper Turbo 模型虽然速度极快，但并未针对翻译任务进行优化**。若需进行非英语到英语的翻译，仍需回退到 Large 版本模型 [20]。\n3.  **专业领域知识缺失**：在医疗（如 Amazon Transcribe Medical）等行业，虽然已有针对性训练，但对于极冷门的专业术语和复杂背景噪声下的远场识别（Far-field ASR）仍具有挑战性 [21, 22]。\n4.  **计算资源门槛**：数十亿参数模型的微调（Fine-tuning）和推理对 VRAM（显存）要求极高，例如 Whisper Large-v3 仍需约 10GB 显存，这限制了在低功耗设备上的部署 [5, 23]。\n\n### 四、 未来可能的突破点\n\n1.  **多模态生成式 AI（Multimodal GenAI）**：将语音直接作为大语言模型（LLM）的一种输入模态，而非先转文字再处理，从而保留语音中的情感、语调等元信息 [24, 25]。\n2.  **完全去模块化**：目前的系统虽号称端到端，但仍保留了特征提取、编码、解码等逻辑。未来的突破可能在于完全融合的神经网络，直接实现从原始音频到复杂业务逻辑（如直接生成会议行动项摘要）的映射 [26, 27]。\n3.  **生产侧的“极致性能”优化**：WeNet 提出的 **\"Production First\"** 理念将持续推动模型在昇腾 NPU 等国产化硬件以及移动端的原生高性能运行 [28, 29]。\n4.  **无监督与弱监督学习的极致利用**：随着 OWSM 等项目的成熟，利用海量互联网无标注数据训练出的“超级语音模型”将使小语种识别不再依赖昂贵的人工标注数据 [6, 30]。\n\n**总结**：2025-2026 年是语音识别告别“单独模块化”的一年。**基础模型化**、**智能体化**以及**软硬一体的国产化部署**是当前最显著的发展航标。",
    "conversation_id": "1d51604e-53db-4bef-b2ff-c6744401b23d",
    "sources_used": [
      "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "bb9688e5-48a8-411c-88d7-3b417e991873",
      "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
      "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015"
    ],
    "citations": {
      "1": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "2": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "3": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "4": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "5": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "6": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "7": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "8": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "9": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "10": "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
      "11": "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
      "12": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "13": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
      "14": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "15": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "16": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "17": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
      "18": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "19": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
      "20": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "21": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "22": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
      "23": "a4f4f597-f7ca-4372-9555-9af1d705c695",
      "24": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "25": "bb9688e5-48a8-411c-88d7-3b417e991873",
      "26": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "27": "601f1e60-2bee-42f3-b92f-eb99db388f57",
      "28": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "29": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
      "30": "3736b005-7a2c-452c-9caa-1183bb8c7a99"
    },
    "references": [
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 1,
        "cited_text": "Skip to main content Contact us AWS Marketplace Sign in to console Create account Amazon Transcribe Overview Use Cases Features Pricing Getting Started More Products Artificial Intelligence Amazon Transcribe Amazon Transcribe Automatically convert speech to text and gain insights Get started with Amazon Transcribe Try Free Demo Why Amazon Transcribe? Amazon Transcribe is a fully managed, automatic speech recognition (ASR) service that makes it easy for developers to add speech to text capabilities to their applications. It is powered by a next-generation, multi-billion parameter speech foundation model that delivers high accuracy transcriptions for streaming and recorded speech. Thousands of customers across industries use it to automate manual tasks, unlock rich insights, increase accessibility, and boost discoverability of audio and video content."
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 2,
        "cited_text": "Realize the value of your speech data today with Amazon Transcribe. Benefits of Amazon Transcribe Easily embed voice technologies in your applications with Amazon Transcribe, a fully managed, multi-billion parameter speech foundation model that instantly converts real-time or recorded speech into text. It is trained on millions of hours of audio data across a variety of languages. Amazon Transcribe accounts for different accents, noisy environments, and acoustic conditions that enables you to produce more accurate outputs."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 3,
        "cited_text": "Supports over 125 languages Use AI to caption videos How to use Speech-to-Text 02:26 mins Features Advanced speech AI Speech-to-Text can utilize Chirp 3 , Google Cloud’s foundation model for speech trained on millions of hours of audio data and billions of text sentences. This contrasts with traditional speech recognition techniques that focus on large amounts of language-specific supervised data. These techniques give users improved recognition and transcription for more spoken languages and accents."
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 4,
        "cited_text": "Support for 85+ languages and variants Build for a global user base with extensive language support . Transcribe short, long, and even streaming audio data. Speech-to-Text also offers users more accurate and globe-spanning deployments for transcription with Chirp 3 , the next generation of universal speech models. Chirp 3: Transcription was built using self-supervised training on millions of hours of audio and 28 billion sentences of text spanning 100+ languages. Transcribe short, long, or streaming audio  View guide Streaming speech recognition"
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 5,
        "cited_text": "Size   Parameters   English-only model   Multilingual model   Required VRAM   Relative speed   tiny   39 M   tiny.en   tiny   ~1 GB   ~10x   base   74 M   base.en   base   ~1 GB   ~7x   small   244 M   small.en   small   ~2 GB   ~4x   medium   769 M   medium.en   medium   ~5 GB   ~2x   large   1550 M   N/A   large   ~10 GB   1x   turbo   809 M   N/A   turbo   ~6 GB   ~8x The  .en  models for English-only applications tend to perform better, especially for the  tiny.en  and  base.en  models. We observed that the difference becomes less significant for the  small.en  and  medium.en  models. Additionally, the  turbo  model is an optimized version of  large-v3  that offers faster transcription speed with a minimal degradation in accuracy."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 6,
        "cited_text": "Jp / En / Kr / Zh Tight integration with neural vocoders (the same as TTS) SSL: Self-supervised Learning Support HuBERT Pre-training: Example recipe: egs2/LibriSpeech/ssl1 UASR: Unsupervised ASR (EURO: ESPnet Unsupervised Recognition - Open-source) Architecture wav2vec-U (with different self-supervised models) wav2vec-U 2.0 (in progress) Support PrefixBeamSearch and K2-based WFST decoding S2T: Speech-to-text with Whisper-style multilingual multitask models Reproduces Whisper-style training from scratch using public data: OWSM"
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 7,
        "cited_text": "oktitle={ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, pages={1--5}, year={2023}, organization={IEEE} } @inproceedings{peng2023reproducing, title={Reproducing {W}hisper-style training using an open-source toolkit and publicly available data}, author={Peng, Yifan and Tian, Jinchuan and Yan, Brian and Berrebbi, Dan and Chang, Xuankai and Li, Xinjian and Shi, Jiatong and Arora, Siddhant and Chen, William and Sharma, Roshan and others}, booktitle={2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)}, pages={1--8}, year={2023}, organization={IEEE} } @inproceedings{sharma2023espnet, title={ESPnet-{SUMM}: Introducing a novel large dataset, toolkit, and a cross-corpora evaluation of speech summarization systems}, author={Sharma, Roshan and Chen, William and Kano, Takatomo and Sharma, Ruchira and Arora, Siddhant and Watanabe, Shinji and Ogawa, Atsunori and Delcroix, Marc and Singh, Rita and Raj, Bhiksha}, booktitle={202"
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 8,
        "cited_text": "Other Microsoft Rewards Free downloads & security Education Gift cards Licensing Unlocked stories View Sitemap No results Voice Live API is now integrated with the new Foundry Agent Service Read the blog Azure Speech in Foundry Tools Energize your apps and agents with prebuilt, customizable, multilingual speech AI models. Get started with Azure Create with Microsoft Foundry Get started with Azure Get started with Azure OVERVIEW Discover the latest Azure Speech capabilities Build voice-enabled, multilingual generative AI apps with fast transcriptions and natural-sounding voices. Explore Azure Speech Enable AI agents with end-to-end speech, including customized transcription, voice, and avatars. Explore Voice Live API Enable real-time, multi-language speech-to-speech translation and speech-to-text transcription of audio streams. Learn more Run AI models wherever your data resides. Deploy your apps in the cloud or at the edge with containers. Develop with containers"
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 9,
        "cited_text": "Azure Speech is part of Foundry Tools (formerly Azure AI Services) and provides APIs for speech-to-text, text-to-speech, translation, and speaker recognition. It was previously known as Azure AI Speech. Yes, we’re rebranding many of our former Azure AI Services as Foundry Tools. This shift reflects a broader platform unification under Foundry, and signals that these services are now positioned as core tools for building agentic AI applications. \n  Azure Speech in Foundry Tools still offers the same powerful capabilities—like speech recognition, text-to-speech, and translation—but is now part of a cohesive toolkit designed for developers building intelligent agents."
      },
      {
        "source_id": "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
        "citation_number": 10,
        "cited_text": "Contact Us Log In Sign Up Free Virtual Event: Multilingual Strategies for Real-Time Voice Agents Watch Now The Voice AI Economy is   Powered by Deepgram Build with the most accurate and cost-effective real-time APIs for speech-to-text, text-to-speech, and voice agents. Available in real-time and batch, cloud and self-hosted. Sign Up Free Playground Speech to Text Text to Speech Voice Agent Audio Intelligence Your transcriptions will show here. Copy Download A single, unified  Voice Agent API Instead of stitching together separate components, Deepgram unifies speech-to-text, text-to-speech, and LLM orchestration into a single API, reducing complexity, latency, and cost."
      },
      {
        "source_id": "1f880f6f-b602-45ca-a4ea-88f66cc535f9",
        "citation_number": 11,
        "cited_text": "Your customer or end user speaking naturally. Partner-provided transport layer that bridges stream audio into Deepgram's APIs and plays back TTS audio to the end user, including Telephony partners (via PSTN/SIP) Conversational speech recognition that detects end-of-turn and interruptions, and streams transcripts in real-time. Coordinates context, memory, and AI reasoning. Context: Maintains conversation history and system settings. System Updates: Adjusts role or behavior. Prompt Updates: Refines instructions in real time. Response Injections: Adds guidance or context. Function Calling: Executes actions or fetches data. LLM (via API): Connects to language models for response generation."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 12,
        "cited_text": "The architecture is composed of three modules: encoder, decoder and joint network. Each module has one (or three) config(s) with various parameters in order to configure the internal parts. The following sections describe the mandatory and optional parameters for each module. Encoder For the encoder, we propose a unique encoder type encapsulating the following blocks: Branchformer, Conformer, Conv 1D and E-Branchformer. It is similar to the custom encoder in ESPnet1, meaning we don't need to set the parameter  encoder: [type]  here. Instead, the encoder architecture is defined by three configurations passed to  encoder_conf :"
      },
      {
        "source_id": "aebf9cb7-1f9a-4d0c-9e58-21dbf5ac7281",
        "citation_number": 13,
        "cited_text": "Recent Update 🎉 2025.09.01: Add Whisper large v3 and turbo model . 🤗 2025.08.11: Add code-switch online model and server demo . 👑 2023.05.31: Add WavLM ASR-en , WavLM fine-tuning for ASR on LibriSpeech. 🎉 2023.05.18: Add Squeezeformer , Squeezeformer training for ASR on Aishell. 👑 2023.05.04: Add HuBERT ASR-en , HuBERT fine-tuning for ASR on LibriSpeech. ⚡ 2023.04.28: Fix 0-d tensor , with the upgrade of paddlepaddle==2.5, the problem of modifying 0-d tensor has been solved. 👑 2023.04.25: Add AMP for U2 conformer . 🔥 2023.04.06: Add subtitle file (.srt format) generation example . 🔥 2023.03.14: Add SVS(Singing Voice Synthesis) examples with Opencpop dataset, including DiffSinger 、 PWGAN and HiFiGAN , the effect is continuously optimized. 👑 2023.03.09: Add Wav2vec2ASR-zh . 🎉 2023.03.07: Add TTS ARM Linux C++ Demo (with C++ Chinese Text Frontend) . 🔥 2023.03.03 Add Voice Conversion StarGANv2-VC synthesize pipeline . 🎉 2023.02.16: Add Cantonese TTS . 🔥 2023.01.10: Add code-switch asr CLI and Demos . 👑 2023.01.06: Add code-switch asr tal_cs recipe . 🎉 2022.12.02: Add end-to-end Prosody Prediction pipeline (including using prosody labels in Acoustic Model). 🎉 2022.11.30: Add TTS Android Demo . 🤗 2022.11.28: PP-TTS and PP-ASR demos are available in AIStudio and official website of paddlepaddle . 👑 2022.11.18: Add Whisper CLI and Demos , support multi language recognition and translation. 🔥 2022.11.18: Add Wav2vec2 CLI and Demos , Support ASR and Feature Extraction. 🎉 2022.11.17: Add male voice for TTS . 🔥 2022.11.07: Add U2/U2++ C++ High Performance Streaming ASR Deployment . 👑 2022.11.01: Add Adversarial Loss for Chinese English mixed TTS . 🔥 2022.10.26: Add Prosody Prediction for TTS. 🎉 2022.10.21: Add SSML for TTS Chinese Text Frontend. 👑 2022.10.11: Add Wav2vec2ASR-en , wav2vec2.0 fine-tuning for ASR on LibriSpeech. 🔥 2022.09.26: Add Voice Cloning, TTS finetune, and ERNIE-SAT in PaddleSpeech Web Demo . ⚡ 2022.09.09: Add AISHELL-3 Voice Cloning example with ECAPA-TDNN speaker encoder. ⚡ 2022.08.25: Release TTS finetune example. 🔥 2022.08.22: Add ERNIE-SAT models: ERNIE-SAT-vctk 、 ERNIE-SAT-aishell3 、 ERNIE-SAT-zh_en . 🔥 2022.08.15: Add g2pW into TTS Chinese Text Frontend. 🔥 2022.08.09: Release Chinese English mixed TTS . ⚡ 2022.08.03: Add ONNXRuntime infer for TTS CLI. 🎉 2022.07.18: Release VITS: VITS-csmsc 、 VITS-aishell3 、 VITS-VC . 🎉 2022.06.22: All TTS models support ONNX format. 🍀 2022.06.17: Add PaddleSpeech Web Demo . 👑 2022.05.13: Release PP-ASR 、 PP-TTS 、 PP-VPR . 👏🏻 2022.05.06:  PaddleSpeech Streaming Server  is available for  Streaming ASR  with  Punctuation Restoration  and  Token Timestamp  and  Text-to-Speech . 👏🏻 2022.05.06:  PaddleSpeech Server  is available for  Audio Classification ,  Automatic Speech Recognition  and  Text-to-Speech ,  Speaker Verification  and  Punctuation Restoration . 👏🏻 2022.03.28:  PaddleSpeech CLI  is available for  Speaker Verification . 👏🏻 2021.12.10:  PaddleSpeech CLI  is available for  Audio Classification ,  Automatic Speech Recognition ,  Speech Translation (English to Chinese)  and  Text-to-Speech ."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 14,
        "cited_text": "ASR: Automatic Speech Recognition State-of-the-art performance in several ASR benchmarks (comparable/superior to hybrid DNN/HMM and CTC) Hybrid CTC/attention based end-to-end ASR Fast/accurate training with CTC/attention multitask training CTC/attention joint decoding to boost monotonic alignment decoding Encoder: VGG-like CNN + BiRNN (LSTM/GRU), sub-sampling BiRNN (LSTM/GRU), Transformer, Conformer, Branchformer , or E-Branchformer Decoder: RNN (LSTM/GRU), Transformer, or S4 Attention: Flash Attention , Dot product, location-aware attention, variants of multi-head Incorporate RNNLM/LSTMLM/TransformerLM/N-gram trained only with text data Batch GPU decoding Data augmentation"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 15,
        "cited_text": "The stage number differs according to the task. Please read the task-specific shell script (e.g.,  asr1/asr.sh ) to see the number to specify. The packed model can be uploaded to huggingface by setting the previously mentioned flags. Usage of Self-Supervised Learning Representations as feature ESPnet supports self-supervised learning representations (SSLR) to replace traditional spectrum features. In some cases, SSLRs can boost the performance. To use SSLRs in your task, you need to make several modifications."
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 16,
        "cited_text": "Install S3PRL by  tools/installers/install_s3prl.sh . If HuBERT / Wav2Vec is needed, fairseq should be installed by  tools/installers/install_fairseq.sh . Here's various tips for using SSLRs. To reduce the time used in  collect_stats  step, please specify  --feats_normalize uttmvn  in  run.sh  and pass it as arguments to  asr.sh  or other task-specific scripts. (Recommended) In the configuration file, specify the  frontend  and  preencoder . Taking  HuBERT  as an example: The  upstream  name can be whatever supported in S3PRL.  multilayer-feature=True  means the final representation is a weighted-sum of all layers' hidden states from SSLR model. frontend: s3prl   frontend_conf:    frontend_conf:    upstream: hubert_large_ll60k # Note: If the upstream is changed, please change the input_size in the preencoder.    download_dir: ./hub    multilayer_feature: True Here the  preencoder  is to reduce the input dimension to the encoder, to reduce the memory cost. The  input_size  depends on the upstream model, while the  output_size  can be set to any values. preencoder: linear   preencoder_conf:    input_size: 1024 # Note: If the upstream is changed, please change this value accordingly.    output_size: 80 Because the shift sizes of different  upstream  models are different, e.g.  HuBERT  and  Wav2Vec2.0  have  20ms  frameshift. Sometimes, the downsampling rate ( input_layer ) in the  encoder  configuration need to be changed. For example, using  input_layer: conv2d2  will results in a total frameshift of  40ms , which is enough for some tasks."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 17,
        "cited_text": "Self-supervised learning representations as features, using upstream models in S3PRL in frontend. Set  frontend  to  s3prl Select any upstream model by setting the  frontend_conf  to the corresponding name. Transfer Learning : easy usage and transfers from models previously trained by your group or models from ESPnet Hugging Face repository . Documentation and toy example runnable on colab . Streaming Transformer/Conformer ASR with blockwise synchronous beam search. Restricted Self-Attention based on Longformer as an encoder for long sequences OpenAI Whisper model, robust ASR based on large-scale, weakly-supervised multitask learning"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 18,
        "cited_text": "Streaming ASR ESPnet supports streaming Transformer/Conformer ASR with blockwise synchronous beam search. For more details, please refer to the paper . Training To achieve streaming ASR, please employ blockwise Transformer/Conformer encoder in the configuration file. Taking  blockwise Transformer  as an example: The  encoder  name can be  contextual_block_transformer  or  contextual_block_conformer . encoder:  contextual_block_transformer   encoder_conf:    block_size:  40  # block size for block processing    hop_size:  16  # hop size for block processing    look_ahead:  16  # look-ahead size for block processing    init_average:  true  # whether to use average input as initial context    ctx_pos_enc:  true  # whether to use positional encoding for the context vectors"
      },
      {
        "source_id": "1b32bc58-62a2-40ec-8ee3-2ab43d1e45b1",
        "citation_number": 19,
        "cited_text": "Inference Various decoding algorithms are also available for Transducer by setting  search_type  parameter in your decode config: Beam search algorithm without prefix search [Graves, 2012] . ( search_type: default ) Time Synchronous Decoding [Saon et al., 2020] . ( search_type: tsd ) Alignment-Length Synchronous Decoding [Saon et al., 2020] . ( search_type: alsd ) modified Adaptive Expansion Search, based on [Kim et al., 2021] and [Boyer et al., 2021] . ( search_type: maes ) The algorithms share two parameters to control the beam size ( beam_size ) and the partial/final hypotheses normalization ( score_norm ). In addition, three algorithms have specific parameters:"
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 20,
        "cited_text": "Command-line usage The following command will transcribe speech in audio files, using the  turbo  model: whisper audio.flac audio.mp3 audio.wav --model turbo The default setting (which selects the  turbo  model) works well for transcribing English. However, the  turbo  model is not trained for translation tasks . If you need to translate non-English speech into English , use one of the multilingual models ( tiny ,  base ,  small ,  medium ,  large ) instead of  turbo . For example, to transcribe an audio file containing non-English speech, you can specify the language:"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 21,
        "cited_text": "Use Transcribe Toxicity Detection for gaming, social media and other peer to peer conversations. Detect and categorize toxic audio and foster a safe and inclusive online environment. Medical doctors and practitioners can use Amazon Transcribe Medical and AWS Healthscribe to quickly and efficiently document clinical conversations into electronic health record (EHR) systems for analysis. The service is HIPAA- eligible and trained to understand medical terminology. How to get started Demo Check out our differentiating features"
      },
      {
        "source_id": "b8469813-5d75-4eab-8fda-7f5cc2f5a49f",
        "citation_number": 22,
        "cited_text": "Receive real-time speech recognition results as the API processes the audio input streamed from your application’s microphone or sent from a prerecorded audio file (inline or through Cloud Storage). AI-powered speech recognition and transcription Speech-to-Text uses model adaptation to improve the accuracy of frequently used words, expand the vocabulary available for transcription, and improve transcription from noisy audio. Model adaptation lets users customize Speech-to-Text to recognize specific words or phrases more frequently than other options that might otherwise be suggested. For example, you could bias Speech-to-Text towards transcribing \"weather\" over \"whether.\""
      },
      {
        "source_id": "a4f4f597-f7ca-4372-9555-9af1d705c695",
        "citation_number": 23,
        "cited_text": "pip install setuptools-rust Available models and languages There are six model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and inference speed relative to the large model. The relative speeds below are measured by transcribing English speech on a A100, and the real-world speed may vary significantly depending on many factors including the language, the speaking speed, and the available hardware."
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 24,
        "cited_text": "USE CASES Develop multimodal generative AI apps with speech models Build voice-enabled agents Use foundation models along with customized audio-in and audio-out models to power agents with voice. Learn more Transcribe speech to text Transcribe call center or meeting conversations. Go global with audio captioning in more than 100 languages. Learn more Convert text to speech Build bots that speak naturally. Differentiate your brand with customized, realistic voices and speaking styles. Learn more Use post-call analytics"
      },
      {
        "source_id": "bb9688e5-48a8-411c-88d7-3b417e991873",
        "citation_number": 25,
        "cited_text": "Azure OpenAI Incorporate multimodality and enhance apps with models that combine multiple types of data, such as text, images, video, and audio. Learn more Microsoft Foundry Get everything you need to develop generative AI applications and custom agents on one platform. Learn more Content Safety in Foundry Control Plane Deliver secure and trustworthy solutions with built-in tools that put responsible AI principles into practice. Learn more Azure Content Understanding Accelerate the transformation of multimodal data into insights. Learn more Azure Translator"
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 26,
        "cited_text": "Use key features across 100+ languages that make it easy to use and customize. These include features such as automatic punctuation, custom vocabulary, automatic language identification, speaker diarization, word-level confidence scores, and vocabulary filters.   Access advanced features such as redaction of sensitive information, automatic language detection, content moderation, and custom language models. Extract key business insights from customer calls, video files, clinical conversations and more.   Automatically extracts insights such as sentiment, call categories, call characteristics, and generative AI-powered summaries with Amazon Transcribe Call Analytics."
      },
      {
        "source_id": "601f1e60-2bee-42f3-b92f-eb99db388f57",
        "citation_number": 27,
        "cited_text": "Convert speech content into text and apply generative AI to automate routine tasks and unlock insights trapped in your audio and video content. Use Cases Use Amazon Transcribe Call Analytics and Amazon Connect Contact Lens to improve customer experience and boost agent productivity with real-time or post-call conversation insights and automate tasks like note-taking, call classification, and generative AI-powered summaries, With Amazon Transcribe, you can subtitle on-demand and broadcast content to increase accessibility and improve customer experience. Boost productivity by accurately capturing meetings and conversations that matter to you."
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 28,
        "cited_text": "WeNet Roadmap | Docs | Papers | Runtime | Pretrained Models | HuggingFace | Ask WeNet Guru We share Net together. Highlights Production first and production ready : The core design principle, WeNet provides full stack production solutions for speech recognition. Accurate : WeNet achieves SOTA results on a lot of public speech datasets. Light weight : WeNet is easy to install, easy to use, well designed, and well documented. Install Install python package pip install git+https://github.com/wenet-e2e/wenet.git"
      },
      {
        "source_id": "f99a36c6-f3a6-4c61-b0d5-c4d42f2dd015",
        "citation_number": 29,
        "cited_text": "Clone the repo git clone https://github.com/wenet-e2e/wenet.git Install Conda: please see https://docs.conda.io/en/latest/miniconda.html Create Conda env: conda create -n wenet python=3.10 conda activate wenet conda install conda-forge::sox Install CUDA: please follow this link , It's recommended to install CUDA 12.1 Install torch and torchaudio, It's recomended to use 2.2.2+cu121: pip install torch==2.2.2+cu121 torchaudio==2.2.2+cu121 -f https://download.pytorch.org/whl/torch_stable.html For Ascend NPU users: Install CANN: please follow this link to install CANN toolkit and kernels."
      },
      {
        "source_id": "3736b005-7a2c-452c-9caa-1183bb8c7a99",
        "citation_number": 30,
        "cited_text": "ang, Xuankai and Li, Huazhe and Wu, Peter and Watanabe, Shinji and Jin, Qin}, title={{Muskits}: an End-to-End Music Processing Toolkit for Singing Voice Synthesis}, year={2022}, booktitle={Proceedings of Interspeech}, pages={4277-4281}, url={https://www.isca-speech.org/archive/pdfs/interspeech_2022/shi22d_interspeech.pdf} } @inproceedings{lu22c_interspeech, author={Yen-Ju Lu and Xuankai Chang and Chenda Li and Wangyou Zhang and Samuele Cornell and Zhaoheng Ni and Yoshiki Masuyama and Brian Yan and Robin Scheibler and Zhong-Qiu Wang and Yu Tsao and Yanmin Qian and Shinji Watanabe}, title={{ESPnet-SE++: Speech Enhancement for Robust Speech Recognition, Translation, and Understanding}}, year=2022, booktitle={Proc. Interspeech 2022}, pages={5458--5462}, } @inproceedings{gao2023euro, title={{EURO: ESP}net unsupervised {ASR} open-source toolkit}, author={Gao, Dongji and Shi, Jiatong and Chuang, Shun-Po and Garcia, Leibny Paola and Lee, Hung-yi and Watanabe, Shinji and Khudanpur, Sanjeev}, bo"
      }
    ]
  }
}
