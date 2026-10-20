---
number: 120
status: Active
formerly:
- CASE-tmpvt6wb
title: 'Six units with uniform coupling, A = αI + β(11ᵀ − I): their sum is exactly dynamically independent at every coupling tried, while a single unit and the sum of three are not, and no grouping of the units is a weakly coupled block'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- individuation
date: '2026-10-19'
line: distributed-agency
illustrates:
- CLAIM-388
summary: >-
  The n-unit form of A5's two-unit example in the exchange of
  2026-10-19 on coarse-to-fine processes. The sum closes exactly; no
  proper group of units is a block. It is the closure-without-block cell
  of A5's two-by-two table, and the system [QUESTION-218](../questions.d/QUESTION-218.md) would test
  for compensation and entrainment. Fictional by construction.
supports:
- CLAIM-388
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# CASE-120: Six units with uniform coupling, A = αI + β(11ᵀ − I): their sum is exactly dynamically independent at every coupling tried, while a single unit and the sum of three are not, and no grouping of the units is a weakly coupled block

## The case

A5 gave the continuous-time case of two units, ẋ = Ax with
A = [[−a, b], [b, −a]], a > b > 0. The coordinate z = x₁ + x₂ obeys
ż = (b − a)z exactly, while for b large the two units are strongly coupled
rather than separate blocks. A5: "Exact aggregation ⇏ near-decomposability."

Here it is in the record's setting for dynamical independence, a linear
Gaussian VAR(1) ([THEORY-733](../theory.d/THEORY-733.md)): six units, X_t = A X_{t−1} + ε_t with
A = αI + β(11ᵀ − I) and ε_t ~ N(0, Σ). Held fixed: the coupling between
every pair is the same β. Varied: β from 0.01 to 0.15 with α = 0.2 or 0.05,
one inhibitory case (α, β) = (0.3, −0.1), and Σ = I or a random positive
definite matrix. Measured: the transfer entropy from X to three coarse
variables, the sum of all six, one unit, and the sum of three.

Result ([CLAIM-388](../claims.d/CLAIM-388.md) gives the numbers): the sum of all six is exactly
independent in every setting; the other two are not, and their dependence
grows with |β|.

## What it can show

That a test for a unit by closure and a test by weak coupling across a
group's edge can disagree when the coupling is symmetric, not only when it
is one-way, as [CLAIM-157](../claims.d/CLAIM-157.md) already records. It is the closure-without-block
cell of A5's table:

| | strong closure | weak closure |
|---|---|---|
| strong block separation | both agree | block selected, dynamics not closed |
| weak block separation | **this case** | neither selected |

It cannot show that the sum is one system in any further sense. Nothing
here compensates, entrains or maintains itself, and the units are not
agents. Nor does it bear on systems whose coupling is not uniform: a
generic VAR(p ≥ 2) has no exactly closed linear variable at all
([THEORY-733](../theory.d/THEORY-733.md)).
