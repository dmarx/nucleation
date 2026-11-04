---
status: Active
title: 'Each logical unit of work goes on its own branch and its own pull request, cut from the default branch'
version: 1
tags:
- record
date: '2026-11-04'
summary: >-
  A session given one designated branch had been putting everything on it,
  so one pull request (dmarx/nucleation#397) came to hold a luria pin,
  configuration, two syntheses, an exchange's filing and a vocabulary
  change. At the owner's instruction, each logical unit of work now gets a
  branch of its own, cut from the default branch, and a pull request of its
  own. Rejected: one branch per session; one branch for everything; leaving
  it to whatever branch a session was started on.
---

# ADR-tmp8mm4e: Each logical unit of work goes on its own branch and its own pull request, cut from the default branch

## Context

Sessions are often started with one designated branch, and until now they
put every piece of work on it. On 2026-11-04 the pull request for one such
branch, dmarx/nucleation#397, held a luria pin, scheme configuration, the
filing of a synthesis, the filing of an exchange, and a split of a core
term with its sweep. Review threads for unrelated work shared one page,
and nothing could merge until everything was ready. When a follow-up was
proposed as its own pull request, the session said its instructions kept
it to the one branch. The owner: "let's fix that. you should spin up a new
branch for each logical unit of work, which should each get its own PR."

## Decision

- **One unit, one branch, one pull request.** A logical unit is what a
  reviewer would accept or reject as a whole: the filing of one source,
  one decision with what it changes, one tooling bump, one sweep.
- **Cut from the default branch**, unless the unit depends on unmerged
  work, in which case cut from that branch and say so in the pull request.
- **This decision is the standing permission.** A session told to develop
  on one branch may open others for other units of work in the same
  repository, each with its own pull request, without asking again.
- **Work already on a branch stays there.** A unit is not split out after
  the fact unless the owner asks.
- The rest of CLAUDE.md's practice holds for every branch: open the pull
  request early, push each commit, pull the bot's repair before pushing,
  and put the changelog fragment in the same contribution.

## Alternatives considered

- **One branch per session.** A session's units are unrelated as often as
  not, and the pull request grows until it cannot be reviewed.
- **One branch for everything.** What this replaces.
- **Leave it to the session's designated branch.** It made the default an
  instruction nobody chose.

## Consequences

- More, smaller pull requests, each reviewable and mergeable on its own.
- A temporary code minted on one branch can collide only through
  numbering, which `luria concretize` settles where merges serialize.
- CLAUDE.md's "Working" section states the rule and points here.
