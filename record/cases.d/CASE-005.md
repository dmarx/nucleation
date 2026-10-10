---
number: 5
status: Active
formerly:
- CASE-tmp7b5rt
title: 'The language-model experiments: frame commutator, trajectory-preserving selection, ICL against TTT'
version: 1
standing: stipulated
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
variant_of:
- CASE-029
summary: >-
  A45 §5, kept in outlines v3 and v4: order effects of opposed versus
  independent framings in an LLM, a comparison of three ways of choosing
  a translation against human judgement, and prompt-only versus test-
  time-trained adaptation. Proposed, not run.
supports:
- CLAIM-tmpc3xwx
---
<!-- inactive-ok-file: CLAIM-074 CLAIM-117 CLAIM-118 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-083 — Superseded; replaced, and cited as the history this entry answers or replaces -->

# CASE-005: The language-model experiments: frame commutator, trajectory-preserving selection, ICL against TTT

## The case

- **Experiment 1, a pragmatic frame commutator.** Solidarity and condemnation
  framings in both orders,
  Δ_(A,B)(u) = D_JS(Q(· | c, A, B, u), Q(· | c, B, A, u)), "not literally an
  operator commutator", with token-matched, paraphrase and order-insensitive
  controls. The sharp question: "are solidarity and condemnation more
  order-sensitive than two informationally independent framing cues?" Prior
  art on prompt order (Lu et al. 2022, Xiang et al. 2024, Cobbina and Zhou
  2025) narrows the contribution to "whether order effects respect
  theoretically specified pragmatic relationships".
- **Experiment 2, translation preserves framing dynamics.** Choose translations
  by maximum semantic similarity, by maximum static pragmatic similarity and by
  maximum trajectory similarity, and ask which predicts human judgement. "If
  trajectory-level comparison adds nothing beyond simpler baselines, the
  proposed dynamical criterion loses much of its motivation."
- **Experiment 3, ICL against TTT.** Prompt-only, test-time-trained and control
  interpreters, with a transfer gain, testing whether "**Pragmatic frames may be
  learned as transferable interpretive dispositions, rather than merely imposed
  as transient contextual instructions.**" A48 advised deferring it: TTT "could
  easily expand this into two research programs".

## What it can show

Experiment 2 is the direct test of [CLAIM-117](../claims.d/CLAIM-117.md) and of [CLAIM-083](../claims.d/CLAIM-083.md)'s stake. It is the
ancestor of the manuscript's Case I success criterion; the three-way selection
design is gone by A52. Experiment 3 tests [CLAIM-074](../claims.d/CLAIM-074.md). Its prompt-only arm is the
manuscript's §5 distinction ([CLAIM-118](../claims.d/CLAIM-118.md)), but the manuscript has no TTT
experiment. Every arm is open to [CLAIM-085](../claims.d/CLAIM-085.md). None has been run.
