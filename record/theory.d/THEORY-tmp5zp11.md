---
status: Proposed
title: 'Yu, Kim and Kim (2026) report that when LLM-written, search-optimized documents are added to fixed per-query pools of real web documents, retrievers place them in the top results more often than their share of the pool (over 80% exposure at 67% of the pool for both BM25 and an LLM re-ranker) while answer accuracy stays level, so that retrieval loses its human-written sources without any drop in measured accuracy; adversarially falsified documents are largely filtered by an LLM re-ranker but reach about a fifth of BM25''s top results.'
version: 1
source:
- LIT-tmp9a7jh
tags:
- information-retrieval
date: '2026-11-12'
promote_when: >-
  an independent study, or a replication with repeated runs on another
  corpus, finds that retrievers expose LLM-generated documents at a rate
  exceeding their share of the candidate pool.
summary: >-
  Yu, Kim and Kim (2026), read in NOTE-tmpaeun2 (Read). The authors name
  "Retrieval Collapse", a two-stage failure in which (1) AI-generated
  content comes to dominate search results, eroding source diversity, and
  (2) low-quality or adversarial synthetic content enters the retrieval
  pipeline. On 1,000 MS MARCO queries, each with ten Google-retrieved web
  documents (Original Pool), they add GPT-5-nano documents one per round for
  20 rounds (pool contamination 0% → 66.7%), in two scenarios: an "SEO" pool
  (LLM rewrites of original documents with high-IDF keywords) and an "Abuse"
  pool (clickbait drafts with named entities and numbers falsified).
---

# THEORY-tmp5zp11: Yu, Kim and Kim (2026) report that when LLM-written, search-optimized documents are added to fixed per-query pools of real web documents, retrievers place them in the top results more often than their share of the pool (over 80% exposure at 67% of the pool for both BM25 and an LLM re-ranker) while answer accuracy stays level, so that retrieval loses its human-written sources without any drop in measured accuracy; adversarially falsified documents are largely filtered by an LLM re-ranker but reach about a fifth of BM25's top results.

## The account

Yu, Kim and Kim (2026) report that when LLM-written, search-optimized documents are added to fixed per-query pools of real web documents, retrievers place them in the top results more often than their share of the pool (over 80% exposure at 67% of the pool for both BM25 and an LLM re-ranker) while answer accuracy stays level, so that retrieval loses its human-written sources without any drop in measured accuracy; adversarially falsified documents are largely filtered by an LLM re-ranker but reach about a fifth of BM25's top results.

## Evidence

The reading in NOTE-tmpaeun2; its key results are quoted there with locations.
