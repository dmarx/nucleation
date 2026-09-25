---
status: Skimmed
paper: LIT-tmpj6y5q
title: 'Distinguishability and Accessible Information in Quantum Theory'
version: 1
date: '2026-09-25'
summary: >-
  The thesis translates classical distinguishability measures into quantum ones: it derives the mixed-state fidelity as the statistical overlap minimized over all measurements, gives new upper and lower bounds on accessible information (including a simple derivation of the Holevo bound), and proves that noncommuting mixed states cannot be broadcast.
---

<!-- inactive-ok-file: LIT-tmpj6y5q — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpnch50: Distinguishability and Accessible Information in Quantum Theory

## Contribution

The dissertation turns information-theoretic distinguishability measures for probability distributions (error probability, Kullback-Leibler relative information, mutual information) into measures for quantum states, aiming at applications in quantum cryptography and computation. It derives an exact expression for the fidelity between mixed states and studies the measurement that attains it. It derives and compares several bounds on quantum mutual information, including a short derivation of Holevo's upper bound and a tighter bound implicit in it, plus bounds on quantum relative information. It then applies these to the inference-disturbance tradeoff and proves a no-broadcasting theorem generalizing no-cloning to mixed states.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Ch. 2 grounds the classical measures operationally: error probability and the Chernoff bound, Kullback-Leibler as "keeping the expert honest", Shannon mutual information (Contents, Ch. 2).
- Accessible information set up as a binary channel with nonorthogonal/mixed letter states ρ0, ρ1; J = H(p) - π0H(p0) - π1H(p1), with the maximum over all POVMs the target (§1.2).
- Fidelity F(ρ0,ρ1) is derived by a Schwarz-inequality argument whose equality conditions a suitable measurement can meet; it reduces to Wootters' |⟨ψ0|ψ1⟩| for pure states (§3.3.1, Eq. 3.36). Note that F here is the unsquared trace-root form.
- Bounds S(t) (Holevo), L(t), M(t) and the Jozsa-Robb-Wootters Q(t) are compared numerically on qubit examples (§3.5, Figs. 3.2-3.7).
- No-broadcasting (§4.3) is flagged as a collaboration with H. Barnum, C. M. Caves, R. Jozsa and B. Schumacher; it holds that commuting states can be broadcast and noncommuting ones cannot.
- Ch. 5 is an extensive annotated bibliography (528 references).

## Open questions

- Foundational source for the Fuchs-van de Graaf-era toolkit (fidelity, trace-distance relations) and for no-broadcasting. The deeper read should check which results are primary here versus in the companion papers (e.g. Barnum et al. 1996 PRL; Fuchs & van de Graaf 1999 IEEE-IT).
- ML link (real but generic): classical-to-quantum lifts of KL, Bhattacharyya/fidelity and mutual information parallel the divergence choices ML makes. Ch. 2's operational derivations of KL and mutual information are the most ML-reusable part.
