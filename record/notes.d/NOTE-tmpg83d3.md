---
status: Read
paper: 'LIT-tmpv09vj'
title: 'Patsyk, Sivan, Segev and Bandres — Branched flow of light in a soap film'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from the publisher's PDF posted on the Segev group's
    Technion faculty publications page,
    https://phsites.technion.ac.il/publications/msegev/Nature-583-60-2020.pdf,
    6 pages, text by pdftotext: the whole main text, the four figure
    captions and the reference list. Not read: the Methods, published
    online only, and the Supplementary Information and Videos, which this
    PDF points to. The filer rechecked every quote below against the
    downloaded text; all were found.
date: '2026-11-15'
summary: >-
  Light guided in a soap film under a micrometre thick branches as it
  propagates, because the film's smooth thickness variations make a weak
  correlated potential with correlation length far above the wavelength.
  The paper tests two universal signatures of branched flow, the
  first-branch distance scaling as lc v0^−2/3 (read from the scintillation
  index) and heavy-tailed branch intensities, and reports a branch that
  keeps its width over ten Rayleigh lengths. Linear wave physics; no claim
  about computation.
---
<!-- inactive-ok-file: CLAIM-182 — a Proposed claim, cited as an analogy or as having no bearing -->

# NOTE-tmpg83d3: Patsyk, Sivan, Segev and Bandres — Branched flow of light in a soap film

## Contribution

The first experimental observation of branched flow of light. Branched
flow had been seen for electrons in two-dimensional electron gases and for
microwaves in cavities, never in optics. The platform is cheap and
reconfigurable: a weak air flow near the film gives a new realization of the
disorder, and the potential can be reconstructed from the film's
white-light interference colours. With it the authors test two universal
signatures of branched flow and report a third observation, that branches
resist diffraction broadening.

## Key insight

A weak disordered potential that varies slowly compared with the
wavelength does not scatter a wave diffusely. It focuses it, through
caustics, into channels that keep splitting; how far the wave travels
before the first split is set by the correlation length and the strength
of the disorder alone.

## Assumptions

- The film is a two-dimensional slab waveguide, single-mode in thickness,
  so an effective index n_eff(x, z) stands in for the three-dimensional
  index, and the paraxial wave equation takes the form of a
  time-independent Schrödinger equation with V(x, z) = k0²(n̄² − n_eff²),
  ⟨V⟩ = 0.
- The disorder is weak, v0 of a few per cent, with correlation length much
  larger than the wavelength.
- The disorder statistics are stationary across a film (they vary by about
  5% across its sections).
- The scaling law is taken from earlier theory (Kaplan 2002; Metzger et
  al. 2010), and checked here, not derived.

## Key results

- **Mechanism** (p. 60): "When waves propagate through a weak disordered
  potential with correlation length larger than the wavelength, they form
  channels (branches) of enhanced intensity that keep dividing as the waves
  propagate." The branches are caustics, "foldings of the Lagrangian
  manifold in phase space".
- **The potential** (p. 61, Fig. 1c): "smooth thickness variations in the
  film act as a correlated disordered potential", with "v0 ≈ 1–5% and
  lc ≈ 90–350 µm".
- **First-branch scaling** (pp. 61–62, Fig. 3): earlier work found the
  first-branch distance to satisfy d0 ∝ lc v0^−2/3, and here the
  scintillation index "grows sharply at a distance proportional to"
  lc v0^−2/3, over ensembles of 10–20 realizations averaged across the
  transverse coordinate.
- **Heavy tail** (Fig. 4a–b): over 100 realizations in one film, "the
  cumulative probability displays a heavy tail, as compared to that in an
  uncorrelated random potential (the Rayleigh fit)".
- **Arrested diffraction** (p. 63, Fig. 4e): "The branched channel
  maintains the same width for at least ten diffraction lengths (Rayleigh
  lengths)". The paper distinguishes this from Anderson localization,
  since the potential also varies along the direction of propagation.
- **Linearity** (abstract): "despite the random variations in the medium
  and the linear nature of the effect, the filaments remain collimated".

## Concepts

Branched flow; caustics; correlated weak disorder; scintillation index;
first-branch distance; heavy-tailed intensity statistics; optical
potential; arrest of diffraction broadening.

## Bearing on the record

- **A's characterization.** That branched flow is waves in "a smoothly
  varying, weakly disordered medium" concentrating "into narrow, branching
  channels", and that the soap film's thickness variations make "a
  spatially correlated optical potential" under "linear wave physics",
  holds. The condition that the correlation length exceed the wavelength
  is left out. The "et al." after four names is wrong. The scintillation
  index and the scaling A credits to the 2026 paper ([LIT-tmpn3i8n](../literature.d/LIT-tmpn3i8n.md)) are
  already here.
- **[CLAIM-182](../claims.d/CLAIM-182.md), [THEORY-272](../theory.d/THEORY-272.md), [THEORY-1036](../theory.d/THEORY-1036.md), [TERM-064](../terms.d/TERM-064.md), [THEORY-758](../theory.d/THEORY-758.md)**: no
  bearing. This is wave transport, not storage, memory, capacity or
  multiscale analysis. Any bridge to learning is A's analogy, and the
  paper makes no claim about computation.

## Limitations

- The heavy tail is shown against a Rayleigh fit only; no exponent or
  model fit is given in the main text.
- The scaling is shown as agreement between marked lc v0^−2/3 lines and
  scintillation peaks across a few films, not as a fitted exponent; the
  Supplementary Information, which may hold more, was not read.
- The arrest of diffraction is shown for one characteristic branch; that
  it "seems to be a universal feature" is offered, not tested.
