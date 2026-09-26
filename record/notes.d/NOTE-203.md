---
number: 203
status: Skimmed
formerly:
- NOTE-tmp8l29l
paper: LIT-225
title: 'MDL induction, Bayesianism, and Kolmogorov complexity'
version: 1
date: '2026-09-26'
summary: >-
  Ideal MDL, derived from Bayes's rule with the universal prior, coincides with Bayesian MAP selection exactly when the data are random with respect to the hypothesis and the hypothesis is random with respect to the prior (the "Fundamental Inequality"). For finite-set models it reduces to Kolmogorov's minimal sufficient statistic, so compression is almost always the best strategy for both identifying hypotheses and predicting.
---
<!-- inactive-ok-file: LIT-225 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-203: MDL induction, Bayesianism, and Kolmogorov complexity

## Contribution

The paper establishes how the Bayesian and minimum description length approaches relate. It sharpens MDL and MML into an "ideal MDL" principle, defined from Bayes's rule through Kolmogorov complexity. That principle takes the prior of a hypothesis to be its algorithmic universal probability and minimizes the model's code length plus the data's code length given the model. The Fundamental Inequality states the conditions under which the principle applies: the data must be random relative to each contemplated hypothesis, and the hypotheses random relative to the universal prior. When models are restricted to finite sets, ideal MDL becomes Kolmogorov's minimal sufficient statistic. Overall the paper argues that data compression is almost always the best strategy for hypothesis identification and for prediction.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.1, Def. 3 (p. 9): defines the Kolmogorov minimal sufficient statistic (KMSS) H0 as the least-complex set H with K(H|n) + log d(H) = K(D|n). Thm 1: over finite-set hypotheses, (i) Bayes's rule with the universal prior and uniform likelihood, (ii) KMSS and (iii) ideal MDL select the same hypothesis. Example 1 applies this to coin tossing.
- §2.2: a probabilistic generalization of KMSS that coincides with MAP but not necessarily with ideal MDL unless further conditions hold.
- §2.4, Thm 3 (Fundamental Inequality, p. 13): if D is Pr(·|H)-random and H is P-random, then −log Pr(D|H) − log P(H) lies within α(P,H) = K(Pr(·|H)) + K(P) of K(D|H) + K(H), and the converse also holds. §2.5: under this condition ideal MDL and Bayesianism agree.
- §2.6 and Example 4: application to parametric statistics and polynomial fitting. The authors are explicit that K is uncomputable and that practical encodings are outside the paper's scope.
- §3, Thms 7–8 (pp. 21–22): for μ-random sequences the universal (Solomonoff) predictor M converges to μ, and the shortest-program (monotone complexity Km) predictor agrees with −log μ(y|x) in the limit. Hence prediction by shortest description is justified in the typical case, although by Gács's result Km and −log M differ in general.
- §4: maximally compressed descriptions give good results on data samples random for the probabilistic hypotheses, and such samples have probability tending to 1.

## Open questions

- This is the explicit bridge between the "K-complexity ↔ minimal sufficient statistic" heading and Bayesian and MDL practice (Thm 1 states the equivalence directly). It is the natural source for a theory claim that "compression = good induction, with conditions".
- The Fundamental Inequality makes the scope explicit: the equivalence needs both the data and the hypothesis to be typical. A note should record that condition rather than the unconditional slogan.
- Check how the journal version (IEEE TIT 2000) differs from the arXiv submission, and compare with Grünwald's later critiques of ideal MDL and with k03's individual-data MDL guarantees.
