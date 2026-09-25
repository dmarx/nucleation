---
status: Skimmed
paper: LIT-tmpbydeh
title: 'Backens & Duman, graphical calculus for Spekkens'' toy bit'
version: 1
date: '2026-09-25'
summary: >-
  Spekkens' toy bit theory (maximal-knowledge fragment, post-selected measurements) has a graphical calculus modelled on the ZX-calculus that is universal, sound and complete. The toy theory and qubit stabilizer quantum mechanics can therefore be compared entirely in diagrams, and at the categorical level they differ only in the phase group (Z2×Z2 vs Z4).
---

<!-- inactive-ok-file: LIT-tmpbydeh — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpmqjev: Backens & Duman, graphical calculus for Spekkens' toy bit

## Contribution

Quantum theory has no local hidden-variable model, but some such models still reproduce many "quantum" features and are used to probe the ψ-ontic vs ψ-epistemic question. Spekkens' toy theory is one of them: classical probabilistic mechanics plus a limit on what an observer can know. For a single bit it closely resembles stabilizer quantum mechanics. The authors build a graphical language for the toy bit theory, inspired by the ZX-calculus, and prove it complete: any equation derivable in another formalism can be derived graphically. The two theories can then be analysed side by side in analogous diagrammatic formalisms.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1–2: Spekkens' theory is a local hidden-variable theory and ψ-epistemic by construction, yet it reproduces incompatibility, teleportation and no-cloning. It does not violate Bell inequalities, which stabilizer QM does. A toy bit has four ontic states (a 2×2 grid over X, Z), and the observer holds an epistemic state (§2.1).
- §3: how graphical languages are made rigorous, as formal systems over symmetric monoidal categories (§3.1–3.2).
- §4: components and rewrite rules (green/red phased spiders, a colour-change rule, an Euler decomposition), with proofs of universality (§4.3) and soundness (§4.4). §4.5: the only categorical difference from the stabilizer ZX-calculus is the phase group, Klein four Z2×Z2 against Z4. That difference shows up as an "11-commutation" rule where ZX has π-commutation.
- §5: completeness is proved via binary stabilizer and graph-state theorems, map-state duality, and reduction to rGS-LO diagram equalities.
- §6: next steps are automation in Quantomatic, mixed states and less-than-maximal knowledge via the CPM construction, and higher dimensions.

## Open questions

- It is a concrete instance of the "same structure, different phase group" diagnosis of what separates quantum from classical-with-epistemic-restriction. It sits beside the held *Quasi-quantization* note.
- A deeper read should check exactly which quantum/classical differences (e.g. Bell violation) the phase-group difference captures diagrammatically, and whether later work (a mixed-state or qudit extension) completed the §6 programme.
