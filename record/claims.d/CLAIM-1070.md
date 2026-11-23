---
number: 1070
status: Proposed
formerly:
- CLAIM-tmpcag0t
title: 'The governance of an adaptive organization is partly the governance
  of its temporal response structure, the rates at which it detects, absorbs,
  resists, corrects, learns from and reorganizes in response to different
  classes of demand: identity stabilization makes selected relations persistent
  across faster fluctuations, adaptive capacity keeps effective control over
  those relations, including their persistence and coupling, and an appropriate
  architecture preserves the capacity to reshape that spectrum without losing
  the conditions for viable organization'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144), the owner's
    manuscript from the exchange "Explain First Contact RL": A48 §1 and
    §15 state it: the spectrum and the capacity to transform it as objects
    of governance. No other change.
role: thesis
warrant: interpretive
defeated_if: An organization that meets every declared demand across timescales
  with a response spectrum it cannot change, in an environment whose demand
  family changes; or one that keeps its capacity to reshape its spectrum while
  losing the conditions of viable organization, without that counting as a
  failure. Also defeated if it only restates CLAIM-1066 and TERM-167
  with nothing added by making the response spectrum itself the object of
  governance.
tags:
- self-governance
- control-theory
- society-and-governance
date: '2026-11-23'
line:
- will-organization
- realizability
rests_on:
- CLAIM-1066
- CLAIM-099
complements:
- CLAIM-1152
summary: A42's retained thesis in the exchange "Explain First Contact RL"
  (ChatGPT, third share of 2026-11-22), answering the owner's U22, which quoted
  A40's "designing and maintaining the spectrum of organizational response
  times" and asked A to "double-click" on it. The owner quoted this thesis
  back at U23 with others. Quoting is not endorsing. The wording is A's (ChatGPT,
  in the exchange of 2026-11-22); adopting it is the owner's call.
works:
- governance-of-possibility
---

<!-- inactive-ok-file: CLAIM-711 CLAIM-758 CLAIM-1066 TERM-167 — Proposed; cited in this filing of 2026-11-23 (third share) -->

# CLAIM-1070: The governance of an adaptive organization is partly the governance of its temporal response structure, the rates at which it detects, absorbs, resists, corrects, learns from and reorganizes in response to different classes of demand: identity stabilization makes selected relations persistent across faster fluctuations, adaptive capacity keeps effective control over those relations, including their persistence and coupling, and an appropriate architecture preserves the capacity to reshape that spectrum without losing the conditions for viable organization

## The claim

A42: "The governance of an adaptive organization is partly the
governance of its temporal response structure: the rates at which it
detects, absorbs, resists, corrects, learns from, and reorganizes in
response to different classes of demand." And: "Adaptive governance =
demand-appropriate response + viable capacity to retune response."

## Steps (A42)

- **The response operator, not the eigenvalues.** G(s) = C(sI − A)⁻¹B =
  Σ_j (Cv_j)(w_jᵀB)/(s − λ_j). A mode's weight in governance is its
  persistence (λ_j), its controllability (w_jᵀB) and its consequence for
  demands (Cv_j). This adds the third factor to [CLAIM-1192](CLAIM-1192.md); a dated
  note there records it.
- **The filter:** [CLAIM-1152](CLAIM-1152.md).
- **Multiband architecture.** "The rate of executing a decision can be
  separated from the rate of revising the rules that authorize it"
  ([CLAIM-711](CLAIM-711.md)).
- **Four dimensions of the spectrum:** relaxation, sensing, control and
  correction, and maintenance and revision. "the bottleneck can move".
  The four failures of [CLAIM-568](CLAIM-568.md) apply.
- **Slow modes can entrench error.** [CLAIM-400](CLAIM-400.md)'s maintained legibility
  state adds terms in 1/(1 − λ), so "an initially useful standard can
  become path-dependent governance architecture" ([CLAIM-758](CLAIM-758.md)).
- **The design problem.** Choose θ and π to minimize operating,
  maintenance and reconfiguration costs, subject to [TERM-115](../terms.d/TERM-115.md) readiness
  for each demand and to the viability kernel of [TERM-167](../terms.d/TERM-167.md). The costs
  "need not be commensurable".

## Admission ([ADR-075](../decisions.d/ADR-075.md))

*A separating case.* [CLAIM-1066](CLAIM-1066.md) and [CLAIM-099](CLAIM-099.md) hold of an organization
whose slow modes stay controllable and whose capacity to govern among
regimes is kept, but whose demand family never changes. In it there is
no call to reshape the spectrum, and the claim's last clause is idle.
What the claim adds is that the demand distribution moves, so the
spectrum must be retunable, and that capacity is a further object of
governance.

## Note of 2026-11-23: the manuscript governance-of-possibility

Restatement. The central formulation of the owner's manuscript (ADR-
tmpsfjxu, A48 §15), "adaptive governance as the maintained viability of a
demand-appropriate temporal response repertoire", restates this claim with
[CLAIM-1066](CLAIM-1066.md) and [TERM-167](../terms.d/TERM-167.md)'s second-order kernel,
adding only "justified" demands. Audited ([ADR-075](../decisions.d/ADR-075.md)): no separating case,
derivation or discriminating prediction was found beyond them, and
"appropriate" is a free parameter, so it is a recap and no claim is filed.

## Note of 2026-11-23: A50's revision of the thesis

<!-- inactive-ok-block: CLAIM-1188 CLAIM-1003 — Proposed, filed from A50 of the exchange "Explain First Contact RL" on 2026-11-23 -->
A50 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23) quotes this thesis's short form, "Regulation governs the evolving repertoire of temporal responses to demands", as the article's previous thesis and proposes "a significant revision": regulation governs "the evolving relationship between the demands an industrial ecology can recognize and formulate, and the responses it can organize, realize, and maintain" ([CLAIM-1188](CLAIM-1188.md)). What it adds is the query side, the capacity to formulate demands, whose loss is harder to detect than a loss of response ([CLAIM-1003](CLAIM-1003.md)). Whether the revision replaces this thesis in the manuscript is the owner's call; the claim is unchanged.
