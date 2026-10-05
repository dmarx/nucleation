---
number: 564
status: Read
formerly:
- NOTE-tmp8fh62
paper: LIT-735
title: 'The Epistemic Benefit of Transient Diversity'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read in full: the author's posted manuscript (28 pp., dated 29 September
    2009), §§1–4, figures from captions. Page references are the
    manuscript's.
date: '2026-10-05'
summary: >-
  A bandit model with beta priors. Sparse networks beat dense ones, as in
  2007, but extreme priors reverse the order, and sparse networks of
  dogmatic agents often never converge. Limited information and dogmatism
  each sustain diversity, and together sustain it too long. What
  communities need is diversity that is transient.
---
<!-- inactive-ok-file: THEORY-148 — Proposed; the transient-diversity account filed in this batch -->

# NOTE-564: The Epistemic Benefit of Transient Diversity

## Contribution

It generalised the 2007 result to a richer model and found a second route
to the same benefit (stubborn priors). It also found the failure that comes
from combining the two routes, and named the underlying good: transient
diversity.

## Key insight

Diversity of pursuit is valuable only on the way to agreement. Anything
that keeps minority options alive also delays agreement. The right amount
is enough to survive misleading early evidence and not so much that the
evidence never wins.

## Assumptions

- Two methods with objective success probabilities 0.5 and 0.499 (n. 12);
  agents hold beta priors with α, β drawn uniformly from an interval; myopic
  choice; Bayesian update on own and neighbours' outcomes.
- Runs stop after 10,000 rounds; failing to agree by then counts as failure.

## Key results

- **Networks** (Figures 3–4): cycle > wheel > complete; over all six-agent
  networks, success falls with density.
- **Priors** (Figure 6): as the maximum α, β rises towards 10,000 the order
  reverses; at extreme priors the complete network is best.
- **Variance over time** (Figure 7): diversity of actions persists much
  longer under extreme priors and in sparse networks.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Limiting information or making priors extreme each maintains diversity | strong | simulations, Figures 3–7 |
| C2 | Both together make diversity too stable and learning fails | strong | Figure 6 at high priors for cycle and wheel |
| C3 | Dense communication contributed to the delay in accepting the bacterial cause of ulcers | weak | historical narrative read through the model |
| C4 | Rationality in science is a property of groups more than individuals | weak | interpretive, after Hull |

## Method

Agent-based simulation of a two-armed bandit with beta priors, on the
cycle, wheel and complete graphs and all networks of up to six agents.

## Concepts

- **transient diversity** — variety in what members pursue that lasts long
  enough to prevent premature abandonment, and then gives way to consensus.

## Connections

Extends [LIT-724](../literature.d/LIT-724.md). It sides with Kitcher and Strevens, against Kuhn,
in showing diversity without diverse inductive standards, while adding a
cost of diversity their models lack.

## Bearing on the record

Source of [THEORY-148](../theory.d/THEORY-148.md). Rosenstock et al. ([LIT-733](../literature.d/LIT-733.md)) find this
the robust result of the literature. For the owner's essay it supplies a
formal case with the shape of "protective lock-in" (§5.4), where a
protective regime comes to sustain itself: the mechanisms that protect a
minority commitment become, past a point, the mechanisms that prevent the
group from ever settling.

## Limitations

The same narrow model as 2007, at a success gap of 0.001. The ulcer history
is an illustration, not a test.

## Open questions

How to tell, in a real community, whether diversity is transient or
entrenched before the outcome is known.
