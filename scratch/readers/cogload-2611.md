
## Step 1: copy found (2026-11-27)

- arXiv abs https://arxiv.org/abs/2611.33197 (v1, 16 Nov 2026; NeurIPS 2026, 33 pp; CC BY 4.0) - fetched, 200.
- arXiv HTML https://arxiv.org/html/2611.33197 (v1) - fetched, 200; reading this.
- Code/data: https://github.com/arushig100/CogLoadBench (named in paper; not fetched).
- Main text (secs 1-6) read.

## Step 2: sections read (2026-11-27)

- Read in full from arXiv HTML v1: abstract, secs 1-6, references, appendices A-F (B construction, C per-model tables, D ELS features/training/eval/robustness/ablations/data, E real-world, F steering). Nothing skipped except arXiv page chrome. PDF not separately fetched (HTML complete).
- Key facts noted: ELS = per-model 2-hidden-layer MLP (64,32) on 30 hand-built activation statistics, BCE on matched low(0)/high(1) pairs; length features excluded. Steering = ridge probe on hidden states to behavior-calibrated ELS (F1-drop target), attenuate component during prefill at 3 mid-late layers, norm rescale. Macro +0.42 F1 vs random -0.03, CAA +0.05, RepE-PCA -0.17; many cells within 1 SE.
