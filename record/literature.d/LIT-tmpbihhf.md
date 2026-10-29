---
status: Active
status_note: >-
  skimmed 2026-10-29 (NOTE-tmp4j67k) as the companion LIT-tmpr8qf7 cites
  for its premise. Worth keeping for its own statement that per-entity
  frame freedom is an inductive bias, and for the parsed-CLUTRR control in
  which forcing orthogonal transports costs 64.6 points out of
  distribution.
title: 'Relational Composition as Parallel Transport: What Per-Entity Frames Force in Attention'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed and skimmed the same day, from the exchange "Paper assessment",
    whose A1 cited its Table 5. arXiv API: 2610.34945, v1 submitted
    2026-10-26, which is `published:` (ADR-002); cs.LG, with cs.AI and
    cs.FL; 31 pp. Read from the arXiv PDF v1, extracted with
    `pdftotext -layout`.
tags:
- compositionality
- representation-learning
- mathematics
- anthology-candidate
date: '2026-10-29'
published: '2026-10-26'
arxiv: '2610.34945'
first_author: 'Sarkar'
keywords:
- 'per-entity frame freedom'
- 'parallel transport'
- 'attention'
- 'faithful representation'
- 'finite groups'
- 'Krohn–Rhodes'
implementations: []
summary: >-
  Sarkar, Mukherjee & Sato (2026), [ARXIV-2610.34945](https://arxiv.org/abs/2610.34945). Under
  per-entity O(d) frames, an invariant attention score depends on two
  entities only through norms and ⟨xᵢ, Tᵢⱼxⱼ⟩, and a transport computed
  from one vector per endpoint has rank at most one, so relations must be
  supplied. On parsed CLUTRR unconstrained transports score 0.848 out of
  distribution, a transformer 0.436, and orthogonal ones 0.202; on
  StepGame's commutative algebra rotations help. The paper calls the
  premise "a chosen inductive bias, not a consequence of fresh names".
---

# LIT-tmpbihhf: Relational Composition as Parallel Transport: What Per-Entity Frames Force in Attention

Sarkar, A., Mukherjee, A., & Sato, M. (2026). Relational composition as
parallel transport: What per-entity frames force in attention. Preprint.
[ARXIV-2610.34945](https://arxiv.org/abs/2610.34945)

## Key takeaways

- Per-entity frame freedom is adopted "as an inductive bias", and the
  paper says it is not derived (pp. 2, 12–13).
- Under it, invariant scores are ϕ(‖xᵢ‖, ‖xⱼ‖, ⟨xᵢ, Tᵢⱼxⱼ⟩) and equivariant
  messages lie in span{xᵢ, Tᵢⱼxⱼ} (Theorem 1). A covariant transport
  computed from the endpoints alone has rank at most the endpoints' rank
  (Theorem 2), so one vector per entity can never give an orthogonal
  transport: "relations must be supplied".
- Which transports a task needs is "decided by the algebra of its
  relations" (p. 3). Orthogonality helps on StepGame and costs 64.6 points
  on CLUTRR, where the paper's motivation is that a nonidentity idempotent
  has no invertible faithful representation (p. 9, App. B.4).
- With matched anchors B = QA, an orthogonal transport is identified only
  on the anchored subspace (p. 9).

## Standing in the record

It is the source of the premise that [LIT-tmpr8qf7](LIT-tmpr8qf7.md) calls "the task's", and
its own CLUTRR control is the plainest evidence that the premise is
task-relative. That bears on [CLAIM-098](../claims.d/CLAIM-098.md) and [CLAIM-035](../claims.d/CLAIM-035.md), which hold that
translation is generally not a group action. Only the parts named in
[NOTE-tmp4j67k](../notes.d/NOTE-tmp4j67k.md) were read. `anthology-candidate`, as for its companion.
