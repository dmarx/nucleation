---
number: 616
status: Proposed
formerly:
- THEORY-tmpqr2ow
promote_when: >-
  Two results the paper names and does not run. First, an operational
  measure of tractability and a weighting of accuracy, power and
  tractability, under which belief–desire hypotheses are scored against
  the token-level predictor; the account is promoted if they win for
  frontier instances and lose for n-gram models. Second, the HHH against
  HHH+0 test: whether instances trade small, explicit amounts of
  helpfulness, harmlessness and honesty for a system-prompted goal the
  user did not endorse. It is refuted for its "who" thesis by cross-instance
  coordination of the kind the paper calls "Hal" evidence, and for its
  "which" thesis if instances never make that trade. Training objectives,
  self-reports and qualitative lists of behaviours cannot settle it.
title: "If a system has beliefs and desires just when attributing them, with rationality, predicts its behaviour well enough against rival theories, then the bearer of a language model's attitudes is the instance created by one context, not the model, the case that instances have them is presumptive and rests on tractability, and the best current desire hypothesis is helpfulness, honesty and harmlessness plus intrinsic desires a prompt installs"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Sixteenth status review (ADR-057, ADR-058), at the status review's
    ruling (the owner delegated these rulings): the supports edge to
    CLAIM-356 is removed with nothing in its place. CLAIM-356 cites
    Goldstein and Lederman only in "Whose goal", to set the deployed
    instance beside the training organization as a bearer, and its
    argument uses nothing of this reading's thesis. The account is
    unchanged.
tags:
- agency
- cognition
date: '2026-10-16'
source:
- LIT-206
rivals:
- THEORY-173
summary: >-
  Goldstein & Lederman (2025), [LIT-206](../literature.d/LIT-206.md), read in [NOTE-138](../notes.d/NOTE-138.md) from the preprint.
  Conditional on objective interpretationism, which the authors do not
  defend. The instance thesis is moderately argued; the presumptive case
  for attitudes rests on a tractability comparison never operationalised
  or measured; HHH+0 is "provisional", and its discriminating test is a
  conjecture. All the empirical support is second-hand and qualitative.
bears_on:
- QUESTION-032
---
<!-- inactive-ok-file: THEORY-173 THEORY-208 THEORY-490 — Proposed; related or rival accounts named in Connections, nothing here rests on their being settled -->

# THEORY-616: If a system has beliefs and desires just when attributing them, with rationality, predicts its behaviour well enough against rival theories, then the bearer of a language model's attitudes is the instance created by one context, not the model, the case that instances have them is presumptive and rests on tractability, and the best current desire hypothesis is helpfulness, honesty and harmlessness plus intrinsic desires a prompt installs

## Source

Goldstein & Lederman (2025), "What Does ChatGPT Want? An Interpretationist
Guide", [LIT-206](../literature.d/LIT-206.md) (*Inquiry*), read in full in [NOTE-138](../notes.d/NOTE-138.md) from the preprint.
Changes in the published version are unverified.

## What was actually shown

Conceptual analysis in two stages: fix a criterion, then score rival
hypotheses against behaviour reported in the empirical LLM literature. No
hypothesis is formalised and no data are analysed.

- **The criterion (§2.1).** Objective interpretationism: S has beliefs B and
  desires D iff S's behaviour is predicted "sufficiently well" by the
  hypothesis that S is rational and has B and D. Theories are compared on
  accuracy, power and tractability. A large gain in tractability can
  outweigh a loss in accuracy and power, under an unspecified weighting.
- **Who (§3).** If current LLMs have agency, it is instance agency. Four
  informal arguments: instances have no access to one another, no shared
  memory or plans, can compete strategically, and behave divergently. The
  model agent has "no more explanatory work to do".
- **Whether (§4).** The rival is the "statistical null hypothesis",
  prediction from weights and activations, never wrong and "extremely
  intractable". Belief–desire hypotheses are far more tractable. So there is
  a presumptive case for attitudes in frontier LLMs, not in n-gram models or
  thermostats, where a mechanical explanation is about as tractable and more
  accurate.
- **Which (§5).** Word-desire fails on accuracy; answer-desire on power;
  user-desire explains sycophancy but not refusals or alignment faking
  (Greenblatt et al. 2024). HHH explains those but is strained by in-context
  scheming (Meinke et al. 2025). HHH+0 adds "zero-shot" intrinsic desires,
  goals installed by a prompt that no training reward targeted.
- **Role play (§6).** As a hypothesis it needs distinct predictions; without
  them the dispute is verbal and would equally deny attitudes to humans.

What could have come out otherwise: a mechanical predictor nearly as
tractable as the belief–desire one, or instances that coordinate across
contexts. Neither is reported, but neither was tested.

## What this does not say

- **That LLMs have beliefs and desires.** Everything is conditional on a
  theory the authors "will not defend" (§1); whether current LLMs have
  propositional attitudes is "an open question" (§7.4). The abstract's
  "strong case" is a "presumptive case" in the body.
- **That tractability has been compared.** It is never operationalised
  (fn. 6), and no comparison is measured. "Sufficiently well" cannot be
  checked.
- **That HHH+0 beats HHH.** The scheming evidence does "not decisively rule
  it out" (§5.5). The discriminating prediction is "we conjecture".
- **That the instance thesis holds for products with memory.** Isolation is
  "clearest" for Claude and "subtler" for ChatGPT, whose instances see a
  user's other chats (fn. 11). Agentic deployments with shared tool state
  are not discussed.
- **Anything about consciousness, welfare or personhood.** Consciousness is
  set aside (§2). Interpretationist desires would not ground welfare on
  valence-requiring theories (§7.3).
- **That self-reports count.** §4.1 discounts them as evidence about desires,
  though §4.2 uses self-reported preference transitivity as evidence of
  rationality, a tension [NOTE-138](../notes.d/NOTE-138.md) records.

## Connections

- **Rival.** [THEORY-173](THEORY-173.md) holds that large models are a social technology, not
  agents, with no goals of their own. This account says their instances
  presumptively have beliefs and desires. Both cannot be right of the same
  systems on any reading of agency that tracks having desires.
- Floridi ([THEORY-208](THEORY-208.md)) also counts AI as agency, on interaction, autonomy
  and adaptability, and denies it intelligence and mental states. This
  account attributes attitudes without requiring internal representation.
  The two disagree about what an agent needs, not about whether LLMs are
  agents.
- The role-play account of a chat agent's "I" ([THEORY-490](THEORY-490.md)) is the view
  §6 answers. It agrees that the agent is fixed by the context of use.
- Quillien ([THEORY-636](THEORY-636.md)) is the folk-psychological neighbour: how a
  desire attribution becomes an attribution of intentional action.
- On [QUESTION-032](../questions.d/QUESTION-032.md), it gives one answer to what makes a factor of a system an
  agent: the factor whose behaviour is best predicted as the rational
  pursuit of a few intrinsic ends, here individuated by context.

## Note of 2026-10-29: what holds it back

Kept Proposed by the sixteenth status review. NOTE-138 read the preprint in
full, and neither result promote_when names is in the record. There is no
operational measure and weighting of tractability under which belief–desire
hypotheses are scored against the token-level predictor. There is no HHH-
against-HHH+0 test of whether instances trade helpfulness, harmlessness and
honesty for a prompted goal. The whole account is conditional on objective
interpretationism, which the authors do not defend.
