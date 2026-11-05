---
status: Read
paper: 'LIT-tmpldjyt'
title: 'Kane and Lubensky — Topological boundary modes in isostatic lattices'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in full on 2026-11-05 from the arXiv v2 PDF (12 November 2013),
    https://arxiv.org/pdf/1308.0554, extracted with pdftotext; no paywall.
    Read: the whole main text (introduction, mechanical modes and band
    theory, the 1D model, the index theorem, the deformed kagome model,
    continuum elasticity, conclusions) and the supplementary proof of the
    index theorem. Nothing skipped. The arXiv text may differ in detail
    from the Nature Physics version. Quotes checked by string match
    against the extracted text.
date: '2026-11-05'
summary: >-
  In isostatic lattices the zero-mode count of a region is a local count
  of sites and bonds plus a topological count fixed by winding numbers of
  the bulk equilibrium matrix. Gapped phases of different topological
  polarization therefore carry floppy modes, or states of self-stress, at
  their edges and domain walls where constraints and freedoms locally
  balance. Shown in a 1D rotor chain (the SSH model) and a deformed kagome
  lattice; linear theory, needing a bulk gap and a gauge choice of unit
  cell.
---
<!-- inactive-ok-file: THEORY-tmpmju6r — Proposed and new; the account filed from this reading -->

# NOTE-tmpp5rni: Kane and Lubensky — Topological boundary modes in isostatic lattices

## Contribution

It connects isostatic mechanics to topological band theory and turns the
Maxwell–Calladine relation into a local index theorem with a topological
term. It predicts topologically distinct bulk mechanical phases with
protected boundary floppy modes and states of self-stress. The boundary
modes of twisted kagome had been found by Sun et al. (2012); this paper
gives their topological account.

## Key insight

Zero modes have two sources: a local surplus of freedoms over constraints,
and a topological polarization of the bulk that pushes freedom to one side
of an interface and stress to the other. The second operates even where
the local count balances.

## Assumptions

- **Lattice**: periodic and locally isostatic, coordination z = 2d, unit
  masses and spring constants.
- **Linear, harmonic** theory of infinitesimal distortions.
- **A bulk gap**, so that the winding number is path independent; acoustic
  modes at k = 0 are a non-topological exception.
- **The boundary of S** lies deep in a gapped phase.
- **A gauge choice**: "A second caveat for equation (7) is that, in
  general, the winding number is not gauge invariant and depends on how the
  sites and bonds are assigned to unit cells." The fix is a standard unit
  cell, possible for an isostatic lattice with z = 2d.

## Key results

- **Isostatic** (abstract): "When these are balanced, the system is on the
  verge of mechanical instability and is termed isostatic."
- **What was known** (abstract): "It has recently been shown that certain
  extended isostatic lattices exhibit floppy modes localized at their
  boundary." "These boundary modes are insensitive to local perturbations,
  and appear to have a topological origin".
- **Maxwell's count** (Introduction): "Maxwell’s count is incomplete,
  though, because N0 can exceed dNs − Nb if there are Nss states of
  self-stress"; the corrected ν = N0 − Nss = dNs − Nb "is valid for
  infinitesimal distortions."
- **The 1D model**: a rotor-spring chain mapping onto the
  Su–Schrieffer–Heeger model. Its two phases are distinct in that "it is
  impossible to tune between the two phases without passing through a
  transition where the gap vanishes." One interface (Fig. 1h) has "a state
  of self-stress localized to the middle three bonds, in addition to floppy
  modes localized at either end."
- **The index theorem**: "There appear to be two distinct origins for zero
  modes." In the classical count they come from a mismatch of sites and
  bonds, "while at a domain wall they arise in a location where there is no
  local mismatch." ν^S = ν_L^S + ν_T^S, "where νLS is a local count of
  sites and bonds in S and νTS is a topological count, which depends on the
  topological structure of the gapped phases on the boundary of S."
  Proved in the supplement.
- **Deformed kagome**: distinct topological phases whose edge and
  domain-wall mode counts agree with the theorem.
- **Continuum elasticity**: distinguishes the phases by the sign of a
  coefficient, but "Elastic energies are restricted to small wavenumber and
  cannot by themselves determine topological characteristics".
- **Prediction** (abstract): "we predict the existence of new topological
  bulk mechanical phases with distinct boundary modes".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The zero-mode count of a region is a local count plus a topological count | strong: proof | index theorem; supplement |
| C2 | Gapped isostatic phases are classed by winding numbers of det Q(k) | strong: derivation, given a gap and a gauge | band-theory section |
| C3 | Domain walls bind floppy modes or states of self-stress, by orientation | strong in the models: computed | 1D model, deformed kagome |
| C4 | Continuum elasticity cannot detect the topology | moderate: argued from the models | continuum section |

## Concepts

- **Equilibrium matrix Q**: forces F = Q·T from bond tensions, bond
  extensions e = Qᵀu. N0 = dim ker Qᵀ zero modes, Nss = dim ker Q states of
  self-stress.
- **Isostatic**: constraints balance degrees of freedom; locally isostatic
  if z = 2d at every site under periodic boundary conditions.
- **Topological polarization** R_T = Σ n_i a_i, the n_i winding numbers of
  the phase of det Q(k) around the Brillouin zone's cycles.
- **Local count** ν_L^S = Tr ρ^S τ^z.
- **Domain wall**: an interface between phases of different R_T, binding
  floppy modes or states of self-stress according to its orientation.

## Connections

It supplies the topological account of the boundary modes Sun et al.
(2012) found in twisted kagome. Its relation ν = dim ker Qᵀ − dim ker Q
is the classical Maxwell–Calladine identity in the equilibrium-matrix
convention, the transpose of Rocks and Mehta's (LIT-tmpx12go). Chen et al.
(LIT-tmpchla8, read in NOTE-tmpztu5h) carry the topological polarization
to origami and kirigami.

## Bearing on the record

- **The pasted synthesis on constraint architectures** (A, cited as M6).
  A writes that "certain mechanically marginal lattices possess
  zero-energy modes localized at their boundaries ... predicted using
  topological properties of the bulk structure". Right about marginality
  and bulk prediction. Shaded or missing:
  - the count has a local term as well as a topological one, so not every
    boundary mode is topological;
  - domain walls of the opposite orientation bind states of self-stress,
    not freedom, and in a periodic system the two walls' indices cancel;
  - the phenomenon was already known (Sun et al. 2012); the contribution
    is the topological theory and the prediction of new phases;
  - the theory is linear and needs a bulk gap and a gauge choice.
  On A's Maxwell–Calladine statement: ν = dim ker Qᵀ − dim ker Q = dNs −
  Nb is A's identity with Q = Rᵀ, and the paper's "valid for
  infinitesimal distortions" supports A's caveat.
- **CLAIM-480** (composing interactions can turn an interior into an
  effective constraint). Qualifies: here composing two gapped, locally
  balanced phases creates at their interface a freedom, or a stress, that
  neither bulk has. Interconnection can create effective freedoms as well
  as effective constraints.
- **CLAIM-495 and THEORY-1082** (global sections of a graph connection as
  vectors fixed by every holonomy; phase relations solvable iff each
  cycle's phase vanishes). Qualifies, loosely, as an analogy only. Both
  count kernel dimensions of a structured linear map from topological
  data, cycle holonomy there and Brillouin-zone winding here; but the
  record's results concern global sections on a finite graph, and this is
  an index, kernel minus cokernel, with a bulk–boundary correspondence. A
  did not cite these codes for this work.
- **CLAIM-347 and TERM-060** (frustration). Unrelated in content: the
  self-stresses here are linear-algebraic, not conflicts of demands.
- Filed: THEORY-tmpmju6r. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **Linear and harmonic**: silent on whether the zero modes extend to
  finite mechanisms.
- **A gap and the right unit-cell gauge** are required.
- **Only 1D and 2D models**; 3D and point-singular (Weyl- or Dirac-like)
  cases are left open, as the authors say.
- **Continuum elasticity** cannot detect the topology.

## Open questions

- Do the boundary counts hold in three dimensions, or in gapless lattices?
- Do the protected linear modes survive as finite motions?
