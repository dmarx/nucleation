---
status: Open
title: 'Is the ε⁻² sample complexity of estimating the bisimulation metric between finite Markov chains from occupancy samples optimal, and does an estimator keep a polynomial guarantee on samples from one running trajectory?'
version: 1
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-19'
line: 'pragmatic-transport'
refines:
- QUESTION-008
summary: >-
  Filed when the promotion audit (batch 042, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-280](../theory.d/THEORY-280.md). Theorem 1 of Calo et al. ([LIT-948](../literature.d/LIT-948.md)) was re-checked: an
  ε-accurate estimate from O((|X||Y|(|X|+|Y|) + (|X|+|Y|)log(1/δ))/((1−γ)²ε²))
  independent occupancy samples per chain. That the ε⁻² rate is optimal was
  part of the former promote_when, and this question holds it, with the
  single-stream case the authors expect but do not test.
---

# QUESTION-tmpimdnt: Is the ε⁻² sample complexity of estimating the bisimulation metric between finite Markov chains from occupancy samples optimal, and does an estimator keep a polynomial guarantee on samples from one running trajectory?

## Why it is a question

[THEORY-280](../theory.d/THEORY-280.md) now states an upper bound: with observed finite states, a known
cost bounded by 1 and independent draws from each chain's discounted
state-pair occupancy, a stochastic primal-dual method estimates the
bisimulation metric to ε with probability 1 − δ from a number of samples
polynomial in the state-space sizes, 1/(1−γ), log(1/δ) and 1/ε². Calo et al.
say the ε⁻² dependence is optimal "as can be deduced from" lower bounds for
static optimal transport ([NOTE-763](../notes.d/NOTE-763.md)); they do not prove it for the dynamic
problem, and the dependence on |X| and |Y| has no lower bound at all. Their
guarantee also needs restarts, since an exact occupancy sample runs the chain
from its start to a geometric time; samples from one running trajectory are
correlated and undiscounted, and the authors only "expect" the method to cope.

## What would answer it

A lower bound for estimating the bicausal transport distance between finite
chains from occupancy samples, of order ε⁻² and polynomial in the state-space
sizes, would settle the first part yes; an estimator with a better rate in ε
would settle it no. A guarantee for samples from one trajectory of an ergodic
chain, with the mixing time in place of the restarts, would settle the second
part yes; a family of chains on which the single-stream estimator stays biased
however long it runs would settle it no. More experiments with tuned step
sizes on correlated data cannot settle either: they show behaviour on chosen
chains, not a rate.
