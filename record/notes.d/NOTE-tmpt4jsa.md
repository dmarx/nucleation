---
status: Skimmed
paper: 'LIT-tmpegvxm'
title: 'Foschi, Hull and Ku — Closed-form kinematics of degree-4 origami vertices'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in part on 2026-11-05 from the arXiv v2 PDF
    (https://arxiv.org/pdf/2206.12691), text extracted by pdftotext. Read:
    the abstract and Sections I–V of the main text, with the theorem
    statements, Example 1 and the two applications. Not read: Appendices
    A–C, which hold the proofs of Theorems 2 and 3 and the details on
    bird's feet. Hence Skimmed: the results are as stated, their proofs
    unchecked. Registered as a stand-in for the unread "Rigid Foldings"
    chapter of Hull's Origametry, at the owner's request. Quotes below were
    checked against the extracted text, which loses the product symbol in
    the closure condition.
date: '2026-11-05'
summary: >-
  Two algebraic equations in the tangents of half the folding angles, for
  opposite and for adjacent creases, describe the configuration space of
  any degree-4 rigid origami vertex, developable, elliptic or hyperbolic.
  They recover the flat-foldable relations and Huffman's, give new ones for
  general developable vertices, show in a worked example that the two
  folding modes are disconnected when the sector angles do not sum to 2π,
  prove a square-twist pouch bistable, and give a folding table with a
  single mode. Proofs in unread appendices.
---
<!-- inactive-ok-file: LIT-tmp8rseg LIT-tmphy9wm THEORY-tmp960op — Unavailable, Proposed or new; the works this stands in for, and the account filed from it -->

# NOTE-tmpt4jsa: Foschi, Hull and Ku — Closed-form kinematics of degree-4 origami vertices

## Contribution

Equations for the folding angles of a degree-4 vertex were known in closed
form for flat-foldable vertices, and by Huffman's relations in part for
others. This paper derives algebraic equations for completely general
degree-4 vertices, Euclidean (developable) and non-Euclidean, that trace
the whole configuration space, and uses them on two designs.

## Key insight

Parameterized by tan(ρ/2), the configuration space of a degree-4 vertex is
two algebraic curves, the folding modes. Whether they meet depends on
whether the vertex can be unfolded at all: only a developable vertex has a
flat state for the curves to share.

## Assumptions

- **A single degree-4 vertex** with rigid faces.
- **Self-intersection** is drawn faded in the plots, not excluded from the
  equations.
- **Sector-angle classes**: developable (sum 2π), elliptic (sum below 2π)
  and hyperbolic (sum above 2π).

## Key results

- **Closure** (§II): with R(e_i, ρ_i) the rotation about crease e_i by
  ρ_i, a necessary condition for the vertex to fold rigidly "is R(ei , ρi )
  = I where I is the identity matrix [18]", the product over the creases,
  [18] being belcastro and Hull (2002).
- **Flat-foldable degree 4** (§II, Theorem 1, "For a proof, see [17] or
  [19]", Origametry and Tachi and Hull): opposite folding angles equal up to
  sign, and "adjacent folding angles have a linear relationship when
  parameterized by the tangent half-angle".
- **Two modes** (Corollary 1): "Degree-4 rigid-foldable vertices have
  exactly two folding modes, meaning that their configuration space
  consists of two curves in R4 ."
- **Disconnection** (§III, Example 1): "in both the elliptic and hyperbolic
  cases the configuration spaces are disconnected, whereas in the
  developable vertex they are" connected, since "it is impossible to
  unfold the vertex so that all the creases have folding angles of zero at
  the same time". The hyperbolic case they call "less intuitive".
- **Square-twist pouch** (§V A): "the rigid origami configuration space of
  the square twist pouch determined by sector angle θ is discrete": the
  unfolded state and two folded states, a proof of the bistability felt as
  a snap.
- **Care with roots** (Remark 2): isolating a mode from the equations needs
  tracking "which branch of the square root is needed to preserve the
  folding mode".

## Concepts

- **Developable / elliptic / hyperbolic vertex**: sector angles summing to
  2π, less, or more.
- **Folding mode**: one of the two curves of a degree-4 configuration
  space.
- **Valley / mountain**: ρ_i > 0 / ρ_i < 0.

## Connections

- **The original it stands in for.** Of the "Rigid Foldings" chapter of
  Hull's Origametry ([LIT-tmp8rseg](../literature.d/LIT-tmp8rseg.md)), it restates the flat-foldable degree-4
  fold-angle equations, "linear when parameterized by the tangent of half
  the folding angles, also known as the Weierstrass transformation" in the
  publisher's summary, as its Theorem 1, citing the book for the proof. It
  does not restate the chapter's reciprocal diagrams, its zero-area
  theorem, or its infinitesimal and second-order rigidity.
- **Also belcastro and Hull (2002)** ([LIT-tmphy9wm](../literature.d/LIT-tmphy9wm.md)): it states their
  single-vertex identity-product condition as necessary, citing them, but
  not the global or affine form; for that see Akitaya et al.,
  [LIT-tmpj5g19](../literature.d/LIT-tmpj5g19.md).
- **Agreement.** It finds, from exact equations, the disconnection that
  Berry, Lee-Trimble and Santangelo ([LIT-tmp24k66](../literature.d/LIT-tmp24k66.md)) find near flat, and for
  degree 4 on both sides of 2π, as they do.

## Bearing on the record

- **The pasted synthesis.** A does not cite this paper. Its square-twist
  pouch is an exact bistable example for A's "bistability as memory", but
  the bistability is kinematic, a discrete configuration space, not a
  double-well energy as in A's illustration.
- **[CLAIM-495](../claims.d/CLAIM-495.md) (O(d) holonomy; non-commutativity is not holonomy).**
  Supports the claim's last clause. Four rotations about distinct crease
  axes, which do not commute, compose to the identity at every rigidly
  folded state of the vertex, so a loop of non-commuting edge maps is flat.
  It does not engage the claim's partial-compatibility case.
- **[CLAIM-459](../claims.d/CLAIM-459.md), [THEORY-1270](../theory.d/THEORY-1270.md), [THEORY-1273](../theory.d/THEORY-1273.md)** (bistable regimes; Schlögl;
  metastability by fluctuation): a different mechanism. Those are
  dynamical and stochastic bistability.
- Filed: [THEORY-tmp960op](../theory.d/THEORY-tmp960op.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **Degree 4 only.**
- **Proofs unread**: Theorems 2 and 3 are proved in the appendices.
- **The disconnection is shown in a worked example** with a general
  reason given in a sentence, not stated as a theorem in the main text.
- **Self-intersecting parts of the curves** are only faded in the plots.
