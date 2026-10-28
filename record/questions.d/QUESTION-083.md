---
number: 83
status: Open
formerly:
- QUESTION-tmp2y4xi
title: 'Beyond stable, differentiated authority, which one update rule can produce, can processes that share it come to hold mutually regulated authority with specialized niches, without any governance role being coded in, when some competences show only in rare contexts?'
version: 2
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Narrowed under ADR-049 at the fourth status review. Its first part
    is QUESTION-tmpl8ywi, Answered by CLAIM-277. This question keeps
    niches and mutual regulation.
tags:
- self-governance
- complex-systems
date: '2026-10-13'
line: distributed-agency
summary: >-
  A10's first decisive question, and the experiment A7 called the ideal
  first result. Two Proposed claims answer it in advance: trust emerges as
  a regularity of endorsement ([CLAIM-277](../claims.d/CLAIM-277.md)), and roles are regimes, not
  kinds ([CLAIM-279](../claims.d/CLAIM-279.md)). Nothing has been run. An answer is a population
  model with no role primitives, and whether durable differentiated
  authority forms.
refined_by:
- QUESTION-tmpl8ywi
- QUESTION-132
- QUESTION-135
bearing:
- CLAIM-279
---
<!-- inactive-ok-file: CLAIM-277 CLAIM-279 CLAIM-288 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# QUESTION-083: Beyond stable, differentiated authority, which one update rule can produce, can processes that share it come to hold mutually regulated authority with specialized niches, without any governance role being coded in, when some competences show only in rare contexts?

## Why it is a question

A10 §10, Question 1: "Can heterogeneous operators spontaneously develop
stable, adaptive patterns of mutually regulated influence?" A7's ideal first
result: "*A population of initially undifferentiated, heterogeneous operators
develops specialized niches, persistent but revisable trust, and higher-level
governance structures solely through local transformation, temporally
discounted policy evaluation, and constrained endogenous endorsement.*" A7
§11's H1 and H7 are its two halves. The owner's condition at U5 was that
niches would emerge "if permitted to evolve appropriately".

The record holds two theses that answer it in advance, [CLAIM-277](../claims.d/CLAIM-277.md) and
[CLAIM-279](../claims.d/CLAIM-279.md), and neither has a model behind it. The design constraint is
A6's: "The crucial experimental design choice is **not to hard-code these
outcomes**." [CLAIM-288](../claims.d/CLAIM-288.md) limits what a positive answer would show. It
would show that governance emerges from fixed local objectives, not that the
organization constitutes itself.

An answer is a population model with no governance or role primitives, the
parameter regimes in which durable differentiated authority forms or fails
to, and ablations showing which mechanism each regime needs (A7 §12.4).

## Note of 2026-10-18: the owner's niche idea again, and a sharper experiment

The owner returned to niche specialization at U46 of the exchange of
2026-10-17: "this looks like a potentially useful integration point for
ideas from ecology like niche specialization." It is the idea's second
appearance ([CLAIM-279](../claims.d/CLAIM-279.md)). A46 found this question and strengthened its
experiment with ecological criteria:

- Compare allocation of influence "based on independent contribution
  estimates, similarity to the dominant policy, or historical
  endorsement alone".
- Ask "whether specialists emerge spontaneously, whether cooperation
  reduces higher-order arbitration costs, whether a rare specialist can
  regain influence when its relevant context returns, and whether the
  organization can reorganize after losing one of its established
  specialists."
- Compare against "ordinary mixtures of experts, contextual routing, and
  multitask-learning baselines. Those architectures already produce
  specialization." The model must show something more, "such as
  **endogenous revision of roles and authority under changing
  conditions**".

From Chesson (2000), A46 took the distinction an answer should report:
coexistence through stabilizing niche differences, not equality of
authority ("Equality of authority ≠ coexistence through differentiated
competence"). The failure mode an answer must rule out, niche exclusion
by authority deprivation, is noted on [CLAIM-277](../claims.d/CLAIM-277.md). Nothing has been run.

## Note of 2026-10-18 (later): a formal bridge, and four sharper questions

A synthesis the owner relayed later on 2026-10-18 (workbench entry of
that date) brought statistical feature learning and ecological
coexistence theory to this question.

- **The potential case is exact.** In symmetric resource-mediated
  competition, A = UᵀU and r = Uᵀb − c, the population dynamics are
  multiplicative gradient flow on a convex feature-selection objective.
  A rare component's invasion fitness is the negative partial derivative
  of that objective, and uninvadable equilibria are its KKT points
  ([CLAIM-369](../claims.d/CLAIM-369.md)). So in that case the recovery test of the note above
  is a marginal-value test. The identity fails once interactions are
  asymmetric or the operators' objectives compete, and that is where this
  question's organizations live.
- **Four refinements are filed as questions:**
  - when feature geometry predicts coexistence ([QUESTION-135](QUESTION-135.md));
  - when differentiation yields positive recovery when rare, rather than
    imposed or entrenched roles ([QUESTION-132](QUESTION-132.md)), with recovery
    exponents λ^resident and λ^conditional;
  - whether specialization can relieve structural frustration by
    enlarging the attainable set ([QUESTION-133](QUESTION-133.md));
  - whether influence-dependent training destroys a marginalized
    specialist's competence ([QUESTION-134](QUESTION-134.md)).
- **The proposed study is [CASE-117](../cases.d/CASE-117.md).** It sets ordinary
  mixture-of-experts routing as the baseline, and imposed against
  endogenous diversity as the central ablation.

Chesson ([LIT-1219](../literature.d/LIT-1219.md)) is still unread. The synthesis recommends reading it
before any negative-frequency-dependence criterion here is given stronger
standing.

## Note of 2026-10-28: the first part split off

The fourth status review split this question under [ADR-049](../decisions.d/ADR-049.md). Whether one update rule yields stable, differentiated authority without a role coded in, and whether it also entrenches, is [QUESTION-tmpl8ywi](QUESTION-tmpl8ywi.md), Answered by [CLAIM-277](../claims.d/CLAIM-277.md) on [CASE-tmpasrij](../cases.d/CASE-tmpasrij.md). This question keeps niches, rare-context competence and mutual regulation.
