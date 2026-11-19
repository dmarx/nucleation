---
status: Read
paper: LIT-tmp3su77
title: 'Zbontar and others 2021 — Barlow Twins: Self-Supervised Learning via Redundancy Reduction'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2103.03230 (HTTP 200, 2.43 MB PDF;
    header "arXiv:2103.03230v3 [cs.CV] 14 Jun 2021"; first page "Proceedings
    of the 38th International Conference on Machine Learning, PMLR 139,
    2021"). Kind of copy: arXiv preprint, the authors' own version (v3) of
    the ICML 2021 paper; lawful (step 5: arXiv). Date: 2026-11-19. Nothing
    stopped the fetch. Text: pdftotext (no -layout) to dl/text.txt. Read:
    abstract, §1, §2 (method, the loss, the IB motivation, implementation),
    §3 (results: linear, semi-supervised, transfer, detection), §4 ablations
    (loss terms, normalization, batch size, augmentations, projector width
    and depth, symmetry breaking, BYOL with larger heads, λ sensitivity), §5
    discussion (InfoNCE, asymmetric twins, whitening, clustering, Noise As
    Targets, IMAX, future directions), Appendix A (connection to the
    information bottleneck), Appendix B-C (evaluation protocols) briefly.
    Skipped: the numeric cells of Tables 1-4 and 6-7 (extraction scrambles
    them; only Table 5's loss-ablation numbers were read, from the extracted
    column order); Figures 2-5 read from captions and text only. RECHECK
    (record/ searched for: Barlow, redundancy reduction, factorial code,
    information bottleneck, cross-correlation, whitening, BYOL/SimSiam): -
    Not held as a work. Verdict stands. - Held entries that carry it:
    THEORY-229 (Active; Simon et al. 2023, LIT-242, NOTE-741): gradient flow
    of a symmetrized Barlow Twins loss on a linear or kernel model learns
    eigenvectors stepwise; LIT-228 (linear Barlow Twins as CCA);
    QUESTION-141 (asymmetric objectives) discusses Barlow Twins;
    SYNTHESIS-034 cites THEORY-229. NOTE-165 and NOTE-752 mention H.
    Barlow's redundancy principle. These are the record's existing analyses
    of the method; this reading is the first of the method's own paper.
date: '2026-11-19'
---
<!-- inactive-ok-file: CLAIM-tmpw8xkt SYNTHESIS-034 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmptbvgq: Zbontar and others 2021 — Barlow Twins: Self-Supervised Learning via Redundancy Reduction

## Contribution

Zbontar, Jing, Misra, LeCun and Deny propose a joint-embedding self-supervised loss that standardizes each embedding unit over the batch, computes the cross-correlation matrix between the embeddings of two distorted views, and pushes it toward the identity: the diagonal toward 1 (invariance to the distortions) and the off-diagonal toward 0 (redundancy reduction, after H. Barlow's principle). The construction avoids collapse without negatives, large batches, predictors, stop-gradients or momentum encoders, and keeps improving with very wide embeddings. The authors connect it, through stated approximations, to an information-bottleneck objective under a Gaussian assumption.

## Key results

- §2.1, the two terms: the invariance term "makes the embedding invariant to the distortions applied"; the redundancy reduction term "decorrelates the different vector components of the embedding".
- §1 and Figure 1: the loss is said to avoid collapse by construction: "naturally avoiding trivial constant (i.e. collapsed) embeddings".
- §4, Table 5 (300-epoch ablation, ImageNet linear top-1): "removing the invariance term (on-diagonal term) or the redundancy reduction term (off-diagonal term) of our loss function leads to worse/collapsed solutions"; the extracted table gives 57.3% for "Only invariance term (on-diag term)" and 0.1% for "Only red. red. term (off-diag term)", against 71.4% for the full loss. Replacing cross-correlation with cross-covariance (no batch standardization, no BN in the projector) drops to 53.4%.
- §4, batch size (Figure 2): "unlike S IM CLR, our model is robust to small batch sizes", almost unaffected at 256.
- §4, dimensionality (Figure 4): "our method keeps improving with all output dimensionality tested", up to 16384, while SimCLR and BYOL saturate.
- §4, Table 6: adding a predictor and/or stop-gradient slightly decreases performance; "Our loss function avoids these trivial solutions by construction, even in the case of symmetric networks."
- §5, comparison with InfoNCE: both losses have an invariance term and a variability term relying on batch statistics, but "the I NFO NCE objective maximizes the variability of the embeddings by maximizing the pairwise distance between all pairs of samples, whereas our method does so by decorrelating the components of the embeddings".
- §5 and Appendix A: the loss "can be interpreted as a proxy entropy estimator of the distribution of embeddings under a Gaussian parametrization"; the link to the IB objective holds only "through the following simplifications and approximations" (Gaussian entropy as log-determinant, β > 1, Frobenius norm of the cross-correlation in place of the log-determinant, cross- in place of auto-correlation).
- §5, on BYOL and SimSiam: "these asymmetric methods cannot be described as the optimization of an overall learning objective".

## Assumptions

- Each embedding unit is mean-centred and divided by its standard deviation over the batch before the cross-correlation is formed; this standardization is what keeps the diagonal target meaningful (§2.1, Algorithm 1).
- The IB reading assumes Gaussian embeddings and replaces the log-determinant by a Frobenius-norm surrogate; the authors claim, without proof, that the surrogate "has the same global optimum".
- Positive pairs are two distortions of one image drawn from a BYOL-style augmentation distribution; the method is "not robust to removing some types of data augmentations".

## Concepts

- Cross-correlation matrix between the twin embeddings, computed over the batch, entries in [−1, 1].
- Invariance term (on-diagonal) and redundancy reduction term (off-diagonal), traded off by λ (5·10⁻³ in practice).
- Redundancy reduction / factorial code (Barlow 1961): recoding redundant inputs into statistically independent components.
- Soft whitening: the off-diagonal term as a soft version of W-MSE's hard whitening.
- Information bottleneck for SSL: informative about the sample, uninformative about the distortion.

## Bearing on the record

- CLAIM-481 (the note of 2026-11-19, A27: pure diffusion collapses each component, so non-collapse terms are needed): supports the need, with a qualification on the mechanism. Barlow Twins' anti-collapse acts on the feature dimensions (decorrelate units, each with unit batch variance), not on pairs of samples. Table 5 is the evidence that the decorrelation term alone yields nothing (0.1%), while the invariance term alone, with batch standardization holding each unit's variance at one, does not collapse fully (57.3%). So in this method part of the non-collapse work is done by the standardization, not by the redundancy term.
- CLAIM-tmpw8xkt: leaves open. The invariance term identifies the two views; the paper does not discuss which coarser classes form or whether they are reused.
- LIT-228: consistent but not restated. LIT-228's reading of linear Barlow Twins as CCA is LIT-228's own result on a modified loss; this paper makes no spectral or CCA claim. It relates itself to IMAX (Becker and Hinton), InfoNCE, W-MSE and the information bottleneck instead.
- LIT-249, LIT-231: LIT-231 lists Barlow Twins among volume-maximizing methods; this paper's own reading, a Gaussian entropy proxy, is consistent with that classification.

## Limitations

- The information-theoretic justification rests on several stated approximations and an unproved claim that the decorrelation surrogate has the same optimum; there is no theorem.
- Evidence is empirical, on ImageNet with ResNet-50 and one augmentation pipeline; the ablations are single runs at 300 epochs.
- The paper does not analyse its learning dynamics or what representation the optimum is; the CCA reading is from LIT-228, not from here.
- Collapse is discussed as complete (constant output) or "informational" (redundant units) only; dimensional collapse is not measured.
