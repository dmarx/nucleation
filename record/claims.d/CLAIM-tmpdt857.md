---
status: Active
title: 'Blackwell''s order measures what an ideal decision-maker could do, not what a given receiver can reconstruct, and the line''s claims that a rendering can improve access describe garblings that real receivers do better with, which is the shape of the Blackwell thesis''s own defeat condition'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Conceded on 2026-10-10 and reconciled by CLAIM-tmp0jq5k:
    Blackwell's order is the ceiling on what a rendering makes
    possible, and a receiver's access is usable information, which a
    garbling can raise. CLAIM-087 v2 is stated for receivers, and
    CLAIM-050 v2's condition no longer counts a bounded receiver's
    gain as a defeat of the order.
role: counter
tags:
- information-theory
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-087
- CLAIM-081
grounds:
- THEORY-156
- THEORY-176
objects_to:
- CLAIM-050
uses:
- TERM-034
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal and
  structure lenses); no turn of the exchange connects the two claims. A
  generator that sees only the text makes its image a garbling of the
  text about the situation, so by Blackwell's theorem the image is no
  better for any decision. [CLAIM-087](CLAIM-087.md) says such an image can improve
  access. Either that effect is impossible, or judged access is not
  Blackwell informativeness, and then [CLAIM-050](CLAIM-050.md)'s standard is not the one
  [CLAIM-115](CLAIM-115.md)'s receiver and its defeat condition use. It meets the shape
  of [CLAIM-050](CLAIM-050.md)'s defeat condition, not its letter. It is distinct from
  [CLAIM-140](CLAIM-140.md), which sets the analyst against the receiver: this sets the
  ideal receiver against an actual one.
---
<!-- inactive-ok-file: CLAIM-050 — Proposed; open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: CLAIM-087 CLAIM-081 CLAIM-076 — Proposed; the improvement, legibility and cross-modal claims this objection rests on or cites, open -->
<!-- inactive-ok-file: CLAIM-115 — Proposed; the manuscript's thesis, cited for its receiver and its defeat condition, open -->
<!-- inactive-ok-file: THEORY-156 THEORY-176 — Proposed; cited as the readings of Blackwell's order and of restricted decoders, not as settled -->
<!-- inactive-ok-file: CLAIM-tmp0jq5k — Proposed; the record's reconciliation of this objection, cited as open -->

# CLAIM-tmpdt857: Blackwell's order measures what an ideal decision-maker could do, not what a given receiver can reconstruct, and the line's claims that a rendering can improve access describe garblings that real receivers do better with, which is the shape of the Blackwell thesis's own defeat condition

## The objection

Blackwell's order quantifies over every decision rule. In [THEORY-156](../theory.d/THEORY-156.md), α is
more informative than β if, "for every closed bounded convex set A of loss
vectors, every risk vector attainable with β is attainable with α". The
decision-maker it describes may use any rule at all. So a garbling can
never be better for that decision-maker, in any problem.

**The cross-modal chain is a garbling.** Let a generator see only the
text u, so that its channel T(v | u) does not depend on the situation z.
Then

P(V = v | Z = z) = Σ_u T(v | u) P(U = u | Z = z),

so P(V | Z) is T applied to P(U | Z). The image is a garbling of the text
about the situation, and by Blackwell's theorem it is no better than the
text for any bounded decision problem about the situation. The generator's
general knowledge of the world does not change this, so long as it does
not depend on the item's situation. The record's own control makes this
the design. [CLAIM-076](CLAIM-076.md) quotes C7 Appendix D: "For cross-modal chains, do not
let captioners see the source text or the intended communicative condition
unless testing a specified side-information intervention." Each stage is
then a garbling of the one before it.

**The line says such a rendering can do better.** [CLAIM-087](CLAIM-087.md) quotes A97 §6:
"an image might convey solidarity through posture or facial expression
more effectively than the source text's literal content alone". Its defeat
condition is that "judged access to the source's interpersonal relation
never rises above the text-only baseline at any stage". [CLAIM-081](CLAIM-081.md) carries
A86 §3's version: the telephone game is progressive garbling, and "a
message can become more legible while becoming less informative about what
originally happened".

So one of two things holds.

- [CLAIM-087](CLAIM-087.md)'s effect is impossible, if access means what an ideal
  decision-maker could do. Then its prediction fails by theorem, and no
  study is needed to settle it.
- Judged access is not Blackwell informativeness. A real receiver who does
  better with the garbling than with the source was not using the best
  rule on the source, which is what Blackwell's order assumes. Then
  [CLAIM-050](CLAIM-050.md)'s standard is not the one the line's receiver uses.

The second is the likelier, and it is the one that costs the argument.
[CLAIM-115](CLAIM-115.md) makes survival relative to what "a receiving system can still
reconstruct and act upon". Its defeat condition is stated on "Human
judgements of communicative fidelity", which are a bounded receiver's.
[TERM-034](../terms.d/TERM-034.md) defines fidelity "relative to an interpreter". [CLAIM-115](CLAIM-115.md) rests on
[CLAIM-050](CLAIM-050.md), and [CLAIM-050](CLAIM-050.md)'s order describes no particular interpreter.

**[CLAIM-050](CLAIM-050.md)'s defeat condition names this case.** "A case where one
rendering is a garbling of another yet is judged better on every
communicative task the manuscript names, which would show the Blackwell
order is the wrong standard rather than an incomplete one." [CLAIM-087](CLAIM-087.md)'s
case has that shape and does not meet the letter. It concerns one task,
access to one relation, not every task the manuscript names, so it does
not defeat [CLAIM-050](CLAIM-050.md). But Blackwell's theorem forbids a garbling to be
better on any single task. So a garbling that real receivers do better
with, on even one task, shows that their standard is not Blackwell's order
for that task. [CLAIM-081](CLAIM-081.md)'s legibility is not a task in the manuscript's
family Q, and it supports the point only. The record holds [CLAIM-087](CLAIM-087.md) and
[CLAIM-050](CLAIM-050.md) both as Proposed and does not connect them.

**The nearest acknowledgement is for networks.** [THEORY-176](../theory.d/THEORY-176.md)'s relation 2:
"The rules the stitched network can use are A_{>ℓ} ∘ s with s ∈ S, not
every measurable rule on r. Its loss bounds r's best attainable risk for
that problem from above". That is the same gap between ideal and
restricted decision rules, stated for stitching and not for receivers.
[QUESTION-016](../questions.d/QUESTION-016.md) credits improvement to "interpreters with side information".
In the blind-captioner design there is none.

## What it does not say

- It does not say [CLAIM-087](CLAIM-087.md) is false. Its effect is possible for a bounded
  receiver.
- It does not say [CLAIM-050](CLAIM-050.md) is false. Blackwell's order is the right
  standard for what a rendering makes possible in principle. The objection
  is that the line uses that standard for its formal ground, and a
  receiver's standard for its thesis and its tests.
- It does not repeat [CLAIM-140](CLAIM-140.md). That claim contrasts the analyst's probe
  system with the receiver. This one contrasts an ideal receiver with an
  actual one.

## What would answer it

- A receiver-restricted order, with decision rules limited to a stated
  class, as in "usable information". That order loses Blackwell's garbling
  theorem, as [THEORY-176](../theory.d/THEORY-176.md)'s relations show for stitching, so it needs its
  own results.
- Or an argument that judged access tracks ideal informativeness, together
  with an account of what [CLAIM-087](CLAIM-087.md)'s prediction then means.
