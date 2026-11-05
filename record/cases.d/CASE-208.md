---
number: 208
status: Proposed
formerly:
- CASE-tmpjldzw
title: 'A prestressed Kresling stack: reordering the cells'' energy barriers from outside opens the 8 of 56 transitions between stable states that the barrier order blocked, while the 16 that pass through other stable states are not made direct'
version: 1
standing: documented
kind: reported-study
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-571
reported_in:
- LIT-2091
- NOTE-1569
summary: >-
  Filed at the owner's request on 2026-11-05, to file "one or more CASEs
  for origami as a toy model of a resource bounded constraint
  configuration space". Zang, Zhao, Misseroni and Paulino ([NOTE-1569](../notes.d/NOTE-1569.md)):
  a stack of three bistable Kresling cells has 8 stable states and 56
  ordered transitions; 32 are feasible, 16 cannot be made without passing
  through other stable states, and 8 are blocked by the order of the
  cells' energy barriers. Springs and handles, applied from outside,
  prestress the cells and reorder the barriers in place, which makes the
  8 blocked transitions feasible; the 16 are not opened. Read as a
  resource model, the barriers bound the transitions, and the blocked
  ones are opened by changing the architecture, not by a larger load: the
  physical counterpart of [CASE-198](CASE-198.md). Jules et al. ([NOTE-1617](../notes.d/NOTE-1617.md))
  show the same dependence on the order of thresholds in a Kresling
  memory. A mechanical study; its organizational reading is an analogy.
  Adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-571 CASE-198 — Proposed; the entries filed beside it on 2026-11-05, cited as filed, nothing here rests on their being settled -->

# CASE-208: A prestressed Kresling stack: reordering the cells' energy barriers from outside opens the 8 of 56 transitions between stable states that the barrier order blocked, while the 16 that pass through other stable states are not made direct

## The case

**The study.** Zang, Zhao, Misseroni and Paulino ([NOTE-1569](../notes.d/NOTE-1569.md)) model and
build Kresling origami cells, each bistable, and stack three. Spring
elements of three kinds, axial, torsional and along the mountain creases,
prestress a cell; the authors call this geometrical frustration. In the
model and in prototypes the prestress moves the cell's energy barrier
continuously, and enough of it in the deploying direction turns the cell
from bistable to monostable. The barrier is "the difference between the
local maximum on the landscape and the initial base energy."

**The count.** Three bistable cells give 2³ = 8 stable states and
8 × 7 = 56 ordered transitions between them. In the standard stack:

- **16** cannot be made without passing through other stable states;
- **8** more are infeasible because of the order of the cells' intrinsic
  barriers;
- **32** are feasible, 56 − 16 − 8 = 32; eight were checked by experiment.

Prestressing the cells in place makes the 8 blocked transitions
feasible, four of them shown by experiment. The 16 that need
intermediate states are not among them. The authors note that building
different cells could open the same paths, but that "this discrete
approach inevitably introduces new infeasible folding paths and does not
support in-situ reconfiguration."

**The resource reading (the filer's).** Read the barriers as the
resource bound on each cell's switch, in the sense of [CLAIM-571](../claims.d/CLAIM-571.md):
under the declared loading, a transition between stable states is made
when the load carries each cell that must switch over its barrier, in
the order the path requires. The 8 blocked transitions are not blocked by
the size of the load. They need a cell to switch before one whose barrier
is lower, and under one load applied to the whole stack, on this reading,
a larger load does not change which barrier is crossed first. So no
budget of that load opens them, and changing the architecture, the
barriers' order, does. That is [CASE-198](CASE-198.md)'s architecture-mediated
route, met in a physical system: a move that changes the architecture
opens what no budget under the old one could. The 16 are a different
matter. They are reachable, as sequences through intermediate stable
states; what is missing is a direct path, and prestress does not supply
one.

**A neighbour.** Jules et al. ([NOTE-1617](../notes.d/NOTE-1617.md)) stack four bistable Kresling
barrels in series and find a Preisach memory whose transition graph
depends on the switching thresholds only through their order; when the
two orders coincide there are no Garden of Eden states. Barrier order, not
barrier size, decides what is reachable there too.

## What it can show

- **That [CLAIM-571](../claims.d/CLAIM-571.md)'s "for a fixed architecture" does work**, in a
  built system: what is infeasible under one ordering of barriers is
  feasible under another, without refabrication.
- **That a budget and an order are different bounds.** Raising the load
  meets a threshold; it does not reorder thresholds. Some transitions need
  the second.
- **That opening transitions in place differs from redesigning**, which
  the authors say opens some paths and closes others. Read against
  [CLAIM-025](../claims.d/CLAIM-025.md), the stable states play the regimes, the barrier order the
  organization among them, and the springs and handles the capacity to
  transform it; the reading of the paper offers this as an analogy.
- **An analogy to relief, with a caution.** Read the 56 transitions as
  demands and feasibility as acceptance, and prestress enlarges the
  feasible set with no demand dropped, the shape of [CLAIM-347](../claims.d/CLAIM-347.md)'s relief by
  strict enlargement. But the frustration that does the enlarging is
  stored elastic energy, the energetic sense [TERM-060](../terms.d/TERM-060.md) sets apart from its
  own. The mapping is the record's, not the paper's.
- **[CLAIM-079](../claims.d/CLAIM-079.md), weakly.** The cells keep their stable states while which
  transitions are possible changes.

## What it cannot show

- **Anything about organizations.** It is a mechanical study; every
  organizational reading here is an analogy.
- **That one prestress setting opens all 8 and closes none of the 32.**
  The filed reading reports the 8 opened in the frustrated stack and does
  not say whether any previously feasible transition was lost.
- **That the load cannot open the 8 in any protocol.** That is the
  filer's reading of the paper's reason, the order of the barriers, under
  one load applied to the whole stack.
- **Scale.** Three cells; the theory omits the panel buckling the
  experiments show, and the SI, with the nonlinear springs, was not read.
- **That the structure sets its own constraints.** The prestress is
  supplied from outside.
