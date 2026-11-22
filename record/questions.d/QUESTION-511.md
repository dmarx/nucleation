---
number: 511
status: Open
formerly:
- QUESTION-tmp82zpm
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

<!-- inactive-ok-file: TERM-tmpf5ymd — Proposed; filed 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-835 CLAIM-807 CLAIM-828 CLAIM-812 TERM-137 — Proposed or new, filed with this question -->
<!-- inactive-ok-file: THEORY-tmpthmd7 THEORY-tmpu3iio THEORY-tmpklef6 THEORY-tmpr9w2r LIT-tmp9yy1o LIT-tmpgptvp — Proposed or Deferred; the readings of 2026-11-21, and works registered from them -->
<!-- inactive-ok-file: THEORY-2157 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# QUESTION-511: Does recent work on the informativeness of small-eigenvalue subspaces during learning bear on the signature of a transition the exchange proposed, in which a previously weak direction becomes informative, a local degeneracy changes and a new distinction becomes independently decodable?

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
  ([CLAIM-835](../claims.d/CLAIM-835.md); the senses are sorted in [TERM-137](../terms.d/TERM-137.md)).

On A41's sharpening the question is open until it is answered for a
stated spectrum.

## Candidate answers in the exchange

- **A41's prediction.** "The developmental onset of a new semantic
  distinction may first appear as a change in task sensitivity within a
  spectrally quiet subspace, potentially preceding a visible change in
  variance or an identifiable transition in local singularity structure."
  The recent work A41 found is Staats et al. (held: [THEORY-420](../theory.d/THEORY-420.md)), Acharya
  et al. ([LIT-2959](../literature.d/LIT-2959.md)), Song et al. ([LIT-2973](../literature.d/LIT-2973.md)) and Xu ([LIT-2967](../literature.d/LIT-2967.md)),
  the last three read on 2026-11-21 (see the note below). None tracks a direction through learning toward
  a new distinction, so none answers the question. They show that small
  directions can matter at a checkpoint.
- **A42's mechanism.** A factored feature switched on just above its
  threshold has variance of order ε² and a gain in fit of order ε
  ([CLAIM-807](../claims.d/CLAIM-807.md)), so in that model events 1 and 2 coincide at s = λ.
  Its variance stays small after the stability change.
- **A43's three times** ([CLAIM-828](../claims.d/CLAIM-828.md)): encoded, stable, expressed. On
  this account event 1 can precede event 2 by any amount, and event 3
  lags event 2 by a delay that grows with how long the feature sat below
  threshold.
- **A measurement caution** ([CLAIM-812](../claims.d/CLAIM-812.md)). A change in an estimated
  learning coefficient can be a sloppy direction coming into resolution
  rather than a change of stratum. Event 2 needs the estimate's dependence
  on its inverse temperature, not one value.

A proposed test is [LEAD-207](../leads.d/LEAD-207.md).

## What would count as an answer

For a stated spectrum, a tracked direction in a model whose new
distinction can be named, with the three events dated on one clock. The
answer is the order found, and whether it survives a change of
coordinates that leaves the function unchanged. A41 warns that
low-variance rankings can change under "harmless representation
reparameterizations".

## Note of 2026-11-21: Lau et al., read

A caution from the estimator's source ([NOTE-2239](../notes.d/NOTE-2239.md), [THEORY-2157](../theory.d/THEORY-2157.md)) on
reading a change in local learning-coefficient estimates as a transition:
the estimate is made at one inverse temperature, β* = 1/log n, with a
localizer of precision γ, and both set which directions count (on a
quadratic loss, Σ ½·te_i/(te_i + γ), t = n/log n); consistency is a
conjecture; and an unsettled sampler underestimates ("If the step size is
too low, the sampler may not equilibriate, leading to underestimation",
App. H). A change in the estimate over training is evidence of a change of
stratum only with the sampler settings fixed across checkpoints, settling
checked, and β and γ varied ([LEAD-207](../leads.d/LEAD-207.md), [CLAIM-812](../claims.d/CLAIM-812.md)). The paper
itself has no dynamical content beyond its Outlook.

## Note of 2026-11-21: Song, Ahn & Yun, Xu, Acharya, Rimal & Dhakal, and Hoogland et al., read

The four readings leave the question open, and one tells against A41's
candidate answer.

- **None tracks a direction through training.** Xu ([THEORY-tmpu3iio](../theory.d/THEORY-tmpu3iio.md)) and
  Acharya et al. ([THEORY-tmpklef6](../theory.d/THEORY-tmpklef6.md)) use final checkpoints; Acharya et al.'s
  only trajectory is through depth ("Our layer-wise analysis is
  descriptive"). Song et al. ([THEORY-tmpthmd7](../theory.d/THEORY-tmpthmd7.md)) measure only training-loss
  descent and recompute the subspace at every step, so no direction is
  followed. Hoogland et al. ([THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)) date stages by the local
  learning coefficient, a scalar, not by any direction; they do date event
  2's kind of change against behaviour, at fixed sampler settings.
- **Quiet in one metric, loud in another.** Xu's bottom band is quiet in
  the logit metric but "holds on average 1.5 to 6.6 times its share of the
  directions in variance" at late residual states (App. D). So A41's
  "spectrally quiet subspace", read as low representation variance, does
  not fit Xu's directions, the work A41 cites for it; read as low
  amplification by the unembedding, it fits, and the question must say
  which. "Concepts Whisper" uses the phrase itself ("word-level semantics
  occupy the spectrally quiet subspace"), in that logit-metric sense.
- **A test the record could run.** Xu's suggested training origin, after
  Thrampoulidis ([LIT-tmp9yy1o](../literature.d/LIT-tmp9yy1o.md)) and Zhao et al. ([LIT-tmpgptvp](../literature.d/LIT-tmpgptvp.md)), places the
  distinctions among plausible candidates at the bottom of the spectrum as
  training proceeds; "Testing this origin would require tracking the
  organization during training" (§7). Pythia's public checkpoints, among
  Xu's ten models at their final step, would allow tracking the bottom
  band's consequence spectrum through training: a direction becoming
  informative, in a stated spectrum.
- **No inner product is intrinsic.** [THEORY-018](../theory.d/THEORY-018.md) holds that softmax
  training fixes the final representation only up to an invertible linear
  map. Xu's singular ranking and "equal length", and Acharya et al.'s
  energy fractions, are not invariant under h ↦ Ah, W ↦ WA⁻¹ ([THEORY-234](../theory.d/THEORY-234.md));
  Xu's quotient of metrics and its generalized eigenvectors are. This
  qualifies every reading here, and is the "harmless representation
  reparameterizations" caution above made exact: an answer must be stated
  in an invariant, or for a stipulated inner product.

Written as `bears_on` from Xu's and Hoogland et al.'s readings. No status
change.

## Note of 2026-11-22: a correction, at the owner's word

An earlier note here says Song, Ahn and Yun "measure only training-loss descent", and the relay behind it treated that as less than learning. The owner corrected both: "training loss falling is evidence that learning is happening. the capabilities are being measurably developed. … that's a measure of the learning that is happening, which is concretely the changes that are happening within the organization of the model's representational space". The relay also read the paper's "bulk subspace" in the owner's sense of "bulk". It is the paper's term for the many low-curvature directions, the bulk by count, where the owner's "bulk" is the dominant directions, the bulk by weight ([TERM-tmpf5ymd](../terms.d/TERM-tmpf5ymd.md)).

Read so, Song et al. bear on the owner's question more than the earlier note said. Projecting each update onto the dominant directions, the bulk by weight, stops training. Projecting onto the rest, the low-curvature directions that carry little of the operator's activity, trains as fast as SGD. So capability develops through the non-dominant directions. What the paper still does not do is follow one direction through training or say which distinctions it comes to carry. The note is the assistant's (Claude, in this session).

