---
number: 1221
status: Proposed
formerly:
- CLAIM-tmp2jhc1
title: 'A fallback capacity can matter without being used: it keeps a party able to refuse, and so changes the terms others offer, so redundancy that keeps credible alternatives within a governing relationship (constitutional redundancy) differs from redundancy that keeps performance when a component fails (operational redundancy), and optimizing away capacity that ordinary operation never exercises can remove a condition of non-domination'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that, in the relationships the claim covers, the terms a party
  obtains do not depend on alternatives it does not exercise: that its
  share and its say are set by its contribution or by what it actually
  does, not by what it could do instead, so that removing an unexercised
  fallback leaves its terms unchanged. Not defeated by fallbacks whose
  upkeep costs more than the terms they protect are worth: the claim says
  the value is not measured by use, not that every fallback is worth
  keeping, which is QUESTION-395's weighing.
tags:
- society-and-governance
- game-theory
- ethics
date: '2026-11-24'
line:
- dependence-and-domination
- readiness
works:
- governance-of-becoming
uses:
- TERM-124
complements:
- CLAIM-690
- CLAIM-682
- CLAIM-670
bears_on:
- QUESTION-395
summary: >-
  A24 §7 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24). "A fallback capability can support a party's
  ability to refuse unacceptable terms." "Their value cannot be assessed
  exclusively through how often they are exercised. A reserve may make it
  unnecessary to exercise the power of withdrawal by changing the terms
  others are willing to offer." Operational redundancy "Maintains
  performance when a component fails"; constitutional redundancy
  "Maintains credible alternatives when a governing relationship becomes
  inadequate or objectionable." "optimizing away every apparently unused
  capacity can inadvertently optimize away the conditions of
  non-domination." The bargaining step is the assistant's derivation,
  checked (see the body). The wording is A's (ChatGPT, in the exchange
  'Memes, Contracts, and Systemic Normativity'); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: TERM-124 CLAIM-690 CLAIM-682 — Proposed; the term this is stated in and the held claims on control over terms, domination and produced dependence -->

# CLAIM-1221: A fallback capacity can matter without being used: it keeps a party able to refuse, and so changes the terms others offer, so redundancy that keeps credible alternatives within a governing relationship (constitutional redundancy) differs from redundancy that keeps performance when a component fails (operational redundancy), and optimizing away capacity that ordinary operation never exercises can remove a condition of non-domination

## The claim

A24 §7: "If cooperation encourages specialization, then maintaining some
apparently redundant independent capacities may have moral and political
significance. A fallback capability can support a party's ability to
refuse unacceptable terms." Its examples: "alternative suppliers, emergency
savings, independent expertise, collective bargaining institutions,
redundant infrastructure and protected opportunities for alternative
inquiry."

| Type (A24 §7) | Function |
|---|---|
| Operational redundancy | "Maintains performance when a component fails." |
| Constitutional redundancy | "Maintains credible alternatives when a governing relationship becomes inadequate or objectionable." |

"The same capability can serve both functions. An independent assessment
process may rarely be needed during ordinary operation. But its existence
can prevent another process from acquiring unrestricted interpretive
authority."

## The bargaining step (gap filled)

A24 asserts that a reserve changes "the terms others are willing to offer"
without showing it. A22 §9 and A24 §4 use the model that shows it, the
equal-weight Nash bargaining solution: with joint value V and outside
options o_A and o_B,

u_B = o_B + (V − o_A − o_B)/2 = (V − o_A + o_B)/2,

so each unit of B's outside option raises B's share by half a unit, and
lowers A's by the same, **whether or not B ever takes the outside option**:
at the solution B stays in the relationship. With A22's numbers (V = 20,
o_A = 4), B gets 8, 9 or 10 as o_B is 0, 2 or 4 (checked with
`python3 -I`). The fallback's value is in the disagreement point, which is
never reached. This is the textbook threat-point property, stated here
because the claim needs it and A does not give it.

A24 §4's model shows the reverse: specialization raises joint production
(10 + 16s) while lowering B's independent capacity (5(1 − s(1 − p)), with
p the protection of B's fallback). At full specialization and no
protection, the split is 14.75 to 11.25 in A's favour; with full
protection, 12.25 to 13.75 (checked with `python3 -I`). A24's caption:
"Maintaining fallback capacity is not priced in this model, so it cannot
establish an optimal degree of protection."

## Why "non-domination"

The record's domination ([TERM-124](../terms.d/TERM-124.md)) is a capacity, "used or not", to set or
change the terms on which a party can act, exit, contest or renegotiate,
not answerable to the party; [CLAIM-682](CLAIM-682.md)'s test includes the dependent's
lack of "effective means of protection, influence, challenge or justified
withdrawal". A constitutional reserve is one such means: it keeps exit
credible. Removing it because ordinary operation never draws on it removes
the condition while leaving every observable of operation unchanged, which
is why efficiency measured on use will tend to remove it.

## What it does not say

- Not that every unused capacity is a constitutional reserve, or worth its
  cost. Telling a warranted reserve from waste when operation seldom
  exercises it is [QUESTION-395](../questions.d/QUESTION-395.md), which this claim bears on by giving one
  thing the reserve does that its use-rate does not show.
- Not that a party with a fallback is undominated: [CLAIM-690](CLAIM-690.md) holds that
  what sorts dependence is control over exit, renegotiation and the
  conditions of supply, of which a fallback secures only the first.

## Note of 2026-11-25: the threat point run on a fallback the supply erodes, from the manuscript governance-of-becoming, Article 9
<!-- inactive-ok-file: CLAIM-1237 CASE-264 — Proposed or new; the computation and the bargaining case it uses -->

The bargaining step above holds the outside option fixed. [CLAIM-1237](CLAIM-1237.md)
lets it decay: B's (there, P's) fallback is a capacity in [CLAIM-605](CLAIM-605.md)'s model,
eroded by substitutive supply, and the split is [CASE-264](../cases.d/CASE-264.md)'s arm A. The
half-unit property holds at every step of the decay (checked), and the
share falls from 6.000 to 4.199 over six time units while P never exits.
So the claim's "changes the terms others offer" runs in both directions:
a reserve kept raises the terms, and one that the arrangement's own
supply lets decay lowers them, unnoticed by any measure of use. Past
[CLAIM-605](CLAIM-605.md)'s deadline ending the supply no longer restores the reserve, so
the claim's warning about "optimizing away capacity that ordinary
operation never exercises" has a timing in that model. The script and its
output of 2026-11-25 are under
scratch/manuscripts/governance-of-becoming/analysis/. The computation is
the assistant's, run by its filer only; no change of status. The wording
is the assistant's (Claude, in this session).

**Correction of 2026-11-25 (the review of Part III, Part B).** "So the
claim's 'changes the terms others offer' runs in both directions"
overstates what is new. This claim's own body already holds the reverse:
"A24 §4's model shows the reverse", specialization lowering B's
independent capacity and moving the split to 14.75 to 11.25 in A's
favour, as comparative statics. What [CLAIM-1237](CLAIM-1237.md) adds is that
reverse in time, with a deadline: the fallback decays under the
arrangement's own supply, the terms fall at each renegotiation, and
ending the supply restores them only before [CLAIM-605](CLAIM-605.md)'s deadline. Read
the sentence as "the A24 §4 reverse, now in time, with a deadline".
Since this note, [CLAIM-1237](CLAIM-1237.md) has been revised (version 2) and
rechecked by the review's reader from separate code. No change of
status. The wording is the assistant's (Claude, in this session);
adopting it is the owner's call.
