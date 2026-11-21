---
status: Proposed
title: 'Hoogland and colleagues'' stages, read off plateaus of the local learning coefficient in two small transformers, ground the weak half of reading (b) of the owner''s suggestion on singularities, that stages of development leave their mark in local learning coefficients, and not its strong half, that stages are switches of the dominant singular region; the coefficient''s decreases qualify both'
version: 1
form: source
grounds:
- THEORY-tmpr9w2r
concludes:
- CLAIM-823
tags:
- learning-theory
- loss-landscapes
date: '2026-11-21'
line:
- learned-structure
summary: >-
  [CLAIM-823](../claims.d/CLAIM-823.md) cited Hoogland et al. ([LIT-2966](../literature.d/LIT-2966.md)) unread, as reporting
  stagewise changes in the coefficient. Read ([NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md)), the paper
  supports that half for two small transformers, leaves the switch of
  dominant singular region untested, and documents three decreases its
  motivating account does not produce ([QUESTION-tmphkb1w](../questions.d/QUESTION-tmphkb1w.md)). The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-823 THEORY-tmpr9w2r CLAIM-812 — Proposed or new; the claim this argues on and the reading it rests on -->

# ARG-tmpfh555: Hoogland and colleagues' stages, read off plateaus of the local learning coefficient in two small transformers, ground the weak half of reading (b) of the owner's suggestion on singularities, that stages of development leave their mark in local learning coefficients, and not its strong half, that stages are switches of the dominant singular region; the coefficient's decreases qualify both

## The inference

[CLAIM-823](../claims.d/CLAIM-823.md) says, on reading (b), that the stages of representational
development are switches of the dominant singular region, "or at least
leave their mark in local learning coefficients", and cites Hoogland and
colleagues as reporting stagewise changes in the coefficient. The reading
([THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)) is offered as ground for both halves.

## Critical questions

- **Does the work say this, read in context?** For the weak half, yes:
  "these changes in degeneracy coincide with significant changes in the
  internal computational structure and the input/output behavior of the
  transformers" (abstract), with boundaries recurring across seeds (B.4).
  For the strong half, no. The singular learning process is an analogy
  ("an analogy to the singular learning process informs our methodology
  for stage division", §2), its link to training "remains to be
  understood" (§5), and the authors never say a stage is a change of
  dominant singularity.
- **Is it said within the scope the claim needs?** Narrowly: two small
  transformers, one run each in depth, one fixed nβ and γ per setting.
  The claim is general.
- **Does the claim lean on the reading for more than it holds?** It would,
  for the strong half. And three stages are decreases of the coefficient
  (LM3, LR3, LR4), which a crossover to a richer, higher-λ region does not
  produce: the example transitions "describe LLC increases", and a full
  account "is an open problem" (§8). A decrease at equal loss lowers the
  free energy too (§8), so the competition picture can be extended to
  cover it, but neither the paper nor the claim does so.

## Verdict

Grounds the weak half, in two small models. Leaves the strong half
untested. The decreases are a datum the claim must place, put as
[QUESTION-tmphkb1w](../questions.d/QUESTION-tmphkb1w.md). A measurement caution applies as well: at the paper's
settings a rise in the estimate could be directions stiffening past the
estimator's cut-off ([CLAIM-812](../claims.d/CLAIM-812.md)), which the fixed nβ and γ cannot exclude.
