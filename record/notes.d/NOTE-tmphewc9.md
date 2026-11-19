---
status: Read
paper: LIT-tmp2di18
title: 'Aryabumi and colleagues — To Code, or Not To Code? Exploring Impact of Code in Pre-training'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2408.10914v1 (HTML,
    CC BY-NC-ND): sections 1–7 in full; appendices skimmed; values plotted
    only in figures not read. Running notes on the branch
    claude/readers/scheduling-followups (the procedure proposed in pull
    request 537). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Code-initialized, balanced and text-only pretraining compared at 400B
  total tokens. Code first wins on reasoning before cooldown and loses
  after it; mixing is recommended. Natural-language tokens are not
  matched; no cost to a threshold; one run per arm.
---
<!-- inactive-ok-file: LEAD-tmpjdtrl CLAIM-756 THEORY-tmpk9cmk THEORY-tmpsewbi THEORY-tmpd6smn THEORY-tmpd6l4a — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmphewc9: Aryabumi and colleagues — To Code, or Not To Code? Exploring Impact of Code in Pre-training

## Contribution

A broad ablation of code in pretraining at fixed total tokens: code- or
balanced-initialized models continued on text, code share from scratch,
code quality, and cooldown with and without code.

## Key results

1. **Code first, before cooldown.** Code→text and balanced→text "beat the
   text-only baseline on NL reasoning tasks by 8.8% and 8.2% relative
   improvement respectively" (§3.1); Table 2: 53.3 and 53.0 against 49.0.
   Code→text sees 180B text tokens, text-only 400B. Phase 2 is not pure
   text: "We use a 10% of code in text mixture data during continual
   pre-training of code-initialized models" (footnote 5).
2. **Mixing from scratch.** "The best performance is from a model with 25%
   code and 75% text, with a 3.4% relative improvement over a model with 0%
   code" (§3.3); knowledge falls as code rises.
3. **Cooldown.** With code it adds to reasoning and knowledge; "cooldown
   without code does not provide any increases for both NL reasoning and
   Code" (§3.5). After cooldown (Table 2) text-only reaches 54.1, balanced→
   text 54.9, code→text 52.1: code first ends below text-only. The authors
   do not discuss this.
4. **Recommendation.** "include a balanced mixture of code and text data
   during pre-training from scratch" (§3.6).

## Assumptions

Zero-shot benchmark averages stand in for natural-language ability; single
runs; the continued phase's learning-rate schedule is not stated.

## Concepts

Code-initialized continued pretraining; cooldown; code-share optimum.

## Bearing on the record

- **LEAD-tmpjdtrl**, the owner's code-first idea: the positive instance, at
  final score only. No saving is stated in tokens or compute; read from
  Table 2, code first matches text-only knowledge and beats its reasoning
  with less than half the text before cooldown, and loses after it.
- **CLAIM-756**, weak qualification: a phase weak on its own (code alone
  scores poorly on language) belongs to a policy that does better before
  cooldown. Final score, one run, reversed after cooldown: not the cost
  evidence the claim's notes ask for.
- **THEORY-tmpk9cmk** (Hu and colleagues), parallel and weaker: a long
  first phase (half the budget), no threshold, no matched control.
- **THEORY-tmpsewbi** (Stern and colleagues, filed in this change): the
  compute-matched counterpart that finds no benefit. The designs differ:
  total tokens matched here, FLOPs there; benchmark scores here, loss
  there; a long first phase here, a short one there; and code is still in
  phase 2 here.
- **THEORY-tmpd6smn** (Liu and colleagues), consistent: early code beats
  late; here late code in a cooldown also helps.
- **THEORY-tmpd6l4a** (Skill-it), partly in tension: code then text beats
  balanced throughout before cooldown, but natural-language amount is
  confounded, and the authors recommend mixing.
- **THEORY-293**, analogy: knowledge falls monotonically with code share.

## Limitations

Single runs; natural-language tokens unmatched; several internal numerical
inconsistencies between the introduction and §§3.4–3.5.
