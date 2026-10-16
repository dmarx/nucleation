---
number: 289
status: Active
formerly:
- CLAIM-tmp75182
title: 'Non-stochastic strings stay non-stochastic under total recursive models: their minimal randomness deficiency agrees with the finite-set one to within O(log n) in argument and value'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A string x of length n and a total recursive function p with x in its
  range, K(p) ≤ α and δ(x | p) ≤ β_x(α + c log n) − c log n for every
  constant c. Equivalently, a failure of LIT-239's Proposition B.2(b) or
  Remark B.3 as stated. A gap of constant size, or of order log n, does not
  defeat it, since the claim is made only to O(log n).
tags:
- information-theory
- mathematics
date: '2026-10-14'
line:
- formal-apparatus
grounds:
- LIT-239
summary: >-
  The step that [THEORY-260](../theory.d/THEORY-260.md)'s promotion (version 2) names as the record's
  own: carrying [LIT-239](../literature.d/LIT-239.md)'s non-stochastic strings, proved for finite-set
  models, to total recursive function models through Propositions B.1(b)
  and B.2(b) with Remark B.3. Remark B.3 asserts wholesale that every
  result of the paper extends to total functions up to a logarithmic term.
  This writes the extension out for this one result. It holds at O(log n)
  precision only, and does not reach [LIT-229](../literature.d/LIT-229.md)'s sophistication, which is
  defined at constant precision.
---

# CLAIM-289: Non-stochastic strings stay non-stochastic under total recursive models: their minimal randomness deficiency agrees with the finite-set one to within O(log n) in argument and value

## The claim

Notation, from [LIT-239](../literature.d/LIT-239.md) Appendix B:
- For a total recursive p, l_x(p) = min{|d| : p(d) = x}.
- Its randomness deficiency is δ(x | p) = l_x(p) − K(x | p).
- β_x(α) = min{δ(x | S) : S ∋ x, K(S) ≤ α}, over finite sets.
- β^tot_x(α) = min{δ(x | p) : x ∈ range p, K(p) ≤ α}, over total recursive
  functions. This one is the record's notation.

For x of length n and every α:

  β^tot_x(α + O(1)) ≤ β_x(α) + O(1)  and  β_x(α + O(log n)) ≤ β^tot_x(α) + O(log n).

Hence the strings of Corollary IV.9 keep their shape under total recursive
models. Take k = α₀ = n − √n. There are strings x of length n and
complexity n − √n ± O(log n) such that:
- every total recursive model of complexity at most n − √n − O(log n)
  leaves deficiency at least √n − O(log n);
- some total recursive model of complexity n − √n + O(log n) has deficiency
  O(log n).

Their simplest model with logarithmic deficiency has complexity near n.

## The argument

1. **From sets to functions.** Proposition B.1(b) turns any finite
   S ∋ x into a total p with K(p) = K(S) + O(1), l_x(p) ≤ log |S| and
   δ(x | p) ≤ δ(x | S) + O(1). This gives the first inequality.
2. **From functions to sets.** Proposition B.2(b) turns a total p into a
   set S ∋ x with K(S) ≤ K(p) + K(l_x(p)) + c and
   δ(x | S) ≤ δ(x | p) + 2 log K(p) + K(l_x(p)) + 2 log K(l_x(p)) + c.
   - These terms are O(log n) once K(p) ≤ n + O(log n) and
     l_x(p) ≤ n + O(1).
   - Remark B.3 makes that restriction free. For every p there is p′ with
     K(p′) ≤ min{K(p), n} + O(log n), δ(x | p′) ≤ δ(x | p) + O(log n) and
     l_x(p′) ≤ min{l_x(p), n} + 1.
   - Composing the two gives the second inequality.
3. **Non-stochastic strings.** Corollary IV.9 with k = α₀ = n − √n, as the
   paper applies it in §VI-D, gives the following for the finite-set
   functions:
   - β_x(i) > √n − C log n for i ≤ n − √n − C log n;
   - β_x(i) < C log n for i ≥ n − √n + C log n.

   Substituting through steps 1 and 2 moves each threshold, and each
   bound, by O(log n). That gives the claim.

The record checked steps 1 and 2 against the text of Appendix B ([NOTE-787](../notes.d/NOTE-787.md)).
The record's own contribution is the substitution in step 3.

## A correction it carries

[LIT-239](../literature.d/LIT-239.md) §VI-D says the deficiency is about √n "with respect to … every
other finite set of complexity less than n − O(log n)". Corollary IV.9
gives this only below n − √n − O(log n). It cannot hold above K(x), since
the singleton {x} has complexity K(x) + O(1) ≈ n − √n and deficiency
O(1). [NOTE-787](../notes.d/NOTE-787.md) repeats the paper's phrase. The statement above uses the
corollary's bound.

## Where it is used

- **[THEORY-260](../theory.d/THEORY-260.md)**, promoted at version 2, whose second clause asks for
  strings whose sophistication is near their length. [LIT-229](../literature.d/LIT-229.md) proves this
  directly for total functions at constant precision (Theorem 6.5(iv)).
  This claim is the independent route through [LIT-239](../literature.d/LIT-239.md). It meets the
  clause at logarithmic precision, which is the precision [THEORY-260](../theory.d/THEORY-260.md)
  claims for the agreement of the classes.

## What it does not say

- Nothing at constant precision. [LIT-229](../literature.d/LIT-229.md)'s sophistication counts f as
  sufficient when K(f) + l_x(f) =⁺ K(x). Converting a deficiency of
  O(log n) into that condition costs further logarithmic terms, and this
  claim does not argue it.
- Nothing about how many strings are non-stochastic. Corollary IV.9 gives
  existence, not frequency.
