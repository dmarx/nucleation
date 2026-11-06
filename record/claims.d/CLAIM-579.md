---
number: 579
status: Proposed
formerly:
- CLAIM-tmpov8rf
title: 'A reserve is described by where in a configuration space it can be applied, not only by how much there is: an organization can hold ample slack and still be pinned, when none of it can be brought to bear at the bottleneck of the transition it needs'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Revised at the twenty-sixth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), so that its use of
    TERM-106 says which sense. The summary said "reconfiguration slack is a
    field over configurations", which is what a reserve held is, not the
    slack a transition needs; it now names TERM-106's reconfiguration
    reserve, and the body ties the reserve to the term's one-sided slack.
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the cases cited are all cases of nonfungible resources and
  nothing more, so that a vector of resource types (TERM-105) already
  says what location adds; or an organizational case in which slack reaches
  the bottleneck whenever its total suffices, across differences in where it
  sits, how it is coupled and who can direct it. Not defeated by mechanical
  cases in which location does not matter, since the claim is that it can.
tags:
- operations-research
- complex-systems
- society-and-governance
date: '2026-11-05'
line:
- readiness
complements:
- CLAIM-562
- CLAIM-586
grounds:
- THEORY-1418
uses:
- TERM-106
summary: >-
  The assistant's own hypothesis, offered at the owner's invitation on
  2026-11-05, from four readings that point the same way. In Stern, Pinson
  and Murugan's sheets, where actuators sit predicts success far better than
  how many there are; Hopkins's actuation spaces say where a flexure must be
  driven; nonfungible geometry ([CASE-212](../cases.d/CASE-212.md) and [CLAIM-586](CLAIM-586.md)) shows more
  of a resource does not fix the wrong geometry; and in Dollar and Howe's
  hand, coupling decides which freedoms can be driven at all. The proposal
  is that a reconfiguration reserve (TERM-106), the stock held for a
  transition rather than the slack the transition needs, is a field over
  configurations, what can be applied at each point, and that the transition threshold of
  [CLAIM-571](CLAIM-571.md) is met only where that field reaches the bottleneck. The
  obvious objection is that this restates nonfungibility; the claim is that
  location adds addressability, which a list of resource types does not
  carry. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CASE-205 CASE-212 CLAIM-562 CLAIM-577 NOTE-1596 — Proposed or Skimmed; entries of 2026-11-04 and 2026-11-05 from the readiness and constraint-architecture filings, cited as open -->

# CLAIM-579: A reserve is described by where in a configuration space it can be applied, not only by how much there is: an organization can hold ample slack and still be pinned, when none of it can be brought to bear at the bottleneck of the transition it needs

## The claim

[CLAIM-571](CLAIM-571.md) treats a transition's need as one number, the peak along the
best path, and a budget as one number to compare with it. The readings
suggest a reserve also has a location: the configurations at which it can
be applied. Write it as a(q), the extra capacity that can be brought to bear
at q. A path is affordable when r(γ(t)) ≤ B + a(γ(t)) along it, so what
matters is whether the reserve reaches the bottleneck configurations, not
its total ∫a or its maximum elsewhere. The reserve is TERM-106's
reconfiguration reserve, and the title's slack is that reserve, which
measured against current output is organizational slack (TERM-107). With
a the same everywhere and a budget of r(A), the condition is that a is at
least the slack from A, TERM-106's one-sided form; location matters when a
varies.

## Why it is plausible

- **Placement over count.** Stern, Pinson and Murugan ([NOTE-1571](../notes.d/NOTE-1571.md)): a
  few actuators that cover the folding islands succeed where many placed at
  random fail. [CLAIM-562](CLAIM-562.md) states it.
- **Where a mechanism must be driven.** Hopkins's actuation spaces
  ([NOTE-1596](../notes.d/NOTE-1596.md)) say where actuators must act to drive a permitted motion
  without parasitic error, which depends on stiffness, not on the freedom
  space.
- **Coupling decides addressability.** In Dollar and Howe's hand
  ([NOTE-1575](../notes.d/NOTE-1575.md)), one actuator drives eight joints, and which shapes it can
  command is fixed by the transmission, not by the actuator's strength.
  [CASE-205](../cases.d/CASE-205.md) is the constructed version.
- **Nonfungible geometry.** [CASE-212](../cases.d/CASE-212.md) and [CLAIM-586](CLAIM-586.md): no amount of a
  resource fills a face the geometry forbids.

## What it adds beyond nonfungibility

A vector of resource types ([TERM-105](../terms.d/TERM-105.md)) says what kinds of resource there
are. Location says where each can act. Two organizations with the same
vector of reserves can differ in whether any of it reaches the bottleneck:
trained staff on the wrong shift or in the wrong station, money that a rule
lets be spent only on operations, authority held by someone not present. On
this reading, a funding rule can preserve the total reserve and still pin
the organization by moving where the reserve may be applied, a variant of
[CLAIM-577](CLAIM-577.md)'s mechanism.

## What it does not say

- It is a hypothesis drawn from mechanical analogies and one constructed
  case. No organizational case in the record shows slack present in total
  and absent at the bottleneck.
- It gives no measure of location for organizations; the field a(q) is
  notation until one is found.
