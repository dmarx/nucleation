---
number: 513
status: Active
formerly:
- CLAIM-tmp4htg4
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
- CLAIM-519
grounds:
- THEORY-1249
- THEORY-1260
summary: >-
  From the reading of Richens, Abel, Bellot and Everitt ([LIT-1891](../literature.d/LIT-1891.md),
  [NOTE-1469](../notes.d/NOTE-1469.md)), registered as the objection to watch against the owner's
  U20 thesis [CLAIM-519](CLAIM-519.md). It defeats that thesis's functional reading
  only. The thesis's defeated_if is not met: the theorem holds "regardless
  of ... architecture", makes no matched-resource comparison and no
  intervention on internals, and its authors say the map runs "from the
  agent's policy rather than its activations". Within its scope, though,
  calling a world model an explanatory attribution is too weak. The bound
  was re-derived and checked against an adversarial agent.
---

# CLAIM-513: Across a family of goals, a world model is not an optional explanation of competent behaviour: in a fully observed, finite, communicating, stationary environment, a goal-conditioned policy within a factor 1 − δ of optimal on every composite goal of depth n fixes every transition probability to within √(2P(1 − P)/((n − 1)(1 − δ))), so observers reading the same policy must ascribe the same world model; what it leaves open is whether a predictive component is realized inside the agent, since a lookup table over histories and goals has the same policy

## The objection

Richens et al.'s reduction uses either-or goals. One goal is at most k
successes of a transition (s, a) → s′ in n tries; the other is more than
k. A competent agent's first action locates the binomial median, and the
k at which its choice switches fixes P ([THEORY-1249](../theory.d/THEORY-1249.md)). So the
attribution is determined by the policy. This is unlike a Savage-style
fit, which exists even for a random policy, and unlike Orseau et al.'s
verdict, which is relative to a prior ([THEORY-624](../theory.d/THEORY-624.md)).

Within that scope, [CLAIM-519](CLAIM-519.md)'s "ascribing a world model is an
explanation of the behaviour" is too weak. The world model is a
measurable property of the goal-conditioned disposition, though not of
any finite run.

It also corrects one item in the thesis's list of evidence that goes
beyond the interface. Generalization across goals does not discriminate a
table from a model when the table's domain includes the goals. Such a
table is competent in the theorem's sense and yields the same world model
([THEORY-1260](../theory.d/THEORY-1260.md)).

## What it does not say

- That any component represents P. The theorem is silent on the agent's
  internals, which is the thesis's explicit-component reading, untouched.
- Anything for one fixed objective, partial observation or stochastic
  policies. A single-task or myopic agent need encode nothing about the
  dynamics (their Theorem 2), and the thesis's own setup is of that kind.
- Anything about cost or compression. A lower bound on the resources any
  competent implementation needs is the thesis's compression point, still
  open.

## Note of 2026-11-01: "realized inside" has two readings, and interventions settle one

<!-- inactive-ok-block: CLAIM-tmp1qybv CLAIM-515 — Proposed; cited as context -->
The claim leaves open "whether a predictive component is realized inside
the agent". The constitution debate read today (THEORY-tmp3pqnm,
CLAIM-tmp1qybv) separates two things that phrase could mean. (1) The
agent's competence is produced through an internal state that carries
predictions and later shapes action. That is causal. An intervention on
the state, such as a patch to it, can be surgical, and it is what tells
the lookup table from the model. (2) The competence consists, at a time,
in such a component. Every intervention on the competence then also acts
on some component along another path, and no finite set of interventions
shows the relation. What is left open here is (1), which interventions can
settle. CLAIM-515's "realized" should say which it means.

No status, title or warrant changes.
