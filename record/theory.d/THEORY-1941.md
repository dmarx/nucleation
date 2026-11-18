---
number: 1941
status: Proposed
formerly:
- THEORY-tmppelva
title: 'Cerrato, Sahlgren and Heilmann find that, in a simulated hiring screen, an organization''s upstream choices of label, feature measurement and model-selection metric change the counterfactual explanations given to rejected candidates more than the explanation method''s own validity threshold does, and argue that counterfactual explanations used as justification or recourse therefore bracket the decision-maker''s contestable choices and put the burden of a better outcome on the subject'
version: 1
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
---

# THEORY-1941: Cerrato, Sahlgren and Heilmann find that, in a simulated hiring screen, an organization's upstream choices of label, feature measurement and model-selection metric change the counterfactual explanations given to rejected candidates more than the explanation method's own validity threshold does, and argue that counterfactual explanations used as justification or recourse therefore bracket the decision-maker's contestable choices and put the burden of a better outcome on the subject

## Source

[LIT-2713](../literature.d/LIT-2713.md), read in arXiv 2608.30956v1.

## What was actually shown

On American Community Survey data, with a screening label top 10% of earners under a salary cap, the authors vary four upstream parameters of a structural causal model of the pipeline (salary cap, definition of private-sector worker, model-selection metric, validation strategy) and measure how far the counterfactual sets of DiCE-kdtree and NICE move, against the movement caused by varying the CE method's validity threshold τ. "Three of the four interventions move both methods clearly" beyond the τ band; validation strategy moves them comparably. Agreement between explanations also falls under upstream interventions (Fig. 3). The normative argument, that CEs as justification or recourse assume a fixed model and so foreclose the question whether the decider "ought to have acted differently", is argued, not tested.

## What this does not say

- That CEs are defective as such: "we do not report this result intending to demonstrate a limitation of CEs per se".
- That organizations use CEs to shirk responsibility: that is offered as a risk, with a stylized example.
- Anything beyond one simulated task, two retrieval-based methods and random forests.
