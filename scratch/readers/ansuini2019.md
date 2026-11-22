# Reader notes: ansuini2019 (LIT-2998)

Ansuini, Laio, Macke & Zoccolan (2019), "Intrinsic dimension of data
representations in deep neural networks", NeurIPS 2019, arXiv:1905.12784.
Read 2026-11-22.

## Provenance and copies located
- **Read:** arXiv PDF, https://arxiv.org/pdf/1905.12784 (v2, 28 Oct 2019;
  footer "33rd Conference on Neural Information Processing Systems (NeurIPS
  2019), Vancouver, Canada"). Kind: authors' preprint on arXiv (lawful).
  HTTP 200, application/pdf, fetched 2026-11-22; text by pdftotext.
  Metadata checked on the arXiv API (export.arxiv.org); no email address
  sent anywhere.
- No other copy sought: the arXiv copy is the full paper with appendix.
- **Read:** everything, main text §§1–4 and Appendix A.1 (datasets,
  architectures, checkpoints, ID estimation, variability across classes and
  seeds), figure captions 1–9. **Skipped:** the figures' plotted values
  (text extraction only; numbers below are those stated in the text),
  the code repository (github.com/ansuini/IntrinsicDimDeep) and the
  figshare data, not opened.
- No neighbour or supplement read or quoted.

## Summary
The paper measures the global intrinsic dimension (ID) of the point cloud
that a set of images makes in each layer of trained CNNs, with the TwoNN
estimator (Facco et al. 2017, ref. [16]), and compares it with a PCA-based
linear count, with untrained networks, with a covariance-matched Gaussian,
and with networks trained on shuffled labels. Across 14 ImageNet networks
(AlexNet, 8 VGG, 5 ResNet) and a fine-tuned VGG-16, ID is far below layer
width, rises in early layers and then falls ("hunchback"), and the
last-hidden-layer ID on training data correlates with test accuracy across
architectures. The linear count is one to two orders of magnitude larger
and does not distinguish trained from random networks; the authors infer
that representations lie on low-dimensional, curved manifolds.

## Contribution
A systematic, layer-by-layer, many-architecture map of a nonlinear global
ID estimate in large CNNs, with controls (random weights, Gaussian surrogate,
luminance-perturbed and label-shuffled MNIST) that separate it from linear
dimension and tie it to training on learnable labels.

## Key results (section, verbatim)
1. **Estimator** (§2). μ_i = r_i(2)/r_i(1) "follows a Pareto distribution
   with parameter d + 1 on [1, +∞), f(μ_i|d) = d μ_i^−(d+1)", assuming
   "the density is constant on the scale of the distance between each point
   and its second nearest neighbor". Bias: "For larger IDs and finite
   sample size, the approach moderately underestimates the correct value
   ... the values reported in the following figures, when larger ∼ 20,
   should be considered as lower bounds." Scale checked by decimation
   (Fig. 2B).
2. **ID ≪ width** (Abstract; §3.1). "the ID is orders of magnitude smaller
   than the number of units in each layer"; VGG-16-R pool4: "ID ≈ 19 and
   ED ≈ 10^5".
3. **Hunchback** (§3.1, Fig. 3). "the ID initially grew, then reached a
   peak or a plateau and, finally, progressively decreased towards its
   final value"; VGG and ResNet peaks "between 100 and 120 in the relative
   depth range 0.2-0.4". Footnote 1 excepts AlexNet and the small MNIST
   network. Profiles "approximately collapsed" on relative depth.
4. **Last-layer ID predicts accuracy, across architectures only**
   (§3.2, Fig. 4; A.1.4). Last-hidden ID ≈ 12 (ResNet-152) to ≈ 25
   (AlexNet), widths 512–4096; "a strong predictor of the performance of
   the network on the test set, as measured by top 5-score (Fig. 4, Pearson
   correlation coefficient r = 0.94)"; r = 0.99 within ResNets. But across
   50 seeds of one VGG-16 on CIFAR-10, "finding no correlation with accuracy
   (r=-0.003)".
5. **Linear vs nonlinear dimension** (§3.3, Fig. 5). Spectrum: "We did not
   find a clear gap in the eigenvalue spectrum", "qualitatively consistent
   with that obtained for stimulus-representations in primary visual cortex
   [23]" (Stringer et al., bioRxiv). PC-ID = components for 90% of variance
   of the correlation matrix: "about one or two orders of magnitude larger
   than the value of the ID computed with TwoNN", VGG-16 last hidden PC-ID
   ≈ 200 vs ID ≈ 18.
6. **Covariance-matched Gaussian** (§3.3, Fig. 5B). For "a synthetic
   Gaussian dataset with the same second-order moments", "the ID of the
   synthetic dataset was two orders of magnitude larger, and grew with N
   ... as expected in the case of an ill-defined estimator".
7. **Random weights** (§3.3, Fig. 5C). PC-ID profile "qualitatively the
   same as in trained networks"; TwoNN ID on random weights "remarkably
   flat"; "the ID kept growing after that the ED had already started to
   substantially decline".
8. **Early rise from irrelevant correlated features** (§3.4, Fig. 6). A
   per-image luminance offset (MNIST*, λ = 100) drops input ID "from ≈ 13
   ... to ≈ 3" and produces a hunchback in a net that had none.
9. **Random labels** (§3.5). On shuffled MNIST the ID "grew considerably
   in the second half of the network, almost saturating the upper bound,
   which is set by the ED, in the output layer".
10. **Training dynamics** (§3.3, Fig. 9). Last-hidden ID is non-monotonic
    in training: "after an initial drop, the ID slowly increased, but,
    differently from [15], without resulting in substantial overfitting".
11. **Interpretation** (§4). "progressive reduction of the ID, rather than
    gradual flattening, seems to be the key to achieving linearly separable"
    representations; "a flattening of data manifolds may not be a general
    computational goal".

## Assumptions
- Local uniformity of density up to the second neighbour; a single global
  ID per point cloud (no mixture of dimensions per layer).
- IDs above ~20 are lower bounds; mid-layer peaks (100–120) are therefore
  floors, not values.
- Sample sizes 450–2000 points; ImageNet hunchback uses 7 dog-heavy
  classes (koala, shih-tzu, rhodesian, yorkshire, vizsla, setter,
  butterfly), 500 images each, averaged per class.
- Last-layer ID–accuracy relation is a correlation over 14 pretrained
  torchvision models, not an intervention.
- The output-layer bound "Nc ≤ 2^ID" (ID ≳ 10 for ImageNet) is a heuristic
  ("each category is associated with a binary representation").
- "PC-ID" is a 90%-variance count on the correlation matrix, not a
  participation ratio.

## Concepts
Intrinsic dimension (global, TwoNN); embedding dimension ED (= ambient
width); PC-ID (linear, 90% variance); hunchback profile; relative depth;
decimation/scale test; covariance-matched Gaussian surrogate; curved vs flat
manifolds; pruning of irrelevant low-level features (whitening) in early
layers.

## Verdict on the exchange's characterization
- TERM-136 quotes A29: representations "can have intrinsic dimensions far
  below their layer widths, and … intrinsic dimensionality changes
  systematically across layers". **Accurate** (results 2, 3).
- LIT-2998 summary: "rises in early layers and falls in later ones, and a
  low final dimension predicts accuracy". **Accurate with two
  qualifications**: the rise is absent in the small MNIST net and weak in
  AlexNet (footnote 1, §3.4); the prediction holds across architectures
  (r = 0.94) and not across seeds of one architecture (r = −0.003, A.1.4),
  and it is the ID of the training set.
- "learned representations concentrate on low-dimensional manifolds"
  (LIT-2998 standing): accurate, and the paper adds that they are curved,
  not low-dimensional subspaces; the record should not read it as low
  linear rank.
- NOTE-541 ("intrinsic dimension rising then falling with depth"):
  accurate.

## Bearing on named codes
- **TERM-136 — supports, and qualifies.** Supports the intrinsic sense m
  and its separation from ambient D (the paper's ED), results 2, 5.
  Qualifies: (a) m as measured here is a global, scale-dependent estimate,
  checked by decimation, and a lower bound above ~20; (b) the paper's
  linear dimension is PC-ID (90% variance), a fifth notion beside D_PR, so
  "effective dimension" in TERM-136 should not be read as the paper's
  linear dimension. The TERM's "(Deferred: registered, not read)" can be
  replaced by the reading.
- **CLAIM-848 — parallel; supports its last clause, qualifies by
  direction.** CLAIM-848 says D_PR does not track intrinsic dimension
  (smooth codes of m = 20–100 all give D_PR ≈ 20–29 at width 768).
  Ansuini finds the same decoupling empirically but in the opposite
  direction and with a different linear measure: PC-ID ≈ 200 ≫ TwoNN ID
  ≈ 18 (result 5), and PC-ID does not separate trained from random nets
  (result 7). Together: a linear count can sit either above (90%-variance
  count, curved low-ID manifold) or below (PR, smooth high-m code) m. The
  paper does not compute a participation ratio, so it neither tests
  CLAIM-848's numbers nor contradicts them.
- **CLAIM-847 — background, with a pointed control.** The paper does not
  treat norms or concentration. Its covariance-matched Gaussian (result 6)
  shows that the second moments, which fix D_PR and hence CLAIM-847's norm
  spread, do not fix nearest-neighbour geometry: the Gaussian with the same
  covariance has an ID two orders larger and ill-defined. Consistent with
  CLAIM-847's scope (a Gaussian representation) and a warning against
  carrying it to real representations' local geometry.
- **THEORY-tmpwtoad (Stringer) — parallel/background.** Ansuini cites
  Stringer [23] (bioRxiv 2018) twice: the gapless last-layer spectrum is
  "qualitatively consistent" with V1's, and the early ID expansion "is
  consistent with a recent characterization of the dimensionality of image
  representations in primary visual cortex [23]". No exponent is fitted,
  so Stringer's 1 + 2/d bound is not tested; and Ansuini's low curved ID is
  a different quantity from Stringer's spectral decay.

## Limitations
- Correlational; no causal test that lowering last-layer ID improves
  generalization; no within-architecture relation (r = −0.003).
- High IDs are underestimates; the hunchback's peak height is a floor.
- Few classes, few hundred points per manifold for the ImageNet profiles.
- CNNs on images only; no transformers or language models.
- PC-ID threshold (90%) is ad hoc, on the correlation matrix.
- Training-dynamics evidence is "exploratory" (one VGG-16, CIFAR-10).

## Candidate THEORY
"In trained image CNNs the TwoNN intrinsic dimension of a layer's
representations is one to several orders of magnitude below the layer's
width, rises over the first layers and then falls to about 12–25 in the
last hidden layer, is one to two orders below a 90%-variance PCA count,
and across architectures (not across seeds) its last-hidden-layer value
correlates with test accuracy (r = 0.94 over 14 ImageNet models); random
weights give a flat profile, and shuffled labels a rising one."
`promote_when`: An independent study, with an intrinsic-dimension estimator
other than TwoNN or with TwoNN on other image networks, reproduces the
rise-then-fall profile and the gap to a linear PCA count, and finds the
last-layer ID–accuracy correlation across architectures.

## Recheck (search after reading)
Searched record/ for Facco, Levina–Bickel, TwoNN/two-NN, local intrinsic
dimensionality/Amsaleg/Houle, Ma et al. noisy labels, Shwartz-Ziv/Tishby,
SVCCA/Raghu, untangling/DiCarlo, Chung–Lee–Sompolinsky manifold capacity,
random labels/Zhang, tunnel effect, Achille–Soatto, Basri–Jacobs, curved vs
flat manifolds, covariance-matched null, PCA/explained-variance dimension.
Held entries the first search missed, with bearing:
- **LEAD-210** (track probe-set representations against isotropic,
  covariance-matched and shuffled nulls): **directly relevant.** Its
  "Gaussian matched to the learned covariance" null is Ansuini's Fig. 5B
  control, which Ansuini runs through TwoNN with decimation and finds an ID
  two orders larger, growing with N. Suggests adding TwoNN ID (with a
  decimation check) to the LEAD's per-checkpoint measurements; and
  Ansuini's Fig. 9 is a checkpoint-tracking precedent (non-monotonic
  last-layer ID).
- **SYNTHESIS-120** (how a representation comes to draw a new distinction;
  "Effective dimension sets it", line 109): qualifies. Effective (PR)
  dimension and intrinsic dimension diverge in trained networks; any
  account in it that leans on low dimension should say which.
- **NOTE-549 / LIT-708** (rarely categorical, highly separable cortical
  representations; PR of condition centroids rises along the cortical
  hierarchy, 2.0 to 5.3): contrast. A PR along a brain hierarchy rising vs a
  nonlinear ID falling over late CNN layers; different measures and
  objects, not a conflict.
- **NOTE-789 / LIT-946, THEORY-251** (Kirsanov et al., manifold capacity,
  dimension as participation ratio, in language models): parallel.
  Ansuini's §4 links its result to Chung–Lee–Sompolinsky capacity
  ([30], [33]); THEORY-251 is the record's held instance of that
  apparatus, with dimension in the PR sense, not TwoNN's.
- **NOTE-541 / LIT-678** (intermediate-layer classifiers for OOD; names
  Ansuini and the tunnel effect): consistent; last-layer ID compression
  and penultimate-layer suppression of shift-relevant variation are the
  same region of the network. No new bearing beyond the existing mention.
- **THEORY-083** (neural collapse, via NOTE-541): parallel; last-layer ID
  of order 10 is compatible with collapse toward class means, but the paper
  does not measure collapse.
- Not held: Facco et al. 2017 (TwoNN), Levina–Bickel 2005, Ma et al. 2018
  (dimensionality-driven learning), Chung–Lee–Sompolinsky 2018; possible
  registrations if the record leans on the estimator.
- Hits on "two nearest", "Levina" (a different Levina, criticality),
  "Houle"/"Thouless" were false positives.
