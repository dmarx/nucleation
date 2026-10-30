---
number: 1050
status: Active
formerly:
- THEORY-tmpmjn0i
title: 'In Athreya, Czuppon and Gokhale''s adaptive-dynamics model of an incipient endosymbiosis, mutual dependence (the product of the partners'' obligacies) evolves ahead of reproductive cohesion (the product of their adhesions) early on, but only under the mapping in which each partner''s free-living growth depends on its own obligacy alone while dissociation depends on both partners'' adhesions; the authors'' own appendix shows the bias vanishing under matched mappings and reversing under the opposite one, and their survey of real symbioses cannot test it'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1211, the reading in full of the bioRxiv
    version 2 of Athreya, Czuppon & Gokhale (2025). The result is a model
    result, shown by simulation for early trajectories of the exponential
    model, and its direction is set by a structural assumption the
    authors chose "from biological considerations". The authors say their
    table of real symbioses "does not allow us to confirm/refute" it.
    Hence Proposed.
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-fourth status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    reports Athreya, Czuppon and Gokhale's model result with their own
    appendix's dependence on the mapping and their own concession that
    the survey cannot test it, read in full in NOTE-1211 from bioRxiv
    v2; no discrepancy with the version of record is named. Nothing in
    the record contradicts it. What the condition asked beyond the
    title, evidence from real symbioses, moves to THEORY-tmpsudhw,
    Proposed, which extends this entry and keeps the condition word for
    word (ADR-065 §3). The answers edge on QUESTION-277 is moved to
    bears_on (ADR-060). The old promote_when: "Evidence on which way the
    traits of a real incipient endosymbiosis enter its dynamics: whether
    a partner's free-living growth falls with its own investment in the
    partnership only, or with both partners', and whether the stability
    of the association (loss of the symbiont, failed transmission) needs
    both partners' adaptations or one's. That evidence must come from
    experiments or comparative data, not the model, and it must be
    paired with measured trajectories showing dependence ahead of
    co-transmission in a young symbiosis. Further simulations under the
    same mapping, or more qualitative tables of dependence and
    transmission mode, cannot settle it. It is refuted for a system if
    its free growth depends on both partners' obligacy and its
    dissociation on one partner's adhesion (the mapping that reverses
    the bias), or if young symbioses are found co-transmitted before
    they are mutually dependent."
tags:
- endosymbiosis
- individuation
date: '2026-10-27'
source:
- LIT-1570
bears_on:
- QUESTION-277
summary: >-
  Athreya, Czuppon & Gokhale (2025), [LIT-1570](../literature.d/LIT-1570.md), read in [NOTE-1211](../notes.d/NOTE-1211.md). In
  the exponential version of the model, all four traits rise
  monotonically. Each partner becomes more obligate than adhesive,
  because a gain in adhesion is "damped by the other adhesion" in the
  dissociation rate. Table S1 shows this is a consequence of that
  mapping: matched mappings give no bias, and the opposite mapping biases
  trajectories towards cohesion. The record's summary of the result,
  "even when investments are uncorrelated", is true of the traits' genetic
  correlation but not of their functional coupling, which is what decides
  it.
---
<!-- inactive-ok-file: THEORY-tmpsudhw — Proposed; filed beside this reading by the twenty-fourth status review: the inference the authors draw for nature -->
<!-- inactive-ok-file: QUESTION-277 LIT-1605 — Open or Deferred; the question this bears on, and an unread model of host control set beside it -->
# THEORY-1050: In Athreya, Czuppon and Gokhale's adaptive-dynamics model of an incipient endosymbiosis, mutual dependence (the product of the partners' obligacies) evolves ahead of reproductive cohesion (the product of their adhesions) early on, but only under the mapping in which each partner's free-living growth depends on its own obligacy alone while dissociation depends on both partners' adhesions; the authors' own appendix shows the bias vanishing under matched mappings and reversing under the opposite one, and their survey of real symbioses cannot test it

## Source

Athreya, Czuppon & Gokhale (2025), *The American Naturalist* 206(5):
435–451, [LIT-1570](../literature.d/LIT-1570.md), read in full in [NOTE-1211](../notes.d/NOTE-1211.md) from the bioRxiv
version 2 (2025-05-31), not the version of record. The section "Does
mutual dependence evolve before or after reproductive cohesion?", Figure
5, Supplementary Note S4.B–E, Table S1, Figures S11–S14, and Table 3
with its caption.

## What was actually shown

- **Model.** Free-living growth is f_H = r_H(1 − Ω_H) and
  f_S = r_S(1 − Ω_S). Collective growth is f_C = r_C Ω_HΩ_Sα_Hα_S, and
  dissociation d = d₀(1 − α_Hα_S). The collective grows without a
  carrying capacity (the "exponential model"), which is valid while the
  traits are small.
- **Analytically.** The invasion criterion is exact and separable:
  f̃(1 − d̃/(a f̃_C)) > f(1 − d/(a f_C)). There is an optimization
  principle, no branching, and all four traits rise monotonically.
- **By simulation (Figure 5).** Both partners evolve Ωᵢ > αᵢ, and Ω_HΩ_S
  outruns α_Hα_S until the feasibility bound ends the trajectories.
  Figure S14 shows the bias persists with additive trait effects,
  symmetric or tenfold-asymmetric growth parameters, and higher d₀.
- **The structural dependence (Note S4.E, Table S1).** The appendix
  crosses two choices: free growth depending on (i) one's own obligacy
  or (ii) both obligacies, and dissociation depending on (I) one
  adhesion or (II) both.
  - i-II, the default: dependence-biased.
  - ii-I: cohesion-biased.
  - i-I and ii-II: no bias, the slight bias in i-I being "an artefact".

  The authors chose i-II "from biological considerations".
- **Against data (Table 3).** Ten symbioses are classified qualitatively
  by dependence and transmission mode. The authors: "the available
  information does not allow us to confirm/refute the bias".

What could have failed: under the default mapping, the simulations could
have shown no bias. They do not. Under the alternative mapping, the
result fails, as the authors report.

## What this does not say

- **Not that endosymbioses in nature are dependence-first.** The authors
  draw that inference ("strongly suggests"), but it is conditional on the
  mapping and untested.
- **Not about uncorrelated investment in a sense that decides the
  result.** The traits have no genetic correlation in the model, but
  their functional effects are coupled by the mapping. That coupling is
  what produces the bias.
- **Not about late evolution.** The exponential model is trusted only
  early, and whether the bias "survives to later evolutionary times" is
  open.
- **Not about any mechanism of dependence.** Obligacy is a
  phenomenological trade-off. Gene loss, transfer and host control are
  not modelled.

## Connections

- **[QUESTION-277](../questions.d/QUESTION-277.md).** This bears on the order of D and R. It does not
  settle it: the order turns on how each partner's traits act, which is
  an empirical question. It also corrects the question's summary.
- **[LIT-1605](../literature.d/LIT-1605.md).** Frank (1996, unread) models host control of
  transmission. If the host can impose cohesion unilaterally, dissociation
  depends on one partner's trait (mapping I). With free growth depending
  on one's own obligacy that is the matched case i-I, and the
  dependence-first bias largely disappears. The inference is mine.
