---
status: Proposed
promote_when: >-
  A reading of the published paper, or an independent simulation of a
  creased sheet, confirms that sheets trained under the supervisor-gated
  crease-stiffness rule classify unseen test force patterns above chance,
  and that training reduces the number of accessible folded structures as
  the variance of crease stiffness grows while enlarging the attractors of
  those that remain.
title: 'Stern, Arinze, Perez, Palmer and Murugan show in simulation that a creased thin sheet trained by repeatedly folding it under example force patterns, with each crease softening when a supervisor judges the fold correct and stiffening otherwise, comes to fold unseen test force patterns into the correct class''s structure, because the heterogeneous stiffness it acquires eliminates most folded structures and enlarges the basins of a few'
version: 1
tags:
- natural-sciences
- learning-theory
- complex-systems
date: '2026-11-05'
source:
- LIT-tmpz2euq
summary: >-
  Stern, Arinze, Perez, Palmer and Murugan (2020; arXiv 2019), [LIT-tmpz2euq](../literature.d/LIT-tmpz2euq.md),
  read in [NOTE-tmpwrlv9](../notes.d/NOTE-tmpwrlv9.md) from the arXiv v1 preprint, titled differently; the
  PNAS text and the Supplementary Notes were not read. Proposed for that
  reason. It is a result about a model: it does not say that any physical
  sheet has been trained, that the sheet learns without an external
  supervisor, or that it scales beyond small two-class tasks.
---

# THEORY-tmpnd6jt: Stern, Arinze, Perez, Palmer and Murugan show in simulation that a creased thin sheet trained by repeatedly folding it under example force patterns, with each crease softening when a supervisor judges the fold correct and stiffening otherwise, comes to fold unseen test force patterns into the correct class's structure, because the heterogeneous stiffness it acquires eliminates most folded structures and enlarges the basins of a few

## Source

Stern et al. (2020; arXiv v1 2019-10-21), [LIT-tmpz2euq](../literature.d/LIT-tmpz2euq.md); read in [NOTE-tmpwrlv9](../notes.d/NOTE-tmpwrlv9.md), of the preprint.

## What was actually shown

- **Training and test** (Results, Fig. 3): with the rule of Eq. 1, about
  80% of unseen test patterns are classified correctly on spherical-cap
  classes; on two Iris species, 91% of 80 unseen specimens. Test accuracy
  could have stayed at chance; overtraining shows how it fails, all inputs
  folding into one structure.
- **The mechanism** (Eq. 2, Fig. 4): treating structure energies as
  Gaussian with spread set by Δk, the number of accessible structures
  falls fast as Δk grows, and trained sheets show it; "the learning process
  merges attractors of the untrained sheet such that the surviving
  attractors recapitulate features of the desired force-fold mapping."
- **Capacity** (Fig. 5): larger sheets gain more from larger training sets.

## What this does not say

- That plasticity alone trains the sheet: the sign of each update is set
  by an external supervisor against a reference state per class.
- That a physical sheet has been trained; the material argument (a
  stiffness spread under 30% of the mean, a softening-only rule) is about
  feasibility.
- That it handles more than small tasks; the higher-dimensional tasks are
  in the unread Supplementary Notes.
- That the published PNAS text says exactly this; it was retitled and not
  read.
