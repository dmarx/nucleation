---
number: 259
status: Active
formerly:
- THEORY-tmpetzzi
title: "For a recursive family of likelihoods and the universal prior, the Bayesian two-part code length −log Pr(D|H) − log m(H) equals the ideal-MDL length K(D|H) + K(H) plus the randomness deficiency of D for H, up to a constant fixed by the family; so ideal MDL and MAP selection agree to within a constant among hypotheses for which the data are random, and can part where they are not"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-259 (batch 050, ADR-047 v2). The two facts the former
    promote_when named, the domination m(D|H) ≥ 2^{−K} Pr(D|H) (eq. 25) and
    log(m/P) as the universal sum test (Theorem 11), are derived in the
    dated note below, which meets it. The derivation reduces the Fundamental
    Inequality to an identity: the gap between the two code lengths is the
    data's randomness deficiency for the hypothesis. The title is restated
    as that identity. "Only to within the complexity of the hypothesis's
    likelihood" is dropped: the paper's α is an upper bound, and the
    conditional form of domination bounds the slack by the complexity of the
    likelihood family, a constant over H.
tags:
- learning-theory
- model-comparison
- information-theory
date: '2026-10-14'
source:
- LIT-225
summary: >-
  Vitányi & Li (1999/2000), [LIT-225](../literature.d/LIT-225.md), read in [NOTE-801](../notes.d/NOTE-801.md). With the universal
  prior m and a recursive family Pr(·|·), −log Pr(D|H) − log m(H) = K(D|H)
  + K(H) + d(D|H) + O(1), where d(D|H) = log(m(D|H)/Pr(D|H)) is the
  universal randomness deficiency of D for H; d ≥ −K(Pr(·|·)) − O(1), and
  d is bounded exactly when D is Martin-Löf random for H. So ideal MDL and
  MAP agree to within a constant on admissible hypotheses (Theorems 3–5,
  re-derived by the record) and part where the data are not random for the
  hypothesis (0ⁿ against the fair coin). The paper's slack α = K(Pr(·|H))
  + K(P) is an upper bound, not the gap.
---
<!-- inactive-ok-file: THEORY-277 THEORY-087 CLAIM-188 — Proposed; the companion theory filed today and the entries named under Connections -->

# THEORY-259: For a recursive family of likelihoods and the universal prior, the Bayesian two-part code length −log Pr(D|H) − log m(H) equals the ideal-MDL length K(D|H) + K(H) plus the randomness deficiency of D for H, up to a constant fixed by the family; so ideal MDL and MAP selection agree to within a constant among hypotheses for which the data are random, and can part where they are not

## Source

Vitányi & Li (arXiv 1999; IEEE Trans. Inf. Theory 46(2), 2000),
[LIT-225](../literature.d/LIT-225.md), read in [NOTE-801](../notes.d/NOTE-801.md). The pointers are §2.1 (Def. 3,
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

- **Not that MDL and Bayes are equivalent.** The agreement is to within
  the randomness deficiency, which is bounded only for admissible
  hypotheses (see the note of 2026-10-20). The paper states the slack as
  α, which contains K(Pr(·|H)) ≤ K(H) + O(1); that is an upper bound, and
  the conditional form of domination gives the family's complexity
  instead, a constant over H. The converse in Theorem 3(ii)
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
  ([THEORY-277](THEORY-277.md)).

## Connections

- **[THEORY-277](THEORY-277.md).** The complexity-constrained guarantee for the
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

## Note of 2026-10-20: eq. 25 and Theorem 11 derived, and the inequality as an identity

Promotion audit, batch 050. Taken as given: the existence of a universal
lower-semicomputable conditional semimeasure m(·|·), and Levin's coding
theorem K(D|H) = −log m(D|H) + O(1), uniformly in H.

1. **Domination (eq. 25).** Enumerate the lower-semicomputable conditional
   semimeasures μ₁, μ₂, …. Then ξ(D|H) = Σ_i 2^{−K(i)} μ_i(D|H) is one
   too, since Kraft bounds the weights. So m ≥ c·ξ ≥ c·2^{−K(μ)} μ for
   every μ. A recursive likelihood family Pr(·|·) is such a μ, so
   m(D|H) ≥ c·2^{−K(Pr(·|·))} Pr(D|H). Read as an unconditional
   semimeasure, the single distribution Pr(·|H) gives the paper's
   2^{−K(Pr(·|H))} form. Both hold.
2. **The universal sum test (Theorem 11).** For recursive P,
   δ₀(x) = log(m(x)/P(x)) is lower semicomputable, and
   Σ_x P(x) 2^{δ₀(x)} = Σ_x m(x) ≤ 1, so it is a sum P-test. For any
   lower-semicomputable sum test δ, P(x) 2^{δ(x)} is a
   lower-semicomputable semimeasure, so by 1, δ₀ ≥ δ − K(δ) − O(1). So δ₀
   is universal, and D is random for P exactly when δ₀(D) is bounded.
3. **The identity.** Write d(D|H) = log(m(D|H)/Pr(D|H)), the universal
   deficiency of D for Pr(·|H). By the coding theorem,
   −log Pr(D|H) = K(D|H) + d(D|H) + O(1), and under the universal prior
   −log m(H) = K(H) + O(1). So
   −log Pr(D|H) − log m(H) = K(D|H) + K(H) + d(D|H) + O(1).
   By 1, d(D|H) ≥ −K(Pr(·|·)) − O(1). By 2, d is bounded above exactly
   when D is random for H. This is Theorems 3 and 5 under P = m.
4. **Selection (Theorem 4).** Let H₁ be the ideal-MDL choice and H₂ the
   MAP choice, and suppose both have d ≤ c. Then
   L_map(H₁) = L_mdl(H₁) + d₁ ≤ L_mdl(H₂) + c ≤ L_map(H₂) − d₂ + c
   ≤ L_map(H₂) + c + K(Pr(·|·)) + O(1),
   so their posteriors differ by at most a factor 2^{c + K(Pr(·|·)) + O(1)}.
5. **Where they part.** The data 0ⁿ have deficiency about n − O(log n)
   for the fair coin (Example 3), and that is the amount by which the two
   lengths differ there.

What changed: the paper's slack α = K(Pr(·|H)) + K(P) bounds the gap, but
3 shows that the gap is the deficiency itself. Domination conditional on H
bounds the deficiency's negative side by K(Pr(·|·)), which does not grow
with H. Nothing in the paper shows that the slack must reach K(Pr(·|H)).
[NOTE-801](../notes.d/NOTE-801.md)'s "α can be as large as K(H)" describes the bound, not the gap.
For recursive priors other than m, the K(P) term of step 3's prior half
remains, and the narrowed title does not cover them.
