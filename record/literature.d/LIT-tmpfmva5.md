---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmp4mog9) from the arXiv PDF, v5: the abstract,
  §1, §2, the §3 math results, the §4.1 summary, the perplexity analysis,
  §4.2 (distillation), §4.4 briefly, the KL and entropy ablations and §7;
  the code and visual-reasoning results, §5 and the appendices skimmed.
  Worth reading here as the measured case of one intervention moving
  reliability and reachability in opposite directions: RLVR raises pass@1
  and lowers pass@k at large k. It is the source of the sharpening dispute
  whose agentic extension the record already holds (LIT-2441, LIT-2414).
title: 'Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on RL
    post-training as sharpening. Citation checked on the arXiv API: Yang
    Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji
    Song and Gao Huang (the first and sixth authors share an English name);
    v1 submitted 2025-04-18, which is `published:`; v5 (2025-11-24) is the
    copy read. The arXiv journal-ref gives "NeurIPS 2025 Oral; ICML 2025
    AI4MATH workshop best paper", which bears out A's "NeurIPS 2025".
    OpenAlex and Semantic Scholar both refused with HTTP 429 and were not
    retried. No email address was sent to any service. The record held no
    LIT for this work.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2025-04-18'
arxiv: '2504.13837'
first_author: 'Yue'
keywords:
- 'reinforcement learning with verifiable rewards'
- 'RLVR'
- 'pass@k'
- 'reasoning capability boundary'
- 'sampling efficiency'
- 'distillation'
implementations: []
summary: >-
  Yue et al. (2025), arXiv:2504.13837, NeurIPS 2025. RLVR-trained models
  beat their base models in pass@k at small k and are overtaken by them as
  k grows, across model families, RL algorithms and math, code and visual
  benchmarks; the RL models' reasoning paths are already likely under the
  base model, and distillation from a stronger teacher lifts pass@k at
  every k. The authors read RLVR as sharpening within the base model's
  prior. Here for CLAIM-567 and QUESTION-392, and as the single-turn source
  of the dispute held in its agentic form (LIT-2441, THEORY-1703,
  THEORY-1672). Contested by ProRL (LIT-tmp7463t). Its account is
  THEORY-tmp9rnyv.
---
<!-- inactive-ok-file: THEORY-tmp9rnyv — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: THEORY-1703 THEORY-1672 — Proposed; the agentic extension of this dispute -->

# LIT-tmpfmva5: Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

Yue, Y., Chen, Z., Lu, R., Zhao, A., Wang, Z., Yue, Y., Song, S. & Huang,
G. (2025). Does Reinforcement Learning Really Incentivize Reasoning
Capacity in LLMs Beyond the Base Model? *Advances in Neural Information
Processing Systems* (NeurIPS 2025, oral). arXiv:2504.13837.

## Key takeaways

*From the reading, NOTE-tmp4mog9.*

- **The crossover** (abstract): "while RLVR-trained models outperform their
  base models at smaller values of k (e.g., k=1), base models achieve
  higher pass@k score when k is large." And "the reasoning capability
  boundary of LLMs often narrows as RLVR training progresses."
- **The reading** (§4.1): "RLVR mainly sharpens the distribution within the
  base model's prior rather than expanding beyond it." The gain in average
  scores "stems from more efficient sampling on these already solvable
  problems".
- **The contrast** (§4.2): a distilled model's pass@k curve "is
  consistently and significantly above" the base model's.
- **Not only entropy**: raising the RL model's temperature to the base
  model's entropy still leaves it below; "it alone does not fully account
  for the reduction."

## Standing in the record

A's characterization holds and is slightly weaker than the paper, which
says base models "consistently catch up to and eventually surpass"
RL-trained models across its benchmarks. A's "distribution sharpening" is
the paper's own word. The reader's verdict: A should not attribute the
KL-regularized optimum π* ∝ π0 exp(r/β) to this paper. It does not state
it, and most of its RL runs drop the KL term; of the works in this batch
only Balasubramanian and Kasiviswanathan (LIT-tmpdyhv5) state it.

ProRL (LIT-tmp7463t) contests the paper's conclusion; the two differ in
start model, training length and k, and ProRL agrees on math. Meng et al.
(LIT-tmpnkxqn) support the sharpening reading at the token level. Its
training conclusions are ML practice and belong to the anthology
(ADR-048); hence the flag.
