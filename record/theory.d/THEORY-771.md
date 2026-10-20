---
number: 771
status: Active
formerly:
- THEORY-tmp5mn7l
title: 'In a singularly perturbed system, fast states x̃ with dx̃/dt = f̃(x̃, y) + ε·δf and slow states y with dy/dt = ε·ḡ(y) + ε·δg, if f̃ is contracting in x̃ at rate β_f with x̃ = 0 an equilibrium for every y, ḡ is contracting at rate β_g, and |δf| ≤ d_f + α_f,x|x̃| + α_f,y|y|, |δg| ≤ d_g + α_g,x|x̃|, then for every ε below ε_c = β_f / [χ_f(α_f,x + χ_g α_f,y α_g,x / β_g)] the fast states stay within O(ε) of zero and, when d_g = 0, the slow states within O(ε) of the reduced trajectory, uniformly in time after a transient of order (1/β_f + 1/(εβ_g)) log(1/ε)'
version: 3
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-1025. The statement is the paper's
    Hypothesis 2, Lemma 3 and Theorem 1, with two corrections the reading
    found: ε_c is the reciprocal of the expression Remark 8 prints, and the
    O(ε) bound on the slow error needs d_g = 0 (or d_g = O(ε)), which the
    proof's last line assumes without saying. The key estimate (11) was
    re-derived step by step from Lemma 1. Lemma 1 itself and Lemma 4 are
    sketched in the paper and were not re-derived, so the entry is Proposed.
    The linear checks are the record's.
- version: 2
  date: '2026-10-20'
  note: >-
    Del Vecchio and Slotine (2013) is now read (NOTE-1020,
    THEORY-773). It does not itself prove the two sketched steps: its
    Lemma 1 is for a constant metric, and its fast bound is for a cascade
    without the small-gain loop. The reading's own re-derivations do: R2
    proves Lemma 1 for a state- and time-dependent metric, with χ the
    largest singular value of Θ anywhere over the smallest anywhere (not
    the supremum of pointwise condition numbers) and, when Θ depends on y,
    the contraction certificate holding along every admissible path of y;
    R5 replaces Lemma 4 by explicit bounds from an arbitrary initial fast
    state, confirming that d_g = 0 is needed. The promote_when condition
    appears to be met. The entry stays Proposed until the promotion audit
    checks R2 and R5. The account is unchanged.
- version: 3
  date: '2026-10-20'
  note: >-
    Promoted Active at the owner's direction, carrying out the promotion
    audit's decision (record/promotion-audit/decisions/THEORY-771.yaml).
    The promote_when asked for step-by-step re-derivations of Lemma 1 in a
    state- and time-dependent metric and of the passage to O(ε) from an
    arbitrary fast state. Both are recorded in the decision file (R2 and R5
    of NOTE-1020), so the condition is met under ADR-047 v2. Lemma 4 is
    bypassed, not repaired. "What this does not say" gains the two
    precisions R2 makes explicit.
tags:
- complex-systems
- mathematics
date: '2026-10-20'
source:
- LIT-1292
answers:
- QUESTION-221
summary: >-
  Bousquet and Slotine (arXiv 2015), [LIT-1292](../literature.d/LIT-1292.md), read in [NOTE-1025](../notes.d/NOTE-1025.md). It
  gives Simon's near-decomposability the rate in ε that [THEORY-661](THEORY-661.md)'s open
  statement lacks: first order, for trajectory error, uniform in time, under
  contraction of the modules and of the reduced slow system, with an
  explicit, sufficient ceiling on ε. Deterministic. It bounds how far the
  states are from the reduced description, not how much information the
  rest of the system sends into the slow variables, and it takes the slow
  coordinates as given.
---
<!-- inactive-ok-file: NOTE-1020 — new reading, cited for the re-derivations its promotion would rest on -->
<!-- inactive-ok-file: LIT-1127 LIT-1294 — Unavailable; the works this result stands in for, nothing rests on them -->
<!-- inactive-ok-file: THEORY-257 CLAIM-157 CLAIM-331 — Proposed; accounts and claims named for context, nothing here rests on their being settled -->

# THEORY-771: In a singularly perturbed system, fast states x̃ with dx̃/dt = f̃(x̃, y) + ε·δf and slow states y with dy/dt = ε·ḡ(y) + ε·δg, if f̃ is contracting in x̃ at rate β_f with x̃ = 0 an equilibrium for every y, ḡ is contracting at rate β_g, and |δf| ≤ d_f + α_f,x|x̃| + α_f,y|y|, |δg| ≤ d_g + α_g,x|x̃|, then for every ε below ε_c = β_f / [χ_f(α_f,x + χ_g α_f,y α_g,x / β_g)] the fast states stay within O(ε) of zero and, when d_g = 0, the slow states within O(ε) of the reduced trajectory, uniformly in time after a transient of order (1/β_f + 1/(εβ_g)) log(1/ε)

## Source

Bousquet and Slotine (2015), "A contraction based, singular perturbation
approach to near-decomposability in complex systems", arXiv:1512.08464,
[LIT-1292](../literature.d/LIT-1292.md), read in full in [NOTE-1025](../notes.d/NOTE-1025.md). The statement is its
Hypothesis 2, Lemma 3 and Theorem 1 (Appendix). It stands in, on the point
of rates, for Simon and Ando (1961, [LIT-1127](../literature.d/LIT-1127.md)) and Ando and Fisher (1963,
[LIT-1294](../literature.d/LIT-1294.md)), which the record could not obtain.

## What was actually shown

**Setting (8)–(9).** Fast states x̃ (deviations from the quasi-steady
manifold) and slow states y obey

dx̃/dt = f̃(x̃, y, u(εt)) + ε δf(x̃, y, u(εt)),
dy/dt = ε ḡ(y, u(εt)) + ε δg(x̃, y, u(εt)),

against the reduced system dȳ/dt = ε ḡ(ȳ, u(εt)). Remark 4 shows how to
reach this form from dx/dt = f(x, y, u) + εg_x, dy/dt = εg_y by
x̃ = x − x̄(y, u), with x̄ the unique root of f = 0; then δg(0, y) = 0
identically.

**Hypotheses (Hypothesis 2).** f̃ is partially contracting in x̃, with rate
β_f and metric condition number χ_f, and f̃(0, y, u) = 0; ḡ is
(χ_g, β_g)-contracting; the reduced solution is bounded, |ȳ| ≤ M̄; u is
bounded; |δf| ≤ d_f + α_f,x|x̃| + α_f,y|y| and |δg| ≤ d_g + α_g,x|x̃|; and

ε (χ_f/β_f)(α_f,x + (χ_g/β_g) α_f,y α_g,x) < 1.

**The estimate (Lemma 3, (10)–(11)).** Apply the contraction robustness
bound (Lemma 1) to each line, with M_x̃(t) = max_{τ≤t}|x̃(τ)|, ỹ = y − ȳ and
|ỹ(0)| = |Δ|:

|x̃(t)| ≤ χ_f|x̃₀| + ε(χ_f/β_f)(d_f + α_f,x M_x̃ + α_f,y(M̄ + M_ỹ)),
|ỹ(t)| ≤ χ_g|Δ| + (χ_g/β_g)(d_g + α_g,x M_x̃).

The second line has no ε: the disturbance ε·δg is divided by the slow
contraction rate ε·β_g. Substituting the second into the first and taking
the supremum (re-derived here, and it matches the paper's (11)):

M_x̃ ≤ [χ_f|x̃₀| + ε(χ_f/β_f)(d_f + α_f,y(M̄ + χ_g(|Δ| + d_g/β_g)))] / (1 − ε/ε_c).

So x̃₀ = O(ε) gives M_x̃ = O(ε) for all time. Applying Lemma 1 again to the
slow line, |ỹ(t)| ≤ χ_g|Δ|e^{−εβ_g t} + (χ_g/β_g)(d_g + α_g,x M_x̃), which
is O(ε) after the slow transient **only if d_g is zero or O(ε)**. The
paper's last line omits d_g. The Remark 4 construction gives d_g = 0; the
worked example lists d_g = 1, for which the bound on the slow error is
O(1).

**Theorem 1.** From any initial fast state, Lemma 4 brings x̃ to O(ε) by
t = log(1/ε)/β_f while y moves by O(ε log(1/ε)); then Lemma 3 applies, and
after a further (1/(εβ_g)) log(1/ε) the system stays in an O(ε)
neighbourhood of (0, ȳ).

**The critical separation.** ε_c = 1/[(χ_f/β_f)(α_f,x + (χ_g/β_g) α_f,y α_g,x)].
Remark 8 prints ε < (χ_f/β_f)(…) = ε_c, the reciprocal; the worked
example's ε_c = √2/7 is the reciprocal form evaluated on its constants
(with χ = 1: 2(√2/4 + 4·(3/4)(√2/2)) = 7√2/2). Above ε_c the paper's
building example, with one negative conductance, has several equilibria at
2.5ε_c and is often unstable at 5ε_c (Figs. 2–3).

**Linear checks (the record's, [NOTE-1025](../notes.d/NOTE-1025.md)).** Three blocks of three
units, dx/dt = (A* + εC)x, A* minus symmetric Laplacians, y the block sums,
x̃ = (I − VQ)x, identity metric so χ = 1, d_f = d_g = 0. With a symmetric
coupling plus a leak (ε_c = 0.369) and a non-passive one (ε_c = 0.235), the
bounds held at every ε from 0.02ε_c to 0.9ε_c. sup|x̃|/ε and sup|y − ȳ|/ε
stayed bounded as ε fell (first order). The x̃ bound was within a factor of
two at small ε. The bound on y − ȳ was loose by 20 to 1,000 times. Of five
random non-passive couplings, the full system first lost stability at 2.8,
6.3, 19.5, 19.8 and 47 times ε_c: the ceiling is sufficient and can be
conservative by more than an order of magnitude.

What could have come out otherwise: the slow error could have grown with
time, as finite-horizon Tikhonov estimates allow. Contraction of the
reduced slow system is what makes it uniform.

## What this does not say

- **Nothing about dynamical dependence.** The systems are deterministic.
  The bounds are on distances between trajectories, not on the
  information the rest of the system sends into y. With persistent noise
  the fast states do not shrink to O(ε) and the estimate does not apply
  as stated. [QUESTION-221](../questions.d/QUESTION-221.md) asks about dependence and stays open.
- **Not that the slow variables are block aggregates.** y is whatever
  coordinate has dy/dt = O(ε), and the partition into modules is given.
  For a linear system and block sums y = Qx, that needs QA* = 0, every
  column of each block summing to zero in continuous time: the
  equal-column-sum condition of [CLAIM-386](../claims.d/CLAIM-386.md) and [THEORY-755](THEORY-755.md). Neither the
  coordinates nor the blocks are found.
- **Not with a pointwise condition number.** χ is the largest singular
  value of the metric anywhere over the smallest anywhere; the supremum of
  the pointwise condition numbers can be smaller and does not suffice. A
  metric that depends on y must certify contraction along every admissible
  path of y ([NOTE-1020](../notes.d/NOTE-1020.md), R2).
- **Not a necessary condition.** ε_c guarantees; it does not mark where the
  approximation fails.
- **Not that the reduced system is stable whenever the modules are.**
  ḡ's contraction is assumed. Systems with a conserved quantity, as Simon's
  building and Simon–Ando's stochastic blocks are, must first be reduced
  to remove it.
- **Not Simon and Ando's own statement.** It is a different proof in a
  different frame (continuous time, nonlinear, contraction metrics), and
  the paper does not compare its constants with theirs.

## Connections

- **[THEORY-661](THEORY-661.md)** gains the rate its open statement lacked: first order in
  ε for trajectory error, uniform in time, under contraction.
- **[CLAIM-386](../claims.d/CLAIM-386.md).** Its post-transient orders rested on "the standard estimate
  that post-transient states lie within O(ε) of the slow subspace, which
  was not proved here." This is that estimate, in continuous time, under
  contraction. With it, the closure defect of the slow variables,
  ε·δg = ε·QCx̃ in the linear case, is O(ε²) after the transient against a
  drift of O(ε): the second order [CLAIM-386](../claims.d/CLAIM-386.md) measured with equal column
  sums.
- **[CLAIM-390](../claims.d/CLAIM-390.md)** bounds dependence for a block's full state, to second
  order. This bounds trajectory error, to first order. They measure
  different things and do not conflict.
- **[QUESTION-218](../questions.d/QUESTION-218.md).** Remark 6: the micro states act on the macro level
  through their quasi-steady values x̄(y), "an aggregation in time", and
  act only as a group if the coupling is also low rank, which the paper
  separates from weakness.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** Remark 8's cascade, τ_µ = (ε_c,µ ⋯ ε_c,M) τ_M, is an
  "expected" estimate, not a theorem.
