---
status: Proposed
title: "Where an organization's capacity is learned by doing the work it serves, outside supply that does the work first lowers the capacity kept, and the longer it does all of it the longer recovery takes once it stops, while supply that covers only what the organization cannot yet do leaves its learning untouched, so what decides dependence is the order in which supply and capacity are used, not the amount of supply"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the model: capacity C with dC/dt = λP(1 − C) − μC, where P
  is the work the organization does, that does not settle at
  λ(1 − A)/(λ(1 − A) + μ) when outside supply A < 1 does the work first;
  whose time to meet demand after full substitution stops does not grow
  with the substitution's length at rate μ/(λτ − μ); or that is lowered
  by supply which covers only 1 − τC. Not defeated by organizations whose
  capacity is not learned by doing, which the claim does not cover, nor by
  evidence that aid harms capacity by other routes, which it leaves open.
tags:
- society-and-governance
- complex-systems
- mathematics
date: '2026-11-05'
line:
- readiness
- realizability
rests_on:
- CLAIM-558
complements:
- CLAIM-597
- CLAIM-tmpw4ai2
bears_on:
- QUESTION-398
- QUESTION-386
summary: >-
  The assistant's, at the owner's request of 2026-11-05 to look to aid and
  development for theory on how aid-dependent organizations become
  self-sufficient. CLAIM-597 holds an outside supply that repairs the
  organization and leaves its own capacity alone. The readings say aid
  does not leave it alone: it does the work the capacity is learned from.
  Moss, Pettersson and van de Walle cite Kaldor, that a state leaves aid
  dependency as it "learns how to tax", and Azam et al., that this
  learning by doing depends on aid's share of revenue. Moore says raising
  revenue keeps a state's machinery alive at the grassroots. Ostrom et al.
  find recipients losing skill and rebuilding plants they did not
  maintain, and Andrews, Pritchett and Woolcock find capability stagnating
  under aid. In a model where capacity grows with the work done and decays
  with disuse (CLAIM-558), aid that does a share A of the work first holds
  capacity at λ(1 − A)/(λ(1 − A) + μ): with λ = 1, μ = 0.3, 0.769 without
  aid, 0.625 at A = 0.5, 0.25 at 0.9 and none at full substitution. After
  full substitution for 10, 20 and 40 time units, meeting demand takes
  3.8, 6.4 and 11.4 units once aid stops. Aid that covers only what
  capacity cannot yet do keeps service whole and leaves capacity to grow
  as if there were no aid. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-558 CLAIM-597 CLAIM-tmpw4ai2 — Proposed or new; claims this one rests on or extends, cited as open -->

# CLAIM-tmpoh07b: Where an organization's capacity is learned by doing the work it serves, outside supply that does the work first lowers the capacity kept, and the longer it does all of it the longer recovery takes once it stops, while supply that covers only what the organization cannot yet do leaves its learning untouched, so what decides dependence is the order in which supply and capacity are used, not the amount of supply

## The model

A demand of 1 unit of work per unit time is met by outside supply and by
the organization, whose output is τC for capacity C between 0 and 1.
Capacity grows with the work the organization does, P, and decays with
disuse:

  dC/dt = λP(1 − C) − μC.

The disuse term is CLAIM-558's: a capability not exercised decays. Two
rules for using the supply A are compared.

- **Substitution: supply first.** The supply does min(A, 1) and the
  organization does the rest, P = min(τC, 1 − A).
- **Gap-filling: capacity first.** The organization does what it can,
  P = min(τC, 1), and the supply covers 1 − τC while that is positive.

With λ = 1, μ = 0.3 and τ = 1.5 (scratch/formal/supplied_maintenance_toys.py
reproduces and asserts every number), the organization alone keeps
C = 0.769, an output of 1.15, more than demand.

## The claim

1. **Substitution lowers kept capacity in proportion to its share.** At a
   steady share A < 1, C* = λ(1 − A)/(λ(1 − A) + μ): 0.625 at A = 0.5 and
   0.25 at A = 0.9. Service is whole throughout, so nothing looks wrong
   while the supply continues.
2. **Full substitution makes dependence deepen with time.** At A = 1 the
   organization does no work, and capacity decays as e^(−μt), to 0.038
   after 10 units. Once the supply stops, demand is met again only after
   3.84, 6.38 and 11.38 units for substitution lasting 10, 20 and 40. Each
   further unit of substitution adds μ/(λτ − μ) = 0.25 units of recovery,
   because capacity regrows from a smaller seed at the rate λτ − μ. The
   shortfall in service after exit grows from 2.1 to 4.6 to 9.6
   unit-times. After partial substitution at A = 0.9 for 50 units it is
   0.58, and at A = 0.5 it is 0.009.
3. **Gap-filling leaves learning untouched.** From a capacity of 0.05,
   capacity under gap-filling regrows as if there were no supply, meeting
   demand within 5 units and reaching 0.769. Service is whole throughout,
   and the supply falls to zero by itself. Equal service can be bought
   with either rule. What differs is whether the organization does the
   work it learns from.

## What the readings add, and where the model stops

- **The assumption is the readings'.** That a state's capacity is learned
  by doing the work is the route out of dependency that Moss, Pettersson
  and van de Walle take from Kaldor (the state "learns how to tax") and
  from Azam et al.'s learning by doing, and it is Moore's revenue machinery
  kept alive by use. Ostrom et al.'s recipients lose skill under repeated
  help, and Andrews, Pritchett and Woolcock's capability stagnates under
  aid that pays for form.
- **A second mechanism the model leaves out.** In Ostrom et al.'s
  Samaritan's dilemma the recipient chooses low effort because help is
  assured. That is an incentive, not a learning rate, and it would lower
  P under either rule. Gap-filling removes the learning loss, not the
  incentive problem. Ostrom et al.'s remedy, that beneficiaries put in
  some of their own assets and share the decision to continue, addresses
  the incentive.
- **Load beyond capacity.** Pritchett, Woolcock and Andrews warn against
  "premature load bearing", demands on a fledgling system that break it.
  The model has no overload failure, and gap-filling asks for the work up
  to capacity, not beyond it. A model in which overload damages capacity
  would make the order of use matter even more.
- **To CLAIM-597.** There the supply repairs the structure and leaves its
  own capacity alone. Here the supply is not neutral: used first, it takes
  the work the capacity is kept by. Under full substitution CLAIM-597's
  dependence is the best case.
- **To QUESTION-398.** The organization becomes independent of the
  supply exactly when its output covers demand. Under gap-filling the
  supply withdraws itself as capacity grows, so A's withdrawal measure D
  falls to zero as the supply does. Under substitution D grows with the
  supply's duration.
- **To QUESTION-386.** Funding that rewards disbursing, or that pays for
  the work rather than for the organization doing it, selects
  substitution. Ostrom et al. find both pressures inside the donor.

## What it does not say

- **That aid harms capacity by this route in practice.** The readings
  report the mechanism and its contested evidence, including reverse
  causation and confounding by low income. The claim is about the model.
- **That gap-filling is always available.** It needs the supply to
  observe what the organization can do and to stop when it can. Ostrom et
  al. report that a threat to withdraw is not credible when a donor will
  not write off what it has spent.
- **That a threshold is absent.** Here capacity regrows from any non-zero
  seed. If capacity grows only once enough of it exists, as a flame's
  upkeep does (CLAIM-tmpw4ai2), full substitution long enough leaves a
  capacity that does not regrow when the supply stops, the shape of a
  capability trap.
