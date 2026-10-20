---
number: 30
status: Active
formerly:
- THEORY-tmp83kni
title: "For a memory evolving reversibly with its environment, Landauer's bound prices only steps that lose logical distinguishability, at least k ln 2 of entropy per bit lost, exported to the environment and not necessarily as heat, so copying onto a blank register, measuring or evaluating a bit has no minimum cost; learning a label has a floor only in total entropy production, at least the information learnt, which in Goldt and Seifert's perceptron can be paid in the weights' own entropy with vanishing heat"
version: 3
history:
- version: 2
  date: '2026-10-01'
  note: >-
    Added to "What this does not say": the principle does not make
    maintenance free; a standing cost of holding structure only means the
    structure is dissipative, and error correction against noise is itself
    an erasure the principle prices.
- version: 3
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-030 (batch 047, ADR-047 v2): the promote_when asked for a
    derivation for stated dynamics, and the record now holds one (dated note
    below). The title is corrected where the derivation and its own source
    show it false: learning has a minimum cost in total entropy production
    (Goldt and Seifert's Eq. 16), and what has no floor is the heat. The
    open part of the promote_when (weaker assumptions, Earman and Norton,
    Landauer 1961) moves to QUESTION-tmpxmcgr.
tags:
- information-theory
- thermodynamics
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
  logical state, at least k ln 2 of entropy per bit exported to
  non-information-bearing degrees of freedom, which "need not" be heat.
  The record derives it for a memory and environment evolving reversibly
  from an uncorrelated start: the environment's entropy rises by at least
  the logical entropy lost, H(X | f(X)), and an injective step has no
  floor, attained exactly by a permutation. Goldt & Seifert ([LIT-308](../literature.d/LIT-308.md))
  bound information learnt by total entropy production, payable with
  vanishing heat in their toy model. It does not license a k_BT ln 2 heat
  floor per judgment, per gradient step or per bit learnt. Whether the
  bound survives without reversible dynamics is [QUESTION-tmpxmcgr](../questions.d/QUESTION-tmpxmcgr.md).
---
<!-- inactive-ok-file: LIT-328 — Unavailable; named as unread, nothing here quotes it -->

# THEORY-030: For a memory evolving reversibly with its environment, Landauer's bound prices only steps that lose logical distinguishability, at least k ln 2 of entropy per bit lost, exported to the environment and not necessarily as heat, so copying onto a blank register, measuring or evaluating a bit has no minimum cost; learning a label has a floor only in total entropy production, at least the information learnt, which in Goldt and Seifert's perceptron can be paid in the weights' own entropy with vanishing heat

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
- **That the principle is derived from weaker assumptions.** The record's derivation (dated note below) assumes reversible joint dynamics and an uncorrelated start. Bennett presents it as a restatement of the Second Law and gives no formal derivation. He concedes the Earman–Norton dilemma "with some justice" (p. 5). [LIT-114](../literature.d/LIT-114.md) §7.2 reports Norton's verdict that the Landauer literature is "too fragile" ([NOTE-103](../notes.d/NOTE-103.md)).
- **Anything about real hardware.** Bennett notes that real devices dissipate "far in excess" of the bound (p. 2). Fault-tolerant computation, where realistic per-step costs arise, he calls a subject "in its infancy" (p. 5).
- **Anything quoted as Landauer.** Landauer 1961 ([LIT-328](../literature.d/LIT-328.md)) is Deferred and unread. Bennett also gives its title wrongly.
- **That the three "temperatures" in the learning papers are k_BT.** McCandlish's ε/B ([LIT-348](../literature.d/LIT-348.md)), the Gibbs β ([LIT-347](../literature.d/LIT-347.md)) and the IB β ([LIT-338](../literature.d/LIT-338.md)) are formal analogies only ([NOTE-306](../notes.d/NOTE-306.md)).

## Connections

- [LIT-041](../literature.d/LIT-041.md) ([NOTE-032](../notes.d/NOTE-032.md)) prices work in a percept-action loop by the same kind of second-law bound, in k_BT ln 2 per round.
- The nostalgia bound of [LIT-327](../literature.d/LIT-327.md) is the subject of [THEORY-026](THEORY-026.md).

## Derivation (2026-10-20, promotion audit batch 047)

**Dynamics.** A memory M, whose logical state X takes finitely many values, each realized by internal microstates, and an environment E, every degree of freedom that bears no information (a heat bath among them). The joint microdynamics are reversible: a permutation of a finite joint microstate space, or a flow preserving Liouville measure. So the joint Gibbs–Shannon entropy S(ME) is conserved. M and E start uncorrelated, and every logical state has the same internal entropy before and after (a symmetric memory).

1. S(ME) after = S(ME) before = S(M) before + S(E) before.
2. Subadditivity: S(ME) after ≤ S(M) after + S(E) after.
3. So ΔS(E) ≥ −ΔS(M) = k[H(X before) − H(X after)], the internal-entropy terms cancelling, with H in nats.
4. For a logical map X ↦ f(X), H(X) − H(f(X)) = H(X | f(X)) ≥ 0, the distinguishability lost. Erasing a uniform bit loses ln 2, so ΔS(E) ≥ k ln 2. If E is a bath at temperature T this arrives as heat Q ≥ kT ln 2; if E is anything else, nothing forces heat, which is Bennett's "need not".
5. If f is injective on the states that occur (copying (x, 0) ↦ (x, x), measurement into a standard-state register, evaluation (x, 0) ↦ (x, f(x))), H is unchanged and the bound is ΔS(E) ≥ 0. It is attained: an injective map on the occurring states extends to a permutation of M's microstates (a controlled-NOT for the copy, a Toffoli gate for evaluation), applied with E untouched, so ΔS(E) = 0 exactly.
6. A many-to-one map on known data (X deterministic, H = 0) has no floor either, which matches Bennett's remarks that merging known data wastes the k ln 2 and that erasing one of two copies known to be equal costs nothing.

**Learning.** Goldt & Seifert's Eq. 16 (one weight, one label) integrates Horowitz's subsystem second law, d/dt S(ω) + Q̇ − l(ω; σ_T) ≥ 0, from an uncorrelated equilibrium start, giving ΔS(ω) + ΔQ ≥ I(ω : σ_T), and data processing gives I(σ_T : σ) ≤ I(ω : σ_T). So learning has a floor in total entropy production. The heat can be made small: [NOTE-296](../notes.d/NOTE-296.md) recomputed the toy model at ν = 8, τ = 10⁵, with 0.6885 nats learnt for ΔQ ≈ 0.0006 k_BT and ΔS(ω) = 0.6931. Horowitz's inequality is cited, not derived here, and holds to first order in 1/γ.
