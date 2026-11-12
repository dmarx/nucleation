---
status: Read
paper: LIT-2308
title: 'Huang et al. — DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2609.33357. **Read** (main
    text). Read on 2026-11-12. A delegated reader drafted the reading;
    quotations were rechecked by script against the downloaded copy, and any
    that did not match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  DISCERN is a benchmark of 203 tasks on real public life-science datasets
  across eight tracks (GWAS, clinical variants, bulk and single-cell RNA,
  CRISPR screens, enhancers, chromatin, protein stability), at three
  independently scored levels: L1 data integrity (79 tasks, controlled
  defects and matched clean controls), L2 analysis verification (102 tasks,
  confounds and "tool traps" such as a narrow-peak setting on a broad
  histone mark), and L3 hypothesis generation and revision (22 dossiers)
  under three rounds of adversarial review by other LLMs, including
  counterfactual dossiers retained only when they conflict with the agent's
  elicited prior. Eight agents are evaluated. Aggregate scores hide
  level-specific weaknesses; recognising a problem is often not carried into
  the conclusion; caution is frequently misplaced (rejecting sound data);
  hypothesis production and novelty vary widely; computational expenditure
  ranks models more consistently across tracks than evidence judgement does.
---
<!-- inactive-ok-file: CASE-tmpvq90k — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmphk8w6: Huang et al. — DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?

## Contribution

A three-level benchmark that separates data vetting, analysis verification and hypothesis revision, with clean controls to catch over-rejection, prior-elicitation for counterfactual evidence, and separate scoring of whether an agent commits to a hypothesis and how good it is.

## Key results

- Perfect-score rates by level (Abstract; §4.1): “Agents earn perfect scores in only 60.8% of Level 1, 34.2% of Level 2, and 0.6% of Level 3 evaluations”.
- L3 is the commonest bottleneck (§4.1): “L3 is the lowest-scoring component in 46.9% of model–track combinations”.
- Recognition without uptake (§4.2): among 425 challenged L2 evaluations with full credit for issue recognition, 126 (29.6%) got only half credit for result calibration; “Recognizing a limitation is therefore not sufficient unless that limitation also shapes the resulting analysis and scientific claim”.
- Over-caution (§4.3): “only 19 of 64 L1 clean-control evaluations (29.7%) correctly accept the sound data”.
- Commitment against conflicting evidence (§4.3): Kimi submits a hypothesis in 92.3% of eligible counterfactual cases, “whereas Astra abstains in every such case”.
- Novelty (§1; §4.3): “among 94 submitted hypotheses, 46.8% receive no novelty credit under our rubric”.
- Concession is not good revision (§4.3): DeepSeek concedes a point in 41.7% of committed outcomes against 5.9% for Opus, but “concession frequency alone does not establish whether the resulting revision is better supported” (in the PDF this sentence runs beside the Figure 5 caption, so extracted text interleaves them).
- Effort vs judgement (§4.3): rankings by token use and code execution are consistent across tracks (Kendall's W = 0.89–0.95), rankings by evidence judgement and hypothesis behaviour much less so (W = 0.09–0.57).
- Limits (§6): the levels are independently instantiated, so the benchmark does “not establish autonomous end-to-end research”.

## Assumptions

- Rubric-based grading of L3 by an LLM judge, informed by reviewer critiques and rebuttals, with author validation, tracks scientific quality.
- Counterfactual dossiers that conflict with an elicited prior test revision rather than recall.
- Track composite is a geometric mean of L1–L3, so one level cannot compensate for another.

## Concepts

Data integrity vs analysis verification vs hypothesis generation; clean controls (specificity); tool traps; issue recognition vs result calibration; hypothesis commitment vs hypothesis quality; native vs injected counterfactuals; prior elicitation; working styles; adversarial review.

## Bearing on the record

The exchange (A14's table, decoded exchange line 636; also decoded lines 837 and 888, in later turns) says DISCERN tested "Evidence integrity, analysis verification and hypothesis revision under adversarial review" and that "Only 0.6% of the most demanding hypothesis-level evaluations received perfect scores, versus 60.8% at the basic data-integrity level", calling it "a stringent benchmark-specific result". Accurate. Its later gloss, "agents performed much better on simpler data-integrity checks than on difficult hypothesis-generation and revision tasks", is fair as to perfect-score rates, though mean L1 and L3 scores are closer than the perfect-score rates suggest (Astra 86.1 L1, 72.8 L3). The LIT says only that it was cited, which is correct.

The LIT names no code. Entries it bears on, found on recheck:

- **[CLAIM-403](../claims.d/CLAIM-403.md)** (admission, recognition, credibility, uptake separable): **supports, as an instance**. The 29.6% of fully recognised L2 issues that were not carried into calibration is recognition without uptake, measured in a single agent rather than an organization.
- **[CLAIM-266](../claims.d/CLAIM-266.md)** (probes that supply a training signal cannot certify preservation) and **[QUESTION-271](../questions.d/QUESTION-271.md)** (evaluation without capture): **leaves open**. DISCERN uses LLM reviewers and an LLM judge with human adjudication; it does not test judge capture. Its clean controls are a design answer to one evaluation failure (rewarding blanket rejection).
- **[QUESTION-tmpxq2sb](../questions.d/QUESTION-tmpxq2sb.md)** and **[CASE-tmpvq90k](../cases.d/CASE-tmpvq90k.md)**: **illustrates** the scoring separations those studies need (appropriate abstention vs commitment; clean controls as "appropriate non-modification"). Not evidence for either.

## Limitations

Life-science tracks only (two physics tracks in an appendix); bounded tasks; possible familiarity with public datasets; LLM-based L3 grading; Fable excluded for incomplete coverage; the eight models are 2026 proprietary and open-weight systems, so results are time-bound.
