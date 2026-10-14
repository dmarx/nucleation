---
number: 260
status: Active
formerly:
- THEORY-tmpevdge
title: "An individual string's information splits non-trivially into structure and noise only in a model class without a universal member: with partial recursive models every string's minimal sufficient statistic is trivial, while with total recursive functions it is not, and the finite-set, computable-distribution and total-function classes agree to within logarithmic terms"
version: 3
history:
- version: 2
  date: '2026-10-14'
  note: >-
    Promoted from Proposed to Active at the owner's direction. The
    promotion condition asked for a second source proving two things, and
    named LIT-239 as one that could. LIT-239 was read in full in NOTE-787,
    a reading separate from NOTE-790, which filed this account. Clause by
    clause: (1) The correspondence across finite sets, computable
    distributions and total recursive functions, with its error terms, is
    LIT-239's Appendix B. NOTE-787 read Propositions B.1–B.2 step by step,
    and they give equivalence to finite sets within O(log n) for computable
    mass functions (cost −log P(x)) and for total recursive functions (cost
    l_x(p), the same cost as LIT-229's). The restriction to
    K(P) ≤ n + O(log n) costs no more than O(log n) (Remark B.3). This is
    the precision the account claims. (2) The existence of strings whose
    sophistication is near their length is LIT-239 §V-E and §VI-D, as read
    in NOTE-787. For complexity n − √n ± O(log n), some strings have
    deficiency about √n relative to every set of complexity below
    n − O(log n), so they have no sufficient statistic below that
    complexity. Corollary IV.9, whose constructive proof NOTE-787 read,
    realises every admissible shape. These results are stated for finite
    sets. Carrying them to total recursive functions through Proposition
    B.2, at O(log n), is the record's own step. LIT-239 added as a source.
- version: 3
  date: '2026-10-14'
  note: >-
    The record's own step named in version 2, carrying LIT-239's
    non-stochastic strings to total recursive functions through
    Propositions B.1(b)–B.2(b) and Remark B.3, is filed with its argument as
    CLAIM-289 and cited in the body. That claim also corrects the
    threshold: Corollary IV.9 gives deficiency about √n only for models of
    complexity below n − √n − O(log n), not below n − O(log n) as LIT-239
    §VI-D words it and version 2 repeated. The clause is still met. The
    claim is unchanged.
tags:
- information-theory
- mathematics
date: '2026-10-14'
source:
- LIT-229
- LIT-239
summary: >-
  Vitányi (2001/2006), [LIT-229](../literature.d/LIT-229.md), read in [NOTE-790](../notes.d/NOTE-790.md). Sophistication,
  the shortest model that completes an optimal two-part code, is =⁺ 0 for
  every string if partial recursive models are allowed (Lemma 6.2). With
  total recursive models it ranges from about 0 for random strings to
  above n − log n − 2 log log n for some string of every length (Theorem
  6.5), and it agrees with the finite-set and probabilistic versions to
  within O(log n) (Lemmas 7.1–7.2). It is not computable, and a
  sufficient-statistic oracle would compute K (Theorems 8.1, 8.3). It
  says nothing about any computable or learned model.
---
<!-- inactive-ok-file: THEORY-036 THEORY-157 — Proposed; the real-patterns account this bears on, and the probabilistic sufficiency account it is set beside -->

# THEORY-260: An individual string's information splits non-trivially into structure and noise only in a model class without a universal member: with partial recursive models every string's minimal sufficient statistic is trivial, while with total recursive functions it is not, and the finite-set, computable-distribution and total-function classes agree to within logarithmic terms

## Source

Vitányi, "Meaningful Information" (arXiv 2001; IEEE Trans. Inf. Theory
2006), [LIT-229](../literature.d/LIT-229.md), read in full in [NOTE-790](../notes.d/NOTE-790.md): Definitions 5.4 and 6.1,
Lemmas 6.2, 6.4, 7.1 and 7.2, Theorems 6.5, 8.1, 8.3 and 8.5, and §IX.

## What was actually shown

**The split.** K(x) =⁺ min_T {K(T) + K(x | T)} (II.3). A total recursive
function f is a sufficient statistic for x if K(f) + l_x(f) =⁺ K(x),
where l_x(f) is the length of the shortest d with f(d) = x (Def. 5.4).
Sophistication is the least K(f) among sufficient f (Def. 6.1). It is
the paper's measure of the "meaningful" part of x.

**A universal model trivialises it.** If partial recursive functions are
allowed as models, the reference machine U is one, and U(u, ⟨T_f, d⟩) =
U(T_f, d) = x moves every model into the data part. So soph(x) =⁺ 0 for
all x (Lemma 6.2). "If a model class contains a universal model that can
simulate all other models, then this model class is not suitable for
defining two-part codes consisting of meaningful information and
accidental information."

**Totality restores it.** With total recursive models, soph(x) <⁺ K(x)
(Lemma 6.4). liminf soph(x) =⁺ 0, witnessed by maximally random strings
and the identity function (Theorem 6.5(ii)). For every n some x of
length n has soph(x) >⁺ n − log n − 2 log log n (Theorem 6.5(iv)): such
strings are almost all structure. [LIT-239](../literature.d/LIT-239.md) gives an independent route at
O(log n) precision, its non-stochastic strings carried to total
functions in [CLAIM-289](../claims.d/CLAIM-289.md). A model class could have failed at
either end, by trivialising every string or by leaving no string with a
short model. Both ends are proved to be reached.

**The classes agree.** A finite-set sufficient statistic gives a
probabilistic one, and that gives a total-function one, each with
complexity equal to within a constant (Lemma 7.1). A total-function
sufficient statistic gives a finite set with K(S) + log |S| = K(x) +
O(log n) (Lemma 7.2).

**It is uncomputable.** soph is not recursive (Theorem 8.1). An oracle
for sufficient statistics would compute K and the halting sequence
(Theorem 8.3). The paper cites Vereshchagin–Vitányi for the claim that it
cannot be approximated to any significant precision (Lemma 8.7(i)).

## What this does not say

- **Not that the split is objective in an absolute sense.** It is
  relative to the model class and, through §IV, to a distortion measure,
  which the paper says "is a selection of which aspects of the data are
  relevant". What is shown is that three natural classes agree, not that
  every admissible class must.
- **Not a full equivalence at constant precision.** The step from total
  functions back to finite sets costs O(log n), and the set obtained is
  sufficient only to that precision. For short strings the slack is the
  same size as the quantities compared.
- **Not anything about learned models or MDL in practice.** The models
  are shortest programs for total functions, and the quantity cannot be
  computed or usefully approximated. A claim that a trained network
  "captures the meaningful information" in its data cannot be read off
  this result.
- **Not a comparison with Koppel's sophistication or with logical
  depth.** The paper borrows Koppel's word, sets his treatment aside, and
  does not discuss depth.
- **Not the structure-function characterisation.** §IX states that soph
  is where the structure function reaches K(x), and defers it to
  Vereshchagin–Vitányi without proof here.

## Connections

- **[THEORY-036](THEORY-036.md) (Dennett's real patterns).** That account takes
  compressibility against the bit map as Dennett's criterion of a real
  pattern. Theorem 6.5(iv) gives strings that are nearly incompressible,
  with K(x) close to n, yet almost all structure in this sense. So
  "compressible" and "has meaningful structure" come apart for an
  individual object. The paper does not discuss Dennett.
- **[LIT-239](../literature.d/LIT-239.md)** (Vereshchagin–Vitányi) is the sequel the paper names. It
  treats the full structure function for finite sets and extends it to
  the other classes at O(log n).
- **[THEORY-157](THEORY-157.md)** holds the classical, probabilistic theorems on sufficient
  statistics in Markov categories. This account is their
  individual-object, algorithmic counterpart. It needs no distribution,
  and minimality is by program length, not by factorisation.
