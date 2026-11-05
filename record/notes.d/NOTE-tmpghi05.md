---
status: Skimmed
paper: 'LIT-tmpj33xl'
title: 'Evans, Silverberg & Santangelo — Lattice mechanics of origami tessellations'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in part on 2026-11-05, as a stand-in for Silverberg et al.
    (2014), LIT-tmpa3uim, from arXiv 1503.05756v2, PDF,
    https://arxiv.org/pdf/1503.05756v2, extracted by pdftotext; the
    extraction is noisy, with embedded figure code, so some passages
    could not be quoted. Read: the abstract, the introduction, Sec. I (the
    single origami vertex), the opening of Sec. II (the general lattice
    theory), Sec. III on the Miura-ori (the soft-mode and edge-mode
    subsections, and Fig. 6 with the pop-through-defect experiments), and
    Sec. IV (Discussion). Skimmed: the algebra of Sec. II and the
    eigenmode details (Eqs. 12–31). Not read: the reference list, beyond
    checking that ref. [7] is Silverberg et al. (2014). Skimmed, because
    the derivations were not worked through. The published PRE text was
    not read.
date: '2026-11-05'
summary: >-
  A lattice theory of periodic origami: each degree-N vertex has N − 3
  internal degrees of freedom with several configuration branches;
  vertices are joined through shared folds and a Bloch-wave ansatz gives a
  rigidity-like matrix. In the Miura-ori, with facet bending as extra
  folds, soft modes are localized at the edges with an analytic decay
  length, checked on an 8 × 8 paper sheet with an indenter and with
  reversible pop-through defects; degrees of freedom scale with the
  perimeter. Linear, one ground state. It does not state the 2014 paper's
  bistable cells or crystal-defect analogy.
---
<!-- inactive-ok-file: THEORY-tmpv4i3y CLAIM-478 LIT-tmpa3uim — Proposed, Unavailable or new; cited from the reading of Evans, Silverberg & Santangelo (2015) as open -->

# NOTE-tmpghi05: Evans, Silverberg & Santangelo — Lattice mechanics of origami tessellations

## Contribution

- A general framework for the kinematics and linear energetics of an
  origami tessellation treated as a crystalline lattice.
- An analytic decay length for localized deformations of the Miura-ori,
  checked against experiment.
- The identification of edge-localized soft modes, linked to topological
  mechanics.

## Key insight

Origami vertices are local mechanisms with several configuration branches,
and a tessellation is a lattice of them coupled through shared folds. Once
facet bending is admitted, a real Miura-ori is far floppier than the
one-degree-of-freedom count of rigid origami, but its extra freedom lives
at its boundary: soft modes decay into the bulk.

## Assumptions

- Linearized kinematics about the folded ground state.
- Nearly flat facets, with bending represented as extra folds.
- Crease energies as torsional springs of equal stiffness.
- A periodic tessellation, analysed in Fourier space.
- An experiment on laser-cut paper with α = π/3 and ε = π/2.

## Key results

- **Sec. I, the single vertex.** "the associated solutions are generically
  multi-valued. These results imply that there are multiple branches of
  configuration space for any given spherical polygon."
- **Sec. III, the Miura-ori.** With facet bending as two extra folds per
  vertex (degree six), three uniform zero modes at q = 0 including a
  twisting mode, an acoustic-like mode, and inhomogeneous soft modes
  decaying from the boundaries with decay length ℓ(q).
- **Sec. III, experiment.** "Inhomogeneous deformations are created using
  both an external indenter to apply a displacement (Fig. 6B,C) and by
  placing reversible “pop-through defects” (Fig. 6D) [7]."
- **Fig. 6 caption.** "in the presence of a “pop-through defect” (PTD) [7],
  the lattice distorts to accommodate the induced strain." And: "Because
  the PTD induces an extensional distortion rather than a compression, the
  strain is oppositely signed." For a PTD the decay length "can be
  estimated to within 100%".
- **Sec. IV.** "the number of degrees of freedom scale with the perimeter
  of a finite tessellation, rather than the area."

## Concepts

- **Fold and crease**: a fold is a hinge between unbendable, unstretchable
  sheets; a crease is a plastically formed fold with a preferred angle. The
  paper uses the two interchangeably.
- **Internal state s**: the N − 3 component vector fixing all a vertex's
  dihedral angles.
- **Pop-through defect (PTD)**: a reversible local inversion in the
  Miura-ori, cited from ref. [7] and not defined further here.
- **Soft modes and edge states**: inhomogeneous zero modes decaying from
  the boundaries with length ℓ(q).

## Connections

It cites Silverberg et al. (2014), LIT-tmpa3uim, as ref. [7] for the
pop-through defect, and stands in for it, partly.

- **Of the 2014 paper's results, it restates** that Miura-ori sheets admit
  reversible pop-through defects; that the strain a defect induces is
  localized and decays rapidly; and that a real Miura-ori has more freedom
  than rigid-origami counting gives, through facet bending. It adds
  several configuration branches at each vertex.
- **It does not restate** that each Miura-ori unit cell is mechanically
  bistable (its one use of "bistability" is for single vertices, citing
  other work: "providing novel functionality such as complicated
  bistability [15–17]"); that switching cells reprograms the sheet's
  compressive stiffness; how pop-through defects interact; or any analogy
  to vacancies, dislocations or grain boundaries, none of which words
  appear in it.

Silverberg et al. (2015), LIT-tmptep4g, makes the same move in the square
twist, modelling facet bending as virtual creases.

## Bearing on the record

- **The pasted synthesis on constraint architectures, through this
  neighbour.** A's phrase "Miura-ori bistable cells" for the 2014 paper is
  not confirmed here: the neighbour calls pop-through defects reversible
  but says nothing of bistable cells. A's phrase about defects "analogous to
  vacancies, dislocations, and grain boundaries" is not confirmed either:
  the neighbour describes them only as local distortions. Both claims
  remain unchecked.
- **CLAIM-478 (scale separation makes constraints).** Related, weakly.
  Facet bending is a stiffer mode that the paper models as extra folds; as
  in Silverberg et al. (2015), whether a mode counts as a constraint or a
  freedom depends on the energy scale probed. This paper does not make
  that point itself.
- **CLAIM-480 (composing interactions creates constraints).** Related.
  Vertex constraints compose through shared folds, and the composite's
  degrees of freedom sit at its boundary, not through its bulk.
- **CLAIM-495 (O(d) connection; assignments fixed by holonomies).**
  Unrelated in the linear form used here. The single-vertex closure that
  the spherical-polygon construction encodes is a loop-closure condition,
  but the paper does not put it in holonomy terms.
- The record has no entries on edge states or topological mechanics.
  Filed: THEORY-tmpv4i3y. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- Linear theory, so small deformations about one ground state only.
- Bending coarse-grained as folds.
- One 8 × 8 paper sheet; the PTD decay length estimated only to within
  100%.
- Skimmed: the algebra of Sec. II and the eigenmode equations were not
  worked through.
