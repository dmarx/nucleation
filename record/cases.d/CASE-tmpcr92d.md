---
status: Proposed
title: 'A proposed study of open-source projects whose name, code or hosting passed to a new steward, comparing successions the community contested with ones it accepted on where the code, the contributors, the governance and the community''s own verdict went, with the lag between a loss of recognized legitimacy and a loss of productive capability as the key measure'
version: 2
history:
- version: 2
  date: '2026-11-07'
  note: >-
    A55 §4 of the second share of the exchange proposes Freenode and
    Libera, Redis and Valkey, and RethinkDB as cases of their own,
    "Standing: documented", and adds dated facts. The facts are added as
    A's, unverified, under a new section of things to check; the
    instances stay in this study until checked. The study is otherwise
    unchanged.
standing: stipulated
kind: proposed-study
tags:
- individuation
- social-ontology
- social-identity
- social-science
date: '2026-11-07'
line:
- distributed-agency
illustrates:
- CLAIM-328
- CLAIM-tmpjw473
summary: >-
  From the exchange "Individuation, Possibility, and Disposition"
  (2026-11-06 to 07). The design is the owner's, at U16: a project that
  was popular, died when its maintainer stopped attending to it, passed to
  someone who tried to revive it, with the community "measurably
  identifying with some form of \"it's not the same thing that it was\"
  sentiment after the transition", or, more simply, an open-source product
  bought and degraded. The arms, the measures and the main control are
  A's, at A36 §7: contested successions set against accepted ones, with
  the delay between lost legitimacy and lost productive capability as the
  key measure. A's candidate instances, Freenode and Libera Chat (2021)
  and GIMP and SourceForge (2013 to 2016), are A's reports, unverified
  here. The stipulated part is the materials; no result is claimed. The
  wording of the arms and measures is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-329 — Proposed; cited for its criterion, which the study would apply -->
<!-- inactive-ok-file: CLAIM-tmpjw473 — filed from the same exchange, Proposed; the claim the study would test -->

# CASE-tmpcr92d: A proposed study of open-source projects whose name, code or hosting passed to a new steward, comparing successions the community contested with ones it accepted on where the code, the contributors, the governance and the community's own verdict went, with the lag between a loss of recognized legitimacy and a loss of productive capability as the key measure

## The case

**The owner's design (U16).** "I don't have an example off the top of my
head, but another useful case study might be a project which was previously
popular, died when its maintainer stopped attending to it, transferred
ownership to someone else later on who wanted to try to revive it, and the
community measurably identifying with some form of \"it's not the same thing
that it was\" sentiment after the transition. maybe some open source product
being bought and enshitified is a more straightforward example?" It has two
variants: revival after abandonment, and acquisition followed by
degradation. What is held fixed is the name or the code; what is measured is
the community's verdict. Exchange share link:
https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e.

**A's arms (A36 §7).** "The strongest empirical study would compare
*disputed succession* with *accepted succession*." Contested: Freenode and
Libera Chat, Redis and Valkey, GIMP and SourceForge, OpenOffice and
LibreOffice. Accepted: RethinkDB's move to community governance in 2017, and
the `data.table` governance reform A reports as a "quantitative control".
A's list has no clean case of the owner's "bought and enshitified" variant
except OpenOffice after Sun's purchase by Oracle. The reader suggests, from
background knowledge and unverified: Audacity after its 2021 acquisition by
Muse Group, MySQL and MariaDB, Hudson and Jenkins, and, for the
abandonment-and-handover variant, the 2018 `event-stream` handover on npm.

**A's measures (A36 §7).** Technical continuity (code lineage, interfaces,
releases); productive continuity (contributors, reviewers, release
maintainers, CI ownership); governance continuity (permissions, policies,
maintainership); community identification (contemporary statements,
discussions, surveys); behavioural migration (fork participation,
downstream adoption); recovery after intervention (policy reversals,
rejoining). The key measure, in A's words: "the delay between a loss of
recognized legitimacy and a loss of productive capability". A ties it to
[CLAIM-521](../claims.d/CLAIM-521.md): the official project may keep its code, release machinery and
users "long after contributors begin migrating".

**The main threat to inference, which A names.** "contributor migration is
insufficient on its own. We would need contemporaneous statements or surveys
explicitly addressing legitimacy, continuity, or betrayal, and should
distinguish those judgments from cost-driven migration." For Redis and
Valkey A adds that "some major Valkey participants had clear commercial
reasons to oppose the Redis licensing decision". This is [CLAIM-342](../claims.d/CLAIM-342.md)'s
discipline: the verdict must be measured by evidence that does not pass
through the migration it is meant to explain.

## A's candidate instances, as A reports them

Both are A's reports from A36 §§1–2, with A's own citations to web
searches the record does not hold. Nothing below is verified here, and the
case cannot take `standing: documented` until it is.

**Freenode and Libera Chat, 2021.** A: "In May 2021, Andrew Lee asserted
operational control, citing ownership rights acquired through a holding
company years earlier." Most volunteer staff resigned and founded Libera
Chat, and communities moved their channels. A: "The legal and nominal
continuity followed Freenode." "Much of the operational, social, and
normative continuity followed Libera." To check:

- the dates of the takeover and of the resignations (May 2021);
- the ownership route A states (a holding company, years earlier), and the
  dispute over calling it a hostile takeover;
- Libera's figures "By June 30": "more than **40,000 registered users and
  700 projects or communities**";
- the reader adds, from background knowledge, that A omits Freenode's
  takeover of channels in June 2021, which bears on where the communities
  went.

**GIMP for Windows and SourceForge, 2013 to 2016.** A: the GIMP project
moved its Windows installers off SourceForge in 2013; by May 2015
SourceForge treated the old hosting project as abandoned, took it over, and
served installers with bundled offers; the developers repudiated it. A's
caveat: "**GIMP itself had not died**", and what was revived was a
distribution account, not the development project. In January 2016
SourceForge and Slashdot were acquired by BIZX, which ended the bundling in
February. To check:

- the 2013 move and its stated reason;
- the May 2015 takeover, and SourceForge's ground that the account had been
  "abandoned for more than 18 months";
- the wording of the GIMP statement A quotes, "abusing the trust that we and
  our users had put into their service";
- the BIZX acquisition (January 2016) and the end of bundling (February
  2016).

**The other arms' figures, also A's and unverified:** Foster and
Germonprez (2026), "Freeriding and Rebellion", *Information Systems
Journal*, doi:10.1111/isj.70060, on Valkey's first six months (52
contributors from 13 organizations, 22 of them earlier Redis contributors);
a Percona analysis of December 2025 (Valkey from 18 to 49 contributors over
18 months, about 80 pull requests a month in 2025 against Redis's 42);
Redis's AGPLv3 option of May 2025; RethinkDB's company closure (October
2016), the transfer of its code rights to the Linux Foundation (February
2017) and the first community release (A says "that July"; the reader
recalls a later date); and a January 2026 study of `data.table`, given
without author or title (+200% recruitment, threefold retention, pull
request resolution from over 700 days to under a week).

## A55's additions, as A reports them (second share)

A55 §4 of the exchange's second share
(https://chatgpt.com/share/6aeea2bc-d280-83e9-ac1f-f6772adf263c),
answering the owner's U25, proposes Freenode and Libera, Redis and Valkey,
and RethinkDB as three CASEs, each "Standing: documented · Kind:
specimen". Its sources are web searches that were not exported, so every
fact below is A's report, unverified here, and the instances stay in this
study until they are checked. To check:

- **Freenode and Libera.** "On May 19, former Freenode staff announced
  Libera Chat and explicitly expressed an intention to continue Freenode's
  legacy." "On May 25, the Free Software Foundation Europe announced that
  it would migrate its IRC presence to Libera".
- **Redis and Valkey.** "In March 2024, a change in Redis licensing
  prompted the Linux Foundation to establish Valkey from Redis 7.2.4,
  initially preserving its permissive BSD license."
- **RethinkDB.** "In February 2017, CNCF purchased the code rights and
  transferred them to the Linux Foundation under Apache 2.0." A55 drops
  A36's "that July" for the first community release, and adds that
  RethinkDB "should not be called a case of proven long-term success
  without separate longitudinal evidence".
- **GIMP and SourceForge.** A55 agrees with A's earlier caveat: a dispute
  about a distribution project, "not a transfer of ownership of GIMP
  itself".

A55 says the cases illustrate [CLAIM-287](../claims.d/CLAIM-287.md); the record's entry for plural
successors of a collective is [CLAIM-328](../claims.d/CLAIM-328.md), which this study illustrates. It
says RethinkDB illustrates "the productive-provenance distinction in
[TERM-100](../terms.d/TERM-100.md)"; [TERM-100](../terms.d/TERM-100.md)'s senses are formation, maintenance and source
provenance, and in those terms RethinkDB's code keeps its formation
provenance (the company) and moves its maintenance provenance (the
community). That reading is the reader's.

## What it can show

- **A second kind of case for [CLAIM-328](../claims.d/CLAIM-328.md).** The record's succession cases,
  [CASE-105](CASE-105.md) and [CASE-133](CASE-133.md), separate the bundled continuities by a relocation
  or a realignment. Here a change of steward separates them, and the
  community's own verdict is a measured variable. [CLAIM-328](../claims.d/CLAIM-328.md) records that a
  second case is what would move it.
- **A verdict for [QUESTION-118](../questions.d/QUESTION-118.md) in a given instance.** The reader's reading:
  under [CLAIM-329](../claims.d/CLAIM-329.md)'s criterion, causal transmission of the producing
  organization, the Freenode case picks Libera, because the volunteer staff
  moved. A calls Libera a "reconstruction"; in the record's sense that is a
  transmission, not an independent reconstitution.
- **A test of [CLAIM-tmpjw473](../claims.d/CLAIM-tmpjw473.md).** The reader notes it costs little: compare
  the timing of identity statements with the timing of contributor moves.
  Verdicts that precede migration and predict it beyond cost and incentive
  support the claim. Statements that follow the move and add nothing to a
  cost model defeat it.
- **The lag.** A long interval in which the contested project keeps
  releasing while its contributors leave would be [CLAIM-521](../claims.d/CLAIM-521.md)'s hidden
  fragility in a social key. Recovery after a reversal (Redis's AGPLv3
  option, SourceForge under BIZX) that does not bring the contributors back
  would be a putative instance of [CLAIM-463](../claims.d/CLAIM-463.md); A says so only as a suggestion,
  and adds "We should not claim SourceForge's reputation was or was not
  completely repaired without longitudinal evidence".

Given its standing it shows nothing yet: the instances are A's reports, the
arms are not matched, and no measure has been taken.
