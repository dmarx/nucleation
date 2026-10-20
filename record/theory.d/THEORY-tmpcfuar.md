---
status: Active
title: 'In a singularly perturbed system ẋ = f(x, z, t), εż = g(x, z, ε), if g is contracting in z at rate λ_z for every x and ε, the reduced system ẋ = f(x, γ(x), t) on the slow manifold z = γ(x) is contracting at rate λ_x, f is α-Lipschitz in z, |∂γ/∂x · f| ≤ d and g is K-Lipschitz in ε, then for all t ≥ 0 the fast state is within χ_z e^{−λ_z t/ε}|z(0) − γ(x(0))| + εχ_z(d + K)/λ_z of the manifold and the slow state within χ_x|x(0) − x_γ(0)|e^{−λ_x t} + ε[C₁(e^{−λ_x t} − e^{−λ_z t/ε}) + C₂(1 − e^{−λ_x t})] of the reduced trajectory; partial contraction of f in x alone is not enough'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmpio97l. The statement is Del Vecchio and
    Slotine's Lemma 2 and Theorem 3 with one correction: their Theorem 3
    assumes f partially contracting in x, and its proof uses contraction
    of the reduced system, which is assumed here instead. Every step
    (Lemma 1 for a constant metric, Lemma 2, Theorem 3) was re-derived
    step by step in NOTE-tmpio97l, which meets ADR-047 v2's condition for
    Active. The counterexample to the theorem as printed, and the
    numerical checks, are the record's.
tags:
- mathematics
- complex-systems
date: '2026-10-20'
source:
- LIT-tmplpq6l
answers:
- QUESTION-222
summary: >-
  Del Vecchio and Slotine (IEEE TAC 2013), [LIT-tmplpq6l](../literature.d/LIT-tmplpq6l.md), read in [NOTE-tmpio97l](../notes.d/NOTE-tmpio97l.md),
  with their Theorem 3's hypothesis corrected. A global, uniform-in-time,
  first-order bound on the error of the quasi-steady-state reduction, with
  every constant explicit and no requirement that ε be small. The
  reduction is Markovian: eliminating a fast, contracting variable costs
  O(ε) in trajectory error for all time, so no memory term is needed to
  that order. Constant metrics, deterministic, and the bound d on how fast
  the manifold moves is needed along the trajectory.
---
<!-- inactive-ok-file: THEORY-tmp5mn7l — Proposed; the account this one supplies a step for, nothing here rests on it -->

# THEORY-tmpcfuar: In a singularly perturbed system ẋ = f(x, z, t), εż = g(x, z, ε), if g is contracting in z at rate λ_z for every x and ε, the reduced system ẋ = f(x, γ(x), t) on the slow manifold z = γ(x) is contracting at rate λ_x, f is α-Lipschitz in z, |∂γ/∂x · f| ≤ d and g is K-Lipschitz in ε, then for all t ≥ 0 the fast state is within χ_z e^{−λ_z t/ε}|z(0) − γ(x(0))| + εχ_z(d + K)/λ_z of the manifold and the slow state within χ_x|x(0) − x_γ(0)|e^{−λ_x t} + ε[C₁(e^{−λ_x t} − e^{−λ_z t/ε}) + C₂(1 − e^{−λ_x t})] of the reduced trajectory; partial contraction of f in x alone is not enough

## Source

Del Vecchio and Slotine (2013), "A Contraction Theory Approach to
Singularly Perturbed Systems", *IEEE Transactions on Automatic Control*
58(3):752–757, [LIT-tmplpq6l](../literature.d/LIT-tmplpq6l.md), read in full in [NOTE-tmpio97l](../notes.d/NOTE-tmpio97l.md) from the authors'
revised manuscript. The statement is its Lemma 1, Lemma 2 and Theorem 3
(Lemma 1, Lemma 2 and Theorem 2 of the CDC-ECC 2011 version), with the
correction below.

## What was actually shown

**Setting.** ẋ = f(x, z, t), εż = g(x, z, ε), ε > 0. Contraction is
certified by a matrix measure µ in a norm |Θ·| with Θ a **constant**
invertible matrix (µ_Θ(A) = µ(ΘAΘ⁻¹)), and χ is an upper bound on the
condition number |Θ||Θ⁻¹|.

**Hypotheses.**

- g(x, ·, ε) is contracting in z at rate λ_z, uniformly in x, t and ε:
  µ_{Θ_z}(∂g/∂z) ≤ −λ_z. Then g(x, z, 0) = 0 has a unique root z = γ(x)
  for every x (Theorem 2), and ∂γ/∂x = −(∂g/∂z)⁻¹ ∂g/∂x.
- |∂γ/∂x (x) · f(x, z, t)| ≤ d. The proof uses this only along the
  trajectory, so d may be taken as the supremum over it.
- |g(x, z, 0) − g(x, z, ε)| ≤ Kε.
- **The reduced system ẋ = f(x, γ(x), t) is contracting at rate λ_x**, in
  the metric Θ_x. The paper assumes instead that f is partially
  contracting in x (ẏ = f(y, z(t), t) contracting for every path z(t)).
- f is α-Lipschitz in z, and γ is α_γ-Lipschitz.

**Fast bound (Lemma 2).** |z(t) − γ(x(t))| ≤ χ_z e^{−λ_z t/ε}|z(0) − γ(x(0))| + εχ_z(d + K)/λ_z.
z(t) solves the contracting system εẏ = g(x(t), y, ε); γ(x(t)) solves it
with the disturbance ε∂γ/∂x f + g(x, γ, 0) − g(x, γ, ε), of size at most
ε(d + K). Lemma 1 at rate λ_z/ε gives the bound.

**Slow bound (Theorem 3).** With C₁ = χ_x α χ_z |z(0) − γ(x(0))| / (λ_z − ελ_x)
and C₂ = χ_x α χ_z (d + K)/(λ_z λ_x),
|x(t) − x_γ(t)| ≤ χ_x|x(0) − x_γ(0)|e^{−λ_x t} + ε[C₁(e^{−λ_x t} − e^{−λ_z t/ε}) + C₂(1 − e^{−λ_x t})],
and |z(t) − γ(x_γ(t))| is bounded by the fast bound plus α_γ times this.
x solves the reduced system disturbed by f(x, z, t) − f(x, γ(x), t), of size
at most α|z − γ(x)|; Lemma 1, in its differential form, integrated against
the fast bound, gives the slow one. Every step is re-derived in
[NOTE-tmpio97l](../notes.d/NOTE-tmpio97l.md).

**What could have come out otherwise.** The paper's own hypothesis, partial
contraction of f in x, is not enough. In ẋ = −x + 2 tanh z,
εż = −z + 2 tanh x, every hypothesis the paper states holds (λ_x = λ_z = 1,
χ = 1, K = 0, α = α_γ = 2, d ≈ 4.9), but the reduced system
ẋ = −x + 2 tanh(2 tanh x) is bistable. From x(0) = x_γ(0) = 0.01,
z(0) = −1, the full system goes to x ≈ −1.915 and the reduced one to
x ≈ +1.915: an error of 3.83 at t = 20, against a bound of 0.98 at
ε = 0.1 and 0.098 at ε = 0.01 ([NOTE-tmpio97l](../notes.d/NOTE-tmpio97l.md)). The CDC version's
introduction states the right hypothesis, "the reduced system and the fast
system are each partially contracting"; the theorems in both versions
state the wrong one. In the paper's example f does not depend on z
(α = 0), so the example is unaffected.

**Checks (the record's).** On ẋ = −2x + y, ẏ = d(x − y) ([QUESTION-222](../questions.d/QUESTION-222.md)'s
memory example with c = d, ε = 1/d, γ(x) = x, reduced rate λ_x = 1), the
slow error stayed below the bound at d = 5, 20, 100 and 500, at 41 to
74% of it, and sup|x − x_γ|/ε settled near 3: first order, as stated.

## What this does not say

- **Not for a state- or time-dependent metric.** Θ is constant here. The
  extension to Θ(x, t), which Bousquet and Slotine's hypotheses need, is
  re-derived in [NOTE-tmpio97l](../notes.d/NOTE-tmpio97l.md) and is not this paper's.
- **Not a small-gain result.** f's dependence on z enters only through α,
  with no feedback condition, because d bounds the manifold's drift
  globally. When the disturbance on the fast state grows with the slow
  state, as in Bousquet and Slotine, a small-gain condition ε < ε_c is
  needed instead ([THEORY-tmp5mn7l](THEORY-tmp5mn7l.md)).
- **Not for linear systems as stated.** A bound on |∂γ/∂x · f| over all
  x and z fails when f is unbounded and γ is linear. The proof needs it
  only along the trajectory, which is how the paper's example and the
  record's check use it.
- **Not stochastic.** With noise on the fast variable z − γ(x) does not
  shrink to O(ε), and nothing here bounds an information measure.
- **Not sharp.** In the record's check the slow bound was loose by a
  factor of 1.4 to 2.4, and the paper reports a factor of about 40 in its
  example.

## Connections

- **[QUESTION-222](../questions.d/QUESTION-222.md).** Here the coarse variable is the slow state x and
  the eliminated variable z is fast and contracting. The Markovian
  reduction, with no memory coordinate at all, then predicts x to O(ε)
  for all time, with explicit constants. In A5's example, with
  c = κd, the memory kernel bκd e^{−dt} tends to bκδ(t) as d grows, and
  this theorem bounds the error of the memoryless model by O(1/d). It
  answers [QUESTION-222](../questions.d/QUESTION-222.md) in part, for a fast, contracting eliminated
  variable: the finite augmentation is the empty one, and the error is
  controlled. It says nothing when the eliminated variables are slow or
  noisy, which is where the question is hard.
- **[THEORY-tmp5mn7l](THEORY-tmp5mn7l.md).** Bousquet and Slotine apply the same robustness
  lemma to each line of the system and close the loop by small gain. This
  paper supplies the lemma's published proof for constant metrics.
- **[THEORY-661](THEORY-661.md).** A uniform-in-time first-order rate for the
  quasi-steady-state reduction, in a different frame from Simon and Ando
  (nonlinear, continuous time, contraction metrics, a given fast–slow
  split).
