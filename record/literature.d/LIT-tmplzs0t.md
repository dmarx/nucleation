---
status: Active
status_note: >-
  read in full 2026-10-31 ([NOTE-tmp6gc1w](../notes.d/NOTE-tmp6gc1w.md)); worth reading for the cleanest
  theorem that competence across a family of goals fixes the
  environment's dynamics, and for exactly what "contains a world model"
  means in it: the transition function is computable from the
  goal-conditioned input-output map ([THEORY-tmp07kll](../theory.d/THEORY-tmp07kll.md)), which holds of a
  lookup table as much as of a planner ([THEORY-tmpg84fa](../theory.d/THEORY-tmpg84fa.md)). It is the
  objection to the functional reading of [CLAIM-tmph29mx](../claims.d/CLAIM-tmph29mx.md), and it does not
  meet that claim's defeated_if.
title: 'General agents contain world models'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from none: added by the filer of the exchange
    "Analyze nucleation concepts" (2026-10-30 to 31). Citation
    checked against arXiv (v1 2025-06-02). Not named in the
    exchange; registered by the filer as the strongest published
    counterweight to the owner's U20 thesis. The summary follows the
    abstract and the exchange's description; a reading should check
    it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full from arXiv 2506.01622v5 (20 October 2025, the ICML 2025
    camera-ready, PMLR 267), 29 pp., in NOTE-tmp6gc1w; status Deferred →
    Active. The citation now names the venue. The summary is rewritten
    from the text: the old one said the model is extracted "with accuracy
    increasing with the agent's performance", which is right, but left
    out the scope (fully observed, finite, communicating, stationary
    environments; deterministic policies; a regret bound on every goal of
    the family) and the sense of "contain", which is recoverability from
    the policy, not an internal component. The `anthology-candidate` flag
    stays: the paper carries instructions for ML practice.
tags:
- agency
- learning-theory
- anthology-candidate
date: '2026-10-31'
published: '2025-06-02'
arxiv: '2506.01622'
first_author: 'Richens'
keywords:
- 'world models'
- 'general agents'
- 'goal-directed behaviour'
- 'goal-conditioned policies'
- 'linear temporal logic'
- 'regret bounds'
- 'model-free learning'
implementations: []
summary: >-
  Richens, Abel, Bellot & Everitt (2025), ICML. In a fully observed,
  finite, communicating, stationary controlled Markov process, a
  deterministic goal-conditioned policy whose success probability is
  within a factor 1 − δ of optimal on every composite goal of depth up to
  n determines each transition probability to within
  √(2P(1−P)/((n−1)(1−δ))). An algorithm reads the estimate off the
  policy alone, from its first action on either-or goals. A policy
  competent only at one-step goals determines nothing. "Contains a world
  model" means this recoverability from the input-output map, "not its
  specific use", so it holds of any implementation of the same map. The
  experiments use a model-based agent in one 20-state environment.
---
<!-- inactive-ok-file: CLAIM-tmph29mx THEORY-092 — Proposed; the owner's thesis and Block's argument this reading bears on, cited as open -->

# LIT-tmplzs0t: General agents contain world models

Richens, J., Abel, D., Bellot, A., & Everitt, T. (2025). General agents contain world models. *Proceedings of the 42nd International Conference on Machine Learning*, PMLR 267. arXiv:2506.01622.

Read in full in [NOTE-tmp6gc1w](../notes.d/NOTE-tmp6gc1w.md).

## Why this is here

Not named in the exchange. It is the published argument against
[CLAIM-tmph29mx](../claims.d/CLAIM-tmph29mx.md), the owner's U20 thesis that a world model is an
explanatory attribution. Read with Block's lookup-table argument
([THEORY-092](../theory.d/THEORY-092.md)). The reading settles how far it reaches. Under its
assumptions the transition function is identifiable from the
goal-conditioned policy, uniquely to within the bound ([THEORY-tmp07kll](../theory.d/THEORY-tmp07kll.md)).
So on the functional reading, ascribing a world model to a goal-general
agent is not a stance one may withhold, and the thesis's "folk
explanatory tool" is too weak there. But the recovery map runs from the
policy, not from internals, and holds of a lookup table over histories
and goals ([THEORY-tmpg84fa](../theory.d/THEORY-tmpg84fa.md)). It makes no resource comparison and no
intervention, so it does not meet the thesis's defeated_if and does not
reach its claim about realized mechanism. On the thesis's own setup, one
fixed interface with no goal input, Theorem 2 shows nothing need be
encoded at all.
