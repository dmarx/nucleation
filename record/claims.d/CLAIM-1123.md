---
number: 1123
status: Proposed
formerly:
- CLAIM-tmpk8x2j
title: 'When a driven system feeds back on its drive, the per-switch identity and the summed lower bound of the thermodynamics of prediction still hold, but the nostalgia that bounds the dissipation can be negative, and so can the dissipation and the excess work, so the bound no longer makes nonpredictive memory a cost'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A proof that, for a drive that depends on the system's state, the
  per-switch identity or the summed bound fails as the bookkeeping here
  states them; or an error in that bookkeeping such that, corrected, no
  instance has negative summed nostalgia. A result that adds the
  controller's cost and restores a nonnegative total does not defeat it,
  since the claim is about the system-side quantities the source defines.
tags:
- thermodynamics
- information-theory
- agency
date: '2026-11-23'
line:
- learned-structure
- formal-apparatus
grounds:
- CASE-391
- THEORY-026
bears_on:
- QUESTION-494
summary: >-
  [QUESTION-494](../questions.d/QUESTION-494.md)'s note asks which conclusions of the passive account survive
  feedback. [THEORY-026](../theory.d/THEORY-026.md)'s identity, β⟨W_diss⟩ = I[s_t;x_t] − I[s_t;x_{t+1}]
  per switch, uses no assumption about the drive, and its summed bound
  needs only that relaxation lowers the nonequilibrium free energy, which a
  kernel that keeps each equilibrium stationary does whatever chose the
  signal. Both survive feedback, and the run checks them in 500 random
  systems. What fails is the sign: once the next signal depends on the
  state, the state can carry more about x_{t+1} than about x_t, and in the
  run the summed nostalgia is negative in 323 of 500 systems and the
  dissipation and excess work in 6. So the bound stops pricing
  nonpredictive memory and can permit work extraction, paid for by the
  controller's use of the state, which the source's accounting leaves out.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-391 — filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: THEORY-817 — Proposed; cited as an account this claim does not touch -->

# CLAIM-1123: When a driven system feeds back on its drive, the per-switch identity and the summed lower bound of the thermodynamics of prediction still hold, but the nostalgia that bounds the dissipation can be negative, and so can the dissipation and the excess work, so the bound no longer makes nonpredictive memory a cost

## The claim

Take [THEORY-026](../theory.d/THEORY-026.md)'s setting and let the next signal value depend on the
system's state: x_{t+1} ~ D(· | x_t, s_t). Then:

1. **The per-switch identity holds.** β(⟨W_t⟩ − ΔF_neq) =
   H[S_t | X_{t+1}] − H[S_t | X_t] = I[s_t;x_t] − I[s_t;x_{t+1}]. The
   derivation in [THEORY-026](../theory.d/THEORY-026.md)'s note of 2026-10-19, step 1, uses only the
   definitions.
2. **The summed bound holds.** Relaxation happens at a fixed signal value,
   so a kernel that keeps each equilibrium stationary still contracts the
   relative entropy to it. Step 3 of the same note goes through unchanged,
   and β⟨W_diss⟩ ≥ Σ_t (I[s_t;x_t] − I[s_t;x_{t+1}]).
3. **The sign fails.** Step 2 of that note, nonnegativity, needs
   s_t – x_t – x_{t+1} to be a Markov chain, and feedback breaks it: the
   state steers the next signal, so it can predict that signal better than
   it tracks the current one.

[CASE-391](../cases.d/CASE-391.md) exhibits the failure. In 500 random 4-state systems with
3-symbol feedback drives, some step's nostalgia is negative in 405, the
summed nostalgia in 323, and the dissipation and the excess work in 6
(smallest excess work −0.29 k_BT). The identities hold to 2e-15 and the
bound in all 500.

## What follows

Without feedback the bound says that keeping what does not predict costs
at least what it fails to predict. With feedback it says only that the
dissipation is at least a number that may be negative. A negative excess
work is net work drawn from the bath by a system whose drive is steered by
its own state: a Maxwell's-demon arrangement, and the controller that reads
the state is unpriced. [THEORY-817](../theory.d/THEORY-817.md)'s assertion that prediction is not what
efficiency asks for under feedback concerns the agent's work, not this
bound, and is neither supported nor touched.

## Limits

- The demonstrated part is the survival of the identity and the bound (by
  the derivation) and the existence of negative values (by exhibited
  instances). How often they occur depends on the random ensemble and
  means nothing beyond it.
- The claim does not say what the right accounting under feedback is.
  Adding the controller's measurement cost is the standard move in the
  thermodynamics of feedback; the record has not read that literature, and
  no work on it is cited here.
