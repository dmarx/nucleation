---
number: 1941
status: Proposed
formerly:
- THEORY-tmppelva
title: 'Cerrato, Sahlgren and Heilmann find that, in a simulated hiring screen, an organization''s upstream choices of label, feature measurement and model-selection metric change the counterfactual explanations given to rejected candidates more than the explanation method''s own validity threshold does, and argue that counterfactual explanations used as justification or recourse therefore bracket the decision-maker''s contestable choices and put the burden of a better outcome on the subject'
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Reconciled on 2026-11-18 with THEORY-tmpu63nn, the account the
    continuation of the exchange's readings filed from its second
    reading of the same work (NOTE-1996). It stated the same account and
    was never merged, so it was folded in here and removed. Relations
    carried over: corroborates CLAIM-tmpohafo. Its title was:
    "Counterfactual explanations used to justify a decision or to offer
    recourse are partly artifacts of the deployer's upstream choices of
    labels, measures, selection metrics and validation, which shift them
    as much as or more than the explanation method does, so on their own
    they cannot show that a decision was justified or what its subject
    should change, and they bracket whether the decision-maker should
    have acted otherwise"
tags:
- society-and-governance
- philosophy-of-technology
- anthology-candidate
promote_when: >-
  the paper's experiments are reproduced, or a second study shows on
  another task or with other counterfactual methods that upstream design
  choices move counterfactual explanations at least as much as the
  method's own tuning
source:
- LIT-2713
corroborates:
- CLAIM-tmpohafo
---
<!-- inactive-ok-file: CLAIM-tmpohafo — Proposed or Unfetched; entries the second reading bears on, cited with their standing -->
<!-- unresolved-ok-file: THEORY-tmpu63nn — removed at the reconciliation of 2026-11-18; named for provenance -->

# THEORY-1941: Cerrato, Sahlgren and Heilmann find that, in a simulated hiring screen, an organization's upstream choices of label, feature measurement and model-selection metric change the counterfactual explanations given to rejected candidates more than the explanation method's own validity threshold does, and argue that counterfactual explanations used as justification or recourse therefore bracket the decision-maker's contestable choices and put the burden of a better outcome on the subject

## Source

[LIT-2713](../literature.d/LIT-2713.md), read in arXiv 2608.30956v1.

## What was actually shown

On American Community Survey data, with a screening label top 10% of earners under a salary cap, the authors vary four upstream parameters of a structural causal model of the pipeline (salary cap, definition of private-sector worker, model-selection metric, validation strategy) and measure how far the counterfactual sets of DiCE-kdtree and NICE move, against the movement caused by varying the CE method's validity threshold τ. "Three of the four interventions move both methods clearly" beyond the τ band; validation strategy moves them comparably. Agreement between explanations also falls under upstream interventions (Fig. 3). The normative argument, that CEs as justification or recourse assume a fixed model and so foreclose the question whether the decider "ought to have acted differently", is argued, not tested.

## What this does not say

- That CEs are defective as such: "we do not report this result intending to demonstrate a limitation of CEs per se".
- That organizations use CEs to shirk responsibility: that is offered as a risk, with a stylized example.
- Anything beyond one simulated task, two retrieval-based methods and random forests.

## From the second reading (2026-11-17)

The second reading adds a relation: it corroborates [CLAIM-tmpohafo](../claims.d/CLAIM-tmpohafo.md)'s
split of explanation from contestation, which does not rest on it ("it may
be impossible for subjects to reverse their decisions through contesting
such choices absent appropriate transparency"). It does not touch the
claim's interruption entitlement. It adds that some numbers in the text do
not agree with each other (the count of interventions, a $40k against a
$60k cap).
