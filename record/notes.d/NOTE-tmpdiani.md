---
status: Read
paper: LIT-tmpnjnwq
title: 'Site Reliability Engineering, Appendix D — Example Postmortem'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 from Google's open web edition,
    https://sre.google/sre-book/example-postmortem/, HTML converted to
    text: the postmortem and its six footnotes (163-168). Read by the
    filer, not a delegated reader; the quotes below were checked against
    that text on 2026-11-22. The appendix is short, so nothing was skipped.
date: '2026-11-22'
summary: >-
  Google's worked example of a blameless postmortem, for a fictional
  66-minute outage of "Shakespeare Search". Root causes are technical;
  nine action items are owned by named engineers of the responding teams;
  the one policy item applies an error-budget freeze already in force. It
  names no decision above those teams and no one as at fault, and records
  a human error in the timeline without an agent.
---
<!-- inactive-ok-file: CASE-335 — Proposed; the pilot coding of postmortems the reading bears on -->
<!-- inactive-ok-file: CLAIM-750 CLAIM-905 THEORY-2000 — Proposed; the entries the reading bears on -->

# NOTE-tmpdiani: Site Reliability Engineering, Appendix D — Example Postmortem

## Contribution

A template filled in: the shape a Google postmortem is meant to take,
shown on a fictional incident. Chapter 15 of the same book (LIT-2784,
NOTE-2082) states the norms; this shows what a document written to them
contains.

## Key results

Quotations from the web edition (no page numbers).

- **Root causes.** "Cascading failure due to combination of exceptionally
  high load and a resource leak when searches failed due to terms not
  being in the Shakespeare corpus." Trigger: "Latent bug triggered by
  sudden increase in traffic." Footnote 164 defines the section: "An
  explanation of the circumstances in which this incident happened. It's
  often helpful to use a technique such as the 5 Whys [Ohn88] to
  understand the contributing factors."
- **Action items.** Nine, each typed (mitigate, prevent, process, other)
  and owned by one of five engineers who appear in the timeline
  (jennifer, martym, docbrown, agoogler, clarac): a playbook update, load
  balancing, a cascading-failure test "during next DiRT", a leak fix, load
  shedding, regression tests, a deploy, and "Freeze production until
  2015-11-20 due to error budget exhaustion, or seek exception due to
  grotesque, unbelievable, bizarre, and unprecedented circumstances".
- **Caution on action items.** Footnote 165: ""Knee-jerk" AIs often turn
  out to be too extreme or costly to implement, and judgment may be needed
  to re-scope them in a larger context."
- **Lessons.** "What went wrong": "We're out of practice in responding to
  cascading failure"; "We exceeded our availability error budget (by
  several orders of magnitude)".
- **An error without an agent.** The timeline at 15:34: "found
  order-of-magnitude error in whiteboard calculations for instance count
  increase". Elsewhere the timeline names who did what ("docbrown starts
  2x instance count increase").

## Assumptions

- The incident is fictional (a sonnet found "in a Delorean's glove
  compartment"), written to teach the template.
- The error budget and its freeze are prior policy, which the SRE book
  sets out elsewhere; the postmortem applies them and does not revisit
  them.

## Concepts

- Root cause and trigger, kept apart.
- Action item types: mitigate, prevent, process, other.
- "Where we got lucky": near misses, recorded.

## Bearing on the record

- **QUESTION-476** (bears on). The example keeps correction and gives up
  blame by design: the one mistake in the timeline has no agent, and the
  action items fix systems. It says nothing upstream of the responding
  teams, because the fictional incident has nothing there to say: the
  causes are a bug and a surge. So it shows the template, not where the
  trace stops when an upstream decision was in play.
- **CLAIM-750** (bears on, weakly; no relation written). Every action item
  is owned by an engineer of the responding teams, which fits the claim's
  prediction that action items "cluster at or below the reviewing team's
  authority". But a fictional incident whose causes are a bug and a surge
  is no test: there is no upstream decision for the trace to miss. The
  error-budget freeze is the one point at which the example touches a
  decision above the team, and it applies a policy rather than tracing a
  cause to it.
- **THEORY-2000** (parallel). The example matches the chapter's norm:
  causes "without indicting any individual or team".
- **CLAIM-905 and CASE-335** (background). The pilot coded public
  postmortems; this example would code as stopping at the engineering
  group, but it is a teaching document and not in the pilot's population.

## Limitations

- Fictional, and short. It cannot show what real reviews find.
- It shows the names of individual engineers throughout the timeline and
  as owners. Blameless practice here is not anonymity: the template
  names who acted and withholds judgement of them.
