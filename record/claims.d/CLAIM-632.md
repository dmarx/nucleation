---
number: 632
status: Proposed
formerly:
- CLAIM-tmpupm3q
title: 'Records kept of each capacity a response needs bound a reserve''s readiness for a contingency between the sum of their probabilities less one less their number and the weakest of them, and identify it only when the capacities'' dependence is known, so for any verdict that rises with readiness they can refute a required readiness when the weakest capacity falls below it and certify it only when the capacities'' shortfalls together stay within its margin, leaving the band between to joint evidence such as a deadline-bound exercise; where capacities only decay between record and need, a refutation outlasts the record and a certification does not'
version: 3
history:
- version: 1
  date: '2026-11-08'
  note: >-
    Filed at the decision that a SYNTHESIS is an account (ADR-084),
    as its demonstration: SYNTHESIS-009, version 1, was a derived
    result, one claim, and returns to CLAIM under a code of its own.
    Title, body, defeater, role, warrant, lines and bears_on are the
    synthesis's; its premises are `rests_on`; its standing, Proposed, is
    kept.
- version: 2
  date: '2026-11-11'
  note: >-
    The summary's "with CLAIM-600 one of the readiness line's first two
    syntheses" is corrected, from the defects listed in the curation
    entry of 2026-11-10: both were filed as syntheses at the review of
    2026-11-07 and returned to CLAIM on 2026-11-08 (ADR-084), and the
    summary now says so. No other change.
- version: 3
  date: '2026-11-11'
  note: >-
    Answers QUESTION-395, in place of bearing on it, at the owner's
    delegated ruling of 2026-11-11: its body says "They answer the
    half of QUESTION-395 that asks which observations 'identify'
    readiness and which 'only bound' it", and `bears_on` excludes a
    part a claim settles exactly; `answers` is for an answer, held
    or offered (ADR-060). The claim is Proposed, so QUESTION-395
    stays Open and is not split under ADR-049 until an answer is
    Active. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: marginal probabilities for which the
  probability that every capacity holds lies outside
  [max(0, ΣPᵢ − (n − 1)), min Pᵢ], or a value inside that interval that no
  joint distribution attains; or a verdict rising with readiness that
  records certify or refute against these bounds wrongly. Or a premise it
  needs failing: success not a conjunction of the capacities (substitutes,
  which CLAIM-587 excludes); records that do not estimate each capacity's
  probability under the imposed contingency; or capacities that improve
  between record and need without practice, against CLAIM-558. Also
  defeated as a claim of its own if it only restates CLAIM-587's
  conjunction and CASE-210's list of records, adding no criterion for
  which records identify readiness and which bound it.
tags:
- operations-research
- probabilistic-modeling
- causality
date: '2026-11-08'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-587
- CLAIM-558
uses:
- TERM-115
answers:
- QUESTION-395
summary: >-
  [QUESTION-395](../questions.d/QUESTION-395.md) asks which observations tell a warranted reserve of
  specialized capability from wasteful redundancy, and which of them
  identify readiness ([TERM-115](../terms.d/TERM-115.md)) and which only bound it. [CLAIM-587](CLAIM-587.md) makes a
  response the conjunction of complementary capacities. So records kept
  per capacity (rosters, training assessments, equipment availability,
  turnout times) fix only the marginals, which bound readiness by the
  Fréchet inequalities and do not identify it. A record can refute a
  required readiness through the weakest capacity, and can certify it only
  when the shortfalls sum within the margin; between those, only joint
  evidence decides. With [CLAIM-558](CLAIM-558.md)'s decay, a certification expires with
  the record's age and a refutation does not. The inference leans mainly on
  [CLAIM-587](CLAIM-587.md); its integrating work is joining it with [TERM-115](../terms.d/TERM-115.md), [CASE-210](../cases.d/CASE-210.md)'s
  list of evidence and [CLAIM-558](CLAIM-558.md) to answer the question's "identify or
  bound" half. Filed at the synthesis review of 2026-11-07 as a
  synthesis, SYNTHESIS-009, one of the readiness line's first two with
  what is now [CLAIM-600](CLAIM-600.md); both returned to CLAIM on 2026-11-08 (ADR-084).
  The integration's wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-210 CLAIM-584 TERM-107 — Proposed; components cited with their standing -->
<!-- inactive-ok-file: ARG-053 — Rejected; the inference from use counts this replaces -->
<!-- inactive-ok-file: ADR-075 ADR-078 — Proposed; the audit and the review that filed this entry -->

# CLAIM-632: Records kept of each capacity a response needs bound a reserve's readiness for a contingency between the sum of their probabilities less one less their number and the weakest of them, and identify it only when the capacities' dependence is known, so for any verdict that rises with readiness they can refute a required readiness when the weakest capacity falls below it and certify it only when the capacities' shortfalls together stay within its margin, leaving the band between to joint evidence such as a deadline-bound exercise; where capacities only decay between record and need, a refutation outlasts the record and a certification does not

*Returned to CLAIM from [SYNTHESIS-009](../syntheses.d/SYNTHESIS-009.md) on 2026-11-08 ([ADR-084](../decisions.d/ADR-084.md)). The notes below that speak of a synthesis are the synthesis's own.*

*Filed at the synthesis review of 2026-11-07 ([ADR-078](../decisions.d/ADR-078.md)) as an opportunity: [QUESTION-395](../questions.d/QUESTION-395.md) had several in-force answers and no entry saying which records identify readiness and which bound it.*

## The integration

- **[CLAIM-587](CLAIM-587.md)** (A's, Active, demonstrated) is a premise. A response
  succeeds exactly when every one of n complementary capacities holds, and
  readiness is R = Pr(all hold), a product of conditionals and "not in
  general of four unconditional ones". "Where one can stand in for
  another, success is not a pure conjunction", and that case is excluded
  here.
- **[TERM-115](../terms.d/TERM-115.md)** (A's, Active) defines readiness under an imposed
  contingency: "It is defined under intervention, so a record of what was
  done does not measure it."
- **[CASE-210](../cases.d/CASE-210.md)** (A's, Proposed) names the evidence short of intervention:
  "Inventories, training records and drills would." This synthesis says
  what such records can and cannot show. For presence against absence (a
  capacity with probability zero) they settle it; for the level of
  readiness they bound it.
- **[CLAIM-558](CLAIM-558.md)** (the filer's, Active, interpretive) is the premise of the
  expiry clause: "If operation calls on a capability less often than its
  decay allows, operation cannot be what keeps it." Its extension to
  organizations is interpretive, so the clause is conditional on decay.
- **[CLAIM-561](CLAIM-561.md)** and **[CLAIM-520](CLAIM-520.md)** (Active) show that a reserve's value is
  conditional on objectives and uncertainty, and that use or cancellation
  counts alone cannot identify waste. A verdict that rises with R, such as
  an expected-loss gain or a reliability floor R ≥ r*, is the kind this
  synthesis decides. **[CLAIM-569](CLAIM-569.md)** (Active) adds the construction cost a
  waste verdict must not overlook.
- **[CLAIM-414](CLAIM-414.md)** (Active) holds that intervention is not the only way to
  tell systems apart: "Nor is intervention the only way to tell the
  systems apart". Records are such a way, within the bounds below.
- **[ARG-053](../arguments.d/ARG-053.md)** (Rejected) and **[CLAIM-584](CLAIM-584.md)** (Proposed, disclaimed) are the
  inference from use counts that this replaces with a criterion.
  **[TERM-107](../terms.d/TERM-107.md)** (Proposed) is the slack the cost side would draw on.

## Admission

Admitted under [ADR-075](../decisions.d/ADR-075.md)'s derived route. Let Pᵢ be the probability, under
the contingency, that capacity i holds.

1. **The bounds.** By Boole's inequality, Pr(some capacity fails) ≤
   Σ(1 − Pᵢ), so R ≥ max(0, ΣPᵢ − (n − 1)) =: L. And R ≤ Pᵢ for every i,
   so R ≤ min Pᵢ =: U.
2. **They are attained, and so is everything between.** On a unit
   interval, nesting the success sets gives U, laying the failure sets end
   to end gives L, and mixing the two gives every value between. The
   reader's linear program over all joint distributions on {0,1}⁴ agreed
   with L and U on 2,000 random marginal vectors. So the marginals identify
   R only when the dependence is known, or when L = U (some Pᵢ = 0, or all
   but one equal to 1). Four capacities at 0.9 leave R anywhere in
   [0.6, 0.9].
3. **The verdict.** For a verdict that rises with R, records certify it
   when it holds at L, refute it when it fails at U, and are silent
   otherwise. For a floor r*, they refute exactly when min Pᵢ < r*, and
   certify exactly when Σ(1 − Pᵢ) ≤ 1 − r*. A stipulated illustration,
   with value 3R − 2:

   | marginals | bounds on R | verdict |
   |---|---|---|
   | (0.9, 0.9, 0.9, 0.9) | [0.6, 0.9] | undecided: value between −0.2 and 0.7 |
   | (0.97, 0.97, 0.97, 0.95) | at least 0.86 | warranted: value at least 0.58 |
   | (0.6, 0.95, 0.95, 0.95) | at most 0.6 | waste as maintained: value at most −0.2 |

4. **Expiry.** If each Pᵢ only falls between the record and the need
   ([CLAIM-558](CLAIM-558.md)), the true U is at most the recorded one, so a refutation
   from records stays valid as the record ages. The recorded L overstates
   the true L, so a certification does not. The same holds for an estimate
   of R from a joint exercise.

The bounds themselves are textbook. What no entry held, and what makes the
inference nontrivial here, is items 3 and 4: the criterion for which
records settle a verdict and which do not, and the asymmetry in how they
age. They answer the half of [QUESTION-395](../questions.d/QUESTION-395.md) that asks which observations
"identify" readiness and which "only bound" it.

## What it does not say

- **What a reserve is worth.** The value model is a declared input. [CASE-210](../cases.d/CASE-210.md):
  warrant "needs an objective, a distribution of incidents or a robust
  reliability requirement".
- **That a waste verdict calls for abolition.** It is a verdict on the
  reserve as maintained. Practice outside operation ([CLAIM-558](CLAIM-558.md)) may reverse
  it, and rebuilding costs construction ([CLAIM-569](CLAIM-569.md)) or may be impossible
  below a threshold ([CLAIM-605](CLAIM-605.md)).
- **That an exercise measures R under the policy actually followed**
  ([TERM-115](../terms.d/TERM-115.md)'s policy). That holds only if the exercise recognizes and
  mobilizes as the policy would.
- **Anything about readiness in [CLAIM-572](CLAIM-572.md)'s sense**, the observing and
  response budget, which is a different notion.

## Note of 2026-11-12: a sprinkler response as a conjunction of capacities

<!-- inactive-ok-block: CASE-tmpl4kyp CASE-tmpaky45 — filed from the exchange "Meaning Transmission Explained", Proposed -->
The fire-alarm chain filed from the exchange "Meaning Transmission Explained" ([CASE-tmpl4kyp](../cases.d/CASE-tmpl4kyp.md)) is
this claim's setting in miniature. A sprinkler response to a fire needs
the sensor, the relay and the actuator to hold together, a pure
conjunction in [CLAIM-587](CLAIM-587.md)'s sense. Records of each component bound the
response's readiness as this claim says. For illustration, with
per-component probabilities 0.98, 0.99 and 0.95, the bounds are
0.98 + 0.99 + 0.95 − 2 = 0.92 and min = 0.95. The product under
independence is 0.92169, inside them (computed). The test injector in
that chain is not a capacity of the response but of the test, so its
failure lowers the evidence about readiness, not readiness itself. That
is the owner's debugging case ([CASE-tmpaky45](../cases.d/CASE-tmpaky45.md)), where a silent test does
not say whether the response or the test failed. A deadline-bound
exercise, this claim's joint evidence, is in that chain the
independent-smoke probe, which exercises every capacity of the response
at once and nothing else. [CASE-210](../cases.d/CASE-210.md) has the same structure with rescue
squads. Nothing changes. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
