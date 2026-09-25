---
status: Skimmed
paper: LIT-tmpckqmo
title: 'Hierarchical Pitman-Yor topic models'
version: 1
date: '2026-09-25'
summary: >-
  Hierarchies of Pitman-Yor processes can be assembled as modular "blocks" and fit with a single collapsed, blocked Gibbs sampler (extending Chen et al. 2011), making nonparametric topic models with auxiliary data practical; the resulting Twitter-Network Topic Model beats HDP-LDA and a nonparametric author-topic model on perplexity.
---

<!-- inactive-ok-file: LIT-tmpckqmo — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmp9ca8a: Hierarchical Pitman-Yor topic models

## Contribution

The Dirichlet process and its generalization the Pitman-Yor process take distributions as parameters and can be stacked into hierarchical nonparametric Bayesian models. The article gives efficient inference methods for such hierarchies and applies them to latent-variable text models, i.e. topic models. It proposes a general design framework and then a specific nonparametric model for social-media text, using tweets as the case study. The nonparametric model is reported to outperform parametric baselines in goodness of fit and in applications.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Positioning: variational methods for HDP-style models are hard to extend to complex models; a collapsed and blocked Gibbs sampler (Chen et al. 2011) reportedly beats both variational methods and the Chinese restaurant franchise, and is the basis here (§1).
- Framework: represent each PYP node via the Chinese restaurant process with customer/table counts; the posterior factorizes by node, so models are built from reusable blocks and the sampler is decrement-counts / resample topic / update hyperparameters (§3-4, Algorithm in §4.4).
- Twitter-Network Topic Model (TNTM) jointly models text, hashtags, authors and the follower network, coupling HPYP with a Gaussian-process "random function" network model (§5.2).
- Results: TNTM test perplexity ~505 vs ~664 (nonparametric ATM) and ~840 (HDP-LDA) on the T6 tweet corpus, and better network log-likelihood than the random-function network model alone (Table 4).
- Ablation: hashtags give the largest perplexity gain, then authorship; power-law discounts matter little for perplexity but most for network likelihood (Table 5, §5.6.3).
- Clustering: TNTM beats tweet-pooling LDA baselines (Mehrotra et al. 2013) on purity and NMI except a tie on one dataset (Table 6).

## Open questions

- Main reusable contribution is the modular CRP-count representation and sampler; check the table-count sampling details (§4, Appendix A) if implementing.
- Empirical comparisons are against 2013-era baselines on a small, filtered corpus (150 authors); results say little about modern neural topic or embedding methods.
- ML link: PYP discounts give power-law word statistics, relevant background for language modelling priors; otherwise historically rather than currently relevant to ML practice.
