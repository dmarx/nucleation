---
number: 83
status: Active
formerly:
- CASE-tmp51hxx
title: 'A pseudorandom generator''s output against uniform strings: almost disjoint
  in total variation, indistinguishable to every efficient test if the generator
  is secure'
version: 1
standing: stipulated
kind: construction
tags:
- mathematics
- information-theory
date: '2026-10-15'
line: formal-apparatus
summary: >-
  A15 §2's witness, which A15 recommended filing "with its cryptographic assumption
  explicitly stated". It grounds [CLAIM-302](../claims.d/CLAIM-302.md)
  and, by the record's own reduction, [CLAIM-304](../claims.d/CLAIM-304.md).
  Checked against Goldreich (note of 2026-10-15): the definitions match, and the
  separation needs the generator only for samplability.
supports:
- CLAIM-302
- CLAIM-304
---

# CASE-083: A pseudorandom generator's output against uniform strings: almost disjoint in total variation, indistinguishable to every efficient test if the generator is secure

## The case

G: {0,1}ⁿ → {0,1}²ⁿ. P = G(Uₙ), Q = U₂ₙ. G's image has at most 2ⁿ
elements out of 2²ⁿ, so the test "y is in the image of G" separates them
with TV(P, Q) ≥ 1 − 2⁻ⁿ. If G is a secure pseudorandom generator, every
probabilistic polynomial-time distinguisher D has |Pr[D(G(Uₙ)) = 1] −
Pr[D(U₂ₙ) = 1]| ≤ negl(n).

## What it can show

That statistical difference does not imply efficient distinguishability,
and so that agreement under feasible tests does not imply identity of
the distributions. A15: "This is conditional on the existence of a
secure generator, not an unconditional theorem that a specific practical
generator is secure." The conditional attaches to this samplable witness;
the separation itself holds unconditionally ([CLAIM-302](../claims.d/CLAIM-302.md)).

## What the source says (note of 2026-10-15)

Read against Goldreich's 1995 draft of *Foundations of Cryptography*
([LIT-1061](../literature.d/LIT-1061.md)): the indistinguishability and generator definitions are its
Definitions 3.2 and 3.9 (with l(n) = 2n). Three qualifications.

- **The objects are ensembles**, indexed by n. "Negligible" has no meaning
  for one pair.
- **The book's bound is weaker and its convention different.** §3.3.1
  states only that a generator's output is at least ½ away from uniform,
  in a "statistical difference" without the factor ½ of total variation.
  The 1 − 2⁻ⁿ above follows from the same counting with stretch 2n.
- **Postprocessing** preserving indistinguishability is set as an
  exercise (§3.8.4, Exercise 1), not proved in the text.

The book also has the stronger fact this case does not need: Proposition
3.3 gives, with no assumption, an ensemble far from uniform that no
polynomial-size test separates. That ensemble cannot be sampled
efficiently. What the generator adds is a witness that can.

## What it cannot show

Anything about language or minds. A15: the construction is "a
mathematical construction ... not an empirical demonstration about
language." And the gap depends on the representation: given an
expensively computed label, the same pair is trivially separable.
