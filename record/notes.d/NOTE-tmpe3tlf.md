---
status: Skimmed
paper: LIT-tmpht8ga
title: 'Pattern formation outside of equilibrium'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Skimmed. About 30 of the review's 262 pages were read closely, from a
    Tesseract OCR of the scanned copy in the Caltech Authors repository:
    the abstract and contents, §I, §II.A, §II.B.3, §II.E, §III.A.1–4,
    §X.A.1, §X.B.5, the opening of §XI.A and §XIII. Everything else (the
    technical core, §§IV–IX, and §§VII, XII and the appendices) was only
    searched by keyword. The OCR loses most equations; none was checked
    against a page image. This is a reading for the record's question (what
    the review says about dissipative structures, convection, Turing
    patterns and BZ, and about extremum principles), not a reading of the
    review's own technical results.
date: '2026-10-02'
summary: >-
  Read for the record's question only. Patterns away from equilibrium are
  classified by the linear instability of a uniform state (type I_s, III_o,
  I_o) and described near onset by universal amplitude equations. There is
  in general no free energy or Lyapunov functional selecting them. Bénard's
  own 1900 hexagons were surface-tension-driven, not Rayleigh's buoyancy
  convection. Closed chemical systems must reach equilibrium, so their
  patterns are transients or need pumping. No global minimization
  principle exists beyond a perturbative one near threshold.
---
<!-- inactive-ok-file: LIT-tmpxgib0 — Deferred, no lawful full text; Glansdorff & Prigogine, cited for the sentence this review quotes from it -->
<!-- inactive-ok-file: LIT-tmpd737a — Deferred, no lawful full text; Nicolis & Prigogine, cited as the review's source for the name "dissipative structures" -->

# NOTE-tmpe3tlf: Pattern formation outside of equilibrium

*Skimmed: about 30 of 262 pages, chosen for the record's question. The
review's technical core (amplitude and phase equations, defects, pattern
selection, chaos, and the system-by-system chapters) was not read, so there
is no claims table.*

## Contribution

The review puts convection, Taylor–Couette flow, parametric waves,
reaction–diffusion chemistry, biological pattern models, solidification and
optics into one framework. Patterns are classified by the wave-number q₀ and
frequency ω₀ of the linear instability of a uniform state, and described near
onset by universal amplitude equations and further above it by phase
equations. Throughout, the authors weigh theory against quantitative
experiment.

## Key insight

What unifies non-equilibrium patterns is not a thermodynamic principle but
the shared mathematics of instabilities: near threshold, very different
systems obey the same amplitude equation and differ only in its
coefficients. Away from threshold there is no free energy to minimize, so
which pattern appears is settled by boundaries, defects and the protocol, not
by an extremum principle.

## Assumptions

What the read sections take as their setting:

- **Constant external conditions.** The systems are held under constant
  non-equilibrium driving, with a control parameter R raised through a
  threshold R_c (§I.B).
- **Dissipation.** The authors consider "almost exclusively systems where
  dissipation is important" (fn. 1.2). Dissipative dynamical systems are those
  whose phase-space volumes contract onto attractors (§III.A.1).
- **Determinism.** Deterministic "microscopic" equations (Navier–Stokes,
  reaction laws) are the starting point. Noise is usually negligible in
  macroscopic experiments (§XIII.B(iii)).
- **Large systems.** The systems are large compared with the instability
  length 1/q₀, so boundaries are a perturbation (§I.B).

## Key results

From the sections read:

- **Classification (§I.B).**
  - Type I_s (q₀ ≠ 0, ω₀ = 0): stationary periodic patterns, such as
    convection rolls and Turing patterns.
  - Type III_o (q₀ = 0, ω₀ ≠ 0): uniform oscillation, such as the stirred
    BZ reaction.
  - Type I_o (q₀ ≠ 0, ω₀ ≠ 0): travelling or standing waves.
  Footnote 1.1 credits Turing (1952) with first linking macroscopic pattern
  formation to linear instabilities.
- **Rayleigh–Bénard convection (§II.A).** The control parameter is the
  Rayleigh number R = gαΔTd³/(κν). The conducting state goes unstable at
  R_c ≈ 1708, whatever the fluid, with q₀ of order 1/d. The
  finite wave-length comes from a conservation law: the fluid "cannot rise as
  a whole".
- **Bénard–Marangoni (§II.B.3).** "The original experiment of Bénard (1900)"
  in an open dish gave hexagons. Rayleigh (1916) explained them by bulk
  buoyancy, but "it was later discovered (Pearson, 1958) that the hexagon
  pattern resulted from a surface instability caused by a temperature
  dependent surface tension". The control parameter is the Marangoni number,
  which does not involve g.
- **Reaction–diffusion (§II.E).** In the linear two-species model (2.7) a
  stationary finite-wave-number instability needs the activator's diffusion
  length (D₁/a₁)^½ to be shorter than the inhibitor's ("local activation with
  lateral inhibition"). Large cross-coupling instead gives the uniform
  oscillation seen in BZ. "A closed chemical system, just as a closed fluid
  system, ultimately must come to equilibrium. Nonequilibrium phenomena of
  interest to us either occur as a transient … or in response to some
  external chemical pumping" (p. 865).
- **Lyapunov functions (§I.B, §III.A.3).** Near equilibrium a coarse-grained
  free energy selects the pattern, but "in general no such free energy (or
  other so-called Lyapunov potential) can be defined for nonequilibrium
  systems, though there are notable exceptions" (p. 857). Graham's
  "nonequilibrium potential" exists for general systems but is singular and
  "does not determine the dynamics" (p. 868).
- **BZ (§X.A.1).** Belousov found the reaction in 1951; Zaikin and
  Zhabotinsky (1970) "already revealed the existence of chemical waves". The
  Oregonator is "a simplified model". Closed pattern experiments "run down in
  finite time (typically less than 100 periods of oscillation)", which open
  gel reactors fed at their rims overcame (§X.B.5, p. 1046).
- **Turing patterns (§X.B.5).** Stationary Turing structures were long sought
  and found only recently: Ouyang et al. (1989, 1991) with an imposed
  gradient; Castets et al. (1990) in a gel, from differing diffusivities; and
  Ouyang and Swinney (1991), without macroscopic gradients, giving stripes and
  hexagons in the chlorite–iodide–malonic-acid reaction (Fig. 87).
- **Morphogenesis (§XI.A).** "The chemical identification of the morphogens
  has proved elusive, so that the theories are essentially phenomenological"
  (p. 1050). The activator–inhibitor condition is necessary within (2.7) but
  "by no means a general necessary condition" for a type I_s instability.
- **What has not been accomplished (§XIII.B, p. 1077).**
  - No "useful" extremum principle for non-equilibrium steady states, "useful"
    meaning one that replaces and simplifies the dynamics (fn. 13.1).
  - They quote Glansdorff and Prigogine (1971, p. 108): "the search for a
    universal kinetic potential has proved to be unsuccessful". Those
    authors proposed instead "more specialized variational principles" and a
    "universal evolution criterion" in the form of an inequality.
  - Landauer: relative occupation of competing states depends on the
    trajectories joining them, not only on local properties.
  - The maximum-entropy formalism has produced no new physical results on
    pattern formation known to the authors.
  - Self-organized criticality is "not supported by our detailed studies".
- **On life (§XIII.C, p. 1080).** "There is no evidence for the existence of
  any global minimization principles controlling the structure, except as a
  perturbative statement near threshold." Such a principle "would make it
  easier to generalize" from laboratory patterns to biological complexity.
  That reaction–diffusion mechanisms carry molecular information to the
  cellular level is "plausible to us (although by no means demonstrated)".
  Against Anderson (1981), they hold that spontaneously broken continuous
  symmetry, with its phase dynamics, generalized rigidity and topological
  defects, is "established" in non-equilibrium laboratory systems.

## Concepts

- **dissipative structures**: one of three names (with "synergetics" and
  "self-organization") for macroscopic spatial structure in steady state
  under constant non-equilibrium conditions, cited to Nicolis and Prigogine
  ([LIT-tmpd737a](../literature.d/LIT-tmpd737a.md)) (§I.B). The review does not use it as a technical term.
- **type I_s / III_o / I_o instability**: the classification by (q₀, ω₀) at
  threshold (§I.B).
- **amplitude equation**: the universal equation for the slow envelope of the
  unstable mode near threshold (§I.C).
- **Lyapunov function**: V with V(U₀) = 0 and dV/dt < 0 away from the
  attractor U₀, which exists for gradient systems (§III.A.3).

## Connections

- **Prigogine's Nobel lecture ([LIT-tmp452jw](../literature.d/LIT-tmp452jw.md)), read.** On the point the record
  cares about, they agree. The lecture restricts minimum entropy production
  to the strictly linear regime and offers only a sufficient stability
  criterion far from equilibrium. The review finds no global principle at
  all beyond threshold. The difference is emphasis. The lecture presents
  dissipative structures as "a new type of dynamic states of matter" with
  their own thermodynamics. The review treats them as instabilities of
  dynamical systems, uses the term once, and the phrase "entropy production"
  does not occur anywhere in the OCR text. On convection the review corrects the lecture: the
  lecture calls the buoyancy-driven Rayleigh problem the "Bénard
  instability", but Bénard's own cells were Marangoni convection.
- **Glansdorff and Prigogine ([LIT-tmpxgib0](../literature.d/LIT-tmpxgib0.md)), Deferred.** The review is the
  record's only read source for that book's p. 108 admission.
- **Turing ([LIT-tmptpgzu](../literature.d/LIT-tmptpgzu.md)), read.** Credited as the origin of the
  instability-based view (fn. 1.1) and of the morphogen mechanism (§XI.A).
  The first chemical realizations came 37–39 years later.
- **BZ ([LIT-tmpoej2u](../literature.d/LIT-tmpoej2u.md)), read.** The review's BZ section and Zhabotinsky's
  agree on mechanism and phenomenology. The review supplies the point that
  closed pattern experiments run down, which makes the open reactor the
  setting in which BZ patterns are dissipative structures in the steady-state
  sense.
- **Emergence survey ([LIT-021](../literature.d/LIT-021.md)).** [NOTE-007](NOTE-007.md) records that its history of
  emergence runs from Anderson's "More is different" to Prigogine. The
  review's closing section takes up a later Anderson paper (1981) that
  doubted broken symmetry means much away from equilibrium, and argues that
  for laboratory patterns it is "established".

## Bearing on the record

- **[LIT-192](../literature.d/LIT-192.md) (demarcation).** The review gives the physicist's reason the
  demarcation cannot come from the physics of self-organization. The same
  instabilities produce rolls, hexagons, spirals and Turing spots in fluids,
  gels and models of embryos, and there is no global principle that would
  single out one class of dissipative system as directed toward an end. Its
  closing doubt about using such structures as a first step toward life is
  the strongest read statement in the record that dissipative pattern
  formation is necessary at most, not distinctive.
- **[LIT-211](../literature.d/LIT-211.md) ("Dissipative Self-Organizing Systems").** The review's remark
  that closed systems' patterns are transients, and open ones' depend on
  "external chemical pumping", sharpens what a dissipative definition of life
  must add. An organism is not held away from equilibrium by an
  experimenter's feed; whatever a definition says instead is the part that
  does the work.
- **For the parallel filings on entropy-production principles:** §XIII.B is
  a read, citable statement that, as of 1993, no general extremum principle
  for non-equilibrium steady states had produced physical results on pattern
  formation, maximum-entropy formalisms included.
- **No ML instruction.**

## Limitations

- **The review's limits.** By its own account it treats only states "related
  to modes appearing at linear instabilities" (§XIII.C). Dendrites, fractal
  growth and strong turbulence are outside it.
- **This skim's limits.** The technical core was not read, so nothing here
  certifies the amplitude-equation results, the stability balloons or the
  chaos chapters. Quotations come from OCR.

## Open questions

- Is there any non-perturbative principle selecting patterns far from
  threshold? The review says there is none known, and that finding one would
  most likely come from "continu[ing] investigating specific systems".
- Does any of the post-1993 work on entropy-production principles meet the
  review's standard of "useful", that is, replace the dynamics rather than
  restate it? That is the question for the parallel filings.

## Corrections

- none to a seeded skim (there was no seed)
- **Request's choice.** The request offered Bénard (1900) or a standard
  review, and preferred this one if readable. It was readable, as a scanned
  copy in the Caltech Authors repository, and is filed. Citation details are
  right: Rev. Mod. Phys. 65(3):851–1112, 1 July 1993,
  DOI 10.1103/RevModPhys.65.851.
- **Section numbering.** The OCR shows the conclusion's heading as "XII.
  CONCLUSION", but the contents list it as XIII ("XII. Other Systems"
  precedes it). The text's own cross-reference to "Sec. XII.C" for spin
  waves agrees with the contents, so the conclusion is §XIII.
