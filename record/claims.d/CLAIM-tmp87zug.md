---
status: Proposed
title: 'What freed effort builds leaves the withdrawal cost unchanged'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the script; or a showing that the model's
  separability, each capacity learned only from its own task's work, is
  what does the work, by a model in which a capacity built with freed
  effort shortens the substituted task's recovery, so that the claim holds
  only where skills do not transfer, which it then must say.
tags:
- society-and-governance
- learning-and-conditioning
- economics
- control-theory
date: '2026-11-26'
line:
- transient-support
- dependence-and-domination
rests_on:
- CLAIM-602
bears_on:
- QUESTION-tmpsgbj7
statement: >-
  In CLAIM-602's model extended to two capacities, reinvesting the effort
  a supply frees in a second task leaves the substituted task's kept
  capacity, and the time to meet its demand again once the supply stops,
  exactly where substitution alone put them, and under a finite effort
  budget the new capacity is itself held only while the supply lasts; so
  reinvestment answers the Luddite objection for capacity and not for
  dependency, which turns on the supply's security
summary: >-
  The assistant's gap fill on A4 §§8–9 of the exchange "Alignment
  consequences brainstorm" (ChatGPT, 2026-11-26). A4 proposes extending
  [CLAIM-602](CLAIM-602.md) to a capability vector with a finite budget and shows only a
  stipulated linear widget ([CLAIM-tmpz33db](CLAIM-tmpz33db.md)). Done in the model's own
  dynamics: the first capacity's steady state, 0.625 at a supply share of
  0.5 and 0.25 at 0.9, does not depend on reinvestment; recovery after 20
  units of full substitution is 6.38 units, [CLAIM-602](CLAIM-602.md)'s number, whatever
  was reinvested; with a finite budget the reinvested skill, 0.769 at
  exit, decays below 0.001 within 30 units as the first task reclaims the
  effort. Checked with python3 -I (scratch/formal/two_capacity_reinvestment.py).
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpz33db CLAIM-tmp5vitv ARG-tmpee3ck — filed from the same exchange, Open or Proposed -->
<!-- inactive-ok-file: CLAIM-603 CLAIM-690 — Proposed; the held claims on what sorts a dependency -->

# CLAIM-tmp87zug: What freed effort builds leaves the withdrawal cost unchanged

## The gap it fills

A4 §9: "Instead of assuming that work displaced by technology simply
disappears, allow the released time and effort to be allocated to
developing other capacities." It gives a widget whose formulas are
stipulated, not derived. The extension it proposes was not done, and
whether it answers the owner's U2 ([QUESTION-tmpsgbj7](../questions.d/QUESTION-tmpsgbj7.md)) depends on what it
shows.

## The model

[CLAIM-602](CLAIM-602.md)'s: demand 1 per unit time on task 1, output τC₁, capacity
dC_k/dt = λP_k(1 − C_k) − μC_k with λ = 1, μ = 0.3, τ = 1.5. The supply
does a share A of task 1 first, the party does P₁ = min(τC₁, 1 − A), and
reinvests a fraction r of the freed effort in task 2, P₂ = rA. With a
finite budget P₁ + P₂ ≤ 1, so when the supply stops and P₁ rises, P₂
falls.

## The derivation

1. **Separability.** C₁'s equation contains only P₁, and P₁ depends on A
   and C₁ alone. So C₁'s path, and every quantity [CLAIM-602](CLAIM-602.md) derives from
   it, is the same for every r. At steady share A < 1,
   C₁* = λ(1 − A)/(λ(1 − A) + μ): 0.625 at A = 0.5 and 0.25 at 0.9, for
   r = 0, 0.5 and 1. C₂* = λrA/(λrA + μ): 0.625 at A = 0.5, r = 1.
2. **Withdrawal.** After full substitution for 20 units, demand is met
   again 6.38 units after the supply stops, [CLAIM-602](CLAIM-602.md)'s figure, for each
   r.
3. **Finite budget.** At A = 1, r = 1, the party holds C₂ = 0.769 at exit.
   Once task 1 reclaims its effort, C₂ is 0.177 after 10 units and below
   0.001 after 30.

The sum C₁* + C₂* is 1.25 at A = 0.5, r = 1, above the unassisted 0.769,
because capacity saturates in effort; the sum means nothing, as A4 says
of its own widget, since the capacities are not commensurable.

## What follows

A4's objection is right about the accounting of capacity: the party with
reinvestment can do more, in a sense the one-capacity model cannot see
([CLAIM-tmpz33db](CLAIM-tmpz33db.md)). It leaves the dependency where it was. What the party
loses if the supply stops is the same, and with a finite budget it is
more, since the new capacity was paid for with effort the substituted
task now needs back. Whether that dependency is a pathology is not
settled by any capacity count: on the record's account it turns on the
supply, whether it is reciprocal or self-limiting ([CLAIM-603](CLAIM-603.md)), and who
controls the terms on which it is met ([CLAIM-690](CLAIM-690.md)). [CLAIM-tmp5vitv](CLAIM-tmp5vitv.md) applies
that test to supplied cognition. [ARG-tmpee3ck](../arguments.d/ARG-tmpee3ck.md) records the narrowing.

## Limits

- **No transfer.** A capacity built on task 2 that helps relearn task 1
  would shorten recovery. The model has none; the defeater says what
  would follow if transfer is what matters.
- **Parameters are [CLAIM-602](CLAIM-602.md)'s,** invented to show mechanisms.
