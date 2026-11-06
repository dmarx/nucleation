---
number: 200
status: Proposed
formerly:
- CASE-tmp0g3pa
title: 'A transition that a budget reaches only by carry-over: a per-period budget of 1.0 holds either configuration at 0.7, the transition needs 1.3, and rolling over the 0.3 left unspent reaches it, while a rule that cuts or expires unspent funds forecloses it'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Revised at the twenty-sixth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), so that its use of
    TERM-106 says which sense: "It is reconfiguration slack (TERM-106) held
    in installments" called the 0.3 a period slack, where it is the
    reconfiguration reserve that meets the transition's slack of 0.6. The
    construction is unchanged.
standing: fictional
kind: construction
tags:
- operations-research
- society-and-governance
- mathematics
date: '2026-11-05'
line:
- readiness
illustrates:
- CLAIM-571
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: the budget
  recursion B_{t+1}=B̄+(ρ−α)L_t ≥ 1.3, which with B̄ = 1.0, L = 0.3, ρ = 1
  and α = 0 reaches the 1.3 the transition of A's example needs. A gives
  the recursion and the values; reading L as the balance left unspent,
  ρ as the share rolled over and α as the share by which the
  budget-setter cuts the next budget per unit unspent is the filer's. The
  0.3 is slack against current output, and it is what makes the
  transition possible. A rule that expires it (ρ < 1) or a ratchet that
  cuts on it (α > 0) forecloses the transition. It ties A's construction
  to the ratchet and to the question of allocation by observed activity.
  The construction is the filer's, from A's budget recursion; adopting
  it is the owner's call.
---
<!-- inactive-ok-file: TERM-107 TERM-110 THEORY-1421 THEORY-1410 CLAIM-558 — Proposed; A's proposals of 2026-11-04, the entries filed beside them and the readings' accounts, cited as filed -->

# CASE-200: A transition that a budget reaches only by carry-over: a per-period budget of 1.0 holds either configuration at 0.7, the transition needs 1.3, and rolling over the 0.3 left unspent reaches it, while a rule that cuts or expires unspent funds forecloses it

## The case

**Setting.** A's example of [CLAIM-571](../claims.d/CLAIM-571.md): holding either configuration
costs 0.7 a period, and the transition between them peaks at 1.3. The
transition is to be made within one period. A base budget of B̄ = 1.0
a period covers holding with 0.3 to spare and does not cover the
transition.

**A's recursion.** B_{t+1}=B̄+(ρ−α)L_t, with the transition possible in
period t + 1 when B_{t+1} ≥ 1.3. A's values: B̄ = 1.0, L = 0.3, ρ = 1,
α = 0, so B_{t+1} = 1.0 + 0.3 = 1.3. Checked.

**The filer's reading of the symbols.** L_t is what period t leaves
unspent, here B̄ − 0.7 = 0.3; ρ ∈ [0, 1] is the share of it rolled over;
α ≥ 0 is how much the budget-setter cuts the next budget per unit left
unspent. On that reading the transition is possible after one period of
saving exactly when (ρ − α)·0.3 ≥ 0.3, that is ρ − α ≥ 1, which within
those ranges needs ρ = 1 and α = 0: full rollover and no cut. With ρ = 1
and α = 0.5, B_{t+1} = 1.15; with a rollover of 0.6 and no cut, 1.18.
Both fall short.

**What is held fixed.** The configurations, their holding cost, the
transition's peak, and that money buys the needed capacity within the
period. A: "money cannot always be converted into the resource needed on the relevant timescale"; where it is not, no budget rule helps.

## What it can show

- **Slack against current output can be the reconfiguration reserve.**
  Measured against what holding requires, the 0.3 is organizational slack
  ([TERM-107](../terms.d/TERM-107.md)): inputs beyond what current output needs. Its use, the
  transition, is invisible in that output. It is a reconfiguration reserve
  ([TERM-106](../terms.d/TERM-106.md)) built in installments: the transition's slack is 0.6, the
  budget gives 0.3 of it each period, and carry-over
  supplies the rest.
- **Expiry forecloses it.** With ρ < 1 the balance is lost at the period's
  end. Liebman and Mahoney ([NOTE-1553](../notes.d/NOTE-1553.md); [THEORY-1421](../theory.d/THEORY-1421.md)) find that expiring
  budgets produce wasteful year-end spending, and that rollover is
  useless without the budget-setter's commitment.
- **The ratchet forecloses it.** With α > 0, unspent funds signal reduced
  need and cut the next budget: the incentive ratchet of [TERM-110](../terms.d/TERM-110.md).
  Siemroth ([NOTE-1594](../notes.d/NOTE-1594.md); [THEORY-1410](../theory.d/THEORY-1410.md)) advises: "Principals should therefore
  publicly commit to not cut budgets if funds are returned or saved." In
  this case that commitment is what keeps the transition possible.
- **Allocation by observed activity reads the 0.7 as the need.** A
  budget-setter who funds what it sees spent sees 0.7 and no transition.
  That is one mechanism for [QUESTION-386](../questions.d/QUESTION-386.md), here acting on a
  reconfiguration reserve rather than on competence; the competence
  version is [CLAIM-558](../claims.d/CLAIM-558.md)'s decay.

## What it cannot show

- **That real budgets have these numbers**, or that real transitions have
  a single peak within a period. Spreading a transition over periods
  would change the comparison, which needs a cumulative model.
- **That α is what any budget-setter does.** It is a reading of A's
  symbol, not a fitted rule.
- **That saving is costless.** Holding 0.3 back for a period has an
  opportunity cost the case omits.
