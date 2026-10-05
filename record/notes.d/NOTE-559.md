---
number: 559
status: Read
formerly:
- NOTE-tmp09jwk
paper: LIT-733
title: 'In Epistemic Networks, Is Less Really More?'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read in full: the published version posted by an author, §§1–5 and
    footnotes; figures from captions and text.
date: '2026-10-05'
summary: >-
  Over a wider parameter space than Zollman used, the advantage of sparse
  networks vanishes when the better option is even slightly better, when
  groups are larger, or when agents gather more data per round. It
  survives only where inquiry is hard, and Kummerfeld and Zollman's
  effects behave the same way. Transient diversity is the robust lesson.
---
<!-- inactive-ok-file: THEORY-143 — Proposed; the network account filed in this batch -->
<!-- inactive-ok-file: THEORY-148 — Proposed; the transient-diversity account filed in this batch -->

# NOTE-559: In Epistemic Networks, Is Less Really More?

## Contribution

A robustness analysis. It shows the best-known result of network
epistemology is confined to a small region of its own model's parameter
space, says what characterises that region, and draws a methodological
lesson about how such models should inform real communities.

## Key insight

Sparse communication helps only when good evidence is scarce. When evidence
is plentiful, it slows the group down for nothing.

## Assumptions

Zollman's 2007 and 2010 models, unchanged except for parameters: pB from
0.501 to 0.7, trials per round n from 1 to 6,000, network size 4 to 100,
cycle and complete networks, at least 10,000 runs per setting. For
Kummerfeld & Zollman: ε-greedy agents, 8-agent networks, payoff mean 1–4
and standard deviation 3 or 9.

## Key results

- Zollman effect below 2% at pB = 0.51 and zero from pB = 0.525 (size 10,
  n = 1,000; Figure 2).
- Effect larger for smaller n (Figure 3), smaller for larger groups (Figure
  4); at size 100, complete 99.12% correct in 20 rounds against cycle 100%
  in 1,977 (Figure 5).
- Both the Zollman effect and its reverse in exploratory models fade as the
  better action becomes easier to identify (Figure 7).
- Effect size correlates with average time to convergence (Figure 8).
- **Better remedies** (end of §5.2). Where data are scarce, stubborn or
  exploratory agents, or standards for how much data must go into a
  judgment, prevent premature settling "apart from ignoring good data".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The Zollman effect is absent over most of the parameter space | strong | simulations, Figures 2–6 |
| C2 | Network structure matters only when inquiry is difficult | moderate | Figure 8 correlation across settings |
| C3 | Transient diversity is robust across the models | moderate | stated in §5.2 from their runs |
| C4 | Confidence that such effects occur in real communities should fall | weak | argued; model–world fit unknown |
| C5 | Evidence standards or exploratory agents achieve the benefit without restricting communication | moderate | argued in §5.2; in Kummerfeld & Zollman's models, exploration made dense networks the better ones |

## Method

Replication by simulation over a grid of parameters.

## Concepts

- **Zollman effect** — the cycle's advantage over the complete network in
  probability of converging on the better action.
- **how-potentially model** — one that shows a phenomenon may occur in real
  systems and warrants investigation, weaker than representing them.

## Connections

Corrects the generality claimed by [LIT-724](../literature.d/LIT-724.md) (n. 7) and
[LIT-735](../literature.d/LIT-735.md). It cites Holman & Bruner (2015), where connected
networks resist biased agents better, and two experiments with some
evidence for a Zollman-like effect (Mason et al. 2008; Jönsson et al. 2015).

## Bearing on the record

Second source of [THEORY-143](../theory.d/THEORY-143.md), fixing its scope, and support for
[THEORY-148](../theory.d/THEORY-148.md). For the owner's essay: if a corporation's "governing
relationships" are modelled on these networks, the case for limiting
integration applies only where the organization faces close calls on
scarce evidence. Even there, the paper's preferred remedy is a standard for
how much evidence a decision needs, not less communication. That is closer
to the essay's own §8 picture of governance than to restricting what
members hear.

## Limitations

The same idealisations as the models it tests. It explores the Kummerfeld
& Zollman space less thoroughly than Zollman's own.

## Open questions

Which real communities fall where the effect occurs. The authors cite
experiments by Mason et al. that suggest network structure matters more
for harder problems.
