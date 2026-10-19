---
number: 107
status: Active
formerly:
- CLAIM-tmpuwwjx
title: 'Under Markov reconstruction kernels, an observable''s expectation is invariant when the observable is harmonic (K f = f), and drifts by at most Σ ε_i when ‖K_i f − f‖∞ ≤ ε_i; on a finite irreducible chain only constants are harmonic'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/CLAIM-107.yaml, batch 003, ADR-047).
    The title said the observable "is conserved", which gave "a Noether-type
    conservation criterion". Only the mean is conserved. In a walk on
    {0, …, N} absorbed at the ends, f(x) = x is harmonic while the
    distribution of f(S_n) spreads to the endpoints. And mean conservation
    does not make an observable a symmetry. CLAIM-094, Active and granted,
    holds both points against this claim, and they are now in its
    statement. The title and the defeat condition are narrowed to mean
    conservation, the martingale step and the drift bound. THEORY-158 is
    cited for the continuous-time Noether theorem and no longer grounds the
    claim. The derivation and the note of 2026-10-10 are unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the martingale step (K_i f = f for every step gives
  E[f(S_(i+1)) | S_i] = f(S_i)), in the drift bound
  (|E f(S_(i+1)) − E f(S_i)| ≤ ε_(i+1) when ‖K_(i+1) f − f‖∞ ≤ ε_(i+1)), or
  in the maximum-principle argument that only constants are harmonic on a
  finite irreducible chain.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-09'
line:
- pragmatic-transport
- formal-apparatus
works:
- what-survives-translation
uses:
- TERM-027
summary: >-
  The manuscript's §4, citing Baez and Fong. [CLAIM-094](CLAIM-094.md) says what
  the cited theorem needs that the discrete-time criterion leaves out.
objected_by:
- CLAIM-094
complements:
- CLAIM-093
---
<!-- inactive-ok-file: THEORY-158 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-059 — Proposed; cited as the open regimes claim that several closed classes would presuppose -->

# CLAIM-107: Under Markov reconstruction kernels, an observable's expectation is invariant when the observable is harmonic (K f = f), and drifts by at most Σ ε_i when ‖K_i f − f‖∞ ≤ ε_i; on a finite irreducible chain only constants are harmonic

## The claim

§4 cites Baez and Fong ([LIT-773](../literature.d/LIT-773.md)) correctly: for finite continuous-time Markov
processes, a diagonal observable commutes with the generator exactly when its
expectation and second moment are conserved for every initial distribution
([THEORY-158](../theory.d/THEORY-158.md)). It then states its own discrete-time criterion, Kf = f, under
which f(S_n) is a martingale and E f(S_n) is invariant, and bounds the drift
of the mean by Σε_i when ‖K_i f − f‖ ≤ ε_i.

## What it does not say

The manuscript says plainly that Noether's hypotheses do not hold
automatically in communicative systems, and that its bounds are
expectation-preservation estimates only.

- **That the observable's distribution is conserved.** Only its mean is.
  In a walk on {0, …, N} absorbed at the ends, f(x) = x is harmonic while
  the distribution of f(S_n) spreads to the endpoints ([CLAIM-094](CLAIM-094.md)).
- **That the criterion is a Noether theorem.** Mean conservation does not
  make an observable a symmetry. The Noether-type equivalence, for finite
  continuous-time processes, needs the second moment as well and is Baez
  and Fong's ([THEORY-158](../theory.d/THEORY-158.md), Proposed), cited here and not leaned on.

## Where it came from

The owner's U37 objection: "symmetry is a kind of invariance, no? isn't that part
of the point of Noether Theory?" ([CLAIM-040](CLAIM-040.md)). A105 conceded and found Baez
and Fong's Noether theorem for Markov processes: "a genuine
conservation-theoretic connection for the continuous-time Markov special case".
It also gave the discrete harmonic condition Kf = f, its approximate form
(‖Kf − f‖∞ ≤ ε gives drift at most nε, or Σε_i), and a candidate conserved
quantity: "Whether the speaker and audience occupy positions of solidarity or
normative asymmetry". A105's stronger condition, K(h∘f) = h∘f for all bounded h,
which conserves the whole distribution, became the manuscript's "stronger
conditions" without the formula. The limit on borrowing Noether is
[CLAIM-093](CLAIM-093.md).

## Note of 2026-10-10: harmonic observables on irreducible chains

A203 §26 restates the criterion and adds a limit: "For finite irreducible
Markov chains, harmonic functions are constant." That is right, by the maximum
principle. A harmonic f attains its maximum somewhere, and Kf = f makes it
attain the maximum at every state reachable from there, which on an
irreducible chain is every state. So a non-trivial exactly conserved
observable needs reducible dynamics with several closed classes, a restricted
state space, or time-dependent kernels. A203 names the same three. Several
closed classes are themselves a hypothesis about conventions: separate
attractors from which reconstruction does not escape ([TERM-027](../terms.d/TERM-027.md),
[CLAIM-059](CLAIM-059.md)). The approximate form survives without them: ‖Kf − f‖∞ ≤ ε bounds
the drift of the mean by nε, as the manuscript already says.

## Note of 2026-10-19: narrowed to what is shown

The two steps the title now states are one line each. If K_i f = f for every
step, E[f(S_(i+1)) | S_i] = (K_(i+1) f)(S_i) = f(S_i), so f(S_n) is a
martingale and E f(S_n) = E f(S_0). If ‖K_(i+1) f − f‖∞ ≤ ε_(i+1), then
E f(S_(i+1)) − E f(S_i) = E[(K_(i+1) f − f)(S_i)], whose absolute value is at
most ε_(i+1), so the mean drifts by at most Σ ε_i. The note of 2026-10-10
proves the irreducible case. What the old title added, conservation of the
observable and a Noether-type criterion, is [CLAIM-094](CLAIM-094.md)'s objection, granted
and Active, and it now stands in "What it does not say".
