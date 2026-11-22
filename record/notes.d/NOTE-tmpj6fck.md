---
status: Skimmed
paper: LIT-2257
title: 'Kaur, Jain and Berman 2026, read for how slow behavioral states that organize fast movement are found, and why a wide gap between their rates hides them from a single-scale analysis'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-094 from the arXiv preprint
    (arxiv.org/pdf/2605.24135v1, 27 pp.), text extracted with pdftotext.
    Read: abstract, §I, §II (framework and diagnostic criteria), §III.A in
    part, §III.B (C. elegans) and §III.C (Drosophila) in full, and the
    opening of §IV. Skipped: Methods, the Lorenz control's details, the
    residence-time fits, the supplement; figures not viewed. Marked
    Skimmed for those parts. Quotations rechecked by script against the
    downloaded text. Read by the lead worker itself. No email address
    sent.
date: '2026-11-22'
summary: >-
  A method, not a dynamical model. Behavior is represented in a
  time-frequency space (wavelet amplitudes), a transfer operator is
  estimated on it, and its slow eigenvectors are read with the spectral
  theory of metastability: one linear arm per metastable basin, radiating
  from a hub. It recovers a hidden bistable driver of a Lorenz system, the
  run–pirouette split of worms, and four behavioral basins of flies that
  shift over minutes against leg movements at tens of hertz, with
  heavy-tailed residence times and memory beyond a four-state Markov
  model. Where the gap between fast and slow rates is wide, a fixed-scale
  operator finds no slow modes. The reading is [THEORY-tmpqdy16](../theory.d/THEORY-tmpqdy16.md).
---
<!-- inactive-ok-file: THEORY-tmpqdy16 — Proposed; this reading's account -->
<!-- inactive-ok-file: CLAIM-478 — Proposed; a claim the reading bears on -->

# NOTE-tmpj6fck: Kaur, Jain and Berman 2026, read for how slow behavioral states that organize fast movement are found, and why a wide gap between their rates hides them from a single-scale analysis

## Contribution

A route from raw postural time series to slow, metastable behavioral
states, by making timescale a coordinate of the state space. The reading
is [THEORY-tmpqdy16](../theory.d/THEORY-tmpqdy16.md).

## Key results

1. **The geometry** (abstract): "slow modes emerge as linear arms
   radiating from a stationary-weighted hub in the leading non-trivial
   eigenvectors of the transfer operator, with one arm per metastable
   basin across three systems of increasing complexity."
2. **What "slow" means here** (§II.A): "collective modes that are slow
   not because they are decoupled from fast dynamics, but because they
   persist across representations at different temporal resolutions."
3. **A wide gap hides the slow level** (§II, diagnostic criteria): on the
   worm data, with a modest fast–slow gap, the fixed-timescale operator
   also works; "On the fly data, where the gap is much larger, the
   fixed-timescale operator satisfies none of the criteria."
4. **Flies** (§III.C): four basins from 22 joint angles at 100 Hz, which
   map post hoc onto idle and slow, anterior, posterior and wing, and
   locomotion; "the dominant basin shifts gradually over timescales of
   minutes (Fig. 4E), which is orders of magnitude longer than individual
   postural movements". Predictive information between basins persists
   past 100 s where the fitted Markov model's decays by about 10 s.
5. **Heavy tails, not yet a mechanism** (§III.B, §IV): residence times are
   broad and best fit by truncated power laws, as a theory of slowly
   modulated barriers predicts; the authors say these "do not, however, on
   their own separate slow barrier modulation from simpler renewal
   statistics with a broad dwell marginal".

## Assumptions

The arms-and-hub geometry is proven for reversible chains; the operators
here are strongly non-reversible (about 58% of flux in net currents for
flies), so the geometry is used "operationally", checked by four
diagnostic criteria. The number of basins is chosen by the largest ratio
gap in the spectrum.

## Concepts

Transfer operator on a clustered state space; metastable basin; the
arms-and-hub geometry (PCCA+, G-PCCA); participation ratio of an
eigenvector; residence time.

## Bearing on the record

- **[QUESTION-281](../questions.d/QUESTION-281.md)** (bears on). Behavioral states as metastable basins
  between which an animal moves over minutes, with residence-time tails
  that suggest slowly modulated barriers; a measured case of distinctions
  that persist and give way, though the paper does not say by which
  transition.
- **[CLAIM-478](../claims.d/CLAIM-478.md)** (note only). The paper's premise is the claim's shape,
  slow internal states organizing fast movement, but it assumes the
  direction of constraint and does not test it. One point is new for the
  claim: the wider the gap between rates, the harder the slow level is to
  see from fast measurements at one resolution (key result 3). The
  separation that makes a level can hide it from a single-scale
  observer.
- **[CLAIM-331](../claims.d/CLAIM-331.md)** (note only). Slowness as a mark of a level is here an
  operational criterion for finding behavioral levels.

## Limitations

- A method paper; the slow states are found, not shown to constrain.
- Basin counts and arms depend on choices (frequency range, clusters,
  lag), set by data-driven criteria the paper reports.
- Heavy tails do not yet discriminate between mechanisms, by the authors'
  own account.
