---
number: 270
status: Active
formerly:
- CLAIM-tmpxrn16
title: 'Retaining information about where a Markov chain started and staying
  close to the starting distribution are different properties: a chain can
  forget its initial state while its distribution stays far from where it
  began, so convergence is not preservation and losing information about the
  origin is not degradation'
version: 2
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-081 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-081 rests on; CLAIM-081
    now rests on this claim.
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/CLAIM-270.yaml,
    batch 001, ADR-047). The claim was demonstrated by CASE-017 and by
    argument. Two-state constructions for all four combinations of
    retention and drift are added, so that the warrant shows its
    construction. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: A proof that, for Markov chains in general, the mutual information
  between the initial state and the n-th state and the divergence of the n-th
  marginal from the initial distribution are monotone functions of one another.
  A single chain in which they happen to move together does not count.
tags:
- information-theory
- probabilistic-modeling
date: '2026-10-13'
line:
- formal-apparatus
grounds:
- CASE-017
summary: The general content of [CLAIM-081](CLAIM-081.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  the distinction does not rest, through [CLAIM-056](CLAIM-056.md), on [CLAIM-106](CLAIM-106.md)'s account
  of fidelity. I(U_0; U_n) and D[P(U_n), P(U_0)] answer different questions.
  A contractive chain loses information about its initial state while converging
  to a stationary distribution that can be far from the start. The data-processing
  inequality bounds the first and says nothing about the second.
supports:
- CLAIM-081
- CLAIM-189
- CLAIM-191
---
<!-- inactive-ok-file: CLAIM-056 CLAIM-081 CLAIM-189 CLAIM-191 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-270: Retaining information about where a Markov chain started and staying close to the starting distribution are different properties: a chain can forget its initial state while its distribution stays far from where it began, so convergence is not preservation and losing information about the origin is not degradation

## The claim

For a chain U_0 → U_1 → … → U_n, two quantities are easy to conflate:

- **Retention**, I(U_0; U_n), or I(G(U_0); U_n) for a feature G:
  information about a particular starting point.
- **Drift**, D[P(U_n), P(U_0)]: how far the population's distribution has
  moved from where it began.

They come apart in both directions. A contractive chain started from
different states becomes indistinguishable across starts, so retention
falls toward zero, while it converges to a stationary distribution that
may be far from the initial one. [CASE-017](../cases.d/CASE-017.md) is a constructed instance: chains
started in different states converged on each other while staying
"substantially different from the original". A chain can also stay close in
distribution while scrambling which individual started where.

The data-processing inequality says retention cannot increase along a
Markov chain. It is "not a theorem that messages get less comprehensible":
it says nothing about drift, legibility or structure. A state can become
more conventional, and easier to read, while carrying less information
about its origin.

## Where the record applies it

[CLAIM-081](CLAIM-081.md) applies the distinction to serial reconstruction of utterances.
[CLAIM-189](CLAIM-189.md) and [CLAIM-191](CLAIM-191.md) apply it to an argument restated across sessions.
All three now rest on this claim for the distinction.

## What it does not say

- Which quantity matters for a given question. That depends on whether the
  question is about the original or about the convention.
- That a real transmission chain is Markov. Adding independent historical
  evidence to later states changes the graph and invalidates a naive use
  of the inequality.

## Note of 2026-10-19: the four combinations, constructed

Take two states {a, b}, drift measured in total variation, and one step.

| start P(U_0) | kernel | retention I(U_0; U_1) | drift TV(P(U_1), P(U_0)) |
|---|---|---|---|
| (1/2, 1/2) | both states go to a | 0 | 1/2 |
| (1/2, 1/2) | resample uniformly | 0 | 0 |
| (0.9, 0.1) | swap a and b | H(U_0), the maximum | 0.8 |
| (0.9, 0.1) | identity | H(U_0), the maximum | 0 |

The first two rows have the same retention and different drift. The last
two do as well, so neither quantity is a function of the other. That meets
the defeat condition's terms and fails it: no monotone relation holds for
Markov chains in general.
