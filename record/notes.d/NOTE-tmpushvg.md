---
status: Read
paper: LIT-2318
title: 'Bao et al. — Contemporary AI lacks the imagination to diverge or negate in science'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2606.08251. **Read** (main
    text and Methods), 2026-11-12. A delegated reader drafted the reading;
    quotations were rechecked by script against the downloaded copy, and any
    that did not match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  Authors of 121,640 recent preprints (bioRxiv, medRxiv, ChemRxiv, PsyArXiv,
  EdArXiv, SocArXiv; arXiv excluded as dominating pretraining corpora) were
  asked to rate hypotheses that 26 LLMs generated from the puzzle and
  context extracted from their own papers, with leakage of the authors'
  hypotheses filtered out. 6,749 scientists returned 25,139 rating sets on
  novelty, feasibility, probability and adoption favourability. Findings:
  non-reasoning LLMs cluster in a narrow "hivemind" while reasoning models
  spread wider; every model proposes null hypotheses less often than humans;
  scientists favour ideas resembling their own and weight probability over
  novelty, with senior social scientists the most resistant; LLM ideas rate
  worst in social science; LLM judges, novelty metrics and top reward models
  agree with experts near chance, while a Qwen3-14B reward model trained on
  the ratings beats a human peer-review agreement baseline. A
  39-million-paper OpenAlex analysis finds the share of abstracts with no
  null claims rose after ChatGPT's release, and an agent-based simulation
  argues an interior optimum for AI adoption.
---
<!-- inactive-ok-file: LIT-tmpsxqr6 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpushvg: Bao et al. — Contemporary AI lacks the imagination to diverge or negate in science

## Contribution

The largest scientist-in-the-loop evaluation of LLM-generated hypotheses, with author-as-judge design, a test of automated evaluators against those judgements, and a link to corpus-level trends.

## Key results

- Hivemind and nulls (Abstract): “non-reasoning LLMs collapse into a narrow "hivemind" of similar ideas while reasoning models explore a wider hypothesis space, but no model spontaneously proposes null hypotheses, a move humans make more freely.” The main text is weaker: “Humans formulate such hypotheses infrequently, but every LLM in our panel formulates them less often”.
- Self-similarity bias (Scientists discount novelty): “Scientists prefer ideas that resemble their own work” (within-author coefficient 1.28, p < 0.001); probability dominates novelty and feasibility in adoption.
- Pluralistic fields (same section): AI ideas in social science were rated less novel, less feasible and less probable than in any other domain; “Where there is no consensus to imitate, imitation looks shallow.”
- Automated judges (Automated evaluators): with three LLM judges, “no model exceeded r = 0.35 on any dimension”; on 5,000 held-out pairs, LLM-as-a-judge, n-gram and semantic novelty metrics, GraphEval and the top RewardBench reward models “All methods perform near chance”.
- Trained reward model (Reward models): biology model 69% / 62% / 67% pairwise accuracy on novelty / feasibility / probability, against a human reviewer agreement floor of 61.0% from 26,731 OpenReview submissions.
- Corpus (Reckless AI use): after ChatGPT's release, “LLMs sharply raised the all-significant share in both fields”; the post-2022 reversal “undoes a decade of progress”. (The causal reading rests on timing and an AI-use detector.)
- Evaluation circularity (Discussion): “automated evaluation in its current form risks generating an optimistic literature about itself. Judges and judged are drawn from the same distribution, and their agreement reflects shared priors more than shared standards.”
- Criteria evolve (Discussion): “Distilling current taste into a model is feasible, as our results show. Distilling the practice that lets taste evolve is harder”.

## Assumptions

Authors are the best judges of ideas extending their own work; the extracted puzzle/context does not leak the authors' hypotheses (98.6% author confirmation); a TF-IDF ensemble classifier detects null claims (99.5% CV accuracy on LLM-generated labels); the corpus trend after 2022 is attributable to LLM use; simulation primitives (correlated error, shared bias, null suppression) are stylized.

## Concepts

Idea space; hivemind; null hypothesis as negation; self-similarity bias; probability vs novelty; pluralistic fields; LLM-as-a-judge central tendency; within-scientist pairwise preference; reward model of scientific taste; all-significant papers; center drift and knowledge extension; null suppression; computational curiosity.

## Bearing on the record

The exchange (A14's table, decoded): "6,749 scientists rated AI-generated follow-up hypotheses relating to their research"; "Models showed limited diversity, did not spontaneously offer null hypotheses in the study, and automated judges agreed weakly with experts." Accurate to the abstract. Two qualifications: "limited diversity" holds for non-reasoning models (reasoning models diverged more); and "did not spontaneously offer null hypotheses" follows the abstract, while the body reports a lower rate than humans, not zero. [LIT-tmpsxqr6](../literature.d/LIT-tmpsxqr6.md) on the branch pairs it with Si et al. as theory-building comparisons; fair.

The LIT names no code. On recheck:

- **[CLAIM-266](../claims.d/CLAIM-266.md)** (probes supplying a training signal cannot certify what the system preserves) and **[CASE-144](../cases.d/CASE-144.md)** (an evaluator that weights evidence agreeing with its previous favourites stops tracking): **support, as evidence of the risk both describe**. The paper's finding that automated judges agree with experts near chance, and its argument that "Judges and judged are drawn from the same distribution", are the empirical side of evaluator capture; its scientists' self-similarity bias (preferring ideas like their own) is the human side of [CASE-144](../cases.d/CASE-144.md)'s mechanism.
- **[QUESTION-271](../questions.d/QUESTION-271.md)** (evaluating one's own processes without capture): **bears on, leaves open**. A reward model trained on expert judgements beats the human agreement floor; the paper itself warns it distils "current taste", not the practice by which criteria change.
- **[CLAIM-470](../claims.d/CLAIM-470.md)** (inquiry can revise what an answer could be) and **[TERM-092](../terms.d/TERM-092.md)** (inquiry frontier): the Discussion's claim that novelty, feasibility and probability are "functions of an evolving disciplinary horizon" is the authors' view, consistent with [CLAIM-470](../claims.d/CLAIM-470.md); not evidence for it.
- **[CLAIM-238](../claims.d/CLAIM-238.md)** (comparative defeat conditions are null results that cannot in practice be met): **tangential**: the paper's account of null suppression concerns publication and generation of nulls, not defeat conditions. No bearing claimed.

## Limitations

Ratings of hypotheses, not tests of them; five hypotheses per author; arXiv excluded; null-claim and AI-use classifiers trained or validated partly on LLM labels; corpus trends are correlational; simulation is a stylized existence proof; the abstract's "no model spontaneously proposes null hypotheses" is stronger than the main text.
