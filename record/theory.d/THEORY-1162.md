---
number: 1162
status: Active
formerly:
- THEORY-tmpncu1p
title: 'In a consumer-resource model whose species-resource benefits and impacts have correlation rho, the replica-symmetric cavity fixed point loses stability where rho squared equals surviving species over non-depleted resources'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed Active from one study read in full (NOTE-1366), with the
    title limited to what the study derives. The boundary was re-derived
    on 2026-10-29 from the paper's cavity relations: the divergence of
    the two response variances (B15–B16) from (B11) and (B14), and
    ρ*² = γ⁻¹φ_N/φ_R from it with A42's χ = φ_R/D. The cavity ansatz
    itself and the chaos beyond the boundary were not re-derived; they
    are recorded below as what the paper shows by assumption and by
    simulation.
tags:
- ecology
- complex-systems
date: '2026-10-29'
source:
- LIT-1236
- LIT-1234
summary: >-
  Blumenthal, Rocks and Mehta (2024), [LIT-1236](../literature.d/LIT-1236.md): in MacArthur's
  consumer–resource model with benefits c and impacts e correlated by ρ,
  the replica-symmetric steady state is unstable when ρ < ρ*,
  ρ*² = S*/M* at the boundary. With ρ = 1 competitive exclusion keeps
  S*/M* ≤ 1, so the symmetric model never crosses it. What this does not
  say: that non-reciprocity by itself breaks the optimization picture;
  it does so only past a boundary set by species packing, and that the
  other side is chaotic is shown numerically, not derived.
---

# THEORY-1162: In a consumer-resource model whose species-resource benefits and impacts have correlation rho, the replica-symmetric cavity fixed point loses stability where rho squared equals surviving species over non-depleted resources

## Source

Blumenthal, Rocks and Mehta (2024), [LIT-1236](../literature.d/LIT-1236.md), read in [NOTE-1366](../notes.d/NOTE-1366.md); the
stability test is the one Bunin (2017), [LIT-1234](../literature.d/LIT-1234.md), read in
[NOTE-1397](../notes.d/NOTE-1397.md), uses for random Lotka–Volterra communities.

## What was actually shown

The model: S species and M logistic resources, dNᵢ/dt = Nᵢ(Σ_α cᵢα R_α −
mᵢ), dR_α/dt = R_α(K_α − R_α) − Σᵢ Nᵢ eᵢα R_α, with random cᵢα and eᵢα of
mean µ/M and fluctuations σ/√M correlated by ρ. When e = c (ρ = 1) the
effective species interactions Aᵢⱼ = Σ_α cᵢα eⱼα Θ(R_α) are symmetric and
the steady state minimizes an objective.

In the limit S, M → ∞ with M/S fixed, the cavity method under a
replica-symmetric, self-averaging ansatz gives self-consistent equations
for the surviving fractions φ_N, φ_R and the susceptibilities χ
(resources to carrying capacity) and ν (species to mortality). Perturbing
every survivor by independent noise, the second moments x of the species
response and y of the resource response satisfy x = a(y + 1),
y = b(x + 1), with a = φ_R/(σρχ)² and b = σ²γ⁻¹φ_N/D², D = 1 − ρσ²γ⁻¹ν.
Both diverge when ab = 1, i.e. (ρχD)² = γ⁻¹φ_Nφ_R. The cavity equation
for a resource gives χ = φ_R/D, so the condition is ρ²φ_R² = γ⁻¹φ_Nφ_R,
ρ*² = γ⁻¹φ_N/φ_R = (S φ_N)/(M φ_R): the number of surviving species over
the number of non-depleted resources. Beyond it the variances are
negative, so the replica-symmetric fixed point does not exist as a
stable state.

What could have come out otherwise: the boundary could have depended on
σ, µ or the carrying capacities separately; it depends on them only
through the packing ratio. And simulations could have kept reaching
steady states below ρ*; in the paper's runs (S = M up to 1024) they do
not, with positive largest Lyapunov exponents, and a finite-size fit at
two parameter points puts the probability of reaching steady state
towards zero with size.

## What this does not say

- **Not that non-reciprocity alone ends the optimization picture.** Any
  ρ < 1 removes the symmetric objective, but the fixed point stays
  stable down to ρ*. A sparsely packed community (S*/M* small) tolerates
  strong asymmetry; one near the exclusion bound tolerates little.
- **Not a derivation of chaos.** The cavity method locates the loss of
  stability; that the other side is chaotic, rather than multistable or
  periodic, is numerical, at moderate sizes and few parameter points.
- **Not beyond the ansatz.** Replica symmetry is assumed and checked
  against simulations, not proved; no symmetry-broken solution is given.
- **Not for structured interactions.** The interactions are random and
  unstructured, the resources self-replenishing, one consumer level.
- **Not that symmetry guarantees a unique outcome in general.** In random
  Lotka–Volterra communities ([LIT-1234](../literature.d/LIT-1234.md)) a multiple-attractor phase exists
  even for symmetric interactions; what keeps the symmetric
  consumer–resource model unique is that its interaction matrix is a
  product, as in [CLAIM-369](../claims.d/CLAIM-369.md).

## Bearing

It sharpens the reading the synthesis gave [LIT-1236](../literature.d/LIT-1236.md) for [QUESTION-083](../questions.d/QUESTION-083.md):
the limit of reading a community of competing processes as one
optimization is a boundary in reciprocity that depends on how many
processes each shared resource must support, not a switch that any
asymmetry throws.
