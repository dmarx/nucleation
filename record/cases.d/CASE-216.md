---
number: 216
status: Active
formerly:
- CASE-tmpa6s9d
title: 'A four-state annealing toy, unfolded, nucleus, folded and a misfold trap, with free energies and transition states linear in temperature: the fraction folded at one hour peaks at 90.4 % at 318.6 K among constant temperatures, at sixteen hours it is at least 90 % from 313 to 323.5 K, and five minutes at 327 K followed by 318 K leaves 98.5 % folded at the hour, which no constant temperature does; the chance of having reached the folded state agrees to four places'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057): a construction (ADR-042) whose numbers were re-
    run by a second checker (scratch/formal/dna_origami_toys.py and an
    independent script, python3 -I). One sentence corrected: it read
    "F is stable up to 340.9 K but cannot be formed within an hour
    above about 326 K"; 3.0 % forms at 326 K. Standing fictional is
    kept.
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
  target within a time budget is a window in temperature, not an up-set,
  whether it is counted as the fraction folded at the horizon or as the
  chance of having reached the folded state by then; more time widens the
  window; a two-step schedule reaches what no constant temperature reaches
  in the same time. The parameters are chosen to show
  the effect and are not fitted to any origami. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-581 CLAIM-570 CLAIM-569 CLAIM-571 — Proposed; the budgeted-reachability claims the toy bears on, and the claim it is built for -->

# CASE-216: A four-state annealing toy, unfolded, nucleus, folded and a misfold trap, with free energies and transition states linear in temperature: the fraction folded at one hour peaks at 90.4 % at 318.6 K among constant temperatures, at sixteen hours it is at least 90 % from 313 to 323.5 K, and five minutes at 327 K followed by 318 K leaves 98.5 % folded at the hour, which no constant temperature does; the chance of having reached the folded state agrees to four places

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
  318.6 K, with 90.4 % folded. This is a numerical result: a 0.1 K grid
  from 290 to 345 K, refined by a bounded continuous search near the peak,
  gives 90.395 % at 318.618 K. On the grid no constant temperature reaches
  95 %. Within sixteen hours at least 90 % fold from 313 to
  323.5 K; the folded fraction over 300 to 334 K in steps of 2 K is 0.30,
  0.35, 0.41, 0.48, 0.56, 0.68, 0.84, 0.97, 1.00, 1.00, 1.00, 1.00, 0.85,
  0.39, 0.12, 0.03, 0.01, 0.00, rising and then falling.
- **A schedule.** Five minutes at 327 K, above M's melting point, makes
  the nucleus without the trap; 55 minutes at 318 K then completes the
  fold. At one hour: F 98.5 %, M 1.2 %, N 0.3 %.

## Folded at the horizon, and reached by it

The figures above are occupancies, Pr(X_T = F), the fraction folded at the
observation time. With folding reversible, that is not the chance of
having reached the folded state, Pr(τ_F ≤ T), which counts a structure
that folds and then melts. The two are computed separately in
scratch/formal/dna_origami_toys.py, with F made absorbing for the second.
Here they agree to four places, at every temperature from 290 to 345 K and
for the schedule, because F almost never melts on these timescales below
its melting point. The distinction matters in general. Pr(τ_F ≤ T) cannot
fall as T grows, so a window defined by it can only widen with time. A
window defined by occupancy need not, and here it widens because F
holds.

## What it can show

- **A resource that sets the costs it pays.** In the record's budgeted
  reachability the costs are fixed and a budget only admits more moves, so
  more budget never loses a reachable state ([CLAIM-581](../claims.d/CLAIM-581.md), [CLAIM-570](../claims.d/CLAIM-570.md)).
  Here raising T speeds every crossing and at the same time raises the
  entropic barriers and melts the target, so what is reachable is a band of
  T, not everything above a threshold. This is the construction for
  [CLAIM-594](../claims.d/CLAIM-594.md).
- **A budget and a condition that do not reduce to one.** Time is spent and
  is a budget in the record's sense. Temperature is not consumed: it is a
  controlled condition that sets reaction rates and equilibria together.
  The window in T widens with t.
- **A path, not a level.** The schedule does what no level does, as
  Wagenbauer, Wachauf and Dietz's three-step folding matched a 16-hour ramp
  in 1.5 hours, and as Sobczak's dissertation found a short-domain design
  that folds better after rapid cooling and not at all after slow.
- **Holding is not reaching** ([CLAIM-569](../claims.d/CLAIM-569.md), [CLAIM-571](../claims.d/CLAIM-571.md)). F is stable up to
  340.9 K but barely forms within an hour above about 326 K: 3.0 % at
  326 K, 0.8 % at 328 K.

Being fictional, it cannot show that DNA origami behaves this way, nor at
these numbers. The readings that bear on that are filed beside it.
