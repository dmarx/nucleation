---
number: 1064
status: Active
formerly:
- CLAIM-tmpbbfcj
title: 'Penalized discovery makes inquiry never pay'
statement: >-
  In an institution each of whose recognized violations is penalized, newly
  recognized ones included, whose discovery of requirements earns nothing,
  and whose remediation lags recognition, inquiry that only reveals
  requirements never raises its score when the hidden requirements do not
  otherwise come to light: on every path it adds only penalized violations
  and spent budget, so an institution acting on that score makes no inquiry
version: 5
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-181, from the
    model and runs of CASE-396.
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): its ground CASE-396 went Active on a
    reproduced rerun; the coupling argument was rechecked and the path-by-
    path test passes.
- version: 3
  date: '2026-11-24'
  note: >-
    Joins the work governance-of-becoming under ADR-104's rule, as
    stated or used in A49 Article 11 abstract, §7 (ADR-147). No
    change of title or status.
- version: 4
  date: '2026-11-26'
  note: >-
    Dated note of 2026-11-26 from the exchange "Alignment
    consequences brainstorm" (ChatGPT, 2026-11-26), U6–A11, U7–A13
    and U8–A15: A11 §8 applies the claim to AI laboratories, citing
    CLAIM-662; A13 §4 offers Luria's acknowledgements as a partial
    answer, which the assistant checks against the claim's
    conditions; A15's R6 states its outcome ladder. The claim is
    unchanged.
- version: 5
  date: '2026-11-26'
  note: >-
    Joins the work organizational-origins-of-misalignment (ADR-152) at
    its filing, under ADR-104's rule: the outline A11 §IX of the exchange
    "Alignment consequences brainstorm" uses its proposition as a step.
    No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the coupling argument below, for instance a path on which
  inquiry lowers the penalized count or frees budget; or an error in
  scratch/studies/lead-181/model.py whose correction makes the
  path-by-path test in test_model.py fail. Not defeated by a setting in
  which hidden requirements surface from outside at an extra cost, which
  the claim excludes and CASE-396 treats; by a remediation rule that
  serves newly found violations before older ones, which the claim does
  not cover; or by institutions that behave otherwise, about which it
  says nothing.
tags:
- society-and-governance
- mathematics
- operations-research
date: '2026-11-23'
line:
- organizational-normativity
- distributed-agency
works:
- governance-of-becoming
- organizational-origins-of-misalignment
grounds:
- CASE-396
corroborates:
- CLAIM-662
bears_on:
- QUESTION-456
summary: >-
  The dynamic form, for [CASE-396](../cases.d/CASE-396.md)'s institution, of [CLAIM-662](CLAIM-662.md)'s
  step 4. Each period the institution splits a budget among inquiry,
  remediation of recognized violations (oldest first, at least one period
  after recognition) and output; it is charged for every recognized
  violation and earns nothing for finding one. Coupling the paths of a
  policy that inquires with the same policy without inquiry, the
  violations recognized and unmet under the first are those of the second
  plus the violations found and not yet remedied, and its output is
  lower by the inquiry and by any remediation of found violations. So on
  every path its score per period is no higher, and lower whenever it
  pays for inquiry or finds a violation. Checked path by path in
  test_model.py; in the runs the optimum makes no inquiry in all four
  settings, including two in which requirements also surface from
  outside. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

# CLAIM-1064: Penalized discovery makes inquiry never pay

## The claim

[CLAIM-662](CLAIM-662.md)'s step 4 holds that, under governance that "penalizes newly
recognized violations without rewarding their discovery", an audit
improvement that adds a failed demand raises the penalty while the
arrangement is unchanged. This is the same for an institution that
decides each period how much to inquire, in [CASE-396](../cases.d/CASE-396.md)'s model.

## The argument

Fix the draws: which requirements are violated at the start, and the
uniform draws that decide each period which unrecognized requirements an
inquiry of a units finds. Compare a policy (a, b), a > 0, with (0, b):
the same remediation capacity b, no inquiry. No requirement surfaces from
outside.

1. Under (0, b) the recognized set stays the visible set V. Under (a, b)
   it is V together with F_t, the hidden requirements found by period t.
2. Remediation serves eligible violations oldest first, and the visible
   ones are oldest, so both policies remedy the same visible violations in
   the same periods. Capacity left over goes, under (a, b), to found
   violations at least one period old; under (0, b), to output.
3. So in each period the recognized unmet violations under (a, b) are
   those under (0, b) plus the found violations not yet remedied, and its
   output is lower by a and by the remediation of found violations.
4. Each period's score, minus the penalty per recognized unmet violation
   plus output, is therefore no higher under (a, b) on any path. It is
   strictly lower in any period in which inquiry costs output, and in the
   period in which a violation is found, since remediation lags
   recognition by at least one period.

Hence the best policy has a = 0, whatever the penalty, the output value
and the remediation capacity, and an institution acting on its score has
no reason to inquire.

## What it rests on and what it does not say

The argument is the record's own and uses only the model's rules. Two of
them carry it: discovery earns nothing, and remediation lags recognition
(with no lag and free remediation, inquiry is neutral rather than
penalized). It does not cover surfacing from outside at a cost, under
which an institution can gain by finding a violation first; in
[CASE-396](../cases.d/CASE-396.md) the optimum still made no inquiry at a cost of 3 and did at
10. It says nothing of whether any institution is so scored.

## Note of 2026-11-24: the exchange 'Memes, Contracts, and Systemic Normativity', A44 §10

A44 §10 cites this claim, by the code it has on main, rightly, "under
specified assumptions", though its paraphrase drops the condition that the
hidden requirements do not otherwise come to light. It extends the pattern
to other accountability measures: rewarding an absence of complaints
invites making complaints hard to submit, rewarding resolved cases favours
the easiest, rewarding successful audits discourages discriminating ones.
And it qualifies the remedy: "rewarding discoveries can create incentives
to manufacture or exaggerate them." [CASE-396](../cases.d/CASE-396.md)'s reward-for-discovery
regime restores inquiry, but its institution cannot report a discovery it
did not make, so it does not test that qualification. Bearing: an extension
of the pattern, and a limit of the held study's design. The claim is
unchanged. The wording of this note is the assistant's (Claude, in this session), reporting A's (ChatGPT's) text; adopting what it reports is the owner's call.

## Note of 2026-11-25: the researcher's side of the same pattern

ChatGPT, at A21 of the exchange "Hyper article interpretation" (2026-11-22), writing on academic incentives: "Why investigate a possible weakness in your earlier work when doing so might reduce its apparent significance?", and "If corrections and maintenance are difficult to publish, researchers have less incentive to spend time correcting and maintaining existing work." This is the pattern this claim derives for an institution, seen from a researcher evaluated by publications: discovering a flaw in one's own result scores as a loss and earns nothing as discovery. A gives it no model, so the note records an instance of the pattern and does not extend the claim. It bears on [QUESTION-542](../questions.d/QUESTION-542.md). The note is the assistant's (Claude, in this session), reporting A's (ChatGPT's) text; adopting what it reports is the owner's call. The claim is unchanged.

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U6–A11, U7–A13, U8–A15)

<!-- inactive-ok-file: CLAIM-1453 CLAIM-1429 — new; the claims of 2026-11-26 the note names -->

Three bearings, and a qualification in the assistant's voice.

**An application (A11 §8).** A cites [CLAIM-662](CLAIM-662.md) for "Penalizing
discovery", correctly as far as [CLAIM-662](CLAIM-662.md) goes, and draws the conclusion
this claim states: "an AI laboratory scored on the number of safety
failures it discovers might inadvertently select against its own safety
research." This claim, not [CLAIM-662](CLAIM-662.md), is the one that says inquiry never
pays under those conditions; A did not cite it. "More generally, we should
distinguish a reduction in violations from a reduction in the capacity to
recognize violations."

**A requirement (A15, R6).** A's platform must not collapse "No failures
discovered", "Failures discovered", "Failures acknowledged", "Failures
corrected" and "Correction mechanisms maintained" into "a single compliance
indicator", reading the first as "Possibly no effective investigation".
That is this claim's consequence made a rule of reporting
([CLAIM-1453](CLAIM-1453.md)).

**A proposed answer (A13 §4), checked (the assistant).** A13 offers
Luria's acknowledgements as "a concrete partial response": a warning "can
be acknowledged without disappearing from the accounting", and Luria's
principle that "a suppression must not become a silence" is checked in its
documents ([CLAIM-1429](CLAIM-1429.md)). Against this claim's conditions: an
acknowledged finding does not fail the check, so in an institution scored
on pass or fail, recognizing a requirement no longer costs the score, and
the first condition, that each recognized violation is penalized, fails;
inquiry can then pay. But Luria counts acknowledgements in its report, so
an institution scored on that count is back under the condition, with the
count as its penalty. Acknowledgements answer the incentive only where the
count is read as evidence of looking, as A15's ladder reads it, and not as
a score to lower. The third condition, remediation lagging recognition, is
untouched by them. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
