---
number: 144
status: Active
formerly:
- CASE-tmp4ozxp
title: 'The evaluator that stops tracking: two populations of specialists with identical capabilities and task streams, one scored against independent outcomes and one by an evaluator that weights evidence agreeing with its previously favoured specialists, after a shift that makes a marginalized specialist uniquely competent'
version: 2
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: A47 ran the design with a router arm, filed as the
    variant CASE-158. The case is unchanged.
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
variants:
- CASE-158
---

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
failure is recognized; and, against [CLAIM-427](../claims.d/CLAIM-427.md)'s third grade, the
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
  problem. A result counts for the framework only at [CLAIM-427](../claims.d/CLAIM-427.md)'s
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
