---
status: Proposed
promote_when: >-
  A systematic sample, not selected cases: prompts of a stated family (for
  example two-hop factual questions, or rhyming couplets) drawn without
  regard to whether the attribution graph is clear, in which intervening on
  the identified intermediate or planned-word features changes the model's
  output in most of the prompts the model gets right, with the share
  carried by shortcut paths alone measured. It is refuted for a family by
  such a sample in which most correct completions show no intermediate or
  planned representation with a causal effect on the output, or in which
  the shortcut path carries most of them. More case studies chosen because
  the method worked on them cannot settle it: that is the evidence it
  already rests on.
title: 'Claude 3.5 Haiku routinely computes intermediate steps within a single forward pass and plans its outputs ahead, representing a target before the text that leads to it and writing towards it, as Lindsey et al. propose from their case studies'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpl4x31, as the wider thesis that
    THEORY-tmpgx2s5 and THEORY-tmpz8eh5 leave out (ADR-047 v4). The
    article's own Limitations section disclaims it: "Our results are only
    claims about specific examples." After the article was read in full,
    the medical-diagnosis case was added to what the record holds toward
    it, and the jailbreak case (THEORY-tmpzjxhi) to what it holds against;
    the entry was not yet merged, so this was done without a version bump.
tags:
- representation-learning
- cognition
date: '2026-10-26'
source:
- LIT-tmpjvwet
extends:
- THEORY-tmpgx2s5
- THEORY-tmpz8eh5
summary: >-
  Lindsey et al. (2025), [LIT-tmpjvwet](../literature.d/LIT-tmpjvwet.md), read in [NOTE-tmpl4x31](../notes.d/NOTE-tmpl4x31.md): the
  introduction ("Claude 3.5 Haiku routinely uses multiple intermediate
  reasoning steps 'in its head'"; "It displays signs of forward planning")
  and the discussion's sections on plan formation and working backward from
  a goal. The case studies show each mechanism on chosen prompts, and the
  same article has a case without it: on a jailbreak the model "doesn't
  know what it plans to say until it actually says it". The authors report a
  satisfying graph for about a quarter of the prompts they try.
---
# THEORY-tmpfralg: Claude 3.5 Haiku routinely computes intermediate steps within a single forward pass and plans its outputs ahead, representing a target before the text that leads to it and writing towards it, as Lindsey et al. propose from their case studies

## Source

Lindsey et al. (2025), [LIT-tmpjvwet](../literature.d/LIT-tmpjvwet.md), read in full in [NOTE-tmpl4x31](../notes.d/NOTE-tmpl4x31.md): the
Introduction, the case studies, and the Discussion.

## What is asserted

That the mechanisms shown on single prompts are how the model generally
works: "Claude 3.5 Haiku routinely uses multiple intermediate reasoning
steps 'in its head' to decide its outputs. It displays signs of forward
planning, considering multiple possibilities for what it will say well in
advance of saying it. It performs backward planning, working backwards from
goal states to formulate earlier parts of its response."

## What the record holds toward it

- **Two-hop.** [THEORY-tmpgx2s5](THEORY-tmpgx2s5.md): one prompt and five swaps, with a direct
  shortcut beside the two-step path.
- **Planning.** [THEORY-tmpz8eh5](THEORY-tmpz8eh5.md): one couplet in depth, a 25-poem injection
  test, and planned-word features in "about half" of poems examined.
- **An unnamed intermediate.** In the medical case, "preeclampsia"
  features are active though the word is not in the prompt, and inhibiting
  them changes the suggested follow-up question to one suited to the
  alternative diagnosis ([NOTE-tmpl4x31](../notes.d/NOTE-tmpl4x31.md)). One prompt; three further
  examples without interventions.
- **Backward reasoning in a chain of thought.** One hinted cos(23423)
  prompt in which the stated intermediate is computed from the hint
  ([NOTE-tmpl4x31](../notes.d/NOTE-tmpl4x31.md), C6).

## What the record holds against it

- **The jailbreak.** [THEORY-tmpzjxhi](THEORY-tmpzjxhi.md): on one prompt the output word is
  assembled letter by letter with no internal representation before it is
  written, and the request is recognized only from the model's own text.
  The authors: "the model doesn't know what it plans to say until it
  actually says it".
- **Shortcuts beside steps.** The two-hop case has a direct Dallas → say
  Austin edge, with its share of the output unmeasured.

## Why it stays Proposed

The authors' own Limitations: "Our results are only claims about specific
examples. We don't make claims about mechanisms more broadly. For example,
when we discuss planning in poems, we show a few specific examples in
which planning appears to occur. It seems likely that the phenomenon is
more widespread, but it's not our intent to make that claim." And the
selection: a satisfying graph for "about a quarter of the prompts we've
tried", with key nodes hand-tagged to survive the extra pruning applied to
the graphs shown (appendix "Graph Pruning and Visualization"). The same
article contains a case without a represented plan.

## What would confirm or reject it

The promote_when above.
