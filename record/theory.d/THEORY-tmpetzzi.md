---
status: Proposed
promote_when: >-
  A check of the two facts Theorem 3 of LIT-225 rests on, in Li &
  Vitányi's textbook or an independent source: m(D | H) ≥
  2^{−K(Pr(·|H))} Pr(D | H) (eq. 25), and log(m(x)/P(x)) as the universal
  sum test (Theorem 11). The record has read the proof built on them, not
  the facts. It is refuted by a hypothesis class with recursive likelihoods
  and prior, and data D random for an H that is itself random for the
  prior, where −log Pr(D|H) − log P(H) falls below K(D|H) + K(H) by more
  than K(Pr(·|H)) + K(P) plus a constant. What cannot settle it is any
  experiment comparing practical MDL with Bayesian model selection. Neither
  uses Kolmogorov complexity, so agreement or disagreement there says
  nothing about this bound.
title: "Ideal MDL and Bayesian MAP selection under the universal prior agree only to within the complexity of the hypothesis's likelihood, and only among hypotheses for which the data are individually random"
version: 1
tags:
- learning-theory
- model-comparison
- information-theory
date: '2026-10-14'
source:
- LIT-225
summary: >-
  Vitányi & Li (1999/2000), [LIT-225](../literature.d/LIT-225.md), read in [NOTE-tmpp6trb](../notes.d/NOTE-tmpp6trb.md). Theorem 3:
  if D is Martin-Löf random for Pr(·|H) and H for the prior P, then
  −log Pr(D|H) − log P(H) lies within α = K(Pr(·|H)) + K(P) below
  K(D|H) + K(H). Theorem 4: among such hypotheses, the posteriors of the
  ideal-MDL and MAP choices differ by at most 2^{−α}. α can be as large as
  K(H). Outside that set the two can diverge, even on the true
  hypothesis. "Compression equals Bayes" holds only for typical data and
  simple hypotheses.
---
<!-- inactive-ok-file: THEORY-tmppce05 THEORY-087 CLAIM-188 — Proposed; the companion theory filed today and the entries named under Connections -->

# THEORY-tmpetzzi: Ideal MDL and Bayesian MAP selection under the universal prior agree only to within the complexity of the hypothesis's likelihood, and only among hypotheses for which the data are individually random

## Source

Vitányi & Li (arXiv 1999; IEEE Trans. Inf. Theory 46(2), 2000),
[LIT-225](../literature.d/LIT-225.md), read in [NOTE-tmpp6trb](../notes.d/NOTE-tmpp6trb.md). The pointers are §2.1 (Def. 3,
Theorem 1), §2.2 (Theorem 2), §2.3 (Example 2), §2.4 (Example 3,
Theorem 3, Remarks 1–3), §2.5 (Def. 6, Theorems 4–5, Corollary 1) and
Appendix C (Theorem 11).

## What was actually shown

**Ideal MDL.** Select argmin_H {K(H) + K(D | H)}. This is Bayes's rule
with −log P(H) and −log Pr(D | H) replaced by the shortest effective code
lengths K(H) and K(D | H). The question is when that substitution is
licensed.

**The Fundamental Inequality (Theorem 3).** Let Pr(·|·) and the prior P be
recursive. If D is Martin-Löf random for Pr(·|H) and H is random for P,
then

K(D|H) + K(H) − α(P, H) ≤ −log Pr(D|H) − log P(H) ≤ K(D|H) + K(H),
with α(P, H) = K(Pr(·|H)) + K(P).

Conversely, agreement to within a constant implies both randomness
conditions. The upper bound is the definition of randomness through the
universal sum test log(m(x)/P(x)) ≤ 0. The lower bound is domination,
m(D|H) ≥ 2^{−K(Pr(·|H))} Pr(D|H).

**Selection (Theorem 4).** Restrict both rules to "admissible" hypotheses,
those that satisfy both randomness conditions. The ideal-MDL choice then
has posterior at least 2^{−α} times the MAP choice's, and its two-part
length is at most α above. With the universal prior P = m, every H is
random for P. The inequality then holds iff D is random for the
ideal-MDL hypothesis (Theorem 5).

**Where they part (Example 3, Remark 3).** Take the data 0ⁿ. It is not
random for the fair coin B_{1/2}, since −log Pr = n while K(0ⁿ | B_{1/2})
≤ log n + 2 log log n. If B_{1/2} is in fact the source, Bayes with a
suitable prior can select it while MDL selects B₀. With two hypotheses
(p = ½, p ≠ ½), ideal MDL ties where Bayes picks p ≠ ½.

**The finite-set case (Theorem 1).** For hypotheses that are finite sets
with uniform likelihood, universal-prior MAP, ideal MDL and Kolmogorov's
minimal sufficient statistic select the same set, to the O(1) in its
definition.

What could have come out otherwise: the gap α might have depended on the
data, or have had no bound at all. It is bounded by the complexity of the
two distributions involved, whatever the data.

## What this does not say

- **Not that MDL and Bayes are equivalent.** The agreement is to within α,
  and α contains K(Pr(·|H)) ≤ K(H) + O(1), which for a complex hypothesis
  is of the order of the whole model cost. The converse in Theorem 3(ii)
  gives exact agreement only when the two sides match to O(1). The LIT's
  earlier summary ("coincides … exactly when") overstated this, and has
  been corrected.
- **Not that the condition can be checked.** Martin-Löf randomness is not
  decidable, so which hypotheses are admissible cannot be determined from
  the data.
- **Not "with high probability".** Corollary 1 says ideal MDL is Bayes
  with the universal prior "with high probability", but it specifies no
  probability space and gives no proof. Remark 1's weak randomness holds
  with probability above 1 − 1/n under each P, at a log cost in α. That is
  the only quantified statement.
- **Not that MDL avoids overfitting where Bayes does not.** §1 calls this
  "some evidence". No result in the paper shows it.
- **Not anything about practical MDL or the evidence of parametric
  models.** K is uncomputable, and §2.6 puts practical codes out of scope.
  [THEORY-087](THEORY-087.md)'s Occam factors and [LIT-238](../literature.d/LIT-238.md)'s NML are different objects.
- **Not about K(H) + K(D|H) being the right two-part form.** Vereshchagin
  & Vitányi ([LIT-239](../literature.d/LIT-239.md), §V-B(iii)) show this "ultimate compression" form can
  pick badly fitting models, and use log |S| for the data part instead
  ([THEORY-tmppce05](THEORY-tmppce05.md)).

## Connections

- **[THEORY-tmppce05](THEORY-tmppce05.md).** The complexity-constrained guarantee for the
  worst-case two-part code. It holds for every string, with no
  randomness condition. The randomness deficiency that this theory
  requires to be small is the quantity that one controls.
- **[THEORY-087](THEORY-087.md) and [CLAIM-154](../claims.d/CLAIM-154.md).** Both read the evidence's Occam factor as a
  complexity penalty. Here the prior's code length −log P(H) equals K(H)
  only for hypotheses random under P. A hypothesis the modeller's prior
  singles out, with −log P(H) ≫ K(H), is where an evidence ranking and a
  description-length ranking diverge. [CLAIM-188](../claims.d/CLAIM-188.md) narrows [CLAIM-154](../claims.d/CLAIM-154.md) on
  singular models. This is a separate limit on reading its Bayes-factor
  rule as a description-length rule.
- **[LIT-238](../literature.d/LIT-238.md), §6.3.** Bayes and MDL can both be inconsistent when the truth
  is outside every model. This theory's framework, in which "there are
  only data and no true hypothesis", does not treat that case.
