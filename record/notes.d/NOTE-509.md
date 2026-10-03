---
number: 509
status: 'Read'
formerly:
- NOTE-tmpvbc4b
paper: 'LIT-645'
title: 'Ultraviolet Superradiance from Mega-Networks of Tryptophan in Biological Architectures'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the version of record (PMC11075083, CC BY, via the
    Europe PMC full-text XML): main text, Table 1, figure captions,
    references. The supplement was read from arXiv v1 (2302.01469),
    which carries it as S1–S4 with Tables S1–S3; the publisher's own SI
    PDF was not opened. Equations 1–5 of the published text are images
    and were not recovered; the model is quoted from arXiv v1 Eqs. 4–12.
    Figures were read from captions and text, not from plotted data.
date: '2026-10-03'
summary: >-
  A radiative non-Hermitian Hamiltonian for N tryptophan 1La dipoles (single
  excitation) predicts superradiant states in microtubule architectures
  (max Γ/γ ≈ 4000 in a centriole, ≈ 7000 extrapolated for bundles) and a
  thermal quantum yield that grows with size and is insensitive to static
  disorder up to 200 cm⁻¹. Steady-state spectroscopy gives tryptophan QY
  17.6 ± 2.1% in microtubules against 10.6 ± 0.6% in tubulin dimers. No
  lifetimes were measured, so the radiative rate is inferred, not observed.
---

<!-- inactive-ok-file: LIT-627 — Deferred; named for contrast as the collapse-side test of Orch OR, with no relation claimed -->

# NOTE-509: Ultraviolet Superradiance from Mega-Networks of Tryptophan in Biological Architectures

## Contribution

It extends the authors' earlier single-microtubule superradiance model
(Celardo et al. 2019, ref. 28) to tryptophan networks of 10⁴–10⁵ chromophores
in centrioles, axonemes and hexagonal axon-like bundles. It adds a thermal,
disorder-averaged prediction of the fluorescence quantum yield, and it reports
a steady-state measurement of that yield in tryptophan, tubulin dimers and
microtubules.

## Key insight

Superradiance itself is fragile: static disorder of room-temperature size
cuts the brightest state's enhancement by two orders of magnitude. The
quantum yield is not fragile. It depends on how much dipole strength sits
within k_BT of the bottom of the exciton band, and disorder spreads that
strength among neighbouring states without moving it far. So the quantum
yield, not the peak decay rate, is the observable that can show cooperativity
at room temperature.

## Assumptions

- **Two-level emitters, tryptophan only** (SI S2): each tryptophan is its 1La
  transition dipole, λ = 280 nm (E₀ = 35 714 cm⁻¹), μ = 6 D, γ = 4μ²k₀³/3 =
  2.73 × 10⁻³ cm⁻¹ (radiative lifetime about 1.9 ns). Tyrosine,
  phenylalanine, vibronic transitions and higher transitions are left out.
- **Single-excitation manifold**, justified by the weak intensity of
  biological ultraweak photon emission.
- **Effective Hamiltonian** (arXiv v1 Eqs. 5–8): H_eff = Σₙ(ħω₀ − iγ/2)|n⟩⟨n|
  + Σ_{m≠n}(Ω_mn − iΥ_mn/2)|m⟩⟨n|, with the full retarded dipole–dipole
  couplings. The complex eigenvalues E_j − iΓ_j/2 give energies and decay
  rates.
- **Geometry** from PDB 1JFF: 8 tryptophans per dimer, 13 dimers per spiral,
  dimers rotated 27.69° and shifted 0.9 nm per step; bundles in hexagonal
  packing at 50 nm centre to centre; the centriole as nine microtubule
  triplets 100 nm from the axis.
- **Thermal equilibrium** within the excited manifold (Boltzmann weights over
  E_j), and a single, size-independent non-radiative rate per tryptophan,
  γ_nr ≈ 0.0193 cm⁻¹, fixed from the measured tryptophan QY in buffer. The
  authors say this neglects new non-radiative channels in large assemblies.
- **Static disorder only**: uniform on-site energy noise of width W, averaged
  over 10 realisations. No dynamic disorder or exciton–phonon coupling.

## Key results

- **Centriole (Fig. 5).** max(Γ_j/γ) grows with length and saturates near
  4000 at vertebrate centriole lengths. A 320 nm centriole has 112 320
  dipoles, with its spectrum spanning about E₀ ± 100 cm⁻¹. At W = 200 cm⁻¹
  the enhancement falls from about 3600 to about 20. Longer centrioles need
  larger W to lose the same fraction of enhancement (cooperative robustness).
- **Axon-like bundles (Fig. 6).** For 7, 19, 37, 61 and 91 microtubules,
  max(Γ_j/γ) is fitted by a two-variable curve (bundle size and length) with
  no free parameters. Extrapolation gives about 7000 for large bundles.
- **Thermal quantum yield (Fig. 3).** For one microtubule there are three
  regimes: a small (<10%) rise as one dimer forms, a plateau (to 0.1%)
  through the first spiral, then a sigmoid rise to saturation at a few
  wavelengths (about 800 nm, 10 400 tryptophans). For the centriole and the
  91-microtubule bundle the yield is still rising at 10⁵ tryptophans, but in
  the bundle a tenfold increase from 10⁴ to 10⁵ adds only about 1%.
- **Disorder (Fig. 4).** QY is "almost unaffected" at W = 200 cm⁻¹, and
  some enhancement remains at W = 1000 cm⁻¹.
- **Measurement (Table 1; SI Table S2).** Tryptophan-weighted QY at 280 nm:
  tryptophan 12.4 ± 1.1%, tubulin dimer 10.6 ± 0.6%, microtubules 17.6 ±
  2.1%. The last is the mean of 19.5 ± 2.8% (scattering-corrected) and 15.7 ±
  1.3% (uncorrected). At 295 nm, where only tryptophan absorbs: 11.4 ± 1.1,
  10.9 ± 1.3 and 14.7 ± 1.6%. Five freshly prepared solutions per sample
  were averaged. The microtubule emission is slightly sharper and its
  absorption peak slightly lower than the dimer's, in the direction the
  model predicts.
- **Lifetimes (Table S3, arXiv v1).** Superradiant lifetimes 0.43–0.94 ps
  for bundles, centrioles and the idealised axoneme, 2.6–3.9 ps for the
  6U42 axoneme and a single microtubule. Subradiant lifetimes up to about
  14 s.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Ordered tryptophan networks in microtubule architectures have superradiant eigenmodes with enhancements of 10³–10⁴ γ in the absence of disorder | strong as a model result; it is diagonalisation of a standard quantum-optics Hamiltonian on PDB geometry | Figs. 5–6, SI Eqs. 5–8 |
| C2 | The thermal quantum yield rises with network size and is robust to static disorder of room-temperature size | moderate: model result under static disorder only, with a fixed per-site non-radiative rate | Figs. 3–4 |
| C3 | The measured rise in QY from tubulin dimers to microtubules is caused by superradiance | weak to moderate: the rise is statistically significant and in the predicted direction, but no lifetimes were measured, sample concentrations could not be fixed exactly, the microtubule value rests on a scattering correction, and the case against a change in non-radiative rate is an argument ("an unlikely scenario"), not a measurement | Table 1, pp. "Results" |
| C4 | Superradiance enhancement saturates once a structure is a few excitation wavelengths long | moderate: consistent across all structures simulated | Figs. 3, 5, 6; SI |
| C5 | Axons might act as waveguides between superradiant emitters, enabling ultrafast information transfer in the brain | speculation; no result in the paper supports it | Discussion, Conclusions |
| C6 | Enhanced QY in protein aggregates might be photoprotective in Alzheimer's disease | speculation | Conclusions |

## Concepts

- **superradiance (single-excitation)**: a collective eigenmode of N coupled
  emitters whose decay rate exceeds the single emitter's γ, up to about Nγ,
  because one excitation is coherently shared.
- **subradiance**: the paired long-lived, dark modes, with decay rates far
  below γ.
- **superradiance enhancement factor**: max(Γ_j)/γ, the structure's
  brightest state.
- **cooperative robustness**: the disorder needed to suppress superradiance
  grows with system size, because the large decay width couples the system
  strongly to the field.
- **thermal quantum yield**: QY from the Boltzmann-averaged radiative rate
  ⟨Γ⟩_th against a fixed non-radiative rate.

## Connections

- **Derakhshani et al. ([LIT-627](../literature.d/LIT-627.md)).** The other Orch OR evidence filed with
  this work, and its complement rather than its rival. That paper tests the
  gravity-related collapse that Orch OR's "OR" names, using spontaneous
  radiation bounds. This paper says nothing about collapse. It bears only on
  whether ordered microtubule lattices support collective quantum states at
  room temperature. Neither cites the other.
- **Chalmers ([LIT-406](../literature.d/LIT-406.md), [NOTE-336](NOTE-336.md)).** Chalmers argues that quantum theories of
  consciousness explain at best more functions. Whatever this paper's
  superradiant states do in cells, they are a function in that sense.
- **Gao ([LIT-121](../literature.d/LIT-121.md), [NOTE-140](NOTE-140.md))** criticises Penrose's gravity-collapse argument.
  That is unrelated to this paper's physics, which uses no collapse.

## Bearing on the record

- A THEORY on Orch OR would cite this paper only for the narrow claim it
  supports: collective electronic excitations in microtubule-scale tryptophan
  lattices are predicted to survive room-temperature static disorder, and the
  QY difference between dimers and microtubules is consistent with that. It
  cannot source any claim about neurons in vivo, cognition, consciousness or
  collapse.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- No time-resolved measurements, so neither the radiative rate nor
  superradiance itself was observed directly. The authors say the
  non-exponential decays would not give a reliable radiative rate even if
  measured.
- Only dimers and microtubules were measured. Centrioles, bundles and
  axonemes are simulation only; the larger assemblies had scattering and
  purity problems.
- In vitro, taxol-stabilised, lyophilised commercial microtubules, at
  concentrations the authors could not fix exactly because the vials contain
  sucrose and Ficoll.
- Dynamic disorder and exciton–phonon coupling are absent from the model.
- A size-independent non-radiative rate is assumed.

## Open questions

- Do fluorescence lifetime measurements across dimers, microtubules and
  larger assemblies show the shortening the model predicts?
- Does the QY enhancement survive a model with dynamic disorder and vibronic
  coupling?
- Is there any physiological source of UV excitation, or consumer of it, at
  which a superradiant state would matter? The paper points to ultraweak
  photon emission but measures nothing in cells.
