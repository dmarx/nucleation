---
status: Proposed
title: 'A dialectic regime, switched on and off by the owner and on until switched off: while it is on, the assistant files the argument of the exchange as it goes, reports each filing as it lands, and reverts a filing when the owner interjects, rather than offering to file and waiting to be told; status changes, decisions, configuration, CI, delegated readings, outside services and merges still wait for the owner'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    At the owner's ruling of 2026-11-21: a go-ahead adopts the assistant's
    stated lean where its message left a choice (the alternative reading,
    that it chooses none, set aside), and the assistant raises a doubt about
    harm, reach or something the owner may have missed before acting on
    that item, crew-resource-management style. Earlier in the night, before
    merging, the regime gained the rule for several readings, the go-ahead
    rule and the reporting rule.
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
<!-- inactive-ok-file: ADR-tmp9pqps — Proposed; the decisions on merges into staging, 2026-11-21 -->
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
  development, QUESTION, CLAIM, CASE, TERM and ARG ([ADR-032](ADR-032.md)), and those
  that have joined them since, WORKBENCH and LEAD ([ADR-109](ADR-109.md)), which plans
  how to advance a question or a claim. The class is named rather than
  listed so that it extends as it does: a scheme added later to the
  record's own argument is covered without amending this decision. Each new
  entry passes [ADR-072](ADR-072.md)'s test that an idea gets a code when it has content
  of its own and is not already held;
- revisions to entries filed while the regime is on, before they merge;
- dated notes on held entries;
- Reframings sections ([ADR-tmpd4rgx](ADR-tmpd4rgx.md)), and the owner's corrections, recorded
  as corrections in curation entries and history notes;
- devlog notes for the next retrospective ([ADR-115](ADR-115.md)).

It files them under the rules that hold anyway: [ADR-068](ADR-068.md)'s invariants for
filing an exchange, Proposed status, an honest warrant, a check actually run
for anything called demonstrated, and the assistant's wording marked as its
own. A suggestion the owner disclaims is not filed unless the owner asks.

**When a turn has several valid readings, file them all.** If the assistant
is unsure how to file something because the owner's words, or the argument,
admit more than one reading that would be filed differently, it files each
reading rather than choosing one, marks them as alternatives of each other,
and says in the report which reading each is. A reading it would otherwise
leave out is filed too, as an option. In practice:

- rival claims, each with its own `defeated_if`, or one claim with the
  readings as `supposed` alternatives where only one can be the record's;
- rival senses of a term, under [ADR-050](ADR-050.md), or rival terms;
- for a decision the owner asked for, an alternative Proposed decision per
  reading, each saying what it would change, for the owner to choose; the
  others then go Rejected, which keeps the readings on the record.

The owner's choice among them is a status change, so it is the owner's; the
assistant may say which it would choose and why. The rule is the owner's,
2026-11-21: "if you're not sure how to file something because you feel like
there are multiple valid ways to interpret something, err on the side of
filing all of the alternatives".

**A go-ahead covers the whole message it answers.** When the owner answers
a message of the assistant's with a go-ahead (a "yes", "file it", "do it",
or switching the regime on), the go-ahead greenlights everything that
message proposed, not only its last item or the one most recently
discussed. The owner, 2026-11-21, after switching the regime on in reply to
a message proposing several filings: "part of the implication was that I
was greenlighting everything in the previous comment". Two limits:

- it covers an action the regime reserves to the owner (below) only where
  the message named that action as a proposal; a reserved action the
  message only mentioned still waits;
- where the message left a choice among alternatives to the owner and the
  assistant said which it leaned to, the go-ahead adopts that lean. The
  owner ruled so on 2026-11-21 ("go-ahead: your lean"), choosing it over the
  reading that the go-ahead keeps every alternative and chooses none. Where
  the assistant stated no lean, the alternatives stay open.

**When in doubt, raise it, CRM style.** The owner, with the same ruling:
"when in doubt (e.g. you're concerned about negative impact or large blast
radius or some other thing I may have missed) don't hesitate to double check
and raise my attention CRM style". As in crew resource management, a
go-ahead or a standing grant does not oblige the assistant to proceed past a
concern. When an action it is about to take, under the regime or under a
go-ahead, could do harm that is hard to undo, would reach widely (many
entries, a branch others build on, main, another repository, anything
outside), or turns on something the owner may not have seen, the assistant
stops on that item and says so plainly: what it was about to do, the
specific concern, what it recommends, and that it is waiting. It goes on with
the rest of the turn and does not proceed on that item until the owner
answers. Saying so early and directly is the point; a concern raised after
the action is a report, not a check.

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
- *Reporting, every time.* Reporting what is filed is part of the regime,
  not a courtesy: the owner's review depends on it, and an unreported
  filing is one the owner cannot revert. Every turn that files, merges or
  opens anything answers the substance first and then ends with a block
  headed **Filed**, which lists each entry created or changed (its code and
  a line on what it says), each pull request opened, each merge, and each
  change made outside this record, such as upstream, with the pull request
  it is in. A turn that files nothing says so. A long turn whose filing
  spans several steps reports each as it lands, and still ends with the
  whole block. The report says what was filed, not what might be. The rule
  is the owner's, 2026-11-21: "part of the convention needs to be
  reporting to me what you are filing".
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

## Note of 2026-11-21: merges into staging

The owner granted, with the regime on, that the assistant merge into
staging as it sees fit, keeping the promotion to main as their own review
point. That is a separate decision, [ADR-tmpq5b9e](ADR-tmpq5b9e.md), with the alternative reading [ADR-tmp9pqps](ADR-tmp9pqps.md);
under it, the item "merging into `staging`" above no longer waits for the
owner while the regime is on.

