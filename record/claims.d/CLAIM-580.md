---
number: 580
status: Proposed
formerly:
- CLAIM-tmppzkl3
title: 'The transition threshold is stable under error in the resource function: if an estimate of the requirement is within ε of the true one at every configuration, the estimated threshold is within ε of the true one, and an underestimate anywhere can only lower it while an overestimate can only raise it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a configuration space, an admissible path class,
  a requirement r and an estimate r̂ with |r − r̂| ≤ ε everywhere whose
  thresholds differ by more than ε; or an estimate below r everywhere whose
  threshold is above the true one. Not defeated by errors that are larger
  in some places than ε, which the claim's bound covers only through their
  supremum, nor by error in which paths count as admissible, which the
  claim does not address.
tags:
- mathematics
- operations-research
date: '2026-11-05'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-571
complements:
- CLAIM-585
grounds:
- THEORY-1420
summary: >-
  The assistant's own proposition, offered at the owner's invitation on
  2026-11-05. The threshold of [CLAIM-571](CLAIM-571.md) is the least, over admissible
  paths, of each path's peak requirement, and both the peak and the least
  move by at most the largest error in the requirement. So a planner who
  knows each configuration's cost to within ε knows a transition's threshold
  to within ε, and its reconfiguration slack to within 2ε. The error is also
  one-sided in a useful way: overestimating only raises the threshold, and
  underestimating anywhere can only lower it, possibly by opening a cheaper
  path that does not exist. It is the zero-dimensional case of the stability
  of sublevel-set persistence that Mirth et al. use. With several resources
  the same argument bounds the set of sufficient budgets coordinate by
  coordinate. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-571 CLAIM-585 TERM-106 — Proposed or Skimmed; entries of 2026-11-04 and 2026-11-05 from the readiness and constraint-architecture filings, cited as open -->

# CLAIM-580: The transition threshold is stable under error in the resource function: if an estimate of the requirement is within ε of the true one at every configuration, the estimated threshold is within ε of the true one, and an underestimate anywhere can only lower it while an overestimate can only raise it

## The claim

Let B*(A, B) = inf over admissible paths γ from A to B of max_t r(γ(t)),
as in [CLAIM-571](CLAIM-571.md), and let r̂ be an estimate with |r(q) − r̂(q)| ≤ ε at
every q.

- **Bound.** For each path, the peak of r̂ along it is within ε of the
  peak of r, since each value is. Taking the least over the same set of
  paths keeps the bound: |B̂* − B*| ≤ ε. Where no admissible path exists
  both are infinite, since the path class does not depend on r.
- **Slack.** Reconfiguration slack ([TERM-106](../terms.d/TERM-106.md)), the threshold less the
  larger of the two holding costs, is then known to within 2ε.
- **Direction.** If r̂ ≥ r everywhere, every path's peak rises, so
  B̂* ≥ B*; if r̂ ≤ r, B̂* ≤ B*. An underestimate at configurations off
  every cheap path can still lower the estimate, by making a path look
  cheaper than any that is.

A numerical check, on 2,000 random graphs of twelve configurations with
random costs and errors of random size, found the ratio of threshold error
to ε never above 1 (the largest was 0.9989), as the argument requires.

## What it adds

- **A guarantee a planner can use.** Costs of configurations are never
  known exactly. The bound says the threshold does not amplify error.
- **What to measure.** An overestimate matters only along the near-best
  paths; an underestimate matters anywhere it could open a phantom
  shortcut. So the costs worth measuring well are those at the bottleneck
  configurations of the candidate paths, with lower bounds everywhere
  else, not the costs where the organization ordinarily operates.
- **Several resources.** The same per-path argument, coordinate by
  coordinate, puts the set of sufficient budgets of [CLAIM-585](CLAIM-585.md) between
  the true set shifted up by ε and shifted down by ε in each coordinate. No
  single threshold exists to bound there.

## Source

It is the zero-dimensional case of the stability theorem for sublevel-set
persistent homology, which Mirth et al. use ([NOTE-1616](../notes.d/NOTE-1616.md)): "small changes
to the input produce only small changes in the persistent homology". The
merge level of two components is the threshold here.

## What it does not say

- Nothing about error in which paths are admissible, which can change the
  threshold without bound (an infinite threshold made finite by a wrongly
  allowed move, or the reverse).
- Nothing about how to obtain an estimate within ε.
