---
status: Active
title: 'Across a family of goals, a world model is not an optional explanation of competent behaviour: in a fully observed, finite, communicating, stationary environment, a goal-conditioned policy within a factor 1 − δ of optimal on every composite goal of depth n fixes every transition probability to within √(2P(1 − P)/((n − 1)(1 − δ))), so observers reading the same policy must ascribe the same world model; what it leaves open is whether a predictive component is realized inside the agent, since a lookup table over histories and goals has the same policy'
version: 1
role: counter
warrant: demonstrated
defeated_if: >-
  An error in Richens et al.'s Theorem 1, or a policy meeting their
  definition of competence with which two transition functions differing
  by more than the bound are both consistent. Not defeated by showing that
  an agent with no internal model meets the definition, which this claim
  grants; nor by single-task or myopic agents, which it excludes (their
  Theorem 2).
tags:
- agency
- philosophy-of-science
- learning-theory
date: '2026-10-31'
line:
- distributed-agency
objects_to:
- CLAIM-tmph29mx
grounds:
- THEORY-tmp07kll
- THEORY-tmpg84fa
summary: >-
  From the reading of Richens, Abel, Bellot and Everitt (LIT-tmplzs0t,
  NOTE-tmp6gc1w), registered as the objection to watch against the owner's
  U20 thesis CLAIM-tmph29mx. It defeats that thesis's functional reading
  only. The thesis's defeated_if is not met: the theorem holds "regardless
  of ... architecture", makes no matched-resource comparison and no
  intervention on internals, and its authors say the map runs "from the
  agent's policy rather than its activations". Within its scope, though,
  calling a world model an explanatory attribution is too weak. The bound
  was re-derived and checked against an adversarial agent.
---

# CLAIM-tmp4htg4: Across a family of goals, a world model is not an optional explanation of competent behaviour: in a fully observed, finite, communicating, stationary environment, a goal-conditioned policy within a factor 1 − δ of optimal on every composite goal of depth n fixes every transition probability to within √(2P(1 − P)/((n − 1)(1 − δ))), so observers reading the same policy must ascribe the same world model; what it leaves open is whether a predictive component is realized inside the agent, since a lookup table over histories and goals has the same policy

## The objection

Richens et al.'s reduction uses either-or goals. One goal is at most k
successes of a transition (s, a) → s′ in n tries; the other is more than
k. A competent agent's first action locates the binomial median, and the
k at which its choice switches fixes P (THEORY-tmp07kll). So the
attribution is determined by the policy. This is unlike a Savage-style
fit, which exists even for a random policy, and unlike Orseau et al.'s
verdict, which is relative to a prior (THEORY-624).

Within that scope, CLAIM-tmph29mx's "ascribing a world model is an
explanation of the behaviour" is too weak. The world model is a
measurable property of the goal-conditioned disposition, though not of
any finite run.

It also corrects one item in the thesis's list of evidence that goes
beyond the interface. Generalization across goals does not discriminate a
table from a model when the table's domain includes the goals. Such a
table is competent in the theorem's sense and yields the same world model
(THEORY-tmpg84fa).

## What it does not say

- That any component represents P. The theorem is silent on the agent's
  internals, which is the thesis's explicit-component reading, untouched.
- Anything for one fixed objective, partial observation or stochastic
  policies. A single-task or myopic agent need encode nothing about the
  dynamics (their Theorem 2), and the thesis's own setup is of that kind.
- Anything about cost or compression. A lower bound on the resources any
  competent implementation needs is the thesis's compression point, still
  open.
