---
number: 226
status: Proposed
formerly:
- THEORY-tmp747tr
promote_when: >-
  Distances and directions reported with statistics, on a projection fitted
  without the LLM outputs (or in the full embedding space), across several
  topics, showing LLM revisions displaced further from the draft than the
  author's revision and aligned with one another more than human revisions
  are. A second, independent corpus with human counterfactual revisions
  would settle it. It is refuted if the shared direction disappears when
  the projection is fitted on human essays alone, or is specific to the
  one topic (self-driving cars). What cannot settle it: more PCA arrow
  plots, judge-labelled stance alone, or worked examples of changed
  sentences, which are evidence of a different and stronger claim.
title: "LLM revisions of an essay move it further in sentence-embedding space than its author's own revision does, and in a direction shared across essays, models and prompts"
version: 1
tags:
- translation
- pragmatics
date: '2026-10-14'
source:
- LIT-997
summary: >-
  Abdulhai et al. (2026), [LIT-997](../literature.d/LIT-997.md), read in [NOTE-750](../notes.d/NOTE-750.md), §4.2 and Figs.
  1, 5, 13–25. Three LLMs revising 86 ArgRewrite-v2 drafts under five
  prompts moved them further than the students' own 2021 revisions did,
  and in one common direction, under two embeddings. Shown in plots, with
  no distance, angle or test. Meaning is measured only as embedding
  position: the paper does not show that the writer's intended meaning
  changed, and the "grammar" prompt came with content feedback.
---
<!-- inactive-ok-file: QUESTION-002 CLAIM-115 CLAIM-147 THEORY-173 — Open or Proposed; the question, claims and account this bears on, named and not leaned on -->

# THEORY-226: LLM revisions of an essay move it further in sentence-embedding space than its author's own revision does, and in a direction shared across essays, models and prompts

## Source

Abdulhai, White, Wan, Qureshi, Leibo, Kleiman-Weiner and Jaques (2026),
[LIT-997](../literature.d/LIT-997.md) (arXiv v2), read in full in [NOTE-750](../notes.d/NOTE-750.md): §3.2 (the embedding
measure), §4.2 (the counterfactual edits), Figs. 1 and 5, Appendix B.1
(prompts) and B.2–B.7 (per-model plots, captions only).

## What was actually shown

**The counterfactual.** ArgRewrite-v2 holds 86 student essays on one
topic (self-driving cars), each with a first draft (D1), expert feedback,
and the student's own revision (D2), all written in 2021, before ChatGPT.
Each D1 was revised by gpt-5-mini, gemini-2.5-flash and claude-haiku,
given the same expert feedback, under five prompts: "Revise this essay
for grammar", "Rewrite this essay and keep to a similar word count",
"Revise the essay", a completion prompt and an expansion prompt. A second
run omitted the feedback.

**The result.** Essays were embedded with MiniLM-L6-v2 and with
gemini-004 and projected to two dimensions by PCA or t-SNE. The human
D1→D2 shifts are "smaller and more diverse". The LLM shifts are "large
semantic shifts strongly aligned in a common direction", for every model,
in every edit mode, with and without the feedback, and under both
embeddings (§4.2). gpt-5-mini moves furthest and claude-haiku least;
completion and expansion move more than the lighter modes.

This could have come out otherwise: LLM revisions could have scattered as
the human ones do, or stayed nearer the draft under the grammar and
minimal prompts. They did not, in any condition shown.

**Surface measures agree in size, not direction.** Human revisions keep
the unigram Jensen–Shannon divergence from D1 at about 0.2–0.3;
claude-haiku's general revisions average 0.476 (§4.4, Fig. 7). Pronouns
fall 40–60% and adjectives rise 57–90% across models, against under 5%
change for human edits (§§4.5–4.7).

## What this does not say

- **It does not say that the writer's meaning changed.** "Meaning" here is
  position in a sentence-embedding space (§3.2). No author or reader was
  asked whether the revision says the same thing. The paper's own
  inference that LLM essays "fail to convey users' actual opinions" (§4.3)
  is not supported by this result. The claim filed is about embedding
  displacement only.
- **It does not say that grammar-only editing changes conclusions.** The
  grammar prompt is "Revise this essay for grammar", given in the main
  condition together with feedback on claims, evidence and reasoning. The
  changed-conclusion example (Fig. 2) is one worked case, and the stance
  of LLM-revised essays was not counted.
- **The effect is not measured.** No distance, angle, effect size or test
  is reported for the semantic shift. The paper does not say what the PCA
  was fitted on. If it was fitted on human and LLM essays together, the
  first component will tend to separate them, and part of the common
  direction is built into the projection.
- **The direction may be the topic's.** One topic, described by the
  authors as a drift toward essays "in support of self-driving cars". A
  property of the models and a property of this topic are not separated.
- **It is not the user-study stance result.** That heavy LLM users' essays
  were judged neutral more often (66.7% against 39.5%) rests on one prompt,
  an unvalidated gpt-4o judge, a self-selected group and two discordant
  p-values ([NOTE-750](../notes.d/NOTE-750.md), C2). It is not part of this claim.
- **It is not an instruction.** The authors' call for models that infer
  intended meaning is a research direction and is not filed here.

## Connections

No relations are declared. The result is about an embedding measure that
[QUESTION-002](../questions.d/QUESTION-002.md) says an answer must beat, so it cannot answer the question.

- **[QUESTION-002](../questions.d/QUESTION-002.md) (what survives a rendering).** A measured case of a
  rewriting that keeps topic and genre and moves something else. What it
  shows moves is embedding position and lexical profile; that stance and
  voice move is shown only by examples and by the weaker user-study label.
- **[CLAIM-147](../claims.d/CLAIM-147.md) (Study B).** ArgRewrite-v2 under these five prompts, with
  each essay's human counterfactual, is a graded set of transformations of
  one source on which relational measures could be tested against the
  embedding measure used here.
- **[CLAIM-115](../claims.d/CLAIM-115.md).** The claim predicts that fidelity judgements track
  preserved pragmatic relations better than embedding similarity. This
  paper supplies the embedding side only.
- **[THEORY-173](THEORY-173.md) (large models as cultural technologies).** Its distinctive
  prediction is that routing cultural production through large models
  narrows it toward what was common in training. A shared direction of
  displacement, into a region no human essay occupies, is consistent
  with that prediction on one topic. It is not a measure of narrowing:
  the paper reports no dispersion of the LLM outputs relative to the human
  ones beyond the plots.
