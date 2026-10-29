---
status: Proposed
promote_when: >-
  An analysis of the Friedkin–Johnsen reflected-appraisal map (Eqs. 6, 9
  and 10 of LIT-1404) that finds its fixed points and their stability
  for strongly connected relative weights, showing that the autocratic
  fixed points attract almost every start, or a published simulation
  by others that reproduces the contrast with the DeGroot–Friedkin map
  on the same networks. A larger simulation by this record would not
  settle it.
title: 'Under reflected appraisal across issues, whether power concentrates in one member depends on the single-issue step: with Friedkin–Johnsen anchoring on initial positions almost every random strongly connected group evolves to a single leader, and with DeGroot consensus the same random complete networks keep power spread'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed from the reading of Friedkin's 2011/2012 paper (NOTE-tmpegm16),
    set beside the record's reading of Jia, MirTabatabaei, Friedkin and
    Bullo (LIT-1146, NOTE-1135, THEORY-916). Both halves were re-run on
    2026-10-29 in a scratch script that was not kept in the record:
    Friedkin's update as printed on 300 random complete networks each of
    sizes 5, 10 and 20, and on 300 random strongly connected networks of
    size 10 and density 0.4; and, on 100 random complete networks each
    of sizes 5 and 10, Friedkin's update and the DeGroot–Friedkin update
    from the same start. Proposed because the concentration result is
    shown only by simulation, Friedkin's and this record's.
tags:
- network-science
- complex-systems
date: '2026-10-29'
source:
- LIT-1404
- LIT-1146
summary: >-
  Friedkin (2011/2012), [LIT-1404](../literature.d/LIT-1404.md), and Jia et al. (2015), [LIT-1146](../literature.d/LIT-1146.md), use
  the same reflected-appraisal rule, the next self-weight set to the
  member's share of control over the last issue, and different
  single-issue steps. Friedkin's anchored step gives a single leader in
  over 98% of 100,000 random networks; the DeGroot step gives one
  non-autocratic equilibrium except on a star. A re-run on the same
  networks bears out the contrast. It does not say which step real
  groups follow, and Friedkin's experiment cannot tell.
---
<!-- inactive-ok-file: THEORY-916 — Proposed; the companion account, cited as open and not leaned on -->

# THEORY-tmpbnint: Under reflected appraisal across issues, whether power concentrates in one member depends on the single-issue step: with Friedkin–Johnsen anchoring on initial positions almost every random strongly connected group evolves to a single leader, and with DeGroot consensus the same random complete networks keep power spread

## Source

Friedkin, N. E. (2011). A formal theory of reflected appraisals in the
evolution of power. *Administrative Science Quarterly* 56(4), [LIT-1404](../literature.d/LIT-1404.md),
read in [NOTE-tmpegm16](../notes.d/NOTE-tmpegm16.md). Jia, P., MirTabatabaei, A., Friedkin, N. E. and
Bullo, F. (2015), [LIT-1146](../literature.d/LIT-1146.md), read in [NOTE-1135](../notes.d/NOTE-1135.md), whose result is
[THEORY-916](THEORY-916.md).

## What was actually shown

Both models fix the relative interpersonal weights C and, after each
issue, set member i's self-weight to their share of the total control
over that issue's outcome. They differ in how one issue is settled.

- **Friedkin–Johnsen, as [LIT-1404](../literature.d/LIT-1404.md) specifies it.** W = AC + I − A with A =
  diag(1 − w); y(t+1) = AWy(t) + (I − A)y(1), so each member stays
  anchored on their initial position; control V = (I − AW)⁻¹(I − A); the
  next self-weight is the column mean of V. In Friedkin's simulations,
  10,000 random systems for each of two types and five sizes from 5 to
  25, the share that evolves to a single leader is 0.9996–1.0000 for
  complete networks and 0.9900–0.9987 for networks with random zeros;
  the rest end with two members holding all control.
- **DeGroot, as [LIT-1146](../literature.d/LIT-1146.md) specifies it.** W = diag(x) + (I − diag(x))C;
  each issue goes to consensus, and control is W's dominant left
  eigenvector, which becomes the next x. Jia et al. prove convergence from
  every non-autocratic start to one equilibrium ordered by the
  eigenvector centralities of C, autocratic exactly when C is a star.
- **The re-run (2026-10-29).** Friedkin's update as printed: every one
  of 900 random complete networks (300 each of sizes 5, 10 and 20) ended
  with one self-weight above 0.99 and the rest below 0.01. On 300 random
  strongly connected networks of size 10 and density 0.4, 93% ended with
  a single leader and the rest with two. On 100 random complete networks
  each of sizes 5 and 10, from the same starting self-weights, Friedkin's
  update gave a median largest self-weight of 1.0 and the DeGroot–Friedkin
  update 0.29 and 0.13, never above 0.40.

What could have come out otherwise: the re-run could have failed to
reproduce Friedkin's Table 2, or the two updates could have agreed on
complete networks, where neither is a star.

## What this does not say

- **Not that real groups concentrate power.** Both are models. Friedkin's
  experiment tests one step of the rule over five issues, and it scores
  self-weights with the anchored model, so it cannot tell the two steps
  apart. Whether groups settle issues by anchored averaging or by
  consensus is the open empirical question.
- **Not which feature of the anchored step does the work.** In Friedkin's
  specification the self-weight enters twice, on W's diagonal and in the
  anchorage (I − A)y(1). Whether the anchorage alone gives autocracy, or
  only the double entry does, was not separated.
- **Not a proof.** Friedkin's result and the re-run are simulations on
  random weights. Neither excludes classes of C, such as sparse or
  structured networks, where the bilateral or other end states are
  common; the re-run's sparse case had bilateral ends in 7% of runs,
  against under 1% in Friedkin's Type 2.
- **Not that [THEORY-916](THEORY-916.md) is wrong.** Its result is for the DeGroot step,
  and the re-run agrees with it in direction on complete networks. The
  centrality ordering was not checked.

## Connections

[CASE-092](../cases.d/CASE-092.md)'s note of 2026-10-23 asks that a coupled meaning–influence model
be compared with "DeGroot–Friedkin" reflected appraisal. On this account
that is two baselines with opposite predictions, and the comparison
should name the single-issue step. [CLAIM-297](../claims.d/CLAIM-297.md)'s authority updated from
performance has the same shape as both rules.
