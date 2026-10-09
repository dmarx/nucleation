---
number: 205
status: Proposed
formerly:
- THEORY-tmpne099
promote_when: >-
  A second reading that checks the derivation independently and states its
  scope as here, for instance an exact transfer-matrix computation on a
  model other than Ising (a Potts or non-integrable chain on a cylinder
  wide enough to separate ∆₁ from ∆₂) that reproduces both the first
  transition at (λ0/λ1)^(2L_B) and an encoder depending on the block only
  through the leading eigenvector's boundary weak value. Against it: a
  short-range model with a symmetric transfer matrix whose first IB
  feature, in the slab geometry, is not that eigenvector. Results for
  planar blocks inside a buffer shell, or for RSMI at fixed alphabet,
  cannot settle this account either way; they bear on the wider claim it
  does not make.
title: 'For a short-range lattice model on a cylinder, with block and environment as slabs separated by a buffer, the information-bottleneck encoder at its first transition depends on the block only through the boundary weak value of the leading transfer-matrix eigenvector, at β_c = (λ0/λ1)^(2L_B): at large circumference this is the lowest-dimension primary, so the first feature information-theoretic relevance selects is the most RG-relevant operator; nothing is shown for blocks inside a buffer shell or for the fixed-alphabet RSMI optimum'
version: 1
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
  for slabs of a cylinder at the first IB transition; the paper's
  "equivalence" of IB and RG relevance, and [LIT-878](../literature.d/LIT-878.md)'s use of it for RSMI
  filters on planar blocks, go beyond it.
---
<!-- inactive-ok-file: THEORY-194 THEORY-198 THEORY-161 QUESTION-025 CLAIM-092 — Proposed or open; cited as the accounts this one underpins or is set beside, and the question and claim it does not answer -->

# THEORY-205: For a short-range lattice model on a cylinder, with block and environment as slabs separated by a buffer, the information-bottleneck encoder at its first transition depends on the block only through the boundary weak value of the leading transfer-matrix eigenvector, at β_c = (λ0/λ1)^(2L_B): at large circumference this is the lowest-dimension primary, so the first feature information-theoretic relevance selects is the most RG-relevant operator; nothing is shown for blocks inside a buffer shell or for the fixed-alphabet RSMI optimum

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
