---
status: Proposed
title: 'When an agent does the filing, the cost of capturing argument falls on the party that would otherwise pay to re-derive it, which removes the disparity that design-rationale systems were abandoned over'
version: 1
role: thesis
defeated_if: >-
  Agent-filed argument records are abandoned at rates like those of
  IBIS-era systems, for the reason Grudin gives: the people who must
  review, correct or read the record bear a cost that the people who
  benefit from it do not.
tags:
- design-rationale
date: '2026-10-11'
line: nucleating-argument
works:
- luria-nucleating-an-argument
answers:
- QUESTION-tmpdj25c
grounds:
- LIT-759
- LIT-761
- LIT-760
complements:
- CLAIM-tmp2jolp
summary: >-
  The answer to the cautionary literature the owner filed before the
  argument schemes were built ([ADR-030](../decisions.d/ADR-030.md)): design rationale goes uncaptured
  because whoever captures it is not whoever benefits. [ADR-032](../decisions.d/ADR-032.md) noted
  that agent filing changes the risk from capture stopping to capture
  flooding. This claim states why. Proposed: the record has run for one
  week.
---
<!-- inactive-ok-file: CLAIM-tmpu984q — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: CLAIM-tmp2jolp — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: LIT-759 LIT-760 LIT-761 — Deferred; cited for the argument ADR-030 summarises them for, not for a reading here -->

# CLAIM-tmp6b44r: When an agent does the filing, the cost of capturing argument falls on the party that would otherwise pay to re-derive it, which removes the disparity that design-rationale systems were abandoned over

## The claim

The design-rationale literature ([ADR-030](../decisions.d/ADR-030.md)) is largely an account of
why capture systems went unused. Grudin ([LIT-759](../literature.d/LIT-759.md)) identified the disparity:
the work of capture falls on one person and the benefit goes to another.
Buckingham Shum and Hammond ([LIT-761](../literature.d/LIT-761.md)) and Lee ([LIT-760](../literature.d/LIT-760.md)) ask when capture
repays its cost.

A collaborator with no memory pays the rediscovery tax every session
([LU-ADR-001](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-001.md)). When that same collaborator does the filing, capturing and
benefiting fall to the same party, and the capture is cheap because the
context is loaded at the moment of filing. Luria puts it this way: "Filed
with context loaded it costs a paragraph; re-derived cold it costs a
session" ([LU-DP-008](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-8)).

The disparity does not disappear. It moves. The owner now pays for reading
and correcting the record, rather than for writing it. That is why the
failure mode becomes flooding, and why the second-occurrence throttle
([CLAIM-tmp2jolp](CLAIM-tmp2jolp.md)) matters.

## What it does not say

- It does not say agent filing is accurate. Several workbench entries exist
  to correct what an assistant said about the record.
- It does not say the owner's review costs nothing. A week of operation is
  no evidence that the owner will keep reviewing.

## Note of 2026-10-11: flooding as unused anchors

Under the owner's reframing ([CLAIM-tmpu984q](CLAIM-tmpu984q.md)), the cost of capture is the
cost of making things persist, and flooding is persistence without use: a
code that no later entry points at. That makes over-capture measurable as
codes with no inbound references, beyond those that are new. Whether an
anchor goes unused because it was filed too eagerly, or because it is not
discoverable ([QUESTION-tmpw6fmc](../questions.d/QUESTION-tmpw6fmc.md)), the count alone cannot say.
