---
status: Active
title: 'The first open problem of directed transport is not yet posed: a contextual model is a menu of incompatible experiments, and under the natural order on menus any state-independent classical simulation is dominated automatically, so what is open is only the converse or a deficiency bound'
version: 1
role: granted
tags:
- mathematical-statistics
- contextuality
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-156
- THEORY-174
objects_to:
- CLAIM-125
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. Blackwell's order compares experiments,
  each a family of distributions over one parameter. An empirical model
  has no parameter, and if it is contextual it has no joint distribution,
  only one per context. Posing [CLAIM-125](CLAIM-125.md)'s first part needs models
  indexed by situations and an order on menus of experiments. Under the
  natural order, the preservation direction is automatic for a classical
  simulation that does not depend on the situation. Granted, because the
  argument is elementary. It narrows what is open; it does not close it.
---
<!-- inactive-ok-file: CLAIM-125 — Proposed; open, and cited as the claim this objection narrows -->
<!-- inactive-ok-file: THEORY-156 THEORY-174 — Proposed; cited as the readings of Blackwell's order and of simulations, not as settled -->
<!-- inactive-ok-file: CLAIM-tmpyeik3 — Proposed; a companion objection from the same audit, cited for the state-dependent case -->

# CLAIM-tmpkf8pe: The first open problem of directed transport is not yet posed: a contextual model is a menu of incompatible experiments, and under the natural order on menus any state-independent classical simulation is dominated automatically, so what is open is only the converse or a deficiency bound

## The objection

[CLAIM-125](CLAIM-125.md)'s first part: "None of these works compares source and target
models by what they let a decision-maker do. The comparison the bridge
question asks for is an informativeness order in Blackwell's sense
([THEORY-156](../theory.d/THEORY-156.md)), relative to a family of decisions, taken across a change of
cover. When a classical or contextual transport preserves that order is
not addressed." [THEORY-174](../theory.d/THEORY-174.md) agrees that the simulation preorder "is not
shown to relate to Blackwell's informativeness order".

**What has to be said first.** Blackwell's order compares experiments.
Each is a family z ↦ P_z of distributions, one per state of a parameter
([THEORY-156](../theory.d/THEORY-156.md): "an n-tuple of probability measures on a common space, one
per state"). An empirical model gives one distribution per context. If it
is contextual, there is no joint distribution, and a receiver can carry
out one context per trial. And one model has no parameter: it is one set
of tables. So two things must be fixed before part 1 is a question.

1. **The parameter.** A family of models e^z indexed by situations z, for
   instance by which act was performed.
2. **What is compared.** For each context C, z ↦ e^z_C is an experiment.
   The model is then a menu of experiments, one per context, from which a
   decision-maker picks one to perform. The natural order on menus: menu M
   is at least as informative as menu M′ if every experiment in M′ is a
   garbling of some experiment in M. Then for every decision problem, the
   best context of M does at least as well as the best context of M′.

**On that order, one direction is automatic.** A classical non-adaptive
simulation answers each target context C′ by measuring source
measurements inside one source context C ([THEORY-174](../theory.d/THEORY-174.md): "π must send every
context of T into a context of S") and post-processing the outcomes. Take
first the form in which π is fixed and the shared randomness enters only
the post-processing, as a stochastic outcome map that does not depend on
z. If the same procedure is used for every z, then for every z

e′^z_(C′) = K_(C′)#(e^z_C restricted to the measurements used).

Restriction is a deterministic map and K_(C′) is a kernel that does not
depend on z. So the experiment z ↦ e′^z_(C′) is a garbling of the
experiment z ↦ e^z_C. Every target experiment is a garbling of some source
experiment, and the target menu is dominated by the source menu, by
Blackwell's easy direction applied context by context (Theorem 3 in
[THEORY-156](../theory.d/THEORY-156.md)'s reading). No such simulation can let a decision-maker do
better than the source let it.

If the shared randomness also chooses which source context is measured,
as in a mixture of deterministic procedures, each target experiment is a
mixture of garblings of several source experiments. Its best risk in any
decision problem is the average of theirs if the choice is revealed, and
no lower if it is hidden. So it is still no better
than the best source context, problem by problem. But it need not be a
garbling of any one source experiment, so the domination then holds
decision problem by decision problem rather than in the menu order.

So "preserves decision-relevant information" can only mean the converse:
that every source experiment is a garbling of some target experiment, so
the source's information is recoverable from the target. Or it can mean a
bound on how much is lost, which is Le Cam's deficiency taken context by
context. Both are harder questions than the one [CLAIM-125](CLAIM-125.md) states, and
neither is the one it states.

[QUESTION-016](../questions.d/QUESTION-016.md) makes the chain version of the point: "A garbling of a
garbling is a garbling, so sufficiency for Q can only decline along a pure
chain." It does not make the cover version.

## What it does not say

- It does not say part 1 is closed. The converse and the deficiency bound
  are open, and are the real problem.
- It does not say the menu order is the only one. An order that let a
  decision-maker combine contexts across trials, or choose a context at
  random, would pose a different problem. Whichever is meant has to be
  stated.
- It does not cover a transport that depends on the situation, such as a
  translator who knows z. That target need not be a garbling at all
  ([CLAIM-tmpyeik3](CLAIM-tmpyeik3.md)).
- It does not cover adaptive or contextual simulations. Whether the same
  holds for them was not checked.
