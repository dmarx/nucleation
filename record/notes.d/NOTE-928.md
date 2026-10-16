---
number: 928
status: Read
formerly:
- NOTE-tmpetxcq
paper: LIT-1155
title: 'Linial, London & Rabinovich — the geometry of graphs'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from a 26-page PDF hosted on a Michigan State University
    course page (users.math.msu.edu/users/iwenmark/Teaching/CMSE890/),
    produced by Ghostscript in 2007. It is the authors' own typescript, not
    the Combinatorica typesetting: letter-size pages numbered 1–26, no
    journal header, pagination or received dates, while the journal
    version runs 31 pages (215–245). The text calls itself the "final
    version of February 1995", lists what was added after the FOCS '94
    version, and has the journal's title, authors and reference list, so it
    is the accepted manuscript. Page numbers below are the typescript's;
    whether the theorem numbers match the journal's was not checked. The
    text layer was extracted with pdftotext -layout. The display
    mathematics was garbled, so pages 1, 4–9, 11–14, 17, 19 and 22 were
    also read from page images (pdftoppm), and every expression below is
    taken from the images. Read in full: the abstract, §§1–2, §3 (Theorems
    3.1–3.2 with the proof of Claims 1–5, Lemma 3.3, Corollaries 3.4–3.8),
    §4 (Theorem 4.1, Proposition 4.2, two commodities), §6 (Theorem 6.1,
    Lemmas 6.3–6.4) and §8. §5 (isometric dimensions) and §7
    (low-diameter decompositions) were read statement by statement, with
    their proofs followed in outline. The reference list was read. To
    check NOTE-679's citation, the citing passage of Sala et al.
    (arXiv:1804.03329v2) was also fetched and read.
date: '2026-10-16'
summary: >-
  Every n-point metric embeds in ℓ₂ with distortion O(log n) in O(log n)
  dimensions (Theorem 3.2(1), attributed to Bourgain). The paper reproves
  the distortion bound by a randomized Bourgain-style construction into
  ℓ_p^{O(log² n)}, and it gets the dimension from Johnson–Lindenstrauss.
  Every embedding of a constant-degree expander into ℓ_p, 1 ≤ p ≤ 2, of
  any dimension, has distortion Ω(log n) (Proposition 4.2), so the bound
  is tight. The lower bound comes from Leighton and Rao's flow–cut gap,
  and the same embeddings give an O(log k) max-flow/min-cut gap for k
  commodities.
---
<!-- inactive-ok-file: LIT-1161 — Unavailable; Bourgain's paper, read here only as this paper states it -->

# NOTE-928: Linial, London & Rabinovich — the geometry of graphs

## Contribution

The paper treats the shortest-path metric of a graph as a finite metric
space and asks how well it embeds into a normed space, both in distortion
and in dimension. It turns Bourgain's O(log n) embedding into ℓ₂ into a
randomized polynomial-time algorithm, and it finds the least Euclidean
distortion c₂(X) of any finite metric by semidefinite programming. It
proves that constant-degree expanders need distortion Ω(log n) in ℓ₂, so
Bourgain's bound cannot be improved. It also shows that the max-flow/min-cut
gap of a multicommodity flow problem is at most the ℓ₁ distortion of one
metric derived from the flow problem's LP dual, which gives an O(log k)
gap for k commodities with a deterministic algorithm. Isometric dimension
results for trees, cliques, cycles and cubes, a separator theorem and
low-diameter decompositions for low-dimensional graphs make up the rest.

## Key insight

A metric that embeds into ℓ₁ is a nonnegative combination of cut metrics.
So any ratio that is linear in the distances is minimized over ℓ₁ metrics
at a single cut. The max-flow LP dual minimizes such a ratio over all
metrics, and cuts bound it from above. The gap between the two is
therefore at most the distortion with which the optimal metric embeds
into ℓ₁. Read in the other direction, a graph with a large flow–cut gap,
such as an expander, cannot embed into ℓ₁ with small distortion, nor into
ℓ₂, which embeds into ℓ₁.

## Assumptions

- **Distortion (Definition 2.1, p. 4).** An embedding φ of (X, d) into a
  normed space has distortion ≤ c if d(x₁, x₂) ≥ ‖φ(x₁) − φ(x₂)‖ ≥
  (1/c)·d(x₁, x₂) for all pairs. dim_c(X) is the least dimension of a
  normed space admitting such an embedding, and dim(X) = dim₁(X). c_p(X)
  is the least distortion into ℓ_p of any dimension. The paper allows
  semi-metrics (footnote 1).
- **Graphs.** G is connected, possibly weighted, with its shortest-path
  metric; n is the number of vertices or points. In §5 logarithms are to
  base 2.
- **Expanders.** "Constant-degree expander" is used without a definition.
  The proof of Proposition 4.2 needs only that its min-cut ratio is
  Ω(1/n) and that Σ_{i≠j} d_{i,j} is of order n² log n (my reading of the
  Φ = Θ(1/(n log n)) step).
- **Algorithms.** "Random polynomial time" means the embedding succeeds
  with high probability. Theorem 3.2(2) assumes the distance between any
  two points can be evaluated in unit time (§3.2).
- **Results imported without proof.** The Johnson–Lindenstrauss lemma
  (Theorem 3.1); the embedding of ℓ₂ᵐ in ℓ_p^{2m}, 1 ≤ p ≤ 2, with constant
  distortion, and the √d approximation of any d-dimensional norm by an
  ellipsoid (both from Pisier's book, [52]); Lemma 3.3 (from Berger,
  [10]); and the Ω(log n) flow–cut gap on expanders (Leighton and Rao,
  [37]).

## Key results

- **Theorem 3.1 (p. 6), quoted.** "(Johnson–Lindenstrauss [31], see also
  [21]) Any set of n points in a Euclidean space can be mapped to ℝᵗ where
  t = O(log n/ε²) with distortion ≤ 1 + ε in the distances. Such a mapping
  may be found in random polynomial time." The rough sketch: orthogonal
  projection onto a random t-dimensional subspace, "because the length of
  the image of a unit vector under a random projection is strongly
  concentrated around √(t/n)". No constants are given.
- **Theorem 3.2 (p. 6).** Six claims.
  1. "(Bourgain [12], see also [32], [48]). Every n-point metric space
     (X, d) can be embedded in an O(log n)-dimensional Euclidean space with
     an O(log n) distortion."
  2. A deterministic polynomial-time algorithm embeds (X, d) in Euclidean
     space with distortion < c₂(X) + ε, for every ε > 0. In random
     polynomial time it embeds in ℓ₂^{O(log n)} with distortion O(c₂(X)).
     The overview (p. 4) states this as ≤ (1 + ε)·c₂(X).
  3. In random polynomial time, into ℓ_p^{O(log n)}, 1 ≤ p ≤ 2, with
     distortion O(c₂(X)).
  4. In deterministic polynomial time, into ℓ_p^{O(n²)}, 1 ≤ p ≤ 2, with
     distortion O(c₂(X)).
  5. In random polynomial time, into ℓ_p^{O(log² n)}, p > 2, with
     distortion O(log n).
  6. "Every embedding of an n-vertex constant-degree expander into an l_p
     space, 2 ≥ p ≥ 1, of any dimension, has distortion Ω(log n)."
- **How Claim 1 is proved.** The paper says it "appears mostly for future
  reference, but is seen to be an immediate corollary of Claims 3 and 5
  and Theorem 3.1". The working route is Claim 5's construction, whose
  proof covers every p ≥ 1, taken at p = 2, followed by Theorem 3.1. The
  O(log n) distortion is proved in the paper. The O(log n) dimension comes
  from Johnson–Lindenstrauss, applied to the O(log² n)-dimensional image
  (my reading; the paper attributes both to Bourgain).
- **Claim 5's proof (pp. 7–8), the paper's version of Bourgain's
  construction.** For each power of two below n, pick O(log n) random
  subsets A of that size, and map x to the vector of d(x, A) =
  min_{y∈A} d(x, y). For a pair x ≠ y, ρ_t is the least radius at which
  both balls hold at least 2ᵗ points, for ρ_t < d(x, y)/4, and
  ρ_{t̂+1} = d(x, y)/4. A random set of size Θ(n/2ᵗ) hits B(y, ρ_{t−1}) and
  misses the open ball B°(x, ρ_t) with constant probability, giving
  |d(x, A) − d(y, A)| ≥ ρ_t − ρ_{t−1}. With q = O(log n) sets per size, at
  least q/10 do so with high probability. Over all Q = O(log² n) sets,
  Σ|d(x, Aᵢ) − d(y, Aᵢ)| ≥ (log n/10)·ρ_{t̂+1} ≥ log n·d(x, y)/40, and each
  term is at most d(x, y), so the sum is at most C·log² n·d(x, y). Mapping
  x to (d(x, Aᵢ)/Q^{1/p}) gives τ(x, y) ≤ d(x, y) ≤ O(log n·τ(x, y)) "by the
  monotonicity of p-th moment averages". The constant success probability
  and the high-probability count are asserted, not computed.
- **Claim 2's proof (pp. 6–7).** With A = MMᵗ for a distortion-c embedding
  M, (1/c²)d²_{i,j} ≤ a_{i,i} + a_{j,j} − 2a_{i,j} ≤ d²_{i,j}, A positive
  semidefinite. The ellipsoid algorithm finds c to within ε, and Theorem
  3.1 reduces the dimension to O(log n).
- **Claims 3–4.** ℓ₂ᵐ embeds in ℓ_p^{2m} with constant distortion for
  1 ≤ p ≤ 2; "it is enough to map ℓ₂ᵐ isometrically into a random
  m-dimensional subspace of ℓ_p^{2m}" (from [52]). The deterministic
  version uses **Lemma 3.3 (p. 7)**: for a 4-wise independent family
  F ⊂ {−1, +1}ᵐ, x ∈ ℝᵐ and 1 ≤ p ≤ 2,
  ‖x‖₂ ≤ ((1/|F|) Σ_{εᵢ∈F} |⟨x, εᵢ⟩|ᵖ)^{1/p} ≤ √3‖x‖₂, with explicit F of
  O(m²) vectors. Also c₁(X) ≤ c₂(X).
- **Corollary 3.4 (p. 8).** For Y ⊆ X, a randomized algorithm gives
  φ: X → ℓ₁^{O(log² |Y|)}, non-expanding, with ‖φ(x) − φ(y)‖ ≥
  Ω(1/log |Y|)·d(x, y) on Y. For k pairs (sᵢ, tᵢ), a deterministic
  algorithm gives φ into ℓ₁^{O(n²)} with ‖φ(sᵢ) − φ(tᵢ)‖ ≥
  Ω(1/log k)·d(sᵢ, tᵢ).
- **Corollary 3.5 (p. 9).** (X, d) embeds in Euclidean space with
  distortion ≤ c if and only if, for every positive semidefinite Q with
  Q·1⃗ = 0⃗, Σ_{q_{i,j}>0} q_{i,j}d²_{i,j} + c² Σ_{q_{i,j}<0} q_{i,j}d²_{i,j} ≤ 0.
  By Bourgain, this holds for every metric with c = O(log n). The proof is
  by convex duality.
- **Corollary 3.8 (p. 10).** For every n-point metric there is γ > 0 such
  that γ·d embeds in a Hamming space with distortion O(log n), and this is
  tight. The proof rounds ℓ₁ coordinates to integers at arbitrarily small
  cost and writes a coordinate of value s, out of a maximum r, as s ones
  followed by r − s zeros, an isometry.
- **Theorem 4.1 (p. 11).** A deterministic polynomial-time algorithm,
  given a network and demands for k source–sink pairs, finds S ⊂ V with
  Cap(S)/Dem(S) ≤ O(log k)·maxflow. The proof embeds the LP-optimal metric
  by Corollary 3.4(2), picks the best coordinate, and makes it 0/1 by a
  variational argument. The result for non-unit demands is said to be new.
  Footnote 2 notes a randomized version in the FOCS paper and in Aumann
  and Rabani, and a derandomization by Garg.
- **Proposition 4.2 (p. 12).** "Every embedding of an n-vertex constant
  degree expander into an l_p space, 2 ≥ p ≥ 1, of any dimension, has
  distortion Ω(log n). The metric space of such a graph cannot be embedded
  with constant distortion in any normed space of dimension o(log² n)."
  Proof: for Φ = Σ_{[i,j]∈E} d_{i,j} / Σ_{i≠j} d_{i,j}, the expander's own
  metric gives Φ = Θ(1/(n log n)), while every cut metric, hence every ℓ₁
  metric, gives Ω(1/n). This is the Ω(log n) flow–cut gap "observed in
  [37]". ℓ_p for 1 ≤ p ≤ 2 embeds in ℓ₁ with constant distortion, which
  covers ℓ₂. For the dimension clause, any d-dimensional norm is within √d
  of an ellipsoid, so constant distortion in o(log² n) dimensions would
  give o(log n) in ℓ₂.
- **Two commodities (p. 12).** Max-flow equals min-cut, via the ℓ∞² metric
  of distances to the two sources and the rotation (z₁ + z₂)/2,
  (z₁ − z₂)/2, which carries ℓ∞² isometrically to ℓ₁².
- **Isometric dimension (§5, pp. 13–17).** Lemma 5.1: every n-point metric
  embeds isometrically in ℓ∞ⁿ (the Fréchet map). Theorem 5.3: dim(T) =
  O(log n) for every n-vertex tree, and O(log l) for l leaves, tight for
  stars; the proof embeds T isometrically in ℓ∞^{c log n}, c = 1/(log 3 − 1).
  Proposition 5.4: dim(Kₙ) = ⌈log₂ n⌉. Proposition 5.5: degrees in a
  d-dimensional graph are at most 3ᵈ − 1. Lemma 5.6: diam(G) ≥
  ½(n^{1/d} − 1). Theorem 5.7: dim(G) is the least rank of a matrix M with
  max_k |m_{ik} − m_{jk}| = d_G(vᵢ, vⱼ). Theorem 5.8 and Corollary 5.9 on
  complete multipartite graphs; Proposition 5.10: dim(C₂ₘ) = m;
  Corollary 5.12: dim(m-cube) = m; Theorems 5.13–5.15 on stabbing
  dimension and on dim̄, the dimension in ℓ∞, with dim̄(d-cube) = 2^{d−1}.
- **Theorem 6.1 (p. 17).** If dim_c(G) = d and c·d = o(n^{1/d}), G has a
  separator of O(c·d·n^{1−1/d}) vertices leaving no component above
  (1 − 1/(d+1) + o(1))n. Given the embedding, it is found in random
  polynomial time, via a Helly centroid and a random slab.
- **Theorem 7.1 (p. 19).** With d̄ = dim̄_c(G) and d = dim_c(G): d̄ + 1
  blocks of diameter ≤ 2cd̄; d + 1 blocks of diameter ≤ 2cd²; and
  r-subsuming covers by d̄ + 1 (or d + 1) blocks of diameter ≤ (6d̄ + 2)cr
  (or (6d + 2)dcr), of degree ≤ d̄ + 1 (or d + 1). Remark 7.2: with
  Theorem 3.2 this gives O(log n) blocks of diameter O(log³ n), "slightly
  inferior" to the known (O(log n), O(log n)).
- **Section 8 (pp. 20–23).** Proposition 8.1: every directed metric embeds
  isometrically in ℝⁿ under a directed norm. Conjecture 8.2 (with Levin):
  a graph of growth rate ρ is a subgraph of ℤ∞^{O(ρ)}; it is sketched for
  the d-cube by random ±1 projections. Constant-distortion embedding of an
  expander needs Ω(log² n) dimensions, and "It is not impossible" that it
  needs Ω(n). Problems 8.5–8.7, the last asking whether every embedding of
  a graph of minimum degree ≥ 3 in Euclidean space has distortion
  Ω(girth(G)).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every n-point metric embeds in ℓ₂^{O(log n)} with distortion O(log n) | strong | Theorem 3.2(1), attributed to Bourgain; distortion proved by Claim 5's construction, dimension by Theorem 3.1 |
| C2 | A random Bourgain-style map into ℓ_p^{O(log² n)} has distortion O(log n), for any p ≥ 1 | strong | Claim 5's proof, pp. 7–8; probability steps asserted, not computed; the statement says only p > 2 |
| C3 | c₂(X) can be computed to within any ε > 0 in deterministic polynomial time, and has a dual characterization | strong | Claim 2 (SDP and ellipsoid); Corollary 3.5 |
| C4 | Constant-degree expanders need distortion Ω(log n) in ℓ_p, 1 ≤ p ≤ 2, of any dimension, and Ω(log² n) dimensions for constant distortion in any norm | strong | Proposition 4.2, resting on Leighton and Rao's flow–cut gap and two facts from Pisier, all cited |
| C5 | The k-commodity max-flow/min-cut gap is O(log k), with a deterministic algorithm for the cut | strong | Theorem 4.1 |
| C6 | Every n-point metric scales into a Hamming space with distortion O(log n), tight | strong | Corollary 3.8 |
| C7 | Trees have isometric dimension O(log n), tight; dim(Kₙ) = ⌈log₂ n⌉; dim(C₂ₘ) = m; dim(m-cube) = m | strong | §5; Proposition 5.4 is a sketch |
| C8 | Graphs with dim_c(G) = d have separators of O(c·d·n^{1−1/d}) vertices | strong | Theorem 6.1 |
| C9 | Graphs of low dimension have low-diameter decompositions with parameters depending on dimension and distortion only | moderate | Theorem 7.1; the tiling's properties are "not hard to check" |
| C10 | The Bourgain-style embedding gives a principled approach to clustering | weak | §3.2, a remark; the protein test is "work in progress" [38] |

## Method

The Bourgain-style embedding of Claim 5:

1. For each size 2ˡ, l = 1, …, ⌊log n⌋, pick q = O(log n) random subsets
   of that size. Q = O(log² n) sets in all.
2. Map each point x to (d(x, Aᵢ)/Q^{1/p}), i = 1, …, Q.
3. Each coordinate is 1-Lipschitz, so no distance expands.
4. For a pair x, y and a scale t, a set of size about n/2ᵗ separates the
   radii ρ_{t−1} and ρ_t with constant probability. O(log n) sets per
   scale make a tenth of them succeed for every pair at once, and the
   scales sum to d(x, y)/4.
5. Optionally reduce to O(log n) dimensions with Theorem 3.1.

The flow–cut argument of Theorem 4.1:

1. Solve the LP for λ; by duality its optimum is a metric d minimizing
   Σ C_{i,j}d_{i,j} / Σ_μ D_μ d_{s_μ,t_μ}.
2. Embed d into ℓ₁ contracting the k demand pairs by at most O(log k)
   (Corollary 3.4(2)).
3. Take the coordinate with the smallest ratio, and push its values to
   {0, 1} without increasing the ratio. That coordinate is a cut.

## Concepts

- **Distortion ≤ c** — non-expanding, and contracting by at most c
  (Definition 2.1). A two-sided bound, scaled so the upper side is 1.
- **dim_c(X), dim(X)** — the least dimension of any normed space admitting
  a distortion-c, or isometric, embedding. **dim̄(G)** is the same in ℓ∞.
- **c_p(X)** — the least distortion into ℓ_p of any dimension.
- **Cut metric** — d(x, y) = 1 if S separates x and y, else 0. A metric
  embeds in ℓ₁ if and only if it is a nonnegative combination of cut
  metrics (p. 12).
- **Implementing matrix** — M with max_k |m_{ik} − m_{jk}| = d_G(vᵢ, vⱼ);
  its rows are an isometric embedding in ℓ∞ (§5.3).
- **Low-diameter decomposition** — a vertex colouring in which each
  monochromatic connected component has bounded diameter (§7).
- **Growth rate ρ(G)** — max over x, r of log |B(x, r)| / log(r + 1) (§8).

## Connections

The paper's two sources in geometry are Bourgain (1985, [12];
[LIT-1161](../literature.d/LIT-1161.md)) for the O(log n) embedding, and Johnson and Lindenstrauss
(1984, [31]; [LIT-1153](../literature.d/LIT-1153.md)), quoted as Theorem 3.1 with Frankl and Maehara
(1988, [21]) as "see also". Johnson, Lindenstrauss and Schechtman (1987,
[32]) and Matoušek (1992, [48]) are cited beside Bourgain. Its sources in
algorithms are Leighton and Rao (1988, [37]) for the flow–cut gap and the
expander example, Garg, Vazirani and Yannakakis, Klein et al. and Plotkin
and Tardos for the multicommodity results it unifies, Linial and Saks
and Awerbuch and Peleg for low-diameter decompositions, Miller and
Thurston and Miller, Teng and Vavasis for separators, and Goemans and
Williamson and Karger, Motwani and Sudan for the SDP step. Aumann and
Rabani obtained the O(log k) theorem independently.

The paper does not cite Johnson and Lindenstrauss's Problem 4, and it
does not mention Enflo. It says only that the expander bound "closes a
gap left open by Bourgain" (abstract). It does not state what Bourgain's
lower bound was.

## Bearing on the record

- **[THEORY-392](../theory.d/THEORY-392.md) (the Lipschitz extension theorem).** This paper is
  about embedding a metric into ℓ₂, not about extending maps into ℓ₂, and
  it says nothing about L(X, n). It does not touch that account's open
  question, whether K√(log n) is sharp. It does settle the embedding
  question the account's "What this does not say" leaves open, through
  the inference in the next item. The account's mention of "Linial,
  London and Rabinovich (1995) as unchecked" can now cite this NOTE.
- **[NOTE-930](NOTE-930.md)'s unchecked claim.** That NOTE says "Bourgain (1985) gave
  O(log n), and Linial, London and Rabinovich (1995) showed that order is
  needed for expanders, which would answer Problem 4 in the negative."
  Checked against the text, piece by piece.
  - "Bourgain gave O(log n)": confirmed as this paper states it. Theorem
    3.2(1) attributes to Bourgain an embedding of every n-point metric in
    O(log n)-dimensional Euclidean space with O(log n) distortion. Whether
    Bourgain's own paper states the O(log n) dimension cannot be checked
    here. In this paper the dimension comes from Johnson–Lindenstrauss.
  - "LLR showed that order is needed for expanders": confirmed, and the
    result is wider. Proposition 4.2 and Theorem 3.2(6) give Ω(log n) for
    every embedding of an n-vertex constant-degree expander into ℓ_p,
    1 ≤ p ≤ 2, of any dimension. The proof rests on Leighton and Rao's
    Ω(log n) flow–cut gap for expanders, which the paper cites and does
    not reprove.
  - "Which would answer Problem 4 in the negative": not in the paper,
    which cites neither the problem nor Enflo. The inference is sound
    (my observation). Problem 4 asks whether every n-point metric embeds
    in ℓ₂ with distortion K√(log n). An expander needs Ω(log n), which
    exceeds K√(log n) for large n, so the answer is no. Upper and lower
    bounds then meet at Θ(log n) for the worst case.
- **[NOTE-679](NOTE-679.md) (Sala et al.).** The citing sentence in Sala et al.
  (arXiv:1804.03329v2, §1) reads: "Bourgain's theorem [27] shows that
  Euclidean space is unable to obtain comparably low distortion for
  trees—even using an unbounded number of dimensions", and [27] is this
  paper. This paper does not support that sentence. The theorem it
  attributes to Bourgain, Theorem 3.2(1), is an upper bound for every
  metric. Its only Euclidean lower bound, Proposition 4.2, is for
  expanders, not trees. Its only tree result, Theorem 5.3, is that trees
  embed isometrically in ℓ∞^{O(log n)}, which points the other way. My
  observation, from outside the record and unchecked: the tree lower
  bound in ℓ₂ is a different Bourgain paper, on superreflexivity (1986),
  of order √(log log n) for complete binary trees, much weaker than log n.
  [NOTE-679](NOTE-679.md)'s Limitations line, "attributed to Bourgain through Linial et
  al.", should say that the cited paper does not contain the claim.
- **[NOTE-905](NOTE-905.md) (Indyk and Motwani).** Its Fact 4, that ℓ₁ reaches Hamming
  space by an embedding needing bounded integer coordinates, is cited to
  this paper. The proof of Corollary 3.8 contains exactly that: round
  coordinates to integers, then write each in unary.
- **[QUESTION-120](../questions.d/QUESTION-120.md) (random projections).** The paper uses
  Johnson–Lindenstrauss only as a black box. Theorem 3.1 states it with
  t = O(log n/ε²) and distortion ≤ 1 + ε, attributed to Johnson and
  Lindenstrauss "see also" Frankl and Maehara. Its sketch is projection
  onto a random t-dimensional subspace. It is applied as a second stage
  after another embedding: after the SDP embedding (Claim 2) and after
  the O(log² n)-dimensional Bourgain-style map (Claim 1). This is a 1995
  statement that puts ε⁻² in the lemma, which the record found only in
  the lemma's proofs ([NOTE-930](NOTE-930.md)), and it names Frankl and Maehara as
  the explicit source (my observation). Three further pieces bear on the
  question's threads.
  - The Bourgain-style map is random but not linear. Its count has the
    question's shape without its tolerance: O(log n) random sets per
    scale, so that a constant per-pair success probability holds for all
    pairs at once, times log n scales. Its target distortion is O(log n),
    not 1 ± ε (my observation).
  - Claim 3 and Lemma 3.3 go up in dimension. ℓ₂ᵐ goes into a random
    m-dimensional subspace of ℓ_p^{2m}, and Lemma 3.3 maps ℓ₂ᵐ into
    ℓ_p^{O(m²)} by inner products with 4-wise independent ±1 vectors with
    distortion √3, with no threshold. These are expanding ±1 maps that
    keep norms, which is the expand-and-threshold thread without its
    threshold (my observation).
  - Conjecture 8.2's sketch maps the d-cube into ℤ∞^{O(ρ)}, ρ = Θ(d/log d),
    by inner products with random ±1 vectors. It needs only injectivity,
    by a random-walk collision bound and a union bound.
  None of this gives a threshold for the question. The paper supplies no
  constants for Theorem 3.1.
- **For the anthology.** §3.2 proposes the embedding for clustering
  "statistical data" and mentions a protein-sequence test. It is a remark
  without a result, and not an instruction for machine-learning practice.
  The paper is mathematics and algorithms and belongs here.
- **Filed** as [THEORY-394](../theory.d/THEORY-394.md): O(log n) Euclidean distortion for every
  n-point metric, tight for expanders. Theorem 4.1 on multicommodity flow
  could be filed separately if the record comes to need it.

## Limitations

- Constants are unspecified throughout: O(log n) distortion and
  dimension, Ω(log n) for expanders, O(log k) for the flow–cut gap.
- Claim 5's probabilistic steps (constant success per set; a tenth of q
  sets succeeding for all pairs) are asserted without calculation. Claim 1
  is said to follow from "Claims 3 and 5", but Claim 5 is stated only for
  p > 2. The ℓ₂ case is in its proof.
- The expander lower bound depends on Leighton and Rao's gap, and on
  facts from Pisier's book, none proved here. "Constant-degree expander"
  is not defined.
- The lower bounds are worst-case. The paper gives better embeddings for
  some families but no tight distortion for trees, planar graphs or other
  classes in ℓ₂.
- For p > 2 only the upper bound O(log n) is given (Claim 5), with no
  lower bound.
- Some §5 and §7 proofs are sketches or "not hard to check".
- This copy is the authors' February 1995 manuscript, not the journal's
  typeset text.

## Open questions

- The paper's own: Problems 8.5–8.7 (complexity of deciding dim(G) = d;
  the typical dimension of an n-vertex graph; whether minimum degree 3
  forces Euclidean distortion Ω(girth)); Conjectures 8.2 and 8.4; and the
  least dimension for a constant-distortion embedding of an expander,
  between Ω(log² n) and possibly Ω(n).
- For the record: whether Bourgain's paper states the O(log n) dimension,
  and what lower bound it gave, needs a copy of [LIT-1161](../literature.d/LIT-1161.md).
- What Sala et al.'s tree claim should be cited to. Bourgain's 1986
  superreflexivity paper is the candidate, and it is not in the record.
