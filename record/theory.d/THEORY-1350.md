---
number: 1350
status: Active
formerly:
- THEORY-tmpzxpp8
title: 'The Persona Selection Model holds that pre-training gives a language model a distribution over personas, that post-training updates it into a posterior over Assistant personas which runtime context keeps conditioning, and that the Assistant''s traits are a key determiner of behaviour; it disowns a single coherent persona and exhaustiveness, and names as open a router that selects personas and could carry goals no persona has'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-370, at the reading review of 2026-11-11 (by
    topic: representation-learning, ADR-091), and CLAIM-543 now grounds
    on it. The question tests an episode-level mixture against "one
    persona selected per conversation" and notes "The Persona Selection
    Model distinguishes more bearers than the three listed: persona,
    actor, author or narrative, router and the network (NOTE-1512)". No
    other change.
tags:
- representation-learning
- self
date: '2026-11-03'
source:
- LIT-1952
summary: >-
  Marks, Lindsey and Olah (2026), [LIT-1952](../literature.d/LIT-1952.md), read in full in
  [NOTE-1512](../notes.d/NOTE-1512.md). Active as a statement of what the model says and does
  not say, all of it in the text. It does not say that the model is true:
  the authors are "overall unsure how complete" it is, its evidence is
  surveyed rather than new, and its updating is offered as "can be viewed
  as", with the strict form said to be too strong.
bears_on:
- QUESTION-370
---

# THEORY-1350: The Persona Selection Model holds that pre-training gives a language model a distribution over personas, that post-training updates it into a posterior over Assistant personas which runtime context keeps conditioning, and that the Assistant's traits are a key determiner of behaviour; it disowns a single coherent persona and exhaustiveness, and names as open a router that selects personas and could carry goals no persona has

## Source

Marks, Lindsey and Olah (2026), [LIT-1952](../literature.d/LIT-1952.md); read in [NOTE-1512](../notes.d/NOTE-1512.md).

## What was actually shown

**The statement**, in four parts ("Statement of the persona selection
model"): a distribution over personas from pre-training; post-training as
updating it "using training episodes as evidence"; "a posterior distribution
over Assistant personas", on which "contextual information provided at
runtime still affect[s] the Assistant persona simulated during a given
rollout"; and Assistant behaviour as "a key determiner".

**The disclaimers.** PSM "does not assert … the Assistant is a single,
coherent persona that is consistent across contexts", nor exhaustiveness,
nor that the model stays in character or simulates perfectly.

**The open question.** A spectrum from the shoggoth to the operating
system, with the router between: a post-training mechanism "for selecting
which persona to enact", which "works even if no single persona has the
goal", and whose behaviour stays "locally persona-like" (Appendix B: persona
swapping deceives with no persona lying).

The evidence is the authors' survey of others' work and one coin-flip
experiment on one model (88% preferred against 1% dispreferred, against
about 50% for the base model).

## What this does not say

- That language models are persona distributions: the post is a mental
  model whose completeness its authors doubt.
- That post-training is Bayesian conditioning: the authors call the strict
  "fine-tuning = conditioning" view "somewhat too strong for the empirical
  evidence".
- That a router exists: it is a constructed possibility.
- That one persona is selected per conversation: the statement has context
  conditioning the persona within a rollout.
