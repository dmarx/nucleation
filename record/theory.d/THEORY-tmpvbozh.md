---
status: Proposed
title: 'Yıldız and colleagues find that GPT-2 models continually pretrained through 159 domains reach lower perplexity on each than when adapted to it alone, and that a similarity-ordered sequence favours the domain just trained while a random order of the same data ends better overall and forgets less'
version: 1
source:
- LIT-tmpg77d0
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with several random and similarity-based
  orders at fixed total tokens reproduces for GPT-2-scale decoders
  continual pretraining beating single-domain adaptation on each domain,
  and the similarity-ordered sequence giving lower just-trained perplexity
  but worse final perplexity and more forgetting than random order.
summary: >-
  From the reading of LIT-tmpg77d0 in NOTE-tmp4noj0. Domain order at fixed
  data, measured as perplexity and forgetting. Proposed until its
  promote_when is met.
---

# THEORY-tmpvbozh: Yıldız and colleagues find that GPT-2 models continually pretrained through 159 domains reach lower perplexity on each than when adapted to it alone, and that a similarity-ordered sequence favours the domain just trained while a random order of the same data ends better overall and forgets less

## The account

One epoch per domain over 159 M2D2 domains: each domain reaches lower perplexity than single-domain adaptation; similarity order helps the just-trained and recent domains of larger models; random order ends better and forgets less; smaller models gain and forget most.

## Evidence

One run per model and order, with two extra shuffles for one size; perplexity only.
