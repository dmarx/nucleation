---
number: 266
status: Proposed
formerly:
- CASE-tmp5mact
title: 'Equal charge, different tokens: two φ⁴ kinks with the same boundary charge and energy sit anywhere on the line, a perturbed kink can return to the kink family while drifting from its centre, and a winding-two sector of the abelian Higgs model holds two separated vortices, two coincident ones or, above critical coupling, a symmetric one that is unstable'
version: 1
standing: stipulated
kind: construction
tags:
- mathematics
- individuation
- natural-sciences
date: '2026-11-15'
line:
- distributed-agency
draws_on:
- THEORY-1507
- THEORY-1869
illustrates:
- CLAIM-593
summary: >-
  From A5 §§3.2–3.3 and §4.1 of the exchange "Explain String Theory"
  (2026-11-15), after the owner's "this feels like a construction that
  might be useful for some of the formal modeling attempts/purposes/needs"
  of this record. The kink's profile, energy and charge were rechecked on
  filing (scratch/formal/soliton_testbed_checks.py). The vortex part rests
  on [THEORY-1507](../theory.d/THEORY-1507.md) for the sectors and on Czubak & Jerrard ([NOTE-1950](../notes.d/NOTE-1950.md))
  for the coupling-dependent stability; that two unit vortices of a
  winding-two sector can sit apart or together at critical coupling is
  A's statement, not checked against a read source. Proposed because the
  construction is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1507 NOTE-1950 — Proposed, Skimmed or new; the readings the construction uses and the claim it grounds -->

# CASE-266: Equal charge, different tokens: two φ⁴ kinks with the same boundary charge and energy sit anywhere on the line, a perturbed kink can return to the kink family while drifting from its centre, and a winding-two sector of the abelian Higgs model holds two separated vortices, two coincident ones or, above critical coupling, a symmetric one that is unstable

## The construction

**The kink.** Take a real field on the line with energy
E[φ] = ∫ [κ/2 (∂ₓφ)² + λ/4 (φ² − v²)²] dx. Under the boundary values
φ(−∞) = −v and φ(+∞) = +v it has the static solution
φ_K(x; X) = v tanh((x − X)/ℓ), with ℓ = √(2κ/(λv²)), and energy
E_K = (2√(2κλ)/3) v³. Both were rechecked on filing. The charge
Q = (φ(+∞) − φ(−∞))/2v is 1.

- **Translation.** φ_K(·; X₁) and φ_K(·; X₂) have the same charge and the
  same energy for any X₁ ≠ X₂. Equal charge does not imply equal
  configurations.
- **Form against token** (A5 §3.3). Under the gradient flow
  ∂ₜφ = κ∂ₓₓφ − λφ(φ² − v²), measure the distance to the kink family,
  d_K(t) = inf_X ‖φ(·,t) − φ_K(·; X)‖. Measure also the distance to the
  original kink, d₀(t) = ‖φ(·,t) − φ_K(·; X₀)‖. On an infinite homogeneous
  line a perturbation can leave d_K small while d₀ is not: the form
  returns and the centre has moved. A: "a fundamental distinction between
  stability of an organizational form and stability of its location or
  token identity".
- **What the charge needs** (A5 §3.4, run A4). If the boundary values may
  change, the protection lapses. A kink–antikink pair between equal vacua
  has net charge zero and can annihilate.

**The vortex.** In the abelian Higgs model, finite energy puts a
configuration in one sector of quantized winding ([THEORY-1507](../theory.d/THEORY-1507.md);
Czubak & Jerrard, [NOTE-1950](../notes.d/NOTE-1950.md)). A winding-two sector contains:

- at critical coupling, by A's statement, two separated unit vortices or
  two coincident ones, with the same total charge;
- above critical coupling, a symmetric winding-two vortex that is
  "linearly unstable … and hence not even a local energy minimizer"
  (Czubak & Jerrard, Remark 1.1).

The charge does not fix how many cores the sector's configuration has,
where they are, or which persisted.

## What it shows

The charge fixes a sector: a kind of configuration and its net count of
defects. It does not fix which defect is which, where it is, or, for
vortices, how many there are. These are logical separations. A conserved
invariant can hold while any token-tracking criterion fails.

## What it cannot show

- **That token identity is unreal or arbitrary.** Only that the charge
  does not supply it.
- **Anything about organizations.** The construction is mathematical.
  Its organizational use is the claim it grounds.
- **The vortex counts at every coupling.** Only critical coupling (A's
  statement) and the instability above it (read) are covered.
