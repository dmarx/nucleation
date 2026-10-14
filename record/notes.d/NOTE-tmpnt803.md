---
status: Read
paper: LIT-234
title: 'Balestriero, Bottou & LeCun — regularization effects are class dependent'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2204.03632v2, 8 April 2022, 21 pp.),
    text extracted with pdftotext: abstract, §§1–3, appendix A (A.1–A.2),
    the proof of Theorem 1 (appendix B) and every figure caption.
    Figures 4 and 6 were rendered as images and read off by eye, since
    the per-class curves carry the paper's numbers. The NeurIPS 2022
    proceedings version, which the owner linked, was not read; it may
    differ from this preprint.
date: '2026-10-14'
summary: >-
  On ImageNet with ResNet-50, making random crop stronger or changing
  weight decay raises mean test accuracy while some classes lose 20
  points or more, and the shift survives a frozen-backbone transfer to
  iNaturalist. The evidence is per-class curves for hand-picked classes
  over 10–20 runs, plus a Welch test with no multiple-comparison
  correction. Theorem 1 says only that a fit to augmentations that are
  not label-preserving cannot equal the true function.
---
<!-- inactive-ok-file: THEORY-228 THEORY-005 — Proposed; the spectral accounts the seed linked this paper to, which it does not bear on directly -->

# NOTE-tmpnt803: Balestriero, Bottou & LeCun — regularization effects are class dependent

## Contribution

The paper measures per-class test accuracy across a sweep of
regularization strength, with 10 to 20 training runs at each setting. It
finds that the setting best on average is not best for every class. Some
classes fall steeply as the average rises. This holds for random crop
and for weight decay, which uses no domain knowledge. It also holds for
the linear-probe accuracy of a frozen backbone on another dataset.
Before it, the class-dependence of augmentation's label-preservation was
anecdotal. After it, the effect is shown on standard ImageNet models,
for a few named classes.

## Key insight

Choosing regularization by cross-validated average accuracy is
structural risk minimization over a single complexity knob. The paper's
Fig. 1 puts the point in terms of per-class risk curves: they have
different minima, so the average's minimum can sit where some class's
curve is high. Regularization buys variance reduction with bias, and
nothing makes the bias fall evenly across classes.

## Assumptions

- **Setting.** ImageNet-1k with the official PyTorch ResNet-50. Fig. 12
  repeats the weight-decay sweep on DenseNet-121, and Figs. 2–3 use six
  pretrained torchvision models. Transfer is to iNaturalist (10,000
  classes) with frozen weights and a retrained linear classifier.
- **Theorem 1 (§2.1, appendix B).** ℓ2 loss. The model reaches zero
  training error on the augmented set. The proof adds three things the
  statement does not mention: the transformations form a group
  (T₋α inverts Tα, T₀ = id, Tα∘Tβ = Tα+β), the sampling density is
  constant, and the model predicts one constant on each orbit.
- **"Bias" means accuracy loss on a class.** The paper uses "bias" both
  for the estimator's bias and for one class losing accuracy to the
  others. The experiments measure only the second.

## Key results

- **Theorem 1.** If Σ E_α‖y − f*(Tα(x))‖² > 0 (the augmentation leaves the
  level set of f*) and Σ E_α‖y − fθ(Tα(x))‖² = 0 (zero training error),
  then fθ is biased. *Holds when:* the group, constant-density and
  constant-on-orbit conditions above. It shows that the fit is not f*. It
  does not show that the error lands unevenly across classes, which is
  the paper's claim.
- **Label preservation is class-dependent (§2.2, Figs. 2–3, 10–11).**
  Pretrained models are evaluated on cropped test images. Some classes
  stay recognisable down to an 8% crop. For others accuracy starts
  falling at about 50%, while the average turns at about 30%. Six
  architectures agree on which classes are fragile (Fig. 3). CutOut and
  colour jitter behave the same way. Figs. 10 and 11 are captioned
  identically ("color jittering"); one of them is presumably CutOut.
- **Sweep over the random-crop lower bound τ (§2.3, Fig. 4).** ResNet-50
  with τ from 100% to 8%, averaged over 20 runs. Mean test accuracy rises
  from about 70% to about 76%. "Academic gown" falls from about 62% to
  40%. "Barn spider" falls from about 68% to 46%, the abstract's example.
  "Sunglass" and "Windsor tie" also fall, each paired with a class that
  rises.
- **Significance test (§2.3).** A one-sided Welch test per class compares
  no augmentation with τ = 8%. "There is enough evidence to reject H0 with
  95% confidence for 4.4% of all the classes, and with 99% confidence for
  2.1%." No correction for 1,000 tests is made. A class whose true mean is
  unchanged rejects at the nominal 5% or 1%. So 4.4% at the 5% level is
  not, alone, more than chance would give. The 2.1% at the 1% level is
  about twice chance. H₀ is printed as E[Acc(X)] < E[Acc(X_DA)], the
  reverse of the hypothesis the sentence before it describes.
- **Weight decay (§2.4, Figs. 5, 12).** ResNet-50 with horizontal flip
  only, varying γ over 10 runs: "different classes have different test
  accuracy sensitivities to variations in γ". No class-level numbers
  are given in the text, and the figure is read here only as showing
  divergent curves.
- **Transfer (§2.5, Fig. 6).** ImageNet pretraining with varying τ,
  frozen backbone, linear probe on iNaturalist, 10 runs. Average accuracy
  is flat at about 37–40%. Selected classes move by 30–60 points in
  opposite directions. The abstract says that class [#8889](https://github.com/dmarx/nucleation/issues/8889) falls "from 70%
  to 30% … when introducing random crop". In Fig. 6 that class rises
  from about 35% at τ = 100% to about 65–70% at τ ≈ 40–50%, then falls
  back to 35–40% at τ = 8%. The drop is from moderate to strong
  cropping, not from no cropping to cropping.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | How much of an image a crop must keep to stay recognisable varies widely across ImageNet classes, and different architectures agree on which classes are fragile | strong | pretrained models on cropped test images, Figs. 2–3, 10–11 |
| C2 | Strengthening random crop raises mean ImageNet accuracy while some classes lose 20 points or more | moderate | Fig. 4, 20 runs, hand-picked classes; Welch test uncorrected |
| C3 | Weight decay, an uninformed regularizer, also moves per-class accuracy in opposite directions | weak | Fig. 5 and Fig. 12 curves, 10 runs, no numbers or test |
| C4 | The class-dependence of pretraining augmentation persists through a frozen-backbone transfer | moderate | Fig. 6, 10 runs, four pairs of selected classes |
| C5 | Training to zero error on augmentations that are not label-preserving yields a model biased away from f* | strong (but narrow) | Theorem 1, appendix B |
| C6 | Regularization's bias is unevenly distributed across classes by necessity | weak | asserted from C1–C4; no theorem connects Theorem 1 to classes |

## Concepts

- **Label-preserving augmentation.** Tα with f*(Tα(x)) = f*(x), i.e. one
  that keeps x on its level set of the target. The paper's measure of it
  is the accuracy of pretrained models on transformed test images.
- **Class-dependent bias.** A regularizer's effect on the accuracy of one
  class, when that effect differs in sign or size from its effect on the
  average.
- **Structural risk minimization.** Appendix A.1 casts cross-validating
  the weight-decay coefficient as choosing among nested function classes
  {‖θ‖² ≤ β}, via the Lagrangian equivalence of (P1) and (P2). It adds,
  citing others, that augmentations can be cast as explicit Tikhonov-style
  regularizers.

## Connections

The paper sits in Balestriero's line on augmentation as implicit
regularization (LeJeune et al. 2019; Balestriero, Misra & LeCun 2022,
cited for casting DA as explicit regularizers). It cites Raghunathan et
al. (2020) for the harm label-preserving augmentation can do to minimum-norm
interpolants, and Xu et al. (2020) for i.i.d. augmentation amplifying
dataset bias. It does not engage with the worst-group literature (group
DRO, spurious correlations), which measures the same kind of per-group
regression.

## Bearing on the record

- **No THEORY, CLAIM or QUESTION in this record cites the paper**, and
  none holds a claim about class-dependent effects of regularization.
- **What it would support is ML practice.** Tune or report regularization
  per class or worst class, not only on average. That is an instruction
  for machine-learning practice and belongs in the Anthology of the SOTA.
  The LIT's `anthology-candidate` flag is right. No THEORY is filed here.
  The one non-practical finding, that per-class risk curves under one
  complexity knob need not share a minimum, is a standard bias–variance
  point the paper illustrates rather than establishes.
- **For the spectral reading of self-supervised learning** ([THEORY-228](../theory.d/THEORY-228.md),
  [THEORY-005](../theory.d/THEORY-005.md), [THEORY-007](../theory.d/THEORY-007.md)). The seed placed this paper under the
  *spectral approximation* heading through augmentation graphs. The
  paper has no graph, no spectrum and no self-supervised setting. Its
  only point of contact is C1. Under [THEORY-228](../theory.d/THEORY-228.md)'s bound, the
  probability that augmentation changes the label is the quantity C1
  measures, and C1 shows it is far from uniform across classes. That
  bears on how [THEORY-228](../theory.d/THEORY-228.md)'s bound distributes its error across classes.
  It is a remark, not a result the paper draws.

## Limitations

- **Selected classes.** Figs. 4–6 show four pairs of classes each,
  chosen to illustrate divergence. The paper does not report how
  many classes fall, or by how much, except through the uncorrected test.
- **Noise floor.** ImageNet has 50 validation images per class, so one
  image moves a class's accuracy by 2 points. Averaging over 10–20 runs
  reduces training noise, not the sampling noise of the evaluation set.
  The test is run on training runs, so it does not account for the
  second.
- **The theorem does not reach the experiments.** Theorem 1 needs zero
  training error on all augmentations and a group of transformations.
  Random crop is not a group. It says the fit differs from f*, not
  which classes pay for it.
- **One weight-decay figure without numbers.** C3, the claim the abstract
  calls "even more surprising", is the least documented.
- **The authors' conclusion.** "Designing novel regularizers without
  class-dependent bias remains an open research question." The paper
  proposes none.

## Open questions

- How many ImageNet classes lose significantly under standard
  augmentation once evaluation-set noise and multiplicity are accounted
  for? A per-class bootstrap over validation images, with a
  false-discovery correction, would settle it.
- Is the weight-decay effect the same phenomenon as the augmentation
  effect, or class-frequency or difficulty effects of a smaller
  effective capacity? Correlating each class's weight-decay sensitivity
  with its crop fragility (C1) would tell them apart.
