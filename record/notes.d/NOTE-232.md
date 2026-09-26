---
number: 232
status: Skimmed
formerly:
- NOTE-tmpv3qzd
paper: LIT-247
title: 'Tschannen et al., on MI maximization for representations'
version: 1
date: '2026-09-26'
summary: >-
  The success of InfoNCE-style representation learning cannot be attributed to mutual information itself: MI is invariant under invertible reparametrizations, invertible encoders that maximize true MI can be worse than raw pixels, and tighter MI bounds from higher-capacity critics can give worse representations.
---
<!-- inactive-ok-file: LIT-247 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-232: Tschannen et al., on MI maximization for representations

## Contribution

Many unsupervised and self-supervised methods train feature extractors by maximizing an estimate of mutual information between views. The authors point out that MI is hard to estimate and, being invariant under invertible transformations, can favour entangled representations. They argue with experiments that these methods' success depends strongly on the inductive biases of the encoder architecture and of the MI estimator's parameterization, not on MI, and connect InfoNCE to triplet losses from deep metric learning as a more plausible account.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Eq. 1: I(X;Y) = D_KL(p(x,y) ‖ p(x)p(y)) = E_{p(x,y)}[log p(x,y)/(p(x)p(y))]; MI is invariant under homeomorphic reparametrizations of X and Y.
- §2 end: "any distribution-free high-confidence lower bound on entropy requires a sample size exponential in the size of the bound" (citing McAllester and Stratos 2018, spelled "Statos" in the text).
- Contribution list (§2, before §3): (1) with bijective encoders true MI is maximal for every parameter setting yet linear-probe accuracy improves during training, and some invertible encoders are worse than raw pixels; (2) the I_EST objective drives initially invertible encoders towards ill-conditioned ones; (3) for I_NCE and I_NWJ, simple critics with looser bounds can give better representations than high-capacity critics with tighter ones; (4) at equal MI lower-bound value, encoder architecture matters more than the estimator.
- §4: InfoNCE is rewritten and connected to a (k-plet) triplet loss from metric learning, offered as the better explanation.

## Open questions

- It is the limit on what the density-ratio/MI reading buys: the optimal critic being a log RN derivative is a fact about the critic at the optimum, not an explanation of why the encoder's features are good.
- Check the §3 experiments' setups (which bounds, critics and datasets) before citing any specific number.
