---
number: 88
status: Proposed
formerly:
- THEORY-tmp05pbr
promote_when: >-
  Two kinds of result, one for each half. For the defects themselves: the
  same objects (phase singularities with rotating phase around them,
  drifting, annihilating in opposite-charge pairs and rarely in like
  pairs) found across the human cortex in a signal that is not BOLD, such
  as whole-cortex ECoG, MEG source phase or a matched animal recording,
  and found at a spatial scale fixed in advance rather than at the one
  that maximises task decoding. For the organising role: a test in which
  the defects could fail to matter. One form is a perturbation that
  creates, removes or re-signs a spiral and changes the flow or the
  behaviour it is said to route. Another is the comparison LIT-638
  itself leaves open: the same scans analysed both as spiral fields and as
  a discrete repertoire of metastable substates, asking which description
  keeps its explanatory power once the other is regressed out. The account
  is refuted if the spirals do not survive a distance-preserving surface
  analysis (the flat map is the paper's own named weak point), if they
  appear as often in a phase-randomised null at the chosen scale without
  the filtered–unfiltered similarity criterion, or if the discrete-state
  description explains the same transitions and the spiral description
  adds nothing. More decoding from the same HCP data, at the same scale,
  cannot settle it.
title: 'Slow large-scale activity in human cortex is organised as in a pattern-forming medium: its flow is set by interacting spiral defects centred on phase singularities, which sit on boundaries between functional regions, annihilate with spirals of opposite rotation and repel those of the same'
version: 1
tags:
- neuroscience
- complex-systems
- cognition
date: '2026-10-03'
source:
- LIT-638
summary: >-
  Xu, Long, Feng & Gong (2023), [LIT-638](../literature.d/LIT-638.md): in Human Connectome Project
  fMRI band-passed to 0.01–0.1 Hz, the cortical phase field holds about
  16–19 spirals at a time around phase singularities, concentrated on
  boundaries between functional regions; their centres drift
  superdiffusively, opposite spirals annihilate (51% fully, 46% partly)
  and like ones repel (2.6%), and their positions and senses decode task
  condition above a raw-amplitude decoder. One source, fMRI only, at a
  spatial scale chosen because it maximised that decoding; the routing of
  activity flow is read from phase gradients and a phase-oscillator model,
  never perturbed. The kinship with Belousov–Zhabotinsky spirals and
  pattern-formation defects is the record's analogy, not the paper's.
---
<!-- inactive-ok-file: LIT-647 — Deferred, unread (paywalled); named as the electrophysiological review that could bear on this, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-069 — Proposed; named in Connections as the record's other phase-dynamics account of coordination, no relation claimed -->

# THEORY-088: Slow large-scale activity in human cortex is organised as in a pattern-forming medium: its flow is set by interacting spiral defects centred on phase singularities, which sit on boundaries between functional regions, annihilate with spirals of opposite rotation and repel those of the same

## Source

- Xu, Long, Feng & Gong (2023), [LIT-638](../literature.d/LIT-638.md), read in full in
  [NOTE-502](../notes.d/NOTE-502.md): Figs. 2–8, the Methods on scale selection, phase and
  vorticity fields, spiral detection, the null model and the
  phase-oscillator lattice, and the Discussion.

## What was actually shown

**The data.** Xu et al. ([LIT-638](../literature.d/LIT-638.md)) analyse Human Connectome Project
3T fMRI: three random cohorts of 100 subjects (rest, a language task, and a
replication of the language task) and 100 doing the working-memory task.
The signal is BOLD, temporally band-passed to 0.01–0.1 Hz and projected
onto the HCP flat map of each hemisphere. Everything below is therefore
about infra-slow haemodynamic fluctuations on a flattened sheet. The paper
cites, but does not show, that such fluctuations track infra-slow
electrical activity.

**The scale was chosen on the outcome.** The spatial band-pass was set by
sweeping difference-of-Gaussian filters across the wavelengths of the
first twelve geometric eigenmode groups and keeping the range in which
spiral-based task classification was highest: 70.17 mm < Sc < 137.95 mm,
"the classification accuracy is maximized" (Methods). The authors say
spirals at other scales behave similarly, without showing it in the main
text. The decoding numbers below are therefore optimistic estimates; the
replication cohort used the same band.

**The defects.** The Hilbert phase of each vertex defines a phase field,
its gradient a phase vector field, and its curl a vorticity. Spirals are
localised rotations centred on phase singularities, points of near-zero
amplitude round which every phase occurs. A spiral counts only if the
filtered field matches the unfiltered one beyond the 95th percentile of a
3-D Fourier phase-randomised null, because spatial filtering makes spirals
appear in noise too. At rest the left hemisphere holds 16.33 ± 2.22 at a
time (18.8 ± 2.6 during the task), of radius 10.46 ± 4.77 mm; 62% span
more than one of 22 regions, and their density is highest on boundaries
between functional regions and networks, not on sulci, gyri or inflection
points (Fig. 2, Extended Data Fig. 2).

**Their dynamics.** Centres drift at 2.19 ± 1.80 mm/s, superdiffusively
(mean-squared-displacement exponent between 1 and 1.9, mean about 1.5, for
96% of trajectories). Of pairwise interactions, 51.04% are full
annihilation of two spirals of opposite rotation, 46.40% partial
annihilation, and 2.55% repulsion between spirals of the same rotation
(Fig. 4). A full annihilation leaves a plane wave travelling the other way.

**Their bearing on the task.** Spiral positions and rotation senses decode
four language conditions on single trials at 48.33% (replication 50.35%;
chance 25%; phase-randomised null 24.32%), against 30.2% for a decoder
given raw fMRI amplitude at matched input size, and working-memory stimulus
type, load and accuracy above chance. Trial-averaged unfiltered task fMRI
shows spirals at the same places and with the same senses. The authors
then read routing rules off phase-vector streamlines: a pair of opposite
spirals forms an S-shaped "gate" that passes flow, a like pair a "wall"
that diverts it, and during math listening and answering spiral clusters
route flow bottom-up and top-down respectively between auditory and
lateral temporal cortex (Fig. 8). In a 30 × 30 lattice of coupled phase
oscillators, annihilation is again the commonest interaction, and
reversing selected spirals reverses the flow between them.

What could have come out otherwise: spirals could have vanished against
the null, or sat on sulcal folds, or interacted without the
charge-dependent asymmetry, or decoded no better than amplitude. None did.

## Why "a pattern-forming medium", and not more

The claim this account files is that the brain's large-scale slow
activity has the organisation that non-equilibrium pattern-forming media
have: a phase field whose topological defects, of charge ±1, move,
annihilate in opposite pairs and govern the flow around them. The record
holds that organisation in chemistry and physics. Zhabotinsky's review of
the Belousov–Zhabotinsky reaction ([LIT-531](../literature.d/LIT-531.md), read in [NOTE-414](../notes.d/NOTE-414.md)) reports that
in the unstirred, excitable medium colliding waves annihilate and broken
fronts curl into spirals. Cross and Hohenberg ([LIT-527](../literature.d/LIT-527.md)) hold that phase
dynamics and topological defects of a broken continuous symmetry are
established in non-equilibrium laboratory systems. Turing's morphogenesis
paper ([LIT-535](../literature.d/LIT-535.md), read in [NOTE-427](../notes.d/NOTE-427.md)) shows that a reaction–diffusion medium
can produce travelling waves, his case (e), which needs at least three
morphogens.

That is an analogy, and the record draws it, not the paper. Xu et al.
cite Kuramoto's oscillator lattices and defect-mediated turbulence, liken
their spirals to vortices in turbulence, active matter and the heart, and
note that brain spirals differ from fluid defects in diffusing
superdiffusively. They do not use the word "excitable", and their model is
a lattice of phase oscillators, which is an oscillatory medium and not an
excitable one. So the title says "pattern-forming medium" rather than
"excitable medium": the evidence fixes the defect phenomenology, not which
class of medium produces it. No `extends` is declared. The record holds no
theory of pattern formation that this one carries further, and [LIT-531](../literature.d/LIT-531.md),
[LIT-527](../literature.d/LIT-527.md) and [LIT-535](../literature.d/LIT-535.md) are works, not accounts.

## The rival description

Vohryzek et al.'s whole-brain-modelling review ([LIT-080](../literature.d/LIT-080.md), read in [NOTE-054](../notes.d/NOTE-054.md))
describes non-stationary brain dynamics as visits to a repertoire of
discrete substates with dwell times and transition probabilities on a
metastable attractor landscape. Xu et al. argue the reverse for the same
phenomenon: spiral-based coordination means transitions between functional
networks "evolve continuously across space and time, rather than discrete
or sudden changes between different metastable states as previously
suggested" (Discussion). [LIT-638](../literature.d/LIT-638.md) already declares `rivals` against
[LIT-080](../literature.d/LIT-080.md). No theory in the record states the discrete-substate view (a
grep of `record/theory.d` for metastability, substates and [LIT-080](../literature.d/LIT-080.md) finds
none), so no `rivals` is declared here. That claim in the paper is also
the weakest part of it: an interpretation of the routing result, not
tested against a state-switching model. This account takes the defect
organisation as its claim and leaves the continuous-versus-discrete
question open; if a discrete-substate theory is filed, it and this one
should be weighed then, and they may turn out compatible descriptions at
different grains rather than rivals.

## What this does not say

- **It does not say the brain is an excitable medium.** See above: the
  defect phenomenology is shared by oscillatory and excitable media, and
  the paper models only the former.
- **It does not say the spirals are electrical.** The evidence is BOLD at
  0.01–0.1 Hz. Muller et al.'s review of travelling waves ([LIT-647](../literature.d/LIT-647.md))
  is the record's entry for electrophysiological waves, and it is Deferred
  and unread, so nothing here compares the two scales.
- **It does not say the spirals route activity.** "Flow" is the phase
  gradient, not measured transfer of activity or information, and the
  gate and wall rules come from streamlines and a phenomenological lattice.
  Nothing in the brain was perturbed.
- **It does not give a decoding accuracy to quote.** The scale was chosen
  where decoding peaked.
- **It does not exclude the flat map.** Flattening distorts distances, and
  a wave reverberating round a sulcus could appear as a spiral; the
  authors argue against this with a sulcal-depth test only.
- **It does not say what makes cortical defects superdiffusive**, which is
  where the analogy with fluids breaks.

## Connections

- **Coordination by synchrony.** Verzhbinsky et al. ([LIT-633](../literature.d/LIT-633.md)) place
  long-range coordination in brief co-occurring ripples near 90 Hz, with
  no measured direction of travel; this account places it in propagating
  phase structure at 0.01–0.1 Hz. They work three orders of magnitude apart
  in time and neither tests the other.
- **[THEORY-069](THEORY-069.md).** The record's other account of coordination as phase
  dynamics, the HKB transition in relative phase. It concerns two coupled
  components, not a field of defects; no relation is declared.
