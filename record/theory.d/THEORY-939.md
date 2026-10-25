---
number: 939
status: Proposed
formerly:
- THEORY-tmpomtdz
promote_when: >-
  For the characterisation: a proof read and checked (the report states it
  and defers the proof to Wolpert and Tumer's "An Introduction to
  Collective Intelligence", not filed), recorded in this file. For the
  experiment: the version in Intelligent Agent Technology (2001) or the
  Advances in Complex Systems paper (LIT-1515) read and found to
  report the same ordering of clamps. It is refuted by a factored utility
  that is not an increasing function of the world utility given the rest,
  or by a reproduction of the bar problem in which the zero clamp or the
  world utility learns as well as the average-action clamp across
  attendance levels. Results in other problems neither promote nor refute
  the experimental clause.
title: 'In a multi-agent system run against a world utility, a private utility is factored, ranking each agent''s own alternatives with the others fixed as the world utility ranks them, exactly when it is an increasing function of the world utility given the components the agent cannot affect; the world utility minus its value with the agent''s effect set clamped is factored, and in a sixty-agent bar problem clamping to the average action learned better than clamping to absence or using the world utility itself'
version: 1
tags:
- complex-systems
- game-theory
date: '2026-10-24'
source:
- LIT-1506
summary: >-
  Wolpert & Tumer's NASA report ([LIT-1506](../literature.d/LIT-1506.md)), read in full in NOTE-
  tmpo0w02 because their Advances in Complex Systems paper ([LIT-1515](../literature.d/LIT-1515.md))
  could not be reached. The characterisation is stated with its proof
  deferred; the "if" half and the WLU's factoredness were checked when
  filed. Factoredness is ordinal, member by member, and needs no scale
  shared among members. The WLU is not a causal counterfactual: it re-
  scores the actual history with one member's part replaced. Removal was
  not the best clamp.
---
<!-- inactive-ok-file: NOTE-1153 LIT-1515 — the reading this is filed from, and the Unavailable paper it stands in for -->

# THEORY-939: In a multi-agent system run against a world utility, a private utility is factored, ranking each agent's own alternatives with the others fixed as the world utility ranks them, exactly when it is an increasing function of the world utility given the components the agent cannot affect; the world utility minus its value with the agent's effect set clamped is factored, and in a sixty-agent bar problem clamping to the average action learned better than clamping to absence or using the world utility itself

## Source

Wolpert & Tumer, [LIT-1506](../literature.d/LIT-1506.md), read in [NOTE-1153](../notes.d/NOTE-1153.md) from the NASA
Technical Reports Server copy (document 20010066523): the definition of
factored, the Theorem and Eq. 1, and the WLU (p. 3); the clamp derivation
(p. 4); the bar-problem results and Figure 1 (pp. 5–6).

## What was actually shown

- **Factored.** γ_η(C(ζ₀)) ≥ γ_η(C(ζ′₀)) ⇔ G(C(ζ₀)) ≥ G(C(ζ′₀)) for
  initial states differing only for η.
- **The characterisation (stated).** Factored at every ζ iff γ_η = Φ_η(ζ
  outside η's effect set, G(ζ)) with ∂Φ_η/∂G > 0; the proof is in the
  authors' earlier work. The "if" half is immediate: with the first
  argument fixed, which a change in η's state cannot alter, Φ_η increasing
  in G orders η's alternatives as G does. Checked when filed.
- **The WLU is factored.** G(ζ) − G(CL(ζ)): the subtracted term depends
  only on components outside η's effect set, so the WLU is Φ_η with
  Φ_η(x, g) = g − G(CL(·)). Checked when filed.
- **The experiment.** 60 agents, attendance sets of 1 to 6 of 7 nights,
  20 runs. The average-action clamp performed well at every level; the zero
  clamp nearly as well, slipping as nights increased; the all-ones clamp
  poorly for few nights; G worst throughout (Figure 1a).

## What this does not say

- **That the WLU answers "what if the agent had not acted".** Others'
  behaviour is held as it was; it needs no model of their response.
- **That the optimal clamp is derived.** The derivation is "too long to go
  through here".
- **Anything beyond one congestion game** with simple Boltzmann learners,
  where each agent's effect set is taken to be its own actions.
- **What the Advances in Complex Systems paper adds**, a new framework and
  the Aristocrat Utility, which was not read.
