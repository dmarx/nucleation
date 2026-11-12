---
status: Read
paper: LIT-2289
title: 'Ghareeb et al. — A multi-agent system for automating scientific discovery'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://www.nature.com/articles/s41586-026-10652-y.pdf. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  Robin chains LLM agents to run the reasoning parts of a drug-repurposing
  cycle. Crow (concise) and Falcon (deep) are literature agents built on
  PaperQA2; Finch analyses experimental data in Jupyter notebooks. Given a
  disease (dry age-related macular degeneration), Robin poses questions,
  proposes ten candidate disease mechanisms, writes reports on in vitro
  models for each, ranks them by an LLM judge's pairwise comparisons,
  proposes 30 drug candidates, ranks them in an LLM-judged tournament, and
  hands the ranked list to human scientists, who choose candidates and run a
  human-written protocol based on Robin's assay.
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmp3z1rp: Ghareeb et al. — A multi-agent system for automating scientific discovery

## Contribution

A demonstration that literature-grounded hypothesis generation and experimental data analysis can
be automated in one lab-in-the-loop system that produced an in vitro-validated repurposing
candidate.

## Key results

1. Scope (abstract): "a multi-agent system capable of fully automating both hypothesis generation and data analysis for experimental biology", "achieving a semi-autonomous approach to scientific discovery".
2. Attribution (abstract): "All hypotheses, experimental directions, data analyses and data figures in the main text of this report were produced by Robin."
3. Human gate: "This ranked list was then reviewed by human scientists, and the top drug candidates were tested in the laboratory by executing a human-generated experimental protocol based on the assay suggested by Robin."
4. Ranking by LLM judge: "The drug candidates were ranked by an LLM-judged tournament according to the strength of the scientific rationale, pharmacological profile and methodology of the supporting literature."
5. Analysis variability: "the analysis results from Finch can vary between runs, even when given identical prompts and data, due to the stochasticity of the language agent", so eight trajectories are merged by meta-analysis.
6. Stopping rule: "The cycle continues until a human has a satisfactory drug candidate."
7. Self-stated limits (Discussion): Robin "does not yet produce precise, executable protocols", and Finch "is also reliant on prompt engineering by domain experts".
8. Clinical status (Discussion): the hypothesis "would of course require validation in a suitable disease model and ultimately in a randomized, placebo-controlled trial".

## Assumptions

Literature synthesis can find "non-obvious connections between disparate fields"; an LLM judge's
pairwise preferences are a usable ranking signal; consensus of stochastic analyses improves
reliability; humans select and execute experiments.

## Concepts

Lab-in-the-loop; literature agents (PaperQA2-based) vs data-analysis agent; LLM-judged pairwise
tournament; consensus meta-analysis of analysis trajectories; combinatorial synthesis.

## Bearing on the record

[LIT-tmpeyhhi](../literature.d/LIT-tmpeyhhi.md) says Hasib et al. bear on [LIT-2289](../literature.d/LIT-2289.md) as one of "the AI-scientist systems
registered from the same exchange". **Accurate as a category.** "Automating scientific discovery"
in the title overstates the autonomy the paper reports: experiment execution, protocol writing
and candidate selection were human, as the abstract's "semi-autonomous" concedes.

- **[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md) / [CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)**: **does not bear** on improving the improver; Robin's
  procedure is fixed across cycles.
- **[CASE-144](../cases.d/CASE-144.md)** (the evaluator that stops tracking) and **[QUESTION-271](../questions.d/QUESTION-271.md)**: **leaves open, relevant
  design point**: Robin's selection among hypotheses is by an LLM judge reading LLM-written
  reports, the self-evaluation configuration those entries worry about; the paper reports no test
  of the judge against independent outcomes, only that a human then reviewed the list.
- **[CLAIM-403](../claims.d/CLAIM-403.md)** (admission, recognition, credibility, uptake separable): an illustration: Robin
  supplies admission and ranking (credibility) and humans retain uptake.

## Limitations

Supplementary Information and most Methods not read; biological claims (ripasudil, KL001, ABCA1)
recorded as the paper's, not assessed; preprint not compared.
