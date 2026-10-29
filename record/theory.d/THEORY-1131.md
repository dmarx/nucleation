---
number: 1131
status: Proposed
formerly:
- THEORY-tmp7mudy
promote_when: >-
  A replication on Indic pragmatic items whose gold answers are confirmed by
  a panel of native readers of each language, with agreement reported, and
  with enough items per phenomenon that one item does not move a score by
  more than a few points, that again finds (a) MCQ accuracy above NLI
  accuracy on matched items and (b) wrong answers concentrated on the
  literal reading beyond chance. A result on the same 578 items, or one
  whose gold answers come from the item authors alone, does not settle it.
title: 'On native-authored pragmatic items in Hindi, Punjabi, Tamil and Malayalam, current multilingual LLMs pick the right reading from four options more often than they label it unaided, and when wrong they lean toward the literal reading'
version: 1
tags:
- pragmatics
- linguistics
date: '2026-10-29'
source:
- LIT-1817
summary: >-
  Singh et al. (2026), [LIT-1817](../literature.d/LIT-1817.md), read in [NOTE-1345](../notes.d/NOTE-1345.md) from the
  Findings of EMNLP 2026 PDF. MCQ beat NLI in 20 of 20 model–language
  pairs (recomputed). 59.1% of wrong MCQ answers took the literal
  distractor, against 33.3% by chance, and 53.8% of Contradiction items
  were labelled Entailment. The gold answers are each language's one item
  author's reading, cells hold 5–16 items, and the MCQ and NLI sets are
  different items. So "recognizing and reasoning about pragmatic meaning
  are distinct competencies" is the authors' gloss, not a finding.
---

# THEORY-1131: On native-authored pragmatic items in Hindi, Punjabi, Tamil and Malayalam, current multilingual LLMs pick the right reading from four options more often than they label it unaided, and when wrong they lean toward the literal reading

## Source

Singh, Veera Balaji Kumar, Nanda, Madhusoodanan, Guo, Xu and Li (2026),
[LIT-1817](../literature.d/LIT-1817.md), §§3–5, Table 2 and Fig. 3, pp. 43029–43034 of the Findings of
EMNLP 2026; read in [NOTE-1345](../notes.d/NOTE-1345.md).

## What was actually shown

Four native speakers, one per language, wrote 374 MCQ and NLI items over
five phenomena. MCQ distractors include the literal reading; NLI items are
57.5% Contradiction, since a figurative premise often contradicts its literal
hypothesis (p. 43034). Five instruction-tuned LLMs (Llama-3-8B, Gemma-4-31B,
Qwen3-32B, Sarvam-105B, Command-A) were run three-shot on Latin-script
input.

- Mean MCQ accuracy exceeds mean NLI accuracy for every model in every
  language: 20 of 20 (p. 43033), which I recomputed from Table 2.
- "Across all wrong-answer events, models chose the literal distractor 59.1%
  of the time, nearly twice the 33.3% rate expected by chance (p < 0.001)"
  (p. 43034), on the MCQ subset with an identifiable literal distractor.
- On Contradiction items, models predicted Entailment 53.8% of the time and
  Contradiction 23.1% (Fig. 3), pooled over four models.

What could have come out otherwise: errors could have spread evenly over
distractors, or NLI could have matched MCQ for strong models. Neither
happened.

## What this does not say

- **That NLI is harder for the same item.** The MCQ and NLI sets are
  different items, so the gap mixes format with item difficulty.
- **That native speakers would answer as the gold labels do.** Each label is
  one author's reading, reviewed by a team in which only that author speaks
  the language. No human accuracy is reported.
- **That the literal bias is a fixed trait of the models.** The NLI label
  mix is skewed toward Contradiction on purpose, so a model that defaults to
  Entailment is punished more there. The 59.1% subset's size is not given.
- **That recognizing and reasoning about pragmatic meaning are distinct
  competencies** (p. 43035). That is the authors' reading of a format
  effect.
- **Per-phenomenon or per-language rankings.** Cells hold 5–16 items.
