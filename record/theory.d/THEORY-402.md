---
number: 402
status: Proposed
formerly:
- THEORY-tmp05zxn
promote_when: >-
  One case in which the resources and the coordination and cooperation
  costs are each measured in a common unit, before the outcome is known,
  and the balance predicts when the group beats its best member and when
  it loses to it, quantitatively and better than a mechanism-specific model
  of the same task. It is refuted by a group whose measured gain or loss
  runs against that balance. Retellings of published cases, chosen to fit
  and described after the fact, cannot settle it, and neither can the
  standard σ²/n result for averaging independent errors.
title: "Collective intelligence is resource-bounded computation with a larger but modular budget: a group has more sensing, state, processing and action than any member, and pays coordination and cooperation costs because those resources sit in autonomous members, so the same trade-off yields groups that do better than their members on some tasks, groups that run qualitatively different algorithms, and groups that do worse"
version: 1
tags:
- complex-systems
- cognition
date: '2026-10-16'
source:
- LIT-046
- LIT-075
summary: >-
  Pilgrim et al. (2025), [LIT-046](../literature.d/LIT-046.md), read in [NOTE-055](../notes.d/NOTE-055.md), with Dreyer et al.
  (2024), [LIT-075](../literature.d/LIT-075.md) ([NOTE-040](../notes.d/NOTE-040.md)), as its clearest instance. The paper offers a
  four-dimensional resource inventory, a catalogue of constraints and a
  mapping to mechanisms, and calls the known forms of collective
  intelligence "aspects of a single unifying principle". [NOTE-055](../notes.d/NOTE-055.md) judges it
  a vocabulary, not a derivation: the resources have no metric, so the
  framework cannot say in advance when costs outweigh gains, and its
  "predictions" are research questions. Filed Proposed as the account the
  vocabulary states.
---
<!-- inactive-ok-file: LIT-046 — Proposed; the source this account states, placed by its NOTE, whose verdict the account carries -->
<!-- inactive-ok-file: THEORY-043 — Proposed; a neighbouring account named for context, nothing here rests on its being settled -->

# THEORY-402: Collective intelligence is resource-bounded computation with a larger but modular budget: a group has more sensing, state, processing and action than any member, and pays coordination and cooperation costs because those resources sit in autonomous members, so the same trade-off yields groups that do better than their members on some tasks, groups that run qualitatively different algorithms, and groups that do worse

## Source

Pilgrim, Morford, Warren et al. (2025), [LIT-046](../literature.d/LIT-046.md), "The Computational
Foundations of Collective Intelligence", read in full in [NOTE-055](../notes.d/NOTE-055.md). The
empirical instance is Dreyer et al. (2024), [LIT-075](../literature.d/LIT-075.md), read in [NOTE-040](../notes.d/NOTE-040.md),
which [LIT-046](../literature.d/LIT-046.md) does not cite. [NOTE-055](../notes.d/NOTE-055.md) says the paper "does not support or
contradict any THEORY document on its own evidence". This document states
the account the paper puts forward, with that verdict attached.

## What was actually shown

**The inventory (Table 1).** A group has the union of its members' sensory
information, the product of their state and action spaces with a
collective state S_c on top, and their processes plus inter-individual
ones. The caption says the operators denote totals, "not simple addition",
so no metric is given.

**The constraints (§3).** Coordination: synchronisation, communication
cost, integrating the parts of a decomposed task, bandwidth. Cooperation:
diverging preferences, social dilemmas, and "participatory computation",
where contributing and benefiting are one act.

**The mapping (§4, Table 2).** Aggregation cuts noise to σ_i²/n when errors
are uncorrelated. Combined states can represent a distribution over
hypotheses where a member holds one. Collective memory can outlast any
member. The joint action space supports division of labour.

**The trade-off (Fig. 2).** The same budget can move a group further along
a member's resource–quality curve, put it on a different curve, or, with
coordination costs, below the member.

**Cases.** Citing Sasaki et al. (2013), ant colonies beat single ants on
hard discriminations and lose on easy ones, through early amplification of
noisy assessments (§5.2). In [LIT-075](../literature.d/LIT-075.md), ant groups improve with size on a
transport puzzle, while human groups barred from speech do 32% worse than
individuals and talking groups 7% better.

**What could have come out otherwise.** As stated, nothing. The framework
names the outcomes after the fact. It cannot be wrong until its resources
are measured.

## What this does not say

- **That the forms of collective intelligence derive from one principle.**
  The link from resources to mechanisms is argued in prose. [NOTE-055](../notes.d/NOTE-055.md)
  rates the unification claim weak.
- **When a group will beat its members.** That needs the costs and gains in
  one unit. The framework lists constraints and models none.
- **That collectives reason disjunctively or counterfactually.** The paper
  flags this "Speculatively, we predict" and gives no example.
- **That [LIT-075](../literature.d/LIT-075.md) tests it.** The ants-and-humans study is consistent with
  the trade-off, and was not designed or analysed against it.
- **Anything new about averaging.** The σ²/n result is the standard one for
  independent errors.

## Connections

- **The ants-and-humans finding ([THEORY-608](THEORY-608.md))** is the evidence this
  account leans on, with its own caveats: no inferential statistics, and
  mechanisms fitted or observed informally.
- **Minds of minded agents ([THEORY-043](THEORY-043.md))** names this paper as a neighbour.
  The resource view is silent on whether a collective that computes is a
  subject.
- **Variance pooling ([THEORY-696](THEORY-696.md))** is another case of a group gaining
  from averaging over members, in growth rather than in error, with the
  same dependence on how correlated the members are.
