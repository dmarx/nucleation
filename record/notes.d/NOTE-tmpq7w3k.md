---
status: Read
paper: LIT-tmpqhq20
title: 'Xu et al. — A-MEM: Agentic Memory for LLM Agents'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2502.12110. **Read.** Main
    text read in full (abstract, §§1–5, conclusions, limitations); appendices
    (baseline descriptions, extra metrics and models, prompts, k settings,
    NeurIPS checklist) skimmed for the points the main text cites. A delegated
    reader drafted the reading; quotations were rechecked by script against
    the downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  A-MEM is a memory store for LLM agents built on Zettelkasten ideas. Each
  new interaction becomes a "note" with the raw content, a timestamp,
  LLM-generated keywords, tags and a contextual description, and an
  embedding. On insertion the system retrieves the top-k most similar notes
  and asks an LLM which to link to (link generation), then asks an LLM
  whether to rewrite those neighbours' context, keywords and tags in light
  of the new note (memory evolution); the evolved note **replaces** the old
  one.
---
<!-- inactive-ok-file: CLAIM-tmp8qsef — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: CLAIM-182 CLAIM-184 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpq7w3k: Xu et al. — A-MEM: Agentic Memory for LLM Agents

## Contribution

An agent-memory design in which the LLM, not a fixed schema, decides the links between memories and rewrites old memories' descriptions as new ones arrive; the authors frame this as agency "at a more fundamental level" than agentic RAG, in storage and evolution rather than retrieval.

## Key results

- §1: graph-database memories are criticised because "their reliance on predefined schemas and relationships fundamentally limits their adaptability".
- Abstract: memory evolution — "they can trigger updates to the contextual representations and attributes of existing historical memories".
- §3.3: the update is destructive: the evolved memory "then replaces the original memory" in the store; no version or history of the earlier description is kept (none is described anywhere in the paper).
- §4 Cost: "achieving an 85-93% reduction in token usage" against LoCoMo and MemGPT.
- §4 Ablation: "the link generation module serves as a critical foundation for memory organization", with memory evolution adding a further gain.
- Limitations: "the quality of these organizations may still be influenced by the inherent capabilities of the underlying language models".

## Assumptions

- Revising an old note's description in light of a new one is improvement; nothing checks whether an evolution was wrong, and there is no way to undo it.
- Benchmark QA (LoCoMo, DialSim) answer overlap (F1, BLEU-1) measures memory quality; no task measures revision, contradiction handling or correctness of evolved notes.
- Links are similarity-seeded (top-k embedding neighbours) and LLM-judged; link types are untyped.

## Concepts

Agentic memory; Zettelkasten note (content, timestamp, keywords, tags, context, embedding, links); link generation; memory evolution; "box" of linked notes; top-k retrieval; agentic RAG vs agentic storage.

## Bearing on the record

A (A20 §1 and §3) cites it for Zettelkasten-inspired connected memories that update existing notes as new information arrives. **Accurate.** What A's description leaves out, and what matters for luria: the update overwrites (the earlier state of a note is lost), links are untyped similarity links, and nothing records why a note changed or who changed it. A-MEM is a schema-free, self-rewriting store; luria is a typed, versioned record that retires by status. They sit at opposite ends on revision.

- **[QUESTION-108](../questions.d/QUESTION-108.md)**. **Qualifies.** A-MEM's ablation is a rare published separation inside one system: adding LLM-made links (without evolution) improves multi-hop QA over the same notes without links, which bears on the "easier to reach" mechanism (links bring related notes into the retrieved context) rather than "retains more" (the same notes are stored in both arms). It does not test the "operations" mechanism, and its evolution step trades retention for currency: it may lose information when it rewrites. So it is evidence that structure helps by reach on QA tasks, and no evidence on revision tasks, which are what [QUESTION-108](../questions.d/QUESTION-108.md) is about.
- **[CLAIM-184](../claims.d/CLAIM-184.md)** (anchors entrench) / **[CLAIM-182](../claims.d/CLAIM-182.md)** (addressability): A-MEM is a contrast case. Its notes are addressable but rewritten in place, so nothing persists to entrench, and nothing persists to audit either. It neither supports nor tests these claims.
- **[CLAIM-tmp8qsef](../claims.d/CLAIM-tmp8qsef.md)** (the record computes no withdrawals; it reports dependants): A-MEM computes *rewrites* of neighbours automatically by LLM, which is the kind of automatic propagation [CLAIM-tmp8qsef](../claims.d/CLAIM-tmp8qsef.md) says the record declines to do; A-MEM reports no evaluation of whether those rewrites are correct. Leaves the claim open; a possible foil for a study.

## Limitations

Numeric tables extracted poorly from PDF; per-category scores not checked. Appendix experiments with other base models not read in detail. Code not run.
