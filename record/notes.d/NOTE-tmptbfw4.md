---
status: Read
paper: LIT-2297
title: 'Jansen, Clark, Downey and Weld — Generating Literature-Driven Scientific Theories at Scale'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2601.16282. Read: main
    text in full; appendix skimmed. A delegated reader drafted the reading;
    quotations were rechecked by script against the downloaded copy, and any
    that did not match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  The paper defines literature-based theory synthesis: from a theory query
  and a paper corpus, produce theories made of ⟨law, scope, evidence⟩
  tuples. THEORIZER retrieves up to 100 papers, builds a query-specific
  extraction schema, extracts evidence from each paper, generates theories,
  and refines each with self-reflection. Four conditions cross
  literature-supported against parametric-only generation with
  accuracy-focused against novelty-focused prompts.
---
<!-- inactive-ok-file: CASE-tmpiocs1 CASE-tmppm4do CLAIM-tmppk8g6 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmptbfw4: Jansen, Clark, Downey and Weld — Generating Literature-Driven Scientific Theories at Scale

## Contribution

A task formulation, five desiderata (specificity, empirical support, predictive accuracy, novelty, plausibility), a working system, and the backtesting evaluation with a "strong test requirement" for what counts as a test of a prediction.

## Key results

- Literature support helps prediction (Abstract): theories "are significantly better at both matching existing evidence and at predicting future results from 4.6k subsequently-written papers".
- Accuracy-focused laws (§5.2): "laws exhibit similarly high precision across both parametric and literature-supported generation (0.88 and 0.90), with recall ranging from 0.45 to 0.51".
- Novelty-focused laws (§5.2): "61% of predictions from literature-supported theories are supported by recent evidence, compared to only 34% for parametric theories". Recall: "only 16% of literaturesupported laws and 4% of parametric laws" have any relevant recent papers.
- The model's calibration fails on novel laws (§5.2). In the novelty-focused condition "the generating model substantially overestimates predictive accuracy (67–76%) relative to observed support in the literature (34–61%)".
- Novelty against accuracy (Discussion): "novelty and predictive accuracy exhibit a clear tradeoff", and "novelty in this setting reflects absence from the retrieved papers, not empirical validity."
- Parametric saturation (Fig. 3): theories generated with parametric knowledge alone "quickly saturate to generating only duplicates".
- Guard against loose matching (§5.2): each prediction carries "(iii) a strong test requirement, describing the concrete experimental comparison a paper must report to be considered a valid test".

## Assumptions

- LLM judges (Claude Sonnet 4.5, GPT-5-mini) reliably decide support, contradiction or no evidence. There is no human validation of the backtest judgements in the main text.
- Absence of a test in the following six months is read as missing recall, not as a false law.
- Open-access AI/NLP literature is representative. The authors limit scope to "fields whose scholarly literature is primarily open access".
- There is an internal inconsistency to note. §5 says the generator has "a reported knowledge cutoff of June 2024 (GPT 4.1)", but §5.2 says "theories are generated using knowledge available up to June 2025" and evaluated on July–December 2025.

## Concepts

Theory as a set of laws with scope and evidence; backtesting; predictive precision and recall; qualified novelty (seven novelty types); parametric saturation; accuracy-focused vs novelty-focused generation.

## Bearing on the record

The exchange (A14) reports about 13,700 source papers, about 2,900 theories and about 4,600 later papers, and says "literature grounding improved both historical consistency and prediction of later research results". **Accurate**, with one qualification. In the accuracy-focused condition the precision gain is small (0.88 vs 0.90). The large gains are in the novelty-focused condition and in recall. Its line 706 framing, "Assess theories with predictions against withheld or subsequently published results", is a fair statement of the paper's evaluation design.

The LIT names no codes, and no branch entry cites LIT-2297. The content curation left A14's survey to the works' readings.
- **QUESTION-tmpxq2sb / CASE-tmpiocs1**: no direct bearing.
- **CLAIM-tmppk8g6 / CASE-tmppm4do**: no direct bearing.
- The paper's THEORY format (law, scope, evidence) parallels this record's THEORY schema (claim, `source:`, `promote_when:`). Its backtesting is an instance of what the exchange's A17 proposed for step 12, a prospective result recorded before the evidence. The content curation lists that among "Proposals about this record's procedures", not filed. This paper is the empirical precedent for that proposal. It shows a prediction recorded before the evidence can be scored at scale, and that the scoring depends on a "strong test requirement".
- **CLAIM-266**: the self-assessed belief result (calibration fails on novel laws) is a case where the generator's own estimate cannot certify its output.

## Limitations

The appendix theories were not read, and the reader did not inspect the judge prompts. The cutoff-date inconsistency above is unresolved.
