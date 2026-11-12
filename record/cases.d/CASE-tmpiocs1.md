---
status: Proposed
title: 'A proposed study of distributed evidence integration through a record: the hidden-profile tasks of HiddenBench run with conversation, the benchmark''s structured protocol, its Secretary summary, shared notes, a typed record and a governed one, with each clue traced from admission to uptake'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: Filed from the exchange "luria experiment design", A39 §2 and A45 Study 1.
- version: 2
  date: '2026-11-12'
  note: >-
    At the owner's review of #484 on 2026-11-12: "a Luria record could
    outperform ordinary communication simply by doing the Secretary's job
    more effectively", so HiddenBench's Secretary condition is brought into
    the main table of arms as AS, with a further arm AS+ that writes the
    Secretary's summary into the record's schemes. The design now says how
    the shared-notes arm differs from Secretary, makes A4 against AS an
    essential comparison beside A4 against A1, and says what result would
    show that the record wins only by doing Secretary's job better. The
    dated note of 2026-11-12 had put the Secretary arm in a note only.
standing: stipulated
kind: proposed-study
tags:
- social-science
- epistemology
- agency
date: '2026-11-12'
line:
- distributed-agency
- record-as-apparatus
bears_on:
- QUESTION-tmpxq2sb
draws_on:
- THEORY-tmp9qlii
- THEORY-tmprcmsd
- THEORY-tmp5lktm
- THEORY-tmpy4vu1
summary: >-
  From the exchange "luria experiment design" (2026-11-10). The owner asked
  at U12 about multi-agent coordination and at U16 to "check to see if we
  can cite prior research to corroborate or replace some of these
  experiments". A39 found that HiddenBench ([LIT-2294](../literature.d/LIT-2294.md), read on 2026-11-12) already
  benchmarks distributed evidence integration, and proposed adapting it
  rather than building a new pooling task; A45 kept it as Study 1. The
  replacement of A31's and A36's own designs by an existing benchmark is
  the owner's U16 at work; the arms and the stage trace are A's, and
  adopting them is the owner's call. Not run.
---
<!-- inactive-ok-file: LIT-2272 — Deferred; registered from the same exchange, not read -->
<!-- inactive-ok-file: LIT-tmpmvfl2 — Deferred; registered from the same exchange, not read -->
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: LIT-1399 — Unavailable; cited for what each holds, not as settled -->
<!-- inactive-ok-file: THEORY-tmp5lktm THEORY-tmp9qlii THEORY-tmprcmsd THEORY-tmpy4vu1 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# CASE-tmpiocs1: A proposed study of distributed evidence integration through a record: the hidden-profile tasks of HiddenBench run with conversation, the benchmark's structured protocol, its Secretary summary, shared notes, a typed record and a governed one, with each clue traced from admission to uptake

## The case

From A39 §2 of the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda).

**The tasks.** HiddenBench's 65 hidden-profile problems ([LIT-2294](../literature.d/LIT-2294.md)), "without
changing their evidence distribution or ground-truth answers". The
paradigm is Stasser and Titus's ([LIT-tmpmnde8](../literature.d/LIT-tmpmnde8.md)): members hold overlapping
but incomplete information, and the best decision appears only when the
unshared part is pooled. The human meta-analysis is held ([LIT-1399](../literature.d/LIT-1399.md)).

**The arms** (A39):

| arm | coordination |
|---|---|
| A0 | the benchmark's conversational baseline |
| A1 | the benchmark's structured communication protocol |
| AS | Secretary: the benchmark's shared summary of the facts disclosed so far, written each round by a passive summarizer that holds no evidence and takes no part in the discussion |
| AS+ | AS with the summary written into A3's schemes (evidence, hypotheses, objections, source standing) by the same non-participating summarizer; agents read it and post nothing to it |
| A2 | a shared Markdown evidence ledger with identifiers and source labels |
| A3 | a record with fixed schemes for evidence, hypotheses, objections and source standing |
| A4 | A3 with an explicit verification and integration procedure |

AS and AS+ were added at the owner's review of [#484](https://github.com/dmarx/nucleation/issues/484) (2026-11-12); the rest
are A39's.

**Shared notes are not Secretary.** A2 is not meant to reproduce AS, and
differs from it in three ways: the agents write it, each choosing what of
their own evidence to post, where in AS a non-participant summarizes what
has already been said; its entries persist and are addressable by
identifier, where AS is rewritten each round; and each entry carries its
source. AS can only restate what was disclosed in discussion; A2 can admit
a private clue that was never said aloud. AS+ isolates the record's form
from its authorship: it has A3's schemes and AS's summarizer.

"The essential comparison is **A4 versus A1**. If the published structured
protocol performs as well as governed Luria at lower cost, this is
evidence against Luria's additional machinery being useful for that class
of tasks." It has a second essential comparison, **A4 versus AS**: HiddenBench
finds the failure in surfacing, and Secretary is the benchmark's own
strongest shared-state control.

**When the record wins only by doing Secretary's job.** HiddenBench
reports that once every fact is disclosed the tasks are nearly solved, and
that Secretary's gains are "limited and model-dependent". A record arm can
beat A0 and A1 either by surfacing more of the unshared clues (admission),
or by keeping and organizing better what was already disclosed
(recognition, credibility, uptake), which is Secretary's job. The record
wins only by doing that job better if all of these hold: A3 or A4 beats AS;
AS+ matches A3 or A4 within the run-to-run spread; and unique-clue coverage,
the share of privately held clues that enter the shared state, is no
higher in A2, A3 or A4 than in AS. Then the gain is a better summary, which
a non-participant can supply, not something agents writing a record bring.
A record arm that raises unique-clue coverage above AS and AS+ shows the
contrary: the record changes what gets surfaced, which no summary of
disclosed facts can do. Schema change is left out: "Ordinary HiddenBench problems are
not designed to require schema amendments, and adding them would change
the benchmark."

## What it would measure

The benchmark gives final accuracy. A39 instruments the process, so that a
negative result can say where integration failed: unique-clue coverage,
interpretation accuracy, premature commitment, source fidelity and
decision success. These follow [CLAIM-403](../claims.d/CLAIM-403.md)'s stages, admission, recognition,
credibility and uptake.

**Acknowledgement against uptake.** After an agent contributes a decisive
private clue, randomize whether the integrator receives it as a message, as
a durable addressable entry, or as an entry with an explicit obligation to
evaluate its bearing on the current hypothesis, the evidence held
identical. "If the clue appears in the shared record but has no influence
on the outcome, the failure occurs after admission." The falsification
arm: an irrelevant but plausible clue, which an uptake obligation should
not make the team overvalue.

**Two budget regimes**, from [CASE-091](CASE-091.md) by way of A45 Study 1: equal
information, to compare access and operations, and equal memory and
computation, to compare what each substrate keeps. And A31's two fairness
conditions: equal total compute against a single agent given everything,
and equal compute per agent.

## What it could show

Whether the record beats a published structured protocol at integrating
distributed evidence, and at which stage any gain occurs. Not the value of
schema change, which [CASE-tmppm4do](CASE-tmppm4do.md) tests. Transactive-memory experiments
([LIT-tmpmvfl2](../literature.d/LIT-tmpmvfl2.md), [LIT-2272](../literature.d/LIT-2272.md)) are A39's precedent for a further arm that
separates knowing where expertise lies from communication itself, with
standing added as a variable: "a good outcome is not just retrieving the
correct source. It is using that source with the correct level of
authority."

## Note of 2026-11-12: Li, Naito and Shirado, Bragg et al. and Khatua, Zhu et al., read

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Li, Naito and Shirado** ([THEORY-tmp9qlii](../theory.d/THEORY-tmp9qlii.md)): HiddenBench's arms and its
  18-task subset are the natural comparison set. Its Secretary arm, a
  passive per-round summary of disclosed facts, gives limited and
  model-dependent gains (0.241 and 0.713 for the two models), and full
  disclosure nearly solves the tasks, so the failure is in surfacing. The
  shared-notes arm above is close to Secretary; the record arms are to be
  compared with it as the baseline, not only with conversation and the
  protocol. Its group-size results argue for varying the number of agents.
- **Bragg et al.** ([THEORY-tmprcmsd](../theory.d/THEORY-tmprcmsd.md)): AstaBench's principle that cost and
  tool access confound comparisons supports the control "Matched evidence,
  tools, models and budgets across arms", from a benchmark-design paper.
- **Khatua, Zhu et al.** ([THEORY-tmp5lktm](../theory.d/THEORY-tmp5lktm.md)): CooperBench is a candidate
  transfer task, as A31 proposed.
- Stasser and Titus ([THEORY-tmpy4vu1](../theory.d/THEORY-tmpy4vu1.md)) supply the original design, shared
  against unshared conditions with a plurality analysis, that a test of the
  case would reuse.

The design takes the Secretary arm as a baseline arm; it is otherwise
unchanged, and the study remains unrun.
