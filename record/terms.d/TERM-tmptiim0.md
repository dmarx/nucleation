---
status: Proposed
title: 'sloppy, of a parametric model at a point and for an observation design: its Fisher information spectrum, in a declared chart, spreads over many decades with no gap that separates the parameter combinations that matter from those that do not; a graded property, distinct from ill-conditioning, from singularity and from a power-law spectrum'
version: 1
tags:
- information-geometry
- mathematical-statistics
- model-comparison
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
draws_on:
- THEORY-774
- THEORY-777
- THEORY-742
summary: >-
  At the owner's suggestion of 2026-11-21, after the filing of the
  exchange "Rich Get Richer Power Laws": "a TERM for the mathematical
  (information geometric?) sense of 'sloppy' might be merited". The record
  used the word in that sense in several entries ([TERM-tmp5z2du](TERM-tmp5z2du.md),
  [TERM-tmpnxjq4](TERM-tmpnxjq4.md), [CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md), [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md), [CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)) and in
  its readings of sloppy spectra ([THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md)), without
  defining it. A model is sloppy, at a parameter point and for a given
  observation design, when the eigenvalues of its Fisher information,
  in a declared chart (conventionally the logarithms of its bare
  parameters), spread over many decades, and no gap among them marks off
  the combinations that matter from those that do not. The term separates
  this from four neighbours: ill-conditioning (one ratio, which a single
  gap can produce), singularity (a zero eigenvalue on a stratum), the
  hyperribbon (the chart-free shape of the predictions, [TERM-tmp5z2du](TERM-tmp5z2du.md)),
  and a power-law spectrum (a sloppy spectrum falls by roughly a constant
  factor per rank, so it covers decades in proportion to the number of
  parameters). Its job is to let the record's entries on sloppiness,
  singular learning and effective dimension say which of these they mean.
  The source of the concept is Sethna and colleagues ([LIT-tmpsqbr9](../literature.d/LIT-tmpsqbr9.md),
  [LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), [LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md); their reading began on 2026-11-21 and is
  not yet filed). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmp5z2du TERM-tmpnxjq4 CLAIM-tmpcgvcp CLAIM-tmpficzj CLAIM-tmpcg4uu CLAIM-tmpj0k4q CLAIM-tmpym2vz THEORY-777 LIT-tmpsqbr9 LIT-tmpd3swn LIT-tmpm1tji LIT-tmpzkxka TERM-tmpyi882 — Proposed, Deferred or new; the entries this term defines a word for, and the unread works it comes from -->

# TERM-tmptiim0: sloppy, of a parametric model at a point and for an observation design: its Fisher information spectrum, in a declared chart, spreads over many decades with no gap that separates the parameter combinations that matter from those that do not; a graded property, distinct from ill-conditioning, from singularity and from a power-law spectrum

## Definition

Let a model map parameters θ ∈ ℝᵏ to predictions, observed with noise under a fixed design (which quantities, at which times or conditions, with what error). Its Fisher information at θ is g(θ); for least squares with unit noise, g = JᵀJ, with J the Jacobian of the predictions.

- **Sloppy.** The model is *sloppy* at θ, for that design, when the eigenvalues λ₁ ≥ … ≥ λₖ > 0 of g span many decades and are spread across them, each typically a decade or more below the last, with no single gap that splits them into a few that matter and a remainder that does not.
- **Stiff and sloppy directions.** The eigenvectors of the large eigenvalues are *stiff* directions; those of the small ones are *sloppy* directions. The adjective on the model refers to the whole graded spectrum, not to having some sloppy directions.
- **Graded.** There is no threshold in the concept. How many decades, and how even, are said when it matters. The literature's examples span six decades or more ([LIT-tmpsqbr9](../literature.d/LIT-tmpsqbr9.md), unread).
- **Relative to a chart.** Fisher eigenvalues are not invariant under reparametrization: under θ = Aφ the metric becomes Aᵀ g A. The convention is the logarithms of the bare parameters, so that the eigenvalues compare relative changes. A claim that a model is sloppy names its chart, or uses that convention.
- **Relative to a design.** More data or a different design can stiffen a direction. Sloppiness is of a model as observed, not of a model alone ([CLAIM-tmpj0k4q](../claims.d/CLAIM-tmpj0k4q.md): the number of resolved directions grows with data).

**Checked** with `python3 -I`, scratchpad script `sloppy_check.py`. A sum of k exponentials, with log-rate parameters, observed at 40 times with unit noise:
- k = 3: the eigenvalues span 1.9 decades;
- k = 5: 5.0 decades;
- k = 7: 8.8 decades.

The successive gaps are 0.6 to 2.3 decades and widen down the spectrum, so "spread" does not mean equally spaced. The same five-exponential model spans 6.1 decades in the chart of the bare rates, and 8.4 after rescaling three of them by 1, 10 and 100. So the count of decades depends on the chart.

## What it is not

- **Ill-conditioned.** The condition number λ₁/λₖ is one ratio. A spectrum (1, 0.9, 0.8, 0.7, 10⁻⁸) is badly conditioned but not sloppy: four eigenvalues sit within 0.15 decades and one gap of 7.9 decades does all the work (checked). It has a clean split into what matters and what does not, which is what sloppiness lacks.
- **Singular.** A sloppy model has g invertible, so every parameter is identified given enough data. A singular model has a zero eigenvalue on a stratum, and its learning coefficient differs from d/2 ([TERM-tmpnxjq4](TERM-tmpnxjq4.md), senses 4 and 5; [CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md)). The two meet near a stratum, where a sloppy eigenvalue goes to zero with the squared distance, and at finite n, where an unresolved sloppy direction counts like a flat one ([CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)).
- **A hyperribbon.** The hyperribbon is the shape of the set of predictions, whose widths fall roughly geometrically ([TERM-tmp5z2du](TERM-tmp5z2du.md)). That shape does not depend on the chart; the Fisher spectrum does. Sloppiness is the parameter-space face, the hyperribbon the prediction-space face. Their connection, that the widths follow the spectrum, is Transtrum, Machta and Sethna's ([LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md), being read).
- **A power-law spectrum.** A sloppy spectrum falls by roughly a constant factor per rank: geometric in the index. A power law in rank, λₙ ∝ n^(−α), falls ever more slowly. The checked contrast:

  | Eigenvalues | Geometric (ratio ½) covers | Power law (α = 2) covers |
  |---|---|---|
  | 10 | 2.7 decades | 2.0 decades |
  | 50 | 14.8 decades | 3.4 decades |
  | 200 | 59.9 decades | 4.6 decades |

  So a sloppy model with many parameters spans decades in proportion to the number of parameters, and a power-law spectrum spans them in proportion to the log of that number. The participation ratio behaves differently under each ([CLAIM-tmpym2vz](../claims.d/CLAIM-tmpym2vz.md) for the power-law case). Neither is "scale-free" in the sense of [TERM-tmpyi882](TERM-tmpyi882.md) without further conditions.
- **Unimportant.** A sloppy direction is one along which the predictions, as observed, change little. It says nothing of whether a task depends on it ([TERM-tmpnxjq4](TERM-tmpnxjq4.md)).

## Sources

- The concept and the word are Sethna and colleagues'. The source is the systems-biology survey of Gutenkunst and colleagues ([LIT-tmpsqbr9](../literature.d/LIT-tmpsqbr9.md)), the geometry is in Transtrum, Machta and Sethna ([LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md)), and the review is [LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md). All four were unread when this term was filed. The readings begun on 2026-11-21 of [LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md) and [LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md) are to check the definition here against theirs, and a note will record what they change.
- The record's readings of sloppy spectra are [THEORY-774](../theory.d/THEORY-774.md) (the hopping model, whose Fisher metric is given exactly), [THEORY-777](../theory.d/THEORY-777.md) (decimated critical Ising) and [THEORY-742](../theory.d/THEORY-742.md) (the Fisher information a coarse-graining loses).
- The separations from ill-conditioning, from a power-law spectrum and from the chart are the assistant's, checked as above.
