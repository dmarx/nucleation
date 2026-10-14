---
number: 250
status: Proposed
formerly:
- THEORY-tmp8v4zu
promote_when: >-
  A replication on other text-to-image models, with matched controls
  that the original lacks: reversed prompts equated for plausibility
  with their originals, and two-relation prompts compared with
  single-relation prompts over the same entities, all rated by one rater
  pool in one image style. It would show that the reversal drop is
  confined to asymmetric relations and that error analysis of all
  images, not only the worst, finds relation and role errors dominant.
  It is refuted if plausibility-matched reversals show no drop, which
  would make the effect one of prior rather than binding, or if the
  errors turn out to be mostly missing objects. What cannot settle it:
  aggregate benchmark scores without an error analysis, or automatic
  scoring by a vision-language model, which the paper finds tracks human
  judgement poorly.
title: "DALL-E 3 renders single familiar relations well but is not robustly compositional: human-judged agreement falls when subject and object of an asymmetric relation are reversed and when two relations are combined, and its failures on reversed prompts are mostly wrong or role-swapped relations, not missing objects"
version: 1
tags:
- compositionality
date: '2026-10-14'
source:
- LIT-938
summary: >-
  Fu et al. (2025), [LIT-938](../literature.d/LIT-938.md), read in full in [NOTE-813](../notes.d/NOTE-813.md). Three
  human-rating experiments on one model: the reversal drop is
  significant (t(29) = 3.67), the compositional result is descriptive,
  and the error analysis covers only images below 0.2 agreement. The
  authors' explanation by training-data likelihood rests on a Spearman r
  of 0.09 against a GPT-3 proxy. The finding is about one generator, and
  the ">5 objects" failure often quoted with it comes from the
  vision-language models, not from DALL-E 3.
---
<!-- inactive-ok-file: CLAIM-013 CLAIM-123 THEORY-117 — Proposed; the claims and theory this bears on, open -->

# THEORY-250: DALL-E 3 renders single familiar relations well but is not robustly compositional: human-judged agreement falls when subject and object of an asymmetric relation are reversed and when two relations are combined, and its failures on reversed prompts are mostly wrong or role-swapped relations, not missing objects

## Source

Fu, Lee, Wang, Momennejad, Bihl, Lu and Webb (2025), *TMLR*, [LIT-938](../literature.d/LIT-938.md),
read in full in [NOTE-813](../notes.d/NOTE-813.md): §2 (three experiments on DALL-E 3), A.2
(prompts), A.3 (raters) and A.5 (error analysis).

## What was actually shown

- **Familiar single relations.** On Conwell and Ullman's 75 two-entity
  prompts, DALL-E 3 beats DALL-E 2 on every relation (t(49) = 8.552,
  p < .001). Mean agreement is above 0.8 for 'on', 'near' and 'in'.
- **Reversal.** Swapping subject and object lowers agreement (30 prompt
  pairs, t(29) = 3.668, p = 0.001). The drop is large for 'on', 'in' and
  'chasing', which are asymmetric. It is small for 'near' and
  'touching', which are symmetric, and for 'helping'.
- **Two relations.** For three entities linked by two relations, most
  combinations get "relatively low agreement". A few, such as 'in & in'
  and 'helping & near', stay high.
- **The kind of error.** Among reversed-prompt images below 0.2
  agreement, "the overwhelming majority of errors involved either a wrong
  relation or a relation binding error". A binding error is the roles
  swapped back to the familiar configuration.

The reversal test could have come out flat, as it nearly did for the
symmetric relations. The error analysis could have found missing
objects. Neither happened.

## What this does not say

- **Not why.** The authors attribute the reversal drop to lower
  likelihood in the training data. Their evidence is a Spearman
  correlation of 0.090 between agreement and GPT-3 log-likelihood of the
  prompt, which is a weak proxy for DALL-E 3's training distribution.
  Their broader explanation, a multi-object binding problem, is argued
  by citation. Neither is shown.
- **Not that composition fails with the number of relations as such.**
  The two-relation prompts have three entities and no single-relation
  control with the same entities, so more relations and more objects are
  confounded.
- **Not a general claim about text-to-image models.** One model, one API
  version. Experiment 1 used the 'natural' style and Experiments 2–3
  'vivid', with different rater pools, and Experiment 2's relations were
  chosen for high basic agreement.
- **Not about more than three entities.** The "more than five objects"
  collapse in the abstract comes from the vision-language models on SVRT,
  not from image generation.
- **Not a measure of pragmatic or social relations.** Agentic relations
  (helping, hindering, chasing) are depicted actions, judged by match to
  the prompt.

## Connections

- **[QUESTION-018](../questions.d/QUESTION-018.md).** The explanandum, measured: one prompt carrying
  several conditions loses the conjunction and the role bindings, most
  of all for asymmetric and improbable configurations. It does not decide
  among the question's candidate explanations, and so carries no
  `answers` edge. The plausibility correlation leans weakly toward an
  account by local empirical distributions.
- **[CLAIM-123](../claims.d/CLAIM-123.md).** The conditional-independence condition on composing
  scores is untested here; DALL-E 3 is a black box.
- **[THEORY-117](THEORY-117.md).** Compositional generalization tracks the diversity of
  seen combinations. That fits a drop on rarely seen reversed
  configurations, but the paper has no control of training data.
- **[CLAIM-013](../claims.d/CLAIM-013.md) and [CLAIM-097](../claims.d/CLAIM-097.md).** This is a relational benchmark scored by
  humans, which qualifies [CLAIM-013](../claims.d/CLAIM-013.md)'s description of existing benchmarks
  as object-centred. Its A.6 finding, that VLM judges correlate with
  humans at r ≈ 0.43–0.56 against a human split-half of 0.91, extends
  [CLAIM-097](../claims.d/CLAIM-097.md)'s worry about automatic scoring.
- **[CASE-004](../cases.d/CASE-004.md).** The nearest measured analogue of the case: the same
  objects in a changed configuration.
