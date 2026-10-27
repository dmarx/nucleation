---
number: 357
status: Active
formerly:
- THEORY-tmpxr7yk
title: "Computational indistinguishability is strictly coarser than statistical closeness: without any assumption there are ensembles on at most 2^(n/2) strings that no circuit of size 2^(n/8) tells from uniform, though none of them is efficiently samplable, and an efficiently samplable pair of this kind exists if a pseudorandom generator does, since its output covers at most 2^n of the 2^l(n) strings; all of it is about ensembles indexed by n, not single pairs of distributions"
version: 1
tags:
- mathematics
- information-theory
date: '2026-10-15'
source:
- LIT-1061
- LIT-1051
summary: >-
  Goldreich, Foundations of Cryptography vol. 1, [LIT-1061](../literature.d/LIT-1061.md), read in [NOTE-863](../notes.d/NOTE-863.md)
  (Skimmed, 1995 draft, Chapters 1–3 in full), with Håstad, Impagliazzo, Levin
  and Luby (1999), [LIT-1051](../literature.d/LIT-1051.md), read in [NOTE-880](../notes.d/NOTE-880.md). Proposition 3.3 proves by counting
  that some ensemble far from uniform fools every small circuit; its proof is
  non-constructive and the ensemble cannot be sampled efficiently. A generator's
  output is efficiently samplable, indistinguishable from uniform by definition,
  and statistically far by an image count (§3.3.1). That a samplable such pair
  exists only if one-way functions do is cited to Goldreich 1990, not read. The
  book's statistical difference has no factor ½, so it is twice total variation.
supports:
- CLAIM-302
bears_on:
- QUESTION-103
---

# THEORY-357: Computational indistinguishability is strictly coarser than statistical closeness: without any assumption there are ensembles on at most 2^(n/2) strings that no circuit of size 2^(n/8) tells from uniform, though none of them is efficiently samplable, and an efficiently samplable pair of this kind exists if a pseudorandom generator does, since its output covers at most 2^n of the 2^l(n) strings; all of it is about ensembles indexed by n, not single pairs of distributions

## Source

Goldreich, Foundations of Cryptography vol. 1, [LIT-1061](../literature.d/LIT-1061.md), read in [NOTE-863](../notes.d/NOTE-863.md)
(Skimmed) from the 1995 draft (Definitions 3.2, 3.7, 3.9; Proposition 3.3;
§3.3.1; Proposition 3.13; §3.8.2). Section numbers are the draft's; the printed
2001 text was not checked. Håstad, Impagliazzo, Levin and Luby (1999), [LIT-1051](../literature.d/LIT-1051.md),
read in [NOTE-880](../notes.d/NOTE-880.md), for the same definitions in their framework and for Section 8.

## What was actually shown

**The equivalences.** Ensembles {X_n} and {Y_n} are indistinguishable in
polynomial time if every probabilistic polynomial-time test's gap
|Pr[D(X_n) = 1] − Pr[D(Y_n) = 1]| is eventually below every inverse polynomial
(Definition 3.2). They are statistically close if Σ_α |Pr[X_n = α] − Pr[Y_n = α]|
is negligible. The book's stance: "Objects are considered to be computationally
equivalent if they cannot be told apart by any efficient procedure."
Statistically close ensembles are computationally indistinguishable; the
converse fails.

**Unconditional separation (Proposition 3.3).** A Chernoff bound and a union
bound over all circuits of size 2^(n/8) show that 2^(n/2) uniformly chosen
strings fool every such circuit with gap below 2^(−n/8). The resulting ensemble
is far from uniform, yet indistinguishable from it. The proof is
non-constructive, and "One of the two ensembles is not constructible in
polynomial-time." Of the statistic that separates them: "yet f is (necessarily)
impossible to compute in polynomial-time."

**Samplable separation from a generator (§3.3.1).** The output of a generator G
with l(n) > n "must be polynomial-time indistinguishable from uniform, although
it cannot be uniform (or even statistically close to uniform)": strings outside
G's image, all but at most 2^n of 2^l(n), carry the difference. The book states
the bound as at least ½ in its unhalved measure; with l(n) = 2n the same count
gives total variation at least 1 − 2^(−n), and the same 2^(−n) count appears in
the proof of Proposition 3.13. [LIT-1051](../literature.d/LIT-1051.md)
describes indistinguishability as "the computationally restricted adversary
definition of statistical distance", and its statistical distance carries the ½.

## What this does not say

- **That the separation needs an assumption.** It does not. Only an efficiently
  samplable witness needs one.
- **That a samplable witness needs a generator.** The converse is cited, not
  read: "Goldreich showed that a pair of polynomial-time constructible ensembles
  having the above property (i.e., being both computationally indistinguishable
  and having a non-negligibly statistical difference) exists if and only if
  one-way functions exist"
  (G90, cited in §3.8.2). [LIT-1051](../literature.d/LIT-1051.md)'s Section 8 attributes to Goldreich's 1989
  note the equivalence with generators, without bounding "very different";
  combined with [THEORY-352](THEORY-352.md) that gives the one-way-function form, but no held
  reading writes it out.
- **That two given distributions are indistinguishable.** For any fixed n, a
  finite test (membership in G's image) separates G(U_n) from U_2n almost
  perfectly. The notions apply to sequences indexed by n.
- **That indistinguishability survives repeated samples in general.** For
  efficiently constructible ensembles it does (Theorem 3.6, hybrid argument);
  Proposition 3.3's ensemble is not constructible, and the multi-sample
  statement for it is given only for circuits, as an exercise.
- **That efficient post-processing is proved to preserve it in the text.** That
  is set as Exercise 1 of §3.8.4.
- **That the two books' numbers agree as written.** Goldreich's Δ is twice the
  total variation that [LIT-1051](../literature.d/LIT-1051.md) and the record use.

## Connections

- [CLAIM-302](../claims.d/CLAIM-302.md) is the record's statement of this account; it currently grounds
  [LIT-1061](../literature.d/LIT-1061.md) directly, and this THEORY is what it rests on. [CASE-083](../cases.d/CASE-083.md) uses the
  generator witness.
- [QUESTION-103](../questions.d/QUESTION-103.md): a test's gap is hit rate minus false-alarm rate, so this is a
  case where the best ROC in a restricted class sits near chance while the ideal
  one ([THEORY-031](THEORY-031.md), the likelihood-ratio detector) is near perfect. The link to
  signal detection is the record's, not either source's.
- [THEORY-352](THEORY-352.md) supplies the one-way-function form of the generator condition.
