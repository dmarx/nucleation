---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'Minimum Description Length Induction, Bayesianism, and Kolmogorov Complexity'
version: 1
tags:
- learning-theory
- probabilistic-modeling
- information-theory
date: '2026-09-26'
published: '1999-01-27'
arxiv: 'cs/9901014'
doi: '10.1109/18.825807'
first_author: 'Vitányi'
keywords:
- 'MDL'
- 'MML'
- 'Bayes''s rule'
- 'Kolmogorov complexity'
- 'universal distribution'
- 'randomness test'
implementations: []
summary: >-
  Vitányi & Li (1999), [arXiv:cs/9901014](https://arxiv.org/abs/cs/9901014). Ideal MDL, derived from Bayes's rule with the universal prior, coincides with Bayesian MAP selection exactly when the data are random with respect to the hypothesis and the hypothesis is random with respect to the prior (the "Fundamental Inequality"). For finite-set models it reduces to Kolmogorov's minimal sufficient statistic, so compression is almost always the best strategy for both identifying hypotheses and predicting.
---

# LIT-tmp5hrqh: Minimum Description Length Induction, Bayesianism, and Kolmogorov Complexity

Paul M. B. Vitányi, Ming Li (1999), *IEEE Transactions on Information Theory 46(2):446–464 (Mar 2000); first appeared as arXiv preprint (CWI Tech Report 1998)* — [arXiv:cs/9901014](https://arxiv.org/abs/cs/9901014)

## Key takeaways

- Ideal MDL, derived from Bayes's rule with the universal prior, coincides with Bayesian MAP selection exactly when the data are random with respect to the hypothesis and the hypothesis is random with respect to the prior (the "Fundamental Inequality"). For finite-set models it reduces to Kolmogorov's minimal sufficient statistic, so compression is almost always the best strategy for both identifying hypotheses and predicting.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The paper establishes how the Bayesian and minimum description length approaches relate. It sharpens MDL and MML into an "ideal MDL" principle, defined from Bayes's rule through Kolmogorov complexity. That principle takes the prior of a hypothesis to be its algorithmic universal probability and minimizes the model's code length plus the data's code length given the model. The Fundamental Inequality states the conditions under which the principle applies: the data must be random relative to each contemplated hypothesis, and the hypotheses random relative to the universal prior. When models are restricted to finite sets, ideal MDL becomes Kolmogorov's minimal sufficient statistic. Overall the paper argues that data compression is almost always the best strategy for hypothesis identification and for prediction.

## Standing in the record

Filed on 2026-09-26 at the owner's request, from a list they grouped under the heading *Relating K-complexity to minimum sufficient statistics*. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: high — the most direct statement of the heading's claim in a Bayesian/MDL frame and likely to be cited as a source; the skim captures theorem statements but not the conditions' fine print.**

What a deeper reading should check:

- This is the explicit bridge between the "K-complexity ↔ minimal sufficient statistic" heading and Bayesian and MDL practice (Thm 1 states the equivalence directly). It is the natural source for a theory claim that "compression = good induction, with conditions".
- The Fundamental Inequality makes the scope explicit: the equivalence needs both the data and the hypothesis to be typical. A note should record that condition rather than the unconditional slogan.
- Check how the journal version (IEEE TIT 2000) differs from the arXiv submission, and compare with Grünwald's later critiques of ideal MDL and with k03's individual-data MDL guarantees.

Access when seeded: Read the arXiv abstract page (single version, submitted 1999-01-27) and the full 35-page PDF text: keywords, §2.1 (Def. 3, Thm 1), §2.4 (Thm 3), §2.6, §3 (Thms 7–8) and §4. I confirmed the published version's DOI, volume, issue and pages through Crossref (no contact address sent). The arXiv text is the submitted version, so it may differ in detail from the journal article. Keywords are the paper's own (the last one is truncated at the page break in the extracted text).
