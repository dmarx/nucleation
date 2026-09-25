---
number: 74
status: Skimmed
formerly:
- NOTE-tmpskbvw
paper: LIT-044
title: 'The epic story of maximum likelihood'
version: 1
date: '2026-09-25'
summary: >-
  Maximum likelihood took about two centuries to justify. Fisher's three proofs (1922, 1925, and an unpublished 1930 characterization) are defensible under his implicit regularity conditions, and the 1950s counterexamples (Hodges's superefficiency, growing parameter counts, unbounded likelihoods) mark real limits. Yet ML's useful scope still exceeds anything that can reasonably be proved.
---

<!-- inactive-ok-file: LIT-044 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-074: The epic story of maximum likelihood

## Contribution

Maximum likelihood looks like an obvious, even prehistoric idea, but its mathematical history is anything but simple. Lagrange, Daniel Bernoulli, Euler, Laplace and Gauss all explored it, not always in ways now accepted. Stigler traces the story from before Fisher to Le Cam's dissertation. He presents Fisher's unpublished 1930 conditions for consistency and efficiency, and analyses the mathematical basis of Fisher's three proofs. He shows that Fisher's information inequality came out of his analysis-of-variance work, and that the later estimating-function approach came from Euler's relation for homogeneous functions. He reviews how Fisher's work was received and draws lessons from it.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Structure: early history (§2); Pearson & Filon (§3); Fisher (§4); the first proof (§5); "three years later" (§6); the 1925 ANOVA proof (§7); correspondence after 1925 (§8); "the geometric shadow of a nasty…" (§9); Fisher's reply as a third proof (§10); the situation to 1950 (§11); doubts about ML (§12); "of errors in theory" (§13); conclusion (§14).
- The framing device is Hodges's 1951 superefficient estimator (published in Le Cam 1953), the "nasty, ugly little fact" that punctured the claim that ML is uniformly efficient.
- Conclusion (§14): Fisher's proofs hold given the implicit assumptions he was clearly aware of. The 1950s investigations exposed problems he never publicly addressed. Stigler attributes some of Fisher's silence to temperament and the feud with Neyman, and credits the feud with bringing the problems into public view.
- Earlier "proofs" by Hotelling, Doob and Dugué are said never to have had their errors clearly identified in print.

## Open questions

- It is useful historical grounding for any probabilistic-modeling note that leans on MLE optimality claims. It spells out which efficiency claims are theorems and which are conditions.
- A deeper reading should check the §9–10 treatment of the "nasty" example and the 1930 conditions if a note wants to cite a precise account of when ML is efficient.
