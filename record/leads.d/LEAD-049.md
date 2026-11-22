---
number: 49
status: Open
formerly:
- LEAD-tmp89oxs
title: 'Prove a restricted theorem for a population of adaptive operators: sufficient conditions, for symmetric competitive interactions and bounded niche adaptation, for a locally stable differentiated equilibrium in which every specialist can reinvade'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: the restricted theorem is proved
    (CLAIM-tmp6kclm), a counterexample to recovery against re-adapted
    residents filed (CLAIM-tmpdsv4t), and both checked numerically
    (CASE-tmp5sk3q). Status and stage are unchanged; marking the lead
    Done is the owner's call.
stage: idea
priority: high
method:
- formal
tags:
- complex-systems
- ecology
- self-governance
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-132
- QUESTION-133
- QUESTION-135
operationalized_in:
- CASE-tmp5sk3q
summary: >-
  [QUESTION-132](../questions.d/QUESTION-132.md) names it as the natural first target. Named in
  [QUESTION-132](../questions.d/QUESTION-132.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-tmp6kclm CLAIM-tmpdsv4t CASE-tmp5sk3q — Proposed, filed 2026-11-22 by this lead's work and cited in the note of that date -->

# LEAD-049: Prove a restricted theorem for a population of adaptive operators: sufficient conditions, for symmetric competitive interactions and bounded niche adaptation, for a locally stable differentiated equilibrium in which every specialist can reinvade

## What it would do

State the model class, then derive sufficient conditions for local
asymptotic stability of a differentiated equilibrium and positive invasion
growth of each specialist when rare.

Where the record names it:

- [QUESTION-132](../questions.d/QUESTION-132.md): "A restricted theorem would be a natural first target. For
  symmetric competitive interactions and bounded niche adaptation, find
  sufficient conditions under which a differentiated equilibrium is locally
  asymptotically stable and every active specialist has positive growth when
  reintroduced"

## What would count

A theorem answers [QUESTION-132](../questions.d/QUESTION-132.md) for its class and fixes what the population
study must measure. A counterexample within the class shows that
differentiation needs more than competition and bounded adaptation.

## Note of 2026-11-22: carried out

**The model class.** The lead left it open. The choice was [CLAIM-369](../claims.d/CLAIM-369.md)'s
symmetric resource competition (A = UᵀU with u ≥ 0, r = Uᵀb − c), with
each operator's niche vector set by a trait confined to a box and moved
up the rare-mutant selection gradient. It is the smallest addition to a
class the record already holds, it keeps [CLAIM-369](../claims.d/CLAIM-369.md)'s potential, and one
scalar trait suffices for both a theorem and a counterexample.

**What was proved** ([CLAIM-tmp6kclm](../claims.d/CLAIM-tmp6kclm.md), demonstrated).

- (A) Sufficient conditions for local exponential stability of a
  differentiated equilibrium: traits interior and stationary or held at a
  bound by a strictly outward gradient, and a positive definite Hessian of
  L on the free coordinates. This requires linearly independent niche
  vectors.
- (B) Recovery when rare against frozen residents: λ_i ≥ n*_i d_i² > 0,
  with d_i the niche vector's distance from the span of the others'.
- (C) The same rate against re-adapted residents, when the frozen −i
  community itself meets (A).

**The counterexample** ([CLAIM-tmpdsv4t](../claims.d/CLAIM-tmpdsv4t.md), demonstrated). In a two-resource
trade-off, a stable specialist pair coexists with a stable lone
generalist, against which a removed specialist has negative growth. So
the "What would count" counterexample is to recovery once residents
re-adapt, not to differentiation itself.

**The numerical study** ([CASE-tmp5sk3q](../cases.d/CASE-tmp5sk3q.md), scratch/studies/lead-049/) checks
all three theorems and the counterexample.

**What remains.** The steps [QUESTION-132](../questions.d/QUESTION-132.md) names after the restricted
theorem: asymmetric interactions, delayed adaptation ([THEORY-548](../theory.d/THEORY-548.md)),
influence-dependent training ([QUESTION-134](../questions.d/QUESTION-134.md)), invasion graphs with
adaptive traits, and a trainable returning specialist. Whether the lone
generalist is the question's third outcome or a further one is the
owner's to decide.

Status and stage are unchanged. Marking the lead Done is the owner's
call.
