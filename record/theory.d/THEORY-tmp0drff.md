---
status: Proposed
promote_when: >-
  An experiment in bacteria, read first-hand, in which a gene is perturbed
  transiently (for example by inducible CRISPR interference, then
  released) with the growth environment held fixed, and other genes stay
  in their changed expression state for many generations after the
  perturbation is gone, with slow return excluded: either by following the
  culture until the state has outlasted any plausible relaxation time, or
  by showing that unperturbed cells started from the other state hold it
  under the same conditions. Refuted for the network if well-powered
  transient perturbations of the predicted genes (crp, with zraR, melR or
  rhaRS as responders) are always followed by a return to the starting
  state. What would not settle it: further simulations or rule ensembles;
  agreement with strains evolved under a permanent knockout, which is not
  a temporary disturbance; and environmentally induced bistable switches
  such as the lac operon, which were known before and are not
  perturbations of regulation alone.
title: 'Transcriptional regulation alone can give a bacterium''s gene expression a memory: in E. coli, a transient knockdown or overexpression of one regulator, with the environment held fixed, can leave other genes in a different self-maintaining expression state after it is released, as Zhao, Wytock, Reynolds and Motter predict from a Boolean-network model of its regulatory core'
version: 1
tags:
- complex-systems
- network-science
- natural-sciences
date: '2026-10-20'
source:
- LIT-854
summary: >-
  Zhao, Wytock, Reynolds and Motter (2024), [LIT-854](../literature.d/LIT-854.md), read in full in
  [NOTE-655](../notes.d/NOTE-655.md). Their abstract and discussion carry the model result to cells:
  one genotype may hold several heritable expression states without
  epigenetic marks, and history picks among them. They predict that a
  transient crp knockdown leaves zraR, melR or rhaRS changed ([NOTE-655](../notes.d/NOTE-655.md),
  C8, untested). [THEORY-178](THEORY-178.md) is the model result this rests on. No such
  perturbation has been done in cells ([QUESTION-172](../questions.d/QUESTION-172.md)).
extends:
- THEORY-178
answers:
- QUESTION-172
---

# THEORY-tmp0drff: Transcriptional regulation alone can give a bacterium's gene expression a memory: in E. coli, a transient knockdown or overexpression of one regulator, with the environment held fixed, can leave other genes in a different self-maintaining expression state after it is released, as Zhao, Wytock, Reynolds and Motter predict from a Boolean-network model of its regulatory core

## Source

Zhao, Wytock, Reynolds and Motter (2024), [LIT-854](../literature.d/LIT-854.md), read in full in [NOTE-655](../notes.d/NOTE-655.md),
with the Supplementary Text. The thesis is the paper's own reading of its
model result, stated in its abstract and discussion; its concrete
prediction is that a transient crp knockdown leaves zraR, melR or rhaRS in
a changed state ([NOTE-655](../notes.d/NOTE-655.md), C8).

## What is asserted

That regulation by transcription factors, with no epigenetic marking and no
change of environment, is enough for a bacterium's expression state to
remember a past disturbance: a temporary change to one regulator flips a
self-maintaining part of the network, which then holds the new state after
the cause is gone. Genotype would then fix a set of possible expression
states, and history would choose among them.

## What the Active account establishes toward it

[THEORY-178](THEORY-178.md) holds what was shown: in an ensemble of sign-consistent Boolean
rules on the 87-gene core, many single genes admit a transient knockout or
overexpression after which the network settles in a different attractor,
and every such gene reaches a strongly connected component with a positive
circuit. That is a model ensemble. The weak support from adaptive
evolution under a permanent crp knockout ([NOTE-655](../notes.d/NOTE-655.md), C7) is not a transient
perturbation.

## What would confirm or reject it

The promote_when above. The authors' own caveat, that noise in cells can
turn a permanent state into a long-lived one, is the slow-return confound
it asks to exclude ([THEORY-136](THEORY-136.md)). The positive-circuit condition is not
part of this thesis: as a general law of synchronous Boolean networks it
fails ([THEORY-178](THEORY-178.md), note of 2026-10-19).

## Provenance

Filed on 2026-10-20 by the narrowing-loss sweep ([ADR-047](../decisions.d/ADR-047.md) v4, batch 068),
from the wider title [THEORY-178](THEORY-178.md) carried before it was narrowed on
2026-10-19.
