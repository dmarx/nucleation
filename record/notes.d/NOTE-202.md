---
number: 202
status: Skimmed
formerly:
- NOTE-tmp8jvr3
paper: LIT-239
title: 'Kolmogorov''s structure functions and model selection'
version: 1
date: '2026-09-26'
summary: >-
  The structure function of a single data string determines all of its stochastic properties: within any complexity-constrained model class it picks out the best-fitting model with certainty. Every admissible shape of that function occurs for some data, and neither it nor the minimal sufficient statistic is computable.
---
<!-- inactive-ok-file: LIT-239 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-202: Kolmogorov's structure functions and model selection

## Contribution

Kolmogorov proposed in 1974 a non-probabilistic approach to statistics in which data are finite binary strings and models are finite sets containing them. The structure function h_x(α) gives, for each bound α on model complexity, the least log-cardinality of a model of that complexity that contains the data. The authors show that this function fixes all stochastic properties of the data. For every constrained model class it identifies the individually best-fitting model, and it does so with certainty rather than with high probability, whether or not the "true" model lies in the class. They quantify the goodness of fit of an individual model to individual data, show that every graph satisfying the obvious constraints is the structure function of some data, and settle the (un)computability of these functions and of the algorithmic minimal sufficient statistic.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §III-B (pp. 6–7): a hypothesis S for x is judged by three numbers: K(S), the randomness deficiency δ(x|S) = log|S| − K(x|S), and the two-part length Λ(S) = K(S) + log|S|. Theorems IV.4, IV.8 and IV.11 describe the attainable set of triples completely, up to O(log n). The minimal α with a triple (α, 0, K(x)) is the complexity of the minimal sufficient statistic.
- §IV-A/B and Fig. 2: all shapes are possible (IV.4). Minimizing two-part code length at complexity α also (nearly) minimizes randomness deficiency (IV.8), which is the "selection of best-fitting model" result.
- §V-B: gives a foundation for the indirect (two-part) MDL method. Dovetailed search that keeps the shortest |p| + log|S| carries a known goodness guarantee and converges to near-best explanations. §V-D (Lemma V.2): each sufficiently large drop in code length strictly improves fit. §V-C covers maximum likelihood.
- §V-E: strengthens Shen's result on non-stochastic strings. For α0 + β0 < n − O(log n) there are strings of length n that are not (α0, β0)-stochastic.
- §VII (and Appendix D): h_x and λ_x (the ML and MDL estimators) are upper semicomputable but not computable to any reasonable precision. The fit function β_x is not semicomputable in either direction, and no algorithm finds a minimal sufficient statistic from x and K(x).
- Appendix I: reconstructs Kolmogorov's unpublished 1974 proposal from testimony by Cover, Gács and Levin.

## Open questions

- This is the technical core of "K-complexity ↔ minimal sufficient statistic". It is where two-part MDL gets a guarantee phrased about the individual datum rather than in expectation.
- Check how the results carry over from finite-set models to probability and function models (the paper's appendix on "validity for extended models") before applying them to learning with parametric families.
- The O(log n) slack is everywhere. A deeper reading should ask what survives at the data sizes and model complexities that matter in practice.
