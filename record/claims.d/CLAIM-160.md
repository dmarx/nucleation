---
number: 160
status: Proposed
formerly:
- CLAIM-tmpdfqoo
title: 'Data written for a potential future receiver has its intended meaning fixed by the write: even if it is never read, what it was meant to say was settled when it was stored'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    CLAIM-255 leaves complements; it now rests on this claim (status
    review, ADR-057). The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A stored message whose intended meaning, by the line's own observables,
  turns out to depend on who eventually reads it, where no fact about
  the writer's projected receiver and context settles it. Alternatively,
  intended meanings that cannot be recovered even in principle from the
  write and its context of production, so that "fixed" does no work.
  Disagreement among readers does not count: it is a fact about
  recoverability, and CLAIM-115 already makes that receiver-relative.
tags:
- pragmatics
- philosophy-of-language
- information-theory
date: '2026-10-11'
line: pragmatic-transport
grounds:
- CASE-043
- CASE-048
complements:
- CLAIM-204
- CLAIM-151
uses:
- TERM-030
summary: >-
  The owner's claim of 2026-10-11, in their words: "data is written with
  a potential future receiver in mind. even if the data is never read,
  its intended meaning was fixed by the write." It separates when
  identity is fixed (at the write, relative to a projected receiver)
  from when fidelity is measured (at a read, relative to an actual one),
  which the line had left unsettled. It does not say what a text means
  to a given reader is fixed.
illustrated_by:
- CASE-048
objected_by:
- CLAIM-171
bears_on:
- QUESTION-029
---
<!-- inactive-ok-file: CLAIM-255 — Proposed; filed 2026-10-12 from the interlocutor's reading as advice, cited in a note as open -->
<!-- inactive-ok-file: CLAIM-074 CLAIM-115 CLAIM-151 — Proposed; the line's receiver-side claims this one is placed beside, open -->
<!-- inactive-ok-file: CLAIM-171 — Proposed; the open objection to this claim -->
<!-- inactive-ok-file: CLAIM-204 CLAIM-217 — Proposed; cited in a note of 2026-10-12 as open, for what each holds, not as settled -->

# CLAIM-160: Data written for a potential future receiver has its intended meaning fixed by the write: even if it is never read, what it was meant to say was settled when it was stored

## The claim

The owner put it as a variant of the tree falling in the woods
([CASE-049](../cases.d/CASE-049.md) → [CASE-043](../cases.d/CASE-043.md)): "information storage as a variant of
tree-in-woods case. data is written with a potential future receiver in
mind. even if the data is never read, its intended meaning was fixed by the
write".

The variant differs from the tree in exactly one respect. The tree's fall
has no receiver it was made for, so the question whether it "made a sound"
is about a physical event and a perceiver. A write is made for someone: a
reader the writer projects, with a common ground the writer assumes. In
[TERM-030](../terms.d/TERM-030.md)'s terms, the write fixes the frame as the writer configures it
(speaker, audience, common ground, norms, genre). What it was meant to say
is relative to that frame and is settled when the write is made. A later
read, or none, does not reach back and change it.

This places the line's two tests at two different times. [CLAIM-115](CLAIM-115.md) and
[CLAIM-074](CLAIM-074.md) make fidelity receiver-relative: what an actual reader can
reconstruct, at that reader's state of adaptation. [CLAIM-151](CLAIM-151.md) makes the act
partly constituted by expected uptake. This claim says the expectation is
the writer's, fixed at the write, and the reconstruction is the reader's,
measured at each read. An unread record has an intended meaning and no
fidelity to measure.

## The joke as a test

[CASE-048](../cases.d/CASE-048.md) is the hardest case the owner offered. A joke seen at eight
and again at thirty seems to change its meaning for the same person. On
this claim, what changed is what that reader can reconstruct ([CLAIM-074](CLAIM-074.md)'s
"states of adaptation of the same interpreter"). The joke's intended
meaning did not change. It was written for two audiences at once. The
child's reading is the layer addressed to the child, not a failed reading
of the adult one. The objection [CLAIM-171](CLAIM-171.md) reads the same case the other
way.

## What it does not say

- **That what a text means to a reader is fixed.** That is the reader's
  reconstruction and changes with them.
- **That the writer's intention is always recoverable.** It is fixed, not
  thereby accessible. The line's probe questions ([QUESTION-031](../questions.d/QUESTION-031.md)) are about
  access.
- **That every inscription has a projected receiver.** A trace no one
  wrote for anyone, such as tree rings or a sensor's raw log, is closer to
  the tree than to the variant.

## Note of 2026-10-12: whose uptake fixes the act, left to the owner

[CLAIM-151](CLAIM-151.md) version 2, restated in PR [#121](https://github.com/dmarx/nucleation/issues/121), is built to defeat accounts that
fix the act by the utterance and the speaker's internal states alone, on
cases in which the speaker's intention is held fixed and the audience's
role changes. [CLAIM-217](CLAIM-217.md) makes competent participants' uptake "part of
what makes the fact", and [CLAIM-204](CLAIM-204.md) rests on it. This claim reads
[CLAIM-151](CLAIM-151.md)'s expected uptake as the writer's, fixed at the write. This
claim and [CLAIM-204](CLAIM-204.md) are both filed as answers to [QUESTION-029](../questions.d/QUESTION-029.md), and no
relation joins them. If "identity" here means intended meaning only, the
two need not conflict; if it means the act, they do. Which reading holds,
and what follows for this claim's `answers` edge, is left to the owner.

## Note of 2026-10-12: the interlocutor's reading, as advice

The interlocutor's reading of 2026-10-12 recommends to "Retain CLAIM-160 for intended meaning, retain [CLAIM-151](CLAIM-151.md) for socially constituted act identity", on its distinction between "intending to perform an act, performing that act, and being recognized as having performed it" ([CLAIM-255](CLAIM-255.md)). Recorded as advice. Whether this claim narrows to intended meaning, and what follows for its answer to [QUESTION-029](../questions.d/QUESTION-029.md), is still the owner's.

## Note of 2026-10-28: intended meaning, beside the act

The owner's ruling on the fourth status review settles the note of
2026-10-12. This claim is about intended meaning, fixed when it is written.
[QUESTION-029](../questions.d/QUESTION-029.md) asks about the identity of the communicative act, which is
[CLAIM-151](CLAIM-151.md)'s and [CLAIM-204](CLAIM-204.md)'s ground, so this claim bears on that question
and does not answer it. Read that way, it does not conflict with [CLAIM-204](CLAIM-204.md),
and the two complement each other: intending to perform an act against the
act performed and taken up, the interlocutor's distinction of 2026-10-12.
