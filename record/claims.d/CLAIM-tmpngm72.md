---
status: Proposed
title: 'Stored information, belief, correct output, knowledge and understanding come apart in a learning system: there are coherent systems with information stored and not believed, a correct output neither believed nor reliable, reliable correct output without knowledge, a true and reliably sourced belief without knowledge, knowledge not accessible under the default query, knowledge without understanding, understanding without reliably correct output, and knowledge in a composite that neither part has'
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
- CASE-tmpk3qls
- CASE-tmpd1jgy
- CASE-tmpr1f20
- CASE-tmpcz1jq
- CASE-tmpp2okq
- CASE-tmpkttf2
- CASE-tmp55ptq
- CASE-tmppqt0f
summary: >-
  The verdict of the case set LEAD-001 asks for, as a separation table.
  Each case is fictional or a construction, so the claim is an existence
  claim shown by construction: each separation is coherent, not common.
  The criteria are QUESTION-493's candidate answers (A73's truth,
  counterfactual reliability over a declared family and grounding) and
  TERM-079's probes for belief. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-079 — Proposed; cited as the criterion applied, not relied on -->
<!-- inactive-ok-file: CASE-tmpk3qls CASE-tmpd1jgy CASE-tmpr1f20 CASE-tmpcz1jq CASE-tmpp2okq CASE-tmpkttf2 CASE-tmp55ptq CASE-tmppqt0f CASE-tmphawe9 CLAIM-tmpf4pun CLAIM-tmpadjsm CLAIM-tmp5qk10 CLAIM-tmpeonjp — Proposed; filed by the lead run of 2026-11-23 -->

# CLAIM-tmpngm72: Stored information, belief, correct output, knowledge and understanding come apart in a learning system: there are coherent systems with information stored and not believed, a correct output neither believed nor reliable, reliable correct output without knowledge, a true and reliably sourced belief without knowledge, knowledge not accessible under the default query, knowledge without understanding, understanding without reliably correct output, and knowledge in a composite that neither part has

## The claim

Eight separations, each exhibited by a case:

| case | stored | believed | correct output | knows | understands |
|---|---|---|---|---|---|
| CASE-tmpk3qls, probe reads P, model uses Q | yes (P) | no (Q) | no | no | — |
| CASE-tmpd1jgy, right once in 200 samples | — | no | once, not reliable | no | — |
| CASE-tmpr1f20, watermark classifier | yes (cue) | the cue | reliable on the family | no | — |
| CASE-tmpcz1jq, reappointed executive | yes | yes, true | reliable from its source | no | — |
| CASE-tmpp2okq, fact under one cue | yes | under the cue | not under the default | under the cue | — |
| CASE-tmpkttf2, table T | yes | degenerate | on the table | the values | no |
| CASE-tmp55ptq, noisy rule R′ | yes | yes | not on large inputs | not large values | yes |
| CASE-tmppqt0f, generator and verifier | — | — | composite reliable | composite only | — |

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
is the subject of two alternative claims, CLAIM-tmpeonjp (the assistant's
lean) and CLAIM-tmp5qk10.

## What it does not say

- Not that the criteria are right. The claim takes QUESTION-493's
  candidate as given and shows what it separates; a different account of
  knowledge could merge rows.
- Not the ninth case. CASE-tmphawe9, a frozen exact rule, would add
  "understanding without learnability" on one reading of understanding
  (CLAIM-tmpf4pun) and "knowledge without understanding" on the other
  (CLAIM-tmpadjsm). It is left out of the table because the readings
  disagree on it; the eight rows hold on both.
- Not that knowledge needs belief. The generator-verifier row is left
  blank for belief: the composite uses the checked answer as its answer
  and draws no further inferences, so TERM-079's probes have nothing to
  test.
