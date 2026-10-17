---
number: 581
status: Active
formerly:
- THEORY-tmpm3bsn
title: "Two exactly consistent descriptions of one system, at different scales and with equal past–future mutual information, can differ in how that information divides between redundancy and synergy; in small generated Boolean networks under the Williams–Beer redundancy measure the coarser scale was more synergy-biased in every random stochastic system, by at most about 0.07, and the direction mostly reversed for redundancy-biased deterministic ones"
version: 2
history:
- version: 2
  date: '2026-10-17'
  note: >-
    What-this-does-not-say on the redundancy measure points to the now-held
    critiques of I_min (THEORY-tmpim3f9, THEORY-tmp8ox3d). The account is
    unchanged; nothing was recomputed.
tags:
- complex-systems
- information-theory
date: '2026-10-16'
source:
- LIT-027
summary: >-
  Varley & Hoel (2022), [LIT-027](../literature.d/LIT-027.md), read in [NOTE-020](../notes.d/NOTE-020.md). Expanding a 3-node
  macroscale TPM into 4- and 5-node equivalence-class microscales holds
  mutual information fixed with zero inconsistency, so any change in the
  PID's synergy bias B_syn is a change of type, not of amount. In 200
  |Gaussian| TPMs the macroscale gained B_syn by about 0.005–0.07; in 185
  near-deterministic ones most with macro B_syn < 0.5 lost it. One
  redundancy function, no robustness check, tiny constructed systems. The
  "unifying theory" of the title is a framing: the EI section re-describes
  a known decomposition and adds no result.
---
<!-- inactive-ok-file: THEORY-222 THEORY-268 THEORY-497 — Proposed; neighbouring accounts named for comparison, nothing here rests on their being settled -->

# THEORY-581: Two exactly consistent descriptions of one system, at different scales and with equal past–future mutual information, can differ in how that information divides between redundancy and synergy; in small generated Boolean networks under the Williams–Beer redundancy measure the coarser scale was more synergy-biased in every random stochastic system, by at most about 0.07, and the direction mostly reversed for redundancy-biased deterministic ones

## Source

Varley & Hoel (2022), [LIT-027](../literature.d/LIT-027.md), "Emergence as the conversion of
information: a unifying theory", read in full in [NOTE-020](../notes.d/NOTE-020.md).

## What was actually shown

**The measure (Eq. 8).** A partial information decomposition of I(X; Y),
sources the past states of the elements and target the joint future
(Eq. 7), with the Williams–Beer I_min redundancy (Eq. 6). Grouping the
atoms by lattice height gives a spectrum S_i, and the synergy bias is
B_syn = Σ (i/|S|)·S_i, normalised so systems of different sizes compare.

**Logic gates (Table 1).** An XOR built from NAND, AND and OR has B_syn
0.52 as a micro network and 0.833 as a macro gate. But mutual information
also falls, from 2.5 to 1 bit, so these cases mix a change of type with a
loss. The authors say so.

**The expansion method (§3.2).** Split one node of a 3-node macroscale into
an equivalence class of children with the same inputs and outputs, giving
4- and 5-node microscales. Mutual information is unchanged and
inconsistency is zero by construction.

- In all 200 positive-Gaussian systems, B_syn is higher at the macroscale.
  The gain, read off Fig. 4, is about 0.005–0.07 on a scale from 0 to 1,
  and correlates with macroscale B_syn at r = 0.819.
- In the 185 near-deterministic systems, those with macroscale B_syn below
  about 0.5 mostly lose synergy bias at the macroscale, down to about −0.1.

**What could have come out otherwise.** With mutual information and
consistency held fixed, B_syn could have been identical across scales.
It was not, in either direction.

## What this does not say

- **That macroscales convert redundancy into synergy.** That held for one
  generated class. For deterministic, redundancy-biased systems it mostly
  ran the other way. The abstract and title do not say so.
- **That the result holds for another redundancy measure.** Only I_min was
  used. The authors note that it is criticised and that PID redundancy has
  no gold standard. The critiques are now held: I_min credits independent
  sources copied into the target with a full bit of redundancy, and so
  overstates synergy by the same amount where sources are copied
  ([THEORY-tmpim3f9](THEORY-tmpim3f9.md), [THEORY-tmp8ox3d](THEORY-tmp8ox3d.md)). Whether that touches these Gaussian
  systems was not recomputed.
- **That the conversion is a property of the system rather than of the
  construction.** Equivalence-class children share inputs and outputs. If
  they behave as copies, part of the microscale's extra redundancy is put
  there by the expansion. [NOTE-020](../notes.d/NOTE-020.md) could not check the splitting rule
  without the supplementary code.
- **That it is a unifying theory of emergence.** The EI section restates
  EI = determinism − degeneracy and re-describes causal emergence as
  converting transition uncertainty into EI, with no new result. Nothing
  is shown for integrated information or any other measure.
- **That any real system does this.** The macroscales have 3 nodes and the
  data are generated TPMs.

## Connections

- **Effective-information emergence ([THEORY-222](THEORY-222.md))** is Hoel's earlier
  account, which this paper folds under "conversion" by re-description. It
  adds no evidence to that account.
- **The ΦID account ([THEORY-497](THEORY-497.md))** places emergence in one
  description's synergy about its own future, not in a change across
  descriptions. Its review cites this paper for the claim that ΦID lacks a
  macro–micro comparison and calls that a misunderstanding. On [NOTE-020](../notes.d/NOTE-020.md)'s
  reading, splitting a node into equivalence-class children is, for ΦID, a
  change of partition, under which its atoms are expected to change and
  which it does not count as emergence.
- **Local values ([THEORY-268](THEORY-268.md)).** Varley's later paper shows the expected
  quantities used here can be positive while negative at particular
  transitions.
- **The theme issue's editorial ([LIT-021](../literature.d/LIT-021.md))** repeats the claim that this
  paper "overcomes the … dichotomy between strong and weak emergence".
  [NOTE-007](../notes.d/NOTE-007.md) records that the body does not support it.
