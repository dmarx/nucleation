---
status: Active
status_note: 'read in full 2026-10-11 ([NOTE-tmpijpu3](../notes.d/NOTE-tmpijpu3.md)) from the arXiv PDF (v1). Worth reading as the cleanest formal version of Dennett''s intentional stance: whether a system is an agent or a device is a Bayesian model comparison between a mixture of goal-optimizing descriptions (inverse RL) and a mixture of input-output mappings, made by an observer with a prior. It presupposes an identified system, and its results depend on the prior chosen.'
title: 'Agents and Devices: A Relative Definition of Agency'
version: 1
tags:
- agency
- model-comparison
- anthology-candidate
date: '2026-10-11'
published: '2018-05-31'
arxiv: '1805.12387'
first_author: 'Orseau'
keywords:
- 'agency'
- 'intentional stance'
- 'inverse reinforcement learning'
- 'Bayesian model comparison'
- 'Solomonoff induction'
- 'speed prior'
implementations: []
summary: >-
  Orseau, McGill & Legg (2018). A system is described either as a device
  (an input-output mapping) or as an agent (the function it optimizes).
  Bayes' rule over mixtures of each gives the observer's posterior
  probability that the system is an agent. In a gridworld, running in
  circles and wall-following come out devices, and heading for a goal,
  even suboptimally or with rare goal switches, comes out an agent.
  Agency here is explicitly observer-relative.
supports:
- CLAIM-tmpm5571
- CLAIM-tmpwv313
---
<!-- inactive-ok-file: CLAIM-tmpm5571 CLAIM-tmpwv313 — Proposed; the claims this reading bears on, open -->

# LIT-tmpq7txx: Agents and Devices: A Relative Definition of Agency

Laurent Orseau, Simon McGregor McGill and Shane Legg (2018) — [ARXIV-1805.12387](https://arxiv.org/abs/1805.12387)

## Key takeaways

*Read in full; see [NOTE-tmpijpu3](../notes.d/NOTE-tmpijpu3.md).*

- **Two stances, formalized.** "'devices' are directly described in terms of
  an input-output mapping, while 'agents' are described in terms of the
  function they optimise".
- **Relative.** The question "is observer-relative, since it depends the
  observer's prior knowledge".
- **The thermostat is on the knife edge.** Its two descriptions are "of
  comparable simplicity".

## Standing in the record

Filed on 2026-10-11 as the model-comparison half of the admission test for
agents ([CLAIM-tmpwv313](../claims.d/CLAIM-tmpwv313.md)), and as a source for the circularity objection
([CLAIM-tmpm5571](../claims.d/CLAIM-tmpm5571.md)). It presupposes the identified system that the owner's
factorization would supply. Tags: `agency` first; `model-comparison` for the
Bayesian agent-versus-device test. `anthology-candidate` comes last
([ADR-005](../decisions.d/ADR-005.md)): the anthology's `agents-and-environments` topic could hold it for
its RL framing. It is read here for what makes a factor of a person, a
couple or a firm an agent. Not held in the anthology.
