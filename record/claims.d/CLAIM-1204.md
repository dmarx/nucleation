---
number: 1204
status: Proposed
formerly:
- CLAIM-tmpzi0ri
title: 'Counting states at binding predicts assembly'
statement: >-
  In a kinetic constraint-growth system, counting the states each component
  could still take when it first reaches the binding threshold, under
  deterministic growth from the seed set, predicts the chance of exact
  assembly and flags the seed additions that lower it on architectures it
  was not designed on, where island-based predictors do not; its flags are
  weak, and its transfer is across architectures of one system, not across
  systems
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23 from the executed study
    CASE-389. The predictor was designed after the registered test
    failed and was pre-registered, in the study's second amendment, before
    the architectures it was tested on were generated.
role: thesis
warrant: empirical
defeated_if: >-
  An error in the code or the analysis of CASE-389; or a rerun of the
  model on further fresh architectures, at the registered parameters, in
  which threshold-front forcing fails the registered criterion of transfer
  (AUC at least 0.7, recall at least 0.5, and a rank correlation with V no
  more than 0.05 below the best monotone baseline's). Not defeated by its
  failure in another system, which the claim does not assert, nor by its
  low precision, which it states.
tags:
- complex-systems
- probabilistic-modeling
- mathematics
date: '2026-11-23'
line:
- realizability
- formal-apparatus
grounds:
- CASE-389
complements:
- CLAIM-969
bears_on:
- QUESTION-380
summary: >-
  Threshold-front forcing (TFF) grows the seed set deterministically in
  rounds, taking every component bound with at least the threshold
  strength, and scores −Σ log k_v over the states k_v each could take at
  that moment. On five architectures generated only after it was
  registered, it meets the criterion VIC failed: rank correlation with V
  0.64 against the best monotone 0.48, AUC 0.94, recall 0.66. Its
  precision is 0.11: flagged additions lower V by 0.011 on average, 55 %
  of them at all. It uses the growth rule's threshold as well as the
  constraints. It answers [QUESTION-380](../questions.d/QUESTION-380.md) for one system only, since it was
  built on that system. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-389 — new; the executed study this claim is grounded in, filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-969 — Proposed; the committor claim this complements -->
<!-- inactive-ok-file: CLAIM-1205 — new; the claim on the failed predictor, filed by the lead run of 2026-11-23 -->

# CLAIM-1204: Counting states at binding predicts assembly

## The claim

The island-based predictors fail in [CASE-389](../cases.d/CASE-389.md) because what decides a
component's state is the set of states still open when it first becomes
bound strongly enough to attach, and a seed changes that order
([CLAIM-1205](CLAIM-1205.md)). Threshold-front forcing (TFF) scores a seed set by that
quantity directly:

- grow from S in synchronous rounds; in each round every unset component
  bound to set ones with strength at least τ is a candidate (if none, every
  touched component is);
- record each candidate's number k_v of states compatible with its set
  neighbours at that moment, then set every candidate to its target;
- TFF(S) = −Σ log k_v, the log chance of the target if each such choice
  were uniform.

On five architectures generated after it was registered, TFF's rank
correlation with V is 0.64 (best monotone baseline 0.48), the AUC for
telling significant falls from significant rises by its change is 0.94,
and it flags 25 of 38 significant falls. Of its 236 flags most are small
or no falls: flagged additions change V by −0.011 on average, unflagged by
+0.023.

## Relations

- **[CLAIM-969](CLAIM-969.md)** (complements). The committor scores intermediates by their
  future and so can rank a small nucleus above a larger trap, but it needs
  the whole chain solved. TFF is a surrogate computed from the architecture
  and the growth rule's threshold without solving the dynamics, for seed
  sets rather than intermediates.

## What it does not say

- That it transfers across systems: it was designed on this one's
  failures. A test in another system, such as one with coherent
  alternative branches, is what [QUESTION-380](../questions.d/QUESTION-380.md) still lacks.
- That it is computed from the constraints alone. The threshold is a
  condition of the dynamics.
- That its flags are reliable one by one.
