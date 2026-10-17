---
number: 716
status: Active
formerly:
- THEORY-tmpims74
title: "Synergy can be measured as the whole minus the union of its parts, the union information being the least information the sources could jointly carry about the target with every source–target marginal held fixed; this synergy lies between WholeMinusSum and Williams and Beer's S_max, which respectively subtract redundancy and count unique information as synergy, and for two sources it is Bertschinger et al.'s synergy, so independent sources can share information about a target, as the authors' last version concedes against their first"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-1204
summary: >-
  Griffith & Koch (2014), [LIT-1204](../literature.d/LIT-1204.md), read in full in [NOTE-966](../notes.d/NOTE-966.md), v6
  with v1–v2 checked. The definitions, the criticisms of S_max, WMS and ΔI,
  and the properties proved in Appendix C are exact, and every Table 1
  value for two predictors was recomputed. The identification with
  Bertschinger et al.'s CI for two sources is the record's derivation.
  Monotonicity is claimed without proof, and the S_max bound's proof has
  a step the reading could not reconstruct.
---

# THEORY-716: Synergy can be measured as the whole minus the union of its parts, the union information being the least information the sources could jointly carry about the target with every source–target marginal held fixed; this synergy lies between WholeMinusSum and Williams and Beer's S_max, which respectively subtract redundancy and count unique information as synergy, and for two sources it is Bertschinger et al.'s synergy, so independent sources can share information about a target, as the authors' last version concedes against their first

## Source

Griffith & Koch (2014), "Quantifying synergistic mutual information",
arXiv 1205.4265v6 (Guided Self-Organization: Inception, Springer),
[LIT-1204](../literature.d/LIT-1204.md), read in full in [NOTE-966](../notes.d/NOTE-966.md). v1 and v2 were read for the
passage v6 withdraws. The book chapter was not compared.

## What was actually shown

**The measure.** I_VK = min I*(X_1…n : Y) over Pr* with every
Pr*(X_i, Y) fixed; S_VK = I(X_1…n : Y) − I_VK (Eqs. 13–14). The product
Pr(y)ΠPr(x_i|y) is feasible and bounds I_VK above.

**Against the prior measures (Table 1, recomputed).** S_max gives Unq 1
bit of synergy, where there are two unique bits. WholeMinusSum gives
RdnXor 0, one bit of synergy minus one of redundancy. ΔI gives AND 0.104,
below WholeMinusSum's 0.189, and AndDuplicate 0.038. S_VK gives the
intended answer wherever one is stipulated.

**Properties.** Proved: global positivity, self-redundancy, weak
symmetry, weak local positivity for two sources, strong identity
I_VK(X : X_1…n) = H(X_1…n). Claimed without proof: monotonicity, target
monotonicity. Disproved: strong symmetry.

**Two sources.** The constraint set is Bertschinger et al.'s Δ_P, and
H(Y) is fixed on it, so minimising I*(X_1X_2 : Y) is their maximisation
of H(Y | X_1X_2). S_VK is their CI. For AND that gives 0.5 bit of
synergy and 0.311 of redundancy, the top of the paper's open interval
[0.270, 0.5]. The record's derivation, checked numerically.

**The reversal.** v1–v2 give AND zero redundancy "because X1 and X2 are
independent". v6 calls that an error and bounds AND's redundancy below
by 0.082.

What could have come out otherwise: I_VK's bound could have failed to
separate AND's synergy from WholeMinusSum's 0.189. It gives at least
0.270.

## What this does not say

- **That S_VK is the right synergy.** The test is stipulated intuition on
  circuits, and AND's answer was left open.
- **Anything settled for three or more predictors.** I_VK is defined for
  any n and keeps strong identity, but nonnegativity of the induced
  atoms and monotonicity are not proved there, and the authors say they
  were blocked.
- **That independent sources must share information.** v6 says they can
  under this measure; whether they should is the dispute between
  [THEORY-708](THEORY-708.md) and [THEORY-715](THEORY-715.md).

## Connections

- For two sources it coincides with [THEORY-705](THEORY-705.md), which supplies the
  proofs of nonnegativity and identity this paper lacks there.
- It corrects the S_max built from Williams and Beer's I_max ([LIT-1172](../literature.d/LIT-1172.md))
  on unique information, as [THEORY-708](THEORY-708.md) corrects [THEORY-706](THEORY-706.md)'s I_min on
  shared information.
- [THEORY-715](THEORY-715.md) formalises the v1 position this version withdraws.
