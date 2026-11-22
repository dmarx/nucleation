---
status: Proposed
title: "The radial monotonicity of transitive entailment cones, applied to per-item cones between model generations, shows that cone-constrained updates make embeddings more certain whatever their correctness, so supports the rule that a narrower region counts as progress only while it stays correct"
version: 1
form: formal-application
rests_on:
- CLAIM-tmpxcy5s
grounds:
- THEORY-189
- THEORY-tmpe9367
concludes:
- CLAIM-839
tags:
- representation-learning
- mathematics
date: '2026-11-22'
line:
- learned-structure
summary: >-
  [CLAIM-839](../claims.d/CLAIM-839.md) ends with A33's rule that "a network could become more
  confident without becoming more correct", so a narrower region counts
  as progress only while it stays correct. [CLAIM-tmpxcy5s](../claims.d/CLAIM-tmpxcy5s.md) shows a working
  case: in Bui et al.'s scheme every satisfied cone constraint raises the
  item's norm and lowers its norm-based uncertainty, whether or not the
  update is right. So the cone term by itself cannot certify progress,
  and correctness has to come from elsewhere, as it does there, from the
  classification loss and retrieval. Supports that clause of the claim,
  not its thesis. Proposed. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-839 CLAIM-tmpxcy5s THEORY-tmpe9367 — Proposed; the claim, the derivation and the reading this argument joins -->

# ARG-tmpotmon: The radial monotonicity of transitive entailment cones, applied to per-item cones between model generations, shows that cone-constrained updates make embeddings more certain whatever their correctness, so supports the rule that a narrower region counts as progress only while it stays correct

## The inference

Premise: [CLAIM-tmpxcy5s](../claims.d/CLAIM-tmpxcy5s.md) (from [THEORY-189](../theory.d/THEORY-189.md)'s radial monotonicity and Bui et
al.'s Eq. 11, [THEORY-tmpe9367](../theory.d/THEORY-tmpe9367.md)): a point inside a cone of the widest
transitive family is farther from the origin than its apex. Conclusion:
[CLAIM-839](../claims.d/CLAIM-839.md)'s clause "a narrower region counts as progress only while it
stays correct".

## Critical questions (formal application)

**Do the premise's conditions hold in the case?** For embeddings that
satisfy their constraint, and with half-apertures at most π/2, which
Bui's arcsin gives. Bui's penalty is soft, so the case holds to the extent
the constraint is met.

**Does the formal result say what the conclusion needs?** It says that
narrowing, here a radius that grows and an aperture that shrinks with it,
is forced by the constraint and independent of correctness. That is an
instance of "more confident without becoming more correct" by
construction: a measure of narrowing cannot, alone, measure progress.

**Does it say more than the clause?** No. It does not show that progress
is a branching partial order, nor anything about Blackwell
informativeness. It supports the clause, not the thesis.

## Verdict

Supports [CLAIM-839](../claims.d/CLAIM-839.md)'s correctness clause with a demonstrated case.
