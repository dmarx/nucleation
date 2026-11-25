---
number: 2263
status: Proposed
formerly:
- THEORY-tmpgf28l
promote_when: >-
  An independent reading that confirms the parametrization-dependence of
  the Radner–Stiglitz nonconcavity the title asserts — for instance De Lara
  & Gossner (2020), "Payoffs-beliefs duality and the value of
  information", or Chade & Schlee (2002), "Another look at the
  Radner–Stiglitz nonconcavity" — or a reproduction of the efficient-value
  concavity (Prop. 2.3, Cor. 2.4) from the binding-constraint and
  replication argument, with the measure stated. The paper's own proof,
  already followed here, does not by itself promote the account.
title: 'The Radner-Stiglitz nonconcavity of the value of information is an artifact of how the amount of information is measured: under a convex-divergence measure, the value of the efficiently acquired amount is concave with strictly positive marginal value at zero, while the value of the worst acquisition of each amount is almost never concave, and a max-min decision-maker''s value of information is concave too'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed Proposed from NOTE-2354. The three clauses are Whitmeyer's
    Propositions 2.3/2.6/3.3 with Corollary 2.4; the proofs of Lemma 2.2
    and Prop. 2.3 were followed step by step. Proposed because promotion
    wants an independent confirmation of the parametrization-dependence,
    not the paper's own proof alone.
tags:
- information-theory
- mathematics
- epistemology
date: '2026-11-22'
source:
- LIT-3131
bears_on:
- QUESTION-374
---

# THEORY-2263: The Radner-Stiglitz nonconcavity of the value of information is an artifact of how the amount of information is measured: under a convex-divergence measure, the value of the efficiently acquired amount is concave with strictly positive marginal value at zero, while the value of the worst acquisition of each amount is almost never concave, and a max-min decision-maker's value of information is concave too

## Source

Whitmeyer (2024), [LIT-3131](../literature.d/LIT-3131.md), read in
[NOTE-2354](../notes.d/NOTE-2354.md).

## The account

The Radner–Stiglitz (1984) nonconcavity of the value of information — the
marginal value of a small amount of information can be zero, so a
decision-maker will not buy small quantities — is genuine but reflects the
measure of the "amount" of information, not the value of information
itself. Quantify the amount by D(F) = ϕ(∫ c(x,µ) dF) with c a strictly
convex divergence and ϕ weakly convex and increasing. Then:

1. **Efficient acquisition gives concavity.** Reading off the value of the
   *best* experiment delivering each amount (the Efficient Value of
   Information), the amount-of-information constraint binds, and the value
   is concave in the amount, strictly so when ϕ is strictly convex. In any
   non-trivial decision problem its marginal value at zero is strictly
   positive.

2. **Inefficient acquisition is almost never concave.** Reading off the
   value of the *worst* experiment delivering each amount, the value is
   almost never concave: at a dense set of priors its marginal value near
   zero is zero, because near an interior prior the cheap experiments stay
   within one belief region where the decision value is affine. This is
   the Radner–Stiglitz phenomenon.

3. **A max-min decision-maker's value is concave.** Under Gilboa–Schmeidler
   max-min expected utility the value of information is again concave,
   because the adversary's reduced freedom over priors reinforces the
   replication argument.

## Scope

An account attributed to Whitmeyer, Proposed. The positive claim (part 1)
is the load-bearing one; it holds for the convex-divergence family of
measures under efficient acquisition and does not assert that every natural
observation cost yields concavity. State set and action set are finite.

## Bearing

It bears on [QUESTION-374](../questions.d/QUESTION-374.md) (the structure of the observe/act trade): the
observing side's value is concave under efficient acquisition and
generically nonconcave when the experiments are fixed or chosen badly. It
contextualizes [CLAIM-572](../claims.d/CLAIM-572.md)'s fourth result (marginal reasoning fails under a
committed probe order) as that nonconcavity specialized to a fixed
acquisition schedule, as the dated note on the claim records.
