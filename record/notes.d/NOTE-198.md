---
number: 198
status: Skimmed
formerly:
- NOTE-tmp08fwe
paper: LIT-238
title: 'Minimum Description Length Revisited'
version: 1
date: '2026-09-26'
summary: >-
  MDL, reformulated around universal distributions and luckiness functions and presentable without coding theory, extends both penalized likelihood and Bayes, and unifies methods usually seen as rival — AIC vs BIC, cross-validation vs Bayes — within one worst-case framework.
---
<!-- inactive-ok-file: LIT-238 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-198: Minimum Description Length Revisited

## Contribution

An up-to-date introduction to and review of the Minimum Description Length principle as a general theory of inductive inference for statistics, machine learning and pattern recognition. Though MDL grew out of data compression, the exposition needs no knowledge of it. It covers developments since Grünwald's 2007 book — new model selection, averaging and hypothesis-testing methods, and the first fully general definition of MDL estimators. On this view MDL generalizes penalized likelihood and Bayesian methods, replacing penalties and priors with luckiness functions and average-case with worst-case analysis.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 (pp. 1–2): MDL states that the best explanation of data is its shortest description; the review deliberately avoids information theory so statisticians can read it, and addresses the computational cost and arbitrary parameter restrictions that limited classical MDL.
- §2 (pp. 3–17): universal distributions are the core concept — Bayesian, NML/Shtarkov, two-part, prequential plug-in, switch, and RIPr — with asymptotic expansions, unification of model selection and estimation, and the luckiness function (§2.5).
- §3–5: new universal codes (switch distribution combining much of AIC and BIC, §3.1; RIPr for testing composite nulls, §3.3), factorized NML for graphical models (§4), latent-variable and irregular models (§5).
- §6.4 (pp. 28–29): relates MDL to deep learning — flat minima can be described with fewer bits (Hochreiter–Schmidhuber 1997; Hinton–van Camp 1993), and PAC-Bayes bounds give a precise frequentist justification in which −log π(θ), or a KL term via "bits back", acts as a codelength (Blum–Langford 2003; Dziugaite–Roy 2017).
- §7 (pp. 29–30): Grünwald–Mehta (2019) bound NML complexity by Rademacher complexity; Rissanen's later programme moves toward the Kolmogorov structure function and foundations with no "true model"; Lasso and Bayes factors can be read as MDL-like.
- Intro history (p. 2): the review explicitly defers "ideal" Kolmogorov-complexity MDL, MML and Solomonoff induction to the 2007 book.

## Open questions

- The standard modern reference for MDL; §7's pointer to Rissanen's use of the Kolmogorov structure function is the closest this batch comes to the heading's K-complexity / minimal sufficient statistic link — a deeper reading should follow that pointer (Vereshchagin–Vitányi on algorithmic sufficient statistics is the likely next paper).
- §6.4 is the bridge between MDL and the PAC-Bayes/compression generalization bounds in k07, k09, k11.
- Check §2.3 for how estimation and model selection unify, which bears on "two-part code = model + data given model" as a sufficiency decomposition.
