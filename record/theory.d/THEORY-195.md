---
number: 195
status: Active
formerly:
- THEORY-tmpzjtfu
title: 'On the Random Hierarchy Model, in the experiments reported (s = 2, L ≤ 4, small v), deep CNNs matched to the tree and trained in a feature-learning regime reach a tenth of chance error from about n_c m^L examples, polynomial in the input dimension, at the training-set size at which their hidden layers become invariant to swapping synonymous tuples; two-layer networks and the same CNNs as fixed kernels need a number proportional to the whole input space, exponential in the input dimension, and deep CNNs stay near chance when every tuple is made equally likely in every class'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-195 (batch 027,
    ADR-047). Under ADR-047 v3 the one study suffices: NOTE-677 read it in
    full, the paper states these results in its text, and nothing in the
    record contradicts them. The title now claims what was measured, in the
    range measured. It no longer asserts that P* is where the class statistics
    of input patches rise above sampling noise: in this model that threshold
    and the grammar's size are the same expression, and the body disclaims the
    attribution. That clause and the promote_when move, unchanged, to
    QUESTION-165.
- version: 3
  date: '2026-10-20'
  note: >-
    Note of 2026-10-20 added: the wider claim this entry's narrowing
    dropped is now filed as THEORY-786, Proposed, which extends
    this one (ADR-047 v4). The title and status are unchanged.
tags:
- learning-theory
- compositionality
- representation-learning
date: '2026-10-09'
source:
- LIT-877
summary: >-
  Cagnetta, Petrini, Tomasini, Favero and Wyart (2023), [LIT-877](../literature.d/LIT-877.md):
  measured for depth-(L + 1) CNNs and deep fully connected networks on the
  Random Hierarchy Model with s = 2 and L ≤ 4, with a large-v scaling
  argument for the correlation threshold and an exact one-step-gradient
  model of a two-layer network on one patch. The law n_c m^L is fitted,
  not proved for trained deep networks, and in this model the correlation
  threshold and the grammar's size are the same expression, so the data
  cannot say which of the two sets it.
answers:
- QUESTION-025
supports:
- CLAIM-360
extended_by:
- THEORY-786
---

<!-- inactive-ok-file: THEORY-786 — Proposed; the wider claim this entry's narrowing dropped, cited as open -->
<!-- inactive-ok-file: THEORY-186 QUESTION-025 — Proposed or open; cited as the accounts this one is set beside and the question it does not answer -->

# THEORY-195: On the Random Hierarchy Model, in the experiments reported (s = 2, L ≤ 4, small v), deep CNNs matched to the tree and trained in a feature-learning regime reach a tenth of chance error from about n_c m^L examples, polynomial in the input dimension, at the training-set size at which their hidden layers become invariant to swapping synonymous tuples; two-layer networks and the same CNNs as fixed kernels need a number proportional to the whole input space, exponential in the input dimension, and deep CNNs stay near chance when every tuple is made equally likely in every class

## Source

Cagnetta, Petrini, Tomasini, Favero and Wyart (2023; Phys. Rev. X 2024),
[LIT-877](../literature.d/LIT-877.md), Eqs. 3–10 and 13, Figs. 2–9 and 12–14, Appendices B–D, as read
in [NOTE-677](../notes.d/NOTE-677.md).

## What was actually shown

**The data.** A random context-free grammar: n_c classes, L levels of v
symbols, each class and symbol rewriting to m distinct s-tuples from the
level below, drawn at random with no tuple shared between parents. Inputs
are the d = s^L leaves; there are P_max = n_c m^((d−1)/(s−1)) of them,
exponential in d. In the maximal case every string occurs, so neither a
low-dimensional manifold nor smoothness nor a few relevant directions is
available to a learner.

**The measurements.** Two-layer networks need a fixed fraction of P_max
(Fig. 2). Depth-(L + 1) CNNs matched to the tree and trained by SGD under
the maximal-update parametrisation reach a tenth of chance error at
P* ≈ n_c m^L, i.e. P*/n_c ≈ d^(ln m/ln s), across v, m, L ≤ 4 and n_c
(Figs. 3, 4, 12); deep fully connected networks do likewise up to a factor
of about 2^L (Fig. 13). The same CNNs as fixed kernels (the NTK) do not
converge even near P_max (Fig. 14). Hidden layers become insensitive to
swapping a tuple for a synonym around the same P, level l from layer l + 1
on (Figs. 5, 6). With the grammar kept but every tuple made equally likely
in every class, deep CNNs stay near chance at 90% of P_max (Fig. 9). Each
of these could have come out otherwise: the deep networks could have
needed an exponential number, invariance could have appeared at a
different P from generalisation, or the uncorrelated grammar could have
been learned from its hierarchy alone.

**The argument.** For a tuple in a fixed patch, the probability of each
class depends on the tuple only through its parent, so it is equal for
synonyms; over draws of the rules its relative spread is (v/m^L)^(1/2), and
the relative noise of its estimate from P data is (v n_c/P)^(1/2). They
meet at P_c = n_c m^L (Appendix C, asymptotic in v and n_c). In a two-layer
network on one patch, one gradient step makes each hidden response a
weighted sum of exactly these empirical frequencies, so synonym invariance
arrives as they converge (Eq. 13, Fig. 8).

## What this does not say

- **Not that P* is derived for trained deep networks.** The derivation is
  of a statistical threshold; the identification with deep SGD training is
  the coincidence of collapses and a one-step, one-patch model. The
  authors leave open whether end-to-end training reaches the √n_c-better
  rate a clustering algorithm attains.
- **Not that correlation detection, rather than grammar size, sets P*.**
  In the model both are n_c m^L. Fig. 9 shows the correlations are
  necessary; it does not show the threshold is what fixes the number.
- **Not that depth alone escapes the curse.** It escapes it here with
  features learned and with input–label correlations present; lazy deep
  networks and the uncorrelated grammar both fail.
- **Not a claim about natural language or images.** The grammar is
  uniform, s = 2, L ≤ 4, and the CNNs are given the tree's patch size. The
  CIFAR-10 figure is an order-of-magnitude illustration with guessed m and
  L.
- **Not about hierarchies of attributes.** The hierarchy is part–whole: a
  tuple in a position implies its parent. Nothing here concerns
  attributes of one item implying each other, linear directions or concept
  lattices, so it leaves [QUESTION-025](../questions.d/QUESTION-025.md) and [THEORY-185](THEORY-185.md) as they were.
- **Not the coarse-to-fine stages of [THEORY-186](THEORY-186.md).** That account is about
  training time in deep linear networks on a tree of attributes; here
  every level becomes invariant at the same training-set size.
- **Not an instruction.** It says what the number of examples is, not how
  to train.

## Connections

It is the failure-side complement of [THEORY-086](THEORY-086.md): a fixed kernel can exploit
local patch–label correlations (the lazy curves track the feature-learning
ones while P ≪ P*) but cannot compose them, and so stays cursed.

## Note of 2026-10-19: narrowed to the measured result

The promotion audit's batch 027 ([ADR-047](../decisions.d/ADR-047.md) v3) promoted this account on
what the experiments measured, in the range they cover (s = 2, L ≤ 4,
small v): the number of examples deep CNNs need, its coincidence with
synonym invariance in the hidden layers, the failure of shallow and
fixed-kernel learners, and the failure without patch–label correlations.
The scaling argument of §III.B and Appendix C, which puts the
detectability threshold of those correlations at the same n_c m^L, stays
above as the paper's argument. It is a large-v estimate, not a bound
([NOTE-677](../notes.d/NOTE-677.md), claim C4). Whether that threshold, rather than the grammar's
size, sets the number of examples is [QUESTION-165](../questions.d/QUESTION-165.md). Deep fully
connected networks (within a factor of about 2^L, one figure) are not in
the title.

## Note of 2026-10-20: the wider claim filed

The promotion audit narrowed this entry to what was shown. Under
[ADR-047](../decisions.d/ADR-047.md) v4 the claim the narrowing dropped, that detecting patch-class correlations is what sets the number of examples and how deep networks learn the grammar, is now filed as
[THEORY-786](THEORY-786.md), Proposed, which extends this entry and takes it as
evidence. This entry's title and status are unchanged.
