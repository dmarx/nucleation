---
status: Skimmed
paper: LIT-tmph7seu
title: 'Balestriero, Bottou & LeCun 2022 — regularization is class-dependent'
version: 1
date: '2026-09-26'
summary: >-
  Regularizers tuned by cross-validation for average accuracy — random-crop augmentation and even uninformed weight decay — raise mean test accuracy while sharply lowering it on particular classes (e.g. ImageNet "barn spider" 68%→46% with random crop), and this class-dependent bias carries over to transfer tasks.
---
<!-- inactive-ok-file: LIT-tmph7seu — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpagj8n: Balestriero, Bottou & LeCun 2022 — regularization is class-dependent

## Contribution

Deep networks rely on regularizers such as data augmentation and weight decay, with their strength chosen by cross-validation on average performance. The authors show that such regularization reduces model complexity unevenly across classes: the setting that is best on average can be very poor on some classes. The effect appears not only with semantically informed augmentation but also with weight decay, and it persists after transfer — an ImageNet-pretrained ResNet-50 evaluated on iNaturalist loses a large share of accuracy on some classes when random crops were used in pretraining. They conclude that regularizers without class-dependent bias remain an open problem.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Fig. 1 (pp. 1–2): framed against structural risk minimization — deep-learning practice picks one complexity level that is best on average, whereas per-class risk curves disagree on the optimum.
- §2.1–2.2 (pp. 3–5): any augmentation that is not label-preserving introduces bias; Fig. 2 shows random crop stays label-preserving down to 8% of the image for some classes but loses label information near 50% for others.
- §2.3, Fig. 4 (p. 6): sensitivity analysis over the random-crop lower bound (ResNet-50 on ImageNet, 20 runs) shows per-class accuracy moving in opposite directions as the average improves.
- §2.4, Fig. 5 (p. 7): the same class-dependent behaviour occurs when varying weight decay (10 runs), so the bias is not only a matter of badly designed augmentations.
- §2.5, Fig. 6 (p. 8): with a frozen backbone and linear probe on iNaturalist, pretraining augmentation strength changes per-class downstream accuracy, so selecting on source-average accuracy can deploy a model poor on some target classes.

## Open questions

- A practice-relevant warning: reporting only average accuracy hides regularization-induced per-class regressions; supports evaluating per-class or worst-class metrics when tuning augmentation/weight decay.
- Check the magnitude of the effect relative to run-to-run variance per class (ImageNet has 50 validation images per class).
- Only loosely tied to the "spectral approximation" heading; its link is via Balestriero's line on augmentations defining the similarity graph (cf. k17).
