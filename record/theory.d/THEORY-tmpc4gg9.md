---
status: Proposed
promote_when: >-
  A replication with several seeds and reported spread in which independent
  deep Q-learners in the two games again show the opposite effect of
  network size (more defection with more capacity in Gathering, less in
  Wolfpack), with cooperative and defecting policies classified by
  measured behaviour rather than by training environment; and the AAMAS
  2017 version read and found to report the same. It is refuted if the
  sign of the capacity effect does not differ between the games, or if the
  played-off policies do not give Prisoner's Dilemma payoffs in both.
  Results about real societies neither promote nor refute it; it is a
  finding about these simulations.
title: 'In two two-player Markov games whose learned cooperative and defecting policies, played against each other, both give Prisoner''s Dilemma payoffs, independent deep Q-learners responded oppositely to capacity: more hidden units raised aggression in a fruit-gathering game, where tagging a rival is the harder policy to implement, and lowered lone hunting in a wolfpack game, where coordination is; in the gathering game, aggression was learned where apples were scarce or a tagged rival stayed out long'
version: 1
tags:
- game-theory
- social-science
date: '2026-10-24'
source:
- LIT-tmphih4i
summary: >-
  Leibo, Zambaldi, Lanctot, Marecki and Graepel (2017), read in full in
  NOTE-tmpke0z1 from arXiv v1. A descriptive simulation with no seeds or
  spread reported, policies classed by training environment, two agents,
  fixed conditions, apples on a fixed respawn timer, and a mismatch
  between the text's and Figure 7's settings for batch and network size.
---
<!-- inactive-ok-file: NOTE-tmpke0z1 — the reading this is filed from -->

# THEORY-tmpc4gg9: In two two-player Markov games whose learned cooperative and defecting policies, played against each other, both give Prisoner's Dilemma payoffs, independent deep Q-learners responded oppositely to capacity: more hidden units raised aggression in a fruit-gathering game, where tagging a rival is the harder policy to implement, and lowered lone hunting in a wolfpack game, where coordination is; in the gathering game, aggression was learned where apples were scarce or a tagged rival stayed out long

## Source

Leibo, Zambaldi, Lanctot, Marecki & Graepel (2017), LIT-tmphih4i, read in
NOTE-tmpke0z1 from arXiv:1702.03037v1: sections 5.1–5.3 and Figures 4, 6
and 7 (pp. 4–7).

## What was actually shown

- **Scarcity and aggression.** Beam use after 40 million training steps
  is high with scarce apples or long removal, low with plentiful apples or
  short removal (Figure 4A), and once changed during learning almost
  always rises.
- **Embedded dilemmas.** Policies from the two kinds of environment,
  played against each other, give mostly Prisoner's Dilemma matrices in
  Gathering and Prisoner's Dilemma, Chicken and Stag Hunt in Wolfpack
  (Figure 6).
- **Capacity.** A larger network raises aggression in Gathering and lowers
  lone-wolf capture in Wolfpack (Figure 7, right); the authors explain it
  by which policy needs more coordination to implement. Less discounting
  raises defection and a larger replay batch lowers it in both games.

## What this does not say

That the effects are robust: no seeds or spread are reported, and the
settings in Figure 7 differ from those in the text. That the policies
are cooperative or defecting by any measure independent of the
environment they were trained in. Anything about more than two agents,
a depletable resource, institutions, or what happens when scarcity
changes during learning. Or anything about human cooperation, which the
authors offer only as a modelling analogy for habit.
