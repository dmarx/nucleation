---
status: Active
title: 'Richens et al.''s sense of "an agent contains a world model" is that the transition function can be computed from the agent''s goal-conditioned input-output map, uniquely to within the theorem''s error, so the attribution is not a stance an observer may withhold, unlike a representation-theorem fit; but it holds of every implementation of the same map, a lookup table included, and so cannot show that a predictive component is realized inside the agent'
version: 1
tags:
- agency
- philosophy-of-science
- learning-theory
date: '2026-10-31'
source:
- LIT-tmplzs0t
- LIT-642
summary: >-
  Richens, Abel, Bellot and Everitt (2025), LIT-tmplzs0t, read in
  NOTE-tmp6gc1w. The paper says its recovery map is "from the agent's
  policy rather than its activations", that this is "strictly weaker",
  and that it shows "a world model encoded in the agent's policy, not its
  specific use"; it contrasts itself with Savage, whose fit exists even
  for a random policy. That the result applies to Block's lookup table
  (LIT-642) is immediate from Def. 5, which constrains only the map.
  Active: the paper's own statements plus a one-line corollary. It does
  not say whether a compact implementation must have a separable
  predictive part.
---
<!-- inactive-ok-file: THEORY-092 — Proposed; Block's argument, cited as open -->

# THEORY-tmpg84fa: Richens et al.'s sense of "an agent contains a world model" is that the transition function can be computed from the agent's goal-conditioned input-output map, uniquely to within the theorem's error, so the attribution is not a stance an observer may withhold, unlike a representation-theorem fit; but it holds of every implementation of the same map, a lookup table included, and so cannot show that a predictive component is realized inside the agent

## Source

Richens, Abel, Bellot and Everitt (2025), LIT-tmplzs0t, §§2.5, 3, 5 and
footnote 1 (pp. 4–8); read in NOTE-tmp6gc1w. The lookup table is Block's
(LIT-642, THEORY-092).

## What was actually shown

**What "contains" means.** "The existence of this algorithm, which
converts π into a bounded error world model, implies the world model is
encoded in the agent's policy, and learning such policy is
informationally equivalent to learning a world model" (p. 5). The world
model is "any approximation P̂ of the transition function" (p. 4). It is
the environment's, not the agent's subjective model.

**Not a free attribution.** Representation theorems fit beliefs and a
utility to any coherent policy: "we may be able to assign a specific world
model and utility function to a purely random policy ... but this clearly
does not imply that learning a world model is necessary" (p. 8). Theorem
1's P̂ is fixed by the policy to within its error bound
(THEORY-tmp07kll). Two observers with different priors cannot read off
different transition functions. So within the theorem's scope, ascribing
a world model is not a choice of stance in the way Orseau et al.'s
agent-or-device verdict is prior-relative (THEORY-624).

**Not a mechanism.** The map is "from the agent's policy rather than its
activations. This is strictly weaker (as the policy is a function of the
activations)" (p. 7). The theorem holds "regardless of the details of its
training and architecture" (p. 2), and "proves the existence of a world
model encoded in the agent's policy, not its specific use" (p. 7). The
authors decline the interventional criterion used in interpretability as
"tantamount to assuming the agent has a causal world model to begin with"
(footnote 1, p. 8).

**The corollary.** Def. 5 constrains only the map (h, ψ) ↦ a. A table that
stores a δ-bounded agent's choice for every history and goal of depth ≤ n
is itself δ-bounded, and Algorithm 1 returns the same P̂ from it. By the
paper's definition the table contains a world model. Nothing in the
theorem distinguishes it from a planner with an explicit model.

## What this does not say

- **That the attribution is "merely explanatory".** It is a determinate
  property of the goal-conditioned behavioural disposition, though not of
  any finite record of behaviour: the queries are counterfactual goals at
  s₀, which a single run does not show.
- **That a table is a realistic implementation.** It grows with the
  number of histories and goals. Whether every implementation of a
  δ-bounded policy over a rich goal family must spend resources close to
  those of P itself, or must contain a separable predictive part, is not
  addressed. That is the open compression question.
- **That interventions are uninformative.** The paper avoids them as a
  criterion; it does not show they could not locate a model in a given
  agent.
- **Anything beyond its scope.** Full observation, finite stationary
  communicating environments, deterministic policies (THEORY-tmp07kll).
