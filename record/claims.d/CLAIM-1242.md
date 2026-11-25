---
number: 1242
status: Proposed
formerly:
- CLAIM-tmp80nuw
title: A record kept in git passes the migration test for its sources and their history, which are content-addressed and travel with any clone, but not for what lives only on its host, such as pull-request descriptions, reviews and CI logs, which keep the owner's choices before they are filed and which hundreds of its files cite by number, nor for authorship, which most of its commits do not sign
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Gains the line scholarly-publishing (atlas scope 15) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
role: thesis
warrant: empirical
defeated_if: >-
  A count showing that the host-bound material the record cites is all
  filed into its sources, so that a migration loses nothing the record
  relies on; or a showing that the record's commits are signed or its
  authorship is otherwise authenticated.
tags:
- software-engineering
- society-and-governance
date: '2026-11-25'
line:
- record-as-apparatus
- scholarly-publishing
rests_on:
- CLAIM-1291
complements:
- CLAIM-1226
summary: >-
  The assistant's, filling a gap the idea ledger found at A13 of the
  exchange "Hyper article interpretation" (2026-11-22), which proposes the
  migration test ("I move the research record to Host B. Its stable
  identity, version history, contributor attribution, and editorial
  relationships survive") and says a trustworthy record of revisions and
  authorship across providers "requires actual engineering". Applied to
  Nucleation, the case U1 offers, by counts from its own checkout on
  2026-11-25. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1226 CLAIM-1291 CLAIM-1283 — Proposed; A45's reference-implementation claim, A's guarantees and migration test, the owner's thesis, and the assistant's claim on registration -->

# CLAIM-1242: A record kept in git passes the migration test for its sources and their history, which are content-addressed and travel with any clone, but not for what lives only on its host, such as pull-request descriptions, reviews and CI logs, which keep the owner's choices before they are filed and which hundreds of its files cite by number, nor for authorship, which most of its commits do not sign

## The gap

A13's test: "Suppose I publish a hyperarticle with Host A", Host A shuts
down, and "I move the research record to Host B. Its stable identity,
version history, contributor attribution, and editorial relationships
survive." It adds: "That last bit requires actual engineering"
([CLAIM-1291](CLAIM-1291.md)). The owner offers Nucleation as a hyperarticle
([CLAIM-1283](CLAIM-1283.md)). Does Nucleation pass?

## The claim

**What passes.** The sources and their history. Git names each commit by
a hash over its content and its parents, so a clone carries every version
with its identity, and a tampered history no longer matches its hashes.
For the text and its revisions, git is the engineering A13 asks for.

**What does not.** What lives on the host and not in the repository:

- *Pull-request descriptions and reviews.* The record puts the choices
  waiting on the owner in the promotion pull request's description, and
  the owner's inline rulings stay there until the owner removes them
  ([ADR-128](../decisions.d/ADR-128.md)). They reach the sources only as far as a history note or a
  curation entry files them.
- *Citations of pull requests.* Of the record's 11,776 markdown files
  under `record/`, 297 cite a pull request by number (dmarx/nucleation#N,
  "pull request N", "(#N)" or "PR N"), counted with `python3 -I` on
  2026-11-25. On another host those numbers point nowhere.
- *CI logs*, which the working agreement tells a filer to read when
  docs-check fails, and which no source keeps.

**Authorship.** A commit's author and date are what the committer wrote.
Of the 5,416 commits in this checkout's history, 4,670 (86.2%) carry no
signature and 746 carry one this checkout cannot verify (`git log
--format=%G?`, 2026-11-25); every signed one was committed by
GitHub itself, 577 of them merges and 169 not. So the history keeps who is said to have written each version,
not proof of it. The voice an entry is filed in (owner, another assistant,
this one) is a claim made in the text, kept with it, and no more
authenticated than that.

## What it does not say

It makes exact what [CLAIM-1226](CLAIM-1226.md) says in its title, that the
record has "no archival or identifier guarantees beyond its repository".

Not that the record should leave its host, and not that the host-bound
material matters equally: a ruling not yet filed matters more than a CI
log. It says which of A13's guarantees this record gives by construction
and which it gives only by filing.
