---
status: Read
paper: LIT-tmp25uib
title: 'Nachtergaele, read for a general proof of the Mermin–Wagner theorem that needs no translation invariance, as a stand-in for Mermin and Wagner'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 by a delegated reader from the author's
    faculty page (www.math.ucdavis.edu/~bxn/mermin-wagner.pdf, 6 pp.,
    course notes for MAT266, UC Davis, Winter 2006), as a stand-in for
    Mermin and Wagner (1966), LIT-2985 (ADR-114). Every quotation below
    rechecked by the filer by script against the downloaded text.
date: '2026-11-22'
summary: >-
  Course notes proving, by energy-entropy balance on KMS states, that a
  continuous symmetry is not spontaneously broken at finite temperature
  in d ≤ 2 for quantum spin systems with couplings of finite second
  moment, without translation invariance. A rotation is interpolated to
  zero at infinity at bounded energy cost, which two dimensions just
  permit. It does not present Mermin and Wagner's own argument. The
  reading is [THEORY-tmp85ij4](../theory.d/THEORY-tmp85ij4.md).
---
<!-- inactive-ok-file: THEORY-tmp85ij4 — Proposed; this reading's account -->
<!-- inactive-ok-file: LIT-2985 — Unavailable; the original this reading stands in for -->
<!-- inactive-ok-file: CLAIM-842 — Proposed; the claim the reading bears on -->

# NOTE-tmpl5lm3: Nachtergaele, read for a general proof of the Mermin–Wagner theorem that needs no translation invariance, as a stand-in for Mermin and Wagner

## Contribution

An operator-algebraic proof, more general than Mermin and Wagner's, of
the absence of continuous symmetry breaking at finite temperature in
d ≤ 2. The reading is [THEORY-tmp85ij4](../theory.d/THEORY-tmp85ij4.md).

## Key results

1. **The statement** (p. 1): "The original theorem, a special case of
   what we will prove here, says that no spontaneaous breaking of any
   continuous symmetry occurs at finite temperatures (β < ∞) in
   dimensions d ≤ 2" (the typo is the notes').
2. **The condition** (Proposition 2.2, p. 5): sup_x Σ_y |x − y|²|J(x, y)|
   < +∞; "Translation invariance is not required; in fact the argument
   works for inhomogeneous systems with spins of different magnitudes at
   different sites."
3. **The mechanism** (p. 6): a rotation can be interpolated to zero at
   infinity "in such a way that there is a uniform bound on the energy
   involved", using |φ_m(x) − φ_m(y)| ≤ |φ|/m against |Λ_m| ∼ m² in
   d = 2.

## Assumptions

Quantum spin systems on Z^d with a continuous symmetry, couplings of
finite second moment, KMS (equilibrium) states, β < ∞.

## Concepts

KMS state; energy-entropy balance; interpolated rotation.

## Bearing on the record

- **[LIT-2985](../literature.d/LIT-2985.md)**: stands in for the statement only ([ADR-114](../decisions.d/ADR-114.md)). Item 1
  glosses the original more broadly than its model (Halperin, [NOTE-tmpuwmny](NOTE-tmpuwmny.md)).
- **[CLAIM-842](../claims.d/CLAIM-842.md)**: **supports its reach to irregular graphs, within
  equilibrium.** Item 2 means the theorem does not need a regular
  lattice, so an inhomogeneous interaction graph is within its scope as
  long as the couplings' second moment is finite; it is still a theorem
  about a continuous symmetry of a Hamiltonian in an equilibrium state.

## Limitations

Course notes, unrefereed; the proof is on Z^d, so a graph without an
embedding is reached only through the second-moment condition's
generalization, which the notes do not state.
