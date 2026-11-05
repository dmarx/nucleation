---
status: Proposed
title: 'Under a fixed dynamical model an added hard constraint cannot enlarge the set of admissible trajectories, so it cannot enlarge what some admissible path reaches or lower the least cost of reaching it; what it can improve is a property required of every path a disturbance or a given process may take, such as robustness or reliability, and a constraint that does more has changed the mechanism'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the inclusion or the witnesses: a fixed model and constraint
  sets K' ⊆ K under which some history admissible under K' is not
  admissible under K; a property that asks only that some admissible
  history exist (a reach, a viable reach) that is gained, or a least cost
  over admissible histories that falls, when K' replaces K in the same
  model; or a showing that the capped-disturbance or blocked-branch
  witness fails under the definitions stated. Not defeated by a redesigned
  mechanism that does better with fewer degrees of freedom, nor by an
  ideal constraint whose reaction forces lower a cost, both of which the
  claim counts as a change of model.
tags:
- mathematics
- control-theory
- agency
date: '2026-11-05'
line:
- will-organization
- formal-apparatus
complements:
- CLAIM-354
- CLAIM-tmp9jvpb
bears_on:
- QUESTION-tmp8jsu9
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched): "If K' ⊆ K, then
  Traj(K') ⊆ Traj(K)". It guards against reading the thesis that
  constraints enable freedom as monotone. The inclusion is immediate, and with it
  every property that asks only for some admissible history. What a
  constraint can improve is a property quantified over what a disturbance,
  a distractor or a given process may do, since removing their options
  weakens the requirement; two constructions show it. Anything more, as
  in Juarrero's enabling constraints, Hopkins's serial stacking or Dollar
  and Howe's hand, is a change of mechanism. The construction of the
  second half is the filer's. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-354 CLAIM-tmp9jvpb NOTE-1532 — Proposed or Skimmed; the record's graded-freedom claim, an entry of 2026-11-05 from the same paste, and the reading of Juarrero, cited as filed, nothing here rests on their being settled -->

# CLAIM-tmpr4sof: Under a fixed dynamical model an added hard constraint cannot enlarge the set of admissible trajectories, so it cannot enlarge what some admissible path reaches or lower the least cost of reaching it; what it can improve is a property required of every path a disturbance or a given process may take, such as robustness or reliability, and a constraint that does more has changed the mechanism

## The claim

A: "Under a fixed dynamical model, imposing an additional hard constraint
cannot enlarge the set of admissible trajectories. If K' ⊆ K, then
Traj(K') ⊆ Traj(K). We should not claim otherwise. The more interesting
statement concerns changing the mechanism."

**The inclusion.** Fix a model: the histories of state, input and
disturbance it allows. A hard constraint K is a condition on histories,
and Traj(K) is the set of allowed histories that meet it. If K' ⊆ K,
every history meeting K' meets K, so Traj(K') ⊆ Traj(K). Nothing more is
needed.

**What follows at once.** Any property that asks only that some admissible
history exist is monotone under the inclusion:

- the reachable set, the set of end states of admissible histories, can
  only shrink;
- so can the viably reachable set, which is the same with a viability
  condition added to K;
- the least cost of reaching a target, an infimum over admissible
  histories, can only rise or stay.

So the reachability dimension of CLAIM-354 cannot grow under an added
constraint in a fixed model.

**What need not follow.** A property that asks something of every history
some other party may produce is not monotone the same way. Removing that
party's options weakens the requirement.

- **Robustness.** Take ẏ = u + w with |u| ≤ 1 and a disturbance |w| ≤ 2,
  starting at y = 0. The task: keep |y| ≤ 0.1 on [0, 1] whatever w does.
  No policy achieves it: against w ≡ 2, ẏ ≥ 1 and y(1) ≥ 1. Add the hard
  constraint |w| ≤ 1, a barrier that caps the disturbance. Then u =
  −sign(y), with u = 0 at y = 0, keeps ẏ ≤ 0 where y > 0 and ẏ ≥ 0 where
  y < 0, so |y| never grows from 0. The robust property, ∃π ∀w, is gained,
  while what the controller alone can reach is unchanged.
- **Reliability.** CLAIM-tmp9jvpb's fork: a flat state branches into a path
  to the target and a path to a distractor, and unbiased actuation ends at
  the target with probability 1/2. A constraint that blocks the
  distractor branch leaves one admissible continuation, and the same
  actuation reaches the target with probability 1. Stern, Pinson and
  Murugan's sheets are the physical form: a designed folding motion
  competes with "an exponential number of ‘distractor’ folding" branches
  (NOTE-tmp9dvve).

The reluctant writer (CASE-013) is the robust case. Blocking the
distracting websites shrinks what the writer can do, and it removes what
the distraction can do, so finishing the article holds against more of
what may happen. CLAIM-354 records that the precommitment shrinks the set
while making the endorsed project realizable. This claim says why the
two are consistent: the set that shrinks is existential, and the gain is
in a universal property.

**Anything more is a change of mechanism.** By the contrapositive, if a
constraint makes some history possible that was not, the model was not
fixed. A: "A redesigned physical system can have fewer degrees of freedom
while providing better precision, lower control effort, more reliable task
completion, or greater robustness." And: "Kinematic freedom versus
Task-effective capability. They need not coincide." The readings show the
change of mechanism each time.

- **Juarrero's enabling constraints** (THEORY-1335; NOTE-1532) "irreversibly
  link and couple previously separate ... entities". The result is a new
  system with its own state space, not the old one with K shrunk. So the
  account is consistent with this claim, and is not a counterexample to
  it.
- **Freedom and Constraint Topologies.** In the reading of Hopkins (2013),
  "In FACT, new freedom comes from stacking bodies in series, not from
  adding constraints" (NOTE-tmpdewq8). In parallel, constraint spaces add and
  freedom spaces intersect, which is this inclusion; the freedom gained in
  series comes from added bodies.
- **Dollar and Howe's hand** (NOTE-tmpb0ok0). "An adaptive, underactuated hand
  has fewer actuators than degrees of freedom." Coupling eight joints to
  one input shrinks the shapes that can be commanded, and success under
  positioning error rises, the reading says, because contact selects the
  shape. The joints
  stay free. What changed is the actuation, and the property gained is a
  robust one.

## What it does not say

- **That constraints never help.** They can help with robustness and
  reliability, as the two constructions show, and a redesign with fewer
  freedoms can beat the original on every task measure.
- **That an ideal constraint never lowers a cost.** If the constraint is
  modelled with reaction forces that cost nothing, it changes the dynamics
  and not only the admissible set. A mass resting on a table needs no
  effort to stay at height. The claim counts that as a change of mechanism.
- **That a robust gain is free.** The capped disturbance and the blocked
  branch each also remove histories the controller might have wanted.
- **Anything about organizations.** A's organizational reading, that
  structure can make an organization more capable while it has fewer
  options, is an analogy. This claim fixes only which version of it is a
  theorem.
