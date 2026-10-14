---
status: Read
paper: LIT-tmpjy3gf
title: 'Dasgupta & Gupta — an elementary proof of the Johnson–Lindenstrauss lemma'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the author-posted PDF on Sanjoy Dasgupta's UCSD page
    (cseweb.ucsd.edu/~dasgupta/papers/jl.pdf, 6 pages), extracted with
    pdftotext -layout, with page 3 re-extracted without -layout to check
    Lemma 2.2. The copy is the journal version, not a preprint: it is the
    Wiley typeset article, Random Struct. Alg. 22: 60–65, with the DOI
    10.1002/rsa.10073, the received and accepted dates and the publisher's
    running heads. Read in full: the abstract, §1, §2 (Theorem 2.1, Lemma
    2.2 and both proofs) and §3. The reference list was read entry by entry
    against the in-text citations. The displayed mathematics was garbled by
    extraction and was reconstructed; the reconstruction of Lemma 2.2 and
    of f(t₀) was checked by redoing the algebra.
date: '2026-10-14'
summary: >-
  For n points in ℝᵈ and 0 < ε < 1, a projection onto a random
  k-dimensional subspace, scaled by √(d/k), keeps every squared pairwise
  distance within a factor 1 ± ε with probability at least 1/n once
  k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n. The proof bounds each tail of the squared
  length of a random unit vector's first k coordinates by Markov's
  inequality on an exponential of Gaussian squares, and then takes a union
  bound over the n(n−1)/2 pairs.
---

# NOTE-tmpve6z2: Dasgupta & Gupta — an elementary proof of the Johnson–Lindenstrauss lemma

## Contribution

The paper gives a short, self-contained proof of the Johnson–Lindenstrauss
lemma with an explicit dimension, k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n. It uses only
the moment generating function of a squared standard Gaussian, Markov's
inequality and a union bound. The authors do not claim a new line of
reasoning: they say it "follows a fairly standard line of reasoning" used
before, for instance by Frankl and Maehara. What it adds is the short
derivation and the constant, which improves Frankl and Maehara's
9(ε² − 2ε³/3)⁻¹ ln n + 1.

## Key insight

The squared length of a fixed vector projected onto a random k-dimensional
subspace has the same distribution as the squared length of the first k
coordinates of a uniformly random unit vector. That vector can be written
as a Gaussian vector divided by its norm. So the event "the projection is
too short" is the event d(X₁² + … + X_k²) ≤ kβ(X₁² + … + X_d²) for
independent N(0, 1) variables, and its probability is bounded by the
Chernoff method. Each tail is then exponentially small in k, and the
dimension needed is set by the log of the number of pairs.

## Assumptions

- **Euclidean setting.** V is a set of n points in ℝᵈ, and the target is
  ℝᵏ with the Euclidean norm.
- **Range of ε.** 0 < ε < 1.
- **Dimension.** k is a positive integer with k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n
  (2.1). If d ≤ k the theorem is called trivial; the proof treats k < d
  only. The construction reduces dimension and says nothing about maps
  that raise it.
- **The random map.** Projection onto a uniformly random k-dimensional
  subspace S, followed by scaling by √(d/k). Gaussians enter only the
  analysis, as a way to sample a uniform point on S^{d−1}. A Gaussian or
  ±1 matrix is a different construction, discussed in §3 as other authors'
  work.
- **What is preserved.** Squared distances:
  (1 − ε)‖u − v‖² ≤ ‖f(u) − f(v)‖² ≤ (1 + ε)‖u − v‖². The abstract and §1
  speak of distances changing "by only a factor of (1 ± ε)"; the theorem
  states it for squares.

## Key results

- **Theorem 2.1.** For any 0 < ε < 1 and any integer n, let k be a
  positive integer with k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n. Then for any set V of n
  points in ℝᵈ there is a map f : ℝᵈ → ℝᵏ such that for all u, v ∈ V,
  (1 − ε)‖u − v‖² ≤ ‖f(u) − f(v)‖² ≤ (1 + ε)‖u − v‖². The map can be found
  in randomized polynomial time.
- **Lemma 2.2.** Let k < d, let Y be uniform on S^{d−1}, let Z be its
  first k coordinates and L = ‖Z‖², so μ = E[L] = k/d.
  - (a) If β < 1, Pr[L ≤ βk/d] ≤ β^{k/2} (1 + (1 − β)k/(d − k))^{(d−k)/2}
    ≤ exp((k/2)(1 − β + ln β)).
  - (b) If β > 1, Pr[L ≥ βk/d] ≤ β^{k/2} (1 + (1 − β)k/(d − k))^{(d−k)/2}
    ≤ exp((k/2)(1 − β + ln β)).
  The two parts have the same bound. The second inequality in each is
  (1 + x)^{(d−k)/2} ≤ exp(x(d − k)/2); the paper does not write this step
  out.
- **Proof of Lemma 2.2(a), (2.2).** With t > 0, Markov's inequality on
  exp{t(kβ ΣᵢXᵢ² − d Σ_{i≤k}Xᵢ²)} and E[e^{sX²}] = 1/√(1 − 2s) for
  s < 1/2 give g(t) = (1 − 2tkβ)^{−(d−k)/2}(1 − 2t(kβ − d))^{−k/2} for
  0 < t < 1/(2kβ). It is minimized at t₀ = (1 − β)/(2β(d − kβ)), where
  f(t₀) = 1/g(t₀)² = ((d − k)/(d − kβ))^{d−k}(1/β)^k. Part (b) is the
  same with g(−t), for 0 < t < 1/(2(d − kβ)), minimized at −t₀.
- **Lower tail in the theorem.** With β = 1 − ε and
  ln(1 − x) ≤ −x − x²/2 for 0 ≤ x < 1: Pr[L ≤ (1 − ε)μ] ≤ exp(−kε²/4)
  ≤ exp(−2 ln n) = 1/n².
- **Upper tail in the theorem.** With β = 1 + ε and
  ln(1 + x) ≤ x − x²/2 + x³/3 for x ≥ 0: Pr[L ≥ (1 + ε)μ]
  ≤ exp(−k(ε²/2 − ε³/3)/2) ≤ exp(−2 ln n) = 1/n².
- **Union bound.** Each pair fails with probability at most 2/n². Over
  C(n, 2) pairs the failure probability is at most C(n, 2) × 2/n² = 1 − 1/n,
  so f = √(d/k) times the projection works with probability at least 1/n.
  Repeating O(n) times boosts this to a constant.
- **Earlier bounds, as the paper reports them (§1, §2).** Johnson and
  Lindenstrauss: O(log n/ε²), with the lower bound on k "being O(log n)" in
  the paper's wording. Frankl and Maehara:
  k = 9(ε² − 2ε³/3)⁻¹ ln n + 1. Indyk–Motwani and Achlioptas: "essentially
  the same bounds" as Theorem 2.1. Alon: any n points with pairwise
  distances in [1 − ε, 1 + ε] need Ω(log n/(ε² log 1/ε)) dimensions, so
  the result is "essentially tight".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n suffices for a map keeping all squared pairwise distances of n points within 1 ± ε | strong | Theorem 2.1, complete proof |
| C2 | Projection onto a random k-subspace, scaled by √(d/k), is such a map with probability at least 1/n | strong | Proof of Theorem 2.1 |
| C3 | The squared projected length of a random unit vector has tails at most exp((k/2)(1 − β + ln β)) on each side | strong | Lemma 2.2, proved |
| C4 | The proof uses only elementary probability | strong | §2: Gaussian MGF, Markov's inequality, union bound |
| C5 | Indyk–Motwani's analogous statement needs k larger by roughly O(log log n); Achlioptas gets the same k as Theorem 2.1 with ±1 entries | weak | §3, reported without proof |
| C6 | The JL dimension is essentially tight, by Alon's Ω(log n/(ε² log 1/ε)) | weak | §1, cited to an unpublished manuscript |

## Method

1. Reduce the projection of a fixed vector onto a random subspace to the
   projection of a random unit vector onto the first k coordinates.
2. Write the random unit vector as X/‖X‖ with X standard Gaussian in ℝᵈ.
3. Bound each tail of L = Σ_{i≤k}Xᵢ²/Σ_{i≤d}Xᵢ² by Markov's inequality
   on an exponential, optimized over t (Lemma 2.2).
4. Set β = 1 ∓ ε, use the two logarithm inequalities, and require each
   tail to be at most 1/n² (Theorem 2.1).
5. Union bound over the pairs; repeat the random choice O(n) times.

## Concepts

- **Distortion.** For a pair, ‖f(vᵢ) − f(vⱼ)‖²/‖vᵢ − vⱼ‖². The map is
  good when it lies in [1 − ε, 1 + ε] for every pair.
- **Elementary.** In the paper's sense: "elementary probabilistic
  techniques", the large-deviation method for sums of random variables
  (Chernoff, Hoeffding), with no geometric measure concentration.
- **Random k-dimensional subspace.** The map's randomness. The paper does
  not specify how to sample it beyond "take a random k-dimensional
  subspace".

## Connections

The paper places itself after Johnson and Lindenstrauss's original proof
and Frankl and Maehara's simplification, and beside Indyk–Motwani,
Arriaga–Vempala and Achlioptas, who gave "similar proofs" through simple
randomized algorithms (§1). §3 contrasts its random subspace with
Indyk–Motwani's k independent Gaussian vectors, f(x)ᵢ = (1/√d)⟨Uᵢ, x⟩,
which are almost orthogonal, and with Achlioptas's entries drawn
uniformly from {1, −1}. As the extraction prints it, the scaling in §3 is
1/√d; the scaling that makes E‖f(x)‖² = ‖x‖² for a k × d Gaussian matrix
is 1/√k (my observation; the copy may be at fault, or the text). It cites
derandomizations by Engebretsen, Indyk and O'Donnell and by Sivakumar.

The copy's in-text citations do not match its reference list from [12] on.
The text cites [13] for Johnson and Lindenstrauss, [12] for Indyk and
Motwani, [14] for graph embeddings and [15] for derandomization. The list
has thirteen entries, in which those works are [11], [10], [12] and [13].
The in-text numbers run two ahead (my observation, from the copy as
printed).

## Bearing on the record

**[QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md).** The paper bears on the question's
proposed general shape and on two of its three threads.

- **The general shape.** The question asks whether each threshold is "the
  log of the size of the family a map must hold, divided by a squared
  tolerance". In this proof that is literally how the constant arises.
  Each pair fails with probability at most 2 exp(−k(ε²/2 − ε³/3)/2). The
  family is the n(n−1)/2 pairs, and requiring each tail to be at most 1/n²
  gives k ≥ 2 ln(n²)/(ε²/2 − ε³/3). The 4 in (2.1) is 2 × 2, one 2 from
  the log of a family of size about n² (my observation, from the proof).
  The question's ε⁻² is the leading term of (ε²/2 − ε³/3)⁻¹.
- **Superposition.** The ingredient the Baraniuk et al. route needs is a
  per-vector tail bound exponentially small in k, then a union bound over
  a different family. Lemma 2.2 is such a bound, but for a random
  orthogonal projection, not for a matrix with independent entries. The
  transfer to independent-entry matrices is what §3 attributes to
  Indyk–Motwani and Achlioptas. So the concentration step that a RIP proof
  over sparse supports would reuse is closer to theirs than to this
  paper's (my observation; [LIT-tmpcfdvm](../literature.d/LIT-tmpcfdvm.md) is unread).
- **Expand and threshold.** The proof says "if d ≤ k, the theorem is
  trivial" and treats k < d only. The paper is about going down in
  dimension, as the question says. Nothing in it addresses a map that goes
  up and then thresholds.
- **Random features.** The paper says nothing about kernels, Gram
  matrices or sample counts. It does not bear on the 2N = n thread.
- **Tightness.** The paper reports Alon's lower bound,
  Ω(log n/(ε² log 1/ε)), as "essentially tight", short of ε⁻² log n by a
  factor log(1/ε). The question's claim that the bound is tight rests on
  [LIT-tmp8s1wj](../literature.d/LIT-tmp8s1wj.md), not on this paper.

**Checks of what the record says about this paper.**

- LIT summary, "from moment-generating-function bounds on a χ² variable".
  Imprecise. The paper never says χ². It applies Markov's inequality to
  exp{t(kβ Σ_{i≤d}Xᵢ² − d Σ_{i≤k}Xᵢ²)}, a weighted difference of Gaussian
  squares, using the Gaussian MGF E[e^{sX²}] = 1/√(1 − 2s). The quantity
  bounded is the ratio L = Σ_{i≤k}Xᵢ²/Σ_{i≤d}Xᵢ², which is beta
  distributed, not χ².
- LIT summary, "k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n". Correct; it is (2.1).
- LIT takeaway, "the length of a random unit vector's projection onto k
  coordinates". Correct, as the reduction in §2. The bounded quantity is
  the squared length, and the map itself is a projection onto a random
  subspace.
- LIT takeaway, "no measure concentration on the sphere is cited".
  Correct. The cited tools are Chernoff and Hoeffding.
- LIT takeaway, "the map succeeds with probability at least 1/n, so
  repeating finds one quickly". The first half is correct. The paper says
  O(n) repetitions boost the success probability to a constant; "quickly"
  should be that.
- LIT keyword "Gaussian random matrix". Wrong for this paper's map, which
  is a scaled projection onto a random subspace. The Gaussian matrix is
  Indyk–Motwani's construction, described in §3.
- LIT Standing, "the version of the proof most later work quotes". The
  paper cannot confirm this; it is a claim about reception, not about the
  text.
- LIT Standing, "its concentration step is the one Baraniuk et al. turn
  into the restricted isometry property". Imprecise. This paper's
  concentration step is for a random orthogonal projection. The
  independent-entry matrices a RIP proof uses are the constructions §3
  credits to Indyk–Motwani and Achlioptas, the latter "with the same bound
  for k". Whether Baraniuk et al. use this paper's exponent can be settled
  only by reading [LIT-tmpcfdvm](../literature.d/LIT-tmpcfdvm.md).
- LIT citation, "(2003) … 22(1): 60–65". Volume and pages match the copy.
  The copy prints no issue number. Its own citation line reads "Random
  Struct. Alg., 22: 60–65, 2002", with "© 2003" on the same line and
  "© 2002" in the first-page footer. The `published: '2002-11-25'` date is
  not printed in the copy; nothing in it conflicts.
- QUESTION, "ε⁻² log n for keeping the distances of n points". Consistent
  in order. In this paper the guarantee is for squared distances, and the
  explicit form is 4(ε²/2 − ε³/3)⁻¹ ln n.
- QUESTION, sparse binary matrices of the fly and SDM "are the ensembles
  Achlioptas shows keep the JL guarantee". This paper reports Achlioptas's
  ensemble only as entries uniform on {1, −1}, which are zero-mean and
  dense. It does not mention a {0, 1} ensemble. Whether nonnegative sparse
  0/1 matrices are covered is for the reading of
  [LIT-tmppzjx6](../literature.d/LIT-tmppzjx6.md) (my observation).
- **For the anthology.** The paper carries no instruction for
  machine-learning practice. It is mathematics and stays here.

## Limitations

- The success probability is only 1/n per draw. The paper gives no
  constant-probability version without O(n) repetitions, and does not
  trade k against failure probability.
- The proof covers the random subspace only. The Gaussian-matrix and ±1
  variants are described in §3 without proof.
- Squared distances only; the unsquared factor is √(1 ± ε), which the
  paper does not state.
- The tightness remark rests on an unpublished manuscript of Alon and is
  short of matching by log(1/ε).
- Lemma 2.2(b) needs d > kβ for its range of t. When kβ ≥ d the event
  L ≥ βk/d has probability zero, so nothing is lost, but the paper does
  not say this (my observation).
- §2 says "with probability O(1/n²), its (scaled) length is not distorted
  by more than (1 ± ε)". It means the opposite: the length is distorted by
  more than 1 ± ε with probability O(1/n²) (my observation; a slip in the
  text).

## Open questions

- Whether the same per-pair tail, with the same constant, holds for
  nonnegative sparse 0/1 matrices like the fly's. This paper's proof does
  not reach them.
- Whether the factor 4 is the best possible for this method, or only for
  this choice of the 1/n² per-pair budget. The paper does not discuss it.
