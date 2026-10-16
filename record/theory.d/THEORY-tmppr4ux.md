---
status: Active
title: "On one physical piano-movers puzzle scaled to the solver, ant groups solve better as they grow, while human groups barred from speech and gesture solve worse than individuals and talking groups only about as well as one; large ant groups keep speed and heading through wall contact, and the human mechanisms offered are fitted or observed informally, not tested"
version: 1
tags:
- complex-systems
- cognition
- social-science
date: '2026-10-16'
source:
- LIT-075
summary: >-
  Dreyer et al. (2024), [LIT-075](../literature.d/LIT-075.md), read in [NOTE-040](../notes.d/NOTE-040.md). Large ant groups (n =
  28) reach about 90–100% success by 400 corridor widths, small groups (n
  = 48) about 50%. Restricted human groups do 32% worse than individuals'
  median, talking groups 7% better. There are no inferential statistics.
  The ant persistence mechanism is supported by collision data and a model
  whose carrier numbers fall short of calibration; the human majority vote
  (greediness P = 0.2) is tuned by eye, and "follow a random leader" rests
  on unrecorded observation. One ant species, one puzzle, one human
  population.
---
<!-- inactive-ok-file: THEORY-tmp05zxn — Proposed; the account that leans on this finding, named for context -->

# THEORY-tmppr4ux: On one physical piano-movers puzzle scaled to the solver, ant groups solve better as they grow, while human groups barred from speech and gesture solve worse than individuals and talking groups only about as well as one; large ant groups keep speed and heading through wall contact, and the human mechanisms offered are fitted or observed informally, not tested

## Source

Dreyer et al. (2024), [LIT-075](../literature.d/LIT-075.md), "Comparing cooperative geometric puzzle
solving in ants versus humans", *PNAS*, read in full in [NOTE-040](../notes.d/NOTE-040.md) with the
supplement.

## What was actually shown

**The task.** A T-shaped load moved through three chambers and two slits,
built at five scales so that body size to load size stays roughly
constant. Humans in groups pull only on assigned handles. Performance is
path length in configuration space, normalised by the corridor width
d_cor; for humans, also attempted transitions on a hand-built state graph.

**Ants (Fig. 2A).** Large groups (n = 28) reach about 90–100% success by
about 400 d_cor, small groups (n = 48) about 50%. Single ants are three
composite multi-day runs. After a collision large groups keep more of their
speed and turn less (Fig. S5a,b). In simulation, alignment persists 5.9 s
and 4.8 d_cor for large groups against 0.7 s and 1.9 d_cor for small ones
(Table S4). An existing transport model with size-independent rules
reproduces the gap.

**Humans (Fig. 2B; SI Note 7).** Individuals reach 100% within about 50
d_cor; 91 ± 1% of their transitions are consistent with depth-first search.
Restricted groups (n = 48) are 32% worse than the individuals' median,
talking groups (n = 43) 7% better. Restricted groups start moving within
about a second and take the greedy option more often. The talking-group
gain comes from leaving a dead-end state: 91% of groups return after trying
it, against 38% of individuals.

**What could have come out otherwise.** Restricted human groups could have
matched or beaten individuals, as ant groups beat smaller ones. They did
worse.

## What this does not say

- **That the differences are significant.** The paper gives mean ± 1 SE
  and CDF bands and no test. "Significantly" in the text has no test
  behind it, and nothing is controlled for age, composition or repeat
  exposure.
- **That human groups fail by majority vote.** A one-shot vote with
  greediness P = 0.2, set "by adjusting only parameter P", fits "reasonably
  good … in nine out of ten" forks. No alternative model is compared, and
  at three of five forks the vote is among a random quarter of the group.
- **That talking groups follow a random leader.** That comes from
  "personal observations", since voices were not recorded (SI Note 6).
  The claim that leader-following is "strictly superior" to majority vote
  when most choices are wrong is a 200-run stylised simulation.
- **That ant groups have collective memory.** The "short-term collective
  memory" is persistence of heading relabelled. The order parameter is
  measured only in simulation, whose large-group carrier count (50.8) is
  well below experiment (79.9).
- **That simple minds scale and complex ones need communication.** That is
  the abstract's generalisation from one ant species (*P. longicornis*),
  one puzzle and one population recruited in Israel.

## Connections

- **Collective intelligence as resources against coordination costs
  ([THEORY-tmp05zxn](THEORY-tmp05zxn.md))** takes this as its clearest empirical instance: more
  pullers help ants, whose individual cognition contributes little, and
  aggregation through weak channels costs humans the plan each brings.
- **Synchronised functional units ([LIT-933](../literature.d/LIT-933.md)).** Nowak et al. count any
  binding of dynamics as a functional unit. Here a group bound by forces
  alone performs worse than one member, which is a case their scenario
  does not distinguish.
