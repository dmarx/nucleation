---
number: 85
status: Active
formerly:
- CLAIM-tmpo49t2
title: 'A framing effect in a language model is a property of that model under those prompts: generating and judging with one model measures its preferences, and what a translation ought to preserve needs criteria the model cannot supply'
version: 1
role: granted
tags:
- philosophy-of-language
- representation-learning
- philosophy-of-science
date: '2026-10-08'
line: pragmatic-transport
undercuts:
- ARG-008
summary: >-
  A45 §8–9 and A48 §8.5, recovered. Both limbs went in the de-hedging
  after U19, though neither is a hedge: one is a design constraint, the
  other a distinction between normative and descriptive fidelity. The
  manuscript keeps part of the remedy and neither argument.
---
<!-- inactive-ok-file: CLAIM-095 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-085: A framing effect in a language model is a property of that model under those prompts: generating and judging with one model measures its preferences, and what a translation ought to preserve needs criteria the model cannot supply

## The claim

Circularity, A45 §9: "I would explicitly avoid a circular experimental design in
which we: 1. Generate translations with an LLM. 2. Ask the same LLM whether they
preserve pragmatic meaning. 3. Declare its preferred translations more faithful.
That would primarily characterize the model's own preferences." The remedy:
"different models for generation and evaluation, independently constructed
framing conditions, calibrated response measurements, and held-out human
assessments". And: "The existence of a systematic framing effect in one LLM
establishes a property of that model under those prompts. Generalization to
human pragmatics requires additional evidence."

Normative versus descriptive, A45 §8: the paper's two goals are "a **normative
theory of translation fidelity** and a **descriptive theory of how interpreters
construct communicative significance**. LLMs can help test the second. Human
communicative practice remains essential for justifying the first." A48 §8.5:
"model response distributions describe interpreters, not automatically
normative translation quality".

## Where it went

A48 kept both, but neither survived A52. U19 asked to "generally withhold
hedging" ([CLAIM-095](CLAIM-095.md)), and these went in the same sweep, apparently by
inadvertence: A49 itself said the rule did not mean "concealing limitations".
The manuscript keeps parts of the remedy: independent interpreters, split
annotators and held-out human judgements (§10), "heterogeneous-agent chains"
(Case II). It states neither the circularity nor the normative/descriptive
split; its §11 says the choice of observables is "normative and empirically
contestable", which is the nearest it comes.

The circularity limb returned at U26, when the owner told the assistant it was
itself a text-generation action and should delegate. A68: "generating multiple
responses within this conversation doesn't give us independently isolated
inference calls ... That introduces potential experimenter bias and
cross-condition contamination." C6 Appendix F then made it a rule: "Do not use
assistant-authored examples as independent LLM samples or the same generative
model's preferences as an unblinded ground truth" ([CLAIM-028](CLAIM-028.md)). The
manuscript keeps the remedy, not the rule.
