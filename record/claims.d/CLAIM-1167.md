---
number: 1167
status: Active
formerly:
- CLAIM-tmprq9q5
title: 'Perspectives given as graded participation functions on a common measure overlap by the integral of their pointwise minimum, which is zero exactly when the measures they carve out are mutually singular and, for probability densities, equals one minus their total-variation distance, so separation of perspectives comes by degrees and need not be a partition'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from A26 §§3–4 and A29 §5 of the
    exchange "Explain First Contact RL" (ChatGPT, shared 2026-11-22), with
    the assistant's proof and the total-variation identity, checked with
    python3 -I.
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): rests_on CLAIM-1186 dropped, unused by
    the body, which takes the measure as given; the proof (the integral of
    the minimum is one minus the total variation) is checked; no premise,
    nothing objects.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: measurable p_i, p_j: X → [0, 1] with
  ∫ min(p_i, p_j) dμ = 0 and the measures p_i μ, p_j μ not mutually
  singular, or the converse; or probability densities whose affinity
  ∫ min differs from 1 − TV. That a real self's perspectives are not well
  modelled as participation functions on one measure does not defeat it;
  that is a question of modelling, which the claim leaves open.
tags:
- mathematics
- individuation
- self
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
summary: >-
  A26 and A29 of the exchange "Explain First Contact RL" (2026-11-22). A
  perspective is modelled as a participation function p_i: X → [0, 1]
  over a common measure μ, with submeasure μ_i = p_i μ, and the p_i need
  not sum to 1, which "would force a partition of the organization among
  perspectives" (A26). Two probability measures are mutually singular
  when a measurable set carries all of one and none of the other: "a
  perfect measurable distinction separates them". A29: overlap
  O_μ(p_i, p_j) = ∫ min(p_i, p_j) dμ is zero exactly when μ_i ⊥ μ_j. The
  assistant (Claude, in this session) supplied the proof and added that,
  for probability densities, the overlap is 1 − TV, so it is a standard
  affinity. The wording is A's (ChatGPT, in the exchange of 2026-11-22),
  except the proof and the identity, which are the assistant's; adopting
  them is the owner's call.
---

# CLAIM-1167: Perspectives given as graded participation functions on a common measure overlap by the integral of their pointwise minimum, which is zero exactly when the measures they carve out are mutually singular and, for probability densities, equals one minus their total-variation distance, so separation of perspectives comes by degrees and need not be a partition

## The claim

Let μ be a measure on X and let perspectives be measurable participation
functions p_i: X → [0, 1], with submeasures dμ_i = p_i dμ. No partition
of unity is assumed: several perspectives may participate in one region,
each to its own degree (A26 §3). Define the overlap

O_μ(p_i, p_j) = ∫_X min(p_i, p_j) dμ.

Then O_μ(p_i, p_j) = 0 exactly when μ_i ⊥ μ_j (A29 §5). Between the
extremes "lies a continuum of partially overlapping organizations", so
"we get a graded account of perspectival separation instead of a binary
decision about whether two selves are distinct" (A29).

A26 §4 drew the consequence: "Perspectival plurality need not consist of
mutually singular measures", and the underlying measure may be nonatomic,
so that "a continuum of possible perspectival distinctions need not
amount to a countable population of already individuated selves".

## Proof (the assistant's)

Mutual singularity for finite measures: there is a measurable A with
μ_i(Aᶜ) = 0 and μ_j(A) = 0. If ∫ min = 0, then min(p_i, p_j) = 0 μ-a.e.;
take A = {p_i > 0}. Then μ_i(Aᶜ) = ∫_{Aᶜ} p_i dμ = 0, and p_j = 0 a.e. on
A, so μ_j(A) = 0. Conversely, given such an A, p_i = 0 a.e. on Aᶜ and
p_j = 0 a.e. on A, so the minimum vanishes a.e. and its integral is 0.
For probability densities, min(f, h) = (f + h − |f − h|)/2, so
∫ min = 1 − ½∫|f − h| = 1 − TV(f, h): the overlap is the usual affinity,
1 at coincidence and 0 at mutual singularity.

## Check

python3 -I on random 10-point densities: ∫ min = 0.510597 and
1 − TV = 0.510597.

## What it does not say

That overlap under one μ is an intrinsic fact about two perspectives: it
depends on the choice of X, μ and the p_i, and A29 says "there need not
be any canonical list of the p_i".
