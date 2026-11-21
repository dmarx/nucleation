# Reader notes: modular-norm (LIT-tmp4b6aq)

## Step 1: copy located (2026-11-21)
- https://arxiv.org/pdf/2405.14813 (arXiv, lawful), fetched OK, pdftotext.
## Step 2: sections read
- §1-§5 (pp. 1-10) read in full: §3.1 module def (mass, sensitivity, well-normed),
  §3.2 composition/concatenation rules for the norm, §3.3 Prop 3 (feature learning
  apportioned by mass: ratio Mk.mass/M.mass), §2.2/Prop 2-5 Lipschitz-smoothness, §4 experiments.
- Next: App. B.4 mass taring, B residual/depth, D.6 mass allocation, proofs.
- Appendix A.2-A.4, B.1 (atoms, Table 2), B.4 (tare), B.5 (residual nets, Compound 1-2),
  D.2, D.4, D.6 (mass allocation, Fig 6/7), E (proofs of Prop 3, Prop 4) read.
  Skipped: B.6-B.7 attention/GPT detail, C (sharpness formulae), D.5 sweep figures.

## Step 3: draft findings
- Defeater (b) of CLAIM-tmpqwoxz NOT met: mass is a user-set, per-module free parameter;
  Prop 3 bounds module k's linearized output contribution by (Mk.mass/M.mass)*M.norm(dw);
  §2.3 "forces individual layers to learn at specified, regulated rates".
- Qualification: mass ratios are O(1) constants, not width exponents; width handled by
  norm choice (RMS-RMS / spectral with sqrt(dout/din)). Depth: tare fixes hidden total m,
  so each of L blocks gets m/L; paper recommends 1:m:1, constant in L. Mass 0 freezes weights.
  Paper's aim is balance ("no individual layer can learn too fast"), not levels.
- Residual block (L-1)/L*Identity + 1/L*M (Prop 4: depth-independent sharpness); contrast
  with nanoGPT 1/sqrt(L) (D.4). Bears on CLAIM-tmp2yj4t.
- Recheck: THEORY-082 (steepest descent relative to a metric), THEORY-1640 (LoRA freezing),
  THEORY-2077 (relative layer scale), CLAIM-tmpmugkp.
