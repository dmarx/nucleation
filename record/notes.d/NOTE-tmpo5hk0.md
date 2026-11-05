---
status: Read
paper: 'LIT-tmp4oafb'
title: 'Kinoshita and Ohsaki — Bistable compliant frames converted from truss mechanisms'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in full on 2026-11-05 from the publisher's open-access PDF on
    J-STAGE (https://www.jstage.jst.go.jp/article/jcst/3/2/3_2_417/_pdf),
    9 pages, text extracted by pdftotext. Read: the abstract, Secs. 1–6,
    Table 1 and the reference list. The figures were read by caption only,
    since their curves do not survive as text; nothing in the main text was
    skipped. Quotes below were checked against the extracted text; the PDF
    sets "ff" as a ligature.
date: '2026-11-05'
summary: >-
  A bistable compliant truss mechanism, found by an earlier optimization,
  is converted into a single-piece frame by replacing each pin joint with
  a pseudo-joint of thin end regions and optimizing their area and length
  ratios (OPT2) to keep the output displacement and a second
  self-equilibrium state, under a strain cap that prevents a point hinge.
  In the one example the frame keeps the second equilibrium, with the
  largest thin-element strain at 0.99 of the cap. Computational, one
  example, no fabrication.
---
<!-- inactive-ok-file: THEORY-tmpl2ztw — Proposed and new; the account filed from the reading of Kinoshita and Ohsaki (2009) -->

# NOTE-tmpo5hk0: Kinoshita and Ohsaki — Bistable compliant frames converted from truss mechanisms

## Contribution

A conversion step. Earlier work by the second author found bistable
compliant mechanisms as pin-jointed trusses, which sidesteps the local
buckling that stopped frame optimizations with geometric nonlinearity
from converging, but a truss with pin joints cannot be made as a single
piece. This paper adds the second level of a two-level method: OPT1 finds
the truss (from the earlier papers), OPT2 turns it into a frame of rigidly
jointed members that traces the truss's equilibrium path and keeps a
second stable state.

## Key insight

A design found in an idealized constraint model does not carry over to a
model with other constraints for free. Replacing pins by rigid joints
adds bending stiffness everywhere, which can stabilize what the truss
needed a bar for, and can also suppress the snap-through altogether. The
flexibility has to be put back deliberately, at the joints, and bounded so
that it does not collapse into a point hinge.

## Assumptions

- **A truss is given.** OPT1 is not re-described: "See (14) for details of
  OPT1" (Sec. 4.1).
- **Quasi-static, geometrically nonlinear analysis** under a forced input
  displacement at node A; SQP through IDESIGN 3.5 (Sec. 5).
- **Design variables** are only the end-region ratios α (area) and β
  (length) of each member; the thick-part areas stay at the truss values
  (Sec. 4.2).
- **The second stable state needs an obstacle**, placed at a chosen input
  displacement (U_A = 0.0115 m in the example).
- **In the two-bar study** a horizontal spring K stands in for the rest of
  the structure (Sec. 3).

## Key results

- **The definition (Sec. 2).** A bistable truss mechanism produces a large
  output displacement from an input displacement; "The deformed state can
  be retained without external loads; i.e., the structure has two
  self-equilibrium states including the undeformed initial state"; has
  moderately large stiffness in both states once the input is
  constrained; and "The undeformed initial state can be recovered by
  reversely applying a small force as a disturbance at the deformed final
  state."
- **Bistability by contact (Sec. 2).** In the two-bar truss the collinear
  state at P = 0 beyond the limit point "is stabilized by contact to the
  obstacle slightly below the horizontal line between the two supports".
- **The two-bar parametric study (Sec. 3).** "the behavior of the frame
  with a = A/50 is almost equivalent to that of the two-bar truss", a being
  the thin-element area; too-stiff joints lose the snap-through.
- **The objective (Sec. 4.2).** "In order to have the second stable
  self-equilibrium state with an appropriately located obstacle, P∗ should
  have a negative value. Therefore, we minimize P∗ as objective function",
  P∗ the reaction at the second limit point, subject to the output
  displacement being kept, maximum thin-element strain at most ε̄, and
  bounds on α and β.
- **The example (Sec. 5, Table 1).** From a seven-node ground structure, a
  truss with a buckling triangle is found; OPT2 starts from it with member
  3 removed. The frame "also has the second self-equilibrium state", and
  with ε̄ = 0.05 the strain ratios of the four thin ends are 0.06, 0.37,
  0.46 and 0.99. "The constraint on strain prevents concentration of
  deformation, and the mechanism without lumped compliant part can be
  obtained."
- **Conclusion (Sec. 6).** "an almost equivalent frame mechanism without
  any lumped compliant part can be generated from a truss mechanism."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A bistable truss mechanism can be converted into a single-piece frame mechanism that keeps a second self-equilibrium state | weak to moderate: one example, shown by force–displacement curves | Sec. 5, Fig. 11 |
| C2 | A strain cap on the thin elements prevents deformation lumping into a point hinge | weak: the cap is active at one end in one example | Table 1 |
| C3 | Thin elements of about A/50 make a two-bar frame behave like the two-bar truss | moderate, for that geometry | Sec. 3, Figs. 5–6 |

## Concepts

- **Bistable truss mechanism**: the four conditions of Sec. 2 (output from
  input; two self-equilibrium states; stiffness in both; recovery by a
  small reverse force).
- **Pseudo-joint**: "a weak joint" made of "extremely thin elements or
  low-stiffness materials" at a connection (Sec. 3); here the thin end
  regions of each member.
- **Snapthrough**: the jump from the limit point L to S when the load,
  rather than the displacement, is controlled (Sec. 2).
- **Lumped compliant part**: deformation concentrated at one point, which
  causes stress concentration; the strain cap prevents it (Sec. 4.2).

## Connections

It rests on Ohsaki and Nishiwaki (2005) for multistable truss mechanisms
by snap-through and contact, and on Ohsaki, Katoh, Kinoshita, Tanigawa,
Avis and Streinu (2009) for generating them by enumerating statically
determinate trusses; on pseudo-joint ideas from Howell, Prasad and Diaz,
and Saxena and Ananthasuresh. The truss-to-frame step is the converse of
Saxena and Ananthasuresh's frame-to-kinematic-chain transformation, which
the introduction cites.

## Bearing on the record

- **The pasted synthesis on constraint architectures.** It lists the paper
  as M7 and characterizes it no further, so nothing it says of it is wrong.
  Its illustration of double well U(x)=a/4(x²−b²)² for bistability as memory is A's
  own toy, not the paper's model: here the second stable state is a
  snap-through held by an obstacle, and the frame needs a negative P∗ for
  it to exist at all. The synthesis's general point that a bistable
  structure retains a state without load is condition (2). Two things it
  misses: condition (4), that the stored state is erased by a small
  reverse force, and the paper's real subject, the conversion between
  constraint models, which bears on A's own point that what a structure
  permits and what it costs to realize it are different properties.
- **[CLAIM-079](../claims.d/CLAIM-079.md), [CLAIM-345](../claims.d/CLAIM-345.md), [CLAIM-347](../claims.d/CLAIM-347.md), [CLAIM-354](../claims.d/CLAIM-354.md), [CLAIM-365](../claims.d/CLAIM-365.md).** The synthesis
  cites these for its Part 2 as a whole; their titles match its glosses.
  None bears on this paper in substance: its stable states are mechanical
  equilibria, with no viability set, control cost or frustration of
  demands.
- **[CLAIM-459](../claims.d/CLAIM-459.md)** (an input to a bistable balance can be efficacious below a
  threshold without changing which regime operates). The limit point L is
  a mechanical threshold of the same shape, but the paper offers no
  mapping to authority. Analogy only; not support.
- **[CLAIM-463](../claims.d/CLAIM-463.md)** (restoring conditions need not restore a lost capacity).
  This mechanism is the opposite case, cheap reversal by a small force; a
  possible contrast, nothing more.
- **[CLAIM-480](../claims.d/CLAIM-480.md)** (composing interactions can turn an interior into a
  constraint). The spring K of the two-bar study stands for the rest of
  the structure, the kind of reduction the claim states, but the paper
  does not derive it.
- Filed: [THEORY-tmpl2ztw](../theory.d/THEORY-tmpl2ztw.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- One numerical example; no fabrication, experiment or dynamic analysis
  of the snap.
- "equivalent" is judged by overlaying force–displacement curves (Fig.
  11); no error measure is given.
- The frame's second equilibrium is reached with the obstacle in place;
  it is not shown to be stable without it.
- The method needs OPT1's truss first; it does not design frames from
  scratch, and OPT1 is described only by reference.

## Open questions

- Does the conversion hold for other trusses and ground structures, or
  only for one with a single buckling triangle? More examples would tell.
- Could the second stable state be made elastic, without the obstacle,
  once bending stiffness is available?
