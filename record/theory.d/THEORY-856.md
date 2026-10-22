---
number: 856
status: Active
formerly:
- THEORY-tmpqzjvn
title: 'In one laboratory study of a nine-period game between an infrastructure operator, two elected policymakers and three voters (59 groups), letting the first elected policymaker fix the price for all periods moved prices toward the efficient level when policymakers'' payoffs were set equal to consumers'', and moved them further above it when their payoffs were set equal to the operator''s; under period-by-period regulation voters'' pressure lowered the operator-aligned policymakers'' prices without removing the gap'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-1053, a full reading of the main text of
    the open-access article (the online appendices were not read). The
    title claims no more than the one study measured, the reading was of
    the full article, and nothing in the record contradicts it, which meets
    ADR-047 v3. The authors' general conclusion about regulatory
    independence is filed separately as THEORY-858.
tags:
- society-and-governance
- social-science
date: '2026-10-21'
source:
- LIT-1340
summary: >-
  Schram and Ule (2024), [LIT-1340](../literature.d/LIT-1340.md), read in [NOTE-1053](../notes.d/NOTE-1053.md). Capture is a
  treatment, policymakers' payoffs set equal to the operator's, not
  something any party brought about, and "independence" is a price fixed
  by the first policymaker, not an agency. The capture cells hold 18
  groups of three voters. It does not show how capture arises in real
  regulators or that independent agencies entrench it.
extended_by:
- THEORY-858
supports:
- CLAIM-404
---
<!-- inactive-ok-file: THEORY-858 CLAIM-404 CLAIM-342 — Proposed; the general account and open claims this result bears on, nothing here rests on them -->
# THEORY-856: In one laboratory study of a nine-period game between an infrastructure operator, two elected policymakers and three voters (59 groups), letting the first elected policymaker fix the price for all periods moved prices toward the efficient level when policymakers' payoffs were set equal to consumers', and moved them further above it when their payoffs were set equal to the operator's; under period-by-period regulation voters' pressure lowered the operator-aligned policymakers' prices without removing the gap

## Source

Schram, A. & Ule, A. (2024), *Public Choice* 198: 403–425, [LIT-1340](../literature.d/LIT-1340.md),
read in [NOTE-1053](../notes.d/NOTE-1053.md).

## What was actually shown

A 2 × 2 between-subjects design at CREED, Amsterdam: 351 subjects in 59
groups of six (one operator, two policymakers, three voters), nine periods,
each group playing once. Capture: policymakers' payoffs equal the
operator's, or the consumers'. Independence: the policymaker elected in
period 1 fixes the price for all nine periods, or the elected policymaker
sets it each period. Prices in {0, …, 5}; the efficient no-loss price is 1
after investment.

Mean price over periods 1–6 (Table 4):

| | flexible | independent |
|---|---|---|
| consumer-aligned | 0.16 | 0.47 |
| operator-aligned | 1.78 | 3.19 |

- Consumer-aligned: independence raised prices toward 1 (permutation test,
  N = 41, p = 0.015) and cut the mean deviation from the efficient price
  from 0.98 to 0.53 (p < 0.001). Its effect on investment by period 5 (63%
  to 84%) was not significant (p = 0.255).
- Operator-aligned: independence raised prices (N = 18, p = 0.001) and the
  deviation from 1.56 to 2.31 (p = 0.066 by permutation test; significant
  at 1% in the Tobit regression of Table 5).
- Under flexible regulation, operator-aligned prices (1.78) lay below the
  no-pressure equilibrium and above the strong-pressure one, in which
  alignment would not matter: voters' pressure worked, but only partly.
  Voters punished higher past prices; only 36% of newly elected
  operator-aligned policymakers lowered their predecessor's price.

What could have come out otherwise: voters could have pushed
operator-aligned prices to the consumer-aligned level, as the
strong-pressure equilibrium predicts, which would have left independence
nothing to entrench. They did not.

## What this does not say

- **Not how capture comes about.** Alignment is assigned. Nothing in the
  game influences a policymaker, and the result is silent on whether
  independence makes capture more likely.
- **Not about independent agencies.** "Independence" is one policymaker's
  price fixed for the horizon. Mandates, appointments, budgets and review
  are not modelled.
- **Not beyond its scale.** Three voters, two candidates, one issue. The
  authors think real electoral pressure is weaker, which would strengthen
  the entrenchment, but that is their conjecture.
- **Not the general policy conclusion.** That independence helps consumers
  only when its designers serve them is [THEORY-858](THEORY-858.md), Proposed.
- **Not robust in every measure.** With the 45.8% of groups whose operator
  invested in period 1 excluded (the authors' Appendix F, which this
  reading did not check), the capture-cell price effect is significant
  only at 10%, the deviation effect by permutation test is not significant
  (p = 0.415), and by regression it is marginal (p = 0.07).

## Connections

- **[CLAIM-404](../claims.d/CLAIM-404.md)**, last clause. Formal independence of a procedure does
  not make it independent: here independence from voters, installed by a
  captured designer, insulated the capture from the one correction left.
- **[CLAIM-342](../claims.d/CLAIM-342.md).** The voters were the check whose arrival did not pass
  through the policymakers' interest. Independence removed it.
