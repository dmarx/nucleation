---
status: Skimmed
paper: LIT-tmpq22ic
title: 'Garg & Fetzer, causal claims in economics'
version: 1
date: '2026-09-25'
summary: >-
  Turning 44,852 NBER/CEPR economics working papers (1980–2023) into LLM-extracted "claim graphs" (JEL-concept nodes, edges labelled by evidentiary basis) shows the share of causally identified claims rising from 7.7% (1990) to 31.7% (2020). Causal narrative structure and causal novelty predict top-five publication and citations, while non-causal complexity and novelty do not.
---

<!-- inactive-ok-file: LIT-tmpq22ic — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpy611h: Garg & Fetzer, causal claims in economics

## Contribution

As economics grows, a bottleneck is representing what papers claim in a form that can be compared and aggregated. The authors introduce evidence-annotated claim graphs: each paper becomes a directed network of standardized economic concepts, with edges labelled by the kind of evidence, including whether a causal-inference design supports them. A multi-stage AI workflow builds these graphs for 44,852 papers from 1980–2023. Causal edges rise from 7.7% in 1990 to 31.7% in 2020. Causal structure and causal novelty are positively associated with top-five publication and long-run citations, while their non-causal counterparts are weakly or negatively related.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 Introduction: the authors say they extract what papers claim and do not judge whether claims are true (footnote 1, citing Deaton, Heckman, Cartwright). Causal designs are DiD, IV, RDD, RCTs, event studies and synthetic control. They position the work against the credibility-revolution, economics-of-science and scientometrics literatures.
- §2 Construction: a two-stage LLM pipeline (summaries or snippets, then edge extraction) with concepts mapped to JEL codes. Appendix A1 names GPT-4o-mini.
- §2.4 Validation: nine extraction passes per paper aggregated by "edge overlap" (EO ≥ 1 to 9), a snippet-only self-consistency check, and external benchmarks against Brodeur et al. (2024) (285 papers) and an expert "plausibly exogenous" dataset (491 papers).
- §3–4: trends in causal edges by field, then measures of narrative complexity, novelty (novel edges, path-based) and centrality.
- §7 Conclusion: publication selection appears aligned with causally documented structure, while citations track conceptual centrality. The authors present claim graphs as "claim-level infrastructure for cumulative science".

## Open questions

- A concrete example of using LLMs for large-scale structured extraction from scientific literature, the same pattern as this record's own reading notes and relation graphs. The validation design (repeated passes, edge-overlap thresholds) is the transferable part.
- Validation is mostly self-consistency, and external checks cover under 2% of papers. Check how precision and recall change across EO thresholds.
- The associations with publication and citations are correlational, so check the controls.
