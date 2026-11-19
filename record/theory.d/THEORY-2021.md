---
number: 2021
status: Proposed
formerly:
- THEORY-tmpctik9
title: 'Jacobs and colleagues show that recurrent networks with only local encoders and local recurrence learn to propagate travelling waves that carry whole-shape information to each pixel, so that a readout of each neuron''s activity over time segments images needing global context, beating feed-forward networks of matched receptive field and, on Multi-MNIST, U-Nets of similar size'
version: 1
source:
- LIT-2836
tags:
- representation-learning
- neuroscience
date: '2026-11-19'
bears_on:
- QUESTION-491
promote_when: >-
  Independent reproduction on segmentation tasks needing global context,
  with an intervention showing the waves carry the information: blocking
  or damping propagation at test time, with weights and readout fixed,
  removes the advantage, and the advantage of time-series over last-state
  readouts survives on at least one non-toy dataset.
summary: >-
  From the reading of [LIT-2836](../literature.d/LIT-2836.md) in [NOTE-2133](../notes.d/NOTE-2133.md). Jacobs, Budzinski,
  Muller, Ba and Keller (2025), arXiv 2502.06034. Recurrent networks with
  only local encoders and local recurrence learn to propagate travelling
  waves that bring whole-shape information to each pixel; reading each
  neuron's activity over time, rather than its last state, lets them
  segment images that need global context, beating feed-forward CNNs of
  matched receptive field and, on Multi-MNIST, U-Nets of similar size. The
  motivation is Kac's "hearing the shape of a drum", and a wave RNN
  reproduces square drums' fundamental frequencies; even an unbiased
  convolutional LSTM learns waves. Here because A15 of the exchange
  "Topological protection explained" listed it beside Keller et al. as a
  way learned systems carry information ([QUESTION-491](../questions.d/QUESTION-491.md)), and [LIT-647](../literature.d/LIT-647.md)
  mentions it. The role of the waves rests on comparisons and a training-
  time correlation, not on intervention. Read in its NOTE.
---
<!-- inactive-ok-file: LIT-647 — Unavailable; cited in this filing of 2026-11-19 -->

# THEORY-2021: Jacobs and colleagues show that recurrent networks with only local encoders and local recurrence learn to propagate travelling waves that carry whole-shape information to each pixel, so that a readout of each neuron's activity over time segments images needing global context, beating feed-forward networks of matched receptive field and, on Multi-MNIST, U-Nets of similar size

## The account

Each pixel of the hidden state sees only its neighbours. A disturbance spreads as a wave, reflects from boundaries that the input makes by setting local natural frequencies, and the resulting time series at a pixel carries information about the shape it lies in, as the spectrum of a drum carries its geometry. A linear projection or the Fourier amplitudes of that time series serve as the pixel's representation. Locally coupled oscillator networks and convolutional LSTMs both learn wave dynamics; with time-series readouts they segment polygons, tetrominoes and MNIST digits, and on Multi-MNIST the oscillator network with about 55K parameters beats U-Nets of 31K and 69K. Long wavelengths emerge in training as the loss falls (correlation 0.961).

## What it does not show

- That the trained networks compute by the drum mechanism: the authors disclaim it.
- That waves are causally necessary in a trained network: no intervention on propagation.
- Anything about cortex: the models are "highly abstract idealizations of a cortical sheet".
- That the learned boundaries are defects or walls of an ordered phase: they are set by the input encoder.
