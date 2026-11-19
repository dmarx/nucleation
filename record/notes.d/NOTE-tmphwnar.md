---
status: Read
paper: LIT-tmp8nrv2
title: 'Gili and others 2024 — Fibration symmetry-breaking supports functional transitions in a brain network engaged in language'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read from the arXiv PDF v1 (https://arxiv.org/pdf/2409.02674, 43 pp.,
    9 figs), text layer: abstract, §§1–5, Methods §§6–18 and figure
    captions. Skipped: the figure images, which alone carry the inferred
    networks' edge lists, so no partition was checked edge by edge for
    balance; references skimmed. Read by a delegated reader on 2026-11-19;
    the filer rechecked every quotation below against the PDF text.
date: '2026-11-19'
---

# NOTE-tmphwnar: Gili and others 2024 — Fibration symmetry-breaking supports functional transitions in a brain network engaged in language

## Contribution

The paper applies the balanced-colouring (fibration) theory of cluster
synchrony to an inverse problem. For each brain state it infers a
structural subnetwork from the observed functional clusters, then reads
the change of inferred partition between states as symmetry breaking.

## Key results

- **Data.** 11 dorsal-stream language regions (SMA, and left and right
  PreMA, SMG, Broca's area, AG, Wernicke's area); 20 healthy subjects; 3T
  BOLD fMRI, 160 volumes per condition; rest, verb generation and phonemic
  fluency. Group-average phase-locking values; cluster-synchronization
  cliques found by percolation, a clique's inner synchrony exceeding its
  links outward (Eq. 1).
- **Baseline.** A literature-based connectome (arcuate, superior
  longitudinal and frontal aslant tracts, callosal homologues) has five
  fibres, and "each fiber is also an orbit" (§14).
- **Inference.** "Decimate the baseline connectome by removing the minimal
  number of edges until the fibers of the decimated graph match the
  coloring obtained from the functional network" (§3.3). The authors call
  this falsifiable: "If there is no solution, then the hypothesis is
  wrong" (§3.3). The §15 objective weights removals and additions both, and
  gives no weights; minimality is enforced only by a "necessary but not
  sufficient" condition.
- **Rest and task.** At rest four fibres, with only the identity
  automorphism; in both tasks five. "In RS, we have four fibers, and in the
  task, we have five" (§18). The two tasks share one partition with a
  different ranking: "Although the ranking of the CS is different for the
  two tasks, the coloring is not" (§3.3). Verb generation's second and
  third clusters are tied in effect (0.625 against 0.624).
- **Crossing partitions.** Derived here, not stated by the paper: from
  rest to task Broca left joins SMA and Broca right joins the Wernicke
  pair, and the resting pentagon splits. Baseline to rest is not a
  coarsening either. The fibre counts the paper reports (5, 4, 5) order
  partitions that the refinement order cannot compare.
- **Thin margins at rest.** Cluster PLVs are 0.689 to 0.762 against
  links between cliques up to 0.682 (§10).
- **Hedges.** The networks "should be interpreted as idealized networks"
  (§15), and the transitions are "analogous to symmetry breaking in
  ferromagnets" (§4).

## Assumptions

- Group-average PLV cliques are exact synchrony classes.
- The observed partition is the coarsest balanced colouring of the
  effective network, which is stronger than balanced, with no reason
  given.
- Identical cells, unweighted directed edges.
- Baseline tracts from the literature, with no diffusion imaging of these
  subjects.
- The task block design regressed out by a GLM, so remaining synchrony
  counts as intrinsic and not as common drive.
- Function is synchronization.

## Concepts

Symmetry fibration and minimal base; input tree; fibre = balanced
colouring = equitable partition; orbits against fibres; Kamei–Cock
refinement; colour refinement (Weisfeiler–Leman), asserted, not proved;
spontaneous against explicit symmetry breaking.

## Bearing on the record

- **THEORY-1065** (balanced partitions are exactly the robust synchrony
  patterns, with no symmetry needed). The paper applies it to graphs with
  only the identity automorphism, which illustrates "symmetry is one way
  to get balance". But its Definition 4 says a fibre "is proven to be
  synchronous", where THEORY-1065 says invariance "says nothing about
  whether the pattern attracts". No stability test is run.
- **THEORY-1059** (dynamics on the quotient). The minimal base is named
  and not used. Left open.
- **THEORY-276** and **QUESTION-147.** The baseline is the case where
  orbits equal fibres; rest and task have fibres without orbits. It cannot
  serve QUESTION-147, since the graph is inferred from the clusters, not
  the clusters predicted from a known graph.
- **CLAIM-405** (criteria pick crossing units). Corroboration at most:
  the rest and task partitions of one system cross, but under one
  criterion applied to two states, not under two criteria.
- **QUESTION-218** (units that are not blocks). Structural fibres are
  equal-input classes that need no internal coupling. But the pipeline
  assumes the functional block and the structural fibre coincide, so it
  does not test which unit one system should track.
- **CLAIM-618** and **CLAIM-567.** The program establishes only that a
  balanced, invariant configuration exists, the compatibility side.
  Nothing tests attraction or reliable emergence, yet the paper says it
  explains the observed synchrony.
- **CASE-179** and **QUESTION-063.** A partial natural analogue: one
  substrate, several states, each with its own inferred coupling. Nothing
  is manipulated independently, and the task is a shared drive controlled
  only by GLM regression.
- **QUESTION-125.** A candidate boundary change (rest to task), but with
  no parametrized family or dynamical model, and behaviour changes too.
  Left open.

## Limitations

Group averages only; BOLD PLV taken as exact synchrony; near-ties and thin
margins between clusters; literature tracts; edges given only in figures;
no null model of how many arbitrary partitions removal alone would also
make feasible; no dynamics; figure labels inconsistent between §2.2 and
§10.
