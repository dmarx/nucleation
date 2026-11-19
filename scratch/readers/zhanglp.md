# Reader notes: zhanglp (Zhang, Lepori, Pavlick, "Instilling Inductive Biases with Subnetworks", arXiv 2310.10899)

## 2026-11-19: copy located and read
- arXiv PDF https://arxiv.org/pdf/2310.10899 (v2, 1 Feb 2024), fetched without a check; 17 pages incl. appendices A-C. Read in full; appendices read (B arithmetic extensions, C vision configs) more lightly.
- Design: train GPT-2 decoder (2-12 layers, 128-d) on T1 = a+ab (mod 7), tokens 0..999; continuous sparsification finds a mask for S1 = ab (mod 7) (3.2-7.7% of masked params); copy those weights, frozen, into a fresh model; train on T2 = a^2+ab (mod 7) from 1000 ambiguous samples (a=b) plus 10..10^4 disambiguating samples.
- Controls: scratch, random subnetwork of same per-layer size (and one from the complement, App. B.2), full-model transfer.
- Measures final test accuracy against number of disambiguating samples (a sample cost); 5 runs only stated for the 12-layer config.
- First pass on the lead's three parts: (a) yes, a later sample cost with and without the earlier component; (b) no matching of first-stage learners or organizations (all T1 models reach >=0.999); (c) the transplant is itself an intervention on a located component, with a random same-size subnetwork as the control. No ablation of the subnetwork inside a T1-pretrained model.

## 2026-11-19: results read, figures checked from rendered pages
- Fig. 3 (mean over 2-12 layers, read off the plot, approximate): at 10^3 disambiguating samples, subtask induction ~0.98, full-model transfer ~0.96, same-size random subnetwork ~0.70, scratch ~0.51 (text: "only average 50.6%"). Random subnetwork reaches ~1.0 only near 4-6x10^3 (text: "around 6 times as much data"); scratch ends ~0.64.
- At the smallest sample counts (10-20) full-model transfer and the random subnetwork sit at or above subtask induction; the advantage opens from ~50 samples.
- App. B.3 / Fig. 7: freezing vs training the discovered subnetwork makes no difference; letting a random subnetwork train lifts it to full-model-transfer level ("better initialization").
- App. B.3-B.4: a^2 subnetwork from a model trained on a^2+b^2 transfers worse and noisier; authors suspect the source model learned "a different structure". Irrelevant (a^2) subnetwork to a^3+ab helps less than ab. Closest thing in the paper to (b): source organization matters, uncontrolled.
- Doubts: seeds stated only for the 12-layer configuration (5 runs); checkpoint chosen on an eval set drawn from the full input space (unambiguous), which leaks disambiguating information into selection (my observation); full-model-transfer arm's freezing not stated; first-stage cost (200k T1 samples) not counted.

## 2026-11-19: bearings searched
- Not on the record (no LIT for 2310.10899). Lepori's "Break it down" (cited, structural compositionality) also not on the record.
- Searched: subnetwork, grokking, modular arithmetic, lottery ticket, shape bias, inductive bias, transplant, head start, frozen, compositional transfer, learning set. Relevant beyond the named codes: THEORY-970 and THEORY-966 (circuit discovery, redundant subgraphs), THEORY-tmppm9la (Anguita, fine-tuning reuse), THEORY-022 and THEORY-181 (modular-arithmetic grokking background), THEORY-114 (lottery ticket / LMC), QUESTION-495, QUESTION-380.
