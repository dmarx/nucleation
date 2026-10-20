---
status: Read
paper: LIT-tmpc7k0w
title: 'Coifman and Lafon — Diffusion maps'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the published version (Applied and Computational
    Harmonic Analysis 21(1): 5–30, the typeset Elsevier article, 26 pages,
    in Elsevier's open archive) as posted on Thomas Strohmer's UC Davis
    course page, the LIT's `url:`. Text extracted with pdftotext. Read:
    §§1–7, Appendix A (the spectral decomposition and diffusion distance)
    and Appendix B in full (Lemmas 6–9, Proposition 10 = Theorem 2,
    Proposition 11 = Proposition 3, with their proofs). Equations garbled
    by extraction were checked against page renders of pp. 15, 17, 18, 21
    and 29, which hold every display quoted below. Fig. 5 was seen in a
    render; Figs. 1–4, 6, B.1 and B.2 were read from captions and text.
    The identities, the corrected truncation bound, the α-family limit and
    the errors listed under Limitations were re-checked by hand and with a
    numpy script in the scratchpad.
date: '2026-10-20'
summary: >-
  A symmetric non-negative kernel normalized into a reversible Markov
  chain gives a family of diffusion distances D_t, one per number of
  steps t, and an embedding by eigenvectors weighted by λ_l^t in which
  Euclidean distance is D_t. An α-normalization by a kernel density
  estimate makes the small-bandwidth limit the graph Laplacian with a
  density potential (α = 0), the Langevin generator whose invariant
  density is the sampling density (α = 1/2) or the Laplace–Beltrami
  operator (α = 1). The truncation is claimed accurate to relative
  precision δ, which is wrong: the bound is absolute. Several displays
  carry errors, and the heat-kernel proof has a gap.
---
<!-- inactive-ok-file: NOTE-784 — Skimmed; the earlier reading whose phrase is checked here -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-331 THEORY-186 THEORY-481 — Proposed; open claims and accounts this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-tmp3j6t7 — Proposed; the account filed from this reading -->
<!-- inactive-ok-file: LIT-tmptogwd — Deferred; works registered unread, cited as open -->

# NOTE-tmpv8yf2: Coifman and Lafon — Diffusion maps

## Contribution

It is the full-length companion to the 2005 PNAS announcement
([LIT-981](../literature.d/LIT-981.md)), and it carries the proofs that the PNAS paper deferred. From a
symmetric, non-negative affinity it builds a reversible random walk. It
defines a diffusion distance D_t at each number of steps t, and shows that
D_t is the Euclidean distance between points mapped by the walk's
eigenvectors weighted by λ_l^t. It then introduces a one-parameter family
of normalizations, indexed by α, and proves that as the kernel bandwidth ε
goes to 0 the walk's generator converges, on band-limited functions, to
an explicit operator. The family separates the geometry of a sampled
manifold from the density of the samples.

## Key insight

A graph's local affinities, iterated, give a geometry at every scale.
Two points are close at scale t when their t-step transition distributions
are close, which is when many short paths join them. The spectrum of the
one-step operator controls all of these scales at once: the t-th geometry
weights eigenvector l by λ_l^t, so as t grows the fine (fast-decaying)
modes drop below any fixed threshold and the embedding loses dimensions.
"In addition to being the time parameter, t plays the role of a scale
parameter." The geometry is not imposed by a partition. It is read off the
operator, and the order in which detail is lost is the order of |λ_l|.

## Assumptions

- **§2, the general construction.** (X, μ) a measure space and
  k: X × X → ℝ with k(x, y) = k(y, x) and k(x, y) ≥ 0. Unlike the PNAS
  paper, positive semi-definiteness is not required, so eigenvalues may
  be negative, and the ordering and truncation use |λ_l|. The graph is
  assumed connected and k(x, x) > 0 (aperiodicity, footnote 4). For an
  infinite X, the spectral decomposition needs A to be Hilbert–Schmidt
  (Appendix A).
- **§3 and Appendix B, the α-family.** X is all of a compact C^∞
  submanifold M ⊂ ℝⁿ of dimension d, possibly with a smooth boundary
  (Neumann conditions). The sampling density q is smooth and positive.
  The kernel is k_ε(x, y) = h(‖x − y‖²/ε) with h of exponential decay,
  normalized to zeroth moment m₀ = 1 and second moment m₂ = 2. The
  convergence holds on E_K, the span of the first K + 1 Neumann
  eigenfunctions of Δ, for fixed K.
- **Sign convention.** Δ is the Laplace–Beltrami operator taken positive
  semi-definite, Δf = −Σ ∂²f̃/∂s_i² in normal coordinates (Appendix B). One
  display in §3.3 silently uses the opposite convention (see Limitations).
- **§5.** The samples are i.i.d. with density q on M. For noise, the
  points lie within a small perturbation η of M.

## Key results

- **The walk (§2.1, §2.3).** d(x) = ∫ k(x, y) dμ(y), p(x, y) = k(x, y)/d(x).
  It has stationary distribution π(y) = d(y)/Σ_z d(z), and it is
  reversible: π(x)p(x, y) = π(y)p(y, x) (1). Under the assumptions,
  1 = λ₀ > |λ₁| ≥ |λ₂| ≥ ….
- **Diffusion distance (§2.4).**
  D_t(x, y)² = ‖p_t(x, ·) − p_t(y, ·)‖²_{L²(X, dμ/π)}
  = ∫ (p_t(x, u) − p_t(y, u))² dμ(u)/π(u), with t ∈ ℕ a number of steps.
- **The spectral identity (Appendix A).** The conjugate
  a(x, y) = √π(x)/√π(y) · p(x, y) is symmetric, with eigendecomposition
  a = Σ λ_l φ_l(x)φ_l(y) and φ_l orthonormal in L²(X, dμ). Then
  p_t(x, y) = Σ λ_l^t ψ_l(x)φ̃_l(y) (A.1), and
  D_t(x, z)² = Σ_{l≥1} λ_l^{2t} (ψ_l(x) − ψ_l(z))². The paper prints
  ψ_l = φ_l/π and φ̃_l = φ_l π. The correct factors are √π, and only
  they give its own ψ₀ = 1 (checked numerically: with φ_l/π the "constant"
  eigenvector varies by 3.8 on a 60-point example).
- **The diffusion map and Proposition 1 (§2.4).**
  Ψ_t(x) = (λ₁^t ψ₁(x), …, λ_s^t ψ_s(x)), with
  s(δ, t) = max{l : |λ_l|^t > δ|λ₁|^t}. "Ψ_t embeds the data into the
  Euclidean space ℝ^{s(δ,t)} so that in this space, the Euclidean distance
  is equal to the diffusion distance (up to relative accuracy δ)." With
  the full expansion it is exact. With the truncation, what holds is
  0 ≤ D_t² − ‖Ψ_t(x) − Ψ_t(y)‖² ≤ δ²|λ₁|^{2t} (1/π(x) + 1/π(y)) on a
  finite set with counting measure. That bound is absolute, not relative
  to D_t, and the relative error can approach 1 ([THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md)).
- **Scale (§2.2, §2.5, Fig. 1, Fig. 3).** The number of retained
  coordinates s(δ, t) falls as t grows, because |λ_l/λ₁|^t falls. On 900
  points in three clusters (Gaussian kernel, ε = 0.7), P^8 shows three
  blocks, P^64 two and P^1024 one, which is numerically rank one with
  p_1024(x, y) ≈ π(y). "The very notion of a cluster from a random walk
  point of view is a region in which the probability of escaping this
  region is low." No spectral gap is stated or used anywhere in the
  paper. The truncation is a threshold on |λ_l|^t, not a cut at a gap.
- **The α-family (§3.1).** q_ε(x) = ∫ k_ε(x, y)q(y) dy,
  k_ε^(α)(x, y) = k_ε(x, y)/(q_ε(x)^α q_ε(y)^α),
  d_ε^(α)(x) = ∫ k_ε^(α)(x, y)q(y) dy,
  p_{ε,α}(x, y) = k_ε^(α)(x, y)/d_ε^(α)(x), and
  P_{ε,α}f(x) = ∫ p_{ε,α}(x, y)f(y)q(y) dy.
- **Theorem 2 (proved as Proposition 10).** With L_{ε,α} = (I − P_{ε,α})/ε,
  for fixed K, on E_K,
  lim_{ε→0} L_{ε,α} f = Δ(f q^{1−α})/q^{1−α} − (Δ(q^{1−α})/q^{1−α}) f.
  With φ = f q^{1−α}, this is the Schrödinger operator
  Δφ − (Δ(q^{1−α})/q^{1−α})φ. The remainder is R_ε = O(ε) without boundary
  and, as printed, O(ε^γ) for any γ ∈ (0, 1/2) with boundary. Written with
  q = e^{−U}, the limit is Δf + 2(1 − α)⟨∇U, ∇f⟩: the generator of a
  reversible diffusion with drift −2(1 − α)∇U and invariant density
  proportional to q^{2(1−α)}. The paper does not write it this way; the
  record derives it in [THEORY-tmp3j6t7](../theory.d/THEORY-tmp3j6t7.md), and the numerical check is
  there.
- **α = 0 (§3.2).** The ordinary normalized graph Laplacian on isotropic
  weights converges to Δφ − (Δq/q)φ. This is the Laplace–Beltrami operator
  only for uniform q, which agrees with Belkin's result. Footnote 6: the
  scheme "cannot really be used to approximate Δ as the slightest
  nonconstant mode in q is amplified in the factor Δq/q".
- **α = 1/2 (§3.3).** The limit is Δφ − (Δ√q/√q)φ, which the paper relates
  by conjugation, citing Nadler et al., to the forward Fokker–Planck
  equation ∂q/∂t = ∇·(∇q + q∇U) of the Langevin dynamics
  ẋ = −∇U(x) + √2 ẇ (2). Acting on f, the limit is Δf + ⟨∇U, ∇f⟩, minus
  the backward generator of (2). So [LIT-981](../literature.d/LIT-981.md)'s "backward Fokker–Planck"
  and this paper's "forward" are the same operator seen from its two
  sides. The paper's expanded display, Δφ − (‖∇U‖²/4 − ΔU/2)φ, is wrong
  under the paper's own convention (see Limitations).
- **α = 1 (§3.4, Proposition 3 = Proposition 11).** lim L_{ε,1} = Δ, and
  for every t > 0, lim_{ε→0} P_{ε,1}^{t/ε} = e^{−tΔ} on L²(M). "This
  normalization removes all influence of the density and recovers the
  Riemannian geometry of the data set." In Fig. 4, curves sampled
  non-uniformly embed as circles with arclength recovered at α = 1, and
  with corners at dense regions at α = 0.
- **Two scale parameters.** ε sets the kernel's width (locality); t counts
  steps. In the limit, t steps of P_{ε,1} approximate heat time τ = tε,
  so P_{ε,1}^{τ/ε} → e^{−τΔ}. The eigenvalues e^{−τν_l²} pass the
  threshold δ while ν_l² < log(1/δ)/τ, so the resolution length is of
  order √(τ/log(1/δ)). That reading is the record's; the paper says only
  that t "plays the role of a scale parameter" and links the count of
  significant eigenvalues to Weyl's law heuristically (§2.5–2.6).
- **Finite samples (§5).** From Hein, Audibert and von Luxburg, and then
  Singer: |P̄_{ε,α}f(x_i) − P_{ε,α}f(x_i)| = O(m^{−1/2} ε^{−d/4+1/2}) with
  high probability, hence |L̄_{ε,α}f − L_{ε,α}f| = O(m^{−1/2} ε^{−d/4−1/2}).
  Criterion 4: m "must grow faster than ε^{−d/4−1/2}". That exponent is
  half the one the bound implies (see Limitations). For noise of size
  ‖η‖ (Criterion 5), P̃_{ε,α} = P_{ε,α} + O(‖η‖/√ε), which is valid while √ε
  exceeds the perturbation. Weyl's theorem then bounds the eigenvalue
  shifts.
- **Directed diffusion (§4).** k_ε(x, y) = exp(−‖x − y‖²/ε − ⟨∇f, x − y⟩²/ε²)
  penalizes steps across the level sets of f. The limit diffusion runs
  along the level sets, which is cited to Lafon's thesis and not proved
  here. On S² with f = sin(12θ), the first nontrivial eigenfunction is
  cos θ (Fig. 5).
- **Combining scales (§6).** Commute time (Fouss et al.) and
  absorption-based classification of partially labelled data via harmonic
  measure (a Dirichlet problem solved through Kakutani's theorem) are
  described as ways to use all t at once. Nothing is proved and no
  numbers are given.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For the reversible walk built from a symmetric non-negative kernel, D_t equals the Euclidean distance between the full eigenvector expansions weighted by λ_l^t, and D_t is a metric | strong | Appendix A; exact, up to the √π misprint, re-derived in [THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md) |
| C2 | Truncating to the s(δ, t) eigenvectors whose λ_l^t exceeds δλ₁^t in modulus keeps D_t "up to relative accuracy δ" | weak as stated | no proof given; the true bound is absolute, δ²λ₁^{2t}(1/π(x) + 1/π(y)), and the relative error reached 0.985 at δ = 0.05 in a check here |
| C3 | The number of significant eigenvalues, and so the embedding's dimension, falls as t grows, and t acts as a scale | strong | follows from the definition of s(δ, t); Figs. 1 and 3 illustrate |
| C4 | As ε → 0 the α-normalized generator converges on band-limited functions to Δ(fq^{1−α})/q^{1−α} − (Δq^{1−α}/q^{1−α})f | moderate | Proposition 10, proved; the interior expansion is sound, the boundary remainder is misstated (O(ε^{γ/2}) in L², not O(ε^γ)), and the convergence rests on Lemma 8 |
| C5 | With α = 1, P_{ε,1}^{t/ε} converges to the Neumann heat kernel e^{−tΔ}, independent of the density | moderate | Proposition 11; the conclusion is standard, but the proof's semigroup step does not follow as written (see Limitations) |
| C6 | The ordinary graph Laplacian (α = 0) approximates Laplace–Beltrami only for uniform density, and the density term can dominate | strong | follows from C4; footnote 6 and Fig. 4 |
| C7 | α = 1/2 recovers the Fokker–Planck (Langevin) dynamics whose equilibrium the samples are drawn from | strong for the operator, given C4 | §3.3 and the conjugation it cites from Nadler et al.; the expanded display has a sign error |
| C8 | All kernel eigenmap methods (LLE, Laplacian, Hessian eigenmaps, LTSA) are special cases of diffusion maps | weak | §2.7 shows only that they solve a generalized eigenproblem Q₁f = λQ₂f; for fourth-order forms such as the Hessian's, e^{−tQ₂⁻¹Q₁} is not positivity-preserving, so it is not a Markov diffusion |
| C9 | The diffusion distance is "very robust to noise perturbation, unlike the geodesic distance" | weak | asserted in §2.4; §5's perturbation argument concerns P and its eigenvalues, not D_t; Fig. 6 is one illustration |
| C10 | To reach a given precision, m must grow faster than ε^{−d/4−1/2} | weak; the exponent is wrong | Criterion 4, from the error bound cited from Singer, which implies m ≫ ε^{−d/2−1} |
| C11 | An f-adapted anisotropic kernel gives diffusion along the level sets of f | weak here | cited to Lafon's thesis; one example (Fig. 5) |

## Method

1. Choose a symmetric, non-negative affinity k (for points in ℝⁿ, a
   rotation-invariant kernel of width √ε).
2. For data on a manifold, optionally renormalize by the kernel density
   estimate, k^(α) = k/(q_ε^α q_ε^α), with α = 1 to remove the density.
3. Row-normalize to the Markov matrix P.
4. Diagonalize through the symmetric conjugate and keep the
   eigenvectors with |λ_l|^t > δ|λ₁|^t.
5. Embed by Ψ_t(x) = (λ_l^t ψ_l(x))_{l=1..s(δ,t)}.

## Concepts

- **Diffusion distance D_t.** The L²(dμ/π) distance between the t-step
  transition distributions from x and from y. By reversibility it equals
  p_{2t}(x, x)/π(x) + p_{2t}(y, y)/π(y) − 2p_{2t}(x, y)/π(y), so it counts
  paths of length 2t (the record's identity, not the paper's).
- **Diffusion map Ψ_t.** The truncated embedding by λ_l^t ψ_l. "Each
  component of Ψ_t(x) is termed diffusion coordinate."
- **Scale.** Here t is a number of steps of P, and is "a scale parameter".
  The kernel width ε is a second, independent scale. In the manifold limit
  their product is a heat time.
- **α-normalization.** Division of the kernel by the α-th power of a
  kernel density estimate at both ends before row-normalizing. α sets
  "the amount of influence of the density in the infinitesimal
  transitions".
- **"Heisenberg principle" (§2.6).** The informal statement that rows of
  P^t are bumps whose width grows with t. Fewer eigenfunctions then
  synthesize them, and the eigenfunctions near λ = 1 are the smooth ones.
  Nothing is proved.
- **Directed diffusion.** Diffusion made anisotropic by a function's
  gradient. As in the PNAS paper, it is not a non-reversible chain.

## Connections

The construction is Chung's normalized graph Laplacian and the "symmetric
diffusion semi-groups" of Stein. The paper places Laplacian eigenmaps
(Belkin and Niyogi), LLE, Hessian eigenmaps and LTSA beneath it, and takes
the L¹ transition distances of Szummer and Jaakkola and the PageRank
family as precursors. The proofs extend Lafon's thesis from hypersurfaces
to submanifolds. The finite-sample rates are cited from Hein, Audibert and
von Luxburg (2005) and Singer (2005), and the α = 1/2 case from Nadler,
Lafon and Coifman in the same issue. The PNAS announcement is [LIT-981](../literature.d/LIT-981.md)
([NOTE-784](NOTE-784.md), Skimmed), and diffusion wavelets ([LIT-tmptogwd](../literature.d/LIT-tmptogwd.md), unread) is the
multiscale companion the paper cites for compressing P^t. Zhai ([LIT-975](../literature.d/LIT-975.md),
§5.3) identifies his power-kernel metric with D_t. [NOTE-675](NOTE-675.md) uses the
Leeb–Coifman multiscale diffusion distance that descends from it.

## Bearing on the record

- **[LIT-981](../literature.d/LIT-981.md) and [NOTE-784](NOTE-784.md).** This paper settles what [NOTE-784](NOTE-784.md) could not
  see. (i) The α-family is proved here (Proposition 10), not only
  announced. (ii) "Backward Fokker–Planck" for α = 1/2 is right for the
  operator acting on f, and this paper's "forward" is its conjugate. The
  α = 0 statement in [NOTE-784](NOTE-784.md) (potential 2U) also checks out: the limit is
  Δf + 2⟨∇U, ∇f⟩. (iii) This paper drops the PNAS requirement that k be
  positive semi-definite. (iv) The phrase "an empirical method for
  homogenization" is the PNAS paper's and does not occur here. The
  nearest wording is "the classical Newtonian paradigm in which local
  infinitesimal rules of transition of a system lead to global
  macroscopic descriptions by integration". [NOTE-784](NOTE-784.md)'s open question "a
  close reading ... together with Coifman and Lafon's companion paper" is
  answered by this NOTE.
- **[QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md).** The paper is a clean case of a coarse-to-fine
  order induced by an operator rather than an imposed partition, and it
  shows exactly what such an order is.
  - *Refinement.* With the threshold δ fixed, the truncated maps are
    nested: for t′ ≥ t, Ψ_{t′} is a diagonal rescaling of the first
    s(δ, t′) coordinates of Ψ_t, so σ(Ψ_{t′}) ⊆ σ(Ψ_t) ([THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md)).
    Without truncation, and with no zero eigenvalue, every Ψ_t is an
    invertible linear image of every other. Then t changes only the
    metric's weights and coarsens nothing. So the refinement order
    exists only through the threshold, and it is the order of |λ_l|.
  - *Acquisition.* If "acquisition" means applying the same operator
    repeatedly (power iteration, or heat flow e^{−τΔ}), the order in which
    modes survive is again |λ_l|. Refinement and acquisition then coincide
    by construction, because both are read from one eigenbasis. This is
    Conjecture A's commuting case, [A, P_ℓ] = 0 exactly, with the levels
    P_ℓ taken as the operator's own spectral projectors. It does not reach
    the question's real case, an externally given hierarchy whose
    projectors only nearly commute.
  - *Relevance.* Nothing in §§2–3 refers to a target. Relevance enters only
    if the kernel is built for it (§4's f-directed kernel, whose slow
    modes are constant on f's level sets) or in §6's label-absorbing walk.
    So the paper gives a way to make the operator order equal a chosen
    relevance order by design. It gives no condition under which they
    agree when the kernel is not chosen for the target.
  - *Density versus geometry.* The α-family shows that the operator's
    order itself depends on a normalization choice. The same samples give
    different slow modes at α = 0 and α = 1 (Fig. 4: corners against a
    circle). An "operator-induced order" is not a property of the data
    alone.
- **[CLAIM-164](../claims.d/CLAIM-164.md) and the spectral-gap entries.** The paper never uses a gap.
  s(δ, t) is a threshold on |λ_l|^t. [CLAIM-164](../claims.d/CLAIM-164.md) sharpens this: when the
  threshold falls inside a cluster of nearly equal |λ_l|, the retained
  coordinate set is not stable under perturbation, though the truncated
  distance error stays within the bound. A stable truncation cuts at a
  gap, and then the retained span is the gap-isolated subspace. Fig. 1's
  clusters, which merge as t grows, are the metastable blocks of
  [CLAIM-157](../claims.d/CLAIM-157.md)'s kind: a cluster is "a region in which the probability of
  escaping this region is low". But the paper offers this as an
  illustration and proves no link between gaps and clusters. That link is
  in Nadler et al. and the spectral-clustering literature, not here.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** At large t only the slowest modes survive, and P^1024 is
  rank one. The coarse description here is literally the slow one. This
  is an instance of the claim's temporal facet for a reversible walk, in
  which slowness and coarseness are the same spectral fact. It does not
  test whether slowness marks a level elsewhere.
- **[THEORY-186](../theory.d/THEORY-186.md), [THEORY-086](../theory.d/THEORY-086.md) and [THEORY-481](../theory.d/THEORY-481.md).** Those entries order
  acquisition by an operator's eigenvalues: singular values, NTK
  eigenvalues, input variances. Diffusion maps order coarseness by the
  same kind of quantity. The record could say that each of these is a
  case where refinement and acquisition coincide because the levels are
  defined spectrally, and that [THEORY-186](../theory.d/THEORY-186.md)'s fine-first case arises when
  the spectral order is not the order of an independently given tree.
- **[THEORY-478](../theory.d/THEORY-478.md) and [QUESTION-160](../questions.d/QUESTION-160.md).** Their "data bridge", that a sampled
  cloud's diffusion operator approximates a heat kernel, is this paper's
  Proposition 3. It is proved here for a compact smooth submanifold at
  α = 1, which is not a tree, so the bridge they need is still open.
- **[THEORY-009](../theory.d/THEORY-009.md).** Consistent with it: self-adjointness comes from
  k(x, y) = k(y, x) through the conjugate a, with no Riesz.
- **Two THEORY entries are filed.** [THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md) (Active) covers the
  spectral identity, the corrected truncation bound and the nesting in t.
  [THEORY-tmp3j6t7](../theory.d/THEORY-tmp3j6t7.md) (Proposed) covers the α-family limit in drift form.
- **The anthology.** It carries no instruction for machine-learning
  practice, but it is a standard manifold-learning paper that an
  anthology topic could hold. The LIT now carries the
  `anthology-candidate` flag, as [LIT-981](../literature.d/LIT-981.md) does.

## Limitations

- **Proposition 1's "relative accuracy δ" is wrong.** The neglected terms
  are each at most δ²|λ₁|^{2t}(ψ_l(x) − ψ_l(y))². Summed, they are bounded
  by δ²|λ₁|^{2t}(1/π(x) + 1/π(y)), which is not small relative to D_t when
  x and y are close. On a 60-point three-cluster example (ε = 0.7, t = 3,
  δ = 0.05), the absolute bound held for every pair, while the relative
  error in D_t reached 0.985, for two points in the same cluster.
- **Appendix A misprints.** ψ_l = φ_l/π and φ̃_l = φ_l π should be φ_l/√π
  and φ_l√π. As printed, they contradict the paper's own ψ₀ = 1. The
  Hilbert–Schmidt integrand prints π(y)π(y) for π(x)π(y). The second
  equality for a(x, y) drops the constant Σ_z d(z).
- **§2.1** defines Pf with a(x, y) where p(x, y) is meant.
- **§3.3's expanded generator has the wrong sign.** With Δ positive
  semi-definite, as the paper declares, Δ√q/√q = −‖∇U‖²/4 − ΔU/2 when
  q = e^{−U}. The generator is then Δφ + (‖∇U‖²/4 + ΔU/2)φ, which
  annihilates the ground state √q, as it must. The printed
  Δφ − (‖∇U‖²/4 − ΔU/2)φ is that expression in the opposite (∇²)
  convention for Δ, and it does not annihilate √q. A numerical check gave
  a residual of 0.74 for the printed form and 2.5 × 10⁻⁷ for the
  corrected one.
- **§3.4** opens "Finally, when α = 0" for α = 1. The "general α" remark
  writes P_{ε,1} for P_{ε,α}. Proposition 11's proof writes p for q.
- **The boundary remainder.** Proposition 10 bounds L_{ε,α}φ by O(1) on a
  strip of measure O(ε^γ), and concludes R_ε = O(ε^γ) in L². An O(1)
  function on a set of measure ε^γ has L² norm O(ε^{γ/2}). The rate with
  boundary is therefore O(ε^{γ/2}) as argued, slower than printed. The
  PNAS paper's ε^{1/2} figure is not reproduced either.
- **Proposition 11's semigroup step does not follow as written.** It
  bounds ‖P^{t/ε} − (I − εΔ)^{t/ε}‖ by ‖(I − εR_ε)^{t/ε} − I‖. That
  replaces (I − εΔ)^{−1}(I − εΔ − εR_ε) by I − εR_ε, which needs R_ε to
  commute with Δ, and it drops ‖(I − εΔ)^{−t/ε}‖, which is not bounded by
  1. It uses (B.12) for an operator not shown to have non-negative
  spectrum, and it does not show that P_{ε,1} preserves E_K. The
  conclusion is accepted in later literature, but this proof is a sketch.
  The claim that P_{ε,1} is bounded by 1 on L²(M, dx) is also unproved:
  P is a contraction in L²(stationary measure), not in L²(dx).
- **§3.4's circle formula is off by a factor of two in time.** With the
  heat kernel as printed, e_t = 1 + Σ e^{−j²t} cos 2πj(θ_x − θ_y), one gets
  e^{2t} D_t² = ½|e^{2πiθ_x} − e^{2πiθ_y}|²(1 + O(e^{−6t})), not
  e^t D_t² = |…|²(1 + O(e^{−3t})). Checked numerically: the first form
  tends to 1, the printed one to 0. "ψ₁(x) = cos(2iπθ_x)" has a stray i.
  The conclusion, chord length at large t, stands.
- **§5's discrete kernel is misprinted.** It reads
  p̄_{ε,α}(x_i, x_j) = k_ε(x_i, x_j)/(d̄^(α)(x_i) d̄^(α)(x_j)), which is not
  row-stochastic and omits the α-weights. It should be
  k_ε(x_i, x_j)/(q̄_ε(x_i)^α q̄_ε(x_j)^α d̄^(α)(x_i)).
- **Criterion 4's exponent.** An error of O(m^{−1/2} ε^{−d/4−1/2}) vanishes
  only if m grows faster than ε^{−d/2−1}, the square of the stated rate.
- **Weyl's theorem** is quoted for P̃ − P, but P is self-adjoint only in
  L²(π), and π itself moves under the perturbation. The step needs the
  symmetric conjugates.
- **Unproved assertions.** The robustness of D_t to noise (C9), the
  embedding of all kernel eigenmap methods (C8), directed diffusion (C11),
  the Weyl-law account of the embedding dimension, and §6. None is
  quantified.
- **Out of scope by construction.** Only symmetric kernels and reversible
  walks are treated. A non-reversible chain has no symmetric conjugate,
  and the spectral identity of C1 fails for it. This is [QUESTION-052](../questions.d/QUESTION-052.md)'s
  directed half, which [NOTE-784](NOTE-784.md) left open.

## Open questions

- Is there a bound on ‖Ψ_t(x) − Ψ_t(y)‖ relative to D_t, under a condition
  on the eigenvectors' delocalization, or must the truncation error be
  stated absolutely? [THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md) gives the absolute bound only.
- When does the operator order of a diffusion map agree with an
  independently given hierarchy, such as the clusters of a known tree?
  A bound on the commutator between the walk and the hierarchy's
  projectors, of Conjecture A's kind, would settle it for reversible walks
  ([QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md)).
- For metastable data, how does the merge time of two clusters in D_t
  relate to the spectral gap and to escape probabilities? The paper shows
  it (Fig. 1) and proves nothing. Nadler et al. is the next reading.
- A complete proof of the α-family's convergence with boundary, and of
  Proposition 3's semigroup step, is needed before [THEORY-tmp3j6t7](../theory.d/THEORY-tmp3j6t7.md) can be
  Active.
