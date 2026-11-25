---
number: 320
status: Proposed
formerly:
- CASE-tmpgfgy2
title: 'Bourrat''s individuality measures computed'
statement: >-
  Bourrat's interventional and coarse-graining individuality measures
  computed exactly on a minimal ecological-scaffolding model: the variance
  criterion falls as the scaffold is endogenised, the
  environment-conditioned coarse-graining error is zero for the patches
  throughout, and both pass collectives that are not transitions
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-167. Scripts,
    tests and results are under scratch/studies/lead-167/.
standing: documented
kind: executed-study
tags:
- individuation
- information-theory
- philosophy-of-biology
- causality
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-115
- QUESTION-118
draws_on:
- THEORY-424
- THEORY-607
summary: >-
  [LEAD-167](../leads.d/LEAD-167.md) asked for Bourrat's two individuality measures to be computed on
  a model of an evolutionary transition. Both were computed exactly, as the
  record's readings define them ([NOTE-027](../notes.d/NOTE-027.md), [NOTE-064](../notes.d/NOTE-064.md)), on a minimal
  ecological-scaffolding model: six cells in two patches, an external
  scaffold per patch, collective reproduction by recolonisation, and a
  parameter λ that moves the patch's cohesion from the scaffold to the cells.
  Of the 2024 measure ([LIT-005](../literature.d/LIT-005.md)), Â of the patch rises with λ and C2's
  variance falls to zero (0.028 to 0.000), from the least invariant
  candidate to the most; C1 passes every candidate at every λ. Of the 2023
  measure ([LIT-049](../literature.d/LIT-049.md)), δC|E is exactly zero for the patch partition and its
  24 refinements at every λ, so it registers the scaffold's partition before
  any endogenisation and never registers the endogenisation. Both pass
  counterfeits: a candidate that absorbs the external scaffold passes C2 at
  λ = 0, and in a common-input control with no interaction δC|E passes all
  203 partitions while Â ranks the environment-driven patch above a single
  cell. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: LIT-005 LIT-049 — Proposed; the measures computed here, and the reading whose promote_when the result bears on -->
<!-- inactive-ok-file: LIT-1940 — Deferred; Black et al.'s own model, named as not reproduced -->
<!-- inactive-ok-file: CLAIM-884 — new, filed with this case -->

# CASE-320: Bourrat's individuality measures computed

## What was done

The curation of 2026-09-26 (063703) said that Bourrat's two papers, [LIT-005](../literature.d/LIT-005.md)
and [LIT-049](../literature.d/LIT-049.md), "would be settled by a worked model: an explicit computation
of its individuality measure on a model of an evolutionary transition".
[LEAD-167](../leads.d/LEAD-167.md) asked for that computation. Neither paper computes its measure on
any system ([NOTE-027](../notes.d/NOTE-027.md), [NOTE-064](../notes.d/NOTE-064.md)).

**The measures, from the record's readings.**

- *2024* ([NOTE-027](../notes.d/NOTE-027.md)). Â = I(S′; Ŝ), computed by [NOTE-027](../notes.d/NOTE-027.md)'s correct route:
  first the do-channel p(s′ | do(s)) = Σ_e p(s′ | s, e) p(e), then its
  mutual information under a stated input distribution for Ŝ. C1 asks for
  Â_S2 / H(Ŝ2) ≥ [Â_S1 / H(Ŝ1)] at θ₀. C2 asks for low variance of
  Â_S2 | do(E2 = e) over the interventions e on E2. Krakauer et al.'s A*,
  A and nC are reported beside them.
- *2023* ([NOTE-064](../notes.d/NOTE-064.md)). δC is the gap between the truthful prediction (evolve
  the fine state, then average within blocks) and the projected one (average,
  then evolve the coarse state). It is computed in two versions: δC, and
  δC|E, which conditions the projection on the environment and takes the
  worst environmental state.

**Choices the readings leave open, made here.**

- *Input distribution for Ŝ* (fn. 4): uniform, the maximum-entropy convention
  of effective information. The population distribution is also reported,
  and it changes no verdict below.
- *Point prediction*: the conditional expectation of the block means. The
  error is the largest error over blocks (the paper's max-error reading),
  averaged over the stationary distribution.
- *Coarse model*: the best predictor from the coarse state under the
  stationary distribution.
- *Horizons*: 1 and 4 steps.
- *Candidates*: for δC, all 203 partitions of the six cells. For Â, seven
  subsets: a cell; a pair in one patch; the patch; the patch with its
  scaffold variable; a pair across patches; a triple across patches; all
  cells.
- *Two extensions, marked as not Bourrat's*:
  - a distributional δC, the total-variation distance between the two routes'
    predictive distributions;
  - an accuracy-plus-cost objective δC + κ·k, with k the number of blocks.
    This is [NOTE-064](../notes.d/NOTE-064.md)'s suggested repair, with [LIT-049](../literature.d/LIT-049.md)'s one-operation-per-entity
    cost.

**The model, and why this one.** [LIT-005](../literature.d/LIT-005.md) names Black et al.'s ecological
scaffolding as its intended setting, and its C2 is defined for that
scenario. Ecological scaffolding is therefore the most standard choice
here. Black et al.'s own model ([LIT-1940](../literature.d/LIT-1940.md)) is unread on the record, and it
is an individual-based simulation with no exact joint distribution. So it is
not reproduced. What is built is the scenario's skeleton, small enough for
exact information measures (256 states):

- *Cells and patches*: six binary cells in two patches of three.
- *Scaffold*: one external bit per patch, switching on and off on its own.
- *Collective reproduction*: imposed by recolonisation. With probability
  0.05 per step, one patch is refounded from a single cell of the other.
- *Each cell*:
  - keeps its trait with probability a = 0.3;
  - otherwise copies a random member of its own patch with probability
    g = r + (1 − r)λ, and a random member of the whole population otherwise;
  - is noisy with probability 0.05.

λ is the path through the transition:

- At λ = 0 the patch holds together only while its scaffold is present.
- At λ = 1 the cells hold it together whatever the scaffold does.

λ is swept as a parameter, not evolved. Two controls are added, in the
manner of [CASE-101](CASE-101.md)'s common-input arm: a patch whose cells simply copy their
patch's environment, with no interaction. The control is symmetric in one
version and asymmetric in the other.

Scripts, results and 9 passing tests are under
scratch/studies/lead-167/. The tests include [NOTE-027](../notes.d/NOTE-027.md)'s XOR counterexample
(A = 1 bit, Â = 0) and Bourrat's Fig. 2 common cause (A* > 0, Â = 0).

## Results

**Bourrat 2024: Â, C1, C2** (normalised Â = Â/H(Ŝ); C2 variance over all
interventions on E)

| λ | cell Â/H | patch Â/H | cross-triple Â/H | patch+scaffold Â/H | all cells Â/H | patch C2 var | cross-triple C2 var | patch+scaffold C2 var |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.145 | 0.166 | 0.151 | 0.203 | 0.174 | 0.0282 | 0.0129 | 0.0007 |
| 0.5 | 0.164 | 0.200 | 0.174 | 0.223 | 0.203 | 0.0098 | 0.0057 | 0.0001 |
| 0.875 | 0.179 | 0.229 | 0.192 | 0.242 | 0.230 | 0.0009 | 0.0015 | 0.0000 |
| 1 | 0.184 | 0.240 | 0.198 | 0.250 | 0.241 | 0.0000 | 0.0011 | 0.0000 |

- **Â tracks the transition, weakly.**
  - The patch's normalised Â rises with λ. Its lead over a cross-patch
    triple of the same size grows from 0.014 to 0.043.
  - Observational A* of the patch stays near 1 bit throughout (0.97 to
    1.04), while Â rises from 0.50 to 0.72.
- **C2 tracks it best.**
  - The patch's variance falls from 0.028 to 0, from the least invariant
    candidate (bar all cells) to the most invariant.
  - The ordering survives a in {0.1, 0.3, 0.5} and recolonisation in
    {0, 0.05, 0.2}.
  - C2 has no threshold, so it gives a ranking, not a verdict.
- **C1 does not discriminate.**
  - Against the cell at θ₀ = λ = 0 (0.145), every candidate passes at
    every λ, including the cross-patch pair (0.145 at λ = 0).
  - The cells' independent channels add, so any aggregate of cells meets
    the bar.
- **The scaffold can be bought into the candidate.**
  - The patch with its external scaffold variable has the highest normalised
    Â.
  - Its C2 variance is at most 0.0011 at every λ and parameter setting,
    λ = 0 included.
  - Â credits the scaffold's own persistence to the collective, so C2 is
    passed before any endogenisation by drawing the boundary round the
    scaffold.
- **The §7 rule picks the whole population.** "The coarsest grain in which
  Â is maximal" does not pick the patch. Raw Â grows with size, and at
  λ = 1 the normalised Â of all six cells (0.2409) edges the patch's
  (0.2404).
- **Common-input controls, with no interaction.**
  - Â is below A*, as Bourrat argues: 0.28 against 0.51 for the patch.
  - Â is not zero, because the cells keep their own trait.
  - It ranks the environment-driven patch above the cell (normalised 0.094
    against 0.059). It ranks a pair in one patch above a pair across patches
    (0.078 against 0.059), for every a.
  - The mechanism: marginalising the shared environment in the do-channel
    leaves the outputs correlated, and Â rewards grouping cells that share an
    unobserved common cause.
  - C2's variance is exactly 0 in the symmetric control, where the
    environment's two states mirror each other. In the asymmetric control it
    is 0.0085, as low as the scaffold model at λ = 0.5.

**Bourrat 2023: δC**

- **δC|E, his form for ecological confounds**, is exactly zero at every λ
  and both horizons, in both forms, for the patch partition and its 24
  refinements.
  - So the minimal δC is degenerate: the identity partition is always among
    the minima, as [NOTE-064](../notes.d/NOTE-064.md)'s C4 says.
  - The coarsest zero partition is the two patches at every λ < 1. At
    λ = 1, in the point form, it is the whole population, whose mean is a
    martingale.
  - δC|E registers the scaffold's partition from λ = 0 and is blind to
    endogenisation.
  - In the common-input controls, every one of the 203 partitions has δC|E =
    0 in the point form. That sharpens [NOTE-064](../notes.d/NOTE-064.md)'s C6: conditioning on the
    environment does not exclude the ecological case, it passes everything.
- **Unconditional δC.**
  - The patch partition's error falls along λ, from 0.030 to 0.019 to 0.011
    to 0, so in level it tracks endogenisation.
  - In rank it does not. The best partitions are balanced blocks across
    patches, which average out the hidden scaffold; the patches rank 17th to
    40th for λ < 1.
- **With a cost (the extension).**
  - *δC|E + κ·k* picks the patches for small κ at every λ < 1, and in the
    distributional controls too. Its κ window narrows from (0, 0.028] at
    λ = 0 to (0, 0.0055] at λ = 0.875. At λ = 1 it picks the whole
    population. The selected grain does not shift toward the collective as
    the transition proceeds.
  - *Distributional unconditional δC + κ·k* does shift. At λ ≤ 0.5, and in
    both controls, it picks the whole population for every κ. It picks the
    patches at λ = 0.75 (κ ≤ 0.001), λ = 0.875 (κ ≤ 0.0085) and λ = 1
    (κ ≤ 0.0195), at horizon 1. It does so more narrowly at horizon 4.

## Where the two agree and where they diverge

- **They agree** that the patch partition is the structure. Â/H ranks it
  above same-sized cross-patch candidates at every λ, and δC|E's coarsest
  exact partition is the patches.
- **They diverge on the transition.**
  - The interventional measure changes along λ as an ETI should: Â rises and
    C2's variance falls.
  - Bourrat's coarse-graining measure, in the form he gives for
    environmental confounds, is the same before and after.
  - Of the variants tried, only an unconditional, distributional,
    cost-priced δC moves with the transition. That is not Bourrat's
    criterion.
- **They diverge on the counterfeits.**
  - δC|E passes every partition of a population its environment
    reconstructs.
  - Â passes a collective that absorbs its external scaffold, and ranks an
    environment-driven patch above its cells.

## Limits

- One model, a skeleton of the scaffolding scenario and not Black et al.'s
  model. λ is swept, not evolved, so the onset of scaffolding is not
  modelled. Bourrat's sign for that onset, I(E1′; Ŝ1) rising, is reported
  in results.json and is roughly flat, but this model cannot test it.
- One trait, so the multi-trait version of δC is not tested.
- The cells are exchangeable within a patch. That is what makes the patch
  partition exactly lumpable given the scaffold. Heterogeneous cells would
  turn the exact zeros into small values. They would not change the
  rankings unless the heterogeneity were patch-aligned.
- Bourrat's θ and C2's "low" are unspecified, so verdicts are given as
  rankings and trends.
- The distributional δC and the cost objective are extensions. A
  total-variation distance across coarse spaces of different sizes is not
  strictly commensurable.
- The result is filed as [CLAIM-884](../claims.d/CLAIM-884.md).
