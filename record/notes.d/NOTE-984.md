---
number: 984
status: Read
formerly:
- NOTE-tmpuwro4
paper: 'LIT-1256'
title: 'Coifman and Maggioni — Diffusion wavelets'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the published version (Applied and Computational
    Harmonic Analysis 21(1): 53–94, the typeset Elsevier article, 42
    pages, in Elsevier's open archive) as posted on Naoki Saito's UC Davis
    page, the LIT's `url:`. Text extracted with pdftotext. Read: §§1–12
    in full, with the proofs of Proposition 22, Corollary 23, Proposition
    25 (which defers to Coifman and Meyer), Lemma 26, Theorems 27 and 29
    and Corollary 30. §§5–6 (orthogonalization algorithms, rank-revealing
    QR, complexity) and §§8–9 (examples, extension off the set) were read
    and are summarized more briefly. Displays garbled by extraction were
    checked against page renders of pp. 56, 58, 67, 80, 82 and 83. Figs.
    1, 2 and 9 were seen in renders; the others were read from captions
    and text. The nesting, the band structure, the dimension bound (4.12)
    and the errors listed under Limitations were re-checked by hand and
    with numpy scripts in the scratchpad (the circle example of §8.1 at
    n = 256 and 512, and a three-cluster example like §8.4).
date: '2026-10-20'
summary: >-
  A self-adjoint diffusion operator T with spectrum in [0, 1] defines a
  multiresolution analysis by thresholding its dyadic powers at a
  precision ε: V_j is spanned by the eigenvectors with λ^{t_j} ≥ ε, so the
  V_j are exactly nested spectral subspaces and the wavelet spaces W_j are
  spectral bands, about one octave of the generator each. The paper's
  contribution is an algorithm that builds localized orthonormal bases
  for approximations of these spaces without computing eigenvectors, by
  squaring the operator on each compressed basis. As written, that
  algorithm thresholds T^{2^{j−1}}, not T^{2^j−1} as the paper states, and
  the paper's own Fig. 9 follows the former. Localization, stability and
  the near-linear complexity are argued or observed, not proved for the
  compressed algorithm.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-331 THEORY-186 THEORY-257 — Proposed; open claims and accounts this reading bears on, nothing here rests on their being settled -->

# NOTE-984: Coifman and Maggioni — Diffusion wavelets

## Contribution

It lifts the Littlewood–Paley and wavelet constructions to graphs,
manifolds and point clouds. The dilation is a dyadic power of a diffusion
operator T. It states the spectral multiresolution analysis this induces:
approximation spaces V_j of "band-limited functions" and detail spaces W_j.
The new part is the algorithm. It builds orthonormal, roughly localized
bases of scaling functions for approximations of the V_j, together with
the downsampling matrices between levels and compressed matrices of
T^{2^j} on each level, without computing eigenvectors. These give a fast
scaling-function and wavelet transform and a multiscale representation of
the Green's function (I − T)^{−1} through the Schultz product
(I − T)^{−1} = Π_k (I + T^{2^k}) (1.1).

## Key insight

The scale of a diffusion multiresolution is set by the operator, not by a
partition of the space. "We use diffusion as a smoothing and scaling tool
to enable coarse graining." Powers of a smoothing operator lose numerical
rank, because their eigenvalues λ^t fall below any fixed precision one
after another. So the range of T^t at precision ε shrinks as t grows. It
can be represented on fewer, coarser basis functions, and the operator
"itself is dictating the geometry with respect to which it should be
analyzed". Each level is a spectral band. Localization is something the
construction adds to a basis of that band. It is not what defines the
level.

## Assumptions

- **§2, the discrete sketch.** X a finite weighted graph. T "symmetric
  positive definite and positive", ‖T‖₂ ≤ 1, and local: T(δ_k) has small
  support. "High powers of T have low numerical rank": ideally there is
  γ < 1 with Ran_ε(T^{2^j}) < γ Ran_ε(T^{2^{j−1}}) for every j.
  Self-adjointness is used in one place, to compute
  [T²]^{Φ₁}_{Φ₁} = M₀M₀* (§2.2, (4.16)).
- **§4, the general setting.** (X, ρ, μ) a space of homogeneous type
  (doubling: μ(B_{2δ}(x)) ≤ C_X μ(B_δ(x))), with diam X < ∞ for the
  theorems. {T^t} a symmetric diffusion semigroup (Definition 13):
  contractive on every L^p, self-adjoint, positivity-preserving, with
  T^t = e^{−tΔ} for Δ positive self-adjoint. So σ(T) ⊆ [0, 1] (Remark 14).
  Throughout §4.2 onward T is also compact, has γ-strong decay and acts
  η-locally.
- **γ-strong decay (Definition 16).** #{k : λ_k ≥ λ} ≤ C (log₂(1/λ))^γ for
  every λ ∈ (0, 1). For the heat semigroup on a compact d-dimensional
  manifold Weyl's law gives γ = d/2 (§7: "n/2-strong decay"). As printed
  the definition cannot hold for λ near 1 when λ₀ = 1, since the left side
  is at least 1 and the right side tends to 0; it is meant for small λ.
- **Theorem 27.** Dyadic cubes (Christ's construction, Theorem 6) on X;
  T acting δ_X^{J₀}-locally; an initial orthonormal basis Φ₀ that
  ε-spans V₀; and "uniform local finite-dimensionality": the ε-dimension
  of the restriction of Φ₀ to a cube, and to its boundary layer, is at
  most proportional to the cube's measure.
- **Theorem 29.** T maps exponentially decaying functions to
  exponentially decaying ones, and the initial basis decays exponentially
  from a well-spread center set.
- **Non-self-adjoint T.** Footnote 1 says the construction "can be
  immediately generalized" to directed graphs, and the abstract says
  "the symmetry of the operators and their spectral theory need not be
  considered". Remarks 17 and 32 restate it. Nothing in the paper carries
  it out (see Limitations).

## Key results

- **The precision notion (Definition 12).** A set {ξ_i} ε-spans {v_k} if
  ‖P_{⟨ξ⟩}v_k − v_k‖ ≤ ε for every k, and dim_ε is the least dimension of
  such a span. This is a per-vector criterion on a spanning set, not a
  distance between subspaces. The paper notes the "abuse of notation"
  itself.
- **The spectral multiresolution (§4.3).** With t_j = Σ_{l=0}^{j} 2^l =
  2^{j+1} − 1 (4.8), σ_j(T) = {λ ∈ σ(T) : λ^{t_j} ≥ ε} (4.9) and
  V_j = ⟨{ξ_λ : λ ∈ σ_j(T)}⟩ (4.10), with V_{−1} = L²(X). Stated
  properties: lim V_j = ⟨{ξ_i : λ_i = 1}⟩; V_{j+1} ⊆ V_j; the eigenvectors
  are an orthonormal basis of V_j. W_j is the orthogonal complement of
  V_{j+1} in V_j, so V_j = V_{j+1} ⊕⊥ W_j (4.11), and
  L²(X) = ⊕⊥_{j≥−1} W_j is "a wavelet decomposition of the space, induced
  by the diffusion semigroup, and related to the Littlewood–Paley
  decomposition studied in this setting by Stein". Nestedness needs only
  λ ∈ [0, 1] and t_j increasing, and it is exact. W_j is the band
  ε^{1/t_j} ≤ λ < ε^{1/t_{j+1}}. In generator units ν = −ln λ it is
  ln(1/ε)/t_{j+1} < ν ≤ ln(1/ε)/t_j, about one octave, since
  t_{j+1}/t_j → 2. No spectral decay is needed for any of this.
- **The dimension bound (4.12).** Under γ-strong decay,
  dim V_j ≤ C(2^{−j} log₂(1/ε))^γ = C 2^{−jγ} log₂^γ(1/ε). Re-derived:
  λ^{t_j} ≥ ε iff log₂(1/λ) ≤ log₂(1/ε)/t_j, and t_j ≥ 2^j. This is the one
  place where decay of the spectrum turns into compression.
- **Diffusion metric (§4.2).** d^{(t)}(x, y) = Σ_λ λ^t(ξ_λ(x) − ξ_λ(y))²
  = ‖T^{t/2}δ_x − T^{t/2}δ_y‖² (4.2) = K^t(x, x) + K^t(y, y) − 2K^t(x, y)
  (4.3). It is the square of a metric, though the paper calls it the
  metric. The eigenmap x ↦ (λ^{t/2}ξ_λ(x))_{λ∈σ′} is an isometry for the
  full spectrum (4.5). For a doubly stochastic K the top-n eigenvectors
  minimize the local distortion (4.6), which is Ky Fan's principle.
  Re-checked.
- **Proposition 22 (multiscale dyadic orthogonalization).** A local
  family Ψ that is uniformly locally finite-dimensional on dyadic cubes
  and their boundary layers has an orthonormal basis organized in layers
  l = 0, …, L, with every element supported in one cube Q_{J+l,k}. It
  (l + 1)ε-spans the part of Ψ supported in cubes of layer l, and the
  number of elements per cube is bounded by the cube's measure. Proof:
  orthonormalize inside the finest cubes, then at each coarser layer only
  the functions near cube boundaries, against what is already built. The
  cubes come from the space's geometry (Theorem 6), not from T. Corollary
  23 bounds the cost.
- **Proposition 25 (exponential localization).** A Riesz basis with an
  η-accretive Gramian whose entries decay exponentially in a metric with
  summable exponential tails has an orthonormalization whose coefficients
  decay exponentially. Proved by reference to Coifman and Meyer, §11.4.
  Lemma 26 supplies the summability on spaces of homogeneous type.
- **Theorem 27.** Under its assumptions there are orthonormal scaling
  bases Φ_j with V_j = ⟨T^{t_j}Φ₀⟩ ⊆ ⟨Φ_j⟩_{(j_X−j)ε}, each element
  supported in a dyadic cube Q_{J₀+j+l,k}, with counts per cube bounded
  by its measure. The proof applies Proposition 22 to
  Φ̃_j = T^{δ_X^j−1}Φ₀, using (P1) powers of T are contractions, so they
  do not raise ε-dimension; (P2) locality; (P3) preserved centers. Two
  things should be noticed. The theorem works from T^{t}Φ₀ directly, at
  each j separately, so it is not the compressed algorithm. And its V_j is
  the ε-span of the columns of T^{2^j−1}, which is not literally (4.10).
- **Theorem 29.** The same with exponential decay in place of compact
  support, via Proposition 25 applied to (T^{δ_X^j})_ε Φ₀ (the spectral
  truncation of Notation 11). Corollary 30 replaces the hypothesis on Γ by
  Γ being a lattice.
- **The compressed construction (§2.2, §4.6, Fig. 3).** Φ₀ = {δ_k}. At
  level j, T_j = [T^{2^j}]^{Φ_j}_{Φ_j}. A rank-revealing QR of T_j at
  precision ε gives Φ_{j+1} as orthonormal combinations of Φ_j, and
  M_j = [T^{2^j}]^{Φ_{j+1}}_{Φ_j}. Then T_{j+1} = M_j M_j* (4.16), "the only
  place where we use self-adjointness". The wavelets are an
  ε-orthonormalization of the columns of I − Φ_{j+1}Φ_{j+1}* on V_j
  (§4.7, §5.5). Scaling functions on X are recovered by multiplying the
  filters (2.1), (4.18).
  - *Nestedness is exact by construction.* Φ_{j+1} is written on Φ_j, so
    ⟨Φ_{j+1}⟩ ⊆ ⟨Φ_j⟩ whatever the truncation rule and whatever T. Checked:
    ‖Φ_{j+1} − Φ_jΦ_j*Φ_{j+1}‖ ≤ 2 × 10⁻¹⁴ at every level.
  - *What it thresholds.* Since Φ_j is orthonormal, the singular values of
    T_j on V_j are λ^{2^j}, not λ^{2^{j+1}−1}. The cumulative decay of the
    earlier factors is discarded at each orthonormalization. With exact
    truncation the computed spaces are
    Ṽ_j = ⟨ξ_λ : λ^{2^{j−1}} > ε⟩, and the record re-derives this by
    induction in [THEORY-758](../theory.d/THEORY-758.md). §5.4 instead says k = dim Ṽ_{j+1} is the
    count of λ_i^{2^{j+1}−1} ≥ ε, and Fig. 1 marks V₁, …, V₄ on the spectra
    of T, T³, T⁷ and T¹⁵. On the paper's own circle example (n = 512,
    ε = 10⁻⁴) the compressed dimensions are 486, 408, 317, 236, 170, 122,
    87, 62, …, 15 at j = 1, …, 12. The paper's count would give 479, 355,
    251, 177, …. Fig. 9's curve (read from a render) passes about 410, 310
    and 235 at j = 2, 3, 4, which matches the compressed count. The paper's
    count is that of Theorem 27's uncompressed route. Checked: the ε-rank
    of T^{2^j−1} itself is 239, 177, 125, 89, … at n = 256.
  - *How good the approximation is.* §2.2 says Φ₂ spans the range of T³
    "up to precision 2ε", and Theorem 27 has (j_X − j)ε, so errors are
    taken to add across levels. For the compressed scheme no bound is
    proved. In the check, ‖T^{2^j}Φ_j − Φ_jT_j‖ stayed at 2–7 × 10⁻⁵ for
    ε = 10⁻⁴ through j = 14. One step of T is another matter.
    ‖TΦ_j − Φ_jΦ_j*TΦ_j‖ reached 1.2 × 10⁻² at j = 4, because the pivoted
    QR keeps part of the eigenvectors that sit near the threshold and the
    circle's spectrum has no gap there.
- **Complexity (§§4.6, 5, 6).** In general O(n³). With fast spectral decay
  and locality: "O(n² log² n) or even O(n log² n)" (§5, intro). Proposition
  39 and Corollaries 40–41 say the whole construction and the transforms
  cost O(n^k) if each orthonormalization costs O(n^k), "usually k = 1, 2".
  That is a conditional restatement, not a complexity bound. "A detailed
  analysis of computational complexity is left to a forthcoming
  publication."
- **Orthogonalization algorithms (§5).** Modified Gram–Schmidt with
  pivoting (stop when the largest residual norm falls below ε/√|Ψ|). A
  greedy multiscale variant with "geometric pivoting". A mixed L²–L^p
  pivoting that prefers small supports. Strong rank-revealing QR (Gu and
  Eisenstat, p₁ = √(1 + nk(n − k)), p₂ = √n), giving Ṽ_{j+1} "up to error
  ε · p(k, n)". For the first two: "we cannot guarantee good bounds on the
  numerical stability"; and for L²–L^p, "we can construct quite artificial
  examples in which any choice of λ < 1 leads to loss of precision".
- **Examples (§§2.6–2.7, 8).** A dumbbell (1400 points). A corpus of 1047
  Science News articles. The circle (512 points, T = (T′)², ε = 10⁻⁴),
  where coarse scaling functions "tend to sine and cosine functions" and
  V₁₅ holds three. A one-dimensional non-homogeneous conductivity
  ("homogenized versions" of the operator; V₈ is two-dimensional). 500
  uniform points in a square. Three Gaussian clouds in ℝ³ (|X| = 1200,
  |X₃| = 186, |X₅| = 39), where "the top scaling functions in several
  scaling subspaces approximate very well the characteristic function of
  each cloud". Image patches. All are qualitative. No error, cost or
  timing is reported, except an L² error "of order 10⁻⁵" for one
  reconstructed eigenfunction (Fig. 13).
- **Extension off the set (§9).** Extend each scaling function by the SVD
  of the restriction operator from a nested family E_n (band-limited
  functions with geometric harmonics, a classical MRA, or Gaussian bumps)
  on the least n that captures it. Described, with one example (Fig. 18).
  Nothing is proved.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The spectral spaces V_j = ⟨ξ_λ : λ^{t_j} ≥ ε⟩ form a nested chain with V_j = V_{j+1} ⊕⊥ W_j, a Littlewood–Paley-type decomposition | strong | immediate from (4.8)–(4.11); re-derived; the sum ⊕W_j omits the λ = 1 eigenspace, which must be added |
| C2 | Under γ-strong decay, dim V_j ≤ C 2^{−jγ} log₂^γ(1/ε) | strong | (4.12), re-derived; the definition of strong decay needs restricting to small λ |
| C3 | Localized orthonormal scaling bases exist that ε-span V_j, supported in dyadic cubes, with counts bounded by the cubes' measure | moderate | Theorem 27 via Proposition 22, proved under the local finite-dimensionality hypotheses; for the uncompressed route only, with errors (j_X − j)ε |
| C4 | Exponentially localized scaling bases exist under exponential-decay hypotheses | moderate | Theorem 29, resting on a cited proposition of Coifman and Meyer |
| C5 | The compressed algorithm builds nested spaces Ṽ_j approximating V_j, with dim Ṽ_{j+1} = #{λ^{2^{j+1}−1} ≥ ε} up to p(k, n) | weak as stated | nestedness is exact by construction; the count is wrong for the algorithm as written, which thresholds λ^{2^j}, and Fig. 9 shows the latter; no bound on accumulated error is proved |
| C6 | The construction runs in O(n log² n) or O(n² log² n) for local operators with fast spectral decay | weak | asserted; Proposition 39 is conditional on its own premise; full analysis deferred |
| C7 | The orthogonalization schemes yield well-localized, numerically stable bases | weak | "we cannot guarantee"; observed in examples; counterexamples acknowledged for the L²–L^p rule |
| C8 | Coarse scaling functions on a document graph correspond to categories and topics, a "directory structure" | weak | five scaling functions described by their supports; one category (Biology) fails; details deferred to an unpublished report |
| C9 | The construction extends "immediately" to non-self-adjoint operators and directed graphs | weak | asserted in the abstract, footnote 1 and Remarks 17 and 32; the squaring step uses self-adjointness, and the spectral reading of V_j and W_j needs it; biorthogonal versions deferred |
| C10 | The Green's function (I − T)^{−1} can be applied in compressed form through the product of compressed dyadic powers | moderate | the identity (1.1) is exact on the complement of the λ = 1 eigenspace; the error of the compressed product is not bounded; the number of factors depends on the gap below 1 |

## Method

1. Fix ε. Represent T on Φ₀ = {δ_k}.
2. For j = 0, 1, …: factor T_j = [T^{2^j}]^{Φ_j}_{Φ_j} by a (sparse,
   locality-preserving) rank-revealing QR at precision ε. The kept
   orthonormal columns are Φ_{j+1}, written on Φ_j; M_j = Φ_{j+1}*T_j.
3. T_{j+1} = M_jM_j* (self-adjointness).
4. Wavelets Ψ_j: orthonormalize the columns of I − Φ_{j+1}Φ_{j+1}* on V_j,
   reorthogonalizing against the scaling functions.
5. Scaling-function and wavelet transforms: apply the filters level by
   level. Green's function: (I − T)^{−1}f ≈ Π_{k≤K}(I + T^{2^k})f.

## Concepts

- **ε-span and dim_ε** — per-vector approximation of a set of vectors,
  and the least dimension achieving it (Definition 12).
- **Approximation space V_j** — in §4.3 the span of eigenvectors with
  λ^{t_j} ≥ ε, "band-limited functions"; in Theorem 27 the ε-span of
  T^{t_j}Φ₀; in the algorithm the span of Φ_j. The three are treated as
  one, and they differ near the threshold and in the index (see
  Limitations).
- **Wavelet space W_j** — V_j ⊖ V_{j+1}, a band of the spectrum.
- **Layer** — within one V_j, the scaling functions come in layers l,
  whose supports grow like 2^l · 2^j. So one level holds functions of many
  spatial sizes, and the level index is not a spatial size.
- **Vanishing moments (§4.8)** — the number of eigenfunctions in the band
  σ_j \ σ_{j+1} to which T^{2^j}φ is orthogonal to precision ε. Moments are
  measured against the operator's eigenfunctions, not polynomials.
- **γ-strong decay** — the count of eigenvalues above λ grows like
  (log 1/λ)^γ.
- **Compressed graph X_j** — the centers of level-j scaling functions,
  with the metric d^{(t_j)}. Each point of X_j is "a 'local aggregation' of
  points in X_{j−1}, which is completely dictated by the action of the
  operator".

## Connections

The model is Stein's Littlewood–Paley theory for symmetric diffusion
semigroups, with the matrix compression of Beylkin, Coifman and Rokhlin's
non-standard form and the Fast Multipole Method seen "from a 'dual'
perspective": starting from the semigroup rather than from the Green's
operator. The dyadic cubes are Christ's and David's. The exponential
orthonormalization is from Coifman and Meyer. The uncertainty principles
that make eigenspaces approximable by bumps at the matching scale are
Nahmod's, cited and not proved here. Rank-revealing QR is Gu and
Eisenstat's. It is related to algebraic multigrid, H-matrices
(Hackbusch), and the low-rank compression of Cheng, Gimbutas, Martinsson
and Rokhlin, and contrasted with Sweldens' lifting, where a mesh
subdivision and not an operator sets the refinement. The diffusion metric
and eigenmaps are those of diffusion maps ([LIT-1246](../literature.d/LIT-1246.md), [NOTE-985](NOTE-985.md)),
cited as in press. Biorthogonal diffusion wavelets and diffusion wavelet
packets are companion reports. The Leeb–Coifman multiscale diffusion
distance used in [NOTE-675](NOTE-675.md) takes its dyadic times from here.

## Bearing on the record

- **[QUESTION-217](../questions.d/QUESTION-217.md).** The paper is the dyadic, multilevel form of the
  case [THEORY-745](../theory.d/THEORY-745.md) already holds for diffusion maps, and it settles
  what the levels are.
  - *Refinement.* The levels are an exact chain, V_{j+1} ⊆ V_j, ordered by
    eigenvalue, and the order costs nothing. The spectral V_j need only
    λ ∈ [0, 1]. The computed Ṽ_j are nested by construction, for any T. So
    a nested chain is the easy part. What spectral decay buys is
    compression, (4.12) and the γ < 1 shrinkage, not nesting. Without
    decay the chain still exists and simply does not shrink.
  - *What a level is.* Each W_j is a spectral band of about one octave in
    the generator's eigenvalue. Spatial blocks enter only through the basis
    chosen inside the band: the dyadic cubes of Theorem 27, or the pivoting
    rules of §5. They come from the space's geometry or from the
    algorithm, and they do not define the level. Within one V_j the layers
    run over many spatial sizes. So "coarse" here means low in the
    spectrum, and "localized" is a separate property that the band may or
    may not allow.
  - *Acquisition.* Applying T^{2^j} is the diffusion's own time evolution,
    so the operator suppresses the levels in the same order as it refines
    them, as in [THEORY-745](../theory.d/THEORY-745.md). Both orders come from one eigenbasis, so
    this is again Conjecture A's commuting case: every V_j is
    T-invariant, so [T, P_{V_j}] = 0 exactly.
  - *The dyadic schedule is a choice.* "The choice of the factor 2 is
    arbitrary". Remark 33 allows any polynomial m_j in place of squaring.
    The chain is fixed by the order of λ, but where the cuts fall is not.
  - [THEORY-758](../theory.d/THEORY-758.md) (Active) records the exact chain, the bands, the
    corrected count for the compressed algorithm and the closure.
- **[QUESTION-218](../questions.d/QUESTION-218.md).** Are the coarse scaling functions units? The
  reading says no, not as such.
  - What is canonical at level j is the subspace V_j. It is T-invariant,
    so the coarse variable y = Φ_j*x of x_{t+1} = Tx_t + noise closes
    exactly, y_{t+1} = (Φ_j*TΦ_j)y_t + Φ_j*·noise. That is [THEORY-733](../theory.d/THEORY-733.md)'s p = 1
    criterion with A = Aᵀ = T. A symmetric T has invariant subspaces at
    every dimension, which [THEORY-733](../theory.d/THEORY-733.md) notes a general VAR(1) need not
    have. Each V_j is a closed collective-mode space of the kind
    [CLAIM-388](../claims.d/CLAIM-388.md) describes, and the hierarchy is a nested chain of them.
  - A single scaling function is not closed: Tφ_{j,k} is not a multiple of
    φ_{j,k}. Closure belongs to the space, not to its basis elements. The
    basis is "quite arbitrary". Any orthonormal basis of V_j spans the same
    closed space, and the eigenvectors are its delocalized basis.
  - When the spectrum has a gap that isolates metastable clusters, a basis
    of near-indicators exists inside V_j. The paper's three-cloud example
    shows this, and it is [CLAIM-157](../claims.d/CLAIM-157.md)'s block. A check here, with three
    tight Gaussian clouds (eigenvalues 1, 0.9995, 0.9994, then 0.33), found
    that the three-dimensional Ṽ_j at levels 5–9 had pivoted-QR scaling
    functions each carrying at least 98% of its mass on one cloud, while
    the eigenvectors of the same space carried 36%, 50% and 68%. At levels
    10–14 the space was the same (principal-angle sine 10⁻⁴), but the
    algorithm's basis delocalized to 50–73%. The localized basis still
    existed, and the greedy pivoting stopped finding it as the powers
    became dominated by λ₀. Without a gap (the circle) the coarse basis
    tends to sines and cosines and no localized basis exists. So the
    scaling functions are units only where a gap makes block indicators
    lie in the band, and even then only under a pivoting rule that finds
    them. This supports the question's distinction: closure is a property
    of the subspace (the mode), and blockhood is a property of a basis
    that a gap may or may not supply.
- **[THEORY-745](../theory.d/THEORY-745.md).** Consistent. V_j is the span of the diffusion-map
  coordinates retained at t = t_j with an absolute threshold ε. Its
  nesting in j is that entry's nesting in t, and V_j's dyadic times are
  that entry's steps. Diffusion wavelets add the bands W_j, a localized
  basis for each level, and compressed powers.
- **[CLAIM-164](../claims.d/CLAIM-164.md).** The construction uses a threshold, never a gap, and the
  check shows the cost. Near a gapless threshold the computed space is not
  the spectral one: it is invariant under T^{2^j} to about ε and under T
  only to about 10⁻². A stable level needs a gap, as [CLAIM-164](../claims.d/CLAIM-164.md) says.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** Coarse levels are the slowest modes. The homogenization
  example of §8.2 reads the compressed powers as "homogenized versions, at
  a certain scale which is time and space dependent, of the original
  operator". It is an instance of the temporal facet of a level, and not
  a test of it, since slowness and coarseness are defined by the same
  eigenvalues here.
- **[THEORY-661](../theory.d/THEORY-661.md).** Simon's near-decomposability is the gapped case. When
  T has metastable blocks, the bands below the gap carry block
  indicators. The paper does not state this, and proves nothing about gaps.
- **[QUESTION-222](../questions.d/QUESTION-222.md) (memory, Mori–Zwanzig).** Indirect. Because V_j is
  exactly invariant for symmetric T, the projected dynamics need no memory
  term. The compressed algorithm's approximate V_j have a residual
  coupling, of order the threshold under T^{2^j}, which the paper does not
  bound. That residual is the place where a memory kernel would enter.
- **The anthology.** It carries no instruction for machine-learning
  practice. It is a multiscale representation for graphs and point
  clouds, with applications to learning sketched in §12, so an anthology
  topic could hold it, as for diffusion maps. The LIT now carries the
  `anthology-candidate` flag.

## Limitations

- **The index of the spectral spaces is inconsistent.** (4.8)–(4.10) put
  V₀ = ⟨λ ≥ ε⟩ (t₀ = 1). §4.6 calls the ε-range of T "V₁". Theorem 27's
  proof uses T^{δ_X^j−1}, so V₀ is everything and V₁ the range of T, and
  Fig. 1 labels V_j on the spectrum of T^{2^j−1}. The construction matches
  t = 2^j − 1 for V_j, not (4.8)'s 2^{j+1} − 1.
- **The compressed algorithm thresholds T^{2^{j−1}}, not T^{2^j−1}.**
  Squaring T_j on an orthonormal basis forgets how far earlier factors had
  already shrunk each direction. §5.4's k = #{λ^{2^{j+1}−1} ≥ ε} and Fig. 1
  describe the uncompressed route, and Fig. 9 shows the compressed one.
  Every level still keeps an octave band, so the hierarchy keeps its form.
  But each level is about one level less compressed than stated: the
  exponent is about half. The stated count could be recovered by
  thresholding the cumulative power, keeping the singular values from one
  level to the next instead of discarding them. The paper does not do
  this. (A smaller mismatch: §8.1 puts three functions in V₁₅. The
  compressed count here gives five at j = 15 and three at j = 16.)
- **"dim_ε(TΦ₀) = dim Ran_ε(T) = #{λ ≥ ε}" (§4.6) holds only as an
  inequality.** With the per-column criterion of Definition 12, the
  spectral span gives dim_ε ≤ #{λ ≥ ε}. Each column's residual is at most
  ε, and it can be smaller. With §5.1's Frobenius-type stopping rule, a
  long tail of eigenvalues just below ε can force more. Rank-revealing QR
  agrees with the operator-norm count only up to p(k, n).
- **The sum of the W_j omits the top eigenspace.** L²(X) = ⊕_{j≥−1}W_j
  holds only after the λ = 1 eigenspace lim V_j is added. (ii) says "for
  every j ∈ ℤ" for spaces defined only for j ≥ −1.
- **"Diffusion metric" (4.2) is a squared distance.** It is ‖·‖², and it
  does not satisfy the triangle inequality as written.
- **§2.7's embedding uses the wrong eigenvalues.** It weights ξ_i by
  λ_i^{t/2} where λ_i are the eigenvalues of the Laplacian L (with
  λ₀ = 0). Those weights favour rough modes. The eigenvalues of T = I − L,
  (1 − λ_i)^{t/2}, are meant.
- **§7's normalization is not the one it cites.** K̃(x, y) = K(x, y)/p_δ(y)
  divides by the density at one end only, and K̄ divides by the square
  root of ∫K̃(x, y)p(y)dy. As printed, K̄ is neither symmetric nor
  averaging, though the text says the normalization makes it "averaging"
  and the construction assumes a self-adjoint T. It is also not
  Coifman–Lafon's α = 1 kernel, which divides by the density at both ends
  before row-normalizing ([NOTE-985](NOTE-985.md)).
- **Theorem 27 and the algorithm differ.** The theorems with proofs
  (27, 29) build each level from T^{t_j}Φ₀ directly. The compressed
  multiscale scheme, which is the paper's practical contribution and the
  source of its complexity claims, has no error theorem. Its localization
  depends on pivoting heuristics that are not guaranteed.
- **Complexity is not proved.** Proposition 39 assumes its conclusion
  step by step. The O(n log² n) figures are expectations, and the paper
  defers the analysis.
- **Non-self-adjoint operators are asserted, not treated.** Exact ranges
  of powers are nested for any operator, so the nesting survives. But the
  squaring step (4.16) uses T = T*. The band reading of W_j and the
  orthogonality of V_{j+1} ⊕ W_j need a spectral theorem, and for a
  non-normal T the ε-ranks of powers follow singular values, which can
  grow transiently. The biorthogonal construction is deferred.
- **The examples are qualitative.** The document "directory structure",
  the denoising of images and the extension off the set are illustrated
  and not measured.
- **Garbled or unseen.** Figs. 4–8 and 10–18 were read from captions and
  text. The proofs of Proposition 22 and Corollary 23 had several
  extraction-garbled subscripts. Their structure is clear, and the
  constants were not re-checked.

## Open questions

- Is there an error bound for the compressed algorithm across levels, in
  terms of ε, the level and the spectral gaps at the thresholds? The
  check suggests the error under T^{2^j} stays near ε while invariance
  under T fails near a gapless threshold. A bound of the form
  ‖P_{Ṽ_j} − P_{V_j}‖ ≤ (something)·ε/gap_j would settle what a level is
  numerically ([CLAIM-164](../claims.d/CLAIM-164.md)).
- When does a band V_j contain a basis of localized near-indicators, and
  does some pivoting rule provably find it? A positive answer would say
  when operator-induced levels have units ([QUESTION-218](../questions.d/QUESTION-218.md)). The
  candidate condition is a gap isolating metastable sets, Nahmod-type
  uncertainty bounds being the tool the paper points to.
- For a non-reversible operator, do the ranges of dyadic powers still
  give a chain whose levels can be read as bands, of singular values or
  of a Schur form? The biorthogonal diffusion wavelets (Maggioni, Bremer,
  Coifman and Szlam 2005) are the next reading.
- Does an externally given hierarchy (a tree of clusters) agree with the
  diffusion levels when T nearly commutes with its projectors? This is
  [QUESTION-217](../questions.d/QUESTION-217.md)'s open half. The paper treats only the commuting case.
