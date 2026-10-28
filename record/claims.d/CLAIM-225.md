---
number: 225
status: Active
formerly:
- CLAIM-tmpdt857
title: 'Blackwell''s order measures what an ideal decision-maker could do, not what a given receiver can reconstruct, and the line''s claims that a rendering can improve access describe garblings that real receivers do better with, which is the shape of the Blackwell thesis''s own defeat condition'
version: 4
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Conceded on 2026-10-10 and reconciled by CLAIM-199:
    Blackwell's order is the ceiling on what a rendering makes
    possible, and a receiver's access is usable information, which a
    garbling can raise. CLAIM-087 v2 is stated for receivers, and
    CLAIM-050 v2's condition no longer counts a bounded receiver's
    gain as a defeat of the order.
- version: 3
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the reading of Xu et al. on usable
    information (NOTE-1048): the objection's two standards are
    Shannon and V-information, which that paper relates without
    mentioning Blackwell. The claim is unchanged.
- version: 4
  date: '2026-10-28'
  note: >-
    Split under ADR-061. The verdict in "What it does not say", that the
    line uses Blackwell's standard for its formal ground and a receiver's
    for its thesis and its tests, moved to ARG-tmpa4q9l, from CLAIM-050 to
    CLAIM-115, Proposed, which this claim now undercuts. The title is
    unchanged, because it is wholly about the subject matter. The body is
    unchanged.
role: counter
warrant: demonstrated
tags:
- information-theory
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-1096
- THEORY-176
objects_to:
- CLAIM-050
uses:
- TERM-034
undercuts:
- ARG-tmpa4q9l
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
rests_on:
- CLAIM-270
supports:
- CLAIM-087
---
<!-- inactive-ok-file: CLAIM-087 CLAIM-081 CLAIM-076 — Proposed; the improvement, legibility and cross-modal claims this objection rests on or cites, open -->
<!-- inactive-ok-file: CLAIM-115 — Proposed; the manuscript's thesis, cited for its receiver and its defeat condition, open -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited as the readings of Blackwell's order and of restricted decoders, not as settled -->
<!-- inactive-ok-file: CLAIM-199 — Proposed; the record's reconciliation of this objection, cited as open -->
<!-- inactive-ok-file: ADR-061 — Proposed; the decision under whose migration this entry was filed or revised -->
<!-- inactive-ok-file: ARG-tmpa4q9l — Proposed; the argument this claim's support verdict moved to, which it undercuts -->

# CLAIM-225: Blackwell's order measures what an ideal decision-maker could do, not what a given receiver can reconstruct, and the line's claims that a rendering can improve access describe garblings that real receivers do better with, which is the shape of the Blackwell thesis's own defeat condition

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

## Note of 2026-10-21: the two standards in the usable-information literature

Xu, Zhao, Song, Stewart and Ermon 2020 ([LIT-1309](../literature.d/LIT-1309.md)), read in full on
2026-10-21 ([NOTE-1048](../notes.d/NOTE-1048.md)), have this objection's split in their own
terms: Shannon information is the unrestricted predictor's (their Ω), and
V-information the restricted family's, which can be created by
computation, so that a function of the data can carry more of it than the
data ([THEORY-846](../theory.d/THEORY-846.md)). The ideal decision-maker's standard and the given
receiver's are I_Ω and I_V. The paper does not mention Blackwell, and its
quantity is for log loss only. The reconciliation in [CLAIM-199](CLAIM-199.md) stands; its
note of the same day says when the ceiling holds in V-information. The
claim is unchanged.

## Note of 2026-10-27: grounded in what it uses of Blackwell

The status review of this date ([ADR-057](../decisions.d/ADR-057.md)) moved this claim's ground from
[THEORY-156](../theory.d/THEORY-156.md) to [THEORY-1096](../theory.d/THEORY-1096.md). It uses Blackwell's definitions (an experiment, a
garbling, the informativeness order) or the easy direction, that a
garbling never helps a decision-maker free to choose any rule. Both hold
on any outcome spaces, with the proof written out there. [THEORY-156](../theory.d/THEORY-156.md)'s
general converse, which stays Proposed, is not used. Quotations of
[THEORY-156](../theory.d/THEORY-156.md) above are of the definitions it states.

## Note of 2026-10-27: the edge says what the claim uses

The status review of this date ([ADR-057](../decisions.d/ADR-057.md), [ADR-058](../decisions.d/ADR-058.md)) removed `rests_on: CLAIM-087`. The dilemma holds whatever [CLAIM-087](CLAIM-087.md)'s truth ("It does not say [CLAIM-087](CLAIM-087.md) is false"), and [CLAIM-087](CLAIM-087.md)'s garbling bound uses this claim's result, so the dependence runs the other way and [CLAIM-087](CLAIM-087.md) now rests on this claim. `rests_on: CLAIM-081` is now [CLAIM-270](CLAIM-270.md) (Active, demonstrated): "A state can become more conventional, and easier to read, while carrying less information about its origin", the point this claim uses.

## Note of 2026-10-28: split under ADR-061

The support verdict in this claim sat in "What it does not say": "the line
uses that standard for its formal ground, and a receiver's standard for
its thesis and its tests." It is now ARG-tmpa4q9l, from CLAIM-050 to
CLAIM-115, Proposed, since CLAIM-199's reconciliation narrows the
inference without defeating it. The title is unchanged: Blackwell's
theorem and the shape of CLAIM-050's defeat condition are about the
subject matter. This claim undercuts the argument, and its objection to
CLAIM-050 stays for the defeat-condition point.
