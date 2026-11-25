---
number: 1142
status: Proposed
formerly:
- CLAIM-tmpngm72
title: 'Stored, believed, known and understood come apart'
statement: >-
  Stored information, belief, correct output, knowledge and understanding
  come apart in a learning system: there are coherent systems with
  information stored and not believed, a correct output neither believed nor
  reliable, reliable correct output without knowledge, a true and reliably
  sourced belief without knowledge, knowledge not accessible under the
  default query, knowledge without understanding, understanding without
  reliably correct output, and knowledge in a composite that neither part
  has
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  One of the constructions shown incoherent, a system that cannot be
  built as described; or shown not to have the property the claim
  assigns it on the criteria the claim applies (TERM-079's probes for
  belief, QUESTION-493's candidate criteria for knowledge, and for
  understanding the criteria on which both alternative readings agree),
  for instance a probe-decodable fact that the system's own inference is
  shown to use. Not defeated by an argument that some other criterion of
  knowledge or understanding would give another verdict; that is a
  dispute about the criteria, which the claim states as its own.
tags:
- epistemology
- learning-theory
- cognition
date: '2026-11-23'
line:
- learned-structure
bears_on:
- QUESTION-493
grounds:
- CASE-408
- CASE-400
- CASE-416
- CASE-399
- CASE-413
- CASE-409
- CASE-394
- CASE-414
summary: >-
  The verdict of the case set [LEAD-001](../leads.d/LEAD-001.md) asks for, as a separation table.
  Each case is fictional or a construction, so the claim is an existence
  claim shown by construction: each separation is coherent, not common.
  The criteria are [QUESTION-493](../questions.d/QUESTION-493.md)'s candidate answers (A73's truth,
  counterfactual reliability over a declared family and grounding) and
  [TERM-079](../terms.d/TERM-079.md)'s probes for belief. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-079 — Proposed; cited as the criterion applied, not relied on -->
<!-- inactive-ok-file: CASE-408 CASE-400 CASE-416 CASE-399 CASE-413 CASE-409 CASE-394 CASE-414 CASE-403 CLAIM-1092 CLAIM-1059 CLAIM-1028 CLAIM-1086 — Proposed; filed by the lead run of 2026-11-23 -->

# CLAIM-1142: Stored, believed, known and understood come apart

## The claim

Eight separations, each exhibited by a case:

| case | stored | believed | correct output | knows | understands |
|---|---|---|---|---|---|
| [CASE-408](../cases.d/CASE-408.md), probe reads P, model uses Q | yes (P) | no (Q) | no | no | — |
| [CASE-400](../cases.d/CASE-400.md), right once in 200 samples | — | no | once, not reliable | no | — |
| [CASE-416](../cases.d/CASE-416.md), watermark classifier | yes (cue) | the cue | reliable on the family | no | — |
| [CASE-399](../cases.d/CASE-399.md), reappointed executive | yes | yes, true | reliable from its source | no | — |
| [CASE-413](../cases.d/CASE-413.md), fact under one cue | yes | under the cue | not under the default | under the cue | — |
| [CASE-409](../cases.d/CASE-409.md), table T | yes | degenerate | on the table | the values | no |
| [CASE-394](../cases.d/CASE-394.md), noisy rule R′ | yes | yes | not on large inputs | not large values | yes |
| [CASE-414](../cases.d/CASE-414.md), generator and verifier | — | — | composite reliable | composite only | — |

Read by row, they show that none of the five is sufficient for the next
one in the usual ladder (stored, believed, correct, known, understood),
and that the ladder is not a ladder: understanding can be present where
correct output and knowledge of particular values are not (R′), and
correct output can be reliable where belief is about something else (the
watermark). Each verdict is on the criteria named in the summary, and
each case holds fixed everything but the respect it varies, so the claim
is shown by construction; that is the warrant, and it says nothing about
how often real systems are in these states.

What separates reliable performance from non-accidental competence, the
lead's question, is in the middle rows. Reliability over a family as
declared is had by the watermark classifier and the stale-source model,
and both fail when the truthmaker is intervened on. What that failure is
is the subject of two alternative claims, [CLAIM-1086](CLAIM-1086.md) (the assistant's
lean) and [CLAIM-1028](CLAIM-1028.md).

## What it does not say

- Not that the criteria are right. The claim takes [QUESTION-493](../questions.d/QUESTION-493.md)'s
  candidate as given and shows what it separates; a different account of
  knowledge could merge rows.
- Not the ninth case. [CASE-403](../cases.d/CASE-403.md), a frozen exact rule, would add
  "understanding without learnability" on one reading of understanding
  ([CLAIM-1092](CLAIM-1092.md)) and "knowledge without understanding" on the other
  ([CLAIM-1059](CLAIM-1059.md)). It is left out of the table because the readings
  disagree on it; the eight rows hold on both.
- Not that knowledge needs belief. The generator-verifier row is left
  blank for belief: the composite uses the checked answer as its answer
  and draws no further inferences, so [TERM-079](../terms.d/TERM-079.md)'s probes have nothing to
  test.
