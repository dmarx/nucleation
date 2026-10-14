---
status: Read
paper: LIT-224
title: 'Grünwald & Vitányi — Shannon information and Kolmogorov complexity'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v1 PDF (arxiv.org/pdf/cs/0410002, 54 pp.,
    1 Oct 2004, the only version), text extracted with pdftotext: §§1–7
    and Appendix A. The introductory §§1.2–2.2 were read more quickly than
    the rest. The proofs given in the paper were read step by step:
    Theorems 2.10, 3.6, 4.1, 4.4, 4.6 and 5.13, Lemma 3.7, Corollaries 4.3
    and 4.5, Proposition 5.3, Proposition 6.17, Lemma 6.25 and Theorem
    6.27. Theorems 2.2, 2.5, 2.8, 2.9, 3.3, 3.5 and 6.8 are cited from
    Cover & Thomas, Li & Vitányi and Hammer et al. without proof. Results
    attributed to Vereshchagin & Vitányi (LIT-239) were checked against the
    reading of that paper. The arXiv record carries the authors' warning
    that "there are some errors in this paper draft". The skim note filed
    with the paper is NOTE-213.
date: '2026-10-14'
summary: >-
  A survey pairing Shannon's and Kolmogorov's notions. Expected
  Kolmogorov complexity exceeds entropy by between 0 and K(f) + O(1), and
  expected algorithmic mutual information lies between I(X;Y) − K(f) and
  I(X;Y) + 2K(f). An algorithmic sufficient statistic is probabilistically
  nearly sufficient in expectation, one way only. The expected structure
  function brackets the distortion-rate function with a K(f, d, m, R) shift
  in rate. Each link holds only up to the complexity of the distribution.
---
<!-- inactive-ok-file: THEORY-tmp7cr5e THEORY-tmppce05 THEORY-163 THEORY-157 THEORY-238 — Proposed; the theories filed from this reading and those it bears on, open -->

# NOTE-tmpavenk: Grünwald & Vitányi — Shannon information and Kolmogorov complexity

## Contribution

A systematic comparison, concept by concept, of Shannon's probabilistic
information theory and Kolmogorov's algorithmic one: coding, entropy
against complexity, mutual information, data processing, sufficient
statistics, and rate–distortion against the structure function. Most of
it gathers earlier results. Two pieces are new, by the authors' account
(§7). §5.3 shows that algorithmic sufficiency implies probabilistic near-
sufficiency in expectation. §6.3 shows that the expected structure function
brackets the distortion-rate function. After it there is one place where
each Shannon quantity and its Kolmogorov counterpart are set side by side
with the size of the gap stated.

## Key insight

Every bridge from an individual-object quantity to a Shannon quantity
goes through the same inequality, f(x) ≤ 2^{K(f)+O(1)} m(x): a computable
distribution is dominated by the universal one, at a multiplicative cost
of the distribution's own complexity. So each "Shannon = expected
Kolmogorov" statement is exact only up to K(f). The gap is small for
simple sources and unbounded for complex ones.

## Assumptions

- **Computable distributions.** Every bridge theorem needs f computable.
  K(f) enters every error term (Theorems 2.10, 3.6, 5.13, 6.27). Lemma 3.7
  removes the term only by giving f to the machine as an oracle.
- **Additive precision.** Kolmogorov (in)equalities hold to O(1) where
  the conditionals use x* (Theorem 3.3), and to O(log n) otherwise (Theorem
  3.5).
- **Sequential sources (§5.3).** Sufficiency is compared across all
  lengths n, through a "sequential statistic" (Def. 5.9) and a model class
  of sequential information sources.
- **Recursive distortion (§6.3).** Theorem 6.27 needs a recursive
  distortion measure d and a total recursive mass function f.

## Key results

- **Theorem 2.10.** For computable f, 0 ≤ Σ_x f(x)K(x) − H(f) ≤ K(f) + O(1).
  The lower bound is the noiseless coding theorem. The upper bound is
  −log f(x) ≥ K(x) − K(f) − O(1) by domination. A point mass on one x of
  length n with K(x) > n has entropy 0 and expected complexity above n.
  This is consistent, because then K(f) ≥ K(x). Given f as an oracle, the
  gap is O(1) (eq. 2.5).
- **Theorem 3.3 (cited).** K(x, y) = K(x) + K(y | x*) + O(1). With x in
  place of x*, it fails by up to log n − log log n (the K(x*) | x example).
- **Theorem 3.5 (cited, Hammer et al.).** Every linear inequality valid for
  Shannon entropies is valid for Kolmogorov complexities to within
  O(log n), and conversely.
- **Theorem 3.6.** For computable joint f,
  I(X;Y) − K(f) < Σ f(x,y) I(x : y) < I(X;Y) + 2K(f), to within O(1).
  Lemma 3.7 gives exact equality to O(1) with f in the conditional.
- **Theorems 4.4, 4.6 and Corollary 4.5 (data processing).** I(z : y) <
  I(x : y) + K(q) for z computed from x* by q; I(f(x) : g(y)) < I(x : y) +
  K(f) + K(g). For randomised processing,
  Σ_z m(z | x*) 2^{I(z:y) − I(x:y)} = O(1), so a gain of d bits has
  probability O(2^{−d}). The proofs go through the triangle inequality
  K(x | y*) < K(z | y*) + K(x | z*) (Theorem 4.1).
- **Proposition 5.3.** Probabilistic sufficiency holds for every x iff it
  holds in expectation under every θ, iff I(Θ;X) = I(Θ;S(X)) for every
  prior (eq. 5.10). This is exact, by the information inequality.
- **Remark 5.11.** Once equality is relaxed to "within a constant", the
  individual and expectation versions are no longer equivalent.
- **Theorem 5.13 (new).** If a sequential statistic S satisfies
  K(S(x)) + log |S(x)| ≤ K(x) + c for every x, then for every θ with
  K(f_θ) < ∞ there is a constant c' with
  Σ_x f_θ(x)[log |S(x)| − log 1/f_θ(x | S(x))] ≤ c' for all n. So S is
  nearly sufficient in expectation, with g uniform. It is uniform over
  the class only if sup_θ K(f_θ) < ∞. The proof is a sandwich: u + v = w
  to O(1) with u ≥ u′, v ≥ v′ and u′ + v′ = w forces v = v′. The converse
  is not claimed.
- **§6.2 (restating [LIT-239](../literature.d/LIT-239.md)).** β_x(R) = h_x(R) + R − K(x) = λ_x(R) − K(x)
  to logarithmic precision. Witnesses of h_x and λ_x witness β_x. h_x and
  λ_x are upper semicomputable; β_x is not semicomputable.
- **Remark 6.14.** "ML = MDL" holds only when model complexity is bounded
  by a fixed R. Unconstrained, h_x(K(x) + O(1)) = 0 at the overfitting
  model {x}. MDL "may be just as prone to overfitting as is ML" unless it
  is biased to the least complex model on the flat stretch of λ_x.
- **Proposition 6.17.** Finite-set and computable-probability models are
  interchangeable, at a cost of 2 log K(f) + K(⌊log 1/f(x)⌋) + … in
  deficiency and K(⌊log 1/f(x)⌋) in complexity. That is O(log n) once
  K(f) ≤ n + O(log n).
- **Lemma 6.25.** A sufficient statistic y for x makes x typical for y, and
  K(y | x) = O(1). So for each model class and distortion only a bounded
  number of sufficient statistics exist.
- **Theorem 6.27 (new).** For a recursive distortion d and total recursive
  f, over m i.i.d. repetitions,
  (1/m) E h_x(mR + K(f, d, m, R) + O(log n)) ≤ D*_m(R) ≤ (1/m) E h_x(mR).
  Corollary 6.29(ii): lim_{m→∞} (1/m) E h_x(mR) = D*(R). Here h_x is the
  structure function for the model class and distortion d (§6.3.1). Both
  directions are covering arguments. The right-hand step, which sets
  h_x(mR) equal to the radius of x's sphere in the canonical cover, is
  asserted rather than argued. It bounds complexity conditional on mR
  where h_x is unconditional, a gap of order K(mR) that the statement does
  not carry.
- **Example 6.13.** For the uniform source and log-cardinality distortion,
  E h_x(R) = n − R + o(n − R) = (1 + o(1)) D*(R). The displayed arithmetic
  is garbled ("O(n − R/2^{−K(n)})").
- **Appendix A.** Two-part codes over a countable family are universal
  both per sequence and in expectation, within LN(k) + LN(n). K is the
  length function of a universal code for every computable family.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Entropy equals expected Kolmogorov complexity to within K(f) + O(1), and exactly to O(1) given f | strong | Theorem 2.10 and eq. 2.5, proofs read |
| C2 | Shannon mutual information equals expected algorithmic mutual information to within K(f) below and 2K(f) above | strong | Theorem 3.6, Lemma 3.7 |
| C3 | Algorithmic mutual information obeys data processing up to the complexity of the processing, and randomised processing gains d bits with probability O(2^{−d}) | strong | Theorems 4.4, 4.6, Corollary 4.5 |
| C4 | An algorithmic sufficient statistic is probabilistically nearly sufficient in expectation for each computable model, uniformly only when model complexity is bounded | strong | Theorem 5.13; one direction only |
| C5 | Individual and expectation near-sufficiency come apart once equality is relaxed to a constant | moderate | Remark 5.11, a sketched example |
| C6 | Expected structure function and distortion-rate function agree asymptotically per symbol, for recursive sources and distortions | moderate | Theorem 6.27; one step asserted |
| C7 | MDL without a bias to the least complex model overfits like ML | moderate | Remark 6.14, an example (random x) |

## Concepts

- **Algorithmic mutual information.** I(x : y) = K(y) − K(y | x*) =
  K(x) + K(y) − K(x, y) + O(1). Never negative, unlike the pointwise
  Shannon I(X = x : Y) (Example 3.1).
- **Probabilistic sufficient statistic.** S with f_θ(x | S(x)) independent
  of θ (eq. 5.2). Minimal if it is a function of every other.
- **Algorithmic sufficient statistic.** A shortest program for an optimal
  set S ∋ x, K(S) + log |S| = K(x) + O(1). It is defined with no model
  class.
- **Nearly sufficient (individual / expectation).** (5.4) or (5.5) holding
  to within a constant (Def. 5.10).
- **Distortion sphere, randomness deficiency for general models.**
  B_y(r) = {x : d(x, y) = r}; δ(x | y) = log |B_y(d(x, y))| −
  K(x | y, d(x, y)) (Def. 6.21).

## Connections

§6.2 restates Vereshchagin & Vitányi ([LIT-239](../literature.d/LIT-239.md)). §6.3 follows their
individual rate–distortion manuscript, which is not held. §5.2 follows
Gács, Tromp & Vitányi (2001). The randomness deficiency and the
universal distribution are the same objects as in Vitányi & Li ([LIT-225](../literature.d/LIT-225.md)),
here set beside the Shannon–Fano code. §7 names universal coding and
Rissanen's MDL as the practical middle ground, and points to Rissanen and
Tabus on the structure function in MDL. That is the thread Grünwald & Roos
([LIT-238](../literature.d/LIT-238.md), §7) also mention. The rate–distortion half connects to the
information bottleneck ([LIT-338](../literature.d/LIT-338.md)), a rate–distortion problem with a derived
distortion, as [NOTE-300](NOTE-300.md) already says.

## Bearing on the record

- **No THEORY, QUESTION or CLAIM cited this paper before today.** Its
  bridge theorems are filed as [THEORY-tmp7cr5e](../theory.d/THEORY-tmp7cr5e.md). Its §6.2 restates the
  result filed from [LIT-239](../literature.d/LIT-239.md) as [THEORY-tmppce05](../theory.d/THEORY-tmppce05.md).
- **The LIT's summary says too much.** [LIT-224](../literature.d/LIT-224.md) said that "in each pair the
  Shannon notion is, up to additive terms, the expectation of the
  Kolmogorov one". For entropy and mutual information that is right, with
  the additive term K(f). For sufficient statistics it is not. Theorem 5.13
  is a one-way implication, from algorithmic to probabilistic near-
  sufficiency in expectation, and is not an expectation identity. For the
  structure function it holds only asymptotically per symbol, with a rate
  shift of K(f, d, m, R). The LIT is corrected.
- **[NOTE-241](NOTE-241.md) cites this paper correctly.** Its use is the distinction
  between the entropy of a distribution and the complexity of an
  individual string, and that compressed sizes are upper bounds on
  description length. Theorem 2.10 and §2.2 say exactly that.
- **[NOTE-300](NOTE-300.md) cites it correctly** for the pairing of rate–distortion with
  the structure function. Theorem 6.27 is the formal link, with the
  conditions above.
- **[THEORY-238](../theory.d/THEORY-238.md) is consistent with it.** That theory's "Not Kolmogorov
  complexity: 'MDL' here is a Shannon coding rate under a prior" is the
  distinction this paper draws in §2. Theorem 2.10 says the two agree in
  expectation only up to K(f).
- **[THEORY-157](../theory.d/THEORY-157.md) and [CLAIM-152](../claims.d/CLAIM-152.md) (sufficiency).** Proposition 5.3's equivalence
  of the individual, expectation and mutual-information definitions of
  sufficiency holds only when equality is exact, by Remark 5.11.
  Theorem 5.13 then gives a sufficiency that is relative to no single model
  family, only to the class of computable ones. That qualifies [CLAIM-152](../claims.d/CLAIM-152.md)'s
  "any individuation built on sufficiency is relative to the target". The
  algorithmic statistic's target is the data string itself, and its
  relativity is to the reference machine.
- **[THEORY-163](../theory.d/THEORY-163.md) (colour naming near the IB bound).** No direct bearing. §6.1
  treats the rate–distortion function it uses, in expectation, and gives
  the reason an individual-data version differs.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **A survey with a stated error warning.** The arXiv record says there
  are errors in the draft. Those found in this reading are the garbled
  arithmetic in Example 6.13 and in Example 6.16 ("β_x(i) ± O(log n)"),
  and the asserted step in Theorem 6.27. No journal version of this text
  was found.
- **Every bridge costs K(f).** None of the identifications says anything
  about a complex or unknown distribution, or about one string.
- **The new §6.3 result concerns noise-like data.** The authors say
  Theorem 6.27 is "a 'sanity check'" for i.i.d. sources, whose typical
  data "have the characteristics of random noise". It is not a claim about
  structured data.
- **Uncomputable.** As with [LIT-239](../literature.d/LIT-239.md), nothing here is effective.

## Open questions

- Does a converse of Theorem 5.13 hold in any form? Is a probabilistic
  sufficient statistic for a simple model family algorithmically
  sufficient for typical data?
- Can the gap in Theorem 6.27's right-hand inequality be closed without
  the K(mR) conditioning slack, and what does the published individual
  rate–distortion paper (Vereshchagin & Vitányi) do there?
- For which natural families is sup_θ K(f_θ) finite? A Bernoulli family
  with real θ is not, so Theorem 5.13's uniform form does not cover it.
