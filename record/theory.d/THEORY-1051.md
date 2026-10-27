---
number: 1051
status: Proposed
formerly:
- THEORY-tmpyk1k6
promote_when: >-
  Comparative or experimental evidence relating the partners' population
  growth parameters to which becomes obligate first, across independent
  symbioses, with the faster-evolving partner (larger population, faster
  growth) found obligate first more often than chance; and, for at least
  one symbiosis, measured rates of partner birth and death inside the
  collective, with the host's dependence matching the model's prediction
  from their balance (deaths dominating: host fully dependent; births
  dominating: host independent). The model's own simulations, or the
  observation that symbionts are often more obligate than hosts, cannot
  settle it, since symbionts live inside hosts for other reasons. It is
  refuted if slower-evolving partners are as often obligate first, or if
  host dependence is unrelated to within-collective demography.
title: 'In Athreya, Czuppon and Gokhale''s model of an incipient endosymbiosis, the partner with the larger and faster-growing population evolves faster and becomes fully obligate first, a Red King effect in which the collective''s shared fate aligns interests; the other partner''s dependence then stays where it was, rises to full dependence, or falls to none, according to whether partners are born or die inside the collective, and dependence rises at all only if the collective''s carrying capacity is high enough, so a full transition to a mutually dependent, co-reproducing pair is a parameter-dependent outcome and not the default'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1211, the reading in full of the bioRxiv
    version 2 of Athreya, Czuppon & Gokhale (2025). These are model
    results under stated assumptions: symmetric within-collective rates
    only, constant association rate and collective carrying capacity,
    one symbiont unit per host. The carrying-capacity condition is shown
    sufficient by simulation, not necessary. Nothing is tested against
    data. Hence Proposed.
tags:
- endosymbiosis
- individuation
date: '2026-10-27'
source:
- LIT-1570
answers:
- QUESTION-277
summary: >-
  Athreya, Czuppon & Gokhale (2025), [LIT-1570](../literature.d/LIT-1570.md), read in [NOTE-1211](../notes.d/NOTE-1211.md). With
  the symbiont's population larger and faster, its obligacy reaches 1
  first. In the base model the host's R₀ is then exactly 1, so host
  obligacy is neutral. With within-collective deaths the host goes fully
  obligate, and with within-collective births it goes back to
  independence. Obligacy rises from zero only if the collective's carrying capacity
  exceeds about aK_HK_S/d; collective growth rate does not matter. The
  authors take the model as a null: a transition "is far from an
  inevitable outcome of the existence of a higher level of selection".
---
<!-- inactive-ok-file: QUESTION-277 THEORY-141 THEORY-443 CASE-173 CASE-177 — Open or Proposed; the question, accounts and cases this is set beside, nothing here rests on them -->
# THEORY-1051: In Athreya, Czuppon and Gokhale's model of an incipient endosymbiosis, the partner with the larger and faster-growing population evolves faster and becomes fully obligate first, a Red King effect in which the collective's shared fate aligns interests; the other partner's dependence then stays where it was, rises to full dependence, or falls to none, according to whether partners are born or die inside the collective, and dependence rises at all only if the collective's carrying capacity is high enough, so a full transition to a mutually dependent, co-reproducing pair is a parameter-dependent outcome and not the default

## Source

Athreya, Czuppon & Gokhale (2025), [LIT-1570](../literature.d/LIT-1570.md), read in full in
[NOTE-1211](../notes.d/NOTE-1211.md) from the bioRxiv version 2. The sections "Independent
evolution of obligacies and adhesions", "The effect of within-collective
mortality and reproduction", "Collective growth rate and collective
carrying capacity have different effects", the conclusions, Figures 2–4,
Table 2, and Supplementary Notes S3–S4.A.

## What was actually shown

- **Order of obligacy.**
  - With K_S > K_H and r_S > r_H, the symbiont's obligacy reaches 1
    first (Fig. 2). Swapping the parameters swaps the partners, and
    equal parameters give symmetric outcomes (Fig. S4).
  - At Ω_S = 1, the host mutant's R₀ is exactly 1 (Note S4.A), so host
    obligacy is neutral and neutral variation should accumulate.
- **Within-collective demography (Fig. 3, Table 2, Eq. 7).**
  - With deaths only (d_H = d_S > 0), obligacy must start above a
    threshold, and then the host follows the symbiont to 1.
  - With births only (b_H = b_S > 0), obligacy rises freely, and then the
    host falls to 0. There is then no equilibrium: the symbiont dies out
    while the collective grows without bound.
  - Eq. 7 identifies b_S − d_S as the sign that decides.
- **Carrying capacity (Fig. 4, Note S3.B).** Traits leave (0,0) for
  K_C = 50 or 500 but not 10, at either r_C = 1 or 40.
  - The proposed sufficient condition is K_C > aK_HK_S/d, which is 40 at
    those parameters (checked in the reading).
  - Moving a to 0.01 or 5 moved the outcome as predicted.
- **Interpretation.** The authors read the symbiont's head start as the
  Red King effect: the faster-evolving partner concedes first when
  interests are aligned. Here the collective's shared fate does the
  aligning, not a mutualism.

What could have failed: the faster partner could have been the one to
keep its independence, or host dependence could have followed regardless
of demography. In the model, neither happens.

## What this does not say

- **Not tested in any real symbiosis.** No growth parameters, carrying
  capacities or within-collective rates are measured. The authors call
  measuring b and d "imperative".
- **Not for unequal or trait-dependent rates.** Only b_H = b_S and
  d_H = d_S were simulated. The authors expect b_S − d_S to dominate, but
  have not tested it.
- **Not that symbiont-first obligacy explains reduced symbiont genomes.**
  The authors list Muller's ratchet and "environment-induced redundancy"
  as other drivers, which they say depend on the symbiont living inside
  the host.
- **Not a model of conflict.** Interests are aligned by construction, and
  there is no within-collective selection. So it cannot speak to
  policing or to [THEORY-141](THEORY-141.md)'s condition.

## Connections

- **[QUESTION-277](../questions.d/QUESTION-277.md).** One-sided dependence (symbiont obligate, host free)
  and full mutual dependence are both outcomes of one model, decided by
  demography inside the collective. That gives the question a candidate
  variable for when a dependency becomes an individual.
- **[THEORY-443](THEORY-443.md).** The model's transition criterion, full dependence plus
  full cohesion giving the pair a life cycle, is one operational version
  of Darwinian individuality for a partnership. Under it, most dependent
  symbioses stop short.
- **[THEORY-141](THEORY-141.md).** It describes a different mechanism of alignment. Here,
  shared reproduction and the Red King effect align interests, not
  policing. It does not compete with [THEORY-141](THEORY-141.md)'s condition, because it
  models no conflict.
- **[CASE-173](../cases.d/CASE-173.md) and [CASE-177](../cases.d/CASE-177.md).** Aphid–*Buchnera* is the model's
  mutually-obligate, vertical case. The model's single-symbiont
  collectives cannot represent *Hodgkinia*'s splitting.
