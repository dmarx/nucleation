---
number: 1000
status: Active
formerly:
- CLAIM-tmp0v3wu
title: 'Round-trip gain above one breaks symmetry'
statement: >-
  In two coupled meaning–influence institutions, each stable alone, with
  nonnegative channels by which each one's meaning moves the other's
  evidence or conferral, the symmetric state of the pair is unstable exactly
  when the round-trip gain exceeds one, which for the built institutions is
  (θ + σ_E ω)(χ + σ_P ψ) > Δ_E Δ_P with Δ_i each institution's own margin;
  the meaning rates and the conferral memories cancel, and each
  institution's inner loop enters only through its margin
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-015, from the
    executed study CASE-401.
- version: 2
  date: '2026-11-24'
  note: >-
    Promoted to Active at the owner's word of 2026-11-24 ("promote the
    ten", under the dialectic regime; ADR-057): its premise CLAIM-947 is
    Active, no objection targets it, and nothing meets its defeated_if.
    The derivation is in CASE-401, whose code
    (scratch/studies/lead-015/) was rerun on 2026-11-24 by a session
    other than the filer's: the 14 tests pass and every results file
    reproduces except timings, including the 1,802 of 1,802 random
    parameter sets on which the condition agrees with the nonlinear map.
    CASE-401 is promoted in the same pass.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation in CASE-401, or a rerun of its code
  (scratch/studies/lead-015/) in which, with every channel nonnegative and
  each institution stable alone, the spectral radius of the coupled
  Jacobian exceeds 1 while (θ + σ_E ω)(χ + σ_P ψ) < Δ_E Δ_P or the reverse,
  or in which the block condition fails for a nonnegative block matrix with
  stable diagonal blocks. A channel of another form (a negative one, or
  resources acting on the gain of conferral rather than its direction)
  does not count: the claim is stated for these channels, and the study
  reports the others.
tags:
- complex-systems
- self-governance
- mathematics
date: '2026-11-22'
line:
- distributed-agency
rests_on:
- CLAIM-947
grounds:
- CASE-401
complements:
- CLAIM-330
bears_on:
- QUESTION-100
summary: >-
  [LEAD-015](../leads.d/LEAD-015.md)'s condition. Two of [CASE-363](../cases.d/CASE-363.md)'s reduced institutions are
  coupled by four nonnegative channels: θ and ω carry the party's meaning
  into the evaluator's evidence and conferral, χ and ψ the evaluator's
  meaning into the party's. The coupled Jacobian at symmetry is a 4×4 block
  matrix with rank-one cross blocks. For any nonnegative block matrix with
  stable diagonal blocks the spectral radius exceeds 1 exactly when the
  round-trip gain ρ(G_P C_PE G_E C_EP) does, G_i = (I − J_i)⁻¹; here that
  gain is (θ + σ_E ω)(χ + σ_P ψ)/(Δ_E Δ_P), Δ_i = (1 − φ′_i) − g_iσ_i²/2.
  1,802 of 1,802 random parameter sets agreed with the nonlinear map
  ([CASE-401](../cases.d/CASE-401.md)). The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

# CLAIM-1000: Round-trip gain above one breaks symmetry

## The claim

[CLAIM-404](CLAIM-404.md) says the interpretation–authority loop "can close between the two institutions" and that "the two-institution version has not been derived". [CASE-401](../cases.d/CASE-401.md) derives it for the built model.

**The general form.** Let J = [[J_E, C_EP], [C_PE, J_P]] be nonnegative, with ρ(J_E), ρ(J_P) < 1: each institution stable alone. Then ρ(J) > 1 exactly when ρ(G_P C_PE G_E C_EP) > 1, G_i = (I − J_i)⁻¹. G_i is institution i's static gain, how far a sustained push into it moves its state once its own loop has answered; the product is the gain of one trip round the loop between the institutions. The proof is the M-matrix Schur complement with Varga's regular splitting; it holds for blocks of any size.

**For the built institutions.** Each block J_i is [CASE-363](../cases.d/CASE-363.md)'s, with α = 1 − ρ(1 − φ′), β = ρσ, γ = (1 − δ)gσ/2 and δ ([CLAIM-947](CLAIM-947.md)). Only meaning crosses, so the round trip is the scalar L_E L_P with

  L_E = (θ + σ_E ω)/Δ_E,  L_P = (χ + σ_P ψ)/Δ_P,  Δ_i = (1 − φ′_i) − g_iσ_i²/2.

The pair leaves symmetry exactly when (θ + σ_E ω)(χ + σ_P ψ) > Δ_E Δ_P.

Three things follow.

- *It is [CLAIM-330](CLAIM-330.md)'s form one level up.* There, a cross product βγ against the product of the two fields' margins; here, the product of the channel strengths against the product of the institutions' margins. A channel into authority counts through σ, the authority's pull on meaning.
- *Rates and memories cancel.* ρ_i and δ_i scale both sides, as in [CLAIM-947](CLAIM-947.md), so neither institution's speed or conferral memory decides whether the pair is captured, only how fast. The captured state was the same to 3e-11 across ρ and δ.
- *Inner loops enter only through margins.* Δ_i falls as institution i nears its own threshold, so the cross loop needed shrinks with it: at Δ = 0.04 each, θ = 0.1 and ψ = 0.3 gave a round trip of 7.5. With no inner loop (g_i = 0), Δ_i = 1 − φ′_i and the loop between the institutions still destabilizes once the channels are strong enough.

The leading eigenvector is positive in all four components: the mode that grows leans both institutions' meanings and authorities the same way. Below threshold the loop multiplies a standing bias of the party's corpus by 1/(1 − L_E L_P) in both institutions.

## What it does not say

- That it holds for other channels. With corrective channels (the evaluator's reading working against the party's lean) the pair fails by oscillation, as [CLAIM-340](CLAIM-340.md)'s corrective regime does, and no condition is derived. Resources acting on the gain of conferral have no linear term at symmetry ([CLAIM-1021](CLAIM-1021.md)).
- Anything about the captured state's size beyond the numbers of the study, or about hysteresis.
- That the result is new mathematics. The block condition is the standard small-gain form for nonnegative systems; what is new to the record is its application to [CASE-092](../cases.d/CASE-092.md)'s institutions and the cancellation.
- What it means for independence; that is [CLAIM-1202](CLAIM-1202.md).
