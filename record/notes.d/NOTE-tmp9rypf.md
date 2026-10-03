---
status: Read
paper: LIT-tmp8o0fr
title: 'Cross-region neuron co-firing mediated by ripple oscillations'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the publisher's open-access PDF (CC BY-NC-ND 4.0).
    Main text, Figs. 1–6, Discussion, Methods and Extended Data captions
    read. Plotted values were not recoverable from the text layer, so
    every number below is one the text or a caption states. The
    Supplementary Information and the source data were not read. Results
    the paper takes from the original dataset paper (Daume et al.) and
    from earlier co-ripple studies are taken as it reports them.
date: '2026-10-03'
summary: >-
  In 35 patients (43 sessions, 1,373 units) doing a Sternberg task, ripple
  co-occurrence between bundles is about 5% at every distance from 71 to
  223 mm, and unit pairs co-fire a median 34% more during co-ripples than
  in no-ripple periods (n = 31,489 pairs), 117% more by rate-corrected
  STTC. Load 3 raises co-ripple co-firing 13% (maintenance) and 19%
  (retrieval) over load 1. Encoding co-firing recurs at retrieval in 0.29%
  of cell-pair trials in co-ripples versus 0.14% outside them, 0.36%
  versus 0.23% for fast versus slow load 3 responses.
---

<!-- inactive-ok-file: LIT-385 — Deferred: Damasio's convergence-zone proposal is unread; named as an analogy, no relation claimed -->
<!-- inactive-ok-file: THEORY-063 — Proposed; named as an account this reading bears on only weakly, no support claimed -->
<!-- inactive-ok-file: LIT-tmpqw727 — Deferred, paywalled; named for contrast as the traveling-wave review in the same batch -->

# NOTE-tmp9rypf: Cross-region neuron co-firing mediated by ripple oscillations

## Contribution

Earlier work showed that human cortical ripples co-occur across large
distances in the LFP, and that they raise co-firing between nearby
neurons. This paper puts single units and LFP from five bilateral
forebrain regions together during a working-memory task. It shows that
the co-firing boost reaches distant and cross-hemisphere pairs with no
loss over distance, that it scales with memory load, and that co-ripples
carry stimulus-specific co-firing from encoding into retrieval.

## Key insight

Long-range coordination need not be a signal sent along a path. If
distant sites tend to burst at about 90 Hz at the same moments, those
moments become shared windows in which spikes at both sites are more
likely to coincide. The windows open more when the task is harder, and
what coincides in them at retrieval is more often the same pairing that
coincided when the item was seen. Because the effect does not fall off
with distance, the authors read it as a property of the network as a
whole rather than of point-to-point transmission.

## Assumptions

- **Dataset**: the open Daume et al. dataset (DANDI 000673), 35 of its
  patients (one excluded for lack of clean LFP), 43 sessions, Behnke–Fried
  microwires in vmPFC, ACC, preSMA, amygdala and hippocampus, bilaterally,
  placed for clinical reasons in patients with refractory epilepsy.
- **Task**: modified Sternberg, 140 trials per session, load 1 or load 3
  images, 2.5–2.8 s maintenance, then a probe. Mean accuracy 93%, so error
  trials were too few to analyse.
- **Ripple definition** (Methods): 70–100 Hz band, at least three cycles,
  peak z above 2.5, events merged within 25 ms; rejected near large
  deflections and epileptiform activity; channel averages and co-ripples
  visually reviewed. Spike waveforms were subtracted from the raw signal
  before LFP processing.
- **Co-ripple**: at least 25 ms overlap between ripples on two bundles.
  **Co-firing**: spikes of two units within 25 ms. Co-firing analyses keep
  pairs with baseline co-firing of at least 0.025 Hz (12,335 of 16,274).
- **Distance** is population-average tractography streamline length
  between atlas parcels assigned to each region, not measured per patient.
- **Statistics**: permutation tests of medians, linear mixed effects with
  patient as random effect (Rate ∼ Load + (1|Patient)), FDR correction,
  χ² tests for repetition rates.

## Key results

- **Ripples everywhere.** Per-region density about 0.51–0.55 per second,
  duration about 69–75 ms, frequency about 91 Hz (Fig. 1f–i). Ripple rates
  rise over baseline in all regions in every task phase, by 13% in
  encoding and 10% in maintenance on average, and by 36% in preSMA at
  retrieval (Fig. 2a).
- **No decline with distance.** Co-occurrence is a median 13% within a
  bundle and 5% (IQR 4–6%) between bundles, and cross-hemisphere rates
  differ from within-hemisphere ones by 0.1 percentage points (Fig. 1j).
  The co-ripple co-firing gain rises slightly with distance (r = 0.04).
- **Co-firing.** Across 31,489 pairs, co-firing is a median 34% higher in
  co-ripples than in no-ripple periods; median gains by pathway are 49%
  (amygdala–cortex), 21% (hippocampus–cortex), 43% (amygdala–hippocampus),
  42% (cortex ipsilateral) and 44% (cortex contralateral) (Fig. 1k).
- **Not rate alone.** Co-firing above an independent-firing null
  (rate_A × rate_B × 2Δt) is 0.059 Hz in co-ripples against 0.038 Hz
  outside them; STTC is 0.023 against 0.011, 117% higher (n = 26,005
  pairs; Extended Data Fig. 3).
- **Task stages.** Against baseline, co-ripple co-firing rises 28%, 29%
  and 24% in encoding, maintenance and retrieval; no-ripple co-firing
  changes by +1%, −3% and −4% (Fig. 4).
- **Load.** Co-ripple co-firing is 13% (maintenance) and 19% (retrieval)
  higher at load 3; no-ripple co-firing changes by −1% and −0.2%
  (Fig. 5). Ripple-band co-occurrence shows load modulation in 12 of 15
  pairs at retrieval, low gamma in 2 and very high gamma in 0. Amplitude
  envelope correlations show no robust load effect in any band (Extended
  Data Fig. 9).
- **Speed.** Hippocampal and amygdala ripple rates after the probe are
  higher on fast than slow load 3 trials, and hippocampal ripples lead
  amygdala ripples (379 versus 473 ms).
- **Reinstatement.** Encoding-to-retrieval repetition of a pair's
  stimulus-specific co-firing: 0.29% of cell-pair trials in co-ripples
  versus 0.14% in no-ripple periods (χ² = 213.9); 0.36% versus 0.23% for
  fast versus slow load 3 match trials (χ² = 57.5). Matching co-firing
  clusters around co-ripple centres more than around single-site ripples
  or shuffled spikes (Fig. 6c,d). A stimulus-label shuffle within
  co-ripple periods is the control for excitability (Methods).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Ripple co-occurrence between human forebrain sites does not decline with distance beyond the local bundle, up to about 220 mm and across hemispheres | strong for these five regions | Fig. 1j; tract lengths are atlas averages |
| C2 | Co-ripples raise cross-region co-firing beyond what the concurrent rise in firing rate predicts | strong | Extended Data Fig. 3 (two rate-corrected measures) |
| C3 | Co-ripple co-firing scales with working-memory load, more than co-firing outside ripples or co-occurrence in other high-frequency bands | moderate: one task, two load levels | Figs. 3, 5 |
| C4 | Co-ripples hold more stimulus-specific reinstatement of encoding co-firing at retrieval, more on fast trials | moderate: rates are small (fractions of a percent), effects significant by χ² on very large counts | Fig. 6, Extended Data Fig. 10 |
| C5 | Co-ripples are a general mechanism for integrating distributed representations in human cognition | weak: an interpretation | Discussion; one task, clinically placed electrodes, no causal manipulation |
| C6 | Distance invariance indicates an emergent network of coupled oscillators rather than directed transmission | weak: argued from cited models | Discussion |

## Concepts

- **ripple**: a 70–100 Hz oscillatory burst of at least three cycles,
  detected per microwire (Methods).
- **co-ripple**: ripples on two bundles overlapping by at least 25 ms.
- **co-firing**: spikes from two units within 25 ms of each other.
- **STTC (spike time tiling coefficient)**: a pairwise synchrony measure
  corrected for firing rate, bounded between −1 and 1.
- **co-firing repetition**: a cell pair that co-fired during encoding of a
  stimulus co-firing again during retrieval of the same stimulus.

## Connections

- **Xu et al. 2023 ([LIT-tmpkkvdo](../literature.d/LIT-tmpkkvdo.md)) and Muller et al. 2026 ([LIT-tmpqw727](../literature.d/LIT-tmpqw727.md)).**
  Both place large-scale coordination in propagating waves, phase gradients
  across cortex. This paper places it in brief synchronous bursts at
  distant sites with no measured direction of travel. Neither study tests
  the other's mechanism, and they work at very different timescales
  (0.01–0.1 Hz fMRI against 90 Hz LFP).
- **Damasio 1989 ([LIT-385](../literature.d/LIT-385.md)).** Recall as time-locked multiregional
  re-activation of encoding activity is the shape of C4. The paper does
  not cite it, and [LIT-385](../literature.d/LIT-385.md) is unread; the analogy is mine.
- **Kelso 2021 ([LIT-601](../literature.d/LIT-601.md)).** Zero-lag locking of coupled oscillators is
  the regime HKB and its Kuramoto extension describe for relative phase.
  The paper's coupled-oscillator account (C6) cites other models.

## Bearing on the record

- **[THEORY-063](../theory.d/THEORY-063.md)** takes phenomenal unity to be one global functional
  cluster. This reading shows a single-neuron-level integrating mechanism
  across hemispheres in working memory, not unity of experience; it neither
  supports nor tests the theory.
- It supplies one source for a candidate theory: that long-range
  coordination in the human forebrain is carried by transient synchronous
  high-frequency events whose effect does not decay with distance. That
  theory is proposed, not filed.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Correlational.** Ripples are detected, never perturbed. The authors'
  own Methods say ripple rates explain only about 5% of firing-rate
  variance in maintenance and retrieval, and that ripples "modulate but do
  not completely determine" firing.
- **One dataset, one task, two loads.** The authors call the load range
  narrow and ask for other paradigms before calling ripples a general
  cognitive mechanism.
- **Clinical sampling.** Five regions, no posterior parietal cortex, in
  patients with epilepsy; epileptiform periods and seizure-onset contacts
  were excluded.
- **Small absolute effects.** Repetition rates are below half a percent of
  cell-pair trials; significance comes from very large counts.
- **Distance is not measured per patient**, but taken from population
  tractography between parcels.
- **Partial overlap of the rate controls.** STTC is computed only for
  pairs with co-firing in both conditions, because co-ripple time per
  recording is only about 45 s.

## Open questions

- Does disrupting co-ripples (for example by closed-loop stimulation)
  remove the load effect and the reinstatement advantage?
- How do co-ripples relate to the theta–gamma coupling the same dataset
  shows in hippocampal neurons?
- Is the distance invariance kept in posterior and sensory cortex, which
  this sample omits?

## Corrections

- none to a seeded skim (there was no seed)
- **Abstract against Results.** The abstract's "~30%" co-firing increase
  matches the task-stage figures (24–29% over baseline); the all-pairs
  co-ripple versus no-ripple median is 34%.
