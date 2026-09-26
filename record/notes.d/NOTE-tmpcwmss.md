---
status: Skimmed
paper: LIT-tmp5lqr2
title: 'The Conditional Entropy Bottleneck'
version: 1
date: '2026-09-26'
summary: >-
  Training a representation to minimize I(X;Z|Y) while maximizing I(Y;Z) — the Conditional Entropy Bottleneck, targeting the "Minimum Necessary Information" point I(X;Y)=I(X;Z)=I(Y;Z) — empirically improves accuracy, adversarial robustness, OoD detection and calibration and refuses to memorize random labels.
---
<!-- inactive-ok-file: LIT-tmp5lqr2 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpcwmss: The Conditional Entropy Bottleneck

## Contribution

Adversarial vulnerability, poor out-of-distribution detection, miscalibration and memorization of random labels are grouped as failures of "robust generalization". Fischer hypothesizes a common cause: models retain too much information about the training data. He proposes the Minimum Necessary Information (MNI) criterion for judging representations and a training objective, the Conditional Entropy Bottleneck, closely related to the Information Bottleneck, that targets it. Experiments comparing CEB with deterministic and Variational IB models across datasets and robustness challenges give strong empirical support for the hypothesis.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §3 (pp. 2–3): MNI defined by information, necessity (I(X;Y) ≤ I(Y;Z)) and minimality (I(X;Z) ≤ I(X;Y)); the MNI point is I(X;Y)=I(X;Z)=I(Y;Z) — in effect a minimal sufficient representation of X for Y; for deterministic datasets it is approachable.
- §4 (pp. 3–4): because Z←X↔Y, at the MNI point all three conditional informations vanish, so compression is minimizing I(X;Z|Y); variational bounds with a forward encoder e(z|x), backward encoder b(z|y) and classifier c(y|z) give the tractable VCEB objective (Eq. 15).
- §5 and Figs. 1–2 (p. 4): CEB and IB are equivalent for γ = β−1, but CEB "rectifies" the information plane so I(X;Z|Y) ≥ 0 measures in absolute terms how far one is from optimal compression, which IB cannot; reparameterized by ρ = log γ, with the MNI point at ρ = 0.
- §1 (p. 2) and §7: claimed empirical results — better accuracy, adversarial robustness, OoD detection, calibration, and failure to learn information-free (randomly labeled) datasets; §2 frames these as conditions RG1–RG3.
- §3 (p. 3): the adversarial-robustness link is stated explicitly as a hypothesis tested empirically, not derived.

## Open questions

- MNI is an operational version of a minimal sufficient statistic for the label — directly on the heading's theme; a deeper reading should check how the paper relates MNI to sufficiency formally, if it does.
- Separate the practice claim (use CEB as a training objective) from the theory claim (robustness failures are caused by excess retained information); the second is hypothesized and supported only empirically — candidates for a SOTA and a THEORY filed apart.
- Check whether results replicate beyond Fashion-MNIST/CIFAR-10 and whether CEB is used in practice today.
