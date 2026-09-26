---
status: Skimmed
paper: LIT-tmpig4jm
title: 'Studying philosophy makes people better thinkers'
version: 1
date: '2026-09-26'
summary: >-
  In HERI longitudinal data on over half a million US undergraduates, philosophy attracts students who are already verbally stronger and more curious and open-minded, yet after adjusting for freshman-year baselines philosophy majors still outperform all other majors on GRE Verbal, LSAT and a Habits of Mind measure.
---

<!-- inactive-ok-file: LIT-tmpig4jm — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpsvqk5: Studying philosophy makes people better thinkers

## Contribution

The authors test the empirical premise of a traditional argument for philosophy's value: that studying it improves people's thinking. Using freshman- and senior-year survey data on over half a million undergraduates at hundreds of US institutions, they find self-selection — students with stronger verbal ability and more curious, open-minded and rigorous dispositions are more likely to major in philosophy. After controlling for those baseline differences, philosophy majors still outperform every other major on verbal and logical reasoning tests and on a self-report measure of intellectual habits. They present this as the strongest evidence yet that philosophical study causally improves thinking.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2 argues that the familiar GRE/LSAT advantage of philosophy majors is uninformative about causation because self-selection explains it equally well.
- §4: data are HERI/CIRP surveys from 1990–2019; SAT at entry, GRE/LSAT self-reported at graduation (before 2005), and the Habits of Mind and Pluralistic Orientation scales from the 2010 cohort on.
- §5 uses mixed-effects regressions with random intercepts per institution (lme4, emmeans). §5.1: one SD higher SAT Verbal means 57% higher odds of majoring in philosophy, Habits of Mind 34%, Pluralistic Orientation 13%; SAT Math is not significant.
- §5.2 / Figure 1: baseline-adjusted means favour philosophy majors on GRE Verbal, LSAT and Habits of Mind.
- §5.3 tests, and argues against, a second selection effect in which only the best philosophy students take the GRE or LSAT.
- §6: over 800 institutions in the data; the authors claim support for the empirical premise of the argument for philosophy's value.

## Open questions

- A clean example of causal inference from observational data using baseline adjustment; check how much weight the self-reported test scores and the unobserved-confounder assumption can bear.
- Check the effect sizes in §5.2 and whether the gap on GRE Quantitative is also reported.
- Philosophically the payload is metaphilosophical (the value of philosophy, intellectual virtue); tagging is cognition/social-science because the vocabulary has no metaphilosophy or epistemology word.
