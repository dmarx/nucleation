---
number: 562
status: Proposed
formerly:
- CLAIM-tmp675a9
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
- THEORY-1418
- THEORY-1368
complements:
- CLAIM-345
- CLAIM-567
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
<!-- inactive-ok-file: CASE-tmp7oe6s CLAIM-tmpuv9yj — Proposed or new; cited from the note on A's predictions -->
<!-- inactive-ok-file: THEORY-1418 THEORY-1368 CLAIM-567 CLAIM-185 CLAIM-184 — Proposed; the readings' accounts and A's proposals of 2026-11-04, cited as filed, nothing here rests on their being settled -->

# CLAIM-562: Where an intervention acts in a system's constraint structure can predict whether it achieves a target better than how much intervention there is, and adding an intervention to a successful set can make it fail

## The claim

**Placement predicts better than count.** Stern, Pinson and Murugan
([NOTE-1571](../notes.d/NOTE-1571.md); [THEORY-1418](../theory.d/THEORY-1418.md)) fold a crease pattern designed with one motion by
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

**A structural instance.** Chen, Choi and Mahadevan ([NOTE-1574](../notes.d/NOTE-1574.md);
[THEORY-1368](../theory.d/THEORY-1368.md)) give exact least numbers of links that rigidify and that
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
- **[CLAIM-567](CLAIM-567.md)**: the target here is feasible and reachable, and the
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

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Dunn, Dannenberg, Ouldridge, Kwiatkowska, Turberfield and Bath, "Guiding the folding pathway of DNA origami".** Dunn and colleagues ([NOTE-tmpvgzvb](../notes.d/NOTE-tmpvgzvb.md)) fit the claim directly: halving one staple of each seam pair,
less binding strength, improves the designed outcome (90% of broken-seam simulations end in 5:0)
and cuts model misfolds from 52% to 1%, while the full seam set's extra strength causes the traps.
Where the weakening acts, on cooperative long-range contacts, matters more than how much binding is
added. The experimental side is AFM counts on one protocol.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Lee Tin Wah et al., "Observing and controlling the folding pathway of DNA origami".** Lee Tin Wah et al. (2016), [LIT-tmps9gx3](../literature.d/LIT-tmps9gx3.md), support the claim in kind: where
the concentration change was applied (central versus edge staples), not the
amount alone, moved the nucleation site. The paper varies location and
amount together, so it is suggestive, not a clean separation. No status
changes.

No status changes.

## Note of 2026-11-05: A's predictions on productive nucleation

From the fourth synthesis on DNA origami by another assistant (A), "Predicting which organizations will successfully nucleate", pasted by the owner on 2026-11-05.

A's Predictions 1 and 4 restate this claim as predictions about organizations. Placement: "targeted stabilization of components that facilitate many later compatible interactions should outperform equally costly stabilization of components with little downstream influence", measured by a leverage per unit cost. Non-monotonicity: adding an intervention can lower the chance of the target, V(S ∪ {C}) < V(S). A cites the same Stern, Pinson and Murugan work. The assistant's CASE-tmp7oe6s gives an equal-cost pair in A's branching model (71.1 % against 62.7 %), and CLAIM-tmpuv9yj draws from this claim that productive nucleating sets have no closure. A's test would decide the organizational version: "Compare equal-budget interventions at different locations".

No status changes.
