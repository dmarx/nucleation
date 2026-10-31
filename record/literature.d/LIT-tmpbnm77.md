---
status: Active
status_note: >-
  read in full 2026-10-31 ([NOTE-tmpuemsh](../notes.d/NOTE-tmpuemsh.md)); worth reading as the
  published statement of the forward-KL limit on distilling from a
  better-informed teacher, with its entropy consequence
  ([THEORY-tmpfm1ma](../theory.d/THEORY-tmpfm1ma.md)), and for the finding that such supervision helps
  only where it is imitable ([THEORY-tmpjz0xp](../theory.d/THEORY-tmpjz0xp.md)). The trained objective
  clips each entry and is not a forward KL.
title: 'Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A16 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2026-09-29). A16 said it treats the forward-KL projection
    explicitly; that could not be confirmed from the abstract. The
    summary follows the abstract and the exchange's description; a
    reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 2609.37915v1, 19 pp., in
    NOTE-tmpuemsh; status Deferred → Active. The citation stands. The
    summary is rewritten from the text. A16's statement is confirmed:
    Proposition 1 gives the mixture optimum and the conditional mutual
    information as irreducible loss. The authors say it does not exactly
    describe the clipped objective they train. THEORY-tmpfm1ma and
    THEORY-tmpjz0xp filed. The anthology-candidate flag stays.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-31'
published: '2026-09-29'
arxiv: '2609.37915'
first_author: 'Hossain'
keywords:
- 'self-distillation'
- 'on-policy distillation'
- 'imitation gap'
- 'LLM reasoning'
- 'privileged information'
implementations: []
summary: >-
  Hossain, Kousar & Tourni (2026). In on-policy self-distillation the
  frozen initial model, given a reference solution, teaches the student
  along the student's own rollouts. Under forward KL the best student is
  that teacher averaged over the contexts the student cannot see, with
  the conditional mutual information as irreducible loss and higher
  entropy (Proposition 1). The teacher's advantage lies mostly on failed
  trajectories, where standard OPSD puts about 70% of its supervision,
  and is smaller at 4B than at 1.7B. OASIS supervises only verified
  rollouts and gives the teacher the student's own failed attempt in
  place of the reference. It keeps a 3.2–3.8-point gain over the base
  model on AIME and HMMT from Qwen3-1.7B to 8B, where OPSD's gain falls
  to 0.14, in single runs.
---
<!-- inactive-ok-file: QUESTION-tmp4b001 THEORY-tmpjz0xp — Open or Proposed; the question this work was filed for and an account it supports, cited as open -->

# LIT-tmpbnm77: Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning

Hossain, M. I., Kousar, H., & Tourni, I. C. (2026). Overcoming scaling limits in on-policy self-distillation for LLM reasoning. arXiv:2609.37915.

Read in full in [NOTE-tmpuemsh](../notes.d/NOTE-tmpuemsh.md).

## Why this is here

A16 used it for the "privileged teacher" case of self-distillation: what the teacher knows and the student cannot see is averaged away, which is the limit [QUESTION-tmp4b001](../questions.d/QUESTION-tmp4b001.md) starts from. The reading confirms that the paper states this limit ([THEORY-tmpfm1ma](../theory.d/THEORY-tmpfm1ma.md)) and adds its consequence: supervision where the teacher's advantage is privileged makes the student less certain, and the useful supervision is on states the student can already reach ([THEORY-tmpjz0xp](../theory.d/THEORY-tmpjz0xp.md)). Two qualifications. The teacher is the frozen initial model, not the evolving one. And the objective actually trained is a per-entry clipped KL, not the forward KL the proposition is about.
