---
status: Proposed
title: 'Jiang and colleagues find that a brief first phase on procedurally generated abstract data, well under one per cent of the later tokens, lets a language model reach its baseline''s loss with substantially fewer natural-language or code tokens, and that shuffling the procedural sequences or the transferred weights removes the saving'
version: 1
source:
- LIT-tmpb6e1c
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
promote_when: >-
  An independent replication at a stated scale, with several seeds, finds
  that a procedural first phase of under one per cent of the semantic
  tokens lets a model reach a no-first-phase baseline's semantic loss with
  substantially fewer semantic tokens, the shorter runs trained with their
  own schedules, and that shuffling the procedural sequences or the
  transferred weights removes the saving.
corroborates:
- CLAIM-756
summary: >-
  From the reading of [LIT-tmpb6e1c](../literature.d/LIT-tmpb6e1c.md) in [NOTE-tmpcdop1](../notes.d/NOTE-tmpcdop1.md). A second instance,
  beside [THEORY-tmpk9cmk](THEORY-tmpk9cmk.md), of an earlier acquisition lowering a later one's
  cost; disputed at matched compute by [THEORY-tmpsewbi](THEORY-tmpsewbi.md). Proposed until its
  promote_when is met.
---

# THEORY-tmpmy98s: Jiang and colleagues find that a brief first phase on procedurally generated abstract data, well under one per cent of the later tokens, lets a language model reach its baseline's loss with substantially fewer natural-language or code tokens, and that shuffling the procedural sequences or the transferred weights removes the saving

## The account

With all weights transferred and embeddings re-initialized, 2.1M procedural tokens save about 45 and 33 per cent of semantic tokens on C4 and CodeParrot at 124M, 10.4M save 14 per cent on DeepMind-Math, and 82M save 34 per cent of C4 at 1.3B. Shuffled procedural data or shuffled transferred weights give no saving.

## Evidence

No seeds on semantic runs; no natural-language warm-up control; procedures selected by downstream grids.

## Note of 2026-11-19: the task-composition readings, read
<!-- inactive-ok-file: THEORY-tmp51mqd THEORY-tmpw5877 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Complementary interventions: Maennel and colleagues (THEORY-tmpw5877) keep
a saving by resampling first-layer filters from their learned covariance,
where this account removes it by shuffling; Zhang, Lepori and Pavlick
(THEORY-tmp51mqd) lose most of it with a same-size random subset of the
trained weights. Together they place the saving in specific weight
statistics or components.
