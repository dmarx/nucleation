---
number: 521
status: Proposed
formerly:
- THEORY-tmpf9wko
promote_when: >-
  A held reading of the statistical-mechanics analysis itself, the replica
  calculation of Seung, Sompolinsky and Tishby or the rigorous bound of
  Haussler, Kearns, Seung and Tishby, confirming that for the Ising
  perceptron in the thermodynamic limit the generalization error drops
  discontinuously at a critical load while for the spherical perceptron it
  falls smoothly as 1/α. That would make the perceptron statement a held
  result rather than one reported second-hand. For deep networks, what
  would bear on it is a measurement of the entropy of near-optimal
  hypotheses in a trained network; a learning curve with a sharp drop
  cannot settle it, since other mechanisms produce those.
title: "In the thermodynamic limit, with examples and capacity growing together at fixed load, generalization error can jump discontinuously with the load when the entropy of hypotheses just above the best error vanishes faster than the training-error energy grows: a spherical perceptron's error falls smoothly as 1/α, an Ising perceptron's drops to zero at a critical load"
version: 1
tags:
- learning-theory
- loss-landscapes
- anthology-candidate
date: '2026-10-16'
source:
- LIT-672
summary: >-
  Martin & Mahoney (2017), [LIT-672](../literature.d/LIT-672.md), read in [NOTE-542](../notes.d/NOTE-542.md), restating Seung,
  Sompolinsky & Tishby (1992) and Haussler, Kearns, Seung & Tishby (1996),
  which the record does not hold. Generalization is set by maximizing
  s(ε) − α ln(1/(1 − ε)). For weights on a sphere s(ε) ~ ln ε and ε ~ 1/α;
  for ±1 weights s(ε) ~ −(π²/2)ε² ln ε, the first-order condition has no
  solution past a critical load, and the error drops to zero. Uniform
  bounds that see a class only through its size or VC dimension are smooth
  and blind to this. That deep networks have such a phase diagram is the
  authors' conjecture, and their mapping of label noise to load and early
  stopping to temperature is an analogy.
bears_on:
- QUESTION-039
---
<!-- inactive-ok-file: THEORY-087 THEORY-106 THEORY-108 — Proposed; neighbouring accounts of complexity, double descent and phase diagrams, named in Connections, not leaned on -->

# THEORY-521: In the thermodynamic limit, with examples and capacity growing together at fixed load, generalization error can jump discontinuously with the load when the entropy of hypotheses just above the best error vanishes faster than the training-error energy grows: a spherical perceptron's error falls smoothly as 1/α, an Ising perceptron's drops to zero at a critical load

## Source

Martin & Mahoney (2017), [LIT-672](../literature.d/LIT-672.md), read in full in [NOTE-542](../notes.d/NOTE-542.md). The perceptron
results are the paper's restatement of Seung, Sompolinsky & Tishby (1992),
Haussler, Kearns, Seung & Tishby (1996) and Engel & Van den Broeck (2001),
none of which the record holds. [NOTE-542](../notes.d/NOTE-542.md) drafted this candidate and held it
back until one of those is read; it is filed Proposed for that reason.

## What was actually shown

**The volume argument.** In realizable teacher–student learning with the
zero-temperature Gibbs rule, the volume of hypotheses at error ε after m
examples is Ω_m(ε) = Ω₀(ε)(1 − ε)^m in the annealed approximation (Eq. 5).
The error is set by maximizing s(ε) − e(ε), with s(ε) = (1/N) ln Ω₀(ε) and
e(ε) = −α ln(1 − ε) ≈ αε, in the limit m, N → ∞ with α = m/N fixed.

**Continuous weights.** For J on the sphere J² = N, s(ε) ~ ln ε for small ε,
the condition 1/ε − α = 0 gives ε ~ 1/α (Eqs. 6–8): smooth, in line with
PAC and VC.

**Ising weights.** For J ∈ {−1, +1}^N, s(ε) ~ −(π²/2)ε² ln ε (Eq. 10). The
condition −π²ε ln ε − α = 0 (Eq. 13) has no solution for large α, so the
optimum moves to the boundary ε = 0 and the error drops discontinuously at
α_c. The (α, τ) diagram has phases of perfect and poor generalization, a
spin-glass phase and metastable regions (Fig. 3(d), from Seung et al.).

**The rigorous route.** With Q_j hypotheses at error ε_j, the error bound is
min{ε_i : Σ_{j≥i} Q_j(1 − ε_j)^m ≤ δ} (Eq. 16); in the limit the error is at
most ε* + ε_τ, with ε* the rightmost crossing of s(ε) and −α log(1 − ε)
(Eqs. 14–18). For the Ising perceptron s(ε) = H(sin²(πε/2)) gives the drop
to zero.

**What could have come out otherwise.** The paper reports that the replica,
rigorous and numerical results agree for the perceptron ([NOTE-542](../notes.d/NOTE-542.md), C3).

## What this does not say

- **That deep networks have phases.** The authors call it an "obvious
  conjecture"; the only evidence offered is Choromanska et al.'s
  entropy-versus-loss histogram, read as the random energy model.
- **That label noise is load and early stopping is temperature.** The
  mapping (Claim 1) is an analogy. The load identification needs the
  capacity reached by training to scale with m, justified only by
  random-label fitting, and τ depends on stopping time "in some manner that
  we won't make explicit".
- **That uniform bounds are wrong.** They are valid and smooth; a smooth
  upper bound "does not imply that the quantity being upper bounded is
  smooth" (footnote 5). [THEORY-028](THEORY-028.md) is such a bound and does not conflict
  with this account.
- **That early stopping is the only effective regularizer.** That
  follows from the model by construction and is not measured; as an
  instruction it would belong in the anthology.

## Connections

- **[QUESTION-039](../questions.d/QUESTION-039.md)** asks what sets the moment, in examples, at which a
  network acquires a structure, and whether acquisition is one kind of
  event. This gives one mechanism for a threshold in examples per unit of
  capacity: the entropy of near-optimal hypotheses.
- **[THEORY-108](THEORY-108.md)** (Yang et al., [LIT-663](../literature.d/LIT-663.md)) measures a load and temperature
  grid on real networks, with the same kind of control parameters; [LIT-663](../literature.d/LIT-663.md)
  declares `extends` to this paper.
- **[THEORY-106](THEORY-106.md)** (Liao, Couillet & Mahoney, [LIT-679](../literature.d/LIT-679.md)) derives an exact
  transition in random-features ridge regression and cites this paper for
  reading double descent as a transition between phases.
- **Singular learning theory ([THEORY-087](THEORY-087.md)).** Both replace regular
  large-n asymptotics with one that keeps the model's geometry, by volume
  near the optimum. Neither paper makes the connection ([NOTE-542](../notes.d/NOTE-542.md)).
