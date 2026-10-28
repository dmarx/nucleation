---
number: 556
status: Proposed
formerly:
- THEORY-tmpjelp9
promote_when: >-
  For the ontological half: a natural kind, essential property or
  possibility shown not to be identifiable by any clustering, abstraction
  or generative procedure, which would turn a possibility argument into a
  result. For the epistemic half: a statement precise enough to fail, so
  that a kind known without any procedure "very much like" clustering
  would count against it. Agreement between clusterings and accepted
  kinds cannot settle either half, and neither can stability of a
  clustering under resampling, which spurious structure can also show.
title: "Clustering, abstraction and generative modelling can be how we come to identify natural kinds, essential properties and unrealized possibilities, but kinds, essences and possibilities are not by definition what such algorithms would find under ideal conditions, because nothing guarantees they are effectively computable; so an algorithm's output is evidence about a kind, neither objective nor vacuous, and not what makes it one"
version: 1
tags:
- metaphysics
- epistemology
- philosophy-of-science
date: '2026-10-16'
source:
- LIT-187
summary: >-
  Watson (2023), [LIT-187](../literature.d/LIT-187.md), read in full in [NOTE-172](../notes.d/NOTE-172.md). Three pairs of theses,
  one per task: the epistemic one (EC, EA, EG) accepted, the ontological one
  (OC, OA, OG) rejected, each on the same computability ground. The
  rejection is a bare possibility argument with no example of an
  uncomputable kind, and the acceptance is hedged ("or something very much
  like them") so far that it is hard to falsify. The pragmatic,
  context-relative view of kinds is asserted, not defended. Self-supervised
  learning and foundation models are outside its scope.
bears_on:
- QUESTION-028
---
<!-- inactive-ok-file: THEORY-273 — Proposed; a neighbouring account of natural kinds, named for comparison -->

# THEORY-556: Clustering, abstraction and generative modelling can be how we come to identify natural kinds, essential properties and unrealized possibilities, but kinds, essences and possibilities are not by definition what such algorithms would find under ideal conditions, because nothing guarantees they are effectively computable; so an algorithm's output is evidence about a kind, neither objective nor vacuous, and not what makes it one

## Source

David S. Watson (2023), "On the Philosophy of Unsupervised Learning", [LIT-187](../literature.d/LIT-187.md),
*Philosophy & Technology* 36:28, read in full in [NOTE-172](../notes.d/NOTE-172.md).

## What was actually shown

**One structure, three times.** Each task gets an epistemic thesis and an
ontological one.

- *Clustering (§2).* EC: we learn to identify natural kinds via clustering or
  something like it. Accepted, on functionalist grounds. OC: natural kinds are
  what clustering ought to find under ideal conditions. Rejected: there is "no
  a priori reason to believe that all natural kinds are effectively
  computable", so identifiability via clustering is "not a necessary condition
  for natural kindhood" (p. 7). Sufficiency is left to a "broadly pragmatic"
  sketch: kinds are grouped for a context and purpose, constrained by
  inductive usefulness and participation in laws, and kinds and algorithms
  "may even be co-constitutive" (p. 8).
- *Abstraction (§3).* EA accepted. OA rejected: "Abstraction algorithms may be
  sufficient to identify some essential properties, but essential properties
  are not necessarily identifiable via abstraction algorithms" (p. 12).
- *Generative models (§4).* EG accepted. OG rejected: it needs all possibilities
  to be effectively computable, and restricting possibility to the computable
  is "ad hoc and circular" (pp. 16–17).

**Objectivity (§5).** Hyperparameters (k, cut height, distance, architecture),
data provenance and opacity condition every result, and clustering never tests
k = 1, so it can produce false positives without a correction such as the gap
statistic. Against vacuity: practitioners use a few simple distances, and
pipelines corroborate clusters, for example cancer subtypes checked with
log-rank survival tests (pp. 18–19). The proposed remedy is Mayo's severity,
made partly concrete as resampling stability, generalization of clusters to
held-out data, out-of-sample likelihood and train-on-synthetic scores (pp.
20–21). No severity is computed for any example.

**What could have come out otherwise.** A kind could have been shown to be
uncomputable, which would have turned the rejection into a result. The paper
gives no such case.

## What this does not say

- **That some kind is not computable.** The ontological theses are rejected
  because a kind *might* be uncomputable. No example is offered.
- **That clustering finds kinds.** The epistemic theses are hedged ("or
  something very much like them") so heavily that it is unclear what would
  falsify them.
- **That kinds are pragmatic.** That view is asserted: "I will go to no great
  lengths defending this" (p. 8).
- **That unsupervised evidence is privileged.** The gene-expression example says
  an unsupervised separation is "arguably better evidence" of a treatment
  effect. That is hedged, and Søgaard ([LIT-162](../literature.d/LIT-162.md)) denies any such privilege.
- **That unsupervised learning is the most fundamental branch of AI.** The
  abstract says so; the body supports it with one sentence (p. 3).
- **Anything about modern pretraining.** Footnote 1 excludes self-supervised
  learning and foundation models.

## Connections

- **[QUESTION-028](../questions.d/QUESTION-028.md).** The question asks when robust, generalizable,
  intervention-relevant structure warrants treating a communicative category
  as a real kind. This account constrains the answer: an algorithm's finding a
  category is evidence about it, and on this view cannot be what makes it a
  kind. It also concurs with A191's "None of these independently establishes a
  metaphysical ontology". It does not say what would establish one beyond the
  pragmatic sketch.
- **Natural kinds.** [THEORY-273](THEORY-273.md) holds that inductive usefulness is necessary
  but not sufficient for a natural kind. Watson's sketch of sufficiency leans on
  inductive usefulness and participation in laws, so the two meet there.
- **Søgaard ([LIT-162](../literature.d/LIT-162.md))** replies to the line of argument that clustering is
  epistemically privileged. [NOTE-172](../notes.d/NOTE-172.md) pairs them as claim and rebuttal.
- **Persistence as a criterion.** [QUESTION-113](../questions.d/QUESTION-113.md) asks whether stability under
  refinement picks the same categories as evidence does. Watson's stability
  tests are one of the severity tools he names, and he does not say stability
  suffices.
