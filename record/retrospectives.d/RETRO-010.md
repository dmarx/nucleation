---
number: 10
status: Draft
formerly:
- RETRO-tmpm36b1
title: "The stretch from the governance-of-possibility manuscript to the syntheses rule, 2026-11-23 to 2026-11-25: owner corrections were turned into decisions and skills within the hour, but the same error recurred in five forms, filing the wrong kind of object because the rules' letter was followed over their purpose"
tags:
- record
date: '2026-11-25'
reviews:
- ADR-068
- ADR-084
- ADR-104
- ADR-127
- ADR-139
- ADR-143
- ADR-144
- ADR-146
- ADR-145
- ADR-149
- ADR-151
pull_requests:
- https://github.com/dmarx/nucleation/pull/768
- https://github.com/dmarx/nucleation/pull/769
- https://github.com/dmarx/nucleation/pull/775
- https://github.com/dmarx/nucleation/pull/778
- https://github.com/dmarx/nucleation/pull/781
- https://github.com/dmarx/nucleation/pull/784
- https://github.com/dmarx/nucleation/pull/800
- https://github.com/dmarx/nucleation/pull/801
- https://github.com/dmarx/nucleation/pull/805
- https://github.com/dmarx/nucleation/pull/806
- https://github.com/dmarx/nucleation/pull/807
- https://github.com/dmarx/nucleation/pull/809
- https://github.com/dmarx/nucleation/pull/811
discussions:
- https://claude.ai/code/session_01HcmtbsE6G69iL3KUD21o5V
summary: >-
  Workshopped at the owner's word the same day: eleven items, each the
  instruction text that produced an error and a proposed rewording. At the
  owner's word of 2026-11-25 ("before tackling that huge stack of
  work, let's take a beat for a retro"). It covers the assistant's stretch
  from the manuscript governance-of-possibility ([#768](https://github.com/dmarx/nucleation/issues/768), [#769](https://github.com/dmarx/nucleation/issues/769)) to the
  syntheses rule and its correction ([#809](https://github.com/dmarx/nucleation/issues/809), [#811](https://github.com/dmarx/nucleation/issues/811)). What went well: each of
  the owner's corrections became a decision and a skill change, with a
  first application, within the hour, and parallel filers under [ADR-139](../decisions.d/ADR-139.md)
  lost no work. What went wrong is one error in five forms: the
  assistant filed the wrong kind of object, a LIT for a work, a question
  and claims for a procedural decision, an inventory for a synthesis, an
  audit for a manuscript and a retelling for an exchange's progress,
  because it followed the letter of the record's rules, which favoured
  traceability, over their purpose, and the owner caught each one, never
  a guard. It recommends a check of purpose before filing, a pilot
  before any sweep, coordination before editing what another session
  maintains, a narrower held list, and a question about whether
  bookkeeping edits on many entries are the right granularity.
---

<!-- inactive-ok-file: ADR-143 ADR-151 — Proposed; the decisions this retrospective reviews -->

# RETRO-010: The stretch from the governance-of-possibility manuscript to the syntheses rule, 2026-11-23 to 2026-11-25: owner corrections were turned into decisions and skills within the hour, but the same error recurred in five forms, filing the wrong kind of object because the rules' letter was followed over their purpose

## What it covers

The assistant's work in this conversation from 2026-11-23 to 2026-11-25,
after [RETRO-009](RETRO-009.md):

- the manuscript governance-of-possibility: its work ([#768](https://github.com/dmarx/nucleation/issues/768)), the
  write-manuscript protocol and the draft ([#769](https://github.com/dmarx/nucleation/issues/769), [ADR-143](../decisions.d/ADR-143.md)), its study filed
  as cases ([#778](https://github.com/dmarx/nucleation/issues/778)) and its membership pass ([#781](https://github.com/dmarx/nucleation/issues/781));
- four exchange filings: the pseudo-self question ([#775](https://github.com/dmarx/nucleation/issues/775)), "Explain First
  Contact RL" U26 to U32 and a branch ([#784](https://github.com/dmarx/nucleation/issues/784)), and "Hyper article
  interpretation" ([#801](https://github.com/dmarx/nucleation/issues/801)), each with parallel filers;
- the owner's [TERM-092](../terms.d/TERM-092.md) ruling ([#800](https://github.com/dmarx/nucleation/issues/800));
- the hyperarticle atlas: its fifteen scopes as lines ([#805](https://github.com/dmarx/nucleation/issues/805)), three works
  ([#806](https://github.com/dmarx/nucleation/issues/806)), the atlas as a series ([#807](https://github.com/dmarx/nucleation/issues/807)) and the correction that held its
  form as a decision ([#811](https://github.com/dmarx/nucleation/issues/811));
- the syntheses rule ([#809](https://github.com/dmarx/nucleation/issues/809), [ADR-151](../decisions.d/ADR-151.md)).

The governance-of-becoming session's devlog notes of the same days
(2026-11-24 20:58, 22:29; 2026-11-25 03:30, 07:25) are its own retro's;
this one cites them only where they meet its findings.

## What went well, and why

- **Corrections became rules at once.** Each time the owner corrected the
  kind of object filed, the next pull request carried a decision or skill
  change with its first application: the work in place of a LIT ([#768](https://github.com/dmarx/nucleation/issues/768)),
  the protocol rewritten from the record of practice ([#769](https://github.com/dmarx/nucleation/issues/769)), the syntheses
  rule ([#809](https://github.com/dmarx/nucleation/issues/809)), the procedural correction ([#811](https://github.com/dmarx/nucleation/issues/811)). The record now says what
  the owner said, and git blame leads from each rule to its case.
- **Parallel filing held.** Up to six filers shared one checkout under
  [ADR-139](../decisions.d/ADR-139.md) in [#784](https://github.com/dmarx/nucleation/issues/784) and [#801](https://github.com/dmarx/nucleation/issues/801). Committing each group only when its filer
  reported, and holding pushes that would have left dangling references,
  lost nothing and pushed nothing half written, against the stop hook's
  repeated prompting.
- **Checks found real things.** The gap fills computed by script changed
  readings of the source: the query-answer "game" is strategic only under
  shared resources or restricted queries; the joint frontier is fixed by
  the shared budget, not by A58's projection argument; registration is the
  publisher function nobody in the owner's split provides; views related
  only pairwise need not agree around a cycle.
- **Scripted application made conflicts cheap.** Memberships and line tags
  applied by script from readers' JSON were rebuilt on a fresh staging in
  minutes when [#806](https://github.com/dmarx/nucleation/issues/806) collided with [#805](https://github.com/dmarx/nucleation/issues/805).
- **Privacy held** in the hyperarticle filing: no style samples, handles or
  personal detail entered the record.

## What did not go well

1. **The wrong kind of object, five times.** A LIT for a work ([#768](https://github.com/dmarx/nucleation/issues/768),
   devlog 03:20 of 2026-11-23); a question and two claims for a procedural
   decision ([#807](https://github.com/dmarx/nucleation/issues/807), devlog 07:46 of 2026-11-25); syntheses written as
   inventories, an exchange's synthesis as a retelling, and manuscripts as
   audits of the record (all three named by the owner at [#809](https://github.com/dmarx/nucleation/issues/809)). The cause
   is the same each time. The assistant followed the letter of a rule
   whose wording favoured traceability: [ADR-084](../decisions.d/ADR-084.md)'s "names every component
   … and adds nothing", the old write-manuscript step 5's "every step
   cites the entry that holds it, with its standing", the regime's "file
   the argument". It optimised for attribution and coverage over the
   object's purpose, which was an argument for a reader, or a decision.
   The rules encoded the ledger reading and the assistant amplified it.
   No lint or review caught any of the five; the owner caught all of
   them.
2. **Hands free, read as hands on.** The assistant held a works
   registration and ended a turn asking for a go-ahead, because CLAUDE.md
   lists `luria.yaml` among held steps (devlog 07:20). The regime already
   forbade ending a turn on such a question.
3. **Collisions with another session.** The rewrite of
   governance-of-possibility's Part A collided with [#804](https://github.com/dmarx/nucleation/issues/804)'s refresh of the
   same files and was set aside unmerged. Version-number conflicts struck
   [#781](https://github.com/dmarx/nucleation/issues/781) and [#806](https://github.com/dmarx/nucleation/issues/806). The assistant had not checked which open branches
   touched those files before starting.
4. **Bookkeeping at scale.** Single passes edited 116, 65, 40 and 55 held
   entries, each with a version bump and a history note, for memberships
   and lines. The edits are correct under the rules, but they are the
   same tendency as the first item: ledger growth standing in for
   argument. They also make every such pass a serialization hotspot.
5. **Small slips.** Two subscriptions to the wrong pull request number; a
   worker's placeholder file mistaken for a stray; readers stopped by the
   usage limit mid-task and resumed by hand.
6. **A sweep nearly launched unpiloted.** After the syntheses rule landed
   with two demonstrations, the assistant started a sweep of 115 syntheses
   and two manuscripts before the owner had seen the new form at work. The
   owner's pause stopped it before anything ran.

## Recommendations

1. **Check purpose before filing.** Before an entry is filed, ask two
   questions. Whose subject is it: the inquiry's (an argument scheme) or
   the record's own procedure (an ADR or DP)? And who reads it, and for
   what: an argument for a reader (prose), or data a view can derive (a
   field, not a body)? Add the check to the read-and-file skill's intake
   and the write-manuscript skill's step 5.
2. **Pilot, then sweep.** A change of form is applied to two or three
   entries, reviewed by the owner, and only then swept. For the syntheses,
   one line first.
3. **Look before editing shared work.** Before rewriting a file or bumping
   many entries, list the open branches and pull requests touching them,
   and coordinate with the session that owns them.
4. **Narrow the held list.** Revise [ADR-127](../decisions.d/ADR-127.md)'s list of steps that wait for
   the owner to the hard-to-undo ones: merges into main, outside services,
   status changes on the owner's own entries. Registrations under an
   existing rule are filed and reported.
5. **Ask whether mass bookkeeping is the right grain.** A membership or a
   line given to a hundred entries might be recorded once, in the
   decision, and derived, instead of being written into each entry with
   its own version ([DP-003](../../docs/design-principles.md#dp-3)). This is a question for the owner and luria,
   not a change to make now.
6. **Let a guard see the form.** Consider a report, not a lint, that flags
   a SYNTHESIS whose body is mostly list items, and a manuscript part that
   says "the record holds". Fire it on the record before trusting it.

## Workshop: the wording that produced the errors, and proposed rewordings

At the owner's word of 2026-11-25 ("let's workshop this retro … if wording
was a problem: let's brainstorm how we should reword instructions. if
protocols are ambiguous, let's clarify the ambiguity"). Each item gives the
text as it stands, what it produced, and a proposed text. Nothing here is
applied; adopting an item is a revision of the instruction it names, each
in its own pull request with its first application.

### W1. "File the argument" has no test for what is argument

*Now* (CLAUDE.md, the dialectic regime): "While it is on, file the argument
the exchange develops as you go, without offering first: new entries in the
argument schemes …".

*Produced*: every argued turn was filed in the argument schemes, including
a turn about how the record should file itself ([QUESTION-540](../questions.d/QUESTION-540.md) and two
claims, retired in [#811](https://github.com/dmarx/nucleation/issues/811)).

*Proposed*: "While it is on, file what the exchange develops, by its
subject. What it argues about the subject of the inquiry goes in the
argument schemes (those of [ADR-032](../decisions.d/ADR-032.md), and WORKBENCH and LEAD). What it argues
about the record itself (what to file, where, under which scheme,
vocabulary, rule or skill) is procedure, and goes in an ADR or a revision of
one, with the readings in its Alternatives. Claims about the record as an
object of the inquiry (the line record-as-apparatus) are subject matter,
not procedure."

### W2. The held list contradicts hands-free filing and itself

*Now*: "Status changes on held entries, ADRs and DPs, `luria.yaml`, CI,
delegated readings, outside services and merges into main still wait for
the owner".

*Produced*: a works registration held for a go-ahead (devlog 07:20), and an
ambiguity W1 makes worse: if procedure goes in ADRs and ADRs wait, nothing
procedural can be filed hands free.

*Proposed*: "Filing is never held: a Proposed entry of any scheme, ADRs and
DPs included, and a vocabulary entry added under an existing rule, are
filed and reported. What waits for the owner is what is hard to undo or
reaches outside the record: merges into main; outside services and
delegated readings; adopting an ADR or DP (setting it Active); a status
change on an entry the owner holds (Active, Current, or in the owner's
voice); changes to CI and to luria.yaml outside its vocabularies."

### W3. "Several valid readings … file each" applies to procedure too

*Now*: "When a turn admits several valid readings that would be filed
differently, file each, marked as alternatives".

*Produced*: the two answer-claims of [#807](https://github.com/dmarx/nucleation/issues/807), filed as alternatives because
the owner's question had two readings.

*Proposed*: add "This is for readings of the owner's words about the
subject. Alternatives of procedure go in the ADR's Alternatives section,
and the assistant acts on its stated lean."

### W4. "Adds nothing" was read as "says nothing but the list"

*Now* ([ADR-084](../decisions.d/ADR-084.md)'s summary, still standing beside [ADR-151](../decisions.d/ADR-151.md)): syntheses
"map a scope's components and add nothing"; the scheme was "the scheme of
accounts".

*Produced*: inventories ([#809](https://github.com/dmarx/nucleation/issues/809)'s occasion).

*Proposed*: a version of [ADR-084](../decisions.d/ADR-084.md) that says "asserts nothing its components
do not; it states how they combine, which is what a synthesis is", and that
drops "account" and "map" for "synthesis" and "argument". [ADR-151](../decisions.d/ADR-151.md)
already rules this; [ADR-084](../decisions.d/ADR-084.md)'s own text still teaches the old reading to
anyone who reads it first.

### W5. The write-manuscript skill still contradicts itself on voices

*Now*: step 5's first bullet (revised in [#809](https://github.com/dmarx/nucleation/issues/809)) says voices belong in the
README; its third bullet still says "Voices stay separate. Name the owner's
theses as the owner's, another assistant's as theirs, and the drafting
assistant's own additions as its own."

*Proposed*: "Voices stay separate in the record, which keeps them in each
entry. In the text, name a voice only where the argument turns on whose a
step is; the README attributes the rest."

### W6. "Account for" is still the read-and-file skill's closing verb

*Now*: step 9b's "Account for it" and step 10's heading "Account for
everything", where the curation entry is written.

*Proposed*: "Record the audit" and "Close the filing". After [ADR-151](../decisions.d/ADR-151.md)
the word "account" should not name a list anywhere.

### W7. Membership by "any wording" inflates works

*Now* ([ADR-104](../decisions.d/ADR-104.md)): a claim is a member when the manuscript "states the
entry's proposition, in any wording; or" uses it as a step.

*Produced*: 116 members added to governance-of-possibility in one pass,
49 of them stated as neighbours, parallels or limits rather than used.

*Proposed* (an alternative, since the owner's merge of [#781](https://github.com/dmarx/nucleation/issues/781) adopted the
literal reading): "A claim is a member when the work's argument depends on
it: it is a step, or it is the work's own thesis. A claim the work states
to mark a neighbour, a parallel, a limit or a rival is cited, not a
member."

### W8. Bookkeeping edits are versioned like content edits

*Now*: no rule; [ADR-144](../decisions.d/ADR-144.md)'s precedent was "each with a history note and a
version bump", and every pass since followed it.

*Produced*: passes that edited 116, 65, 40 and 55 entries, each a version,
and the version collisions that blocked [#781](https://github.com/dmarx/nucleation/issues/781) and [#806](https://github.com/dmarx/nucleation/issues/806).

*Proposed*: "Adding a relation or a membership (a `works`, `line` or
`complements` value) under a decision is not a new version of the entry:
the decision names the pass and git keeps the edit. A version is a change
to what the entry says: its title, body, definition or status."

### W9. "A decision goes with a demonstration" says nothing of sweeps

*Now* (CLAUDE.md): "the pull request that proposes an ADR carries its
first application".

*Produced*: a sweep of 115 syntheses started minutes after the rule
merged, before the owner had read its demonstrations.

*Proposed*: add "A sweep that applies a new form to many entries starts
after the owner has had a turn on the first application; it then runs one
unit (a line, a manuscript) per pull request."

### W10. Nothing says to look for other sessions' work

*Now*: [ADR-139](../decisions.d/ADR-139.md) governs workers within one session; nothing covers another
session editing the same files.

*Produced*: Part A's rewrite set aside after [#804](https://github.com/dmarx/nucleation/issues/804)'s refresh.

*Proposed*: add to CLAUDE.md's "Working": "Before rewriting a manuscript
file or editing more than a handful of entries, list the open pull
requests and branches that touch them. If another session's open work
does, leave those files and say so, or coordinate in that work's pull
request."

### W11. "One open pull request" against "each unit its own pull request"

*Now*: the regime says "Put them in one open pull request into staging";
[ADR-071](../decisions.d/ADR-071.md) says each logical unit gets its own.

*Proposed*: "Put the regime's filings for one unit of work (one exchange,
one decision) in one open pull request into staging".

## The devlog notes it answers

- 2026-11-23 03:20 (a LIT for a work) and 03:45 (the protocol written from
  a README): item 1 and the first point under what went well.
- 2026-11-25 07:20 (hands free): item 2 and recommendation 4.
- 2026-11-25 07:46 (procedure filed as inquiry): item 1 and recommendation
  1.

## What it does not say

It does not judge the new synthesis form; two demonstrations are not yet a
test of it. It does not review the governance-of-becoming session's work,
which its own retrospective covers.
