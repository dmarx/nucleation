---
number: 1457
status: Active
formerly:
- THEORY-tmpzi9gz
title: 'Majikes, Patrone, Kearsley, Zwolak and Liddle find, in a single-fold DNA origami model with a topology-reporting fluorophore and quencher, that the folded-state yield after annealing rises with staple excess to a turnover between about 1x and 5x and then falls, below 50 % at high excess for fold distances of 131, 1187 and 3407 bases, independent of staple motif at the one fold distance where motif was tested and, by the authors'' report of a supplementary control, unchanged by a twofold slower anneal, as an equilibrium model predicts when each fold domain can be occupied by a separate staple, the blocked state, with folded over blocked equal to the fold''s j-factor over the free staple concentration; they propose, without testing it, that whole origami escapes this through cooperativity and strand displacement along a nucleation front'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings), under ADR-065: the title reports what
    Majikes and colleagues find for one fold and what they propose
    without testing, and NOTE-1633 reads the manuscript's main text,
    captions and tables in full. The motif and anneal-rate clauses are
    narrowed to what was tested and to the authors' report of an unread
    supplementary control (ADR-047 kind 3). The old title was 'Majikes,
    Patrone, Kearsley, Zwolak and Liddle find, in a single-fold DNA
    origami model with a topology-reporting fluorophore and quencher,
    that the folded-state yield after annealing rises with staple excess
    to a turnover between about 1x and 5x and then falls, below 50 % at
    high excess for fold distances of 131, 1187 and 3407 bases,
    independent of staple motif and unchanged by a twofold slower
    anneal, as an equilibrium model predicts when each fold domain can
    be occupied by a separate staple, the blocked state, with folded
    over blocked equal to the fold's j-factor over the free staple
    concentration; they propose, without testing it, that whole origami
    escapes this through cooperativity and strand displacement along a
    nucleation front'. The condition asked for an independent
    measurement, and it moves unchanged to QUESTION-tmp1jy98, which
    lists it under this entry's code; this entry bears_on it: 'An
    independent measurement of single-fold yield against staple excess,
    by a second lab or with a reporter that separates the blocked from
    the unbound scaffold, reproduces the turnover and the decline at
    high excess, and its independence of anneal rate and staple motif.
    The proposed whole-origami escape is not part of the claim and needs
    no test for promotion.'
tags:
- natural-sciences
- thermodynamics
date: '2026-11-05'
source:
- LIT-2133
bears_on:
- QUESTION-tmp1jy98
corroborates:
- CLAIM-598
summary: >-
  Majikes, Patrone, Kearsley, Zwolak and Liddle (2021), [LIT-2133](../literature.d/LIT-2133.md),
  read in [NOTE-1633](../notes.d/NOTE-1633.md) (main text, captions and tables; the supplement,
  with the slower-anneal control, unread). Active as a report; its limits: one lab, one fold at
  a time, one reporter channel that cannot tell blocked from unbound, and
  one fold distance declared anomalous by assumption. The title asserts
  the single-fold measurement and that the authors propose the
  whole-origami escape; it does not assert the escape, nor that the
  blocked state is a kinetic trap.
---

# THEORY-1457: Majikes, Patrone, Kearsley, Zwolak and Liddle find, in a single-fold DNA origami model with a topology-reporting fluorophore and quencher, that the folded-state yield after annealing rises with staple excess to a turnover between about 1x and 5x and then falls, below 50 % at high excess for fold distances of 131, 1187 and 3407 bases, independent of staple motif at the one fold distance where motif was tested and, by the authors' report of a supplementary control, unchanged by a twofold slower anneal, as an equilibrium model predicts when each fold domain can be occupied by a separate staple, the blocked state, with folded over blocked equal to the fold's j-factor over the free staple concentration; they propose, without testing it, that whole origami escapes this through cooperativity and strand displacement along a nucleation front

## Source

Majikes, Patrone, Kearsley, Zwolak and Liddle (2021), [LIT-2133](../literature.d/LIT-2133.md); read
in [NOTE-1633](../notes.d/NOTE-1633.md).

## What was actually shown

- **The turnover** (Fig. 3): "the yield of the folded state increases as a
  function of staple concentration up to about 5× the scaffold
  concentration", then falls. Yield could have saturated with excess, as
  a two-state picture expects; it did not.
- **At every fold distance** (Fig. 4a): all three "fall below 50 % yield at
  high staple:scaffold ratios".
- **Not a rate effect at this scale**: "anneals performed two times slower
  replicated the trend (SI Fig S4)" (the supplement unread).
- **Motif-independent** (Fig. 5): the three motifs "had the same yield of
  the folded state".
- **The proposal**: origami "would nucleate in areas having short fold
  distances, giving rise to a growth front", blocking strands displaced
  only along a ‘nucleation front’.

## What this does not say

- That whole origami escapes the blocked state this way: one notched
  rectangle forms at 100× excess, imaged qualitatively, and the mechanism
  is reasoning.
- That the blocked state is a kinetic trap: at one fold it is an
  equilibrium share, and the authors leave its role in whole origami
  "either thermodynamic or kinetic".
- That the blocked state was seen directly: one channel cannot tell it
  from an unbound scaffold, and it is identified by regime and model.
- Anything about global folding traps, the subject of [THEORY-1398](THEORY-1398.md).
