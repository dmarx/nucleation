---
status: Read
paper: LIT-tmpf5qpo
title: 'Bardes and others 2022 — VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2105.04906 (HTTP 200, 0.87 MB PDF;
    header "arXiv:2105.04906v3 [cs.CV] 28 Jan 2022"; running head "Published
    as a conference paper at ICLR 2022"). Kind of copy: arXiv preprint, the
    authors' own version (v3) of the ICLR 2022 paper; lawful (step 5:
    arXiv). Date: 2026-11-19. Nothing stopped the fetch. Text: pdftotext (no
    -layout) to dl/text.txt; pdftotext warned "xref num 1087 not found ...
    try to reconstruct" and recovered. Square-root glyphs are dropped in
    extraction (e.g. the regularized standard deviation in Eq. 2 appears as
    "Var(x) + ,"). Read: abstract, §§1-7 (introduction, related work, the
    method and loss Eqs. 1-6, implementation, ImageNet and transfer results,
    multi-modal MS-COCO, the asymmetric-network and weight-sharing analyses
    with Tables 4-5, conclusion); Appendix A (relation to other methods:
    Barlow Twins, W-MSE, BYOL and SimSiam, SimCLR, SwAV, OBoW); Appendix D.4
    (loss coefficients, Table 7) and D.5 (normalizations, Table 8). Skipped:
    Appendix B-C (algorithm, optimization protocols), Appendix D.1-D.3 and
    D.6-D.8 except their headings and the D.8 references from Appendix A;
    numeric cells of Tables 1-3 (scrambled in extraction). RECHECK (record/
    searched for: VICReg, variance hinge, standard deviation, collapse,
    dimensional collapse, BYOL/SimSiam): - Not held as a work. Verdict
    stands. - Held entries: LIT-228 / NOTE-752 (and the earlier skim
    NOTE-199) read VICReg as Laplacian eigenmaps after replacing the hinge
    (NOTE-752 line 81 notes the replacement; line 293 asks whether the
    closed forms survive the hinge); LIT-231 / NOTE-850 and QUESTION-171
    (VICReg's uniform-cluster prior); NOTE-716 and LIT-871 mention
    dimensional collapse; QUESTION-141 (asymmetric methods), on which
    Appendix A's correlation measurements bear.
date: '2026-11-19'
---
<!-- inactive-ok-file: CLAIM-tmpw8xkt — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: NOTE-199 — Superseded; cited in this filing of 2026-11-19 -->

# NOTE-tmpprl89: Bardes and others 2022 — VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

## Contribution

Bardes, Ponce and LeCun propose a joint-embedding self-supervised loss with three terms computed on the embeddings: invariance (the mean squared distance between the two views' embeddings), variance (a hinge keeping the batch standard deviation of each embedding variable above a target γ = 1) and covariance (the summed squared off-diagonal entries of each branch's covariance matrix, borrowed from Barlow Twins). Variance and covariance are applied to each branch separately, so the two branches need share neither weights nor architecture nor input modality. The paper's stated main contribution is the variance term, an explicit guard against collapse that needs no normalization, negatives, predictor, stop-gradient or momentum encoder.

## Key results

- §1, the terms: variance is "a hinge loss to maintain the standard deviation (over a batch) of each variable of the embedding above a given threshold"; covariance "decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated".
- §1: "The main contribution of this paper is the Variance preservation term, which explicitly prevents a collapse due to a shrinkage of the embedding vectors towards zero."
- §4, Eq. (1) and text, the standard deviation, not the variance, is essential: "if we take S(x) = Var(x) in the hinge function, the gradient of S with respect to x becomes close to 0 when x is close to x̄. In this case, the gradient of v also becomes close to 0 and the embeddings collapse."
- §4, Eq. (6): loss = λ s(Z, Z′) + µ[v(Z) + v(Z′)] + ν[c(Z) + c(Z′)], with λ = µ = 25, ν = 1 on ImageNet.
- Appendix D.4, Table 7 (100 epochs, linear top-1): invariance alone collapses; invariance plus covariance collapses; invariance plus variance 57.5%; all three 68.6%. "Without variance regularization the representations immediately collapse to a single vector and the covariance term, which has no repulsive effect preventing collapse, has no impact." And "The invariance term is absolutely necessary and without it the network can not learn any good representations."
- §5.1, Table 1: 73.2% ImageNet linear top-1 at 1000 epochs, three seeds, "the difference between worse and best run is lower than 0.1% accuracy for linear classification".
- §6, Table 4: "without VR, the representations collapse, and both stop-gradient (SG) and PR are necessary"; adding the variance term to BYOL and SimSiam helps slightly, which the authors attribute to "very slow collapse" in those methods.
- §6, Table 5: with branches of different weights or architectures VICReg loses less than Barlow Twins (2.1% vs 4.5% from shared to different weights).
- Appendix A, on BYOL and SimSiam: their stop-gradient and moving average "play the role of the repulsive term used in other methods", and "even without covariance regularization, SimSiam and BYOL naturally minimize the average correlation coefficient of the representations."
- Appendix D.5, Table 8: the best setting uses no normalization of the embeddings; standardizing them costs about 0.2%.

## Assumptions

- Positive pairs are two augmentations of one image (or an image and its caption in the MS-COCO experiment).
- Collapse is guarded per variable (variance) and per pair of variables (covariance) within a batch; nothing constrains higher-order dependence except through the expander, whose role is said to be to make decorrelation reduce dependencies "not just the correlations".
- Hyperparameters were tuned on ImageNet (λ = µ > 1, ν < µ for stability).

## Concepts

- Invariance, variance and covariance regularization.
- Complete collapse (all inputs to one vector) versus informational collapse (redundant, correlated variables).
- Expander: the network between representation and embedding, discarded after training.
- Branch-wise regularization: each branch's statistics are regularized separately, which allows non-shared and multi-modal branches.

## Bearing on the record

- LIT-228: qualifies. LIT-228 and NOTE-752 read VICReg as Laplacian eigenmaps after replacing the hinge on the standard deviation by a squared variance term. This paper, which never mentions Laplacians or spectra, says the actual hinge must be on the standard deviation and that a hinge on the variance collapses because its gradient vanishes near the mean (§4). The equivalence is therefore an equivalence for a loss the authors report does not train; it does not describe the dynamics of the loss they use. That is a fact about optimization, not about the optimum, so it leaves LIT-228's closed forms intact as statements about minimizers; NOTE-752's open question about the hinge stands, with this paper's remark as evidence that the difference matters in training.
- CLAIM-481 (the note of 2026-11-19, A27: pure diffusion collapses each component; non-collapse terms are needed): supports. Table 7 is direct evidence: the invariance term alone, the alignment energy whose gradient flow A27 calls Laplacian diffusion, collapses to a single vector; covariance alone cannot stop it; variance is what holds the spread. The paper does not itself describe the invariance term as diffusion.
- CLAIM-tmpw8xkt: leaves open. VICReg identifies views of one image; which coarser classes emerge, and whether they are closed under further operations, is not studied.
- LIT-231: consistent; VICReg is one of the volume-maximizing methods LIT-231 analyses, and nothing here addresses the cluster-size prior.
- QUESTION-141: bears on it empirically, not theoretically: BYOL and SimSiam reduce average correlation without a covariance term (Appendix A, Figure 5), so their asymmetry does some of the decorrelating a symmetric objective does by a term.

## Limitations

- No theory: the paper characterizes neither the optimum nor the dynamics.
- Ablations are 100-epoch single runs; only the 1000-epoch linear result is reported over three seeds.
- The collapse analysis distinguishes complete and informational collapse but does not measure dimensional collapse directly.
- The asserted role of the expander (decorrelation at the embedding reducing dependence at the representation) is studied empirically in Appendix D, which this reading skipped.
