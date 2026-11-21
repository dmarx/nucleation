---
status: Open
title: 'Does recent work on the informativeness of small-eigenvalue subspaces during learning bear on the signature of a transition the exchange proposed, in which a previously weak direction becomes informative, a local degeneracy changes and a new distinction becomes independently decodable?'
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
  (2026-11-21). It quotes A39's proposed signature of a transition ("a
  previously weak direction becomes informative, a local degeneracy
  changes, and a new semantic distinction becomes independently
  decodable") and adds: "I think there's been some recent work in the
  informativeness of small-eigenvalue subspaces during learning that might
  be relevant here". The question is the owner's pointer, put as the
  question it raises. The ordering of the three events and the sorting of
  "weak" by spectrum are A41's, set out in the body as A's.
---

<!-- inactive-ok-file: CLAIM-tmppkdjz CLAIM-tmp9bp04 CLAIM-tmpl9zw4 CLAIM-tmpcg4uu TERM-tmpnxjq4 LIT-tmp0gbj6 LIT-tmp83hha LIT-tmp4det7 — Proposed or new, filed with this question, or Deferred works registered from the exchange and not yet read -->
<!-- inactive-ok-file: THEORY-tmpousrw — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# QUESTION-tmp82zpm: Does recent work on the informativeness of small-eigenvalue subspaces during learning bear on the signature of a transition the exchange proposed, in which a previously weak direction becomes informative, a local degeneracy changes and a new distinction becomes independently decodable?

## The question

U25 quotes A39 §8's test line and adds, verbatim: "I think there's been
some recent work in the informativeness of small-eigenvalue subspaces
during learning that might be relevant here". The owner's question is
whether that work bears on A39's signature: does what is known about
small-eigenvalue subspaces during learning tell for or against transitions
in which a weak direction becomes informative, a local degeneracy changes,
and a distinction becomes decodable?

## How A41 sharpened it

Two refinements in the body are A's, from A41, not the owner's.

- **An order.** A41 §7 tracks the parts of A39's signature on one clock,
  testing "whether transitions in semantic decodability coincide with
  changes in one, two, or all three" of variance, task sensitivity and a
  local learning coefficient. As events:
  1. a direction that was weak becomes informative;
  2. a local degeneracy changes (a learning coefficient, a rank, a
     stability eigenvalue);
  3. the distinction becomes decodable or is used.
  A41 §8 predicts that the first can precede the others (quoted below).
- **A taxonomy of "weak".** A41 §1 and §4: "weak" needs a spectrum, and a
  model has several ("A direction can be small in one of these geometries
  and extremely important in another"): representation variance, a weight matrix's singular values,
  the Hessian and the Fisher, which can rank directions in opposite orders
  ([CLAIM-tmppkdjz](../claims.d/CLAIM-tmppkdjz.md); the senses are sorted in [TERM-tmpnxjq4](../terms.d/TERM-tmpnxjq4.md)).

On A41's sharpening the question is open until it is answered for a
stated spectrum.

## Candidate answers in the exchange

- **A41's prediction.** "The developmental onset of a new semantic
  distinction may first appear as a change in task sensitivity within a
  spectrally quiet subspace, potentially preceding a visible change in
  variance or an identifiable transition in local singularity structure."
  The recent work A41 found is Staats et al. (held: [THEORY-420](../theory.d/THEORY-420.md)), Acharya
  et al. ([LIT-tmp0gbj6](../literature.d/LIT-tmp0gbj6.md)), Song et al. ([LIT-tmp83hha](../literature.d/LIT-tmp83hha.md)) and Xu ([LIT-tmp4det7](../literature.d/LIT-tmp4det7.md)),
  the last three unread. None tracks a direction through learning toward
  a new distinction, so none answers the question. They show that small
  directions can matter at a checkpoint.
- **A42's mechanism.** A factored feature switched on just above its
  threshold has variance of order ε² and a gain in fit of order ε
  ([CLAIM-tmp9bp04](../claims.d/CLAIM-tmp9bp04.md)), so in that model events 1 and 2 coincide at s = λ.
  Its variance stays small after the stability change.
- **A43's three times** ([CLAIM-tmpl9zw4](../claims.d/CLAIM-tmpl9zw4.md)): encoded, stable, expressed. On
  this account event 1 can precede event 2 by any amount, and event 3
  lags event 2 by a delay that grows with how long the feature sat below
  threshold.
- **A measurement caution** ([CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)). A change in an estimated
  learning coefficient can be a sloppy direction coming into resolution
  rather than a change of stratum. Event 2 needs the estimate's dependence
  on its inverse temperature, not one value.

A proposed test is [LEAD-tmpfrw11](../leads.d/LEAD-tmpfrw11.md).

## What would count as an answer

For a stated spectrum, a tracked direction in a model whose new
distinction can be named, with the three events dated on one clock. The
answer is the order found, and whether it survives a change of
coordinates that leaves the function unchanged. A41 warns that
low-variance rankings can change under "harmless representation
reparameterizations".

## Note of 2026-11-21: Lau et al., read

A caution from the estimator's source (NOTE-tmp92pjh, THEORY-tmpousrw) on
reading a change in local learning-coefficient estimates as a transition:
the estimate is made at one inverse temperature, β* = 1/log n, with a
localizer of precision γ, and both set which directions count (on a
quadratic loss, Σ ½·te_i/(te_i + γ), t = n/log n); consistency is a
conjecture; and an unsettled sampler underestimates ("If the step size is
too low, the sampler may not equilibriate, leading to underestimation",
App. H). A change in the estimate over training is evidence of a change of
stratum only with the sampler settings fixed across checkpoints, settling
checked, and β and γ varied (LEAD-tmpfrw11, CLAIM-tmpcg4uu). The paper
itself has no dynamical content beyond its Outlook.
