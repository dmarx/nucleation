---
number: 75
status: Active
formerly:
- CASE-tmpez60y
title: "Twitch Plays Pokémon in anarchy mode: one avatar steered through the map by the running aggregate of a crowd's inputs"
version: 1
standing: documented
tags:
- agency
- complex-systems
- behavioral-integration
date: '2026-10-12'
line: will-organization
summary: >-
  In February 2014 a stream let everyone in its chat play one copy of
  Pokémon Red at once, with every typed button press executed in turn.
  The owner offers its navigation as a working approximation of an agent
  made of a population whose decisions follow drift-diffusion dynamics.
  The crowd's direction reorganizes continuously and is not switched.
  The record holds no source for the case yet.
illustrates:
- CLAIM-262
- CLAIM-025
variants:
- CASE-074
---

# CASE-075: Twitch Plays Pokémon in anarchy mode: one avatar steered through the map by the running aggregate of a crowd's inputs

## The case

In February 2014 an anonymous programmer streamed a game of Pokémon Red
on Twitch, wired so that commands typed in the stream's chat ("up",
"left", "a" and so on) were executed as button presses. Tens of
thousands of people typed at once. In the original mode, later called
anarchy, every command was executed in the order received. The
protagonist moved one step at a time, as the net result of a stream of
inputs that disagreed. Some players pushed toward the goal, some pushed
elsewhere, and some trolled. The game was nonetheless finished. A
democracy mode was added during the run. It tallied the votes over a
short window and executed the winner. Players switched between the two
modes by a vote, shown on an on-screen meter.

The owner's reading, given on 2026-10-12: the navigation regimes of the
collective "operationalize an approximation of the
agent-as-population-subject-to-drift-diffusion-decision-dynamics case".
In anarchy mode the avatar's position is the integral of a noisy input
stream with a bias, a random walk with drift. Reaching an exit or a
door is a boundary crossing. One-way ledges, which the crowd notoriously
kept stepping off, act as partly absorbing boundaries.

## What it can show

That an agent made of a population can be coordinated continuously. The
crowd's net direction shifts as its composition and attention shift,
with no moment at which one state of the whole gives way to another. It
is the continuous case of [QUESTION-079](../questions.d/QUESTION-079.md). It is also a case in which
the parts stay differentiated and keep disagreeing while the whole makes
progress ([QUESTION-078](../questions.d/QUESTION-078.md)).

An observation by the assistant, not the owner's: the same run also had
a discrete switch. The anarchy/democracy meter changed the collective's
constitution at a threshold. So one collective shows both forms,
continuous reorganization inside a mode and a switch between modes.

The owner later judged democracy mode the better demonstration of
drift-diffusion dynamics, especially with the running tally visible as
votes come in. That is filed as the stipulated variant [CASE-074](CASE-074.md).
Anarchy mode shows a drifting walk, and democracy mode shows a decision
by accumulation.

## What it cannot show

The standing is documented, but the record holds no source. The facts
above are general knowledge, to be checked against a source before the
case bears weight. Nobody has fitted a drift-diffusion model to the
input logs here, so "approximates" is the owner's reading, not a
measured fit. The input set has eight buttons, not two alternatives, and
the crowd's bias changes over time. Both put it outside the conditions
of [THEORY-068](../theory.d/THEORY-068.md).
