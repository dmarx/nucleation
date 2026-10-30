---
number: 1188
status: Proposed
formerly:
- THEORY-tmpsjqto
title: 'Once the architecture''s symmetries are factored out, most of the linear barrier between independently trained solutions disappears; the group that matters is the full one, permutations for MLPs and CNNs but for transformers also an orthogonal map on the residual stream, without which a barrier remains; and the barrier left after alignment falls with width'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-30'
source:
- LIT-652
- LIT-661
- LIT-680
- LIT-664
- LIT-655
extends:
- THEORY-112
promote_when: >-
  The residual barrier after full-group alignment accounted for at a scale
  the sources do not reach. The zero barriers so far are for MNIST MLPs, a
  32×-wide ResNet-20 on CIFAR-10, and small ViTs and GPT-2s whose alignment
  was learned against the loss at the midpoint. ImageNet ResNet-50 keeps a
  third of its barrier, and BookCorpus keeps 0.42. What would promote:
  independently trained models at standard width, on ImageNet or a language
  corpus, brought to near-zero held-out barrier by a data-free alignment
  over the architecture's full symmetry group. Or the residual barrier
  shown to track a difference in what the endpoints compute, as LIT-669's
  barriers do, so that "most" is the part that is symmetry and the rest is
  identified. What would refute it: same-data, same-procedure solutions
  whose barrier stays near the unaligned value under every alignment the
  full group allows, learned ones included, when the endpoints are shown to
  rely on the same input attributes. A third or fourth permutation-finding
  algorithm on vision models at moderate scale cannot settle it.
bears_on:
- QUESTION-317
summary: >-
  The wide form [THEORY-112](THEORY-112.md) held before the eleventh status review narrowed
  it, kept as a Proposed reading by the [ADR-047](../decisions.d/ADR-047.md) kind-1 sweep of
  2026-10-30: the source asserts it, and [THEORY-112](THEORY-112.md), Active, is its
  evidence. The old title's last words, that the barrier left after
  alignment rises with depth, were the record's composition, not a
  source's, and are a Proposed claim of their own.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-1 rule this entry is filed under -->

# THEORY-1188: Once the architecture's symmetries are factored out, most of the linear barrier between independently trained solutions disappears; the group that matters is the full one, permutations for MLPs and CNNs but for transformers also an orthogonal map on the residual stream, without which a barrier remains; and the barrier left after alignment falls with width

## Source

- Entezari, Sedghi, Saukh & Neyshabur (2022), [LIT-652](../literature.d/LIT-652.md), read in [NOTE-537](../notes.d/NOTE-537.md).
- Ainsworth, Hayase & Srinivasa (2023), Git Re-Basin, [LIT-661](../literature.d/LIT-661.md), read in
  [NOTE-532](../notes.d/NOTE-532.md).
- Ferbach, Goujaud, Gidel & Dieuleveut (2024), [LIT-680](../literature.d/LIT-680.md), read in [NOTE-543](../notes.d/NOTE-543.md).
- Theus, Cabodi, Anagnostidis, Orvieto, Singh & Boeva (2025), [LIT-664](../literature.d/LIT-664.md),
  read in [NOTE-540](../notes.d/NOTE-540.md).
- Bo Zhao, Dehmamy, Walters & Yu (2025), [LIT-655](../literature.d/LIT-655.md), read in [NOTE-528](../notes.d/NOTE-528.md).

What alignment removed in each network these sources measured is
[THEORY-112](THEORY-112.md), which this entry extends.

## The claim

Entezari et al. conjecture that for wide enough networks most SGD solutions
can each be permuted so that the straight line between any two has about
zero barrier: one basin, seen through different labellings of the hidden
units (Conjecture 1; [NOTE-537](../notes.d/NOTE-537.md), C1). Git Re-Basin holds that wide enough
networks trained independently can be permuted into zero-barrier
connectivity, and that permutation alone does not connect thin ones
([NOTE-532](../notes.d/NOTE-532.md), C1–C2). Ferbach et al. prove the conjecture for wide networks
with independent neurons, with a width requirement that is a bound on
width. Bo Zhao et al. place permutations inside the architecture's full
symmetry group, and Theus et al. carry the group to transformers: feed-
forward units take permutations, attention heads a semi-permutation, and
the residual stream one orthogonal map, without which a barrier remains.

So the claim is general: what separates independently trained solutions on
a straight line is mostly the architecture's symmetry, the full group and
not only permutations, and less of it is left the wider the network. The
measurements reach zero only for MNIST MLPs, 32×-wide ResNet-20s and small
transformers whose alignment was learned against the midpoint loss.

## What would settle it

The promote_when, which is [QUESTION-317](../questions.d/QUESTION-317.md): standard-width models on ImageNet
or a language corpus brought to near-zero held-out barrier by a data-free
alignment over the full group, or the residual barrier shown to be a
difference in what the endpoints compute. Another permutation-finding
algorithm on vision models at moderate scale cannot settle it.
