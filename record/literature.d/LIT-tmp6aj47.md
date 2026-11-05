---
status: Active
status_note: >-
  read in full 2026-11-05 ([NOTE-tmpryygx](../notes.d/NOTE-tmpryygx.md)) from the arXiv preprint; worth
  reading as a short, exact statement of the Tachi–Hull model of
  self-folding (a driving force is a vector field on the configuration
  space, separable by crease, with positive forward force along the
  intended path; a path is uniquely self-foldable when it is the only one
  the field drives), with a new criterion for one-degree-of-freedom paths,
  and its application: the Miura-ori and Chicken Wire tessellations cannot
  be uniquely self-folded, while generic quadrilateral tessellations
  rotationally symmetric about the midpoints of the tile's sides can.
  Registered as a stand-in for the unread chapter "Rigid Origami Theory"
  of Hull's Origametry, [LIT-tmpq0e56](LIT-tmpq0e56.md), whose self-folding section it
  covers. Its main limits: an abstract kinematic model without stiffness
  or bending energy, and monohedral quadrilateral tilings only.
title: 'Self-foldability of monohedral quadrilateral origami tessellations'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 as a stand-in for the unread chapter
    "Rigid Origami Theory" of Hull's Origametry (LIT-tmpq0e56), at the
    owner's request, from the owner's pasted synthesis on FACT, rigidity,
    compliant mechanisms and origami, written by another assistant (A) and
    pasted by the owner on 2026-11-04, which cites the chapter as O2 and
    does not cite this paper. Citation from arXiv metadata, checked by the
    reader: Thomas C. Hull and Tomohiro Tachi; arXiv 1809.04243, v1
    2018-09-12 (math.MG), which is `published:`; journal reference
    Origami⁷: Proceedings of the 7th International Meeting on Origami
    Science, Mathematics, and Education, Tarquin (2018), pp. 521–532, a
    conference proceedings paper. No DOI was found; Crossref's
    bibliographic search returns instead the companion Tachi and Hull,
    "Self-Foldability of Rigid Origami", ASME IDETC 2016
    (doi:10.1115/detc2016-60546), whose journal version is J. Mech. Robot.
    9(2), 021008. Not held before. Copy: the arXiv PDF,
    https://arxiv.org/pdf/1809.04243, 12 pages, extracted with pdftotext.
tags:
- mathematics
- control-theory
date: '2026-11-05'
published: '2018-09-12'
arxiv: '1809.04243'
first_author: 'Hull'
keywords:
- 'self-folding'
- 'rigid origami'
- 'driving force'
- 'origami tessellation'
- 'Miura-ori'
- 'folding modes'
implementations: []
summary: >-
  Hull & Tachi (2018). Restates their 2016 model of self-folding rigid
  origami: a driving force is a vector field on the configuration space,
  additively separable by crease, whose forward force along the intended
  path is positive; the path is uniquely self-foldable if it is the only
  one the field drives, which needs the tangent space at flat to be larger
  than the span of the wrong-mode tangents. Adds a criterion for paths of
  one degree of freedom. Applied to monohedral quadrilateral tessellations:
  the Miura-ori and Chicken Wire patterns have too many modes to be
  uniquely self-foldable, and generic tilings rotationally symmetric about
  the midpoints of the tile's sides, which have two modes, are.
---
<!-- inactive-ok-file: LIT-tmpq0e56 THEORY-tmpmqxmo — Unavailable, Proposed or new; the chapter this stands in for, and the account filed from it -->

# LIT-tmp6aj47: Self-foldability of monohedral quadrilateral origami tessellations

Hull, T. C. & Tachi, T. (2018). Self-foldability of monohedral quadrilateral origami tessellations. In *Origami⁷: Proceedings of the 7th International Meeting on Origami Science, Mathematics, and Education*, Tarquin, pp. 521–532. arXiv:1809.04243.

## Key takeaways

*From the reading, [NOTE-tmpryygx](../notes.d/NOTE-tmpryygx.md). Section and theorem numbers are the arXiv version's.*

- **Driving force** (§2): "A vector field f on S is called a driving force
  for the rigid folding ρ(t) if ρ′ (t) · f (ρ(t)) > 0 for all t ∈ [0, s]."
  Separable means "each actuator at the crease knows its own folding
  angle, but not the others" (footnote 1).
- **A dimension count** (Theorem 2): a driving force for unique self-folding
  needs the tangent space at flat to exceed the span of the wrong-mode
  tangents, "(I.e., we need m > n.)"
- **The result** (abstract): "the Miura-ori and Chicken Wire patterns are
  not self-foldable under our definition, but such tilings that are
  rotationally-symmetric about the midpoints of the tile are uniquely
  self-foldable".
- **The moral** (§5): "fewer folding modes imply easier self-foldability".
- **The caveat** (§5): the model "does not take material stiffness or
  bending energy into account".

## Standing in the record

Registered as a stand-in for Hull's chapter "Rigid Origami Theory"
([LIT-tmpq0e56](LIT-tmpq0e56.md)), which a paywall kept from being read. It covers the
self-folding theory that the chapter's summary names, actuators that
should fold the pattern "to a target state and not to some other rigid
origami state", with its main theorems; not the chapter's NP-hardness
section (for which see [LIT-tmpj5g19](LIT-tmpj5g19.md)), its quadratic-form germ theorem, or
its own statement of the theory's limitations. The pasted synthesis on
constraint architectures does not cite it, but it is the formal version of
A's problem of selecting a branch and of A's distinction between a target existing
and its being reliably reached: a mode exists, and whether crease-local
actuation can select it is a separate question. Filed from it:
[THEORY-tmpmqxmo](../theory.d/THEORY-tmpmqxmo.md). No instruction for machine-learning practice.
