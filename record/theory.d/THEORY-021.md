---
number: 21
status: Proposed
formerly:
- THEORY-tmp3i3z1
promote_when: >-
  The algebra is settled for the exact configurations. What is open is
  whether trained models reach them. The kind of result that would settle it
  is a measurement on trained weights, either the toy's W or a sparse
  autoencoder's decoder directions. It would compute Σᵢ Dᵢ ŵᵢŵᵢᵀ over the
  represented features and find it close to the identity on the span. Finding
  that the Dᵢ sum to m, or that the configuration looks like a polytope, does
  not settle it. Leverage scores always sum to the rank, and a polytope seen by
  eye is not a measured frame operator. Trained configurations whose
  dimensionalities are sticky at the polytope values while Σᵢ Dᵢ ŵᵢŵᵢᵀ stays
  far from the identity would refute the account for trained models.
title: 'In the efficiently packed geometries of uniform superposition the features form a rank-one POVM compressed from the n-feature basis: their dimensionality-weighted projectors sum to the identity'
version: 1
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
---

# THEORY-021: In the efficiently packed geometries of uniform superposition the features form a rank-one POVM compressed from the n-feature basis: their dimensionality-weighted projectors sum to the identity

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

- **That trained networks are in these configurations.** The geometry is
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
