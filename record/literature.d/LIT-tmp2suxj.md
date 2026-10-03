---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmpvg9nc](../notes.d/NOTE-tmpvg9nc.md)); worth reading as the record''s working statement of the Savage–Dickey density ratio: for nested models, the Bayes factor for a point null φ = φ0 is the height of the posterior for φ at φ0 divided by the height of the prior there (Eq. 12), provided the nuisance parameters'' prior under the alternative, as φ → φ0, equals their prior under the null. Its derivation is Appendix A. Read it for the condition and for the limitations of §8 (density estimation in the tails, nested models only, the Borel–Kolmogorov paradox), not for the psychology examples, which are illustrations.'
title: 'Bayesian hypothesis testing for psychologists: A tutorial on the Savage–Dickey method'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the PDF in KU Leuven's institutional repository
    (Lirias), which Unpaywall lists as a lawful repository copy. It is the
    publisher-typeset article, 32 pages, printed pp. 158–189. The first
    author's own copy (ejwagenmakers.com) answered with a "One moment,
    please" bot challenge, which I did not try to pass. Main text,
    Appendix A (the derivation) and Appendix B (the WinBUGS code) were
    read; the reference list was checked for the Dickey citations.
    Crossref confirms the title, the four authors, Cognitive Psychology
    60(3):158–189 and the DOI, but gives only May 2010; `published:` is
    12 January 2010, the "Available online" date the article carries. Not
    held in the Anthology of the SOTA: a grep of its record for
    "Wagenmakers", "Savage" and "Dickey" found nothing.
tags:
- model-comparison
- probabilistic-modeling
- psychometrics
date: '2026-10-03'
published: '2010-01-12'
doi: '10.1016/j.cogpsych.2009.12.001'
url: 'https://lirias.kuleuven.be/retrieve/f96ceb5d-21e1-4da0-961f-5c11d71f14f9'
first_author: 'Wagenmakers'
keywords:
- 'Savage–Dickey density ratio'
- 'Bayes factor'
- 'statistical evidence'
- 'model selection'
- 'hierarchical modeling'
- 'random effects'
- 'order-restrictions'
- 'nested models'
- 'MCMC'
implementations:
- 'WinBUGS (model code in Appendix B)'
- 'R package polspline (logspline density estimates)'
extends:
- LIT-tmp6vz5e
summary: >-
  Wagenmakers, Lodewyckx, Kuriyal & Grasman (2010), Cognitive Psychology
  60(3):158–189. For nested models, H0: φ = φ0 inside H1, the Bayes factor
  BF01 equals the ratio of the posterior to the prior density of φ at φ0
  under H1 (Eq. 12), if the nuisance parameters' prior under H1 tends to
  their prior under H0 as φ → φ0. So a Bayes factor can be read off MCMC
  samples from the larger model alone, with a nonparametric density
  estimate at one point. Order restrictions are handled by truncating
  prior and posterior. Three worked psychology examples, including
  hierarchical one- and two-sample t-tests. Limitations stated in §8:
  density estimates in the tails, nested models only, and the
  Borel–Kolmogorov paradox.
---

<!-- inactive-ok-file: LIT-tmp6vz5e — Deferred: Dickey 1971 is unread (no lawful copy reached); cited as the source this tutorial names for the ratio, and the extends relation rests on this paper's own account of it -->

# LIT-tmp2suxj: Bayesian hypothesis testing for psychologists: A tutorial on the Savage–Dickey method

Eric-Jan Wagenmakers, Tom Lodewyckx, Himanshu Kuriyal and Raoul Grasman
(2010), *Cognitive Psychology* 60(3):158–189 — DOI-10.1016/j.cogpsych.2009.12.001

## Key takeaways

- **The ratio.** When H0 fixes a parameter φ at φ0 and H1 leaves it free,
  BF01 = p(φ = φ0 | D, H1) / p(φ = φ0 | H1): the posterior ordinate over the
  prior ordinate, both under the larger model (Eqs. 11–12). In the binomial
  example (9 of 10 correct, uniform prior) both routes give BF01 = 0.107.
- **The condition.** The nuisance parameters ψ must have
  p(ψ | φ → φ0, H1) = p(ψ | H0). Then they affect the Bayes factor only
  through the posterior of φ, and their own priors may be vague or improper.
  The prior on φ is the opposite case: its height at φ0 sits in the
  denominator, so doubling the width of a uniform prior roughly doubles
  BF01.
- **Order restrictions** come for free: truncating to φ < φ0 doubles the
  prior ordinate, and the posterior ordinate rises only as much as the data
  disagree with the restriction. A restriction the data already obey can at
  most double the evidence against the null.
- **The limits, as the authors give them (§8):** a one-dimensional density
  estimate at a point, unreliable when φ0 is in the posterior's tail; nested
  models only; and the conditioning on a probability-zero event that makes
  the result depend on parameterisation (the Borel–Kolmogorov paradox), so a
  test of μ = 0 can differ from a test of μ/σ = 0.

## Standing in the record

Filed on 2026-10-03 at the owner's request, as the first of a batch on
Bayesian model comparison. No anthology topic holds it: it is a tutorial on
statistical evidence for experimental psychologists, and it carries no
instruction for machine-learning practice.

It is the record's readable statement of the Savage–Dickey density ratio,
because the original, Dickey's 1971 paper ([LIT-tmp6vz5e](LIT-tmp6vz5e.md)), could not be
reached. The `extends` relation to it is declared on this paper's own
account: the authors credit the ratio to Dickey and Lientz (1970), who
attributed it to Savage, and cite Dickey (1971) as the source of the name.
What they build on it is the MCMC route, logspline density estimation at
one point, order-restricted and hierarchical tests. Appendix A then derives
the ratio in four lines from the continuity condition and Bayes' rule.

Where it sits in the batch:

- **Friston & Penny ([LIT-tmpuhjzx](LIT-tmpuhjzx.md))** show that the Savage–Dickey ratio is
  one special case of a more general identity: the evidence for any model
  formed from a full model by changing its prior is the full evidence times
  the posterior expectation of the prior ratio. Savage–Dickey is the case
  where the reduced prior is a point mass. Neither paper cites the other.
- **Bayesian model reduction ([LIT-tmpbgf7s](LIT-tmpbgf7s.md))** calls itself a generalisation
  of the Savage–Dickey ratio "to any new prior". It is the same identity as
  Friston & Penny's, worked out for more distributions.
- **MacKay ([LIT-tmpx82v3](LIT-tmpx82v3.md))** supplies the reason Bayes factors penalise
  complexity, the Occam factor. This tutorial gives the same argument in
  its §2.2.1, citing MacKay's 2003 textbook.

The prior-sensitivity point is where the two halves of the batch meet. Here
the prior ordinate at φ0 sets the Bayes factor directly. In MacKay the
Occam factor is the ratio of posterior to prior accessible volume. For a
single parameter whose posterior is a peak inside a flat prior, these are
two readings of the same quantity.
