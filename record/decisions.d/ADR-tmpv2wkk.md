---
status: Proposed
title: 'The record keeps its research opportunities as LEADs, plans to advance a question or claim by any method, with a status for whether each is still worth following and a stage for how far it is worked out; and a question may presuppose another'
version: 1
tags:
- record
- taxonomy
date: '2026-11-19'
summary: >-
  The record's research opportunities were scattered: proposed-study
  CASEs (54, 28 of them bearing on no question), "What would answer it?"
  prose on 264 of 451 open questions, and proposed tests in dated notes.
  Nothing said which were still wanted, how far each was worked out, or
  which waited on which, and an opportunity that was not an experiment
  had no form at all. The owner asked on 2026-11-19 for a better way to
  represent this backlog, and supported dependencies among questions. A
  new scheme, LEAD, holds a plan to advance a question or claim: by
  reading, conceptual or formal work, a study, a history, or working out
  how a question could be advanced at all. Its status (Open, Done, Dropped,
  Superseded) says whether it is still worth following; a separate
  `stage` (idea, specified, underway) how far it is worked out. It
  `advances` questions and claims, may be `operationalized_in` a CASE that
  holds its design, and may `presuppose` a lead or a question. Questions
  gain `presupposes`, after THEORY's (ADR-029). Rejected: a "What would
  advance it?" section on every question; decision gates on claims; more
  fields on CASE; a backlog file outside the record.
---
<!-- inactive-ok-file: CLAIM-tmpkcdfh CLAIM-tmpitvrh QUESTION-tmpiualy CASE-294 CASE-tmp6idy5 — Proposed or newly filed; cited in this decision -->

# ADR-tmpv2wkk: The record keeps its research opportunities as LEADs, plans to advance a question or claim by any method, with a status for whether each is still worth following and a stage for how far it is worked out; and a question may presuppose another

## Context

The owner, 2026-11-19: "some opportunities are encoded as (or maybe just
prose within) CASEs, some as QUESTIONs, and some QUESTIONs and CASEs
haven't yet clarified how an opportunity could even be operationalized.
This obviously makes identifying and triaging opportunities more
challenging".

On that date the record held 451 open questions, 264 of them with a
"What would answer it?" section; 54 proposed-study CASEs, 28 bearing on
no question; and proposed tests in dated notes, the filing's own rule for
them (read-and-file, step 12). A proposed study had a form (a CASE,
ADR-042); a reading worth doing, a distinction to draw or a proof to
attempt had none. Whether a study was still wanted, how far it was worked
out and what it waited on were said nowhere.

The owner's question of how to triage open questions (QUESTION-tmpiualy)
and claim that experiment is not the only way to advance them
(CLAIM-tmpkcdfh) came from the same exchange. ChatGPT's answer
(CLAIM-tmpitvrh) proposed a "What would advance it?" section on every
question, explicit dependencies among questions, and a primary test and
decision gate for each empirical claim. The assistant's review of 2026-11-19
kept the dependencies and moved the rest onto a backlog; the owner
supported dependencies, having thought the record already kept them. It kept `refines` (202 questions), which says a question is a part
or sharpening of another, not that one cannot be answered before another.

## Decision

1. **A LEAD is a plan to advance a question or claim.** It names what it
   `advances` (required: QUESTION or CLAIM), what kind of work it is
   (`method`: reading, conceptual, formal, empirical, historical,
   operationalization; one or more), and its `line`. A lead is a plan,
   not a finding: what it yields is filed as readings, claims and cases,
   and the lead says where.
2. **Status and stage are separate.** `status` says whether the lead is
   still worth following: Open (in force), Done, Dropped, Superseded.
   `stage` says how far it is worked out: an idea names what it would
   advance; a specified lead says what would be done, what result would
   count for and against what it advances, and roughly what it costs; an
   underway lead is being done. They are orthogonal, as a CASE's standing
   and kind are (ADR-042).
3. **A study's design stays a CASE.** A lead whose design is held in a
   proposed-study CASE names it in `operationalized_in`; the case gains a
   derived `operationalizes`. The design is part of the argument (a case
   can illustrate or ground); the plan to run it is not.
4. **Leads and questions can presuppose.** A lead `presupposes` a lead that
   must be done first, or a question whose concepts or result any way of
   doing it must use. A question `presupposes` a question whose concepts
   or result any answer to it must use, as a THEORY's `presupposes` takes
   another's conclusion as a premise (ADR-029). "Would be easier after"
   is not presupposing and takes no edge.
5. **Operationalization is a lead.** A question that does not yet say how
   it could be advanced gets a lead with method `operationalization`, so
   the gap shows in the backlog rather than staying in prose.
6. **Filing.** A proposed test, reading, construction or study that a
   filing turns up goes in as a lead that advances the entry it bears on,
   at stage idea unless it is worked out; the dated note may name it. This
   changes read-and-file's step 12.

Triage, which leads to follow first, is not decided here. It is
QUESTION-tmpiualy's, and a review over leads and the `presupposes` graph
is the candidate.

The first application, filed with this decision, is ten leads from the
exchange "Topological protection explained" and its readings, on the
learned-structure line and the owner's Reddit case: the Pythia study's
calibration pilot and the study it presupposes (both operationalized in
CASE-294), the Reddit study (CASE-tmp6idy5), a compositional environment
and the inquiry experiment that presupposes it, a thermodynamic
milestone, two readings (the owner's suggestion of the GPT-3 paper, with
ULMFiT; and Lippl and Lindsey), a conceptual lead for QUESTION-493 and a
formal one for QUESTION-495. No question-to-question `presupposes` edge
was clear enough among the line's open questions to write in the
pilot; the review that applies this decision is where they are found.

## Alternatives considered

- **A "What would advance it?" section on every question.** A forecast
  on 451 questions, cheap to write, flattering to the question and stale
  soon; the record already keeps advances after the fact in dated notes
  and `bearing`. Where a forecast is worth writing, it is a lead.
- **A primary test and a decision gate on every empirical claim.** A
  decision gate is a plan for future work; on a claim it mixes what the
  record holds with what it intends. The negative result is already the
  claim's `defeated_if`. The design belongs to a CASE and the plan to a
  lead.
- **More fields on CASE** (a readiness, a bears_on requirement). A case is
  something the argument uses; most opportunities (a reading, a proof) are
  not cases, and a case would need a lifecycle that its status does not
  model.
- **A backlog outside the record** (an issue tracker, a file). It would
  not link to the questions and claims it advances, so the record could
  not show what waits on what.
- **Calling the scheme OPPORTUNITY, PROSPECT, PROBE or SEED.** LEAD is
  short, method-neutral and tentative, and says what one does with it:
  follow it. PROBE suggests experiment; SEED is the record's own metaphor
  but vague; PROSPECT and OPPORTUNITY are long.
- **Status quo.** The backlog stays scattered and triage has nothing to
  work over.

## Consequences

- A question or claim shows the leads that would advance it
  (`advanced_by`), and a question the leads and questions that presuppose
  it (`presupposed_by`), so how much waits on a question can be counted.
- Existing proposed-study CASEs and "What would answer it?" sections are
  not migrated by this decision. A review may file leads for them, line by
  line.
- read-and-file's step 12 changes with this decision; the reader's brief
  does not.
- In force is one status, Open, as luria's schemes allow, which is why the
  lifecycle is a separate field.
