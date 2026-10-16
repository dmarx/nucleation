---
status: Proposed
promote_when: >-
  A worked model of an evolutionary transition in individuality, such as
  ecological scaffolding or a Hammerschmidt-type life cycle, in which one
  stated objective, prediction error plus an explicit measurement and
  computation cost, is computed over candidate partitions and picks out
  the collectives, with the selected grain shifting as the transition
  proceeds. It is refuted if the collectives a biologist would name are
  not selected under any reasonable cost, or if the stage-5 collective
  fitness parameter is introduced where the particle-level map is cheap
  and known. A minimal prediction error alone cannot settle it, since the
  finest partition always minimises that, and neither can more toy
  arithmetic of operation counts.
title: "The individuals that appear in an evolutionary transition in individuality are a summary description of lower-level processes, not a new level of fact: a partition of particles defines collectives when predicting at the coarse grain matches predicting at the fine grain across many traits, and collectives become indispensable, and so quasi-ontological, only because finite measurement and computation make the fine-grained prediction unaffordable"
version: 1
tags:
- complex-systems
- individuation
- philosophy-of-biology
date: '2026-10-16'
source:
- LIT-049
rivals:
- THEORY-141
summary: >-
  Bourrat (2023), [LIT-049](../literature.d/LIT-049.md), read in full in [NOTE-064](../notes.d/NOTE-064.md). The formal criterion
  is accuracy only: δC = C_T − C_P < θ across many traits, conditioned on
  the environment where ecology could fake coherence. As written it is
  degenerate, since the identity partition gives δC = 0. The cost that is
  meant to stop that is argued separately, by a 100-operation toy, and
  never put into the criterion. Nothing is computed on any model. The
  abstract's "cannot be dismissed as merely epistemic" is stronger than
  the body, which says one "pretend[s] as if" the level of selection
  changed.
---
<!-- inactive-ok-file: LIT-049 LIT-005 — Proposed; LIT-049 is the source this account was read from, and its NOTE places it; LIT-005 is named as its successor -->
<!-- inactive-ok-file: THEORY-141 THEORY-222 THEORY-257 THEORY-tmp2hovt THEORY-tmp8fvy7 — Proposed; a rival and neighbouring accounts named for comparison, nothing here rests on their being settled -->

# THEORY-tmppkom6: The individuals that appear in an evolutionary transition in individuality are a summary description of lower-level processes, not a new level of fact: a partition of particles defines collectives when predicting at the coarse grain matches predicting at the fine grain across many traits, and collectives become indispensable, and so quasi-ontological, only because finite measurement and computation make the fine-grained prediction unaffordable

## Source

Bourrat (2023), [LIT-049](../literature.d/LIT-049.md), *Biology & Philosophy* 38:33, read in full in
[NOTE-064](../notes.d/NOTE-064.md).

## What was actually shown

**The criterion (Eqs. 1–2, pp. 11–14).** Take a partition of particles
into collectives and compare two routes to the coarse state at t2: the
truthful one (evolve the fine state, then coarse-grain) and the projected
one (coarse-grain at t1 by averaging, then evolve). Their difference is
δC = C_T − C_P. A partition is acceptable if δC < θ, and the minimal one
below θ, δ*C, is "the best candidate for defining a level of
individuality" (p. 12). It must hold for the same partition across many
traits (p. 13). Where low error could come from ecology alone, as when
cells align by chemotaxis toward resources, the test is δC|E, required to
stay below θ in every environmental state (p. 14).

**The pragmatic argument (pp. 15–17).** "There is nothing that exists at
the higher level that could not be described or predicted, in principle,
for the lower level" (p. 15). But with one operation per entity per step,
100 operations predict 10 entities for 10 steps or 2 collectives for 50
(p. 16). Beyond some horizon the coarse description is the only one
available, and the paper takes that indispensability as "sufficient to
see them as having an ontology" (pp. 16–17).

**The reading of Godfrey-Smith & Kerr (pp. 18–20).** At their fifth stage
a collective fitness parameter appears with no map to particle fitness.
Bourrat reads that as forced by the map being "fundamentally unknown",
not measured or too costly, and concludes that "there is no factual
change of the level at which selection occurs during an ETI … for
pragmatic reasons, it becomes useful to pretend as if this were the
case" (p. 19).

**What could have come out otherwise.** Nothing here could. There is no
model, simulation or data. The only numbers are a mis-averaged angle toy
and the operation count. The account is argued, not tested.

## What this does not say

- **That minimal prediction error finds collectives.** It finds the
  finest partition: if every particle is its own collective, C_P = C_T
  and δC = 0. Fn. 12 concedes zero error without within-group variation.
  The cost term that would prevent this is never part of the criterion.
  δC is also signed, so "δC < θ" accepts any negative error.
- **That conditioning on the environment removes the ecological case.**
  In the paper's own chemotaxis example, cells are coherent given each
  fixed resource state. What would exclude it is variation across
  environments, which makes δC|E an invariance test, not a conditioning
  one ([NOTE-064](../notes.d/NOTE-064.md), C6).
- **That the criterion can be applied where it matters.** It needs C_T,
  a full fine-grained prediction, and the pragmatic argument's case is
  exactly where that is unaffordable.
- **That collectives are more than epistemic tools.** The abstract says
  the change of parameters "cannot be dismissed as merely epistemic". The
  body's ground is still pragmatic indispensability under resource
  limits, and the Conclusion calls individuals "ultimately epistemic
  tools" (p. 20).
- **That the stage-5 map is in fact unknown in real transitions.** No case
  is examined (C10).

## Connections

- **Rival: [THEORY-141](THEORY-141.md).** Okasha, with Buss and Michod, holds that in a
  major transition selection between collectives comes to trump
  selection within them, so the levels at which selection acts are a
  product of evolution. Bourrat holds there is no factual change of level,
  only a change in what can be afforded as description, and cites his own
  work against Okasha's fitness-decoupling account (C1). Both cannot be
  right about whether the level of selection changes.
- **The later paper ([LIT-005](../literature.d/LIT-005.md); [THEORY-tmp343c3](THEORY-tmp343c3.md)).** Bourrat's δC|E is the
  observational, stratify-on-E ancestor of the conditional measure that
  [LIT-005](../literature.d/LIT-005.md) wrongly equates with the interventional one. Both papers leave
  scale selection open: here minimal δC prefers parts, there Â cannot tell
  an individual from a part of one.
- **Coarse-graining accounts of emergence.** δC = 0 is the commuting-diagram
  condition, exact lumpability. Dynamical independence ([THEORY-257](THEORY-257.md)) and
  effective information ([THEORY-222](THEORY-222.md)) are criteria that do write down an
  objective, which is what this account lacks.
- **Collective individuality by organisation ([THEORY-tmp2hovt](THEORY-tmp2hovt.md)).**
  Griesemer and Shavit put the new level in entrenched interactions and
  organisational closure, a fact about the collective. Bourrat's is a fact
  about the observer's budget. The two may pick the same collectives, so
  no `rivals` edge is declared.
- **Reproducers ([THEORY-tmp8fvy7](THEORY-tmp8fvy7.md))**, Bourrat's 2025 framework, inherits the
  no-worked-example habit both papers show.
