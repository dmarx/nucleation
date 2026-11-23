---
status: Read
paper: LIT-tmp5xrt1
title: 'Wright — Replace Redis With Valkey'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Read in full on 2026-11-23 by the filer, from the Fedora wiki change page (owner Jonathan Wright), last updated 2024-10-02, with the FESCo ticket (https://pagure.io/fesco/issue/3203) and the Fedora Discussion thread that dates the proposal to April 17, 2024 (https://discussion.fedoraproject.org/t/f41-change-proposal-replace-redis-with-valkey-system-wide/113413). HTML
    converted to text; the quotes below were checked against that text the
    same day.
date: '2026-11-23'
summary: >-
  Fedora's decision to obsolete Redis for Valkey, with its stated reason. Coded as data in [CASE-tmpntt8e](../cases.d/CASE-tmpntt8e.md).
---
<!-- inactive-ok-file: CASE-tmpntt8e — new, Proposed; the study that codes this reading -->
<!-- inactive-ok-file: CLAIM-617 — Proposed; the claim whose rival this reading instances -->

# NOTE-tmpbx1r1: Wright — Replace Redis With Valkey

## Contribution

Fedora's decision to obsolete Redis for Valkey, with its stated reason, dated by the document itself.

## Key results

- **The reason.** "Obsolete Redis for Valkey due to Redis's license change to RASLv2/SSPL." "Redis's shift to the Server Side Public License (SSPL) that Fedora does not allow poses an issue. Valkey adheres to the original BSD licensing model".
- **The mechanism.** "Add "Obsolete: redis" to valkey-compat package."
- **The decision.** FESCo deferred on 2024-04-29 for the compatibility work, and closed the ticket "Accepted" on 2024-06-03.

## Assumptions

None of the formal kind. It is a statement by an interested party: what it
says of its own reasons is its stated reason, not its motive.

## Concepts

The continuation of a project apart from its name and steward.

## Bearing on the record

The one independent statement in the study that came before the speaker's move (the proposal of April 17, 2024, then the decision of June 3), and its only stated reason is the licence: a migration that needs no verdict on which line is Redis. It is, in a single instance, the cost-and-policy rival that [CLAIM-617](../claims.d/CLAIM-617.md)'s defeat condition names.

## Limitations

One document, by one party, on one day. It records a stated position, and
says nothing of how many people shared it.
