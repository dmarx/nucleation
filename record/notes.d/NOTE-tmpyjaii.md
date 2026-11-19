---
status: Read
paper: LIT-tmpv822r
title: 'Jacobs and others 2025 — Traveling Waves Integrate Spatial Information Through Time'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2502.06034 (HTTP 200, PDF, arXiv v4, 11
    Jun 2025, cs.CV; the PDF names no venue). Kind of copy (step 5): arXiv,
    the authors' own preprint. Lawful. Date: 2026-11-19. No fetch obstacle.
    Read: abstract, Introduction, "Motivation: Hearing the Shape of a Drum"
    (wave RNN on square drums, Fig. 2), Experiments (datasets, NWM,
    ConvLSTM, readouts, CNN and U-Net baselines), Results (Polygons,
    Tetrominoes, MNIST, Multi-MNIST; Tables 1-2), Related Work, Limitations,
    Conclusion; Supplementary "Extended Quantitative Analysis of Wave
    Dynamics" (Figs. 9-10) and "Extended Visualizations of Table 1".
    Skipped: supplementary training details and hyperparameter tables,
    Tables 5-6 (min/max/median by seed), Figs. 13-14, the reference list.
    Text extracted with pdftotext (reading order, for the two-column layout)
    to dl/text.txt; the -layout extraction is kept as dl/text_layout.txt.
date: '2026-11-19'
---
<!-- inactive-ok-file: CLAIM-698 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: LIT-647 — Unavailable; cited in this filing of 2026-11-19 -->

# NOTE-tmpyjaii: Jacobs and others 2025 — Traveling Waves Integrate Spatial Information Through Time

## Contribution

Jacobs, Budzinski, Muller, Ba and Keller (arXiv 2502.06034, v4 2025) ask whether travelling waves can carry global spatial information to neurons whose connections are only local. They take Kac's question, "Can one hear the shape of a drum?", as the model: a wave started inside a boundary reflects from it, and the time series at any interior point comes to carry the boundary's spectrum. A wave-integrating RNN reproduces the theoretical fundamental frequencies of square drums. Trained convolutional recurrent networks with only local encoders and local recurrence (a locally coupled oscillator network, NWM, and a convolutional LSTM) then segment images whose classes depend on whole shapes, using each pixel's time series as its representation. With such time-series readouts they beat feed-forward CNNs of matched receptive field and, on Multi-MNIST, U-Nets of similar size.

## Key results

- Motivation, Fig. 2: for square drums of side 13 to 21, "The wave-based RNN’s results align almost perfectly with theoretical predictions".
- Polygons, Figs. 3-4: the NWM "has learned to use differing natural frequencies inside and outside the shape to induce soft boundaries, causing reflection, thereby yielding different internal dynamics based on shape"; per-class spectra differ, "allowing for > 99% pixel-wise classification accuracy on a test set."
- Results, Fig. 5: "the LSTM learns to generate wave dynamics despite lacking an explicit inductive bias for doing so."
- Results, Table 1: on MNIST and Tetrominoes, models with linear time-series readouts do best; "Recurrent models that rely solely on the last hidden state for predictions achieve the weakest results."
- Multi-MNIST, Table 2: "the NWM with 54K parameters performs better than U-Net’s with 30K and 68K parameters, despite having only local connectivity and no explicit skip connections" (Table 2 lists it as 55K).
- Supplement, Figs. 9-10: the share of locations with long estimated wavelengths rises during training together with falling loss; "these two values, averaged over 5 random seeds, reach a correlation coefficient of 0.961."
- Limitations: "we have no guarantee that our trained models form image representations in precisely that manner"; the authors "caution readers against overinterpreting this analogy as a literal account of how the models operate."

## Assumptions

- Encoders and readouts are pixel-local (3×3 convolutions, receptive field 9×9 in the NWM's encoder), so any global information at a pixel must arrive through the recurrence.
- Circular padding in recurrent convolutions; a fixed integration horizon (100 steps for the NWM, 20 for the LSTM).
- The input sets the medium: in the NWM the image sets each oscillator's natural frequency and damping, which is how boundaries are made.

## Concepts

- Spatial integration through time: global context reaching a local neuron as a delayed, reflected wave.
- Hearing the shape of a drum (Kac 1966): the Laplacian's eigenspectrum on a domain encodes its geometry.
- Time-series readout: the whole trajectory of a neuron, read by a learned linear projection or FFT amplitudes, as the representation, in place of the last state.
- Soft boundaries made by a jump in natural frequency, which reflect waves.
- Phase-lag synchrony as a form of binding (the paper's own link to binding by synchrony).

## Bearing on the record

- [QUESTION-tmpcb0bf](../questions.d/QUESTION-tmpcb0bf.md): qualifies. This is close to the question's Experiment B in one respect: a locally connected recurrent network trained on a task whose answer depends on boundaries in the input, in which the learned dynamics create interfaces (soft boundaries by natural-frequency contrast) that reflect waves. But the interfaces are imposed by the input-to-frequency encoder, not domain walls between symmetry-related ordered phases, and there is no intervention on them. Evidence that the waves matter is a training-time correlation (0.961) and readout comparisons.
- [CLAIM-698](../claims.d/CLAIM-698.md): supports, in a narrow form. A modal, spectral description (per-pixel frequency spectra; the drum analogy) is what makes the trained networks' segmentation legible, and FFT readouts of the dynamics work nearly as well as learned linear ones. The authors themselves warn the drum analogy is not a literal account, and nothing here tests prediction of responses to interventions or merging, which the claim requires to earn its place.
- [LIT-647](../literature.d/LIT-647.md): supports the review's integration theme as summarised in the record, in artificial networks, with the review's first author as co-author; confirms that 2502.06034 is a different work.

## Limitations

- No intervention on the waves in a trained model; the role of waves rests on architecture comparisons, readout comparisons and a correlation across training.
- Toy datasets (polygons, tetrominoes, upscaled MNIST digits); high seed variance for CNN baselines.
- The drum analogy is motivational; the NWM has learned damping and input-set frequencies, so it is not a clamped-boundary wave equation.
- Computational cost: numerical integration with small time steps makes these models slow against U-Nets.
