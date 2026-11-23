---
status: Read
paper: 'LIT-tmp581o9'
title: 'Arbona, Aime and Elezgaray: cooperativity in the annealing of DNA origamis'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Read on 2026-11-23 by the lead run of that date from the arXiv PDF,
    v2 of 2 October 2012 (https://arxiv.org/pdf/1111.7130v2), converted
    to text. Read in full: abstract, sections I to VI, appendices A and B,
    and the figure captions. Not read: the figure images, so every number
    here is from the text; the reference list was scanned only. The
    companion reports the paper cites (a short report in EPL and an AFM
    comparison in JACS 2012) were not read. Section names are the paper's.
date: '2026-11-23'
summary: >-
  UV-absorption melting of three-strand DNA constructs and a
  local-equilibrium model of origami annealing. A staple's melting peak
  rises when a neighbouring staple is already folded (by 1.5 to 8.5 °C in
  four comparisons), and the inner crossover position costs more than the
  outer. The model's neighbour-dependent crossover penalties and a
  strong-correlation closure reproduce the annealing–melting curves and
  their hysteresis for four ~200-staple origamis. Misfolds and kinetics are
  excluded by hypothesis; parameters are fitted on the small constructs.
---
<!-- inactive-ok-file: CASE-tmp2a9lm — new; this reading's account and the study it informs, filed with it -->

# NOTE-tmpfz1bj: Arbona, Aime and Elezgaray: cooperativity in the annealing of DNA origamis

## Contribution

The paper measures, in the smallest construction that has more than one
staple, how one staple's binding changes once another is bound, and builds
from it a model of full origami annealing. Before it, the coupling between
neighbouring staples was assumed or simulated; here it is measured on two
staples and shown to be needed to fit the melting and annealing curves of
large origamis.

## Key results

- **Small origamis (section II).** One 64-base scaffold (B0) and two
  staples, each binding two separate scaffold regions. Melting peaks from
  the derivative of the degree of pairing:
  - B1 with its complement: 57 °C. B1 alone, outer position: 48.5 °C; with
    B2 folded: 51.5 °C. "Therefore, the inner staple B2 helps the pairing
    of the outer staple B1 by suppressing part of the entropic penalty
    related to the bulge formed by the scaffold."
  - B1 inner, alone: 41.5 °C, half width 12 K; with B2 added: 50 °C.
    "the presence of B2 helps the folding of B1 whatever its location."
  - B2: duplex 91 °C, inner 83 °C, outer 86.5 °C, "the same differences
    between the inner and outer positions are observed whatever the
    chemical sequence involved."
  - The B1m–B2m pair, with close melting temperatures: B2m's peak is
    1.5 °C higher with B1m present ("partial folding of the staple B1m
    helps the folding of the staple B2m"), and B1m's moves "from 67 ◦ C to
    72 ◦ C" with B2m present.
- **The model (sections III and IV).** Staples insert by local equilibria
  conditioned on a neighbourhood of staples whose crossovers share a row
  and lie within 75 bases. Hypothesis 1: each staple part is fully bound
  or unbound, and "we also disregard misfolded configurations". Hypothesis
  3, a closure from the small origamis: the staple more likely bound is
  taken to be present whenever the less likely one is. Each crossover
  carries a topological penalty of one of three local intermediate states:
  a bulge (LIS1, loop length reduced by already folded bases), a zero-length
  loop next to a bound staple (LIS2, fitted to B1–B2 and applied to
  B1m–B2m), and the inner position (LIS3, an extra penalty). In the small
  origami "the shift in Tm was less than 10 ◦ C for LIS1, between 5 ◦ C and
  7 ◦ C for LIS2 and up to 15 ◦ C for LIS3." A further stabilizing term,
  proportional to neighbouring bases, corrects a constant −4 K offset.
- **Large origamis (section V).** Four rectangles on M13mp18 at
  0.4 °C min⁻¹: the model reproduces the annealing and melting curves and
  the relative hysteresis ("O2 has only 4K shift between annealing-melting,
  whereas O4 has 10K shift"). Fewer crossovers raise stability: a
  13-27-14 staple design gains "almost 20 ◦ C" over 8-16-8.
- **Conclusion (section VI).** "the folding of each staple is strongly
  dependent on the existence of a nearby cluster of folded staples."
  GC-rich staples "provide with initial nuclei that facilitate the folding
  of the neighbour staples", so AT-rich staples fold at a temperature
  "dependent on the distance to the set of these initial nuclei". The
  hysteresis arises because "the neighborhood of each staple is different
  in the annealing or melting."

## Assumptions

- Each staple part fully bound or unbound; no misfolded binding; no
  scaffold secondary structure (Hypothesis 1).
- No non-contiguous bound parts of one staple (Hypothesis 2).
- Strong correlation between neighbouring staples' presence, ordered by
  their single probabilities (Hypothesis 3); local equilibrium at each
  temperature step, no kinetics.
- Neighbourhoods limited to crossovers in one row within 75 bases; the
  results are said to be robust to this.
- Nearest-neighbour thermodynamics with temperature and salt corrections,
  the salt correction slightly modified to fit the small origamis.

## Concepts

- **Local intermediate state**: the geometry a crossover's loop has when a
  staple's second part binds, which sets its entropic penalty.
- **Inner and outer positions**: whether the shortest path between a
  crossover's ends runs through the staple itself (inner) or through the
  scaffold, forming a bulge (outer).
- **Nucleus**, informally: high-GC staples folding first and lowering their
  neighbours' cost.

## Bearing on the record

- **[QUESTION-380](../questions.d/QUESTION-380.md)** (evidence, partial). The measured shifts are a fold's
  melting temperature rising once a neighbour has closed, the observable
  the question's note of 2026-11-05 on Majikes et al. asked for. The
  paper's picture of nuclei whose effect decays with distance is a
  predictor of when a staple folds from where the first ones sit. It is
  monotone by construction: with misfolds excluded, adding a nucleus can
  only help, so it cannot say which nuclei lower the chance of the target.
- **[THEORY-1454](../theory.d/THEORY-1454.md)** (Majikes et al.; corroboration of the inferred part).
  Majikes et al. infer that short, cheap folds make neighbouring folds
  cheaper and say that confirming it "will require additional testing in
  systems with multiple folds". This earlier work, by another group,
  measures that a bound neighbour raises a fold's melting temperature on
  a two-staple scaffold. It does not reproduce what [THEORY-1454](../theory.d/THEORY-1454.md) measured
  (the comparison with bimolecular binding of the same domain, and the
  fall with fold distance); its loop-length dependence is a model term,
  not a measurement.
- **[CLAIM-562](../claims.d/CLAIM-562.md)** (a parallel). Position in the connectivity, inner against
  outer, changes a staple's melting temperature by 3.5 to 7 °C for the same
  sequence or pair: where a constraint sits matters, in a thermodynamic sense, not
  the success-of-folding sense the claim states. An analogy; no edge.
- **[CASE-tmp2a9lm](../cases.d/CASE-tmp2a9lm.md)** (background). The lead run's test system uses
  cooperative attachment (a component bound by more strength attaches much
  faster), the regime of the kinetic tile assembly model; the paper's
  finding is a measured instance of that kind of cooperativity in origami.

## Limitations

- Two staples per measured construction; the large-origami evidence is a
  model fit, not staple-resolved data, so "multi-fold" coupling beyond
  pairs is inferred.
- Model parameters (LIS2's enthalpy and entropy, the LIS3 unbinding, the
  stabilizing term, the salt correction) are fitted on the small origamis;
  LIS2 is checked on a second staple pair, the rest are not checked
  independently.
- Misfolds and kinetics are excluded, so traps cannot appear; the
  hysteresis is explained by neighbourhoods differing between ramps, not
  by kinetic trapping.
- Figure images not read; numbers are from the text.
