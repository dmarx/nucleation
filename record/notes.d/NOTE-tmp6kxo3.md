---
status: Skimmed
paper: LIT-tmpyzr0s
title: 'Spectral dimensions of bundled networks'
version: 1
date: '2026-09-25'
summary: >-
  In composite "bundled" networks (a copy of a fiber graph attached to every node of a base graph) the Fiedler (spectral-gap) dimension generically decouples from the spectral dimension, so networks with identical density-of-states exponents can have parametrically different equilibration times.
---

<!-- inactive-ok-file: LIT-tmpyzr0s — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmp6kxo3: Spectral dimensions of bundled networks

## Contribution

Many real networks are assembled by reusing and recombining existing modules ("tinkering"), and it is an open problem how the properties of the parts determine the behaviour of the whole. The authors study networks of networks built by modular composition. They show that such compositions generically separate two notions of dimension that coincide in homogeneous structures: the spectral dimension (scaling of the Laplacian eigenvalue density) and the Fiedler dimension (scaling of the smallest nonzero Laplacian eigenvalue with size). Consequently, two networks can share the same thermodynamic exponents yet relax to equilibrium on very different timescales.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Method: diffusion-scale analysis via the Laplacian density matrix rho(tau) = exp(-tau L)/Z and a "spectral heat capacity" C(tau) = -dS/dlog tau, whose plateaus equal d_s/2 and whose large-tau cutoff is set by the Fiedler eigenvalue (Laplacian Renormalization Group framework) (pp. 1-2, Eqs. 1-2).
- Validation on homogeneous fractals: Sierpinski gasket and carpet give d_g = d_s within numerical accuracy (e.g. gasket d_s/2 ~ 0.684 vs d_g/2 ~ 0.683) (p. 2, SM S1).
- For bundled networks d_s equals the fiber's spectral dimension, while perturbation theory gives lambda_k ~ l^b_k / N_f and a composition rule d_g = 2(d_f,f + d_f,b)/(d_f,f + 2 d_f,b / d_g,b), which differs from both base and fiber values except when d_g,b = 2 or fibers are finite (p. 3, Eqs. 3-6).
- Dirac comb (ring of rings) vs Dirac brush (2D base, 1D fibers): same spectral dimension, different large-tau cutoffs (Fig. 1); Eq. 6 checked numerically on lattice-ring, tree-ring, BA-ring and random-tree-fiber families (Fig. 2).
- Physical consequence: in Rouse/Gaussian-network relaxation G(t) ~ t^(-d_s/2) at intermediate times but equilibration time ~ N^(2/d_g); analogous split for Debye heat capacity crossover temperature (Fig. 3, SM S6-S7).
- Outlook argues dimensionality is "relational" for composite architectures and suggests a hierarchy of effective dimensions for multi-level modular assembly (pp. 4-5).

## Open questions

- Strongest claim is the closed-form composition rule (Eq. 6); a deeper read should check the perturbative derivation and its stated validity range (SM S2-S3) and whether it holds beyond the base/fiber sizes scaling together (L_base = L_fiber is assumed in the examples).
- Generality claim ("independent of microscopic details" given finite Hausdorff dimension) is backed by a handful of synthetic families; no real-world network is analysed in the main text.
- ML link is indirect: graph Laplacian spectra, spectral gaps and diffusion timescales matter for spectral GNNs, graph diffusion and mixing times, but the paper itself makes no ML claim.
