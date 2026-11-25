---
number: 317
status: Proposed
formerly:
- CASE-tmpgustv
title: 'Coupled meaning–influence model run'
statement: >-
  The coupled meaning–influence model built with three declared demands and
  a feasible-update oracle: changing only the conferral rule, with search
  and information fixed, moves the share of steps on which a satisfiable
  demand goes unmet from about 0.95 under scoring by agreement with the
  update made to about 0.05 under scoring by each demand's own residual;
  step size, noise and conditioning move it less, and the best fixed
  weighting chosen in hindsight does as well as the second rule
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-081 at the owner's
    triage of leads it could handle on its own. The code, tests and result
    files are committed beside it under scratch/studies/lead-081/.
standing: documented
kind: executed-study
tags:
- self-governance
- complex-systems
- operations-research
date: '2026-11-22'
line:
- distributed-agency
- will-organization
variant_of:
- CASE-099
bears_on:
- QUESTION-124
summary: >-
  A39's case study 2, which [LEAD-081](../leads.d/LEAD-081.md) asks for: [CASE-099](CASE-099.md)'s two-field loop
  (authority shapes the update, the update shapes conferral) built as a
  simulation with three declared demands, [CLAIM-365](../claims.d/CLAIM-365.md)'s local requirements, an
  exact oracle for the frustration residual Φ and an allocation oracle for
  the best any weighting could do with the same update map and gradients.
  On 200 instances whose demands are jointly satisfiable, paired by seed,
  only the conferral rule was changed. Scoring components by agreement with
  the update made ([CASE-092](CASE-092.md)'s Regime A) captured influence in 99% of runs and
  left a requirement violated, though some allocation met them all, on 0.95
  of steps; scoring each by its own demand's residual (Regime B) gave 0.05,
  and the allocation oracle 0. Step size, curvature and gradient noise moved
  Regime A between 0.58 and 0.96, and lowered it only where they stopped
  capture. A fixed uniform weighting failed (0.89), and the best of 66 fixed
  weightings chosen per instance in hindsight did as well as Regime B (0.05).
  With jointly infeasible demands the frustration is structural under every
  rule but A, whose capture makes the one-step oracle report it as
  satisfiable on 87% of steps. A fictional model, by construction; the
  numbers are of this model. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-500 — Proposed or new; the thesis this study tests, and the entries this filing made -->

# CASE-317: Coupled meaning–influence model run

## What was done

[LEAD-081](../leads.d/LEAD-081.md) asks for [CASE-099](CASE-099.md) "with declared demands and an oracle for feasible updates", varying "only how influence is allocated among the components". [CLAIM-500](../claims.d/CLAIM-500.md) and [CLAIM-357](../claims.d/CLAIM-357.md) name it as the test of the governance-induced kind of frustration: "intervening on the allocation of influence with search and information held fixed". The model, its tests and the sweep are in scratch/studies/lead-081/ (model.py, test_model.py, sweep.py, fixed_hindsight.py; results/summary.md has every cell). The run took about 4.5 minutes of wall time on 4 cores.

**The organization.** A state θ in the plane and three components, one per demand. Demand i is met when L_i(θ) = ½(θ − c_i)ᵀH(θ − c_i) ≤ τ_i. The centres lie round the unit circle. In the 200 satisfiable instances a point near the origin is inside every region; in 100 structural instances no point is.

**The declared requirement.** Each step declares [CLAIM-365](../claims.d/CLAIM-365.md)'s local requirement ε_i + g_iᵀd ≤ 0 with ε_i = min(L_i − τ_i, η), η = 0.05. An unmet demand asks for progress η, and a met one asks only not to be broken. Admissible updates are ‖d‖₂ ≤ r.

**The oracles.** The feasible-update oracle computes Φ_r = min_d max_i(ε_i + g_iᵀd) exactly, by enumerating the vertices of the arrangement. The tests check it against [CLAIM-365](../claims.d/CLAIM-365.md)'s dual, against [CASE-115](CASE-115.md)'s Φ_r = ε, and against [CLAIM-357](../claims.d/CLAIM-357.md)'s counterexample. The allocation oracle computes Φ_alloc, the best worst residual reachable by changing only the weights, with the same update map and the same gradients. In every run Φ_r ≤ 0 implied Φ_alloc ≤ 0, so each realized violation here is one some allocation would have avoided.

**What is held fixed.** Influence weights w on the simplex set the update d(w) = −g_w·min(1, r/‖g_w‖), with g_w = Σw_j g_j (A34's rule, clipped). That map is the search, and the gradients are the information. Both are the same under every rule.

**The conferral rules.** Each updates w ← δw + (1 − δ)·softmax(γs). Regime A scores component j by cos(−g_j, d): its proposal's agreement with the update its own authority helped make. That is [CASE-099](CASE-099.md)'s γ arrow, and d(w) is its β arrow. Regime B scores it by (ε_j + g_jᵀd)/η: how its demand fared, which does not pass through agreement with d. Two fixed weightings, uniform and random per instance, are compared, and so is the allocation oracle's minimizer taken each step.

**The measure.** "Frustration" below is the share of the last 100 of 200 steps on which the actual update violates a requirement while Φ_alloc ≤ 0. In [CLAIM-357](../claims.d/CLAIM-357.md)'s terms that is a realized violation, and here every one was allocation-remediable.

## Results

| Rule (base: r = 0.1, γ = 8, δ = 0.9) | Frustration | All met at end | Captured |
|---|---:|---:|---:|
| Regime A | 0.953 ± 0.005 | 0.00 | 0.99 |
| Regime B | 0.052 ± 0.016 | 0.92 | 0.00 |
| Allocation oracle | 0.000 | 1.00 | 0.01 |
| Fixed, uniform | 0.890 ± 0.043 | 0.11 | 0 |
| Fixed, random per instance | 0.960 ± 0.027 | 0.04 | 0.02 |
| Best of 66 fixed, in hindsight (60 instances) | 0.050 (0 on 57) | — | — |

Paired by instance, Regime A was worse than Regime B on all 200 instances, by 0.90 ± 0.02.

| Optimizer or information change | Regime A | Regime B | Fixed uniform |
|---|---:|---:|---:|
| none | 0.953 | 0.052 | 0.890 |
| step r = 0.05 / 0.2 / 0.4 | 0.906 / 0.962 / 0.961 | 0.004 / 0.074 / 0.072 | 0.615 / 0.890 / 0.890 |
| gradient noise σ = 0.1 / 0.3 | 0.703 / 0.678 | 0.170 / 0.357 | 0.701 / 0.647 |
| conditioning H = diag(1, 5) | 0.582 | 0.210 | 0.515 |

Under Regime A the noise and conditioning changes that lowered frustration also ended capture: no run was captured, against 99% at base. Step size left capture in place and left frustration unchanged. Why conditioning stops capture was not worked out.

Regime A's conferral parameters were swept over γ ∈ {0, 1, 2, 4, 8, 16} and δ ∈ {0.5, 0.8, 0.9, 0.95}. No run captured at γ ≤ 1 at any memory. About a quarter to a half captured at γ = 2, and 81–100% at γ ≥ 8. Frustration ran from 0.61 to 1.0 throughout, and was lowest at moderate γ with short memory. Which component won was the one whose region the start was nearest in 54% of runs (chance 33%). It was the initial leader in weight in 34%, which is chance: the ±0.02 initial asymmetry did not decide it.

**Structural control.** With no common region, Φ_r > 0 on every step under Regime B, both fixed rules and the oracle. Under Regime A it was positive on only 10% of steps: once influence is captured and θ sits in one demand's region, a step that progresses on the others without breaking it exists locally, so 87% of steps count as realized violations.

## What it shows

In this model, with search and information held fixed, frustration of satisfiable demands follows the allocation of influence. Changing only the conferral rule moves it by 0.90. That is more than any step size, noise or conditioning change tried moved it under Regime A, and those that moved it most worked through the allocation, by stopping capture. This is the result [LEAD-081](../leads.d/LEAD-081.md)'s "what would count" names as support for [CLAIM-500](../claims.d/CLAIM-500.md) and [CLAIM-357](../claims.d/CLAIM-357.md): "frustration that changes with the allocation of influence while search and information are fixed". Information does matter as well. Noise raises frustration under Regime B and the oracle, but the gap between the rules survives it (0.70 against 0.17 at σ = 0.1; 0.68 against 0.36 at σ = 0.3).

It does not show that the frustration needs conferral dynamics. Regime A's captured state is a fixed weighting at a vertex. A fixed uniform weighting fails about as often. A fixed weighting chosen per instance with knowledge of the demands does as well as Regime B. [CLAIM-500](../claims.d/CLAIM-500.md)'s defeater lists "a fixed weighting rule" among the optimizer mechanisms. Two readings of the result are left to the owner:

1. **The test supports [CLAIM-500](../claims.d/CLAIM-500.md).** The cause is how influence is allocated, and a weighting is an allocation. What the loop adds is that it chooses the weighting endogenously, from the starting geometry, and holds it. Breaking the loop (Regime B) fixes the failure without anyone knowing the right weights.
2. **The test leaves [CLAIM-500](../claims.d/CLAIM-500.md)'s stronger form unsupported.** Every failure observed is a fixed-weighting failure once capture is complete. An optimizer analysis that takes the weighting as given describes it without modelling conferral. What it cannot do without an oracle is name the right weighting, which Regime B finds.

The structural control adds a caution for [CLAIM-357](../claims.d/CLAIM-357.md)'s diagnostics. [CLAIM-365](../claims.d/CLAIM-365.md)'s oracle is local, one step and first order. A captured allocation can move the state to where a jointly infeasible set of demands looks locally satisfiable, so the local test classifies as governance-induced what is globally structural.

## Limits

- A fictional model by construction (standing documented only as a record of the run): three demands, a plane, quadratic demands, one update map. Regime A is the rule [CLAIM-297](../claims.d/CLAIM-297.md) says captures, so capture is partly what was built in. [CLAIM-288](../claims.d/CLAIM-288.md)'s threat applies: the demands and the scores are the modeller's.
- The allocation oracle is a grid search of step 1/60, an upper bound on the exact minimum. The hindsight comparison used 60 instances and a grid of step 1/10.
- No other update map (search) was tried, so "search held fixed" is held at one choice. A40's representational kind, where no allocation reaches an available update, never occurred here.
- [QUESTION-124](../questions.d/QUESTION-124.md)'s persistence condition, a conflict present at t₀ and absent later with Γ bounded away from zero, was not measured as such. Regime A gives Γ ≈ 0.15 on the last half while Φ ≤ 0, from a start where demands were unmet.
- No modular or non-Euclidean geometry was tried.
