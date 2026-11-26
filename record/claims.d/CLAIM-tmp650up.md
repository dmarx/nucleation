---
status: Proposed
title: 'A would-prevail relation always has a potential over its cycles'
statement: >-
  Collapsing each strongly connected component of a negotiation's relation
  of winning moves to one node always leaves an acyclic relation, so on a
  finite set of states a potential always exists over the components even
  where none exists over the states; one-move-at-a-time winning dynamics
  ends in a terminal component, and a terminal component of more than one
  state is a cycle the dynamics never leaves, while a non-terminal cycle is
  passed through on the way to an outcome
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A finite relation of winning moves whose condensation contains a cycle,
  or a run of one-move-at-a-time winning dynamics on a finite set that
  never enters a terminal component. Both are excluded by the standard
  results on strongly connected components; an error in applying them to
  the record's relation of winning moves would defeat it.
tags:
- mathematics
- emotion-and-affect
- game-theory
date: '2026-11-26'
line:
- organizational-affect
- formal-apparatus
complements:
- CLAIM-434
uses:
- TERM-076
- TERM-077
summary: >-
  Prompted by the owner's proposal of 2026-11-26 that a cycle be called
  "indecision" and not the absence of valence. [CLAIM-434](CLAIM-434.md) says a potential
  exists over the states exactly when no chain of winning moves cycles;
  this claim adds what holds when one does. The condensation result and
  the terminal-component result are standard graph theory, and the set is
  the social-choice literature's top cycle (the Smith and Schwartz sets),
  which is not yet on the record. Checked by
  scratch/studies/lead-tmpuszbx/indecision.py. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-076 — Proposed; the definition this result extends -->

# CLAIM-tmp650up: A would-prevail relation always has a potential over its cycles

## The claim

Take the relation of winning moves, loser to winner, over a finite set of
states. Its strongly connected components are the maximal sets of states
that each reach every other by winning moves. Collapsing each component to
a node gives the condensation, and the condensation is always acyclic: a
cycle through two components would merge them into one. By [CLAIM-434](CLAIM-434.md), an
acyclic relation of wins has a potential. So a potential always exists
over the components, though none may exist over the states.

Run the negotiation one winning move at a time from any state. The run
leaves each component it enters for a later one in the condensation's
order, so on a finite set it ends in a *terminal* component, one with no
move out. A run meets three kinds of structure:

- **One state with no move out.** The dynamics stops there: an outcome.
- **More than one state.** The dynamics cycles there for ever: a cycle
  that does not resolve.
- **A non-terminal cycle.** It is passed through and left by a move that
  beats one of its states.

## The check

scratch/studies/lead-tmpuszbx/indecision.py, run with `python3 -I`:

- 2,000 random relations on 2 to 7 states: no condensation is cyclic.
- The majority cycle (would_prevail.py, case 4): one terminal component,
  {a, b, c}.
- A fourth state d that beats c: the cycle is passed through, and d is
  the terminal component.
- A fourth state that feeds the cycle: the cycle is terminal.
- A sparse relation with two basins, a terminal cycle and a single winner:
  which one the dynamics ends in depends on where it starts.

## What it does not say

What a terminal cycle should be called; that is [CLAIM-tmpjylns](CLAIM-tmpjylns.md) and its
alternative [CLAIM-tmp23xiu](CLAIM-tmp23xiu.md). Nor that organizations move one winning move
at a time. [TERM-076](../terms.d/TERM-076.md) already says the reading "does not hold for
simultaneous moves".
