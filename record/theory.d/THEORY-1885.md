---
number: 1885
status: Proposed
formerly:
- THEORY-tmpfiper
promote_when: >-
  The published Neuron version is read and confirms the preprint's ranking
  and figures. Or an independent stimulation data set (not F-TRACT) finds
  search information or communicability outperforming direct structural
  weights and shortest-path measures in predicting evoked responses,
  including between anatomically unconnected regions, with Euclidean
  distance the strongest single predictor.
title: 'Seguin, Jedynak, David, Mansour L, Sporns and Zalesky find that diffusion-like communication measures on the human connectome, search information and communicability, predict the spread of cortico-cortical evoked potentials better than direct structural connection or routing measures, even between unconnected regions, though Euclidean distance is the strongest single predictor'
version: 1
tags:
- neuroscience
- network-science
date: '2026-11-15'
source:
- LIT-2649
summary: >-
  Seguin, Jedynak, David, Mansour L, Sporns & Zalesky (2023), read as the
  bioRxiv preprint in [NOTE-1969](../notes.d/NOTE-1969.md). CCEPs from 29,055 stimulations in 550
  patients against communication measures on a normative connectome.
  Search information and communicability rank first among network
  measures, and they beat direct structural weights even for connected
  pairs. Distance, search information and FC give an out-of-sample R² of
  54% for response probability. All figures are the preprint's. The
  wording is the reader's; adopting it is the owner's call.
---

# THEORY-1885: Seguin, Jedynak, David, Mansour L, Sporns and Zalesky find that diffusion-like communication measures on the human connectome, search information and communicability, predict the spread of cortico-cortical evoked potentials better than direct structural connection or routing measures, even between unconnected regions, though Euclidean distance is the strongest single predictor

## Source

Seguin et al. (2023), [LIT-2649](../literature.d/LIT-2649.md); read as the bioRxiv v1 preprint in
[NOTE-1969](../notes.d/NOTE-1969.md). The Neuron version was not read.

## The result

The F-TRACT data: "550 participants, 29,055 stimulations and 2.77 million
pairs of recording electrodes". Response probability and amplitude between
regions are set against communication measures, from routing to diffusion,
computed on a 1,000-subject diffusion-MRI connectome. "search information
consistently ranked as the most explanatory network measure of response
probability and amplitude". Between unconnected regions, "search
information and communicability markedly outperformed alternative network
measures and ED". Euclidean distance alone has the strongest single
correlation (ρ = −0.62 for probability). A lasso model of distance, search
information and FC explains 54% of out-of-sample variance in response
probability. Routing measures could have won, or direct weights could have
sufficed for connected pairs; neither did.

## What it does not show

- That signals actually travel by diffusion. These are statistical proxies
  ranked by fit.
- That the effect survives the patient population: CCEPs come from
  epilepsy patients, and the connectome is normative, not each patient's.
- Anything about waves, interference or resonance.
- The published figures, which may differ.
