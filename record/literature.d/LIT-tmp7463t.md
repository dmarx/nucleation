---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmppn4n4) from the arXiv PDF, v1: the abstract,
  §1, §2.2–2.3, the §3 headline results, §4.1–4.3, the opening of §4.4,
  §6 and App. A; the appendix figures, per-task plots and training details
  skipped. Worth reading here as the counterclaim to Yue et al.
  (LIT-tmpfmva5): long RL with diversity-preserving choices raises pass@k,
  including from zero on some tasks, which is the test of whether RL ever
  changes what is reachable and not only what is affordable. Its start
  model is already a distilled reasoning model, its k is mostly at most
  128, and it reports narrowing on math, agreeing with Yue there.
title: 'ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on whether
    prolonged RL expands reasoning boundaries. Citation checked on the
    arXiv API: Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong,
    Yejin Choi, Jan Kautz and Yi Dong (NVIDIA); v1 submitted 2025-05-30,
    which is `published:` and the copy read. The PDF says "Preprint. Under
    review." and the arXiv record has no journal-ref; any later venue is
    unverified, since OpenAlex and Semantic Scholar both refused with HTTP
    429 and were not retried. No email address was sent to any service.
    The record held no LIT for this work.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2025-05-30'
arxiv: '2505.24864'
first_author: 'Liu'
keywords:
- 'prolonged reinforcement learning'
- 'reasoning boundaries'
- 'entropy collapse'
- 'KL divergence control'
- 'reference policy reset'
- 'pass@k'
- 'creativity index'
implementations:
- https://huggingface.co/nvidia/Nemotron-Research-Reasoning-Qwen-1.5B
summary: >-
  Liu et al. (2025), arXiv:2505.24864. Over 2,000 steps of RL on a diverse
  136K-problem suite, with DAPO's decoupled clipping and dynamic sampling,
  a KL penalty and periodic hard resets of the reference policy, raise
  DeepSeek-R1-Distill-Qwen-1.5B's pass@k on many tasks, including some
  where the start model solved nothing; gains are largest where the start
  model's pass@128 was lowest and nil or negative on math. Contests Yue et
  al. (LIT-tmpfmva5). Here for CLAIM-576 and QUESTION-392 as the test case
  of RL changing what is possible rather than what is affordable, and
  beside the agentic dispute (LIT-2441, LIT-2414). Its account is
  THEORY-tmpxu3kz.
---
<!-- inactive-ok-file: THEORY-tmpxu3kz — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 — Proposed; the claim this work is a test case for -->

# LIT-tmp7463t: ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models

Liu, M., Diao, S., Lu, X., Hu, J., Dong, X., Choi, Y., Kautz, J. & Dong, Y.
(2025). ProRL: Prolonged Reinforcement Learning Expands Reasoning
Boundaries in Large Language Models. arXiv preprint arXiv:2505.24864.

## Key takeaways

*From the reading, NOTE-tmppn4n4.*

- **The claim** (abstract): "prolonged RL (ProRL) training can uncover
  novel reasoning strategies that are inaccessible to base models, even
  under extensive sampling", including "scenarios where base models fail
  entirely regardless of the number of attempts."
- **The diagnosis of the contrary result** (§1): "an overreliance on
  specialized domains like mathematics" and "premature termination of RL
  training", "typically no more than hundreds of steps".
- **Where it expands** (§4.1): "a significant negative correlation between
  the base model's reasoning boundary and the extent of reasoning
  improvement after RL"; where the base is strong, gains are "minimal or
  even negative", "a narrowing of the reasoning boundary".
- **Agreement on math** (§4.2): there the final model shows "decreased or
  unchanged reasoning capacity compared to the base model, aligning with
  observations of prior work".

## Standing in the record

A's characterization holds as the authors' claim: prolonged RL with
diversity-promoting choices improves high-budget coverage and finds
strategies not seen from base models under extensive sampling. The
reader's verdict names three qualifiers A omits. The "base" is
DeepSeek-R1-Distill-Qwen-1.5B, a distilled reasoning model, not a
pretrained base. "Extensive" sampling is pass@k up to 128 in the parts
read, not Yue et al.'s 1024. And the paper itself reports narrowed
boundaries on math. It uses a KL penalty but resets the reference policy,
so the closed-form tilt π* ∝ π0 exp(r/β) has no fixed π0 here, and the
paper does not state it. Its bound on E[pass@k] (Eq. 5) is Dang et al.'s,
not A's 1 − (1 − p)^N.

So it does not straightforwardly conflict with Yue et al.: different
start, length, tasks and k, and agreement on math. Its training recipe is
ML practice and belongs to the anthology (ADR-048); hence the flag.
