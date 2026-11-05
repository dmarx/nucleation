---
status: Proposed
title: 'Telling which obstruction blocks a transition can itself be computationally hard: over families of reconfiguration problems, deciding whether any admissible path joins two feasible configurations is PSPACE-complete for some, and computing the least peak cost of a path strongly NP-hard for others, so diagnosing the obstruction is a problem with its own complexity'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the cited theorems: polynomial algorithms, unless the classes
  collapse, for pairwise connectivity in Eppstein's flaps and flips or for
  the reconfiguration problems Ito et al. prove PSPACE-complete, or for
  minmax power supply reconfiguration. Not defeated by small instances in
  which the obstruction is easy to tell, since the hardness is over
  families, nor by families in which diagnosis is easy, which the claim
  allows.
tags:
- mathematics
- operations-research
- complex-systems
date: '2026-11-05'
line:
- formal-apparatus
rests_on:
- CLAIM-tmplysd0
grounds:
- THEORY-tmp34oop
- THEORY-tmp57bxg
complements:
- CLAIM-tmpal9mc
- CLAIM-tmp06538
- CLAIM-tmpbi4ca
summary: >-
  The filer's, from the complexity readings filed beside the pasted
  synthesis on resource-bounded realizability (pasted by the owner on
  2026-11-05), against A's obstruction hierarchy (Response 2 §3) and its
  four held obstructions. Whether a transition fails for want of any path or
  for want of budget is a question; over families it has a complexity.
  Eppstein: pairwise connectivity in the flaps-and-flips model is
  PSPACE-complete even at bounded treewidth, with both endpoints valid. Ito
  et al.: reconfiguration of many NP-complete problems is PSPACE-complete,
  and the least worst intermediate cost, CLAIM-tmpbi4ca's threshold, is
  strongly NP-hard for power supply and inapproximable within any constant
  for maxmin clique unless P = NP. Both readers flagged it against
  CLAIM-tmpal9mc. The construction is the filer's, from the readings;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp06538 CLAIM-tmpal9mc CLAIM-tmpbi4ca CLAIM-tmplysd0 THEORY-tmp34oop THEORY-tmp57bxg — Proposed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-tmphme89: Telling which obstruction blocks a transition can itself be computationally hard: over families of reconfiguration problems, deciding whether any admissible path joins two feasible configurations is PSPACE-complete for some, and computing the least peak cost of a path strongly NP-hard for others, so diagnosing the obstruction is a problem with its own complexity

## The claim

CLAIM-tmpal9mc separates a transition with no path from one whose path
exceeds a resource ceiling, and gives each its remedy; CLAIM-tmp06538 adds
compatibility before and regeneration after. To apply a remedy one must
know which obstruction holds. That knowledge is the answer to a question,
and over a family of systems the question has a complexity
(CLAIM-tmplysd0).

- **Is there any path?** Eppstein (NOTE-tmpv7lp6; THEORY-tmp34oop), Theorem
  4: "Pairwise connectivity and global connectivity for" flaps and flips
  is PSPACE-complete, "even for instances with bounded treewidth". Both
  endpoints are valid flat states; whether one reaches the other is the
  hard part. Ito et al. (NOTE-tmpmqj4b; THEORY-tmp57bxg), Theorems 1 and 2:
  power supply, independent set, clique, vertex cover, set cover and
  integer programming reconfiguration are PSPACE-complete, independent
  set and vertex cover remaining so for planar graphs of maximum degree 3.
- **Is the path within the budget?** Ito et al. §4 optimizes "the worst
  objective among all configurations in the reconfiguration sequence",
  which is CLAIM-tmpbi4ca's bottleneck budget with cost as the resource:
  "Lemma 3. Minmax power supply reconfiguration is strongly NP-hard", and
  "Theorem 4. Maxmin clique reconfiguration cannot be approximated within
  any constant factor unless P = NP". Some cases are easy to approximate:
  "Theorem 6. There is a linear-time 2-approximation algorithm for minmax
  set cover reconfiguration".

So telling geometric disconnection from a capacity bottleneck can be
PSPACE-hard, and knowing how far over budget the cheapest path is can be
NP-hard. Checked against the filed readings by the filer.

## What it does not say

- **That diagnosis is a fifth obstruction.** It is a property of the
  others, a cost of knowing which holds; the complexity reader asked
  whether it is a fifth mode, and this claim says it is not one: a system
  can be blocked by a capacity bottleneck whether or not anyone can tell.
- **That diagnosis is hard for one system.** A fixed small system is
  diagnosed by search. The hardness is growth over a family, and an
  organization is diagnosable this way only once the family it belongs to
  is declared.
- **Anything about controllability, reliability or regeneration.** The
  readings concern existence of paths and their cost; how hard it is to
  tell a control limitation or an unstable path is not in them.
