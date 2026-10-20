---
number: 762
status: Read
formerly:
- NOTE-tmp6f398
paper: LIT-1044
title: 'Kornblith, Chen, Lee & Norouzi — Why Do Better Loss Functions Lead to Less Transferable Features?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v2 of 3 November 2021, the NeurIPS
    2021 version, 33 pages), fetched from arxiv.org/pdf/2010.16402v2 and
    extracted with pdftotext, both plain and -layout. Read: the main text
    (§§1–6); Appendix A (training, linear-probe and fine-tuning protocols,
    Tables A.1–A.2); B (Inception v3, Table B.1); C (training accuracy,
    out-of-distribution robustness and calibration, prediction similarity,
    combined regularizers, Tables C.1–C.6); D (per-dataset scatter,
    transfer over training, Chexpert, CKA before and after fine-tuning); E
    (the derivation of R² as a variance ratio, other separation indexes,
    the simplex-ETF measurements of Table E.2, augmentation, separation
    over training); and F (class overlap). Tables were checked against the
    -layout text. Figures were read from their captions and the text. The
    Spearman ρ = −0.93 of §3.4 was recomputed from Tables 1 and 3 and
    agrees.
date: '2026-10-14'
summary: >-
  For ResNet-50 on ImageNet, every training objective that raises accuracy
  over softmax cross-entropy also raises penultimate-layer class
  separation, and fixed penultimate features with more class separation
  transfer worse to new-class datasets (Spearman ρ = −0.93 across nine
  objectives; one temperature knob moves both). The losses differ only in
  the last few blocks, and full fine-tuning erases the difference. For the
  pretraining classes themselves, more separation helps.
---
<!-- inactive-ok-file: THEORY-083 THEORY-104 THEORY-286 — Proposed; the statement of collapse, the layer-wise account, and the two derivations of collapse filed today -->

# NOTE-762: Kornblith, Chen, Lee & Norouzi — Why Do Better Loss Functions Lead to Less Transferable Features?

## Contribution

Before it, alternative losses and output-layer regularizers were judged
by accuracy on the task they trained, with one earlier report (Kornblith,
Shlens & Le 2019) that label smoothing and dropout hurt transfer. After
it, there is a controlled comparison of nine objectives on one
architecture and dataset. Every one that improves ImageNet accuracy gives
fixed features that transfer worse to new classes. The difference sits in
the last few blocks, and it tracks one index of how tightly each class is
clustered in the penultimate layer.

## Key insight

A loss that buys training-class accuracy does so by shrinking
within-class spread in the last layers relative to the spread between
classes. Spread inside a class that is irrelevant to the label is what a
new task, whose classes cut across the old ones, needs to read. The
features become "overfit … to the pretraining classes" (§3.4): better for
those classes even when relearned from fresh data, worse for any other
partition. Only the top of the network pays, and fine-tuning rebuilds the
top.

## Assumptions

Setting, not theorems; the paper is empirical.

- **One pretraining task.** ImageNet ILSVRC 2012, 1000 classes. ResNet-50
  v1.5, 8 runs per loss; Inception v3 with ResNet hyperparameters, 3 runs
  per loss (Appendix B).
- **Training protocol (A.1).** SGD with Nesterov momentum, batch 4096,
  weight decay 8 × 10⁻⁵, standard crop-and-flip augmentation, an
  exponential moving average of the weights. Each loss's hyperparameters
  and stopping epoch (146–196 epochs, Table A.1) were tuned on 50,046
  held-out training images.
- **Not the terminal phase.** Stopping is early, at the best holdout
  accuracy. Training top-1 is 91.62–93.62% (Table C.1), so no network is
  past zero training error. "Collapse" here is relative within-class
  variance at that point, not Papyan et al.'s limit.
- **Transfer by fixed features.** Penultimate-layer features (after
  average pooling), read by L2-regularized multinomial logistic
  regression with L-BFGS, the penalty chosen on a held-out split from 45
  log-spaced values (A.2), or by k-NN with k by leave-one-out. Fine-tuning
  (A.3) is a separate experiment, 3 pretraining runs per loss.
- **Transfer targets.** Food-101, CIFAR-10, CIFAR-100, Birdsnap, SUN397,
  Stanford Cars, Oxford-IIIT Pets, Oxford Flowers (Table A.2), plus
  Chexpert (D.3). Their classes are mostly not ImageNet's (Table F.1).
- **The separation index.** R² = 1 − d̄_within/d̄_total, with cosine
  distance d = 1 − sim(x, y), averaged within each class and over all pairs
  (Eq. 11), on the ImageNet training set. For L2-normalized embeddings and
  balanced classes it is one minus the ratio of within-class to total
  variance, and equals linear CKA between the cosine kernel of the
  embeddings and the one-hot label matrix (E.1).

## Key results

- **Table 1 (ImageNet accuracy and linear transfer, ResNet-50, 8 runs).**
  ImageNet top-1: softmax 77.0, label smoothing 77.6, sigmoid 77.9, extra
  final-layer L2 77.7, dropout 77.5, logit penalty 77.7, logit
  normalization 77.8, cosine softmax 77.9, squared error 77.2. All but
  squared error are significantly above softmax. Mean linear transfer over
  the eight datasets (computed here from the table): softmax 75.9,
  sigmoid 74.6, label smoothing 74.3, dropout 74.2, extra L2 72.4, logit
  penalty 70.6, logit normalization 69.9, cosine softmax 65.8, squared
  error 48.3. Softmax is best or tied on every dataset but Pets, where the
  range is 84.7–92.9. Largest per-dataset gaps: Cars 60.3 (softmax) →
  36.7 (cosine) → 15.3 (squared error); Flowers 94.0 → 75.3 → 46.7. k-NN
  transfer orders the losses the same way. *Holds for:* fixed penultimate
  features, new-class datasets.
- **Table 2 (fine-tuning).** Mean accuracy 85.1–86.4 across losses;
  softmax 86.2, best 86.4, a 0.2-point gap that is not significant. Logit
  normalization and cosine softmax are about 1 point lower, mostly on
  SUN397 (58.3 and 56.9 against 63.4). *Holds for:* full fine-tuning with
  hyperparameters tuned per loss and dataset.
- **Figure 2 and Figure 3 (where the losses differ).** Linear CKA between
  corresponding blocks of networks trained with different losses is high
  through most of the network. Consistent differences appear only "in the
  last third of the network, starting around block 13" of 16. ReLU
  sparsity is similar across losses in the first three stages and
  diverges in the last; penultimate activations are 92.8% non-zero for
  softmax and under 25% for logit normalization, cosine softmax and
  squared error. Figure D.3: fine-tuning changes the later layers most.
  Figure B.1 replicates the CKA picture for Inception v3.
- **Table 3 (class separation R², training set, 8 runs).** Softmax 0.349,
  label smoothing 0.420, sigmoid 0.427, dropout 0.461, logit normalization
  0.517, extra L2 0.572, logit penalty 0.601, cosine softmax 0.641,
  squared error 0.845; standard errors ≤ 0.0006. Figure 4: R² rises with
  depth for every loss, and the losses separate in the last stage. Table
  E.1: Euclidean and mean-subtracted cosine indexes give the same order
  within a few hundredths.
- **§3.4 and Figure 5a (separation against transfer).** Across the nine
  losses, R² and mean linear transfer have Spearman ρ = −0.93, p = 0.002
  (recomputed here from Tables 1 and 3: −0.933). *Holds for:* nine
  points, one per loss, each an average of 8 runs.
- **Table 4 and Figure 5b (one knob).** Cosine softmax at τ = 0.01 to
  0.08: R² 0.236, 0.358, 0.475, 0.562, 0.634, 0.693, 0.738, 0.770; top-1
  74.9, 77.0, 77.5, 77.6, 77.6, 77.5, 77.5, 77.6; mean linear transfer
  (computed here) 76.0 at τ = 0.01 and 58.9 at τ = 0.08. Lowest τ, lowest
  ImageNet accuracy (2.7 points under the best), best features on nearly
  every dataset. Beyond τ = 0.04 accuracy is flat while R² keeps rising
  and transfer keeps falling. *Holds for:* one loss family; below τ = 0.05
  the loss was rescaled by τ for stability.
- **Table E.2 (the simplex-ETF measurements of Papyan et al.).**
  Tr(Σ_W Σ_B†)/C: softmax 21.16, dropout 9.70, label smoothing 9.00,
  sigmoid 6.96, extra L2 6.10, logit normalization 2.94, logit penalty
  2.72, cosine softmax 1.31, squared error 0.33. The equiangularity
  measures (std and mean deviation of class-mean cosines from −1/(C−1))
  also separate softmax from the rest. Norm equality and classifier–mean
  alignment do not. For isotropic covariances Tr(Σ_W Σ_B†)/C =
  (P/C)(1/R² − 1). (Across the nine losses this measure orders mean linear
  transfer with Spearman ρ = 0.92, computed here; the paper does not
  report it.)
- **Figure 6 (same classes, relearned).** A linear head relearned on
  40,000 ImageNet validation images, scored on the other 10,000: features
  from softmax do worst and the more separated features do substantially
  better; the gap between original and relearned heads narrows as R²
  rises.
- **Appendix F and Pets.** 25 of Pets' 37 classes are ImageNet classes;
  mapping an ImageNet classifier's predictions onto Pets' classes gives
  71.2%, against 4.0–34.6% for Food, CIFAR-100, Birdsnap, SUN397, Cars and
  Flowers (CIFAR-10 65.1%). Pets is where more separated features tie or
  win.
- **Table C.2 (same classes under shift).** Alternative losses are
  slightly better than softmax on ImageNet-V2 (65.0 → up to 65.9),
  ImageNet-A (2.7 → up to 4.8), ImageNet-Sketch (21.8 → up to 24.8),
  ImageNet-R (36.8 → up to 39.2) and ImageNet-C (mCE 75.9 → down to 72.5).
  These are the networks' own heads, not probes.
- **Table E.3 (augmentation).** AutoAugment raises top-1 by 0.4–0.7 points
  with R² unchanged within 0.01 (softmax 0.349 → 0.353, cosine 0.641 →
  0.632).
- **Figure E.4 (over training).** For softmax, training-set R² peaks at
  epoch 32 and then falls; for every other loss it is highest at the last
  checkpoint. The ordering of losses is set early. Figure D.2: softmax has
  the best linear transfer through the whole run on most datasets.
- **Table C.4.** Combining two of these losses or regularizers gives no
  further accuracy; the authors read this as a shared mechanism.
- **Table D.1 (Chexpert).** On an i.i.d. split of 22,431 training images,
  softmax features give the best AUC on 4 of 5 pathologies and tie on the
  fifth; squared error is worst throughout.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Objectives that raise ImageNet accuracy over softmax give fixed penultimate features that transfer worse to new-class datasets | strong | Table 1, 8 runs per loss, significance tests; replicated for Inception v3 (Table B.1) and Chexpert (Table D.1) |
| C2 | Penultimate-layer class separation is inversely related to fixed-feature transfer to new classes | moderate | ρ = −0.93 over nine losses (Figure 5a) and a monotone temperature sweep in one loss (Table 4); correlational across losses, one family for the sweep |
| C3 | Class separation is what causes the transfer loss | weak | the authors' "accounts for" (§1); no intervention on separation with the loss held fixed beyond τ, which also changes other things |
| C4 | Loss functions change representations only in the last few blocks | strong | CKA (Figure 2, B.1) and sparsity (Figure 3) |
| C5 | Pretraining loss has little effect after full fine-tuning | moderate | Table 2, 3 runs per loss; the two normalized losses are about 1 point lower |
| C6 | More class separation helps when the downstream classes are the pretraining classes | moderate | Figure 6, the Pets exception, Appendix F |
| C7 | Class separation is not necessary for higher accuracy | moderate | Table E.3, AutoAugment, 3 runs |

## Concepts

- **Class separation (R²).** One minus the ratio of mean within-class
  cosine distance to mean overall cosine distance, in a layer's
  activations (Eq. 11). It is η² of ANOVA on normalized embeddings
  (E.1). It is a relative measure: R² = 1 is every class at a point.
- **Fixed-feature (linear) transfer.** A new classifier on frozen
  penultimate features, the network unchanged.
- **Transfer.** Here, to datasets with different classes. The paper keeps
  this apart from out-of-distribution generalization, "where the training
  and evaluation datasets consist of the same classes but with some degree
  of distribution shift" (§4).
- **"Overfit … to the pretraining classes".** Better at the training
  partition from new data of the same classes, worse at other partitions
  (§3.4).

## Connections

It extends Kornblith, Shlens & Le (2019), which found label smoothing and
dropout hurt transfer, to nine objectives, and ties the effect to one
property of the representation. It uses linear CKA from Kornblith et al.
(2019; [LIT-254](../literature.d/LIT-254.md) in the record). It relates its measurements to Papyan,
Han & Donoho's neural collapse ([LIT-618](../literature.d/LIT-618.md)) in Table E.2 without claiming
its networks are in the terminal phase. It sets itself against the
finding that ImageNet accuracy predicts accuracy under same-class shift
(Recht et al., Taori et al.), and notes few-shot results from very large
pretraining sets where extra final-layer L2 helped some tasks (Zhai et
al., Abnar et al.); it suggests shared classes as the reason, untested.
The neural-collapse review [LIT-978](../literature.d/LIT-978.md) reports it as "networks with more
collapse transfer worse".

## Bearing on the record

- **[QUESTION-051](../questions.d/QUESTION-051.md), second half.** This is the direct measurement its body
  said was "not held, and worth filing". It measures what tighter
  class clustering in the last layer costs for decisions the network was
  not trained on: for new class partitions, a large cost at the
  penultimate layer, rising with R²; for the training classes, a gain. It
  does not give what the question's "What would answer it" asks for in
  full: separation is measured layer by layer (Figure 4) but transfer is
  read only from the penultimate layer, so where in depth the lost
  information is still readable is shown only indirectly, by CKA and by
  fine-tuning recovering it. Filed as [THEORY-246](../theory.d/THEORY-246.md), which answers part
  of the question.
- **[THEORY-083](../theory.d/THEORY-083.md).** The paper's quantity is the same direction as NC1, and
  Table E.2 reports Papyan's own measure, but at early stopping with
  training accuracy near 92%, not in the terminal phase. [THEORY-083](../theory.d/THEORY-083.md) says
  what happens in the limit; this says that how far toward it a network
  is, at a fixed point in training, varies by a factor of about 60 in
  Tr(Σ_W Σ_B†)/C across standard losses, and that softmax is the least
  collapsed. Its Figure E.4 finding that softmax's separation falls after
  epoch 32 is not what [THEORY-083](../theory.d/THEORY-083.md)'s terminal-phase picture would lead one
  to expect, though the regimes differ.
- **[THEORY-104](../theory.d/THEORY-104.md).** [LIT-978](../literature.d/LIT-978.md)'s report reads as support for its mechanism
  ("more collapse at the top, worse readout off-distribution"). The full
  paper is narrower. Its cost is for new classes. For the same classes
  under shift (ImageNet-V2, -A, -Sketch, -R, -C), the more separated
  losses are slightly better (Table C.2), though those are the networks'
  own heads, not probes. [THEORY-104](../theory.d/THEORY-104.md)'s evidence is same-class shift
  (Waterbirds, CelebA, corruptions) across layers of one network; this is
  new-class transfer across losses at one layer. The two are different
  axes and different senses of "off-distribution", so this paper neither
  supports nor tests [THEORY-104](../theory.d/THEORY-104.md) directly. What it shares with it is the
  location: in both, what the training objective changes is confined to
  the last few layers.
- **[THEORY-278](../theory.d/THEORY-278.md) and [THEORY-286](../theory.d/THEORY-286.md).** Squared error gives by far the
  most collapse here (Tr(Σ_W Σ_B†)/C = 0.33). That fits [THEORY-278](../theory.d/THEORY-278.md)'s
  derivation that MSE drives collapse, though Hui–Belkin's weighted MSE
  (κ = 9, M = 60) is not the plain MSE derived there.
- **Anthology.** The paper's conclusion, that loss research should be
  judged on transfer, is an instruction for ML practice. The record holds
  the measurement, not the instruction. The LIT carries
  `anthology-candidate`.

## Limitations

- One pretraining dataset and two convolutional architectures. The
  authors say bigger label spaces "could potentially help to mitigate the
  trade-off" and might overlap downstream classes (§5).
- Supervised classification only. Self-supervised pretraining is cited as
  showing a similar trade, not measured.
- The separation–transfer relation is a correlation over nine losses plus
  one within-loss sweep. Nothing holds R² fixed while varying the loss,
  or varies R² with the loss fixed by a means other than τ.
- The relation of separation to ImageNet accuracy is non-monotonic:
  squared error has the most separation and no accuracy gain (§5).
- Early-stopped networks only. Whether the transfer cost grows in the
  terminal phase is not measured.
- Transfer is read from the penultimate layer only.
- The out-of-distribution numbers (Table C.2) are for each network's own
  head, so they do not separate a better head from better features.

## Open questions

- Does fixed-feature transfer from intermediate layers (say blocks 10–13)
  still fall with penultimate R²? If not, the information is moved out of
  reach of the top, not removed; if so, the loss reaches deeper than CKA
  shows.
- Does the relation hold with a large, diverse pretraining label space,
  where downstream classes are more often unions of pretraining classes?
- Does the cost grow past zero training error, as networks move into
  the terminal phase [THEORY-083](../theory.d/THEORY-083.md) describes?
- With features probed rather than read by the original head, does more
  separation still help under same-class shift?
