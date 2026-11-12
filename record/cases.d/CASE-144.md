---
number: 144
status: Active
formerly:
- CASE-tmp4ozxp
title: 'The evaluator that stops tracking: two populations of specialists with identical capabilities and task streams, one scored against independent outcomes and one by an evaluator that weights evidence agreeing with its previously favoured specialists, after a shift that makes a marginalized specialist uniquely competent'
version: 5
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: A47 ran the design with a router arm, filed as the
    variant CASE-158. The case is unchanged.
- version: 3
  date: '2026-11-11'
  note: >-
    The third grade cited as CLAIM-427's is now cited as ARG-025's:
    CLAIM-427 is Superseded by ARG-025, which holds the grading.
    Reported by the synthesis review of 2026-11-11 (seventh round).
    No other change.
- version: 4
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-264 (ADR-092), from the reading review of
    2026-11-11, by question. The question names it: "CASE-144 is a
    proposed test." Its central question, when an organization
    "become[s] unable to recognize or act upon evidence that its own
    organization of interpretation and authority has rendered
    inconsequential", is a case of the three organizations diverging.
    No other change.
- version: 5
  date: '2026-11-12'
  note: >-
    Draws on THEORY-142 ("the comparator for this study is March's
    model"). First application of draws_on (ADR-095). No other
    change.
standing: stipulated
kind: proposed-study
tags:
- complex-systems
- self-governance
- learning-theory
date: '2026-10-23'
line: distributed-agency
works:
- organization-of-perspective
summary: >-
  Proposed in the exchange of 2026-10-23, "Framework Overview Request",
  at A5 (section 5) with A4's "corrigibility trap", after the owner asked
  which experiments could "kill multiple birds with one stone" (U4) and
  which questions simulation could answer (U5). One design bears on
  [CASE-092](CASE-092.md), [CASE-108](CASE-108.md) and [CASE-117](CASE-117.md) at once, and separates four causes of a
  failure to adapt. A5's central question: "Under what conditions does an
  organization become unable to recognize or act upon evidence that its
  own organization of interpretation and authority has rendered
  inconsequential?" Not run.
bears_on:
- QUESTION-264
draws_on:
- THEORY-142
- THEORY-1784
- THEORY-1738
- THEORY-1801
---
<!-- inactive-ok-file: ADR-095 THEORY-142 — Proposed; the decision this entry's draws_on first applies and the readings it draws on, cited as open; nothing here rests on their being settled -->
<!-- inactive-ok-file: ARG-025 — Proposed; the argument that holds the grades of evidence CLAIM-427 set out, cited for the grading -->
<!-- inactive-ok-file: THEORY-1738 THEORY-1743 THEORY-1772 THEORY-1784 THEORY-1801 THEORY-1805 THEORY-1808 THEORY-1812 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# CASE-144: The evaluator that stops tracking: two populations of specialists with identical capabilities and task streams, one scored against independent outcomes and one by an evaluator that weights evidence agreeing with its previously favoured specialists, after a shift that makes a marginalized specialist uniquely competent

## The design

Two populations of adaptive specialists with the same capabilities face
the same task stream, which has independently defined outcomes. In one,
the evaluator scores specialists against those outcomes. In the other, it
gives more weight to evidence consistent with the specialists it already
favours: the coupled scoring of [CASE-092](CASE-092.md)'s Regime A, where [CASE-099](CASE-099.md) and
[CLAIM-330](../claims.d/CLAIM-330.md) found the symmetric state can be unstable. At first both may
perform alike. Then the task distribution shifts so that a specialist the
organization has marginalized becomes the only competent one.

A5's four conditions for the marginalized specialist:

1. It keeps its competence but has little authority.
2. It keeps competence and has a protected channel to challenge the
   evaluation.
3. It has lost competence for want of learning opportunities.
4. The organization can recognize and revise its evaluator's standard.

A4's "corrigibility trap" is the long version: an evaluation rule that
works well for a long period and then becomes systematically misleading,
where accepting the corrective evidence "would undermine the authority
structure responsible for deciding what counts as credible". Randomize
whether corrective evidence is independently scored, whether minorities
have protected routes to challenge, and whether the evaluator's own rules
can be revised.

## What is measured

Held-out performance across the shift; concentration of interpretation
and of authority; survival and recovery of the minority specialist;
hysteresis after a temporary perturbation; whether the evaluator's
failure is recognized; and, against [ARG-025](../arguments.d/ARG-025.md)'s third grade (from [CLAIM-427](../claims.d/CLAIM-427.md)), the
interventional prediction error of competing models (mixture-of-experts
routing, reflected-appraisal influence, a conventional adaptive policy).

## What the outcomes would show, and what they would not

- **Four causes of one failure.** A5: the design separates "The right
  information wasn't available", "The right information was available but
  ignored", "The specialist once had the right information but lost its
  competence", and "The organization recognized the problem but could not
  revise the governing mechanism". Those are [CLAIM-421](../claims.d/CLAIM-421.md)'s activation,
  enactment and reproduction, and [CLAIM-424](../claims.d/CLAIM-424.md)'s reflexive governance, in
  one experiment.
- **A clean negative case.** A4: "an organization that is excellent at
  optimizing within its current perspective yet persistently fails to
  reconsider the perspective itself."
- **Not novelty by itself.** A4: there is "extensive antecedent work in
  organizational learning and robust distributed systems"; hidden-profile
  research ([QUESTION-089](../questions.d/QUESTION-089.md)) and Byzantine-robust learning already show the
  problem. A result counts for the framework only at [ARG-025](../arguments.d/ARG-025.md)'s
  third grade.

## Note of 2026-10-24: March as the baseline

From the exchange of 2026-10-24 (workbench entry of 2026-10-24, U21–U22).
Rather than a fixed-weight learner, the comparator for this study is
March's model of mutual learning between an organizational code and its
members ([THEORY-142](../theory.d/THEORY-142.md)). In March, rapid socialization can remove the
independent views from which the code might learn, and an environmental
change then exposes it. The extension that would test [CASE-124](CASE-124.md)'s legibility
state keeps the members explicit and lets their scores depend on the
prevailing regime, s_i = S_r(h_i, c, observations), with standing feeding
back into r. The informative outcome is the one March's baseline lacks:
independent views stay present and accurate, and the organization still
fails to credit them. Controls: the same evaluation bias without a
separate r memory, and history-dependent retrieval with no explicit
legibility coordinate, so that the extra state is not rewarded merely for
being there.

## Note of 2026-10-25: run without citation, with a router added

A47 of the exchange of 2026-10-24, continued, reported running this
design without citing it. The specialists were frozen low-rank denoisers,
the required specialist reversed at mid-run, and scoring was either
against independent held-out probes or by agreement with the collective
proposal. A contextual mixture-of-experts router was added. Reported over
12 seeds: audited governance beat fixed and conformity-scored allocation
every time, and the router beat audited governance every time. Not held
and not reproduced. The variant with the router arm, and the arms that
would make it informative, is [CASE-158](CASE-158.md). The case is unchanged.

## Note of 2026-11-12: 8 readings of the works of "luria experiment design"

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Chen, Zhu and Zheng** ([THEORY-1784](../theory.d/THEORY-1784.md)): The criterion-drift remark and the requirement of "a fixed external reference that gates each change of evaluator" bear directly; it gives no answer for open-ended tasks where no reference grader exists, which is [QUESTION-271](../questions.d/QUESTION-271.md)'s hard case. Qualifies.
- **Thaman** ([THEORY-1738](../theory.d/THEORY-1738.md)): RHB's tampering category is the behavioural form of [QUESTION-271](../questions.d/QUESTION-271.md)'s "processes in charge can add, filter or duplicate the tests". Supports the question's premise; no answer.
- **Huang, Xu, Ma et al.** ([THEORY-1801](../theory.d/THEORY-1801.md)): **supports** as an empirical instance of an evaluator that the evaluated can shape; E3 shows feedback from the evaluator helps the evaluated defeat it.
- **Ghareeb et al.** ([THEORY-1805](../theory.d/THEORY-1805.md)): **leaves open, relevant design point**: Robin's selection among hypotheses is by an LLM judge reading LLM-written reports, the self-evaluation configuration those entries worry about; the paper reports no test of the judge against independent outcomes, only that a human then reviewed the list.
- **Lu et al.** ([THEORY-1772](../theory.d/THEORY-1772.md)): Bears as an example. The authors validate the judge against human decisions once, then rely on it.
- **Majumder et al.** ([THEORY-1812](../theory.d/THEORY-1812.md)): The benchmark's evaluation is an LLM judge; the paper does not test its agreement with humans in the main text. Leaves open.
- **Zhang, Hu, Lu, Lange and Clune** ([THEORY-1743](../theory.d/THEORY-1743.md)): *illustrates* the mechanical version (the evaluated process edits the evaluator's input), not the social one of CASE-144.
- **Stasser and Titus** ([THEORY-1808](../theory.d/THEORY-1808.md)): [QUESTION-089](../questions.d/QUESTION-089.md) and CASE-144 cite hidden profiles; CASE-144 (an evaluator that weights agreeing evidence) shares the preference-consistent sampling mechanism.

The case is unchanged.
