# Reader notes: maennel (Maennel et al. 2020, arXiv 2006.10455)

## 2026-11-19 Copy located
- arXiv PDF https://arxiv.org/pdf/2006.10455 (v2? camera-ready, 41 pp, created 2020-11-12) fetched without challenge; text extracted locally.

## Reading done (main text in full; App. A, B, E, F read; C, D skimmed)
- Note: arXiv v2 lists 7 authors (adds Daniel Keysers), not 6.
- Design: upstream = random labels on CIFAR10/ImageNet subset; head replaced; per-layer weights rescaled to init l2 norm (not ResNet18); downstream = disjoint fresh examples, real or random labels, same LR/schedule. Cost = training-accuracy curves / AUC, not steps-to-threshold.
- (a) yes: pretrained vs from-scratch, same hyperparameters; positive and negative transfer (Fig 1; App B scatter, 960+960 CIFAR models, 600+600 ImageNet).
- (b) no matching on first-stage performance; upstream train accuracy never reported. Organizations not compared; "mechanism" split is alignment (early layers) vs specialization (late layers, dead ReLUs).
- (c) partly: replace pretrained conv filters by Gaussian samples from learned covariance (Fig 5) recovers gain; data-only constructed init (Table 1, App E.3); wrong eigenvectors hurt (Tables 5-6). Layer-count transfer (Fig 6). Width mitigates negative transfer (Fig 8).
- Doubts: Table 1 "matches" pretraining only at 100 iterations; at 1000 iters train 0.68 vs Table 7's 0.78. ImageNet Exp. B: no positive transfer except unrescaled ResNet18.
