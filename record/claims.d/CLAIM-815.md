---
number: 815
status: Proposed
formerly:
- CLAIM-tmpdusls
title: 'The exponent 3/2 shared by critical branching cascades and first passage of a random walk comes from one identity, the hitting-time theorem: the chance of total size s, or of first passage at time t, is 1/s or 1/t times a local probability that falls as the inverse square root at balance, so 3/2 = 1 + 1/2'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Newman's review (LIT-2976) was
    read: the line calling it unread now says what it has, and LIT-2976
    leaves grounds, since it gives the walk's 3/2 and not the identity
    (ARG-tmp275n1); THEORY-tmp6jdas corroborates the walk's exponent.
    The thesis and status are unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A failure of the identity P(S = s) = (1/s)·P(X_1 + … + X_s = s − 1) for
  the total progeny of a Galton–Watson tree with i.i.d. offspring X, or of
  P(T = t) = (1/t)·P(S_t = −1) for a left-continuous walk; or a critical
  branching process with finite offspring variance whose total-progeny
  exponent is not 3/2; or the objection that this is only the
  exploration-walk remark A already made.
tags:
- probabilistic-modeling
- mathematics
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- CASE-303
summary: >-
  Fills the gap left by A5 §3 of the exchange "Rich Get Richer Power
  Laws" (2026-11-20). A notes that critical branching and random-walk
  first passage share the exponent 3/2 and says this "is not entirely
  coincidental: the exploration of a branching tree can be represented
  using a random-walk-like process", without the step. The step is the
  hitting-time theorem (Otter, Dwass, Kemperman). Exploring the tree one
  node at a time, the queue is a walk with steps X − 1, and the cascade
  ends when it first reaches −1, so the total size is a first-passage
  time. The cycle lemma gives the factor 1/s, and the local central limit
  theorem gives s^(−1/2) at zero drift. Off balance, the same local
  probability decays exponentially, which gives the cutoff of
  [CASE-303](../cases.d/CASE-303.md). Checked with python3 -I. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
bears_on:
- QUESTION-505
---
<!-- inactive-ok-file: CASE-303 CLAIM-795 — Proposed or new; the case and catalogue claim filed with this one from the same exchange -->
<!-- inactive-ok-file: THEORY-tmp6jdas ARG-tmp275n1 — Proposed; Newman's reading and the argument that it does not carry this claim -->

# CLAIM-815: The exponent 3/2 shared by critical branching cascades and first passage of a random walk comes from one identity, the hitting-time theorem: the chance of total size s, or of first passage at time t, is 1/s or 1/t times a local probability that falls as the inverse square root at balance, so 3/2 = 1 + 1/2

## The gap (A5 §3)

"Notice that this is the same 3/2 exponent encountered in critical
branching processes. That is not entirely coincidental: the exploration
of a branching tree can be represented using a random-walk-like process."
A gives the picture and not the step. It is item 1 and item 3 of
[CLAIM-795](CLAIM-795.md).

## The step

**Exploration.** Explore a cascade one event at a time. Keep a queue of
events not yet explored, starting with one. Exploring an event removes it
and adds its X offspring, so the queue changes by X − 1. The cascade ends
when the queue first empties, that is, when the walk W_n = Σ_{i≤n}(X_i − 1)
first reaches −1. So the total size S is the first-passage time to −1 of a
walk whose steps are X − 1 ≥ −1 (a left-continuous walk).

**The hitting-time theorem.** For such a walk, P(T = n) = (1/n)·P(W_n =
−1). The factor 1/n is the cycle lemma: of the n cyclic shifts of a path
ending at −1, exactly one first reaches −1 at its last step. For the
cascade this is Dwass's formula, P(S = s) = (1/s)·P(X_1 + … + X_s = s − 1).
The simple ±1 walk is the case X ∈ {0, 2}.

**The exponents.** At balance, E[X] = 1, the walk has zero drift, and the
local central limit theorem gives P(W_n = −1) ≈ 1/sqrt(2πσ²n). So

    P(S = s) ≈ (1/s) · (2πσ²s)^(−1/2) ∝ s^(−3/2).

The 3/2 is 1 from the cycle lemma plus 1/2 from diffusion. Off balance,
E[X] = R < 1, P(W_n = −1) decays exponentially in n by large deviations.
For Poisson offspring it is P(Poisson(Rs) = s − 1) ≈ e^(−s(R−1−ln R))/
sqrt(2πs), which gives the cutoff s_c = 1/(R − 1 − ln R) of
[CASE-303](../cases.d/CASE-303.md). So the same identity yields A7's "power law times a
cutoff", and both the power and the cutoff.

## Checked (with python3 -I)

- Poisson offspring: (1/s)·P(Poisson(s) = s − 1) equals the Borel law
  exactly for s = 1 to 5. 200,000 simulated critical cascades match it:
  P(S = 10) is 0.01249 simulated and 0.01251 exact. s^(3/2)·P(S = s) is
  0.3956 at s = 10 and 0.3983 at s = 50, tending to (2π)^(−1/2) = 0.3989.
- Simple walk: (1/t)·P(S_t = −1)·t^(3/2) is 0.7920 at t = 101 and 0.7978
  at t = 10,001, tending to sqrt(2/π) = 0.7979. That limit is twice the
  cascade's because the ±1 walk can return only at odd times. 200,000
  simulated walks give P(T = 11) = 0.0210 against 0.0205.

## What it does not say

- Not that every 3/2 has this origin. The mean-field avalanche exponent
  of other models is 3/2 for the same branching reason, but a
  low-dimensional avalanche has other exponents, and so does a walk in
  higher dimensions or with heavy-tailed steps.
- Not that this was read in a source. The theorem is standard (Otter
  1949, Dwass 1969, Kemperman), none of it registered here. Newman's
  review ([LIT-2976](../literature.d/LIT-2976.md)), A's reference, was read on 2026-11-22: it has the
  walk's 3/2 by generating functions and not the link to branching
  ([ARG-tmp275n1](../arguments.d/ARG-tmp275n1.md)).
- On the objection: A gave the exploration picture. What is added is the
  identity that turns it into the exponent, and the cutoff that falls out
  of the same formula.

## Change of 2026-11-22

The line "Newman's review ... is unread" now says what the review has;
[LIT-2976](../literature.d/LIT-2976.md) leaves `grounds` ([ARG-tmp275n1](../arguments.d/ARG-tmp275n1.md)). Version 2.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md); the reading is
[THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md)) **leaves the claim open; a parallel**. §IV.C
(pp. 15–16) derives the first return of a symmetric ±1 walk to the origin
by generating functions, f_2n ∝ n^(−3/2): "So the distribution of return
times follows a power law with exponent α = 3/2." It never mentions a
branching process, the cycle lemma or Dwass's formula. So it gives one
half of the coincidence by another route and nothing on the identity,
which rests on this claim's own derivation and [CASE-303](../cases.d/CASE-303.md).
[THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md) `corroborates` the walk's exponent; it is not a ground.
Status unchanged.
