---
status: Proposed
promote_when: >-
  An experiment in bacteria, read first-hand, in which a gene is perturbed
  transiently (for example by inducible CRISPR interference, then
  released) with the growth environment held fixed, and other genes stay
  in their changed expression state for many generations after the
  perturbation is gone, with slow return excluded: either by following the
  culture until the state has outlasted any plausible relaxation time, or
  by showing that unperturbed cells started from the other state hold it
  under the same conditions. Refuted for the network if well-powered
  transient perturbations of the predicted genes (crp, with zraR, melR or
  rhaRS as responders) are always followed by a return to the starting
  state. What would not settle it: further simulations or rule ensembles;
  agreement with strains evolved under a permanent knockout, which is not
  a temporary disturbance; and environmentally induced bistable switches
  such as the lac operon, which were known before and are not
  perturbations of regulation alone.
title: 'Transcriptional regulation alone can make a bacterium''s gene-expression state depend on its history: a transient change to one regulator can leave its regulatory network in a different self-maintaining state, but only through a gene that reaches a positive circuit'
version: 1
tags:
- complex-systems
- network-science
- natural-sciences
date: '2026-10-09'
source:
- LIT-tmpolt4z
summary: >-
  Zhao, Wytock, Reynolds and Motter (2024), [LIT-tmpolt4z](../literature.d/LIT-tmpolt4z.md). In an ensemble
  of sign-consistent Boolean rules on the 87-gene core of the E. coli
  regulatory network, 51 genes admit a transient knockout or
  overexpression that moves the network to a different attractor, and
  every such gene reaches a strongly connected component with a positive
  circuit. So one genotype may hold several heritable expression states
  without epigenetic marks. The evidence is a model ensemble; no transient
  perturbation has been shown to have a lasting effect in cells, so the
  account is Proposed.
---

<!-- inactive-ok-file: THEORY-058 — Proposed; named as a neighbouring self-maintaining-loop account -->

# THEORY-tmpcasth: Transcriptional regulation alone can make a bacterium's gene-expression state depend on its history: a transient change to one regulator can leave its regulatory network in a different self-maintaining state, but only through a gene that reaches a positive circuit

## Source

Zhao, Wytock, Reynolds and Motter (2024), [LIT-tmpolt4z](../literature.d/LIT-tmpolt4z.md), read in
[NOTE-tmpavdpk](../notes.d/NOTE-tmpavdpk.md).

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

## Connections

- **[THEORY-136](THEORY-136.md)** gives the evidential standard this account must meet, and
  the promotion condition above is written to it. Its remark that positive
  feedback must be strong to make alternative states matches the paper's
  continuous model: self-activation and switch-like response favour
  irreversibility.
- **[THEORY-058](THEORY-058.md)** puts self-maintaining loops in symptom networks; this is
  the same mechanism at the molecular scale, and like it lacks a direct
  demonstration of hysteresis. No relation is declared.
