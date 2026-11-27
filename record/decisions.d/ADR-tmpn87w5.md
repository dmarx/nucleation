---
status: Active
title: "A search of the record before filing, or before saying something is not held, covers open pull requests and searches the argument by the mechanism's words, reading the bodies of the nearest entries"
version: 1
tags:
- record
date: '2026-11-27'
summary: >-
  Active at the owner's word of 2026-11-27, "go ahead with recommendations
  1, 2, and 5", which accepted recommendations 1 and 2 of the retrospective
  RETRO-tmpxqcui. Four searches in two days missed what the record held. Two
  were keyed to the source's words: the Assistant Axis reading for the
  delusion claims, and CLAIM-118 for von Oswald et al. One used the wrong key
  for a work, a case-sensitive grep that missed Sen. One searched only the
  checked-out tree, while the paperclip-maximization account sat in an open
  pull request. Decided: the search before filing, or before telling the
  owner something is absent, covers the heads of open pull requests as well
  as the tree. It searches the argument schemes case-insensitively by the
  mechanism's words and their synonyms as well as the source's. It reads the
  bodies of the nearest entries, not only their titles. Its first
  application is step 2 of the read-and-file skill. Rejected: leaving it to
  the second, post-reading search, which comes after the brief that the
  first search shaped.
---
<!-- inactive-ok-file: RETRO-tmpxqcui — Draft; the retrospective that recommended this -->

# ADR-tmpn87w5: A search of the record before filing, or before saying something is not held, covers open pull requests and searches the argument by the mechanism's words, reading the bodies of the nearest entries

## Context

ADR-068's step 2 says to check the record before filing anything: works by
DOI, arXiv id, exact title and first author, and ideas by their key words.
In two days that check missed four times (RETRO-tmpxqcui; devlog notes of
2026-11-26 18:13 and 19:55, and 2026-11-27 01:51):

- **The wrong key.** A case-sensitive grep for "paretian liberal" missed
  LIT-285, so the assistant twice told the owner Sen was not on the record.
- **The source's words, not the mechanism's.**
  - Filing von Oswald et al., the search found only literature, and missed
    CLAIM-118, which the paper bears on directly.
  - Filing claims on chatbot-associated delusions, a search for "psychosis",
    "sycophancy" and "delusion" that read only titles missed the Assistant
    Axis reading (NOTE-1505). Its case studies are the most direct evidence
    the record holds.
- **One tree.** Asked to relate shortcut learning to paperclip
  maximization, the assistant found no account of paperclip maximization on
  the checked-out branch. It sat in dmarx/nucleation#837, an open pull
  request, and the owner had to say "try PR 837".

The skill already has a second search after reading. It comes too late to
help: the first search shapes the reader's brief, and the brief shapes what
the reader looks for.

## Decision

Before filing, and before telling the owner that something is not held, the
search of the record:

- **Covers open pull requests.** It fetches the remote branches, which
  include the head of every open pull request, and greps them as well as the
  checked-out tree. Stale branches add noise, and a hit on one is checked
  against its pull request before it is cited:
  `git fetch origin` then `git grep -i -e <word> $(git for-each-ref --format='%(refname)' refs/remotes/origin) -- record/`.
  A hit found only in a pull request is cited by name and pull request until
  that pull request merges.
- **Searches by mechanism as well as by words.** For each idea, it searches
  claims, questions, cases, terms, distinctions and leads, case-insensitively,
  by the mechanism's words and synonyms as well as the source's own. For
  "chatbot psychosis", that means persona, drift, awakening, confirmation and
  hysteresis.
- **Reads bodies.** It opens the nearest few hits and reads their
  statements, not only their titles, before deciding a thing is or is not
  held.
- **Feeds the brief.** What it finds goes into the reader's brief, under
  "why it is being read", by code.

## First application

Step 2 of the read-and-file skill, `.claude/skills/read-and-file/SKILL.md`,
amended to carry the four points above.

## Alternatives considered

- **Rely on the post-reading search.** Rejected for the reason above: by
  then the brief has narrowed what the reader looks for.
- **A luria command for cross-branch search.** Possibly later, upstream. The
  git command does the job now.

## Consequences

- A search costs a fetch and a wider grep. That takes seconds.
- Hits in open pull requests carry temporary codes that may not survive
  promotion. Citing them by name avoids the rewiring RETRO-tmpxqcui
  describes.
