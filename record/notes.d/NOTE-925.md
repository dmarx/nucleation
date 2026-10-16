---
number: 925
status: Read
formerly:
- NOTE-tmp4mti8
paper: LIT-1154
title: 'Larsen & Nelson — optimality of the Johnson–Lindenstrauss lemma'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF, 1609.02094v2 of 9 November 2017 (9
    pages, the version with the simplified argument for small d credited to
    Oded Regev), fetched from arxiv.org/pdf/1609.02094 and extracted with
    pdftotext -layout: abstract, §1 with §§1.1–1.2, §2, §3 and §3.1, and the
    acknowledgments. Pages 1, 4 and 6 were re-extracted without -layout
    where formulas were garbled. Figure 1 was read from its caption and the
    text that uses it. The reference list was scanned. Two expressions
    stay partly garbled and are flagged where used: the binomial in the
    Welch bound and the first step of the count of |P| in the Analysis
    paragraph.
date: '2026-10-14'
summary: >-
  For n, d ≥ 2 and lg^0.5001 n / √min{n, d} < ε < 1 there is an n-point set
  in R^d such that every map into R^m, linear or not, that keeps all squared
  distances within 1 ± ε needs m = Ω(ε⁻² lg(ε²n)), which is Ω(ε⁻² lg n) once
  ε > 1/min{n, d}^0.4999. So the Johnson–Lindenstrauss bound is optimal up
  to a constant, and the distributional lemma plus a union bound is the best
  route. The proof is an encoding argument over k-sparse point sets with
  k = ε⁻²/256, and the count it ends on is m = Ω(k lg(d/k)).
---

# NOTE-925: Larsen & Nelson — optimality of the Johnson–Lindenstrauss lemma

## Contribution

Before this paper the Johnson–Lindenstrauss bound m = O(ε⁻² lg n) was known
to be optimal only against linear maps ([LN16], same authors), and only for
n between about d^{1+γ}/ε² and poly(d). Against arbitrary maps the best lower
bound was Ω(ε⁻² lg n / lg(1/ε)) (Welch, Levenshtein, Alon). This paper
removes the lg(1/ε) gap for arbitrary maps over nearly the whole range of ε.
After it, no embedding of any kind beats the lemma by more than a constant
on worst-case inputs, and the paper concludes that obtaining (1) by the
distributional lemma and a union bound is optimal.

## Key insight

A low-dimensional embedding that keeps squared distances to within 1 ± ε
for a set containing 0, the basis vectors e₁ … e_d and a k-sparse vector
y_S also keeps the inner products ⟨e_j, y_S⟩ to within ±4ε. If the entries
of y_S are 16ε, the support S can be read off the embedding. So the
embedding must carry the information in the supports, which is about
kn lg(d/k) bits for n points. The embedded points can be written down in
O(nm) bits, because the images of the y_S lie in an m-dimensional subspace
and only need to be located to ε in the ℓ∞ norm, at a constant number of
bits per dimension. Counting gives m = Ω(k lg(d/k)), and with k ≈ ε⁻² that
is the Johnson–Lindenstrauss order. Previous hard sets were nearly
orthogonal, and nearly orthogonal sets can be beaten by codes; this one is
not.

## Assumptions

- **The guarantee is on squared distances.** (1): (1 − ε)‖x − y‖₂² ≤
  ‖f(x) − f(y)‖₂² ≤ (1 + ε)‖x − y‖₂² for all x, y ∈ X. Conjecture 1 phrases
  the same thing as "distortion at most 1 + ε".
- **The map is arbitrary.** f : X → R^m need only satisfy (1) on X. It may
  depend on X, and need not be linear, continuous or random.
- **The range of ε.** Theorem 2 needs integers n, d ≥ 2 and
  ε ∈ (lg^0.5001 n / √min{n, d}, 1). The abstract states the simpler form
  1/(min{n, d})^0.4999 < ε < 1, where the bound reads Ω(ε⁻² lg n). Some
  restriction of this kind is necessary: the identity, or projection onto
  span(X), gives m ≤ min{n, d}, so the bound cannot hold for
  ε = o(1/√min{n, d}).
- **Worst case, by existence.** The theorem says some n-point set needs that
  many dimensions. It says nothing about typical or structured inputs.
- **Constants are not tracked.** The construction uses k = ε⁻²/256, and the
  bound is stated in Ω only.

## Key results

- **Theorem 1 (the JL lemma, as the paper states it).** For any X ⊂ R^d of
  size n and ε ∈ (0, 1/2) there is f : X → R^m with m = O(ε⁻² lg n)
  satisfying (1).
- **Lemma 1 (distributional JL).** For any d ≥ 1 and 0 < ε, δ < 1/2 there is
  a distribution D_{ε,δ} over m × d matrices with m ≲ ε⁻² lg(1/δ) such that
  for all u ∈ R^d, P_{Π∼D_{ε,δ}}(|‖Πu‖₂ − ‖u‖₂| > ε‖u‖₂) < δ (3). As
  printed, (3) is on norms, not squared norms (checked against the word
  positions in the PDF). The JL lemma follows with δ < 1/C(n, 2) and a union bound over the difference
  vectors. The paper cites [JW13, KMN11] for tightness of this lemma: any
  such distribution needs m = Ω(min{d, ε⁻² lg(1/δ)}).
- **Theorem 2 (main).** For any integers n, d ≥ 2 and
  ε ∈ (lg^0.5001 n / √min{n, d}, 1) there is X ⊂ R^d with |X| = n such that
  any f : X → R^m providing (1) has m = Ω(ε⁻² lg(ε²n)) (2). The abstract
  states it as m = Ω(ε⁻² lg n) for 1/(min{n, d})^0.4999 < ε < 1.
- **Upper bound it matches.** m = O(min{n, d, ε⁻² lg n}).
- **Conjecture 1.** The smallest m such that every n-point subset of ℓ₂^d
  embeds into ℓ₂^m with distortion at most 1 + ε is
  Θ(min{n, d, ε⁻² lg(2 + ε²n)}) for all n, d > 1 and 0 < ε < 1. Note
  lg(2 + ε²n), not lg n, near the small-ε end.
- **Prior bounds, as the paper reports them.** [JL84]: Ω(lg n) for ε < 1/2.
  [Lev83, Alo03]: Ω(min{n, ε⁻² lg n / lg(1/ε)}). The Welch bound
  ε^{2k} ≥ (1/(n − 1))(n / C(m + k − 1, k) − 1) gives the same with
  2k = ⌈lg n / lg(1/ε)⌉ (the binomial is garbled in extraction; I read it as
  C(m + k − 1, k)). The lower bound extends to n ≤ e^{cε²d}.
- **Incoherence is weaker.** A set is ε-incoherent if its vectors are unit
  and |⟨x, y⟩| = O(ε) for x ≠ y. For ε < 2^{−ω(√lg n)}, an incoherent set of
  n vectors exists in m = o(ε⁻² lg n) dimensions, by Reed–Solomon codes.
  Hard sets built from nearly orthogonal vectors therefore cannot prove
  Theorem 2.
- **Lemma 2 and Corollary 1 (covering).** The unit ball of an m-dimensional
  normed space, and any origin-symmetric convex body T in R^m, can be
  covered by at most 2^{m lg(1 + 2/ε)} translates of εB (resp. εT), for
  0 < ε < 1.
- **Lemma 3.** For every e_j and y_{S_ℓ} in the hard set,
  |⟨f̂(e_j), f(y_{S_ℓ})⟩ − ⟨e_j, y_{S_ℓ}⟩| ≤ 6ε, where f̂(e_j) is f(e_j)
  rounded to a net point within ε. (±2ε from rounding, since
  ‖f(y)‖₂ ≤ 2, and ±4ε from (1) on unit vectors.)
- **The count (Analysis, §3).** The encoding takes
  dm lg(1 + 4/ε) + O(Qm) = O(nm) bits, with Q = n − d − 1 and
  d = n/lg(1/ε). The family has |P| = C(d, k)^Q ≥ (d/(2k))^{kQ} ≥
  (d/(2k))^{kn/2} (the first step is garbled in extraction). Hence
  nm = Ω(kn lg(d/k)), so m = Ω(ε⁻² lg(ε²n / lg(1/ε))), which simplifies to
  Ω(ε⁻² lg(ε²n)) under the assumed range of ε.
- **A sub-optimal first attempt.** Encoding every image to ε in ℓ₂ costs
  m lg(1/ε) bits per point and gives only
  Ω(ε⁻² lg(ε²n / lg(1/ε)) / lg(1/ε)), "roughly recovering" Alon's bound.
- **Subsequent work (§1.2).** Alon and Klartag [AK17] give an alternative
  proof through the space complexity of storing approximate inner
  products, prove the lower bound of Conjecture 1 for all parameters
  (removing the lg^0.5001 n condition), and prove a bipartite version of its
  upper bound with m = O(ε⁻² lg(2 + ε²n)). The paper notes that additive-ε
  inner-product preservation does not imply relative 1 + ε distance
  preservation when distances are small.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Some n-point set in R^d needs m = Ω(ε⁻² lg(ε²n)) under any map keeping squared distances within 1 ± ε, for ε ∈ (lg^0.5001 n/√min{n,d}, 1) | strong | Theorem 2, complete proof in §3 and §3.1 |
| C2 | The JL lemma is optimal up to a constant against all maps, for ε > 1/min{n,d}^0.4999 | strong | abstract; C1 with lg(ε²n) = Θ(lg n) in that range |
| C3 | Obtaining (1) by the distributional lemma and a union bound is optimal | strong | §1.1, from Theorem 2 and the bound it matches |
| C4 | Nearly orthogonal (incoherent) sets cannot be the hard instance, since codes embed them below ε⁻² lg n for small ε | moderate | §1, cited to [AGHP92, NNW14]; not proved here |
| C5 | The optimal dimension is Θ(min{n, d, ε⁻² lg(2 + ε²n)}) | conjecture | Conjecture 1; lower bound later proved by [AK17], as reported in §1.2 |

## Method

1. Fix d = n/lg(1/ε) and k = ε⁻²/256. For S ⊂ [d] with |S| = k, let
   y_S = Σ_{j∈S} e_j / √k, so ⟨y_S, e_j⟩ is 16ε on S and 0 off it.
2. The family P is every sequence (0, e₁, …, e_d, y_{S₁}, …, y_{S_Q}) with
   Q = n − d − 1. Any f satisfying (1) on one of them may be taken with
   f(0) = 0, so it keeps norms, and keeps ⟨e_j, y_S⟩ to within ±4ε, leaving
   a gap of 8ε.
3. Encode f(e_j) to ε in ℓ₂ by a fixed net of (1 + ε)B₂^m: m lg(1 + 4/ε)
   bits each, affordable because there are only d = n/lg(1/ε) of them.
4. Let A be the d × m matrix with rows f̂(e_j), W its column space and
   T = B_∞^d ∩ W. Each A f(y_{S_ℓ}) lies in (22ε)T by Lemma 3. Cover (22ε)T
   by at most 2^{m lg 45} translates of εT, chosen deterministically from T,
   and record the index: O(m) bits per y.
5. Decode: rebuild A, then T, then the cover. The recovered centre c is
   within 7ε of ⟨e_j, y_S⟩ in every coordinate, so its entries are ≤ 7ε off
   S and ≥ 9ε on S, and S is recovered.
6. Injectivity gives O(nm) ≥ lg |P| = Ω(kn lg(d/k)).
7. Other d. For d > n/lg(1/ε), use only the first n/lg(1/ε) basis vectors.
   For d < n/lg(1/ε), first apply a JL map from dimension n/lg(1/ε) to d,
   which costs a factor 1 + O(√(lg n / d)) = 1 + o(ε) under the range
   assumed; a better embedding from d would then contradict the case
   already proved. The paper credits this simplification to Oded Regev.

## Concepts

- **JL guarantee (1).** Two-sided relative error on squared Euclidean
  distances, for all pairs of a fixed set.
- **Distributional JL (DJL).** A data-oblivious random linear map that keeps
  any one vector's norm to within a factor 1 ± ε, with failure probability
  δ.
- **ε-incoherent.** Unit vectors with pairwise |⟨x, y⟩| = O(ε).
- **Encoding argument.** A lower bound proved by showing that a too-good
  embedding would give an injective map from a large family into too few
  bit strings.
- **Covering by εT.** Translates of a scaled convex body; the count depends
  on the body's dimension, not on the ambient d.

## Connections

It completes the authors' linear-map lower bound [LN16] and supersedes the
bounds of Welch, Levenshtein and Alon for ε = o(1). It reads the original
Johnson–Lindenstrauss proof as a random projection, a uniformly random
rotation followed by projection to m coordinates and scaling by 1/√m, which
is linear and oblivious to the data ([LIT-1153](../literature.d/LIT-1153.md)). Tightness of the
distributional lemma is cited to Jayram–Woodruff and Kane–Meka–Nelson, not
proved here. Alon and Klartag's later work is described as an independent
route through ε-nets of rank-d Gram matrices under the entrywise ℓ∞ norm.
The paper lists compressed sensing among applications of dimensionality
reduction but makes no connection between the two thresholds. It does not
mention random features, kernels, expansion to higher dimension, or
thresholding.

## Bearing on the record

- **[QUESTION-120](../questions.d/QUESTION-120.md), the distance thread.** The question's sentence
  "the bound is tight" holds, with three conditions it leaves out. Tightness
  is up to a constant, and the constant is untracked (k = ε⁻²/256). It
  holds only for ε above about 1/√min{n, d}; below that the bound is
  min{n, d}, and the paper conjectures lg(2 + ε²n) in place of lg n near
  that end. And it is a worst case over point sets, shown by existence. So
  ε⁻² lg n is the right order for the worst set, not a sharp threshold in
  the sense of a phase transition, and the paper gives nothing to set
  beside the Donoho–Tanner curve at fixed (δ, ρ).
- **The question's proposed shape.** The question guesses each threshold
  is "the log of the size of the family a map must hold, divided by a
  squared tolerance". The paper supports this for distances from two sides.
  The upper bound is the distributional lemma with δ < 1/C(n, 2) and a union
  bound, which is exactly that shape, and C3 says the shape cannot be beaten.
  The lower bound is itself a log-count: nm ≥ lg |P|.
- **The superposition thread (my observation).** The hard instance is a
  family of k-sparse vectors with k ≈ ε⁻², and the count the proof ends on
  is m = Ω(k lg(d/k)). That is the form of the compressed-sensing bound
  m = Ω(k log(n/k)) in [NOTE-278](../notes.d/NOTE-278.md). In this proof the JL order arises as
  a sparse-support count with sparsity set by the tolerance. The paper does
  not say this. It is a reason to expect the Baraniuk et al. reduction
  ([LIT-1156](../literature.d/LIT-1156.md)) to be the general shape for the first two uses.
- **Also on superposition.** The paper states that ε-incoherent sets, unit
  vectors with pairwise |⟨x, y⟩| = O(ε), fit in m = o(ε⁻² lg n) dimensions
  when ε < 2^{−ω(√lg n)}. Superposition is described in [NOTE-278](../notes.d/NOTE-278.md) as
  features at almost-orthogonal angles. So the JL lower bound is not the
  bound on how many almost-orthogonal directions fit in m dimensions. The
  question should not use it that way.
- **The random-features thread.** Nothing. The paper does not treat random
  features, kernels, generalization or training samples. It supports the
  question's point that keeping distances is a different requirement from
  interpolating well only by showing what the JL guarantee is: a fixed
  set's pairwise squared distances.
- **The expand-and-threshold thread.** Nothing directly. The bound is vacuous
  when m ≥ min{n, d}, since the identity works. For maps that go up in
  dimension, as the fly's does, the lower bound places no constraint.
- **Checks of the current LIT and the QUESTION against the text.**
  - LIT summary, "for every d, n and ε within the lemma's range": wrong.
    The lemma's range is ε ∈ (0, 1/2) (Theorem 1). The lower bound holds
    for ε ∈ (lg^0.5001 n/√min{n, d}, 1) (Theorem 2), or
    1/min{n, d}^0.4999 < ε < 1 in the abstract's form. It does not hold for
    small ε, and extends past 1/2.
  - LIT summary, "need Ω(ε⁻² log n) dimensions": imprecise. Theorem 2
    states Ω(ε⁻² lg(ε²n)); it equals Ω(ε⁻² lg n) only in the abstract's
    range.
  - LIT summary, "with distortion 1 + ε": imprecise. The guarantee is on
    squared distances, (1 − ε)‖x − y‖₂² ≤ ‖f(x) − f(y)‖₂² ≤ (1 + ε)‖x − y‖₂².
  - LIT takeaway "Tight", "keeping distances within 1 ± ε": as above,
    squared distances. "whenever ε is not too small relative to n and d"
    is correct; the exact condition is Theorem 2's.
  - LIT takeaway "no cleverer nonlinear map beats a random projection on
    worst-case inputs": correct up to a constant factor, which should be
    said. The paper's own form is that the DJL lemma plus a union bound is
    optimal.
  - LIT Standing, "what makes ε⁻² log n a threshold rather than an upper
    bound": imprecise. It makes ε⁻² lg n a matching lower bound, up to an
    unstated constant, for a worst-case set. It is not a threshold in the
    phase-transition sense the question uses for Donoho–Tanner.
  - QUESTION, "the bound is tight": correct in order, with the conditions
    above.
  - Bibliography. The copy read is v2, dated 9 November 2017; the copy
    itself does not state the FOCS 2017 venue, so that detail in the LIT
    could not be checked against it. The arXiv category is cs.IT. The
    copy's title is "Optimality of the Johnson-Lindenstrauss lemma". The
    LIT's `published:` 2016-09-07 (v1) is not contradicted by the copy.
- **For the anthology.** No instruction for machine-learning practice.

## Limitations

- Worst case only, and by existence. The hard set is explicit, but nothing
  is said about the dimension needed for typical data or for low intrinsic
  dimension.
- Constants are not given. The construction's k = ε⁻²/256 suggests the
  hidden constant is small.
- The range of ε leaves a gap near 1/√min{n, d}, by a lg^0.5001 n factor.
  The paper reports that [AK17] closes it for the lower bound.
- Only Euclidean target and source, and only the two-sided relative
  guarantee on squared distances. Additive inner-product preservation is a
  different problem, which [AK17] treats.
- Two small slips in the copy: the decoding paragraph writes "j ∉ S_i" for
  j ∉ S_ℓ, and the JL map in the small-d case is said to preserve distances
  to 1 + O(√(lg n/d)) with no stated failure probability, which is
  harmless since only existence is needed.

## Open questions

- Conjecture 1: whether the optimal dimension is
  Θ(min{n, d, ε⁻² lg(2 + ε²n)}) in full; the paper reports the lower bound
  done by [AK17] and the upper bound open beyond a bipartite version.
- For the record (my question): whether the sparse-support count in this
  proof, m = Ω(k lg(d/k)) with k ≈ ε⁻², and the compressed-sensing bound
  of [NOTE-278](../notes.d/NOTE-278.md) are one counting argument. Reading Baraniuk et al.
  ([LIT-1156](../literature.d/LIT-1156.md)) and Do Ba–Indyk–Price–Woodruff would settle it.
