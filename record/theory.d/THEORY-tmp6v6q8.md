---
status: Proposed
promote_when: >-
  A second reading confirms, from §§4–5 and §7, the parity with full fine-tuning on the reported benchmarks, the storage and latency claims, and the finding that the update correlates with and amplifies under-emphasized directions of the pretrained weights.
title: 'Adapting a large pretrained Transformer by freezing its weights and training only a low-rank additive update to selected weight matrices matches full fine-tuning on the language benchmarks reported, stores about 10,000 times less per task on GPT-3, adds no inference latency once the update is merged, and yields an update that amplifies directions already present, but not emphasized, in the specific pretrained weights it modifies'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed Proposed from NOTE-tmpz29f3, a reading of LIT-tmp5b18b.
tags:
- representation-learning
date: '2026-11-12'
source:
- LIT-tmp5b18b
bears_on:
- QUESTION-095
summary: >-
  Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang and Weizhu Chen (2021), LIT-tmp5b18b, read in NOTE-tmpz29f3. arXiv preprint; no venue on the arXiv record (cited elsewhere as ICLR, not checked).
---

# THEORY-tmp6v6q8: Adapting a large pretrained Transformer by freezing its weights and training only a low-rank additive update to selected weight matrices matches full fine-tuning on the language benchmarks reported, stores about 10,000 times less per task on GPT-3, adds no inference latency once the update is merged, and yields an update that amplifies directions already present, but not emphasized, in the specific pretrained weights it modifies

## Source

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang and Weizhu Chen (2021), "LoRA: Low-Rank Adaptation of Large Language Models", LIT-tmp5b18b, read in NOTE-tmpz29f3
from arXiv v2 (2106.09685, 16 October 2021; v1 of 17 June 2021).

## What was shown

- **The method.** Abstract: LoRA "freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture"; unlike adapters, "no additional inference latency".
- **One base, many modules.** §1: "A pre-trained model can be shared and used to build many small LoRA modules for different tasks."
- **The module is a delta on one W0.** §4.1: to switch tasks "we can recover W0 by subtracting BA and then adding a different B′A′". §7.3: "ΔW amplifies some features that are already in W".
- **Base-model turnover, as motivation.** §1: "As larger models are trained every few months", full fine-tuning becomes a deployment problem.

## What it does not show

Language models only; no study of carrying a module across base models or versions.
