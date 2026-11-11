---
name: reading-review
description: 'A review of the readings (THEORY) the record holds and its argument does not use - which readings in force no line builds on, and what to do about each: tie it to a claim or question that should use it, raise a question or claim it calls for, or record that the argument does not need it. Three modes, by line, by topic and by question. Use it when the owner asks for a reading review or to see what the record has read and not built on, after a run of readings in one topic, or beside a synthesis review of a line. ADR-091 holds the invariants; ADR-090 how a reading''s lines are derived.'
---
<!-- .claude/skills/reading-review/SKILL.md -->
<!-- inactive-ok-file: ADR-091 ADR-090 ADR-085 ADR-075 — Proposed; the decisions this skill carries out, until the owner adopts them -->

# Reading review

A reading (THEORY) says what a work holds. The record's argument uses it
when a claim or argument grounds on it, it corroborates a claim, it answers
or bears on a question, or it reports a case. A reading's lines are the
first lines of the entries that use it, derived when the views are built
(ADR-090). The view docs/readings-by-line.md lists each line's
readings and, last, the readings in force that no line uses, by primary
topic.

A reading no line uses is not a defect by itself. The record reads more
than it argues, and some readings are held for the anthology's sake or for
later. The review asks of each unused reading one question: **should the
argument use it?** It answers in one of four ways (stage 3).

## Modes

Pick one per run. Each sets which unused readings are looked at, and what
they are looked at against.

- **By line.** For one line: the readings in force that this line does
  not use (unused by any line, or used only by others) whose topics, or
  whose `bears_on` and `answers` questions, fall in the line's subject,
  read against the line's claims and questions. Its question: what should this
  line be building on and is not? It sits beside a synthesis review of the
  same line, and the line's account (the current-account view) is where to
  start.
- **By topic.** For one primary topic in the view's last section: all its
  unused readings, read against the whole record. Its question: where does
  the record read and not argue? A topic with many unused readings and no
  claim may want a question, or a line.
- **By question.** For the open questions: the unused readings that bear
  on or answer some open question in substance though no relation says so,
  and the open questions whose readings (`bearing`) are all unused by any
  claim. Its question: which readings are evidence the argument has not
  weighed?

## 1. Stage 1: the list

Read docs/readings-by-line.md on the default branch. If it is missing or
stale, render it from the template:

    python3 -c "from luria.config import current; from luria import views; v=[x for x in current().views.values() if x.name=='readings-by-line'][0]; print(views.render(v))" > /tmp/rbl.md

The view lists readings in force only. A Proposed reading the argument
uses is ADR-057's matter (a claim on an unpromoted ground), not this
review's.

Select by every topic a reading carries, not only its primary topic, and by
the questions it bears on. A text search of the readings for the scope's
own terms finds more, with many false hits: keep only what the triage
(stage 2) passes. A run takes at most about sixty readings; split a larger
set by topic and run it in parts, in parallel where readers are used.

## 2. Stage 2: triage, then read

First triage on title and summary: a reading plainly off the scope's
subject is held with that reason and not read further. Read the rest in
full, with its `source`, its notes and its
`promote_when`. Note its status, its topics, and what it would be evidence
for. Read the candidate claims and questions it might serve in full too.
A reader's brief states the tests neutrally. It does not say how earlier
runs came out.

## 3. Stage 3: the verdict, one of four

- **Tie it.** A claim, argument or question already in the record should
  use it: its text cites the reading's work, or argues what the reading
  shows, or asks what the reading answers. Add the relation with `luria
  relate` from the entry that should carry it (`grounds` only if the claim
  needs the reading; `corroborates` from the THEORY if the reading is
  independent evidence the claim does not need; `bears_on` or `answers` from the THEORY for a question). The
  entry's own text must support the relation; quote it in the history note.
  A `bears_on` or `answers` relation is from the reading, so it changes no
  line of the record's own entries.
- **Raise.** The reading calls for something the record does not hold: a
  question it opens for a line, or a claim it supports that no entry
  states. File a QUESTION (Open) with the reading in its body and the
  reading's `bears_on` pointing at it, or draft a CLAIM (Proposed) grounded
  on it, for the owner. A claim drafted here that rests on claims passes
  ADR-075's step 5 first. Give either the line the mode is run for, or the
  first line of the entries it relates to (ADR-085).
- **Hold.** The argument does not need it now, and that is a judgement
  worth keeping: the reading is background, or a rival the record has not
  taken up, or kept for a line set aside. Record it in the curation entry
  with the reason. Change nothing in the reading.
- **Flag.** The reading itself has a defect (stale status, a `source` that
  does not say what it says, a `promote_when` already met), or its work
  holds a passage the argument cites and no reading covers. Report it; fix
  it in a defect sweep, or read the passage with `read-and-file`, not
  here.

Each reading gets one verdict in the count. A reading that raises a
question is counted as raised, even when the same run also ties it to an
existing entry; the curation entry names both. In the by-line mode a tie
counts when the entry tied is the line's own or a premise or component of
the line's entries (the line's account names it).

Some cases recur, settled by the first by-question run:

- **A moved condition.** A question that holds a reading's former
  `promote_when` (ADR-065) takes that reading's `bears_on`: the reading is
  its premise (ADR-060). Write it when the condition moves.
- **Whose words count.** The tied entry's own text, or the question's text
  naming the entry as bearing on it. A question that names a reading as its
  evidence states the relation.
- **A question that tests a claim takes no relation from it.** Where the
  question exists to test what a claim assumes, the claim does not bear on
  its own test; the question cites the claim.
- **A claim that names a question only to set it aside** takes no relation
  (ADR-085's CLAIM-534 exception).
- **Proposed readings** may be tied when their own text, or the
  question's, says they bear; a `bears_on` from a reading does not depend
  on its credence.
- **A run split across readers** writes one curation entry, by whoever
  combines the parts.

Watch for the free relation: a reading "relevant to" a claim is not
evidence for it. Tie only where the claim's or question's own words meet
what the reading holds.

## 4. Account for it

Write a curation entry, "Reading review of DATE, MODE: SCOPE", with:

- the list: how many readings the mode named, and how many were read;
- one row per reading: its verdict, the entry tied or raised, or the
  reason held or flagged;
- what the view now shows for the scope: readings used before and after.

Add a changelog fragment. One run is one contribution (ADR-071).
