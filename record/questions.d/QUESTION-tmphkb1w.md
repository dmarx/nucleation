---
status: Open
title: 'What do decreases of the local learning coefficient during training correspond to, in the model''s structure and in the singular-learning account of stages?'
version: 1
tags:
- learning-theory
- loss-landscapes
date: '2026-11-21'
line:
- learned-structure
summary: >-
  Raised by the reading of Hoogland and colleagues ([NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md),
  [THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)): three of their ten stages are decreases of the
  estimated local learning coefficient, which their motivating account
  does not produce and which they call an open problem. Neither reading of
  the owner's U23 ([CLAIM-834](../claims.d/CLAIM-834.md)) accounts for them. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpr9w2r CLAIM-834 CLAIM-823 CLAIM-802 CLAIM-812 — Proposed or new; the reading that raised the question and the claims it bears on -->

# QUESTION-tmphkb1w: What do decreases of the local learning coefficient during training correspond to, in the model's structure and in the singular-learning account of stages?

## Why it is open

Hoogland and colleagues ([THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)) divide transformer training into
stages at plateaus of the estimated local learning coefficient. In three
stages the estimate falls: LM3 (Δλ̂ = −1.57, previous-token heads), LR3
(−12.3) and LR4 (−44.1, loss of out-of-distribution robustness with
layer-norm collapse). "The LLC decreases during LM3, suggesting an
increase in degeneracy" (§6.3); for LR3–LR4, "we conjecture that this
explains part of the striking decrease in estimated LLC over these stages"
(§7.3). Their account of transitions does not produce them: the singular
learning process's example transitions "describe LLC increases", and
"providing a full theoretical account of these stages is an open problem"
(§8). Wang et al. read decreases as a kind of stage too ([NOTE-1188](../notes.d/NOTE-1188.md), C6).

The owner's U23 ([CLAIM-834](../claims.d/CLAIM-834.md)) has two readings. Reading (b) ([CLAIM-823](../claims.d/CLAIM-823.md))
makes a transition a crossover to a richer, higher-coefficient region;
it produces increases. Reading (a) ([CLAIM-802](../claims.d/CLAIM-802.md)), resolution as something
training does, says nothing about the coefficient's direction. Neither
accounts for the decreases.

## Candidate answers

- **More degeneracy at equal loss.** A decrease at constant loss also
  lowers the free energy nL + λ log n (§8), so a move to a more degenerate
  region of equal fit is a transition of the same competition. The paper
  names it and does not develop it.
- **Collapse mechanisms.** Layer-norm, unembedding, embedding and
  attention collapse create degeneracy (D.2), conjectured to explain part
  of LR3–LR4.
- **An estimator effect.** At the paper's fixed nβ and γ a direction
  counts in the estimate only above a curvature cut-off ([CLAIM-812](../claims.d/CLAIM-812.md)); a
  direction flattening below it lowers λ̂ without any change of stratum.
  Estimates are also taken away from minima (A.7).

## What would count as an answer

For at least one documented decrease, a structural change that is shown
to create the degeneracy (by computing the coefficient of the collapsed
configuration, or by an intervention that removes the collapse and the
decrease together), with the decrease surviving a variation of nβ and γ
([LEAD-207](../leads.d/LEAD-207.md)).
