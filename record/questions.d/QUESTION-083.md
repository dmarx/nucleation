---
number: 83
status: Open
formerly:
- QUESTION-tmp2y4xi
title: 'Beyond stable, differentiated authority, which one update rule can produce, can processes that share it come to hold mutually regulated authority with specialized niches, without any governance role being coded in, when some competences show only in rare contexts?'
version: 4
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Narrowed under ADR-049 at the fourth status review. Its first part
    is QUESTION-295, Answered by CLAIM-277. This question keeps
    niches and mutual regulation.
- version: 3
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added, from the readings of Cooper and West,
    Power et al., Bunin, Hofbauer and Schreiber, Marsland et al.,
    Blumenthal et al., Letten et al. and Li et al. The question is
    unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: Serván and Allesina read
    (NOTE-tmpwunhc), no order-of-arrival entrenchment in the
    positive definite potential case; Ito and Kaneko read
    (NOTE-tmp2xl62), influence without mutual regulation; Chesson
    1990 Unfetched and 1994 Unavailable. The question is unchanged.
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
- QUESTION-295
- QUESTION-132
- QUESTION-135
bearing:
- CLAIM-279
---
<!-- inactive-ok-file: CLAIM-277 CLAIM-279 CLAIM-288 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1219 — Unavailable since 2026-10-29; cited as the reading the synthesis recommended, not reached, nothing here rests on it -->
<!-- inactive-ok-file: LIT-tmpdoqmq LIT-tmpf923j — Unfetched and Unavailable since 2026-10-29; Chesson 1990 and 1994, cited in the note of that date as not read, nothing here rests on them -->

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

The fourth status review split this question under [ADR-049](../decisions.d/ADR-049.md). Whether one update rule yields stable, differentiated authority without a role coded in, and whether it also entrenches, is [QUESTION-295](QUESTION-295.md), Answered by [CLAIM-277](../claims.d/CLAIM-277.md) on [CASE-182](../cases.d/CASE-182.md). This question keeps niches, rare-context competence and mutual regulation.

## Note of 2026-10-29: the ecology and mixture-of-experts works, read

Eight works the synthesis of 2026-10-18 brought to this question are now
read. Two are positive instances with a qualification, and the rest limit
what an answer can borrow.

- **Positive, in a narrow setting.** Cooper and West, [LIT-1225](../literature.d/LIT-1225.md)
  ([NOTE-1369](../notes.d/NOTE-1369.md)): division of labour emerges with no group-level
  selection and no coded roles, from kin selection on one shared rule,
  with relatedness and a single task. Power et al., [LIT-1235](../literature.d/LIT-1235.md)
  ([NOTE-1368](../notes.d/NOTE-1368.md)): differentiated organization emerges, but with a
  coded-in constraint, the normalizing trade-off, which the authors say
  the result depends on (Appendix H) and which is imposed, not derived.
  [CLAIM-288](../claims.d/CLAIM-288.md)'s caveat, that this is organization from fixed local objectives
  and not self-constitution, applies to both.
- **History dependence, shown less than read.** Bunin, [LIT-1234](../literature.d/LIT-1234.md)
  ([NOTE-1397](../notes.d/NOTE-1397.md)), derives where the unique outcome ends. That the
  alternative outcomes then depend on order of arrival is shown by
  simulation only, and "entrenchment of whatever gained influence early"
  is the synthesis's reading of that phase, which the paper does not test.
- **Assembly end-points.** Hofbauer and Schreiber, [LIT-1233](../literature.d/LIT-1233.md)
  ([NOTE-1379](../notes.d/NOTE-1379.md)): the −i communities are assembly end-points, so whether
  a role can be filled depends on the end-points reached without it, as
  the synthesis read them.
- **Revision needs removal or asymmetry.** Marsland, Cui and Mehta,
  [LIT-1230](../literature.d/LIT-1230.md) ([NOTE-1352](../notes.d/NOTE-1352.md)): under symmetric resource competition assembly
  is monotone, and no assembly sequence can undo an invasion except by
  killing species.
- **Where optimization ends.** Blumenthal, Rocks and Mehta, [LIT-1236](../literature.d/LIT-1236.md)
  ([NOTE-1366](../notes.d/NOTE-1366.md)): loss of reciprocity produces chaos only when the
  correlation ρ falls below √(S*/M*), so the limit of reading such a
  population as an optimizer is a boundary that depends on packing, not a
  point.
- **The bridge to Chesson is two by two.** Letten, Ke and Fukami,
  [LIT-1237](../literature.d/LIT-1237.md) ([NOTE-1377](../notes.d/NOTE-1377.md)), translate Chesson's terms into resource
  impacts for two species and two resources at a stable equilibrium.
  For many operators, Chesson's pairwise ρ does not by itself say whether
  the community coexists.
- **Rare contexts are not modelled.** Li et al., [LIT-1411](../literature.d/LIT-1411.md)
  ([NOTE-1380](../notes.d/NOTE-1380.md)), prove specialization among identically initialized
  experts, but their tasks arrive uniformly, so whether a specialist for a
  rare context survives is not addressed.

Chesson, [LIT-1219](../literature.d/LIT-1219.md), is now Unavailable, so the note of 2026-10-18's
recommendation to read it first stays unmet. The question is unchanged
and stays Open.

## Note of 2026-10-29: order of arrival in the potential case, a one-way core, and Chesson again

- **Serván and Allesina**, LIT-tmp8en4t (NOTE-tmpwunhc). In symmetric
  competitive Lotka–Volterra assembly with a positive definite interaction
  matrix, as a Gram matrix of independent feature vectors is, there is no
  entrenchment by order of arrival: every order of arrival ends in the
  same community, and no invasion sequence returns to an earlier one.
  Order-dependence needs a symmetric matrix that is not positive definite,
  which a Gram matrix cannot be, or asymmetry. That agrees with Marsland,
  Cui and Mehta's monotone assembly, in the earlier note of this date, and
  sharpens it: in this class an early entrant can be displaced, but the
  community it is displaced into is fixed by the pool, not by history. The
  invasion graph of any symmetric system is acyclic (THEORY-tmplmes0).
- **Ito and Kaneko**, LIT-tmpwxstp (NOTE-tmp2xl62). A population of
  identical processes under one update rule, with no governance primitive,
  in which differentiated and durable influence forms. That is the part
  QUESTION-295 (Answered) already holds. It shows nothing on niches or on
  mutual regulation: the periphery has almost no influence on the core (2
  of about 1,344 possible links), so the regulation is one-way, and
  nothing in the model is a competence that shows in rare contexts.
- **Chesson.** His 1990 paper, LIT-tmpdoqmq, is Unfetched and his 1994
  paper, LIT-tmpf923j, Unavailable, so the note of 2026-10-18's
  recommendation to read Chesson before a negative-frequency-dependence
  criterion gets stronger standing is still unmet.

The question is unchanged and stays Open.
