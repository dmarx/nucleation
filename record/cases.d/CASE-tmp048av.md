---
status: Active
title: "Twitch Plays Pokémon in democracy mode, with the running tally shown while the votes come in"
version: 1
standing: stipulated
tags:
- agency
- complex-systems
- behavioral-integration
date: '2026-10-12'
line: will-organization
variant_of:
- CASE-tmpez60y
summary: >-
  The crowd of [CASE-tmpez60y](CASE-tmpez60y.md) in democracy mode. Each move is the button
  that collects the most votes in a short window, and the running tally
  is shown while the votes arrive, so the current majority can sway the
  votes still coming. The owner judges it a better demonstration of a
  population with drift-diffusion decision dynamics than anarchy mode.
  Showing the tally adds feedback, and feedback moves the dynamics
  toward winner-take-all.
illustrates:
- CLAIM-tmp6vyef
- CLAIM-158
- CLAIM-122
- CLAIM-tmp5vc3p
---

# CASE-tmp048av: Twitch Plays Pokémon in democracy mode, with the running tally shown while the votes come in

## The case

This is the same crowd and the same game as [CASE-tmpez60y](CASE-tmpez60y.md), in democracy
mode. Votes for each button are counted over a short window, and when
the window closes the button with the most votes is pressed. The owner
stipulates one more feature, given on 2026-10-12: "a version where the
vote tally is visible while votes are coming in (i.e. so the current
state of majority can influence the ongoing vote process)".

Whether the original stream showed the tally live has not been checked
here. The owner poses the case as a version to imagine, so it is
stipulated.

## What it can show

The owner's judgement is that it demonstrates drift-diffusion decision
dynamics better than anarchy mode does. The reasons below are the
assistant's.

- **Each move is a decision by accumulation.** In anarchy mode it is the
  avatar's position that drifts and diffuses, and that is a walk, not a
  choice. Here every move is a choice. Votes accumulate for each
  alternative, and the choice is fixed when the window closes. That is
  the interrogation protocol of [THEORY-068](../theory.d/THEORY-068.md): a decision read out at a
  fixed time rather than at a threshold.
- **A hidden tally is the balanced case.** If voters cannot see the tally,
  their votes are independent, and the counts are perfect integrators
  with no leak and no inhibition. For two buttons the difference of the
  counts is a random walk with drift, which is the drift diffusion model
  itself.
- **A visible tally adds feedback.** If the leading count draws further
  votes, the accumulators excite themselves, or equivalently inhibit
  their rivals more than they leak. In [THEORY-068](../theory.d/THEORY-068.md)'s terms the net leak
  turns negative. Early votes then weigh more than late ones (primacy),
  and the process tends toward winner-take-all, like herding in an
  information cascade.

So the visible tally is a dial on the constitution. Without it the crowd
is a balanced integrator. With it the crowd moves toward commitment
early, the regime where switching between stable states looks like the
better description. That is the dependence on constitution that
[CLAIM-tmp6vyef](../claims.d/CLAIM-tmp6vyef.md) claims, in one system.

## What it cannot show

It is stipulated, so it illustrates and bears no weight. Two things are
not settled here:

- **The feedback's sign.** That a visible majority attracts votes and
  does not provoke contrarians is assumed, not measured.
- **The reduction.** With eight buttons and a goal that changes, the
  case falls outside [THEORY-068](../theory.d/THEORY-068.md)'s conditions, two alternatives and
  stationary evidence. The reduction to one drift-diffusion variable
  holds only for a two-way vote.
