---
status: Open
title: 'How can overlapping higher-level perspectives be identified from the activity of the members who realize them, without being inserted into the model and without their number being fixed in advance, and told apart from coactivity that a common cause produces; and does a structure so inferred, such as a feature allocation under an Indian buffet prior or a nested topic hierarchy, predict an organization''s responses to interventions on its records, membership and authority better than its communication and authorization relations alone?'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed from T18–T22 of the exchange "Experimental Infrastructure
    Review": the methodological question T18–T20 raised about the Northstar
    simulation, merged with the owner's two proposals for answering it,
    hLDA (T21) and the Indian buffet process (T22).
tags:
- social-ontology
- probabilistic-modeling
- causality
- individuation
date: '2026-10-26'
line: distributed-agency
refines:
- QUESTION-259
summary: >-
  The owner's T18 made employees the population from which an
  organization's perspectives form, and [QUESTION-259](QUESTION-259.md) asks how such
  populations generate perspectives. This asks the prior, methodological
  question: how one would know that they had. The Northstar simulation's
  analyzer ([CASE-tmprl1px](../cases.d/CASE-tmprl1px.md)) found "candidate organizational modes" with the
  number of factors fixed, and its reply said they "could reflect shared
  environmental disturbances". The owner's answer, at T21 ("i wonder if
  something like hLDA might fit here") and T22 ("maybe we could benefit
  from a restaurant process model, like an indian buffet model"), is a
  Bayesian nonparametric latent structure. Those are this question's
  candidate methods, not its answer. It does not ask whether perspectives
  exist in firms.
---
<!-- inactive-ok-file: CLAIM-418 CLAIM-327 CLAIM-427 CLAIM-135 CLAIM-188 TERM-072 TERM-074 — Proposed; the claims and terms the question is framed by, cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: CASE-tmprl1px CLAIM-tmpwr001 CASE-tmplcm41 — Proposed; filed with this question from the same exchange -->

# QUESTION-tmpixgs8: How can overlapping higher-level perspectives be identified from the activity of the members who realize them, without being inserted into the model and without their number being fixed in advance, and told apart from coactivity that a common cause produces; and does a structure so inferred, such as a feature allocation under an Indian buffet prior or a nested topic hierarchy, predict an organization's responses to interventions on its records, membership and authority better than its communication and authorization relations alone?

## Why it is a question

Four conditions pull against each other, and each turn of the exchange
added one.

1. **Not inserted.** "Organizational perspectives are patterns we attempt
   to identify in that machinery—not additional agents we insert above it"
   (T19), so "there is no PerspectiveState inside CorporateState". This is
   [CLAIM-418](../claims.d/CLAIM-418.md)'s first part as a constraint on method.
2. **Overlapping.** Participation is not exclusive ("there is no
   requirement that ∑_p w_ep,t = 1", T19). T22: "perspectives need not be
   mutually exclusive, and we shouldn't have to decide in advance how many
   there are." A partition into clusters cannot express this, and T21 noted
   that classical hLDA gives each document one path through its tree,
   which the nested HDP relaxes ([LIT-002](../literature.d/LIT-002.md), [NOTE-023](../notes.d/NOTE-023.md)). The reading confirms it:
   in hLDA two documents share a topic only by sharing the whole path
   above it ([THEORY-tmp5t37f](../theory.d/THEORY-tmp5t37f.md)).
3. **Not common cause.** T18 §5: "a dynamical mode is not automatically a
   perspective. A high-variance activity pattern might merely reflect a
   shared reporting schedule." T22: "correlated activity may be caused by
   common external events. Employees responding to the same incident don't
   necessarily constitute one emergent perspective." That is [CASE-101](../cases.d/CASE-101.md)'s
   first population, whose members "respond alike to a common input", and
   [QUESTION-063](QUESTION-063.md)'s shared drive against coupling. A check filed with
   [CASE-tmprl1px](../cases.d/CASE-tmprl1px.md) finds three cross-departmental modes among employees who
   never interact.
4. **More than the graph.** T22 §6: "Can inferred participation predict
   the effect of changing an authorization pathway, beyond what the
   authorization graph already tells us? … If an IBP detects an
   organizational mode but that mode adds nothing once communication and
   authority are modeled, we should be reluctant to identify it as a
   causally important perspective." And: "We'd also need to allow the
   inference procedure to find no persuasive organizational perspectives
   at all."

The record holds the parts. [TERM-072](../terms.d/TERM-072.md) says its organizational sense "would
be shown wanting … if sense 1 could not be told from coordinated feedback
in general". [CLAIM-327](../claims.d/CLAIM-327.md) gives a candidate criterion: a collective variable
is in the dynamics when members read it, condition on it and regenerate
it. [CLAIM-135](../claims.d/CLAIM-135.md) says recovery is reconstruction, identification and
constitution, and identifiability reaches the second at most. [CLAIM-154](../claims.d/CLAIM-154.md) and
[CLAIM-188](../claims.d/CLAIM-188.md) price naming a recovered unit, which an inferred number of
features is. [CLAIM-427](../claims.d/CLAIM-427.md) says that recovering modes in the framework's own
terms counts for nothing. What no entry asks is the combined question for
a population of members whose higher-level organization is to be
inferred.

## The candidate methods

- **hLDA and the nested HDP** (T21): a topic hierarchy over the content of
  members' messages ([LIT-tmpk69gp](../literature.d/LIT-tmpk69gp.md), [NOTE-tmpcuo7o](../notes.d/NOTE-tmpcuo7o.md)). T21 said not to "identify its topics directly with
  perspectives", and to "allow the hierarchy to lose if it doesn't provide
  useful explanatory compression". The record already holds a
  nonparametric topic model fitted jointly with an author network
  ([LIT-013](../literature.d/LIT-013.md)'s Twitter-Network Topic Model, [NOTE-008](../notes.d/NOTE-008.md)), which is the
  topics-and-relations combination T21 proposed. T21 also named the
  author–topic model ([LIT-tmpnzjy3](../literature.d/LIT-tmpnzjy3.md)) and the mixed membership stochastic
  blockmodel ([LIT-tmpt5wer](../literature.d/LIT-tmpt5wer.md)).
- **A feature allocation under an Indian buffet prior** (T22, developed at
  T23): which members hold which latent features, with their number left
  open (the review T22 cites, [LIT-tmpxrrf9](../literature.d/LIT-tmpxrrf9.md), [NOTE-tmp9hj4u](../notes.d/NOTE-tmp9hj4u.md)). T23's dynamic beta–Bernoulli form is [CASE-tmplcm41](../cases.d/CASE-tmplcm41.md), with its checks.
  T23 recommends fitting it to a mechanistic simulator that does not itself
  assume the prior ("Option A"), so that "feature discovery can be tested
  against a world that did not itself assume IBP-distributed employees".

Either way, [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md) says what a recovered feature could amount to:
at most a constituent of a perspective, whose organization lies in
relations the allocation leaves open.

## What the readings of the candidate methods show

All seven works T21–T23 cite were read on 2026-10-26.

- **Only the feature allocation overlaps as condition 2 asks.** hLDA's
  overlap is nested: a member shares a theme with another only by sharing
  everything above it ([THEORY-tmp5t37f](../theory.d/THEORY-tmp5t37f.md)). In the author–topic model and the
  blockmodel a member's participation is a vector on the simplex, so more
  of one theme is less of another ([NOTE-tmpjg8xz](../notes.d/NOTE-tmpjg8xz.md), [NOTE-tmphwzim](../notes.d/NOTE-tmphwzim.md)). The
  beta-process family is the one whose participation has no sum-to-one
  constraint.
- **Inferred memberships are not identified.** The author–topic model and
  the blockmodel each leave a continuum of changes of basis free, beyond
  the permutations their papers name ([THEORY-tmp7wy54](../theory.d/THEORY-tmp7wy54.md), [THEORY-tmplo0xb](../theory.d/THEORY-tmplo0xb.md);
  [CLAIM-148](../claims.d/CLAIM-148.md)'s note of 2026-10-26). So a comparison under condition 4 has
  to be made on predicted edges and intervention outcomes, never on the
  memberships themselves.
- **Condition 4 needs extending the relational baseline.** The blockmodel
  is the natural model "given the communication and authorization
  relations", but as published it models only one static graph's edges,
  with no dynamics or interventions; it would have to be extended to the
  intervention outcome. The topic models cannot pass T21's own
  falsification test (identical messages, different authorization
  pathways), as T21 expected of "a content-only hLDA model": their
  likelihoods see only words and authorship.
- **Time and groups have established forms, with gaps.** The dependent IBP
  lets features appear and fade over a covariate such as time without
  fixing their number, with each feature's prevalence held fixed
  ([THEORY-tmpumk4q](../theory.d/THEORY-tmpumk4q.md)). The hierarchical beta process shares a feature
  library across groups with group-specific prevalences, but each member
  belongs to one fixed group ([THEORY-tmpz726y](../theory.d/THEORY-tmpz726y.md)). A beta-process hierarchy
  over overlapping and changing groups is not in the literature read, and
  is an open part of this question.
- **An intermediate layer is still co-occurrence.** Correlated
  latent-feature models put a layer of categories over the features
  ([THEORY-tmpwm0kx](../theory.d/THEORY-tmpwm0kx.md)), a candidate for something between a feature and a
  perspective. A category is a pattern of co-occurrence, so by
  [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md)'s standard it is not a perspective either; and in those
  models a category can switch features on, never off.

## What would count as an answer

A procedure that (i) recovers overlapping modes with their number
inferred, (ii) separates them from modes a shared exogenous driver
produces in a model with no interaction, and (iii) predicts the effect of
intervening on the coupling (team records, delegation, membership,
authorization pathways) better than an equally flexible model given the
communication and authorization relations and no modes, on held-out
interventions. A showing that no such procedure adds anything beyond the
relational graph would answer it too, in the negative.

## What would not answer it

- A factorization that fits trajectories, however flexible.
- Recovering the prior's structure from data generated under that prior,
  which tests the inference, not the structure ([CLAIM-203](../claims.d/CLAIM-203.md)'s note of
  2026-10-26). hLDA's paper has the published example: eight of ten trees
  recovered from corpora simulated under its own prior ([THEORY-tmpvs18m](../theory.d/THEORY-tmpvs18m.md)).
- A mode named after the departments or roles that make it up.
