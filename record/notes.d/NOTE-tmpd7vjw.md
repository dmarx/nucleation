---
status: Read
paper: LIT-tmp2k8rj
title: 'Lee & Naor — extending Lipschitz functions via random metric partitions'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the author-posted PDF on James R. Lee's page
    (homes.cs.washington.edu/~jrl/papers/pdf/lipext.pdf), 30 pages, with
    affiliations U.C. Berkeley and Microsoft Research. It is a preprint,
    not the journal text: the PDF was produced from TeX on 10 January 2004,
    it carries no journal header, dates or DOI, it runs 30 letter pages
    against the journal's pp. 59–95, and it cites the authors' C. R. Acad.
    Sci. note as "to appear, 2003". Theorem numbers below are the
    preprint's; whether the journal renumbered them or changed constants
    was not checked. The text layer was extracted with pdftotext -layout;
    pages 2, 5, 7, 11, 20, 23, 24 and 25 were also read from page images,
    where displayed formulas were garbled. Read in full: §1 (all stated
    theorems and the open problems), §2 (Lemma 2.1 and proof), §3
    (Definitions 3.1–3.7, Lemma 3.8, Lemma 3.11, Corollaries 3.12–3.13,
    Lemma 3.16, Theorem 3.17 and proofs), §4 (Theorem 4.1 cases 1–3,
    Theorem 4.3 and Corollaries 4.4–4.5), §5 (Theorem 5.1, Proposition
    5.2, Corollary 1.8, the proof of Theorem 1.12, Remark 5.3) and the
    appendix (Lemma 6.1, Theorem 6.2). Followed in outline: Lemma 3.14 and
    Corollary 3.15, which the paper itself only sketches, and the
    measurability arguments. The reference list was read.
date: '2026-10-16'
summary: >-
  A random partition of a metric space whose pieces are small and whose
  points are, on average, far from piece boundaries yields a "gentle"
  partition of unity, and averaging a Lipschitz map over it extends the map
  into any Banach space. This gives ae(X) ≤ C log n/log log n for every
  n-point metric space X (Theorem 1.10), improving Johnson, Lindenstrauss
  and Schechtman's C log n; ae(X) ≤ C log λ(X) for doubling X; ae ≤ C r²
  on K_r-minor-free graph metrics; e(ℓ₂ᵈ, Z) ≤ C√d; and, with the
  Johnson–Lindenstrauss lemma, eₙ(L₂, Z) ≤ C√(log n). For maps into
  Hilbert space it does not improve Johnson and Lindenstrauss's
  K√(log n), and it leaves √(log n) open.
---

# NOTE-tmpd7vjw: Lee & Naor — extending Lipschitz functions via random metric partitions

## Contribution

The paper turns the random partitions of theoretical computer science
("stochastic metric decomposition") into a method for extending Lipschitz
maps. A distribution over partitions with small pieces, in which each
point is likely to sit well inside its piece, gives a partition of unity
whose weights change slowly; averaging the map's values at chosen points
of X with those weights is the extension. The paper names a new property,
absolute extendability: a bound on the extension constant that depends
only on the domain X, for every containing space Y and every Banach
target Z. It proves such bounds for doubling spaces, graph metrics with an
excluded minor, surfaces of bounded genus and finite metric spaces, and it
improves the known bounds for n-point domains into Banach spaces and for
Euclidean domains.

## Key insight

One Lipschitz extension point by point degrades the constant at each
step; a random cover glued by averaging does not, if the boundary of the
cover is "smooth on average". The constant of the extension is set by how
much the partition-of-unity weights at two nearby points differ,
integrated against how far the chosen anchor points are. A random
partition at every scale 2ⁿ, with each point padded away from boundaries
with probability δ at margin εΔ, gives weights that differ by
O(d(x, y)/(εδ · d(x, X))), and so an extension constant O(1/(εδ)). For an
n-point X the improvement to log n/log log n comes from spreading the
smoothing over M ≈ log log n consecutive scales, so that the per-scale
cutting costs log(|B(x, 5ⁿ⁺¹)|/|B(x, 5ⁿ)|), which telescope to log n,
are divided by M.

## Assumptions

- **Targets.** Z a Banach space, or a closed convex subset C of one
  (Lemma 2.1). In the appendix, a complete β-barycentric metric space:
  there is c from bounded-support probability measures to Z with
  c(δ_z) = z and d_Z(c(μ), c(ν)) ≤ β · diam(supp(μ + ν)) · ‖μ − ν‖_TV
  (Definition 1.14). Banach spaces have β = 1; Hadamard spaces too.
  Theorem 1.10 is proved only for Banach targets.
- **Domains.** X ⊆ Y, Y an arbitrary metric space. Lemma 2.1 needs Ψ
  locally finite or X separable. Theorem 3.17 needs X compact and a
  non-degenerate Borel measure on X; Theorem 4.3 uses counting measure on
  a finite X.
- **Decompositions.** ∆-bounded: every piece has diameter ≤ ∆
  (Definition 3.2). (ε, δ)-padded: if d(x, X) ≤ ε∆, then with probability
  ≥ δ the point x is at distance ≥ ε∆ from the complement of its piece
  (Definition 3.3). (ε, δ)-separating: the probability that x and y are
  split is ≤ d(x, y)/(δ∆) (Definition 3.7). Theorem 4.1 needs such a
  decomposition at every scale 2ⁿ, n ∈ ℤ.
- **Doubling constant.** λ(X) is the least λ such that every ball is
  covered by λ balls of half the radius.
- **Notation.** e(X, Y, Z) is the least K such that every Lipschitz
  f: X → Z extends to Y with ‖f̃‖_Lip ≤ K‖f‖_Lip; e(Y, Z) its sup over
  X ⊆ Y; eₙ(Y, Z) its sup over |X| ≤ n; ae(X) = sup over Y ⊇ X and Banach
  Z of e(X, Y, Z).

## Key results

- **Theorem 1.2, as the paper cites Johnson and Lindenstrauss.**
  "For every metric space Y and every integer n, eₙ(Y, L₂) ≤ 2√(log n)."
  The constant 2 is the paper's. Johnson and Lindenstrauss's text, as
  read in [NOTE-tmpmv42v](NOTE-tmpmv42v.md), gives K√(log n) with K unspecified (my
  observation).
- **Cited lower bound.** "In [17], it was also shown that … for every
  1 ≤ p < 2, eₙ(L_p, L₂) ≥ C(p)(log n/log log n)^{1/p−1/2}."
- **Theorems 1.3 and 1.4, cited (Johnson, Lindenstrauss and Schechtman
  1986).** eₙ(Y, Z) ≤ C log n for every metric space Y and Banach space Z;
  e(Y, Z) ≤ Cd for every d-dimensional normed space Y. Theorem 1.5
  (Matoušek): e(T, Z) ≤ C for metric trees.
- **Lemma 2.1.** If Y admits a K-gentle partition of unity with respect to
  X (K ≥ 1), every Lipschitz f: X → C, C closed convex in a Banach space,
  extends with ‖f̃‖_Lip ≤ 3K‖f‖_Lip, linearly and continuously in f. The
  extension is f̃(x) = ∫ f(γ(ω)) Ψ(ω, x) dμ(ω) off X.
- **Lemma 3.8 (partition extension).** A finitely supported (ε, δ)-padded
  ∆-bounded decomposition of a closed X extends to an
  (ε/(16+8ε), δ)-padded (1 + ε/2)∆-bounded decomposition of any Y ⊇ X.
  This is what lets hypotheses be placed on X alone.
- **Lemma 3.11.** Every metric space admits an (ε, ½)-padded ∆-bounded
  decomposition with ε = 1/(256 log C(X; 2∆, ∆/4)), C(X; R, r) the largest
  set with all distances in [r, R]. The proof uses a random order on a
  net and a random radius in [∆, 2∆], and bounds
  Pr[B(x, t) is cut] ≤ Σ_k (2t/∆)(1/k) ≤ (8t/∆) log C(X; 6∆, ∆).
- **Corollary 3.12.** Doubling X: (C/log λ(X), ½)-padded at every scale.
- **Lemma 3.14 and Corollary 3.15 (sketched).** K_r-minor-free graph
  metrics: (c/r², ½)-padded, from Klein, Plotkin and Rao with
  Fakcharoenphol and Talwar's β(r) = Ω(1/r). Surfaces of genus g:
  (c/(g+1), ½)-padded.
- **Lemma 3.16.** Closed X ⊆ ℓ₂ᵈ: a decomposition of ℓ₂ᵈ that is
  (ε, 1/(2√d))-separating and ∆-bounded for every ε > 0, from random
  balls of radius ∆/2 (Charikar et al.).
- **Theorem 3.17.** For compact X ⊆ Y and a non-degenerate Borel measure σ
  on X, a ∆-bounded decomposition of Y with, for d({x, y}, X) < ∆/16,
  Pr[x, y split] ≤ (2d(x, y)/∆)[1 + log(σ(B_X(x, 5∆))/σ(B_X(x, ∆)))]
  (eq. 3), generalizing Calinescu–Karloff–Rabani and
  Fakcharoenphol–Rao–Talwar to infinite spaces.
- **Theorem 4.1.** Decompositions at every scale 2ⁿ that are (ε, δ)-thick
  or (ε, δ)-padded give a C/(εδ)-gentle partition of unity;
  (ε, δ)-separating ones give C(1/ε + 1/δ). The proof's explicit
  constant in case 1 is 340/(δ d(x, X)) in (15).
- **Theorem 4.3.** For every m-point X ⊆ Y, Y admits a
  C(log m/log log m)-gentle partition of unity. Corollary 4.5 gives the
  bound O(5^{2M}/M² + (log m)/M) · d(x, y), and M ≈ log log m is chosen.
- **Theorem 5.1 (the main theorem).** With a universal constant C:
  1. ae(X) ≤ C log λ(X) for every metric space X (Theorem 1.6).
  2. ae(X) ≤ C r² for every K_r-excluded metric X (Theorem 1.7).
  3. ae(X) ≤ C(g + 1) for X in a surface of genus g (Corollary 1.9).
  4. **ae(X) ≤ C log n/log log n for every n-point metric space X
     (Theorem 1.10).**
  5. e(ℓ₂ᵈ, Z) ≤ C√d for every Banach space Z (Theorem 1.11); hence
     e(Y, Z) ≤ C√d · dist(Y, ℓ₂ᵈ) for normed Y, and C·d by John's theorem.
- **Corollary 1.8.** For a family of finite graphs F, ae(⟨F⟩) < ∞ if and
  only if ⟨F⟩ does not contain all finite metrics (by Robertson and
  Seymour).
- **Proposition 5.2.** For X ∆-dense in Y inside an n-dimensional
  manifold with Ricci(g) ≥ −(n−1)rg, e(X, Y, Z) ≤ C · n(1 + √(r∆)).
- **Theorem 1.12.** For 1 < p ≤ 2 and every Banach space Z,
  eₙ(L_p, Z) ≤ C(p)(log n)^{1/p}. For p = 2 this is C√(log n). Proof for
  p = 2 (p. 24): by the proof of the Johnson–Lindenstrauss lemma, random
  rank-d operators T_ω on the span of X with
  P(|‖T_ω x‖₂ − ‖x‖₂| ≥ ½) ≤ 2e^{−cd}; for d ≈ (4/c) log n a set A of
  probability ≥ ½ on which ‖T_ω x − T_ω y‖₂ ≥ ½‖x − y‖₂ for all pairs;
  extend f ∘ T_ω⁻¹ from T_ω(X) by Theorem 5.1(5) with constant
  (4C/√c)√(log n)‖f‖_Lip; average over A. The upper side is needed only
  in expectation, ∫‖T_ω z‖ dP = O(‖z‖₂). For 1 < p < 2, Marcus and
  Pisier's p-stable maps S_ω: L_p → L₂ lose c_p(log n)^{1/p−1/2} with
  probability ≥ ½, and E‖S_ω z‖₂/‖z‖_p = C_p < ∞ for p > 1.
- **Lemma 1.13 / Remark 5.3 (sketch).** For 2 < p < ∞,
  eₙ(L₂, L_p) ≥ C(log n/log log n)^{(p−2)/p²}, quantifying the second
  author's e(L₂, L_p) = ∞ (Naor 2001) through the Mazur map on a net of
  the ball of ℓ₂^{2m}, n = m^{2m}. This answers negatively the question
  of [17] and [18] whether supₙ eₙ(L₂, Z) < ∞ for every Banach Z.
- **Lemma 6.1, Theorem 6.2 (appendix).** A (K, L)-gentle partition of
  unity gives extensions into a β-barycentric Z with constant
  β max{KL, 2K + 2}; padded or thick decompositions give (36/ε, 680/δ),
  separating ones (36/ε, 160(1 + ε/δ)). Theorem 1.10 does not transfer:
  Theorem 4.3's construction does not give condition 2.
- **Open problems (§1.4).** Whether e(L₂, L₁) is finite (Ball); whether
  e(L_p, L_q) < ∞ for 2 < p < ∞, 1 < q < 2; and "it is not known
  whether, for every metric space X and every normed space Z,
  eₙ(X, Z) = O(√(log n)). All known lower bounds fail to beat the
  '√(log n) barrier.'"

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A K-gentle partition of unity gives Lipschitz extensions into any Banach space with constant 3K, linear in f | strong | Lemma 2.1, full proof |
| C2 | Padded, thick or separating random partitions at every scale give gentle partitions of unity with K = O(1/(εδ)) or O(1/ε + 1/δ) | strong | Theorem 4.1, full proof |
| C3 | Every n-point metric space X has ae(X) ≤ C log n/log log n | strong | Theorem 4.3 with Theorem 3.17 and Lemma 2.1; Theorem 5.1(4) |
| C4 | ae(X) ≤ C log λ(X) for doubling X | strong | Lemma 3.11, Corollary 3.12, Lemma 3.8, Theorem 4.1 |
| C5 | ae ≤ C r² for K_r-minor-free graph metrics, and finite-graph families are absolutely extendable iff they do not contain all finite metrics | moderate | Lemma 3.14 is a sketch resting on [20], [10], [31]; Corollary 1.8 via Robertson–Seymour |
| C6 | e(ℓ₂ᵈ, Z) ≤ C√d and eₙ(L_p, Z) ≤ C(p)(log n)^{1/p} for 1 < p ≤ 2 | strong | Lemma 3.16, Theorem 4.1(3); proof of Theorem 1.12 using the JL lemma |
| C7 | eₙ(L₂, L_p) ≥ C(log n/log log n)^{(p−2)/p²} for 2 < p < ∞ | moderate | Remark 5.3, a sketch of Naor (2001) |

## Method

1. **Decompose at every scale.** For each n ∈ ℤ, a random partition of Y
   with pieces of diameter ≤ 2ⁿ (or 5ⁿ) and a selector γⁱ picking a point
   of X near each piece (Definition 3.1: d(γⁱ, Γⁱ) < 2d(X, Γⁱ)). Lemma
   3.8 builds it on Y from one on X.
2. **Weight by distance to X.** A bump ϕₙ(x) = ϕ(d(x, X)/(ε2ⁿ⁻³)) turns on
   only the scales comparable to d(x, X); at most five are on at once
   (Theorem 4.1). For finite X, Theorem 4.3 widens the bump to M ≈ log log m
   scales.
3. **Weight by padding.** In the padded case each piece's weight at x is
   g(π(x)/(ε2ⁿ⁻¹)), π(x) the distance from x to the piece's boundary, so a
   point near a boundary gets little weight there.
4. **Normalize** by S(x), giving Ψ(i, ω, x) with ∫Ψ = 1, and **average**:
   f̃(x) = ∫ f(γ(ω)) Ψ(ω, x) dμ(ω).
5. **Bound** ∫ d(γ(ω), x)|Ψ(ω, x) − Ψ(ω, y)| dμ by a constant times
   d(x, y) (Claim 4.2 and estimates (10)–(18)).

## Concepts

- **K-gentle partition of unity** — Ψ: Ω × Y → [0, ∞) with
  ∫Ψ(ω, x) dμ = 1 off X, Ψ = 0 on X, and a selector γ: Ω → X with
  ∫ d(γ(ω), x)|Ψ(ω, x) − Ψ(ω, y)| dμ(ω) ≤ K d(x, y).
- **Stochastic decomposition** — a probability space of partitions of Y
  into Borel pieces, each with a selector into X.
- **Padded, thick, separating** — Definitions 3.3, 3.5, 3.7 above;
  padded implies thick with δ replaced by εδ (Remark 3.6).
- **Absolute extendability** — ae(X) < ∞: the extension constant from X
  is bounded over every superspace Y and every Banach target Z.
- **Barycentric metric space** — Definition 1.14; the substitute for
  taking expectations in a non-linear target.
- **⟨G⟩** — all submetrics of the 1-dimensional complex of G under every
  choice of edge weights in [0, ∞].

## Connections

The extension problem and the parameter eₙ come from Marcus and Pisier
(1984), Johnson and Lindenstrauss ([LIT-tmp7skui](../literature.d/LIT-tmp7skui.md), cited as [17]) and
Johnson, Lindenstrauss and Schechtman (1986, [18]); none of the last is in
the record. Theorem 1.10 improves [18]'s Theorem 1.3, and Theorem 1.11
improves its Theorem 1.4 for Euclidean domains. Theorem 1.12's p = 2 case
uses Johnson and Lindenstrauss's dimension-reduction lemma ([THEORY-tmpns5kz](../theory.d/THEORY-tmpns5kz.md))
as a tool, exactly as their Theorem 1 did, but averages over the random map
instead of fixing one. The decompositions come from theoretical computer
science: Gupta, Krauthgamer and Lee (doubling), Klein, Plotkin and Rao with
Fakcharoenphol and Talwar and Rao (excluded minors), Calinescu, Karloff and
Rabani with Fakcharoenphol, Rao and Talwar (finite metrics, the
log n/log log n), Charikar et al. (ℓ₂ᵈ). The barycentric targets follow
Gromov's codiffusions and Lang, Pavlović and Schroeder's Hadamard-space
extensions.

The paper cites [17] for Theorem 1.2 and its lower bound only. It does not
cite or discuss [17]'s Theorem 2 or Benyamini's appendix, the bound for
separated domains ([THEORY-tmpub08y](../theory.d/THEORY-tmpub08y.md)).

## Bearing on the record

- **[THEORY-tmp7nqd6](../theory.d/THEORY-tmp7nqd6.md), the bound in n.** For maps from an n-point subset
  of any metric space into Hilbert space, this paper gives nothing better
  than Johnson and Lindenstrauss. Its general bound, Theorem 1.10 /
  Theorem 5.1(4), is ae(X) ≤ C log n/log log n for any Banach target,
  which for Z = L₂ is weaker than K√(log n) by a factor of order
  √(log n)/log log n. What it improves is Johnson, Lindenstrauss and
  Schechtman's C log n for arbitrary Banach targets (Theorem 1.3), by a
  factor log log n, and it makes the bound absolute: independent of the
  containing space Y as well as of Z. Separately, Theorem 1.12 gives the
  same order √(log n) as Johnson and Lindenstrauss in the dual setting:
  domain an n-point subset of L₂, target any Banach space,
  eₙ(L₂, Z) ≤ C√(log n). There, as in Johnson and Lindenstrauss, the
  √(log n) is √d for d of order log n, after dimension reduction (my
  observation): here from e(ℓ₂ᵈ, Z) ≤ C√d, there from the √k between
  ℓ₂ᵏ and ℓ∞ᵏ.
- **The lower bound.** The paper restates Johnson and Lindenstrauss's
  eₙ(L_p, L₂) ≥ C(p)(log n/log log n)^{1/p−1/2} for 1 ≤ p < 2 and adds no
  better lower bound for Hilbert targets. Its own lower bound, Lemma 1.13,
  is for Hilbert domains and L_p targets, p > 2, with exponent
  (p−2)/p² ≤ 1/8; it is far below √(log n).
- **Sharpness is not settled.** The paper states the question as open in
  a wider form: whether eₙ(X, Z) = O(√(log n)) for every metric space X
  and normed space Z, and "All known lower bounds fail to beat the
  '√(log n) barrier'" (§1.4). For Hilbert targets the gap Johnson and
  Lindenstrauss left, a factor (log log n)^{1/2}, stands as it was. For
  arbitrary Banach targets the gap is between C log n/log log n above and
  the Hilbert-target lower bound of order (log n/log log n)^{1/2} below
  (my observation from the cited bounds).
- **[THEORY-tmpub08y](../theory.d/THEORY-tmpub08y.md), separated sets.** The paper says nothing about them.
  Two observations of mine. First, its bounds and the separated-set bound
  are incomparable. An equilateral n-point set has D/ε = 1, so Benyamini's
  bound gives 4, while Theorem 1.10 gives C log n/log log n and
  Theorem 1.6 gives C log n (λ = n for that set). The points 2⁰, …, 2ⁿ on
  a line have D/ε of order 2ⁿ but bounded doubling constant, so Theorem
  1.6 gives a constant where the separated bound gives order 2ⁿ. Second,
  Benyamini's 4D/ε holds for every superspace and every Banach target,
  so it is itself an absolute extendability bound, ae(X) ≤ 4D/ε, for
  families of unbounded cardinality. The paper's §1.2 says the only
  previously known absolutely extendable families were so "for a 'trivial'
  reason": absolute Lipschitz retracts or bounded cardinality. Johnson and
  Lindenstrauss's appendix, which the paper does not cite on this point,
  is a third case.
- **[QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md), random projections.** Marginal. The only random
  linear maps in the paper are in the proof of Theorem 1.12. They are
  used differently from Lemma 1 of Johnson and Lindenstrauss: only the
  lower side (no pair shrinks by more than ½) must hold for all n² pairs,
  at d of order log n with fixed distortion, by the same union bound;
  the upper side is needed only on average, because the extension
  averages over the random map. For 1 < p < 2 a p-stable map, with no
  exponential concentration, pays a factor (log n)^{1/p−1/2} instead of
  dimension. The random partitions are random but not linear; their cut
  probability (8t/∆) log C(X; 6∆, ∆) in Lemma 3.11 also scales as the log
  of a family's size, but by a harmonic sum over a random order, not by
  concentration (my observation). Nothing here reaches the random-features
  or expand-and-threshold threads.
- **[LIT-tmp2k8rj](../literature.d/LIT-tmp2k8rj.md)'s filing-time statements.** "Extends Lipschitz maps by
  gluing along random partitions": right, by averaging over a partition of
  unity built from them. "Bounds on extension constants in terms of the
  number of points and of the doubling constant": right, Theorems 1.10 and
  1.6, with targets any Banach space and superspace arbitrary. "The
  absolute extendability constant is at most a constant times the log of
  the doubling constant": right, Theorem 1.6. The Standing's framing, "the
  later work on the extension problem of Johnson and Lindenstrauss's
  Theorem 1 … whose sharpness they left open", needs correcting: the paper
  does not address that sharpness for Hilbert targets and leaves the
  √(log n) question open.
- Nothing here is machine-learning practice. The paper is mathematics and
  belongs here.

## Limitations

- Constants are universal but not given, except in the gentle-partition
  estimates (340, 680, 36, 160) and Lemma 3.11's 256.
- Theorem 1.10 is for Banach targets only; the paper says its proof does
  not transfer to barycentric spaces.
- The excluded-minor and genus results are sketched and rest on cited
  decompositions; Remark 5.3 is a sketch.
- No lower bound shows any of the upper bounds tight, except where the
  paper notes ae must grow with genus.
- Slips in this preprint (my observations): Lemma 3.11 states
  C(X; 2∆, ∆/4) but the proof bounds by C(X; 6∆, ∆) and C(X; 8∆, ∆), which
  does not affect Corollary 3.12; the concentration in Theorem 1.12's proof
  is printed as |‖T_ω x‖₂ − ‖x‖₂| ≥ ½, which needs ‖x‖₂ = 1 or a relative
  form; Remark 5.3 sets ε = 1/n^{1/2−1/p} where m is meant and ends with
  exponent (2−p)/p² where Lemma 1.13's (p−2)/p² is right; Lemma 2.1's proof
  writes γ: Ω → T and the integrand d(γ(ω), x) where f(γ(ω)) is meant.
  Whether the journal version fixes them was not checked.

## Open questions

- The paper's own (§1.4): whether eₙ(X, Z) = O(√(log n)) for every metric
  space X and normed Z; whether e(L₂, L₁) < ∞; whether e(L_p, L_q) < ∞ for
  2 < p < ∞, 1 < q < 2; extension of large-scale Lipschitz, Hölder and
  uniformly continuous maps; higher-order Whitney extension.
- Whether log n/log log n is the right order for ae of n-point spaces.
  A lower bound above √(log n) for some Banach target would separate it
  from Hilbert targets; later literature on this is outside the record.
- Whether a single parameter interpolates between the separated-set bound
  4D/ε and log λ(X), since each wins on examples where the other fails
  (my observation).
