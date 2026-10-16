---
number: 524
status: Active
formerly:
- THEORY-tmpg26fz
title: "On cyclic measurement scenarios, where the contexts' overlaps form one chordless N-cycle, the ℤ/2 Čech obstruction computed on the (N−1)-th iterated joint model is exact for logical and strong contextuality, the bound N − 1 being tight; beyond cycles no such result is established, the published extension is false on its own example, and the completeness conjecture fails on a Kochen–Specker cover that is never detected at any level"
version: 1
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-16'
source:
- LIT-280
- LIT-281
extends:
- THEORY-526
summary: >-
  Carù (2018), [LIT-280](../literature.d/LIT-280.md), read in [NOTE-253](../notes.d/NOTE-253.md), and the same result republished
  as Thm IV.32 of Carù's 2019 thesis, [LIT-281](../literature.d/LIT-281.md), read in [NOTE-254](../notes.d/NOTE-254.md). The
  cyclic theorem is proved and was confirmed on Hardy, on the (2,2,4)
  counterexample and on 659 random contextual cycle models. The failures
  beyond cycles (Prop 8.2 / IV.34, the §8 cover, Conjecture 9.1 / IV.41)
  are the readers' computations and a lifting lemma, not the author's.
  The joint models grow exponentially; nothing analyses the cost.
---

# THEORY-524: On cyclic measurement scenarios, where the contexts' overlaps form one chordless N-cycle, the ℤ/2 Čech obstruction computed on the (N−1)-th iterated joint model is exact for logical and strong contextuality, the bound N − 1 being tight; beyond cycles no such result is established, the published extension is false on its own example, and the completeness conjecture fails on a Kochen–Specker cover that is never detected at any level

## Source

Carù (2018), "Towards a complete cohomology invariant for non-locality
and contextuality", arXiv 1807.04203, [LIT-280](../literature.d/LIT-280.md), read in [NOTE-253](../notes.d/NOTE-253.md). Carù
(2019), DPhil thesis, Oxford, [LIT-281](../literature.d/LIT-281.md), read in [NOTE-254](../notes.d/NOTE-254.md); its Chapters
III–IV republish [LIT-279](../literature.d/LIT-279.md) and [LIT-280](../literature.d/LIT-280.md), with the joint model renamed the
line model.

## What was actually shown

**The construction.** The joint model S^(1) pulls back adjacent
contexts; S^(k) iterates it. S^(k) is a well-defined empirical model, and
it is strongly (or logically, at a section) contextual exactly when S is
(Props 4.2, 4.6, 5.1). A non-vanishing obstruction on it is sound (Thm
7.2).

**Why it helps.** On joint contexts, which are unions of full
rectangles, the signed "Z-shaped" combinations that fool the ordinary
obstruction can no longer sit inside one context (Lemmas 7.4–7.5, Thm
7.6).

**The theorem ([LIT-280](../literature.d/LIT-280.md) Thm 7.7; [LIT-281](../literature.d/LIT-281.md) Thm IV.32).** On a cyclic
scenario with |M| contexts, LC ⇔ CLC^(|M|−1) and SC ⇔ CSC(S^(|M|−1)).
The readers confirmed it on Hardy, on Carù's 2017 (2,2,4)
counterexample (detected on all 22 sections at level 3 and on none at
levels 1–2), and on 659 random contextual cycle models. Hardy needs
level 3, so the bound is tight. This covers the Bell (2,2,d) and N-cycle
scenarios, and removes two of the three failures in [THEORY-526](THEORY-526.md).

**Beyond cycles (the readers' findings).**

- *Prop 8.2 (= IV.34) is false as stated.* The paper's own Table 5 model
  fails at level 2 for section s₁₀ with n = 3; [NOTE-253](../notes.d/NOTE-253.md) gives an explicit
  family.
- *The §8 Kochen–Specker cover of [LIT-277](../literature.d/LIT-277.md) is never fully detected.* Under
  the paper's definitions, a lifted ℤ/2 family through (s_{ABC,A},
  s_{AEG,A}) survives at every level, which refutes the closing
  conjecture that some level is complete for every model (Conjecture 9.1;
  IV.41 in the thesis). The thesis's claim that the first line model
  removes all its false negatives rests on a wrong equation in the
  level-0 system.
- *Cost.* For that cover the joint models have 5, 10, 30, 150 and 1,350
  contexts at levels 0–4.

What could have come out otherwise: some random cycle model could have
escaped detection at level |M| − 1. None of 659 did.

## What this does not say

- **That a complete cohomological invariant exists for every scenario.**
  Off cycles nothing general is established, and the stated conjecture is
  false.
- **That the invariant is cheap.** "Without compromising the practical
  computability" (§1) is asserted; the objects grow like iterated line
  graphs.
- **That cohomology is the only exact route.** The thesis's Chapter V
  decides logical and strong contextuality on any scenario by local
  computation on join trees, at a cost exponential in treewidth; the
  thesis never connects the two ([NOTE-254](../notes.d/NOTE-254.md)). That chapter's reformulation
  is close to a restatement of the definitions, and its speed comparison
  uses an unnatural baseline, so it is not filed here.
- **Anything probabilistic.** As with the ordinary obstruction, only
  supports are used. The thesis's probabilistic line model preserves
  marginals and reflects contextuality one way (Thm IV.40); it is not a
  completeness result.

## Connections

- [THEORY-526](THEORY-526.md) is the ordinary obstruction this repairs on cycles, and
  [THEORY-012](THEORY-012.md) the exact criterion both relax.
- The thesis's Chapters VI–VII (All-vs-Nothing stabiliser groups reduce
  to three-qubit GHZ; no two-qubit or W-class state is strongly
  non-local) were not checked by the reading and are not filed.
