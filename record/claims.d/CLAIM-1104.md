---
number: 1104
status: Proposed
formerly:
- CLAIM-tmph25dl
title: 'Identity stabilization and adaptability are not two ends of one scale:
  constraints that conserve selected relations across time make coordinated
  response possible and can make alternatives slow or costly to reach, so
  a constraint''s adequacy depends on the timescales of the demands it governs
  and on how fast it can be revised, and adaptive governance maintains a hierarchy
  of revisable constraints whose response times suit their demands, conserving
  selectively what enables later transformation'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144), the owner's
    manuscript from the exchange "Explain First Contact RL": A48 §5, §6
    and §15 state it: not one scale, adequacy relative to the demands. No
    other change.
role: thesis
warrant: interpretive
defeated_if: An organization in which every identity-conserving constraint
  either lowers or raises the cost of every later demanded change, so that
  stabilization and adaptability do lie on one scale; or one whose constraints'
  adequacy is the same for demands of every deadline and horizon. Also defeated
  if it only restates CLAIM-478 (rate differences make constraints), CLAIM-758
  (overconsolidation) and CLAIM-025 with nothing added by indexing adequacy
  to the demands' timescales.
tags:
- self-governance
- society-and-governance
- control-theory
date: '2026-11-22'
line:
- will-organization
- realizability
rests_on:
- CLAIM-478
- CLAIM-758
- CLAIM-025
complements:
- CLAIM-1144
summary: 'A38 of the exchange "Explain First Contact RL" (ChatGPT, second
  share of 2026-11-22), answering the owner''s U20. It accepts the tension
  and denies that it is a trade-off on one scale: stabilization lowers the
  cost of familiar operation and may raise the cost of unfamiliar reorganization.
  The wording is A''s (ChatGPT, in the exchange of 2026-11-22); adopting it
  is the owner''s call.'
works:
- governance-of-possibility
---

<!-- inactive-ok-file: CLAIM-184 CLAIM-423 CLAIM-478 CLAIM-758 TERM-167 — Proposed; cited in this filing of 2026-11-22 (second share) -->

# CLAIM-1104: Identity stabilization and adaptability are not two ends of one scale: constraints that conserve selected relations across time make coordinated response possible and can make alternatives slow or costly to reach, so a constraint's adequacy depends on the timescales of the demands it governs and on how fast it can be revised, and adaptive governance maintains a hierarchy of revisable constraints whose response times suit their demands, conserving selectively what enables later transformation

## The claim

A38's sharpened thesis: "Organizational identity is stabilized through
constraints that conserve selected relationships across time. These
constraints make reliable coordination possible but may also render
alternative organizations costly, slow, or inaccessible. Because demands
differ in urgency, duration, recurrence, and developmental horizon, the
adequacy of a constraint cannot be judged independently of the
timescales on which it operates and can be revised." And: "The goal is
selective conservation of what enables future transformation."

## Steps (A38)

- **Identity as a continuity relation.** It is not x_t = x_0. Identity is
  S_t ~_I S_t′ under a declared criterion, which A38 ties to [CLAIM-361](CLAIM-361.md)'s
  distinction between satisfying, reprioritizing, transforming and
  suppressing demands.
- **Slow relations as effective constraints**, ε ẋ = f(x, z, u), ż =
  g(x, z, u), with x ≈ h(z, u) on the slow scale: [CLAIM-478](CLAIM-478.md). Speeds as
  asymmetries of authority: [CLAIM-423](CLAIM-423.md).
- **Demands as predicates on histories over horizons, with deadlines.**
  Timely satisfaction needs T* ≤ τ, and readiness is [TERM-115](../terms.d/TERM-115.md)'s
  probability. "A system can possess the capability to respond while
  being organized too slowly to respond when it matters."
- **A minimal model:** [CLAIM-1010](CLAIM-1010.md).
- **Not always a trade-off.** A standard removes repeated negotiation and
  a rehearsed procedure speeds response, while consolidation raises the
  cost of changing the framework ([CLAIM-758](CLAIM-758.md), [CLAIM-184](CLAIM-184.md)).
- **A temporal readiness kernel.** Viab(M_D), with M_D the states whose
  readiness for each declared demand meets its reliability requirement:
  [TERM-167](../terms.d/TERM-167.md) indexed by demand class.
- **A table of five demand horizons** (immediate, operational,
  developmental, institutional, intergenerational), each with its
  governance capacity and failure mode, and the closing test: "When a
  system remains stable, what is it actually preserving—the organization
  needed to respond to future demands, or merely the conditions that keep
  its present regime in place?"

## Admission ([ADR-075](../decisions.d/ADR-075.md))

*A separating case.* Take an organization whose constraints settle fast
relations into slow ones ([CLAIM-478](CLAIM-478.md) holds), whose consolidation raises the
cost of one later acquisition ([CLAIM-758](CLAIM-758.md) holds), and whose operative,
governing and transforming capacities can fail apart ([CLAIM-025](CLAIM-025.md) holds).
Let every demand it faces have the same deadline and horizon. Then a
constraint's adequacy is not indexed to the demands' timescales, and the
claim's central clause has no work to do. What the claim adds is that
demands differ in timescale, so that one constraint can be adequate to
one and obstruct another. [CLAIM-1010](CLAIM-1010.md) shows this in a model.
