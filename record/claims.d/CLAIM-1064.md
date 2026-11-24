---
number: 1064
status: Active
formerly:
- CLAIM-tmpbbfcj
title: 'In an institution each of whose recognized violations is penalized, newly recognized ones included, whose discovery of requirements earns nothing, and whose remediation lags recognition, inquiry that only reveals requirements never raises its score when the hidden requirements do not otherwise come to light: on every path it adds only penalized violations and spent budget, so an institution acting on that score makes no inquiry'
version: 3
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
    stated or used in A49 Article 11 abstract, §7 (ADR-tmpenzcn). No
    change of title or status.
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

# CLAIM-1064: In an institution each of whose recognized violations is penalized, newly recognized ones included, whose discovery of requirements earns nothing, and whose remediation lags recognition, inquiry that only reveals requirements never raises its score when the hidden requirements do not otherwise come to light: on every path it adds only penalized violations and spent budget, so an institution acting on that score makes no inquiry

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
