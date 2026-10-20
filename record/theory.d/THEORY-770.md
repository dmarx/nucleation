---
number: 770
status: Active
formerly:
- THEORY-tmp9jqpz
title: 'In a closed population, any mapping of ancestors to descendants gives the Price equation: mean fitness times the change in mean character equals the covariance of fitness and character plus the fitness-weighted mean of the change in character, over any time interval and with no assumption beyond closure'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Split from THEORY-673 by the promotion audit (batch 058, ADR-040 and
    ADR-047 v2), on the pattern of THEORY-736's split from THEORY-109 and
    THEORY-741's from THEORY-110. THEORY-673 bundled the Price equation's
    derivation with Luque's generalization-sketch reading of it. Batch 056
    re-derived the derivation; this THEORY holds it, and THEORY-673 keeps
    the reading and extends this one.
tags:
- philosophy-of-biology
- mathematics
date: '2026-10-20'
source:
- LIT-205
summary: >-
  Luque (2016), [LIT-205](../literature.d/LIT-205.md), §3, read in [NOTE-101](../notes.d/NOTE-101.md), after Price (1970); the
  derivation re-derived by the promotion audit. An identity, not a model:
  it says nothing about which partition of the change a causal model
  licenses, predicts nothing until fitness and transmission are specified,
  and fails without closure (migration).
extended_by:
- THEORY-673
---

# THEORY-770: In a closed population, any mapping of ancestors to descendants gives the Price equation: mean fitness times the change in mean character equals the covariance of fitness and character plus the fitness-weighted mean of the change in character, over any time interval and with no assumption beyond closure

## Source

Luque (2016), [LIT-205](../literature.d/LIT-205.md) (*Biology & Philosophy* 32(1):97–125), §3, p. 7,
read in full in [NOTE-101](../notes.d/NOTE-101.md) from the author's PhilSci-Archive manuscript.
The equation is Price's (1970); Luque states and derives it. The
derivation was worked through by the promotion audit (batches 056 and
058).

## What was actually shown

**Setting.** Ancestors i at time t, with frequency q_i, character z_i and
fitness w_i, the number of descendants each leaves at t + 1. Each ancestor's
descendants have mean character z'_i, and Δz_i = z'_i − z_i. The population
is closed: every entity at t + 1 descends from, or is, an entity at t, so
there is no migration. Write w̄ = Σ q_i w_i and z̄ = Σ q_i z_i.

**Derivation.** Descendant frequencies are q'_i = q_i w_i / w̄, so the
descendants' mean character is z̄' = Σ q_i w_i z'_i / w̄. Then

w̄ Δz̄ = Σ q_i w_i (z_i + Δz_i) − w̄ Σ q_i z_i
     = [Σ q_i w_i z_i − w̄ z̄] + Σ q_i w_i Δz_i
     = Cov(w, z) + E(w Δz),

with covariance and expectation taken over ancestors weighted by q_i.
With relative fitness ω = w / w̄ this is Δz̄ = Cov(ω, z) + E(ω Δz). Only
closure and the ancestor–descendant mapping are used, and the interval
from t to t + 1 is arbitrary.

**Equivalent partitions.** Luque's Table 1 lists others, among them
Okasha's Cov(ω, z') + E(Δz), obtained by writing z'_i = z_i + Δz_i inside
the covariance instead of the expectation. They are rearrangements of the
same identity.

**What could have come out otherwise.** The identity could have needed an
assumption beyond closure, such as additivity, discrete generations or a
fixed population size. It does not.

## What this does not say

- It does not say which partition of Δz̄ a given causal model licenses.
  Different equivalent forms assign the same change differently to
  "selection" and "transmission"; that question is [THEORY-673](THEORY-673.md)'s.
- It predicts nothing on its own. Fitnesses and the transmission term must
  come from a model, so it is not dynamically sufficient.
- It fails without closure. With migration a further term is needed.
- It does not carry Luque's generalization-sketch reading, the f = ma
  analogy or the replies to the tautology charge. Those stay in [THEORY-673](THEORY-673.md),
  which is Proposed.
