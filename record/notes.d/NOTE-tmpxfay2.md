---
status: Skimmed
paper: LIT-tmp0jmv4
title: 'Poole et al., variational bounds of mutual information'
version: 1
date: '2026-09-26'
summary: >-
  Every variational lower bound on mutual information in use — Barber–Agakov, Donsker–Varadhan/MINE, NWJ/f-GAN-KL, InfoNCE — is one family, tight at a critic that is a function of the log density ratio log p(y|x)/p(y), and InfoNCE is the multi-sample member that trades variance for a hard ceiling of log K.
---
<!-- inactive-ok-file: LIT-tmp0jmv4 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpxfay2: Poole et al., variational bounds of mutual information

## Contribution

The paper puts the neural-network-parameterized lower (and some upper) bounds on mutual information into a single framework. It finds that existing lower bounds degrade when the true MI is large, with either high bias (InfoNCE) or high variance (NWJ, MINE-style). It proposes a continuum of interpolated bounds that trade bias against variance, and characterizes bounds and gradients empirically on controlled high-dimensional problems, including decoder-free representation learning.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.2, Eq. 3–7: with the energy-based family q(x|y) = p(x)e^{f(x,y)}/Z(y), the unnormalized Barber–Agakov bound is tight when f(x,y) = log p(y|x) + c(y); Jensen gives Donsker–Varadhan (Eq. 5); the tractable TUBA bound (Eq. 6) with a(y)=e recovers NWJ (Eq. 7), whose unique optimal critic is f*(x,y) = 1 + log p(x|y)/p(x). The paper notes that a Monte-Carlo I_DV as in MINE is neither an upper nor a lower bound.
- §2.3, Eq. 8–10: the multi-sample NWJ bound with a(y; x_{1:K}) the batch Monte-Carlo partition estimate becomes exactly InfoNCE (Eq. 10); the text says this "provides a proof" that I_NCE is a lower bound on MI, and footnote 2 adds that van den Oord et al.'s derivation "relied on an approximation, which we show is unnecessary" — the proof is Eq. 8–10 themselves.
- §2.3, after Eq. 10: the optimal critic for I_NCE is written as f(x,y) = log p(y|x) + c(y), citing Ma & Collins (2018); I_NCE is upper-bounded by log K, so it is loose when I(X;Y) > log K, and the optimal critic does not depend on batch size.
- §2.6: the optimal critics of both I_NWJ and I_NCE are functions of the log density ratio log p(y|x)/p(y), so any log-density-ratio estimator yields an MI lower bound; the authors train the ratio with a Jensen–Shannon objective and evaluate with NWJ ("I_JS").
- Figure 2: on correlated Gaussians with MI stepping up, I_NCE at batch size 64 saturates while single-sample bounds track MI with high variance.

## Open questions

- This is the cleanest place where "the optimal contrastive critic is the density ratio" and "InfoNCE ≤ log K" are stated as properties of a bound, rather than CPC's approximate derivation ([ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md), appendix A.1, which uses an ≈ step).
- Check the index convention: Eq. 10 normalizes over y_j for fixed x_i, under which the free term of an optimal critic should be a function of x_i; the text writes c(y). Whether this is a notational swap in the paper or my misreading is unverified.
- §2.5 (structured bounds with tractable encoders) is the bound [LIT-226](../literature.d/LIT-226.md) (CEB) cites in its footnote 7; worth reading in full for that link.
