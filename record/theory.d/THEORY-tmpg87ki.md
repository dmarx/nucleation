---
status: Active
title: 'In GPT-J, for 652 CounterFact facts the model knows, the per-fact causal-tracing effect at an MLP layer adds at most 3.2 points of explained variance in the success of editing that fact at that layer, beyond what the choice of layer alone explains, across ROME, MEMIT and constrained fine-tuning and five editing objectives; ROME rewrites the fact at over 96% at every layer but the last, including layers where tracing does not place it, and the only reliable link appears when the edit is made on the noised input that tracing uses'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmpg0dnu, the reading of Hase et al. (2023)
    in full. One study, but the title claims only what it measured, and
    nothing in the record contradicts the measurements (ADR-047 v3):
    THEORY-998's "best in middle layers" is an average over facts, which
    this result leaves standing. The record checked the paper's averages
    against its tables and found one table cell in conflict with the
    figure (NOTE-tmpg0dnu), which does not touch the title. The
    authors' account of why is the Proposed THEORY-tmpiz2n7.
tags:
- representation-learning
- causality
date: '2026-10-27'
source:
- LIT-tmpg22tp
summary: >-
  Hase et al. (2023), LIT-tmpg22tp, read in NOTE-tmpg0dnu: §§4–5,
  Tables 1–8 and Appendices A–C. For ROME at GPT-J's layer 6, ρ = −0.13
  between rewrite score and tracing effect; R² 0.947 from the layer, 0.948
  with tracing added. Over twenty method–objective pairs the largest gain
  is 0.032 (fine-tuning on five layers, Fact Forcing). It does not say that
  facts are stored nowhere in particular, nor that the layer does not
  matter: the layer explains most of the variance, and ROME is best on
  average at the layer tracing favours on average.
---
<!-- inactive-ok-file: THEORY-tmpiz2n7 THEORY-1011 — Proposed; the account of why and the storage hypothesis this result bears on, cited as open -->

# THEORY-tmpg87ki: In GPT-J, for 652 CounterFact facts the model knows, the per-fact causal-tracing effect at an MLP layer adds at most 3.2 points of explained variance in the success of editing that fact at that layer, beyond what the choice of layer alone explains, across ROME, MEMIT and constrained fine-tuning and five editing objectives; ROME rewrites the fact at over 96% at every layer but the last, including layers where tracing does not place it, and the only reliable link appears when the edit is made on the noised input that tracing uses

## Source

Hase, Bansal, Kim and Ghandeharioun (2023), NeurIPS 2023,
arXiv:2301.04213, LIT-tmpg22tp, read in full in NOTE-tmpg0dnu.

## What was actually shown

**Setting.** GPT-J (6B, 28 layers), 652 CounterFact facts it completes
correctly. Causal tracing as in Meng et al. (LIT-1536): Gaussian noise on
the subject's embeddings, MLP outputs restored over a window of five
layers, and the effect at a layer taken as the maximum over tokens, as a
fraction of the probability lost. Edits at layers {1, 5, 6, 9, 13, 17, 21,
25 (or 24), 28} by ROME (one layer), MEMIT (five), and ℓ∞-constrained
fine-tuning (one or five).

**Measure.** For each method and objective, the R² of a regression of
edit success on the edit layer (categorical), and the gain when the
per-fact tracing effect at that layer is added, with an F-test.

**Results.** Error Injection with ROME: ρ = −0.13 at layer 6; R² 0.947
from the layer, 0.016 from tracing alone, 0.948 from both. Across the
other objectives (Tracing Reversal, Fact Erasure, Fact Amplification,
Fact Forcing) and methods, the gain is at most 0.032, and is significant
and largest for fine-tuning under Fact Forcing (0.027 and 0.032), the one
objective that edits on the noised input. ROME's mean rewrite score is
99% at layer 6 and above 96% at every layer but 28. The same holds for
paraphrase, neighbourhood and overall scores, for a tracing window of 10,
for the tracing effect at the last subject token, for GPT-2 XL, for ZSRE,
for representation zeroing, and for the 74 facts whose tracing effects
are concentrated in a few layers.

**What could have come out otherwise.** Facts traced to a layer could
have been edited best at that layer, and facts traced elsewhere edited
worse at the default layer. Editing five layers could have aligned with a
five-layer tracing window. The concentrated-effect subset could have shown
the link that the full set hides. None did.

## What this does not say

- **Not that the layer is irrelevant.** The layer explains most of the
  variance, and ROME is best on average at layer 6, near where tracing
  peaks on average. The result is about the per-fact deviation from that
  average.
- **Not that facts are stored nowhere, or everywhere.** "Stored" here
  means where causal tracing peaks. The finding is that this does not
  locate the edit. It does not say what would.
- **Not that causal tracing is uninformative.** It is a statement about
  tracing as a guide to editing. Meng et al.'s traces (THEORY-998) stand
  as measurements.
- **Not beyond the setting.** Two models up to 6B parameters, short
  English factual prompts, layer-level MLP edits, and denoising or zeroing
  as the localization.
- **Not why.** The authors' account, that tracing and editing answer
  different questions and that an edit at one layer can override what
  others have accumulated, is THEORY-tmpiz2n7, Proposed.

## Connections

- **THEORY-1011.** Its promote_when names this test and its refutation
  condition ("edits of equal quality are available at layers that tracing
  does not implicate"). This result meets that condition for the rewrite
  score. See NOTE-tmpg0dnu.
- **THEORY-282.** Makelov et al.'s equivalence of fact patches and
  rank-one edits gives a reason an edit can work at a layer whatever that
  layer carries. That is a mechanism for this result, from another
  direction.
- **THEORY-998** is the average-over-facts result this one is consistent
  with.
