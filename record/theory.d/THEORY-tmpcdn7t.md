---
status: Proposed
title: 'In slices of striatum, visual and prefrontal cortex and hippocampus, Hebbian co-activation leaves a synaptic eligibility trace, lasting about 1 s in striatum, 3 to 10 s in cortex and about 2 s in CA1, that a later neuromodulator or plateau potential converts into a weight change and whose sign it can set: experimental support for three-factor learning rules on behavioural time scales'
version: 1
tags:
- neuroscience
- learning-and-conditioning
date: '2026-10-30'
source:
- LIT-1494
extends:
- THEORY-909
bears_on:
- QUESTION-311
promote_when: >-
  The seconds-scale trace shown in behaving animals, not only in slices: an
  experiment in vivo in which interfering with the trace's mechanism (for
  example CaMKII in striatal spines) during the interval between action and
  delayed outcome abolishes learning from that outcome while leaving learning
  from immediate outcomes intact, and independent replication of at least the
  striatal and cortical time constants. Refuted if learning from delays of
  seconds survives the abolition of synaptic traces, carried instead by
  persistent network activity or short-term plasticity. Further slice
  experiments with the same protocols cannot settle it.
summary: >-
  The wide form [THEORY-909](THEORY-909.md) held before the tenth status review narrowed
  it, kept as a Proposed reading by the [ADR-047](../decisions.d/ADR-047.md) kind-1 sweep of
  2026-10-30: the source asserts it, and [THEORY-909](THEORY-909.md), Active, is its
  evidence. Gerstner, Lehmann, Liakoni, Corneil & Brea (2018), [LIT-1494](../literature.d/LIT-1494.md),
  read five experimental papers as a decaying eligibility trace whose
  conversion, and direction, a third factor sets, and as support for
  three-factor rules on behavioural time scales; the evidence is mostly
  slices, one laboratory per region, and the reviewers grant that other
  mechanisms could bridge the gap.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-1 rule this entry is filed under -->

# THEORY-tmpcdn7t: In slices of striatum, visual and prefrontal cortex and hippocampus, Hebbian co-activation leaves a synaptic eligibility trace, lasting about 1 s in striatum, 3 to 10 s in cortex and about 2 s in CA1, that a later neuromodulator or plateau potential converts into a weight change and whose sign it can set: experimental support for three-factor learning rules on behavioural time scales

## Source

Gerstner, Lehmann, Liakoni, Corneil & Brea (2018), [LIT-1494](../literature.d/LIT-1494.md), read in full
in [NOTE-1130](../notes.d/NOTE-1130.md): a review of Yagishita et al. (2014), He et al. (2015),
Brzosko et al. (2015, 2017) and Bittner et al. (2017). The delay windows
those papers measured are [THEORY-909](THEORY-909.md), which this entry extends.

## The claim

The reviewers read the five papers as the experimental arrival of
three-factor learning rules, until then a theoretical assumption.
Co-activation of pre- and postsynaptic neurons sets a decaying flag at the
synapse, and "a non-zero third factor is needed to transform the
eligibility trace into a change of the synapse" and to set the "direction
of change" (p. 4). In striatum "the decay of the eligibility trace occurs
on a time scale of 1 s" (p. 7); in cortex pre-before-post pairing "leaves
an eligibility trace that decays over 5–10 s and that can be converted into
LTP by the neuromodulator noradrenaline" (p. 9), with a separate LTD trace
converted by serotonin; in CA1 a plateau potential within about 2 s
potentiates the input. Windows of seconds are what learning from delayed
outcomes in behaviour needs.

What [THEORY-909](THEORY-909.md) holds is the measured windows, attributed to the
reviewers' reading. In cortex the direction of change followed the pairing
order as well as the modulator, so the two are not separated, and the one
reversal of a single protocol's sign, by dopamine in CA1, took about a
minute and may be consolidation. Almost all of it is in slices with imposed
protocols, and the reviewers concede "there is nothing—apart from
conceptual elegance—to favor eligibility traces over alternative neuronal
mechanisms" (p. 12).

## What would settle it

The promote_when, which [QUESTION-311](../questions.d/QUESTION-311.md) also asks: the seconds-scale trace
shown in behaving animals, with interference in the trace's mechanism
between action and delayed outcome abolishing learning from that outcome
but not from immediate ones, and independent replication of the time
constants. Further slice experiments cannot settle it.
