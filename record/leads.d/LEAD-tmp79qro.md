---
status: Open
title: "Prototype mark-and-review collection with luria patterns and a view: trace the closure of declared working roots, list the material outside it for review without deleting anything, and compare that set with the material history shows to be inactive"
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed from A34's third pilot and A31 §§1–4, 7, 8, 12 and 15 of the
    exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26).
    The checks of A31's configuration against luria 1.11.0 and the
    working tree, and the corrected root policy, are the assistant's
    (Claude, in this session).
stage: costed
method:
- operationalization
- empirical
tags:
- design-rationale
- software-engineering
- information-retrieval
date: '2026-11-26'
line:
- record-as-apparatus
advances:
- CLAIM-tmpdid0k
summary: >-
  A34: "Prototype a tracing collector using Luria's existing `patterns` and
  `views`. Declare provisional roots such as current syntheses, ongoing
  leads, and explicitly protected questions. Trace the relevant dependency
  relations and generate a worklist of material outside that closure. Do
  not delete anything." Its comparison is of three sets: outside the
  roots, historically inactive, and both, which "separates structural
  liveness from dynamical liveness". A31 wrote the patterns and the view.
  Checked on 2026-11-26, all of them load in luria 1.11.0, but A31's roots
  use Current syntheses and the record has none, so as written the account
  roots mark nothing. It serves the owner's proposal of controlled
  forgetting (CLAIM-tmpu1fef). The pilot is A's;
  the checks and the corrected design are the assistant's (Claude, in this
  session), and adopting them is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpdid0k CLAIM-184 CLAIM-tmpu1fef — Proposed, or cited for what it holds; the hypothesis this lead serves and the limit on what a trace can decide, cited on 2026-11-26 -->

# LEAD-tmp79qro: Prototype mark-and-review collection with luria patterns and a view: trace the closure of declared working roots, list the material outside it for review without deleting anything, and compare that set with the material history shows to be inactive

## What A31 proposed, checked

Each pattern and declaration of A31 was loaded into luria 1.11.0 with the
record's `luria.yaml` (as a stand-in text, nothing written) and, where it
loads, matched against the working tree of 2026-11-26.

| A31 | loads | on 2026-11-26 |
|---|---|---|
| §1 `unbuilt_active_claim`: Active claims no claim rests on | yes | 215 of 474 Active claims |
| §2 `retired_anchor`: Active claims resting on a Superseded one | yes | none ([CLAIM-184](../claims.d/CLAIM-184.md), note of 2026-11-26) |
| §3 `accounted_for_claim`: Active claims a Current synthesis integrates | yes | none: no SYNTHESIS is Current (115 Proposed, 11 Superseded). With Proposed ones counted, 451 of 474, so not a worklist that discriminates |
| §4 `proposal_without_open_lead` | yes | 527 of 817 Proposed claims |
| §4 `question_without_open_lead` | yes | 328 of 498 Open questions |
| §7 `account_root`, `account_premises` (variable-length `rests_on*`) | yes | none, for the reason in §3 |
| §7 `lead_root`, `lead_premises` | yes | 432 claims advanced by an Open lead; 572 with their premises |
| §8 the `retention-review` view | yes | luria's view environment gives `docs()`, `match()` and `vocabulary()`, as A31 says; the template is valid in form and needs its file under `record/views.d/` |
| §12 `retention-grounds` vocabulary and a `many` field | yes | no entry carries it yet |
| §6 `hot_on_cold` | only once a `retention` field is declared | see [LEAD-tmpolbqp](LEAD-tmpolbqp.md) |

With A31's roots corrected to take Current or Proposed syntheses, the
trace marks 1,067 of 1,346 claims; 244 Active or Proposed claims fall
outside it (228 Proposed, 16 Active), beside 33 Superseded and 2 Rejected.

## The design

1. **Roots**, each a declared pattern:
   - claims a Current or Proposed SYNTHESIS integrates;
   - claims an Open LEAD advances;
   - claims that answer or bear on an Open QUESTION;
   - claims marshalled into a manuscript (`works`), which A31 §7 lists as a
     miss and the record already marks;
   - once the owner adopts it, claims carrying a `retention_grounds` value
     (A31 §12's protected roots: foundational, corrective,
     negative-knowledge, developmental, reproducibility, accountability).
2. **Trace** from the roots along `rests_on*`, through arguments with
   `argued_from` (the pattern the record already declares), and to
   objections either way, since a live claim keeps its objections live.
3. **Report** what is outside the closure, faceted by status and line.
   Nothing is changed or deleted; the page is a worklist for review.
4. **Compare** with [LEAD-tmpn6mi2](LEAD-tmpn6mi2.md)'s activity: the claims with no
   non-mechanical event in the last 30 days. Report three sets, outside the
   roots, inactive, and both, and read 20 drawn from each of the two
   disagreements to say what each method misses.

Steps 1 to 3 can run now, as a script over luria's view functions in
`scratch/`, with no change to `luria.yaml`; registering the patterns and
the view in `luria.yaml` is the owner's call. Step 4 needs
[LEAD-tmpn6mi2](LEAD-tmpn6mi2.md). A34's figure draws this pilot after the temporal graph,
while its caption says "Configuration experiments can begin in parallel
with history extraction"; only step 4 waits.

## What would count

- **For the method:** a reader blind to the sets, given 20 claims drawn from
  the intersection, judges at least 15 not needed by any open line of
  inquiry; and the two disagreement sets differ in ways A31 §7's list of
  omissions explains ("nested synthesis membership, support through `ARG`,
  objections, external evidence, manuscript citations, and dependencies
  expressed in prose").
- **Against:** 5 or more of the 20 judged needed. The roots then miss a kind
  of liveness, and the trace cannot be used to choose candidates for
  cooling.

What no result here can do is say that an entry outside the closure may
go. [CLAIM-664](../claims.d/CLAIM-664.md) holds that no rule reading only the support graph and the
statuses can decide whether a dependant falls; a trace is a worklist for
that judgement, as A31 puts it: "Review, not reclaim."

## Cost

The structural half: an afternoon, most of it already done in the checks
above. The comparison: an hour once the activity data exist, and the
blind reading.
