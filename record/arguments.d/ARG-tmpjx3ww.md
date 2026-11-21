---
status: Proposed
title: 'The recent findings that small spectral directions matter support the claim that a model''s metrics can rank directions in opposite orders, but do not show that the hyperribbon account mistook a hierarchy of widths for one of importance, since a hyperribbon is already measured in the metric of the predictions and the findings concern other spectra'
version: 1
form: evidence
grounds:
- THEORY-420
- LIT-tmp0gbj6
- LIT-tmp83hha
- LIT-tmp4det7
concludes:
- CLAIM-tmppkdjz
tags:
- information-geometry
- representation-learning
date: '2026-11-21'
line:
- learned-structure
summary: >-
  A41 §§2 and 8 of the exchange "Rich Get Richer Power Laws" (2026-11-21)
  offer four findings on small spectral directions as "a powerful
  correction to our hyperribbon account". They bear on the claim A41 also makes, that
  metrics disagree ([CLAIM-tmppkdjz](../claims.d/CLAIM-tmppkdjz.md)). They do not bear on the hyperribbon,
  which is defined in the metric of the predictions, a spectrum none of
  them measures. The ledger flagged the conflation at A41's L26. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: CLAIM-tmppkdjz LIT-tmp0gbj6 LIT-tmp83hha LIT-tmp4det7 LIT-tmpd3swn — Proposed, filed with this argument, or Deferred works registered from the exchange and not yet read -->

# ARG-tmpjx3ww: The recent findings that small spectral directions matter support the claim that a model's metrics can rank directions in opposite orders, but do not show that the hyperribbon account mistook a hierarchy of widths for one of importance, since a hyperribbon is already measured in the metric of the predictions and the findings concern other spectra

## The inference

A41 cites four findings: zeroing the small singular values of transformer
weight matrices damages the model, and after fine-tuning the smallest
decile matters (Staats et al., held as [THEORY-420](../theory.d/THEORY-420.md)); concept directions
sit in the low-variance tail of the unembedding covariance (Acharya et
al., [LIT-tmp0gbj6](../literature.d/LIT-tmp0gbj6.md)); SGD progresses in the loss Hessian's bulk, not its top
subspace (Song et al., [LIT-tmp83hha](../literature.d/LIT-tmp83hha.md)); and perturbing the unembedding's
least-amplified directions moves next-token distributions more than
matched random perturbations (Xu, [LIT-tmp4det7](../literature.d/LIT-tmp4det7.md)). From these A41 §8
concludes two things. First, "the hierarchy of geometric magnitude can be
very different from the hierarchy of functional significance". Second,
"We originally treated the hyperribbon hierarchy as a hierarchy of
importance. But strictly speaking, a hyperribbon tells us which parameter
combinations are distinguishable under a particular observation metric."

## Critical questions

- **Does the measure measure what it is said to?** For the first
  conclusion, yes. Each finding sets a small quantity in one spectrum
  (weight singular value, representation variance, Hessian curvature,
  logit amplification) against a large effect in another (task loss,
  concept separation, training progress, predictive change). That is an
  instance of metrics disagreeing, which is [CLAIM-tmppkdjz](../claims.d/CLAIM-tmppkdjz.md). For the
  second, no. A hyperribbon is defined in the Fisher metric of the
  model's predictions under its stated noise ([LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), unread): its
  thin directions are those that change the predictions little, which is
  what "unimportant for prediction" means. None of the four findings
  measures that spectrum for parameters. Xu's G_pred is a predictive
  Fisher, but pulled back to a hidden state rather than to parameters. So
  the findings do not show a hyperribbon misranking anything. They show
  that other spectra are poor proxies for the predictive one, and the
  hyperribbon account never used them as proxies.
- **Would the evidence be expected if the claim were false?** If metrics
  always ranked directions alike, the findings would not occur. They are
  evidence for the disagreement. Three are unread, so how large and how
  general the disagreement is, the record cannot yet say.
- **Does it tell the claim apart from its rivals?** The rival "small
  means unimportant in every metric" is refuted by any one finding. The
  rival "the predictive metric is the only one that matters" is not
  touched, since the findings measure importance by effects on
  prediction.

## Verdict

Supports [CLAIM-tmppkdjz](../claims.d/CLAIM-tmppkdjz.md) as instances, pending the readings. Does not
support A41 §2's "correction to our hyperribbon account". What A41 §8 states
correctly, that a hyperribbon is relative to its observation metric, was
true by the hyperribbon's definition. It is not a lesson of the
small-eigenvalue work. The parts of A41 that conflate representation
variance with a parameter-space Fisher hierarchy are the ledger's gap
at L26, recorded here.
