---
number: 1046
status: Active
formerly:
- CLAIM-tmp7qzux
title: 'The observational partitions a family of affordable probes induces are not the lattice of possible decompositions: the map from probe subsets to partitions sends a union of families to the common refinement of their partitions, but an intersection of families to a partition that can be strictly coarser than the finest common coarsening, so its image is closed under meets and not under joins, and with m probes it has at most 2^m members against the Bell number of partitions of the configurations'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, filling a gap in A15 §2 of the
    exchange "Explain First Contact RL" (ChatGPT, shared 2026-11-22),
    checked with python3 -I.
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): point 2 gains a counterexample showing the
    image is not join-closed, which the title asserts and the proof had
    not shown; a demonstrated claim resting on CLAIM-264 (Active); nothing
    objects to it.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: a pair of probe families whose union induces
  a partition other than the common refinement of theirs, or an
  intersection of families inducing a partition finer than the join of
  theirs. A probe family whose probes change the configurations they are
  applied to does not count: the claim is stated for fixed configurations
  and fixed response laws, as CLAIM-574 is.
tags:
- mathematics
- individuation
- epistemology
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-264
complements:
- CLAIM-574
bears_on:
- QUESTION-393
uses:
- TERM-069
summary: >-
  A15 §2 says "the lattice of all partitions of Ω is generally much larger
  than the set of partitions realizable by our affordable probes", and that
  the probe lattice "is a structure of which distinctions our methods
  support", not of selves. It gives no argument and does not say how the
  two orders relate. They relate as follows. For fixed configurations Ω and
  fixed response laws, let π(Q) be the partition of Ω into classes no probe
  in Q separates. Then π(Q1 ∪ Q2) is the meet (common refinement) of π(Q1)
  and π(Q2), while π(Q1 ∩ Q2) is at least as coarse as their join and can
  be strictly coarser. So π is order-reversing and meet-preserving, its
  image is a meet-closed part of the partition lattice and need not be a
  sublattice, and with m probes it has at most 2^m members, against
  Bell(|Ω|) partitions (32 against 115,975 for m = 5 and |Ω| = 10). Checked
  with python3 -I on 3,000 random probe systems (no union failed; the
  intersection was strictly coarser than the join in 100) and on an
  explicit case. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

# CLAIM-1046: The observational partitions a family of affordable probes induces are not the lattice of possible decompositions: the map from probe subsets to partitions sends a union of families to the common refinement of their partitions, but an intersection of families to a partition that can be strictly coarser than the finest common coarsening, so its image is closed under meets and not under joins, and with m probes it has at most 2^m members against the Bell number of partitions of the configurations

## The claim

Let Ω be a set of configurations (candidate organizations of a self, in
A15's use), 𝒬 a set of admissible probes, and for each q a response law
D_z(q) fixed for each z in Ω. For Q ⊆ 𝒬 write z ∼_Q z′ when D_z(q) = D_z′(q)
for all q ∈ Q, and π(Q) for the partition into its classes ([TERM-069](../terms.d/TERM-069.md)'s
observational equivalence).

1. **Unions give meets.** z ∼_{Q1∪Q2} z′ exactly when z ∼_{Q1} z′ and
   z ∼_{Q2} z′, so π(Q1 ∪ Q2) = π(Q1) ∧ π(Q2), the common refinement.
2. **Intersections need not give joins.** ∼_{Q1∩Q2} contains both ∼_{Q1}
   and ∼_{Q2} and is an equivalence, so it contains their join, the finest
   equivalence containing both; π(Q1 ∩ Q2) is at least as coarse as
   π(Q1) ∨ π(Q2). It can be strictly coarser: on three configurations, let
   q1 and q2 each take three distinct values and q3 be constant. With
   Q1 = {q1, q3} and Q2 = {q2, q3}, π(Q1) and π(Q2) are both the discrete
   partition, so is their join, and π(Q1 ∩ Q2) = π({q3}) is one block.
   The image need not be closed under joins either: on Ω = {a, b, c, d} let
   q1 induce {a, b}{c}{d} and q2 induce {a}{b}{c, d}. The image of π is the
   one-block partition, π({q1}), π({q2}) and the discrete partition; the
   join π({q1}) ∨ π({q2}) = {a, b}{c, d} is none of them. Checked with
   python3 -I.
3. **Size.** π takes at most 2^|𝒬| values, while Ω has Bell(|Ω|)
   partitions. With five affordable probes and ten configurations, at most
   32 decompositions are visible among 115,975.

So the order of probe families maps into the partition lattice reversing
order, preserving meets, and generally landing on a small meet-closed part
of it that is not a sublattice. That is the sense of A15's warning that the
lattice "is a structure of which distinctions our methods support": most
ways of carving a self into parts are not offered by any affordable family,
and two families' shared probes can see less than either family's
partitions jointly suggest.

## The check

`python3 -I` on 3,000 random binary probe systems (2 to 6 configurations, 1
to 5 probes, random pairs of subfamilies): π(Q1 ∪ Q2) equalled the meet in
every case; π(Q1 ∩ Q2) was coarser than or equal to the join in every case,
strictly in 100. The explicit case above was run as well, and the Bell
numbers computed (Bell(10) = 115,975; Bell(20) ≈ 5.17 × 10^13 against 256
for eight probes).

## What it does not say

It holds probes and configurations fixed, as [CLAIM-574](CLAIM-574.md) does. When a probe
changes what it probes, the families are of probe sequences ([TERM-069](../terms.d/TERM-069.md), the
term [TERM-165](../terms.d/TERM-165.md)), and the order is over those. It says nothing about
which of the visible partitions, if any, is a decomposition into
perspectives: that is the further, causal question ([CLAIM-454](CLAIM-454.md), [QUESTION-393](../questions.d/QUESTION-393.md)).
