---
status: Open
title: 'When a network acquires a new distinction, does a direction that was weak become informative first, before a local degeneracy changes and before the distinction becomes decodable, and in which of the model''s spectra was it weak?'
version: 1
tags:
- learning-theory
- representation-learning
- information-geometry
date: '2026-11-21'
line:
- learned-structure
summary: >-
  The owner's U25 in the exchange "Rich Get Richer Power Laws"
  (2026-11-21). It quotes A39's proposed test ("a previously weak direction
  becomes informative, a local degeneracy changes, and a new semantic
  distinction becomes independently decodable") and adds: "I think there's
  been some recent work in the informativeness of small-eigenvalue
  subspaces during learning that might be relevant here". The question is
  the owner's pointer, put as the question it raises; A41's candidate
  answer is set out in the body.
---

<!-- inactive-ok-file: CLAIM-tmppkdjz CLAIM-tmp9bp04 CLAIM-tmpl9zw4 CLAIM-tmpcg4uu TERM-tmpnxjq4 LIT-tmp0gbj6 LIT-tmp83hha LIT-tmp4det7 — Proposed or new, filed with this question, or Deferred works registered from the exchange and not yet read -->

# QUESTION-tmp82zpm: When a network acquires a new distinction, does a direction that was weak become informative first, before a local degeneracy changes and before the distinction becomes decodable, and in which of the model's spectra was it weak?

## The question

U25 quotes A39 §8's test line and adds, verbatim: "I think there's been
some recent work in the informativeness of small-eigenvalue subspaces
during learning that might be relevant here". The owner's pointer raises
an ordering question about three events in acquiring a distinction:

1. a direction that was weak becomes informative;
2. a local degeneracy changes (a learning coefficient, a rank, a
   stability eigenvalue);
3. the distinction becomes decodable or is used.

Do they come in a fixed order, and does the first precede the others?
"Weak" needs a spectrum: representation variance, a weight matrix's
singular values, the Hessian, or the Fisher. These can rank directions in
opposite orders (CLAIM-tmppkdjz; the senses are sorted in TERM-tmpnxjq4).
The question is open until it is answered for a stated spectrum.

## Candidate answers in the exchange

- **A41's prediction.** "The developmental onset of a new semantic
  distinction may first appear as a change in task sensitivity within a
  spectrally quiet subspace, potentially preceding a visible change in
  variance or an identifiable transition in local singularity structure."
  The recent work A41 found is Staats et al. (held: THEORY-420), Acharya
  et al. (LIT-tmp0gbj6), Song et al. (LIT-tmp83hha) and Xu (LIT-tmp4det7),
  the last three unread. None tracks a direction through learning toward
  a new distinction, so none answers the question. They show that small
  directions can matter at a checkpoint.
- **A42's mechanism.** A factored feature switched on just above its
  threshold has variance of order ε² and a gain in fit of order ε
  (CLAIM-tmp9bp04), so in that model events 1 and 2 coincide at s = λ.
  Its variance stays small after the stability change.
- **A43's three times** (CLAIM-tmpl9zw4): encoded, stable, expressed. On
  this account event 1 can precede event 2 by any amount, and event 3
  lags event 2 by a delay that grows with how long the feature sat below
  threshold.
- **A measurement caution** (CLAIM-tmpcg4uu). A change in an estimated
  learning coefficient can be a sloppy direction coming into resolution
  rather than a change of stratum. Event 2 needs the estimate's dependence
  on its inverse temperature, not one value.

A proposed test is LEAD-tmpfrw11.

## What would count as an answer

For a stated spectrum, a tracked direction in a model whose new
distinction can be named, with the three events dated on one clock. The
answer is the order found, and whether it survives a change of
coordinates that leaves the function unchanged. A41 warns that
low-variance rankings can change under "harmless representation
reparameterizations".
