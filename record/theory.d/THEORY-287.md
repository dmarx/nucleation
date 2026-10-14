---
number: 287
status: Proposed
formerly:
- THEORY-tmpuieof
promote_when: >-
  A replication on other model families and sizes, with shifts chosen
  without regard to whether they lower accuracy, and with significance
  tests, in which checking whether a test input still realizes the
  DAS-located variable predicts correctness better than output confidence
  and than probes of the variable's orthogonal complement. It is refuted
  if, under task-preserving shifts, probes of the complement or of
  locations chosen without causal analysis predict as well, once their
  location is controlled for. What cannot settle it: in-distribution
  results, where the paper's last-token probe and its causal-variable
  probe coincide.
title: "Internal variables located by interchange intervention as mediating a language model's in-distribution behaviour predict whether its outputs stay correct under shifts that keep the task's mechanism better than output confidence or probes of the rest of the representation"
version: 1
tags:
- causality
- representation-learning
date: '2026-10-14'
source:
- LIT-987
summary: >-
  Huang, Tao, Icard, Yang and Potts (2025), [LIT-987](../literature.d/LIT-987.md), read in
  [NOTE-765](../notes.d/NOTE-765.md). In Llama-3-8B-Instruct over five tasks and ten shifts,
  counterfactual simulation is best on 8 of 10; a probe of the located
  variable beats a probe of its orthogonal complement on 7 of 10.
  Interchange accuracy and predictive power rise together only until
  accuracy nears 1. It does not say that the located variables are
  constitutive, that causal features always win, or anything about shifts
  that change the mechanism.
---
<!-- inactive-ok-file: CLAIM-078 — Proposed; the success criterion this result parallels, open -->
<!-- inactive-ok-file: THEORY-282 THEORY-243 — Proposed; filed from the same dispute -->

# THEORY-287: Internal variables located by interchange intervention as mediating a language model's in-distribution behaviour predict whether its outputs stay correct under shifts that keep the task's mechanism better than output confidence or probes of the rest of the representation

## Source

Huang, Tao, Icard, Yang and Potts (2025), [LIT-987](../literature.d/LIT-987.md), read in [NOTE-765](../notes.d/NOTE-765.md):
§§4–6, Tables 2, 3 and 7, Figure 4, appendices A, B and D.

## What was actually shown

**Design.** For each task a high-level causal model is taken from prior
work, and DAS localizes its key variable V in the residual stream on
correct in-distribution examples. A test input's correctness is
predicted by transplanting its value of V into k verified examples and
scoring whether the output follows the high-level model (counterfactual
simulation), or by classifying the value of V (value probing). Baselines
are temperature-scaled output confidence and linear probes trained on
correctness labels, at the last prompt token or on B = V⊥. Shifts change
only conditions the task function ignores (Chinese names, a rephrased
template, a lira sign, typos, a distracting option, a longer passage) and
were selected for lowering accuracy. Balanced test sets, AUC-ROC, three
folds.

**Results.** Out of distribution, counterfactual simulation with output
mapping is best on 8 of 10 shifts, e.g. IOI with Chinese names 0.997
against 0.767 for the best confidence score, and PriceTag with a lira sign
0.856 against 0.631. The exceptions are a value-probing win on MMLU with
changed option symbols and a confidence win on UnlearnHP with a longer
passage. A probe of V beats a probe of B on 7 of 10. On RAVEL, as
accuracy falls from 89% to 72% across two-shot demonstrations,
confidence falls from 0.903 to 0.693 while counterfactual simulation
stays between 0.89 and 0.94 (Table 7). On IOI and RAVEL, AUC-ROC rises
with IIA until IIA nears 1; some early-layer representations with high
IIA predict poorly (Figure 4).

What could have come out otherwise: the background subspace, or
features chosen without causal analysis, could have predicted as well
under shift. On three shifts the background probe did.

## What this does not say

- **Not constitution.** The located variables are those that mediate the
  output under interchange intervention on in-distribution data. The
  paper makes no claim about what constitutes the behaviour.
- **Not "causal against merely correlated".** The comparison features
  are a correctness probe at heuristic locations and a probe of the
  complementary subspace. In distribution the last-token probe and the
  causal-variable probe give identical scores on four of five tasks.
- **Not that interventional fit is enough.** High IIA did not make a
  feature predictive in early layers.
- **Not uniform.** Three of ten shifts reverse the probe comparison,
  value probing is weak on several, and confidence wins one.
- **Not beyond one model and two shifts per task**, nor for shifts that
  alter the mechanism itself, which the design excludes.
- **Not checked against the illusion.** The located subspaces were not
  tested for the structure in [THEORY-282](THEORY-282.md). They are in the residual
  stream, where that structure was not found.

## Connections

- **[QUESTION-030](../questions.d/QUESTION-030.md)**, the empirical half: "which candidate relations
  predict responses to independently specified interventions". This is a
  measured case in a network. Variables identified by intervention as
  mediating keep predicting behaviour across changes the mechanism
  ignores, better than variables identified otherwise. Not marked
  `answers:`, since the relations are internal to a model, not relations
  of a communicative act.
- **[QUESTION-028](../questions.d/QUESTION-028.md).** An instance of intervention-relevant structure
  that generalizes across surface changes, which is one of that
  question's qualifiers. It says nothing on whether that makes a kind
  real.
- **[CLAIM-078](../claims.d/CLAIM-078.md).** The same form of success, a structural measure
  predicting what a surface measure misses, in another domain. Not
  evidence for the manuscript's measures.
- **[CLAIM-150](../claims.d/CLAIM-150.md).** Predictive success under intervention, with nothing
  inferred about constitution, as the claim requires.
- **[THEORY-282](THEORY-282.md)** and **[THEORY-243](THEORY-243.md).** The located variable is
  fixed by DAS within a basis and validated by IIA. The first account
  warns that interventional success alone can mislead; this paper's
  residual-stream placement is the one where that was not found. The
  second warns that equally good alignments can differ. A joint test
  would ask whether alignments tied on IIA predict equally well out of
  distribution; §6.3 suggests correctness prediction as a tie-breaker.
