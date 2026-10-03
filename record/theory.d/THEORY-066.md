---
number: 66
status: Active
formerly:
- THEORY-tmpcv4h8
title: 'A Markov-blanket partition is defined relative to a chosen internal set, so a graph has one around almost any set of nodes, and the formalism alone does not say which set is the system'
version: 1
tags:
- individuation
- probabilistic-modeling
- philosophy-of-science
date: '2026-10-03'
source:
- LIT-603
- LIT-526
summary: >-
  The formal core of Bruineberg et al.'s critique ([LIT-603](../literature.d/LIT-603.md), C4 in
  [NOTE-447](../notes.d/NOTE-447.md)). In a directed acyclic graph the blanket of a node set A
  is its parents, children and the children's other parents, and A is
  conditionally independent of everything outside A and its blanket.
  That holds for every A, so any set whose blanket leaves something
  outside gets a valid internal, blanket and external partition. Having
  a blanket therefore picks out no set. In Friston's soup ([LIT-526](../literature.d/LIT-526.md)) the
  set was picked by spectral clustering with k = 8, not by the blanket.
  Active because it is a short derivation that anyone can check. It covers
  graphical (Pearl) blankets and the 2013 procedure. It does not cover
  the later sparse-coupling definitions at nonequilibrium steady state,
  which the record has not read.
extended_by:
- THEORY-073
---
<!-- inactive-ok-file: THEORY-073 THEORY-072 THEORY-071 — Proposed; the wider claims this one supports or sits beside, not leaned on -->

# THEORY-066: A Markov-blanket partition is defined relative to a chosen internal set, so a graph has one around almost any set of nodes, and the formalism alone does not say which set is the system

## Source

- Bruineberg, Dołęga, Dewhurst & Baltieri (2020 preprint), [LIT-603](../literature.d/LIT-603.md),
  read in [NOTE-447](../notes.d/NOTE-447.md): §3.2 (Pearl blankets), §4.2 (the soup re-run), §5.1
  and Figure 7 (Friston blankets on an arbitrary network).
- Friston (2013), [LIT-526](../literature.d/LIT-526.md), read in [NOTE-421](../notes.d/NOTE-421.md): §3 (how the blanket of the
  simulated soup was found).

## The claim, derived

Take a directed acyclic graph G over variables V, and any distribution that
factorises over it as ∏ p(x_v | pa(v)). For a set A ⊂ V, let

mb(A) = (pa(A) ∪ ch(A) ∪ pa(ch(A))) ∖ A,

the parents of A, its children, and its children's other parents.

**A is conditionally independent of R = V ∖ (A ∪ mb(A)) given mb(A).**
The factors of the joint that mention any variable in A are p(x_a | pa(a))
for a in A, and p(x_c | pa(c)) for children c of A. These factors mention
only variables in A ∪ mb(A). Every other factor is constant in x_A. So
p(x_A | x_mb, x_R) is proportional to a product that does not contain x_R,
and the independence follows. This is Pearl's local Markov property
written for a set, and the same argument works for undirected graphs with
the neighbours of A as its blanket.

Nothing in the derivation used a property of A. It holds for every subset.
So every A with R non-empty yields a partition into internal (A), blanket
(mb(A)) and external (R) states. Friston's further split of the blanket
into sensory states (parents of A) and active states (children of A) is
likewise defined once A is given. The formalism takes the internal set as
an input. Its output is a blanket. It never outputs the internal set.

## What the sources show

**Bruineberg et al. state it and draw it.** They apply the four-way
labelling to an arbitrary 18-node network. In their words, the partition
"cannot simply be applied to any graphical model without first making some
additional assumptions". Labelling x10 as internal yields one blanket, and
labelling x9 yields a different one (Figure 7). The Friston blanket "does
not define what is inside and what is outside (or at least not without
further assumptions), but can rather only be identified once we have
already made this choice (by labelling one node as 'internal')". Neither
blanket's sensory states coincide with the network's observed variables.
[NOTE-447](../notes.d/NOTE-447.md) rates this C4, strong for arbitrary graphs.

**Friston's own procedure shows it.** In the soup of [LIT-526](../literature.d/LIT-526.md), the internal
set was not found by looking for a blanket. Spectral graph theory picked
the eight most densely coupled subsystems from a time-averaged adjacency
matrix, and the blanket was then traced as their parents, children and
co-parents ([NOTE-421](../notes.d/NOTE-421.md), Key results). The selection did the individuating
work. A clustering criterion and a value of k did it, and neither belongs
to the Markov-blanket formalism. Bruineberg et al. reproduce this from
Friston's code (§4.2).

## What this does not say

- **It does not say that blankets are useless or that the free energy
  principle is false.** The derivation is the reason blankets are useful
  in variational inference, and it leaves Lemma 2.1 of [LIT-526](../literature.d/LIT-526.md) untouched.
- **It does not cover every later definition.** Recent work defines a
  blanket by sparse coupling in the flow, or in the Hessian of the
  log-density at nonequilibrium steady state. Bruineberg et al. note this
  and do not analyse it, and the record has read it only as Raja et al.
  summarise it ([LIT-598](../literature.d/LIT-598.md), Eqs. 4–5), where the partition is again
  given before its conditions are checked. Whether some formulation also
  selects the internal set is open. The open question in [NOTE-447](../notes.d/NOTE-447.md)
  asks the same thing.
- **It does not say that an added selection criterion must be arbitrary.**
  A criterion such as densest coupling, or Friston's conjectured minimum
  blanket entropy (C8 in [NOTE-421](../notes.d/NOTE-421.md)), could be principled. The claim is only
  that such a criterion is added to the formalism, and that whatever it is
  does the individuating.
- **It is about individuation, not about any of the four unities of
  [ADR-024](../decisions.d/ADR-024.md).** "Internal states" here are a set of variables, not a self, an
  agent or a subject.

## Connections

- **[THEORY-073](THEORY-073.md)** extends this account to its wider and Proposed
  conclusion: in practice the boundary comes from modelling choices, and a
  blanket cannot represent a boundary the system produces.
- **Closure of constraints ([LIT-582](../literature.d/LIT-582.md))** takes the other route. It
  defines the boundary by which constraints the system produces, not by a
  set chosen beforehand. [THEORY-072](THEORY-072.md) uses it for the demarcation of
  organisms.
- **The Yoneda lemma ([THEORY-032](THEORY-032.md))** has the same shape in another formal
  setting. The relation determines its relata only among objects that are
  already given.
