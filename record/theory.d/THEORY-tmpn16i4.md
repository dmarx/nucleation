---
status: Proposed
promote_when: >-
  The step that is argued and not shown, that Blackwell-equivalent
  representations can carry different stitching penalties, is measured: two
  representations, each an invertible function of the other (the paper's
  own case is a spatial permutation of a layer's activations), stitched
  into the same top network under the paper's protocol (1×1 convolutional
  stitcher, trained on the task's training set, penalty on its test set),
  with the difference in penalty larger than the spread across stitching
  seeds and across two top networks. Or an independent published treatment
  that relates the stitching penalty to the comparison of experiments, or
  to a usable-information order, and reaches the same relation. It is
  refuted by a step of the derivation shown wrong, or by the stitching
  order shown, for the paper's map class, to be invariant under every
  invertible transformation of the representation. More experiments in
  which a better-trained representation lowers a weaker network's error
  cannot settle it, since they are compatible with both readings.
title: "A task-loss stitching penalty compares representations in one decision problem, through a fixed top network and a restricted map class, so it is not Blackwell's order: representations that are functions of each other can stitch differently, and a negative penalty shows the fitted map did not reproduce the layers it replaced"
version: 1
tags:
- representation-learning
- mathematical-statistics
date: '2026-10-09'
source:
- LIT-tmpyp4ka
- LIT-781
- LIT-363
summary: >-
  Bansal, Nakkiran & Barak (2021), [LIT-tmpyp4ka](../literature.d/LIT-tmpyp4ka.md), define the stitching
  penalty L_ℓ(r; A) − L(A), with L_ℓ(r; A) the least task loss of A's top
  layers fed r through a map from a simple family S, and use it to call
  one representation better than another. Read against Blackwell (1953),
  [LIT-781](../literature.d/LIT-781.md), and [THEORY-156](THEORY-156.md), that ordering is one coordinate of the
  comparison of experiments with the decision rules cut down to A's head
  composed with S. It is not invariant under Blackwell equivalence, which
  the paper intends, and it meets Blackwell's order only where the fitted
  map reproduces the replaced layers exactly. The relations are this
  record's derivations from the paper's definitions, not the paper's.
supports:
- CLAIM-tmpkx2sz
---
<!-- inactive-ok-file: THEORY-156 THEORY-008 THEORY-112 — Proposed; the order this one is compared with, and accounts named in What this does not say, cited as readings, not as settled -->

# THEORY-tmpn16i4: A task-loss stitching penalty compares representations in one decision problem, through a fixed top network and a restricted map class, so it is not Blackwell's order: representations that are functions of each other can stitch differently, and a negative penalty shows the fitted map did not reproduce the layers it replaced

## Source

- Bansal, Nakkiran & Barak (2021), [LIT-tmpyp4ka](../literature.d/LIT-tmpyp4ka.md), §§2–3 (eq. 1, the
  definition of the penalty, and the invariance and asymmetry arguments)
  and §6 with Figs. 2C and 3B–C, as read in [NOTE-tmpmiadh](../notes.d/NOTE-tmpmiadh.md).
- Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), as read in [NOTE-595](../notes.d/NOTE-595.md) and stated in
  [THEORY-156](THEORY-156.md), for the order compared against.
- Lenc & Vedaldi (2014), [LIT-363](../literature.d/LIT-363.md), as read in [NOTE-309](../notes.d/NOTE-309.md), for the identity
  stitch that fails between linearly equivalent networks.

## What was actually shown

**The paper's definition.** For a top network A, a layer ℓ, a candidate
representation r and a family S of "simple" maps,
L_ℓ(r; A) = inf over s ∈ S of L(A_{>ℓ} ∘ s ∘ r), and the stitching penalty
is L_ℓ(r; A) − L(A) (eq. 1). L is the test error of A's own task. In
practice s is a 1×1 convolution between two BatchNorms, trained on the
task's training set. A negative penalty is read as r being better than A's
first ℓ layers, and §6 builds "more is better" on such readings: a bottom
trained on 25K CIFAR-10 samples lowers a 10K network's error by up to
about 22 points (Fig. 2C).

**The comparison.** Treat a representation r as an experiment about the
label Y: for each label y, the law of r(X) given Y = y. CIFAR-10 and
ImageNet have finitely many labels, so [THEORY-156](THEORY-156.md) applies. There, r is at
least as informative as r′ exactly when r attains, in every decision
problem with bounded loss, every risk r′ attains, and exactly when r′ is a
garbling of r. Four relations follow from the definitions. They are this
record's derivations, not the paper's, and each is elementary.

1. **One problem, not all.** The penalty uses one loss. Blackwell's order
   quantifies over every decision problem, and comparison by one problem
   is strictly weaker: two experiments can have the same, or ordered,
   Bayes risk for the task loss and be incomparable. So a negative
   penalty does not give r ⊒ A_{≤ℓ} in Blackwell's order.
2. **Restricted rules, so upper bounds.** The rules the stitched network
   can use are A_{>ℓ} ∘ s with s ∈ S, not every measurable rule on r. Its
   loss bounds r's best attainable risk for that problem from above, and
   L(A) does the same for A's first ℓ layers. Comparing two upper bounds
   orders neither best risk. A positive penalty therefore does not show
   that r carries less task-relevant information than A's layers; it may
   only be unusable by A's head through S.
3. **Not invariant under Blackwell equivalence.** If r′ = g ∘ r with g
   invertible, each is a function of the other, and they are equivalent in
   Blackwell's order. Their penalties need not agree when g is not in S.
   The paper says so and wants it (§3): because a 1×1 stitcher is weaker
   than general orthogonal maps, "model stitching can predict that
   shuffling pixels leads to a 'worse' representation", although a pixel
   shuffle loses nothing. Lenc and Vedaldi's identity stitch between
   networks that a learned linear map makes interchangeable gives more than
   99% error ([LIT-363](../literature.d/LIT-363.md), Table 4): with S = {identity}, linear equivalence
   is invisible.
4. **Where the two orders meet.** If some s ∈ S gave s ∘ r = A_{≤ℓ} on the
   input distribution, then given each label A_{≤ℓ}(X) is s applied to
   r(X), so A's layers are a garbling of r and r dominates them in
   Blackwell's order, and the stitched network is A, with penalty zero.
   That is Lenc and Vedaldi's regression form of stitching
   (φ′ ≈ E φ), and it is the form whose success certifies a
   direction of Blackwell sufficiency, restricted to garblings in S. A
   negative penalty, the evidence for "more is better", shows the
   opposite of reproduction: the stitched network beats A, so s ∘ r is
   not A_{≤ℓ}. What the fitted map found is an input on which A's head
   does better than on its own layers.

**What could have come out otherwise.** Relations 1, 2 and 4 are
consequences of definitions and cannot fail except by an error in a step.
Relation 3 is a possibility the definitions allow, and the paper argues
that it occurs; it has not been measured. The pixel-shuffle experiment the
paper describes, and does not run, is the test that `promote_when` asks for.

## What this does not say

- **Not that stitching is uninformative.** A low penalty between two
  networks shows that, for that task, one network's head can use the
  other's layers through a cheap map. That is a real and useful fact about
  interchangeability, and the paper's comparisons with CKA rest on it.
- **Not that "more is better" is false.** A 25K-sample representation that
  lowers a 10K network's error is better for that task through that head.
  The claim here is about what kind of ordering that is, not whether it
  holds.
- **Not that a stitching order could never recover Blackwell's.** Stitching
  over every decision problem, with an unrestricted decoder, would compare
  best risks problem by problem, which is Blackwell's order ([THEORY-156](THEORY-156.md)).
  The paper's protocol fixes the problem and restricts the decoder; what
  happens between the two is not addressed here.
- **Not about information measures in general.** Kernel-based measures
  such as CKA, which [THEORY-008](THEORY-008.md) relates to linear readout, are a different
  comparison again; and invariance under the architecture's symmetry group
  ([THEORY-112](THEORY-112.md)) is a smaller class than Blackwell equivalence.
- **Not a measured result.** The paper reports no experiment that
  separates the two orders. The relations are derivations, and the one
  that needs a measurement is named in `promote_when`.
