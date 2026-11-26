---
status: Proposed
title: 'Jurisdictions over shared states can leave a system without valence'
statement: >-
  Assigning an organization's contests to regions, each governed by a
  different perspective whose own ranking is consistent, can make the
  ordering its contests would be settled along cyclic when the regions
  share states, so that the system has no valence though every perspective
  and every region has an ordering; and where the perspectives agree on one
  of the shared pairs, the same assignment can give a potential that is no
  perspective's ranking; so where jurisdiction boundaries fall decides
  whether an organization has valence at all, and which
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction of LEAD-tmpuszbx's cases 6 and 6a: that,
  under the stated one-hop influence and influence-weighted settlement, the
  winning moves of case 6 are not a cycle, or case 6a's potential is one of
  the perspectives' rankings. Not defeated by settlement rules under which
  no such assignment cycles, which the claim does not exclude; it states a
  possibility.
tags:
- self-governance
- emotion-and-affect
- game-theory
date: '2026-11-26'
line:
- organizational-affect
- will-organization
complements:
- CLAIM-tmpic0m1
- CLAIM-434
uses:
- TERM-017
- TERM-076
- TERM-023
summary: >-
  Found by [LEAD-tmpuszbx](../leads.d/LEAD-tmpuszbx.md)'s computation, 2026-11-26. It corrects the
  workbench entry's scenario 3, which had said a jurisdiction split
  without interaction has a composite potential; a split over states that
  the regions share can instead cycle. It is a relative of Sen's Paretian
  liberal, in which decisive personal domains together with the Pareto
  rule yield a cyclic social preference; Sen is not on the record. The wording and the
  construction are the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: TERM-076 — Proposed; the definition of valence used -->

# CLAIM-tmpzzeqo: Jurisdictions over shared states can leave a system without valence

## The construction

The states are a, b and c, and there are two perspectives, P1 with
b ≻ a ≻ c and P2 with c ≻ a ≻ b. Each ranking is consistent, and they
disagree on every pair. Jurisdiction ([TERM-017](../terms.d/TERM-017.md): "which constraints count
as applicable to this case") assigns the pair (b, c) to region y, which P2
governs, and the pairs (a, b) and (a, c) to region x, which P1 governs.
Influence is one-hop ([CLAIM-282](CLAIM-282.md)), and a pair is settled by
influence-weighted vote. The winning moves are then:

- a → b in region x, where P1 prefers b;
- c → a in region x, where P1 prefers a;
- b → c in region y, where P2 prefers c.

That is a cycle, a → b → c → a. By [CLAIM-434](CLAIM-434.md) there is no potential, and so
by [TERM-076](../terms.d/TERM-076.md) there is no valence. Both the run and the check are in
scratch/studies/lead-tmpuszbx/would_prevail.py, case 6.

Case 6a changes P2 to c ≻ b ≻ a, so the perspectives agree on (a, b). The
winning moves are then c → a and b → c, and the potential is a ≻ c ≻ b.
That is neither perspective's ranking: [TERM-076](../terms.d/TERM-076.md)'s "nobody's ranking until
it is shown to be one", produced here by jurisdiction. Case 6′ gives P1
all three pairs and recovers P1's ranking.

## What it says

Jurisdiction is a dimension of the will-organization ([TERM-023](../terms.d/TERM-023.md)), and this
claim shows that it does work for valence of its own. With the rankings
and the influence held fixed, moving one pair across a regional boundary
turns a system with valence into one without it. The organizational
reading: departments that are each internally consistent and each decisive
in their own domain can leave the whole without a common currency, where
their domains touch the same states.

It is a relative of Sen's liberal paradox, in which decisive personal
domains together with the Pareto rule yield a cyclic social preference.
Here domain decisiveness alone is enough, because the cycle runs through
contested pairs only. Sen is prior art for the mechanism and should be
registered. The claim adds the reading for organizational valence.

## What it does not say

That every jurisdiction split over shared states cycles: case 6a does not.
Nor that a will-organization should avoid shared states. The cycle can
be broken by precedence across regions, as in case 6′, and that is a
design choice the claim leaves open.
