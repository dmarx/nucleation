---
status: Proposed
title: "In the symmetric resource-competition class that MacArthur's consumer-resource model reduces to, Chesson's niche overlap is the cosine of two components' niche vectors, his average fitness is a component's net marginal value at zero abundance per unit niche norm, and a rare component's growth against a lone resident is its niche norm times its fitness less the overlap times the resident's"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: that MacArthur's model with fast
  resources, every resource positive, does not reduce to A = UᵀU and
  r = Uᵀb − μ under the stated map; that under that map Chesson's ρ, s or
  κ, as his Table 1 (2011) defines them, differ from the cosine, the norm
  or r_j/‖u_j‖; or that the invasion growth of a rare component against a
  lone resident differs from ‖u_i‖(κ_i − ρκ_j). Also defeated, in its
  attribution only, by a reading of Chesson (1990) showing that his
  overlap measure for MacArthur's model is not Table 1's ρ. Not defeated
  by models in which a component's impact on a resource differs from its
  benefit, or a resource is exhausted, which the claim excludes; nor by
  coexistence among more than two components, which it does not address.
tags:
- ecology
- mathematics
- learning-theory
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-369
grounds:
- THEORY-tmpac7iw
bears_on:
- QUESTION-132
- QUESTION-083
summary: >-
  Filed by the lead run of 2026-11-22 from a reading of Chesson (2011), the
  stand-in for Chesson (1990). MacArthur's model with fast resources is
  CLAIM-369's class under u_jl = c_jl √(v_l K_l / r_l), b_l = √(v_l K_l r_l)
  and cost μ_j. Under that map Chesson's sensitivity is ‖u_j‖, his overlap
  the cosine of u_j and u_k, and his average fitness
  κ_j = r_j/‖u_j‖ = −∂_j L(0)/‖u_j‖. A rare component's growth against a
  lone resident j is ‖u_i‖(κ_i − ρκ_j), so CLAIM-369's invasion fitness,
  in the two-component case, is Chesson's criterion ρ < κ_i/κ_j < 1/ρ.
  Checked numerically. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpac7iw — Proposed, filed by the lead run of 2026-11-22 from the reading this claim rests on -->
<!-- inactive-ok-file: CLAIM-885 — Proposed, filed 2026-11-22 by another lead and cited for its many-component bound -->

# CLAIM-tmpv65bg: In the symmetric resource-competition class that MacArthur's consumer-resource model reduces to, Chesson's niche overlap is the cosine of two components' niche vectors, his average fitness is a component's net marginal value at zero abundance per unit niche norm, and a rare component's growth against a lone resident is its niche norm times its fitness less the overlap times the resident's

## The claim

MacArthur's consumer–resource model, as Chesson states it (THEORY-tmpac7iw,
Table 1 of the chapter), has consumers j with consumption rates c_jl ≥ 0
and maintenance requirements μ_j, and logistic resources l with renewal
rates r_l, carrying capacities K_l and unit values v_l. With fast
resources, R_l = K_l(1 − Σ_k N_k c_kl / r_l) while that is positive, and a
consumer's per-capita growth is

  Σ_l c_jl v_l K_l − μ_j − Σ_k (Σ_l c_jl v_l K_l c_kl / r_l) N_k.

**The map.** Let u_jl = c_jl √(v_l K_l / r_l), the columns of U, and
b_l = √(v_l K_l r_l). Then Σ_l c_jl v_l K_l c_kl / r_l = u_j · u_k and
Σ_l c_jl v_l K_l = u_j · b. So the reduced model is CLAIM-369's, with
A = UᵀU, r = Uᵀb − μ and maintenance cost c = μ, and nonnegative niche
vectors, which is CLAIM-369's sign condition for the ecological reading.

**Chesson's measures under the map.**

1. Sensitivity: s_j = √(Σ_l c_jl² v_l K_l / r_l) = ‖u_j‖.
2. Overlap: ρ_jk = u_j · u_k / (‖u_j‖ ‖u_k‖), the cosine of the niche
   vectors, in [0, 1] because they are nonnegative.
3. Average fitness: κ_j = (u_j · b − μ_j)/‖u_j‖ = r_j/‖u_j‖. Since
   ∇L(n) = An − r, r_j = −∂_j L(0): κ_j is the marginal value of
   component j at zero abundance per unit niche norm.

**Invasion.** Let j be alone at equilibrium, n_j* = r_j/‖u_j‖², which
needs r_j > 0. A rare component i then grows at

  r_i − (UᵀU)_ij n_j* = ‖u_i‖κ_i − ‖u_i‖‖u_j‖ρ r_j/‖u_j‖² = ‖u_i‖(κ_i − ρκ_j).

That is CLAIM-369's s_i = −∂_i L at the resident equilibrium, factored
into Chesson's terms. Each of two components invades the other exactly
when κ_i > ρκ_j and κ_j > ρκ_i, that is ρ < κ_i/κ_j < 1/ρ: Chesson's
eq. (2). Scaling a niche vector together with its cost leaves ρ alone
and scales its κ, which is the chapter's "the heights of the consumption
rate curves" (p. 47) entering fitness and not overlap.

**Checks.** A record script (scratch/studies/lead-196/chesson_overlap.py,
51 tests) builds random models and checks A = UᵀU and r = Uᵀb − μ, the
three measures, Chesson's eq. (1), the form Letten, Ke and Fukami use,
and the invasion growth against the full consumer–resource model
integrated with the resident alone. They agree to numerical precision
whenever every resource stays positive. Where the resident exhausts a
resource they do not, as the exclusion of that case says.

**CASE-118.** Its unit vectors are ‖u_i‖ = 1, so κ_i = r_i, and with
r = (1 + δ, 1 − δ) the criterion is its |δ| < (1 − ρ)/(1 + ρ). With
δ = 0 the invasion growth is 1 − ρ.

## Why the record holds it

CASE-118 left open whether its ρ, the cosine of two unit feature vectors,
is Chesson's overlap for MacArthur's model, and QUESTION-132 names its
first outcome for Chesson. This settles the first for Chesson's measure
as his 2011 chapter states it, and it puts the record's marginal-value
test for recovery when rare in the coordinates the coexistence literature
uses: overlap, how far two components' niche vectors point the same way,
and fitness, how much a component is worth per unit of the niche it
occupies.

## The stronger reading it does not support

- **That ρ and κ decide coexistence among many components.** The
  factorization is pairwise. With more components the invasion growth at
  a −i community involves the whole resident set; CLAIM-885 gives the
  bound n*_i d_i² there. Pairwise overlaps do not fix it (QUESTION-083's
  note of 2026-10-29).
- **That overlap is a cosine in any competitive system.** It is one here
  because the same c_jl sets a consumer's impact on a resource and its
  benefit from it. Where impact and benefit differ, A is not symmetric,
  there is no L, and Chesson's ρ = √(α₁₂α₂₁/α₁₁α₂₂) is no cosine.
- **That an organization's operators have such niche vectors.** The map
  is from MacArthur's model, not from learned contributions.
