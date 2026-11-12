---
status: Proposed
title: 'Demand read from activity or revenue weights each person''s taste by how much they act or spend, so it diverges from person-weighted preference wherever activity goes with taste; and what moves a revenue-optimal design is each group''s marginal revenue response, not its head count or share of spending, so a responsive minority can set a design parameter against the majority''s preference with no change in anyone''s taste'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below. As a contribution, defeated if the
  record already holds the divergence of activity- or revenue-weighted
  demand from person-weighted preference, or the marginal-response
  condition, in a form that applies to an optimizer reading demand from
  behaviour; CLAIM-482 (an organization's aggregate revealed preference
  exists only if its winning moves never cycle) and the performative
  prediction readings (THEORY-839, THEORY-861) are the nearest and state
  neither.
tags:
- social-science
- game-theory
- society-and-governance
date: '2026-11-12'
line:
- distributed-agency
bears_on:
- QUESTION-129
summary: >-
  A's (ChatGPT's), A27 §1, A29 §3 and A31 §2 of the exchange "Medical
  Ethics and Media Enshitification" (2026-11-11), working out the owner's
  U13 and U14. Two results. First, the activity-weighted share of a taste
  can be far from its share of people: 5 users of 100 who each act thirty
  times give 61.2% of the activity. Second, A31: "a minority's influence
  comes from the magnitude of its marginal economic response, not from its
  head count or present spending share alone", with a quadratic example in
  which 5% of players move the optimum to 0.678 of the way toward their
  preferred design. Both computations rechecked by the filer. The owner's
  mechanism, [CLAIM-tmpcv1pg](CLAIM-tmpcv1pg.md), rests on it. The wording is A's; adopting it
  is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpcv1pg — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: LIT-tmpvev3t — Deferred; registered from the same exchange, unread -->

# CLAIM-tmpmz271: Demand read from activity or revenue weights each person's taste by how much they act or spend, so it diverges from person-weighted preference wherever activity goes with taste; and what moves a revenue-optimal design is each group's marginal revenue response, not its head count or share of spending, so a responsive minority can set a design parameter against the majority's preference with no change in anyone's taste

## The claim

**Weighting (A27 §1).** With p_ij person i's propensity to choose category j
and a_i their activity,

- population preference: (1/N) Σ_i p_ij;
- activity-weighted demand: Σ_i a_i p_ij / Σ_i a_i.

If activity and taste are correlated the two diverge. A27's example: 95
occasional users with one session each favouring A, 5 heavy users with
thirty sessions each favouring B. B is preferred by 5% of people and gets
150 of 245 sessions, 61.2% of the activity. "Platforms generally observe
the second quantity more directly than the first." Spending can replace
activity as the weight.

**Marginal response (A29 §3, A31 §2).** A firm choosing a design parameter d
to maximize Π(d) = N_H r_H(d) + N_L r_L(d) + A(d) − C(d) moves d in the
direction of the sign of N_H r_H′(d) + N_L r_L′(d) + A′(d) − C′(d). So
"spending concentration doesn't automatically imply influence over
design": a group that spends most of the money but is insensitive to d
does not move it, and a small group that is very sensitive does.

A31's example: 95% of players prefer d = 0 and 5% prefer d = 1, with
quadratic revenue losses and the minority forty times as sensitive per
person. The optimum is d* = 0.05·40 / (0.95 + 0.05·40) = 2/2.95 ≈ 0.678.
A29's discrete version: 990 players each spend $0.05 less and 10 each
spend $8 more, a net gain of $30.50, and the change is made "despite
reduced spending by 99% of its players".

**The derivation, checked.** The weighted share is arithmetic: 5 × 30 =
150, 95 × 1 = 95, 150/245 = 0.6122. For the quadratic case, with
r_L = −(d)² and r_H = −40(1 − d)², the first-order condition
−2(0.95)d + 2(0.05)(40)(1 − d) = 0 gives d = 4/5.9 = 0.678. And
990 × (−0.05) + 10 × 8 = −49.50 + 80 = 30.50. Recomputed with python on
2026-11-12.

## What it does not say

That anyone is worse off: A29 says the example "does not establish that 99%
became worse off. Spending and welfare aren't equivalent." That heavy
users' tastes change (that is the owner's further mechanism,
[CLAIM-tmpcv1pg](CLAIM-tmpcv1pg.md)). Or that any firm optimizes this way: Pape and colleagues'
71% is a counterfactual from a model ([LIT-tmpvev3t](../literature.d/LIT-tmpvev3t.md), unread), and Zendle and
colleagues' range from uniform to highly concentrated games (A31 §2) is
cited without an identifier.
