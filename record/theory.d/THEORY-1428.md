---
number: 1428
status: Active
formerly:
- THEORY-tmpv4i3y
title: 'Evans, Silverberg and Santangelo show that a lattice theory of origami tessellations predicts that the inhomogeneous soft deformations of a Miura-ori sheet are edge modes decaying from its boundaries with an analytic decay length, so that its number of degrees of freedom scales with its perimeter, not its area'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the thirtieth status review (ADR-065), at the
    coordinator's ruling under the owner's delegation. The title was:
    "Evans, Silverberg and Santangelo show that a lattice theory of origami
    tessellations predicts that the soft deformations of a Miura-ori sheet
    are edge modes decaying from its boundaries with an analytic decay
    length, so that its number of degrees of freedom scales with its
    perimeter, not its area". "The soft deformations" becomes "the
    inhomogeneous soft deformations", because the paper's three uniform
    zero modes, the twist the softest of them, are bulk modes (kind 3,
    dated note).

    The promote_when was: "An independent experiment or calculation on
    finite Miura-ori sheets finds soft deformations decaying from the
    boundaries with the predicted wavenumber-dependent decay length, and a
    count of degrees of freedom that scales with the perimeter rather than
    the area." It asked for replication, and it moved word for word to
    QUESTION-tmpwo0r9. The source was read in full (NOTE-1587, Read). Its
    step from J0 and D(q) to Eqs. 16 and 24 was checked by
    scratch/formal/evans_miura_check.py, second-checked by the coordinator
    on 2026-11-06.
tags:
- natural-sciences
- mathematics
date: '2026-11-05'
source:
- LIT-2070
summary: >-
  Evans, Silverberg & Santangelo (2015), LIT-2070, read in full in
  NOTE-1587 from the arXiv v2 source, with the step from J0 and D(q) to
  the dispersion relation and decay length checked. Active as a report of
  what the theory predicts. A linear theory about one ground state, with
  facet bending coarse-grained as folds, checked on one 8 × 8 paper sheet,
  with the decay length for a pop-through defect estimated only to within
  100%. Registered as a stand-in for Silverberg et al. (2014); it does not
  carry that paper's claims of bistable cells or crystal-like defects.
  Whether another group's test agrees is QUESTION-tmpwo0r9.
---

# THEORY-1428: Evans, Silverberg and Santangelo show that a lattice theory of origami tessellations predicts that the inhomogeneous soft deformations of a Miura-ori sheet are edge modes decaying from its boundaries with an analytic decay length, so that its number of degrees of freedom scales with its perimeter, not its area

## Source

Evans, Silverberg & Santangelo, "Lattice Mechanics of Origami Tessellations", Physical Review E (2015), LIT-2070. Read in full from the arXiv 1503.05756v2 source, in NOTE-1587.

## What was actually shown

- **Theory.** A Bloch-wave lattice theory of vertices coupled through shared folds. For the Miura-ori, with facet bending as extra folds, det[D(q)J] = 0 has real roots at q = 0 only, which gives three uniform zero modes. Imaginary q_y gives inhomogeneous soft modes decaying from the boundaries, with an analytic decay length ℓ(q) (Sec. III, Eqs. 16 and 24).
- **Experiment.** An 8 × 8 paper Miura-ori, deformed with an indenter and with reversible pop-through defects (Fig. 6). For a defect the decay length "can be estimated to within 100%".
- **Conclusion (Sec. IV).** "the number of degrees of freedom scale with the perimeter of a finite tessellation, rather than the area."

## Checked

All of it is in scratch/formal/evans_miura_check.py, second-checked by the coordinator on 2026-11-06.

- **The q → q_x reading.** Two entries of the printed D^T(q) carry a bare q. Only q = q_x reproduces Eq. 16. On that reading, det[D(q)J], built from the paper's printed J0 and D^T(q), vanishes on Eq. 16, and Eq. 24 follows from it.
- **J0 was not checked.** The paper states its entries without derivation, and they were taken as given.
- **The reviewer's own count.** A bar-and-joint Miura-ori, each face split by one diagonal, has exactly B − 3 infinitesimal floppy modes at every size tried, where B is the number of boundary vertices. That is a perimeter count. It is plain Maxwell counting for a triangulated disc with no states of self-stress, generic to triangulated sheets, and the paper does not make that point.

## What this does not say

- Anything beyond linear deformations about one ground state.
- That the uniform soft modes are edge modes. Three uniform zero modes exist in the infinite lattice, the twist softest over a wide range of Γ.
- That Miura-ori cells are bistable, or that defects behave like vacancies, dislocations or grain boundaries.
- That the scaling was measured. It is the theory's conclusion, checked against decay lengths on one sheet.

## Note of 2026-11-06: reader J, the bulk modes

The old title said "the soft deformations" are edge modes. The paper's infinite-lattice analysis has three uniform zero modes, contraction, twist and saddle, which are bulk modes. Fig. 5 calls the twist the softest "over a wide range". The paper's "these soft modes are edge states" refers to the inhomogeneous modes of the finite sheet. Hence "inhomogeneous".
