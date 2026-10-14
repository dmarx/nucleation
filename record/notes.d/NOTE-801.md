---
number: 801
status: Read
formerly:
- NOTE-tmpp6trb
paper: LIT-225
title: 'Vitányi & Li — MDL induction, Bayesianism and Kolmogorov complexity'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v1 PDF (arxiv.org/pdf/cs/9901014, 35 pp.,
    27 Jan 1999, the submitted version of IEEE Trans. Inf. Theory
    46(2):446–464, 2000), text extracted with pdftotext: §§1–4 and
    Appendices A–C, with every theorem, example and remark. The proofs of
    Theorems 1–5, 7 and 8, Claims 1–2 and Lemma 3 and Theorems 9–11 were
    read step by step. Theorem 6 (Solomonoff) and Claims 3–4 (Gács) are
    cited without proof. Two facts the main proof rests on, eq. (25) and
    the coding theorem, are quoted from Li & Vitányi's textbook and were
    not checked there. The journal version was not read. The skim note
    filed with the paper is NOTE-203.
date: '2026-10-14'
summary: >-
  With the universal prior, the Fundamental Inequality puts
  −log Pr(D|H) − log P(H) within α = K(Pr(·|H)) + K(P) of K(D|H) + K(H)
  when D is random for H and H is random for P. So ideal MDL and MAP
  agree to a factor 2^{−α} among such "admissible" hypotheses. α can be as
  large as K(H), and outside the admissible set the two can pick different
  hypotheses. For finite-set models, MAP, ideal MDL and Kolmogorov's
  minimal sufficient statistic coincide.
---
<!-- inactive-ok-file: THEORY-259 THEORY-087 THEORY-036 — Proposed; the theory filed from this reading and the entries it bears on, open -->

# NOTE-801: Vitányi & Li — MDL induction, Bayesianism and Kolmogorov complexity

## Contribution

The paper defines "ideal MDL" as selecting the H that minimises
K(H) + K(D | H), and derives it from Bayes's rule by substituting the
universal distribution m = 2^{−K} for both the prior and the likelihood.
It then states exactly when that substitution is licensed. Before it, MDL
and Bayes were said to be "related" without a stated condition. After it,
the condition is individual randomness: the data must be Martin-Löf random
for the hypothesis, and the hypothesis random for the prior. For finite-set
hypotheses it shows that Bayes with the universal prior, ideal MDL and
Kolmogorov's minimal sufficient statistic select the same set. It adds a
prediction result: for μ-random sequences, prediction by the shortest
monotone program converges to the true conditional.

## Key insight

The Shannon–Fano length −log P(x) and the shortest effective length K(x)
differ exactly by the universal randomness test log(m(x)/P(x)). Where that
test is near zero, Bayes's code lengths and Kolmogorov's are the same
numbers, so the posterior mode and the minimum description coincide. Where
it is large, the data are "atypical" for the hypothesis. There the two
principles part company, and MDL avoids the hypothesis for which the data
are atypical even if it is true.

## Assumptions

- **Countable, recursive hypotheses.** H ranges over an enumerable class.
  Each Pr(· | H) is a recursive probability mass function (Def. 4), and the
  prior P is recursive, except where P := m, which is only enumerable
  (§2.5).
- **Forcing hypothesis.** For the generalised minimal sufficient statistic
  (Def. 4, eq. 8), every D must have an H_D with Pr(D | H_D) = 1 and
  K(D | H_D) = O(1).
- **Randomness for finite objects is sharp only up to constants.** "D is
  Pr(· | H)-random" means log(m(D | H)/Pr(D | H)) ≤ 0 to within O(1)
  (Theorem 11). Remark 1 relaxes this to a "weak randomness" that holds
  with probability above 1 − 1/n, at an extra logarithmic cost in α.
- **Uncomputable.** K is not computable, and §2.6 explicitly leaves
  practical codes aside.
- **Prediction (§3).** Binary sequences, μ a recursive semimeasure (a
  positive recursive measure in Theorem 7), and ω μ-random.

## Key results

- **Theorem 1 (finite sets).** For H = {H ⊆ {0,1}ⁿ}, D ∈ {0,1}ⁿ and n
  large: three rules select the same hypothesis. They are (i) Bayes with
  prior m and likelihood 1/d(H), taking the least complex MAP set, (ii)
  the Kolmogorov minimal sufficient statistic H₀, the least K(H | n) with
  K(H | n) + log d(H) = K(D | n), and (iii) ideal MDL. The proof uses
  K(H | n) + K(D | H, n) ≥ K(D | n) − O(1) for all H. Because the defining
  equality holds only to O(1), "the same hypothesis" means the same up to
  the choice of that constant.
- **Theorem 2.** The least complex MAP hypothesis under prior m equals the
  generalised minimal sufficient statistic (eq. 8). It uses
  −log Pr(D | H) ≥ K(D | H) − O(1) for recursive Pr.
- **Theorem 3 (Fundamental Inequality).** If Pr(·|·) and P are recursive,
  D is Pr(· | H)-random and H is P-random, then

  K(D|H) + K(H) − α(P, H) ≤ −log Pr(D|H) − log P(H) ≤ K(D|H) + K(H),
  with α(P, H) = K(Pr(·|H)) + K(P).

  Conversely, equality to O(1) implies both randomness conditions. The
  proof is two lines from m(D | H) ≥ 2^{−K(Pr(·|H))} Pr(D | H) (eq. 25) and
  the universal sum test (Theorem 11). The authors note K(Pr(·|H)) ≤ K(H)
  + O(1). Since Pr(·|H) is computable from H, the slack can be as large as
  the hypothesis's own complexity. The converse (ii) is given one line.
- **Theorem 4.** Restricted to the admissible set H_D (H is P-random and D
  is Pr(·|H)-random), the MAP hypothesis H_bayes and the ideal-MDL
  hypothesis H_mdl satisfy 2^{−α(P,H)} ≤ Pr(H_mdl | D)/Pr(H_bayes | D) ≤ 1
  and 0 ≤ [K(D|H_mdl) + K(H_mdl)] − [K(D|H_bayes) + K(H_bayes)] ≤ α(P,H).
  The statement does not say at which H α is evaluated.
- **Theorem 5 and Corollary 1.** With P := m and α = O(1), the Fundamental
  Inequality holds iff D is Pr(· | H_mdl)-random. Corollary 1, that "with
  high probability ideal MDL is an application of Bayes's rule with the
  universal prior", is stated without a proof or a measure.
- **Divergence cases.** Example 3: two hypotheses p = ½ and p ≠ ½, with
  D = 0ⁿ. Bayes picks p ≠ ½. Ideal MDL ties at log n + O(log log n). The
  generalised minimal sufficient statistic selects nothing. Remark 3: if
  B_{1/2} is in fact true and the data happen to be 0ⁿ, Bayes "with an
  appropriate prior" selects B_{1/2}, while MDL selects B₀.
- **Theorem 6 (Solomonoff, cited).** Σₙ Sₙ ≤ K(μ) ln 2 / 2 for the expected
  squared error of the universal predictor M.
- **Theorem 7.** For positive recursive μ and fixed |y|,
  M(y | x)/μ(y | x) → 1 as |x| → ∞ with μ-probability one. The sequences
  where this holds are exactly the μ-random ones. Proof: M/μ is a
  μ-submartingale with expectation ≤ 1, and M(x)/μ(x) ≥ 2^{−K(μ)}.
- **Theorem 8 and Corollary 2.** For μ-random ω with prefix xy, |y| fixed:
  lim −log μ(y | x) = Km(xy) − Km(x) + O(1). So, with μ-probability going
  to one, the y that maximises μ(y | x) is the one minimising
  Km(xy) − Km(x). The proof leans on Gács's results (Claims 3–4).
  −log M and Km agree to O(1) on random strings but differ unboundedly in
  general.
- **Appendix C.** Martin-Löf tests, their enumeration (Lemma 3), a
  universal P-test (Theorem 9), l(x) − C(x | l(x)) − 1 as the universal
  uniform test (Theorem 10), and κ₀(x | P) = log(m(x)/P(x)) as the
  universal sum P-test (Theorem 11).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | When D is random for H and H for P, Bayes code lengths and Kolmogorov code lengths agree to within K(Pr(·\|H)) + K(P) | strong | Theorem 3, given eq. (25) and Theorem 11 |
| C2 | Among admissible hypotheses, ideal MDL and MAP pick hypotheses whose posteriors differ by at most 2^{−α} | strong | Theorem 4, immediate from Theorem 3 |
| C3 | For finite-set models, universal-prior Bayes, ideal MDL and the Kolmogorov minimal sufficient statistic coincide | strong | Theorem 1, up to the O(1) in the defining equality |
| C4 | Outside the admissible set, ideal MDL and Bayes can select different hypotheses, including when the true one is available | moderate | Example 3 and Remark 3, examples only |
| C5 | Ideal MDL coincides with Bayes "with high probability" | weak | Corollary 1, asserted without proof or a measure |
| C6 | For μ-random sequences, shortest-program prediction converges to the true conditional | strong | Theorems 7–8, with Gács's claims cited |
| C7 | Bayesianism is prone to overfitting and MDL is not | weak | stated in §1 as "some evidence"; no result shows it |

## Concepts

- **Ideal MDL.** Select argmin_H {K(D | H) + K(H)}, breaking ties by least
  K(H) (Def. 2).
- **Admissible hypothesis.** H is P-random and D is Pr(· | H)-random (Def.
  6).
- **Randomness deficiency.** κ₀(x | P) = log(m(x)/P(x)) = −log P(x) −
  K(x) + O(1), the universal sum test.
- **Kolmogorov minimal sufficient statistic (KMSS).** The least complex
  finite set H ∋ D with K(H | n) + log d(H) = K(D | n) + O(1) (Def. 3).
- **Exception-based MDL.** Minimise K(H) + K(E | H) for the
  misclassified exceptions E. With positive examples only it selects the
  trivial grammar. It reduces to ideal MDL only for supervised data
  D = (x, y) with K(x | H) constant (Remark 4).

## Connections

The paper's ideal MDL is the principle Vereshchagin & Vitányi ([LIT-239](../literature.d/LIT-239.md))
later give an individual-data guarantee within a complexity class. Their
§V-B(iii) shows that this paper's K(H) + K(D | H) form, the "ultimate
compression" of the two-part code, can select badly fitting models, which
is why they use log |S| instead. Grünwald & Roos ([LIT-238](../literature.d/LIT-238.md)) cite it as the
reference for Kolmogorov-complexity MDL and defer it to Grünwald's 2007
book. Grünwald & Vitányi ([LIT-224](../literature.d/LIT-224.md)) cover the same universal distribution
and randomness deficiency in Shannon terms. It builds on Solomonoff,
Levin, Gács and Martin-Löf, and on Rissanen's and Wallace's practical
principles, which it claims to idealise.

## Bearing on the record

- **No THEORY, QUESTION or CLAIM cited this paper before today.** Its
  Fundamental Inequality and Theorem 4 are filed as [THEORY-259](../theory.d/THEORY-259.md).
- **The LIT's summary says too much.** [LIT-225](../literature.d/LIT-225.md) said ideal MDL coincides with
  MAP "exactly when" the randomness conditions hold. The theorem gives
  agreement to within α = K(Pr(·|H)) + K(P) when they hold, and the
  converse only for agreement to O(1). It is not an exact equivalence. The
  slack is the complexity of the hypothesis's likelihood, which for a
  complex hypothesis is no smaller than the hypothesis itself. The
  summary's "so compression is almost always the best strategy" is the
  paper's own, from Corollary 1 and Corollary 2. Only the prediction half,
  Corollary 2, is proved. The LIT is corrected.
- **[THEORY-087](../theory.d/THEORY-087.md) and [CLAIM-154](../claims.d/CLAIM-154.md).** Both price models by Bayesian evidence
  with priors chosen by the modeller. This paper's prior is the universal
  m, so its "Occam term" is K(H). Theorem 3 says that a recursive prior
  matches it only for P-random hypotheses. A hypothesis the modeller's
  prior treats as special, with −log P(H) ≫ K(H), is exactly where the
  evidence-based and the description-length rankings diverge. That bears
  on how far [CLAIM-154](../claims.d/CLAIM-154.md)'s Bayes-factor threshold can be read as a
  description-length rule. The paper does not consider parametric Occam
  factors.
- **[THEORY-036](../theory.d/THEORY-036.md).** No bearing beyond [LIT-239](../literature.d/LIT-239.md)'s. The paper does not
  discuss real patterns.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Uncomputable throughout.** The authors say practical encodings are
  out of scope (§2.6).
- **"Random for H" is a condition on the unknown.** The admissible set is
  defined by Martin-Löf randomness, which is not decidable. Which
  hypotheses are admissible cannot be checked.
- **The slack is not small in general.** α(P, H) contains K(Pr(·|H)),
  which can equal K(H). The Fundamental Inequality is tight only for simple
  hypotheses and simple priors.
- **Corollary 1 and the overfitting claim are informal.** No probability
  space is specified for "with high probability".
- **Arithmetic and wording.** The polynomial example (Example 4) is
  correct: 5d against nd, so degree 2 wins for n > 5. The text writes
  "y = (y₁, …, xₙ)" for y = (y₁, …, yₙ). The journal version may differ.

## Open questions

- How large is α(P, H) for the hypothesis classes used in practice, say
  k-parameter families truncated to d bits per parameter? If K(Pr(·|H)) is
  about kd, the agreement is only up to the whole model cost.
- Is there a measure under which Corollary 1's "with high probability"
  holds, and what is it a probability over: data, hypotheses, or both?
- How does this relate to Grünwald's later results that Bayes and MDL can
  both be inconsistent under misspecification ([LIT-238](../literature.d/LIT-238.md), §6.3)? There
  the true distribution is outside the class, which this paper's
  framework, where "there are only data and no true hypothesis", does not
  treat.
