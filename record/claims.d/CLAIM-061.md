---
number: 61
status: Active
formerly:
- CLAIM-tmphg89g
title: 'Renderings that keep the proposition can perform a different communicative act, so preserving the proposition is not sufficient for preserving the communicative event'
version: 2
history:
- version: 2
  date: '2026-10-28'
  note: >-
    Narrowed and promoted at the status review of 2026-10-28 (ADR-057,
    ADR-059). Version 1's title read 'Renderings that share a loose situation model can differ in footing and illocutionary force, so preserving the proposition is neither necessary nor sufficient for preserving the communicative event'. The necessity half moves
    to CLAIM-486, Proposed, conceding CLAIM-053 and CLAIM-229.
    Footing leaves the title, conceding CLAIM-227: the record has no
    validated measure of it. THEORY-162 moves from grounds to
    corroborated_by (ADR-058). The defeated_if is restated for the
    sufficiency half.
role: thesis
warrant: interpretive
defeated_if: >-
  Human judgements of the act performed track propositional sameness:
  renderings judged to keep the proposition are reliably judged to keep
  the act, including in documented cases such as CASE-056's literal kiss
  where it is read as amorous.
tags:
- philosophy-of-language
- linguistics
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- CASE-027
- CASE-018
- LIT-785
- LIT-780
- CASE-056
corroborated_by:
- THEORY-162
supersedes:
- CLAIM-006
uses:
- TERM-030
summary: >-
  Manuscript §1, and the Abstract's "retain its topic while reversing
  the speaker's stance, and ... change almost every word while
  preserving the interpersonal relation". The descendant of the owner's
  frame thesis ([CLAIM-006](CLAIM-006.md)) without its ranking; the central thesis
  ([CLAIM-115](CLAIM-115.md)) rests on it.
complements:
- CLAIM-064
- CLAIM-091
- CLAIM-054
- CLAIM-084
- CLAIM-486
illustrated_by:
- CASE-012
- CASE-027
supports:
- CLAIM-115
- CLAIM-129
- CLAIM-151
- CLAIM-220
objected_by:
- CLAIM-053
- CLAIM-227
- CLAIM-229
---
<!-- inactive-ok-file: LIT-766 — Unavailable; Hofstadter, unread here, named as the reading the necessity candidate waits on -->

<!-- ref::uses-file: TERM-030 — footing and the speaker's position are components of TERM-030's configuration c = (u, s, a, k, n, g, h), which is where the delivery frame's who-to-whom-from-what-position went; until 2026-10-27 it used TERM-035, now Superseded -->
<!-- inactive-ok-file: THEORY-162 CLAIM-486 — Proposed; the reading that corroborates this claim, and the necessity half split from it, cited as open -->
<!-- inactive-ok-file: CLAIM-006 TERM-035 — Superseded; replaced, and cited as the history this entry answers or replaces -->
<!-- inactive-ok-file: CLAIM-115 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: LIT-780 LIT-785 — Unavailable; the work is unread here, cited as what the exchange or manuscript cites and not leaned on -->

# CLAIM-061: Renderings that keep the proposition can perform a different communicative act, so preserving the proposition is not sufficient for preserving the communicative event

## The claim

Manuscript §1: "The three utterances share a loose situation model while
differing in footing and illocutionary force. Preserving the proposition is
therefore neither necessary nor sufficient for preserving the communicative
event."

It was first stated at A12, as an asymmetry: "the propositional content can
remain largely unchanged while the speaker's apparent relationship to that
content changes completely. Conversely, you can alter many of the propositions
while preserving the speaker's attitude, social position, and communicative
intention—and the result may feel more faithful." Sufficiency fails in
[CASE-027](../cases.d/CASE-027.md); necessity fails in [CASE-018](../cases.d/CASE-018.md), read in reverse.

A14 added why force alone will not do: "in strict Austinian terminology,
*illocutionary force* may not capture every difference ... affectionate teasing
versus contemptuous judgment" can both be assertions, so footing and stance are
needed too.

## What it does not say

Not that the proposition is irrelevant, nor that the frame is *the* main
variable ([CLAIM-006](CLAIM-006.md)). Austin ([LIT-785](../literature.d/LIT-785.md)) and Goffman ([LIT-780](../literature.d/LIT-780.md)) are cited for it and
unread here.

## Support from dynamic semantics

The "not sufficient" half now has formal support ([THEORY-162](../theory.d/THEORY-162.md)):

- **Krifka** ([LIT-835](../literature.d/LIT-835.md)) gives one proposition with two different updates,
  declaration and assertion.
- **Heim** ([LIT-838](../literature.d/LIT-838.md)) gives truth-conditionally equivalent sentences that
  differ in what a following pronoun can pick up.
- **Veltman** ([LIT-818](../literature.d/LIT-818.md)) treats "might" as a test with no propositional
  content.

None of the three addresses footing.

## Note of 2026-10-10: the replies

Two corrections from the audit ([CLAIM-229](CLAIM-229.md)). [CASE-018](../cases.d/CASE-018.md) is a case of the
same proposition with a different act, which refutes sufficiency; "necessity
fails in [CASE-018](../cases.d/CASE-018.md), read in reverse" is mistaken, since reading it in reverse
keeps the words. The necessity half has A12's sentence and one documented
candidate, [CASE-031](../cases.d/CASE-031.md), pending a reading of [LIT-766](../literature.d/LIT-766.md). The fictional cases in
`grounds` are existence proofs for the sufficiency half, which is modal;
they do not bear on how common the dissociation is, which [CLAIM-115](CLAIM-115.md)'s
comparative test needs. The text above is unchanged.

## Note of 2026-10-27: stated in the live term

The status review of this date ([ADR-057](../decisions.d/ADR-057.md)) found this claim using [TERM-035](../terms.d/TERM-035.md),
which is Superseded. It now uses [TERM-030](../terms.d/TERM-030.md): footing and the speaker's position are components of [TERM-030](../terms.d/TERM-030.md)'s configuration c = (u, s, a, k, n, g, h), which is where the delivery frame's who-to-whom-from-what-position went. The claim's status is not
changed by this.

## Note of 2026-10-28: narrowed to sufficiency, and promoted

The status review of this date narrowed this claim and promoted it
([ADR-057](../decisions.d/ADR-057.md)). Its three objections are granted claims, and under [ADR-059](../decisions.d/ADR-059.md) a
conceded objection is recorded by revising its target, which version 1
had not done: the note of 2026-10-10 left the text unchanged.

- **[CLAIM-229](CLAIM-229.md)'s correction is made.** [CASE-018](../cases.d/CASE-018.md) is the same proposition
  with a different act, so it bears on sufficiency only. "Necessity fails
  in [CASE-018](../cases.d/CASE-018.md), read in reverse", above, is the version 1 text it corrects.
- **The necessity half moves** to [CLAIM-486](CLAIM-486.md), Proposed. The manuscript
  does not argue it ([CLAIM-053](CLAIM-053.md)), and its one documented case, [CASE-056](../cases.d/CASE-056.md),
  meets the defender's reply only partly: the coarser "greet one another
  warmly" survives.
- **Footing leaves the title** ([CLAIM-227](CLAIM-227.md)): the record has no validated
  measure of footing, and the analyst's own labels changed between
  passes. The title says "a different communicative act", which A14's
  point about force not capturing teasing against contempt still serves.

What remains is modal and has a documented case. [CASE-056](../cases.d/CASE-056.md) records the
UBS handbooks: where kissing is "exclusively an expression of amorous or
erotic interest", a literal rendering keeps the proposition and changes
the act. [CASE-027](../cases.d/CASE-027.md) and [CASE-018](../cases.d/CASE-018.md) are existence proofs beside it. Krifka's
declaration and assertion, one proposition with two updates ([THEORY-162](../theory.d/THEORY-162.md)),
corroborate it, but [THEORY-162](../theory.d/THEORY-162.md) is not a claim about translation, so it is
corroboration, not a ground.
