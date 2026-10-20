---
number: 247
status: Active
formerly:
- THEORY-tmp7x3wf
title: 'For finite action-free labelled Markov chains, the discounted bisimulation metric, defined as the unique fixed point of Ferns et al.''s equation, is a bicausal optimal-transport distance, and it equals the value of a finite linear program over occupancy couplings'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-247.yaml, batch 006, ADR-047).
    The title now names the fixed-point definition of the metric. Its
    equality with the logical bisimulation metric, and that distance zero
    means bisimilar, are cited in LIT-962, not proved, and are now under
    "What this does not say". The promote_when asked for an independent
    check of the identification and of Lemma 1, or a refereed derivation.
    LIT-962 is refereed (NeurIPS 2024), and both steps were re-derived for
    the review by an independent route, written out in the note below. The
    promote_when is removed.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-962
summary: >-
  Calo, Jonsson, Neu, Schwartz & Segovia-Aguas (2024), [LIT-962](../literature.d/LIT-962.md), read in
  [NOTE-757](../notes.d/NOTE-757.md). For finite action-free chains with real labels r and
  discount γ, the bisimulation metric's fixed-point equation is the
  Bellman equation of transport over bicausal couplings with cost
  (1−γ)|r(x)−r(y)|, so the two coincide. The transport cost equals
  1/(1−γ) times the minimum of a linear objective over occupancy
  couplings, under flow and coherence constraints (Lemma 1, Theorem 1).
  It says nothing of systems with actions. Its link to trace distance is
  one-way and second-hand.
---
<!-- inactive-ok-file: QUESTION-008 CLAIM-034 — Deferred or Proposed; the set-aside question this bears on, its surviving one-way claim, and the companion account filed the same day, cited as open -->

# THEORY-247: For finite action-free labelled Markov chains, the discounted bisimulation metric, defined as the unique fixed point of Ferns et al.'s equation, is a bicausal optimal-transport distance, and it equals the value of a finite linear program over occupancy couplings

## Source

Calo, Jonsson, Neu, Schwartz and Segovia-Aguas (2024), [LIT-962](../literature.d/LIT-962.md), read in
[NOTE-757](../notes.d/NOTE-757.md): §2 (Eqs. 2–5), §3 (Lemma 1, Theorem 1), Appendix A.1 and
Appendix B (Theorem 3 and the proof of Lemma 1).

## What was actually shown

**The setting.** Take two finite stationary Markov chains M_X and M_Y,
with fixed initial states, a ground cost c on state pairs and γ ∈ (0, 1).
The transport distance is W_γ = inf ∫ Σ_t γ^t c(X_t, Y_t) dM_XY over
bicausal couplings: joint processes in which, given the joint past, each
chain's next state keeps its own law.

**The Bellman form (Theorem 3, after Moulos 2021).** The infimum is
attained by a stationary transition coupling. W_γ(x, y) is the unique
solution of V(xy) = c(xy) + γ inf_{p ∈ Π_xy} Σ p(x'y') V(x'y'), where Π_xy
is the set of couplings of P_X(·|x) and P_Y(·|y). The proof is an
application of Bertsekas (1977).

**The identification (§2.2).** For a chain with no actions, the
bisimulation metric of Ferns et al. is the unique solution of
U(xy) = (1−γ)|r(x)−r(y)| + γ inf_{p ∈ Π_xy} Σ p(x'y') U(x'y'). That is the
same equation with c(xy) = (1−γ)|r(x)−r(y)|, so U = W_γ. This could have
failed: had the bisimulation metric's step been anything other than an
optimal coupling of next-state laws with this cost, the equations would
differ. The equality of this fixed point with the logical definition (a
supremum over a grammar of functional expressions) is van Breugel and
Worrell's theorem, cited.

**The finite LP (Lemma 1, Theorem 1).** Let µ(xy, x'y') be the discounted
frequency of the transition from pair xy to pair x'y'. A distribution µ on
(X×Y)² arises from a valid transition coupling if and only if it
satisfies three linear systems:

- the flow constraint;
- coherence with P_X;
- coherence with P_Y.

Then W_γ = (1/(1−γ)) min ⟨µ, c⟩ over that polytope, a program with
|X|²|Y|² variables. The "if" direction is proved by building
π_µ = µ/ν_µ and showing that the flow equations have a unique solution,
since I − γZ is invertible.

## What this does not say

- **Not for systems with actions.** The chains have no inputs. The
  identification is for action-free labelled Markov chains. Ferns et al.'s
  MDP metric, which takes a maximum over actions, is mentioned and not
  recast as transport. A communicative system updated by a chosen
  utterance is the action case.
- **Not that the fixed point is the logical bisimulation metric.** The
  equality of this fixed point with the Desharnais–van Breugel–Worrell
  metric, a supremum over a grammar of functional expressions, is van
  Breugel and Worrell's theorem, cited in [LIT-962](../literature.d/LIT-962.md) and not proved there
  ([NOTE-757](../notes.d/NOTE-757.md), claim C6, "second-hand"). This THEORY holds the fixed-point
  form only.
- **Not a new proof that the metric characterises bisimilarity.** That
  distance zero means bisimilar is cited from van Breugel and Worrell
  (2001) and Desharnais et al. (2002). Calo et al. do not reprove it.
- **Not a comparison with trace equivalence.** The only statement about
  traces is second-hand: Bian and Abate (2017) show that near-bisimilar
  implies close finite-trace distributions, and the converse "is not
  shown to hold". The paper does not say that dropping bicausality yields
  a trace distance. The record may want to argue that (see [QUESTION-008](../questions.d/QUESTION-008.md)),
  but it is not shown here.
- **Not efficient computation in the strong sense.** The strongly
  polynomial solvability of the LP is asserted via Ye (2011), not proved.
  Sinkhorn Value Iteration's iteration bound,
  K ≥ 324 ‖c‖²∞ log(|X||Y|)/((1−γ)⁵ε²), holds only with exact inner
  fixed points. The authors call removing that condition a conjecture.
- **Not undiscounted or weak bisimulation.** γ < 1 throughout. The
  weak-bisimulation metric (Desharnais et al. 2002) is not treated.

## Connections

- **[QUESTION-008](../questions.d/QUESTION-008.md)** (Deferred) asks whether pragmatic fidelity is
  approximate bisimulation. This THEORY supplies the formal object for the
  action-free case: approximate bisimulation as a transport cost over
  couplings that may not anticipate. It does not answer the question,
  which needs actions and a judgement that observational equivalence
  ([TERM-033](../terms.d/TERM-033.md)) gets wrong. No `answers:` relation is filed.
- **[CLAIM-034](../claims.d/CLAIM-034.md).** The metric is symmetric. The one-way simulation that
  [CLAIM-034](../claims.d/CLAIM-034.md) calls for would need an asymmetric (simulation) metric, which
  the paper does not give.
- **[THEORY-280](THEORY-280.md)** builds on this LP and makes the same quantity
  estimable from samples.

## Note of 2026-10-19: the two checks, by an independent route

**The identification.** For any cost c, define
(T V)(xy) = c(xy) + γ min over p in Π_xy of Σ p(x′y′) V(x′y′). A minimum of
linear functionals over one fixed set is 1-Lipschitz in sup norm, since each
p is a probability vector. So ‖T V − T W‖∞ ≤ γ ‖V − W‖∞, and T has a unique
fixed point. With c(xy) = (1−γ)|r(x) − r(y)|, Eq. 3 and Eq. 5 are the same
operator, so their unique fixed points coincide.

**Lemma 1, as an occupancy-measure LP.** Read the pairs xy as the states of
a finite MDP whose actions at xy are the couplings in Π_xy. A stationary
coupling π gives an occupancy measure µ_π that satisfies the flow
constraint and both coherence constraints. Conversely, take a feasible µ
with pair marginal ν. Where ν > 0, set π = µ/ν, and take any coupling
elsewhere. Coherence makes π a coupling of the two next-state laws. Then ν
solves νᵀ = (1−γ)δᵀ + γνᵀZ_π, and I − γZ_π is invertible, so that
solution is unique and µ = µ_π. The objective ⟨µ, c⟩ is the discounted
cost of π times (1−γ), so the LP's minimum is (1−γ)W_γ, by Theorem 3. This
is the textbook occupancy-measure argument, not the paper's own text.
