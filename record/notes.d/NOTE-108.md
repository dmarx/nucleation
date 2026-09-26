---
number: 108
status: Skimmed
formerly:
- NOTE-tmp943v3
paper: LIT-162
title: 'Søgaard — Is unsupervised clustering somehow truer?'
version: 1
date: '2026-09-26'
summary: >-
  Neither the "No-Bias" nor the "Simplicity-Truth" argument shows unsupervised clustering is epistemically superior to supervised classification; since clusterings can be derived by supervised classification, supervised methods are at least as justified.
---
<!-- inactive-ok-file: LIT-187 — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->

<!-- inactive-ok-file: LIT-162 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-108: Søgaard — Is unsupervised clustering somehow truer?

## Contribution

Philosophers of science have questioned the epistemic standing of machine-learning methods, and some have argued that unsupervised clustering is better justified than supervised classification. Søgaard names two such arguments. The No-Bias Argument says clustering is less shaped by scientists' preconceptions. The Simplicity-Truth Argument says parametric simplicity bears on truth in clustering in a way it does not in supervised learning. He argues both are fallacious, and that supervised classification is at least as justified as unsupervised clustering.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 frames the question: each partitioning is a hypothesis drawn from a Bell-number-sized space. §1.1 separates sample bias, label bias and inductive bias.
- §1.2 states the No-Bias Argument: clustering escapes label bias, and its sample bias is cheap to mitigate. §1.3 states the Simplicity-Truth Argument, quoting Rochefort-Maranda & Liu (2020) that simplicity links to truth only in unsupervised contexts.
- §2 rebuts the No-Bias Argument via sample bias (§2.1.1), label bias (§2.1.2) and epistemic value (§2.2). §2.3 adds considerations that favour supervised methods, such as computational efficiency and convergence: a GMM trained with EM versus Naive Bayes, which have the same expressive power at fixed parameter size.
- §3 rebuts the Simplicity-Truth Argument. On function estimation (§3.1), clustering can be reduced to supervised classification. On parametric simplicity (§3.2), the technical literature treats overfitting as a live issue in clustering (Hansen & Larsen 1996), and k works the same way across both paradigms. The reduction then yields a reductio against simplicity playing a distinctive role.
- §4: both arguments rest on a picture of clustering that conflicts with the technical literature. Reviewers pointed to the Watson–Sterkenburg debate as context (see [LIT-187](../literature.d/LIT-187.md)).

## Open questions

- A direct counterweight to claims, including Watson's ([LIT-187](../literature.d/LIT-187.md)), that unsupervised structure discovery is less theory-laden. This is relevant wherever the anthology treats clustering or representation learning as discovery.
- Check the reduction of clustering to supervised classification (§3.1): is it general, or does it rely on the easy, well-separated cases discussed in the philosophical literature?
- Check whether the argument extends to self-supervised learning, which the paper does not appear to address.
