---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpyq606](../notes.d/NOTE-tmpyq606.md)); worth reading as the founding paper of reaction–diffusion pattern formation and the origin of what the Brussels school later called the "Turing bifurcation". A homogeneous, stable steady state of reacting and diffusing chemicals can be destabilized by diffusion itself and settle into a stationary pattern with an intrinsic "chemical wave-length". The analysis is linear and near onset by design, every biological application is offered as suggestion, and the paper says outright that its patterns are "dynamic equilibria" fed by "a continual supply of free energy", which places them among dissipative structures before the term existed.'
title: 'The Chemical Basis of Morphogenesis'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the JSTOR scan of the published article, Phil. Trans. R.
    Soc. Lond. B 237(641):37–72, as posted on a Caltech course page,
    https://www.dna.caltech.edu/courses/cs191/paperscs191/turing.pdf, 37
    PDF pages; the publisher's PDF at royalsocietypublishing.org returned
    HTTP 403 to this session, and Unpaywall lists no open-access copy). I
    read the abstract and all thirteen sections and the references. The
    scan's OCR text loses most displayed equations, so I read page images
    of printed pp. 37, 55, 58 and 60 for the stability conditions (9.4a,
    b), the parametrization (9.5)–(9.7), the non-linear amplitude
    equations and the §10 data. The six cases of §8 and
    the summary of §11 were read from the text. Equations (6.1)–(6.11),
    (8.3)–(8.6) and §12's spherical-harmonic formulae were not checked
    against images. The article carries "Received 9 November 1951—Revised
    15 March 1952" and "Published 14 August 1952"; `published:` is the
    latter, which Crossref also gives. Not held in the Anthology of the
    SOTA: a grep of its literature.d, notes.d and theory.d for
    "morphogenesis", "Turing" and the DOI found no entry for it.
tags:
- complex-systems
- natural-sciences
- mathematics
date: '2026-10-02'
published: '1952-08-14'
doi: '10.1098/rstb.1952.0012'
first_author: 'Turing'
keywords:
- 'morphogenesis'
- 'morphogens'
- 'reaction-diffusion'
- 'instability'
- 'symmetry breaking'
- 'chemical wave-length'
- 'phyllotaxis'
- 'gastrulation'
implementations: []
summary: >-
  Turing (1952), DOI-10.1098/rstb.1952.0012. Chemicals ("morphogens")
  that react and diffuse through tissue can turn a stable homogeneous
  state unstable, with random disturbances setting which pattern grows. On
  a ring of cells the linearized onset takes six forms. The most important
  is stationary waves of finite "chemical wave-length", which (9.4a, b)
  allow for two morphogens only if they diffuse at different rates. A
  20-cell example computed on the Manchester computer gives a three-lobed
  pattern. Hydra tentacles, whorled leaves, dappling and gastrulation are
  suggested applications, not tested ones.
---
<!-- inactive-ok-file: LIT-tmpd737a — Deferred, no lawful full text; Nicolis & Prigogine, named only as where the Brusselator's Turing bifurcation is worked out, not leaned on -->

# LIT-tmptpgzu: The Chemical Basis of Morphogenesis

A. M. Turing (1952), *Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences 237(641):37–72* — DOI-10.1098/rstb.1952.0012

## Key takeaways

- A system of reacting and diffusing chemicals can start homogeneous and stable and become unstable as its parameters drift. Random disturbances then grow into a pattern, so symmetry is broken without any pre-existing asymmetry that matters.
- In the case that matters most, the pattern is a set of stationary waves whose spacing, the "chemical wave-length", is fixed by reaction rates and diffusibilities, not by the size of the tissue. For two morphogens this needs them to diffuse at different rates.
- The patterns are steady only dynamically. They need "a continual supply of free energy", taken from "fuel substances" degraded to "waste products", because diffusion continually degrades energy (p. 66).

## Standing in the record

Filed on 2026-10-02 at the owner's request, as one of the canonical systems of
the dissipative-structure programme. The Nobel lecture ([LIT-tmp452jw](LIT-tmp452jw.md)) names
the stationary reaction–diffusion instability of the Brusselator the "Turing
bifurcation", after this paper. Nicolis and Prigogine's monograph
([LIT-tmpd737a](LIT-tmpd737a.md)) works the Brusselator case out.

Its bearing on what the record holds:

- **It is a dissipative structure in all but name, and the paper says why.**
  Turing writes no thermodynamics, but his §10 makes the thermodynamic
  point plainly: the final patterns are "only dynamic equilibria" and are
  maintained by free energy degraded from fuel to waste. That is the
  Prigogine criterion (an open system, held away from equilibrium, sustained
  by flows) stated a quarter-century before the Nobel lecture, for a biological model.
- **The demarcation question in [LIT-192](LIT-192.md).** Turing's mechanism is offered as
  part of how an organism gets its form, yet it is the same mechanism as a
  chemical pattern in a gel. That is a concrete case of what Nahas and Sachs
  report: dissipative pattern formation is shared by organisms and
  non-organisms, so it cannot be what demarcates them.
- **Primitive metabolic cycles ([LIT-036](LIT-036.md)).** Its catalytic, non-equilibrium
  cycle of species whose homogeneous state goes unstable is an heir of this
  paper's method. [NOTE-079](../notes.d/NOTE-079.md) records that its authors set their mechanism
  against Turing's and say the difference is that "it is truly the catalysts
  and not the reactants that self-organize".
- **The Belousov–Zhabotinsky reaction ([LIT-tmpoej2u](LIT-tmpoej2u.md)) and Cross and Hohenberg
  ([LIT-tmpht8ga](LIT-tmpht8ga.md)).** Turing's case (e), travelling waves, needs three or more
  morphogens; BZ waves are the excitable-medium kind his linear analysis does
  not cover. Stationary Turing patterns in a chemical reactor came only
  in 1989–1991 (Ouyang et al. with an imposed gradient; Castets et al. 1990;
  Ouyang and Swinney 1991, without one), in open reactors fed continuously
  with reagents. Cross and Hohenberg (§X.B.5, §XIII) review them as
  "confirming Turing's original intuition".

No instruction for machine-learning practice. The anthology does not hold it.
