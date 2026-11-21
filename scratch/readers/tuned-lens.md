# Reader notes: tuned-lens (LIT-tmp8pcca)

## Step 1: copy located (2026-11-21)

- https://arxiv.org/pdf/2303.08112 fetched 2026-11-21, PDF, 25 pages, arXiv v6 (11 Nov 2025).
  Kind: arXiv (lawful). Text extracted with pdftotext -layout; not committed.
- Authors on the PDF: Belrose, Ostrovsky, McKinney, Furman, Smith, Halawi, Biderman, Steinhardt
  (the LIT lists six; Biderman and Steinhardt are missing).

## Step 2: sections read (2026-11-21)

Read: abstract, sections 1-6, appendix A (captions), B and B.1 (captions), C and C.1 in full,
D.1, E (skimmed; static analysis, not on brief). Figures read from captions and text only.
Key points:
- Iterative inference framed via Jastrzebski et al. 2017; App. C reproduces Taylor-expansion argument;
  Pythia 6.9B residual-gradient cosine negative >=95% of the time, magnitude <=0.05.
- Trajectory "converge[s] smoothly", "each successive layer achieving lower perplexity" (Sec 1).
- Representational drift (Sec 3): covariance of hidden states drifts apart with layer separation;
  layer 4 outlier dims in Pythia 12B; "smooth representational drift with depth" (Fig 6);
  final-layer covariance changes sharply. Transfer penalties low near diagonal, rho=-0.78 with cov similarity.
- C.1: layer deletion in Pythia 6.9B: only the first layer is crucial.
- Causal: CBE, Spearman 0.89 (Pythia 410M L18); stimulus-response alignment higher at later layers.
- v6 notes earlier lenses "severely undertrained" (Muon); experiments not redone.
