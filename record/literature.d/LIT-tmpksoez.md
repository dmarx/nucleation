---
status: Active
status_note: >-
  read in full 2026-10-29 (NOTE-tmp42yyb), from arXiv v1; worth reading as a convex way to make a transport cost depend on sets of assignments rather than single ones, and for its limits: the structure is supplied, only submodular interactions are tractable, and its own threshold cost is not submodular.
title: 'Structured Optimal Transport'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A6 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2017-12-17 (AISTATS
    2018, PMLR 84) (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from arXiv 1712.06199v1, the only arXiv version, with numerical checks (NOTE-tmp42yyb); THEORY-tmpdtrq6 filed. Citation unchanged. The summary is rewritten from the text. Two errors in the paper: the threshold function of eq. (12) is not concave, so the cost it defines is not submodular; and Lemma 3.1's "trivial" symmetry fails for one-sided group costs.
tags:
- mathematics
- anthology-candidate
date: '2026-10-29'
published: '2017-12-17'
arxiv: '1712.06199'
first_author: 'Alvarez-Melis'
keywords:
- 'optimal transport'
- 'nonlinear generalization'
- 'structured couplings'
- 'domain adaptation'
implementations: []
summary: >-
  Alvarez-Melis, Jaakkola & Jegelka (2017). Optimal transport whose cost is the Lovász extension of a submodular set function on source–target assignments, so that assignments made together, such as one labelled group sent to one region, can cost less than the sum of their parts. The problem stays convex and is a zero-sum game against cost matrices in the base polytope; it is ordinary OT when the set function is modular, and is solved by saddle-point mirror prox with Sinkhorn and base-polytope projections. The groups are supplied in advance. Single-run experiments on point matching, colour transfer, 100-sample digit adaptation and sentence similarity favour the structured couplings.
---

# LIT-tmpksoez: Structured Optimal Transport

Alvarez-Melis, D., Jaakkola, T. S., & Jegelka, S. (2018). Structured optimal transport. *AISTATS 2018*, PMLR 84, 1771–1780.

## Why this is here

A6, as exploratory: it would matter if pragmatic force rests on a configuration of cues (speaker role, form of address, a later commitment) and not on each cue alone, which is the ternary-structure worry of [QUESTION-283](../questions.d/QUESTION-283.md). The test would be behavioural prediction, not expressiveness.

The reading (NOTE-tmp42yyb) narrows the fit: SOT encodes structure among assignments between two objects, from groups fixed in advance and only of the grouping (submodular) kind; it cannot learn a ternary relation among cue values. A configuration of cues could enter only as a pre-set grouping whose joint mapping is cheaper.
