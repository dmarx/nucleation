---
status: Active
status_note: >-
  Read on 2026-11-12 from arXiv. Registered as a stand-in for [LIT-tmpt3cxh](LIT-tmpt3cxh.md),
  VoCol, which no lawful copy reached.
title: 'Git4Voc: Git-based Versioning for Collaborative Vocabulary Development'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Registered on 2026-11-12 as a stand-in for LIT-tmpt3cxh (Unavailable).
    Identifier checked on the arXiv API: v1 2016-01-11, the only version;
    whether a published version exists (the reader names ICSC 2016) was not
    checked. Not held: no hit for Git4Voc or the arXiv id. No email address
    was sent to any service.
tags:
- databases
- design-rationale
date: '2026-11-12'
published: '2016-01-11'
arxiv: '1601.02433'
first_author: 'Halilaj'
keywords: []
implementations: []
summary: >-
  Lavdim Halilaj, Irlán Grangel-González, Gökhan Coskun and Sören Auer
  (2016), arXiv 1601.02433. Collaborative vocabulary development is "the
  process of finding consensus" among experts from different systems; the
  authors argue that a version control system is "the heart of the problem"
  and adapt Git. They list eleven requirements (communication, provenance,
  roles, workflow independence, quality assurance, documentation, deltas
  between versions, editor independence, modularity, multilinguality,
  labeled releases) and meet them with conventions and hooks: issues on
  GitHub-like platforms for discussion; commit history for provenance; a
  branching model by kind of change (basic, semantic, structural); server-
  or client-side hooks that enforce roles and run syntax checks (Rapper) and
  best-practice checks (OOPS!) before a commit, cancelling it on failure;
  post-commit documentation generation; one triple per line in Turtle so
  diffs work; files of at most 300 triples as modules; tags for releases.
  Git cannot show semantic diffs; external tools are proposed. Registered on
  2026-11-12 as a stand-in for [LIT-tmpt3cxh](LIT-tmpt3cxh.md); it is the same group's
  preceding design: Git-based versioning, validation hooks that refuse a
  commit, roles and recorded reasons; it does not restate VoCol's integrated
  environment.
---
<!-- inactive-ok-file: LIT-tmpt3cxh — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# LIT-tmpusag6: Git4Voc: Git-based Versioning for Collaborative Vocabulary Development

Lavdim Halilaj, Irlán Grangel-González, Gökhan Coskun and Sören Auer (2016), arXiv 1601.02433.

## Standing in the record

Registered on 2026-11-12 as a stand-in for [LIT-tmpt3cxh](LIT-tmpt3cxh.md), which the reading of the works cited in the exchange "luria experiment design" could not reach. it is the same group's preceding design: Git-based versioning, validation hooks that refuse a commit, roles and recorded reasons; it does not restate VoCol's integrated environment.
