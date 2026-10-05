---
status: Read
paper: LIT-tmpe51mm
title: 'Exploration and Exploitation in Organizational Learning'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read in full: printed pp. 71–87 from the JSTOR copy in an NTNU
    doctoral-course readings folder; reference list skimmed. Figures read
    through captions and text only, since the plotted values do not survive
    the scan's extraction. Page references are the printed pages.
date: '2026-10-05'
summary: >-
  Exploitation's returns are surer, nearer and closer to the decision than
  exploration's, so adaptive processes favour it and become
  self-destructive. In a simulation of mutual learning, an organizational
  code improves only from members who deviate from it. Slow socialization,
  a mix of fast and slow learners, and moderate turnover raise what the
  organization knows; under environmental change without turnover, its
  knowledge decays to chance. Where only first place counts, variance beats
  reliability.
---
<!-- inactive-ok-file: THEORY-tmpfn4zv — Proposed; filed in this batch -->
<!-- inactive-ok-file: THEORY-tmpqnfk9 — Proposed; transient diversity, named for a parallel -->

# NOTE-tmpsry8p: Exploration and Exploitation in Organizational Learning

## Contribution

It named the exploration–exploitation trade-off as a general problem of
adaptive organizations and showed, in a simple model, that the speed at
which an organization socializes its members is itself a choice about
exploration, with costs and benefits distributed unevenly among members.

## Key insight

An organization's store of knowledge can learn only from the people who
disagree with it. Teaching them its beliefs quickly makes each of them more
accurate sooner and makes the organization stop learning.

## Assumptions

- Reality has m binary dimensions (m = 30); n = 50 members and a code hold
  beliefs of 1, 0 or −1 on each.
- Members learn only from the code (probability p1 per differing
  dimension); the code learns from the majority of the members who know
  more than it does (rate governed by p2). Members do not learn from each
  other directly, and nobody observes reality.
- Turnover (p3) replaces members with recruits whose beliefs are random,
  not drawn toward the code. Turbulence flips dimensions of reality with a small probability per period.
- 80 runs per setting; n is not varied. March says the qualitative results
  are insensitive to m and n.

## Key results

- **Closed system** (p. 75). Members and code converge to a stable
  equilibrium of shared, not necessarily accurate, beliefs. Equilibrium
  knowledge is highest when the code learns fast from members socialized
  slowly; with fast socialization, slower code learning does better.
- **Heterogeneity** (pp. 76–77). For any average p1, a mix of fast (0.9)
  and slow (0.1) learners reaches higher equilibrium knowledge than a
  uniform population. Gains come from slow learners and accrue to fast
  ones, so no individual has an incentive to learn slowly.
- **Turnover** (pp. 79–80). With fast socialization, moderate turnover
  improves the code; with slow socialization, fast turnover leaves too
  little exploitation.
- **Turbulence** (pp. 80–81). Without turnover, code knowledge rises and
  then falls to chance, a random walk. Moderate turnover (p3 = 0.1 with turbulence
  at 0.02) sustains it. Recruiting people closer to the code would weaken
  this. Tenure then advantages individuals, which March expects to produce
  pressure to secure tenure for oneself and restrict it for others.
- **Competition for primacy** (pp. 81–84). As competitors increase,
  variance in performance matters more and, in the limit, "the mean
  becomes irrelevant". Knowledge that raises mean and reliability does not
  guarantee advantage.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Adaptive processes improve exploitation faster than exploration, and can become self-destructive | moderate | argument from the timing and certainty of returns; prior literature on competency traps |
| C2 | Slow socialization raises equilibrium organizational knowledge, especially when the code learns fast | moderate | simulation, Figure 1 |
| C3 | A mix of fast and slow learners beats a uniform population with the same average rate | moderate | simulation, Figures 2–3 |
| C4 | Moderate turnover improves organizational knowledge, and under turbulence prevents its decay to chance | moderate | simulation, Figures 4–5; depends on recruitment not being drawn toward the code |
| C5 | Where only relative position counts, variance can matter more than mean | moderate | model of independent draws; acknowledged incomplete |

## Method

Monte Carlo simulation of a stylized model, 80 runs per parameter setting,
with m = 30 and n = 50. Outcomes are the proportion of reality correctly
represented in the code and, on average, in members' beliefs, at
equilibrium or at period 20. The competition section uses a separate
analytic model of performance as independent draws from distributions.

## Concepts

- **exploration** — "experimentation with new alternatives"; returns
  "uncertain, distant, and often negative" (p. 85).
- **exploitation** — refinement and extension of existing competences;
  returns "positive, proximate, and predictable" (p. 85).
- **organizational code** — the languages, beliefs and practices of the
  organization; its knowledge level is the proportion of reality it
  represents correctly.
- **socialization rate (p1)** — how fast members adopt the code.

## Connections

It cites earlier work by Herriott, Levinthal and March on slow learning,
and David on path dependence. Its model resembles the epistemic-network
models behind [THEORY-tmpqnfk9](../theory.d/THEORY-tmpqnfk9.md): in both, diversity in what members believe
or pursue must last long enough to be learned from. The mechanism differs.
Here diversity is lost to a central code; there, to communication among
peers.

## Bearing on the record

Source of [THEORY-tmpfn4zv](../theory.d/THEORY-tmpfn4zv.md).

For the owner's essay: §5.4 (protective lock-in) gets a mechanism by which
an organization's beliefs stay fixed while the world changes, "regardless
of changes in reality", without anyone deciding it. §6.1 gets a case of
stability that is not viability: the converged equilibrium is stable and
degrades. §8.2 gets an organizational analogue of Longino's and Zollman's
point that a community's knowledge depends on keeping dissent alive. The
model has no exit, voice or governance: turnover is an exogenous rate, not
members choosing to leave, so it says nothing about how members respond to
decline.

## Limitations

Results come from one stylized model with fixed m and n. Members never
observe reality, and never learn from each other. Turnover's benefit
depends on recruitment rules March sets aside. The competition analysis
assumes independent draws and is called "incomplete" because mean and
variance can be chosen strategically. No optimal balance is derived.

## Open questions

Whether the results hold when members learn from each other as well as from
the code, and what organizational structures, other than turnover, keep
deviation alive long enough for the code to learn from it.
