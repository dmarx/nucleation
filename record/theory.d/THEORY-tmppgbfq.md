---
status: Active
title: "A pseudorandom generator exists if and only if a one-way function exists, where both are secure against uniform adversaries and every reduction is an oracle Turing machine, as statements about ensembles indexed by n; the construction from an arbitrary one-way function is only weak-preserving, so security at one length is bought at a much greater one"
version: 1
tags:
- mathematics
- information-theory
date: '2026-10-15'
source:
- LIT-1051
- LIT-1061
summary: >-
  Håstad, Impagliazzo, Levin and Luby (1999), [LIT-1051](../literature.d/LIT-1051.md), read in [NOTE-880](../notes.d/NOTE-880.md), with
  Goldreich's Foundations of Cryptography, [LIT-1061](../literature.d/LIT-1061.md), skimmed in [NOTE-863](../notes.d/NOTE-863.md) from
  the 1995 draft. Theorem 6.2.2: "There are one-way functions iff there are
  pseudorandom generators." The hard direction runs one-way function → false
  entropy generator → pseudoentropy generator → generator, by uniform
  reductions, with seeds of length n^10 in the direct construction. Adversaries
  are algorithms; the paper has no circuit version, and that the proof carries
  over to non-uniform adversaries is the reading's inference, not the paper's
  statement. Everything is asymptotic. Goldreich states the theorem and does not
  prove it.
supports:
- CLAIM-302
- CLAIM-304
---

# THEORY-tmppgbfq: A pseudorandom generator exists if and only if a one-way function exists, where both are secure against uniform adversaries and every reduction is an oracle Turing machine, as statements about ensembles indexed by n; the construction from an arbitrary one-way function is only weak-preserving, so security at one length is bought at a much greater one

## Source

Håstad, Impagliazzo, Levin and Luby (1999), [LIT-1051](../literature.d/LIT-1051.md), SIAM Journal on Computing
28(4), read in full in [NOTE-880](../notes.d/NOTE-880.md) from the authors' 46-page typescript
(Definitions 2.1.1, 3.1.1–3.6.1; Sections 4–7; Theorem 6.2.2). Goldreich,
Foundations of Cryptography vol. 1, [LIT-1061](../literature.d/LIT-1061.md), read in [NOTE-863](../notes.d/NOTE-863.md) (Skimmed) from
the 1995 draft, Chapters 1–3, for the standard definitions and the easy
direction.

## What was actually shown

**Definitions.** A one-way function is a P-time function ensemble f for which
no adversary of the given time-success ratio finds any preimage of f(X), X
uniform. A pseudorandom generator is a P-time g with output longer than input
such that g(U_t) and U_ℓ are computationally indistinguishable (Definition
3.3.3); one bit of stretch extends to any polynomial stretch (Proposition 3.3.4;
Goldreich, Theorem 3.11). Security is a time-success ratio T_n/sp_n(A) over
adversaries, which the paper presents as a refinement of the convention that a
breaking adversary runs in polynomial time with inverse-polynomial success.

**The theorem.** "There are one-way functions iff there are pseudorandom
generators." A generator gives a one-way function by an elementary argument
(attributed to Levin 1987 in [LIT-1051](../literature.d/LIT-1051.md); Proposition 3.13 in Goldreich, for
stretch 2n). The converse is the paper's contribution. A one-way function with
the Goldreich–Levin bit and hashing tuned to its degeneracy gives a false
entropy generator: output whose computational entropy exceeds its Shannon
entropy (Theorem 6.2.1). That gives a pseudoentropy generator, whose
computational entropy exceeds its input's (Lemma 4.7.2), and hashing many
copies of that gives a generator (Theorem 4.6.4). Intermediate steps need
advice of polynomially many values, removed by XORing the generators for every
candidate (Proposition 4.8.1).

**Uniformity.** Adversaries are uniform by default, and a reduction is a pair of
oracle Turing machines: one builds the new primitive from f, the other turns any
adversary against it into an inverter for f. The step from one copy to many
needs both distributions P-samplable: "It is crucial that D and E are
P-samplable because the sampling algorithms are used by M." This is why
computational entropy is defined against a P-samplable comparison distribution.

**Cost.** "the reduction for general one-way functions is only
weak-preserving": security for seeds of length n^O(1) implies only polynomially
related security for f at length n. Composed literally the reductions need
seed length n^34; the direct construction (Theorem 7.0.5) needs n^10.

## What this does not say

- **That it is a statement about circuits.** No circuit appears in the paper and
  it defines no non-uniform one-way function. Because each reduction is a fixed
  oracle machine the proofs would carry over to non-uniform adversaries, but the
  paper does not say so; that is [NOTE-880](../notes.d/NOTE-880.md)'s inference. The "non-uniform version
  of computational entropy" the paper mentions concerns the comparison
  distribution, not the adversary.
- **That any particular generator is secure.** Existence is conditional on a
  one-way function, which is itself unproved and implies P ≠ NP.
- **That a generator built this way is practical.** Weak preservation and seeds
  of n^10 mean a generator from an arbitrary one-way function is secure only at
  far greater length. Poly-preserving reductions are known only for regular or
  nearly regular functions.
- **That anything holds at a fixed n.** All definitions are asymptotic over
  ensembles; for a single length a finite test separates the output from uniform.
- **That Goldreich's book proves it.** The draft states it as Theorem 3.29, "It
  is known that one-way functions exist if and only if pseudorandom generators
  exist", without proof, and the printed 2001 text was not checked.
- **That computational entropy here is HILL entropy as usually cited.** The
  paper's is Shannon entropy against uniform adversaries; the circuit,
  min-entropy version that goes by that name is not defined in it.

## Connections

- [THEORY-tmpxr7yk](THEORY-tmpxr7yk.md): the samplable far-but-indistinguishable pair exists if a
  generator does; with this theorem, if a one-way function does. Section 8 of
  [LIT-1051](../literature.d/LIT-1051.md) attributes the converse, a samplable such pair gives a generator, to
  Goldreich's 1989 note, which the record holds as [LIT-1053](../literature.d/LIT-1053.md) (Unavailable).
- [CLAIM-302](../claims.d/CLAIM-302.md) and [CLAIM-304](../claims.d/CLAIM-304.md) condition on pseudorandom generators; by this theorem
  that condition may be read as the existence of one-way functions, in the
  uniform setting.
- [QUESTION-110](../questions.d/QUESTION-110.md): the time-success ratio is a worked cost of recovery that folds
  the success criterion into the cost, and the paper's linear-, poly- and
  weak-preserving reductions say how such a cost transfers between
  representations. [QUESTION-103](../questions.d/QUESTION-103.md): pseudoentropy is information content as
  efficient observers can tell it.
