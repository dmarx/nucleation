# Reader notes: zhanglp (Zhang, Lepori, Pavlick, "Instilling Inductive Biases with Subnetworks", arXiv 2310.10899)

## 2026-11-19: copy located and read
- arXiv PDF https://arxiv.org/pdf/2310.10899 (v2, 1 Feb 2024), fetched without a check; 17 pages incl. appendices A-C. Read in full; appendices read (B arithmetic extensions, C vision configs) more lightly.
- Design: train GPT-2 decoder (2-12 layers, 128-d) on T1 = a+ab (mod 7), tokens 0..999; continuous sparsification finds a mask for S1 = ab (mod 7) (3.2-7.7% of masked params); copy those weights, frozen, into a fresh model; train on T2 = a^2+ab (mod 7) from 1000 ambiguous samples (a=b) plus 10..10^4 disambiguating samples.
- Controls: scratch, random subnetwork of same per-layer size (and one from the complement, App. B.2), full-model transfer.
- Measures final test accuracy against number of disambiguating samples (a sample cost); 5 runs only stated for the 12-layer config.
- First pass on the lead's three parts: (a) yes, a later sample cost with and without the earlier component; (b) no matching of first-stage learners or organizations (all T1 models reach >=0.999); (c) the transplant is itself an intervention on a located component, with a random same-size subnetwork as the control. No ablation of the subnetwork inside a T1-pretrained model.
