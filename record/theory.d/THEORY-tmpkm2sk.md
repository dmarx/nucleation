---
status: Active
title: 'The growth rate of thermodynamic depth is the entropy rate of whichever macrostate process it is computed over, so the choice of macrostates sets it anywhere from zero up; among partitions of a stationary process''s past that predict every finite stretch of the future as well as the whole past does, the causal states are the coarsest, so they have the least entropy and the least entropy rate'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmpjq49q. The dive identity is the paper's
    (12)–(22), and the optimality its Section VII A–C. Each is re-derived
    below step by step, which meets the condition for Active under ADR-047
    v2. Prescience is taken at every finite future length, not under the
    paper's footnote 2, which makes it vacuous. The entropy-rate step
    replaces the paper's one-step argument, which covers only a Markov
    rival. Both repairs are the record's.
tags:
- complex-systems
- information-theory
date: '2026-10-20'
source:
- LIT-tmpvvjya
summary: >-
  Crutchfield and Shalizi (1999; arXiv 1998), [LIT-tmpvvjya](../literature.d/LIT-tmpvvjya.md), read in
  [NOTE-tmpjq49q](../notes.d/NOTE-tmpjq49q.md). Depth is not a structure measure until its states are fixed.
  Predictive sufficiency, then minimality, fixes them as the causal states.
  The choice is canonical only given the measuring instrument and the
  target, the observed future. The redefined dive is still an entropy rate.
---
<!-- inactive-ok-file: THEORY-157 — Proposed; named as the general sufficiency result this is an instance of, nothing here rests on it -->
# THEORY-tmpkm2sk: The growth rate of thermodynamic depth is the entropy rate of whichever macrostate process it is computed over, so the choice of macrostates sets it anywhere from zero up; among partitions of a stationary process's past that predict every finite stretch of the future as well as the whole past does, the causal states are the coarsest, so they have the least entropy and the least entropy rate

## Source

Crutchfield and Shalizi (1999; arXiv 1998), [LIT-tmpvvjya](../literature.d/LIT-tmpvvjya.md), read in full in
[NOTE-tmpjq49q](../notes.d/NOTE-tmpjq49q.md): Eqs. (9)–(22), Section V, Section VII A–C. The repairs to
Section VII's prescience condition and to its dive proof are the record's.

## What was actually shown

**Setting.** (S_t) is a stationary process on a finite alphabet. A
macrostate assignment is any stationary process of states. A **rival** is a
countable partition R of pasts, with η(past) its cell, applied at each time
by the same rule. The **causal partition** ε groups pasts with the same
conditional law of the future.

**1. The dive is an entropy rate.** Lloyd and Pagels' averaged depth is
D_L = H[S_{−L+1..−1} | S_0] = H[S_{−L+1..0}] − H[S_0]. So
D_L − D_{L−1} = H[S_{−L+1..0}] − H[S_{−L+2..0}]
= H[S_{−L+1} | S_{−L+2..0}]. This is non-increasing in L and tends to the
reverse-time entropy rate. By stationarity that equals the forward rate
h_μ, since both are lim H[S_{1..L}]/L. Re-derived here.

**2. The choice of macrostates sets it from zero up.** Lump everything into
one state, and the depth is 0. Replace each macrostate by a pair (state,
label), with a fresh label at every step drawn independently with any
distribution of entropy k. Then the entropy rate becomes h_μ + k. Since k
ranges over [0, ∞), the dive can take any value at least the lumped one.
The paper gives the equiprobable case, log n.

**3. Prescient rivals refine ε.** Let R̂ satisfy H[S→^L | R̂] = H[S→^L | S]
for every L, where S = ε(past). Every such entropy is finite.

- Both R̂ and S are functions of the past, and the future is independent of
  the past given S. So H[S→^L | R̂, S] = H[S→^L | S] = H[S→^L | R̂].
- Hence I(S→^L; S | R̂) = 0. For any cell r̂ of positive probability, every
  causal state s that meets r̂ has the same law of S→^L, namely the one given
  r̂.
- This holds for every L, and finite-dimensional laws fix the law of the
  whole future. So r̂ meets only one causal state, up to probability zero.
  Thus S = g(R̂) almost surely.

**4. The least entropy.** C_μ = H[S] = H[g(R̂)] ≤ H[R̂], with equality iff
g is injective almost surely, that is, iff R̂ is ε.

**5. The least entropy rate.** The causal-state sequence is
(S_t) = (g(R̂_t)). So H[S_1..S_n] ≤ H[R̂_1..R̂_n] for every n. Dividing by
n and letting n → ∞ gives h^S ≤ h^{R̂}.

What could have failed: a coarser or incomparable partition could have
matched the predictions at every finite length, which step 3 excludes. A
refinement could also have had a lower entropy rate through
non-Markovian structure, which step 5 excludes. The paper's own proof of
step 5 compares H[R̂′|R̂] with H[S′|S]. That covers only a rival whose
state process is Markov.

## What this does not say

- **Not that causal-state depth is objective outright.** ε is canonical
  given the alphabet the instrument produces and the target (the whole
  observed future). The paper's logistic map yields one state through a
  generating partition and countably many (C_μ ≈ 2.71 bits) through a
  non-generating one.
- **Not that the redefined dive measures structure.** For an ε-machine,
  h^S = h_μ − H[next symbol | S, S′]. It is zero for IID processes, and it
  equals h_μ whenever the transitions record the symbol (the logistic-map
  example: 0.677867 bits both ways).
- **Not anything about partially predictive states.** Every result here is
  about rivals that keep all predictive information. It says nothing about
  the trade-off below that, which is [THEORY-tmp35hmc](THEORY-tmp35hmc.md)'s territory.
- **Not under the paper's footnote 2.** Normalized by L, "prescience"
  holds for every finite-entropy partition, the one-state partition
  included, and step 3 fails.
- **Not the paper's strict inequality v < C_μ** whenever the excess
  entropy is positive. [NOTE-tmpjq49q](../notes.d/NOTE-tmpjq49q.md) gives a two-state counterexample.

## Connections

- **[CLAIM-152](../claims.d/CLAIM-152.md).** An instance with two parameters fixed before the partition
  exists: the target, the observed future, and the instrument that defines
  the observed alphabet.
- **[THEORY-157](THEORY-157.md).** Step 3 is the predictive form of "a minimal sufficient
  statistic is a function of every sufficient statistic", for countable
  partitions.
- **[THEORY-tmp35hmc](THEORY-tmp35hmc.md).** The memoryless, finite-β counterpart. There every
  information-bottleneck optimum is a coarsening of ε. Here every fully
  predictive partition is a refinement of ε. So ε is the boundary between
  the two regimes in the refinement order.
- **[QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md).** Among fully predictive states, the refinement
  order is monotone in both entropy and entropy rate.
