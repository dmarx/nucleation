---
status: Proposed
title: 'A four-state annealing toy, unfolded, nucleus, folded and a misfold trap, with free energies and transition states linear in temperature: within an hour the target is reached only in a narrow band of constant temperatures, best 90.3 % at 318.6 K, within sixteen hours in a wider band, 313 to 323.5 K, and five minutes at 327 K followed by 318 K reaches 98.5 % within the hour, which no constant temperature does'
version: 1
standing: fictional
kind: construction
tags:
- natural-sciences
- complex-systems
- mathematics
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-569
- CLAIM-571
summary: >-
  The assistant's, on the owner's request of 2026-11-05 to connect the
  record's inquiry to DNA origami. A minimal model of thermal annealing in
  which the resource that pays for crossing barriers, temperature, also
  sets the free energies and barriers it pays for. Four states: U
  (unfolded), N (a nucleus, as in Schneider, Möritz and Dietz's compacted
  intermediate), F (the folded target) and M (a misfold trap). Each state
  and each transition state has an enthalpy and an entropy, so its free
  energy is linear in temperature, and rates are Arrhenius. Computed with
  python3 -I by matrix exponentials of the rate matrix. Reachability of the
  target within a time budget is a window in temperature, not an up-set;
  more time widens the window; a two-step schedule reaches what no constant
  temperature reaches in the same time. The parameters are chosen to show
  the effect and are not fitted to any origami. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-581 CLAIM-570 CLAIM-569 CLAIM-571 CLAIM-tmp7y162 — Proposed; the budgeted-reachability claims the toy bears on, and the claim it is built for -->

# CASE-tmpa6s9d: A four-state annealing toy, unfolded, nucleus, folded and a misfold trap, with free energies and transition states linear in temperature: within an hour the target is reached only in a narrow band of constant temperatures, best 90.3 % at 318.6 K, within sixteen hours in a wider band, 313 to 323.5 K, and five minutes at 327 K followed by 318 K reaches 98.5 % within the hour, which no constant temperature does

## The case

States and transition states, with enthalpy H (kcal/mol) and entropy S
(kcal/mol/K) relative to U, free energy G = H − TS:

| | H | S | melts at H/S |
|---|---|---|---|
| U | 0 | 0 | |
| N | −120 | −0.36 | 333.3 K |
| F | −300 | −0.88 | 340.9 K |
| M | −150 | −0.46 | 326.1 K |
| transition U–N | −40 | −0.155 | |
| transition N–F | −260 | −0.84 | |
| transition U–M | −60 | −0.22 | |

Moves are U ↔ N, N ↔ F and U ↔ M. The rate from state i through
transition state ‡ is ν exp(−(G‡ − G_i)/RT), with ν = 10⁶ s⁻¹ and
R = 0.001987 kcal/mol/K. Every run starts in U. The time budget t is
additive (time spent); the temperature T is the level held, or a schedule
of levels.

- **Hot (above 326 K).** M is unstable and does not trap, but the step
  from N to F is entropically costly: its barrier from N is −140 + 0.48T,
  15.5 kcal/mol at 324 K and 19.4 at 332 K. Within an hour little folds:
  0.8 % at 328 K.
- **Cold (below about 308 K).** Every barrier out of U is small, M forms
  as fast as N, and M's escape barrier, 17 to 19 kcal/mol, holds it for
  more than sixteen hours: 78 % trapped at 296 K, at one hour and at
  sixteen alike.
- **The window.** Within one hour the best constant temperature is
  318.6 K, with 90.3 % folded, and no constant temperature from 290 to
  345 K reaches 95 %. Within sixteen hours at least 90 % fold from 313 to
  323.5 K; the folded fraction over 300 to 334 K in steps of 2 K is 0.30,
  0.35, 0.41, 0.48, 0.56, 0.68, 0.84, 0.97, 1.00, 1.00, 1.00, 1.00, 0.85,
  0.39, 0.12, 0.03, 0.01, 0.00, rising and then falling.
- **A schedule.** Five minutes at 327 K, above M's melting point, makes
  the nucleus without the trap; 55 minutes at 318 K then completes the
  fold. At one hour: F 98.5 %, M 1.2 %, N 0.3 %.

## What it can show

- **A resource that sets the costs it pays.** In the record's budgeted
  reachability the costs are fixed and a budget only admits more moves, so
  more budget never loses a reachable state ([CLAIM-581](../claims.d/CLAIM-581.md), [CLAIM-570](../claims.d/CLAIM-570.md)).
  Here raising T speeds every crossing and at the same time raises the
  entropic barriers and melts the target, so what is reachable is a band of
  T, not everything above a threshold. This is the construction for
  [CLAIM-tmp7y162](../claims.d/CLAIM-tmp7y162.md).
- **Two resources that do not reduce to one.** Time and temperature are
  both spent, but only time is a budget in the record's sense; temperature
  is a setting of the landscape. The window in T widens with t.
- **A path, not a level.** The schedule does what no level does, as
  Wagenbauer, Wachauf and Dietz's three-step folding matched a 16-hour ramp
  in 1.5 hours, and as Sobczak's dissertation found a short-domain design
  that folds better after rapid cooling and not at all after slow.
- **Holding is not reaching** ([CLAIM-569](../claims.d/CLAIM-569.md), [CLAIM-571](../claims.d/CLAIM-571.md)). F is stable up to
  340.9 K but cannot be formed within an hour above about 326 K.

Being fictional, it cannot show that DNA origami behaves this way, nor at
these numbers. The readings that bear on that are filed beside it.
