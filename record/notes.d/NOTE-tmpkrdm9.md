---
status: Read
paper: LIT-tmp2dmok
title: 'Rudner and others 2013 — Anomalous edge states and the bulk-edge correspondence for periodically-driven two dimensional systems'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1212.3324 (served v2, 25 Jul 2013), HTTP
    200, PDF. Kind of copy: arXiv preprint, the authors' manuscript of the
    Phys. Rev. X article (step 5, arXiv). Fetched 2026-11-19; nothing
    stopped the fetch. Text extracted with pdftotext to dl/text.txt. Read:
    abstract; introduction; §I (bulk-edge correspondence, static vs driven);
    §II (model of anomalous edge states); §III A–B (construction of the
    invariant) and the numerical confirmation; the end of §IV; §V
    Discussion. Skimmed: §III C (relation to Chern numbers). Skipped: §IV's
    frequency-domain derivation; Appendices A–C (proofs). Verdict on the
    source's characterization ("anomalous edge states in periodically driven
    systems that static invariants miss"): accurate. The use it was cited
    for, interfaces between dynamically distinguished phases, holds only by
    inference. The paper establishes dynamically distinguished phases with
    the same stroboscopic bulk, but it treats edges, not interfaces between
    two driven regions.
date: '2026-11-19'
---

# NOTE-tmpkrdm9: Rudner and others 2013 — Anomalous edge states and the bulk-edge correspondence for periodically-driven two dimensional systems

## Contribution

For periodically driven, non-interacting 2D lattice systems, the paper shows that the Chern numbers of the Floquet bands do not determine the chiral edge modes. Chiral edge modes can exist when every Floquet band has Chern number zero. The paper constructs a new bulk invariant, a winding number W of the time-dependent evolution operator U(k, t) over the whole driving period, that gives the net number of chiral edge modes in each quasi-energy gap. It derives this in the time domain and, for weak harmonic driving, in the frequency domain, and it proposes cold-atom, solid-state and photonic realizations (arXiv 1212.3324 v2; Phys. Rev. X 3, 031005, 2013).

## Key results

- **The anomaly** (abstract): "in driven systems in two dimensions (2D), robust chiral edge states can appear even though the Chern numbers of all the bulk Floquet bands are zero."
- **Why statics differ** (§I): "Therefore, in a static two-band system, the Chern number uniquely defines the net number of chiral edge states crossing the band gap." In the driven case quasi-energy lives on a circle, so an edge mode can wind through the zone edge at ε = π/T.
- **The one-period operator is not enough** (§I): "The example above shows that the bulk Floquet operator, U (T ), does not carry sufficient information to predict the number of chiral Floquet edge modes".
- **The model** (§II): a five-step hopping cycle on a bipartite square lattice. At JT/5 = π/2, "Therefore the bulk Floquet operator for this case is simply the identity", yet in a strip "Over each complete driving cycle, a particle moves by one unit cell along the edge."
- **Same stroboscopic bulk, opposite edges** (§II): for the reversed cycle, "although particles circle around the plaquettes in the anti-clockwise direction, the Floquet operator (which is still identity) is the same as that of the original cycle." The intra-cycle information "determines the propagation direction of the edge states when the system is terminated."
- **The invariant** (§III A–B): "The winding number depends on the full time evolution, throughout the driving cycle, through the unitary evolution operator U (t)." For U(k, T) = 1 the authors show the edge count equals W[U]: "In appendix A we show that this guess is correct". For general U they deform to an operator Uε with trivial Floquet operator and compute W[Uε].
- **Checked numerically** (§III, Fig. 3): example spectra "confirm the correspondence between the winding number, calculated from the bulk evolution operator in the periodic geometry, and the edge state count in each gap in the strip geometry."
- **Chern numbers as differences** (§III C): Chern numbers relate to differences of winding numbers between gaps, as the derivation of the relationship shows (read in outline only).
- **Main result and caveats** (§V): "Our main result in this work is the construction of a new invariant which fully captures the edge state spectrum for periodically driven systems." For realistic slow driving, "strictly speaking, there is no gap in the Floquet spectrum at any quasi-energy", though edge states remain well defined for weak driving. "we have not discussed the filling of these states". And "A full topological classification for driven systems is yet to be developed".

## Assumptions

- Non-interacting particles; translationally invariant, finite-range tight-binding hopping; strict time-periodicity.
- No extra symmetries imposed (class A analogue).
- A gap in the quasi-energy spectrum at the ε of interest.
- Edges are terminations against vacuum (strip geometry). Interfaces between two different driven regions are not treated.

## Concepts

- **Floquet operator U(T) and quasi-energy**: stroboscopic evolution over one period. Quasi-energy is defined modulo 2π/T, so the spectrum lies on a circle.
- **Anomalous edge states**: chiral edge modes in a driven system whose Floquet bands all have zero Chern number.
- **Winding number W[U]**: a 3D winding of U over (kx, ky, t), defined for a loop with U(T) = 1. It is the bulk invariant of a driving process, not of a state.
- **Dynamically distinguished phases**: two drives with the same stroboscopic bulk (here U(T) = 1 for both) but opposite intra-cycle circulation, and so opposite edge chirality.

## Bearing on the record

- QUESTION-378: qualifies, and it is the source's reason for filing (the LIT cites it for interfaces between dynamically distinguished phases). The paper shows that two bulk systems with identical one-period evolution are topologically distinct by their intra-cycle dynamics, with opposite edge chirality against vacuum. It does not treat an interface between two driven regions. That such an interface would carry the difference of their winding numbers is an inference from the edge counts, not a result of the paper. For the question, this adds a kind of distinctness between phases that no snapshot of the state reveals.
- QUESTION-tmp57ji2: leaves open. The edge modes are single-particle states on a fixed drive. Mode occupation and back-action on the drive or on any order parameter are excluded ("we have not discussed the filling of these states").
- CLAIM-606: leaves open, but it marks a third sense of "topological" that the record should keep apart. Here the invariant belongs to a periodic process (a loop of evolution operators), not to a field configuration (THEORY-1507) and not to a static Hamiltonian around a defect (Teo and Kane, LIT-tmp4lexz). A structure protected this way persists only while the drive runs, which places it with the supplied routes as much as with the topological one.
- THEORY-1408: a parallel. Like Kane and Lubensky's index theorem, it equates a boundary count with a bulk topological count. Here the bulk count needs the whole time evolution, not a single operator. It is not a case of THEORY-1408's mechanical zero-mode count and does not meet its promote_when.

## Limitations

- Read: abstract, introduction, §I, §II, §III A–B and the numerical confirmation, the end of §IV and §V. Skimmed: §III C. Skipped: §IV's frequency-domain derivation and Appendices A–C (the proofs that n_edge = W[U]).
- Non-interacting, clean and translation-invariant. The question of filling and of interactions, and the full classification with symmetries, are left open by the authors.
- Edges only, not interfaces.
