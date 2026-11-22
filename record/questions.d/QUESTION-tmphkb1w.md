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
<!-- inactive-ok-file: THEORY-tmpm3ux2 THEORY-tmpu0f9k LIT-tmpnwcsg — Proposed or Deferred; the readings of Lee et al. and of Yang filed 2026-11-22, and Carroll et al., registered from the first and unread -->

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

## Note of 2026-11-22: Lee, Smith, Adam and Hoogland, read

Adds a name and two sources to the first candidate; leaves the question
open. Lee et al.'s Appendix A.2 ([THEORY-tmpm3ux2](../theory.d/THEORY-tmpm3ux2.md), [NOTE-tmp1sot8](../notes.d/NOTE-tmp1sot8.md)): "if
the two phases agree on the linear term (they have the same minimum
loss), then the trade-off will be pushed down into lower-order terms,
and there can be a 'Type-B' transition, in which complexity (as measured
by the LLC) decreases, in exchange for an increase in lower-order
terms." That is the candidate "more degeneracy at equal loss", with one
difference: the paper puts the trade against the lower-order terms of
the free energy (log log n and beyond), since within nL + λ log n alone
the lower-λ phase wins at every n when the losses are equal, and a
transition in n needs a lower-order term pulling the other way. It cites Carroll, Hoogland,
Farrugia-Roberts and Murfet 2025 ([LIT-tmpnwcsg](../literature.d/LIT-tmpnwcsg.md), registered from this
reading and unread) and Hoogland et al. 2025, the TMLR version of the
work that raised this question ([LIT-2966](../literature.d/LIT-2966.md)). The paper measures no LLC
over training, so it explains no observed decrease. Carroll et al. is
the next reading for this candidate.

## Note of 2026-11-22: Yang, read

Leaves it open. Yang's probe pitchfork ([THEORY-tmpu0f9k](../theory.d/THEORY-tmpu0f9k.md)) says nothing of
learning coefficients. Its reverse traversal, which merges the branches
back as β falls, ends in a nondegenerate minimum, so it offers no route
to a decrease; its collapse diagnostics are representational collapse
in DINO, not the layer-norm collapse of the second candidate. No edge.
