---
number: 655
status: Proposed
formerly:
- CLAIM-tmphgjbz
title: 'The preference an optimizer reads from its remaining users can move with no one''s preferences changing: the change in a weighted average splits exactly into a change in the groups'' weights and a change within the groups, and when a design drives out the users it serves worst the first term alone moves the measured demand toward the design, so a metric can improve while the set of people for whom the product works shrinks'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the decomposition below. As a contribution, defeated if the
  record already holds composition change as a source of apparent change
  in measured preference; the Price equation (THEORY-770) is the general
  form, and this claim is its application to demand read from the users
  who remain.
tags:
- social-science
- mathematical-statistics
- society-and-governance
date: '2026-11-12'
line:
- distributed-agency
bears_on:
- QUESTION-441
summary: >-
  A's (ChatGPT's), A31 §4A and §5 of the exchange "Medical Ethics and
  Media Enshitification" (2026-11-11), with A35 §6's attrition weighting
  and A37 §8's "selection out of the evidence-generating population". On
  the owner's U13–U15. A31: "nobody's underlying preferences need change
  for the observed market preference distribution to move." The
  decomposition is exact and the filer rechecked it. A's corollary for
  method: groups must be defined before the intervention. The wording is
  A's; adopting it is the owner's call.
---

# CLAIM-655: The preference an optimizer reads from its remaining users can move with no one's preferences changing: the change in a weighted average splits exactly into a change in the groups' weights and a change within the groups, and when a design drives out the users it serves worst the first term alone moves the measured demand toward the design, so a metric can improve while the set of people for whom the product works shrinks

## The claim

Let ω_{g,t} be group g's share of the economically weighted activity at
time t and u_{g,t} the group's average preference for a feature. The
apparent market preference is ū_t = Σ_g ω_{g,t} u_{g,t}, and (A31 §5)

Δū = Σ_g (ω_{g,t+1} − ω_{g,t}) u_{g,t} + Σ_g ω_{g,t+1} (u_{g,t+1} − u_{g,t}),

a change of composition plus a change of preference. The identity is exact:
the right side telescopes to Σ_g ω_{g,t+1}u_{g,t+1} − Σ_g ω_{g,t}u_{g,t}.

A31 §4A: if a design makes a game less appealing to low spenders and some
leave, the high spenders' share of what remains rises, so the measured
preference moves toward them, and further changes in their direction look
more profitable, though no one's taste changed. A35 §6 names the same
effect for news ("attrition weighting": "Dissatisfied or underserved users
leave the observable population") and states the consequence: "a metric can
improve while the set of people for whom the product works is shrinking."

A31's methodological corollary: "groups should be defined before the
relevant design changes", or the intervention's effects are read as prior
differences.

## Where it sits

- [THEORY-770](../theory.d/THEORY-770.md), the Price equation: the same split for a population's mean
  character under selection. A31 §6 applies its between-design and
  within-lineage form to the spread of designs among games; this claim is
  the within-product, composition-only case.
- [CLAIM-342](CLAIM-342.md) (a judgement–observation loop confirms itself unless the
  evidence does not pass through the interpretation it tests): exit is a
  route by which the evidence comes to pass through it, because the
  product decides who remains to be observed.
- [CLAIM-348](CLAIM-348.md) (a coarse-graining adequate for an institution's performance
  can merge states its members' claims must distinguish): a measure taken
  over remaining users is such a coarse-graining for those who left.

## What it does not say

That exit is the actual cause of any observed drift; A31 §9 gives the
three-level study that would tell composition from preference change. Or
that specialization on the remaining users is wrong: A37 §8, "A product is
allowed to specialize", and the normative issue arises only where the
firm's claims of success concern a broader population than its data now
represent.
