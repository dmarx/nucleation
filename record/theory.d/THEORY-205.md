---
number: 205
status: Active
formerly:
- THEORY-tmpne099
title: "For a short-range lattice model on a cylinder with a symmetric transfer matrix whose leading excited eigenvalue is non-degenerate, with block and environment as slabs L_B transfer steps apart, the uninformative information-bottleneck encoder first loses stability at β = (λ0/λ1)^(2L_B), in the direction of the boundary weak value of the leading excited eigenvector, which by the cited conformal finite-size relation is the lowest-dimension primary at large circumference; the uninformative encoder can stop being optimal at a smaller β, and nothing is shown for blocks inside a buffer shell or for the fixed-alphabet RSMI optimum"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-205 (batch 039, ADR-047 v2). The derivation is re-derived step
    by step in a dated note below and is exact, not leading-order.
    "At its first transition" becomes "first loses stability". The
    uninformative encoder can stop being optimal at a smaller β, shown on
    a 3-state chain. The transfer matrix is stated as symmetric with a
    non-degenerate leading excited eigenvalue, and the CFT reading is
    marked as cited. The promote_when, widened to ask when the two
    thresholds coincide, moves to QUESTION-185.
tags:
- natural-sciences
- information-theory
date: '2026-10-09'
source:
- LIT-885
summary: >-
  Gordon, Banerjee, Koch-Janusz and Ringel (2020), [LIT-885](../literature.d/LIT-885.md), Eqs.
  3–5 and B2–C11, with one numerical check on a three-site critical
  Ising cylinder, reproduced exactly in [NOTE-690](../notes.d/NOTE-690.md). The theorem holds
  for slabs of a cylinder, at the point where the uninformative encoder
  first loses stability. The global first transition can come earlier,
  and when the two coincide is QUESTION-185. The paper's
  "equivalence" of IB and RG relevance, and [LIT-878](../literature.d/LIT-878.md)'s use of it for RSMI
  filters on planar blocks, go beyond it.
answers:
- QUESTION-065
---
<!-- inactive-ok-file: THEORY-194 QUESTION-025 CLAIM-092 — Proposed or open; cited as the accounts this one underpins or is set beside, and the question and claim it does not answer -->

# THEORY-205: For a short-range lattice model on a cylinder with a symmetric transfer matrix whose leading excited eigenvalue is non-degenerate, with block and environment as slabs L_B transfer steps apart, the uninformative information-bottleneck encoder first loses stability at β = (λ0/λ1)^(2L_B), in the direction of the boundary weak value of the leading excited eigenvector, which by the cited conformal finite-size relation is the lowest-dimension primary at large circumference; the uninformative encoder can stop being optimal at a smaller β, and nothing is shown for blocks inside a buffer shell or for the fixed-alphabet RSMI optimum

## Source

Gordon, Banerjee, Koch-Janusz and Ringel (2020; Phys. Rev. Lett. 126,
240601, 2021), [LIT-885](../literature.d/LIT-885.md): main text Eqs. 3–5 and Fig. 3; Appendix B
(Eqs. B1–B9), Appendix C (Eqs. C1–C11), Appendix F; as read in
[NOTE-690](../notes.d/NOTE-690.md).

## What was actually shown

**The setting.** An infinite cylinder of circumference L carrying a
short-range lattice model with transfer matrix T. The block V and the
environment E are runs of whole slices, separated along the axis by L_B
slices. The relevance variable of the information bottleneck (IB) is E.

**The derivation.** Writing all distributions through powers of T and
its eigendecomposition gives P(v|e) = P(v)[1 + ε r_v r_e] up to terms in
(λ2/λ0)^(L_B), with ε = (λ1/λ0)^(L_B) and r_v the ratio of the leading
excited to the ground eigenvector on V's boundary slice. The IB equations
then reduce to P(h|v) ∝ P(h) exp(β ε² r_v ⟨r_v⟩_h). Linearizing around
the uniform encoder puts the first transition at β_c⁻¹ = ε², with the
encoder's first non-trivial direction r_v; a third-order expansion gives
the binary encoder above it in closed form. As L → ∞, λ_i/λ0 →
exp(−2π∆_i/L), so r_v belongs to the lowest-dimension primary.

**What could have come out otherwise.** On a critical Ising cylinder of
circumference 3, an iterative IB solver given the exact joint law could
have found its transition elsewhere, or an encoder not following the
boundary spins. It found 146.340 < β_c < 146.350 against a predicted
146.34458, and the predicted encoder. [NOTE-690](../notes.d/NOTE-690.md) reproduces the
prediction exactly from the singular values of the normalized
block–environment channel, and notes that in this geometry the reduction
is exact rather than leading-order: the Markov property along the
cylinder makes P(v, e) a sum of rank-one terms with weights
(λ_i/λ0)^(L_B), so β_c = (λ0/λ1)^(2L_B) with no correction.

## What this does not say

- **Not that this is where the uninformative encoder stops being
  optimal.** The theorem is a linear-stability result. Below the
  bifurcation an encoder far from uninformative can already beat it,
  which happens on a skewed 3-state chain (dated note below). The two
  thresholds agree in the Ising check, and when they agree in general is
  [QUESTION-185](../questions.d/QUESTION-185.md).
- **Not that IB and RG relevance are equivalent in general**, as the
  paper's abstract puts it. The theorem concerns the first IB feature in
  one geometry. Later transitions are not derived.
- **Not that RSMI filters are the most relevant operators.** RSMI
  ([LIT-873](../literature.d/LIT-873.md), [LIT-878](../literature.d/LIT-878.md)) maximizes I(H;E) at a fixed alphabet, which the
  paper calls the β → ∞ limit of IB without analysing it, and its blocks
  are planar squares inside a buffer shell, not slabs. [NOTE-690](../notes.d/NOTE-690.md)
  sketches a leading-order argument that closes the first gap in the slab
  geometry; the second is open.
- **Not dependent on criticality**, except for the reading. At any
  temperature the first IB feature is the leading excited
  transfer-matrix mode; only calling it a scaling operator with
  dimension ∆₁ needs a CFT.
- **Not a result about short-ranged effective Hamiltonians.** That is
  [THEORY-198](THEORY-198.md)'s subject (full capture keeps the Hamiltonian short-ranged);
  this account says which feature a minimal capture takes, and neither
  implies the other.
- **Not covering degenerate leading operators.** With several operators
  of the same lowest dimension the IB fixes a subspace; the paper's
  symmetry argument says the encoder then carries a representation of the
  symmetry when the alphabet is large enough, and gives a Z4 example
  where a two-symbol alphabet breaks it.
- **Not an instruction for machine learning.** It says what an
  information-bottleneck optimum is in a lattice model, not how to train
  anything.

## Connections

It is the formal counterpart of [THEORY-194](THEORY-194.md), which states on numerical
evidence that the coarse-graining maximizing information with the far
environment is the RG-relevant one: it proves the operator half of that
claim in a neighbouring geometry and regime, and does not meet
[THEORY-194](THEORY-194.md)'s `promote_when`, which asks for unknown variables found or a
proof about effective Hamiltonians in two or more dimensions. It sits
beside [THEORY-198](THEORY-198.md) ([LIT-881](../literature.d/LIT-881.md)) as the second theorem of the same programme.
It is a worked analogue for [THEORY-161](THEORY-161.md) and [CLAIM-092](../claims.d/CLAIM-092.md), which pose meaning
and translation as information bottlenecks: here what the bottleneck
keeps first is computed exactly, and it is the leading singular direction
of the channel. That is an analogy, not evidence for either.

## Note of 2026-10-19: the derivation, re-derived

The setting: T symmetric, with eigenvalues λ0 > |λ1| > |λ2| ≥ ⋯ and
orthonormal eigenvectors ψ_i, where ψ0 > 0 by Perron–Frobenius. Write
r_i = ψ_i/ψ0, and let n be the number of transfer steps between V's
boundary slice s and E's boundary slice t.

1. **The joint law.** A slice's marginal is π = ψ0², and the n-step law
   of t given s is π(t) Σ_i (λ_i/λ0)^n r_i(s) r_i(t). Along the cylinder
   E is independent of V given s, and V of E given t. So
   P(v, e) = P(v)P(e)[1 + Σ_{i≥1} ε_i r_i(s(v)) r_i(t(e))], with
   ε_i = (λ_i/λ0)^n.
2. **An exact singular-value decomposition.** Since Σ_s ψ_i ψ_j = δ_ij,
   the r_i∘s are orthonormal and mean-zero under P(v), and so are the
   r_i∘t under P(e). So step 1 is an exact singular-value decomposition
   of P(v,e)/√(P(v)P(e)), with singular values 1 and |ε_i|. Nothing is
   dropped, as [NOTE-690](../notes.d/NOTE-690.md) observed.
3. **The second variation.** Perturb the uninformative encoder,
   p(h|v) = p(h)(1 + δ g_h(v)) with each g_h mean-zero. To second order
   in δ, I(H;V) − β I(H;E) = (δ²/2) Σ_h p(h)(‖g_h‖² − β‖K g_h‖²). Here K
   takes a function of V to its conditional expectation given E. Since
   K(r_i∘s) = ε_i r_i∘t, the largest ‖Kg‖²/‖g‖² over mean-zero g is
   ε_1², reached only at g = r_1∘s. So the uninformative encoder first
   loses stability at β = ε_1^(−2) = (λ0/λ1)^(2n), in the direction r_1(s).
4. **The Ising check.** For critical 2D Ising on a cylinder of
   circumference 3, with n = 9, the eigenvalues are λ0 = 17.87705 and
   λ1 = 13.55181. Both (λ0/λ1)^18 and the inverse squared singular value
   of the exact channel are 146.34458, the value [LIT-885](../literature.d/LIT-885.md) predicts. So L_B
   counts transfer steps.
5. **Global optimality is a different threshold.** The uninformative
   encoder is optimal exactly when I(U;V) ≥ β I(U;E) for every encoder U.
   That fails once β > 1/s*, where s* = sup I(U;E)/I(U;V). Since
   s* ≥ ρ_m² = ε_1², this threshold is never later than the bifurcation.
   - **Ising:** s*/ρ_m² = 0.999999 numerically, so the two coincide.
   - **A skewed 3-state chain:** take
     T = [[1, 0.9, 0.05], [0.9, 1, 0.05], [0.05, 0.05, 0.3]] with n = 3.
     The bifurcation is at (λ0/λ1)^6 ≈ 69,391. A binary encoder that
     flags the rare state with probability 10⁻⁴ already gives
     I(U;V) − 5000 I(U;E) < 0, and s* ≈ 27 ρ_m².

   So the theorem locates the bifurcation, and not in general the first
   transition of the global optimum. The encoder that wins on the 3-state
   chain still separates states by the sign of r_1. Whether the global
   optimum's first feature is always the leading excited mode is part of
   [QUESTION-185](../questions.d/QUESTION-185.md).
