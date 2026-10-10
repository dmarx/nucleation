---
status: Active
title: 'Causal-loop consistency and sheaf contextuality are both local-to-global problems, but passing to distributions affects them oppositely: a loop with no deterministic solution has a distributional fixed point, while a model with no global section in its supports has no global distribution either'
version: 1
role: granted
tags:
- contextuality
- causality
- mathematics
date: '2026-10-10'
line: pragmatic-transport
undercuts:
- ARG-tmpsb1c4
grounds:
- LIT-278
- LIT-016
- THEORY-012
- CASE-035
- LIT-tmp1mxid
complements:
- CLAIM-037
- CLAIM-044
summary: >-
  A161, after the owner's U46, sharpened. A161 saw that a causal loop
  and a contextual model are "not the same", but not that they run in
  opposite directions under passage to distributions, or why. Its
  parity pattern is [LIT-278](../literature.d/LIT-278.md)'s identification of Liar cycles with
  contextual support tables, which the record holds and has read
  ([NOTE-251](../notes.d/NOTE-251.md)). A173 and A178 kept the three kinds of global consistency
  apart; A218 Ch10.9 keeps the feedback case.
---
<!-- inactive-ok-file: LIT-tmp1mxid — Deferred; registered unread, cited only for its fixed-point condition -->
<!-- inactive-ok-file: ARG-tmpsb1c4 — Rejected; cited as the inference this claim undercuts -->
<!-- inactive-ok-file: CLAIM-037 CLAIM-044 CLAIM-038 CLAIM-056 CLAIM-098 CLAIM-127 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: LIT-813 — Superseded; withdrawn by its authors, and cited only to say that A161 recommended it as current -->

# CLAIM-tmpc4chg: Causal-loop consistency and sheaf contextuality are both local-to-global problems, but passing to distributions affects them oppositely: a loop with no deterministic solution has a distributional fixed point, while a model with no global section in its supports has no global distribution either

## The claim

A161 answered the owner's U46 ("don't we know this to be the case because
of causality paradoxes from general relativity?") with a comparison. The
grandfather paradox, as a consistency condition on a causal loop, is
x = ¬x: "There is no solution". If p is the probability that x = 1, the
condition becomes p = 1 − p, so p = ½. "A distributional fixed point exists
even though no deterministic fixed point exists." This is the fixed-point
condition of Deutsch's model of closed timelike curves ([LIT-tmp1mxid](../literature.d/LIT-tmp1mxid.md)),
and in classical form it is the stationary distribution of the NOT kernel.

A161 then said the contextual case is different: "In the three-context
parity example, replacing each deterministic assignment with a probability
distribution does not produce a nonnegative global joint distribution". That
is right. For [CASE-035](../cases.d/CASE-035.md) (S = M, M = H, H ≠ S), every deterministic global
assignment violates at least one constraint, so no joint distribution can
satisfy all three with probability 1.

What A161 did not say is that the two run in opposite directions, and why.

- **The fixed-point problem prescribes no marginals, and convexity helps.**
  A continuous self-map of a compact convex set of distributions has a fixed
  point. Passing from values to distributions creates solutions.
- **The extension problem prescribes marginals, and positivity hurts.** A
  global distribution must reproduce the given context distributions. Every
  global distribution has a deterministic assignment in its support, and
  that assignment's restrictions lie in the context supports. So a model
  with no global assignment consistent with its supports has no global
  distribution either. Probabilistic noncontextuality implies possibilistic
  noncontextuality, as in Abramsky and Brandenburger's hierarchy ([LIT-016](../literature.d/LIT-016.md),
  [THEORY-012](../theory.d/THEORY-012.md)), the reverse of the causal-loop direction.

The shared pattern is the Liar's. x = ¬x is a Liar cycle of length one, and
A = B, B = C, C ≠ A is an odd cycle of length three. Abramsky, Barbosa,
Kishida, Lal and Mansfield ([LIT-278](../literature.d/LIT-278.md), read in [NOTE-251](../notes.d/NOTE-251.md)) identify Liar
cycles with strongly contextual support tables, informally, with one exact
case: the length-4 Liar cycle is the PR box. A161 does not cite it.

## The domain of realizability

A161: "**Principle: Always specify the domain of global realizability.**"
The domain is an assignment of values, a probability measure, a causal
history or a dynamical fixed point, and the answer to "is there a global
realization?" changes with it. A173's secondary table keeps "global
assignments, joint distributions, and causal fixed points" apart, and A178
keeps a "Dynamical consistency case: causal feedback": "Deterministic causal
loops and stochastic fixed-point constructions clarify the difference
between global empirical extension and dynamical self-consistency." This is
the methodological half of the claim. [CLAIM-037](CLAIM-037.md) and [CLAIM-044](CLAIM-044.md) already
practise it for contextuality.

Granted, because the mathematics is elementary, and because it is the
reason the owner's inference fails ([ARG-tmpsb1c4](../arguments.d/ARG-tmpsb1c4.md)): a causal paradox and
a contextual model are not two cases of one phenomenon.

## What it does not say

- It does not say Deutsch's model is the physics of closed timelike curves.
  Lloyd et al.'s post-selected closed timelike curves (arXiv:1005.2219, not
  held) treat the grandfather paradox differently, and limit the reading.
- It does not say general relativity bears on pragmatic data at all. A161:
  "I would avoid claiming that **general relativity proves that
  communicative observational systems need not possess global
  realizations**." Nor does it support [CLAIM-038](CLAIM-038.md), whose evidence is
  [LIT-016](../literature.d/LIT-016.md) and [CASE-035](../cases.d/CASE-035.md), not physics.
- It does not say the fixed point is unique. In finite dimension it always
  exists, by a Brouwer-type argument for the map on density matrices, so
  A161's hedge "Under the appropriate assumptions" is unnecessary.
  Uniqueness is the open issue, and A161 does not raise it.

## Where it went

A161 drew a new direction from the comparison: "our theory should not
assume communication always proceeds along an acyclic sequence". It asks
two questions: "Can the available local observations be assembled into one
globally admissible observational model?" and "Does the interacting
communicative system possess a dynamically self-consistent state or
trajectory? Their answers need not agree." It bears on the chain picture of
transport ([CLAIM-056](CLAIM-056.md), [CLAIM-098](CLAIM-098.md)) and on interventions ([CLAIM-127](CLAIM-127.md)).

The question has less content than it seems. A161 itself notes that dialogue
loops "Normally ... unfold through successive time steps and pose no causal
paradox". Unrolled in time they are a chain, so the question has content
only for equilibrium or simultaneous-update models. Its prior art for the
solvability half is cyclic structural causal models (Bongers, Forré, Peters
and Mooij, arXiv:1611.06221, not held), which can have no solution or
several. It is folded in here rather than filed as a question, because no
turn took it further. A218 Ch10.9 keeps the feedback case in the plan.

A161 also recommended Gogioso and Pinzani's *The Sheaf-Theoretic Structure
of Definite Causality* as current. The record holds it as [LIT-813](../literature.d/LIT-813.md),
Superseded, because its authors withdrew it in favour of [LIT-800](../literature.d/LIT-800.md), [LIT-808](../literature.d/LIT-808.md)
and [LIT-788](../literature.d/LIT-788.md). A78 had recommended it first.
