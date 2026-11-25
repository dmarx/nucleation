---
number: 1281
status: Active
formerly:
- CLAIM-tmpj4pw3
title: 'Responses split under attribution reversal'
statement: >-
  Under reversal of a social attribution with its grounds held fixed, every
  response splits uniquely into a part that reverses with the attribution
  and a part that does not: conformity and defiance lie wholly in the first
  and a response governed by the grounds alone wholly in the second, so the
  size of the reversing part, not its direction, measures how far the
  attribution sets the terms of response; the transformation type records
  only which parts are present, and reversing the attribution together with
  its grounds measures nothing
version: 2
history:
- version: 2
  date: '2026-11-24'
  note: >-
    Active: an independent checker, who did not write it, reproduced every
    computation in it with its own code (2026-11-24). The owner left the
    promotion of verified entries to the assistant's discretion.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the decomposition (a response function on a symmetric range
  of attributions that does not split uniquely into a part even and a part
  odd under reversal); or a showing that, with the grounds held fixed, a
  response governed by the grounds alone has a nonzero reversing part, so
  that the measure does not separate the attribution's authority from the
  grounds'.
tags:
- mathematics
- self-governance
- social-identity
date: '2026-11-24'
line:
- distributed-agency
- formal-apparatus
summary: >-
  Fills a gap in A8 §4 and A9 §VI of the exchange "Memes, Contracts, and
  Systemic Normativity" (ChatGPT, 2026-11-24). A8 lets the group C2 act
  on a scalar attribution by reversal and notes that conformity (r = s)
  and opposition (r = −s) both transform by the sign character, so
  "Defiance and submission can be structurally related forms of
  governability", which is [CLAIM-425](CLAIM-425.md)'s point and Cooley's "remoter
  conformity" in [CLAIM-415](CLAIM-415.md). A9 also states equal sensitivity, |dr/ds| = 1,
  just before calling the shared sign transformation "a miniature
  character-theoretic result". The transformation type
  does not carry sensitivity, and it separates attribution from grounds
  only if the grounds are held fixed. This claim gives the decomposition
  that does, checked with python3 -I. The construction is A8's; the
  decomposition and correction are the assistant's. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-415 CLAIM-425 — Proposed; the held claims this formalizes -->

# CLAIM-1281: Responses split under attribution reversal

## The source and the gap

A8 §4, on "I am whatever you say I am": with s a social characterization
and R_P(s) the response, A8 writes R_conform(s) = s, R_oppose(s) = −s
and R_indifferent(s) = c. Let C2 act by reversing s. "Both conformity and
opposition transform according to the sign representation under reversal
of the external signal. ... Their policies differ, but their transformation
character, under this particular group action, is identical." A9 §VI adds that
"both exhibit the same absolute dependence", |dr₊/ds| = |dr₋/ds| = 1, and
then calls the shared sign transformation "a miniature character-theoretic
result"; the slope sits beside that result, not inside it.

The first statement is right. The second does not follow from it: equal
slope is a property of the two functions A8 chose, not of how they
transform. And the construction says nothing about what is held fixed when
s is reversed, which decides whether it measures anything.

## The claim

Let a response r(s, g) depend on an attribution s, ranging over a set
closed under s ↦ −s, and on the grounds g the attribution would answer to.
Let C2 act by reversing s with g held fixed.

1. **Decomposition.** r = r₊ + r₋ uniquely, with
   r₊(s, g) = ½[r(s, g) + r(−s, g)] unchanged by reversal and
   r₋(s, g) = ½[r(s, g) − r(−s, g)] reversed by it. These are the
   trivial and sign components.
2. **Where the orientations lie.** Conformity (r = s) and opposition
   (r = −s) are wholly r₋; they differ by the factor −1. A response
   governed by the grounds alone, r = f(g), is wholly r₊. A constant
   c ≠ 0 is wholly r₊.
3. **The measure.** The size of r₋, for instance its root mean square over
   the attributions met, measures how far the attribution, as distinct
   from the grounds, sets the response. Its sign does not enter: defiance
   scores as conformity does. This is [CLAIM-425](CLAIM-425.md)'s "both let the
   judgements set the terms of response" as a quantity.
4. **What the transformation type does not carry.** r = 0.05s and r = s³
   transform exactly as r = s does, with very different sensitivity; the
   zero response (A8's indifference with c = 0) satisfies both
   r(−s) = −r(s) and r(−s) = r(s). So "same character" identifies which
   components are present, not how large they are; A9's |dr/ds| = 1 is an
   extra assumption.
5. **The anchoring condition.** If reversing s also reverses g, as it does
   when attributions track their grounds, a person governed only by the
   grounds has a reversing part as large as a conformist's. The action must
   reverse the attribution independently of the grounds, as [CASE-140](../cases.d/CASE-140.md) varies
   an attribution's breadth with its words fixed. This is what A8 §11 asks
   for in "independently anchored transformations of social attribution".

**Check.** `python3 -I` on s ∈ [−1, 1], 201 points, root mean square:
conformity and opposition ‖r₋‖ = 0.580, ‖r₊‖ = 0; c = 0.3 gives ‖r₋‖ = 0,
‖r₊‖ = 0.300; r = 0.05s gives ‖r₋‖ = 0.029; r = s³ gives 0.384; r = 0
satisfies both parities; r = 0.4 + 0.5s gives ‖r₋‖ = 0.290 and
‖r₊‖ = 0.400.

## What it does not say

- **Not that the reversing part is all of social influence.** A response
  can depend on the attribution evenly, for example on its breadth or
  salience whatever its direction ([CASE-140](../cases.d/CASE-140.md)); that part is in r₊ and this
  measure misses it. A fuller test would let the group act on breadth too.
- **Not that a small reversing part is self-governance.** [CLAIM-425](CLAIM-425.md) asks
  also that access to others' judgements be kept; a closed response
  (A8 §10's "Nothing you say can tell me who I am") has a small r₋ and
  fails that clause.
- **Not a result in character theory proper.** Only the two-element group
  and its two characters are used; nothing here needs [CLAIM-132](CLAIM-132.md)'s
  conditions beyond that.
