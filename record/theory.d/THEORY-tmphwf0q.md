---
status: Proposed
promote_when: >-
  A second source derives, for geometric Brownian motion stopped at an
  exponentially distributed time of rate ν, the double Pareto law with
  exponents α and −β the roots of ½σ²s² + (μ − ½σ²)s − ν = 0, or the record
  derives it; and the deterministic case's survival x^(−ν/μ). Mitzenmacher
  (THEORY-2150) derives the zero-drift case, which meets it for μ = ½σ²
  only. Not met by the birth-and-death or branching results, which the
  title does not assert.
title: 'Reed and Hughes show that a process growing exponentially in expectation and killed at a time with constant hazard has a power-law tail, a single Pareto for deterministic growth and a double Pareto set by a quadratic for geometric Brownian motion'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 from the delegated reading in NOTE-tmpbic9d; quotations
    rechecked by the filer against the text.
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-22'
source:
- LIT-3007
bears_on:
- QUESTION-505
summary: >-
  Reed and Hughes (2002), [LIT-3007](../literature.d/LIT-3007.md), read in [NOTE-tmpbic9d](../notes.d/NOTE-tmpbic9d.md). Killing
  exponential growth at a random time gives power-law tails; with noise
  the law is a double Pareto whose exponents solve a quadratic. Support for
  its applications is visual. Proposed until the general double Pareto is
  derived independently.
---
<!-- inactive-ok-file: CLAIM-795 THEORY-2150 SYNTHESIS-119 CLAIM-824 — Proposed or new; this account's reading and the entries it bears on -->

# THEORY-tmphwf0q: Reed and Hughes show that a process growing exponentially in expectation and killed at a time with constant hazard has a power-law tail, a single Pareto for deterministic growth and a double Pareto set by a quadratic for geometric Brownian motion

## Source

Reed and Hughes (2002), [LIT-3007](../literature.d/LIT-3007.md), read in [NOTE-tmpbic9d](../notes.d/NOTE-tmpbic9d.md) from the published
version on the first author's faculty page.

## What was actually shown

"Consider the simple case of deterministic exponential growth X(t) = e^(μt)
killed at a random time T which is exponentially distributed with
parameter ν": the killed state has survival x^(−ν/μ) above 1 (p. 1). For
geometric Brownian motion "the distribution of X̄ is a two-sided Pareto or
double Pareto distribution", with α and −β "the roots of the quadratic
equation" ½σ²s² + (μ − ½σ²)s − ν = 0 (p. 2, eqs. 8–9). At zero log drift
α = β = √(2ν)/σ; as σ → 0 the upper root tends to ν/μ (checked by the filer,
python3 -I). Analogues are stated for multiplicative, birth-and-death and
Galton–Watson processes, with proofs elsewhere.

## What this does not say

- Not that the exponent is a bare ratio of rates, except for deterministic
  growth.
- Not that any of its empirical systems was produced by this mechanism:
  the evidence is log-log linearity, with no fit or test against the
  lognormal.
- Not that "identical growth rates can coexist with highly unequal sizes";
  that is A's gloss on the deterministic case.

## Connections

Item 6 of [CLAIM-795](../claims.d/CLAIM-795.md); [SYNTHESIS-119](../syntheses.d/SYNTHESIS-119.md)'s random observation time; [CLAIM-824](../claims.d/CLAIM-824.md)'s
Gibrat-plus-random-time route (filer A's file). Mitzenmacher ([THEORY-2150](THEORY-2150.md))
reports it and derives the zero-drift case. It `bears_on` [QUESTION-505](../questions.d/QUESTION-505.md). It
is not in `corroborates` on [CLAIM-795](../claims.d/CLAIM-795.md): the claim's item 6 grounds on it.
