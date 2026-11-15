---
number: 1829
status: Proposed
formerly:
- THEORY-tmpdkd7v
promote_when: >-
  An independent replication, in at least two LLMs over at least 2,000
  sequential edits, that shows three things. (a) The change in the edited
  layers' outputs on held-out preserved keys, ‖ΔPK0‖, is small relative
  to MEMIT's corresponding change. (b) Efficacy, generalization and
  general-ability scores are maintained where MEMIT and ROME degrade.
  (c) An ablation shows that the projection, not the regularizer or the
  previous-edits term alone, carries the preservation. It does not need
  the authors' account of distribution shift, which the title does not
  assert.
title: 'On Fang and colleagues, projecting a locate-then-edit weight update onto the null space of the preserved knowledge keys, taken in practice as the eigenvectors of their uncentred covariance with eigenvalues at most 10⁻², and dropping the preservation term from the objective, keeps the edited layer''s outputs on preserved keys nearly unchanged and sustains edit success and general ability over thousands of sequential edits where MEMIT and ROME degrade'
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2555
summary: >-
  Fang, Jiang, Wang, Ma, Shi, Wang, He & Chua (2025), [LIT-2555](../literature.d/LIT-2555.md), read
  in [NOTE-1908](../notes.d/NOTE-1908.md). Exact preservation holds for an exact null space; the
  method uses a thresholded one, so preservation is approximate and its
  size unmeasured. The sequential-editing results are strong on LLaMA3 and
  hold on GPT-J and GPT2-XL. The sharp edges: no measurement of leakage,
  no reported null-space dimension, specificity well below pre-edit, and
  a misstated "best baseline" comparison.
---

# THEORY-1829: On Fang and colleagues, projecting a locate-then-edit weight update onto the null space of the preserved knowledge keys, taken in practice as the eigenvectors of their uncentred covariance with eigenvalues at most 10⁻², and dropping the preservation term from the objective, keeps the edited layer's outputs on preserved keys nearly unchanged and sustains edit success and general ability over thousands of sequential edits where MEMIT and ROME degrade

## Source

Fang et al. (2025), [LIT-2555](../literature.d/LIT-2555.md), read in [NOTE-1908](../notes.d/NOTE-1908.md) from arXiv v4.

## What was actually shown

- **The exact-null-space guarantee**, by construction (Eq. 10, App. B).
- **The thresholded projector in use** (footnote 1).
- **Sequential-editing results** on LLaMA3-8B, GPT-J and GPT2-XL
  (Table 1), with general ability kept to 3,000 edits.
- **Plug-in gains** for MEMIT, PRUNE and RECT.

The results could have come out otherwise: projection might have cost
efficacy, as constraining an update often does.

## What this does not say

- **That preserved outputs are unchanged.** With a thresholded null space
  they move. By how much is not measured.
- **Why dropping the preservation term prevents degradation.** The
  authors' distribution-shift account is supported by visualizations,
  not proved.
- **Anything about editing across heterogeneous domains,** where MuEdit
  reports this method collapsing.
- **Anything about where facts are stored.**
