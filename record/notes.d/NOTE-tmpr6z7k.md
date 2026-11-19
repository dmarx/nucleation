---
status: Skimmed
paper: LIT-tmp4lexz
title: 'Teo and Kane 2010 — Topological Defects and Gapless Modes in Insulators and Superconductors'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1006.0690 (served v2, 22 Sep 2010), HTTP
    200, PDF. Kind of copy: arXiv preprint, the authors' manuscript (step 5,
    arXiv). Fetched 2026-11-19; nothing stopped the fetch. Text extracted
    with pdftotext to dl/text.txt. Read: abstract; §I; §II introduction and
    Table I; §II A (symmetry classes); §III A.1–3 (θ-winding invariant,
    dislocation in a 3D integer quantum Hall state, topological insulator
    heterostructures and domain walls); opening of §III B (dislocation in a
    weak topological insulator); §IV A (chiral zero modes, index n = N+ −
    N−, Jackiw–Rebbi, Jackiw–Rossi); §VI conclusion. Skipped: §II B–C
    (classifying spaces, Bott periodicity), §III C–E, §IV B (Majorana bound
    states), most of §V (Thouless and fermion-parity pumps), Appendices A–D.
    Verdict on the source's characterization ("a unified classification of
    topological defects and the gapless modes they bind in insulators and
    superconductors"): accurate. One caution: the "topology" here is of the
    Hamiltonian around the defect, not the defect's order-parameter charge.
date: '2026-11-19'
---

# NOTE-tmpr6z7k: Teo and Kane 2010 — Topological Defects and Gapless Modes in Insulators and Superconductors

## Contribution

A classification of defects in non-interacting insulators and superconductors by the topology of the Hamiltonian around the defect, not by the defect's own order-parameter charge. Far from the defect the Bloch or Bogoliubov–de Gennes Hamiltonian H(k, r) varies slowly with position r on a surface S^D enclosing it. Defects are classified by the homotopy class of this family (gapped, under the ten Altland–Zirnbauer symmetry classes), giving a "periodic table" for defects that depends only on δ = d − D. The authors then propose a generalized bulk-boundary correspondence: a nontrivial class goes with protected gapless modes bound to the defect. They observe this correspondence in examples. They do not prove it.

## Key results

- **The object classified** (abstract): "We introduce a generalization of the bulk-boundary correspondence that relates the topological classes to defect Hamiltonians to the presence of protected gapless modes at the defect."
- **Equivalence by gap, not by field configuration** (§II): the table "describes the equivalence classes of Hamiltonians H(k, r), that can be continuously deformed into one another without closing the energy gap".
- **Dependence on δ only** (§I, eq. 1.1): "Thus, all line defects with δ = 2 have the same topological classification, irrespective of d, as do point defects with δ = 1 and pumping cycles with δ = 0."
- **Observed, not proved** (§I): "In this paper we will not attempt to prove the index theorem. Rather, we will observe that the topological classes for H(k, r) coincide with the expected classes of gapless defect modes."
- **An interface as the D = 0 case** (§I): "A non trivial difference corresponds to an interface between two topologically distinct phases."
- **Dislocation in a 3D quantum Hall state** (§III A): "the topological invariant associated with a line defect, which determines the number of chiral fermion branches is given by the winding number of θ."
- **The mode outlives the structure that produced it** (§III B, weak topological insulator): "the Hamiltonian has a non trivial winding around the line defect, even though the defect has no obvious structural origin." And: "But once present, the line defect is more robust than the weak topological insulator."
- **Same pattern at a domain wall** (§III A.3): "Thus, the chiral mode, protected by the strong invariant (3.1), is more robust than the bulk state that gave rise to it."
- **Interface modes depend on the path across the wall, not only on the two sides** (§III A.3). If the coupling between two magnetic topological insulators is weakened, "at some point the chiral mode has to disappear", and at the switch between short and long paths of θ "the gap on the domain wall must go to zero, allowing the chiral mode to escape."
- **Point defects, net count** (§IV A): "The topological invariant is related to an index that characterizes the chirality of the zero modes", n = N+ − N−, a net count of zero modes by chirality.
- **Where the defect charge and the mode invariant coincide** (§IV A.2, Jackiw–Rebbi): "Domain walls where m(x) changes sign as a function of x are associated with the well known zero energy soliton states", and "the invariant (4.2) changes by 1 when m changes sign." For the Jackiw–Rossi vortex the invariant "can be expressed as the winding number of the phase of" the order parameter (§IV A.3).
- **Scope** (§VI): "topologically protected modes can occur in a context somewhat more general than simply boundary modes". The conclusion asks for a formulation that "goes beyond the adiabatic approximation we used in this paper", and for one that can be applied to interacting or disordered problems.

## Assumptions

- Non-interacting (single-particle) Bloch or BdG Hamiltonians with a bulk energy gap. Interactions and disorder are outside the formalism, and the conclusion names them as open.
- Adiabatic, slow variation of H(k, r) far from the defect. Some heterostructure cases (§III A.3) fall outside this regime and are handled by a continuity assumption ("it is natural to expect that the physics would not change if the interface was" smoothed out).
- Stable equivalence and the ten symmetry classes. Crystalline symmetries are not included.
- The defect is a fixed background. Its texture is given, not dynamical.

## Concepts

- **Defect Hamiltonian H(k, r)**: the electronic or excitation Hamiltonian as a function of crystal momentum and of position on a surface enclosing the defect. Its homotopy class is the defect's "topological class" here.
- **δ = d − D**: the classification depends only on this. A line defect in 3D, a point defect in 2D and an end of a 1D system can share a class.
- **Generalized bulk-boundary correspondence / index theorem**: the topological index of the defect Hamiltonian equals an analytic index counting protected modes (net chirality for zero modes).
- **Two topologies**: the defect's structural or order-parameter charge (Burgers vector, sign change of a mass, phase winding) and the winding of the Hamiltonian around it. In the Jackiw–Rebbi, Jackiw–Rossi and dislocation examples the first determines the second. In the disordered weak topological insulator the second survives when the first is no longer defined.

## Bearing on the record

- CLAIM-606: qualifies. The claim's topological route is persistence by an order-parameter charge (THEORY-1507). Teo and Kane's "topological defect" is classified by a different object, the winding of the Hamiltonian that excitations see around the defect. What it protects is the bound modes, and only while the bulk gap stays open. It does not protect the defect's persistence. A protected bound mode is therefore not evidence that its host is on the topological route. The record should keep defect topology and bound-mode (spectral) topology apart.
- CLAIM-694: qualifies, by a parallel on the spectral side. For point defects the invariant fixes n = N+ − N−, a net count of zero modes by chirality, not which modes there are. Pairs of opposite chirality can be added or removed freely. This is the same net-count-not-token structure as CLAIM-694, applied to hosted modes. It is a parallel and not evidence for the claim's field-theoretic statement.
- THEORY-1507: leaves open; complements. The paper does not treat the energy bound or the vacuum manifold. It shows where the two topologies are linked: in Jackiw–Rebbi the kink's sign change of m is what changes the mode invariant by one, so a THEORY-1507 kink fixes the bound-mode count when the mass term is the order parameter.
- QUESTION-tmp57ji2: leaves open. The bound modes are single-particle states on a fixed texture, so no back-action on the defect is modelled. The question's feedback is outside this framework, which treats the defect as a background. The one dynamical point is that the mode can be "more robust than" the structure that produced it. That is one-way robustness, not mutual maintenance.
- QUESTION-378: qualifies the "distinct phases" condition. An interface between topologically distinct phases is the D = 0 case and carries protected modes. But where the invariant (θ) is not quantized on either side, whether the interface carries a mode depends on the path the interpolation takes across the wall and on the coupling between the sides, not only on which phases meet.

## Limitations

- Skimmed, not read in full. Read: abstract, §I, §II introduction and Table I, §III A (θ-winding, dislocation in a 3D quantum Hall state, topological insulator heterostructures), the opening of §III B on the dislocation in a weak topological insulator, §IV A (chiral zero modes, Jackiw–Rebbi, Jackiw–Rossi), and §VI. Skipped: §II B–C (classifying spaces, Bott periodicity), §III C–E, §IV B (Majorana bound states without chiral symmetry), most of §V (pumping cycles) and Appendices A–D.
- The correspondence between invariant and modes is observed in examples, not proved.
- Non-interacting and adiabatic. Its bearing on interacting or nonequilibrium defects, including the record's active and driven cases, is not established.
