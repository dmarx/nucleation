---
number: 604
status: Proposed
formerly:
- CLAIM-tmpw4ai2
title: "Where a structure's upkeep draws on a flux in proportion to its own intact state, as a flame's does, it has an ignition threshold below which it goes out with the supply still on, a supply level below which it collapses rather than declines, and an outage after which restoring the supply does not relight it; upkeep supplied regardless of the structure's state has none of the three"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the model: an intact fraction under first-order damage at
  rate d and repair of each damaged part at rate κsI, so dI/dt = −dI +
  κsI²(1 − I), that has no
  unstable interior steady state when κs > 4d, that holds a non-zero state
  for supply s below 4d/κ, or that relights from below the lower steady
  state when s is restored; or one under supplied repair ρs(1 − I) that
  shows any of the three. Not defeated by systems whose uptake depends on
  their state in some other way, which the claim does not cover, nor by
  noise carrying a finite system across the threshold, which it sets aside.
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-05'
line:
- realizability
- distributed-agency
complements:
- CLAIM-597
- CLAIM-273
- CLAIM-516
grounds:
- THEORY-072
- THEORY-1270
bears_on:
- QUESTION-085
- QUESTION-399
- QUESTION-398
summary: >-
  The assistant's, at the owner's request of 2026-11-05 to connect
  [CLAIM-597](CLAIM-597.md)'s supplied maintenance to the record's dissipative structures.
  The record separates order held by an outside flow, the Bénard cell, from
  order that keeps up the conditions of its own maintenance, the candle
  flame ([THEORY-072](../theory.d/THEORY-072.md), [TERM-070](../terms.d/TERM-070.md), [QUESTION-085](../questions.d/QUESTION-085.md)). [CLAIM-597](CLAIM-597.md) modelled only the
  first. The second is modelled by letting uptake from the flux scale with
  the intact share: dI/dt = −dI + κsI²(1 − I). With d = 0.2 and κs = 2 the
  structure holds 0.887, as supplied repair at ρs = 1.575 does, but it goes
  out from 0.10 with the supply on, collapses when the supply falls below
  40 % of its level, and after an outage longer than about 10.3 time units
  does not relight when the supply returns. Supplied repair recovers from
  any start and declines smoothly. Both decay as e^(−dt) once the supply
  stops, so the self-maintaining structure is no less dependent on the
  flux. What it gains is independence from a provider who delivers repair,
  at the price of thresholds. That gives [QUESTION-085](../questions.d/QUESTION-085.md) three observable
  signatures. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmpbzli4 — Skimmed; a reading of the persistence filing, cited as open -->
<!-- inactive-ok-file: CLAIM-597 THEORY-072 — Proposed; entries this claim extends or rests its reading on, cited as open -->

# CLAIM-604: Where a structure's upkeep draws on a flux in proportion to its own intact state, as a flame's does, it has an ignition threshold below which it goes out with the supply still on, a supply level below which it collapses rather than declines, and an outage after which restoring the supply does not relight it; upkeep supplied regardless of the structure's state has none of the three

## The two kinds of upkeep

Let I be the intact share of a structure, damaged at rate d, and let s be
a flux that comes from outside.

- **Supplied repair** ([CLAIM-597](CLAIM-597.md)): dI/dt = −dI + ρs(1 − I). Repair arrives at
  a rate set by the supply, whatever the structure does. This is the heat
  under a Bénard cell, or a strand pool that refills DNA origami.
- **Self-sustaining uptake**: dI/dt = −dI + κsI²(1 − I). Each damaged part is
  repaired at a rate proportional to how much of the structure is intact,
  κsI. The structure draws the flux in through its own working state. A
  flame vaporizes the wax and draws in the oxygen that keep it burning
  ([THEORY-072](../theory.d/THEORY-072.md)). A state that taxes the people it serves
  collects its revenue through its own working.

## The claim

With d = 0.2 and κs = 2 (scratch/formal/supplied_maintenance_toys.py
reproduces and asserts every number):

1. **Ignition threshold.** Besides I = 0 the uptake model has two steady
   states, where I(1 − I) = d/κs: I₋ = 0.113, unstable, and I₊ = 0.887,
   stable. A structure started below I₋ goes out with the supply on. From
   0.10 it falls below 10⁻³ in 50 time units, while from 0.12 it reaches
   0.887. Supplied repair matched to hold the same share (ρs = 1.575)
   reaches 0.887 from 0.05 or anywhere else. Self-sustaining upkeep needs a
   nucleus. Supplied upkeep does not.
2. **Collapse, not decline.** The kept state exists only while κs ≥ 4d, so
   here while the supply is at least 40 % of its level. At 50 % the
   structure holds 0.724 and at 45 % 0.667. At 39 % it goes out. Supplied
   repair at 39 % still holds 0.754 = ρsf/(ρsf + d), and degrades smoothly
   all the way down.
3. **Hysteresis.** With the supply cut, both decay as e^(−dt). Restoring
   the supply relights the uptake structure only if it is still above I₋,
   so an outage longer than ln(I₊/I₋)/d = 10.3 time units cannot be
   undone by restoring the supply. After 5 units off it returns to 0.887,
   and after 30 it does not return. Supplied repair returns from any
   outage.

## What it adds

- **Dependence on a flux against dependence on a provider.** A
  self-sustaining structure is no less dependent on its flux than a
  supplied one. Withdrawal brings back decay at the damage rate in both,
  and [CLAIM-597](CLAIM-597.md)'s point 2 holds for both. What it escapes is dependence on
  someone who delivers the repair. Its repair is its own work, so it needs
  only access to the flux. The cost of that independence is the three
  thresholds.
- **To [QUESTION-085](../questions.d/QUESTION-085.md).** The question asks whether a maintained r/place
  artwork is a flame or a convection cell. If its defence is recruited by
  the image itself, the image's repair rate should rise with its intact
  share, and three things should be visible in the placement records. A
  small or badly damaged image should not be rebuilt even while its
  community is active. Once attack outruns defence past some level, the
  image should fall fast rather than erode. And an image that is wiped
  for long enough should not come back when its defenders return.
  Defenders arriving at a rate fixed by the subreddit's size predict none
  of these. [CLAIM-273](CLAIM-273.md)'s imported order is compatible with either answer.
- **To [QUESTION-399](../questions.d/QUESTION-399.md) and [QUESTION-398](../questions.d/QUESTION-398.md).** Becoming self-maintaining, in this
  sense, moves a structure from [CLAIM-597](CLAIM-597.md)'s smooth dependence to a
  threshold one. A's withdrawal measure D(s) would then be near zero above
  I₋ for a short withdrawal and jump to one for a long one, since the
  measure depends on the withdrawal's length as well as the state.
- **To [CLAIM-516](CLAIM-516.md).** The uptake model's feedback runs from the structure to
  its own repair, a one-member cycle. [CLAIM-516](CLAIM-516.md) says such a cycle is not
  closure, and the model agrees. One constraint maintaining the
  conditions of its own production is a flame, not an organism
  ([TERM-070](../terms.d/TERM-070.md), [THEORY-072](../theory.d/THEORY-072.md)).

## What the ecological readings add

Read after the owner proposed reintroduction and ecological recovery as cases.
- **Applied nucleation fits the self-sustaining kind** ([NOTE-1676](../notes.d/NOTE-1676.md), [NOTE-1660](../notes.d/NOTE-1660.md)). Planted tree islands keep drawing seed dispersers through their own growth. Weeding stopped at 2.5 years and their advantage lasted to 16–18. About 64 m² is cited as the minimum for a nucleus to spread, which works like an ignition threshold.
- **Field evidence for the claim's thresholds is thin.** Schröder, Persson and De Roos ([NOTE-1666](../notes.d/NOTE-1666.md)) find alternative stable states in most conclusive laboratory experiments and in few field experiments. Of 15 tests in which a pressure was removed, 3 showed the system failing to return.
- **A partial cut can give a plateau.** Cutting the Kirtland's Warbler's supplied habitat gives lower plateaus rather than collapse ([NOTE-1674](../notes.d/NOTE-1674.md)). That is the smooth decline of supplied upkeep.

The model's three signatures are therefore what to test for, not what to expect.

## What the counterpoint and urban readings add

- **An empirical ignition threshold, at household level.** Balboni et al. ([NOTE-1654](../notes.d/NOTE-1654.md)) estimate an S-shaped asset transition in Bangladesh with an unstable threshold near one cow's value. Households below it lose assets, and households above it accumulate for eleven years. The data cannot tell a smooth S from a jump, and the collapse and outage signatures are not tested.
- **None at regional scale.** Kline and Moretti ([NOTE-1646](../notes.d/NOTE-1646.md)) find a constant agglomeration elasticity for the Tennessee Valley Authority, so no threshold and no second equilibrium. Their region's forty-year persistence is slow reversion. That is the case this claim's signatures are needed to tell apart from self-sustaining upkeep.
- **A model with the claim's structure.** Michaels et al. ([NOTE-1651](../notes.d/NOTE-1651.md)) model infrastructure kept up by private building, with a threshold share of good housing below which it decays. The threshold is assumed, not estimated.

## What it does not say

- **That self-maintenance always has thresholds.** Uptake proportional to
  I^n with n > 1 gives them. Uptake linear in I (n = 1) gives a single
  transcritical threshold in supply, with no ignition barrier at fixed
  supply. The claim covers the quadratic case. A real structure's exponent
  is an empirical matter.
- **That the deterministic thresholds are sharp in a small system.** In a
  finite system each kept state is metastable and is left by fluctuation
  after a time exponential in size ([THEORY-1273](../theory.d/THEORY-1273.md)). Entropy production does
  not decide which kept state wins ([THEORY-1270](../theory.d/THEORY-1270.md)). The thresholds here are
  the deterministic ones.
- **That a flame-like organization is better.** It is cheaper to keep
  once lit and harder to light and to restore. Which is preferable depends
  on how often the flux fails and for how long.

## Note of 2026-11-05: the readings on persistence after shocks

Qualified at city scale. Davis and Weinstein's search fits models with one to four equilibria to Japanese cities after bombing and finds no lower equilibrium ([NOTE-tmpbzli4](../notes.d/NOTE-tmpbzli4.md)). No collapse or hysteresis followed the destruction of about half of all structures, so any threshold lies beyond the observed shocks. Bleakley and Lin's account of portage persistence ([NOTE-tmpslfbd](../notes.d/NOTE-tmpslfbd.md)) has a locally stable low equilibrium, consistent with the claim's form, but they say their results do not directly show multiple equilibria. In Moving to Opportunity ([NOTE-tmpqfxp3](../notes.d/NOTE-tmpqfxp3.md)) the dose response is roughly linear, and the authors find little evidence of a "critical age" below which children must move to benefit. No status changes.
