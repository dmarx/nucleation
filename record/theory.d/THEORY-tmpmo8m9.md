---
status: Proposed
promote_when: >-
  A reading of Bergemann and Morris (2016a), "Bayes correlated equilibrium
  and the comparison of information structures in games" (Theoretical
  Economics 11(2)), in which its main theorem, the equivalence of
  individual sufficiency and the incentive order for many players, and the
  converse direction for one player are checked from the proof. The
  survey's statement of them does not suffice, and neither does the
  one-player inclusion re-derived below.
title: 'Giving players more information shrinks what an information designer can make them do: for one player, being more informative in Blackwell''s sense, being a garbling''s source and leaving a smaller set of Bayes correlated equilibria in every decision problem are the same order; for many players the incentive order is individual sufficiency, which neither implies nor is implied by sufficiency of the players'' joint information'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Proposed from NOTE-tmp3sq32. The survey states the three-way
    equivalence for one player and the many-player result in §4.2, citing
    Bergemann and Morris (2016a), and proves neither. One direction for
    one player, that a more informative prior structure gives a smaller
    BCE set, was re-derived below. The rest waits on the cited paper.
tags:
- game-theory
- information-theory
date: '2026-10-21'
source:
- LIT-tmp363mx
summary: >-
  Bergemann and Morris (2019), LIT-tmp363mx, read in NOTE-tmp3sq32, §4.2.
  A third face of Blackwell's order: the better-informed receiver is the
  harder one to steer. For many players the right order is not the
  statistical sufficiency of their joint information. Bayesian players
  only; for bounded ones a garbling can make a receiver easier to steer
  and easier to inform at once.
---
<!-- inactive-ok-file: THEORY-156 — Proposed; the reading of Blackwell's order this extends, cited as open -->
<!-- inactive-ok-file: CLAIM-199 CLAIM-326 — Proposed; the Blackwell line, named for comparison, cited as open -->

# THEORY-tmpmo8m9: Giving players more information shrinks what an information designer can make them do: for one player, being more informative in Blackwell's sense, being a garbling's source and leaving a smaller set of Bayes correlated equilibria in every decision problem are the same order; for many players the incentive order is individual sufficiency, which neither implies nor is implied by sufficiency of the players' joint information

## Source

Bergemann and Morris (2019), LIT-tmp363mx, §4.2, read in NOTE-tmp3sq32,
citing Bergemann and Morris (2016a) for the proofs. Blackwell (1951,
1953) for the first two orders.

## What was actually shown

In the survey, by statement only:

- For one player there is a "three way equivalence between (i) the 'more
  informative' ordering; (ii) the 'sufficiency' ordering; and (iii) the
  'incentive constrained' ordering". (i) ⇔ (ii) is Blackwell's theorem.
- For many players, "individual sufficiency" is equivalent to the
  incentive order. One structure is individually sufficient for another
  if some combination of the two makes each player's signal in the first
  a sufficient statistic for his beliefs about the state and the others'
  signals in the second. It "neither implies nor is implied by" joint
  sufficiency.
- The value of information in games is ambiguous because more
  information widens what players can condition on and narrows the
  incentive-compatible set. Common-interest games isolate the first, BCE
  the second.

**Re-derived here, one direction for one player.** Let the prior
structure S be a garbling of S′: a combined structure in which t is drawn
from t′ by a kernel independent of θ. Take any σ′ obedient for S′ and
define σ(a | t, θ) = Σ_{t′} σ′(a | t′, θ) P(t′ | t, θ). In the combined
structure t is independent of (θ, a) given t′, so for the receiver of
type t told a,

E[u(a, θ) − u(a′, θ) | t, a] = Σ_{t′} P(t′ | t, a) E[u(a, θ) − u(a′, θ) | t′, a] ≥ 0,

each term non-negative by obedience under S′. So σ is obedient under S
and induces the same joint law of (θ, a). Every outcome attainable when
the receiver knows more is attainable when it knows less.

What could have failed: a designer facing a less informed receiver could
have been unable to replicate a recommendation that used the receiver's
finer information. Simulating t′ from (t, θ), which an omniscient
designer can do, is what makes it possible.

## What this does not say

- **The converse is not checked.** That a structure not more informative
  admits, in some decision problem, an outcome attainable under it but
  not under the other, is stated, not shown here.
- **The many-player equivalence is not checked.**
- **Not for bounded receivers.** For a receiver restricted to a rule
  class, a garbling can raise what it can use (THEORY-tmpgz4cf), so the
  better-informed receiver need not be the harder one to steer.
- **Not for designers who cannot condition on the prior information.**
  The re-derivation simulates t′ from (t, θ).

## Connections

- **THEORY-156** is Blackwell's (i) ⇔ (ii). This adds (iii).
- **CLAIM-199 and CLAIM-326.** In the record's language: Blackwell's
  ceiling bounds what a receiver can do with a rendering, and the
  incentive order says the same ceiling bounds, from the other side, how
  far a designer can push a receiver who holds it.
- **THEORY-tmpetatd** gives the set this orders.
