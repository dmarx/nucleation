---
number: 605
status: Active
formerly:
- CLAIM-tmp6t2vz
title: "Where capacity is learned by doing, decays with disuse and needs capacity already present to grow, support that does the work has a deadline after which withdrawal no longer restores capacity, and a slow taper of such support is worse than an abrupt cut because it holds practice down long enough to cross the threshold; support that covers only what the party cannot yet do needs no taper but cannot lift a party already below the threshold"
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated
    these rulings), under ADR-057, with CLAIM-602 and CLAIM-604, on
    which it rests. The readings it reconciles or illustrates move
    from grounds to corroborated_by (ADR-058). The title states the
    disuse decay the deadline needs. Old title: 'Where capacity is
    learned by doing and its growth needs capacity already present,
    support that does the work has a deadline after which withdrawal
    no longer restores capacity, and a slow taper of such support is
    worse than an abrupt cut because it holds practice down long
    enough to cross the threshold; support that covers only what the
    party cannot yet do needs no taper but cannot lift a party
    already below the threshold'. The twenty-fifth status review
    re-ran scratch/formal/capability_trap_toy.py and checked by the
    comparison principle that a slower taper never leaves more
    capacity.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the model: capacity C with dC/dt = λPC(1 − C) − μC, where
  substitutive support A gives P = min(τC, 1 − A) and capacity-first
  support gives P = min(τC, 1), for which full substitution has no
  duration after which withdrawal fails to restore C; for which a linear
  taper of substitutive support from a given start recovers whenever an
  abrupt cut does; or for which capacity-first support lifts a party from
  below the unstable threshold. Not defeated by organizations whose
  learning does not need capacity already present, which CLAIM-602
  covers, nor by evidence that some tapers work, which the claim allows
  for tapers shorter than the limit.
tags:
- society-and-governance
- complex-systems
- mathematics
date: '2026-11-05'
line:
- readiness
- realizability
rests_on:
- CLAIM-602
- CLAIM-604
complements:
- CLAIM-600
corroborated_by:
- THEORY-1483
- THEORY-1492
- THEORY-1465
bears_on:
- QUESTION-398
summary: >-
  The assistant's, filling gaps the supplied-maintenance filing left, at
  the owner's request of 2026-11-05 to "proceed systematically filling
  all of those identified gaps". [CLAIM-602](CLAIM-602.md) modelled crowding out with no
  threshold, so capacity always regrew from a seed. Its own limits named
  the threshold case, Azam et al.'s trap. Here learning by doing needs
  capacity already present, dC/dt = λPC(1 − C) − μC. With λ = 1, μ = 0.3
  and τ = 1.5, a party alone keeps C = 0.7, and C below 0.276 decays to
  nothing. The model gives three results. Support that does all the work
  has a deadline: after ln(0.7/0.276)/0.3 = 3.10 time units capacity has
  crossed the threshold, and withdrawal no longer restores it. Tapering
  such support is worse the slower it is: from C = 0.45 under support
  doing 95 % of the work, an abrupt cut recovers, a taper over 5 periods
  recovers, and any taper longer than 9.13 periods traps the party.
  Capacity-first support needs no taper, since it withdraws itself, but
  it cannot lift a party already below the threshold. That reconciles
  Azam et al.'s optimal up-front cut, made for substitutive aid, with the
  Kenya exit study's success with gradual exits in which participants
  already did the work. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

# CLAIM-605: Where capacity is learned by doing, decays with disuse and needs capacity already present to grow, support that does the work has a deadline after which withdrawal no longer restores capacity, and a slow taper of such support is worse than an abrupt cut because it holds practice down long enough to cross the threshold; support that covers only what the party cannot yet do needs no taper but cannot lift a party already below the threshold

## The model

Demand is 1 unit of work, and the party's output is τC for capacity C
between 0 and 1. Capacity grows with the work the party does, P, at a
rate that also needs capacity already present, and decays with disuse:

  dC/dt = λPC(1 − C) − μC.

- **Substitutive support** A does the work first: P = min(τC, 1 − A).
- **Capacity-first support** covers only what the party cannot do:
  P = min(τC, 1).

With λ = 1, μ = 0.3 and τ = 1.5 (scratch/formal/capability_trap_toy.py
reproduces and asserts every number), a party with no support has three
steady states:
- C = 0, which is stable;
- an unstable threshold at C = 0.276, where λτC(1 − C) = μ;
- a kept state at C = 0.7.

The extra factor C in the learning term is what [CLAIM-602](CLAIM-602.md) left out. It
makes capacity something that is needed to build capacity.

## The claim

1. **Full substitution has a deadline.** Under support that does all the
   work, capacity decays as e^(−μt) from 0.7. It crosses the threshold
   after ln(0.7/0.276)/0.3 = 3.10 time units. Withdrawn after 2 or 3
   units, the party recovers to 0.7. Withdrawn after 3.5 or 5, it decays
   to nothing. This is the capability trap that [CLAIM-602](CLAIM-602.md) named as a
   limit and did not model.
2. **A slow taper of substitutive support is worse than an abrupt cut.**
   From C = 0.45, under support that does 95 % of the work:
   - an abrupt cut recovers, with a service shortfall of 0.97 over 60
     periods;
   - a linear taper over 5 periods recovers, with a larger shortfall of
     2.61;
   - any taper longer than 9.13 periods traps the party.

   The taper keeps doing the work while capacity is still low, so it
   holds practice down until capacity crosses the threshold. A gentler
   withdrawal is the riskier one.
3. **Capacity-first support needs no taper, and cannot ignite.** From
   C = 0.45, capacity-first support lets capacity grow to 0.7. The
   support it supplies, 1 − τC, falls to zero by itself. From C = 0.20,
   below the threshold, the same support lets capacity decay to nothing.
   Covering the shortfall keeps service whole. It does not supply the
   capacity that growth needs. Lifting a party past the threshold takes
   support of another kind, one that adds capacity directly, as Balboni
   et al.'s asset transfer did ([THEORY-1465](../theory.d/THEORY-1465.md)).

## What it reconciles

- **Azam, Devarajan and O'Connell** ([THEORY-1483](../theory.d/THEORY-1483.md)) find the optimal exit
  from aid that fills a fiscal gap is to reduce aid "up front". Their aid
  substitutes, displacing revenue at the margin. On this model an abrupt
  cut is then the safer exit.
- **The Kenya exit study** ([THEORY-1492](../theory.d/THEORY-1492.md)) finds that gradual exit with
  participants operating independently before closure made it more likely
  that activities continued. There the participants already did the work,
  which is the capacity-first case, where a gradual withdrawal is what the
  support does anyway.

The two findings disagree only if the support is the same. On this model
the kind of support decides the exit: cut substitutive support abruptly,
and let capacity-first support withdraw itself.

## What it does not say

- **That abrupt cuts are costless.** The abrupt cut's service shortfall is
  real, and in the model it is borne by the party. A taper shorter than
  the limit trades a smaller trap risk for a larger shortfall. The claim
  is about the risk of the trap, not about welfare.
- **That the numbers carry over.** The threshold, the deadline and the
  longest safe taper all depend on invented parameters. The model shows
  the direction: slower tapers of substitutive support are riskier.
- **That substitutive support should never be tapered.** A taper shorter
  than the limit recovered. The point is that the limit exists, and that
  lengthening a taper "to be safe" can cross it.
