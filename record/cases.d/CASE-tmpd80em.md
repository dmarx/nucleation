---
status: Proposed
title: 'Two of the built meaning–influence institutions, an evaluator and an evaluated party, coupled through the evidence and resources the party supplies and the standing the evaluator''s reading confers: with each institution stable alone, the symmetric state of the pair is unstable exactly when (θ + σ_E ω)(χ + σ_P ψ) > Δ_E Δ_P, and the loop between them captures the evaluator''s reading even when its own conferral is independent of its interpretation'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-015. The code,
    tests and result files are committed beside it under
    scratch/studies/lead-015/.
standing: documented
kind: executed-study
tags:
- complex-systems
- self-governance
- society-and-governance
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-363
bears_on:
- QUESTION-100
summary: >-
  The build LEAD-015 asks for. Two copies of CASE-363's reduced
  institution, an evaluator E and an evaluated party P, read the same two
  hypotheses and are coupled through four named channels: the party's
  prevailing interpretation tilts the evidence the evaluator reads (θ) and
  the authority inside it (ω); the evaluator's reading is evidence the party
  reads (χ) and redistributes authority inside the party (ψ). CLAIM-404's
  loop, in A21's words, is θ and ψ. Linearized at the symmetric state, the
  4×4 Jacobian is unstable exactly when the round-trip gain
  (θ + σ_E ω)(χ + σ_P ψ)/(Δ_E Δ_P) exceeds 1, Δ_i = (1 − φ′_i) − g_iσ_i²/2
  being each institution's own margin; the meaning rates and conferral
  memories cancel. 1,802 of 1,802 random parameter sets agreed with the
  nonlinear map. The evaluator's reading is captured with its own authority
  untouched when its conferral reads no interpretation; cutting the return
  channel removes the instability whatever the party supplies. Resources
  read as capacity rather than direction leave the linear condition
  unchanged and capture one side below it. A fictional model, by
  construction; the numbers are of this model. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-363 CLAIM-947 — new; LEAD-090's build and its threshold, filed 2026-11-22, of which this is the two-institution variant -->
<!-- inactive-ok-file: CLAIM-tmp0v3wu CLAIM-tmpz8q70 CLAIM-tmp42aba — new; the claims this study grounds, filed in the same batch -->

# CASE-tmpd80em: Two of the built meaning–influence institutions, an evaluator and an evaluated party, coupled through the evidence and resources the party supplies and the standing the evaluator's reading confers: with each institution stable alone, the symmetric state of the pair is unstable exactly when (θ + σ_E ω)(χ + σ_P ψ) > Δ_E Δ_P, and the loop between them captures the evaluator's reading even when its own conferral is independent of its interpretation

## What was done

LEAD-015 asks to "Extend the model to two regulating institutions and derive the condition under which their symmetric state is unstable, as CLAIM-330 does for one." CLAIM-404 names what closes the loop: an evaluator "whose evidence or resources the evaluated party affects", and an evaluator's reading that affects "the evaluated party's standing". The code, its 14 tests and the experiments are in scratch/studies/lead-015/ (model.py, test_model.py, run.py; results/*.json; the README holds the derivation and says how to rerun). Everything ran in under a minute on one thread.

**Each institution.** CASE-363's reduced map, unchanged: meaning m and authority a, with m′ = (1 − ρ)m + ρ(b + σa + φ′m) and a′ = δa + (1 − δ)tanh(gσm/2 + t), φ′ = φ(1 − ε). The one addition is t, an outside tilt of the institution's conferral, zero in CASE-363. A test checks that each half of the coupled map is LEAD-090's exact mean field. Both institutions read the same two hypotheses (A might be "the party's practice is sound").

**The channels, as read from CLAIM-404.** Four, each nonnegative in the main result:

- θ, *evidence, party to evaluator*: b_E = θm_P. What the party discloses or generates leans with its own prevailing interpretation; the informational route.
- ω, *resources, party to evaluator*: t_E = ωm_P. The party's resources favour the evaluator's specialist whose line agrees with the party's.
- χ, *evidence, evaluator to party*: b_P = χm_E. The evaluator's published reading is evidence the party reads.
- ψ, *standing, evaluator to party*: t_P = ψm_E. The evaluator's reading redistributes resources and authority inside the party toward the specialist whose line it favours.

A21's chain, "Public interpretation → Political and regulatory decisions → Distribution of resources and authority → Conditions of future media production → Public interpretation", is θ and ψ.

**The derivation.** At the symmetric state the Jacobian is J = [[J_E, C_EP], [C_PE, J_P]], with J_i CASE-363's 2×2 block and rank-one cross blocks (only meaning crosses). For any nonnegative J whose diagonal blocks are stable, I − J is a nonsingular M-matrix exactly when its Schur complement is, and by Varga's regular-splitting theorem that holds exactly when the round-trip gain ρ(G_P C_PE G_E C_EP) is below 1, G_i = (I − J_i)⁻¹. So the pair leaves symmetry exactly when the round trip exceeds 1. With rank-one channels the round trip is L_E L_P, and det(I − J_i) = ρ_i(1 − δ_i)Δ_i gives

  L_E = (θ + σ_E ω)/Δ_E,  L_P = (χ + σ_P ψ)/Δ_P,  Δ_i = (1 − φ′_i) − g_iσ_i²/2,

where Δ_i > 0 is CLAIM-947's condition that institution i is stable alone. The condition is (θ + σ_E ω)(χ + σ_P ψ) > Δ_E Δ_P, CLAIM-330's form one level up. ρ_i and δ_i cancel. The leading eigenvector is positive in all four components. Below threshold, a standing bias b₀ of the party's corpus moves the stationary meanings by m_P* = b₀/(Δ_P(1 − L_E L_P)) and m_E* = L_E b₀/(Δ_P(1 − L_E L_P)).

## Results

**The condition (tests, e1).** The analytic Jacobian matched finite differences on 200 random parameter sets in both resource readings. The block theorem held on 2,000 random nonnegative block matrices each of sizes 2+2, 3+2, 3+3 and 4+5, and the scalar round trip equalled the matrix one on 300 sets. On 1,802 random parameter sets with each institution stable alone and |λ − 1| ≥ 0.01 (198 nearer the threshold skipped), the nonlinear map left symmetry exactly when the condition held (1,802 of 1,802; 715 unstable). In one unstable case the captured state was the same to 3e-11 for ρ in {0.05, 0.2, 0.8} and δ in {0, 0.5, 0.9}.

**CLAIM-404's cases (e2).** Both institutions at σ = 0.4, φ = 0.3, ε = 0.2, g = 4, so Δ = 0.44 each and each is stable alone; the state is (m_E, a_E, m_P, a_P).

| case | channels | round trip | from a small push |
|---|---|---|---|
| A21's chain, below | θ = 0.4, ψ = 1 | 0.83 | returns to symmetry |
| A21's chain, above | θ = 0.6, ψ = 1 | 1.24 | (0.385, 0.298, 0.288, 0.548) |
| no loop inside either (g = 0 in both, Δ = 0.76) | θ = 1, ψ = 1.6 | 1.11 | (0.360, 0, 0.273, 0.519) |
| evaluator in Regime B (g_E = 0) | θ = 1, ψ = 1 | 1.20 | (0.367, 0, 0.279, 0.530) |
| informational independence, resources only | θ = 0, ω = 1.5, ψ = 1 | 1.24 | (0.239, 0.455, 0.200, 0.379) |
| return channel cut | θ = 3, ω = 3, ψ = χ = 0 | 0 | returns (spectral radius 0.958) |
| each near its own threshold (g = 9, Δ = 0.04) | θ = 0.1, ψ = 0.3 | 7.5 | (0.284, 0.471, 0.276, 0.524) |

In every captured case both institutions lean the same way, and from opposite small leans the pair went to the side of the larger one. With the evaluator in Regime B its authority stayed exactly balanced (a_E = 0) while its reading settled at m_E = 0.367 on a balanced corpus.

**Amplification below threshold (e3).** With the party's corpus biased by b₀ = 0.02 and θ = 0.4, raising ψ moved the round trip from 0 to 0.95; the evaluator's stationary reading rose from 0.041 to 0.235, matching the linear formula to within 2% up to a round trip of 0.5, after which the nonlinearity held it below the formula (0.235 against 0.83 at 0.95).

**Agent level (e4).** Two of LEAD-090's agent-level institutions (k = 50 items per specialist, one frame a round), coupled through θ and ψ, φ = 0.2 so Δ = 0.52; 200 seeds from exact symmetry, 800 rounds, a run counted captured when |m_E| over its last 200 rounds exceeded 0.19 (half the reduced captured value at round trip 1.42).

| round trip | captured | mean \|m_E\| | same sign |
|---|---|---|---|
| 0.59 | 0.5% | 0.053 | 87% |
| 0.89 | 15.5% | 0.109 | 95% |
| 1.42 | 87% | 0.313 (reduced 0.380) | 98.5% |
| 2.37 | 100% | 0.618 (reduced 0.648) | 100% |
| 0 (θ = 0.8, ψ = 0) | 0% | 0.039 | 78% |

**Resources as capacity (e5).** If the party's resources scale the evaluator's conferral gain, g_E(1 + ωm_P), rather than tilt it, the channel has no linear term at symmetry: the spectral radius stayed 1.0048 for ω from 0 to 2. It does change the nonlinear map. Above threshold it enlarged the captured reading on the side it favours (m_E from 0.385 to 0.754 at ω = 2) and shrank the other (−0.151). Below threshold (spectral radius 0.996 and 0.987), a start at 0.9 on the favoured side was captured at ω = 2 and ω = 5 respectively, and a start at −0.9 returned to symmetry. With θ = 0 (spectral radius 0.958), ω = 5 with ψ = 2, and ω = 10 with ψ = 1 or 2, were captured from the favoured side only.

**Corrective return channels (e5).** With χ, ψ ≤ 0, the evaluator's reading working against the party's lean, the condition above does not apply. Of 20,000 random draws with each institution stable alone, 2,159 were unstable, 2,158 of them through a complex pair (oscillation) and none through a real eigenvalue above 1, as CLAIM-340's corrective regime fails by oscillation for one institution.

## What it shows

That the interpretation–authority loop can close between two institutions, each stable alone, at a condition of CLAIM-330's form: the product of the cross-channel strengths against the product of the institutions' own margins. Each institution's own loop enters only through its margin, so an institution near its own threshold is captured by a weak cross loop, and two with no loop inside either can still be captured by the loop between them. CLAIM-tmp0v3wu states the condition; CLAIM-tmpz8q70 what it says about formal and informational independence; CLAIM-tmp42aba the capacity reading of resources.

## What it does not show

- That the channels are the right reading of CLAIM-404. They are the assistant's; the capacity reading of resources is a second, and they disagree below the threshold.
- Anything about corrective channels beyond the count above; no condition for the oscillatory instability was derived.
- That the two institutions should share one meaning axis. If the party's interest fixes its corpus bias, the pair has no symmetric state, and what survives is the amplification 1/(1 − L_E L_P).
- That the numbers bear on any regulator or newsroom. The model is the assistant's reading of CASE-092 and CLAIM-404, and its parameters are illustrative.
