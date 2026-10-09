---
status: Read
paper: 'LIT-tmpyp4ka'
title: 'Revisiting Model Stitching to Compare Neural Representations'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv v1 PDF (arXiv:2106.07682v1, 17 pp.): the
    abstract, §§1–8, the references, and Appendices A (A.1–A.4) and B
    (B.1–B.4). Text extracted with pdftotext. Figures 2–9 were read as
    rendered page images and their values estimated from the plots; the
    paper gives no tables of numbers except Table 1, which is qualitative.
    Then compared line by line with the NeurIPS 2021 camera-ready PDF from
    proceedings.neurips.cc (12 pp., main text and references). The
    camera-ready adds a paragraph on concurrent work by Csiszárik et al.,
    softens "a much better suited tool" to "can be a better suited tool
    ... in various scenarios", and adds a societal-impacts sentence; the
    sections, definitions, figures and the sign slip in §2 are otherwise
    unchanged. Its supplement was not fetched, so the appendices read are
    those of arXiv v1. Lenc and Vedaldi (LIT-363) was read earlier
    (NOTE-309); Kornblith et al.'s CKA paper and Csiszárik et al. were
    not read.
date: '2026-10-09'
summary: >-
  An empirical paper with no theorems. It defines the stitching penalty,
  the change in a top network's test error when its bottom ℓ layers are
  replaced by another representation through a trained 1×1 convolution, and
  uses it to show, in single runs mostly on CIFAR-10, that networks from
  different seeds, and supervised and self-supervised ImageNet networks,
  are interchangeable layer by layer where CKA calls them different, and
  that a bottom trained on more data improves a weaker top. The ordering
  it gives is by one task's loss through a fixed head and a restricted map
  class, which is not an ordering by information.
---
<!-- inactive-ok-file: THEORY-tmpn16i4 THEORY-112 THEORY-116 THEORY-156 THEORY-002 THEORY-008 CLAIM-125 CLAIM-050 CLAIM-106 — Proposed; cited as the accounts and claims this reading sits beside, not as settled -->

# NOTE-tmpmiadh: Revisiting Model Stitching to Compare Neural Representations

## Contribution

Lenc and Vedaldi ([LIT-363](../literature.d/LIT-363.md)) introduced stitching layers to test whether two
networks' features are equivalent up to a learned linear map. This paper
turns that test into a general-purpose measurement. It defines a
task-relative, asymmetric stitching penalty and argues that it shows what
CKA cannot: two representations can be interchangeable for the task while
CKA calls them far apart, and one representation can be *better* than
another, which a symmetric similarity cannot say. It then reports three
empirical regularities: networks trained from different seeds stitch at
every layer (stitching connectivity); different training methods yield
early layers that stitch into each other; and representations trained with
more data, and near the top with more width or training time, improve a
weaker network when plugged into it.

## Key insight

Ask not how similar two representations are, but whether one can stand in
for the other: replace the bottom of a trained network by the candidate
representation, allow only a cheap trained adapter between them, and
measure the change in the network's own loss. The answer is in the task's
units, and it can be directional: r may replace A's layers when A's layers
cannot replace r.

## Assumptions

- **The stitching family is "simple".** S is a 1×1 convolution with a
  BatchNorm before and after it (§2, App. A.4), or a 768×768 token-wise
  linear map for the ViT. Simplicity is argued, not defined. The control
  is a randomly initialised bottom network, whose penalty rises to about
  34 points (CIFAR-10) and about 45 (ImageNet) at the deepest layers, but
  is near zero for the first fifth of the layers (Fig. 2A–B, Fig. 5).
- **The infimum is a training run.** L_ℓ(r; A) = inf over s ∈ S of
  L(A_{>ℓ} ∘ s ∘ r) (eq. 1) is approximated by fitting s with Adam, cosine
  decay, learning rate 0.001, on the task's training set; the penalty is
  measured on its test set. So the measured penalty mixes approximation,
  optimisation and generalisation.
- **The top network is fixed.** Only s is trained. A_{>ℓ} is A's own
  upper network, unchanged.
- **One task.** The loss is the test error of the task A was trained for
  (CIFAR-10 or ImageNet classification). The authors say so: "model
  stitching depends on the downstream task" (§3).
- **Mostly same architecture.** r = B_{≤ℓ} for a B of A's architecture,
  except in the width experiment, where the channel counts differ. Stitching
  is between ResNet blocks only.
- **Setting.** CIFAR-10 with ResNet-18 (64 first-layer filters) unless
  stated; ImageNet with ResNet-50, using published PyTorch, VISSL and DINO
  checkpoints; a ViT trained on CIFAR-5m and stitched on CIFAR-10. The
  CIFAR networks are trained with random crops and horizontal flips.

## Key results

All values are read off plots; none is tabulated in the paper.

- **Definition of the penalty (§2).** Penalty = L_ℓ(r; A) − L(A). The text
  then says: "If the penalty is non-negative, then we say that the
  representation r is at least as good as the first ℓ layers of A." With a
  loss, a non-negative penalty means r does no better; the intended
  condition must be non-positive. The slip is in both arXiv v1 and the
  camera-ready. The figures use the right sign: "better representation
  improves performance" is plotted as a negative penalty (Fig. 2C).
- **Table 1 (qualitative).** CKA: "varies (can be 0)" for different
  initialisations, "0.35–0.9" for self-supervision, "far (can be 0 for
  data, 0.7 for width)". Stitching: "close (up to 3% error)", "close (up
  to 5% error)", "better".
- **Stitching connectivity (Fig. 2A, §4).** For ViT, ResNet-18 at 0.5×,
  1× and 2× width, ResNet-164, Myrtle-CNN, and ResNet-18 on disjoint
  training sets, the penalty stays between about −1 and +5 points at every
  layer; the ViT is the largest, about 5 at mid depth. One pair of seeds
  per architecture. Definition 1 ("low penalty", "test loss comparable to
  A") and Conjecture 2 ("for natural architectures and data-distributions
  ... stitching-connected") are stated informally.
- **Self-supervised vs supervised (Fig. 2B, §5; Fig. 6, App. B.2.2).**
  SwAV and DINO bottoms into a supervised ResNet-50: penalty about 0–3
  points at all layers. SimCLR: rising to about 8.5 near the top; SimCLR's
  own accuracy is 68.8% against about 75% for the others, so near the top
  this is mostly the gap between the two base models. On CIFAR-10, SimCLR
  and supervised ResNet-18s stitch in both directions within about 3
  points, the same range as two supervised seeds, while their CKA falls to
  0.35 at layer 2.
- **Label distribution (Fig. 3A).** Bottoms trained on Object vs Animal
  labels or with 10% or 50% label noise, into a standard top: within about
  3 points up to the middle of the network, then about 12–23 points at the
  top. With 100% random labels: about 8 points at a quarter of the depth,
  55 at about 0.35, 80 at the top.
- **Samples (Fig. 2C).** Top trained on 10K CIFAR-10 samples (error
  33.66%). A 25K bottom lowers the error from about 15% of the depth on,
  by about 5 points at mid depth and about 22 at the top. A 5K bottom
  raises it by about 15–18 points from 40% of the depth on. The 10K
  bottom itself, which should be the baseline, wanders from +2 to about −7
  points; the paper does not say whether it is the top network's own
  layers or a second 10K network.
- **Training time (Fig. 3B).** Top at epoch 80 (error 8.59%). The epoch-160
  bottom is about +0.5 points at shallow layers and about −0.3 to −0.8 only
  from 60% of the depth on. The epoch-40 bottom rises to about +4.7 at the
  top. The text's "representations improve in a manner that is compatible"
  rests on that last-layer gap of under one point.
- **Width (Fig. 3C, §6).** Top at 0.25× width (error 8.56%). The text lists
  {0.25×, 1×, 2×}; the figure also has 0.125×. The 2× bottom is about +0.5
  to +1 points through 60% of the depth and about −0.8 only after that.
  The 1× bottom is *worse* than the 0.25× self-stitch at mid depth (about
  +2 to +3). "Can be stitched to those with lower width and improve
  performance, but not vice versa": the reverse direction is not plotted.
- **Kernel size (App. B.1, Fig. 4).** Three unlabelled curves of stitched
  test error against kernel sizes 1–9; one gets worse with larger kernels.
  The text calls the effect "minimal".
- **Fine-tuning (App. B.3, Fig. 8).** With a random ResNet-164 bottom,
  retraining the whole top gives a lower penalty (about 9.5–15) than
  stitching (about 14–18), so fine-tuning flatters a random representation
  more. The figure is captioned "More is similar with CKA?", a copy of
  Fig. 7's caption, and its x-axis, labelled "fraction", runs 5 to 25.
- **Freeze training (§6, App. B.4, Fig. 9).** Layers whose penalty is near
  zero at 5K samples are frozen and the rest trained on 50K: final error
  about 0.11 against about 0.08 for full training. The main text says "the
  first three, and the last three layers ... within 2%"; the appendix says
  layers {0, 1} and {8, 9, 11}, five layers, and "up to ≈ 3%". It also
  refers to a top trained on the full dataset in Fig. 2C, whose top was
  trained on 10K.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Stitching penalty is a better tool than CKA for comparing representations | argument, with examples | §3: the spurious-coordinates example (a construction), the pixel-shuffle example (an argument), and Table 1 |
| C2 | Two networks of one architecture and data distribution, trained from different seeds, are stitching-connected | moderate (experiment), stated as an informal conjecture | Fig. 2A, one pair per architecture, six architectures, CIFAR-10 only |
| C3 | Supervised and self-supervised networks learn representations that stitch at all layers | moderate (experiment) | Fig. 2B (ImageNet, three SSL methods) and Fig. 6 (CIFAR-10, SimCLR); single runs |
| C4 | Early layers are insensitive to label quality; late layers are not | moderate (experiment) | Fig. 3A |
| C5 | Representations trained with more data are better versions of the same representation | moderate for samples | Fig. 2C: 25K into 10K lowers error from shallow layers on |
| C6 | The same holds for width and training time | weak | Fig. 3B–C: improvement under one point, only in the top 40% of layers; mid-layer penalties are positive |
| C7 | Stitching is asymmetric: wider into narrower helps "but not vice versa" | not supported here | no figure shows the reverse direction |
| C8 | Layers have their own sample complexity, so some can be frozen early | weak | §6 and App. B.4 disagree on which layers and how close |
| C9 | The stitching layer is not doing the learning | moderate for deep layers, weak for shallow ones | random-bottom control, Fig. 2A–B, Fig. 5: high penalty deep, near zero in the first fifth of layers |

## Concepts

- **stitching penalty** — L_ℓ(r; A) − L(A), with L_ℓ(r; A) the least loss
  of A's top layers fed r through some s ∈ S; measured with a trained s.
- **stitching family S** — the allowed adapters; it is where invariances
  are chosen ("we can explicitly ensure invariance under any given family
  of transformations by adding it to the stitching layer", §3).
- **stitching-connected** — every stitched model S_i, i = 0, …, L, joining
  B's first i layers to A's rest, has test loss "comparable to A"
  (Definition 1). S_0 = A and S_L = B, so the sequence is a discrete
  path between the networks.
- **"Anna Karenina" scenario** — all successful models learn roughly the
  same internal representations, and better models learn better versions
  of them; its opposite is "snowflakes".
- **"more is better"** — r trained with more resources should lower A's
  error when plugged in, i.e. have a negative penalty.

## Connections

- **Lenc and Vedaldi ([LIT-363](../literature.d/LIT-363.md), [NOTE-309](NOTE-309.md)).** The source of the stitching
  layer. [NOTE-309](NOTE-309.md) found that the identity stitch fails (> 99% error) and
  that their deep-layer equivalence is judged by recovered task accuracy
  through a learned layer. This paper keeps the second feature, makes it
  the definition, and uses a much smaller adapter (1×1 rather than
  m × m × D filters). Lenc and Vedaldi's ImageNet/Places stitching found
  Conv5 not interchangeable; this paper finds ResNets interchangeable at
  every layer, on CIFAR-10 and between ImageNet training methods.
- **CKA and the kernel view ([THEORY-008](../theory.d/THEORY-008.md), [THEORY-002](../theory.d/THEORY-002.md)).** [THEORY-008](../theory.d/THEORY-008.md) holds
  that what a regularised linear readout can decode is a function of the
  normalised kernel, and that CKA averages readout agreement. Stitching
  departs from that view in two ways the paper names: it is nonlinear in
  what it decodes (A's whole top is the decoder), and it is tied to one
  task. The paper's spurious-coordinates example, where CKA drops but the
  representation is unchanged in use, is the kind of case where the two
  part.
- **Mode connectivity ([THEORY-112](../theory.d/THEORY-112.md), [THEORY-116](../theory.d/THEORY-116.md)).** The paper calls
  stitching connectivity "complementary to mode connectivity": a discrete
  path whose intermediate models each share all but one layer with an
  endpoint. [THEORY-112](../theory.d/THEORY-112.md) says the linear barrier between seeds largely
  vanishes once the architecture's symmetries are factored out. Stitching
  connectivity is consistent with that, and weaker: the 1×1 convolution is
  a general linear map per layer, a larger group than permutations, and it
  is fitted to the task loss, not to the weights. [THEORY-116](../theory.d/THEORY-116.md) reads a
  surviving barrier as a difference in mechanism; the label-noise result
  here, where early layers stitch and late layers do not, is the same
  shape of finding by another measure, and it is my connection, not the
  paper's.
- **Platonic representation hypothesis ([LIT-302](../literature.d/LIT-302.md), [NOTE-286](NOTE-286.md)).** [NOTE-286](NOTE-286.md)
  lists "model stitching" first among the convergence evidence Huh et al.
  survey. This paper is that evidence for vision, at one architecture: it
  shows interchangeability up to a learned linear map for one task, not
  convergence of kernels.
- **Concurrent work.** The camera-ready names Csiszárik et al. (NeurIPS
  2021), which varies the stitching layer, including a sparsity penalty
  (not read). It cites it as NeurIPS volume 35; the 2021 volume is 34.

## Bearing on the record

- **It produces [THEORY-tmpn16i4](../theory.d/THEORY-tmpn16i4.md).** The paper's "more is better" is an
  ordering of representations, and the record holds Blackwell's order of
  experiments ([THEORY-156](../theory.d/THEORY-156.md)). The two are different orders. Taking the
  representation r(X) as an experiment about the label Y:
  - the penalty is one decision problem, the task's loss, where Blackwell's
    order quantifies over all of them;
  - the decision rules allowed are A_{>ℓ} ∘ s with s ∈ S, not every rule,
    so the stitched loss bounds r's best attainable risk from above and
    L(A) bounds that of A's layers from above, and comparing two upper
    bounds orders neither best risk;
  - representations that are Blackwell-equivalent, each a function of the
    other, can stitch differently. The paper wants this: its pixel-shuffle
    argument (§3) says a 1×1 stitcher "can predict that shuffling pixels
    leads to a 'worse' representation", though a shuffle loses nothing;
  - the one point where they meet is exact reproduction: if some s ∈ S had
    s ∘ r = A_{≤ℓ}, A's layers would be a function of r, so r would
    dominate them in Blackwell's order and the penalty would be zero. A
    negative penalty, the paper's evidence for "more is better", therefore
    shows that s ∘ r did not reproduce A_{≤ℓ}.
  These steps are my derivations from the paper's definitions and
  [THEORY-156](../theory.d/THEORY-156.md), not the paper's.
- **[CLAIM-125](../claims.d/CLAIM-125.md).** Stitching is a learned, directed transport between
  representations, judged by what a fixed downstream decision-maker can do
  with it. That is the shape of the comparison [CLAIM-125](../claims.d/CLAIM-125.md) calls open. The
  paper does not settle it: its judgement is by one decision problem,
  through a fixed head, with the map trained on the problem itself, and it
  gives no characterisation, only measurements. It is prior art for the
  practice of comparing representations by decision performance, and it
  does not meet that claim's `defeated_if`.
- **[CLAIM-050](../claims.d/CLAIM-050.md).** It is an ML counterpart of "fidelity relative to the
  decisions the receiver must make", for a single decision. It also shows
  what is lost by fixing the decision: Blackwell-equivalent representations
  can be judged different.
- **[CLAIM-106](../claims.d/CLAIM-106.md).** Its penalty is graded and directional, and equivalence
  (zero penalty both ways) is a special case, which is that claim's
  structure in a different domain. The paper's evidence for direction is
  thin (C7).
- **ML practice.** It recommends stitching as a diagnostic ("we hope that
  model stitching will become a part of the standard diagnostic repertoire
  of the deep learning community") and suggests freezing layers early as a
  training speed-up. Both are practice; the anthology is the place for
  them, hence `anthology-candidate`.

## Limitations

- **No theory.** "Formal" in the paper means a definition. Definition 1 and
  Conjecture 2 are informal, and no property of the penalty is proved: not
  that it is a preorder, not transitivity, not invariance under any group.
- **Single runs, values from plots.** No seeds, no error bars, no tables.
  Differences of a point or two, which carry the width and training-time
  claims, are within what the 10K self-stitch baseline wanders (Fig. 2C).
- **Mostly one architecture and one dataset.** ResNet-18 on CIFAR-10 for
  everything in §§5–6 except the ImageNet SSL comparison. Vision only, as
  the authors say.
- **The comparison is relative to a fixed top.** Every "more is better"
  comparison is r against A's own layers through A's head. Chains such as
  25K > 10K > 5K are each against the 10K head; whether the order changes
  with the head is not tested.
- **The endpoints are trivial.** Near the top of the network the stitched
  model is nearly the bottom network, so the penalty there is close to the
  difference between the two base models' errors. The informative points
  are the middle layers, where for width and training time the sign goes
  the other way.
- **The random-network control fails at shallow layers.** A random bottom
  stitches with near-zero penalty in the first fifth of the layers (the
  paper reads this as early layers being near-random), so low early-layer
  penalties carry little information about learned structure.
- **The sign slip in §2** and the B.4/§6 and Fig. 8 inconsistencies noted
  above.

## Open questions

- Is the stitching order, for a fixed task, a preorder, and does it depend
  on the choice of top network? A test across several heads would say.
- Does stitching connectivity survive restriction of S to the
  architecture's symmetry group (permutations, or orthogonal maps for a
  transformer's residual stream)? That would connect it to [THEORY-112](../theory.d/THEORY-112.md)'s
  alignment results.
- If stitching is repeated over a family of tasks on one input
  distribution, does the resulting order approach Blackwell's order on
  some latent variable? Nothing here bears on it, since every comparison
  is one task.
