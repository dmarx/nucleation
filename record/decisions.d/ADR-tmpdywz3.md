---
status: Active
title: 'A pull request description that several writers edit is divided into marked sections, each kept by one writer, and every edit reads the description just before writing and writes only if it has not changed since'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Active at the owner's ruling of 2026-11-21 on the promotion pull
    request, 599: "adopt the ADRs and the candidate line, then merge". It
    was applied on staging before adoption, in the pull request that
    proposed it.
tags:
- record
- process
date: '2026-11-21'
summary: >-
  At the owner's go of 2026-11-21 ("lgtm") on the elaboration of the fourth
  recommendation of the retrospective of that day (pull request 600). The
  promotion pull request's description had three writers: the workflow, and
  two sessions. One session rebuilt it from its own picture of the batch,
  and the list of choices waiting on the owner, which it had not written, was
  lost without anyone deciding to drop it. Shared descriptions are now
  divided into sections opened by markers. Each writer edits its own
  sections and copies the rest through unchanged. The owner's inline rulings
  are removed only by the owner. An edit compares the body's text just before
  writing with the text it last read, writes only if it is unchanged, and
  reads the body back. A wrong line is corrected, not the body rebuilt. Rejected: choices
  as comments, a file on staging, and a single writer.
---

# ADR-tmpdywz3: A pull request description that several writers edit is divided into marked sections, each kept by one writer, and every edit reads the description just before writing and writes only if it has not changed since

## Context

The promotion pull request ([ADR-125](ADR-125.md)) is the owner's review point. Its description holds the batch and the choices waiting on the owner, and the owner rules inline there, under each choice. On 2026-11-21 it had three writers:

- the Promotion PR workflow, which writes the body once, when it opens the pull request, and never again;
- this record's assistant in one session, adding choices as each unit merged;
- another session tending the same pull request.

GitHub keeps one body, and the last write wins. At 08:08 the other session rewrote the description to correct its account of the batch, and the choices section it had not written was dropped. The loss was found only because the first session re-read the description before its next edit. The retrospective of that day (pull request 600) set out a proposal, and the owner approved it: "lgtm".

## Decision

1. **Marked sections.** A description that more than one writer edits is divided into sections, each opened by an HTML comment naming it: `<!-- section: batch -->`, `<!-- section: choices -->`, and so on. The text the workflow writes on opening is its own section, `<!-- section: opened -->`, and is not edited.
2. **Each section has a keeper.**
   - **Batch:** whoever merges into staging adds the row for what they merged.
   - **Choices:** whoever adds a choice keeps it, and marks it done when it is done.
   - **The owner's rulings,** written inside the choices section, are never removed or reworded by anyone but the owner.
   - A writer copies every section it does not keep through byte for byte.
3. **Read, then write, then check.** Keep the body as last read, and compare it with the body as it is immediately before writing: the text, not the pull request's `updated_at`, which also moves whenever the pull request's head moves. Write only if the text is unchanged; otherwise merge into the newer text. After writing, read the body back once and confirm the other sections are intact.
4. **Correct the line, do not rebuild the body.** A writer who finds a section wrong fixes the wrong line, in that section, and says so in the turn that does it.
5. **Scope.** This applies to any pull request description with more than one writer. The promotion pull request is the standing case. A pull request with one writer needs no markers.

## Alternatives

- **Choices as comments.** Comments are append-only, so nothing is lost. But the owner's inline rulings worked because each answer sat under its question in one place, and comments scatter that.
- **A file on staging holding the choices**, copied into the description. It is durable and reviewable, but heavier than the problem, and a file promoted to main has to be cleared after each promotion.
- **One writer only.** It does not fit a record where several sessions merge into staging in one night.

## Consequences

- The first application is the open promotion pull request, 599. Its description is restructured into marked sections in the turn this decision is filed, with nothing removed.
- CLAUDE.md's paragraph on working through staging, which says to add the choices waiting to the promotion pull request, gains a pointer to this decision.
- Found in the first application: `updated_at` is not the check. Merging a pull request into staging moved [#599](https://github.com/dmarx/nucleation/issues/599)'s head and its `updated_at` with no change to the text, so the decision compares the text itself.
