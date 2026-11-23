---
number: 192
status: Open
formerly:
- LEAD-tmpydsk9
title: 'Prove a projection perturbation bound for the coarse-graining claim, reading the biorthogonal diffusion wavelets first'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Note of 2026-11-23 added: the lead run of that date. The 2005
    biorthogonal report is Unfetched and its neighbour was read; the
    bound is proved for any T with norm at most one and filed as a
    Proposed claim, with a numerical check. The lead's status and stage
    are unchanged.
stage: idea
priority: medium
method:
- reading
- formal
tags:
- mathematics
- individuation
date: '2026-11-19'
line:
- distributed-agency
- formal-apparatus
advances:
- CLAIM-164
summary: >-
  Named in [NOTE-984](../notes.d/NOTE-984.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-tmpdsu37 LIT-tmpzikaq NOTE-tmpv196v THEORY-tmpyi9zg — new and Unfetched, filed by the lead run of 2026-11-23 and cited in the note of that date -->

# LEAD-192: Prove a projection perturbation bound for the coarse-graining claim, reading the biorthogonal diffusion wavelets first

## What it would do

Read the work on biorthogonal diffusion wavelets [NOTE-984](../notes.d/NOTE-984.md) names, then
attempt the bound.

Where the record names it:

- [NOTE-984](../notes.d/NOTE-984.md): "The biorthogonal diffusion wavelets (Maggioni, Bremer,
  Coifman and Szlam 2005) are the next reading."

## What would count

A bound gives [CLAIM-164](../claims.d/CLAIM-164.md) a demonstrated step.

## Note of 2026-11-23: run

Done by the lead run of 2026-11-23, branch
claude/lead-192-projection-bound; working notes in
scratch/studies/lead-192/PROGRESS.md.

- **The reading.** Maggioni, Bremer, Coifman and Szlam (2005) is
  registered as [LIT-tmpzikaq](../literature.d/LIT-tmpzikaq.md) and is Unfetched: CiteSeerX and the Wayback
  capture of Maggioni's Yale page reset the connection, and SPIE is
  paywalled. Its abstract was read on Duke's listing. Sevi, Rilling and
  Borgnat (2023), [LIT-tmpyklac](../literature.d/LIT-tmpyklac.md), which says its scaling functions are the
  report's, was skimmed in its place ([NOTE-tmpv196v](../notes.d/NOTE-tmpv196v.md), [THEORY-tmpyi9zg](../theory.d/THEORY-tmpyi9zg.md)).
  It gives the construction for directed graphs and no error bound.
- **The bound.** Proved, and filed as [CLAIM-tmpdsu37](../claims.d/CLAIM-tmpdsu37.md) (Proposed, thesis,
  demonstrated). For the chain A_{i+1} = P_{i+1}A_i²P_{i+1} from any T with
  ‖T‖₂ ≤ 1, the kept subspace is within (d_j + f_j)/σ_min(R^{2^j}) of any
  invariant subspace of its dimension, where d_j is the column residual
  and f_j the drift, and f_j accumulates at most by doubling per level
  plus the column and row residuals. For symmetric T this is
  (d_j + f_j)/λ_k^{2^j}, which with rank-revealing QR is a relative gap
  (λ_{k+1}/λ_k)^{2^j} plus drift. That is the demonstrated step for
  [CLAIM-164](../claims.d/CLAIM-164.md) this lead asked for.
- **The check.** scratch/studies/lead-192: numpy runs on four
  operators and nine pytest checks, all within the bound; tight with the
  true drift on the gapped clouds.
- **What remains.** Reading the 2005 report itself, if a copy can be
  reached. Whether the doubling in the drift bound is ever attained,
  which the check suggests it is not. A spectral reading of the levels
  for a non-normal T, where the denominator is σ_min(R^{2^j}) and the row
  residual must be controlled separately.
