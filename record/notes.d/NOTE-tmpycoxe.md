---
status: Read
paper: LIT-2329
title: 'Li, Zoumpoulis, Puranam, Parker et al. — Artificial intelligences and human scientists exhibit complementary strengths in theory building'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2609.32562. **Read**
    (abstract, significance statement, introduction, results R.1–R.3 and
    Discussion read; Methods skimmed; extended data, supplementary materials
    and survey instruments skipped). Read 2026-11-12. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  On a social-science task — predicting which features of academic papers
  are associated with their discussing racial or gender inequality, against
  a machine-learning benchmark, then explaining the realized patterns — the
  authors compare 25 LLMs with 13 senior researchers and 60 doctoral
  students. Individually, the LLMs matched or beat most humans on most
  tasks, produced more elaborate theories (more paths and latent variables)
  that blind raters preferred, but the extra complexity did not buy
  accuracy. Human theories were far more diverse, and human crowds gained
  more from aggregation.
---
<!-- inactive-ok-file: CLAIM-tmpyp3u3 LIT-tmpsxqr6 TERM-tmp8deza — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: LIT-046 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpycoxe: Li, Zoumpoulis, Puranam, Parker et al. — Artificial intelligences and human scientists exhibit complementary strengths in theory building

## Contribution

- A head-to-head, data-tethered comparison of human and LLM theory building, prediction,
  and revision, at individual and crowd level.
- Measures of theory complexity, semantic diversity (embedding dispersion, core–tail
  clustering), aggregation gain, and revision magnitude vs prior error.

## Key results

1. Abstract, p. 3: "the AIs outperformed most humans individually on most of the present
   tasks, while human theories were more diverse and exhibited greater gains in predictive
   accuracy from aggregation."
2. Abstract: theoretical complexity "was in part ornamental, in that it was not associated
   with more accurate predictions about empirical patterns in data".
3. Abstract: "The AIs were significantly more likely than human scientists to revise their
   theories to incorporate new evidence; human scientists updated their beliefs in a
   selective way that is sensitive to prior prediction errors."
4. R.3, p. 12: "GenAI systems exhibited 42% larger pre- to post-ML semantic revisions than
   human contributors (0.145 vs. 0.102; P < 0.001".
5. R.3, p. 12: "humans changed their theories more when their initial predictions were
   inconsistent with the ML evidence. No comparable relationship was observed among GenAI
   systems" (OLS β = −0.098 for humans; 0.008 for GenAI; interaction P = 0.003).
6. Discussion, p. 16: LLMs "may have approached the post-ML task as a new generation problem
   conditioned on expanded context rather than as an incremental revision of a prior
   theory", possibly "a stateless, prompt-driven revision process."
7. Discussion: yet "their ability to discard prior theories based on new evidence and thus
   avoid theory-induced blindness ... compared favorably to human scientists", while "it is
   not clear if AI should be characterized as comparatively open-minded".
8. R.2: human explanations' distances from their group centroid were "approximately 2.4
   times those of GenAI explanations"; "only 9.6–31.5% of human explanations belonged to the
   core, compared with 92–100% of GenAI explanations".
9. R.1: human crowds "were, on average, 86% more diverse, providing a compositional basis for
   their larger gains from aggregation."
10. Discussion, p. 17: "AI dependence may reduce the diversity of the paths of inquiry
    pursued"; the risk is a drift towards a scientific monoculture.
11. Introduction: the ML benchmark "does not reveal causal relationships", and "a theory may
    be scientifically valuable despite disagreement with this benchmark."

## Assumptions

- Agreement of predictions with an ML-identified correlational benchmark is a fair standard
  for theory quality (the authors flag its limits, result 11).
- Semantic distance between embeddings measures revision and diversity.
- One domain (inequality discourse), four task × effect conditions; the authors repeatedly
  call the expertise and complexity-gradient patterns exploratory.

## Concepts

theory building; a priori prediction and post-hoc revision (pre–post design); ML
benchmark; theory complexity (paths, latent variables); ornamental complexity; predictive
efficiency; semantic diversity, core–tail structure; aggregation gain; wisdom of crowds;
error-sensitive updating; scientific monoculture.

## Bearing on the record

- CASE-188's note says A14 reports from LIT-2329, unread, that 'revising a theory
  more readily is not necessarily better scientific behavior'. **The quoted sentence is not
  in the paper** (searched; "necessarily" occurs only elsewhere). It is A's gloss. The
  paper's own finding supports a version of it — LLMs revised more, but not in proportion to
  prior error (results 3–6) — while its Discussion also credits the LLMs' readiness to
  discard theories as avoiding "theory-induced blindness" (result 7). One should
  keep the quote attributed to A, and if the note is upgraded, cite results 3–6 instead.
- LIT-tmpsxqr6 groups LIT-2329 with Si et al. and LIT-2318 as "theory-building
  comparisons". Fair.

- **CASE-188** (Proposed; corrigible resolve vs entrenchment): *supports its distinction
  with evidence*. The paper separates *how much* a theorist revises from *whether revision
  tracks error*: humans showed error-sensitive revision; LLMs showed larger, error-insensitive
  revision. This is the distinction between corrigibility and mere changeability CASE-188
  wants its diagnostic to draw, measured. Qualifier: one-shot revision, not a long-term
  commitment.
- **CLAIM-tmpyp3u3** / **TERM-tmp8deza** (a record represents standing, not belief
  states): *bears*. The authors' speculation that LLMs may "not maintain an explicit belief
  state at all" (result 6) is a reason a record, not the agents' context, would have to
  carry what was previously held for revision to be incremental.
- **QUESTION-tmpxq2sb** (Open, branch) and **CLAIM-403** (Active): *bears on aggregation*.
  Homogeneous LLM crowds gained less from aggregation (results 1, 9); in a team of agents
  from one model family, adding members adds little independent evidence.
- **LIT-999 / NOTE-840** (Golub & Jackson, wisdom of crowds) and **LIT-046 / NOTE-055**
  (Pilgrim et al., collective intelligence): the diversity–aggregation result is a case of
  the mechanisms those entries hold.
- **LIT-2326** (Belief-R, read in this batch): complementary: Belief-R finds a trade-off
  between updating and maintaining; this finds LLM revision uncalibrated to error.

## Limitations

Extended Data (where expertise and complexity regressions sit) not read; methods only
skimmed; figures not inspected. Single domain; correlational benchmark.
