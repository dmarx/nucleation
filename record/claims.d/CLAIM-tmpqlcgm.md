---
status: Proposed
title: 'Yields cannot tell a generative nucleus from one that only gives a head start: two assemblies can have the same chance of success with the nucleus established and without it, one because the nucleus speeds a later step among other components and one because it does not, so only the rate of that later step, compared with and without the nucleus, identifies the route'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a recomputation of the two-part model
  with its stated rates in which the two systems' success probabilities
  differ in either arm; or a proof that, for absorbing Markov assemblies,
  the success probabilities with and without an established nucleus
  determine whether the nucleus changes the rates of steps it takes no
  part in. Not defeated by richer measurements, such as time courses,
  that may separate the two systems; the claim is about yields.
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-11-05'
line:
- realizability
- formal-apparatus
uses:
- TERM-tmp3awsy
complements:
- CLAIM-tmpiyvk1
bears_on:
- QUESTION-tmp4jbc3
- QUESTION-380
summary: >-
  The assistant's, on the owner's invitation of 2026-11-05 to add claims
  to the DNA origami filing, and a partial answer to A's question
  [QUESTION-tmp4jbc3](../questions.d/QUESTION-tmp4jbc3.md). The model has two parts: a nucleus N, and a later
  part B formed by other components. N forms at rate a; B at b0 without N
  and b1 with it; any unfinished state traps at κ. A generative system,
  with a = 1, b0 = 0.5, b1 = 2 and κ = 0.5, succeeds 80.0 % of the time
  with N established and 56.7 % without. A system where N gives only a
  head start, b0 = b1 = 2 with a ≈ 0.799 and κ = 0.5, gives the same two
  numbers. The interventional effect on yield is identical, 23.3 points,
  and the routes differ: the downstream rate changes by 1.5 in one and 0
  in the other. Checked in scratch/formal/dna_origami_toys.py. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: TERM-tmp3awsy — Proposed, Skimmed or new; entries cited as open -->

# CLAIM-tmpqlcgm: Yields cannot tell a generative nucleus from one that only gives a head start: two assemblies can have the same chance of success with the nucleus established and without it, one because the nucleus speeds a later step among other components and one because it does not, so only the rate of that later step, compared with and without the nucleus, identifies the route

## The construction

Two parts must both form for the target: the nucleus N and a downstream
part B made by components outside N. From the state with neither, N forms
at rate a and B at rate b0. With N present, B forms at b1. With B present,
N still forms at a. Every unfinished state traps at rate κ, absorbing.

Starting with N established, the chance of success is b1/(b1 + κ).
Starting with neither,

  q(∅) = (a · b1/(b1 + κ) + b0 · a/(a + κ)) / (a + b0 + κ).

| System | a | b0 | b1 | κ | with N | without N | Δk(B) |
|---|---|---|---|---|---|---|---|
| generative | 1 | 0.5 | 2 | 0.5 | 0.800 | 0.567 (17/30) | 1.5 |
| head start only | 0.799 | 2 | 2 | 0.5 | 0.800 | 0.567 | 0 |

The two systems give the same success with and without the nucleus, and
so the same interventional effect Δ_N = 0.233. In the first, the nucleus
quadruples the rate at which other components form B. In the second, B
forms at the same rate either way, and establishing N helps only by
sparing the time it would take to form.

## The claim

1. **Yields do not identify the route.** Since two systems can agree in
   both arms, no function of these yields separates a generative nucleus
   from a head start.
2. **The downstream rate does.** The quantity that differs is A's
   Δk(y → y′) = k(y → y′ | do(N = 1)) − k(y → y′ | do(N = 0)), here the
   rate of forming B with and without N, measured within one system. A
   matched-state comparison of that rate is the decisive measurement, as
   [QUESTION-tmp4jbc3](../questions.d/QUESTION-tmp4jbc3.md) says.

## What it adds

- **To [QUESTION-tmp4jbc3](../questions.d/QUESTION-tmp4jbc3.md):** A asked for downstream hazards "not only final
  yield". This shows that final yield, even in both arms, cannot stand in
  for them.
- **To [TERM-tmp3awsy](../terms.d/TERM-tmp3awsy.md):** a productive nucleus, judged by Δ_N, may or may
  not be generative. Calling one generative needs the hazard measurement.
- **In DNA origami:** Schneider, Möritz and Dietz's deletion of early
  segments showed slower folding, a yield-and-time effect. Per-staple
  binding rates with and without the early segments, at matched
  progress, would decide the route.

## What it does not say

- **That time courses cannot separate the systems.** They may: the two
  differ in the time to success. The claim is about success
  probabilities.
- **Anything about which route real nuclei take.**
