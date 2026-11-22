---
status: Proposed
title: "Kevei's restatement of Kesten's theorem, read as a source at second hand in place of the unfetched paper, grounds the claim that multiplicative growth with an additive floor gives a stationary Pareto tail with κ solving E[A^κ] = 1, under stricter conditions than the claim stated and with log-contraction required"
version: 1
form: source
grounds:
- THEORY-tmpsmrhx
- THEORY-tmpocjqv
concludes:
- CLAIM-824
tags:
- probabilistic-modeling
- mathematics
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  CLAIM-824 grounded its Kesten half on Kesten (LIT-3005), unread and now
  Unfetched. Kevei's note (THEORY-tmpsmrhx) states the theorem with its
  hypotheses and attributes it to Kesten; Alsmeyer and Mentemeier
  (THEORY-tmpocjqv) give the matrix form and attribute its statement to
  Kesten. Read as sources, they carry the claim's Kesten half at second
  hand, with E|B|^κ, non-degeneracy and a two-sided tail the claim had
  not stated, and with E log A < 0 forced rather than permitted. So
  THEORY-tmpsmrhx replaces LIT-3005 in the claim's grounds. The wording
  is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-824 THEORY-tmpsmrhx THEORY-tmpocjqv — Proposed; the claim and the two readings this argument joins -->
<!-- inactive-ok-file: LIT-3005 — Unfetched; Kesten, located and not read -->
<!-- inactive-ok-file: LIT-tmpn76uh — Deferred; Goldie (1991), registered and unread -->

# ARG-tmpn6ufb: Kevei's restatement of Kesten's theorem, read as a source at second hand in place of the unfetched paper, grounds the claim that multiplicative growth with an additive floor gives a stationary Pareto tail with κ solving E[A^κ] = 1, under stricter conditions than the claim stated and with log-contraction required

## The inference

CLAIM-824's second half: W' = AW + B gives a stationary tail
P(W > x) ∝ x^(−κ) with E[A^κ] = 1. THEORY-tmpsmrhx (Kevei) states that
theorem and attributes it to Kesten; THEORY-tmpocjqv (Alsmeyer and
Mentemeier) states its matrix form and attributes the statement to
Kesten. If they say it, in context and within scope, the claim's Kesten
half is grounded at second hand.

## Critical questions (source)

**Does the work say this, read in context?** Yes. "The first results on
existence and tail behavior of the solution are due to Kesten [25], who
proved that if EAκ = 1, EAκ log+ A < ∞, log A conditioned on A ≠ 0 is
nonarithmetic, and E|B|κ < ∞ for some κ > 0 ... then the solution of (1)
has Pareto-like tail" (Kevei, p. 1). It is the statement the note sets out
to extend, so it is stated with care, not in passing.

**Is it said within the scope the claim needs?** With three differences,
all now in the claim's `defeated_if`. The moment condition is E|B|^κ, not
E[B^κ]. Non-degeneracy, P{Ax + B = x} < 1, is assumed. The tail is
two-sided, "c+ + c− > 0", so the right tail may vanish when B is signed.
And the claim's "even when the process contracts on average" understated:
"The assumption EAκ = 1 together with A ≢ 1 imply that E log A < 0"
(p. 6). The claim's title is corrected accordingly.

**Is the source in a position to know?** Kevei is a specialist note in a
refereed probability journal on exactly this theorem; Alsmeyer and
Mentemeier re-prove the matrix form. Both name Kesten as the source of
the statement. Neither quotes Kesten's own hypotheses, and Alsmeyer and
Mentemeier say his matrix statement carried "one extra condition". So the
attribution of the scalar statement to Kesten is the usual one, and the
scalar proof the record relies on is Goldie's (LIT-tmpn76uh), as Kevei
says: "Later Goldie [18] simplified the proof of the same result in the
one-dimensional case".

**Does another source say otherwise?** None in the record. Grey's result,
reported by Kevei (p. 2), is not a contrary source but a limit on what the
tail shows: a regularly varying tail can come from B alone when
E[A^κ] < 1, which is now in the claim's "What it does not say".

## Verdict

THEORY-tmpsmrhx grounds CLAIM-824's Kesten half at second hand, and
replaces LIT-3005 in its `grounds`; THEORY-tmpocjqv stands behind the
attribution to Kesten in d dimensions. The claim's status is unchanged.
A reading of Kesten (1973) itself would check what he proved against what
the neighbours report.
