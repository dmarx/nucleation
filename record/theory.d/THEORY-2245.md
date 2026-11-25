---
number: 2245
status: Proposed
formerly:
- THEORY-tmp8cdhs
promote_when: >-
  An independent simulation of two uncoupled groups of noisy phase
  oscillators with the same common noise shows their complex order
  parameters converging (|Z₁ − Z₂| → 0) from different initial states at a
  within-group noise correlation well below 1, and diverging when the
  common noises differ.
title: 'Ko shows that two groups of phase oscillators with no coupling between them, each driven by a common noise plus independent local noise, synchronize their collective order parameters when the common noise is the same for both, from any initial state and down to a within-group noise correlation near 0.1, proved for uncoupled groups at large N and seen numerically with coupling inside the groups, which can weaken it'
version: 1
tags:
- complex-systems
- network-science
date: '2026-11-22'
source:
- LIT-2245
bears_on:
- QUESTION-063
summary: >-
  From the reading of [LIT-2245](../literature.d/LIT-2245.md) in [NOTE-2335](../notes.d/NOTE-2335.md), for [LEAD-023](../leads.d/LEAD-023.md). A model in
  which synchrony between the collective variables of two groups is wholly
  exogenous. It does not say how to tell such synchrony from coupling in
  data. Proposed until its promote_when is met.
---

# THEORY-2245: Ko shows that two groups of phase oscillators with no coupling between them, each driven by a common noise plus independent local noise, synchronize their collective order parameters when the common noise is the same for both, from any initial state and down to a within-group noise correlation near 0.1, proved for uncoupled groups at large N and seen numerically with coupling inside the groups, which can weaken it

## Source

Ko (2026), [LIT-2245](../literature.d/LIT-2245.md), read in [NOTE-2335](../notes.d/NOTE-2335.md).

## What was actually shown

Euler–Maruyama simulations of two groups of N = 1000 phase oscillators
under common and local noise, in four cases (identical or not, coupled
within or not), started from contrasting states. With the same common
noise the order parameters converge; with different common noises they do
not, which is the control that could have come out otherwise. For
uncoupled groups a phase-density map shows equal densities are invariant
and that their overlap grows to 1.

## What this does not say

That shared drive is the explanation of any observed between-group
synchrony, or how to detect it. That the result holds for groups with
different frequency distributions, for partly shared drives, or for
coupled groups as a theorem: the last is numerical only.
