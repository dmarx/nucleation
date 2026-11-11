---
number: 1437
status: Active
formerly:
- THEORY-tmp07nzo
title: 'Cumberworth and Reinhardt review simulation results indicating that, in DNA origami, a staple''s later domains bind without a second translational entropy penalty once its first domain is bound, while each loop closed with the scaffold adds a penalty that depends on the order of binding, and that in the small designs simulated the first effect outweighs the second, so that staples tend to bind fully once started, while assembly is mostly downhill and needs no nucleation barrier, unlike DNA bricks'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the thirtieth status review (ADR-065), at the
    coordinator's ruling under the owner's delegation. The title was:
    "Cumberworth and Reinhardt review simulation results indicating that,
    in DNA origami, a staple's later domains bind without a second
    translational entropy penalty once its first domain is bound, while
    each loop closed with the scaffold adds a penalty that depends on the
    order of binding, so that in the small designs simulated staples tend
    to bind fully once started and assembly needs no nucleation barrier,
    unlike DNA bricks". Its "so that" derived the absence of a nucleation
    barrier from the loop effects, which the review does not do (kind 3,
    dated note).

    The promote_when was: "An experiment on a 2D DNA origami, resolving
    domains or staples during annealing (FRET, or oligomer inclusion),
    shows that most staples bind fully soon after their first domain binds,
    and that assembly proceeds without a measurable nucleation barrier." It
    moved word for word to QUESTION-445, which refines QUESTION-410.
    The source was read in full (NOTE-1626, Read), with the quoted passages
    checked against the text.
- version: 3
  date: '2026-11-11'
  note: >-
    bears_on QUESTION-445: the question says it holds "promotion condition formerly on THEORY-1437" (ADR-065), so
    the reading is its premise (ADR-060). The relation was never written
    when the condition moved; sweep of 2026-11-11, from the reading
    review by question. No other change.
tags:
- natural-sciences
- thermodynamics
- complex-systems
date: '2026-11-05'
source:
- LIT-2121
summary: >-
  Cumberworth and Reinhardt (2025), [LIT-2121](../literature.d/LIT-2121.md), read in full in [NOTE-1626](../notes.d/NOTE-1626.md)
  from the submitted version. Active as a report of the review's synthesis
  of coarse-grained simulations, mostly the authors' own, of small 2D
  designs. The authors note evidence that staples do not bind fully once
  started in a larger 3D-lattice-based design, and that their lattice
  model's loop costs are fixed only up to a constant. The experimental
  evidence on origami hysteresis they report is mixed. Whether experiment
  bears the account out is [QUESTION-445](../questions.d/QUESTION-445.md).
bears_on:
- QUESTION-445
---

# THEORY-1437: Cumberworth and Reinhardt review simulation results indicating that, in DNA origami, a staple's later domains bind without a second translational entropy penalty once its first domain is bound, while each loop closed with the scaffold adds a penalty that depends on the order of binding, and that in the small designs simulated the first effect outweighs the second, so that staples tend to bind fully once started, while assembly is mostly downhill and needs no nucleation barrier, unlike DNA bricks

## Source

Cumberworth and Reinhardt (2025), [LIT-2121](../literature.d/LIT-2121.md); read in full in [NOTE-1626](../notes.d/NOTE-1626.md).

## What was actually shown

- **Later domains** (§2.1). They bind "within the same overall structure, and there is no analogous loss of translational degrees of freedom upon bonding". Each, though, closes a loop whose entropic cost "depends on the order in which the staple domains bond to the scaffold".
- **The balance** (§2.1). "Simulations run with DNA origami-specific models have demonstrated that loop penalties do not outweigh the gains of intramolecular bonding, but do have a significant impact on the overall degree of cooperativity."
- **Full binding once started** (§§2.1, 2.3). "once a staple bonds with its first domain, it will typically bond fully before additional staples bond", in the small designs simulated.
- **No barrier for origami** (§2.3). Free-energy projections are "mostly downhill", reported as a separate free-energy result. Full binding is used to explain why no barrier is needed: partly assembled structures aggregate less, and blocking is rare. For bricks, by contrast, a barrier "is essential for the target structure to form in high yields" (§2.2).
- **Could have come out otherwise.** The simulations could have shown staples binding partially and interleaving, or origami needing a barrier as bricks do.

## What this does not say

- That it holds for large or 3D origami. The authors cite evidence that full binding fails in larger 3D lattice designs.
- That it is measured. It is a review of simulation.
- That the loop costs are quantitatively right. In the authors' lattice model they are fixed "up to some constant" (§3.3).
- That origami cannot have a barrier. One can be designed in by stacking, by a long loop-closing staple, or by toehold exchange.
- That blocking never matters. It is judged rare at typical concentrations, which leaves low concentrations open.

## Note of 2026-11-06: reader J, the connective

The old title ran "so that … staples tend to bind fully once started and assembly needs no nucleation barrier", deriving both results from the balance of translational and loop entropy.

The review ties only full binding to that balance: loop penalties "do not outweigh the gains of intramolecular bonding" (§2.1). It reports downhill, barrier-free assembly as a separate free-energy result (§2.3). It then uses full binding to explain why no barrier is needed: partly assembled structures aggregate less, and blocking is rare. The title now keeps the two apart.
