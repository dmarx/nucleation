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
grounds:
- THEORY-tmpkkhou
- THEORY-tmp0qrm2
- THEORY-tmp02gkd
- THEORY-tmph35ra
- THEORY-tmphv65i
- THEORY-tmp2ece2
- THEORY-tmpukudp
complements:
- CLAIM-597
- CLAIM-tmpw4ai2
bears_on:
- QUESTION-398
- QUESTION-386
summary: >-
  The assistant's, at the owner's request of 2026-11-05 to look to aid and
  development for theory on how aid-dependent organizations become
  self-sufficient. [CLAIM-597](CLAIM-597.md) holds an outside supply that repairs the
  organization and leaves its own capacity alone. The readings say aid
  does not leave it alone: it does the work the capacity is learned from.
  Moss, Pettersson and van de Walle cite Kaldor, that a state leaves aid
  dependency as it "learns how to tax". Azam, Devarajan and O'Connell's
  1999 model already has taxing experience built by revenue collected
  and decaying with time, and capacity kept lower the more aid finances. Moore says raising
  revenue keeps a state's machinery alive at the grassroots. Ostrom et al.
  find recipients losing skill and rebuilding plants they did not
  maintain, and Andrews, Pritchett and Woolcock find capability stagnating
  under aid. In a model where capacity grows with the work done and decays
  with disuse ([CLAIM-558](CLAIM-558.md)), aid that does a share A of the work first holds
  capacity at λ(1 − A)/(λ(1 − A) + μ): with λ = 1, μ = 0.3, 0.769 without
  aid, 0.625 at A = 0.5, 0.25 at 0.9 and none at full substitution. After
  full substitution for 10, 20 and 40 time units, meeting demand takes
  3.8, 6.4 and 11.4 units once aid stops, because the work an organization
  can do is capped by its capacity, so it regrows from a seed. Aid used
  after capacity, covering only what it cannot yet do, keeps service whole
  and leaves capacity to grow as if there were no aid. The first point is
  Azam et al.'s; the second and third are not in their paper. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-558 CLAIM-597 CLAIM-tmpw4ai2 — Proposed or new; claims this one rests on or extends, cited as open -->
<!-- inactive-ok-file: NOTE-tmp22pjn — new; readings of the aid-dependency filing, cited as open -->

# CLAIM-tmpoh07b: Where an organization's capacity is learned by doing the work it serves, outside supply that does the work first lowers the capacity kept, and the longer it does all of it the longer recovery takes once it stops, while supply that covers only what the organization cannot yet do leaves its learning untouched, so what decides dependence is the order in which supply and capacity are used, not the amount of supply

## The model

A demand of 1 unit of work per unit time is met by outside supply and by
the organization, whose output is τC for capacity C between 0 and 1.
Capacity grows with the work the organization does, P, and decays with
disuse:

  dC/dt = λP(1 − C) − μC.

The disuse term is [CLAIM-558](CLAIM-558.md)'s: a capability not exercised decays. Two
rules for using the supply A are compared.

- **Substitution: supply first.** The supply does min(A, 1) and the
  organization does the rest, P = min(τC, 1 − A).
- **Capacity-first.** The organization does what it can, P = min(τC, 1),
  and the supply covers 1 − τC while that is positive. Azam et al. call
  aid that fills the gap between spending and the revenue a state chose
  "gap-filling"; in their model it displaces revenue at the margin, which
  is substitution here, so the name is not used for this rule.

With λ = 1, μ = 0.3 and τ = 1.5 (scratch/formal/supplied_maintenance_toys.py
reproduces and asserts every number), the organization alone keeps
C = 0.769, an output of 1.15, more than demand.

## The claim

1. **Substitution lowers kept capacity in proportion to its share.** At a
   steady share A < 1, C* = λ(1 − A)/(λ(1 − A) + μ): 0.625 at A = 0.5 and
   0.25 at A = 0.9. Service is whole throughout, so nothing looks wrong
   while the supply continues. This is not new. In Azam et al.'s model kept
   experience is the revenue collected over its decay rate, which falls
   with aid; the form here only saturates it.
2. **Full substitution makes dependence deepen with time.** At A = 1 the
   organization does no work, and capacity decays as e^(−μt), to 0.038
   after 10 units. Once the supply stops, demand is met again only after
   3.84, 6.38 and 11.38 units for substitution lasting 10, 20 and 40. Each
   further unit of substitution adds μ/(λτ − μ) = 0.25 units of recovery,
   because capacity regrows from a smaller seed at the rate λτ − μ. That
   depends on the work being capped by capacity, P ≤ τC, which Azam et
   al.'s model does not assume, and they do not analyse exit. The
   shortfall in service after exit grows from 2.1 to 4.6 to 9.6
   unit-times. After partial substitution at A = 0.9 for 50 units it is
   0.58, and at A = 0.5 it is 0.009.
3. **Capacity-first leaves learning untouched.** From a capacity of 0.05,
   capacity under the capacity-first rule regrows as if there were no supply, meeting
   demand within 5 units and reaching 0.769. Service is whole throughout,
   and the supply falls to zero by itself. Equal service can be bought
   with either rule. What differs is whether the organization does the
   work it learns from.

## What the readings add, and where the model stops

- **The assumption is the readings'.** That a state's capacity is learned
  by doing the work is the route out of dependency that Moss, Pettersson
  and van de Walle ([NOTE-tmpd45i4](../notes.d/NOTE-tmpd45i4.md)) take from Kaldor (the state "learns how to tax") and
  from Azam et al.'s learning by doing ([NOTE-tmpvgfdp](../notes.d/NOTE-tmpvgfdp.md)), and it is Moore's
  revenue machinery kept alive by use ([NOTE-tmpfngj0](../notes.d/NOTE-tmpfngj0.md)). Ostrom et al.'s
  recipients lose skill under repeated help ([NOTE-tmp22pjn](../notes.d/NOTE-tmp22pjn.md)), and Andrews,
  Pritchett and Woolcock's capability stagnates under aid that pays for
  form ([NOTE-tmpfpey1](../notes.d/NOTE-tmpfpey1.md)).
- **Matched in practice, in one study.** In the Kenya summary of the FANTA
  exit study ([NOTE-tmp46avq](../notes.d/NOTE-tmp46avq.md)), "gradual exit, with the opportunity for
  project participants to operate independently prior to project closure,
  made it more likely that activities would be continued", and activities
  supplied by the project until the end declined. Operating independently
  before closure is the capacity-first rule's doing of the work while
  support remains. The summary is eight pages without a comparison group.
- **A second mechanism the model leaves out.** In Ostrom et al.'s
  Samaritan's dilemma the recipient chooses low effort because help is
  assured. That is an incentive, not a learning rate, and it would lower
  P under either rule. Capacity-first removes the learning loss, not the
  incentive problem. Ostrom et al.'s remedy, that beneficiaries put in
  some of their own assets and share the decision to continue, addresses
  the incentive.
- **Load beyond capacity.** Pritchett, Woolcock and Andrews warn against
  "premature load bearing" ([NOTE-tmpss5e0](../notes.d/NOTE-tmpss5e0.md)), demands on a fledgling system
  that break it.
  The model has no overload failure, and capacity-first asks for the work up
  to capacity, not beyond it. A model in which overload damages capacity
  would make the order of use matter even more.
- **To [CLAIM-597](CLAIM-597.md).** There the supply repairs the structure and leaves its
  own capacity alone. Here the supply is not neutral: used first, it takes
  the work the capacity is kept by. Under full substitution [CLAIM-597](CLAIM-597.md)'s
  dependence is the best case.
- **To [QUESTION-398](../questions.d/QUESTION-398.md).** The organization becomes independent of the
  supply exactly when its output covers demand. Under capacity-first the
  supply withdraws itself as capacity grows, so A's withdrawal measure D
  falls to zero as the supply does. Under substitution D grows with the
  supply's duration.
- **To [QUESTION-386](../questions.d/QUESTION-386.md).** Funding that rewards disbursing, or that pays for
  the work rather than for the organization doing it, selects
  substitution. Ostrom et al. find both pressures inside the donor.

## What the ecological readings add

- **A faster route than disuse.** In hatchery steelhead, captive rearing selects for success in captivity. Fitness in the wild falls within one generation, and the loss compounds over generations ([NOTE-tmp52jvk](../notes.d/NOTE-tmp52jvk.md), [NOTE-tmpkfeb0](../notes.d/NOTE-tmpkfeb0.md)). The pattern is this claim's: support that does the work lowers the capacity kept, and more so the longer it runs. The mechanism is selection, not unlearning, and recovery after withdrawal is not measured.
- **A confound to keep apart.** Morris et al. ([NOTE-tmpbfqjw](../notes.d/NOTE-tmpbfqjw.md)) find longer release programmes with fewer failures. That is continued supply, not substitution, and it does not test this claim.

## What the counterpoint readings add

- **Cash is this claim's benign case.** Cash supplements the recipients' work rather than doing it, and work did not fall ([NOTE-tmpy2r15](../notes.d/NOTE-tmpy2r15.md), [NOTE-tmpxsjeo](../notes.d/NOTE-tmpxsjeo.md)). The claim gives no reason to expect crowding out from it.
- **The amount matters in another way.** Under capacity-first support, the amount does not cause dependence. But Balboni et al.'s threshold ([NOTE-tmp6tzyt](../notes.d/NOTE-tmp6tzyt.md)) shows that the amount decides whether the capacity-building process starts at all. Support too small decays without any dependence. "Not the amount of supply" holds only for dependence.

## What it does not say

- **That aid harms capacity by this route in practice.** The readings
  report the mechanism and its contested evidence, including reverse
  causation and confounding by low income. The claim is about the model.
- **That capacity-first is always available.** It needs the supply to
  observe what the organization can do and to stop when it can. Ostrom et
  al. report that a threat to withdraw is not credible when a donor will
  not write off what it has spent.
- **That a threshold is absent.** Here capacity regrows from any non-zero
  seed. Azam et al. have a real trap: with long enough memory there are two
  steady states, a high-aid one that is locally stable and a low-aid one
  on a saddle, and a threshold on initial institutions decides which a
  myopic planner reaches. Their recipient is better off in the high-aid
  state, so graduating is the donor's gain, and their optimal exit is to
  reduce aid "up front". None of that is in this model. If capacity grows only once enough of it exists, as a flame's
  upkeep does ([CLAIM-tmpw4ai2](CLAIM-tmpw4ai2.md)), full substitution long enough leaves a
  capacity that does not regrow when the supply stops, the shape of a
  capability trap.
