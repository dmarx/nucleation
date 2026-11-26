---
number: 1068
status: Proposed
formerly:
- CLAIM-tmpc5mmp
title: 'Codes did not bypass retrieval by content'
statement: >-
  In the record's exchanges a code did not bypass retrieval by content:
  content the record held under codes was re-derived without them in 20 of
  48 reconstructed exchanges, because the collaborator had to find the code
  by what the content said
version: 2
history:
- version: 2
  date: '2026-11-26'
  note: >-
    A dated note: the exchange 'Alignment consequences brainstorm' (ChatGPT,
    2026-11-26), A27 §§3 and 11 and A29 §6 (see the note). No other change.
role: counter
warrant: empirical
defeated_if: >-
  The exchanges whose reconstructions report held content re-derived
  without its code turn out to be ones where the collaborator did not have
  the record's codes to hand, so that no code was available to bypass
  anything. Or a transcript-level count shows that coded content recurring
  in exchanges is cited by its code far more often than it is re-derived.
tags:
- epistemology
- design-rationale
date: '2026-11-23'
line:
- nucleating-argument
objects_to:
- CLAIM-180
grounds:
- CASE-393
bears_on:
- QUESTION-038
summary: >-
  Filed from the run of [LEAD-107](../leads.d/LEAD-107.md) on 2026-11-23. It is one of two readings
  of the same counts; the other is [CLAIM-1023](CLAIM-1023.md), and the lead worker
  leans to that one. This reading takes the clause "a code bypasses
  retrieval by content altogether" in [CLAIM-180](CLAIM-180.md)'s title as a claim about
  the exchanges, and the counts of [CASE-393](../cases.d/CASE-393.md) as against it. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-180 — Proposed; the claim this objection targets, cited as under test -->
<!-- inactive-ok-file: CLAIM-1023 — new; filed by the lead run of 2026-11-23 -->

# CLAIM-1068: Codes did not bypass retrieval by content

## The claim

[CLAIM-180](CLAIM-180.md) says a restatement too far from its original is taken for new,
and that "a code bypasses retrieval by content altogether": "An addressed
item can be reached by its name from anywhere." In the record's exchanges
it was not.

[CASE-393](../cases.d/CASE-393.md) finds 159 (reconstruction, item) units in which content
held under a code before the exchange began was re-derived in it without
that code: "re-derived", "uncited", "announced as new", "already held".
They come from 20 of the 48 reconstructions. In some of those exchanges
the replies plainly read the record: one reconstruction counts 133 codes
cited (workbench 2026/10/22/103820). Even so, items the record held were
re-derived beside the codes that were cited.

Of 21 items re-derived before they had codes, four were re-derived again
after their codes existed. Those are [TERM-072](../terms.d/TERM-072.md), [CLAIM-414](CLAIM-414.md), [QUESTION-271](../questions.d/QUESTION-271.md) and
[CASE-156](../cases.d/CASE-156.md). None is reported cited.

A name reaches an item from anywhere only for a reader who already has
the name. A collaborator restating an idea does not start from the code.
It starts from the idea, and has to get from the idea to the code by
content. That step is retrieval by content, with the same limit [CLAIM-180](CLAIM-180.md)
describes. So a code moves the retrieval failure; it does not remove it.

## What it does not say

- It does not say codes do nothing. Nothing here measures how often a
  coded item was recognised, because the reconstructions do not report
  that ([CLAIM-1023](CLAIM-1023.md), [CLAIM-1056](CLAIM-1056.md)).
- It does not deny the critical-distance account of drift. It denies only
  the bypass clause, as a description of the exchanges.

## Note of 2026-11-23: what holds it back

[CASE-393](../cases.d/CASE-393.md) is now Active and reproduces; this is one of two readings of
its counts, with [CLAIM-1023](CLAIM-1023.md), and the choice between them is the owner's
under [ADR-127](../decisions.d/ADR-127.md). Its causal clause, that the collaborator had to find the code
by what the content said, is not measured by the study, which cannot see
what the collaborator had to hand.

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U15–A29), cooled entries are found by content
<!-- inactive-ok-file: TERM-tmp96b3g CLAIM-tmpdkwbk LIT-tmpua7jt — Proposed or Deferred; filed from the same exchange on 2026-11-26 -->

The availability tiers proposed in the exchange (TERM-tmp96b3g) leave a cold entry "Recoverable by identity", by its code, and take it out of default search. This claim is the reason that is not enough: in the record's exchanges content held under codes was re-derived without them in 20 of 48 reconstructed exchanges, "because the collaborator had to find the code by what the content said". A collaborator who does not know a cold entry's code meets it only through something that matches its content. A29 §6's ghost representation, after ARC's ghost lists (LIT-tmpua7jt), is the remedy that fits: a cooled entry keeps its keywords in a cheap second index that every search consults, so an inquiry that meets cooled material is told so. A27 §11's retrieval contract (default search excludes cold entries) would, without it, turn this claim's failure into policy. Cooling that keeps dependencies visible (CLAIM-tmpdkwbk) does not cover this case, which is about finding, not about review. A bearing on a design; no edge. The note is the assistant's (Claude, in this session). No status change.
