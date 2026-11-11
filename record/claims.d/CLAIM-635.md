---
number: 635
status: Proposed
formerly:
- CLAIM-tmp008ey
title: 'Under Markov reconstruction kernels, an observable conserved exactly at every step and not constant on the support of the starting law keeps information about the start at every generation, bounded below independently of the generation, so such a chain cannot converge to a law independent of its start, while a bounded conservation defect does not prevent forgetting'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the martingale step (K_i f = f for every
  step gives E[f(S_n) | S_0] = f(S_0)), in the identity
  E|g(S_0)| = E_joint[h] − E_product[h] for h(x, y) = sgn(g(x)) g(y) with
  g = f − E f(S_0), in the total-variation step, or in Pinsker's
  inequality as used; or a two-state chain with a bounded defect that
  cannot forget its start, against the witness given.
tags:
- probabilistic-modeling
- information-theory
- mathematics
date: '2026-11-11'
line:
- pragmatic-transport
- formal-apparatus
rests_on:
- CLAIM-107
- CLAIM-270
bears_on:
- QUESTION-006
summary: >-
  [CLAIM-107](CLAIM-107.md) makes an exactly conserved observable a martingale, and
  [CLAIM-081](CLAIM-081.md) and [CLAIM-270](CLAIM-270.md) separate retention of information about the start
  from drift. Put together: if K_i f = f at every step and f is not
  constant on where the chain starts, then I(S_0; S_n) ≥ (E|g(S_0)|)² /
  (2‖g‖∞²) nats for every n, with g = f − E f(S_0). Exact conservation of a
  non-constant pragmatic observable is a retained piece of the ancestor,
  so it excludes convergence to a start-independent convention, whatever
  makes the observable harmonic (several closed classes, a restricted
  state space or time-dependent kernels). An approximately conserved one
  does not: a two-state chain with defect p forgets its start. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-068 ADR-075 — Proposed; cited for the convergence this claim excludes, open -->

# CLAIM-635: Under Markov reconstruction kernels, an observable conserved exactly at every step and not constant on the support of the starting law keeps information about the start at every generation, bounded below independently of the generation, so such a chain cannot converge to a law independent of its start, while a bounded conservation defect does not prevent forgetting

## The claim

Let S_0, S_1, … be a chain on a finite state space with Markov kernels K_1,
K_2, …, possibly different at each step, and let f be an observable with
K_i f = f for every i ([CLAIM-107](CLAIM-107.md)'s exact criterion). Let m = E f(S_0) and
g = f − m, and suppose g(S_0) is not almost surely zero. Then for every n,

I(S_0; S_n) ≥ (E|g(S_0)|)² / (2‖g‖∞²) nats.

So retention, [CLAIM-270](CLAIM-270.md)'s I(U_0; U_n) and [CLAIM-081](CLAIM-081.md)'s directed retention
profile, stays bounded away from zero, and the chain cannot converge to a
law that does not depend on where it started. An approximately conserved
observable, ‖K_i f − f‖∞ ≤ ε, carries no such guarantee.

## Admission

By the derivation route ([ADR-075](../decisions.d/ADR-075.md), step 5).

1. Since K_i 1 = 1, g is harmonic for every K_i too. By [CLAIM-107](CLAIM-107.md)'s
   martingale step, E[g(S_n) | S_0] = g(S_0) for every n.
2. Let h(x, y) = sgn(g(x)) g(y), so |h| ≤ ‖g‖∞. Under the joint law of
   (S_0, S_n), E[h] = E[sgn(g(S_0)) g(S_0)] = E|g(S_0)| by step 1. Under the
   product of the marginals, E[h] = E[sgn(g(S_0))] · E g(S_n) = 0, since
   E g(S_n) = E g(S_0) = 0.
3. For any bounded h, the difference of its means under two laws is at
   most 2‖h‖∞ times their total-variation distance, so
   E|g(S_0)| ≤ 2‖g‖∞ · TV(joint, product).
4. Pinsker's inequality gives TV(joint, product) ≤ √(I(S_0; S_n)/2) in
   nats. Squaring gives the bound.

The bound does not depend on n, and it needs no irreducibility or
time-homogeneity: it holds under each of the three escapes [CLAIM-107](CLAIM-107.md)'s note
of 2026-10-10 names. On a finite irreducible chain only constants are
harmonic ([CLAIM-107](CLAIM-107.md)), and the claim is empty there.

**A bounded defect does not prevent forgetting.** On {0, 1} let each kernel
flip the state with probability p ∈ (0, 1), and f(x) = x. Then
‖K f − f‖∞ = p, the mean drifts by at most np ([CLAIM-107](CLAIM-107.md)), and I(S_0; S_n)
→ 0, so the chain forgets its start.

**A check.** With S_0 uniform on {0, 1}, identity kernels and f(x) = x, the
bound gives 1/2 nat against a true ln 2. Over 3,000 random reducible,
time-dependent five-state chains with a harmonic f, the bound held in every
case (the reviewer's script, minimum slack 0.09 nats).

It is not held: [CLAIM-107](CLAIM-107.md) has the martingale and says when non-constant
harmonic observables exist; [CLAIM-270](CLAIM-270.md) and [CLAIM-081](CLAIM-081.md) separate retention from
drift; no entry joins conservation to retention.

## What it adds to the line

It joins the line's two inquiries. A pragmatic observable that actual
kernels conserve exactly ([QUESTION-006](../questions.d/QUESTION-006.md), "exactly") is information the chain
keeps about the ancestor, so [CLAIM-081](CLAIM-081.md)'s "convergence is not preservation"
has a converse for such observables, and [CLAIM-068](CLAIM-068.md)'s attraction toward a
convention reached "whatever its start" ([TERM-027](../terms.d/TERM-027.md)) and exact conservation of
a non-constant observable cannot both hold of one chain. Only the bounded
defect of [QUESTION-006](../questions.d/QUESTION-006.md) is compatible with attraction to one convention.

## What it does not say

- That real serial reconstruction is Markov. A chain whose retellers see
  earlier generations is [CLAIM-056](CLAIM-056.md)'s defeater, and outside this claim.
- That any pragmatic observable is conserved exactly by actual kernels.
- That retention keeps the whole distribution of the observable: only its
  conditional mean is kept ([CLAIM-094](CLAIM-094.md)).
