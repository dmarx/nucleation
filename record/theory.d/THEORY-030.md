---
number: 30
status: Proposed
formerly:
- THEORY-tmp83kni
promote_when: >-
  A derivation, for stated dynamics, that a many-to-one map of the logical
  state exports at least k ln 2 of entropy per bit of lost
  distinguishability while a bijective step (copy onto a blank register,
  measurement into a standard-state memory) has no positive floor. Bennett's
  argument is informal and cites its models rather than reproducing them.
  Landauer 1961 (LIT-328) read closely would add the original statement but
  not settle it. Agreement among position papers cannot settle it. It would
  be refuted by a demonstrated positive lower bound on the entropy cost of a
  logically reversible operation, or by an erasure of known data done with
  less than k ln 2 of entropy export per bit. A reading of the Earman–Norton
  dilemma that shows the principle to be circular would demote it to
  pedagogy, which Bennett already concedes it partly is.
title: 'Landauer''s principle prices only logically irreversible steps, and prices them in exported entropy rather than heat, so acquiring, copying or evaluating a bit, and learning it, carry no minimum thermodynamic cost'
version: 2
history:
- version: 2
  date: '2026-10-01'
  note: >-
    Added to "What this does not say": the principle does not make
    maintenance free; a standing cost of holding structure only means the
    structure is dissipative, and error correction against noise is itself
    an erasure the principle prices.
tags:
- information-theory
- natural-sciences
- learning-theory
- philosophy-of-science
date: '2026-09-30'
source:
- LIT-360
- LIT-308
- LIT-327
summary: >-
  Bennett (2003), [LIT-360](../literature.d/LIT-360.md): the cost attaches to many-to-one maps of the
  logical state (erasure, merging of control flow), and it is at least k ln 2
  of entropy exported per bit, which "need not" be heat. Goldt & Seifert
  ([LIT-308](../literature.d/LIT-308.md)) and Still et al. ([LIT-327](../literature.d/LIT-327.md)) agree. Information learnt is bounded
  by entropy production and can be paid almost entirely in weight entropy.
  The only per-bit heat term is Landauer's, on entropy removed. The synthesis
  across the three is the record's. It does not license a k_BT ln 2 heat
  floor per judgment, per gradient step or per bit learnt.
---

# THEORY-030: Landauer's principle prices only logically irreversible steps, and prices them in exported entropy rather than heat, so acquiring, copying or evaluating a bit, and learning it, carry no minimum thermodynamic cost

## Source

- Bennett (2003), [LIT-360](../literature.d/LIT-360.md), pp. 1–6, as read in [NOTE-310](../notes.d/NOTE-310.md).
- Goldt & Seifert (2017), [LIT-308](../literature.d/LIT-308.md), Eq. (16) and Supp. §II, as read in [NOTE-296](../notes.d/NOTE-296.md).
- Still, Sivak, Bell & Crooks (2012), [LIT-327](../literature.d/LIT-327.md), Eqs. (19)–(21), as read in [NOTE-295](../notes.d/NOTE-295.md).

## What was actually shown

**Bennett states the scope** ([NOTE-310](../notes.d/NOTE-310.md), C1, C2, C5, C7). A logically irreversible operation is a logical state with two or more predecessors, such as erasure or a merge in the flow of control. It must be matched by an entropy increase of at least k ln 2 per bit in the non-information-bearing degrees of freedom. Typically that increase is heat, but it "need not" be (p. 1). Bijective operations have no floor. These include copying onto a blank register, erasing one of two copies known to be equal, and measurement. Bennett calls the belief in "an intrinsic cost of order kT for every elementary act of information processing" a misconception (pp. 5–6). Erasure of random data can be thermodynamically reversible. Merging known data wastes the k ln 2, and reversible reprogramming could avoid that waste (pp. 1, 4).

**The two learning-thermodynamics results fit this scope, and neither goes beyond it.**

- *[LIT-308](../literature.d/LIT-308.md)* bounds the information a perceptron learns about fixed labels by the weights' total entropy production, ΔS(ω) + ΔQ (Eq. 16). In the paper's own toy model the bound is nearly saturated with almost no heat. [NOTE-296](../notes.d/NOTE-296.md) recomputed this: at ν = 8, τ = 10⁵, 0.689 nats are learnt for ΔQ ≈ 0.0006 k_BT, and ΔS(ω) carries the rest. The heat falls due when the weights are reset, which is Bennett's erasure.
- *[LIT-327](../literature.d/LIT-327.md)* has one information-proportional heat bound, on I_e, the conditional entropy removed from the system over a protocol (Eq. 19). This is the Landauer term. The rest of its accounting prices nonpredictive memory, not information held.

Three independent readings ([NOTE-295](../notes.d/NOTE-295.md), [NOTE-296](../notes.d/NOTE-296.md), [NOTE-310](../notes.d/NOTE-310.md)) arrive at the same account. Acquiring, copying and evaluating information have no minimum cost. Erasing or overwriting it costs at least k ln 2 of entropy per bit of lost distinguishability. That convergence is the record's synthesis, not a claim any one paper makes about the others.

## What this does not say

- **That there is a k_BT ln 2 heat floor per judgment, per gradient step, or per bit learnt.** The prior-art map's row 13 ("Q ≥ k_BT ln 2 · C_step") needs exactly that, and none of the three sources supplies it (curation 2026-09-29, 233704). The defensible form is k_BT ln 2 of entropy per predicate bit *erased or overwritten*.
- **That holding a structure costs nothing.** The principle is a lower bound on the cost of logically irreversible steps, not a claim that maintenance is free. A structure held away from equilibrium, as a living or noisy physical substrate must hold it, dissipates continually, and keeping information against noise requires error correction, which erases and so is itself priced here. A standing maintenance cost means the structure is dissipative; it is not in tension with this account. [NOTE-321](../notes.d/NOTE-321.md) first read it as one, and was corrected.
- **That the principle is derived.** Bennett presents it as a restatement of the Second Law and gives no formal derivation. He concedes the Earman–Norton dilemma "with some justice" (p. 5). [LIT-114](../literature.d/LIT-114.md) §7.2 reports Norton's verdict that the Landauer literature is "too fragile" ([NOTE-103](../notes.d/NOTE-103.md)).
- **Anything about real hardware.** Bennett notes that real devices dissipate "far in excess" of the bound (p. 2). Fault-tolerant computation, where realistic per-step costs arise, he calls a subject "in its infancy" (p. 5).
- **Anything quoted as Landauer.** Landauer 1961 ([LIT-328](../literature.d/LIT-328.md)) is Deferred and unread. Bennett also gives its title wrongly.
- **That the three "temperatures" in the learning papers are k_BT.** McCandlish's ε/B ([LIT-348](../literature.d/LIT-348.md)), the Gibbs β ([LIT-347](../literature.d/LIT-347.md)) and the IB β ([LIT-338](../literature.d/LIT-338.md)) are formal analogies only ([NOTE-306](../notes.d/NOTE-306.md)).

## Connections

- [LIT-041](../literature.d/LIT-041.md) ([NOTE-032](../notes.d/NOTE-032.md)) prices work in a percept-action loop by the same kind of second-law bound, in k_BT ln 2 per round.
- The nostalgia bound of [LIT-327](../literature.d/LIT-327.md) is the subject of [THEORY-026](THEORY-026.md).
