---
status: Active
title: 'E1: synthetic three-state stochastic computations (C2–C3)'
version: 1
standing: stipulated
tags:
- probabilistic-modeling
- mathematics
date: '2026-10-08'
line: pragmatic-transport
illustrates:
- CLAIM-tmpbwst7
- CLAIM-tmpx6akp
- CLAIM-tmpn361s
summary: >-
  Run at U23 ("run it"): hand-chosen row-stochastic matrices on three
  abstract states, seed 20261008, "not fitted to text, pretrained
  models, or human measurements". Executed; results are exact properties
  of the chosen matrices. None reached a later draft.
supports:
- CLAIM-tmp8w5c7
---
<!-- inactive-ok-file: CLAIM-tmpghha4 CLAIM-tmpn361s CLAIM-tmpx6akp — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CASE-tmpiueso: E1: synthetic three-state stochastic computations (C2–C3)

## The case

U23 quoted A55's "It contains proposed experiments but no invented experimental
findings" and said "run it". A57: "There's no callable text-generation model or
model API credential in this runtime, so I can't honestly run the proposed LLM
or human-subject experiments. I can run the mathematical/computational tests."
C2 (run_experiments.py) and C3 (EXPERIMENT_REPORT.md): three abstract states
(affiliative/complicit, neutral, condemnatory); "Stochastic transition matrices
... were selected to demonstrate theoretical distinctions. These matrices were
**not fitted to text, pretrained models, or human measurements**." Seed
20261008.

Results, as C3 states them:

| Test | Observation |
|---|---|
| Framing order (neutral start, A→B vs B→A) | TV = 0.4355; JS = 0.18291 bits |
| Matched initial results, different response after framing | baseline TV = 0; post-framing TV = 0.4475 |
| Contractive transmission | Dobrushin = 0.70; between-start separation after step 30 ≈ 0; departure from original = 0.37037 |
| Identity transmission | Dobrushin = 1; separation = 1; departure = 0 |
| Alternating transmission | Dobrushin = 0.80; separation = 0.00124; departure = 0.62438 |
| Bound verification, TV(xM, yN) ≤ dob(N)·TV(x, y) + max_i TV(M_i, N_i) | 10,000/10,000 trials satisfied within floating-point tolerance |

C3 also simulated "3,000 sample paths per kernel for potential further
analysis" and reports nothing from them. The static/dynamic equality is
"constructed by design", and the bound check is "a numerical check of an
analytic inequality, not its proof".

## What it can show

Existence, by construction. C3: "classical stochastic frames can be
noncommutative; static agreement does not entail agreement over future
interventions; and convergence among transmission chains does not imply
preservation of the original message. No statistical inference about texts,
speakers, models or audiences follows." A59: "These are constructive
mathematical examples—not evidence that LLMs or humans exhibit those numerical
effects." The second row is a stipulated instance of [CLAIM-tmpx6akp](../claims.d/CLAIM-tmpx6akp.md); the first, of [CLAIM-tmpbwst7](../claims.d/CLAIM-tmpbwst7.md).
The contractive row is the two forgettings of [CLAIM-tmpn361s](../claims.d/CLAIM-tmpn361s.md). The "alternating"
kernel is contractive too (0.80), so no run exercised the amplifying regime of
[CLAIM-tmpghha4](../claims.d/CLAIM-tmpghha4.md) (the chunk coder's observation, checked against C3's table).
