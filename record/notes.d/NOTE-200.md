---
number: 200
status: Skimmed
formerly:
- NOTE-tmp6768d
paper: LIT-236
title: 'Rate-distortion generalization bounds'
version: 1
date: '2026-09-26'
summary: >-
  Defining an algorithm's compressibility in source-coding terms shows that the Xu–Raginsky mutual-information bound is really a lossless compression rate, and allowing lossy compression yields bounds via the rate-distortion dimension that stay meaningful where I(S;W) is huge.
---
<!-- inactive-ok-file: LIT-236 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-200: Rate-distortion generalization bounds

## Contribution

Generalization bounds have been stated in terms of mutual information between sample and output, compressibility of the hypothesis, and fractal dimension, and these look unrelated. The authors prove bounds via rate-distortion theory that place all three in one framework. They define a generalized compressibility from source coding and show the "compression error rate" controls the generalization error in expectation and with high probability. Lossless compression recovers and improves mutual-information bounds; lossy compression links generalization to the rate-distortion dimension, a fractal dimension.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 (pp. 3–4): surveys three lines — information-theoretic (Russo–Zou, Xu–Raginsky and conditional-MI refinements), compressibility (Littlestone–Warmuth, Arora et al. 2018 and successors), and fractal/intrinsic-dimension of SGD trajectories (Şimşekli et al. 2020 etc.).
- §1 (p. 4): the key reinterpretation — I(S;W) in Xu–Raginsky Thm. 1 is an upper bound on the lossless compression rate of the algorithm, not merely "dataset dependency"; so a large I(S;W) need not mean poor generalization if the algorithm is lossily compressible.
- Contents (p. 2): §3 defines algorithm compressibility (3.1), then expectation bounds (3.2) and tail bounds (3.3); §4.1 introduces "information-theoretic covering" for tail bounds; appendices treat conditional compressibility and Donsker–Varadhan via compression.
- §5 (p. 15): future work lists making bounds computable by estimating rate-distortion functions, relating rate-distortion dimension to other fractal dimensions, connecting to PAC-Bayes (footnote 15 cites Blum–Langford 2003 for the analogous link with Littlestone–Warmuth) — the programme k07 carries out.

## Open questions

- The paper most directly reframes "information the algorithm keeps about the sample" as a code length, which is the bridge the heading wants between compression/description length and sufficiency.
- Check whether the lossy framework says anything about sufficient statistics of the sample (a compressed W that preserves loss is close to a statistic sufficient for the loss).
- Bounds are data-independent (k07 §I says so); check the regimes where they are non-vacuous.
