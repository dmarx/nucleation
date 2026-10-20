---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpfc575](../notes.d/NOTE-tmpfc575.md)) in full, from arXiv:1303.6738v1 with its nine-page supplement; worth reading for the original numerics behind the claim that coarse-graining contracts irrelevant directions of the Fisher metric (Fig. 3: a 64×64 square-lattice Ising model at its critical point, 13 couplings and a field, up to six checkerboard decimations, in which the field and temperature eigenvalues stay put and the rest fall in bands drawn at b^(2y−d) per step for y = 0, −2, −4), for the supplement's scaling argument for that rate (Eqs. 28–41), which already states that only directions with 2y ≥ d are carried by the singular part, and for the hopping model of diffusion, whose density at time t carries Fisher eigenvalues scaling as t^(3/2−k) ([THEORY-tmpcvqfo](../theory.d/THEORY-tmpcvqfo.md)). Read it knowing that the Ising rates are read off a figure with no error bars, no fitted exponents and no second lattice size, and that the eigenvalues are assigned to y by drawn bands, with y = 0 not an operator of the 2D Ising model ([THEORY-tmpzyxwe](../theory.d/THEORY-tmpzyxwe.md), Proposed); that the derivation of the rate is the same scaling argument Raju, Machta and Sethna (2018) later repeat, and assumes the coarse metric is the Hessian of a coarse free energy in the bare couplings; that the Fig. 3 caption's rate 2^(−d−y) contradicts the supplement and the figure, whose bands fall as 2^(y−d/2); that the diffusion model is not a coarse-graining of one data set, so its leading eigenvalues grow with t rather than staying put; that the main text's "'relevant' directions in the RG are exactly those whose FIM eigenvalues do not contract" is contradicted by its own supplement for relevant directions with 0 < 2y < d; and that the closing claim that emergent theories are "due to" the sloppy hierarchy is not shown, since the paper traces both to the same separation of scales.
title: 'Parameter Space Compression Underlies Emergent Theories and Predictive Models'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Registered on 2026-10-20 at the coordinator's request, as the source of the numerics on which LIT-1254 (Raju, Machta and Sethna 2018) rests its Eq. 21. Citation from the arXiv abstract page and Crossref: Machta, B. B., Chachra, R., Transtrum, M. K. & Sethna, J. P., Science 342(6158):604–607 (November 2013), doi:10.1126/science.1238723, arXiv:1303.6738 (one version, submitted 27 March 2013). `published:` is the arXiv v1 date, 27 March 2013, which precedes the Science issue of 1 November 2013, per ADR-002. Not found in this record before filing: a grep of record/literature.d for "Machta", "1303.6738" and "Parameter space compression" found only LIT-1254, which cites it. The anthology was not checked, per ADR-048.
- version: 2
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmpfc575) from arXiv:1303.6738v1, main text and supplement, with the figures rendered and read as images. The published Science text was not compared: science.org returned 403 and the authors' Cornell copy failed TLS verification from this client. Status Deferred → Active. THEORY-tmpcvqfo (the hopping-model spectrum, re-derived and checked) and THEORY-tmpzyxwe (the Ising coarse-graining spectrum, Proposed) are filed from the reading.
tags:
- information-geometry
- natural-sciences
- complex-systems
date: '2026-10-20'
published: '2013-03-27'
arxiv: '1303.6738'
doi: '10.1126/science.1238723'
first_author: 'Machta'
keywords:
- 'sloppy models'
- 'Fisher information matrix'
- 'renormalization group'
- 'continuum limit'
- 'Ising model'
- 'diffusion'
- 'emergence'
- 'model reduction'
summary: >-
  Machta, Chachra, Transtrum & Sethna (Science 2013). Two physics models are not sloppy at their microscopic scale and become so when observed coarsely. In a 1-D hopping model the Fisher spectrum of the density at time t spreads as t^(3/2−k), ordered particle creation, drift, diffusion constant, then skew and higher moments. In Monte Carlo on a decimated 64×64 critical Ising model with 13 couplings and a field, the field and temperature eigenvalues stay put while the rest fall in bands drawn at b^(2y−d) per step. The rate is argued by scaling, not derived, and the Ising numbers have no error bars. The paper reads the resemblance to sloppy models from biology as a common cause of effective theories, which it does not show.
---
<!-- inactive-ok-file: THEORY-tmpzyxwe — Proposed; this reading's own empirical claim, cited as open -->

# LIT-tmps1ffa: Parameter Space Compression Underlies Emergent Theories and Predictive Models

Machta, B. B., Chachra, R., Transtrum, M. K. & Sethna, J. P. (2013). Parameter Space Compression Underlies Emergent Theories and Predictive Models. *Science* 342(6158): 604–607. doi:10.1126/science.1238723. arXiv:1303.6738.

Read in full in [NOTE-tmpfc575](../notes.d/NOTE-tmpfc575.md), from the arXiv copy and its supplement.

## Key takeaways

- In a 1-D hopping model whose density at time t is observed with fixed
  Gaussian error, the Fisher metric is exactly t² times the distribution of
  the difference of two (t−1)-step walks, and its k-th eigenvalue scales as
  t^(3/2−k) ([THEORY-tmpcvqfo](../theory.d/THEORY-tmpcvqfo.md)). The leading directions measure particle
  creation, drift and the diffusion constant.
- In a decimated critical Ising model, the two eigenvalues along the field
  and the gradient of T_c stay roughly constant over six steps of b = √2,
  and the others fall by many decades, in bands the authors draw at
  b^(2y−d) per step for y = 0, −2, −4 ([THEORY-tmpzyxwe](../theory.d/THEORY-tmpzyxwe.md), Proposed). These
  are the numerics on which [LIT-1254](LIT-1254.md) rests its Eq. 21 ([THEORY-742](../theory.d/THEORY-742.md)).
- The supplement's scaling argument (Eqs. 31 and 41) states that the
  singular part dominates only when 2y ≥ d, the dividing line [NOTE-972](../notes.d/NOTE-972.md)
  found on Raju, Machta and Sethna's scalings.

## Standing in the record

Here as the source of the numerics behind [THEORY-742](../theory.d/THEORY-742.md)'s excluded scaling
claim. It does not change that claim's standing: the paper's own derivation
is the same scaling argument, and its Monte Carlo is one lattice size at
one temperature, without error bars.
