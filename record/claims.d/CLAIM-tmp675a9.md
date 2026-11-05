---
status: Proposed
title: 'Where an intervention acts in a system''s constraint structure can predict whether it achieves a target better than how much intervention there is, and adding an intervention to a successful set can make it fail'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A finding, in the same or a fuller model of self-folding sheets, that at
  matched numbers of actuators the union of their folding islands
  predicts success no better than the count does, or that the failure
  caused by an added actuator disappears under the energy model of the
  supplement or under small noise. Not defeated by systems in which more
  intervention does help on average, nor by organizational settings
  where the analogy fails; the claim is about where intervention sits in a
  constraint structure, shown in mechanical systems.
tags:
- complex-systems
- natural-sciences
- mathematics
date: '2026-11-05'
line:
- realizability
grounds:
- THEORY-tmpq2qdv
- THEORY-tmp278tq
complements:
- CLAIM-345
- CLAIM-tmp9jvpb
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 5, narrowed to
  what Stern, Pinson and Murugan show. In their simulations, whether the
  actuated creases' folding islands cover the sheet predicts success much
  better than the number of actuators, five well-placed ones succeeding 60
  times as often, and one added actuator with a small island can stop a
  folding that succeeded. A's "greater intervention capacity need not monotonically improve success" goes further than the paper and is not filed.
  Chen, Choi and Mahadevan add a structural instance. The construction is
  the filer's, from A's reading of Stern et al.; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmpq2qdv THEORY-tmp278tq CLAIM-tmp9jvpb CLAIM-185 CLAIM-184 — Proposed; the readings' accounts and A's proposals of 2026-11-04, cited as filed, nothing here rests on their being settled -->

# CLAIM-tmp675a9: Where an intervention acts in a system's constraint structure can predict whether it achieves a target better than how much intervention there is, and adding an intervention to a successful set can make it fail

## The claim

**Placement predicts better than count.** Stern, Pinson and Murugan
([NOTE-tmp9dvve](../notes.d/NOTE-tmp9dvve.md); [THEORY-tmpq2qdv](../theory.d/THEORY-tmpq2qdv.md)) fold a crease pattern designed with one motion by
applying fixed torques, of the right sign, at chosen creases. Placed at
random, "actuators are needed on 18 out of a total of 60 creases to even
have a 50% probability of folding the pattern." A crease's folding island
is "the largest subset of the pattern that will fold in the desired
branch, if that subset is cut out and actuated at the chosen crease", and
UFI is the fraction of creases in the union of the actuated creases'
islands. Then "a set of 5 actuators is 60× more likely to fold the
pattern if it has U F I = 1 rather than U F I < 1.", and "spatial
placement of actuators is a much better predictor of folding success than
just the number of actuators."

**More can be worse.** "adding another actuator with a very small folding
island as in Fig. 5h, can stop the previously successful folding!" The
paper explains it as competition between actuators, the sheet misfolding
just outside the small island.

**A structural instance.** Chen, Choi and Mahadevan ([NOTE-tmpazhb8](../notes.d/NOTE-tmpazhb8.md);
[THEORY-tmp278tq](../theory.d/THEORY-tmp278tq.md)) give exact least numbers of links that rigidify and that
connect a quad kirigami sheet; equal numbers of links give very different
degrees of freedom depending on where they go, and random choice almost
never finds a minimal set.

The common form: a target is reached through a constraint structure, and
what an intervention does depends on which part of that structure it
engages. A count of interventions is blind to that.

A's proposed experiment tests this directly: "test whether measures of where the actuators sit in the compatibility structure predict P_A better than actuator count or total energy."

## Relations

- **[CLAIM-345](CLAIM-345.md)**: equal controllability rank does not fix the cost of
  control. The two answer different parts of one question: rank does not
  fix effort, and count does not fix success.
- **[CLAIM-tmp9jvpb](CLAIM-tmp9jvpb.md)**: the target here is feasible and reachable, and the
  question is whether it is reliably reached.
- **[CLAIM-185](CLAIM-185.md) and [CLAIM-184](CLAIM-184.md)** (anchors; anchors entrench). Folding islands
  are local seeds that fix a global outcome, and a badly placed seed fixes
  a distractor. A: "not automatically a nucleation site in the strict
  thermodynamic sense".

## What it does not say

- **That greater intervention need not improve success monotonically**,
  in A's form. The paper shows that one added actuator can ruin one
  success, and presents it as something that "can sometimes" happen; with
  random placement its statistic is of success that needs more actuators,
  not fewer.
- **A condition for success.** The authors: "we are unable to formulate a
  strict necessary and sufficient condition for successful folding
  without full pattern information."
- **Anything beyond the flat state.** The need for careful actuation
  "mathematically applies only at the flat state", though for soft sheets
  it must be kept up to larger angles.
- **Generality.** One 4 × 4 pattern for the actuation statistics,
  zero-temperature descent, idealized vertices. The organizational
  reading, that where an organization intervenes can matter more than how
  much, is an analogy.
