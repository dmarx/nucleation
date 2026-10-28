---
number: 106
status: Active
formerly:
- CLAIM-tmpumy4f
title: 'Pragmatic fidelity is a graded, potentially asymmetric property of transport, not an equivalence relation; equivalence is its zero-distortion limit'
version: 2
history:
- version: 2
  date: '2026-10-28'
  note: >-
    Promoted at the status review of 2026-10-28 (ADR-057). Its grounds
    and the terms it uses are Active, and nothing in the record meets
    its defeated_if. Its one objection, CLAIM-218, says the record's
    measure D_Q is symmetric, not that this claim is false; the claim
    now says it does not hold that D_Q realizes it.
role: thesis
warrant: interpretive
defeated_if: >-
  Judgements of translation fidelity behave as an equivalence: symmetric
  between source and target and transitive along chains, so that a
  graded directed measure adds nothing.
tags:
- philosophy-of-language
- mathematics
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- CASE-015
objects_to:
- CLAIM-067
supersedes:
- CLAIM-067
uses:
- TERM-015
- TERM-008
summary: >-
  The owner's objection at U20, accepted in full by A50 ("an important
  correction") and made the thesis of outline v4. The manuscript §12:
  "stochastic transport generalizes exact equivalence to graded
  fidelity."
supports:
- CLAIM-056
- CLAIM-101
- CLAIM-128
- CLAIM-244
- CLAIM-246
objected_by:
- CLAIM-218
complements:
- CLAIM-210
- CLAIM-242
- CLAIM-259
---
<!-- inactive-ok-file: CLAIM-259 — Proposed; the directed repair of the measure, cited as open -->
<!-- ref::uses-file: TERM-015 — stated in "fidelity, as graded, directed transport distortion"; the body names the term only inside quotations of its source, which are not altered (ADR-038) -->
<!-- inactive-ok-file: CLAIM-056 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-106: Pragmatic fidelity is a graded, potentially asymmetric property of transport, not an equivalence relation; equivalence is its zero-distortion limit

## The claim

U20: "I think presenting this as an equivalence might be too constraining. I
agree that there should be some transport map that at least gets to within some
eps, but that's just a similarity constraint, not an equivalence. This is why
the game 'telephone' works." A50: "I think this is an important correction."
A52's thesis: "**Pragmatic fidelity is therefore a graded, potentially
asymmetric property of transport, rather than fundamentally an equivalence
relation.**"

Two consequences A50 drew: "There is no requirement that the transport be
invertible or symmetric", and "similarity is not transitive" ([CLAIM-056](CLAIM-056.md)).
Manuscript §6: the transport ([TERM-008](../terms.d/TERM-008.md)<!-- ref::uses: TERM-008 -->) "is intentionally directed: compression and
interpretation need not be invertible"; §12: "stochastic transport generalizes
exact equivalence to graded fidelity".

## What it does not say

That equivalence is useless: "We can still recover equivalence as a special
case—for example, zero distortion under a suitably separating observation
family." Nor which distortion measure to use ([QUESTION-017](../questions.d/QUESTION-017.md)). Nor that A86's D_Q realizes it:
D_Q is symmetric ([CLAIM-218](CLAIM-218.md)), and a directed term is proposed in [CLAIM-259](CLAIM-259.md).

## Note of 2026-10-28: promoted

The status review of this date promoted this claim ([ADR-057](../decisions.d/ADR-057.md)). [CASE-015](../cases.d/CASE-015.md)
and the terms it uses are Active, and no judgement data in the record
show fidelity verdicts behaving as an equivalence. [CLAIM-218](CLAIM-218.md), its one
objection, is aimed at the measure: "It does not say CLAIM-106 is false."
That is conceded above, in what the claim does not say. The directed
repair, [CLAIM-259](CLAIM-259.md), stays Proposed.
