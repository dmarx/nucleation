---
status: Proposed
title: 'First Contact''s one failure is a choice of level: a shared-autonomy assistant that stabilizes the lander overrides the user''s commands, damping their influence over the next state while raising it over the episode, so command-to-outcome information depends on the horizon it is taken at, and the horizon the method needs is the level of a rate hierarchy at which the user''s goals live; the task knowledge it assumes away is knowledge of that level'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A shared-autonomy case where the horizon at which command-to-outcome
  information tracks task success is not set by the timescale of the
  user's goals, for instance one where it tracks success at every horizon,
  or at a horizon unrelated to how fast the user's goals change; or an
  account of the Lunar Lander inversion that explains it without the
  assistant's overriding damping short-horizon influence.
tags:
- learning-theory
- control-theory
- information-theory
date: '2026-11-21'
line:
- will-organization
- distributed-agency
rests_on:
- CLAIM-tmpydua7
- CLAIM-361
- CLAIM-478
- CLAIM-761
uses:
- TERM-tmp0g123
complements:
- CLAIM-tmpydua7
summary: >-
  The second half of the relation the owner asked for on 2026-11-21, between
  the record's account of learning occasioned by obstruction and First
  Contact (Reddy, Levine and Dragan, 2022; [ANTH-LIT-503](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-503.md)): its failure case
  read through the record's accounts of rate differences and stabilization.
  The assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpydua7 TERM-tmp0g123 CLAIM-478 — Proposed or Open; the claims and term this joins -->

# CLAIM-tmpspx4i: First Contact's one failure is a choice of level: a shared-autonomy assistant that stabilizes the lander overrides the user's commands, damping their influence over the next state while raising it over the episode, so command-to-outcome information depends on the horizon it is taken at, and the horizon the method needs is the level of a rate hierarchy at which the user's goals live; the task knowledge it assumes away is knowledge of that level

## The failure

In the fifth domain, shared-autonomy Lunar Lander, the one-step score
I(x_t; (s_t, s_{t+1})) correlated strongly *negatively* with task success.
The assistant helps by preventing crashes, "which necessarily involves
ignoring a large fraction of the user's commands" (the paper, as the
anthology reads it, [ANTH-NOTE-250](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-250.md)). Taking the score at the episode's length
restored a positive correlation, and the authors name choosing Δ, which
"requires prior knowledge of the timescale of the user's desired influence",
as the primary limit on the method. [CLAIM-361](CLAIM-361.md) already reads this as a proxy
scoring relief as suppression, with the horizon part of the comparison.

## The relation

**The assistant stabilizes.** In [TERM-tmp0g123](../terms.d/TERM-tmp0g123.md)'s sense the assistant damps
perturbations of the lander's state toward a safe set. Damping is what an
override is: the next state depends less on the command. So stabilization
lowers the user's influence at the fast scale by construction, and raises
it at the slow one, since a lander that has not crashed is one whose later
states the user can still steer. [CLAIM-761](CLAIM-761.md) holds that a stabilized
constraint can be stored work that enlarges what is realizable; this is the
case where it enlarges reach at one scale by narrowing it at another.

**So the horizon is a level.** [CLAIM-478](CLAIM-478.md) holds that rate differences help
make structure: degrees of freedom that settle faster than others become a
constraint on them over the window between the two rates. Here the fast
level is the vehicle's state, which the assistant settles; the slow level is
the user's goal, where to land. Command-to-outcome information taken inside
the fast window measures the assistant's damping; taken across the window,
at the slow level, it measures the user's control of the goal. The right Δ
is a time between the two rates, and the knowledge the method assumes away
is which level of that hierarchy the user's goals live at.

**What it adds to the obstruction account.** [CLAIM-tmpydua7](CLAIM-tmpydua7.md) reads First
Contact as forming a channel to repair a failure of information. This half
says a channel has a level: help that stabilizes one level can look, at that
level, like the channel failing. A diagnosis of an obstruction ([CLAIM-556](CLAIM-556.md)'s
levels, [QUESTION-404](../questions.d/QUESTION-404.md)) needs the level at which influence is judged, chosen
before scoring, as [CLAIM-361](CLAIM-361.md) requires of the horizon.

## What it does not say

- Not that the level can always be found from the data. The paper's fix
  used the task's episode length; the claim is that some such knowledge is
  needed, not how to get it.
- Not that the record's rate-hierarchy results ([CLAIM-780](CLAIM-780.md) and those around
  it) apply quantitatively. They are for chains with separated rates; a
  lander with an assistant was not modelled.
- Whether stabilizing help erodes the user's own capacity is a separate
  question, [QUESTION-tmp6iu8e](../questions.d/QUESTION-tmp6iu8e.md).
