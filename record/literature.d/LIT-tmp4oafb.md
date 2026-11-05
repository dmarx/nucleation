---
status: Active
status_note: >-
  read in full 2026-11-05 ([NOTE-tmpo5hk0](../notes.d/NOTE-tmpo5hk0.md)) from the publisher's open-access
  PDF on J-STAGE; worth reading as a short worked case of a design found
  in one constraint model (pin-jointed bars, no bending) having to be
  re-realized in another (rigid joints with bending) by a second
  optimization: a bistable truss mechanism, whose second stable state is
  snap-through stopped by an obstacle, is converted into a single-piece
  frame by sizing thin end regions at the former pin joints under a strain
  cap, so that no point hinge forms. Its main limits: one numerical
  example, no fabrication or experiment, equivalence shown only by
  overlaid force–displacement curves, and the second stable state still
  rests on a placed obstacle.
title: 'Synthesis of Bistable Compliant Structures from Truss Mechanisms'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami, written by another
    assistant (A) and pasted by the owner on 2026-11-04, which lists it as
    M7 without characterizing it. Citation checked against Crossref by the
    reader: Takuya Kinoshita and Makoto Ohsaki (Kyoto University), Journal
    of Computational Science and Technology (JSME) 3(2), 417–425, journal
    article. A's citation is correct. Crossref gives the year only and no
    preprint was found, so `published:` is the first of January 2009; the
    paper itself carries "Received 21 Apr., 2009", and the PDF was made in
    August 2009. Not held before (no hit for the DOI, the title or either
    author). Copy: the publisher's open-access PDF on J-STAGE,
    https://www.jstage.jst.go.jp/article/jcst/3/2/3_2_417/_pdf, 9 pages,
    extracted with pdftotext.
tags:
- natural-sciences
- operations-research
date: '2026-11-05'
published: '2009-01-01'
doi: '10.1299/jcst.3.417'
first_author: 'Kinoshita'
keywords:
- 'compliant mechanism'
- 'bistable structure'
- 'optimization'
- 'snapthrough'
- 'pseudo-joint'
implementations: []
summary: >-
  Kinoshita & Ohsaki (2009). Bistable compliant mechanisms are easier to
  find as pin-jointed trusses, since optimizing frames with geometric
  nonlinearity failed to converge because of local buckling, but a pin-
  jointed truss cannot be made in one piece. The authors convert a given
  bistable truss, whose second stable state is snap-through held by contact
  with an obstacle, into an equivalent frame: each pin joint becomes a
  pseudo-joint of thin end regions whose area and length ratios are
  optimized to keep the output displacement and a second self-equilibrium
  state, under a cap on strain that stops deformation lumping into a point
  hinge. A two-bar study and one seven-node example show it.
---
<!-- inactive-ok-file: THEORY-tmpl2ztw — Proposed and new; the account filed from this reading -->

# LIT-tmp4oafb: Synthesis of Bistable Compliant Structures from Truss Mechanisms

Kinoshita, T. & Ohsaki, M. (2009). Synthesis of Bistable Compliant Structures from Truss Mechanisms. *Journal of Computational Science and Technology* 3(2): 417–425. doi:10.1299/jcst.3.417.

## Key takeaways

*From the reading, [NOTE-tmpo5hk0](../notes.d/NOTE-tmpo5hk0.md). Sections are the paper's.*

- **What bistable means here.** Among four conditions, "The deformed state
  can be retained without external loads" and "The undeformed initial state
  can be recovered by reversely applying a small force as a disturbance at
  the deformed final state" (Sec. 2).
- **Where the second state comes from.** The collinear state "is stabilized
  by contact to the obstacle slightly below the horizontal line between the
  two supports" (Sec. 2): snap-through plus a unilateral contact, not an
  elastic double well.
- **Why trusses first.** "due to local buckling of each element,
  optimization process with frame element considering geometrical
  nonlinearity did not converge" (Sec. 2).
- **Bending replaces a bar.** "The truss becomes unstable if the bar CD is
  removed", but it is stabilized by rigidly jointed members "that have
  bending stiffness" (Sec. 3).
- **The strain cap does the work.** "The constraint on strain prevents
  concentration of deformation, and the mechanism without lumped compliant
  part can be obtained" (Sec. 5).

## Standing in the record

The pasted synthesis on constraint architectures lists it among its
compliant-mechanism sources and says nothing more of it. Its own
illustration of bistability as memory, a quartic double well, is A's and
is not this paper's mechanism, whose second state is held by an obstacle
after snap-through. What the paper is good for here is narrower and more
useful: a design found in an idealized constraint model has to be
re-realized, by a second optimization, in a model with different
constraints (bending at the joints), and the cheap reversal by a small
force is part of its definition. The record holds no other mechanics of
trusses or snap-through. Filed from it: [THEORY-tmpl2ztw](../theory.d/THEORY-tmpl2ztw.md). No instruction
for machine-learning practice.
