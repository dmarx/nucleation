---
status: Active
title: 'For a weighted cellular sheaf of finite-dimensional vector spaces on a finite cell complex, the kernel of the degree-k Hodge Laplacian is the k-th sheaf cohomology, in degree 0 the space of global sections, and the linear flow ẋ = −Δ^k x converges exponentially to the orthogonal projection of its initial state onto that kernel, each eigencomponent decaying at its own eigenvalue; the inner products on the stalks are part of the data, so the same sections can come with different rates, and the Laplacian does not determine the sheaf'
version: 1
tags:
- mathematics
- network-science
date: '2026-10-27'
source:
- LIT-tmpnpxhs
summary: >-
  Hansen and Ghrist (2019), [LIT-tmpnpxhs](../literature.d/LIT-tmpnpxhs.md), read in [NOTE-tmpzqos6](../notes.d/NOTE-tmpzqos6.md) from arXiv
  v2: Theorem 3.1 (discrete Hodge theory), H^0 ≅ Γ (p. 7) and Proposition
  8.1 (the flow), each with a proof; Fig. 3.1 for the Laplacian not
  determining the sheaf. Active as mathematics. The paper does not speak of
  relaxation rates or time-scale separation, does not say what produces the
  restriction maps, and treats only linear flows of a fixed Laplacian.
---
<!-- inactive-ok-file: CLAIM-tmpdjt64 — Proposed; the gluing claim this formal statement serves, cited as open -->

# THEORY-tmpga5mk: For a weighted cellular sheaf of finite-dimensional vector spaces on a finite cell complex, the kernel of the degree-k Hodge Laplacian is the k-th sheaf cohomology, in degree 0 the space of global sections, and the linear flow ẋ = −Δ^k x converges exponentially to the orthogonal projection of its initial state onto that kernel, each eigencomponent decaying at its own eigenvalue; the inner products on the stalks are part of the data, so the same sections can come with different rates, and the Laplacian does not determine the sheaf

## Source

Hansen and Ghrist (2019), [LIT-tmpnpxhs](../literature.d/LIT-tmpnpxhs.md), §§2.2.2, 3.1–3.2, 8.1 and 8.6 of
arXiv 1808.01513v2 (pp. 7, 9–11, 34–35, 39); read in [NOTE-tmpzqos6](../notes.d/NOTE-tmpzqos6.md).

## What was actually shown

**Sections are the kernel.** A cellular sheaf assigns a vector space to
each cell and a linear restriction map to each incidence; a global section
is an assignment that agrees under every map (Def. 2.5, p. 6). The
coboundary δ^k collects the disagreements, and "H^0(X; F) is naturally
isomorphic to Γ(X; F), the space of global sections" (p. 7). Theorem 3.1
(p. 10) is discrete Hodge theory for any complex of finite-dimensional
Hilbert spaces: ker Δ^k ≅ H^k, with C^k = ℋ^k ⊕ im δ^{k−1} ⊕ im (δ^k)*. In
degree 0 on a graph, L = δ*δ, and Lx = 0 exactly when F_{u⊴e}x_u =
F_{v⊴e}x_v on every edge: agreement in the edge's comparison space, not
equality of the vertex values.

**The flow.** Proposition 8.1 (p. 34): "The dynamical system ẋ = −Δ^k_F x
has as its space of equilibria ℋ^k(X; F), the space of harmonic k-cochains
of F. The trajectory of this dynamical system initialized at x₀ converges
exponentially quickly to the orthogonal projection of x₀ onto ℋ^k(X; F)."
The proof writes x(t) = Σᵢ e^{−tλᵢ}⟨vᵢ, x₀⟩vᵢ over an orthonormal
eigenbasis, so each component decays at its eigenvalue and the slowest
decay is at the smallest nonzero one. For k = 0, "a distributed system can
reach consensus on the nearest global section to an initial condition"
(p. 35). For the discrete scheme x[t + 1] = (I − αL)x[t] the best step is
α = 2/(λ_max + λ_min) and the contraction r = (λ_max − λ_min)/(λ_max +
λ_min) (p. 39).

**The weights matter, and the Laplacian forgets.** The stalks' inner
products are data: normalizing is reweighting the sheaf (§3.4, p. 15), and
the weights on an approximating sheaf "will be crucial to the spectral
behavior of their Laplacians" (p. 39). Two sheaves with different stalk
dimensions and maps have the same Laplacian (Fig. 3.1, p. 11): "one cannot
hear the shape of a sheaf".

What could have come out otherwise: the identifications and the flow are
checkable line by line, and the Fig. 3.1 example by multiplying out two
2 × 2 products.

## What this does not say

- **Anything about time scales.** The paper never uses "relaxation rate"
  or "time-scale separation". That the nonzero spectrum is a hierarchy of
  rates, that a gap separates time scales, the two-cluster window and the
  n² chain are readings and computations of the exchange of 2026-10-27
  ([CLAIM-tmpywecm](../claims.d/CLAIM-tmpywecm.md)), consistent with the proof's formula but not in the
  paper.
- **Where the restriction maps come from.** The paper takes them as given
  and, in its applications, builds them from measurements (§§8.2, 8.7) or
  designs them (§8.5). It does not say interactions generate them
  ([CLAIM-tmpdjt64](../claims.d/CLAIM-tmpdjt64.md)).
- **That the sections are nontrivial.** The zero cochain is always a
  section, and a sheaf whose maps are zero has every cochain as a section
  (p. 11). Questions of interest are about nontrivial sections (§9.2,
  p. 42), as [THEORY-299](THEORY-299.md) found for knowledge sheaves.
- **That the spectrum identifies the sheaf**, or the correspondences it
  encodes (Fig. 3.1).
- **Anything about nonlinear coupling, time-varying maps or oscillators.**
  The flow is linear with a fixed Laplacian. "Synchronization" in this
  paper (§8.7) is the estimation problem of finding an approximate global
  section of measured pairwise relations, not the dynamical
  synchronization of coupled oscillators.
- **Anything about infinite complexes or stalks in general.** §3.3 gives
  conditions for bounded and compact coboundaries; where δ is compact on an
  infinite-dimensional space the eigenvalues accumulate at zero, so "there
  will be no smallest nontrivial eigenvalue" (p. 14).
