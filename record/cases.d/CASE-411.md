---
number: 411
status: Proposed
formerly:
- CASE-tmpntt8e
title: 'Eleven open-source successions coded from their public records, timing outside verdicts against the move: the earliest outside verdicts were arranged with the founders, every independent identity verdict found was made in the same act as the speaker''s own move, recognition followed the maintainers where they moved wholesale and never the name except by reunion, and only one original line stopped producing'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, as a delegated lead worker. The
    coding rules, the data (51 dated events, each with its source address),
    the timing script, its tests and the results are committed under
    scratch/studies/lead-185/.
standing: documented
kind: executed-study
tags:
- individuation
- social-ontology
- social-identity
- software-engineering
date: '2026-11-23'
line:
- distributed-agency
variant_of:
- CASE-223
illustrates:
- CLAIM-328
bears_on:
- QUESTION-118
reported_in:
- NOTE-2383
- NOTE-2387
- NOTE-2404
- NOTE-2376
- NOTE-2384
- NOTE-2369
summary: >-
  [CASE-223](CASE-223.md)'s design run on public records: eleven cases from the record's
  own list and the lead's brief (eight contested, two accepted, one
  unclassified), coded by rules written before the table, with 51 dated
  events each read from its source on 2026-11-23. The earliest outside
  verdicts on a successor were printed in its founders' own announcement
  (LibreOffice, Valkey) or were a foundation's taking it in (OpenTofu,
  Valkey, Forgejo). A response by an organization independent of the
  founders was found in four contested cases, after 0 to 1,189 days; three
  of the four were the speaker's announcement of its own move, and the one
  statement made before a move (Fedora's proposal to replace Redis) gave
  the licence as its only reason. The only verdict found dated before the
  move it decided is the Hudson community's rename vote (214 to 14), whose
  voters were the movers. Recognition went to the successor in both cases
  where the creator or the body of core maintainers moved (Jenkins, Libera
  Chat), split where part of the core moved (MariaDB, Valkey), and no
  successor took the original's name except io.js, by reunion. Only
  Hudson's line stopped producing, 2,294 days or fewer after the vote; the
  other originals still release. The public records cannot time verdicts
  apart from migration, which is [ARG-067](../arguments.d/ARG-067.md)'s critical question. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-223 CLAIM-617 ARG-067 — Proposed; the design this runs, the claim it would test and the argument it was to rule -->
<!-- inactive-ok-file: CLAIM-1067 CLAIM-1154 CLAIM-1158 CLAIM-1041 — new, Proposed; the claims filed from this run -->

# CASE-411: Eleven open-source successions coded from their public records, timing outside verdicts against the move: the earliest outside verdicts were arranged with the founders, every independent identity verdict found was made in the same act as the speaker's own move, recognition followed the maintainers where they moved wholesale and never the name except by reunion, and only one original line stopped producing

## What was done

[LEAD-185](../leads.d/LEAD-185.md) asks for [CASE-223](CASE-223.md)'s design to be run: forks and successions
of open-source projects, coding when the community treats the successor as
the same project, and timing the verdicts against the move. The run used
public records only: project and foundation announcements, LWN.net and
other reporting, Fedora's change pages and FESCo tickets, and archived wiki
pages. Everything is under scratch/studies/lead-185/: `CODING.md` (the
rules), `cases.csv` and `events.csv` (the data, each event with its source
address and whether it was read), `timings.py` and `test_timings.py` (14
tests, passing), `results.json` and `summary.md`.

**The frame.** Every case [CASE-223](CASE-223.md) names and every example the brief names,
not those easiest to document. Two were excluded before coding, with
reasons: GIMP and SourceForge (a distribution mirror was taken, not the
project, as A's own caveat in [CASE-223](CASE-223.md) says), and `data.table` (no change
of steward, and no study named). Eleven were coded.

**The arms.** Contested: two lines each claim to be or continue the
project, and both release within twelve months of the successor's
announcement. Accepted: one line only. Audacity could not be placed, since
its fork's first release was not dated.

**What was coded.** For each case: the move the founders name (an
acquisition, a licence change, a takeover, a company's formation), the
successor's announcement and first release, endorsements printed in the
founders' announcement, a foundation's taking the successor in, the first
response by an organization independent of the founders (a statement, or a
statement announcing the speaker's own move; with its stated reason, coded
identity, licence or practical), a downstream's replacement of the
original, the original line's end, any reversal by the steward, and
whether the maintainers moved. The rules were written after a scoping pass
over the sources and before the table; the changes made while coding are
listed in `CODING.md`.

## The cases

| case | arm | maintainers moved | move to successor (days) | successor to first independent response (days) | that response | outcome by 2026-11 |
|---|---|---|---|---|---|---|
| OpenOffice.org to LibreOffice | contested | partial | 244 | 238 (Fedora 15) | move, identity and practical | successor |
| MySQL to MariaDB | contested | partial | 192 | 1,189 (Fedora's decision) | move, identity and practical | split |
| Hudson to Jenkins | contested | yes | 57 | none found | — | successor |
| Node.js to io.js | contested | partial | no discrete move | none found | — | reunited |
| Terraform to OpenTofu | contested | no | 15 | none found | — | undetermined |
| Redis to Valkey | contested | partial | 8 | 20 (Fedora's proposal) | statement, licence | split |
| Gitea to Forgejo | contested | partial | 51 | none found | — | undetermined |
| freenode to Libera Chat | contested | yes | 0 | 0 (SourceHut) | move, identity | successor |
| RethinkDB to the Linux Foundation | accepted | yes | 124 | — | — | successor |
| Audacity to Muse Group | unclassified | — | — | — | — | undetermined |
| `event-stream` handover | accepted | — | — | 78 (npm's revocation) | move, practical | revoked |

## The results

1. **The earliest outside verdicts were arranged with the founders.** The
   LibreOffice announcement printed Canonical's "the Ubuntu Project will be
   pleased to ship LibreOffice", and Google's, Novell's, Red Hat's, the
   FSF's and others' support ([NOTE-2383](../notes.d/NOTE-2383.md)). Valkey's founding release named
   AWS, Google Cloud, Oracle, Ericsson and Snap. OpenTofu (26 days after its
   fork), Valkey (day 0) and Forgejo (day 0) were taken in by a foundation
   or non-profit. These are verdicts by non-founders, but none independent
   of the move.
2. **An independent response was found in four of the eight contested
   cases**, after 0 days (freenode), 20 (Redis), 238 (OpenOffice.org) and
   1,189 (MySQL). In Hudson, Node.js, Terraform and Gitea none was found in
   the sources read.
3. **Three of the four were a move announced as a verdict.** SourceHut's
   "We entirely reject the illegitimate new leaders" is in the post saying
   "We will be moving our channels to Libera Chat, effective today"
   ([NOTE-2404](../notes.d/NOTE-2404.md)). Fedora's LibreOffice and MariaDB decisions are the
   replacement itself ([NOTE-2376](../notes.d/NOTE-2376.md)). The one statement made before its
   speaker's move, Fedora's proposal to replace Redis, gave the licence as
   its only reason ([NOTE-2384](../notes.d/NOTE-2384.md)): a migration needing no verdict on
   which line is Redis.
4. **One verdict precedes the move it decided, by its movers.** The Hudson
   community voted 214 to 14 to rename, and the lists, accounts and code
   organization were to move "in the coming days" ([NOTE-2387](../notes.d/NOTE-2387.md)). The
   voters were the community that moved.
5. **Recognition followed the maintainers where they moved wholesale, and
   never the name.** Where the creator or the body of core maintainers
   moved (Hudson, freenode), the successor is the recognized line: Hudson's
   own later steward wrote that "Jenkins is the replacement for it"
   ([NOTE-2369](../notes.d/NOTE-2369.md)). Where part of the core moved and the steward kept an
   employed team, recognition split (MySQL, Redis) or went to the successor
   (OpenOffice.org, whose name passed to Apache). No successor took the
   original's name except io.js, when the lines reunited under Node.js on
   io.js's code.
6. **Only one original line stopped producing.** Hudson's ended on or
   before 2017-05-11, 2,294 days after the vote. Every other contested
   original still releases or runs, from 970 days (Redis, which added the
   AGPLv3 in 2025) to 6,234 days (MySQL) after its successor appeared.
7. **The accepted arm.** RethinkDB's community and former employees carried
   it to the Linux Foundation 124 days after the company closed, with a
   first release on 2017-07-17. `event-stream`'s handover was accepted
   without contest until npm took the package back, 78 days after the new
   maintainer's first dated act, on security grounds.

## Checks of [CASE-223](CASE-223.md)'s list

- RethinkDB: the first community release was 2.3.6 on July 17, 2017, so
  A's "that July" was right and the reader's later recollection wrong. The
  CNCF's purchase and transfer to the Linux Foundation was February 6, 2017.
- Valkey: formed March 28, 2024, to "continue development on Redis 7.2.4"
  under the BSD licence, as A55 said. Redis added the AGPLv3 on May 1, 2025.
- freenode: the resignations and Libera Chat both date from May 19, 2021.
  The FSFE's move on May 25 and Libera's figures of June 30 were not checked.
- GIMP and SourceForge: not coded (excluded above).

## What it shows

It shows what public records can and cannot time. They date moves well and
verdicts badly. Independent verdicts on identity appear in them as the
reasons given for a move, in the same document and on the same day. A
verdict apart from its speaker's move, by people who are not the movers,
was not found. So the part of the design that [ARG-067](../arguments.d/ARG-067.md) said would tell
[CLAIM-617](../claims.d/CLAIM-617.md) from [CLAIM-329](../claims.d/CLAIM-329.md)'s criterion alone cannot be run on these records
([CLAIM-1067](../claims.d/CLAIM-1067.md), with an alternative reading at [CLAIM-1154](../claims.d/CLAIM-1154.md)). The survey
arm, contemporaneous surveys of participants, remains unrun.

On [QUESTION-118](../questions.d/QUESTION-118.md) it gives a pattern ([CLAIM-1158](../claims.d/CLAIM-1158.md)): the community's
recognition follows the producers, not the name, as [CLAIM-329](../claims.d/CLAIM-329.md)'s criterion
would have it. The split cases are [CLAIM-328](../claims.d/CLAIM-328.md)'s plural succession at a change
of steward: the name and an employed team with one line, part of the core
and some downstreams with the other. On the lag [CASE-223](CASE-223.md) took as its key
measure ([CLAIM-1041](../claims.d/CLAIM-1041.md)): a steward that keeps paid producers does not lose
productive capability when it loses legitimacy, so the lag is unbounded in
most cases; this is [CLAIM-521](../claims.d/CLAIM-521.md)'s point in a social key, in the reverse
direction to the one A expected.

## What it does not show

- Contributor numbers. None were counted; the brief rules out the GitHub
  interface for other repositories, and no contributor series was built.
- Private motives. Reasons are the reasons stated.
- Anything at scale. Eight contested cases; the cross-tabulation of
  maintainers and outcome has two cases in its "yes" row.
- That no independent verdict precedes the move in any of these cases. It
  shows none in the sources read; mailing-list archives were reached only
  where they were open, and Fedora's list archive was behind a bot check.
