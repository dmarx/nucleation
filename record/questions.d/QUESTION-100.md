---
number: 100
status: Open
formerly:
- QUESTION-tmp8ixku
title: 'Beyond the linearization at symmetry, when does coupling interpretation-dependent retrieval to performance-dependent endorsement produce stable expertise, and when does it produce self-reinforcing interpretive capture?'
version: 3
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Split under ADR-049. When the linearized symmetric state is unstable,
    and whether independent scoring removes the instability, is
    QUESTION-241, Answered by CLAIM-330. This question is reworded
    to what is left: the nonlinear dynamics, and expertise against
    capture. Version 1's title lacked "Beyond the linearization at
    symmetry".
- version: 3
  date: '2026-10-26'
  note: >-
    A dated note added: a nonlinear fold with history dependence, and
    capture without fidelity in a population (CASE-162), neither of
    them CASE-092. The question is unchanged.
tags:
- self-governance
- complex-systems
date: '2026-10-15'
line: distributed-agency
refines:
- QUESTION-087
summary: >-
  A22 §8's question, from the owner's U22: connect retrieval-mediated anchoring
  to the record's formulation of a distributed agent as two dual canvases, meaning
  and influence ([CLAIM-285](../claims.d/CLAIM-285.md), [TERM-053](../terms.d/TERM-053.md)). [QUESTION-087](QUESTION-087.md) asks whether self-reproducing
  authority can be pathological by the organization's own standard. This names one
  mechanism by which it could become so.
answered_by:
- CLAIM-297
refined_by:
- QUESTION-117
- QUESTION-121
- QUESTION-253
- QUESTION-241
---
<!-- inactive-ok-file: CLAIM-275 CLAIM-276 CLAIM-277 CLAIM-278 CLAIM-281 CLAIM-285 CLAIM-297 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# QUESTION-100: Beyond the linearization at symmetry, when does coupling interpretation-dependent retrieval to performance-dependent endorsement produce stable expertise, and when does it produce self-reinforcing interpretive capture?

## Why it is a question

A22: "The current organization of meaning influences who receives
authority; the distribution of authority influences which meanings
become available next." If an operator's competence is judged by how
relevant its results are to the current interpretation, "the
interpretation influences the measure by which interpretive authority is
allocated", and "A process can appear competent partly because it
searches in the region the collective has already privileged."

The record's pieces are [CLAIM-275](../claims.d/CLAIM-275.md) (meaning, policy and influence
co-evolve), [CLAIM-277](../claims.d/CLAIM-277.md) (trust as the regularity of endorsement, with its
entrenchment loop), [CLAIM-282](../claims.d/CLAIM-282.md) (cycles recycle authority), [CLAIM-281](../claims.d/CLAIM-281.md)
(role-indexed endorsement as a counter-mechanism) and [CLAIM-276](../claims.d/CLAIM-276.md)
(coherence, fidelity and plurality are separate quantities). [CLAIM-297](../claims.d/CLAIM-297.md) is
the thesis.

An answer is [CASE-092](../cases.d/CASE-092.md) analysed: fixed points of the coupled dynamics, when
the symmetric state is unstable, and whether role-indexed or
independently scored endorsement removes the captured regime. A22: "these
outcomes are not guaranteed merely by writing coupled diffusion
equations." The answer is also what [CLAIM-278](../claims.d/CLAIM-278.md) asks of the operator
framework, an outcome it forbids.

**Split, 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).** The linear part is [QUESTION-241](QUESTION-241.md),
Answered by [CLAIM-330](../claims.d/CLAIM-330.md): in [CASE-099](../cases.d/CASE-099.md)'s linearization the symmetric state is
unstable exactly when βγ > (1 − α)(1 − δ), only the loop can make it so,
and independent scoring (Regime B) removes the instability. Open here:
whether [CASE-092](../cases.d/CASE-092.md)'s full model has that linearization, its nonlinear
attractors and hysteresis, whether capture costs fidelity (the rest of
[CLAIM-297](../claims.d/CLAIM-297.md)), and whether role-indexed endorsement removes the captured
regime.

## Note of 2026-10-26: a nonlinear fold, and capture in a population

<!-- inactive-ok-file: CASE-162 — Proposed; the lab's capture runs filed 2026-10-26, cited as bearing on the remainder, not as answering it -->

[CASE-162](../cases.d/CASE-162.md) bears on the remainder without answering it
(dmarx/PerspectiveLab@7e2edc2).

- In a four-variable model of authority, record and competence, with no
  retrieval and no meaning state, the positive equilibrium appears at a
  fold, c = 0.4247 with competence frozen and full observation. A declared
  history is trapped only from c = 0.4469, and the onset depends on the
  starting history, falling toward the fold as the history strengthens
  without reaching it. That is history dependence with B better
  throughout, so the captured regime costs fidelity.
- In a 32-member event-level population, independent scoring with every
  cue admitted leaves no wrong incumbent in 64 worlds. Self-scoring at
  c = 0.5 leaves 39. Admission of cues that depends on the record leaves
  41 at s = 0.75 with no self-scoring at all.

Neither model is [CASE-092](../cases.d/CASE-092.md), and role-indexed endorsement is not tested.
The question is unchanged.
