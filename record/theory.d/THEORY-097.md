---
number: 97
status: Proposed
formerly:
- THEORY-tmpkyk0k
promote_when: >-
  A causal result and a second paradigm. The causal one: co-ripples
  disrupted or induced (closed-loop stimulation timed to ripples, or a
  matched sham) at distant forebrain sites, with the effect measured on
  cross-region co-firing, on its load dependence and on reinstatement at
  retrieval. The account is refuted if removing co-ripples leaves
  long-range co-firing and reinstatement unchanged, or if the co-firing
  gain falls off with distance in a sample that covers posterior parietal
  and sensory cortex, which this one omits. The second paradigm: the same
  co-ripple co-firing effects in a task other than a Sternberg recognition
  task, or across a load range wider than one versus three items. More
  correlations from the same open dataset (DANDI 000673) cannot settle it,
  and nor can further reports that ripples co-occur in the LFP, since that
  much was known before LIT-633.
title: 'Long-range coordination in the human forebrain is carried by brief ripples that co-occur at distant sites: during them neurons co-fire more whatever the distance between them, and at retrieval they carry stimulus-specific reinstatement of encoding co-firing'
version: 1
tags:
- neuroscience
- cognition
- network-science
date: '2026-10-03'
source:
- LIT-633
summary: >-
  Verzhbinsky, Daume, Cheng, Rutishauser & Halgren (2026), [LIT-633](../literature.d/LIT-633.md):
  in 1,373 single units from five bilateral forebrain regions of 35
  epilepsy patients doing a Sternberg task, ripples (70–100 Hz, about
  70 ms) co-occur between bundles at a median 5% at every tract distance
  from 71 to 223 mm, and unit pairs co-fire a median 34% more during
  co-ripples than in no-ripple periods, beyond a rate-only null and with
  no loss over distance. The gain rises with load (13% in maintenance, 19%
  at retrieval), and encoding co-firing for a stimulus recurs at retrieval
  in 0.29% of cell-pair trials in co-ripples against 0.14% outside them.
  Correlational throughout: one task, two load levels, clinically placed
  electrodes, nothing perturbed.
---
<!-- inactive-ok-file: THEORY-088 — Proposed; filed in the same batch, named for contrast, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-063 — Proposed; named in Connections as an account of integration this one does not test, no relation claimed -->
<!-- inactive-ok-file: LIT-385 — Deferred, unread; Damasio's convergence-zone proposal, named as the older idea the reinstatement result resembles, no relation claimed -->
<!-- inactive-ok-file: LIT-647 — Deferred, unread; the traveling-wave review, named for contrast, nothing here rests on it -->

# THEORY-097: Long-range coordination in the human forebrain is carried by brief ripples that co-occur at distant sites: during them neurons co-fire more whatever the distance between them, and at retrieval they carry stimulus-specific reinstatement of encoding co-firing

## Source

- Verzhbinsky, Daume, Cheng, Rutishauser & Halgren (2026), [LIT-633](../literature.d/LIT-633.md),
  read in full in [NOTE-494](../notes.d/NOTE-494.md): Figs. 1–6, Extended Data Figs. 3, 9 and
  10, the Methods on ripple, co-ripple and co-firing definitions, and the
  Discussion and Limitations.

## What was actually shown

**The data.** Verzhbinsky et al. ([LIT-633](../literature.d/LIT-633.md)) reanalyse an open dataset:
35 patients with refractory epilepsy, 43 sessions, Behnke–Fried microwires
placed for clinical reasons in hippocampus, amygdala, vmPFC, ACC and
preSMA of both hemispheres, during a Sternberg working-memory task with
load 1 or load 3. A ripple is a 70–100 Hz burst of at least three cycles;
a co-ripple is ripples on two bundles overlapping by at least 25 ms;
co-firing is spikes from two units within 25 ms.

**Distance does not matter.** Ripples occur at about 0.5 per second in
every region, last about 70 ms and peak near 91 Hz. Between bundles they
co-occur at a median 5% (13% within a bundle), and the rate barely changes
with population-average tract length from 71 to 223 mm, ipsilateral or
contralateral. Across 31,489 unit pairs, co-firing is a median 34% higher
during co-ripples than when neither site ripples; the abstract's "~30%"
is the task-stage figure. The gain is about as large for contralateral
cortical pairs (44%) as for ipsilateral ones (42%), and rises slightly, not
falls, with distance (r = 0.04).

**It is not just more spikes.** Against an independent-firing null,
co-firing is 0.059 Hz in co-ripples against 0.038 Hz outside them, and the
rate-corrected spike time tiling coefficient is 117% higher (Extended Data
Fig. 3). This is the result that could most easily have come out the other
way: if ripples only raised excitability, the rate-corrected measures
would not move.

**It tracks load.** Load 3 raises co-ripple co-firing over load 1 by 13% in
maintenance and 19% at retrieval, against about zero outside ripples.
Ripple-band co-occurrence is load-modulated in 12 of 15 region pairs at
retrieval, low gamma in 2 and non-oscillatory very high gamma in none.

**It carries content.** A cell pair that co-fired when a stimulus was
encoded co-fires again when that stimulus is retrieved in 0.29% of
cell-pair trials during co-ripples, against 0.14% in duration-matched
no-ripple periods, and in 0.36% against 0.23% for fast and slow load 3
responses (Fig. 6). A stimulus-label shuffle inside co-ripple periods
controls for excitability.

## What this does not say

- **It does not say ripples cause the coordination.** Nothing was
  perturbed. The authors' own Methods say ripple rates explain only about
  5% of firing-rate variance in maintenance and retrieval, and that
  ripples "modulate but do not completely determine" firing. "Carried by"
  in the title is the paper's reading of a correlation, and is what the
  `promote_when` asks to be tested.
- **It does not say ripples are a general cognitive mechanism.** The
  evidence is one task with two load levels, and the authors themselves
  ask for other paradigms and a wider range of difficulty before calling
  it general.
- **It does not say most of the time is co-rippling.** Co-occurrence is a
  few percent; co-ripple time per recording is about 45 s. The
  reinstatement effect is a fraction of a percent of cell-pair trials,
  significant because the counts are very large.
- **It does not cover the whole forebrain.** Five regions, no posterior
  parietal or sensory cortex, in patients with epilepsy, and distances are
  atlas averages, not measured per patient.
- **It does not establish the coupled-oscillator mechanism.** That distant
  sites lock at zero lag despite conduction delays because many pathways
  join them is argued in the Discussion from cited models and not tested.

## Connections

- **Integration and the workspace.** The authors say that the "general
  lack of evidence for integration of neuronal firing over wide expanses of
  association cortex" has challenged workspace-type theories, and offer
  this as evidence for "an essential component of that process". That is
  a claim about cognitive integration in working memory, not about
  experience.
- **[THEORY-063](THEORY-063.md).** That account takes phenomenal unity to be the
  integration of one world-model into a single functional cluster, with
  the neural level borrowed from the dynamic-core hypothesis. Co-ripples
  are one measured mechanism by which distant neurons could form such a
  cluster, but nothing here measures whether they go with experience being
  unified, and a cluster of maximal causal density is not a 5% co-occurrence
  of brief bursts. No relation is declared: this account neither extends
  nor rivals that one, and gives it no support.
- **[LIT-385](../literature.d/LIT-385.md).** Damasio's convergence-zone proposal, that recall is the
  time-locked re-enactment across regions of activity laid down at
  encoding, has the shape of the reinstatement result. The paper does not
  cite it and the record has not read it, so it is an analogy only.
- **Propagation against synchrony.** Xu et al.'s spirals ([LIT-638](../literature.d/LIT-638.md),
  [THEORY-088](THEORY-088.md)) and Muller et al.'s traveling-wave review
  ([LIT-647](../literature.d/LIT-647.md), unread) put large-scale coordination in phase that moves
  across cortex. This account puts it in co-occurrence with no measured
  direction of travel, at a timescale about three orders faster. No paper
  in the record sets the two against each other.
