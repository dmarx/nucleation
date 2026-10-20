---
number: 133
status: Active
formerly:
- THEORY-tmp3fc4z
title: "In List and Menzies's account of causes as difference-makers, a higher-level property that makes a difference to an effect is its cause, and its realizer is not, exactly when in some nearest situation without that realizer the property is realized differently and the effect still occurs; which holds depends on each causal system's counterfactual structure, not on levels a priori"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-133 (batch 047, ADR-047 v2): the downward-exclusion result is
    re-derived in the paper's framework (dated note below). The title is
    corrected in two places where it was false as written: it now requires
    that the higher-level property is itself a difference-maker, and it says
    the effect occurs in some nearest situation, not that it would occur.
    The promote_when, evidence about a particular system, moves to
    QUESTION-213.
tags:
- metaphysics
- philosophy-of-science
- causality
date: '2026-10-05'
source:
- LIT-722
summary: >-
  List & Menzies (2009), [LIT-722](../literature.d/LIT-722.md). Take causes to be difference-makers.
  Then Kim's exclusion principle fails, and a revised one holds or fails
  system by system. Given that a higher-level property makes a difference
  to an effect, its realizer is not a cause exactly when some nearest
  situation without the realizer has the property realized otherwise and
  the effect present; the record re-derived this. The claim that
  higher-level relations are typically insensitive to their realizers is
  an observation about scientific practice, and Pernu disputes the paper's
  main example. Which systems meet the condition is [QUESTION-213](../questions.d/QUESTION-213.md).
supports:
- CLAIM-158
presupposed_by:
- THEORY-410
---
<!-- inactive-ok-file: THEORY-048 — Proposed; named for a parallel, nothing here rests on it -->

# THEORY-133: In List and Menzies's account of causes as difference-makers, a higher-level property that makes a difference to an effect is its cause, and its realizer is not, exactly when in some nearest situation without that realizer the property is realized differently and the effect still occurs; which holds depends on each causal system's counterfactual structure, not on levels a priori

## Source

List & Menzies (2009), [LIT-722](../literature.d/LIT-722.md), read in [NOTE-560](../notes.d/NOTE-560.md).

## What was actually shown

List & Menzies ([LIT-722](../literature.d/LIT-722.md)) take F to cause G when, in relevantly similar
situations, G follows F and fails without it. In that framework they prove
three things:

- A property and its realizer can both be causes of the same effect, but
  only under special conditions: the higher-level relation must be
  realization-sensitive, so the effect would vanish under small changes of
  realizer.
- The realizer is the cause and the higher-level property is not (upward
  exclusion) when the effect tracks the particular realizer.
- The higher-level property is the cause and the realizer is not (downward
  exclusion) exactly when the effect would still follow in some nearest
  situations where the property is realized differently.

The result could have come out the other way: on Kim's principle, upward
exclusion is guaranteed whenever the realizer is sufficient. The paper's
examples are a pigeon trained on red and Andersen's monkeys, whose reaching
intentions are read from aggregate firing rates realised by many neural
patterns.

## What this does not say

- **Not that higher-level causes are always autonomous.** That depends on
  which worlds count as nearest, which the authors leave context- and
  discipline-relative. Their claim that the special sciences typically
  require realization-insensitivity is an observation, not a theorem.
- **Not settled by the neuroscience example.** Pernu ([LIT-147](../literature.d/LIT-147.md)) argues
  neuroprosthetic decoding supports identifying intentions with neural
  states rather than their autonomy.
- **Not specifically about minds.** The framework applies to any levels.
  Applying it to organizations is the record's suggestion, not the
  authors'.

## Connections

- **Biology and psychology ([THEORY-048](THEORY-048.md)).** Biological findings implement
  psychological functions without replacing them, which is downward
  exclusion under this account. No relation is declared, since that
  theory's sources do not use the framework.
- **Group agency ([THEORY-127](THEORY-127.md)).** A rational group's judgments supervene on
  members' whole sets of judgments without being fixed issue by issue.
  Whether a group-level attitude is then a cause of what the group does is
  this account's question. Its answer turns on whether the outcome would
  survive a different distribution of members' judgments realizing the
  same group attitude.

## Derivation (2026-10-20, promotion audit batch 047)

The framework: F is a cause of G iff F is a difference-maker for G, that is F □→ G and ¬F □→ ¬G. Counterfactuals are Lewis–Stalnaker: true iff the consequent holds at every nearest antecedent-world, with strong centering and the limit assumption. At the actual world the realizer P, the property F and the effect G all hold, and P entails F, so every ¬F-world is a ¬P-world.

By centering, F □→ G and P □→ G are true. So F causes G iff ¬F □→ ¬G, and P causes G iff ¬P □→ ¬G.

**Result.** Suppose F causes G. Then P is not a cause of G iff some nearest ¬P-world is an (F ∧ ¬P ∧ G)-world: F realized differently, G still present.

- *If.* Such a world is a nearest ¬P-world where G holds, so ¬P □→ ¬G fails.
- *Only if.* If P is not a cause, some nearest ¬P-world w has G. Suppose w were a ¬F-world. Because the ¬F-worlds are among the ¬P-worlds, no ¬F-world is closer than the nearest ¬P-worlds, so w, at that distance, is a nearest ¬F-world. Then ¬F □→ ¬G puts ¬G at w, a contradiction. So w is an (F ∧ ¬P ∧ G)-world.

**Corollary.** F and P are both causes iff every nearest ¬P-world lacks G. Which case holds is fixed by which situations are nearest for the system in question, not by the levels.

The title before this note said the effect "would still follow" and did not require F to make a difference. Without ¬F □→ ¬G, G surviving a change of realizer does not make F a cause, and the condition the proof needs is about some nearest ¬P-world, not all.
