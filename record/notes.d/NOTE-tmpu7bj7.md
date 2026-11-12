---
status: Read
paper: LIT-tmppcaeo
title: 'Edge et al. — From Local to Global: A GraphRAG Approach to Query-Focused Summarization'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2404.16130. **Read.** Main
    text read in full (abstract, §§1–7); appendices A–G (prompts,
    community-level examples, statistical tables, evaluation prompts) skipped
    except where the main text points to them for numbers. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  GraphRAG answers "global" questions about a whole corpus ("What are the
  main themes in the dataset?"), which ordinary vector RAG cannot, because
  retrieving the top-k similar chunks samples the corpus instead of
  summarizing it. At index time an LLM extracts entities, relationships and
  "claims" from text chunks, merges them into a knowledge graph (exact
  string matching for entity names), partitions the graph hierarchically
  with Leiden community detection, and pre-generates a report-like summary
  for every community at every level. At query time each community summary
  yields a partial answer with a 0–100 helpfulness score (map), and the best
  partial answers are summarized into a global answer (reduce).
---
<!-- inactive-ok-file: CLAIM-tmp8qsef — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpu7bj7: Edge et al. — From Local to Global: A GraphRAG Approach to Query-Focused Summarization

## Contribution

A pipeline that turns a corpus into a hierarchy of LLM-written community summaries over an LLM-extracted entity graph, and an evaluation method (persona-generated global questions, head-to-head LLM judging on comprehensiveness, diversity, empowerment and a "directness" control).

## Key results

- Abstract: vector RAG "RAG fails on global questions directed at an entire text corpus", since this is query-focused summarization, not retrieval.
- §3.1.3: extraction is itself lossy: "is a form of abstractive summarization"; entities are merged by "our analysis uses exact string matching for entity matching".
- §5.1: "global approaches significantly outperformed conventional vector RAG (SS) in both comprehensiveness and diversity criteria" (win rates 72–83% Podcast, 72–80% News for comprehensiveness).
- §5.1: "Empowerment comparisons showed mixed results"; the LLM judge's reasons pointed to specific examples, quotes and citations, which the graph index tends to lose.
- §5.1 / Table 2: root-level summaries (C0) cost far less than map-reduce over source text: "it required over 97% fewer tokens".
- §5.2 (claim-based measures): "there were no statistically significant differences observed among the global search conditions or between global search and TS".
- §6.2 Broader impacts: vector RAG risks "samples of retrieved facts falsely presented as global summaries".

## Assumptions

- An LLM judge's head-to-head preference, without ground truth, measures answer quality; the claim-count re-measure only partly validates it (78% agreement on comprehensiveness where the judge was not tied).
- The questions are LLM-generated from a corpus description; no human questions or users.
- Summaries can stand in for the source: the graph is built once and not revised; there is no mechanism for correction, contradiction or provenance beyond the community report.

## Concepts

Global sensemaking questions; query-focused summarization (QFS); vector RAG; LLM-derived knowledge-graph index with "covariates (e.g., claims)"; hierarchical Leiden communities (C0–C3); community summaries; map-reduce answering with helpfulness scores; adaptive benchmarking via personas; comprehensiveness, diversity, empowerment, directness.

## Bearing on the record

A (A20 §3) cites it for knowledge graphs and summaries generated to answer questions about large corpora. **Accurate.** Two refinements matter for the record: (1) the graph and its "claims" are LLM extractions and summaries, built once for retrieval, with no standing, provenance chain, revision or governance; it is a retrieval index, not a maintained record; (2) its own claim-based result does not separate the graph from plain hierarchical summarization of the source (no significant difference vs TS), so it is weak evidence that graph structure as such, rather than summarization, does the work.

- **QUESTION-108** (retains more / easier to reach / operations easier). **Qualifies and sharpens.** GraphRAG's design is a direct instance of the "easier to reach" mechanism: the benefit over vector RAG comes from pre-computing summaries that cover the whole corpus, and its own Experiment 2 finds no significant gain of the graph conditions over graph-free map-reduce summarization (TS), only a cost gain. That is a published case where structure's measured value is accessibility and cost, not retention or operations, which is the separation QUESTION-108 asks for. It also shows a known confound: GraphRAG retains *less* (extraction is "abstractive summarization"; empowerment suffers when specifics are lost), so a structured index can win on reach while losing on retention. It leaves the "operations" mechanism untouched: no revision task is tested.
- **CLAIM-tmp8qsef** (via QUESTION-108's note): leaves open; GraphRAG has no dependency or withdrawal operation at all.

## Limitations

Appendix results (per-level statistics, prompts) not read. Evaluation entirely LLM-judged on two corpora; no human sensemaking study; no fabrication-rate measurement (the authors say so in §6.1). The graph is static: nothing about updating the index as the corpus changes.
