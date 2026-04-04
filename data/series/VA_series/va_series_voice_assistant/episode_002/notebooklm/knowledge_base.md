# 知识库：Whisper 深度解析：多语言 ASR 的工程实践

生成时间: 2026-04-02 09:59
查询轮数: 4

## 技术全景

{
  "value": {
    "answer": "基于提供的来源，以下是对 **Whisper** 核心技术架构与多语言 ASR 工程实践的深度解析，重点提取了技术演进、核心算法、架构模式及关键指标：\n\n### 1. 主要架构模式：Transformer Sequence-to-Sequence\nWhisper 采用标准的 **Transformer 编码器-解码器 (Encoder-Decoder)** 架构，也被称为 **Sequence-to-Sequence (序列到序列)** 模型 [1, 2]。其核心流程如下：\n*   **输入处理**：特征提取器将原始音频输入转换为 **log-Mel 谱图 (log-Mel spectrogram)** [1, 3]。Whisper 特有的处理方式是将所有音频填充或截断至 **30秒**，且不需要额外的注意力掩码 (Attention Mask)，模型能直接从信号中推断需忽略的部分 [4]。\n*   **编码器 (Encoder)**：将音频谱图特征编码为隐藏状态序列 [1, 2]。\n*   **解码器 (Decoder)**：利用**交叉注意力机制 (Cross-attention)**，结合编码器状态和先前预测的 Token，**自回归 (Autoregressively)** 地预测文本 Token [1, 2]。\n*   **深度融合 (Deep Fusion)**：解码器内部集成了语言模型的功能。相比于外部结合语言模型的“浅层融合”，这种架构支持端到端训练，性能通常更优 [2]。\n\n### 2. 技术演进路线\nWhisper 的技术演进体现了从大规模监督预训练到特定任务优化和轻量化的过程：\n*   **大规模弱监督预训练 (WSPSR)**：不同于 Wav2Vec 2.0 的无监督预训练，Whisper 在 **680,000 小时** 的大规模**标注**音频数据上直接进行监督学习，学习语音到文本的直接映射 [5-7]。\n*   **多任务联合学习**：模型被训练同时处理多种任务，包括多语言 ASR、语音翻译 (Speech Translation)、语种识别 (LID) 和语音激活检测 (VAD) [8]。\n*   **知识蒸馏 (Knowledge Distillation)**：演进出 **Distil-Whisper**。它通过复制原编码器并压缩解码器层数（仅保留2层），在 22,000 小时伪标签数据上训练，实现大幅提速 [9, 10]。\n*   **工程化推理优化**：演化出多种高性能实现，如使用 C/C++ 重新实现的 `whisper.cpp` [11]，以及利用 CTranslate2 引擎实现的 `faster-whisper` [12]。\n\n### 3. 核心算法名称\n*   **交叉熵目标函数 (Cross-entropy Objective)**：用于预训练和微调的标准分类损失函数 [13]。\n*   **字节对编码 (Byte-pair encoding, BPE)**：分词器使用的算法，预训练涵盖 96 种语言，具有广泛的词表适应性 [14, 15]。\n*   **投机解码 (Speculative Decoding)**：将 Distil-Whisper 作为辅助模型，在数学上确保输出一致的前提下，使推理速度提升 2 倍 [10, 16]。\n*   **束搜索 (Beam Search)**：解码阶段常用的搜索策略 [17, 18]。\n*   **滑动窗口缓冲推理 (Sliding window buffered inference)**：用于处理超过 30 秒的长音频转录算法 [19, 20]。\n\n### 4. 关键技术指标\n*   **训练规模**：总计 **680,000 小时** 标注数据，其中 **117,000 小时** 为多语言数据，涵盖 96 种语言 [5]。\n*   **模型规格**：提供从 **Tiny (39M 参数)** 到 **Large (1550M 参数)** 的多种尺寸，以及针对英语优化的 `.en` 版本和针对速度优化的 **Turbo (809M)** 版本 [21, 22]。\n*   **转录精度**：在 LibriSpeech 测试集上达到接近 **3% 的词错误率 (WER)**，在 TED-LIUM 上达到 **4.7% WER** [23]。\n*   **加速效果**：\n    *   **faster-whisper**：比官方实现快达 **4 倍**，且显存占用更低 [12, 24]。\n    *   **Distil-Whisper**：推理速度快 **6 倍**，参数减少 **50%**，而 WER 损失在 1% 以内 [10, 25]。\n    *   **insanely-fast-whisper**：利用 Flash Attention 2 等优化，可在 **98 秒** 内完成 150 分钟音频的转录 [26]。\n*   **资源占用**：Large 模型通常需要约 **10GB VRAM**，而 Tiny 模型仅需约 **1GB** [22, 27]。",
    "conversation_id": "ef4b3f56-d848-4548-a89c-d09edf73dd71",
    "sources_used": [
      "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "633960af-000b-4429-bbdb-11ef34edf441",
      "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "2101e08e-4d7e-47f3-aad5-d94ddc170884",
      "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "38fdb474-c0d4-4e41-8e96-dad5f4790493",
      "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "24726456-5f36-471c-8e85-d7c18566f228"
    ],
    "citations": {
      "1": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "2": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "3": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "4": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "5": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "6": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "7": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "8": "633960af-000b-4429-bbdb-11ef34edf441",
      "9": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "10": "2101e08e-4d7e-47f3-aad5-d94ddc170884",
      "11": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "12": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
      "13": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "14": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "15": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "16": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "17": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
      "18": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "19": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "20": "633960af-000b-4429-bbdb-11ef34edf441",
      "21": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "22": "633960af-000b-4429-bbdb-11ef34edf441",
      "23": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "24": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "25": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "26": "24726456-5f36-471c-8e85-d7c18566f228",
      "27": "633960af-000b-4429-bbdb-11ef34edf441"
    },
    "references": [
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 1,
        "cited_text": "Whisper is a Transformer based encoder-decoder model, also referred to as a sequence-to-sequence model. It maps a sequence of audio spectrogram features to a sequence of text tokens. First, the raw audio inputs are converted to a log-Mel spectrogram by action of the feature extractor. The Transformer encoder then encodes the spectrogram to form a sequence of encoder hidden states. Finally, the decoder autoregressively predicts text tokens, conditional on both the previous tokens and the encoder hidden states. Figure 1 summarises the Whisper model."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 2,
        "cited_text": "Figure 1: Whisper model. The architecture follows the standard Transformer-based encoder-decoder model. A log-Mel spectrogram is input to the encoder. The last encoder hidden states are input to the decoder via cross-attention mechanisms. The decoder autoregressively predicts text tokens, jointly conditional on the encoder hidden states and previously predicted tokens. Figure source: OpenAI Whisper Blog . In a sequence-to-sequence model, the encoder transforms the audio inputs into a set of hidden state representations, extracting important features from the spoken speech. The decoder plays the role of a language model, processing the hidden state representations and generating the corresponding text transcriptions. Incorporating a language model internally in the system architecture is termed deep fusion . This is in contrast to shallow fusion , where a language model is combined externally with an encoder, such as with CTC +  n n n -gram ( c.f. Internal Language Model Estimation ). With deep fusion, the entire system can be trained end-to-end with the same training data and loss function, giving greater flexibility and generally superior performance ( c.f. ESB Benchmark )."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 3,
        "cited_text": "The second operation that the Whisper feature extractor performs is converting the padded audio arrays to log-Mel spectrograms. These spectrograms are a visual representation of the frequencies of a signal, rather like a Fourier transform. An example spectrogram is shown in Figure 2. Along the  y y y -axis are the Mel channels, which correspond to particular frequency bins. Along the  x x x -axis is time. The colour of each pixel corresponds to the log-intensity of that frequency bin at a given time. The log-Mel spectrogram is the form of input expected by the Whisper model."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 4,
        "cited_text": "The Whisper feature extractor performs two operations. It first pads/truncates a batch of audio samples such that all samples have an input length of 30s. Samples shorter than 30s are padded to 30s by appending zeros to the end of the sequence (zeros in an audio signal corresponding to no signal or silence). Samples longer than 30s are truncated to 30s. Since all elements in the batch are padded/truncated to a maximum length in the input space, we don't require an attention mask when forwarding the audio inputs to the Whisper model. Whisper is unique in this regard - with most audio models, you can expect to provide an attention mask that details where sequences have been padded, and thus where they should be ignored in the self-attention mechanism. Whisper is trained to operate without an attention mask and infer directly from the speech signals where to ignore the inputs."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 5,
        "cited_text": "Table of Contents Introduction Fine-tuning Whisper in a Google Colab Prepare Environment Load Dataset Prepare Feature Extractor, Tokenizer and Data Training and Evaluation Building a Demo Closing Remarks Introduction Whisper is a pre-trained model for automatic speech recognition (ASR) published in September 2022 by the authors Alec Radford et al. from OpenAI. Unlike many of its predecessors, such as Wav2Vec 2.0 , which are pre-trained on un-labelled audio data, Whisper is pre-trained on a vast quantity of labelled audio-transcription data, 680,000 hours to be precise. This is an order of magnitude more data than the un-labelled audio data used to train Wav2Vec 2.0 (60,000 hours). What is more, 117,000 hours of this pre-training data is multilingual ASR data. This results in checkpoints that can be applied to over 96 languages, many of which are considered low-resource ."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 6,
        "cited_text": "This quantity of labelled data enables Whisper to be pre-trained directly on the supervised task of speech recognition, learning a speech-to-text mapping from the labelled audio-transcription pre-training data  1 {}^1 1 . As a consequence, Whisper requires little additional fine-tuning to yield a performant ASR model. This is in contrast to Wav2Vec 2.0, which is pre-trained on the unsupervised task of masked prediction. Here, the model is trained to learn an intermediate mapping from speech to hidden states from un-labelled audio only data. While unsupervised pre-training yields high-quality representations of speech, it does not learn a speech-to-text mapping. This mapping is only learned during fine-tuning, thus requiring more fine-tuning to yield competitive performance."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 7,
        "cited_text": "1 {}^1 1  The name Whisper follows from the acronym “WSPSR”, which stands for “Web-scale Supervised Pre-training for Speech Recognition”. Fine-tuning Whisper in a Google Colab Prepare Environment We'll employ several popular Python packages to fine-tune the Whisper model. We'll use  datasets[audio]  to download and prepare our training data, alongside  transformers  and  accelerate  to load and train our Whisper model. We'll also require the  soundfile  package to pre-process audio files,  evaluate  and  jiwer  to assess the performance of our model, and  tensorboard  to log our metrics. Finally, we'll use  gradio  to build a flashy demo of our fine-tuned model."
      },
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 8,
        "cited_text": "Whisper [Blog] [Paper] [Model card] [Colab example] Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification. Approach A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets."
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 9,
        "cited_text": "3. Approach ✍️ To distill Whisper, we copy the entire encoder module and freeze it during training. We copy only two decoder layers, which are initialised from the first and last decoder layers from Whisper. All other decoder layers from Whisper are discarded: Distil-Whisper is trained on a knowledge distillation objective. Specifically, it is trained to minimise the KL divergence between the distilled model and the Whisper model, as well as the cross-entropy loss on pseudo-labelled audio data. We train Distil-Whisper on a total of 22k hours of pseudo-labelled audio data, spanning 10 domains with over 18k speakers:"
      },
      {
        "source_id": "2101e08e-4d7e-47f3-aad5-d94ddc170884",
        "citation_number": 10,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2311.00430 Help | Advanced Search Computer Science > Computation and Language arXiv:2311.00430 (cs)   [Submitted on 1 Nov 2023] Title: Distil-Whisper: Robust Knowledge Distillation via Large-Scale Pseudo Labelling Authors: Sanchit Gandhi , Patrick von Platen , Alexander M. Rush View a PDF of the paper titled Distil-Whisper: Robust Knowledge Distillation via Large-Scale Pseudo Labelling, by Sanchit Gandhi and 2 other authors View PDF Abstract: As the size of pre-trained speech recognition models increases, running these large models in low-latency or resource-constrained environments becomes challenging. In this work, we leverage pseudo-labelling to assemble a large-scale open-source dataset which we use to distill the Whisper model into a smaller variant, called Distil-Whisper. Using a simple word error rate (WER) heuristic, we select only the highest quality pseudo-labels for training. The distilled model is 5.8 times faster with 51% fewer parameters, while performing to within 1% WER on out-of-distribution test data in a zero-shot transfer setting. Distil-Whisper maintains the robustness of the Whisper model to difficult acoustic conditions, while being less prone to hallucination errors on long-form audio. Distil-Whisper is designed to be paired with Whisper for speculative decoding, yielding a 2 times speed-up while mathematically ensuring the same outputs as the original model. To facilitate further research in this domain, we make our training code, inference code and models publicly accessible.  Comments:   30 pages, 2 figures, 25 tables   Subjects:   Computation and Language (cs.CL) ; Sound (cs.SD); Audio and Speech Processing (eess.AS)   Cite as: arXiv:2311.00430 [cs.CL]   (or arXiv:2311.00430v1 [cs.CL]  for this version) https://doi.org/10.48550/arXiv.2311.00430 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 11,
        "cited_text": "whisper.cpp Stable: v1.8.1 / Roadmap High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model: Plain C/C++ implementation without dependencies Apple Silicon first-class citizen - optimized via ARM NEON, Accelerate framework, Metal and Core ML AVX intrinsics support for x86 architectures VSX intrinsics support for POWER architectures Mixed F16 / F32 precision Integer quantization support Zero memory allocations at runtime Vulkan support Support for CPU-only inference Efficient GPU support for NVIDIA OpenVINO Support Ascend NPU Support Moore Threads GPU Support C-style API Voice Activity Detection (VAD)"
      },
      {
        "source_id": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
        "citation_number": 12,
        "cited_text": "Faster Whisper transcription with CTranslate2 faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2 , which is a fast inference engine for Transformer models. This implementation is up to 4 times faster than openai/whisper for the same accuracy while using less memory. The efficiency can be further improved with 8-bit quantization on both CPU and GPU. Benchmark Whisper For reference, here's the time and memory usage that are required to transcribe 13 minutes of audio using different implementations:"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 13,
        "cited_text": "Whisper is pre-trained and fine-tuned using the cross-entropy objective function, a standard objective function for training sequence-to-sequence systems on classification tasks. Here, the system is trained to correctly classify the target text token from a pre-defined vocabulary of text tokens. The Whisper checkpoints come in five configurations of varying model sizes. The smallest four are trained on either English-only or multilingual data. The largest checkpoints are multilingual only. All 11 of the pre-trained checkpoints are available on the Hugging Face Hub . The checkpoints are summarised in the following table with links to the models on the Hub:"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 14,
        "cited_text": "Luckily for us, the 🤗 Transformers Whisper feature extractor performs both the padding and spectrogram conversion in just one line of code! Let's go ahead and load the feature extractor from the pre-trained checkpoint to have ready for our audio data: from  transformers  import  WhisperFeatureExtractor feature_extractor = WhisperFeatureExtractor.from_pretrained( \"openai/whisper-small\" ) Load WhisperTokenizer Now let's look at how to load a Whisper tokenizer. The Whisper model outputs text tokens that indicate the index of the predicted text among the dictionary of vocabulary items. The tokenizer maps a sequence of text tokens to the actual text string (e.g. [1169, 3797, 3332] -> \"the cat sat\")."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 15,
        "cited_text": "Traditionally, when using encoder-only models for ASR, we decode using Connectionist Temporal Classification (CTC) . Here we are required to train a CTC tokenizer for each dataset we use. One of the advantages of using an encoder-decoder architecture is that we can directly leverage the tokenizer from the pre-trained model. The Whisper tokenizer is pre-trained on the transcriptions for the 96 pre-training languages. Consequently, it has an extensive byte-pair that is appropriate for almost all multilingual ASR applications. For Hindi, we can load the tokenizer and use it for fine-tuning without any further modifications. We simply have to specify the target language and the task. These arguments inform the tokenizer to prefix the language and task tokens to the start of encoded label sequences:"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 16,
        "cited_text": "Speculative Decoding Distil-Whisper can be used as an assistant model to Whisper for speculative decoding . Speculative decoding mathematically ensures the exact same outputs as Whisper are obtained while being 2 times faster. This makes it the perfect drop-in replacement for existing Whisper pipelines, since the same outputs are guaranteed. For speculative decoding, we need to load both the teacher: openai/whisper-large-v3 . As well as the assistant ( a.k.a student) distil-whisper/distil-large-v3 . Let's start by loading the teacher model and processor. We do this in much the same way we loaded the Distil-Whisper model in the previous examples:"
      },
      {
        "source_id": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
        "citation_number": 17,
        "cited_text": "Installation The module can be installed from PyPI : pip install faster-whisper   Other installation methods (click to expand) Install the master branch pip install --force-reinstall  \" faster-whisper @ https://github.com/SYSTRAN/faster-whisper/archive/refs/heads/master.tar.gz \" Install a specific commit pip install --force-reinstall  \" faster-whisper @ https://github.com/SYSTRAN/faster-whisper/archive/a4f1cc8f11433e454c3934442b5e1a4ed5e865c3.tar.gz \" Usage Faster-whisper from   faster_whisper   import   WhisperModel   model_size   =   \"large-v3\"   # Run on GPU with FP16   model   =   WhisperModel ( model_size ,  device = \"cuda\" ,  compute_type = \"float16\" )  # or run on GPU with INT8   # model = WhisperModel(model_size, device=\"cuda\", compute_type=\"int8_float16\")   # or run on CPU with INT8   # model = WhisperModel(model_size, device=\"cpu\", compute_type=\"int8\")   segments ,  info   =   model . transcribe ( \"audio.mp3\" ,  beam_size = 5 )  print ( \"Detected language '%s' with probability %f\"   %  ( info . language ,  info . language_probability ))  for   segment   in   segments :  print ( \"[%.2fs -> %.2fs] %s\"   %  ( segment . start ,  segment . end ,  segment . text ))"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 18,
        "cited_text": "For more control over the generation parameters, use the model + processor API directly: Ad-hoc generation arguments can be passed to  model.generate , including  num_beams  for beam-search,  return_timestamps  for segment-level timestamps, and  prompt_ids  for prompting. See the docstrings for more details. import   torch   from   transformers   import   AutoModelForSpeechSeq2Seq ,  AutoProcessor   from   datasets   import   Audio ,  load_dataset   device   =   \"cuda:0\"   if   torch . cuda . is_available ()  else   \"cpu\"   torch_dtype   =   torch . float16   if   torch . cuda . is_available ()  else   torch . float32   model_id   =   \"distil-whisper/distil-large-v3\"   model   =   AutoModelForSpeechSeq2Seq . from_pretrained (  model_id ,  torch_dtype = torch_dtype ,  low_cpu_mem_usage = True ,  use_safetensors = True  )  model . to ( device )  processor   =   AutoProcessor . from_pretrained ( model_id )  dataset   =   load_dataset ( \"hf-internal-testing/librispeech_asr_dummy\" ,  \"clean\" ,  split = \"validation\" )  dataset   =   dataset . cast_column ( \"audio\" ,  Audio ( processor . feature_extractor . sampling_rate ))  sample   =   dataset [ 0 ][ \"audio\" ]  input_features   =   processor (  sample [ \"array\" ],  sampling_rate = sample [ \"sampling_rate\" ],  return_tensors = \"pt\"  ). input_features   input_features   =   input_features . to ( device ,  dtype = torch_dtype )  gen_kwargs   =  {  \"max_new_tokens\" :  128 ,  \"num_beams\" :  1 ,  \"return_timestamps\" :  False , }  pred_ids   =   model . generate ( input_features ,  ** gen_kwargs )  pred_text   =   processor . batch_decode ( pred_ids ,  skip_special_tokens = True ,  decode_with_timestamps = gen_kwargs [ \"return_timestamps\" ])  print ( pred_text )"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 19,
        "cited_text": "Sequential Long-Form The latest distil-large-v3 checkpoint is specifically designed to be compatible with OpenAI's sequential long-form transcription algorithm. This algorithm uses a sliding window for buffered inference of long audio files (> 30-seconds), and returns more accurate transcriptions compared to the chunked long-form algorithm . The sequential long-form algorithm should be used in either of the following scenarios: Transcription accuracy is the most important factor, and latency is less of a consideration You are transcribing batches of long audio files, in which case the latency of sequential is comparable to chunked, while being up to 0.5% WER more accurate"
      },
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 20,
        "cited_text": "Internally, the  transcribe()  method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window. Below is an example usage of  whisper.detect_language()  and  whisper.decode()  which provide lower-level access to the model. import   whisper   model   =   whisper . load_model ( \"turbo\" )  # load audio and pad/trim it to fit 30 seconds   audio   =   whisper . load_audio ( \"audio.mp3\" )  audio   =   whisper . pad_or_trim ( audio )  # make log-Mel spectrogram and move to the same device as the model   mel   =   whisper . log_mel_spectrogram ( audio ,  n_mels = model . dims . n_mels ). to ( model . device )  # detect the spoken language   _ ,  probs   =   model . detect_language ( mel )  print ( f\"Detected language:  { max ( probs ,  key = probs . get ) } \" )  # decode the audio   options   =   whisper . DecodingOptions ()  result   =   whisper . decode ( model ,  mel ,  options )  # print the recognized text   print ( result . text )"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 21,
        "cited_text": "Size   Layers   Width   Heads   Parameters   English-only   Multilingual   tiny   4   384   6   39 M ✓ ✓ base   6   512   8   74 M ✓ ✓ small   12   768   12   244 M ✓ ✓ medium   24   1024   16   769 M ✓ ✓ large   32   1280   20   1550 M   x ✓ large-v2   32   1280   20   1550 M   x ✓ large-v3   32   1280   20   1550 M   x ✓ For demonstration purposes, we'll fine-tune the multilingual version of the small checkpoint with 244M params (~= 1GB). As for our data, we'll train and evaluate our system on a low-resource language taken from the Common Voice dataset. We'll show that with as little as 8 hours of fine-tuning data, we can achieve strong performance in this language."
      },
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 22,
        "cited_text": "Size   Parameters   English-only model   Multilingual model   Required VRAM   Relative speed   tiny   39 M   tiny.en   tiny   ~1 GB   ~10x   base   74 M   base.en   base   ~1 GB   ~7x   small   244 M   small.en   small   ~2 GB   ~4x   medium   769 M   medium.en   medium   ~5 GB   ~2x   large   1550 M   N/A   large   ~10 GB   1x   turbo   809 M   N/A   turbo   ~6 GB   ~8x The  .en  models for English-only applications tend to perform better, especially for the  tiny.en  and  base.en  models. We observed that the difference becomes less significant for the  small.en  and  medium.en  models. Additionally, the  turbo  model is an optimized version of  large-v3  that offers faster transcription speed with a minimal degradation in accuracy."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 23,
        "cited_text": "When scaled to 680,000 hours of labelled pre-training data, Whisper models demonstrate a strong ability to generalise to many datasets and domains. The pre-trained checkpoints achieve competitive results to state-of-the-art ASR systems, with near 3% word error rate (WER) on the test-clean subset of LibriSpeech ASR and a new state-of-the-art on TED-LIUM with 4.7% WER ( c.f. Table 8 of the Whisper paper ). The extensive multilingual ASR knowledge acquired by Whisper during pre-training can be leveraged for other low-resource languages; through fine-tuning, the pre-trained checkpoints can be adapted for specific datasets and languages to further improve upon these results."
      },
      {
        "source_id": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
        "citation_number": 24,
        "cited_text": "Faster Whisper transcription with CTranslate2 faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2 , which is a fast inference engine for Transformer models. This implementation is up to 4 times faster than openai/whisper for the same accuracy while using less memory. The efficiency can be further improved with 8-bit quantization on both CPU and GPU. Benchmark Whisper For reference, here's the time and memory usage that are required to transcribe 13 minutes of audio using different implementations:"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 25,
        "cited_text": "Distil-Whisper [Paper] [Models] [Colab] [Training Code] Distil-Whisper is a distilled version of Whisper for English speech recognition that is 6 times faster , 49% smaller, and performs within 1% word error rate (WER) on out-of-distribution evaluation sets: Model   Params / M   Rel. Latency ↑   Short-Form WER ↓   Long-Form WER ↓ large-v3 1550   1.0 8.4 11.0 distil-large-v3 756   6.3   9.7 10.8 distil-large-v2 756   5.8   10.1   11.6 distil-medium.en 394 6.8 11.1   12.4 distil-small.en 166 5.6   12.1   12.8"
      },
      {
        "source_id": "24726456-5f36-471c-8e85-d7c18566f228",
        "citation_number": 26,
        "cited_text": "Insanely Fast Whisper An opinionated CLI to transcribe Audio files w/ Whisper on-device! Powered by 🤗 Transformers , Optimum & flash-attn TL;DR - Transcribe 150 minutes (2.5 hours) of audio in less than 98 seconds - with OpenAI's Whisper Large v3 . Blazingly fast transcription is now a reality!⚡️ pipx install insanely-fast-whisper==0.0.15 --force Not convinced? Here are some benchmarks we ran on a Nvidia A100 - 80GB 👇 Optimisation type   Time to Transcribe (150 mins of Audio)   large-v3 (Transformers) ( fp32 )   ~31 ( 31 min 1 sec )   large-v3 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~5 ( 5 min 2 sec ) large-v3 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~2 ( 1 min 38 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~3 ( 3 min 16 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~1 ( 1 min 18 sec ) large-v2 (Faster Whisper) ( fp16  +  beam_size [1] )   ~9.23 ( 9 min 23 sec )   large-v2 (Faster Whisper) ( 8-bit  +  beam_size [1] )   ~8 ( 8 min 15 sec )"
      },
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 27,
        "cited_text": "pip install setuptools-rust Available models and languages There are six model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and inference speed relative to the large model. The relative speeds below are measured by transcribing English speech on a A100, and the real-world speed may vary significantly depending on many factors including the language, the speaking speed, and the available hardware."
      }
    ]
  }
}

## 深度实现

{
  "value": {
    "answer": "基于提供的来源，对 **Whisper 多语言 ASR 的工程实践与实现细节** 进行深入解析：\n\n### 1. 核心算法流程：端到端的 Sequence-to-Sequence\nWhisper 采用了标准的 **Transformer 编码器-解码器 (Encoder-Decoder)** 架构 [1, 2]。其处理流程如下：\n*   **音频特征提取**：原始音频首先被下采样至 **16kHz** [3, 4]。特征提取器将其转换为 **log-Mel 谱图**，这是一种模拟人类听觉的频率分布表示 [5, 6]。\n*   **30秒固定窗口**：Whisper 的核心工程特性是将音频统一处理为 **30秒** 的块 [7]。短音频补零，长音频截断或滑动窗口处理，无需额外的注意力掩码（Attention Mask），模型能自主推断忽略部分 [7, 8]。\n*   **编码与解码**：编码器将谱图特征转换为隐藏状态。解码器则利用 **交叉注意力机制 (Cross-attention)** 结合编码器输出，**自回归 (Autoregressively)** 地预测文本 Token [1, 2]。\n*   **多任务联合**：通过在序列起始处添加特殊的 **Task Tokens**，单个模型可同时执行语种识别 (LID)、语音激活检测 (VAD)、转录 (Transcribe) 和翻译 (Translate) 任务 [9, 10]。\n\n### 2. 关键代码架构与模型规模\n在工程实现（如 Hugging Face `transformers`）中，架构由以下核心组件构成：\n*   **WhisperProcessor**：封装了 `FeatureExtractor`（谱图转换）和 `Tokenizer`（Token 到文本映射）[11]。\n*   **WhisperForConditionalGeneration**：核心模型类，支持从 **Tiny (39M 参数)** 到 **Large-v3 (1550M 参数)** 的五种主要规格 [12, 13]。\n*   **具体参数指标**：\n    *   **训练数据**：**680,000 小时** 标注数据，其中 11.7 万小时为多语言数据 [14, 15]。\n    *   **资源占用**：Large 模型需约 **10GB VRAM**，Tiny 仅需 **1GB** [13]。\n    *   **性能精度**：LibriSpeech 测试集 WER 接近 **3%**，TED-LIUM 达到 **4.7%** [16]。\n\n### 3. 性能优化策略\n工程实践中通过多种手段提升了推理效率：\n*   **知识蒸馏 (Distil-Whisper)**：通过复制原编码器并极度压缩解码器（如仅留 2 层），实现 **6倍提速** 和 **50% 的体积缩减**，且 WER 损失维持在 1% 以内 [17, 18]。\n*   **投机解码 (Speculative Decoding)**：将 Distil-Whisper 作为助手模型预测草稿，再由 Large 模型验证，可在保证输出一致的前提下实现 **2倍加速** [19, 20]。\n*   **底层重构与量化**：\n    *   **faster-whisper**：使用 CTranslate2 引擎重构，支持 **int8 量化**，推理速度快 4 倍且显存占用更低 [21, 22]。\n    *   **whisper.cpp**：纯 C/C++ 实现，无第三方库依赖，针对 Apple Silicon (Metal/Core ML) 和多核 CPU (AVX/OpenVINO) 进行了深度优化 [23-25]。\n*   **硬件加速**：`insanely-fast-whisper` 利用 **Flash Attention 2**，可在 **98秒** 内转录 150 分钟音频 [26, 27]。\n\n### 4. 与竞品的技术对比\n| 维度 | Whisper (Open Source) | AssemblyAI (Universal-3) | Wav2Vec 2.0 |\n| :--- | :--- | :--- | :--- |\n| **训练范式** | **大规模监督预训练** [28] | 闭源商业模型 [29] | 无监督预训练+微调 [28] |\n| **核心优势** | 极强的零样本迁移能力和多语言支持 [14, 16] | 行业最低 WER，实时流式支持，幻觉降低 30% [30] | 语音表征质量高，但需更多微调 [28] |\n| **功能特性** | 支持翻译、多语言转录 [10] | 包含说话人识别、情感分析、代码切换 [31, 32] | 专注于纯 ASR [28] |\n| **工程实现** | 多样化（Python/C++/Rust 等）[33] | API 云端调用 [31] | 主要是 Python 框架 [28] |\n\n**数据对比总结**：Whisper 官方实现在 RTX 3070 Ti 上转录 13 分钟音频需 2分23秒，而经过优化的 `faster-whisper` 在 fp16 下仅需 **1分03秒**，配合 Batching 甚至可缩短至 **17秒** [22]。相比之下，AssemblyAI 等商业模型侧重于 **实时流式 (Streaming)** 场景的极低延迟和更完善的语音理解能力 [29, 34]。",
    "conversation_id": "ef4b3f56-d848-4548-a89c-d09edf73dd71",
    "sources_used": [
      "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "633960af-000b-4429-bbdb-11ef34edf441",
      "d45d638d-6616-4965-afc1-ed6232bb08bc",
      "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "38fdb474-c0d4-4e41-8e96-dad5f4790493",
      "4b47235d-662b-4853-adeb-f4e863c3cd53",
      "24726456-5f36-471c-8e85-d7c18566f228",
      "238aa703-f8b9-4b60-91e8-b088f06cf90e"
    ],
    "citations": {
      "1": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "2": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "3": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "4": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "5": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "6": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "7": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "8": "633960af-000b-4429-bbdb-11ef34edf441",
      "9": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "10": "633960af-000b-4429-bbdb-11ef34edf441",
      "11": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "12": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "13": "633960af-000b-4429-bbdb-11ef34edf441",
      "14": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "15": "d45d638d-6616-4965-afc1-ed6232bb08bc",
      "16": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "17": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "18": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "19": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "20": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "21": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
      "22": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
      "23": "4b47235d-662b-4853-adeb-f4e863c3cd53",
      "24": "4b47235d-662b-4853-adeb-f4e863c3cd53",
      "25": "4b47235d-662b-4853-adeb-f4e863c3cd53",
      "26": "24726456-5f36-471c-8e85-d7c18566f228",
      "27": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "28": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "29": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "30": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "31": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "32": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "33": "4b47235d-662b-4853-adeb-f4e863c3cd53",
      "34": "238aa703-f8b9-4b60-91e8-b088f06cf90e"
    },
    "references": [
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 1,
        "cited_text": "Whisper is a Transformer based encoder-decoder model, also referred to as a sequence-to-sequence model. It maps a sequence of audio spectrogram features to a sequence of text tokens. First, the raw audio inputs are converted to a log-Mel spectrogram by action of the feature extractor. The Transformer encoder then encodes the spectrogram to form a sequence of encoder hidden states. Finally, the decoder autoregressively predicts text tokens, conditional on both the previous tokens and the encoder hidden states. Figure 1 summarises the Whisper model."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 2,
        "cited_text": "Figure 1: Whisper model. The architecture follows the standard Transformer-based encoder-decoder model. A log-Mel spectrogram is input to the encoder. The last encoder hidden states are input to the decoder via cross-attention mechanisms. The decoder autoregressively predicts text tokens, jointly conditional on the encoder hidden states and previously predicted tokens. Figure source: OpenAI Whisper Blog . In a sequence-to-sequence model, the encoder transforms the audio inputs into a set of hidden state representations, extracting important features from the spoken speech. The decoder plays the role of a language model, processing the hidden state representations and generating the corresponding text transcriptions. Incorporating a language model internally in the system architecture is termed deep fusion . This is in contrast to shallow fusion , where a language model is combined externally with an encoder, such as with CTC +  n n n -gram ( c.f. Internal Language Model Estimation ). With deep fusion, the entire system can be trained end-to-end with the same training data and loss function, giving greater flexibility and generally superior performance ( c.f. ESB Benchmark )."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 3,
        "cited_text": "It is crucial that we match the sampling rate of our audio inputs to the sampling rate expected by our model, as audio signals with different sampling rates have very different distributions. Audio samples should only ever be processed with the correct sampling rate. Failing to do so can lead to unexpected results! For instance, taking an audio sample with a sampling rate of 16kHz and listening to it with a sampling rate of 8kHz will make the audio sound as though it's in half-speed. In the same way, passing audio with the wrong sampling rate can falter an ASR model that expects one sampling rate and receives another. The Whisper feature extractor expects audio inputs with a sampling rate of 16kHz, so we need to match our inputs to this value. We don't want to inadvertently train an ASR system on slow-motion speech!"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 4,
        "cited_text": "We can see that we've got a 1-dimensional input audio array and the corresponding target transcription. We've spoken heavily about the importance of the sampling rate and the fact that we need to match the sampling rate of our audio to that of the Whisper model (16kHz). Since our input audio is sampled at 48kHz, we need to downsample it to 16kHz before passing it to the Whisper feature extractor. We'll set the audio inputs to the correct sampling rate using dataset's cast_column method. This operation does not change the audio in-place, but rather signals to  datasets  to resample audio samples on the fly the first time that they are loaded:"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 5,
        "cited_text": "The second operation that the Whisper feature extractor performs is converting the padded audio arrays to log-Mel spectrograms. These spectrograms are a visual representation of the frequencies of a signal, rather like a Fourier transform. An example spectrogram is shown in Figure 2. Along the  y y y -axis are the Mel channels, which correspond to particular frequency bins. Along the  x x x -axis is time. The colour of each pixel corresponds to the log-intensity of that frequency bin at a given time. The log-Mel spectrogram is the form of input expected by the Whisper model."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 6,
        "cited_text": "The Mel channels (frequency bins) are standard in speech processing and chosen to approximate the human auditory range. All we need to know for Whisper fine-tuning is that the spectrogram is a visual representation of the frequencies in the speech signal. For more detail on Mel channels, refer to Mel-frequency cepstrum . Figure 2: Conversion of sampled audio array to log-Mel spectrogram. Left: sampled 1-dimensional audio signal. Right: corresponding log-Mel spectrogram. Figure source: Google SpecAugment Blog ."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 7,
        "cited_text": "The Whisper feature extractor performs two operations. It first pads/truncates a batch of audio samples such that all samples have an input length of 30s. Samples shorter than 30s are padded to 30s by appending zeros to the end of the sequence (zeros in an audio signal corresponding to no signal or silence). Samples longer than 30s are truncated to 30s. Since all elements in the batch are padded/truncated to a maximum length in the input space, we don't require an attention mask when forwarding the audio inputs to the Whisper model. Whisper is unique in this regard - with most audio models, you can expect to provide an attention mask that details where sequences have been padded, and thus where they should be ignored in the self-attention mechanism. Whisper is trained to operate without an attention mask and infer directly from the speech signals where to ignore the inputs."
      },
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 8,
        "cited_text": "Internally, the  transcribe()  method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window. Below is an example usage of  whisper.detect_language()  and  whisper.decode()  which provide lower-level access to the model. import   whisper   model   =   whisper . load_model ( \"turbo\" )  # load audio and pad/trim it to fit 30 seconds   audio   =   whisper . load_audio ( \"audio.mp3\" )  audio   =   whisper . pad_or_trim ( audio )  # make log-Mel spectrogram and move to the same device as the model   mel   =   whisper . log_mel_spectrogram ( audio ,  n_mels = model . dims . n_mels ). to ( model . device )  # detect the spoken language   _ ,  probs   =   model . detect_language ( mel )  print ( f\"Detected language:  { max ( probs ,  key = probs . get ) } \" )  # decode the audio   options   =   whisper . DecodingOptions ()  result   =   whisper . decode ( model ,  mel ,  options )  # print the recognized text   print ( result . text )"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 9,
        "cited_text": "Traditionally, when using encoder-only models for ASR, we decode using Connectionist Temporal Classification (CTC) . Here we are required to train a CTC tokenizer for each dataset we use. One of the advantages of using an encoder-decoder architecture is that we can directly leverage the tokenizer from the pre-trained model. The Whisper tokenizer is pre-trained on the transcriptions for the 96 pre-training languages. Consequently, it has an extensive byte-pair that is appropriate for almost all multilingual ASR applications. For Hindi, we can load the tokenizer and use it for fine-tuning without any further modifications. We simply have to specify the target language and the task. These arguments inform the tokenizer to prefix the language and task tokens to the start of encoded label sequences:"
      },
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 10,
        "cited_text": "Whisper [Blog] [Paper] [Model card] [Colab example] Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification. Approach A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 11,
        "cited_text": "Combine To Create A WhisperProcessor To simplify using the feature extractor and tokenizer, we can wrap both into a single  WhisperProcessor  class. This processor object inherits from the  WhisperFeatureExtractor  and  WhisperProcessor  and can be used on the audio inputs and model predictions as required. In doing so, we only need to keep track of two objects during training: the  processor  and the  model : from  transformers  import  WhisperProcessor processor = WhisperProcessor.from_pretrained( \"openai/whisper-small\" , language= \"Hindi\" , task= \"transcribe\" )"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 12,
        "cited_text": "Size   Layers   Width   Heads   Parameters   English-only   Multilingual   tiny   4   384   6   39 M ✓ ✓ base   6   512   8   74 M ✓ ✓ small   12   768   12   244 M ✓ ✓ medium   24   1024   16   769 M ✓ ✓ large   32   1280   20   1550 M   x ✓ large-v2   32   1280   20   1550 M   x ✓ large-v3   32   1280   20   1550 M   x ✓ For demonstration purposes, we'll fine-tune the multilingual version of the small checkpoint with 244M params (~= 1GB). As for our data, we'll train and evaluate our system on a low-resource language taken from the Common Voice dataset. We'll show that with as little as 8 hours of fine-tuning data, we can achieve strong performance in this language."
      },
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 13,
        "cited_text": "Size   Parameters   English-only model   Multilingual model   Required VRAM   Relative speed   tiny   39 M   tiny.en   tiny   ~1 GB   ~10x   base   74 M   base.en   base   ~1 GB   ~7x   small   244 M   small.en   small   ~2 GB   ~4x   medium   769 M   medium.en   medium   ~5 GB   ~2x   large   1550 M   N/A   large   ~10 GB   1x   turbo   809 M   N/A   turbo   ~6 GB   ~8x The  .en  models for English-only applications tend to perform better, especially for the  tiny.en  and  base.en  models. We observed that the difference becomes less significant for the  small.en  and  medium.en  models. Additionally, the  turbo  model is an optimized version of  large-v3  that offers faster transcription speed with a minimal degradation in accuracy."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 14,
        "cited_text": "Table of Contents Introduction Fine-tuning Whisper in a Google Colab Prepare Environment Load Dataset Prepare Feature Extractor, Tokenizer and Data Training and Evaluation Building a Demo Closing Remarks Introduction Whisper is a pre-trained model for automatic speech recognition (ASR) published in September 2022 by the authors Alec Radford et al. from OpenAI. Unlike many of its predecessors, such as Wav2Vec 2.0 , which are pre-trained on un-labelled audio data, Whisper is pre-trained on a vast quantity of labelled audio-transcription data, 680,000 hours to be precise. This is an order of magnitude more data than the un-labelled audio data used to train Wav2Vec 2.0 (60,000 hours). What is more, 117,000 hours of this pre-training data is multilingual ASR data. This results in checkpoints that can be applied to over 96 languages, many of which are considered low-resource ."
      },
      {
        "source_id": "d45d638d-6616-4965-afc1-ed6232bb08bc",
        "citation_number": 15,
        "cited_text": "Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > eess >  arXiv:2212.04356 Help | Advanced Search Electrical Engineering and Systems Science > Audio and Speech Processing arXiv:2212.04356 (eess)   [Submitted on 6 Dec 2022] Title: Robust Speech Recognition via Large-Scale Weak Supervision Authors: Alec Radford , Jong Wook Kim , Tao Xu , Greg Brockman , Christine McLeavey , Ilya Sutskever View a PDF of the paper titled Robust Speech Recognition via Large-Scale Weak Supervision, by Alec Radford and 5 other authors View PDF Abstract: We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results but in a zero-shot transfer setting without the need for any fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.  Subjects:   Audio and Speech Processing (eess.AS) ; Computation and Language (cs.CL); Machine Learning (cs.LG); Sound (cs.SD)   Cite as: arXiv:2212.04356 [eess.AS]   (or arXiv:2212.04356v1 [eess.AS]  for this version) https://doi.org/10.48550/arXiv.2212.04356 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 16,
        "cited_text": "When scaled to 680,000 hours of labelled pre-training data, Whisper models demonstrate a strong ability to generalise to many datasets and domains. The pre-trained checkpoints achieve competitive results to state-of-the-art ASR systems, with near 3% word error rate (WER) on the test-clean subset of LibriSpeech ASR and a new state-of-the-art on TED-LIUM with 4.7% WER ( c.f. Table 8 of the Whisper paper ). The extensive multilingual ASR knowledge acquired by Whisper during pre-training can be leveraged for other low-resource languages; through fine-tuning, the pre-trained checkpoints can be adapted for specific datasets and languages to further improve upon these results."
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 17,
        "cited_text": "Distil-Whisper [Paper] [Models] [Colab] [Training Code] Distil-Whisper is a distilled version of Whisper for English speech recognition that is 6 times faster , 49% smaller, and performs within 1% word error rate (WER) on out-of-distribution evaluation sets: Model   Params / M   Rel. Latency ↑   Short-Form WER ↓   Long-Form WER ↓ large-v3 1550   1.0 8.4 11.0 distil-large-v3 756   6.3   9.7 10.8 distil-large-v2 756   5.8   10.1   11.6 distil-medium.en 394 6.8 11.1   12.4 distil-small.en 166 5.6   12.1   12.8"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 18,
        "cited_text": "3. Approach ✍️ To distill Whisper, we copy the entire encoder module and freeze it during training. We copy only two decoder layers, which are initialised from the first and last decoder layers from Whisper. All other decoder layers from Whisper are discarded: Distil-Whisper is trained on a knowledge distillation objective. Specifically, it is trained to minimise the KL divergence between the distilled model and the Whisper model, as well as the cross-entropy loss on pseudo-labelled audio data. We train Distil-Whisper on a total of 22k hours of pseudo-labelled audio data, spanning 10 domains with over 18k speakers:"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 19,
        "cited_text": "Speculative Decoding Distil-Whisper can be used as an assistant model to Whisper for speculative decoding . Speculative decoding mathematically ensures the exact same outputs as Whisper are obtained while being 2 times faster. This makes it the perfect drop-in replacement for existing Whisper pipelines, since the same outputs are guaranteed. For speculative decoding, we need to load both the teacher: openai/whisper-large-v3 . As well as the assistant ( a.k.a student) distil-whisper/distil-large-v3 . Let's start by loading the teacher model and processor. We do this in much the same way we loaded the Distil-Whisper model in the previous examples:"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 20,
        "cited_text": "from   datasets   import   load_dataset   dataset   =   load_dataset ( \"hf-internal-testing/librispeech_asr_dummy\" ,  \"clean\" ,  split = \"validation\" )  sample   =   dataset [ 0 ][ \"audio\" ]  result   =   pipe ( sample )  print ( result [ \"text\" ]) Note: speculative decoding should be on average 2x faster than using \"only\" Whisper large-v2 at a mere 8% increase in VRAM memory usage while mathematically ensuring the same results. This makes it the perfect replacement for Whisper large-v2 in existing speech recognition pipelines."
      },
      {
        "source_id": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
        "citation_number": 21,
        "cited_text": "Faster Whisper transcription with CTranslate2 faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2 , which is a fast inference engine for Transformer models. This implementation is up to 4 times faster than openai/whisper for the same accuracy while using less memory. The efficiency can be further improved with 8-bit quantization on both CPU and GPU. Benchmark Whisper For reference, here's the time and memory usage that are required to transcribe 13 minutes of audio using different implementations:"
      },
      {
        "source_id": "38fdb474-c0d4-4e41-8e96-dad5f4790493",
        "citation_number": 22,
        "cited_text": "openai/whisper @ v20240930 whisper.cpp @ v1.7.2 transformers @ v4.46.3 faster-whisper @ v1.1.0 Large-v2 model on GPU Implementation   Precision   Beam size   Time   VRAM Usage   openai/whisper   fp16   5   2m23s   4708MB   whisper.cpp (Flash Attention)   fp16   5   1m05s   4127MB   transformers (SDPA) 1 fp16   5   1m52s   4960MB   faster-whisper   fp16   5   1m03s   4525MB   faster-whisper ( batch_size=8 )   fp16   5   17s   6090MB   faster-whisper   int8   5   59s   2926MB   faster-whisper ( batch_size=8 )   int8   5   16s   4500MB"
      },
      {
        "source_id": "4b47235d-662b-4853-adeb-f4e863c3cd53",
        "citation_number": 23,
        "cited_text": "whisper.cpp Stable: v1.8.1 / Roadmap High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model: Plain C/C++ implementation without dependencies Apple Silicon first-class citizen - optimized via ARM NEON, Accelerate framework, Metal and Core ML AVX intrinsics support for x86 architectures VSX intrinsics support for POWER architectures Mixed F16 / F32 precision Integer quantization support Zero memory allocations at runtime Vulkan support Support for CPU-only inference Efficient GPU support for NVIDIA OpenVINO Support Ascend NPU Support Moore Threads GPU Support C-style API Voice Activity Detection (VAD)"
      },
      {
        "source_id": "4b47235d-662b-4853-adeb-f4e863c3cd53",
        "citation_number": 24,
        "cited_text": "Core ML support On Apple Silicon devices, the Encoder inference can be executed on the Apple Neural Engine (ANE) via Core ML. This can result in significant speed-up - more than x3 faster compared with CPU-only execution. Here are the instructions for generating a Core ML model and using it with  whisper.cpp : Install Python dependencies needed for the creation of the Core ML model: pip install ane_transformers pip install openai-whisper pip install coremltools To ensure  coremltools  operates correctly, please confirm that Xcode is installed and execute  xcode-select --install  to install the command-line tools. Python 3.11 is recommended. MacOS Sonoma (version 14) or newer is recommended, as older versions of MacOS might experience issues with transcription hallucination."
      },
      {
        "source_id": "4b47235d-662b-4853-adeb-f4e863c3cd53",
        "citation_number": 25,
        "cited_text": "For more information about the Core ML implementation please refer to PR #566 . OpenVINO support On platforms that support OpenVINO , the Encoder inference can be executed on OpenVINO-supported devices including x86 CPUs and Intel GPUs (integrated & discrete). This can result in significant speedup in encoder performance. Here are the instructions for generating the OpenVINO model and using it with  whisper.cpp : First, setup python virtual env. and install python dependencies. Python 3.10 is recommended."
      },
      {
        "source_id": "24726456-5f36-471c-8e85-d7c18566f228",
        "citation_number": 26,
        "cited_text": "Insanely Fast Whisper An opinionated CLI to transcribe Audio files w/ Whisper on-device! Powered by 🤗 Transformers , Optimum & flash-attn TL;DR - Transcribe 150 minutes (2.5 hours) of audio in less than 98 seconds - with OpenAI's Whisper Large v3 . Blazingly fast transcription is now a reality!⚡️ pipx install insanely-fast-whisper==0.0.15 --force Not convinced? Here are some benchmarks we ran on a Nvidia A100 - 80GB 👇 Optimisation type   Time to Transcribe (150 mins of Audio)   large-v3 (Transformers) ( fp32 )   ~31 ( 31 min 1 sec )   large-v3 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~5 ( 5 min 2 sec ) large-v3 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~2 ( 1 min 38 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~3 ( 3 min 16 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~1 ( 1 min 18 sec ) large-v2 (Faster Whisper) ( fp16  +  beam_size [1] )   ~9.23 ( 9 min 23 sec )   large-v2 (Faster Whisper) ( 8-bit  +  beam_size [1] )   ~8 ( 8 min 15 sec )"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 27,
        "cited_text": "For more details on speculative decoding, refer to the following resources: Speculative decoding for 2x faster Whisper inference blog post by Sanchit Gandhi Assisted Generation: a new direction toward low-latency text generation blog post by Joao Gante Fast Inference from Transformers via Speculative Decoding paper by Leviathan et. al. Additional Speed & Memory Improvements You can apply additional speed and memory improvements to Distil-Whisper which we cover in the following. Flash Attention We recommend using Flash Attention 2 if your GPU allows for it. To do so, you first need to install Flash Attention :"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 28,
        "cited_text": "This quantity of labelled data enables Whisper to be pre-trained directly on the supervised task of speech recognition, learning a speech-to-text mapping from the labelled audio-transcription pre-training data  1 {}^1 1 . As a consequence, Whisper requires little additional fine-tuning to yield a performant ASR model. This is in contrast to Wav2Vec 2.0, which is pre-trained on the unsupervised task of masked prediction. Here, the model is trained to learn an intermediate mapping from speech to hidden states from un-labelled audio only data. While unsupervised pre-training yields high-quality representations of speech, it does not learn a speech-to-text mapping. This mapping is only learned during fine-tuning, thus requiring more fine-tuning to yield competitive performance."
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 29,
        "cited_text": "AssemblyAI Documentation: Real-time Transcription LiveKit SDK: Building Voice Agents Voice Agent Best Practices Guide Introducing Medical Mode: Purpose-built accuracy for medical terminology Learn more Speech-to-Text Streaming Speech-to-Text Speech Understanding LLM Gateway Guardrails Speech-to-Speech Product overview Deployment Self-Hosted Voice AI Cloud Use Cases Conversation Intelligence Medical Transcription Contact Centers Voice Agents AI Notetakers Customers Zoom leverages AssemblyAI to help advance its AI research and development. Read the story Siro achieves a 90% Reduction in customer complaints and support tickets. \n Watch the video Developers   Documentation API Reference Cookbooks Support Quick Links Status Changelog Discord Resources   Blog Partners Research Benchmarks Security Introducing Universal-3 Pro Streaming Universal-3 Pro Streaming brings prompting, disfluency control, code-switching, real-time diarization, and 99+ language support to real-time use cases Playground Pricing Enterprise Contact us Log in Get started The best way to build Voice AI apps"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 30,
        "cited_text": "industry-leading accuracy Avoid garbage in, garbage out Your product experience is only as good as the inputs it’s built on. AssemblyAI’s models lead the industry in accuracy and reliability. Industry’s lowest Word Error Rate (WER) Up to 30% less hallucinations than other providers Preferred by 73% of end users in unbiased evaluations Explore our latest model CAPABILITIES Go beyond transcription Access a full suite of speech understanding capabilities to uncover insights, identify speakers, and build powerful product experiences."
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 31,
        "cited_text": "Correctly identify speakers with advanced diarization capabilities Automatically format text and alphanumerics for clearer outputs Accurately capture multilingual speech with automatic language detection Check out our products Build-ready Easy to start, even easier to scale We built AssemblyAI to be the easiest platform on the market for developers to build, ship, and scale on. Serving 600M+ inference calls and over 840M API calls per month Over 40 terabytes of audio processed daily Pay only for what you use and scale to millions of hours without contracts or throttles"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 32,
        "cited_text": "90%  reduction in customer complaints and support tickets Unlock the value of voice data Build what’s next on the platform powering thousands of the industry’s leading of Voice AI apps. Try our API for free Contact sales Build new AI products with voice data leveraging AssemblyAI’s industry-leading Voice AI models for accurate speech-to-text, speaker detection, sentiment analysis, chapter detection, PII redaction, and more. ©  2025  AssemblyAI, Inc."
      },
      {
        "source_id": "4b47235d-662b-4853-adeb-f4e863c3cd53",
        "citation_number": 33,
        "cited_text": "model parameters mel filters vocabulary weights You can download the converted models using the models/download-ggml-model.sh script or manually from here: https://huggingface.co/ggerganov/whisper.cpp For more details, see the conversion script models/convert-pt-to-ggml.py or models/README.md . Bindings Rust: tazz4843/whisper-rs | #310 JavaScript: bindings/javascript | #309 React Native (iOS / Android): whisper.rn Go: bindings/go | #312 Java: GiviMAD/whisper-jni Ruby: bindings/ruby | #507 Objective-C / Swift: ggml-org/whisper.spm | #313 exPHAT/SwiftWhisper .NET: | #422 sandrohanea/whisper.net NickDarvey/whisper Python: | #9 stlukey/whispercpp.py (Cython) AIWintermuteAI/whispercpp (Updated fork of aarnphm/whispercpp) aarnphm/whispercpp (Pybind11) abdeladim-s/pywhispercpp (Pybind11) R: bnosac/audio.whisper Unity: macoron/whisper.unity"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 34,
        "cited_text": "Speech-to-Text Unlock the value of prerecorded voice data, and power workflows with unmatched accuracy. Learn more Streaming Speech-to-Text Build intuitive voice agent workflows with ultra-low latency, high accuracy, precise end-of-turn controls, and more. Learn more Speech Understanding Enable deep analysis and high-value insights with sophisticated audio-intelligence models. Learn more Product overview Everything you need to build voice apps that outpace the competition The accuracy and capabilities required to build products that stand out, and the flexibility to scale to millions of users without blinking an eye."
      }
    ]
  }
}

## 实战应用

{
  "value": {
    "answer": "基于对来源的深度解析，Whisper 在多语言 ASR 的工程实践中展现了极高的灵活性。以下是其真实应用场景、工业级方案、基准数据及开发者实战经验的详细列表：\n\n### 1. 真实应用场景与案例\n*   **医疗转录 (Medical Transcription)**：专门用于处理复杂的医学术语，通过 disfluency 控制（过滤或保留“嗯、啊”等语气词）和特定模式提高准确度 [1, 2]。\n*   **会议记录与 AI 笔记 (AI Notetakers)**：如 Zoom 利用其进行 AI 研发，Siro 通过转录减少了 90% 的客户投诉 [1, 3]。\n*   **多语言对话分析 (Conversational Analysis)**：识别说话人角色（如医生/病人），并支持自然的代码切换（Code-switching，如中英夹杂）[4, 5]。\n*   **端侧语音助手 (On-device Voice Agents)**：利用 `whisper.cpp` 在 iPhone 13 等设备上实现完全离线的语音指令识别 [6, 7]。\n*   **媒体内容创作**：如 `Open-Lyrics` 用于自动生成多语言歌词和翻译 [8]。\n\n### 2. 工业级部署方案\n*   **全托管云端方案**：\n    *   **Hugging Face Inference Endpoints**：支持一键部署，提供自动扩缩容，起步价低至 $0.06/小时 [9, 10]。\n    *   **OpenAI API**：提供 `whisper-1` 及其优化版本（如 `gpt-4o-transcribe`），支持高达 25MB 的文件上传和 speaker diarization（说话人日志）[11, 12]。\n    *   **Groq Cloud**：利用 LPU 架构实现极速推理，宣称成本降低 89%，速度提升 7.41 倍 [13, 14]。\n*   **自托管与容器化方案**：\n    *   **Speaches**：兼容 OpenAI API 的服务器，支持 Docker 部署和流式传输 [8]。\n    *   **faster-whisper + CTranslate2**：通过 int8 量化显著降低显存，适合私有化部署 [15]。\n\n### 3. 性能基准数据 (基于 NVIDIA RTX 3070 Ti / A100)\n| 实现方案 | 硬件/配置 | 150分钟音频耗时 | 13分钟音频耗时 | 显存/内存占用 |\n| :--- | :--- | :--- | :--- | :--- |\n| **OpenAI 官方** | GPU (fp16) | ~31 分钟 | 2 分 23 秒 | ~4.7GB (Large) [16, 17] |\n| **faster-whisper** | GPU (batch=8) | - | **17 秒** | ~6.1GB [16] |\n| **insanely-fast-whisper** | A100 (Flash Attention 2) | **98 秒** | - | - [17] |\n| **whisper.cpp** | M1 Mac (Core ML) | - | 1 分 05 秒 (对比 CPU 快 3 倍) | ~3.9GB (Large) [16, 18] |\n| **Distil-Whisper** | GPU | - | 提速 6 倍 | 体积减小 50% [19, 20] |\n\n### 4. 开发者最佳实践\n*   **使用投机解码 (Speculative Decoding)**：将 `Distil-Whisper` 作为助手模型，配合 `Whisper Large` 使用。这可以在数学上保证输出完全一致的前提下，将推理速度提升 **2 倍** [21, 22]。\n*   **Prompt 工程优化**：通过 `prompt` 参数引导模型。例如，提供公司专有名词（如 \"DALL·E\"）可防止模型将其误识别为 \"DALI\" [23, 24]。\n*   **集成 VAD 过滤**：在转录前使用 `Silero VAD` 过滤掉 2 秒以上的静音片段，能显著减少无效计算并提升长音频转录的稳定性 [25, 26]。\n*   **少样本微调**：在 Hindi（印地语）等低资源语言上，仅需 **8 小时** 的标注数据进行微调，即可将 WER 从 63.5% 降低至 32% [27, 28]。\n\n### 5. 常见踩坑经验\n*   **采样率不匹配**：Whisper 强制要求 **16kHz** 采样率。如果输入音频采样率不对且未进行重采样（downsample），会导致识别速度异常（如语速减半）或识别失败 [29, 30]。\n*   **长音频幻觉 (Hallucinations)**：在处理长音频时，如果使用简单的分段转录，模型可能会在静音处反复生成重复的词。建议通过限制 `max_new_tokens` 或使用特定的长音频滑动窗口算法来缓解 [31, 32]。\n*   **环境依赖冲突**：\n    *   在 Python 3.11 下使用 `pipx` 安装可能解析版本错误，需使用 `--ignore-requires-python` 参数 [33]。\n    *   Windows 下常出现 \"Torch not compiled with CUDA\" 错误，通常需要手动指定 index-url 安装对应版本的 torch [34]。\n*   **硬件限制**：Mac 上的 `mps` 后端优化不如 CUDA，且非常耗显存（12GB 显存通常只能支持 `batch_size=4`） [35]。\n*   **微调副作用**：有开发者反馈，微调 ASR（语音转文本）任务后，模型的 LID（语种识别）能力可能会下降 [36]。",
    "conversation_id": "ef4b3f56-d848-4548-a89c-d09edf73dd71",
    "sources_used": [
      "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "4d431d87-322c-4ab3-8d98-5f20f55937b2",
      "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "c84ffb6e-2203-475e-a691-e005d6b0df59",
      "24726456-5f36-471c-8e85-d7c18566f228",
      "4b47235d-662b-4853-adeb-f4e863c3cd53",
      "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "391d2de4-b3c4-426f-bb1a-4ad8a535777f"
    ],
    "citations": {
      "1": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "2": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "3": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "4": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "5": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "6": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "7": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "8": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "9": "4d431d87-322c-4ab3-8d98-5f20f55937b2",
      "10": "4d431d87-322c-4ab3-8d98-5f20f55937b2",
      "11": "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "12": "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "13": "c84ffb6e-2203-475e-a691-e005d6b0df59",
      "14": "c84ffb6e-2203-475e-a691-e005d6b0df59",
      "15": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "16": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "17": "24726456-5f36-471c-8e85-d7c18566f228",
      "18": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "19": "4b47235d-662b-4853-adeb-f4e863c3cd53",
      "20": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "21": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "22": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "23": "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "24": "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "25": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "26": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "27": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "28": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "29": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "30": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "31": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "32": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "33": "24726456-5f36-471c-8e85-d7c18566f228",
      "34": "24726456-5f36-471c-8e85-d7c18566f228",
      "35": "24726456-5f36-471c-8e85-d7c18566f228",
      "36": "391d2de4-b3c4-426f-bb1a-4ad8a535777f"
    },
    "references": [
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 1,
        "cited_text": "AssemblyAI Documentation: Real-time Transcription LiveKit SDK: Building Voice Agents Voice Agent Best Practices Guide Introducing Medical Mode: Purpose-built accuracy for medical terminology Learn more Speech-to-Text Streaming Speech-to-Text Speech Understanding LLM Gateway Guardrails Speech-to-Speech Product overview Deployment Self-Hosted Voice AI Cloud Use Cases Conversation Intelligence Medical Transcription Contact Centers Voice Agents AI Notetakers Customers Zoom leverages AssemblyAI to help advance its AI research and development. Read the story Siro achieves a 90% Reduction in customer complaints and support tickets. \n Watch the video Developers   Documentation API Reference Cookbooks Support Quick Links Status Changelog Discord Resources   Blog Partners Research Benchmarks Security Introducing Universal-3 Pro Streaming Universal-3 Pro Streaming brings prompting, disfluency control, code-switching, real-time diarization, and 99+ language support to real-time use cases Playground Pricing Enterprise Contact us Log in Get started The best way to build Voice AI apps"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 2,
        "cited_text": "Today’s top Voice AI companies rely on AssemblyAI’s speech-to-text and speech understanding models to launch groundbreaking products fast and scale with ease. Streaming Speech-to-Text   Speech-to-Text   Voice Agent Try stating information like names, dates, and address, along with technical data like codes, commands, formulas, and special formatting to see how our model performs... Universal-3 Pro Streaming Context-aware Audio tags Verbatim Keyterms Speaker roles Code switching Source Clinical evaluation history:  00:00 01:59   \"prompt\": \"Produce a transcript for a clinical history evaluation. It's important to capture medication and dosage accurately. Every disfluency is meaningful data. Include: fillers (um, uh, er, erm, ah, hmm, mhm, like, you know, I mean), repetitions (I I I, the the), restarts (I was- I went), stutters (th-that, b-but, no-not), and informal speech (gonna, wanna, gotta)\" Without prompting"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 3,
        "cited_text": "90%  reduction in customer complaints and support tickets Unlock the value of voice data Build what’s next on the platform powering thousands of the industry’s leading of Voice AI apps. Try our API for free Contact sales Build new AI products with voice data leveraging AssemblyAI’s industry-leading Voice AI models for accurate speech-to-text, speaker detection, sentiment analysis, chapter detection, PII redaction, and more. ©  2025  AssemblyAI, Inc."
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 4,
        "cited_text": "With disfluency prompting Do you and Quentin still socialize,  uh , when you come to Los Angeles, or is it like he's so used to having you here? No, no, no,  we, we , we're friends. What do you do with him? Source Proper noun spelling: 00:00 01:59   \"keyterms_prompt\": [\"Kelly Byrne-Donoghue\"] Without keyterms prompting \"Hi, this is Kelly  Byrne Donahue \" Without keyterms prompting \"Hi, this is Kelly  Byrne-Donahue \" Source Caputuring speaker roles: 00:00 01:59   \"prompt\": \"Produce a transcript with every disfluency data. Additionally, label speakers with their respective roles. 1. Place [Speaker:role] at the start of each speaker turn. Example format: [Speaker:NURSE] Hello there. How can I help you today? [Speaker:PATIENT] I'm feeling unwell. I have a headache.\"} With traditional speaker labels"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 5,
        "cited_text": "Speaker A : 5Mg. And do you take it regularly? \n ‍ \n Speaker B : Oh yeah, yeah. \n ‍ \n Speaker A : Good. \n ‍ \n Speaker B : Every evening. \n ‍ \n Speaker A : And no side effects with it? With speaker labels prompting Speaker [Nurse] : 5Mg. And do you take it regularly? \n ‍ \n Speaker [Patient] : Oh yeah, yeah. \n ‍ \n Speaker [Nurse] : Good. \n ‍ \n Speaker [Patient] : Every evening. \n ‍ \n Speaker [Nurse] : And no side effects with it? Source Spanish and english audio: 00:00 01:59   \"language_detection\": True \n \"prompt\": Preserve natural code-switching between English and Spanish. Retain spokenlanguage as-is (correct \"I was hablando con mi manager\"). Without codeswitching"
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 6,
        "cited_text": "Supported platforms: Mac OS (Intel and Arm) iOS Android Java Linux / FreeBSD WebAssembly Windows ( MSVC and MinGW ) Raspberry Pi Docker The entire high-level implementation of the model is contained in whisper.h and whisper.cpp . The rest of the code is part of the ggml machine learning library. Having such a lightweight implementation of the model allows to easily integrate it in different platforms and applications. As an example, here is a video of running the model on an iPhone 13 device - fully offline, on-device: whisper.objc"
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 7,
        "cited_text": "whisper-iphone-13-mini-2.mp4 You can also easily make your own offline voice assistant application: command command-0.mp4 On Apple Silicon, the inference runs fully on the GPU via Metal: metal-base-1.mp4 Quick start First clone the repository: git clone https://github.com/ggml-org/whisper.cpp.git Navigate into the directory: cd whisper.cpp Then, download one of the Whisper models converted in ggml  format . For example: sh ./models/download-ggml-model.sh base.en Now build the whisper-cli example and transcribe an audio file like this:"
      },
      {
        "source_id": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
        "citation_number": 8,
        "cited_text": "speaches is an OpenAI compatible server using  faster-whisper . It's easily deployable with Docker, works with OpenAI SDKs/CLI, supports streaming, and live transcription. WhisperX is an award-winning Python library that offers speaker diarization and accurate word-level timestamps using wav2vec2 alignment whisper-ctranslate2 is a command line client based on faster-whisper and compatible with the original client from openai/whisper. whisper-diarize is a speaker diarization tool that is based on faster-whisper and NVIDIA NeMo. whisper-standalone-win Standalone CLI executables of faster-whisper for Windows, Linux & macOS. asr-sd-pipeline provides a scalable, modular, end to end multi-speaker speech to text solution implemented using AzureML pipelines. Open-Lyrics is a Python library that transcribes voice files using faster-whisper, and translates/polishes the resulting text into  .lrc  files in the desired language using OpenAI-GPT. wscribe is a flexible transcript generation tool supporting faster-whisper, it can export word level transcript and the exported transcript then can be edited with wscribe-editor aTrain is a graphical user interface implementation of faster-whisper developed at the BANDAS-Center at the University of Graz for transcription and diarization in Windows ( Windows Store App ) and Linux. Whisper-Streaming implements real-time mode for offline Whisper-like speech-to-text models with faster-whisper as the most recommended back-end. It implements a streaming policy with self-adaptive latency based on the actual source complexity, and demonstrates the state of the art. WhisperLive is a nearly-live implementation of OpenAI's Whisper which uses faster-whisper as the backend to transcribe audio in real-time. Faster-Whisper-Transcriber is a simple but reliable voice transcriber that provides a user-friendly interface. Open-dubbing is open dubbing is an AI dubbing system which uses machine learning models to automatically translate and synchronize audio dialogue into different languages. Whisper-FastAPI whisper-fastapi is a very simple script that provides an API backend compatible with OpenAI, HomeAssistant, and Konele (Android voice typing) formats."
      },
      {
        "source_id": "4d431d87-322c-4ab3-8d98-5f20f55937b2",
        "citation_number": 9,
        "cited_text": "Features Everything you need to deploy AI models at scale Fully Managed Infrastructure Don't worry about Kubernetes, CUDA versions, or configuring VPNs. Focus on deploying your model and serving customers. Autoscaling Automatically scales up as traffic increases and down as it decreases to save on compute costs. Observability Understand and debug your model through comprehensive logs & metrics. Inference Engines Deploy with vLLM, TGI, SGLang, TEI, or custom containers. Hugging Face Integration Download model weights fast and securely with seamless Hugging Face Hub integration."
      },
      {
        "source_id": "4d431d87-322c-4ab3-8d98-5f20f55937b2",
        "citation_number": 10,
        "cited_text": "Future-proof AI Stack Stay current with the latest frameworks and optimizations without managing complex upgrades. Pricing Choose a plan that fits your needs Self-Serve Pay as you go when using Inference Endpoints Pay for what you use, per minute Starting as low as $0.06/hour Billed monthly Email support See Instance Pricing Enterprise Get a custom quote and premium support Lower marginal costs based on volume Uptime guarantees Custom annual contracts Dedicated support, SLAs Request a Quote Testimonials"
      },
      {
        "source_id": "d689a9f5-058d-40ac-a249-2fad6764f90e",
        "citation_number": 11,
        "cited_text": "Events Meetups Hackathon Support Forum Discord API Dashboard Speech to text Learn how to turn audio into text. The Audio API provides two speech to text endpoints: transcriptions translations Historically, both endpoints have been backed by our open source Whisper model ( whisper-1 ). The  transcriptions  endpoint now also supports higher quality model snapshots, with limited parameter support: gpt-4o-mini-transcribe gpt-4o-transcribe gpt-4o-transcribe-diarize All endpoints can be used to:"
      },
      {
        "source_id": "d689a9f5-058d-40ac-a249-2fad6764f90e",
        "citation_number": 12,
        "cited_text": "Transcribe audio into whatever language the audio is in. Translate and transcribe the audio into English. File uploads are currently limited to 25 MB, and the following input file types are supported:  mp3 ,  mp4 ,  mpeg ,  mpga ,  m4a ,  wav , and  webm . Known speaker reference clips for diarization accept the same formats when provided as data URLs. Quickstart Transcriptions The transcriptions API takes as input the audio file you want to transcribe and the desired output file format for the transcription of the audio. All models support the same set of input formats. On output:"
      },
      {
        "source_id": "c84ffb6e-2203-475e-a691-e005d6b0df59",
        "citation_number": 13,
        "cited_text": "The McLaren Formula 1 Team chooses Groq for inference. The McLaren F1 Team is fueled by decision-making, analysis, development and real-time insights. So the McLaren F1 Team chose Groq. Read More Don’t take our word for it. Proof from the people shipping. Read Customer Stories If we have things where performance matters more, we come to Groq - you deliver real, working solutions, not just buzzwords. We optimized our infrastructure to its limits – but the breakthrough came with GroqCloud. Overnight, our chat speed surged 7.41x while costs fell by 89%. I was stunned. So, we tripled our token consumption. We simply can’t get enough."
      },
      {
        "source_id": "c84ffb6e-2203-475e-a691-e005d6b0df59",
        "citation_number": 14,
        "cited_text": "Groq has created immense savings and reduced so much overhead for us. We’ve been able to keep costs for our main offerings incredibly low, helping keep our premium plan at a reasonable price for students of all backgrounds. If we have things where performance matters more, we come to Groq - you deliver real, working solutions, not just buzzwords. We optimized our infrastructure to its limits – but the breakthrough came with GroqCloud. Overnight, our chat speed surged 7.41x while costs fell by 89%. I was stunned. So, we tripled our token consumption. We simply can’t get enough."
      },
      {
        "source_id": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
        "citation_number": 15,
        "cited_text": "Faster Whisper transcription with CTranslate2 faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2 , which is a fast inference engine for Transformer models. This implementation is up to 4 times faster than openai/whisper for the same accuracy while using less memory. The efficiency can be further improved with 8-bit quantization on both CPU and GPU. Benchmark Whisper For reference, here's the time and memory usage that are required to transcribe 13 minutes of audio using different implementations:"
      },
      {
        "source_id": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
        "citation_number": 16,
        "cited_text": "openai/whisper @ v20240930 whisper.cpp @ v1.7.2 transformers @ v4.46.3 faster-whisper @ v1.1.0 Large-v2 model on GPU Implementation   Precision   Beam size   Time   VRAM Usage   openai/whisper   fp16   5   2m23s   4708MB   whisper.cpp (Flash Attention)   fp16   5   1m05s   4127MB   transformers (SDPA) 1 fp16   5   1m52s   4960MB   faster-whisper   fp16   5   1m03s   4525MB   faster-whisper ( batch_size=8 )   fp16   5   17s   6090MB   faster-whisper   int8   5   59s   2926MB   faster-whisper ( batch_size=8 )   int8   5   16s   4500MB"
      },
      {
        "source_id": "24726456-5f36-471c-8e85-d7c18566f228",
        "citation_number": 17,
        "cited_text": "Insanely Fast Whisper An opinionated CLI to transcribe Audio files w/ Whisper on-device! Powered by 🤗 Transformers , Optimum & flash-attn TL;DR - Transcribe 150 minutes (2.5 hours) of audio in less than 98 seconds - with OpenAI's Whisper Large v3 . Blazingly fast transcription is now a reality!⚡️ pipx install insanely-fast-whisper==0.0.15 --force Not convinced? Here are some benchmarks we ran on a Nvidia A100 - 80GB 👇 Optimisation type   Time to Transcribe (150 mins of Audio)   large-v3 (Transformers) ( fp32 )   ~31 ( 31 min 1 sec )   large-v3 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~5 ( 5 min 2 sec ) large-v3 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~2 ( 1 min 38 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~3 ( 3 min 16 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~1 ( 1 min 18 sec ) large-v2 (Faster Whisper) ( fp16  +  beam_size [1] )   ~9.23 ( 9 min 23 sec )   large-v2 (Faster Whisper) ( 8-bit  +  beam_size [1] )   ~8 ( 8 min 15 sec )"
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 18,
        "cited_text": "Core ML support On Apple Silicon devices, the Encoder inference can be executed on the Apple Neural Engine (ANE) via Core ML. This can result in significant speed-up - more than x3 faster compared with CPU-only execution. Here are the instructions for generating a Core ML model and using it with  whisper.cpp : Install Python dependencies needed for the creation of the Core ML model: pip install ane_transformers pip install openai-whisper pip install coremltools To ensure  coremltools  operates correctly, please confirm that Xcode is installed and execute  xcode-select --install  to install the command-line tools. Python 3.11 is recommended. MacOS Sonoma (version 14) or newer is recommended, as older versions of MacOS might experience issues with transcription hallucination."
      },
      {
        "source_id": "4b47235d-662b-4853-adeb-f4e863c3cd53",
        "citation_number": 19,
        "cited_text": "Activity Custom properties Stars 48.2k stars Watchers 365 watching Forks 5.4k forks Report repository Releases  32 v1.8.4    Latest  Mar 19, 2026 + 31 releases Packages  0 Uh oh! There was an error while loading. Please reload this page . Uh oh! There was an error while loading. Please reload this page . Contributors Uh oh! There was an error while loading. Please reload this page . Languages C++   53.6% C   22.9% Cuda   10.4% Metal   3.1% GLSL   2.0% CMake   1.4% Other   6.6% You can’t perform that action at this time."
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 20,
        "cited_text": "Distil-Whisper [Paper] [Models] [Colab] [Training Code] Distil-Whisper is a distilled version of Whisper for English speech recognition that is 6 times faster , 49% smaller, and performs within 1% word error rate (WER) on out-of-distribution evaluation sets: Model   Params / M   Rel. Latency ↑   Short-Form WER ↓   Long-Form WER ↓ large-v3 1550   1.0 8.4 11.0 distil-large-v3 756   6.3   9.7 10.8 distil-large-v2 756   5.8   10.1   11.6 distil-medium.en 394 6.8 11.1   12.4 distil-small.en 166 5.6   12.1   12.8"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 21,
        "cited_text": "Speculative Decoding Distil-Whisper can be used as an assistant model to Whisper for speculative decoding . Speculative decoding mathematically ensures the exact same outputs as Whisper are obtained while being 2 times faster. This makes it the perfect drop-in replacement for existing Whisper pipelines, since the same outputs are guaranteed. For speculative decoding, we need to load both the teacher: openai/whisper-large-v3 . As well as the assistant ( a.k.a student) distil-whisper/distil-large-v3 . Let's start by loading the teacher model and processor. We do this in much the same way we loaded the Distil-Whisper model in the previous examples:"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 22,
        "cited_text": "from   datasets   import   load_dataset   dataset   =   load_dataset ( \"hf-internal-testing/librispeech_asr_dummy\" ,  \"clean\" ,  split = \"validation\" )  sample   =   dataset [ 0 ][ \"audio\" ]  result   =   pipe ( sample )  print ( result [ \"text\" ]) Note: speculative decoding should be on average 2x faster than using \"only\" Whisper large-v2 at a mere 8% increase in VRAM memory usage while mathematically ensuring the same results. This makes it the perfect replacement for Whisper large-v2 in existing speech recognition pipelines."
      },
      {
        "source_id": "d689a9f5-058d-40ac-a249-2fad6764f90e",
        "citation_number": 23,
        "cited_text": "For  gpt-4o-transcribe  and  gpt-4o-mini-transcribe , you can use the  prompt  parameter to improve the quality of the transcription by giving the model additional context similarly to how you would prompt other GPT-4o models. Prompting is not currently available for  gpt-4o-transcribe-diarize . Here are some examples of how prompting can help in different scenarios: Prompts can help correct specific words or acronyms that the model misrecognizes in the audio. For example, the following prompt improves the transcription of the words DALL·E and GPT-3, which were previously written as “GDP 3” and “DALI”: “The transcript is about OpenAI which makes technology like DALL·E, GPT-3, and ChatGPT with the hope of one day building an AGI system that benefits all of humanity.” To preserve the context of a file that was split into segments, prompt the model with the transcript of the preceding segment. The model uses relevant information from the previous audio, improving transcription accuracy. The  whisper-1  model only considers the final 224 tokens of the prompt and ignores anything earlier. For multilingual inputs, Whisper uses a custom tokenizer. For English-only inputs, it uses the standard GPT-2 tokenizer. Find both tokenizers in the open source Whisper Python package . Sometimes the model skips punctuation in the transcript. To prevent this, use a simple prompt that includes punctuation: “Hello, welcome to my lecture.” The model may also leave out common filler words in the audio. If you want to keep the filler words in your transcript, use a prompt that contains them: “Umm, let me think like, hmm… Okay, here’s what I’m, like, thinking.” Some languages can be written in different ways, such as simplified or traditional Chinese. The model might not always use the writing style that you want for your transcript by default. You can improve this by using a prompt in your preferred writing style."
      },
      {
        "source_id": "d689a9f5-058d-40ac-a249-2fad6764f90e",
        "citation_number": 24,
        "cited_text": "The first method involves using the optional prompt parameter to pass a dictionary of the correct spellings. Because it wasn’t trained with instruction-following techniques, Whisper operates more like a base GPT model. Keep in mind that Whisper only considers the first 224 tokens of the prompt. Prompt parameter python 1  2  3  4  5  6  7  8  9  10  11  12  13  import  fs  from   \"fs\" ;  import  OpenAI  from   \"openai\" ;  const  openai =  new  OpenAI();  const  transcription =  await  openai.audio.transcriptions.create({  file : fs.createReadStream( \"/path/to/file/speech.mp3\" ),  model :  \"whisper-1\" ,  response_format :  \"text\" ,  prompt : \"ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T.\" ,  });  console .log(transcription.text); 1  2  3  4  5  6  7  8  9  10  11  12  13  from  openai  import  OpenAI  client = OpenAI()  audio_file =  open ( \"/path/to/file/speech.mp3\" ,  \"rb\" )  transcription = client.audio.transcriptions.create(   model= \"whisper-1\" ,   file=audio_file,   response_format= \"text\" ,   prompt= \"ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T.\"   )  print (transcription.text) 1  2  3  4  5  6  7  curl --request POST \\   --url https://api.openai.com/v1/audio/transcriptions \\   --header  \"Authorization: Bearer  $OPENAI_API_KEY \"  \\   --header  'Content-Type: multipart/form-data'  \\   --form file=@/path/to/file/speech.mp3 \\   --form model=whisper-1 \\   --form prompt= \"ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T.\""
      },
      {
        "source_id": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
        "citation_number": 25,
        "cited_text": "Word-level timestamps segments ,  _   =   model . transcribe ( \"audio.mp3\" ,  word_timestamps = True )  for   segment   in   segments :  for   word   in   segment . words :  print ( \"[%.2fs -> %.2fs] %s\"   %  ( word . start ,  word . end ,  word . word )) VAD filter The library integrates the Silero VAD model to filter out parts of the audio without speech: segments ,  _   =   model . transcribe ( \"audio.mp3\" ,  vad_filter = True ) The default behavior is conservative and only removes silence longer than 2 seconds. See the available VAD parameters and default values in the source code . They can be customized with the dictionary argument  vad_parameters :"
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 26,
        "cited_text": "Voice Activity Detection (VAD) Support for Voice Activity Detection (VAD) can be enabled using the  --vad  argument to  whisper-cli . In addition to this option a VAD model is also required. The way this works is that first the audio samples are passed through the VAD model which will detect speech segments. Using this information, only the speech segments that are detected are extracted from the original audio input and passed to whisper for processing. This reduces the amount of audio data that needs to be processed by whisper and can significantly speed up the transcription process."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 27,
        "cited_text": "Size   Layers   Width   Heads   Parameters   English-only   Multilingual   tiny   4   384   6   39 M ✓ ✓ base   6   512   8   74 M ✓ ✓ small   12   768   12   244 M ✓ ✓ medium   24   1024   16   769 M ✓ ✓ large   32   1280   20   1550 M   x ✓ large-v2   32   1280   20   1550 M   x ✓ large-v3   32   1280   20   1550 M   x ✓ For demonstration purposes, we'll fine-tune the multilingual version of the small checkpoint with 244M params (~= 1GB). As for our data, we'll train and evaluate our system on a low-resource language taken from the Common Voice dataset. We'll show that with as little as 8 hours of fine-tuning data, we can achieve strong performance in this language."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 28,
        "cited_text": "Our best WER is 32.0% after 4000 training steps. For reference, the pre-trained Whisper  small  model achieves a WER of 63.5%, meaning we achieve an improvement of 31.5% absolute through fine-tuning. Not bad for just 8h of training data! We're now ready to share our fine-tuned model on the Hugging Face Hub. To make it more accessible with appropriate tags and README information, we can set the appropriate key-word arguments (kwargs) when we push. You can change these values to match your dataset, language and model name accordingly:"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 29,
        "cited_text": "It is crucial that we match the sampling rate of our audio inputs to the sampling rate expected by our model, as audio signals with different sampling rates have very different distributions. Audio samples should only ever be processed with the correct sampling rate. Failing to do so can lead to unexpected results! For instance, taking an audio sample with a sampling rate of 16kHz and listening to it with a sampling rate of 8kHz will make the audio sound as though it's in half-speed. In the same way, passing audio with the wrong sampling rate can falter an ASR model that expects one sampling rate and receives another. The Whisper feature extractor expects audio inputs with a sampling rate of 16kHz, so we need to match our inputs to this value. We don't want to inadvertently train an ASR system on slow-motion speech!"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 30,
        "cited_text": "We can see that we've got a 1-dimensional input audio array and the corresponding target transcription. We've spoken heavily about the importance of the sampling rate and the fact that we need to match the sampling rate of our audio to that of the Whisper model (16kHz). Since our input audio is sampled at 48kHz, we need to downsample it to 16kHz before passing it to the Whisper feature extractor. We'll set the audio inputs to the correct sampling rate using dataset's cast_column method. This operation does not change the audio in-place, but rather signals to  datasets  to resample audio samples on the fly the first time that they are loaded:"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 31,
        "cited_text": "Sequential Long-Form The latest distil-large-v3 checkpoint is specifically designed to be compatible with OpenAI's sequential long-form transcription algorithm. This algorithm uses a sliding window for buffered inference of long audio files (> 30-seconds), and returns more accurate transcriptions compared to the chunked long-form algorithm . The sequential long-form algorithm should be used in either of the following scenarios: Transcription accuracy is the most important factor, and latency is less of a consideration You are transcribing batches of long audio files, in which case the latency of sequential is comparable to chunked, while being up to 0.5% WER more accurate"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 32,
        "cited_text": "To enable chunking, pass the  chunk_length_s  parameter to the  pipeline . For distil-large-v3, a chunk length of 25-seconds is optimal. To activate batching, pass the argument  batch_size : pipe   =   pipeline (  \"automatic-speech-recognition\" ,  model = model ,  tokenizer = processor . tokenizer ,  feature_extractor = processor . feature_extractor ,  max_new_tokens = 128 ,  chunk_length_s = 25 ,  batch_size = 16 ,  torch_dtype = torch_dtype ,  device = device , ) The argument  max_new_tokens  controls the maximum number of generated tokens per-chunk . In the typical speech setting, we have no more than 3 words spoken per-second. Therefore, for a 30-second input, we have at most 90 words (approx 128 tokens). We set the maximum number of generated tokens per-chunk to 128 to truncate any possible hallucinations that occur at the end of the segment. These tokens get removed at the chunk borders using the long-form chunking transcription algorithm, so it is more efficient to truncate them directly during generation to avoid redundant generation steps in the decoder."
      },
      {
        "source_id": "24726456-5f36-471c-8e85-d7c18566f228",
        "citation_number": 33,
        "cited_text": "pipx install insanely-fast-whisper ⚠️  If you have python 3.11.XX installed,  pipx  may parse the version incorrectly and install a very old version of  insanely-fast-whisper  without telling you (version  0.0.8 , which won't work anymore with the current  BetterTransformers ). In that case, you can install the latest version by passing  --ignore-requires-python  to  pip : pipx install insanely-fast-whisper --force --pip-args= \" --ignore-requires-python \" If you're installing with  pip , you can pass the argument directly:  pip install insanely-fast-whisper --ignore-requires-python ."
      },
      {
        "source_id": "24726456-5f36-471c-8e85-d7c18566f228",
        "citation_number": 34,
        "cited_text": "Frequently Asked Questions How to correctly install flash-attn to make it work with  insanely-fast-whisper ? Make sure to install it via  pipx runpip insanely-fast-whisper install flash-attn --no-build-isolation . Massive kudos to @li-yifei for helping with this. How to solve an  AssertionError: Torch not compiled with CUDA enabled  error on Windows? The root cause of this problem is still unknown, however, you can resolve this by manually installing torch in the virtualenv like  python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 . Thanks to @pto2k for all tdebugging this."
      },
      {
        "source_id": "24726456-5f36-471c-8e85-d7c18566f228",
        "citation_number": 35,
        "cited_text": "How to avoid Out-Of-Memory (OOM) exceptions on Mac? The mps backend isn't as optimised as CUDA, hence is way more memory hungry. Typically you can run with  --batch-size 4  without any issues (should use roughly 12GB GPU VRAM). Don't forget to set  --device-id mps . How to use Whisper without a CLI? All you need to run is the below snippet:   pip install --upgrade transformers optimum accelerate  import   torch   from   transformers   import   pipeline   from   transformers . utils   import   is_flash_attn_2_available   pipe   =   pipeline (  \"automatic-speech-recognition\" ,  model = \"openai/whisper-large-v3\" ,  # select checkpoint from https://huggingface.co/openai/whisper-large-v3#model-details   torch_dtype = torch . float16 ,  device = \"cuda:0\" ,  # or mps for Mac devices   model_kwargs = { \"attn_implementation\" :  \"flash_attention_2\" }  if   is_flash_attn_2_available ()  else  { \"attn_implementation\" :  \"sdpa\" }, )  outputs   =   pipe (  \"<FILE_NAME>\" ,  chunk_length_s = 30 ,  batch_size = 24 ,  return_timestamps = True , )  outputs"
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 36,
        "cited_text": "LBolitho Feb 5, 2025 Thanks for this, it's really awesome. Would it be possible to fine-tune this model to listen for a particular sound (like a frog call)? I have done this with the wav2vec model and had fairly good results but always looking to improve. Cheers, Liam liam.bolitho@gmail.com · 2sl Feb 19, 2025 Hey! Did you figure it out? It seems quite interesting! Athrensis Feb 8, 2025 This comment has been hidden rajdev1 Feb 10, 2025 hi xiayq Apr 21, 2025 I using this code find ASR improved, but LID is deceased. I want to fintune ASR and LID at the same time. How to do it?"
      }
    ]
  }
}

## 前沿趋势

{
  "value": {
    "answer": "根据提供的来源，关于「Whisper 深度解析：多语言 ASR 的工程实践」领域的最新研究突破（涵盖 2025-2026 年趋势）、未解决挑战及未来方向的解析如下：\n\n### 1. 2025-2026 年重要技术突破与论文趋势\n\n*   **模型架构的极限优化 (Whisper Turbo & Distil-Whisper)**：\n    *   **Whisper Turbo**：OpenAI 推出的 `turbo` 版本是 `large-v3` 的优化版，在保持极高准确度的同时，推理速度提升了约 **8 倍** [1]。\n    *   **知识蒸馏 (Distil-Whisper)**：Sanchit Gandhi 等人的研究（2023年提交，2025年广泛应用）通过伪标签技术将 Whisper 蒸馏为更小模型。其 `distil-large-v3` 在参数减少 50% 的情况下，推理速度提升 **6 倍**，且 WER（词错误率）损失控制在 1% 以内 [2, 3]。\n*   **投机解码 (Speculative Decoding)**：\n    *   这是一种数学上保证输出一致性的加速方案。通过使用 `Distil-Whisper` 作为助手模型预测草稿，再由 `Whisper-large-v3` 进行验证，可在不损失任何精度的前提下实现 **2 倍的推理加速** [4, 5]。\n*   **硬件感知的工程实现**：\n    *   **Flash Attention 2**：集成至 `insanely-fast-whisper` 等项目，使 150 分钟音频的转录时间缩短至 **98 秒** 以内 [6]。\n    *   **专用芯片推理 (LPU)**：Groq 等厂商通过专门为推理设计的 LPU 架构，实现比传统 GPU 快 **7.41 倍** 的速度，并大幅降低成本 [7, 8]。\n    *   **端侧优化 (whisper.cpp)**：截至 2026 年 3 月，`whisper.cpp` 已演进至 v1.8.4，支持 Apple Neural Engine (Core ML) 加速，使 iPhone 13 等设备能完全离线运行 ASR，且编码器性能提升 **3 倍** [9-11]。\n\n### 2. 未解决的挑战\n\n*   **低资源语言的精度鸿沟**：\n    *   尽管 Whisper 支持 96 种语言，但性能差异巨大。工业标准通常只认可 WER 低于 50% 的语言，而许多极低资源语言仍无法达到此标准 [12, 13]。\n*   **长音频的“幻觉”与上下文丢失**：\n    *   Whisper 采用 30 秒滑动窗口，处理长音频时易产生重复或虚假内容的“幻觉” [3]。虽然 Distil-Whisper 有所缓解，但在极端声学条件下，如何保持长程一致性仍是难题 [3]。\n*   **多任务微调的副作用**：\n    *   开发者反馈在对特定语言进行 ASR 微调后，模型的 **LID (语种识别)** 能力可能会下降，难以兼顾所有任务的性能 [14]。\n*   **实时流式的复杂性**：\n    *   标准 Whisper 是非流式的，实现“准实时”转录需要复杂的滑动窗口缓冲策略 [15]。\n\n### 3. 未来可能的突破点与发展方向\n\n*   **从“语音转文本”到“语音理解” (Speech-to-Understanding)**：\n    *   未来的方向不仅是转录，而是直接提取语义。例如 AssemblyAI 的 **Universal-3** 模型已开始集成提示词 (Prompting)、说话人角色识别 (Speaker Roles) 和情感分析，使模型具备类似 LLM 的理解能力 [16-18]。\n*   **深度融合 (Deep Fusion) 与端到端多模态**：\n    *   利用 Transformer 的编码器-解码器特性，将语言模型更紧密地集成在系统内部（而非外部浅层融合），以获得更强的跨领域泛化能力 [19]。\n*   **上下文感知提示 (Context-aware Prompting)**：\n    *   利用前一段落的转录文本作为当前窗口的 `prompt`，可大幅修正专有名词和缩写（如将 \"DALI\" 修正为 \"DALL·E\"）[20]。\n*   **医疗与行业特化模型**：\n    *   针对特定领域（如医疗术语、法律记录）进行专用的准确度优化和非言语事件标识（如 [beep] 声识别）将成为工程落地的重点 [16, 21]。",
    "conversation_id": "ef4b3f56-d848-4548-a89c-d09edf73dd71",
    "sources_used": [
      "633960af-000b-4429-bbdb-11ef34edf441",
      "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "2101e08e-4d7e-47f3-aad5-d94ddc170884",
      "24726456-5f36-471c-8e85-d7c18566f228",
      "c84ffb6e-2203-475e-a691-e005d6b0df59",
      "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "238aa703-f8b9-4b60-91e8-b088f06cf90e"
    ],
    "citations": {
      "1": "633960af-000b-4429-bbdb-11ef34edf441",
      "2": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "3": "2101e08e-4d7e-47f3-aad5-d94ddc170884",
      "4": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "5": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
      "6": "24726456-5f36-471c-8e85-d7c18566f228",
      "7": "c84ffb6e-2203-475e-a691-e005d6b0df59",
      "8": "c84ffb6e-2203-475e-a691-e005d6b0df59",
      "9": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "10": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "11": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
      "12": "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "13": "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "14": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "15": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
      "16": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "17": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "18": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
      "19": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
      "20": "d689a9f5-058d-40ac-a249-2fad6764f90e",
      "21": "238aa703-f8b9-4b60-91e8-b088f06cf90e"
    },
    "references": [
      {
        "source_id": "633960af-000b-4429-bbdb-11ef34edf441",
        "citation_number": 1,
        "cited_text": "Size   Parameters   English-only model   Multilingual model   Required VRAM   Relative speed   tiny   39 M   tiny.en   tiny   ~1 GB   ~10x   base   74 M   base.en   base   ~1 GB   ~7x   small   244 M   small.en   small   ~2 GB   ~4x   medium   769 M   medium.en   medium   ~5 GB   ~2x   large   1550 M   N/A   large   ~10 GB   1x   turbo   809 M   N/A   turbo   ~6 GB   ~8x The  .en  models for English-only applications tend to perform better, especially for the  tiny.en  and  base.en  models. We observed that the difference becomes less significant for the  small.en  and  medium.en  models. Additionally, the  turbo  model is an optimized version of  large-v3  that offers faster transcription speed with a minimal degradation in accuracy."
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 2,
        "cited_text": "Distil-Whisper [Paper] [Models] [Colab] [Training Code] Distil-Whisper is a distilled version of Whisper for English speech recognition that is 6 times faster , 49% smaller, and performs within 1% word error rate (WER) on out-of-distribution evaluation sets: Model   Params / M   Rel. Latency ↑   Short-Form WER ↓   Long-Form WER ↓ large-v3 1550   1.0 8.4 11.0 distil-large-v3 756   6.3   9.7 10.8 distil-large-v2 756   5.8   10.1   11.6 distil-medium.en 394 6.8 11.1   12.4 distil-small.en 166 5.6   12.1   12.8"
      },
      {
        "source_id": "2101e08e-4d7e-47f3-aad5-d94ddc170884",
        "citation_number": 3,
        "cited_text": "Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs >  arXiv:2311.00430 Help | Advanced Search Computer Science > Computation and Language arXiv:2311.00430 (cs)   [Submitted on 1 Nov 2023] Title: Distil-Whisper: Robust Knowledge Distillation via Large-Scale Pseudo Labelling Authors: Sanchit Gandhi , Patrick von Platen , Alexander M. Rush View a PDF of the paper titled Distil-Whisper: Robust Knowledge Distillation via Large-Scale Pseudo Labelling, by Sanchit Gandhi and 2 other authors View PDF Abstract: As the size of pre-trained speech recognition models increases, running these large models in low-latency or resource-constrained environments becomes challenging. In this work, we leverage pseudo-labelling to assemble a large-scale open-source dataset which we use to distill the Whisper model into a smaller variant, called Distil-Whisper. Using a simple word error rate (WER) heuristic, we select only the highest quality pseudo-labels for training. The distilled model is 5.8 times faster with 51% fewer parameters, while performing to within 1% WER on out-of-distribution test data in a zero-shot transfer setting. Distil-Whisper maintains the robustness of the Whisper model to difficult acoustic conditions, while being less prone to hallucination errors on long-form audio. Distil-Whisper is designed to be paired with Whisper for speculative decoding, yielding a 2 times speed-up while mathematically ensuring the same outputs as the original model. To facilitate further research in this domain, we make our training code, inference code and models publicly accessible.  Comments:   30 pages, 2 figures, 25 tables   Subjects:   Computation and Language (cs.CL) ; Sound (cs.SD); Audio and Speech Processing (eess.AS)   Cite as: arXiv:2311.00430 [cs.CL]   (or arXiv:2311.00430v1 [cs.CL]  for this version) https://doi.org/10.48550/arXiv.2311.00430 arXiv-issued DOI via DataCite"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 4,
        "cited_text": "Speculative Decoding Distil-Whisper can be used as an assistant model to Whisper for speculative decoding . Speculative decoding mathematically ensures the exact same outputs as Whisper are obtained while being 2 times faster. This makes it the perfect drop-in replacement for existing Whisper pipelines, since the same outputs are guaranteed. For speculative decoding, we need to load both the teacher: openai/whisper-large-v3 . As well as the assistant ( a.k.a student) distil-whisper/distil-large-v3 . Let's start by loading the teacher model and processor. We do this in much the same way we loaded the Distil-Whisper model in the previous examples:"
      },
      {
        "source_id": "ccddf948-8637-4c9e-ae51-9ff827b31b72",
        "citation_number": 5,
        "cited_text": "from   datasets   import   load_dataset   dataset   =   load_dataset ( \"hf-internal-testing/librispeech_asr_dummy\" ,  \"clean\" ,  split = \"validation\" )  sample   =   dataset [ 0 ][ \"audio\" ]  result   =   pipe ( sample )  print ( result [ \"text\" ]) Note: speculative decoding should be on average 2x faster than using \"only\" Whisper large-v2 at a mere 8% increase in VRAM memory usage while mathematically ensuring the same results. This makes it the perfect replacement for Whisper large-v2 in existing speech recognition pipelines."
      },
      {
        "source_id": "24726456-5f36-471c-8e85-d7c18566f228",
        "citation_number": 6,
        "cited_text": "Insanely Fast Whisper An opinionated CLI to transcribe Audio files w/ Whisper on-device! Powered by 🤗 Transformers , Optimum & flash-attn TL;DR - Transcribe 150 minutes (2.5 hours) of audio in less than 98 seconds - with OpenAI's Whisper Large v3 . Blazingly fast transcription is now a reality!⚡️ pipx install insanely-fast-whisper==0.0.15 --force Not convinced? Here are some benchmarks we ran on a Nvidia A100 - 80GB 👇 Optimisation type   Time to Transcribe (150 mins of Audio)   large-v3 (Transformers) ( fp32 )   ~31 ( 31 min 1 sec )   large-v3 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~5 ( 5 min 2 sec ) large-v3 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~2 ( 1 min 38 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  bettertransformer )   ~3 ( 3 min 16 sec ) distil-large-v2 (Transformers) ( fp16  +  batching [24]  +  Flash Attention 2 ) ~1 ( 1 min 18 sec ) large-v2 (Faster Whisper) ( fp16  +  beam_size [1] )   ~9.23 ( 9 min 23 sec )   large-v2 (Faster Whisper) ( 8-bit  +  beam_size [1] )   ~8 ( 8 min 15 sec )"
      },
      {
        "source_id": "c84ffb6e-2203-475e-a691-e005d6b0df59",
        "citation_number": 7,
        "cited_text": "Get Started Speed at a winning cost The McLaren F1 Team chooses Groq for inference globally. The Groq LPU LPU built for inference, exceptional speed and affordability at scale. 3m developers and teams Born for this. Literally. To deliver different results, you need a different stack. Others rely on GPUs alone. Our edge? Custom silicon. Groq pioneered the LPU in 2016, the first chip purpose-built for inference. Every design choice focuses on keeping intelligence fast and affordable. Learn More Benchmarks don’t ship. Workloads do."
      },
      {
        "source_id": "c84ffb6e-2203-475e-a691-e005d6b0df59",
        "citation_number": 8,
        "cited_text": "The McLaren Formula 1 Team chooses Groq for inference. The McLaren F1 Team is fueled by decision-making, analysis, development and real-time insights. So the McLaren F1 Team chose Groq. Read More Don’t take our word for it. Proof from the people shipping. Read Customer Stories If we have things where performance matters more, we come to Groq - you deliver real, working solutions, not just buzzwords. We optimized our infrastructure to its limits – but the breakthrough came with GroqCloud. Overnight, our chat speed surged 7.41x while costs fell by 89%. I was stunned. So, we tripled our token consumption. We simply can’t get enough."
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 9,
        "cited_text": "Supported platforms: Mac OS (Intel and Arm) iOS Android Java Linux / FreeBSD WebAssembly Windows ( MSVC and MinGW ) Raspberry Pi Docker The entire high-level implementation of the model is contained in whisper.h and whisper.cpp . The rest of the code is part of the ggml machine learning library. Having such a lightweight implementation of the model allows to easily integrate it in different platforms and applications. As an example, here is a video of running the model on an iPhone 13 device - fully offline, on-device: whisper.objc"
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 10,
        "cited_text": "Core ML support On Apple Silicon devices, the Encoder inference can be executed on the Apple Neural Engine (ANE) via Core ML. This can result in significant speed-up - more than x3 faster compared with CPU-only execution. Here are the instructions for generating a Core ML model and using it with  whisper.cpp : Install Python dependencies needed for the creation of the Core ML model: pip install ane_transformers pip install openai-whisper pip install coremltools To ensure  coremltools  operates correctly, please confirm that Xcode is installed and execute  xcode-select --install  to install the command-line tools. Python 3.11 is recommended. MacOS Sonoma (version 14) or newer is recommended, as older versions of MacOS might experience issues with transcription hallucination."
      },
      {
        "source_id": "702efcb3-8c4d-45f0-947b-ebfbcdc00c31",
        "citation_number": 11,
        "cited_text": "Activity Custom properties Stars 48.2k stars Watchers 365 watching Forks 5.4k forks Report repository Releases  32 v1.8.4    Latest  Mar 19, 2026 + 31 releases Packages  0 Uh oh! There was an error while loading. Please reload this page . Uh oh! There was an error while loading. Please reload this page . Contributors Uh oh! There was an error while loading. Please reload this page . Languages C++   53.6% C   22.9% Cuda   10.4% Metal   3.1% GLSL   2.0% CMake   1.4% Other   6.6% You can’t perform that action at this time."
      },
      {
        "source_id": "d689a9f5-058d-40ac-a249-2fad6764f90e",
        "citation_number": 12,
        "cited_text": "In this case, the inputted audio was german and the outputted text looks like: Hello, my name is Wolfgang and I come from Germany. Where are you heading today? We only support translation into English at this time. Supported languages We currently support the following languages through both the  transcriptions  and  translations  endpoint: Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh."
      },
      {
        "source_id": "d689a9f5-058d-40ac-a249-2fad6764f90e",
        "citation_number": 13,
        "cited_text": "While the underlying model was trained on 98 languages, we only list the languages that exceeded <50% word error rate (WER) which is an industry standard benchmark for speech to text model accuracy. The model will return results for languages not listed above but the quality will be low. We support some ISO 639-1 and 639-3 language codes for GPT-4o based models. For language codes we don’t have, try prompting for specific languages (i.e., “Output in English”). Timestamps By default, the Transcriptions API will output a transcript of the provided audio in text. The timestamp_granularities[]  parameter enables a more structured and timestamped json output format, with timestamps at the segment, word level, or both. This enables word-level precision for transcripts and video edits, which allows for the removal of specific frames tied to individual words."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 14,
        "cited_text": "LBolitho Feb 5, 2025 Thanks for this, it's really awesome. Would it be possible to fine-tune this model to listen for a particular sound (like a frog call)? I have done this with the wav2vec model and had fairly good results but always looking to improve. Cheers, Liam liam.bolitho@gmail.com · 2sl Feb 19, 2025 Hey! Did you figure it out? It seems quite interesting! Athrensis Feb 8, 2025 This comment has been hidden rajdev1 Feb 10, 2025 hi xiayq Apr 21, 2025 I using this code find ASR improved, but LID is deceased. I want to fintune ASR and LID at the same time. How to do it?"
      },
      {
        "source_id": "9a64e529-ab73-48ea-b053-2b0eec8f9fcb",
        "citation_number": 15,
        "cited_text": "speaches is an OpenAI compatible server using  faster-whisper . It's easily deployable with Docker, works with OpenAI SDKs/CLI, supports streaming, and live transcription. WhisperX is an award-winning Python library that offers speaker diarization and accurate word-level timestamps using wav2vec2 alignment whisper-ctranslate2 is a command line client based on faster-whisper and compatible with the original client from openai/whisper. whisper-diarize is a speaker diarization tool that is based on faster-whisper and NVIDIA NeMo. whisper-standalone-win Standalone CLI executables of faster-whisper for Windows, Linux & macOS. asr-sd-pipeline provides a scalable, modular, end to end multi-speaker speech to text solution implemented using AzureML pipelines. Open-Lyrics is a Python library that transcribes voice files using faster-whisper, and translates/polishes the resulting text into  .lrc  files in the desired language using OpenAI-GPT. wscribe is a flexible transcript generation tool supporting faster-whisper, it can export word level transcript and the exported transcript then can be edited with wscribe-editor aTrain is a graphical user interface implementation of faster-whisper developed at the BANDAS-Center at the University of Graz for transcription and diarization in Windows ( Windows Store App ) and Linux. Whisper-Streaming implements real-time mode for offline Whisper-like speech-to-text models with faster-whisper as the most recommended back-end. It implements a streaming policy with self-adaptive latency based on the actual source complexity, and demonstrates the state of the art. WhisperLive is a nearly-live implementation of OpenAI's Whisper which uses faster-whisper as the backend to transcribe audio in real-time. Faster-Whisper-Transcriber is a simple but reliable voice transcriber that provides a user-friendly interface. Open-dubbing is open dubbing is an AI dubbing system which uses machine learning models to automatically translate and synchronize audio dialogue into different languages. Whisper-FastAPI whisper-fastapi is a very simple script that provides an API backend compatible with OpenAI, HomeAssistant, and Konele (Android voice typing) formats."
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 16,
        "cited_text": "AssemblyAI Documentation: Real-time Transcription LiveKit SDK: Building Voice Agents Voice Agent Best Practices Guide Introducing Medical Mode: Purpose-built accuracy for medical terminology Learn more Speech-to-Text Streaming Speech-to-Text Speech Understanding LLM Gateway Guardrails Speech-to-Speech Product overview Deployment Self-Hosted Voice AI Cloud Use Cases Conversation Intelligence Medical Transcription Contact Centers Voice Agents AI Notetakers Customers Zoom leverages AssemblyAI to help advance its AI research and development. Read the story Siro achieves a 90% Reduction in customer complaints and support tickets. \n Watch the video Developers   Documentation API Reference Cookbooks Support Quick Links Status Changelog Discord Resources   Blog Partners Research Benchmarks Security Introducing Universal-3 Pro Streaming Universal-3 Pro Streaming brings prompting, disfluency control, code-switching, real-time diarization, and 99+ language support to real-time use cases Playground Pricing Enterprise Contact us Log in Get started The best way to build Voice AI apps"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 17,
        "cited_text": "Speaker A : 5Mg. And do you take it regularly? \n ‍ \n Speaker B : Oh yeah, yeah. \n ‍ \n Speaker A : Good. \n ‍ \n Speaker B : Every evening. \n ‍ \n Speaker A : And no side effects with it? With speaker labels prompting Speaker [Nurse] : 5Mg. And do you take it regularly? \n ‍ \n Speaker [Patient] : Oh yeah, yeah. \n ‍ \n Speaker [Nurse] : Good. \n ‍ \n Speaker [Patient] : Every evening. \n ‍ \n Speaker [Nurse] : And no side effects with it? Source Spanish and english audio: 00:00 01:59   \"language_detection\": True \n \"prompt\": Preserve natural code-switching between English and Spanish. Retain spokenlanguage as-is (correct \"I was hablando con mi manager\"). Without codeswitching"
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 18,
        "cited_text": "industry-leading accuracy Avoid garbage in, garbage out Your product experience is only as good as the inputs it’s built on. AssemblyAI’s models lead the industry in accuracy and reliability. Industry’s lowest Word Error Rate (WER) Up to 30% less hallucinations than other providers Preferred by 73% of end users in unbiased evaluations Explore our latest model CAPABILITIES Go beyond transcription Access a full suite of speech understanding capabilities to uncover insights, identify speakers, and build powerful product experiences."
      },
      {
        "source_id": "391d2de4-b3c4-426f-bb1a-4ad8a535777f",
        "citation_number": 19,
        "cited_text": "Figure 1: Whisper model. The architecture follows the standard Transformer-based encoder-decoder model. A log-Mel spectrogram is input to the encoder. The last encoder hidden states are input to the decoder via cross-attention mechanisms. The decoder autoregressively predicts text tokens, jointly conditional on the encoder hidden states and previously predicted tokens. Figure source: OpenAI Whisper Blog . In a sequence-to-sequence model, the encoder transforms the audio inputs into a set of hidden state representations, extracting important features from the spoken speech. The decoder plays the role of a language model, processing the hidden state representations and generating the corresponding text transcriptions. Incorporating a language model internally in the system architecture is termed deep fusion . This is in contrast to shallow fusion , where a language model is combined externally with an encoder, such as with CTC +  n n n -gram ( c.f. Internal Language Model Estimation ). With deep fusion, the entire system can be trained end-to-end with the same training data and loss function, giving greater flexibility and generally superior performance ( c.f. ESB Benchmark )."
      },
      {
        "source_id": "d689a9f5-058d-40ac-a249-2fad6764f90e",
        "citation_number": 20,
        "cited_text": "For  gpt-4o-transcribe  and  gpt-4o-mini-transcribe , you can use the  prompt  parameter to improve the quality of the transcription by giving the model additional context similarly to how you would prompt other GPT-4o models. Prompting is not currently available for  gpt-4o-transcribe-diarize . Here are some examples of how prompting can help in different scenarios: Prompts can help correct specific words or acronyms that the model misrecognizes in the audio. For example, the following prompt improves the transcription of the words DALL·E and GPT-3, which were previously written as “GDP 3” and “DALI”: “The transcript is about OpenAI which makes technology like DALL·E, GPT-3, and ChatGPT with the hope of one day building an AGI system that benefits all of humanity.” To preserve the context of a file that was split into segments, prompt the model with the transcript of the preceding segment. The model uses relevant information from the previous audio, improving transcription accuracy. The  whisper-1  model only considers the final 224 tokens of the prompt and ignores anything earlier. For multilingual inputs, Whisper uses a custom tokenizer. For English-only inputs, it uses the standard GPT-2 tokenizer. Find both tokenizers in the open source Whisper Python package . Sometimes the model skips punctuation in the transcript. To prevent this, use a simple prompt that includes punctuation: “Hello, welcome to my lecture.” The model may also leave out common filler words in the audio. If you want to keep the filler words in your transcript, use a prompt that contains them: “Umm, let me think like, hmm… Okay, here’s what I’m, like, thinking.” Some languages can be written in different ways, such as simplified or traditional Chinese. The model might not always use the writing style that you want for your transcript by default. You can improve this by using a prompt in your preferred writing style."
      },
      {
        "source_id": "238aa703-f8b9-4b60-91e8-b088f06cf90e",
        "citation_number": 21,
        "cited_text": "Source Non-speech audio event: 00:00 01:59   \"prompt\": \"Produce a transcript suitable for conversational analysis. Every disfluency is meaningful data. Include: Tag sounds: [beep]\" Without audio tagging \"Your call has been forwarded to an automatic voice message system. At the tone, please record your message. When you have finished recording, you may hang up or press 1 for more options.\" With audio tagging \"Your call has been forwarded to an automatic voice message system. At the tone, please record your message. When you have finished recording, you may hang up or press 1 for more options.  [beep] \""
      }
    ]
  }
}
