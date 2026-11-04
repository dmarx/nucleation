---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmpzgqov](../notes.d/NOTE-tmpzgqov.md)) from the authors' manuscript of
  1999-09-05, posted on Rockafellar's own publications page at the
  University of Washington, not the typeset journal version; worth reading
  as the paper that turns conditional value-at-risk from a quantity defined
  through value-at-risk into the minimum of a convex function of one extra
  scalar, so that minimizing it over decisions is a convex program, and on
  sampled scenarios with linear losses a linear program, with the VaR
  obtained as a byproduct. Its limits: it assumes a loss distribution with
  no atoms, works in one period at a fixed confidence level with a known or
  simulable distribution, and its evidence of numerical quality is two
  small examples, in one of which pseudo-random sampling at β = 0.99 is
  off by up to about 5% in CVaR.
title: 'Optimization of conditional value-at-risk'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the pasted bibliography on
    emergency readiness, written by another assistant (A) and pasted by the
    owner on 2026-11-04, which lists it under tail risk and critical
    transitions with no gloss. Citation checked against Crossref and
    OpenAlex: R. Tyrrell Rockafellar and Stanislav Uryasev, The Journal of
    Risk 2(3), 21–41, journal article, doi 10.21314/JOR.2000.038. A's
    citation is correct in every field. Crossref gives only the year 2000
    and OpenAlex 2000-01-01, a year placeholder, so neither gives a day;
    `published:` is the date the manuscript read carries on its title page,
    5 September 1999, the earliest date any source gives (ADR-002). Not
    held before: no hits for CVaR, value-at-risk, expected shortfall,
    Uryasev or the DOI. Read from the authors' manuscript
    (https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf),
    linked as item rtr179 from Rockafellar's publications page
    (https://sites.math.washington.edu/~rtr/papers.html): 26 pages, with
    some broken table cross-references and without the journal's
    pagination. Status Active.
tags:
- operations-research
- mathematics
- probabilistic-modeling
date: '2026-11-04'
published: '1999-09-05'
doi: '10.21314/JOR.2000.038'
first_author: 'Rockafellar'
keywords:
- 'conditional value-at-risk'
- 'value-at-risk'
- 'mean excess loss'
- 'stochastic programming'
- 'linear programming'
- 'portfolio optimization'
- 'hedging'
implementations: []
summary: >-
  Rockafellar & Uryasev (2000). For a loss f(x, y) of a decision x under
  random y, the function F_β(x, α) = α + (1−β)⁻¹ E[f(x, y) − α]⁺ is convex
  and continuously differentiable in α; its minimum over α is the β-CVaR,
  and the left end of its set of minimizers is the β-VaR (Theorem 1). So
  minimizing CVaR over x is minimizing F_β jointly over (x, α), which also
  yields the VaR of the optimal decision (Theorem 2): a convex program when
  the loss is convex in x, and a linear program on sampled scenarios when
  it is linear, with no normality assumed. Illustrated on a three-asset
  portfolio under normal returns, where minimum-CVaR, minimum-VaR and
  minimum-variance portfolios coincide, and on hedging a NIKKEI options
  portfolio with a non-normal loss.
---
<!-- inactive-ok-file: THEORY-tmpeqky9 — Proposed and new; cited from the reading of Rockafellar and Uryasev (2000) as open -->

# LIT-tmpdvjiy: Optimization of conditional value-at-risk

Rockafellar, R. T. & Uryasev, S. (2000). Optimization of conditional value-at-risk. *The Journal of Risk* 2(3): 21–41. doi:10.21314/JOR.2000.038.

## Key takeaways

*From the reading, [NOTE-tmpzgqov](../notes.d/NOTE-tmpzgqov.md). Page numbers are the 1999 manuscript's, not the journal's.*

- **CVaR without VaR first.** For fixed x, F_β(x, α) "is convex and
  continuously differentiable" in α (Theorem 1, p. 5), and its minimum is
  the CVaR, which can therefore "be calculated without first having to
  calculate the β-VaR on which its definition depends" (p. 6).
- **One joint minimization.** "Minimizing the β-CVaR of the loss
  associated with x over all x ∈ X is equivalent to minimizing Fβ (x, α)
  over all (x, α) ∈ X × IR" (Theorem 2, p. 6), and the minimizing α gives
  the VaR.
- **A linear program on scenarios, for any distribution.** "the
  possibility of such reduction to linear programming does not depend on y
  having a special distribution, such as a normal distribution" (p. 9).
- **VaR hides the tail.** In the hedging example one portfolio has β-VaR
  −205,927 and β-CVaR 1,183,040 (p. 19); the method "also lowers VaR
  because CVaR ≥ VaR" (p. 19).
- **Rare scenarios must be sampled.** With pseudo-random samples,
  convergence to the minimum-variance values "is slow at best" (p. 11).

## Standing in the record

Registered from the pasted bibliography on emergency readiness, which lists
it under tail risk with no gloss and uses it, implicitly, as the formal tool
for optimizing against the average of the worst outcomes rather than the
mean. That fits the paper. The paper is about portfolio losses with a known
or simulable distribution and a fixed β. It says nothing about rarely
exercised capabilities, readiness or slack; to value capacity kept for rare
events with it, one has to supply the loss of a capacity decision in every
scenario and sample the rare ones, which the paper's own slow convergence at
β = 0.99 warns about. Its nearest held neighbour is [LIT-1975](LIT-1975.md) (adjustable
robust linear programming), the worst-case rival to its tail-expectation
treatment in the same machinery. Filed from it: [THEORY-tmpeqky9](../theory.d/THEORY-tmpeqky9.md).
