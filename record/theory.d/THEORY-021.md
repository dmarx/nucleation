---
number: 21
status: Active
formerly:
- THEORY-tmp3i3z1
title: 'In the exact configurations of uniform superposition (regular polygons, the tetrahedron, antipodal pairs, and tegum products of these that span the hidden space, with equal norms within each factor) the features form a rank-one POVM compressed from the n-feature basis: their dimensionality-weighted projectors sum to the identity'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-021.yaml, batch 010, ADR-047).
    The title said "the efficiently packed geometries", which would take in
    the square antiprism and arbitrary packings. It now lists the
    configurations whose algebra is checked: regular polygons, the
    tetrahedron, antipodal pairs, and spanning tegum products of them, with
    equal norms within each factor. The square antiprism (Dᵢ = 3/8) is
    excluded, because its symmetry group acts reducibly on ℝ³, so its
    tightness depends on its vertex heights, and NOTE-278 does not check it.
    The promote_when said "The algebra is settled for the exact
    configurations" and asked only whether trained models reach them. That
    question moves, unchanged, to QUESTION-tmpm0s0z. The algebra is
    re-derived in the note of 2026-10-19 below, which under ADR-047 v2 (the
    owner's rule of 2026-10-19) meets the condition for the narrowed claim.
tags:
- representation-learning
- mathematics
- quantum-foundations
date: '2026-09-30'
source:
- LIT-323
summary: >-
  Elhage et al. (2022), [LIT-323](../literature.d/LIT-323.md), found that features in uniform superposition
  settle into polytopes and tegum products, with feature dimensionalities
  clustering at 3/4, 2/3, 1/2, 2/5 and 3/8. The tight-frame and POVM reading
  is the reader's inference in [NOTE-278](../notes.d/NOTE-278.md), checked numerically there. It was
  refined when filing: a tegum product is not globally tight, but the
  Dᵢ-weighted POVM still sums to the identity. None of this is in the paper.
  It does not make superposition contextual or quantum, and it says nothing
  yet about trained real models.
answers:
- QUESTION-058
---
<!-- inactive-ok-file: THEORY-017 — Proposed; named in Connections for which structure is intrinsic, not leaned on -->

# THEORY-021: In the exact configurations of uniform superposition (regular polygons, the tetrahedron, antipodal pairs, and tegum products of these that span the hidden space, with equal norms within each factor) the features form a rank-one POVM compressed from the n-feature basis: their dimensionality-weighted projectors sum to the identity

## Source

Elhage et al. (2022), [LIT-323](../literature.d/LIT-323.md): Geometry of Superposition, the feature
dimensionality Dᵢ = ‖Wᵢ‖² / Σⱼ(ŵᵢ·Wⱼ)², tegum products, and Fred Zhang's HTML
comment on leverage scores. Read in [NOTE-278](../notes.d/NOTE-278.md), whose Bearing section
states the tight-frame inference.

## What was actually shown

**In the paper.** In the ReLU-output toy with n sparse uniform features in m
dimensions, the per-feature dimensionality Dᵢ clusters at the values of
uniform polytopes. These are 3/4 for the tetrahedron, 2/3 for the triangle,
1/2 for antipodal pairs, 2/5 for the pentagon and 3/8 for the square
antiprism. Many configurations are tegum products: polytopes in orthogonal
subspaces, with no interference across them. Across efficiently packed
features the Dᵢ sum to m. Zhang's comment explains why: Dᵢ is a leverage
score when the vectors are in isotropic position ([NOTE-278](../notes.d/NOTE-278.md)).

**The reader's inference.** The unit directions of the triangle, pentagon,
tetrahedron and antipodal pairs form a tight frame, with
Σᵢ ŵᵢŵᵢᵀ = (n/m)·I. So Eᵢ = (m/n)ŵᵢŵᵢᵀ is a rank-one POVM, and tr Eᵢ = m/n = Dᵢ
([NOTE-278](../notes.d/NOTE-278.md)). V = √(m/n)·W is a co-isometry. Compressing the standard basis of
ℝⁿ, a projection-valued measure, through V gives exactly this POVM: Naimark's
dilation run backwards.

**Two refinements, checked when filing.**

- *Dᵢ is forced.* For any unit-norm tight frame,
  Dᵢ = 1 / (ŵᵢᵀ F ŵᵢ) = m/n, where F is the frame operator. The paper's
  sticky values are exactly m/n of the polytope.
- *Tegum products are not tight.* A triangle ⊕ an antipodal pair in ℝ³ has
  frame-operator eigenvalues 1.5, 1.5 and 2, so it is not a tight frame. But
  each factor is tight, so Σᵢ Dᵢ ŵᵢŵᵢᵀ = I still holds. The POVM with weights
  Dᵢ survives, and the equal-weight tight frame does not. The first is the
  general statement.

So in these geometries the hidden space carries one unsharp observable whose
elements do not commute. It is the compression of the disentangled model's
feature basis, which the paper stipulates as the input basis. That is a
precise form of the paper's slogan that a small network is "noisily
simulating" a larger, sparse one.

## What this does not say

- **That the square antiprism, or any packing not listed in the title, is
  such a configuration.** Its symmetry group acts reducibly on ℝ³, so its
  tightness is not forced and is not checked here.
- **That trained networks are in these configurations.** That is
  [QUESTION-tmpm0s0z](../questions.d/QUESTION-tmpm0s0z.md). The geometry is
  toy-only, best-of-many runs, and the authors expect it to generalise least
  ([NOTE-278](../notes.d/NOTE-278.md)). Non-uniform importance or sparsity deforms the polytopes, and
  the identity need not hold.
- **That superposition is contextual or quantum.** One POVM is one context, and
  it trivially admits a global distribution over its outcomes. Kochen–Specker contextuality is a failure of several
  contexts to glue ([THEORY-012](THEORY-012.md)), and non-commutation alone is not that
  ([NOTE-302](../notes.d/NOTE-302.md)).
- **That the POVM is intrinsic.** It needs an inner product to define ŵᵢ and
  orthogonality. In the toy the O(m) symmetry makes WᵀW intrinsic. At a
  softmax output no inner product is identified ([NOTE-302](../notes.d/NOTE-302.md)).
- **Anything about the compressed-sensing bound**, whose hypotheses the
  trained toy does not satisfy ([NOTE-278](../notes.d/NOTE-278.md), C11).

## Connections

[THEORY-017](THEORY-017.md): WᵀW is the invariant, and the feature basis is supplied from
outside the space. [LIT-304](../literature.d/LIT-304.md) is in tension with this, as [NOTE-278](../notes.d/NOTE-278.md) notes: a
causal inner product cannot make more than m of these directions orthogonal.
Engels et al. ([LIT-322](../literature.d/LIT-322.md)) generalise the directions to subspaces.

## Note of 2026-10-19: the algebra, re-derived, and the narrowing

Let W₁, …, Wₙ be the feature vectors in ℝ^m, with frame operator
F = Σⱼ WⱼWⱼᵀ. The paper's dimensionality is
Dᵢ = ‖Wᵢ‖² / Σⱼ(ŵᵢ·Wⱼ)² = ‖Wᵢ‖² / (ŵᵢᵀFŵᵢ), so

Σᵢ Dᵢ ŵᵢŵᵢᵀ = Σᵢ WᵢWᵢᵀ / (ŵᵢᵀFŵᵢ).

**One factor.** The vertices of a regular polygon in ℝ², of the tetrahedron
in ℝ³, or of an antipodal pair in ℝ¹, all of norm c, form an orbit of a
finite group acting irreducibly. F commutes with the group, so by Schur's
lemma and the trace F = (nc²/m)·I. Then ŵᵢᵀFŵᵢ = nc²/m, so Dᵢ = m/n and
Σᵢ Dᵢ ŵᵢŵᵢᵀ = (m/n)(F/c²) = I. With V = √(m/n)·Ŵ, whose columns are the ŵᵢ,
VVᵀ = I_m, so V is a co-isometry, and Eᵢ = V eᵢeᵢᵀ Vᵀ = (m/n) ŵᵢŵᵢᵀ is the
standard basis's projection-valued measure compressed through V.

**A tegum product.** Take factors in mutually orthogonal subspaces S_k with
⊕S_k = ℝ^m. Inner products across factors vanish, so ŵᵢᵀFŵᵢ sees only i's
own factor, and the one-factor case holds inside each S_k:
Σ_{i∈k} Dᵢ ŵᵢŵᵢᵀ = P_k, the projector onto S_k. Summing, Σ_k P_k = I. F
itself is not scalar when the factors have different n_k/m_k, which is the
"not globally tight" refinement above.

**Checked numerically for this note.** The triangle, pentagon and heptagon
(Dᵢ = 2/3, 2/5, 2/7), the tetrahedron (3/4), an antipodal pair (1/2), the
octahedron as three antipodal pairs, and a triangle ⊕ an antipodal pair of a
different norm all give Σᵢ Dᵢ ŵᵢŵᵢᵀ = I.

**What the hypotheses do.** Equal norms within a factor are sufficient, not
necessary. The identity needs only F to act as a scalar on each factor's
span, and in ℝ¹ that holds for any two antipodal vectors, whatever their
norms. The narrowed title states the sufficient condition, which is the
paper's polytope case. The square antiprism is excluded until its frame
operator is checked at the paper's vertex heights. Whether trained models
reach any of these configurations is [QUESTION-tmpm0s0z](../questions.d/QUESTION-tmpm0s0z.md).
