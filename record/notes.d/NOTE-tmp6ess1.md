---
status: Skimmed
paper: LIT-tmp0w06o
title: 'QM as stochastic optimization on spacetimes'
version: 1
date: '2026-09-25'
summary: >-
  The authors claim that the Schrödinger equation (and relativistic wave equations) can be derived rather than postulated, as a log-transformed Hamilton-Jacobi-Bellman equation of a stochastic optimal control problem on Minkowski spacetime, with the imaginary unit arising from the Minkowski metric.
---

<!-- inactive-ok-file: LIT-tmp0w06o — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmp6ess1: QM as stochastic optimization on spacetimes

## Contribution

The paper aims to explain the origin of the complex (imaginary) structure of quantum mechanics. It argues that relativistic invariance, spacetime geometry and a demand for linearity are the key ingredients. Starting from a stochastic control problem, the authors derive the Stueckelberg covariant wave equation, obtain a Telegrapher's equation from it, and from there recover the relativistic and nonrelativistic quantum equations. The stated payoff is insight into quantum mechanics from a coordinate-invariant stochastic optimization problem instead of postulates.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Starts from classical action minimization, replaces paths by a Markov diffusion dX = v ds + σ dW, and minimizes expected action; the value function satisfies an HJB equation, with optimal velocity v = -(1/m)∇J (Stochastic Classical Mechanics section, Eqs. 2-8).
- Places the lineage in Nelson (1966), Yasue (1981), Papiez (1982) and later stochastic-control approaches, and says their missing piece is why Schrödinger is diffusion in imaginary time (Introduction).
- Demands coordinate invariance with diffusion in four-position; Minkowski signature plus a logarithmic transform that linearizes the HJB equation (noise amplitude coupled to mass) yields the Stueckelberg equation (sections "Coordinate Invariance, Diffusions in the Minkowski Spacetime and Wick rotation"; "Coordinate Invariance Together with Linearity Leads to Quantum Mechanics").
- Telegrapher's equation offered as the "missing link" to the Dirac equation; Schrödinger recovered in the nonrelativistic limit (subsections of the same).
- Conclusion takes an interpretive stance: supports a realist/statistical reading of the wavefunction, says the results do not support the PBR theorem's thesis, and speculates about stochastic spacetime at Planck scale as the noise source (Conclusion and Discussion).

## Open questions

- Strongest claim: derivation "from first principles". Check which assumptions do the work: the log transform and the specific noise-mass coupling are chosen to make the HJB equation linear, which is the standard Hopf-Cole/path-integral-control trick. Is anything beyond that, plus a Wick rotation justified by the metric, being derived?
- The anti-PBR remark rests on a single citation (Rizzi 2018); check whether the paper argues it or only asserts it.
- ML link (honest, indirect): the same HJB/log-transform linearization underlies path-integral control and Schrödinger-bridge formulations used in diffusion generative models. Useful as a physics-side instance of that correspondence, not as an ML result.
