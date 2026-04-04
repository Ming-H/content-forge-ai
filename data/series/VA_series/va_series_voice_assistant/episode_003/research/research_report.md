# 调研报告

当前流式 ASR 的工业实践已确立以 Conformer 结合 Transducer 架构为核心，通过分块注意力机制和先进的 VAD 策略来实现低延迟识别。开源社区中，WeNet 和 Sherpa-ONNX 提供了从训练到高性能部署的完整工具链，极大地降低了实现 <200ms 实时系统的门槛。然而，未来趋势正指向更高效的架构如 Zipformer 和 E-Branchformer，以及无状态解码策略，旨在进一步消除延迟并降低计算成本。