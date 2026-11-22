---
number: 901
status: Proposed
formerly:
- CLAIM-tmpqaqtx
title: 'In a simulation of an organization that corrects once and is then damaged, the second correction after an undisclosed lesion of evidence generation, admission or scoring is decided by whether the apparatus can find its own damage and has a producer to rebuild it, not by which of the three operations is damaged; where maintenance is realized, inside or outside, is separated only when both maintained capacities are destroyed'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-048 as a delegated
    lead worker, from the run filed as CASE-332.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in scratch/studies/lead-048/model.py such that, once corrected,
  the stated construction gives a different pattern: a lesion of one
  operation survived without the self-test, or without a producer, or the
  three operations giving different counts in some arrangement, or
  reciprocal and external maintenance separated by an injury other than the
  double lesion. A different model with other rules for detection, repair
  or maintenance does not defeat it; the claim is about this construction.
tags:
- self-governance
- epistemology
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-332
bears_on:
- QUESTION-086
- QUESTION-285
complements:
- CLAIM-414
- CLAIM-522
uses:
- TERM-100
summary: >-
  From the run of [LEAD-048](../leads.d/LEAD-048.md) ([CASE-332](../cases.d/CASE-332.md)), a reduced simulation of
  [CASE-186](../cases.d/CASE-186.md). With the self-test, reciprocal and external maintenance
  recover a second correction after any one operation is lesioned, in 64 of
  64 matched worlds, and the unmaintained arrangement in none. Without it,
  no arrangement recovers. Generate, admit and score give the same counts.
  Partial loss of either capacity separates production from none, and only
  destroying both separates reciprocal from external maintenance. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-332 CASE-265 — new or Proposed; the run this claim is drawn from, and the constant outside controller it is compared with -->
<!-- ref::uses-file: TERM-100 — "where maintenance is realized", inside or outside the boundary, is TERM-100's maintenance provenance -->

# CLAIM-901: In a simulation of an organization that corrects once and is then damaged, the second correction after an undisclosed lesion of evidence generation, admission or scoring is decided by whether the apparatus can find its own damage and has a producer to rebuild it, not by which of the three operations is damaged; where maintenance is realized, inside or outside, is separated only when both maintained capacities are destroyed

## The claim

[CASE-332](../cases.d/CASE-332.md) ran [CASE-186](../cases.d/CASE-186.md)'s organization in reduced form, on 64 matched worlds
per cell. The organization corrected the first reversal alike under every
maintenance arrangement. Its audit apparatus was then damaged before a
second change, in-family or out of family.

- **Component lesions.** A lesion of generate, admit or score, undisclosed,
  was recovered from in 64 of 64 worlds where the apparatus tested itself
  on known inputs and a producer, internal or external, could rebuild the
  operation. It was recovered from in 0 of 64 where it could not test
  itself, whatever the maintenance, and in 0 of 64 where nothing produced,
  whether or not it tested itself. Which operation was lesioned made no
  difference to any count. The failure is located in the loop of
  self-diagnosis and repair, not in an operation.
- **Capacity lesions.** Cutting diagnostic or evidence-governance integrity
  to a quarter separated production from none, 64 against 0. Interrupting
  the producer, and destroying the internal producer, separated nothing
  within the horizon run. Destroying both capacities separated reciprocal
  maintenance, which stays at its fixed point at zero, from external
  restoration, which does not: 0 against 64.

## What it does not say

- It is not evidence about any real organization. Most of the pattern is
  fixed by the model's rules: the self-test detects a changed operation,
  repair needs a producer, and protection of admission lapses with its
  integrity. The computation shows that the rules compose as stated across
  the arms, counted on matched worlds.
- It does not say the three operations are interchangeable in general.
  Here each lesion is total for the second correction and the self-test
  finds each at once. With partial lesions or weaker tests they could come
  apart.
- It does not bear against [CLAIM-522](CLAIM-522.md). The outside service here restores at
  a constant rate and does not supply the internal law as state feedback,
  so an intervention on state can find it out, as in [CASE-265](../cases.d/CASE-265.md).
- It does not test the recognition of an inadequate hypothesis family. The
  adequacy test is built in, as [CASE-186](../cases.d/CASE-186.md) stipulates.

## What it changes

[LEAD-048](../leads.d/LEAD-048.md) said that "a second correction that fails when one component is
lesioned and survives the others locates where maintenance is realized".
In this construction no component does that. What locates maintenance is
the double lesion, and the differences between arrangements under injury
are of the kind [CLAIM-414](CLAIM-414.md) describes: matched under the sham, exposed by
the intervention.
