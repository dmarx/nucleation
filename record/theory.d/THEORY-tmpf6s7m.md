---
status: Proposed
title: 'Papadimitriou and Jurafsky find that LSTM language models whose recurrent weights are trained on Java code, on matched-pair parenthesis languages or on MIDI music, then frozen while only the embeddings are finetuned on Spanish, reach far lower Spanish perplexity than ones trained on random text, and that flat crossing pairs transfer as well as nested ones'
version: 1
source:
- LIT-tmporqpp
tags:
- learning-theory
- representation-learning
- linguistics
date: '2026-11-19'
promote_when: >-
  An independent replication with the frozen-recurrent-weights protocol
  over several seeds finds that code-, music- and paired-token-pretrained
  LSTMs reach markedly lower perplexity on a natural target language than
  random-text-pretrained ones, and that flat crossing-pair and nested-pair
  corpora give statistically indistinguishable transfer.
summary: >-
  From the reading of LIT-tmporqpp in NOTE-tmpwj0be. The predecessor of
  THEORY-tmpk9cmk: it shows reuse exists, under a frozen interface, and
  measures no cost of later learning. Proposed until its promote_when is
  met.
---

# THEORY-tmpf6s7m: Papadimitriou and Jurafsky find that LSTM language models whose recurrent weights are trained on Java code, on matched-pair parenthesis languages or on MIDI music, then frozen while only the embeddings are finetuned on Spanish, reach far lower Spanish perplexity than ones trained on random text, and that flat crossing pairs transfer as well as nested ones

## The account

Train a three-layer LSTM language model on a first corpus, freeze its
recurrent weights, finetune only the embeddings on Spanish with disjoint
vocabularies. Spanish perplexity after code is about 139, after nested or
flat parenthesis languages about 170, after music about 256, after random
text 493 to 514; after any natural language, lower still. The authors read
this as a head-dependent pairing bias, not necessarily hierarchical, doing
most of the work.

## Evidence

Five seeds per condition; one target language; corpora unmatched in size
for music and code; no full-training arm or learning curve.
