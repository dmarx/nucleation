---
number: 74
status: Active
formerly:
- CASE-tmp048av
title: "Twitch Plays Pokémon in democracy mode, with the running tally shown while the votes come in"
version: 4
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: the crowd formalized as a network of accumulators
    (CASE-160), its conditions held by CLAIM-453, and a reported
    run of the visible tally. The case is unchanged.
- version: 3
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-077 (ADR-092), from the reading review of
    2026-11-11, by question. The question takes it as its instance: in
    democracy mode with the tally visible, the voters agree because
    "each one sees where the majority is going and follows it",
    agreement "produced by the coupling" while "the voters' valuations
    need not move at all". No other change.
- version: 4
  date: '2026-11-12'
  note: >-
    Draws on THEORY-068 ("That is the interrogation protocol of
    THEORY-068"). First application of draws_on (ADR-095). No
    other change.
standing: stipulated
kind: specimen
tags:
- agency
- complex-systems
- behavioral-integration
date: '2026-10-12'
line: will-organization
variant_of:
- CASE-075
summary: >-
  The crowd of [CASE-075](CASE-075.md) in democracy mode. Each move is the button
  that collects the most votes in a short window, and the running tally
  is shown while the votes arrive, so the current majority can sway the
  votes still coming. The owner judges it a better demonstration of a
  population with drift-diffusion decision dynamics than anarchy mode.
  Showing the tally adds feedback, and feedback moves the dynamics
  toward winner-take-all.
illustrates:
- CLAIM-262
- CLAIM-158
- CLAIM-122
- CLAIM-261
bears_on:
- QUESTION-077
draws_on:
- THEORY-068
---
<!-- inactive-ok-file: ADR-095 — Proposed; the decision the history note of 2026-11-12 applies -->

# CASE-074: Twitch Plays Pokémon in democracy mode, with the running tally shown while the votes come in

## The case

This is the same crowd and the same game as [CASE-075](CASE-075.md), in democracy
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
[CLAIM-262](../claims.d/CLAIM-262.md) claims, in one system.

## What it cannot show

It is stipulated, so it illustrates and bears no weight. Two things are
not settled here:

- **The feedback's sign.** That a visible majority attracts votes and
  does not provoke contrarians is assumed, not measured.
- **The reduction.** With eight buttons and a goal that changes, the
  case falls outside [THEORY-068](../theory.d/THEORY-068.md)'s conditions, two alternatives and
  stationary evidence. The reduction to one drift-diffusion variable
  holds only for a two-way vote.

## Note of 2026-10-25: the crowd as a network of accumulators

From A35–A37 of the exchange of 2026-10-24, continued.

- **The reduction.** [CASE-160](CASE-160.md) formalizes this crowd as a linear
  network of accumulators. The hidden tally is the balanced case κ = λ,
  where the influence-weighted support is exactly a drift-diffusion
  process. The visible tally adds positive feedback, κ > λ. In
  [CASE-155](CASE-155.md)'s two-process form the hidden tally is c = 0 and the
  visible one c > 0, with c < 0 the contrarian case. [CLAIM-453](../claims.d/CLAIM-453.md) holds
  the conditions.
- **A35 found this case** "already describes your proposed experiment
  remarkably closely". It proposed running both protocols, free response
  and the fixed window this case describes, and leaving the feedback's sign
  free ("Some participants might follow the majority; others might react
  against it"). That is this case's "What it cannot show".
- **A reported run.** A37 reported a population simulation whose "positive
  public-tally feedback" condition decided faster and less accurately than
  the balanced one: 18.5 against 49.5 steps, and 67.1% against 85.4%
  correct. The run is not held and its parameters are not given. The
  direction is the one this case predicts for a visible tally, and a check
  with fixed bounds and κ − λ from 0 to 2 confirms it ([CASE-160](CASE-160.md)).

The case is unchanged.

## Note of 2026-11-04: the mode vote as a rule for selecting actions, from "Organizational Nucleation and SLT"

The owner's U16 pointed to the Twitch Plays Pokémon and r/place cases as
"particularly illuminating here". A16 used this case and [CASE-075](CASE-075.md).

- **A command vote is a first-order intervention.** A16 §3 calls a chat
  command "ordinarily a **first-order intervention**". In the owner's
  sense (U17, as the owner clarified at review), an intervention is taking
  an action on the current state, so a vote crosses the player's
  intervention threshold. What it does not show is its aim: a player may
  vote left to move left, to follow the majority or to frustrate another
  group.
- **The mode vote is one level up.** "Ordinary button votes select actions;
  a vote about which mode should govern selects a *rule for selecting
  actions*." That is the shape of a higher-order volition ([TERM-102](../terms.d/TERM-102.md)).
  A16: "The analogy is not identity".
- **The tally coordinates without changing criteria.** A16 §6: under the
  shown tally the crowd can converge "because participants see where the
  majority is going", which can be "coordination without changed
  endorsement criteria". The spiral of silence ([THEORY-242](../theory.d/THEORY-242.md)) is the held
  case of expressed opinion leaving private opinion with no member changing
  belief.

The Reddit case is [CASE-079](CASE-079.md), r/place. No status changes.
