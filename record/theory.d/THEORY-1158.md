---
number: 1158
status: Active
formerly:
- THEORY-tmpy1s8c
title: 'On synchronization of S4 relations with outliers, an untrained mechanism that composes relations through third vertices gains 26–45 points over the single direct path, and weighting the candidate paths by the Wilson loops of squares that avoid the missing edge adds 0.6–7.8 points, most where clean two-hop paths become a minority; it stays below spectral synchronization with one reweighting pass on every setting and within 2.2 points of plain spectral synchronization either way; its 0.99 AUC for corrupted triangles is the ceiling that exactly flat clean data set, not a measure of detection power'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed first. 'without beating spectral synchronization' was a
    mis-statement: by Table 1 (NOTE-1331), holonomy weighting beats plain
    spectral synchronization on three of four settings (0.988 against
    0.987, 0.937 against 0.933, 0.700 against 0.678) and trails it only on
    the sparse graph (0.886 against 0.897), while spectral synchronization
    with one reweighting pass is ahead on every row. The title now says
    so; the dropped wording is kind 3 of ADR-047's routing, recorded here.
    Old title: "On synchronization of S4 relations with outliers, an
    untrained mechanism that composes relations through third vertices
    gains 26–45 points over the single direct path, and weighting the
    candidate paths by the Wilson loops of squares that avoid the missing
    edge adds 0.6–7.8 points, most where clean two-hop paths become a
    minority, without beating spectral synchronization; its 0.99 AUC for
    corrupted triangles is the ceiling that exactly flat clean data set,
    not a measure of detection power". Promoted to Active under ADR-065,
    at the status review's ruling (the owner delegated these rulings). The
    title reports what one study, read in full in NOTE-1331, measured,
    with the study's hedges kept, and nothing in the record contradicts
    it. The old promote_when read: "A rerun of the released harness, or an
    independent implementation, that reproduces Table 1's single-path,
    uniform and holonomy columns within their stated intervals, including
    the paired holonomy − uniform gains. A rerun on new synthetic data
    built flat does not bear on the second half of the title, which is
    arithmetic and already checked." Its demand for a rerun of the
    released harness reproducing Table 1 asks for replication, more than
    the title asserts, and moves to QUESTION-343.
tags:
- network-science
- compositionality
date: '2026-10-29'
source:
- LIT-1820
summary: >-
  Sarkar, Mukherjee and Sato (2026), [LIT-1820](../literature.d/LIT-1820.md), §3 and Table 1, read
  in [NOTE-1331](../notes.d/NOTE-1331.md). The accuracies are the paper's, on 1000 instances
  per cell, and were not rerun. The AUC ceiling was recomputed here:
  1.42% of corrupted triangles at p = 0.3 have cancelling corruptions,
  so the ceiling is 0.9929. What the experiment does not show is
  anything about learned operators, language, or relations not given as
  group elements.
---

# THEORY-1158: On synchronization of S4 relations with outliers, an untrained mechanism that composes relations through third vertices gains 26–45 points over the single direct path, and weighting the candidate paths by the Wilson loops of squares that avoid the missing edge adds 0.6–7.8 points, most where clean two-hop paths become a minority; it stays below spectral synchronization with one reweighting pass on every setting and within 2.2 points of plain spectral synchronization either way; its 0.99 AUC for corrupted triangles is the ceiling that exactly flat clean data set, not a measure of detection power

## Source

Sarkar, Mukherjee and Sato (2026), [LIT-1820](../literature.d/LIT-1820.md), §3, Table 1 and Figure 1
(pp. 3–4) of the arXiv preprint 2610.37656v1; read in [NOTE-1331](../notes.d/NOTE-1331.md).

## What was actually shown

**The task.** Fourteen entities carry hidden S4 frames. A random connected
set of pairs is observed, each replaced with probability p by a different
uniform element, and the task is the relation between an unobserved pair
(p. 3). Relations are the faithful 4×4 permutation matrices, nothing is
learned, and four rounds of the update are run.

**The accuracies (Table 1, p. 4).** Single path / uniform average of
two-hop candidates / holonomy-weighted / Singer's spectral method / spectral
with one reweighting pass:

- sparse, degree 5, p = 0.2: 0.625 / 0.872 / 0.886 / 0.897 / 0.912;
- dense, degree 8, p = 0.2: 0.645 / 0.982 / 0.988 / 0.987 / 0.990;
- dense, p = 0.3: 0.488 / 0.912 / 0.937 / 0.933 / 0.949;
- dense, p = 0.45: 0.309 / 0.623 / 0.700 / 0.678 / 0.753.

The paired holonomy − uniform gains are +0.014, +0.006, +0.026 and +0.078.
The paper locates the onset where clean two-hop paths become a minority,
(1 − p)² = ½ at p ≈ 0.29 (p. 4). Scoring a candidate by a triangle that
contains it costs 5–12 points. Composition is the capability. Routing is
a refinement, and the spectral baseline with one reweighting pass is
ahead on every row. The paper says so: "Holonomy attention is not a better
synchronizer" (p. 3).

**What could have failed.** Routing could have added nothing over uniform
averaging at high corruption, or avoiding-loop scoring could have done no
better than literal scoring. Neither happened.

**The AUC.** Clean triangles score tr H/d = 1 exactly, and one corrupted
edge always gives H ≠ I. So the only corrupted triangles that tie with
clean ones are those whose corruptions cancel. The paper gives 1.4% at
p = 0.3, and the AUC "sits at its ceiling 0.993" (p. 4). Recomputed here
by enumerating S4: 0.01422, ceiling 0.99289. The commuting-score cap,
½(1 + (|G| − |[G, G]|)/(|G| − 1)), recomputed for S4, is 0.7609, matching
the paper's 0.76 (measured 0.759). The two-cluster AUC of 0.98 is of the
same kind: within-cluster relations are built consistent and cross-cluster
ones random.

## What this does not say

- **That holonomy attention works on learned or linguistic relations.**
  The group and its representation are supplied. The paper names
  operators "generated from context" as the next step (p. 4).
- **That the AUC measures a detector's power.** It measures how often
  corruptions cancel on data whose clean part is exactly flat.
- **That loop-consistency is evidence of correctness in general.** Here
  the truth is flat by construction, so a consistent reconstruction is a
  correct one. [CASE-179](../cases.d/CASE-179.md)'s arm that revises correspondences "by consistency
  alone" is the setting where the two come apart.
