---
number: 272
status: Active
formerly:
- THEORY-tmplenr2
title: 'In Hopfield''s 1982 simulations at N = 30 and 100, a network of threshold units with symmetric Hebbian couplings acts as a content-addressable memory whose stored random patterns are attractors: recall degrades severely near 0.15N patterns, a pattern placed 10 bits from another at N = 100 often fuses with it, and at 25-fold overload no stored pattern stays stable'
version: 3
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-272 (batch 051, ADR-047 v3). Hopfield (1982) was read
    in full and gives its numbers in the text. The title is narrowed
    to his simulations at N = 30 and 100. The fusion clause is held to
    the one design at N = 100, and the overload clause to the measured
    case, no stored pattern stable at N = 100 and n = 500. The
    forgetting clause, reported only in words, is dropped. The dated
    note below checks the energy argument and the crosstalk estimate.
    The large-N request in the promote_when moves to
    QUESTION-201.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 069, ADR-047 v4) filed THEORY-800,
    Proposed, to carry what the narrowing dropped. This entry's status,
    title and claims are unchanged; a dated note says what moved.
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
extended_by:
- THEORY-800
---
<!-- inactive-ok-file: THEORY-800 — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->
<!-- inactive-ok-file: CLAIM-179 CLAIM-180 — Proposed; open, and cited as open: the theses of the nucleating-argument line are under test, not settled -->

# THEORY-272: In Hopfield's 1982 simulations at N = 30 and 100, a network of threshold units with symmetric Hebbian couplings acts as a content-addressable memory whose stored random patterns are attractors: recall degrades severely near 0.15N patterns, a pattern placed 10 bits from another at N = 100 often fuses with it, and at 25-fold overload no stored pattern stays stable

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

## Note of 2026-10-20: what was measured, and the two checks

Checked for the promotion audit (batch 051, [ADR-047](../decisions.d/ADR-047.md) v3).

1. **The energy argument.** Take V in {0, 1}, T symmetric and Tᵢᵢ = 0.
   Updating unit i changes E = −½ Σᵢⱼ TᵢⱼVᵢVⱼ by ΔE = −ΔVᵢ Σⱼ TᵢⱼVⱼ. The
   threshold rule raises Vᵢ only when that sum is positive and lowers it
   only when the sum is negative, so every change lowers E. The state
   space is finite, so asynchronous updating ends at a fixed point.
2. **The crosstalk estimate.** For a stored random pattern, the local field
   has a signal of ±N/2 and n − 1 noise terms. Each noise term is a sum of
   about N/2 terms of ±1, so the noise has rms [(n − 1)N/2]^½ (Eq. 10). At
   n = 10 and N = 100: σ ≈ 21.2, z ≈ 2.36, a bit errs with probability about
   0.009, and a perfect 100-bit recall has probability about e^−0.92 ≈ 0.40.
   That agrees with the paper; its simulation gave 0.6.
3. **What the title keeps.**
   - At N = 100, five patterns are almost always stable; at fifteen, about
     half are recalled within 5 bits.
   - At N = 30 with five patterns, a start within 5 bits of a memory
     reaches it more than 90% of the time.
   - At N = 100, an extra pattern 10 bits from another was "often fused"
     with it.
   - At N = 100 with n = 500, no stored pattern was stable.

   Whether 0.15N holds at large N, and how the fusion distance scales, is
   [QUESTION-201](../questions.d/QUESTION-201.md).

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 069) filed [THEORY-800](THEORY-800.md)
as Proposed, extending this entry. It carries Hopfield's large-N capacity of about 0.15N and his forgetting clause, which this entry's title carried before batch 051 narrowed it to his simulations at N = 30 and 100. This entry is its evidence and is not changed by the filing.
