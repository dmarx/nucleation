---
status: Active
title: 'A regulation that only adds hard constraints to a fixed dynamical model can only shrink the compatibility complex of the public demands, so it cannot relieve their frustration; a regulation relieves frustration among the original demands only by changing the dynamics, through the technologies, infrastructure or access it brings about'
version: 3
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-057: every premise Active (CLAIM-582,
    CLAIM-347, CLAIM-361), no objection, derivation re-checked by brute
    force (20,000 random instances, no violation).
- version: 3
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-tmpsfjxu), the owner's
    manuscript from the exchange "Explain First Contact RL": A48 §2 states
    it: relief only by changing the dynamics. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  A regime that adds only hard constraints to a fixed model of the
  ecosystem and still makes a set of the original demands jointly
  attainable that was not attainable before. Since the derivation below
  shows none exists under the stated definitions, what would defeat the
  claim is a showing that the definitions misdescribe regulation: that
  the attainable histories of an ecosystem under a regime are not the
  histories of the unregulated model that its constraints admit.
tags:
- society-and-governance
- mathematics
- operations-research
date: '2026-11-22'
line:
- realizability
- distributed-agency
rests_on:
- CLAIM-582
- CLAIM-347
- CLAIM-361
summary: >-
  A31 §4 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-22): adding a hard constraint at fixed technologies, incentives
  and strategies reduces the admissible action set and "cannot expand
  what is feasible", but "a regulation may restrict immediate choices
  while expanding the ecosystem's longer-term repertoire of jointly
  viable configurations"; A33 §8 calls this developmental regulation. It
  is [CLAIM-582](CLAIM-582.md) carried to the compatibility complex of [CLAIM-347](CLAIM-347.md). The
  derivation is given below, and A31 §4's reform criterion, a strict
  enlargement of the complex for the same demands, follows from it. The
  idea is A's; the derivation and wording are the assistant's (Claude, in
  this session); adopting it is the owner's call.
works:
- governance-of-possibility
---

# CLAIM-tmpk4bou: A regulation that only adds hard constraints to a fixed dynamical model can only shrink the compatibility complex of the public demands, so it cannot relieve their frustration; a regulation relieves frustration among the original demands only by changing the dynamics, through the technologies, infrastructure or access it brings about

## The claim

Let D be the declared public demands, each an acceptance set A_j of
histories, and R(g) the histories attainable under regime g. The
compatibility complex is C(g; D) = {J ⊆ D : R(g) ∩ ⋂_{j∈J} A_j ≠ ∅}
([CLAIM-347](CLAIM-347.md); A33 §2 writes it so). Relief is a strict enlargement of the
complex for the same demands ([CLAIM-347](CLAIM-347.md)), judged against a fixed
reference set of them ([CLAIM-361](CLAIM-361.md)).

**Derivation.** If g′ adds only hard constraints to g under a fixed
dynamical model, every history admissible under g′ is admissible under
g ([CLAIM-582](CLAIM-582.md)), so R(g′) ⊆ R(g). Then for each J, R(g′) ∩ ⋂_{j∈J} A_j ⊆
R(g) ∩ ⋂_{j∈J} A_j, so every face of C(g′; D) is a face of C(g; D):
C(g′; D) ⊆ C(g; D). No strict enlargement is possible, so no relief. A
regime that relieves frustration among the original demands has
therefore changed the model: it has brought about technologies,
infrastructure, access rules or institutions that make histories
attainable which were not. That is A31 §4's case, a rule that leads
firms to develop cleaner processes so that environmental, safety and
supply demands that were incompatible become jointly attainable.

Checked by brute force with `python3 -I` over 20,000 random instances
(12 histories, 4 demands, random acceptance sets and nested attainable
sets): no instance had C(g′) ⊄ C(g).

## What follows for evaluating a reform

- **Abandoning a demand is not relief.** If the regime improves only
  because a demand was dropped, the complex has been computed for a
  different D ([CLAIM-347](CLAIM-347.md), [CLAIM-361](CLAIM-361.md)). A31 §4: "if the only change is that
  the regulator abandoned an inconvenient demand, the new regime hasn't
  relieved frustration under the original specification."
- **Incentives at fixed dynamics move realization, not possibility.** A
  tax or subsidy that changes which admissible history participants
  choose, without changing what is admissible, leaves C(g; D) where it
  was and changes how reliably a jointly acceptable history is realized
  ([CLAIM-tmpx9nrj](CLAIM-tmpx9nrj.md)).
- **A hard constraint can still be worth having at fixed dynamics.** It
  can improve a property required of every admissible path, as
  [CLAIM-582](CLAIM-582.md) says, and it can redistribute an unavoidable mismatch
  ([CLAIM-588](CLAIM-588.md)).

## What it does not say

It does not say that a regulation which changes the dynamics thereby
relieves anything. The new technology must actually enlarge R(g), and
participants must adopt it, which is the separate question of
realization. Nor does it say that relief is the only aim of regulation
([CLAIM-588](CLAIM-588.md)'s three design targets).
