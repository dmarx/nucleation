---
status: Read
paper: 'LIT-tmp3py9h'
title: 'Holm and Stechmann — Hasimoto transformation and vortex soliton motion driven by fluid helicity'
version: 1
history:
- version: 1
  date: '2026-11-18'
  note: >-
    Read in full on 2026-11-15 by the reader of Hasimoto (1972) for
    nucleation #508, from arXiv nlin/0409040v1 (15 pp., the only
    version), from arxiv.org, text by pdftotext; no report was written
    then. Read again in full on 2026-11-18 by a second reader from the
    same copy (abstract, §§1–6, footnotes and references). pdftotext
    garbles several integrals (eqs. 1.1, 4.10, 5.5) and splits the ½ of
    4.9 and 4.13; eqs. 4.4–4.15 are legible. The filer rechecked every
    quotation below against the text.
date: '2026-11-18'
summary: >-
  Under the Rasetti–Regge Dirac bracket, the local induction approximation
  of fluid helicity, taken as a vortex filament's Hamiltonian, gives a
  curve motion that the Hasimoto transformation maps to the complex
  modified KdV equation, the NLS hierarchy's second flow. Formal; no
  soliton constructed. Read as a second neighbour of Hasimoto (1972).
---
<!-- inactive-ok-file: LIT-2611 THEORY-1868 NOTE-1951 CLAIM-606 — Unavailable, Skimmed, Proposed or new; the work this stands in for, the stand-in's reading and account, and the entries this bears on -->

# NOTE-tmpja35d: Holm and Stechmann — Hasimoto transformation and vortex soliton motion driven by fluid helicity

## Contribution

Vortex filaments, vorticity concentrated on a curve (eq. 2.1), are given
Hamiltonian dynamics under the Rasetti–Regge Dirac bracket, which §3
(Lemma 3.1) shows equal to the Marsden–Weinstein bracket up to a
time-dependent reparameterization along the filament. With kinetic energy
as the Hamiltonian the known result is the cubic NLS (abstract: "when the
Hamiltonian is the Local Induction Approximation (LIA) of the kinetic
energy"). The paper takes helicity instead and obtains the next flow of
the hierarchy: "This connection between cmKdV and fluid helicity is the
main result of the paper."

## Key results

- **Hasimoto's map, attributed** (§1): "Hasimoto [1972] discovered the
  fascinating map from vortex filament solutions of Euler's equations for
  ideal incompressible fluids in the Local Induction Approximation (LIA)
  to soliton solutions of the NonLinear Schrödinger (NLS) equation." An
  attribution only: the paper never writes the NLS or shows its soliton.
- **The cutoff** (§4.1, eq. 4.4): the Biot–Savart integral is replaced by
  log(ε⁻¹)κb, "where ǫ is the radius of the thin vortex tube which our
  filament approximates", citing Arms and Hama (1965). After eq. 4.7 the
  authors "assumed log ǫ−1 is approximately constant" and absorb it into
  time.
- **The binormal law** (eq. 4.15), Ṙ = κb, "the standard da Rios-Betchov
  LIA equation", given as a contrast case, not derived.
- **The main theorem** (Theorem 4.1): ψ_t = ψ_sss + (3/2)|ψ|²ψ_s, and
  "Thus, soliton solutions of (4.12) yield LIA ω-filament solutions driven
  by helicity, and vice versa." The map from eq. 4.9 is credited: "This
  equation was shown in Langer & Perline [1991] to map into the complex
  mKdV equation (4.11) under the Hasimoto transformation."
- **Not a material line** (§2): a filament moved by a Hamiltonian other
  than kinetic energy does not follow the fluid, "so in general ω will not
  be frozen into the fluid motion".
- **The hierarchy stalls** (§5): "iterating this correspondence produces
  a sequence of Hamiltonians which apparently have no fluid dynamical
  significance."
- **No solitons shown** (§6): the map from cmKdV solitons to filament
  motions is left open, "We shall, however, leave these issues for other
  publications and other researchers."

## Assumptions

Singular vorticity on a curve; gauge-invariant Hamiltonians only; the
local induction approximation for a thin tube of radius ε, with log ε⁻¹
constant; homogeneous boundary conditions; formal analysis, "Analytical
issues ... will be neglected in this paper."

## Concepts

Rasetti–Regge Dirac bracket; Marsden–Weinstein bracket; reparameterization
as gauge; vortex impulse as a Casimir; helicity; local induction
approximation; da Rios–Betchov binormal law; Hasimoto transformation as a
momentum map (Langer and Perline); NLS hierarchy; complex modified KdV.

## Bearing on the record

- **[LIT-2611](../literature.d/LIT-2611.md) (Hasimoto 1972).** A second neighbour. It confirms that
  Hasimoto's map runs from the local induction approximation to the NLS,
  and the transformation ψ = κ exp(i∫τ ds), and adds the thin-tube cutoff.
  It carries none of the travelling hump, its speed 2τ, its shape or the
  treatment of Betchov, so [LIT-2611](../literature.d/LIT-2611.md)'s list of what nothing read carries is
  unchanged.
- **[LIT-2612](../literature.d/LIT-2612.md), [NOTE-1951](NOTE-1951.md) (Van Gorder).** An independent secondary source
  agreeing on the attribution and the variable; [NOTE-1951](NOTE-1951.md)'s assumptions
  name the local induction approximation without its cutoff.
- **[THEORY-1868](../theory.d/THEORY-1868.md).** Supports, as an attribution only, its first clause,
  that under the local induction approximation the curvature–torsion field
  obeys the cubic NLS; nothing on the sech soliton, friction or decay.
- **[QUESTION-469](../questions.d/QUESTION-469.md).** The filament is assumed, not derived (eq. 2.1), and
  under a Hamiltonian other than kinetic energy it is not even a material
  line: how the carrier moves is set by the Hamiltonian chosen for it, not
  by the flow. Noted there.
- **[CLAIM-606](../claims.d/CLAIM-606.md).** None directly: Theorem 4.1's solitons are asserted
  through integrability, and none is shown.

## Limitations

Formal by the authors' own statement; the title's "vortex soliton motion"
is not constructed; the key step to cmKdV is Langer and Perline's; a
preprint with no journal version found.
