---
number: 635
status: Active
formerly:
- CLAIM-tmp008ey
title: 'Under Markov reconstruction kernels, an observable conserved exactly at every step and not constant on the support of the starting law keeps information about the start at every generation, bounded below independently of the generation, so such a chain cannot converge to a law independent of its start, while a bounded conservation defect does not prevent forgetting'
version: 3
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Proposed → Active at the status review's ruling (the owner delegated
    these rulings; ADR-057, ADR-047's rule on re-derivations). Both
    premises, CLAIM-107 and CLAIM-270, are Active; no objection is filed.
    The derivation was re-derived step by step by a second checker (the
    note of 2026-11-20), and scratch/formal/claim635_conservation_retention_check.py
    checks each step, the bound and the witness on 3,000 random reducible,
    time-dependent chains over 40 steps, with three controls that fire.
    The status is credence in the derivation, not in ADR-075, which is
    Proposed and supplies only the admission route. The claim is
    unchanged.
- version: 3
  date: '2026-11-21'
  note: >-
    A dated note: applied to the restatement of the record's entries by
    CLAIM-772 (ARG-124), and its neutral case given a rate by
    CLAIM-779. No change of status or title. Merged
    beside the status review's version 2 on 2026-11-21.
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
<!-- inactive-ok-file: CLAIM-772 CLAIM-779 ARG-124 — Proposed; filed in the contribution of 2026-11-20 on an entry's life cycle -->
<!-- inactive-ok-file: CLAIM-068 — Proposed; cited for the convergence this claim excludes, open -->

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

## Note of 2026-11-20: the derivation re-checked

A second checker went through each step at the status review of
2026-11-20.

1. **The martingale step.** For a time-dependent chain,
   E[f(S_n) | S_0 = x] = (K_1 K_2 ⋯ K_n f)(x). Applying K_n f = f first,
   then K_(n−1) f = f, and so on, gives f(x). Since each K_i is
   stochastic, K_i 1 = 1, so g = f − m is harmonic for every K_i too and
   E[g(S_n) | S_0] = g(S_0).
2. **The identity.** Under the joint law, E[sgn(g(S_0)) g(S_n)] =
   E[sgn(g(S_0)) E[g(S_n) | S_0]] = E[sgn(g(S_0)) g(S_0)] = E|g(S_0)|.
   Under the product of the marginals the two factors are independent,
   and E g(S_n) = E g(S_0) = 0 by step 1, so E[h] = 0.
3. **The total-variation step.** With TV(P, Q) = ½ Σ |P − Q|,
   |Σ h (P − Q)| ≤ ‖h‖∞ Σ |P − Q| = 2‖h‖∞ TV(P, Q), and ‖h‖∞ ≤ ‖g‖∞.
4. **Pinsker.** I(S_0; S_n) is the Kullback–Leibler divergence of the
   joint law from the product of its marginals, and TV ≤ √(KL/2) in nats.
   So E|g(S_0)| ≤ 2‖g‖∞ √(I/2), and squaring,
   I ≥ (E|g(S_0)|)² / (2‖g‖∞²). The bound is positive exactly when g(S_0)
   is not almost surely zero, that is, when f is not constant on the
   support of the starting law.
5. **No start-independent limit.** If the law of S_n given S_0 = x
   converged to one law for every x in the support, the joint law would
   converge to the product of its marginals, and on a finite space
   I(S_0; S_n) would go to zero, against step 4.
6. **The witness.** For the flip chain, K f − f = p(1 − 2x), so the
   defect is p, and P(S_n ≠ S_0) = (1 − (1 − 2p)^n)/2 → ½ for p in
   (0, 1), so S_n becomes independent of S_0 and I(S_0; S_n) → 0. Any
   defect bound ε > 0 admits such a chain, with p = min(ε, ½).

The worked example checks: g = ±½, so the bound is (¼)/(2 · ¼) = ½ nat
against ln 2. The script cited in "A check" was not on the record;
scratch/formal/claim635_conservation_retention_check.py now is. It checks
steps 1 to 4 and the bound on 3,000 random chains with two or three
closed classes, transient states and kernels redrawn at every step, over
40 steps (minimum slack 0.020 nats), and the witness for p from 0.01 to
0.9. Its controls fire: kernels mixed toward a common law break the
martingale and the bound, the bound without its factor 2 fails the
worked example, and information scaled by ln 2 falls below the bound on
some instance.

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

## Note of 2026-11-20: applied to the record's own entries

[CLAIM-772](CLAIM-772.md) uses this claim as the result that makes forgetting and
anchoring one contraction: a chain keeps exactly what its steps conserve, so
a record anchors content by having sessions copy it rather than reconstruct
it. [ARG-124](../arguments.d/ARG-124.md) is the application, and finds it holds for stored text and
only loosely for interpretation.

[CLAIM-779](CLAIM-779.md) adds a rate between this claim's two cases. The witness
here for "a bounded defect does not prevent forgetting", the two-state flip
chain, is contracting (eigenvalue 1 − 2p) and forgets geometrically. A
feature the step leaves neutral but copies with error, on an unbounded
state, forgets too, but only as 1/n in the linear Gaussian model. A bearing
of use, not evidence about this claim's derivation.
