---
number: 389
status: Active
formerly:
- CLAIM-tmpmonrv
title: 'In a stable linear Gaussian VAR(1), exact dynamical independence of a linear coarse-graining implies that its Mori–Zwanzig memory vanishes, but not conversely: memory needs coupling out of the coarse variable and back, and dependence needs only the way back, so a coarse variable can be Markov in its own law with zero memory and still be dynamically dependent'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A2–A5 made this counterexample the
    centre of a proposed paper and A3 misread it as satisfying every
    condition but independence; the same law as an autonomous AR(1) (see
    CLAIM-397), and the VAR(p ≥ 2) remark under "What it does not say"
    checked on an AR(2). The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation, or in the counterexample: a check showing
  that for A = [[0.5, 0.4], [0, 0.3]], Σ = I − AAᵀ and Y = X₁ either some
  memory kernel K₁₂K₂₂^(j−1)K₂₁ is non-zero or the transfer entropy from X
  to Y is zero.
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-222
grounds:
- THEORY-733
- LIT-1245
summary: >-
  Derived in the reading of Chorin, Hald and Kupferman (2000),
  [NOTE-989](../notes.d/NOTE-989.md), and re-checked here. It settles, for the linear Gaussian
  VAR(1) class, the relation [QUESTION-222](../questions.d/QUESTION-222.md) left open between memory in
  the reduced dynamics and [THEORY-257](../theory.d/THEORY-257.md)'s dynamical independence: memory is
  the round trip Y → rest → Y, dependence the inward leg alone. Not about
  VAR(p ≥ 2), where the reading reports that an independent variable can
  carry memory, nor about nonlinear systems.
supports:
- CLAIM-398
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the account whose criterion this relates to memory, open -->
# CLAIM-389: In a stable linear Gaussian VAR(1), exact dynamical independence of a linear coarse-graining implies that its Mori–Zwanzig memory vanishes, but not conversely: memory needs coupling out of the coarse variable and back, and dependence needs only the way back, so a coarse variable can be Markov in its own law with zero memory and still be dynamically dependent

## The claim

Take X_t = AX_{t−1} + ε_t, stable, ε_t ~ N(0, Σ), Σ ≻ 0, with stationary
covariance Π, and a linear coarse-graining Y = LX with row space W. Work
with linear functionals of the state in L²(Π), where the transition
operator acts as Aᵀ and Mori's projection is the Π-orthogonal projection
onto W. Split Aᵀ into blocks: K₁₁ (W → W), K₂₁ (W → W⊥), K₁₂ (W⊥ → W) and
K₂₂ (W⊥ → W⊥). The discrete-time Mori–Zwanzig decomposition then has
memory kernels M_j = K₁₂K₂₂^(j−1)K₂₁, j ≥ 1 ([NOTE-989](../notes.d/NOTE-989.md)).

- **Independence ⇒ no memory.** By [THEORY-733](../theory.d/THEORY-733.md), Y is exactly
  dynamically independent iff W is invariant under Aᵀ, that is iff
  K₂₁ = 0. Then every M_j = 0.
- **No memory ⇏ independence.** A = [[0.5, 0.4], [0, 0.3]],
  Σ = I − AAᵀ (positive definite), Y = X₁. Then Π = I, so the blocks are
  read directly off Aᵀ: K₂₁ = 0.4 and K₁₂ = 0, and every M_j = 0. Y's
  autocovariance is 0.5ᵗ, so in its own law Y is an AR(1), Markov. Yet X₂
  enters Y_t with coefficient 0.4 and is uncorrelated with Y's whole past
  (Cov(X_{t−1}, X_{t−1−k}) = A^k has a zero (2, 1) entry). So
  T(X → Y) = ½ ln(Var(Y_t|Y⁻)/Σ₁₁) = ½ ln(0.75/0.59) = 0.120 nats. That
  was re-checked from the exact stationary covariances (0.1200).

In words: memory is information that leaves the coarse variable and comes
back to it. Dependence is information that arrives from outside, whether or
not it started inside. A coarse variable can receive news it never sent.

## What it does not say

- **Nothing for VAR(p ≥ 2) or for state-space models.** The reading
  reports that there an exactly independent variable can carry memory
  ([THEORY-733](../theory.d/THEORY-733.md)'s criterion constrains every lag, and the lags mix inside
  W). That was not re-checked here.
- **That zero memory is common.** It is not generic; the reading found it
  in none of 200 random models.
- **Anything about nonlinear projections.** For a deterministic flow with
  an invariant measure, the reading derives that zero memory, zero noise
  and exact closure coincide. That is a different statement, with no noise
  injected from outside, and it is recorded in the NOTE, not here.

## Note of 2026-10-20: why "not conversely"

For any scalar stationary process, Mori's memory for the projection onto
the current value is a functional of the process's own autocovariance, and
vanishes iff that autocovariance is geometric ([CLAIM-397](CLAIM-397.md), from the
reading of Lin and Lu, [NOTE-1029](../notes.d/NOTE-1029.md)). Memory is a property of Y's own law;
dependence is a property of its joint law with the rest of the system. So
no memory measure can detect dependence, which is the structural reason
the converse fails.

## Note of 2026-10-21: a paper's centre, one misreading, and the AR(2) check

The exchange of 2026-10-20 (A2–A5) made this counterexample the centre of
a proposed paper, twice in A2 (as "Markov without independence" and as
"zero memory with transfer entropy", one construction). A3 used it as a
witness that every condition but independence holds. It is not: Y's own
past predicts Y with residual variance 0.75 against 0.59 from the full
past, so predictive sufficiency holds only for prediction from Y itself.

**The same law, different dependence.** A5 and A7 used it as a
non-identifiability result. Y's autocovariance is 0.5ᵏ, so Y has the law
of an autonomous AR(1) with φ = 0.5 and innovation variance 0.75, whose
transfer entropy is 0. So no functional of Y's law, memory measure or
otherwise, decides dynamical independence. A7: "This is not a sample-size
limitation." Checked on 2026-10-21; the general form is the note of the
same date on [CLAIM-397](CLAIM-397.md).

**Independent with memory.** The report under "What it does not say",
that in VAR(p ≥ 2) an exactly independent variable can carry memory, was
checked on 2026-10-21 in the simplest case. An autonomous AR(2),
Y_t = 0.5Y_{t−1} + 0.3Y_{t−2} + ε, has Mori memory c₁ = 0.147 and
c₂ = −0.0315, non-zero, with autocovariance Hankel rank 2 and memory rank
1, as [CLAIM-397](CLAIM-397.md) predicts. So A4's "impossible" cell (independent with
memory) is impossible only in VAR(1). [QUESTION-tmp1nqby](../questions.d/QUESTION-tmp1nqby.md) carries both
witnesses.
