---
status: Read
paper: LIT-tmp64v07
title: 'Grokking and Generalization Collapse: Insights from HTSR theory'
version: 1
history:
- version: 1
  date: '2026-09-30'
  note: >-
    Read in full (Full text of arXiv 2506.04434 v1 (4 Jun 2025, the only
    version; marked "Preprint. Under review."), 15 pp., from the arXiv PDF.
    Read all of it: abstract, §§1–5, references, and Appendices A (setup,
    Table 3), B (metric definitions, eqs. 7–10), C (the WD = 0.01 run, Figs.
    6–7), D (trap statistics, Table 4) and E (limitations). Text was
    extracted with PyMuPDF. Pages 2, 6, 7 and 13 were rendered and Figs. 1,
    4, 5, 6 and 7 read from the images, since several findings below rest on
    the plots and not the prose. The "Supplementary Information" cited in
    §3.2 and App. D is not in the arXiv PDF and was not read. Not held in
    the Anthology of the SOTA: a grep of its literature.d for the arXiv id,
    the title, "HTSR" and "WeightWatcher" found nothing. `published:` is the
    arXiv v1 date.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-30'
summary: >-
  A depth-3, width-200 ReLU MLP trained on 1,000 MNIST images (the
  Omnigrok recipe, with weights and biases scaled ×8, MSE loss, AdamW, WD
  = 0) for 10⁷ steps goes through three phases read off the accuracy
  curves. In pre-grokking (to ~10⁵ steps) training accuracy saturates
  while test accuracy stays low. In grokking (~10⁵–10⁶) test accuracy
  rises to ~0.85. In "anti-grokking" (~10⁶–10⁷) it falls to ~0.45–0.5
  while training accuracy stays near 1. The average HTSR power-law
  exponent α of the two hidden weight matrices goes 4.0 → 2.9 → 1.1 at the
  phase ends (Table 1). In the collapse phase, correlation traps (outlier
  eigenvalues of the elementwise-shuffled weight matrix) appear. The
  paper's own weight-decay control shows FC2's α below 2, and traps in
  both layers, *without* a collapse (Fig. 6, Table 2). That undercuts its
  headline claim that α < 2 "invariably" heralds collapse.
---

# NOTE-tmpcarnz: Grokking and Generalization Collapse: Insights from HTSR theory

## Contribution

The paper extends the Omnigrok-style MNIST grokking run to 10⁷ optimisation steps with no weight decay and reports a third phase after grokking. In this phase test accuracy falls by roughly half while training accuracy stays near perfect. The authors call it "anti-grokking". They track the phases with the Heavy-Tailed Self-Regularization (HTSR) power-law exponent α of each hidden layer's weight spectrum, computed with WeightWatcher v0.7.5.5. The comparisons are the ℓ² weight norm and three of Golechha's progress measures: activation sparsity, absolute weight entropy and approximate local circuit complexity. They also introduce "correlation traps" as a marker of the collapse.

## Key insight

Measure each layer by the tail exponent of its weight-matrix eigenvalue density. By HTSR's lights, α ≈ 5–6 means random-like, 2–5 means well-correlated, α ≈ 2 means ideal, and α < 2 means over-correlated. Read this way, pre-grokking is "some layers still random" (FC1 α ≈ 5), grokking is "all layers near 2", and collapse is "a layer below 2 with rank-one outliers". The paper's own weight-decay control shows the last step is not a sufficient signal.

## Assumptions

- **The model.** 784 → 200 → 200 → 10 ReLU MLP ("3 Linear layers"). Weights and biases take the PyTorch defaults and are then multiplied by 8.0. Everything is float64 (Table 3).
- **The data.** 1,000 MNIST training images, 100 per class, stratified. The test set is the standard 10,000 images.
- **Training.** MSE on one-hot targets, AdamW with lr 5·10⁻⁴ and default β and ε, batch 200, 10⁷ steps. WD = 0 for the main results and WD = 0.01 for App. C.
- **HTSR.** The ESD is that of X = (1/N)WᵀW. The PL tail ρ(λ) ~ λ^(−α) is fitted by Clauset–Shalizi–Newman MLE, with λ_min chosen to minimise the KS distance. The α ranges and the "α = 2 ideal" and "α < 2 overfit" readings are taken from the prior HTSR and SETOL work ([9]–[11]), not established here. [9] is a draft on GitHub.
- **Correlation traps.** Shuffle W elementwise to W_rand, fit a Marchenko–Pastur bulk, and flag eigenvalues beyond the Tracy–Widom edge of λ⁺_rand (eq. 6). The KS test of ESD(W_rand) against the fitted MP law is the extra statistic.
- **What is tracked.** Only FC1 and FC2 are reported. The 200 → 10 output layer's α is never shown.
- **Phase boundaries** are drawn by eye from the accuracy curves at ~10⁵, ~10⁶ and ~10⁷ steps.

## Key results

- **Three phases, WD = 0 (Fig. 1).**
  - Pre-grokking: training accuracy rises from 10² steps and saturates by ~10⁵. Test accuracy reaches ~0.4.
  - Grokking: test accuracy rises to ~0.85, peaking near 10⁶.
  - Anti-grokking: test accuracy falls to ~0.45–0.5 by 10⁷.
- **α at the right edge of each phase, WD = 0 (Table 1, "values … taken from Fig. 4").**

  | layer | pre-grokking | grokking | anti-grokking |
  |---|---|---|---|
  | FC1 | 5.0 ± 0.7 | 3.6 ± 0.5 | 0.9 ± 0.4 |
  | FC2 | 2.9 ± 0.7 | 2.3 ± 0.2 | 1.3 ± 0.3 |
  | average | 4.0 ± 0.6 | 2.9 ± 0.2 | 1.1 ± 0.3 |

  In Fig. 4, FC2's α crosses 2 at about the test-accuracy peak (~10⁶), not well before it.
- **Correlation traps (Table 2).**
  - WD = 0, pre-grokking: 0 in both layers.
  - WD = 0, grokking: 1 ± 0 in each layer (but see corrections).
  - WD = 0, anti-grokking: FC1 7.5 ± 5.6, FC2 1 ± 0.
  - WD > 0, late window: FC1 2.0, FC2 1.0.
- **Trap statistics for FC1, WD = 0 (Table 4).** KS statistic and p-value against MP go from 0.0120 (p ≈ 1) at pre-grokking, to 0.0212 (p ≈ 1) at grokking, to 0.3044 (p = 1.877·10⁻⁵) with 9 traps at collapse. Fig. 3 (FC2) shows one trap at λ ≈ 10^6.5 "right before collapse" (p ≈ 4·10⁻¹³) and several in [10^2.x, 10^6.5] at the end.
- **Comparison metrics, WD = 0 (Fig. 5).**
  - The ℓ² norm is flat at ~90 to ~10⁵ steps, then rises to ~420, steepest during anti-grokking.
  - Activation sparsity rises from 0.77 to ~0.99 by 10⁵, dips slightly at peak test accuracy, then keeps rising.
  - Absolute weight entropy is flat at ~4·10⁴, then falls sharply, going negative, during collapse.
  - Local circuit complexity falls from ~14 to ~0 during grokking and stays near 0, with noise at the end.
- **WD = 0.01 control (App. C, Figs. 6–7).**
  - Test accuracy peaks at ~0.88 near 3·10⁵ steps, dips slightly, then plateaus at ~0.83–0.85.
  - The norm falls from ~95 to ~20.
  - Weight entropy falls from ~3.8·10⁴ to ~4·10³, mostly around the test peak.
  - Circuit complexity falls to ~0.
  - Average α settles near 2. FC2's α falls to ≈1.2 and stays there, while FC1 oscillates around 2–2.5.
  - There is no collapse.
- **Proposed account (§5).** Pre-grokking is when only some layers converge (α ≈ 4) while others stay near-random (α ≈ 5). Grokking is when all "important" layers approach α ≈ 2. Anti-grokking is when one or more layers overfit "in some yet undetermined way" (α < 2, traps, possibly rank collapse). The paper hypothesises that traps are rank-one perturbations causing "a large mean-shift" E[W_ij] and hence an "atypical" weight distribution.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With WD = 0, continued training long after grokking produces a large test-accuracy drop with training accuracy near 1 ("anti-grokking") | moderate (experiment), one setup | Fig. 1; one architecture, one data subset, unstated number of seeds |
| C2 | HTSR α tracks the pre-grokking → grokking transition (α falls toward 2 as test accuracy rises) | moderate (experiment) | Fig. 4, Table 1 |
| C3 | α < 2 identifies, and "invariably" heralds, the collapse | weak; contradicted in-paper | Fig. 4 for WD = 0, but in the WD = 0.01 run FC2 α ≈ 1.2 and traps are present without collapse (Fig. 6, Table 2) |
| C4 | Correlation traps appear only in the collapse phase | weak; internally inconsistent | Table 2 gives traps at grokking (1 ± 0) and in the non-collapsing WD > 0 run. Table 4 and §4.2 say none before collapse |
| C5 | Pre-grokking is caused by some layers being underfit (α ≥ 5) while others are trained (α ≤ 4) | weak (correlation, read as mechanism) | Table 1 (FC1 5.0 ± 0.7 vs FC2 2.9 ± 0.7); no intervention |
| C6 | ℓ² norm, activation sparsity, weight entropy and circuit complexity track the first two phases but not anti-grokking | weak–moderate | Fig. 5; judged by eye with no threshold for any of them. The norm's steepest rise is in fact in the collapse window |
| C7 | Grokking occurs without weight decay, with rising weight norm | moderate (experiment); confirms Golechha | Figs. 1 and 5 |
| C8 | Traps signify an "atypical" weight distribution that "will not generalize well" | assertion / hypothesis | §5; "hypothesized", "in some unspecified way" |
| C9 | HTSR α ≈ 2 is a "universal layer-convergence target" and "theoretically established" cutoff | assertion (imported) | abstract, §4.1; rests on [9]–[11], and App. E concedes it is not bidirectional |
| C10 | One can detect overfitting and generalisation collapse "without direct access to the test data" | weak | follows from C3, which its own control undercuts |

## Method

1. Train one small MLP for 10⁷ steps, logging checkpoints.
2. At each checkpoint, run WeightWatcher on each hidden weight matrix to get α (PL tail MLE with KS-chosen λ_min).
3. At each checkpoint, also shuffle each hidden weight matrix, fit a Marchenko–Pastur bulk, and count eigenvalues beyond its Tracy–Widom-adjusted edge.
4. Compute the ℓ² norm and Golechha's three progress measures (eqs. 7–10).
5. Compare the metrics' trajectories against the accuracy-defined phases by eye, repeating once with WD = 0.01.

## Concepts

- **Grokking / pre-grokking / anti-grokking.** Here these are phases of the *accuracy curves* (fit, then generalise, then lose generalisation). They are not phases of any representation-level quantity.
- **HTSR α.** The tail exponent of a layer's weight-correlation eigenvalue density. Lower means heavier-tailed, i.e. more spectral mass in a few large eigenvalues.
- **Correlation trap.** An outlier eigenvalue of the elementwise-randomised weight matrix, read as a rank-one (or higher) structure large enough to survive shuffling, i.e. a large shift in the mean of the weight entries.
- **Very-Heavy-Tailed (VHT) phase.** α < 2 in HTSR's taxonomy, read as over-correlation or overfitting.
- **Approximate local circuit complexity Λ_LC.** Summed KL between output distributions before and after zeroing 10% of the weights (eq. 10). It measures output sensitivity to pruning.
- **Absolute weight entropy.** H_abs(W) = −Σ|w_ij| log|w_ij| (eq. 9). It is not a Shannon entropy of a distribution. It goes negative once many |w| > 1, so under WD = 0 it falls mechanically as the norm grows (Fig. 5). That is my reading of the definition; the paper does not note it.

## Connections

- **The IB account under [THEORY-tmpd8w6r](../theory.d/THEORY-tmpd8w6r.md) ([LIT-324](../literature.d/LIT-324.md), [NOTE-298](NOTE-298.md)).** The paper measures no information quantity, so it neither corroborates nor refutes any of the three IB claims. Taking them one at a time:
  - *Fitting then compression in I(X;T).* Not measured. The three phases are defined by train and test accuracy, and the tracked quantities are weight-spectrum, activation and output-sensitivity statistics.
  - *Compression causes generalisation.* Orthogonal as stated. The paper does show that some *weight-level* concentration statistics keep moving the same way through generalisation and then through its loss, at least in the WD = 0 run: α keeps falling, traps appear, absolute weight entropy falls. So "a weight-level simplification coincides with generalisation" and "a weight-level simplification coincides with its collapse" are both on show. That is a caution against reading any monotone "simplification" statistic as the cause of generalisation. It is not evidence about I(X;T), and it does not meet [THEORY-tmpd8w6r](../theory.d/THEORY-tmpd8w6r.md)'s refuter ("compress without generalising"), which is stated for I(X;T).
  - *Compression driven by SGD noise.* Orthogonal. The optimiser is AdamW with batch 200 of 1,000, and noise is never varied. The collapse appears in the regime with *no* explicit regulariser, over 10⁷ steps.
- **The simplification question.** The grokking phase does coincide with functional simplification markers. Local circuit complexity (output sensitivity to pruning 10% of weights) falls from ~14 to ~0, and activation sparsity rises toward 1. In the WD = 0 run this happens while the weight norm is flat and then *rising*, so it is not a weight-norm simplification. None of these is I(X;T), and none is a representation-level information measure. The later anti-grokking phase is a further *concentration* of the weight spectrum (α < 2, rank-one traps, "even rank collapse" per §5). That is simplification in a spectral sense that goes with worse, not better, generalisation.
- **[LIT-345](../literature.d/LIT-345.md) / [NOTE-283](NOTE-283.md) (Nanda et al.).** Nanda's cleanup phase is a weight-norm fall under λ = 1 weight decay, and it is where test loss drops. Here, grokking with WD = 0 happens as the norm starts to *rise* (Fig. 5), so this grokking is not cleanup by weight decay. The two papers agree only that train-accuracy saturation and generalisation are separated by a hidden-progress phase. Nanda found no grokking at λ = 0 on modular addition ([NOTE-283](NOTE-283.md)). The MNIST/large-init setting here groks at WD = 0, as Power et al. did.
- **[LIT-341](../literature.d/LIT-341.md) / [NOTE-287](NOTE-287.md) (Power et al.).** Power's headline run also used no weight decay and generalised near 10⁶ steps. Power trained to a 10⁶ budget; this paper trains to 10⁷, which is where the collapse appears. Whether algorithmic-task grokking at WD = 0 also collapses past 10⁶ is not tested here or there.
- **[LIT-348](../literature.d/LIT-348.md) (McCandlish).** No gradient-noise measurement here, so no bearing.
- **Anthology.** The setup is Omnigrok's ([ANTH-LIT-540](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-540.md)). Omnigrok's LU picture has test loss U-shaped in weight norm, so it would predict test degradation as the norm grows past the Goldilocks zone. The norm does grow sharply through anti-grokking (Fig. 5). The paper does not consider this, and I have not checked it against [NOTE-282](NOTE-282.md) in the anthology. Varma et al.'s "ungrokking" ([ANTH-LIT-539](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-539.md)) is distinguished in §2 as retraining on a smaller dataset under WD. Nanda et al. is [ANTH-LIT-085](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-085.md).
- **Within this batch.** Saxe et al. (2018) is the published critique of [LIT-324](../literature.d/LIT-324.md)'s I(X;T) estimates. This paper does not touch that dispute. Zhou et al. (2025) finds its phase transition very early (10²–10³ iterations) in parameter and kernel dynamics. This paper's phases are defined over 10⁵–10⁷ steps by accuracy. The two describe different time scales and different quantities.

## Bearing on the record

- **For [THEORY-tmpd8w6r](../theory.d/THEORY-tmpd8w6r.md): no evidence either way on I(X;T).** The paper is orthogonal to all three IB claims. It can be cited only for the weaker, general point that a monotone "simplification" statistic of the weights (here the spectral exponent and a weight-entropy surrogate) can accompany first generalisation and then its collapse. So such a statistic falling is not by itself an explanation of generalisation. It would support the THEORY's "What this does not say" discipline, not its rejection argument.
- **For the grokking cluster ([LIT-341](../literature.d/LIT-341.md), [LIT-345](../literature.d/LIT-345.md)).** It adds a phase *after* grokking in a non-algorithmic, WD = 0 setting. It is one setup, and the phenomenon is plausible, but the diagnostic claims are weak.
- **ML practice.** This has more practical content than most of the record: a data-free monitor (WeightWatcher α) proposed for detecting overfitting in long training runs. Given C3's in-paper counterexample and the single setup, it is an anthology candidate as a *claim*, not as a practice. The anthology does not hold it.

## Limitations

- One architecture, one 1k-sample MNIST subset, one learning rate, and one WD value for the control. The run count is unstated and the seed is given as 0.
- The phase boundaries are chosen by eye from accuracy curves, and the metrics are compared by eye with no thresholds for the competitors.
- The central diagnostic is contradicted by the paper's own WD = 0.01 control, and the trap counts disagree between Tables 2 and 4.
- The output layer's α is not reported.
- The interpretation of α (the ranges, "α = 2 ideal") is imported from HTSR and SETOL work, part of it an unrefereed draft on GitHub. App. E concedes the α–generalisation map is "not yet fully understood" and not bidirectional.
- The mechanism of the collapse is left open ("in some yet undetermined way"). The "atypical distribution will not generalize" argument is an analogy with statistical estimators.
- It does not cite Omnigrok, whose LU account bears directly on a collapse accompanied by a growing weight norm. So the norm is dismissed without the one theory that makes a prediction about it.
- The abstract's "invariably" and "α alone delineates all three phases" claim more than the body shows.

## Open questions

- In runs where a layer sits at α < 2 without collapse (as here with WD = 0.01), what distinguishes it from the collapsing case? Is it the average α, the trap count in FC1, or the norm?
- Is anti-grokking the LU mechanism run in reverse: under WD = 0, does the norm grow past Omnigrok's critical w_c and test loss follow the U back up? A norm-constrained WD = 0 run would separate the HTSR and LU readings.
- Does algorithmic-task grokking at WD = 0 (Power et al.'s setting) also collapse past 10⁶–10⁷ steps?
- Does any representation-level information quantity (I(X;T) with a network-intrinsic noise model) track these three phases? The paper gives no data on this.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The abstract says the collapse is "invariably heralded by α < 2 and the appearance of Correlation Traps", and contribution 4 (§1) says "when the HTSR PL exponent α < 2, this identifies the collapse". In the paper's own WD = 0.01 control, FC2's α falls to ≈1.2 by ~10⁶ steps and stays there to 10⁷ (Fig. 6), and Table 2 counts traps in both layers (FC1 2.0, FC2 1.0) in the late window. Yet test accuracy plateaus at ~0.83–0.85, with no collapse. App. C reports only that the *average* α "plateau[s] around the critical value of α ≈ 2" and does not mention FC2. On the paper's own data, α < 2 in a layer, with traps, is not sufficient for collapse.
- "Only the HTSR α can distinguish between all 3 phases" and "the l2 weight norm … fail[s] to distinguish grokking from anti-grokking" are both overstated. In Fig. 5 (WD = 0) the norm is flat at ~90 until ~10⁵ steps. It then rises, and most steeply (to ~420) inside the anti-grokking window. The paper sets no threshold for the norm. It judges the other metrics by "negative control" (they keep moving in the same direction) while crediting α with a threshold (α = 2) that it calls "theoretically established" and "universal". Its own App. E concedes the α–generalisation link "is not a strictly bidirectional implication".
- The record should note several internal inconsistencies.
  - **Traps at grokking.** Table 2 gives FC1 1 ± 0 and FC2 1 ± 0 correlation traps at the grokking point (WD = 0). Table 4 gives 0 traps for FC1 at grokking, and §4.2 says "neither layer shows evidence of correlation traps until the anti-grokking phase".
  - **The MP variance.** Table 4 gives σ_MP ≈ 0.949 at anti-grokking, and the App. D prose says "σ_mp ≈ 2" for the same fit.
  - **Seeds.** Table 1 and the ±1σ bands in Figs. 1 and 4 imply several seeds ("Various seeds are used"), but Table 3 says "Random Seed 0 (for all libraries)". The number of runs is never stated.
  - **Pre-grokking in Table 4.** The row is described as "Immediately after initialization" in App. D, but as ~10⁵ steps in the table caption.
  - **Figure captions.** The Fig. 4 caption ("Top … Middle … Bottom") does not match the 2×2 figure, which also contains an accuracy panel. The Fig. 5 caption likewise lists three panels for a four-panel figure.
- The collapse is from ~0.85 to ~0.45–0.5 test accuracy (Fig. 1 caption: "collapses (to 0.5)"), not to chance (0.1). Training accuracy also dips slightly at the very end of Fig. 1, so "training accuracy stays perfect" (abstract) is approximately, not exactly, what the plot shows.
- Pre-grokking is not a flat, chance-level plateau here. In Figs. 1 and 4 test accuracy climbs from ~0.13 to ~0.4 between 10² and 10⁵ steps, drawn as a straight segment on the log axis, which suggests sparse logging in that interval. §4.1 places the grokking rise "around 10⁴–10⁵ steps", but the Fig. 1 caption and the shading place it after ~10⁵.
- The setup (1k MNIST, depth-3 width-200 MLP, MSE on one-hot targets, AdamW, Kaiming-uniform init scaled ×8) is exactly the MNIST grokking recipe of Liu, Michaud & Tegmark's *Omnigrok* ([ANTH-LIT-540](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-540.md)), which the paper does not cite. It cites instead Liu et al.'s NeurIPS 2022 "effective theory" paper as [6] for the weight-norm account.
