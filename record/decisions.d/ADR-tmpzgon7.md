---
status: Proposed
title: 'A dialectic regime, switched on and off by the owner and on until switched off: while it is on, the assistant files the argument of the exchange as it goes, reports each filing as it lands, and reverts a filing when the owner interjects, rather than offering to file and waiting to be told; status changes, decisions, configuration, CI, delegated readings, outside services and merges still wait for the owner'
version: 1
tags:
- record
- process
date: '2026-11-21'
summary: >-
  The owner, 2026-11-21: "brainstorm an ADR that would permit us (you and I)
  to enter and exit an engagement regime in which we can focus on the
  dialectic interaction on the assumption that I'll want to file and modify
  claims and such to document the conversation as we go. I'd still like to
  see what is being filed like you're already reporting, but I'd rather
  interject to have you revert a change than have you wait for me to
  command it. sometimes it's preferable to risk asking forgiveness once to
  asking permission a thousand times." And, on the draft: "it should be
  episode independent. it's an on/off switch. it's on until it's off. you
  are definitely permitted to invite that we exit that mode if you think it
  will become awkward for me or you to continue because of next steps or
  whatever."
---
<!-- inactive-ok-file: ADR-115 ADR-tmpd4rgx — Proposed; the decisions on devlog notes and on reframings this regime files under -->

# ADR-tmpzgon7: A dialectic regime, switched on and off by the owner and on until switched off: while it is on, the assistant files the argument of the exchange as it goes, reports each filing as it lands, and reverts a filing when the owner interjects, rather than offering to file and waiting to be told; status changes, decisions, configuration, CI, delegated readings, outside services and merges still wait for the owner

## Context

When the record's argument is developed in conversation, each filing has
gone through a handoff: the assistant answers, offers to file, and waits;
the owner says "file it"; the assistant files. In the session of 2026-11-20
and 21 the handoff came round about a dozen times, for the life cycle of an
entry, contraction, drift, hierarchy and hyperbolicity, depth scaling, the
retrospective scheme, predicates as constraints. Each round cost the owner a
turn spent on permission rather than on the argument, and left the record a
step behind the exchange it documents.

The safeguards that made asking first prudent now exist elsewhere. Work lands
in `staging` through pull requests, never in `main` directly ([ADR-116](ADR-116.md)).
Nothing reaches `main` until a promotion the owner or the Promote workflow
makes. Every change is a commit, so any filing can be reverted without loss.
The assistant's wording is already marked as its own
and every new claim enters Proposed. What remains of the risk is filing a
framing the owner would not have filed, and that is cheaper to revert once
than to prevent by asking each time.

## Decision

**A regime, not an episode.** The owner switches the dialectic regime on and
off, with "dialectic on" and "dialectic off" or any equally clear words. It
is on until switched off. It is not tied to a topic, a pull request or a
stretch of work. A new session cannot see an earlier session's switch, so it
starts off until the owner switches it on.

**While it is on, the assistant files without asking** what the exchange
develops in the record's own argument:

- new entries in the **argument schemes**: the schemes of argument
  development, QUESTION, CLAIM, CASE, TERM and ARG (ADR-032), and those
  that have joined them since, WORKBENCH and LEAD (ADR-109), which plans
  how to advance a question or a claim. The class is named rather than
  listed so that it extends as it does: a scheme added later to the
  record's own argument is covered without amending this decision. Each new
  entry passes ADR-072's test that an idea gets a code when it has content
  of its own and is not already held;
- revisions to entries filed while the regime is on, before they merge;
- dated notes on held entries;
- Reframings sections (ADR-tmpd4rgx), and the owner's corrections, recorded
  as corrections in curation entries and history notes;
- devlog notes for the next retrospective ([ADR-115](ADR-115.md)).

It files them under the rules that hold anyway: [ADR-068](ADR-068.md)'s invariants for
filing an exchange, Proposed status, an honest warrant, a check actually run
for anything called demonstrated, and the assistant's wording marked as its
own. A suggestion the owner disclaims is not filed unless the owner asks.

**Still the owner's word, regime or not:**

- a change of status on a held entry (promotion, rejection, supersession);
- an ADR or DP, so that the regime cannot amend itself;
- changes to `luria.yaml`, including adding a topic word;
- workflows and CI;
- delegated readings, which spend agent time;
- anything sent to an outside service;
- merging into `staging` or `main`.

**Mechanics.**

- *Where filings go.* While the regime is on, its filings go to one open
  pull request into `staging`, cut from `staging`: the filing of the
  exchange, which [ADR-068](ADR-068.md) already counts as one unit, so [ADR-071](ADR-071.md) holds.
  When the owner merges it, the next filing opens a new one. Its entries can
  cite each other's temporary codes because they share the branch. Work the
  regime does not cover goes to its own branch as before.
- *One commit per turn,* titled with what that turn filed. "Revert that"
  then names the last turn's commit, and the revert is a `git revert`,
  never a rewrite of history.
- *Reporting.* Each turn answers the substance first and then reports the
  filing in a short block: the codes, a line on each, the pull request. The
  report says what was filed, not what might be.
- *Interjection.* "Revert that", "don't file that" or "reword it" is acted
  on in the next turn. Silence leaves a filing standing on the branch; it
  is still unmerged, and the owner's merge is the review.

**The assistant may invite an exit.** When the next steps would make filing
as it goes awkward, for the owner or for the assistant (a run of tooling
work, a decision the regime excludes, a branch about to conflict, a stretch
where the exchange is exploring rather than asserting), the assistant says
so and suggests switching off. The owner decides.

**At an exit** the assistant summarizes what the regime filed since it went
on, with the open questions, and leaves the pull request for the owner.

## Alternatives considered

- **Ask each time, the status quo.** Safe, and it puts the cost on the
  owner, a turn per filing, and keeps the record behind the exchange.
- **A switch given only in chat, with no decision.** It would not survive a
  context summary, and the assistant's standing instruction to commit and
  push only when asked would still apply. A decision and a line in
  CLAUDE.md make it the standing ask.
- **Always on.** Filing during tooling work, where a filing can break CI or
  collide with a workflow change, is where reverting is not cheap. The
  switch keeps the regime to the dialectic.
- **Scoped to an episode, a branch or a topic.** The owner's first draft
  was read this way and rejected: the regime is a switch.
- **The workbench first,** promoting to claims once the owner engages.
  Lower risk, but it splits one argument across two places and adds a
  promotion step the regime exists to remove. The assistant may still use
  the workbench for material that is exploratory rather than asserted.
- **The assistant merges its own regime pull requests into staging.** It
  would remove the last wait, and remove the owner's review with it.

## Consequences

- The record keeps pace with the exchange, and the owner's turns go to the
  argument.
- More revisions per entry before merge, and more commits to read in the
  pull request. The per-turn commit and report keep them legible.
- The risk moves from filing too little to filing a framing the owner would
  not have: guarded by the report, the revert, Proposed status and the
  owner's merge.
- A `docs-check` run per push.
- If reverts become frequent, that is a reason to narrow what the regime
  files, and a topic for the next retrospective.

## First application

The CLAUDE.md map says how the regime works. The first filings made with it
on will cite this decision by its temporary code.
