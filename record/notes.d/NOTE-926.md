---
number: 926
status: Read
formerly:
- NOTE-tmp4oub5
paper: LIT-1159
title: 'Achlioptas — database-friendly random projections'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from a 15-page manuscript titled "Database-friendly Random
    Projections" (Dimitris Achlioptas, Microsoft Research), hosted at
    infolab.usc.edu/csci599/Fall2002/paper/DR3_jl.pdf. It is not the JCSS
    text, whose Elsevier copy returned 403. The copy is set in the Academic
    Press journal template (the PDF's source is acad_journal.dvi, created
    3 April 2002), with unfilled running-head placeholders, no subtitle, no
    received date and no journal citation. It is longer than a PODS
    paper and shorter than the published 17 pages, so I take it for a
    journal submission draft of about April 2002, between PODS 2001 and
    JCSS 2003. Its numbering is Lemma 1.1, Theorem 1.1, Theorem 2.1,
    Lemmas 4.1, 5.1, 5.2, 6.1, 6.2 and 6.3, and equations (1)–(27).
    Extracted with pdftotext -layout, which lost nearly all mathematics, so
    every page was read from page images rendered with pdftoppm. Sections
    1–6, the acknowledgment and the twelve references were read in full.
    The copy omits the proof of Lemma 6.3 for the sparse distribution
    ("we omit it"); that proof was not read because it is not there.
date: '2026-10-14'
summary: >-
  A random projection keeps all pairwise distances of n points within
  1 ± ε with probability at least 1 − n^−β when k ≥ (4 + 2β)/(ε²/2 − ε³/3)
  · log n and the matrix entries are independent ±1, or √3 times {+1, 0, −1}
  with probabilities 1/6, 2/3, 1/6. This is the same k₀ as the best bound
  for Gaussian projections. The proof shows that every even moment of a
  unit vector's projection is at most that of the all-equal vector
  (1, …, 1)/√d, and that this vector's moments are at most the Gaussian
  ones.
---
<!-- inactive-ok-file: LIT-1158 — Unavailable; the fly paper, named for what this reading says about it -->

# NOTE-926: Achlioptas — database-friendly random projections

## Contribution

Before this paper every construction of a Johnson–Lindenstrauss embedding
projected onto a spherically random subspace, or onto vectors with Gaussian
entries. The paper shows that spherical symmetry is not needed. Two
distributions of entries in {−1, 0, +1} (up to scale) give the same
guarantee with the same number of dimensions as the best Gaussian bound
(Dasgupta and Gupta), and for each fixed d a marginally better one. The
projection then reduces to sums and differences of attributes, which a
database computes with standard SQL aggregates.

## Key insight

What a JL embedding needs is concentration of the squared length of one
fixed vector's projection, not spherical symmetry (§3). With non-Gaussian
entries that concentration depends on the vector, so the proof finds the
worst vector. It is the all-equal vector w = (1, …, 1)/√d and its sign
flips, a "typical" vector, not a spiky one like (1, 0, …, 0) (§3, Lemma
6.1). Its projection has even moments no larger than a Gaussian's (Lemma
6.2), so every vector's projection is at least as concentrated as in the
spherical case. The paper's intuition: a lattice-valued random vector
cannot align with α arbitrarily well, while a Gaussian one can with small
probability, and the bad event that sets k is overestimating the length.

## Assumptions

- **Entries.** r_ij independent, from either
  r_ij = +1 or −1 with probability 1/2 each, or
  r_ij = √3 × {+1 with probability 1/6, 0 with 2/3, −1 with 1/6}
  (Theorem 1.1). Both have mean 0 and variance 1.
- **Scaling.** E = (1/√k) A R, with A the n × d data matrix and R the
  d × k random matrix (Theorem 1.1). The analysis uses R scaled by 1/√d
  and f(α) = √(d/k)(α·c₁, …, α·c_k) (§4.1).
- **Parameters.** ε, β > 0, k ≥ k₀ (Theorem 1.1). No condition relates k
  to d; the statement does not require k < d. My observation: for
  ε ≥ 3/2 the denominator ε²/2 − ε³/3 is not positive, so the bound is
  meaningful only for ε < 3/2. Lemma 5.1 is stated "for any ε > 0".
- **What the proof uses of the distributions.** Only independence, mean 0,
  variance 1, Lemma 6.3, and E(Y^{2ℓ}) ≤ (2ℓ)!/(ℓ!2^ℓ), the Gaussian moment
  (end of §6). The paper says these are "the only two points" where the
  distributions matter.

## Key results

- **Lemma 1.1 (Johnson and Lindenstrauss).** Given ε > 0 and integer n,
  for k ≥ k₀ = O(ε⁻² log n) and every set P of n points in ℝᵈ there is
  f : ℝᵈ → ℝᵏ with (1 − ε)‖u − v‖² ≤ ‖f(u) − f(v)‖² ≤ (1 + ε)‖u − v‖² for
  all u, v ∈ P.
- **Theorem 1.1 (main).** For ε, β > 0, let
  k₀ = (4 + 2β)/(ε²/2 − ε³/3) · log n. For integer k ≥ k₀ and R with
  entries from either distribution above, E = (1/√k) A R maps row i of A
  to row i of E, and with probability at least 1 − n^−β, for all u, v ∈ P,
  (1 − ε)‖u − v‖² ≤ ‖f(u) − f(v)‖² ≤ (1 + ε)‖u − v‖².
- **Theorem 2.1 (Frankl and Maehara, as cited).** For ε ∈ (0, 1/2), any
  sufficiently large P ⊂ ℝᵈ and k ≥ k₀ = ⌈9(ε² − 2ε³/3)⁻¹ log |P|⌉ + 1,
  such an f exists.
- **Prior best (§2).** Dasgupta and Gupta's analysis gives
  k ≥ k₀ = (4 + 2β)(ε²/2 − ε³/3)⁻¹ log n, "exactly the same as the bound in
  Theorem 1.1". The paper says Theorem 1.1 also holds with r_ij ~ N(0, 1)
  by combining that analysis with Indyk and Motwani's viewpoint.
- **Unbiasedness (Eqs. 1–2).** For any independent r_ij with E r_ij = 0
  and Var r_ij = 1, E(Q_j) = 0, E(Q_j²) = ‖α‖²/d, and
  E‖f(α)‖² = ‖α‖².
- **Reduction (Eq. 3).** It suffices that for every fixed α,
  Pr[(1 − ε)‖α‖² ≤ ‖f(α)‖² ≤ (1 + ε)‖α‖²] ≥ 1 − 2/n^{2+β}. A union bound
  over the (n choose 2) pairs then gives failure probability at most
  (n choose 2) × 2/n^{2+β} < 1/n^β.
- **Lemma 4.1 (Gaussian case).** If r_ij ~ N(0, 1), then for any ε > 0 and
  unit α, Pr[‖f(α)‖² > 1 + ε] < exp(−(k/2)(ε²/2 − ε³/3)) and
  Pr[‖f(α)‖² < 1 − ε] < exp(−(k/2)(ε²/2 − ε³/3)). Here
  ‖f(α)‖² ~ χ²(k)/k. Requiring 2 exp(−(k/2)(ε²/2 − ε³/3)) ≤ 2/n^{2+β}
  gives k₀. The paper says the upper-tail bound is tight up to lower-order
  terms, so with a union bound no better k is possible for spherically
  random vectors.
- **Lemma 5.1.** For either distribution, any ε > 0 and unit α, with
  S(α) = Σⱼ (α·c_j)², Pr[S > (1 + ε)k/d] and Pr[S < (1 − ε)k/d] are each
  < exp(−(k/2)(ε²/2 − ε³/3)). Proof by Markov's inequality on the moment
  generating function. Upper tail: h = (d/2) ε/(1 + ε) gives
  ((1 + ε) exp(−ε))^{k/2} (Eq. 11). Lower tail: expanding exp(−hQ²) to
  second order and using E Q⁴ ≤ 3/d², with the same h, which the paper
  calls "not optimal but … good enough", gives
  (1 − ε/(2(1 + ε)) + 3ε²/(8(1 + ε)²))^k exp(ε(1 − ε)k/(2(1 + ε)))
  (Eq. 16), and both are then bounded by series expansion.
- **Lemma 5.2.** For h ∈ [0, d/2), d ≥ 1 and unit α,
  E exp(hQ₁(α)²) ≤ 1/√(1 − 2h/d) (Eq. 4) and E Q₁(α)⁴ ≤ 3/d² (Eq. 5).
- **Lemma 6.1 (worst vector).** With w = (1, …, 1)/√d, for every unit α and
  k = 0, 1, …, E Q(α)^{2k} ≤ E Q(w)^{2k} (Eq. 18). Proof by replacing two
  unequal coordinates α₁, α₂ with c = √((α₁² + α₂²)/2) each and iterating.
- **Lemma 6.2 (Gaussian domination).** With T ~ N(0, 1/d), for all d ≥ 1
  and k = 0, 1, …, E Q(w)^{2k} ≤ E T^{2k} (Eq. 19). It reduces to
  E Y^{2ℓ} ≤ E T₁^{2ℓ} for one coordinate (Eq. 27): 1 for ±1;
  3^{ℓ−1} ≤ (2ℓ)!/(ℓ!2^ℓ) for the sparse distribution.
- **Lemma 6.3 (two-coordinate balancing).** For r₁, r₂ i.i.d. from either
  distribution, a, b ∈ ℝ, c = √((a² + b²)/2), any M and k = 0, 1, …,
  E(M + a r₁ + b r₂)^{2k} ≤ E(M + c r₁ + c r₂)^{2k}. Proved for ±1 by a
  binomial expansion with D_{2j} ≥ 0; the sparse case is omitted. The paper
  states, without proof, that with P(r = 0) > 2/3, a range of three values
  and variance 1, the lemma fails, so "2/3 is tight".
- **Closing remarks (§6).** Since E Y^{2ℓ} < E T^{2ℓ} for some ℓ, both
  inequalities of Lemma 5.1 are strict for each fixed d, giving "a
  correspondingly better bound for k₀". By Jensen's inequality, ±1 entries
  minimize E exp(hQ²) for all h. The paper does not quantify the
  improvement.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | ±1 entries give a JL embedding with k₀ = (4 + 2β)/(ε²/2 − ε³/3) · log n and success probability 1 − n^−β | strong | Theorem 1.1, full proof in §§4–6 |
| C2 | The sparse √3·{+1, 0, −1} distribution (1/6, 2/3, 1/6) gives the same guarantee | moderate | Theorem 1.1; the sparse case of Lemma 6.3 is omitted in this copy |
| C3 | Among unit vectors, (1, …, 1)/√d has the largest even moments of its projection | strong | Lemma 6.1, from Lemma 6.3 |
| C4 | For each fixed d the bound is strictly, though marginally, better than for spherically random vectors | weak | remark after Lemma 6.2; no quantity given |
| C5 | Putting more than 2/3 of the mass at 0 breaks Lemma 6.3 | weak | asserted after Lemma 6.3, no proof |
| C6 | The union-bound k₀ cannot be improved with spherically random vectors | moderate | stated after Lemma 4.1 as tightness of the χ² upper tail "up to lower order terms", not proved here |
| C7 | The projection can be computed in a database with standard SQL aggregates, a third of the attributes per coordinate for the sparse case | moderate | §1.1 description; no implementation or timing |

## Method

1. Draw R (d × k) with independent entries from one of the two
   distributions.
2. Compute E = (1/√k) A R. With the sparse distribution, each new
   attribute is formed by discarding about 2/3 of the attributes at random,
   splitting the rest at random into two parts, summing each, and taking
   the difference (§1.1). The √3 and 1/√k scalings can be applied after
   the multiplication (§4.1).
3. Take row i of E as the image of point i.

## Concepts

- **JL-embedding.** Any embedding with the guarantee of Lemma 1.1 (§1).
- **Database-friendly.** The projection matrix has entries in {−1, 0, +1},
  so the embedding is "a single aggregate over k random partitions of the
  attributes" (abstract).
- **Projection as estimators (§3).** Each column of R is an independent,
  unbiased estimator of the squared length; the projection sums k of them.
  Orthonormality is a nicety, not a requirement.
- **Worst-case vector.** w = (1, …, 1)/√d and its 2ᵈ sign flips, the unit
  vector whose projection has the largest even moments (§3, Lemma 6.1).
- **Randomization as insurance (§1.1).** A random rotation spreads each
  pair's distance over all coordinates, so that sampling k coordinates
  works; the paper likens it to randomizing before Quicksort.

## Connections

It descends from Johnson and Lindenstrauss's lemma
([LIT-1153](../literature.d/LIT-1153.md)) through Frankl and
Maehara, Indyk and Motwani, and Dasgupta and Gupta, whose bound it matches
(§2). It cites applications to low-rank approximation (Papadimitriou et
al.), approximate nearest neighbours (Indyk and Motwani; Kleinberg),
clustering (Schulman), data streams (Indyk), learning halfspaces (Vempala)
and mixtures of Gaussians (Dasgupta; Arora and Kannan). The proof
structure, one fixed vector's tail times a union bound over the family, is
the one [QUESTION-120](../questions.d/QUESTION-120.md) attributes
to Baraniuk et al. ([LIT-1156](../literature.d/LIT-1156.md)) for
sparse supports. This copy does not cite Baraniuk et al., who came later.

## Bearing on the record

**[QUESTION-120](../questions.d/QUESTION-120.md).**

- **The general shape.** The paper reduces the whole task to one
  inequality for a fixed vector (Eq. 3) and a union bound over the
  (n choose 2) pairs. So k₀ = (4 + 2β)/(ε²/2 − ε³/3) · log n is
  2 log(n^{2+β}) divided by a function of ε that behaves like ε²/2: the log
  of the number of pairs over the tolerated failure, divided by a squared
  tolerance (my rewriting). This is the clearest instance of the shape
  the question proposes, and the paper says, for the Gaussian case, that
  the χ² upper tail makes it tight as long as a union bound is used.
- **The ensemble is not the explanation by itself.** The paper shows the
  guarantee does not depend on spherical symmetry, only on concentration,
  and isolates what it does depend on: zero mean, unit variance,
  independence, and sub-Gaussian even moments. That supports the
  question's "the shared tool is real" for any map with such entries.
- **Expand and threshold.** The question's counter-argument holds up, and
  this paper sharpens it. Theorem 1.1 places no condition on k against d,
  so an expanding signed ±1 map would keep distances too (my observation).
  But neither the fly's map nor SDM's is the paper's object. The fly's
  matrix is binary {0, 1}, nonnegative, with about six of fifty entries
  nonzero per row ([LIT-1158](../literature.d/LIT-1158.md)), so
  its entries have nonzero mean, and over 2/3 of them are zero, the level
  at which the paper says its Lemma 6.3 fails. SDM's address matrix is
  dense, uniform ±1 ([NOTE-779](NOTE-779.md)); it is the first Achlioptas
  ensemble, but what SDM keeps is the set of addresses within a Hamming
  radius after a threshold, and the paper says nothing about thresholds.
- **Random features and superposition.** The paper does not touch either.
  It neither supports nor weakens the question's claim that 2N = n counts
  something else.

**Checked against the text.**

- The LIT's k₀ = (4 + 2β)/(ε²/2 − ε³/3) · log n, success probability
  1 − n^−β, and the two distributions are correct (Theorem 1.1).
- The LIT says the two distributions "give the same guarantee as a
  Gaussian matrix". Correct; the paper adds that for each fixed d the
  bound is marginally better.
- The LIT says the sparse distribution "costs a third of the additions".
  The paper says "a threefold speedup, as we only need to process a third
  of all attributes for each of the k coordinates". That is in expectation;
  the paper does not count additions.
- The LIT's Standing says the paper is "the step from a rotation to a
  sparse random matrix of small integers, which is the form random
  projections take in the fly olfactory circuit … and in sparse
  distributed memory". Imprecise twice. The sparse distribution is only
  2/3 zeros and signed with mean zero; the paper says 2/3 is the most its
  lemma allows. The fly's matrix is sparser and nonnegative, and SDM's is
  dense ±1. The paper's step is from spherical symmetry to independent
  zero-mean, unit-variance entries with sub-Gaussian moments.
- The QUESTION says "the sparse binary matrices of the fly and of SDM are
  the ensembles Achlioptas shows keep the JL guarantee". Wrong as stated.
  The paper's ensembles are signed ±1 and √3·{+1, 0, −1} at density 1/3.
  The fly's {0, 1} matrix with about 12% density is outside both and
  outside Lemma 6.3. SDM's address matrix is the dense ±1 ensemble, not a
  sparse one. The paper proves nothing about thresholded outputs.
- The QUESTION's "ε⁻² log n for keeping the distances of n points" agrees
  with the paper in order; the paper's exact constant is the k₀ above.
- The LIT's title carries the JCSS subtitle "Johnson-Lindenstrauss with
  binary coins", which this copy lacks. The copy gives no journal, volume,
  pages or date, so the LIT's bibliography could not be checked against it.

No THEORY is filed from this reading. It carries no instruction for
machine-learning practice; its database recipe is practice for databases.

## Limitations

- This copy is a pre-publication draft. The JCSS text may differ in
  numbering, constants or proofs, and may include the omitted sparse case
  of Lemma 6.3.
- The sparse case of Lemma 6.3 is not proved in this copy, and the claim
  that 2/3 is tight is unproved.
- The "strictly better" bound for fixed d is not quantified.
- No experiments, implementation or timing support the database claims.
- The paper states that randomness is reduced but notes the amount
  "is still quite large"; it gives no count.
- The sparse recipe in §1.1 splits the kept attributes into "two equal
  parts". My observation: with independent signs the parts are equal only
  in expectation.

## Open questions

- How sparse a zero-mean matrix can be before the JL guarantee, not just
  Lemma 6.3, fails. The paper leaves the 2/3 limit tied to its own proof.
- Whether a nonnegative {0, 1} matrix, after centring, satisfies the
  paper's conditions, and what the fly's top-5% threshold keeps in place of
  distances. That is the third thread of
  [QUESTION-120](../questions.d/QUESTION-120.md), and this paper
  does not reach it.
