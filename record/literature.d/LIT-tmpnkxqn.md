---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmpfe486) from the arXiv PDF, v1: the abstract,
  §1, §2.1–2.2, §3.1–3.2, §4.2 and §7; §2.3–2.6, §4.1, §4.3, §5 and the
  appendices skimmed or skipped, and the figures not seen. Worth reading
  here as the token-level counterpart of Yue et al.'s sharpening reading
  (LIT-tmpfmva5): RLVR changes few next-token distributions, mostly by
  reallocating mass among tokens the base model already ranks, and the
  accuracy gap between base and RL models sits at those few positions.
title: 'Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on what RL
    post-training changes at the token level. Citation checked on the arXiv
    API: Haoming Meng, Kexin Huang, Shaohang Wei, Chiyu Ma, Shuo Yang, Xue
    Wang, Guoyin Wang, Bolin Ding and Jingren Zhou; the PDF's byline reads
    "Qwen Pilot Team, Alibaba Group", and the work is cited by first
    author. v1 submitted 2026-03-23, the only version, which is
    `published:` and the copy read. The arXiv comment and the PDF footnote
    ("Published at ICLR 2026") give the venue, bearing out A's "ICLR
    2026"; OpenReview was not checked. OpenAlex and Semantic Scholar both
    refused with HTTP 429 and were not retried. No email address was sent
    to any service. The record held no LIT for this work.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2026-03-23'
arxiv: '2603.22446'
first_author: 'Meng'
keywords:
- 'RLVR'
- 'token-level analysis'
- 'distributional shift'
- 'Jensen-Shannon divergence'
- 'cross-sampling'
- 'divergence-weighted advantage'
implementations: []
summary: >-
  Meng et al. (2026), arXiv:2603.22446, ICLR 2026. RLVR fine-tuning of
  Qwen2.5-32B leaves most next-token distributions nearly unchanged (over
  83% of positions under DAPO, over 98% under SimpleRL). Sampling the RL
  model's token only at the highest-divergence positions, a few percent of
  tokens, lifts the base model to RL-level AIME accuracy, and sampling the
  base model's token there drops the RL model to base level. RLVR "rarely
  elevates tokens that were highly unlikely in the base model". Here as
  the token-level support for Yue et al.'s sharpening (LIT-tmpfmva5),
  bearing on QUESTION-392. Its account is THEORY-tmpr8g5y.
---
<!-- inactive-ok-file: THEORY-tmpr8g5y — Proposed; new entries filed in the same contribution -->

# LIT-tmpnkxqn: Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs

Meng, H., Huang, K., Wei, S., Ma, C., Yang, S., Wang, X., Wang, G., Ding,
B. & Zhou, J. (2026). Sparse but Critical: A Token-Level Analysis of
Distributional Shifts in RLVR Fine-Tuning of LLMs. *International
Conference on Learning Representations* (ICLR 2026). arXiv:2603.22446.

## Key takeaways

*From the reading, NOTE-tmpfe486.*

- **Sparse shift** (§2.2): "Under DAPO, more than 83% of token positions
  exhibit near-zero divergence, while this proportion exceeds 98% under
  SimpleRL."
- **Critical positions** (§3.2): with the base model primary, "Injecting
  fewer than 4% RL-sampled tokens per sequence on average, corresponding to
  fewer than 40 effective token substitutions per response, is sufficient
  to close the performance gap from the base model (approximately 8%) to
  the RL model (approximately 25%)" (SimpleRL, AIME 2024). In reverse,
  reverting about 5% of high-divergence positions collapses the RL model to
  base level.
- **Selection, not invention** (§4.2, §7): RLVR "rarely elevates tokens that
  were highly unlikely in the base model", refining behaviour "by
  reallocating probability mass within an existing candidate set".

## Standing in the record

A's characterization holds: sparse token-distribution shifts, and a small
fraction of token choices that can transfer or erase much of the gap. The
reader's verdict adds that the fraction is not arbitrary: it is the
positions where the two models' distributions diverge most, above a
threshold. "Much of" understates it: the paper reports full recovery and
full collapse on AIME at about 4–10% of tokens, though for DAPO that is
some 280 tokens per response, not 40. The paper states neither the
KL-regularized optimum nor 1 − (1 − p)^N. Its divergence-weighted
advantage (§5, not read) is ML practice and belongs to the anthology
(ADR-048); hence the flag.
