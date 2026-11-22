---
status: Proposed
title: 'For a linear coarse-graining of a linear Gaussian VAR, with an external target, Mori''s projection, excess error against the optimal predictor over two steps and a dimension budget declared, the five conditions on an effective description obey exactly three entailments: dynamical independence entails memory closure in VAR(1) but not in VAR(2); sufficiency, independence and memory closure together entail fidelity; and exact fidelity entails sufficiency; so leaving one out, independence and tractability can fail alone, memory closure only from VAR(2), sufficiency only at a positive tolerance, and fidelity never'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in one of the three proofs, or a model of the declared class
  and regime whose exact defects put it in a configuration the three
  entailments forbid; or a configuration the claim says is realizable
  whose witness in CASE-tmpo5jhq, recomputed from exact covariances,
  fails to land in it. A different table under a different declaration
  of target, metric, horizon or budget does not defeat it.
tags:
- mathematics
- complex-systems
- information-theory
date: '2026-11-22'
line:
- formal-apparatus
answers:
- QUESTION-252
rests_on:
- CLAIM-389
grounds:
- CASE-tmpo5jhq
uses:
- TERM-065
complements:
- CLAIM-tmp9xo66
summary: >-
  [LEAD-173](../leads.d/LEAD-173.md)'s answer to [QUESTION-252](../questions.d/QUESTION-252.md) for linear Gaussian VAR(1) and VAR(2).
  Pairwise only D ⇒ M (VAR(1)) and, at zero tolerance, A ⇒ P hold; the
  entailment that forbids failing A alone is three-place, P ∧ D ∧ M ⇒ A,
  and a pairwise table cannot show it. Tractability, as a dimension
  budget, is independent of everything. Proofs here, constructions in
  [CASE-tmpo5jhq](../cases.d/CASE-tmpo5jhq.md). The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpo5jhq CLAIM-tmp9xo66 — new; the study this claim rests on and the alternative declaration filed beside it -->

# CLAIM-tmp186gy: For a linear coarse-graining of a linear Gaussian VAR, with an external target, Mori's projection, excess error against the optimal predictor over two steps and a dimension budget declared, the five conditions on an effective description obey exactly three entailments: dynamical independence entails memory closure in VAR(1) but not in VAR(2); sufficiency, independence and memory closure together entail fidelity; and exact fidelity entails sufficiency; so leaving one out, independence and tractability can fail alone, memory closure only from VAR(2), sufficiency only at a positive tolerance, and fidelity never

## The claim

The class, the regime and the five conditions are as declared in
[CASE-tmpo5jhq](../cases.d/CASE-tmpo5jhq.md): X a stable stationary linear Gaussian VAR(p) with Σ ≻ 0,
Y_t = LX_t, target Z_{t+1} = GX_{t+1}; P is E[Z_{t+1} | X⁻] = E[Z_{t+1} | Y_t];
D is E[Y_{t+1} | X⁻] = E[Y_{t+1} | Y⁻]; M is zero Mori memory for the
projection onto span(Y_t), equivalently E[Y_{t+1} | Y⁻] = ΩY_t; A is that
the reduced model Ẑ_{t+k} = HΩ^{k−1}Y_t has relative excess error at most
ε over E[Z_{t+k} | X⁻] for k = 1, …, h, h = 2; C is dim Y ≤ b.

**E1. In VAR(1) with Σ ≻ 0, D ⇒ M.** This is [CLAIM-389](CLAIM-389.md): D holds iff
the row space of L is invariant under Aᵀ, and then every memory kernel
vanishes. It fails in VAR(2): an autonomous AR(2) coarse variable is
dynamically independent and has memory. The proof needs Σ ≻ 0, and the
companion form of a VAR(2) has singular noise, which is where it breaks.

**E2. In every regime, P ∧ D ∧ M ⇒ A, for every ε ≥ 0 and every h.**
D and M give E[Y_{t+1} | X⁻_t] = ΩY_t, and by the tower property and
stationarity E[Y_{t+j} | X⁻_t] = Ω^jY_t. P at time t+k−1 gives
E[Z_{t+k} | X⁻_{t+k−1}] = HY_{t+k−1}. So
E[Z_{t+k} | X⁻_t] = HΩ^{k−1}Y_t = Ẑ_{t+k}, and A's defect is zero. The
proof uses only linearity, Gaussianity and stationarity, not the VAR
form.

**E3. At ε = 0, with k = 1 in the horizon set, A ⇒ P.** A's defect at
k = 1 is P's defect, since HY_t is the best predictor of Z_{t+1} from Y_t.

**Completeness.** Every configuration of the 32 that E1–E3 do not forbid
has a witness in [CASE-tmpo5jhq](../cases.d/CASE-tmpo5jhq.md): 16 in VAR(1) at ε = 0, 22 at ε = 0.01, 22
in VAR(2) at ε = 0 and 30 at ε = 0.01. So these are the only entailments,
and the table is:

- **Leave-one-out.** Failing D with the other four holding is realizable
  in every regime: Y = (an autonomous AR(1), [CLAIM-389](CLAIM-389.md)'s dependent
  coordinate), with a target that reads the AR(1) part. Failing C is
  realizable everywhere: pad Y. Failing M is impossible in VAR(1) (E1)
  and realizable in VAR(2): Y = (AR(1), AR(2)). Failing P is impossible
  at ε = 0 (E3) and realizable at any ε > 0, by a leak below ε. Failing A
  is impossible everywhere (E2).
- **Pairwise.** Of the twenty ordered pairs only D ⇒ M (VAR(1)) and
  A ⇒ P (ε = 0) hold. Nothing implies or is implied by C.
- **Not visible pairwise.** E2 is three-place. In VAR(1) it reduces to
  P ∧ D ⇒ A, still two premises. That is the leave-one-out design's own
  return over a pairwise one: the fifth condition fails alone nowhere,
  and no pair shows it.

**What dissolved into parameters** ([QUESTION-252](../questions.d/QUESTION-252.md)'s last request). At
h = 1, A is P, so A is not a separate condition at that horizon; it
becomes one only from h = 2. At ε = 0 it is stronger than P, at ε > 0
neither implies the other, so whether P can fail alone is a fact about
the tolerance, not the system. C, as a dimension budget, interacts with
nothing; as a sample budget it would be a parameter of A ([CLAIM-401](CLAIM-401.md)).
And whether M can fail alone is a fact about the model class (VAR(1)
against VAR(2)), as [QUESTION-252](../questions.d/QUESTION-252.md) asks.

## What it does not say

- **Not that the five are independent in general.** Under other
  declarations the table changes. With the target taken to be Y's own
  future, P and A each collapse into D ∧ M ([CLAIM-tmp9xo66](CLAIM-tmp9xo66.md)). With a
  horizon set that omits k = 1, E3 goes. With A's error measured against
  the realized future, A can fail with P, D and M exact, by noise alone,
  and E2 goes. Which declaration [QUESTION-252](../questions.d/QUESTION-252.md) means is the owner's call;
  this claim holds for the one stated.
- **Not about approximate versions.** P, D and M are exact here and only
  A carries a tolerance. With tolerances on all four, E1–E3 become
  continuity bounds, which were not derived.
- **Not about nonlinear systems or coarse-grainings**, nor state-space
  models with observation noise, nor any class beyond VAR(2), though E2
  and E3 hold for any stationary Gaussian process.
- **Not that the witnesses are typical.** The witnesses with P exact are
  built with a copy row, and those with D or M failing behind an exact A
  put the failure in a part of Y the target does not read: target-
  relativity, which is [CLAIM-401](CLAIM-401.md)'s point, doing the work.
