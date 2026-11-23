---
status: Read
paper: LIT-tmpnnk6t
title: 'Horak — Replace MySQL with MariaDB'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Read in full on 2026-11-23 by the filer, from the Fedora wiki feature page (owner Honza Horak), last updated 2013-06-02, with the FESCo ticket that records its acceptance (https://pagure.io/fesco/issue/1006, a static archive). The ticket gives the devel-announce date 2013-01-21, used as `published:`; the devel-list archive page itself sits behind a bot check (Anubis) and was not read. HTML
    converted to text; the quotes below were checked against that text the
    same day.
date: '2026-11-23'
summary: >-
  Fedora's decision to make MariaDB the default in place of MySQL, with its stated reasons. Coded as data in [CASE-tmpntt8e](../cases.d/CASE-tmpntt8e.md).
---
<!-- inactive-ok-file: CASE-tmpntt8e — new, Proposed; the study that codes this reading -->

# NOTE-tmp576vq: Horak — Replace MySQL with MariaDB

## Contribution

Fedora's decision to make MariaDB the default in place of MySQL, with its stated reasons, dated by the document itself.

## Key results

- **The decision.** FESCo, 2013-01-30: "AGREED: Replace MySQL with MariaDB is F19 feature, Fedora prefers MariaDB (+7,-0)"; "Feature accepted as proposed (including obsoletion as a transition mechanism)".
- **Reasons about the steward.** "Recent changes made by Oracle indicate they are moving the MySQL project to be more closed. They are no longer publishing any useful information about security issues (CVEs), and they are not providing complete regression tests".
- **Reasons about the successor.** "MariaDB, which was founded by some of the original MySQL developers, has a more open-source attitude and an active community. We have found them to be much easier to work with, especially in regards to security matters."
- **The name stays.** "package mysql will retire as of Fedora 19. It means the name "mysql" will become only a virtual provider for compatibility reasons."

## Assumptions

None of the formal kind. It is a statement by an interested party: what it
says of its own reasons is its stated reason, not its motive.

## Concepts

The continuation of a project apart from its name and steward.

## Bearing on the record

An independent downstream's replacement decision, 1,189 days after MariaDB's first release. Its stated reasons mix the practical (security disclosure, tests, ease of work) with the successor's provenance in the original developers; the study codes them identity+practical. The decision is itself the move.

## Limitations

One document, by one party, on one day. It records a stated position, and
says nothing of how many people shared it.
