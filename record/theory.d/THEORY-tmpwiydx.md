---
status: Active
title: 'In Szeidl and Szucs''s model of two outlets competing for readers and advertisers, where state-owned advertisers reward only the connected outlet''s slant, with weight δ, every equilibrium has the slant gap between the connected and the unconnected outlet equal to their owners'' ideal-point gap plus a favor-exchange term (βδ/NT)·Σ over government advertisers of masⱼWⱼ, up to measurement noise; readers'' preference for slant cancels from the gap, so equal observed gaps can come from different mixes of ideology and exchange'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmpefpic. The result is the paper's Propositions
    1–2 and equation (8), proved in its Appendix A.4; it is re-derived below
    step by step, which meets the condition for Active under ADR-047 v2.
    The last clause, that equal gaps can come from different mixes, is the
    record's reading of (8).
tags:
- society-and-governance
- social-science
- game-theory
date: '2026-10-21'
source:
- LIT-tmp6b6sj
extended_by:
- THEORY-tmplydnj
summary: >-
  Szeidl and Szucs (2021), LIT-tmp6b6sj, read in NOTE-tmpefpic. A
  necessary condition on equilibrium slant, not a closed form: masⱼ depends
  on the equilibrium shares. It holds under the model's logit readers,
  Cobb–Douglas advertisers with exogenous budgets, quadratic ideology cost
  and one-shot episodes. The authors check numerically, not analytically,
  that the conditions pick out an equilibrium at their estimates.
---
<!-- inactive-ok-file: THEORY-tmplydnj — Proposed; the structural estimates that rest on this condition, filed beside it -->

# THEORY-tmpwiydx: In Szeidl and Szucs's model of two outlets competing for readers and advertisers, where state-owned advertisers reward only the connected outlet's slant, with weight δ, every equilibrium has the slant gap between the connected and the unconnected outlet equal to their owners' ideal-point gap plus a favor-exchange term (βδ/NT)·Σ over government advertisers of masⱼWⱼ, up to measurement noise; readers' preference for slant cancels from the gap, so equal observed gaps can come from different mixes of ideology and exchange

## Source

Szeidl and Szucs (2021), *Econometrica* 89(1), LIT-tmp6b6sj, read in
NOTE-tmpefpic. Propositions 1 and 2, equation (8), and their proofs in the
supplement's Appendix A.4. The derivation below is the record's.

## What was actually shown

**Setup.** Outlet i ∈ {1, 2} chooses true slant s̃ᵢ to maximize
Vᵢ = β·E[Σⱼ pᵢqᵢⱼ] − (NT/2)(s̃ᵢ − ŝᵢ)². Measured slant is
sᵢ = s̃ᵢ + ζ + ξᵢ, and a reference outlet r has s_r = ŝ_r + ζ + ξ_r. Reader
shares are logit: Nᵢ/N = exp[αᵢ + γ(sᵢ − s_r)] / Σₗ exp[αₗ + γ(sₗ − s_r)].
Advertiser j, with budget Wⱼ and state-ownership indicator Gⱼ, maximizes
Σᵢ log(qᵢⱼ)·Nᵢ·exp[νᵢⱼ]·exp[Gⱼ(θᵢ + δᵢ(sᵢ − s_r))] subject to
Σᵢ pᵢqᵢⱼ = Wⱼ. Only outlet 1 is connected: δ₁ = δ > 0 and δ₂ = 0.

**Step 1, demand (Proposition 1).** With Cobb–Douglas weights wᵢⱼ the
budget share is aᵢⱼ = pᵢqᵢⱼ/Wⱼ = wᵢⱼ/(w₁ⱼ + w₂ⱼ). So
log(a₁ⱼ/a₂ⱼ) = log(N₁/N₂) + νⱼ + Gⱼ[θ + δ(s₁ − s_r)], with νⱼ = ν₁ⱼ − ν₂ⱼ
and θ = θ₁ − θ₂. The logit gives log(N₁/N₂) = α + γ(s₁ − s₂). Together:
log(a₁ⱼ/a₂ⱼ) = α + γ(s₁ − s₂) + θGⱼ + δ(s₁ − s_r)Gⱼ + νⱼ.

**Step 2, outlet 1's first-order condition.** Write zⱼ for the right-hand
side and Λ(z) = eᶻ/(1 + eᶻ), so a₁ⱼ = Λ(zⱼ) and outlet 1's revenue is
Σⱼ Wⱼ a₁ⱼ. Since s₁ = s̃₁ + ζ + ξ₁, ∂zⱼ/∂s̃₁ = γ + δGⱼ, and Λ′ = Λ(1 − Λ).
The objective is smooth, defined on all of ℝ and bounded above (the
quadratic dominates bounded revenue), so at an optimum
β Σⱼ Wⱼ E[a₁ⱼ(1 − a₁ⱼ)](γ + δGⱼ) = NT(s̃₁ − ŝ₁). With masⱼ = E[a₁ⱼ(1 − a₁ⱼ)],
s̃₁ = ŝ₁ + (βγ/NT)Σⱼ masⱼWⱼ + (βδ/NT)Σ_{j: Gⱼ=1} masⱼWⱼ.

**Step 3, outlet 2.** a₂ⱼ = 1 − Λ(zⱼ) and ∂zⱼ/∂s̃₂ = −γ, so
∂a₂ⱼ/∂s̃₂ = γΛ(1 − Λ). The government term does not involve s₂, since
δ₂ = 0. Hence s̃₂ = ŝ₂ + (βγ/NT)Σⱼ masⱼWⱼ, with the same masⱼ because
a₂(1 − a₂) = a₁(1 − a₁).

**Step 4, the gap.** Subtracting, and adding back measurement noise
(sᵢ − s_r = s̃ᵢ − ŝ_r + ξᵢ − ξ_r):
s₁ − s₂ = (ŝ₁ − ŝ₂) + (βδ/NT)Σ_{j: Gⱼ=1} masⱼWⱼ + (ξ₁ − ξ₂).
The reader term (βγ/NT)Σⱼ masⱼWⱼ appears in both outlets' conditions with
the same masⱼ and cancels.

What could have failed: the reader term could have differed between the
outlets, leaving the gap confounded with audience tastes. It does not,
because with two outlets the marginal shares coincide. The paper uses
that to argue that audiences cannot explain the change in relative slant.

## What this does not say

- **Not a closed form or a uniqueness result.** masⱼ depends on the
  equilibrium shares, so (8) is a fixed-point condition. Existence and
  uniqueness are checked numerically at the estimates, not proved.
- **Not that the split is identified from one episode.** One gap fixes the
  sum of the two terms, not each. Separating them takes variation in the
  exchange term with the ideal points held fixed, which is the paper's
  identifying assumption, and the empirical split is
  THEORY-tmplydnj, Proposed.
- **Not robust to more than two outlets** as stated. With more outlets
  the marginal shares need not coincide and the reader term need not
  cancel.
- **Not dynamic.** Each episode is a separate one-shot equilibrium.

## Connections

- **THEORY-tmp6l5uw.** δ, the government's ability to reward slant, is the
  continuous analogue of Besley and Prat's transaction cost τ, here allowed
  to differ by outlet.
- **CLAIM-tmppi0xf.** The last clause of the title is an instance of a
  description closed under ordinary dynamics that does not fix the
  response to an intervention on the mechanism. The intervention δ → 0
  removes one term and not the other.
