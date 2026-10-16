---
status: Read
paper: LIT-tmp7skui
title: 'Johnson & Lindenstrauss — extensions of Lipschitz mappings into a Hilbert space'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from a scan of the published article (Contemporary
    Mathematics 26, 1984, pp. 189–206, 18 pages, DOI
    10.1090/conm/026/737400 printed on the first page), hosted on a
    Stanford course page at web.stanford.edu/class/cs114/readings/JL-Johnson.pdf
    and stamped "Licensed to Stanford Univ." The text layer was extracted
    with pdftotext -layout. Most display equations did not survive
    extraction, so every page was also read from its page image, and the
    expressions below are taken from the images. Read in full: the
    introduction, §1 (Lemmas 1–5, Proposition 1, Theorems 1–3 and their
    proofs), §2 (Problems 1–4) and §3, the appendix with Benyamini's
    version of Theorem 2 and Lemma 6. The reference list was read. Only
    the proofs of Proposition 1 and Lemma 5 were followed in outline,
    step by step but without checking each inequality.
- version: 2
  date: '2026-10-16'
  note: >-
    Annotated: the unchecked observation on Bourgain and on Linial, London
    and Rabinovich is checked against NOTE-tmpetxcq.
date: '2026-10-14'
summary: >-
  Lemma 1: any n points in ℓ₂ⁿ map into ℓ₂ᵏ, k = [K(τ) log n], with
  ‖f‖_lip‖f⁻¹‖_lip ≤ (1+τ)/(1−τ), by a Haar-random rank-k orthogonal
  projection, with positive probability. The proof concentrates the norm
  of a projected unit vector about its median by Lévy's isoperimetric
  inequality and takes a union bound over the normalized differences of
  the points; K ≥ (10/τ)² suffices. The lemma is a tool for Theorem 1:
  Lipschitz maps from n-point subsets of any metric space into ℓ₂ extend
  to the whole space with Lipschitz constant at most C(log n)^{1/2} times
  the original.
---
<!-- inactive-ok-file: LIT-tmpwy0he — Unavailable; Bourgain, named where the checked observation says so -->

# NOTE-tmpmv42v: Johnson & Lindenstrauss — extensions of Lipschitz mappings into a Hilbert space

## Contribution

The paper is about extending Lipschitz maps. L(X, n) is the smallest
constant such that every map f from an n-point subset of X into ℓ₂ extends
to all of X with ‖f̃‖_lip ≤ L‖f‖_lip. The paper proves L(X, n) ≤ C(Log n)^{1/2}
for every metric space X (Theorem 1), which verifies a conjecture of
Marcus and Pisier. It proves a lower bound of order (Log n / Log Log n)^{1/p−1/2}
for L_p, 1 ≤ p < 2 (Theorem 3), and an extension theorem for separated
domains (Theorem 2). The tool for Theorem 1 is Lemma 1, the dimension
reduction now called the Johnson–Lindenstrauss lemma. The paper calls it
"a simply stated elementary geometric lemma" and "a simple consequence of
the isoperimetric inequality for the n-sphere in the form studied in [2]"
(Figiel, Lindenstrauss and Milman 1977).

## Key insight

A random rank-k orthogonal projection shortens every fixed unit vector by
nearly the same factor, with failure probability exponentially small in
k. A finite set of directions, here the normalized differences of n
points, therefore survives together once k is a constant times the log of
the set's size. In ℓ₂ᵏ with k of order log n, Kirszbraun's theorem and the
ℓ∞ form of the non-linear Hahn–Banach theorem do the extension, and the
cost of passing between ℓ₂ᵏ and ℓ∞ᵏ is √k, which is where (log n)^{1/2}
comes from.

## Assumptions

- **Lemma 1.** A ⊂ ℓ₂ⁿ with card A = n, n ≥ 2, and 1 > τ > 0. The ambient
  space has dimension n, the number of points. No other condition.
- **Randomness.** U is drawn from normalized Haar measure σ on O(n); the
  map is U*QU, with Q the projection onto the first k coordinates.
- **Size.** k = [K log n]; the median bound M_r ≥ √(k/3) holds "at least
  for K log n sufficiently large".
- **Convention.** "Log x denotes the maximum of 1 and the natural
  logarithm of x." Lemma 1 itself is written with lower-case log.
- **Theorem 1.** X any metric space, M ⊂ X finite with card M = n,
  f: M → ℓ₂. The target is Hilbert space throughout §1 except Theorem 3,
  whose maps go into a subspace of L_p.

## Key results

- **Lemma 1 (p. 190–191).** "For each 1 > τ > 0 there is a constant
  K = K(τ) > 0 so that if A ⊂ ℓ₂ⁿ, card A = n for some n = 2, 3, …, then
  there is a mapping f from A onto a subset of ℓ₂ᵏ (k = [K log n]) which
  satisfies ‖f‖_lip ‖f⁻¹‖_lip ≤ (1+τ)/(1−τ)." The statement bounds the
  product of the two Lipschitz constants, so it is scale-free. The
  introduction phrases it as moving the points into k dimensions by a map
  that "expands or contracts all pairwise distances by a factor of at
  most 1 + ε", with answer k ≤ C(ε) Log n.
- **Proof of Lemma 1 (pp. 191–193).** With r(x) = r_k(x) = √n (Σ_{i≤k} x(i)²)^{1/2}
  = √n‖Qx‖ and B = {(x − y)/‖x − y‖ : x, y ∈ A, x ≠ y} ⊂ Sⁿ⁻¹:
  - From p. 58 of [2], for each y ∈ Sⁿ⁻¹ and ε > 0,
    σ[U : M_r − √n ε ≤ r(Uy) ≤ M_r + √n ε] ≥ 1 − 4 exp(−nε²/2), with M_r
    the median of r on Sⁿ⁻¹.
  - (1.1): the same holds for all y ∈ B at once with probability
    ≥ 1 − 2n(n+1) exp(−nε²/2).
  - (1.2): |∫ r dμ − M_r| < C, with C ≤ 4 Σ_{m≥1} (m+1) e^{−m²/2} (Lemma 1.7
    of [2]).
  - (1.3): by Khintchine's inequality with constant √2,
    √(k/2) ≤ ∫ r_k dμ ≤ √k. Hence √(k/3) ≤ M_r for K log n large.
  - Setting ε = τ√(k/3n): σ[(1−τ)M_r ≤ r(Uy) ≤ (1+τ)M_r for all y ∈ B]
    ≥ 1 − 2n(n+1) exp(−τ²k/18) ≥ 1 − 2n(n+1) exp(−τ²K log n/18), "which is
    positive if, say, K ≥ (10/τ)²."
  - So k = [100 τ⁻² log n] suffices. The τ⁻² dependence is in the proof,
    not in the statement. The probability can be made "arbitrarily close
    to one by adjusting k".
- **Lower bound remark (p. 193).** "The estimate K log n in Lemma 1 cannot
  be improved." A ball of radius 2 in ℓ₂ᵏ holds at most 4ᵏ vectors at
  mutual distance ≥ 1, so for τ small enough no map sends an orthonormal
  set of more than 4ᵏ vectors into k dimensions with distortion
  (1+τ)/(1−τ). This shows that k must grow like log n. It says nothing
  about how K must depend on τ.
- **Theorem 1 (p. 194).** sup_{n≥2} (log n)^{−1/2} L(∞, n) < ∞: there is K
  such that every f from an n-point subset M of a metric space X into ℓ₂
  has an extension f̃: X → ℓ₂ with ‖f̃‖_lip ≤ K√(log n) ‖f‖_lip. Proof:
  Lemma 1 with τ = 1/2 gives g⁻¹ from A = f[M] into ℓ₂ᵏ, k ≤ K log n, with
  ‖g⁻¹‖_lip ≤ 1 and ‖g‖_lip ≤ 3. Extend g by Kirszbraun, pass to ℓ∞ᵏ by the
  identity I (‖I‖ = 1, ‖I⁻¹‖ = √k), extend h = Ig⁻¹f by the non-linear
  Hahn–Banach theorem, and set f̃ = g̃I⁻¹h̃. Then
  ‖f̃‖_lip ≤ 3√k ‖f‖_lip ≤ 3K√(log n) ‖f‖_lip.
- **Theorem 2 (p. 195).** If A ⊂ X has d(x, y) ≥ ε > 0 for x ≠ y ∈ A and
  diameter D, every Lipschitz f: A → ℓ₂ extends with
  ‖f̃‖_lip ≤ (6D/ε)‖f‖_lip. The proof factors through ℓ₁^B and, by a weak
  form of Grothendieck's inequality, through ℓ∞ with ‖H‖ ≤ 3‖G‖.
- **Theorem 2, Benyamini (appendix, p. 205).** The same for any Banach
  space Z in place of ℓ₂, with ‖f̃‖_lip ≤ (4D/ε)‖f‖_lip, via Lemma 6: a
  retraction of ℓ∞(Γ) onto the positive part of the ℓ₁(Γ) ball with
  Lipschitz constant ≤ 2, and a map H into A = {αe_γ} with ‖H‖_lip ≤ 4.
- **Lemma 2.** The positively homogeneous extension of f: S(Y) → X with
  f(0) = 0 satisfies ‖f̃‖_lip ≤ 2‖f‖_lip + ‖f‖_∞.
- **Lemma 3.** The unit sphere of an n-dimensional Banach space has an
  ε-net of cardinality at most (1 + 4/ε)ⁿ, by a volume argument on
  disjoint balls of radius ε/4.
- **Lemma 4.** There is δ > 0 such that for 1 ≤ p < 2 and every N, L_p
  contains E with d(E, ℓ₂ᴺ) ≤ 2 on which every projection from L_p has
  norm ≥ δN^{1/p−1/2}. Uses γ₁(ℓ₂ᴺ) = γ∞(ℓ₂ᴺ) = √(2n/π); the copy prints n
  where N is meant (my reading).
- **Proposition 1 and Lemma 5.** A linearization from Lindenstrauss
  (1964), and a smoothing of positively homogeneous Lipschitz maps with
  ‖F̃|_X − U‖_lip ≤ (8k + 2)‖F|_{S(X)} − U|_{S(X)}‖_∞ and ‖F̃‖_lip ≤ 4‖F‖_lip,
  for dim X = k.
- **Theorem 3 (p. 201).** There is a constant (printed τ in the statement,
  δ in the introduction) > 0 such that for all n ≥ 2 and 1 ≤ p < 2,
  L(p, n) ≥ τ (Log n / Log Log n)^{1/p−1/2}. Taking p = 1 and
  L(∞, n) ≥ L(1, n) gives L(∞, n) ≥ δ(Log n / Log Log n)^{1/2}. The proof
  sets ε = Log⁻² n and N = Log n / (2 Log Log n).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | n points in ℓ₂ⁿ embed in ℓ₂ᵏ, k = [K(τ) log n], with Lipschitz distortion (1+τ)/(1−τ), by a random orthogonal projection | strong | Lemma 1, full proof; K ≥ 100/τ² suffices |
| C2 | The log n in Lemma 1 cannot be improved | strong | Remark on p. 193, packing bound of 4ᵏ |
| C3 | L(X, n) ≤ C(log n)^{1/2} for every metric space X | strong | Theorem 1, from Lemma 1 and Kirszbraun |
| C4 | L(p, n) ≥ δ(Log n / Log Log n)^{1/p−1/2} for 1 ≤ p < 2 | strong | Theorem 3 |
| C5 | Extensions from ε-separated sets of diameter D cost at most 6D/ε into ℓ₂, 4D/ε into any Banach space | strong | Theorem 2; Benyamini's appendix |
| C6 | The Marcus–Pisier bound and Theorem 1 likely give the right order of L(p, n) | weak | stated as a belief in the introduction; open |

## Method

Lemma 1's proof is the method later papers inherit.

1. Reduce to directions: B, the at most n(n−1) normalized differences of
   the points, lies on Sⁿ⁻¹.
2. For one direction, the rescaled projected norm r(Uy) concentrates
   about its median M_r with tail 4 exp(−nε²/2) (Lévy's inequality as in
   [2]).
3. Locate the median: it is within a constant of the mean, and the mean is
   between √(k/2) and √k by Khintchine.
4. Union bound over B, giving failure ≤ 2n(n+1) exp(−τ²k/18).
5. Choose K ≥ (10/τ)² so the bound is below 1.

## Concepts

- **L(X, n)** — the smallest L such that every f from an n-point subset of
  X into ℓ₂ extends to X with ‖f̃‖_lip ≤ L‖f‖_lip. L(p, n) means
  L(L_p(0,1), n).
- **Random rank-k projection** — U*QU with U Haar-distributed on O(n) and
  Q the coordinate projection onto the first k coordinates.
- **Distortion** — ‖f‖_lip‖f⁻¹‖_lip, the product of the Lipschitz constants
  of a map and its inverse. The lemma bounds it by (1+τ)/(1−τ).
- **d(X, Y)** — the Banach–Mazur distance, inf ‖T‖‖T⁻¹‖ over linear
  isomorphisms.
- **Log x** — max(1, ln x).

## Connections

The concentration step is taken from Figiel, Lindenstrauss and Milman
(1977), the paper's reference [2], on almost spherical sections of convex
bodies. The extension machinery is Kirszbraun's theorem and the
non-linear Hahn–Banach theorem (Wells and Williams), and Lindenstrauss's
1964 non-linear projections. The problem is Marcus and Pisier's. The
paper does not frame Lemma 1 as dimension reduction for data, and says
nothing about algorithms.

Later proofs registered by [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) replace the Haar rotation and
the isoperimetric inequality: Dasgupta and Gupta ([LIT-tmpjy3gf](../literature.d/LIT-tmpjy3gf.md)) by χ²
moment bounds, Achlioptas ([LIT-tmppzjx6](../literature.d/LIT-tmppzjx6.md)) by sparse sign matrices. The
ε⁻² dependence that later statements lead with, and its optimality
([LIT-tmp8s1wj](../literature.d/LIT-tmp8s1wj.md)), are not in this paper's statement.

Problem 3 asks whether every n-point metric space embeds with distortion
1 + ε into some Banach space of dimension K(ε) log n. Problem 4 asks for
distortion K√(log n) into ℓ₂, and notes from Enflo that this would be best
possible. My observation, from outside the paper and not checked in the
record: Bourgain (1985) gave O(log n), and Linial, London and Rabinovich
(1995) showed that order is needed for expanders, which would answer
Problem 4 in the negative. (Checked 2026-10-16 in [NOTE-tmpetxcq](NOTE-tmpetxcq.md): both
hold as Linial, London and Rabinovich state them, Theorem 3.2(1) and
Proposition 4.2, with the expander bound for ℓ_p, 1 ≤ p ≤ 2. They cite
neither Problem 4 nor Enflo, so the negative answer is the record's
inference. Bourgain's own paper is Unavailable, [LIT-tmpwy0he](../literature.d/LIT-tmpwy0he.md).)

## Bearing on the record

- **[QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md), the general shape.** The question proposes that each
  threshold is the log of the size of the family a map must hold, divided
  by a squared tolerance. Lemma 1's proof has exactly that shape for
  distances. The family is B, of size at most n(n−1); the bound is
  2n(n+1) exp(−τ²k/18); so k of order τ⁻² log n. The paper supplies this
  for the first thread and, by construction, for nothing else.
- **The superposition thread.** Two pieces of this paper bear on it, my
  observation. Lemma 3, the (1 + 4/ε)ⁿ net on a sphere, is the second
  ingredient a union bound over sparse supports needs; the paper proves it
  but uses it only for Theorem 3, not with Lemma 1. And the remark on
  p. 193 runs the other way from superposition: k dimensions hold at most
  4ᵏ vectors that are near-orthonormal in the strict sense of distortion
  (1+τ)/(1−τ) with τ small, while Lemma 1 applied to an orthonormal set
  puts n of them in k of order τ⁻² log n. Together they bracket how many
  nearly orthogonal directions fit in k dimensions, which is the count
  [NOTE-278](NOTE-278.md)'s bound concerns. The paper does not discuss sparse vectors.
- **The random-features thread.** Nothing. The paper has no kernels, no
  regression, no sample count, and no 2N = n. It supports the question's
  first doubt only negatively: its guarantee is about keeping a finite set
  of distances, and says nothing about interpolation.
- **The expand-and-threshold thread.** Nothing directly. Lemma 1 maps
  ℓ₂ⁿ into ℓ₂ᵏ with k = [K log n], linear, no thresholding. The question's
  observation that the lemma "is about going down" is right for this
  paper.

Statements in [LIT-tmp7skui](../literature.d/LIT-tmp7skui.md) and the QUESTION checked against the text:

1. LIT summary and takeaway: "into O(ε⁻² log n) dimensions". Imprecise.
   Lemma 1 states k = [K(τ) log n] with K unspecified. The τ⁻² dependence
   appears only in the proof, as K ≥ (10/τ)², so k = [100 τ⁻² log n]
   suffices.
2. LIT summary: "every pairwise distance kept within a factor 1 ± ε".
   Imprecise. The statement bounds ‖f‖_lip‖f⁻¹‖_lip ≤ (1+τ)/(1−τ); the proof
   gives (1−τ)M_r ≤ r(Uy) ≤ (1+τ)M_r for every normalized difference, which
   is 1 ± τ on distances (not squared distances) after dividing by M_r.
3. LIT summary: "any n points in a Hilbert space". The lemma takes
   A ⊂ ℓ₂ⁿ with card A = n. Equivalent, since n points span at most n
   dimensions (my observation), but the paper does not say so.
4. LIT takeaway: "a projection onto a uniformly random k-dimensional
   subspace, rescaled". Right in substance. The paper's map is U*QU with U
   Haar on O(n); the rescaling is implicit in the scale-free statement.
5. LIT takeaway: "The dimension does not depend on the ambient
   dimension." Not stated. The ambient space in Lemma 1 is ℓ₂ⁿ, n being
   the number of points; independence of ambient dimension follows (my
   observation) but is not a claim of the paper.
6. LIT takeaway: "The squared length of a fixed vector's projection
   concentrates sharply around its mean." Wrong for this paper. The proof
   concentrates the norm r(Uy) = √n‖QUy‖, not its square, around its
   median M_r, by Lévy's isoperimetric inequality as in [2]; the mean
   enters only to locate the median, via Lemma 1.7 of [2] and Khintchine's
   inequality. The squared-length, moment-generating argument is Dasgupta
   and Gupta's ([LIT-tmpjy3gf](../literature.d/LIT-tmpjy3gf.md)), not this paper's.
7. LIT takeaway: "a union bound over the n² pairs". Right: the union is
   over B, at most n(n−1) normalized differences, with failure bound
   2n(n+1) exp(−τ²k/18).
8. LIT takeaway: it "bounds an extension constant" for maps "from subsets
   of metric spaces". Right, with the precision that the subsets are
   finite, of size n, and the bound is L(X, n) ≤ K√(log n) (Theorem 1,
   Lemma 1 with τ = 1/2).
9. QUESTION: "The Johnson–Lindenstrauss lemma gives ε⁻² log n". As in 1:
   the lemma as stated gives K(τ) log n; ε⁻² is in the proof.
10. QUESTION: "the bound is tight ([LIT-tmp8s1wj](../literature.d/LIT-tmp8s1wj.md))". Attributed to another
    work, unchecked here. This paper proves only that the log n factor
    cannot be improved for small τ (p. 193); it says nothing on the
    τ-dependence.
11. LIT summary: "The lemma was a step towards a Lipschitz-extension
    theorem". Right: the paper calls it "the main tool for proving
    Theorem 1". "It is now cited for itself" is the record's observation,
    not the paper's.

Nothing here is ML practice. The paper is mathematics and belongs here.

## Limitations

- Lemma 1 gives existence with positive probability, and K(τ) only as a
  sufficient choice; no explicit construction and no optimal constant.
- The lower bound on p. 193 is about n, for fixed small τ; the paper has
  no lower bound in τ.
- Theorem 1's last step, 3√k ≤ 3K√(log n), uses √(K log n) ≤ K√(log n),
  which needs K ≥ 1; harmless, but the constants are loose throughout.
- The authors leave open whether Theorem 1's (log n)^{1/2} is best
  possible; Theorem 3 gives only (Log n / Log Log n)^{1/2} below.

## Open questions

- The paper's own: whether Theorem 1 is sharp; Problems 1–4 (§2), in
  particular Problem 3, the analogue of Lemma 1 for Banach spaces other
  than Hilbert space, chiefly ℓ∞ⁿ.
- For [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md): whether the proof's three steps (concentration
  for one vector, a net or finite family, a union bound) are the same steps
  in Baraniuk et al.'s RIP proof ([LIT-tmpcfdvm](../literature.d/LIT-tmpcfdvm.md)) once the family is
  the union of nets on k-sparse subspaces. Reading that paper beside
  Lemmas 1 and 3 would settle it.
