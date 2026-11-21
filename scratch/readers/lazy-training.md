# Reader notes: lazy-training (LIT-tmp67epj)

## Step 1: copy located (2026-11-21)
- https://arxiv.org/pdf/1812.07956 -> arXiv v5 (7 Jan 2020), 20 pp PDF, fetched OK. Lawful (arXiv).

## Step 2: sections read
- Read in full: abstract, §1 (1.1-1.3, kappa criterion eq. 1), §2 (Thms 2.2-2.5), §3 (two-layer, CNN), §4, App. A (A.1-A.3), B.1, B.5 tail, C.
- Skimmed: B.2-B.4 proofs (constants).
- Key for defeater (a): ALL parameters (readout included) move O(1/alpha) while output change is O(1) (Thm 2.2, 2.4). Tangent kernel = sum of hidden-layer kernel K^(a) and output-layer kernel K^(b) (App A.2); differs from output-layer-only random features. So lazy = parameters-vs-output separation, not hidden-vs-readout. 1/alpha^2 objective scaling = "proper time parameterization".
