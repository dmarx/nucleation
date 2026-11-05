---
status: Read
paper: 'LIT-tmp24k66'
title: 'Berry, Lee-Trimble and Santangelo — Vertex curvature and the topology of origami configuration space'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in full on 2026-11-05 from the arXiv v1 PDF
    (https://arxiv.org/pdf/1910.01008v1), text extracted by pdftotext.
    arXiv holds only v1, which predates acceptance; the published PRE text
    may differ and was not compared. Read: the abstract, Sections I
    (mathematical formulation), II (single vertices) and III (conclusions),
    and Appendices A and B, 8 pages in all. Nothing skipped but the
    reference list. Quotes below were checked against the extracted text.
date: '2026-11-05'
summary: >-
  Extends Chen and Santangelo's second-order theory to origami whose
  vertices carry Gaussian curvature K. The vertex condition becomes hᵀQh =
  K; with one negative eigenvalue in Q, a vertex with small K > 0 has its
  two nappes (popped up, popped down) in disconnected components near the
  flat state, and one with K < 0 has them joined by a neck, given that
  faces may not pass through each other. Degree-4 vertices are split for
  both signs. The multi-vertex extension is conditional, and the
  suggestion that curvature can prevent misfolding is deferred to future
  work.
---
<!-- inactive-ok-file: THEORY-tmps6lqg — Proposed or new; cited from the reading of Berry, Lee-Trimble and Santangelo (2020) as open -->

# NOTE-tmpt066u: Berry, Lee-Trimble and Santangelo — Vertex curvature and the topology of origami configuration space

## Contribution

Non-Euclidean origami, in the authors' words, means "faces are flat,
but" that "the vertices have Gaussian curvature" (§I). The paper carries
the second-order analysis of flat triangulated origami over to such
vertices and shows that the sign of the curvature changes the topology of
the configuration space near the flat state.

## Key insight

At a flat vertex the second-order condition is a cone, hᵀQh = 0, whose two
nappes touch at the flat state. Curvature shifts the right-hand side to K.
With one negative eigenvalue in Q, K > 0 gives a two-sheeted hyperboloid
whose sheets no longer meet, and K < 0 a one-sheeted hyperboloid whose
sheets are joined. Whether popping up and popping down are connected is
set by the sign of the curvature, a quantity fixed when the sheet is made.

## Assumptions

- **Almost flat** (§I): sector sums near 2π, fold angles near flat, |K|
  small. All results are local to the flat state.
- **Mostly triangulated faces**; a non-triangular face is handled by
  adding diagonals held flat.
- **No self-intersection**, implemented as fold angles strictly within
  (−π, π), with an orientation. The disconnection depends on it.
- **For several vertices** (§III), two distinct real solutions for each
  vertex height.

## Key results

- **The isometry condition** (§I, eq. 4, App. A): hᵀQ_n h = K_n, read by the
  authors as "This is then a discrete version of Gauss’ theorema egregium",
  with the caution "Despite the plausible form of Eq. (4), the proof that
  Eq. (4) correctly determines the isometries to quadratic order is
  somewhat involved."
- **One vertex** (§II, eqs. 9–10): for K > 0 "the two nappes have split
  into two disconnected components"; for K < 0 "both nappes remain
  connected near the flat state but are connected by a neck".
- **Numerics** (§II): tracing a symmetric 5-fold vertex with fold angles
  kept in (−π, π), the nappes are "touching at one point (K = 0),
  disconnected (K > 0), or connected by a narrow neck (K < 0)."
- **Self-intersection** (§II): against Streinu and Whiteley, who find the
  configuration space connected, "in their analysis, faces can pass
  through each other"; and "Anecdotally, it does appear that when faces are
  allowed to pass through each other, isometric trajectories can pass from
  one nappe to the other for any K."
- **Degree 4** (§II): "the two nappes become disconnected for both positive
  and negative Gaussian curvature."
- **Several vertices** (§III): the argument needs "We further assume that
  this equation has two distinct real solutions for hn ." Open: "it is
  difficult to determine whether or not every combination of nappes can be
  realized when K > 0." For K < 0, "there is no reason that global
  constraints might not lead to disconnected components of the
  configuration space".
- **Design** (§III): "Gaussian curvature provides a new means of
  controlling how a responsive origami structure self-folds by separating
  the individual nappes so that misfolding is significantly less likely."
  "This suggestion will be followed up in a future work."

## Concepts

- **Vertex curvature**: K_n = 2π − Σα_i, the angle deficit.
- **Nappe**: one of the two sheets of a vertex's near-flat configuration
  space, told apart by the sign of the component along Q's negative
  eigenvector (popping up or down).
- **Configuration space**: the isometries of the fold pattern, edge lengths
  and face angles preserved.

## Connections

It extends Chen and Santangelo (2018), LIT-tmp0ouv4, from flat to curved
vertices, and contrasts with Streinu and Whiteley's connectedness result,
which Abel et al. (2016), LIT-tmpry5n6, also cite. Foschi, Hull and Ku
(2022), LIT-tmpegvxm, reach the same disconnection for non-Euclidean
degree-4 vertices from exact equations rather than a near-flat expansion.
Its introduction cites Akitaya et al., LIT-tmpj5g19, for "Understanding
whether an origami fold pattern can be folded without tearing is NP-hard".

## Bearing on the record

- **The pasted synthesis's description.** A writes that the configuration
  space of positively curved vertices "separates into disconnected
  components. No continuous non-self-intersecting folding path joins
  them". Those words are A's paraphrase; they do not occur in the paper.
  The abstract's words are "decomposes into disconnected subspaces; there
  is no pathway between them without tearing the origami". A's paraphrase
  is right in substance but drops the conditions: the result is for
  near-flat states with small curvature and no self-intersection, the
  multi-vertex statement is conditional, and A omits both the
  negative-curvature contrast and the degree-4 exception.
- **A's use of it.** As an instance of "Feasible target ⇏ reachable
  target" it is fair. Each nappe's states are feasible, and under the
  declared admissible motions one cannot reach the other. It also bears
  out A's line that impossibility is relative to the declared model of
  admissible transformations: allow faces to pass through each other and
  the separation reportedly disappears.
- **CLAIM-347 (frustration as an ordinal fact).** Qualifies. A declared set
  of admissible transformations fixes which configurations connect, which
  echoes TERM-060's "under its admissible transformations", applied to
  reachability rather than joint satisfiability. It is not frustration:
  every configuration on each nappe meets every constraint. A's gloss,
  that the two are "not interchangeable", is right.
- **TERM-060 (structural frustration).** Kept distinct for the same reason:
  no demand set here is jointly unsatisfiable.
- **QUESTION-281 (dynamical transitions; nucleation across a barrier).**
  Qualifies by contrast. This is a kinematic separation, not an energetic
  barrier: no energy suffices to cross it without tearing. A says the two
  kinds of transition "should not be conflated", and this paper is a case
  for keeping them apart.
- **CLAIM-495, CLAIM-538, THEORY-1082**: not engaged. Curvature changes the
  topology of a quadric here; nothing is transported round a loop.
- **CLAIM-464, CLAIM-352** (reachability under admissible moves): loose
  support for the general point that reachability depends on the move set;
  not engaged in substance.
- Filed: THEORY-tmps6lqg. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **Local**: near-flat, small |K|.
- **Conditional** for several vertices, and which combinations of nappes
  are realizable is open.
- **The proof of eq. 4** to quadratic order is, by the authors, "somewhat
  involved", and is sketched in an appendix.
- **Kinematic**: energetics only through an illustrative torsional-spring
  functional.
- **Preprint**: the PRE version was not compared.
