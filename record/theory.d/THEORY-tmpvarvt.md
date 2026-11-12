---
status: Proposed
promote_when: >-
  A second reading confirms, from Table 1 and §4.1, the personalization times, the CLIP-I, DINO and face-similarity ranking of the five methods, and the stated training budget.
title: 'A tuning-free personalization model for SDXL, trained once on an ID-grouped dataset for two weeks on 8 A100s, stacks embeddings of several photos of one person in place of the class word and personalizes in about 10 s on a V100, against 1284 s for DreamBooth and 2400 s for Textual Inversion, with the highest CLIP-I and DINO of the five methods compared and face similarity second to IP-Adapter''s'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed Proposed from NOTE-tmpul1vj, a reading of LIT-tmp8l2rx.
tags:
- representation-learning
date: '2026-11-12'
source:
- LIT-tmp8l2rx
corroborates:
- CLAIM-tmpnwq8a
bears_on:
- QUESTION-095
summary: >-
  Zhen Li, Mingdeng Cao, Xintao Wang, Zhongang Qi, Ming-Ming Cheng and Ying Shan (2023), [LIT-tmp8l2rx](../literature.d/LIT-tmp8l2rx.md), read in [NOTE-tmpul1vj](../notes.d/NOTE-tmpul1vj.md). technical report (arXiv comment: "Tech report").
---

# THEORY-tmpvarvt: A tuning-free personalization model for SDXL, trained once on an ID-grouped dataset for two weeks on 8 A100s, stacks embeddings of several photos of one person in place of the class word and personalizes in about 10 s on a V100, against 1284 s for DreamBooth and 2400 s for Textual Inversion, with the highest CLIP-I and DINO of the five methods compared and face similarity second to IP-Adapter's

## Source

Zhen Li, Mingdeng Cao, Xintao Wang, Zhongang Qi, Ming-Ming Cheng and Ying Shan (2023), "PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding", [LIT-tmp8l2rx](../literature.d/LIT-tmp8l2rx.md), read in [NOTE-tmpul1vj](../notes.d/NOTE-tmpul1vj.md)
from arXiv v1 (2312.04461, 7 December 2023, the only version).

## What was shown

- **Method.** Abstract: it "encodes an arbitrary number of input ID images into a stack ID embedding"; §3.2 also trains "the LoRA [2, 25] residuals" of the attention layers, so the module is itself tied to SDXL.
- **Table 1** (25 IDs, 40 prompts; speed "on a single NVIDIA Tesla V100 GPU"):

  | method | CLIP-T | CLIP-I | DINO | Face Sim. | Speed (s) |
  |---|---:|---:|---:|---:|---:|
  | DreamBooth | 29.8 | 62.8 | 39.8 | 49.8 | 1284 |
  | Textual Inversion | 24.0 | 70.9 | 39.3 | 54.3 | 2400 |
  | FastComposer | 28.7 | 66.8 | 40.2 | 61.0 | 8 |
  | IP-Adapter | 25.1 | 71.2 | 46.2 | 67.1 | 12 |
  | PhotoMaker | 26.1 | 73.6 | 51.5 | 61.8 | 10 |

- **A discrepancy.** §4.2 says PhotoMaker has "the largest CLIP-T and DINO scores, and the second best Face Similarity". By Table 1 the largest CLIP-T is DreamBooth's (29.8 against 26.1); PhotoMaker has the largest CLIP-I and DINO. The record cites the table.
- **The maker's cost.** §4.1: trained on "8 NVIDIA A100 GPUs for two weeks with a batch size of 48".
- **The tuned route's human cost.** §1: data for fine-tuning "each time requires manual collection".

## What it does not show

Authors' own benchmark and baselines; DreamBooth's configuration on SDXL is not described. Text and table disagree on CLIP-T.
