---
number: 178
status: Active
formerly:
- THEORY-tmpcasth
title: 'In an ensemble of sign-consistent Boolean rules on the 87-gene core of E. coli''s regulatory network, a transient knockout or overexpression of one gene can leave the network in a different attractor after release, and every gene that does so reaches a strongly connected component containing a positive circuit'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision file for THEORY-178 (batch 033, ADR-047
    v3). The study was read in full, and the title now claims no more
    than it showed: a model ensemble, not cells. The positive-circuit
    condition is stated as measured in this network, because as a general
    law of synchronous Boolean networks it fails. A dated note below gives
    the counterexample. The promote_when, a transient perturbation in
    cells with slow return excluded, moves unchanged to QUESTION-172.
- version: 3
  date: '2026-10-20'
  note: >-
    The wider claim this account dropped when it was narrowed, that
    transcriptional regulation alone can give a bacterium's expression
    state a memory of a transient disturbance, as the paper predicts for
    cells, is filed as the Proposed THEORY-tmp0drff, which extends this
    one (ADR-047 v4, narrowing-loss sweep, batch 068). Status and title
    are unchanged.
tags:
- complex-systems
- network-science
- natural-sciences
date: '2026-10-09'
source:
- LIT-854
summary: >-
  Zhao, Wytock, Reynolds and Motter (2024), [LIT-854](../literature.d/LIT-854.md). In an ensemble
  of sign-consistent Boolean rules on the 87-gene core of the E. coli
  regulatory network, 51 genes admit a transient knockout or
  overexpression that moves the network to a different attractor, and
  every such gene reaches a strongly connected component with a positive
  circuit. So one genotype may hold several heritable expression states
  without epigenetic marks, in the model. The evidence is a model
  ensemble, read in full in NOTE-655, and the title claims no more. No
  transient perturbation has been shown to have a lasting effect in
  cells; that experiment is QUESTION-172.
supports:
- CLAIM-184
extended_by:
- THEORY-tmp0drff
---
<!-- inactive-ok-file: THEORY-tmp0drff — Proposed; the wider claim this account dropped, filed separately and cited as open -->

<!-- inactive-ok-file: THEORY-058 — Proposed; named as a neighbouring self-maintaining-loop account -->

# THEORY-178: In an ensemble of sign-consistent Boolean rules on the 87-gene core of E. coli's regulatory network, a transient knockout or overexpression of one gene can leave the network in a different attractor after release, and every gene that does so reaches a strongly connected component containing a positive circuit

## Source

Zhao, Wytock, Reynolds and Motter (2024), [LIT-854](../literature.d/LIT-854.md), read in full in
[NOTE-655](../notes.d/NOTE-655.md), with the Supplementary Text.

## What was actually shown

The regulatory network of *E. coli* from RegulonDB is cut to the core of its
largest subnetwork: 87 genes and 290 signed edges, outside which no gene can
change the core. The true update rules are unknown, so the paper samples
Boolean rules that use each gene's regulators with their known signs. It
varies how nested and how biased the rules are, and which regulators tend
to dominate. From each attractor, each gene is clamped off or on until the
network settles, then released.

- **Across the ensemble, 51 of the 87 genes can leave the network in a
  different attractor after release.** The 36 that cannot are leaves, or
  feed only self-repressing leaves.
- **Each of the 51 can reach a strongly connected component containing a
  positive circuit**, and every gene that can reach one is irreversible for
  some rules. Positive circuits are necessary for more than one stable state
  (Thomas's rule, cited); the paper extends the argument to attractors that
  are fixed only in part.
- **The likelihood rises with the weighted number of paths** to such
  components (a power law explaining 55–62% of the variance).
- **Transitions tend to run from small basins of attraction to larger
  ones.**

What could have come out otherwise: the core might have had few positive
circuits reachable by single genes, or transient clamps might have
returned the network to its basin almost always. Neither happened in the
model. The one comparison with cells is with strains evolved for ten days
after a permanent crp knockout. It confirms the signed network's predicted
direction of change well and the irreversibility prediction only weakly
(P = 0.03 on comparison groups of 2 and 8 genes).

## What this does not say

- **Not that it has been observed.** No transient perturbation was
  performed. By [THEORY-136](THEORY-136.md)'s standard, a lasting shift after a temporary
  disturbance is evidence only once slow return is excluded, and the
  authors expect noise and division to make the model's permanent changes
  merely long-lived.
- **Not that the 51 genes do this in cells.** Each is irreversible "for
  some rules"; which rules the cell runs is unknown, and most attractors of
  the model may never be visited.
- **Not that bacteria have no epigenetics, or that regulatory memory is new.**
  Environmentally triggered bistable switches (lac, mar, sporulation) are
  long known. The claim is that genetic perturbation of regulation alone,
  across a whole network, suffices.
- **Not that adaptive evolution is a release of a transient knockout.** The
  paper's "akin to" between them is an intuition, and its supporting test
  is weak.
- **Not a statement about eukaryotic cell fate**, where chromatin marks do
  the locking the paper sets aside.
- **Not that a positive circuit is necessary in every Boolean network.**
  In this core every irreversible gene reaches one. As a general law of
  synchronous networks the condition fails (see the note of 2026-10-19).

## Connections

- **[THEORY-136](THEORY-136.md)** gives the evidential standard that a claim about cells
  must meet, and [QUESTION-172](../questions.d/QUESTION-172.md) is written to it. Its remark that positive
  feedback must be strong to make alternative states matches the paper's
  continuous model: self-activation and switch-like response favour
  irreversibility.
- **[THEORY-058](THEORY-058.md)** puts self-maintaining loops in symptom networks; this is
  the same mechanism at the molecular scale, and like it lacks a direct
  demonstration of hysteresis. No relation is declared.

## Note of 2026-10-19: why the positive-circuit condition is stated for this network

The promotion audit tried to re-derive the paper's necessity argument as a
general theorem ([ADR-047](../decisions.d/ADR-047.md) v2). It does not hold for synchronous Boolean
networks in general.

1. Take a negative 2-cycle, a → b and b ⊣ a, with a' = ¬b and b' = a.
   Every state lies on one period-4 cycle:
   (0,0) → (1,0) → (1,1) → (0,1) → (0,0).
2. Put an independent copy (c, d) elsewhere in the network. The joint
   network has four attractors, one for each phase offset between the two
   cycles.
3. Clamp a and release it. The (a, b) cycle resumes at a shifted phase
   while (c, d) keeps its own, so the network can end on a different joint
   attractor. Yet a reaches only {a, b}, which holds no positive circuit.

So necessity needs more than Thomas's rule. It needs that no gene outside
the reach of positive circuits sits on a free negative oscillator. The
paper silences autorepression when a gene is off, which removes the
simplest case, a negative self-loop. In this core the condition holds,
because the 36 genes that are never irreversible are 32 leaves and four
genes (metJ, pdhR, argP, nac) whose only output is an autorepressive leaf
([NOTE-655](../notes.d/NOTE-655.md), from the Supplementary Text). The title therefore states the
condition as measured in this network.

## Note of 2026-10-20: the wider claim, filed separately

When this account was narrowed, its wider form went nowhere a later result
could confirm or reject it. Under [ADR-047](../decisions.d/ADR-047.md) v4 it is now the Proposed
[THEORY-tmp0drff](THEORY-tmp0drff.md): that transcriptional regulation alone can give a
bacterium's expression state a memory of a transient disturbance, as the
paper predicts for cells. This account is that one's evidence, and nothing
here changes.
