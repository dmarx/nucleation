---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'Minimum Description Length Revisited'
version: 1
tags:
- learning-theory
- probabilistic-modeling
- information-theory
date: '2026-09-26'
published: '2019-08-21'
arxiv: '1908.08484'
doi: '10.1142/S2661335219300018'
first_author: 'Grünwald'
keywords:
- 'minimum description length'
- 'universal distributions'
- 'normalized maximum likelihood'
- 'model selection'
- 'luckiness function'
implementations: []
summary: >-
  Grünwald & Roos (2019), [ARXIV-1908.08484](https://arxiv.org/abs/1908.08484). MDL, reformulated around universal distributions and luckiness functions and presentable without coding theory, extends both penalized likelihood and Bayes, and unifies methods usually seen as rival — AIC vs BIC, cross-validation vs Bayes — within one worst-case framework.
---

# LIT-tmpk2hsw: Minimum Description Length Revisited

Peter Grünwald, Teemu Roos (2019), *International Journal of Mathematics for Industry 11(1):1930001 (2019)* — [ARXIV-1908.08484](https://arxiv.org/abs/1908.08484)

## Key takeaways

- MDL, reformulated around universal distributions and luckiness functions and presentable without coding theory, extends both penalized likelihood and Bayes, and unifies methods usually seen as rival — AIC vs BIC, cross-validation vs Bayes — within one worst-case framework.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

An up-to-date introduction to and review of the Minimum Description Length principle as a general theory of inductive inference for statistics, machine learning and pattern recognition. Though MDL grew out of data compression, the exposition needs no knowledge of it. It covers developments since Grünwald's 2007 book — new model selection, averaging and hypothesis-testing methods, and the first fully general definition of MDL estimators. On this view MDL generalizes penalized likelihood and Bayesian methods, replacing penalties and priors with luckiness functions and average-case with worst-case analysis.

## Standing in the record

Filed on 2026-09-26 at the owner's request, from a list they grouped under the heading *Relating K-complexity to minimum sufficient statistics*. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: high — the reference work for description-length reasoning that the other papers in this section cite (k11 cites it directly), and the skim only covers its framing and ML section.**

What a deeper reading should check:

- The standard modern reference for MDL; §7's pointer to Rissanen's use of the Kolmogorov structure function is the closest this batch comes to the heading's K-complexity / minimal sufficient statistic link — a deeper reading should follow that pointer (Vereshchagin–Vitányi on algorithmic sufficient statistics is the likely next paper).
- §6.4 is the bridge between MDL and the PAC-Bayes/compression generalization bounds in k07, k09, k11.
- Check §2.3 for how estimation and model selection unify, which bears on "two-part code = model + data given model" as a sufficiency decomposition.

Access when seeded: arXiv abs page (v1 2019-08-21 submitted by Roos, v2 2019-12-18) and v2 PDF read for §1 (pp. 1–3), section heads, §6.4 and §7 (pp. 28–30). Crossref for the journal record (article 1930001, issue dated 2019-12, online 2020-03-12). The journal version was not read.
