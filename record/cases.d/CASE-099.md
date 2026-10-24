---
number: 99
status: Active
formerly:
- CASE-tmp8tn9v
title: 'The two-hypothesis coupled meaning–influence model linearized at its symmetric state: a meaning bias m and an authority bias a, each stable alone, coupled by authority shaping interpretation (β) and interpretation shaping endorsement (γ)'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- self-governance
date: '2026-10-16'
line: distributed-agency
variant_of:
- CASE-092
summary: >-
  A14 §2 of the exchange of 2026-10-16. Near the symmetric state of the
  two-hypothesis, two-specialist model, (m, a) evolves by a 2×2 matrix
  J = [[α, β], [γ, δ]] plus noise. With nonnegative entries and α, δ < 1,
  the symmetric state is unstable exactly when βγ > (1 − α)(1 − δ), and
  the unstable direction mixes meaning and authority. Checked here. A
  construction about a linearization, not a fitted or simulated result.
supports:
- CLAIM-330
- CLAIM-338
- CLAIM-400
variants:
- CASE-106
- CASE-123
- CASE-124
- CASE-tmpw4r7u
---

<!-- inactive-ok-file: CLAIM-297 — Proposed; the thesis this construction bears on and the claim it grounds -->

# CASE-099: The two-hypothesis coupled meaning–influence model linearized at its symmetric state: a meaning bias m and an authority bias a, each stable alone, coupled by authority shaping interpretation (β) and interpretation shaping endorsement (γ)

## The construction

[CASE-092](CASE-092.md) has two hypotheses, A and B, and two retrieval specialists, one
better at finding evidence for each. A14 §2 reduced it to two numbers:
m ∈ [−1, 1], the prevailing interpretive bias toward A, and a ∈ [−1, 1],
the relative authority of the A-specialist. Near the symmetric state
(m, a) = (0, 0) it wrote

  (m_{t+1}, a_{t+1})ᵀ = J (m_t, a_t)ᵀ + (ξ_t, ζ_t)ᵀ,  J = [[α, β], [γ, δ]],

with α the persistence of the meaning distribution, δ the persistence of
authority, β the effect of authority on interpretation (the A-specialist's
retrievals push meaning toward A) and γ the effect of interpretation on
endorsement (in [CASE-092](CASE-092.md)'s Regime A, operators are scored against the
dominant interpretation, so a lean toward A raises the A-specialist's
score).

## What it shows

The eigenvalues are λ± = ½[(α + δ) ± √((α − δ)² + 4βγ)]. Take α, β, γ, δ
≥ 0 and α, δ < 1, so each field alone is stable. Then λ+ is the larger
eigenvalue and, since 2 − α − δ > 0,

  λ+ > 1 ⇔ (α − δ)² + 4βγ > (2 − α − δ)² ⇔ βγ > (1 − α)(1 − δ).

A14's condition is right. Three things follow, and were checked here:

1. **The loop, not either arrow, destabilizes.** If βγ = 0 the eigenvalues
   are α and δ, both inside the unit circle. One-way coupling, however
   strong, leaves the symmetric state stable.
2. **The unstable direction is mixed.** For β, γ > 0 the eigenvector of
   λ+ is (β, λ+ − α), with both components positive: the mode that grows
   is a combined lean of meaning and authority, not either alone. That is
   the object [CLAIM-164](../claims.d/CLAIM-164.md) says a gap makes definite, a subspace, though A14
   noted the caveat that Jacobian eigenvalues are not the singular-value
   gaps [CLAIM-164](../claims.d/CLAIM-164.md) is about.
3. **Regime B removes it.** Scoring operators by independently assessed
   relevance sets γ ≈ 0, so by 1 the coupling cannot destabilize the
   symmetric state, whatever the endorsement memory.

Near the threshold λ+ approaches 1 and its relaxation time
τ = −Δt / ln λ+ grows without bound, so the mixed mode is also the slow
one: the coupling makes a slow collective variable before it makes an
unstable one.

## What it does not show

That the nonlinear bounded system has two captured attractors (A14: it
"could lead to competing stable interpretive–authority configurations");
that the signs assumed hold in any implementation of [CASE-092](CASE-092.md); or that
capture lowers fidelity, which is [CLAIM-297](../claims.d/CLAIM-297.md)'s further claim. It is the
textbook instability condition for a positive 2×2 linear system, applied
to this reading of the coupling. Fictional by construction.

## Note of 2026-10-18: a proposed extension with demands and a feasible-update oracle

A39 §3 of the exchange of 2026-10-17 proposed extending this case as its
"case study 2": "The new experiment would add explicit competing demands
and a feasible-update oracle. It would ask whether interpretation–
endorsement feedback can make a system persistently fail to use an
available satisfactory update." The oracle computes the residual Φ of
[CLAIM-365](../claims.d/CLAIM-365.md), so the extension would separate structural from
governance-induced frustration ([CLAIM-357](../claims.d/CLAIM-357.md)) in this model. Its key
contrast, "endorsement based on independent performance evidence versus
endorsement scored through the interpretations whose authority is being
evaluated", is not new: it is Regime B against the γ arrow here, and
[CLAIM-342](../claims.d/CLAIM-342.md)'s and [CLAIM-297](../claims.d/CLAIM-297.md)'s thesis. A39 called it "the best candidate for
an early discriminating experiment". A40's Study C restates it. Not run.
The dynamics it would need are [QUESTION-124](../questions.d/QUESTION-124.md)'s.
