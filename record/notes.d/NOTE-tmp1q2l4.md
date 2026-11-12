---
status: Read
paper: LIT-tmpsxqr6
title: 'Si, Yang and Hashimoto — Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2409.04109. **Read** (main
    paper, §§1–11 and ethics section); appendices (templates, review form,
    idea examples with reviews, mixed-effects tables, execution agent)
    skimmed: Appendix N's mixed-effects paragraph read. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  A controlled comparison of research ideas written by 49 expert NLP
  researchers with ideas from a Claude-3.5-Sonnet ideation agent (retrieve
  papers, generate 4,000 seed ideas per topic, deduplicate, rank by a
  pairwise Swiss-tournament ranker), on seven prompting-research topics,
  with ideas normalized to one template and style. 79 experts wrote 298
  blind reviews. AI ideas were rated significantly more novel than human
  ideas in three statistical treatments (per review, per idea, per
  reviewer), excitement sometimes higher, feasibility slightly lower but not
  significantly. The agent's ideas became repetitive at scale (about 200
  unique of 4,000), and LLM judges agreed with human reviewers less than
  humans agree with each other.
---
<!-- inactive-ok-file: CLAIM-184 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmp1q2l4: Si, Yang and Hashimoto — Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers

## Contribution

The first large blind human comparison of expert and LLM research ideation with controls for topic and writing style, and evidence on two limits of the overgenerate-and-rank agent: little diversity and unreliable self-evaluation.

## Key results

- Abstract: "we find LLM-generated ideas are judged as more novel (p < 0.05) than human expert ideas while being judged slightly weaker on feasibility".
- §1: feasibility trade-off unproven: gains "may come at the slight expense of feasibility, but our study size did not have sufficient power to conclusively identify these effects". Appendix N's mixed model: AI ideas −0.330 on feasibility.
- §7.1: of 4,000 seed ideas per topic "there are only 200 non-duplicate" unique ideas.
- §7.2: the best LLM evaluator "only achieves an accuracy of 53.3%", below the 56.1% human inter-reviewer consistency.
- §6.3: human reviewing of ideas is noisy: "reviewers have a relatively low agreement (56.1%)" versus 66.0% (NeurIPS 2021) and 71.9% (ICLR 2024).
- §6.1: human participants' ideas were "about the top 43% of all their past ideas", mostly written on the spot.
- §10 Q4: an execution agent's results "can be misleading because the agent often skips or modifies steps in the baselines or proposed methods".

## Assumptions

- Blind expert ratings of written proposals measure idea quality; novelty is judged, not checked against outcomes (the authors say so and plan an execution study).
- The human ideas are a fair baseline (they concede they are median, not best, ideas).
- Style normalization by an LLM preserves content (first author checked human ideas manually).

## Concepts

Research ideation; overgenerate-and-rerank; Swiss-system pairwise ranking; style normalization; human rerank condition; idea diversity / duplication; LLM-as-a-judge reliability; inter-reviewer agreement; execution study.

## Bearing on the record

A (A14 §1 and filing table, "Si et al. 2025") says: over 100 NLP researchers; LLM proposals rated more novel, somewhat less feasible; weak LLM self-evaluation; little idea diversity. **Accurate**, with one qualification: the feasibility shortfall is not statistically significant in the main tests (the paper says "slightly weaker" and that the study lacked power); "somewhat less feasible" should be stated as a non-significant trend.

- **LIT-2329** (Li 2026, "complementary strengths in theory building") and **LIT-2318** (Bao 2026, "Contemporary AI lacks the imagination to diverge or negate"): both unread. Si et al. is an earlier, read baseline in the same comparison class. Its results **bear on both without settling either**: rated novelty favours the LLM, which sits uneasily with a blanket "lacks imagination" thesis, but the duplication result (200 of 4,000) is evidence of narrow generation, which is consonant with it. Its point that human idea judgments are noisy (56.1% agreement) bounds what any human-rated comparison like LIT-2329's can show. Write as context, not support.
- **QUESTION-tmps5iou / journal-article line**: if the article claims luria helps idea generation or theory building, Si et al. shows how such a claim is evaluated (blind experts, matched topics, normalized style) and that LLM judges cannot substitute for the reviewers. Methodological bearing only.
- **CASE-188** (entrenchment vs resolve) and **CLAIM-184**: §7.2's finding that LLM rankers disagree with expert rerankers (17 of 49 overlap) is a warning against scoring revision quality by LLM judge; leaves both open.

## Limitations

Appendix tables not checked number by number; the Test 2/3 numeric tables extracted poorly. The planned execution study is not part of this paper.
