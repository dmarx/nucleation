---
status: Proposed
promote_when: >-
  A second reading of the published text (Contemporary Physics 46,
  323–351), or an independent source, confirms what the title says: that
  Newman recommends the cumulative distribution and the maximum-likelihood
  exponent over a least-squares line on a log-log histogram, which biases
  the exponent; that he gives the catalogue named, with α = 1 − a/b for
  combinations of exponentials, α = 1 + 1/γ for inverse powers, 3/2 for
  the walk's first return and α = 2 + (k0 + c)/m for the general Yule
  process; and that he holds that different mechanisms apply to different
  cases and that most observed power laws are probably not the result of
  phase transitions.
title: "Newman recommends measuring a power law by its cumulative distribution and a maximum-likelihood exponent rather than a least-squares fit to a log-log histogram, and holds that many mechanisms produce power laws, among them combinations of exponentials, inverses of quantities, random-walk first return times, the Yule process, critical phenomena and self-organized criticality, that different ones apply to different cases, and that most observed power laws are probably not the result of phase transitions"
version: 1
tags:
- complex-systems
- probabilistic-modeling
date: '2026-11-22'
source:
- LIT-2976
corroborates:
- CLAIM-803
- CLAIM-841
- CLAIM-817
- CLAIM-824
- CLAIM-815
bears_on:
- QUESTION-505
summary: >-
  Newman (2005), [LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md). A tutorial review: its
  results are mostly other people's, with heuristic derivations the author
  flags. What the record uses is the catalogue of mechanisms with their
  exponents, which grounds items 2, 3, 6 and 7 of [CLAIM-795](../claims.d/CLAIM-795.md) and adds four
  mechanisms with no feedback (random typing, highly optimized tolerance,
  coherent noise, record dynamics), and its judgement that most observed
  power laws are probably not from phase transitions. It has no model
  comparison, and it calls the Yule process the most widely accepted
  theory for citations, cities and income. Proposed until the reading is
  confirmed.
---
<!-- inactive-ok-file: CLAIM-795 CLAIM-815 — Proposed; the claims this reading grounds or corroborates, and the argument for the first -->

# THEORY-tmp6jdas: Newman recommends measuring a power law by its cumulative distribution and a maximum-likelihood exponent rather than a least-squares fit to a log-log histogram, and holds that many mechanisms produce power laws, among them combinations of exponentials, inverses of quantities, random-walk first return times, the Yule process, critical phenomena and self-organized criticality, that different ones apply to different cases, and that most observed power laws are probably not the result of phase transitions

## Source

Newman (2005), "Power laws, Pareto distributions and Zipf's law",
Contemporary Physics 46, 323–351, [LIT-2976](../literature.d/LIT-2976.md), read in full from the arXiv
v3 in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md).

## The account

Measuring: a straight-looking log-log histogram "is, in most cases, a poor
way proceed" [sic] (p. 3), and least squares biases the exponent (2.26 ±
0.02 against a true 2.5 on synthetic data, where the maximum-likelihood
estimate gives 2.500 ± 0.002, p. 4); "a power-law model is only one of
several possibilities" (p. 8).

Mechanisms, with "many different mechanisms for producing power laws and
... different ones ... applicable to different cases" (p. 5):

- an exponentially distributed y with x ∝ e^(by): α = 1 − a/b (random
  typing; Reed and Hughes's growth observed at an exponential age);
- an inverse power x = y^(−γ) with p(y = 0) finite: α = 1 + 1/γ;
- the first return time of a symmetric walk: α = 3/2;
- the Yule process with initial value k0 and offset c: α = 2 + (k0 + c)/m,
  "the most widely accepted theory" for citations, city populations and
  personal income (p. 19);
- critical phenomena, which need tuning and so are "an unlikely
  explanation for generic power-law distributions" (p. 19), and
  self-organized criticality, "probably not the universal law that some
  have claimed it to be" (p. 22);
- highly optimized tolerance, coherent noise, multiplicative processes
  with a lower bound, record dynamics (§IV.G).

And "most experimentally observed power laws are probably not the result
of phase transitions" (p. 12).

What could have come out otherwise: little, since the formulas are known.
The filer checked the identities (python3 -I): with a = −λ and b = g,
1 − a/b = 1 + λ/g, Reed's density exponent, so the survival exponent is
λ/g, [CLAIM-795](../claims.d/CLAIM-795.md)'s item 6; x = 1/y gives γ = 1 and α = 2; the Yule
exponent at m = 2, k0 = 1, c = 0 is 2.5, and at k0 = 0, c = m it is 3.

## What this does not say

- Not a test of fit or a comparison with alternatives; that is [LIT-2987](../literature.d/LIT-2987.md).
- Not anything on critical branching, rate mixtures or sample-space
  reduction (items 1, 4 and 5 of [CLAIM-795](../claims.d/CLAIM-795.md)), nor on the hitting-time
  identity behind [CLAIM-815](../claims.d/CLAIM-815.md).
- Not that the shape of a distribution says nothing about mechanism:
  Newman assigns mechanisms by plausibility.
