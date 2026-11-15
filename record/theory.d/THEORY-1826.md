---
number: 1826
status: Proposed
formerly:
- THEORY-tmp1nwro
promote_when: >-
  An intervention showing that the edited matrix's condition number, not
  the edits' size or count alone, drives the loss of general abilities.
  For example: across edit sequences whose accumulated updates have equal
  Frobenius norm and equal count, general-ability loss tracks the
  condition number, and changing the condition number by itself moves
  general ability correspondingly. Plus an independent replication, with
  the restraint's strength chosen on held-out edits, that capping the
  accumulated update's singular values near the original matrix's
  largest keeps general ability and edit success above unrestrained
  sequential editing.
title: 'On Ma and colleagues, in sequential single-fact editing of a transformer MLP output matrix, the growth of the edited matrix''s condition number with the number of edits, driven by the top singular values of the accumulated edit update, is what degrades the model''s general abilities, and capping the accumulated update''s singular values near the original matrix''s largest preserves those abilities while keeping the edits'
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2552
summary: >-
  Ma, Wang, Xu, Ling & Gu (2025), [LIT-2552](../literature.d/LIT-2552.md), read in [NOTE-1910](../notes.d/NOTE-1910.md).
  The causal reading rests on a perturbation upper bound for a proxy
  quantity, on the rise of the condition number with edits, and on a
  correlation between that rise and the decline (C.5). The remedy's
  benefit is shown on three editors and three LLMs. The sharp edges:
  there is no intervention on the condition number at fixed update size;
  the bound's side conditions are not checked; and PRUNE does not
  provably bound the condition number.
---

# THEORY-1826: On Ma and colleagues, in sequential single-fact editing of a transformer MLP output matrix, the growth of the edited matrix's condition number with the number of edits, driven by the top singular values of the accumulated edit update, is what degrades the model's general abilities, and capping the accumulated update's singular values near the original matrix's largest preserves those abilities while keeping the edits

## Source

Ma et al. (2025), [LIT-2552](../literature.d/LIT-2552.md), read in full in [NOTE-1910](../notes.d/NOTE-1910.md).

## What was actually shown

- **The bound.** Least-squares perturbation bounds on a key's adjustment
  scale with the condition number (Thms 3.1–3.2).
- **The rise.** On LLaMA-2, the condition number of the edited matrix
  rises steeply with edits, through its largest singular value.
- **The correlation.** That rise is accompanied by a decline in general
  ability (C.5).
- **The remedy.** Logarithmic shrinkage of the accumulated update's
  large singular values preserves downstream and editing scores across
  MEND, ROME and MEMIT on GPT-2 XL, LLaMA-2 and LLaMA-3.

The remedy could have failed, since shrinking the update's top
directions might have undone the edits.

## What this does not say

- **That the condition number causes the decline.** No intervention
  isolates it.
- **That PRUNE bounds the condition number.** It caps the update's top
  singular values and leaves σmin alone.
- **Anything about batch editing**, or about editing across domains.
