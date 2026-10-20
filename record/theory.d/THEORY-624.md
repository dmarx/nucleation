---
number: 624
status: Proposed
formerly:
- THEORY-tmpragh3
promote_when: >-
  The comparison run on systems other than seven gridworld trajectories,
  with the prior fixed before the data and justified independently of
  the verdicts it gives: robots, animals or deployed models whose agency
  is not in dispute and devices whose agency is, with the posterior
  separating them and staying stable across reasonable priors. It is
  refuted as a criterion of agency if every reasonable prior can be
  matched by another that reverses the verdicts on the same behaviour, or
  if accidentally optimal devices come out as agents where an
  interventional test says they are not. Further toy trajectories, or the
  formalism's coherence, cannot settle it.
title: "Whether an identified system is an agent or a device can be cast as Bayesian model comparison between descriptions of the function it optimises and descriptions of its input-output mapping, so the verdict is relative to the observer's prior; on toy gridworld trajectories goal-seeking comes out agent-like and wall-following device-like, and some priors make everything look like an agent"
version: 1
tags:
- agency
- model-comparison
date: '2026-10-16'
source:
- LIT-911
rivals:
- THEORY-527
- THEORY-801
answers:
- QUESTION-032
summary: >-
  Orseau, McGill & Legg (2018), [LIT-911](../literature.d/LIT-911.md), read in [NOTE-705](../notes.d/NOTE-705.md). A formal
  version of Dennett's choice of stance: the posterior probability that a
  system is an agent, from mixtures of goal-optimizing (inverse RL) and
  input-output descriptions. Illustrated on seven gridworld trajectories,
  with no human study. It presupposes an identified system, and its
  verdicts depend on the prior; under the speed prior everything may look
  like an agent.
---
<!-- inactive-ok-file: CLAIM-168 CLAIM-174 THEORY-036 THEORY-249 — Proposed; related or rival accounts named in Connections, nothing here rests on their being settled -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; cited for the position it states, not leaned on -->

# THEORY-624: Whether an identified system is an agent or a device can be cast as Bayesian model comparison between descriptions of the function it optimises and descriptions of its input-output mapping, so the verdict is relative to the observer's prior; on toy gridworld trajectories goal-seeking comes out agent-like and wall-following device-like, and some priors make everything look like an agent

## Source

Orseau, McGill & Legg (2018), "Agents and Devices: A Relative Definition of
Agency", [LIT-911](../literature.d/LIT-911.md), read in full in [NOTE-705](../notes.d/NOTE-705.md) from the arXiv PDF (v1).

## What was actually shown

- **The definition (§3).** "Devices" are described "in terms of an
  input-output mapping, while 'agents' are described in terms of the function
  they optimise". Agents are ε-greedy toward an optimal policy for some
  utility, with ε integrated out. Bayes' rule over a mixture of each gives
  the observer's posterior that the system is an agent.
- **Observer relativity (§§1, 3.1).** The question "is observer-relative,
  since it depends the observer's prior knowledge". Solomonoff and speed
  priors are offered; "a more observer-dependent prior could also be
  considered".
- **The gridworld (from the prose).** Running in circles and following walls
  are better described as devices. Going straight to a goal, or reaching one
  suboptimally, is better described as an agent. Random behaviour is poorly
  explained by both. With a switching prior, a system that changes goals
  mid-trajectory stays an agent "as long as the switches are rare".
- **Everything an agent.** Under the speed prior, "if any device can be
  represented as an agent then everything may look like an agent because the
  penalty for devices is too large". The proposed fix is to penalise agents
  more.
- **Dennett's examples, informally.** The thermostat is "on the knife edge",
  describable as device or agent with "descriptions of comparable
  simplicity".

The formalism is well formed ([NOTE-705](../notes.d/NOTE-705.md), C1). What could have come out
otherwise on the toy cases is the ranking of seven trajectories, which came
out as intuition expects.

## What this does not say

- **Where the system ends.** It assumes "a clearly identified system that
  takes a sequence of inputs and returns a sequence of outputs". The boundary
  is given, not found.
- **That agency is a fact about the system alone.** The verdict depends on
  the prior, and the paper says so.
- **That the result generalises.** Seven gridworld trajectories, no human
  study and no real system.
- **That counterfactual behaviour matters.** Only what the system actually
  does enters. That is the point Kenton et al. ([THEORY-527](THEORY-527.md)) press: an
  accidentally optimal input-output mapping may be classified as an agent.
- **That "every physical system can be described as either an agent … or a
  device" settles which it is.** The conclusion's dichotomy is a choice of
  description, made by the posterior under a prior.

## Connections

- **Rival.** Kenton et al. ([THEORY-527](THEORY-527.md)) define agents by counterfactual
  adaptation found through interventions on mechanisms, and argue against
  compression-based definitions. The two disagree on accidentally optimal
  systems.
- The prior that makes everything an agent is the permissiveness objection
  ([CLAIM-010](../claims.d/CLAIM-010.md)) in formal dress. [THEORY-036](THEORY-036.md) records the same worry about
  Dennett's compression criterion for real patterns, which "admits almost
  every non-random pattern".
- [CLAIM-174](../claims.d/CLAIM-174.md) takes this comparison as the model-comparison half of its
  admission test, priced by [CLAIM-154](../claims.d/CLAIM-154.md). [CLAIM-168](../claims.d/CLAIM-168.md) presses that the
  identified-system assumption presupposes the boundary a criterion of
  agency should find.
- [THEORY-249](THEORY-249.md) argues that whether a goal is "meaningful" needs a principle
  outside the system, Occam among them. A prior here is such a principle.
- On [QUESTION-032](../questions.d/QUESTION-032.md) it answers relative to an observer: a factor is an agent
  to the degree that its behaviour is better compressed as optimising
  something than as a mapping.
