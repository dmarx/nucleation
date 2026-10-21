---
status: Active
title: 'In Weatherall, O''Connor and Bruner''s network model a policy maker''s credence depends on the evidence it has received only through the total excess of successes over failures of the new action, so a propagandist''s effect is the excess of failures it adds; for the same pulls, running single-trial studies and publishing the failures adds at least as large an excess as any other division into studies, which is why biased production does best with the smallest studies'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmp8rwaa. The paper finds by simulation (its
    Fig. 7) that a propagandist with fixed resources does best with the
    smallest studies. The sufficient statistic and the pathwise
    domination are the record's, derived below step by step, which meets
    the condition for Active under ADR-047 v2.
tags:
- epistemology
- network-science
date: '2026-10-21'
source:
- LIT-tmpx95z2
summary: >-
  Weatherall, O'Connor and Bruner (2020; arXiv 2018), [LIT-tmpx95z2](../literature.d/LIT-tmpx95z2.md), read in
  [NOTE-tmp8rwaa](../notes.d/NOTE-tmp8rwaa.md). With two symmetric hypotheses, each result's likelihood
  ratio depends only on successes minus failures, so the audience's belief
  is a monotone function of the cumulative excess; whoever chooses what the
  audience sees chooses that number. It holds for the paper's two-point
  hypothesis space and naive updating, and says nothing about richer
  hypothesis spaces or audiences that model the selection.
---
<!-- inactive-ok-file: CLAIM-342 — Proposed; the anchor claim named in a connection, cited as open -->

# THEORY-tmpg79sv: In Weatherall, O'Connor and Bruner's network model a policy maker's credence depends on the evidence it has received only through the total excess of successes over failures of the new action, so a propagandist's effect is the excess of failures it adds; for the same pulls, running single-trial studies and publishing the failures adds at least as large an excess as any other division into studies, which is why biased production does best with the smallest studies

## Source

Weatherall, O'Connor and Bruner (2020), [LIT-tmpx95z2](../literature.d/LIT-tmpx95z2.md), read in full in
[NOTE-tmp8rwaa](../notes.d/NOTE-tmp8rwaa.md): §2's model, §4's biased production and Fig. 7, and Appendix
A's likelihood ratio ((1 − 2ε)/(1 + 2ε))^{2x−n}. The derivation is the
record's.

## What was actually shown

**The paper.** A propagandist with a fixed budget of pulls on action B
divides them into studies of size n, runs them honestly and publishes only
those with fewer than n/2 successes. "it is always better for them to break
their data up into the smallest possible chunks", shown by simulation for a
budget of 50 data points (Fig. 7).

**The sufficient statistic.** A policy maker weighs H: p_B = .5 + ε against
¬H: p_B = .5 − ε. A study with x successes in n trials has likelihood ratio
P(x | ¬H)/P(x | H) = ((.5 − ε)/(.5 + ε))^x ((.5 + ε)/(.5 − ε))^{n−x}
= ((1 − 2ε)/(1 + 2ε))^{2x−n}. Bayes' rule multiplies the odds on H by the
inverse of each ratio received, in any order, so after results
(x₁, n₁), …, (x_r, n_r) the odds are the prior odds times
((1 + 2ε)/(1 − 2ε))^D, with D = Σ(2xⱼ − nⱼ) = Σ(successes − failures). The
credence is increasing in D and depends on the evidence through D alone.
Policy makers influence no one, so the scientists' results, and their part
of D, are the same with or without a propagandist. The propagandist's effect
on a policy maker is therefore the (negative) contribution of what it
publishes to D.

**Single trials dominate, pathwise.** Fix the propagandist's pulls in a
round, with F failures among them, and any division into studies. A
published study s has x_s < n_s/2 and adds x_s − f_s < 0 to D, with f_s its
failures. The total added is
Σ_{published} (x_s − f_s) ≥ −Σ_{published} f_s ≥ −F.
With single-trial studies every failure (x = 0 < ½) is published and every
success (x = 1) is not, so the total added is exactly −F, the least possible.
For the same pulls, then, single-trial studies leave every policy maker's
credence at its lowest, round by round, and the paper's Fig. 7 is the
expectation of this ordering.

What could have failed: the order or grouping of results could have
mattered to the policy makers' posterior. With two symmetric hypotheses it
does not.

## What this does not say

- **Not for richer hypothesis spaces.** With a continuum of values of p_B,
  or asymmetric alternatives, a study's evidential weight is not a function
  of successes minus failures alone, and grouping can matter.
- **Not for an audience that models the selection.** A policy maker that
  knew only spurious studies are published would read a published
  single-trial failure as nearly uninformative.
- **Not a claim about cost or detectability.** The paper's remark that many
  small studies are cheap or hard to spot is outside the model.
- **Not about selective sharing's double counting.** There the propagandist
  forwards existing results, some of which a policy maker already holds; the
  statistic still governs, but the forwarded results are not the
  propagandist's own pulls.

## Connections

- **[THEORY-tmpnq01l](THEORY-tmpnq01l.md).** The same statistic explains why larger studies
  usually starve the selective-sharing propagandist: a spurious result
  needs a negative excess, which for p_B > .5 grows rarer with n except in
  the regime of very small ε where, as the paper's Appendix A notes,
  P(x < n/2) rises with n over the values it studied.
- **[CLAIM-342](../claims.d/CLAIM-342.md).** The audience's whole state is one number fed by two
  channels; evidence that does not pass through the propagandist is the
  only counterweight.
