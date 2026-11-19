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
  From the reading of LIT-tmpb6e1c in NOTE-tmpcdop1. A second instance,
  beside THEORY-tmpk9cmk, of an earlier acquisition lowering a later one's
  cost; disputed at matched compute by THEORY-tmpsewbi. Proposed until its
  promote_when is met.
---

# THEORY-tmpmy98s: Jiang and colleagues find that a brief first phase on procedurally generated abstract data, well under one per cent of the later tokens, lets a language model reach its baseline's loss with substantially fewer natural-language or code tokens, and that shuffling the procedural sequences or the transferred weights removes the saving

## The account

With all weights transferred and embeddings re-initialized, 2.1M procedural tokens save about 45 and 33 per cent of semantic tokens on C4 and CodeParrot at 124M, 10.4M save 14 per cent on DeepMind-Math, and 82M save 34 per cent of C4 at 1.3B. Shuffled procedural data or shuffled transferred weights give no saving.

## Evidence

No seeds on semantic runs; no natural-language warm-up control; procedures selected by downstream grids.
