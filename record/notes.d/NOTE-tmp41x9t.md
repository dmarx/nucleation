---
status: Read
paper: LIT-993
title: 'Ovsjanikov et al. — Functional maps'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the author-posted PDF on co-author Justin Solomon's
    MIT page (people.csail.mit.edu/jsolomon/assets/fmaps.pdf, 11 pages,
    the SIGGRAPH 2012 paper as in ACM TOG 31(4)), text extracted with
    pdftotext in reading order: §§1–9, every figure caption, and Appendix
    A, the proof of Theorem 5.1, which was checked. The figures' plots
    were read from their captions and axis labels only.
date: '2026-10-14'
summary: >-
  A bijection T: M → N is fully encoded by the linear map f ↦ f∘T⁻¹ it
  induces on functions, a matrix C in chosen bases. If T preserves volume
  (or the bases are discretely orthonormal), C is orthogonal, so its
  inverse is its transpose; if T is an isometry, it commutes with the
  Laplace–Beltrami operator, so C maps each eigenspace to the matching
  one. Descriptor, landmark, segment and commutativity constraints are
  linear in C, so matching reduces to a least-squares solve with a
  100-eigenfunction basis, which beat Blended Intrinsic Maps on SCAPE and
  TOSCA.
---
<!-- inactive-ok-file: THEORY-tmp11baf THEORY-009 THEORY-239 — Proposed; the account filed from this reading, and two accounts it bears on, open -->
<!-- inactive-ok-file: CLAIM-098 — Proposed; the claim that translation is directed, which this reading bears on, open -->

# NOTE-tmp41x9t: Ovsjanikov et al. — Functional maps

## Contribution

The paper replaces a point-to-point correspondence between two shapes by
the linear operator it induces between their function spaces, written as
a matrix in a basis of Laplace–Beltrami eigenfunctions. Many constraints
that are combinatorial for point maps become linear in that matrix, and
maps can be added, inverted and composed by matrix algebra. Shape
matching becomes one least-squares solve followed by an ICP-style
refinement.

## Key insight

A map moves functions, and moving functions is linear even when the map
is not. For a near-isometry the matrix in the low Laplacian eigenbasis is
small and nearly block-diagonal, because isometries preserve the
Laplacian and so carry each eigenspace onto the matching one.

## Assumptions

- **The map.** T: M → N is bijective (§4). The functional representation
  is T_F(f) = f∘T⁻¹. Generalized functional maps (Definition 1) need not
  come from any T.
- **Bases.** Any bases; for near-isometries the first n Laplace–Beltrami
  eigenfunctions, n = 100 in all experiments (§5.1).
- **Orthonormality (Theorem 5.1).** Either the discrete bases are
  orthonormal in the standard inner product, or T is volume preserving,
  μ_N(T(x)) = μ_M(x).
- **Stability of the truncated basis.** "the space of functions spanned
  by all the first n eigenfunctions … can be shown to be stable under
  near-isometries as long as the nth and (n + 1)st eigenvalues are well
  separated", citing Kato (1995). Cited, not shown.
- **Shapes.** Meshes, with the cotangent Laplacian (Meyer et al. 2002);
  the method is intrinsic and cannot tell a shape from its mirror image
  without extra constraints.

## Key results

- **Remarks 4.1–4.3.** T can be recovered from T_F (indicator functions
  map to indicator functions); T_F is linear; in bases it is a matrix C
  with c_ij the jth coefficient of T_F(φ_i^M), so for orthonormal bases
  c_ij = ⟨T_F(φ_i^M), φ_j^N⟩. (The text then writes T_F(a) = Ca, which with
  b_j = Σ_i a_i c_ij is Cᵀa; the index convention is inconsistent but
  nothing turns on it.)
- **Theorem 5.1, proof in App. A, checked.** (1) If the bases are
  discretely orthonormal, or T is volume preserving, C is orthonormal.
  The proof shows the functional representation D of T⁻¹ satisfies
  C = Dᵀ, by change of variables in the defining integrals, and CD = I.
  (2) An isometry commutes with the Laplace–Beltrami operator ("well
  known", not proved). *Holds when:* T is a bijection; the volume
  condition is what makes the two integrals equal.
- **Sparsity (§5.1).** For an exact isometry, C_ij ≠ 0 only if the two
  eigenfunctions share an eigenvalue, so C is diagonal when no eigenvalue
  repeats. Empirically, on TOSCA cats, more than 94% of entries fall
  below 0.1 in magnitude, and C "stops being diagonal very quickly under
  even mild non-isometric deformations", especially at high frequency.
- **Compactness (Fig. 3).** 30–40 eigenfunctions represent ground-truth
  maps between 27.8K-vertex cats almost as well as the point map; the
  unweighted cotangent Laplacian is more compact than the area-weighted
  one; larger deformations need more basis functions.
- **Linear constraints (§§5.3–5.4).** Function preservation Ca = b
  covers descriptors, landmarks and segments. Commutativity with
  operators S_F, R_F on the two shapes, R_F C = C S_F, is linear in C.
- **Conversion back to points (§6.1).** Delta functions have coefficients
  φ_i(x), so nearest-neighbour search between the columns of CΦ_M and
  Φ_N, by Plancherel, recovers a point map in O(V_N log V_N + V_M log V_N).
- **Refinement (§6.2).** Alternate nearest-neighbour assignment with the
  best orthonormal C: ICP in the spectral embedding. It needs a good
  initial C because the embeddings are defined only up to orthogonal
  transformations within eigenspaces.
- **Benchmarks (§7, Figs. 6–8).** On SCAPE and TOSCA, the method beats
  Blended Intrinsic Maps (Kim et al. 2011) and Sahillioğlu and Yemez
  (2011) under symmetric evaluation, with parameters fixed before the
  benchmark. Refining those methods' maps with 20 iterations improves
  them, in 5–15 s for 10–50K points.
- **Collections (§8.2).** Composition is matrix multiplication; ICSM
  cycle-consistency with ‖C − I‖_Fro as distance from identity, and "map
  diffusion" by squaring a block "SuperMap" matrix, lower errors on 11
  SCAPE shapes (Figs. 10–11).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A bijection is equivalent to its induced linear operator on functions | strong | Remarks 4.1–4.2, elementary |
| C2 | Volume-preserving bijections have orthogonal functional matrices; inverse is transpose | strong | Theorem 5.1(1), App. A, checked |
| C3 | Isometries commute with the Laplacian, so their matrices are block-diagonal on eigenspaces | strong | Theorem 5.1(2) and §5.1; standard, cited |
| C4 | The span of the first n eigenfunctions is stable under near-isometries given a gap at n | moderate | cited to Kato (1995), not shown |
| C5 | Near-isometric maps are compact and near-sparse in the low eigenbasis | moderate | Figs. 3–4, TOSCA cats |
| C6 | The method beats the 2011 state of the art on SCAPE and TOSCA | moderate | Figs. 6–8, one benchmark |

## Method

1. Compute Laplace–Beltrami eigenfunctions on each mesh (cotangent
   scheme), keep 100.
2. Build function-preservation constraints from WKS and HKS descriptors
   and from segment correspondences (persistence-based segmentation, heat
   kernel maps).
3. Add commutativity with the Laplacian.
4. Solve for C in least squares.
5. Refine by spectral ICP with orthonormal C; read off a point map by
   nearest neighbours.

## Concepts

- **Functional representation T_F.** f ↦ f∘T⁻¹, the push-forward of
  functions along a bijection.
- **Generalized linear functional map.** Any linear map between the
  function spaces, given by a matrix C in chosen bases; it need not come
  from a point map (the zero map is the paper's example).
- **Operator commutativity.** R_F C = C S_F for given operators on the
  two shapes, such as a symmetry or the Laplacian.

## Connections

The paper builds on spectral matching (Jain et al. 2007; Mateus et al.
2008; Ovsjanikov et al. 2008), which assumed a one-to-one, diagonal
correspondence of eigenfunctions; dropping that assumption removes sign
and ordering ambiguities. It uses heat and wave kernel signatures (Sun et
al. 2009; Aubry et al. 2011), and ICSM (Nguyen et al. 2011) for
collections. It points to representation theory (Weyl 1946) as the
general idea of studying maps through their action on functions, and to
vector diffusion maps (Singer and Wu 2011) for map diffusion.

## Bearing on the record

- **[QUESTION-052](../questions.d/QUESTION-052.md).** [LIT-993](../literature.d/LIT-993.md) is registered as "a correspondence between
  two realizations represented as a linear operator between function
  spaces, truncated to low Laplacian eigenspaces, with directed maps
  included". The first two parts are right. "Directed maps included"
  says more than the paper does. Its operators run from M to N, but every
  result about structure (Theorem 5.1, the sparsity, the refinement)
  assumes a bijection, and the regularization pushes C toward
  orthonormality, so that inversion is transposition. Nothing in it
  treats a non-invertible or one-way transformation. The paper does
  support the question's eigenspace framing in one respect: what an
  isometry preserves is each Laplacian eigenspace, not each eigenvector,
  which is the point of [CLAIM-164](../claims.d/CLAIM-164.md).
- **[THEORY-009](../theory.d/THEORY-009.md) and [THEORY-239](../theory.d/THEORY-239.md).** Functional maps are a case in which
  an operator between two different spaces is useful without being
  self-adjoint. Their structure comes from orthogonality (volume
  preservation) and commutation with the two Laplacians, not from a
  symmetric pair distribution. This neither supports nor contradicts
  [THEORY-009](../theory.d/THEORY-009.md), which concerns operators on one space; it is a worked
  example of the two-space setting [THEORY-239](../theory.d/THEORY-239.md) covers.
- **[CLAIM-098](../claims.d/CLAIM-098.md)** holds that translation is directed and need not be
  invertible. Functional maps handle non-bijective input maps only by
  inverting a truncated matrix, a numerical step with no guarantee. So
  they offer no construction for the directed case.
- **[THEORY-tmp11baf](../theory.d/THEORY-tmp11baf.md)** is filed from this reading.
- No instruction for machine-learning practice; the paper is geometry
  processing. Nothing for the anthology.

## Limitations

- Restricted to near-isometric deformations by the choice of basis; the
  authors name better bases for other deformations as future work.
- The stability of truncated eigenspaces is cited, not shown, and needs a
  spectral gap at the cut.
- Which matrices C come from point maps is called "a difficult open
  problem" (§5.5).
- Symmetric shapes need extrinsic or segment constraints to disambiguate.
- One benchmark family (SCAPE, TOSCA).

## Open questions

- A characterization of the matrices that come from point-to-point maps.
- Bases for non-isometric deformations, where the Laplacian no longer
  commutes with the map.
- What plays the role of the eigenspace-preserving structure for a map
  that is not a bijection, which is the directed case of [QUESTION-052](../questions.d/QUESTION-052.md).
