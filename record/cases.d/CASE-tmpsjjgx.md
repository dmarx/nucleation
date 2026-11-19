---
status: Proposed
title: 'Genres and audiences as classes that engagement data identifies jointly (films by who engages with them, people by what they engage with), which become distinctions a platform acts on and then feed back on the data they were found in: the owner''s example, with a laboratory that separates classes inferred, classes used, and classes that reshape preferences'
version: 1
standing: stipulated
kind: proposed-study
tags:
- network-science
- social-science
- individuation
date: '2026-11-19'
line:
- formal-apparatus
- distributed-agency
illustrates:
- CLAIM-tmpw8xkt
draws_on:
- THEORY-993
bears_on:
- QUESTION-028
- QUESTION-276
summary: >-
  The owner's example, from U10 of the exchange "Topological protection
  explained" (2026-11-18): "how graph clusters/communities like coherent
  "genres" emerge in engagement data like person-film ratings or
  user-subreddit participation". The owner said it "should be described
  in Nucleation"; it was not found. The nearest held entries are [CASE-042](CASE-042.md),
  the owner's collaborative-filtering laboratory for communicative kinds,
  [CASE-097](CASE-097.md) and [QUESTION-113](../questions.d/QUESTION-113.md), the owner's LEGO archetypes from part
  co-occurrence, and [QUESTION-276](../questions.d/QUESTION-276.md), perspectives from member activity. The
  joint identification, the confounds and the three-arm laboratory are
  A's (A24, A26 §11, A27 §5, A29 §9), and A24's toy matrix is
  hypothetical. It illustrates the owner's [CLAIM-tmpw8xkt](../claims.d/CLAIM-tmpw8xkt.md).
---
<!-- inactive-ok-file: THEORY-tmpyydjg — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-119 CLAIM-327 CLAIM-tmpw8xkt — Proposed; cited in this filing of 2026-11-19 -->

# CASE-tmpsjjgx: Genres and audiences as classes that engagement data identifies jointly (films by who engages with them, people by what they engage with), which become distinctions a platform acts on and then feed back on the data they were found in: the owner's example, with a laboratory that separates classes inferred, classes used, and classes that reshape preferences

## The example

The owner, at U10 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf):

> I believe an example I've previously explored which should be described in Nucleation is how graph clusters/communities like coherent "genres" emerge in engagement data like person-film ratings or user-subreddit participation, etc.

In a bipartite matrix of people against films (or users against
subreddits), two films are interchangeable for the engagement process
when the same people engage with them in the same way; two people are
when they engage with the same films. Identifying each side by its
profile over the other is what yields genres and audiences, each relative
to the other (A24 §2; a degree-corrected bipartite block model is the
standard estimator, [LIT-tmpc7kaa](../literature.d/LIT-tmpc7kaa.md)). Formal concept analysis gives the
exact form: concepts are pairs of a set of people and a set of films each
of which determines the other (A26 §4; [CLAIM-119](../claims.d/CLAIM-119.md)). The classes then
become distinctions in use: a recommender routes by genre, users find
each other by it, creators write for it.

## What makes it a case of [CLAIM-tmpw8xkt](../claims.d/CLAIM-tmpw8xkt.md)

The differences among films within a genre, and among people within an
audience, stop mattering to the process, and the classes become what
later operations act on. Whether the classes are closed under the
process's own operations is testable: a recommendation policy defined on
the classes should predict engagement as well as one defined on items.

## Confounds (A24 §6; held)

Shared exposure, popularity, platform promotion and selection all
produce clusters; a missing rating is not a dislike ([CASE-042](CASE-042.md)'s
missing-not-at-random rule). The latent classes are identified only up
to a gauge unless anchors fix them ([CASE-042](CASE-042.md), [THEORY-993](../theory.d/THEORY-993.md)).

## A laboratory (A26 §11, A27 §5, A29 §9)

A simulated bipartite engagement network in three arms: classes inferred
and never used; classes that steer recommendations while preferences stay
fixed; classes that steer recommendations while users and creators
adapt. Measure predictive adequacy, stability, the cost of the task and
closure of the class dynamics, against a negative control in which
popularity and exposure alone generate clusters. A27 §5 adds an arm
training self-supervised objectives on the graph, varying which
equivalences are encouraged, to separate collapse, abstraction and
overcompression.

## What it could and could not show

The third arm is where a category confirms itself: if users come to
behave as the genre says because the recommender treats them so, the
category's predictive success no longer warrants it as a kind ([CLAIM-402](../claims.d/CLAIM-402.md),
[CLAIM-327](../claims.d/CLAIM-327.md)). A's three outcomes for that arm, that the loop reinforces,
creates or erases distinctions, are what to look for. The laboratory
cannot show what the owner's real data showed; the owner's earlier
analysis is not on record.

## A test of closure (the assistant's)

Offered on 2026-11-19 after this filing and accepted by the owner the
same day. [CLAIM-tmpw8xkt](../claims.d/CLAIM-tmpw8xkt.md) makes the claim substantive only where the
classes are closed under the process's own operations. That is
measurable on engagement data split by time. Infer genre and audience
classes from period 1. Then compare two predictions of period-2
engagement: one made at the level of the classes alone (class-to-class
engagement rates carried forward), and one made at the level of items and
people. The closure defect is how much the item-level prediction beats
the class-level one; a reified class has a small defect ([THEORY-820](../theory.d/THEORY-820.md)'s
informational closure, [CLAIM-386](../claims.d/CLAIM-386.md)'s closure defect). The control is a
partition with the same class sizes built from popularity and exposure
alone, which the confounds above say will also cluster. If the genre
partition's defect is not smaller than the control's, the clusters are
not units of the process in the claim's sense, whatever their
descriptive fit. The wording is the assistant's (Claude, in this
session); adopting it is the owner's call.

## An intervention arm (ChatGPT's, at its review of 2026-11-19)

Proposed in ChatGPT's review of the filing, forwarded by the owner. The
closure test is observational. To tell compression from an operative
category, intervene on the recommendation policy while holding the
inferred classification fixed: change exposure experimentally (for
instance, randomize part of what each user is shown across class
boundaries) and ask two things. Does the classification remain a
sufficient basis for predicting engagement when exposure is changed?
And does acting on the classification alter preferences themselves, or
only which preferences become observable? A class that predicts only
under the policy that uses it is a compression of that policy's
exposure; one that keeps predicting under changed exposure is a unit of
the users' own engagement; one whose members' preferences move toward
the class when the policy acts on it is [CLAIM-327](../claims.d/CLAIM-327.md)'s self-reinforcing
collective variable. The wording is ChatGPT's in substance; adopting it
is the owner's call.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Larremore, Clauset and Jacobs ([THEORY-tmpyydjg](../theory.d/THEORY-tmpyydjg.md)), read, give the joint identification as a degree-corrected bipartite block model: the groups on each side are defined by their expected connections to the other side's groups. In their film example (IMDb co-appearance, not ratings), five of six movie blocks were language groups and one a genre; they read blocks as traces of "multiple mechanisms responsible for the existence of edges". That supports the case's confounds. Degree correction is the in-model guard against popularity classes: without it the model "tends to sort vertices by degree".

No status change.
