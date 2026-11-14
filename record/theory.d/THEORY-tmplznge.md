---
status: Proposed
promote_when: >-
  A run of the authors' archived code (Zenodo, doi:10.5281/zenodo.23751909)
  at the parameters of their Table 1, or an independent reimplementation
  from their Materials and Methods, shows the bistable interval the title
  states: at some resource supply s, shrubland and grassland each persist
  after 1,000 iterations, depending on the initial configuration. The run
  must also say which survival-threshold convention produces it, since
  the text and Table 1 disagree. It does not need the field shift to be
  shown to be a phase transition, which the title attributes to the
  authors and does not assert.
title: 'On Sun and colleagues, a cellular automaton in which shrubs deplete resources weakly over a wide radius and grasses strongly over a narrow one gives, as resource supply rises, patterned shrubland, then an interval where either type excludes the other depending on the initial configuration, then patterned grassland; the authors read this as a first-order phase transition and match it to the shrub-to-grass shift they observe within 180 to 250 mm of annual rainfall at the desert margin of northern China'
version: 1
tags:
- ecology
- complex-systems
date: '2026-11-14'
source:
- LIT-tmpruadv
bears_on:
- QUESTION-281
summary: >-
  Sun, Yu, Li, Rietkerk, D'Odorico, Chen, Wang, Zhang & Yu (2026),
  [LIT-tmpruadv](../literature.d/LIT-tmpruadv.md), read in [NOTE-tmpmu9w0](../notes.d/NOTE-tmpmu9w0.md). The model's bistability is shown
  (Fig. 3C, with hysteresis in SI Fig. S2, unread). The field's is
  inferred from alternation between plots, nonlinear cover change and
  rising spatial skewness, none of which is specific to a first-order
  transition. The sharp edge: kernel widths and strengths are not
  measured; the fairy-circle and desert-edge results come from scenarios
  set by hand; and the survival thresholds in Table 1 are the reverse of
  what the text says. Proposed until the model's bistable interval is
  reproduced.
---

# THEORY-tmplznge: On Sun and colleagues, a cellular automaton in which shrubs deplete resources weakly over a wide radius and grasses strongly over a narrow one gives, as resource supply rises, patterned shrubland, then an interval where either type excludes the other depending on the initial configuration, then patterned grassland; the authors read this as a first-order phase transition and match it to the shrub-to-grass shift they observe within 180 to 250 mm of annual rainfall at the desert margin of northern China

## Source

Sun et al. (2026), [LIT-tmpruadv](../literature.d/LIT-tmpruadv.md), read in full in [NOTE-tmpmu9w0](../notes.d/NOTE-tmpmu9w0.md) from the
publisher's PDF that the owner supplied. The SI, the dataset and the code
were not read.

## What was actually shown

- **In the model.** On a 200 × 200 lattice with global dispersal, each
  plant convolves a kernel into an interaction field. The kernel has
  competition of strength c/(n−·s) out to radius r− and facilitation K+
  out to r+. Shrubs have r− = 20 and grasses r− = 3. From random starts
  at density 0.01, the stable state after 1,000 iterations is shrubs at
  low s, grasses at high s, and "in the transition zone either can win
  by excluding the other" (Fig. 3C). The asymmetry in facilitation is
  "not essential for phase transition" (p. 8). This part could have come
  out otherwise: the two types might have coexisted, or switched without
  overlap.
- **In the field.** Along a transect of 30 sites and 25 more plots in
  the window, shrub cover falls and grass cover rises nonlinearly within
  180–250 mm MAP. Plots in the window alternate between shrub and grass
  dominance, and patch size, spacing and their skewness change sharply
  (Fig. 2). Patch size and spacing regress on a conservative-to-acquisitive
  trait axis with R² from 0.35 to 0.48.
- **The authors' reading.** Precipitation acts as an external field
  driving a first-order transition, like magnetization reversal in the
  Ising model. Fairy circles are metastable states near its threshold.
  The loss of cover at the desert edge under disturbance is a separate,
  continuous transition.

## What this does not say

- **That the field shift is a phase transition.** Alternation between
  plots at similar rainfall is what bistability would produce, but so
  would unmeasured heterogeneity. The paper has no time series or repeat
  visits, and rising skewness marks nearness to a threshold, not its
  kind ([THEORY-1315](THEORY-1315.md)).
- **That the EI trade-off is measured.** The kernels' ranges and
  strengths are model parameters; the field test correlates patch
  geometry with leaf and size traits.
- **That fairy circles arise from the dynamics.** In the simulation they
  follow from halving the shrub kernel and switching off shrub dispersal
  by hand. Metastability is named, not tested.
- **That the edge decline is critical.** The power law is a fit with a
  free critical point, accepted at R² > 0.9.
- **Which threshold convention the result needs.** The text puts the
  grass survival threshold below the shrubs' (Hg < Hs); Table 1 gives
  H_g = 1.1 above H_s = 1.0.
