---
status: Read
paper: 'LIT-tmpf3sak'
title: 'Taxonomizing local versus global structure in neural network loss landscapes'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (33 pages, text layer). Sections 1–5 and Appendices
    A–D read in full. The phase diagrams (Figures 2–8, 13–23) are read from
    their captions and the text; the extracted text carries axis ticks but
    not the plotted values, so no per-pixel number is reported here. The
    individual curve values in Figure 12 (for example mc = −10.686 at batch
    size 16, width 2) are read from the plot labels the text layer keeps.
date: '2026-10-03'
summary: >-
  mc(θ, θ′) = ½(L(θ) + L(θ′)) − L(γ(t*)) on a trained Bezier curve, in 0-1
  training error (Eq. 4); mc < 0 is a barrier, mc ≈ 0 well connected, mc > 0
  unconverged ends. With Hessian top eigenvalue and trace and output CKA on
  mixup points, a load by temperature grid splits into phases I–IV, with
  IV-B (flat, connected, similar) the most accurate. Sharpness alone
  mispredicts across phases; with 10% label noise, the sharp phases beat
  flat but poorly connected phase III, and double descent appears along the
  Hessian transition.
---

<!-- inactive-ok-file: THEORY-087 — Proposed; named for the regular versus singular complexity penalty, with no relation claimed -->

# NOTE-tmp3zzdt: Taxonomizing local versus global structure in neural network loss landscapes

## Contribution

A systematic empirical map of where realistic networks' loss landscapes are
locally sharp or flat and globally connected or not, as two practical
control parameters vary. Before it, sharpness was the main landscape
predictor of generalization and mode connectivity was a property shown for
good models on clean data. After it, there is a measured phase diagram in
which the two disagree, and in which connectivity and output similarity,
which need no test data, separate good from bad regions that the Hessian
does not.

## Key insight

A loss landscape has a local character, the curvature where training
stopped, and a global one, whether independently trained solutions can be
joined at low loss and whether they compute the same function. These vary
independently. A network can sit in a very flat region of a landscape that
is a set of separated basins (phase III), and that is worse than sitting in
a sharp region of a connected one. Good generalization needs the global
property first and the local one second.

## Assumptions

- **Load-like parameter**: model width (ResNet18 channel width k in
  {k, 2k, 4k, 8k}), training-set size, fraction of randomized labels, or
  additive pixel noise, "the amount and/or quality of data, relative to the
  size of the model" (Section 2).
- **Temperature-like parameter**: batch size (smaller is hotter), learning
  rate or weight decay, held constant through training in the standard
  setting so that each axis moves one quantity (Appendix B.3, footnote 3).
- **Training**: SGD, constant learning rate 0.05, batch 128, weight decay
  5e-4 in the standard setting; stop when the training loss changes by less
  than 1e-4 for 5 epochs or after 150 epochs; no data augmentation, to
  avoid confounding; five runs per grid point (Appendix B.3).
- **Connectivity**: quadratic Bezier curve (three bends counting the
  endpoints), trained 50 epochs from learning rate 0.01; 0-1 training error
  on the curve, evaluated at five t values (Appendix A.2). Ablations over
  learning rate and a cubic curve leave the picture unchanged (A.4.2).
- **Similarity**: linear CKA (Eq. 3) of softmax outputs on 640 mixup points,
  λ ~ Beta(16, 16). On the raw training set, CKA is trivially high once the
  models fit it (A.1, A.4.1).
- **Hessian**: PyHessian power iteration and Hutchinson trace on one batch
  of 200 samples (B.4).

The setting is image classification at CIFAR scale plus one small
translation task with 4K sentence pairs. "Phase" is used operationally, for
regions of the grid separated by sharp changes in a metric. No limit is
taken, so no phase transition is established in the statistical-mechanics
sense.

## Key results

- **Standard setting (Figure 2, ResNet18, CIFAR-10, width × batch size).**
  The Hessian transition coincides with a more than tenfold fall in training
  loss. Test accuracy improves markedly only after the connectivity
  transition. Phase III and IV-A have "almost the same" Hessian but
  different accuracy.
- **Phase definitions (Section 3.1).** I: training loss high, Hessian large,
  mc poor. II: training loss high, Hessian large, mc positive because the
  ends are unconverged. III: training loss small, Hessian small, mc poor.
  IV: training loss small, Hessian small, mc near zero. IV-B has larger CKA
  than IV-A.
- **ℓ₂ distance** between weights is less informative than CKA, because
  the same function has many weight realizations (Figure 2g).
- **Learning-rate decay (Figure 3)** keeps the four phases. Its accuracy
  gain peaks almost exactly at the connected/poorly-connected boundary
  (Appendix C, Figure 13).
- **Label noise (Figure 4).** With 10% randomized labels, a dark band of
  low accuracy, double descent in width and in temperature, follows the
  Hessian transition. On a width column through phase III, the best
  accuracy is in phase I/II, which is sharp and not at zero loss.
- **Data amount (Figures 6–7).** The Hessian grows with data and mode
  connectivity worsens with data (the well-connected region shrinks), while
  accuracy rises; only CKA tracks the trend.
- **Label-noise fraction (Figure 8).** Below a training loss of 5e-3 the
  Hessian trace changes slowly with noise from 2.5% to 60%, while
  connectivity and CKA degrade.
- **Translation (Appendix D.4).** For six-layer Transformers on IWSLT'16
  De-En with 4K pairs, mc stays negative up to embedding dimension 512, and
  optimal early stopping gives a large test improvement (Figure 19).
- **Pixel noise (Appendix D.6)** leaves connectivity near zero but lowers
  CKA.
- **Large batch (D.7.1)** raises the Hessian; the linear scaling rule (D.7.2)
  flattens the temperature axis, since it holds noise variance roughly
  constant.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The best test accuracy occurs in the locally flat, globally well-connected, high-similarity phase (IV-B) | moderate: consistent across the grids shown, but one architecture family dominates, and the phase boundaries are read by eye | Figures 2–8, 14–23 |
| C2 | Local sharpness alone does not predict test accuracy across phases | strong within these experiments: phase III against IV-A, label noise, data amount and weight decay each give a counterexample | Figures 2, 5, 6, 8 |
| C3 | When the landscape is poorly connected, training to zero loss can lower test accuracy | moderate: shown at constant learning rate; attributed to insufficient exploration; one translation task agrees | Figure 4, D.3, D.4 |
| C4 | Width improves connectivity, data improves similarity, label quality improves connectivity | moderate: read from phase diagrams on CIFAR-10 | Section 5 |
| C5 | Empirical double descent is a consequence of transitions between qualitatively different phases | weak to moderate: the band coincides with the Hessian transition; the causal reading leans on the cited theory | Figure 4, Section 3.2 |
| C6 | Connectivity and similarity are computable without test data, so they are non-trivial generalization predictors | moderate: true of the metrics; their cost is several model trainings plus a curve fit per point | Section 1 |

## Method

Train two models per grid point from different initializations (five runs
in total), fit a Bezier curve between them on the training set, report
mc at the worst of five evaluated points, report the top Hessian eigenvalue
and trace at the endpoint, and report linear CKA of their outputs on mixup
interpolations. Average over runs, plot each metric over the load by
temperature grid, and read the phases off the transitions.

## Concepts

- **load-like parameter**: a control parameter that changes the
  landscape by changing data quantity or quality relative to model size.
- **temperature-like parameter**: a control parameter that changes the
  noise in SGD and so the "effective loss" that training sees, without
  changing L(θ).
- **globally well-connected**: connectivity level E[mc] ≈ 0 (Definition 4
  calls a landscape "globally nice" when μ is near 1 and β > 0, and the text
  says β ≈ 0 is best; the definition and the text differ slightly here).
- **globally nice**: well connected and with high similarity μ between
  trained models.
- **rugged convexity**: the picture, taken from Martin and Mahoney, of a
  single large connected basin with rough local structure.

## Connections

- **Martin and Mahoney ([LIT-tmpms4ta](../literature.d/LIT-tmpms4ta.md))** supply the load and temperature
  parameters, the expectation of sharp phases and "bad fluctuations" between
  them, and the rugged-convexity picture.
- **Garipov et al. ([LIT-tmpotq71](../literature.d/LIT-tmpotq71.md))** supply the curve-fitting procedure and
  schedule; **Draxler et al. ([LIT-tmp3kyq9](../literature.d/LIT-tmp3kyq9.md))** the companion definition.
- **Liao et al. ([LIT-tmpufwlh](../literature.d/LIT-tmpufwlh.md))** and **Dereziński et al. ([LIT-tmpzk7ci](../literature.d/LIT-tmpzk7ci.md))**
  are the theoretical double-descent-as-phase-transition results this paper
  says it corroborates.
- **Papyan's class/cross-class structure ([LIT-613](../literature.d/LIT-613.md))** is cited as one of the
  papers showing the Hessian is low-rank with outliers. This paper then
  summarizes the Hessian by its top eigenvalue and trace only. In Papyan's
  picture the top eigenvalue is a class-driven outlier, so that half of
  "local sharpness" here measures between-class structure at the endpoint;
  the trace adds the bulk. This is my reading, not the paper's.
- **Kornblith et al.'s CKA** is the similarity used. Here it is applied to
  the network's output, not to a hidden layer (footnote 2).

## Bearing on the record

- **Watanabe ([LIT-616](../literature.d/LIT-616.md)) and the regular/singular complexity penalty
  ([THEORY-087](../theory.d/THEORY-087.md)).** The local probe here is curvature at the endpoint. In
  singular learning theory the relevant local quantity is degeneracy (the
  learning coefficient), which a trace or top eigenvalue does not measure.
  The anthology's degeneracy practice ([ANTH-SOTA-325](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-325.md)) reports that the
  estimated learning coefficient still orders runs by test accuracy after
  the training loss has saturated, which is where this paper finds the
  Hessian failing. That is a candidate reconciliation: the
  failures here may be failures of curvature, not of local measures as
  such. Nothing in this paper tests it.
- **MacKay's Occam factor ([LIT-623](../literature.d/LIT-623.md))** prices a basin by det⁻¹ᐟ² of the
  Hessian. This paper's phase III, flat yet poorly generalizing, is a
  warning that a large Occam factor at the endpoint does not by itself
  imply generalization when the basins are disconnected. That is my
  connection, not the paper's.
- **THEORY candidate (not filed):** "In trained classifiers, global
  landscape structure (low-loss connectivity between independent solutions,
  and similarity of the functions they compute) predicts test accuracy
  across load and temperature where endpoint curvature does not; curvature
  separates only converged from unconverged training." Source: this paper,
  with [LIT-tmpms4ta](../literature.d/LIT-tmpms4ta.md) for the phase framing; promote when a second group's
  measurements reproduce phase III against IV-A.
- **Anthology.** Bears on [ANTH-SOTA-012](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-012.md) (sharpness correlates with test
  error) as a set of counterexamples, and carries its own instruction
  (check mode connectivity before training to zero loss).

## Limitations

- **One architecture family carries the claims.** ResNet18 on CIFAR-10
  makes up most figures; VGG11, SVHN, CIFAR-100 and the Transformer appear
  in the appendix at lower resolution.
- **No data augmentation**, by design, so the networks are not those
  trained in practice; the authors say augmentation can improve accuracy
  "if used properly".
- **Phases are read from colour maps.** No boundary is fitted, and the
  IV-A/IV-B split is admitted to be a smooth crossover.
- **Connectivity is measured on one curve family**, a quadratic Bezier
  trained for 50 epochs. A negative mc says this family found no low path,
  not that none exists, and permutation alignment is not tried.
- **CKA is on outputs only**, so "similar models" means similar predictions
  on interpolated inputs.
- **Cost.** Each test-accuracy plot needs "several days" on an 8-GPU V100
  server (B.5).

## Open questions

- Are the barriers of phases I and III permutation barriers, which
  re-basin alignment would remove, or real separations between basins?
- Does a degeneracy measure (the local learning coefficient) separate
  phase III from IV-A where the Hessian fails?
- Do phase diagrams outside the load/temperature form, which the authors
  name as future work, have the same structure?

## Corrections

- none (there was no seed)
- **Definition 4 against the text.** Definition 4 calls a landscape globally
  nice when β is "larger than 0", while Section 2 and Appendix A.2 say good
  connectivity is β ≈ 0 and a large positive β means unconverged ends. The
  text's reading (β ≈ 0) is the one the figures use.
