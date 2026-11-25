---
number: 55
status: Active
formerly:
- CASE-tmp1uzfn
title: 'The discriminating fidelity study'
statement: >-
  The discriminating fidelity study: renderings built to dissociate wording,
  proposition, static stance and transport structure, judged by named
  populations in two languages on stated tasks
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11, by question: bears_on QUESTION-075
    added. The question's text: "The record's replies answer part of
    it": "CASE-055 names populations, tasks and an invariance test for
    one study." No other change.
standing: stipulated
kind: proposed-study
tags:
- psychometrics
- translation
- pragmatics
date: '2026-10-10'
illustrates:
- CLAIM-220
- CLAIM-202
- CLAIM-204
variant_of:
- CASE-005
line: pragmatic-transport
summary: >-
  A proposed study, filed on 2026-10-10 as the record's repair of
  [CLAIM-233](../claims.d/CLAIM-233.md), [CLAIM-232](../claims.d/CLAIM-232.md), [CLAIM-244](../claims.d/CLAIM-244.md), [CLAIM-226](../claims.d/CLAIM-226.md),
  [CLAIM-222](../claims.d/CLAIM-222.md) and [CLAIM-227](../claims.d/CLAIM-227.md). It restores [CASE-005](CASE-005.md)'s three-way
  selection with human receivers, and adds a proposition-plus-force
  rival, a behavioural task-indexed criterion, predictors rated by other
  raters, named populations, an interlingual arm and a measurement
  stage. It has not been run, and its margins are not yet fixed.
bears_on:
- QUESTION-075
---
<!-- inactive-ok-file: CLAIM-220 CLAIM-202 CLAIM-204 CLAIM-240 CLAIM-228 — Proposed; the record's revised theses and restated measures of 2026-10-10, open, which this design would test -->
<!-- inactive-ok-file: CLAIM-244 — Proposed; an objection this design answers, left open until the owner decides on the revised theses -->
<!-- inactive-ok-file: CLAIM-129 — Proposed; open, cited in the note of 2026-10-10 for the gap between recovering structure and reaching the act -->

# CASE-055: The discriminating fidelity study

## The case

A design, stipulated by the record on 2026-10-10 in reply to the audit's
objections to the central tests. It is in the line of [CASE-005](CASE-005.md), [CASE-021](CASE-021.md) and
[CASE-040](CASE-040.md), which are also proposed designs, and of [CASE-005](CASE-005.md)'s Experiment 2 in
particular, whose three-way selection it restores. It is the study the
revised theses [CLAIM-220](../claims.d/CLAIM-220.md), [CLAIM-202](../claims.d/CLAIM-202.md) and [CLAIM-204](../claims.d/CLAIM-204.md) name in
their defeat conditions. Every margin, power and rate it needs is to be fixed
in its preregistration, by the owner; none is fixed here.

**Stage 0: measurement ([CLAIM-227](../claims.d/CLAIM-227.md)).** Before any fidelity test:

- definitions of stance and footing given to the judges in writing;
- a fixed response format;
- reliability between judges and between two passes by the same judge,
  against a target fixed in advance;
- known-groups validation: renderings that differ only in the attributed
  speaker ([CASE-018](CASE-018.md)'s reattributions used as stimuli) must be rated as
  differing in footing, and renderings that differ only in wording must not.

Its results bear on [QUESTION-076](../questions.d/QUESTION-076.md).

**Source items.** Two kinds.

- [CASE-040](CASE-040.md)'s topic × act cells (spending or relationships, teasing or
  reprimand), written by item writers.
- Naturally occurring utterances of teasing, reproach and reprimand, drawn by
  a stated sampling rule, with their act labelled by raters who did not
  select them.

**Rendering arms, for each source item.**

- (a) Proposition kept, footing changed: [CASE-027](CASE-027.md)'s kind, the sociologist's
  Henley.
- (b) Proposition changed, footing kept: the necessity half of "neither
  necessary nor sufficient" ([CLAIM-229](../claims.d/CLAIM-229.md)).
- (c) Static stance and footing matched to the source, response to later
  framings different: the renderings [CLAIM-202](../claims.d/CLAIM-202.md) needs.
- (d) A professional translation under a stated brief.
- English intralingual retellings, for comparison with the interlingual arm.

**Languages ([CLAIM-222](../claims.d/CLAIM-222.md)).** English sources. Targets: French or German,
where the T/V choice is obligatory, and Japanese, where honorific marking is.
In each, footing is grammatically marked on the target side only, so a
rendering must choose a footing the English leaves open. Renderings by
professional translators under stated briefs.

**Receivers ([CLAIM-226](../claims.d/CLAIM-226.md)).** Named populations of native readers of each
language, recruited by a stated sampling frame. Source-language readers
supply the source terms; target-language readers the target terms.
Measurement invariance across the two communities is tested on anchor items
whose act is fixed by convention (a formal apology, a greeting to a
superior), so that a difference between populations is estimated and not
read as distortion by transport. For historical sources (Villon, Henley,
Marot) a separate arm, whose source term is scoped as fidelity to a stated
modern reading, since there is no source audience to ask.

**Criterion ([CLAIM-232](../claims.d/CLAIM-232.md), [CLAIM-244](../claims.d/CLAIM-244.md)).** Behavioural and
task-indexed: the receiver's choice of act (which of a stated set of acts the
rendering performs) and choice among offered continuations, under stated
tasks. Holistic fidelity ratings are collected as a secondary outcome, for
[CLAIM-240](../claims.d/CLAIM-240.md).

**Predictors.** All human-rated predictors are rated by raters other than
those who supply the criterion.

- Human-rated: propositional sameness; sameness of proposition and
  illocutionary type; the static stance and footing profile.
- Machine: embedding similarity, surface similarity, topic factors, a
  supervised text model trained to predict act labels.
- Theory: class-level observational distortion ([CLAIM-228](../claims.d/CLAIM-228.md)), the order
  effects of sequence contexts ([CLAIM-231](../claims.d/CLAIM-231.md)), the directed decision term
  ([CLAIM-259](../claims.d/CLAIM-259.md)), and the change of cover ([CLAIM-257](../claims.d/CLAIM-257.md)).

**Analysis.** Judge and group random effects, so that disagreement between
judges is modelled and not averaged away. Predictions scored on held-out
renderings. Equivalence tests with margins and power fixed in a
preregistration, which also fixes the observables and their weights.

## What it can show

Whether the central theses survive rivals that hold the pragmatic point: the
proposition with its force, and the static pragmatic profile. Whether the
transport structure adds to the static profile. Whether any of it holds
across a language pair in which footing must be chosen.

Its standing is stipulated, so as yet it shows nothing. Run, it could not
show the ontological clause of the October thesis ([CLAIM-150](../claims.d/CLAIM-150.md)), nor which
distinctions a translation ought to keep ([CLAIM-252](../claims.d/CLAIM-252.md)), nor anything about
language pairs it does not run.

## Note of 2026-10-10: the interlocutor's reading of the design

At U61 the owner asked for "an updated proposal that takes PR#121 into
account". The assistant's revised proposal (A232 §8) says its central
experiment "follows the design filed in PR [#121](https://github.com/dmarx/nucleation/issues/121)" as this case, and
reproduces it, Stage 0 included, so nothing in the measurement stage is new.
It adds three things. None is adopted here.

1. **Two more items to preregister.** A232 Stage 6 lists "exclusion rules"
   and "the principal language-pair comparison" beside the tasks,
   observables, weights, margins and power this design already leaves to
   the preregistration.
2. **Response to later framing as a receiver outcome.** A232 Stage 4 makes
   "How does the answer change after specified subsequent framing?" a
   primary outcome, beside the choice of act and of continuation. Here the
   criterion is the choice of act and of continuation only, and response to
   later framings enters as a predictor rated by other raters, through arm
   (c) and [CLAIM-202](../claims.d/CLAIM-202.md).
3. **A map of outcomes (A232 §11).** In the record's terms: "Strong
   success" is [CLAIM-220](../claims.d/CLAIM-220.md) and [CLAIM-202](../claims.d/CLAIM-202.md) both surviving, though A232
   also asks the transport measures to beat "strong supervised
   alternatives", which [CLAIM-202](../claims.d/CLAIM-202.md)'s condition does not; "Partial
   success" is [CLAIM-220](../claims.d/CLAIM-220.md) surviving and [CLAIM-202](../claims.d/CLAIM-202.md) defeated;
   "Structural-method success only" is signatures that transfer without
   predicting receivers, the gap [CLAIM-135](../claims.d/CLAIM-135.md) and [CLAIM-129](../claims.d/CLAIM-129.md) describe between
   recovering structure and reaching the act;
   "Failure" is [CLAIM-220](../claims.d/CLAIM-220.md)'s defeat condition met; and "Ontological
   limit" is [CLAIM-150](../claims.d/CLAIM-150.md).

One difference. A232 counts "the observables cannot be measured reliably"
as failure. Here a Stage 0 failure is a negative answer to
[QUESTION-076](../questions.d/QUESTION-076.md). No defeat condition of the theses names it, so they would
be left untested, not defeated.

The design above is unchanged.

## Note of 2026-11-22: a draft preregistration, nothing fixed

<!-- inactive-ok-file: CLAIM-504 — Proposed; the strong contextual baseline the draft specifies, open -->

For [LEAD-146](../leads.d/LEAD-146.md) the assistant drafted the preregistration this design leaves
to the owner. It is in scratch/studies/lead-146/preregistration-draft.md,
with the power simulation beside it (power.py, results.json). It fixes
nothing. Every margin, power and rate stays the owner's, and the draft
lists seventeen choices, each with its alternatives and a lean. The design
above is unchanged.

What it drafts:

- **Hypotheses**, each as the defeat condition of its claim, on one effect:
  the held-out increment in R² that one predictor set adds over another in
  predicting receivers' recovery, with folds grouped by source item. H1 is
  [CLAIM-220](../claims.d/CLAIM-220.md)'s test: pragmatic observables over proposition, and over
  proposition with force. H2 is [CLAIM-202](../claims.d/CLAIM-202.md)'s as worded: transport over the
  static profile on arm (c). H2′ is [CLAIM-202](../claims.d/CLAIM-202.md) restated against a strong
  contextual baseline, which is what [CLAIM-205](../claims.d/CLAIM-205.md) asks for. [QUESTION-074](../questions.d/QUESTION-074.md)'s
  composition test is offered as exploratory.
- **The baseline.** [CLAIM-504](../claims.d/CLAIM-504.md) names its kind and leaves it unspecified. The
  draft gives it three parts:
  - the same context-response ratings that the transport measures
    ([CLAIM-228](../claims.d/CLAIM-228.md), [CLAIM-231](../claims.d/CLAIM-231.md), [CLAIM-259](../claims.d/CLAIM-259.md)) are computed from;
  - a learner tuned by nested cross-validation;
  - a supervised text model.

  So the increment measures what the structure adds, not what more data
  add.
- **Populations and frames** ([CLAIM-226](../claims.d/CLAIM-226.md)):
  - first-language adult readers in one named country for each language,
    from one named panel, with census quotas;
  - predictor raters from a separate pool;
  - an optional bilingual population;
  - about twenty anchor items for the invariance test. If fewer than three
    quarters of the anchors are invariant, the interlingual defeat tests
    are not run.
- **The language pair** ([CLAIM-222](../claims.d/CLAIM-222.md)): English → German, French or Japanese.
  The lean is German, because the result depends on the invariance test
  passing. Japanese is a second pair if the budget allows.
- **Prevalences**, as assumptions for a pilot to replace:
  - mean recovery 0.65;
  - three quarters of source items with a majority act;
  - half of the arm (c) renderings passing the static-match check;
  - 10% of receivers excluded.
- **Decision rule**: defeated if the 90% interval's upper bound is below
  the margin; supported if its lower bound is above it; otherwise
  inconclusive.
- **Margin and power**, computed:
  - At a margin of 0.05 in held-out R², 160 analysed items an arm (960
    renderings, 30 receivers each) give power 0.95 to support an increment
    near 0.10, and almost certainly defeat a null one.
  - A margin of 0.02 needs 400 items for power 0.93.
  - A margin of 0.01 is out of reach at these assumptions.

  Power to support, not power to defeat, is what limits the design. The
  same small-sample bias makes the defeat rule too liberal at the margin:
  a thesis whose true increment equals the margin is defeated 9% of the
  time at the lean, not 5%. The draft leans to 0.05 and says the reason is
  feasibility.

The wording is the assistant's (Claude, in this session); adopting it is
the owner's call.
