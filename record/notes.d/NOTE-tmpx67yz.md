---
status: Skimmed
paper: LIT-tmpubwzo
title: 'Barandes, The Stochastic-Quantum Correspondence'
version: 1
date: '2026-09-25'
summary: >-
  Every quantum system can be represented as an "indivisible" (non-Markovian) stochastic process on an ordinary configuration space, and the reverse also holds. On that reading the wave function is a derived mathematical tool, like a Lagrangian, and not part of the ontology.
---

<!-- inactive-ok-file: LIT-tmpubwzo — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpx67yz: Barandes, The Stochastic-Quantum Correspondence

## Contribution

The paper claims an exact correspondence between quantum theory and a class of stochastic processes it calls indivisible. These processes unfold in a classical configuration space under ordinary probability, but their transition maps cannot in general be factored through intermediate times. On this view the wave function is a secondary representational device, not a primary ontological ingredient. Interference, decoherence, entanglement, noncommuting observables and collapse then receive deflationary explanations. Practically, the correspondence gives a new reconstruction of quantum theory alongside the Hilbert-space, path-integral and quasiprobability ones. It also lets Hilbert-space methods be used for generic non-Markovian stochastic dynamics in other sciences.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.1–2.2: an indivisible process is a configuration space plus transition matrices Γ(t←t0) that are specified only from a few conditioning times. It avoids both the Markov approximation and the infinite tower of higher-order conditionals that fully specifying a non-Markovian process would require.
- §3.1, "the dictionary": write Γ_ij = |Θ_ij|² entry by entry. This is an identity, not a postulate, with Θ non-unique and likened to a potential. Using configuration projectors, Γ_ij = tr(Θ† P_i Θ P_j), which yields the Hilbert-space representation (§3.2). Kraus decompositions and unistochastic processes are covered in §3.3–3.4.
- §3.7: "division events" explain why Markov chains approximate real processes so well. A system coupled to an eavesdropping environment has its correlations reset at many conditioning times.
- §4 treats measurement as an ordinary stochastic process involving the apparatus: emergeables, collapse as conditioning, the measurement problem and uncertainty.
- §5: an "indivisible interpretation" in which systems always have definite configurations and superposition is an artefact of catching a process between division events. It proposes canonical quantization as the move from deterministic to stochastic dynamics (§5.1), and leaves locality and causation to future work (§5.4).

## Open questions

- It offers a bridge from non-Markovian stochastic modelling to Hilbert-space and linear-algebra methods. §5.4 explicitly suggests applying it to phenomenological processes in biology and finance, which touches sequence and time-series modelling.
- Check what the reconstruction adds beyond a re-encoding. How much freedom does the non-uniqueness of Θ leave, and does anything select unitary Θ other than a stipulation?
- Locality and causation are deferred (§5.4). Any claim about Bell nonlocality should be checked against the follow-up papers, including arXiv:2507.21192.
