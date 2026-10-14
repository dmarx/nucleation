---
number: 272
status: Proposed
formerly:
- THEORY-tmplenr2
promote_when: >-
  A reading of the analytic treatment of the same model (Amit, Gutfreund
  and Sompolinsky 1985 and 1987, or an equivalent) or of a later
  simulation at N in the thousands, confirming that random patterns
  stored by Eq. 2 are attractors with basins of nonzero width up to a
  load near 0.14–0.15N, that recall then collapses for all patterns
  rather than degrading pattern by pattern, and that two patterns fuse
  once their overlap is high. It is refuted if the capacity scaling fails
  at large N, or if the large-N basins shrink to zero width at any load.
  A further simulation at N = 30 or 100 cannot settle it, since those are
  the sizes the claim already rests on.
title: 'A network of threshold units with symmetric Hebbian couplings is a content-addressable memory whose stored patterns are attractors, with limits: recall degrades near 0.15N random patterns, memories closer than about a tenth of N fuse, and overload loses every memory unless old ones are forgotten'
version: 1
tags:
- complex-systems
- neuroscience
- cognition
date: '2026-10-14'
source:
- LIT-918
summary: >-
  Hopfield (1982), [LIT-918](../literature.d/LIT-918.md), read in full in [NOTE-819](../notes.d/NOTE-819.md). The energy
  descent is derived for symmetric couplings; everything quantitative,
  including the 0.15N figure, the basin width and the merging distance,
  is simulation at N = 30 and 100. It does not say that spurious states
  come only from overload: they appear at a low load too. Nor does it say
  anything about addressed memory.
---
<!-- inactive-ok-file: CLAIM-179 CLAIM-180 — Proposed; open, and cited as open: the theses of the nucleating-argument line are under test, not settled -->

# THEORY-272: A network of threshold units with symmetric Hebbian couplings is a content-addressable memory whose stored patterns are attractors, with limits: recall degrades near 0.15N random patterns, memories closer than about a tenth of N fuse, and overload loses every memory unless old ones are forgotten

## Source

J. J. Hopfield (1982), *PNAS* 79:2554–2558, [LIT-918](../literature.d/LIT-918.md), read in full in
[NOTE-819](../notes.d/NOTE-819.md).

## What was actually shown

- **Derived.** For Tᵢⱼ = Tⱼᵢ and asynchronous threshold updates,
  E = −½ Σᵢ≠ⱼ TᵢⱼVᵢVⱼ changes by ΔE = −ΔVᵢ Σⱼ TᵢⱼVⱼ ≤ 0 at each update
  (Eqs. 7–8), so the state ends at a local minimum. With storage
  Tᵢⱼ = Σₛ (2Vᵢˢ − 1)(2Vⱼˢ − 1), a stored random pattern's local field has
  mean ±N/2 and crosstalk of rms [(n − 1)N/2]^½ (Eqs. 3–4, 10).
- **Simulated, N = 30 and 100.**
  - *Capacity.* "About 0.15 N states can be simultaneously remembered
    before error in recall is severe": at N = 100, five patterns are
    almost always stable; at fifteen, about half end within 5 bits and
    the rest far away (Fig. 2).
  - *Basins.* At N = 30, n = 5, a start within 5 bits of a memory reaches
    it more than 90% of the time, falling to 0.2 at 12 bits.
  - *Merging.* At N = 100, an eighth pattern placed 30 bits from another
    leaves both stable; at 20 the minima are displaced; at 10 they are
    "often fused".
  - *Overload.* Past capacity, new memories make "all memory states
    irretrievable unless there is a provision for forgetting"; saturating
    couplings keep the recent and lose the distant past.

Each simulated result could have come out otherwise: the stored patterns
need not have been stable, the basins could have been a bit wide, and
nearby patterns could have stayed distinct. The capacity figure was also
checked against the Gaussian estimate (predicted 0.40 perfect recall at
n = 10, N = 100; observed 0.6).

## What this does not say

- **It does not give a sharp capacity.** 0.15N is where about half the
  memories are well retained at these sizes. The paper expects it "for
  all large N" from the noise estimate, but shows it only at N ≤ 100.
- **Spurious states are not a symptom of overload.** At n = 5, N = 30, 10%
  of random starts end in "stable states of no obvious meaning". Reading
  them as what appears past capacity, as the record did before this
  reading, is wrong.
- **Merging and overload are different failures.** Fusion comes from two
  memories being close, at any load. Overload makes every memory
  unreachable, not merged.
- **Nothing about addresses.** The model stores by content only. Any
  contrast between retrieval by content and by code ([CLAIM-180](../claims.d/CLAIM-180.md)) needs
  another source; Kanerva's random-access-memory limit ([LIT-921](../literature.d/LIT-921.md)) is one.
- **Not a model of a brain, a person or a record.** Hopfield offers the
  biology as motivation. Readings of an argument record through it are
  analogy.

## Connections

- **[CLAIM-180](../claims.d/CLAIM-180.md)** rests on this model for its basin picture. This account
  supports that picture and corrects the claim's attribution of merging
  to capacity (see [NOTE-819](../notes.d/NOTE-819.md)).
- **[CLAIM-179](../claims.d/CLAIM-179.md)**: the overload result is the sharper form of the flooding
  analogy in [LIT-918](../literature.d/LIT-918.md)'s standing: loss of all memories, unless forgetting is
  provided.
- **[THEORY-261](THEORY-261.md)** (sparse distributed memory) states the related
  capacity for Kanerva's memory, which grows with the number of hard
  locations, not with N.
- **[THEORY-136](THEORY-136.md)** holds what evidence shows alternative stable states in a
  field system; this account is the designed case, where the attractors
  are written in.
