---
number: 752
status: Active
formerly:
- THEORY-tmpepvai
title: 'In optimal prediction of a Hamiltonian system with separable energy and canonical initial law, projected by conditional expectation, the t-model''s leading-order memory term tPLQLx makes the effective Hamiltonian of the resolved variables non-increasing, so the eliminated variables'' memory enters as a damping that grows linearly in time'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-975. The t-damping equation is the paper's
    (26)–(27) and the result its Theorem 8.1, with the paper's proof. Every
    step is re-derived below, which meets the condition for Active under
    ADR-047 v2. The check on the model problem and the observation that the
    true conditional mean's effective energy is not monotone are the
    record's.
tags:
- mathematics
- natural-sciences
- complex-systems
date: '2026-10-20'
source:
- LIT-1253
answers:
- QUESTION-222
summary: >-
  Chorin, Hald and Kupferman (2002), [LIT-1253](../literature.d/LIT-1253.md), read in [NOTE-975](../notes.d/NOTE-975.md):
  Theorem 8.1. Truncating the Mori–Zwanzig memory integral at its lag-zero
  value gives dΦ/dt = R̄(Φ) + tS(Φ), and under the stated conditions this
  dissipates the free energy of the resolved variables. It says nothing
  about how well the t-model predicts, gives no error bound, and holds
  only for the conditional-expectation projection; the true conditional
  mean's effective energy need not decrease.
supports:
- CLAIM-tmpcrdhj
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the closure criterion this is contrasted with, open -->
# THEORY-752: In optimal prediction of a Hamiltonian system with separable energy and canonical initial law, projected by conditional expectation, the t-model's leading-order memory term tPLQLx makes the effective Hamiltonian of the resolved variables non-increasing, so the eliminated variables' memory enters as a damping that grows linearly in time

## Source

Chorin, Hald and Kupferman (2002), *Physica D* 166:239–257, [LIT-1253](../literature.d/LIT-1253.md),
read in full in [NOTE-975](../notes.d/NOTE-975.md) from the published version. The t-damping
equation is the paper's (26)–(27); the result is its Theorem 8.1 with the
proof of §8. The derivation below follows it and fills its steps.

## What was actually shown

**Setting.** A Hamiltonian H(q, p) = T(p) + V(q) on ℝ²ⁿ, with initial data
drawn from ρ = Z⁻¹e^{−H}, and e^{−T}, e^{−V} decaying fast enough that
boundary terms vanish in integration by parts. The first m conjugate pairs
(qᵢ, pᵢ), i ≤ m, are resolved, each with its momentum. L = Σⱼ(H_pⱼ∂_qⱼ −
H_qⱼ∂_pⱼ). P is the conditional expectation given (q̂, p̂), and Q = I − P.
The effective Hamiltonian is ℋ(q̂, p̂) = −log∫e^{−H}dq̃dp̃.

**The t-damping equation.** The Mori–Zwanzig memory term
∫₀ᵗ Kⱼ(ϕ̂(t − s), s) ds, with its integrand replaced by the value at s = 0,
is tSⱼ(ϕ̂(t)) with Sⱼ = PLQLxⱼ. So, for i ≤ m,
ṗᵢ = PLpᵢ + tPLQLpᵢ and q̇ᵢ = PLqᵢ + tPLQLqᵢ.

**Step 1, the Markovian part.** Lpᵢ = −H_qᵢ and Lqᵢ = H_pᵢ. Differentiating
ℋ under the integral, ℋ_qᵢ = P H_qᵢ and ℋ_pᵢ = P H_pᵢ. So PLpᵢ = −ℋ_qᵢ and
PLqᵢ = ℋ_pᵢ: without memory, the reduced flow is Hamiltonian in ℋ and
conserves it.

**Step 2, factorization.** Under ρ conditioned on (q̂, p̂), q̃ and p̃ are
independent, since e^{−H} = e^{−T(p)}e^{−V(q)}. So P[a(p)b(q)] =
P[a]·P[b].

**Step 3, PLQLpᵢ.** Let gᵢ = H_qᵢ − ℋ_qᵢ = V_qᵢ − ℋ_qᵢ, a function of q
alone, with P gᵢ = 0. QLpᵢ = −gᵢ, so LQLpᵢ = −Σⱼ T_pⱼ ∂_qⱼgᵢ (the ∂_p terms
vanish). By Step 2, PLQLpᵢ = −Σⱼ P[T_pⱼ]·P[∂_qⱼgᵢ].

- For j > m: P[T_pⱼ] = −∫∂_pⱼ(e^{−T})dp̃ / ∫e^{−T}dp̃ = 0.
- For j ≤ m: P[T_pⱼ] = ℋ_pⱼ (Step 1).
- For j ≤ m, differentiate P gᵢ = ∫gᵢe^{−V}dq̃ / ∫e^{−V}dq̃ = 0 in qⱼ:
  P[∂_qⱼgᵢ] − P[gᵢV_qⱼ] + P[gᵢ]P[V_qⱼ] = 0. The last term is zero, and
  P[gᵢℋ_qⱼ] = ℋ_qⱼP[gᵢ] = 0, so P[∂_qⱼgᵢ] = P[gᵢgⱼ].

So PLQLpᵢ = −P[gᵢ Σ_{j≤m} gⱼℋ_pⱼ].

**Step 4, PLQLqᵢ.** By the same steps with kᵢ = H_pᵢ − ℋ_pᵢ, a function of
p alone: LQLqᵢ = −Σⱼ V_qⱼ ∂_pⱼkᵢ, P[V_qⱼ] is 0 for j > m and ℋ_qⱼ for
j ≤ m, and P[∂_pⱼkᵢ] = P[kᵢkⱼ]. So PLQLqᵢ = −P[kᵢ Σ_{j≤m} kⱼℋ_qⱼ].

**Step 5, the energy.** Along the t-damping flow, by the chain rule and
Step 1, the Markovian parts cancel:

dℋ/dt = Σᵢ(ℋ_qᵢq̇ᵢ + ℋ_pᵢṗᵢ) = t Σᵢ(ℋ_qᵢ PLQLqᵢ + ℋ_pᵢ PLQLpᵢ).

Since ℋ_qᵢ and ℋ_pᵢ are functions of (q̂, p̂), they move inside P:

dℋ/dt = −t P[(Σᵢ kᵢℋ_qᵢ)²] − t P[(Σᵢ gᵢℋ_pᵢ)²] ≤ 0 for t ≥ 0,

because a conditional expectation of a square is non-negative.

**Check on the paper's model** (two oscillators, H = ½(x₁² + x₂² + x₃² +
x₄² + x₁²x₃²), q = (x₁, x₃), p = (x₂, x₄), resolving (x₁, x₂)). Here
ℋ = ½x₂² + ½x₁² + ½log(1 + x₁²) + const, k₁ = 0, and g₁ = x₁x₃² −
x₁/(1 + x₁²) with x₃ | x₁ ~ N(0, 1/(1 + x₁²)). The formula gives
dℋ/dt = −t x₂²·x₁²·Var(x₃² | x₁) = −2t x₁²x₂²/(1 + x₁²)². Computing dℋ/dt
directly from the paper's (28), dΦ₂/dt = −Φ₁(1 + 1/(1 + Φ₁²)) −
2tΦ₁²Φ₂/(1 + Φ₁²)², gives the same.

What could have failed: the leading-order memory term could have been
energy-neutral or energy-injecting, so that the cheapest memory correction
did not reproduce the decay of the conditional mean at all. Under these
conditions it cannot be either.

## What this does not say

- **Not that the t-model predicts well.** It shows the direction of the
  effect, not its rate. On the paper's model it over-damps the first peak
  (0.39 against 0.63 at t ≈ 5.2) and is no better than the Markovian
  equation to t ≈ 4 (re-check in [NOTE-975](../notes.d/NOTE-975.md)). No error bound is given.
- **Not that the true conditional mean dissipates ℋ.** In the re-check, ℋ
  evaluated on the Monte Carlo mean rises from 0.0091 at t = 15 to 0.0273
  at t = 25, and the mean keeps a residual oscillation of about 0.1, while
  the t-damped solution goes to rest. The t-model's monotone dissipation is
  a property of the approximation.
- **Not for other projections.** The linear and finite-rank projections
  are not positivity-preserving, so Step 5's sign fails in general.
- **Not without separability or conjugate pairs.** Step 2 needs
  e^{−H} = e^{−T}e^{−V}; Step 1 needs each resolved coordinate resolved
  with its momentum.
- **Not a short-memory result.** Evaluating the integrand at lag zero over
  all of [0, t] treats the kernel as constant over the window. The paper
  calls the t-model a short-memory approximation; as an expansion it is
  valid for t short against the memory time.
- **Not a Markovian augmentation.** The t-model adds no memory
  coordinates. It is a non-autonomous equation in the resolved variables
  alone.

## Connections

- **[QUESTION-222](../questions.d/QUESTION-222.md): answers in part.** For Hamiltonian systems under
  these conditions, the leading-order memory of the eliminated variables
  is dissipative for the resolved free energy and grows linearly in time,
  and it can be computed from the projection at one instant. That gives
  the form of the memory's first effect. It leaves the question's main ask
  open: a finite-dimensional augmentation with k memory coordinates and a
  bound on its prediction error.
- **[THEORY-257](THEORY-257.md).** That criterion conditions on the coarse variable's own
  history in a stationary process; optimal prediction conditions on the
  resolved initial value under an initial law. Neither result bears on
  the other directly.
