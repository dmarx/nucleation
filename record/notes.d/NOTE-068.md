---
number: 68
status: Skimmed
formerly:
- NOTE-tmpna8bp
paper: LIT-050
title: 'Tembine et al., mean-field-type games with Rosenblatt noise'
version: 1
date: '2026-09-25'
summary: >-
  Replacing Rosenblatt noise (non-Gaussian, self-similar, long-range dependent) with Brownian, fractional-Brownian or jump noise before optimising yields suboptimal controllers. The authors derive the Rosenblatt-driven LQ optimal gain via a modified algebraic Riccati equation, and extend the analysis to zero-sum saddle points, non-zero-sum Nash equilibria and mean-field-type games.
---

<!-- inactive-ok-file: LIT-050 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-068: Tembine et al., mean-field-type games with Rosenblatt noise

## Contribution

The paper brings Rosenblatt noise into stochastic systems, control and mean-field-type game theory to address the limits of Gaussian and Markovian models. It cites real-data evidence of skew, heavy tails and long-range dependence in water demand, e-commerce, power grids, wireless channels and agricultural supply chains. The Rosenblatt process, non-Gaussian, non-Markovian and self-similar, is offered as a baseline model for such behaviour. The authors develop stochastic-calculus formulas for it, apply them to dynamical systems and optimal control, and show that conventional noise approximation is suboptimal. They then give saddle-point conditions for zero-sum games and state-feedback Nash equilibria for non-zero-sum games, and argue that this matters for prediction and control.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §II (pp. 3–21) presents data vignettes of non-Gaussianity: e-commerce "whale" spending, prosumer net load, Punjab water use, Sahel mango supply chains, CPU/GPU/TPU adoption, AI funding, onion prices, underwater channels and EV battery health. These are presented as histograms/densities with "Rosenblatt-like" tails, and no formal fit test is shown in the parts I read.
- §III (p. 21): R_H(t) is a double Wiener–Itô integral with 1/2 < H < 1. It is self-similar (R_H(ct) =d c^H R_H(t)) and non-Gaussian, obtained as a nonlinear transform of fBM, and shares fBM's covariance.
- §VI (pp. 24–27): for scalar ergodic LQ control, the optimal gain solves (1−H)b₂K̂² + b₁K̂ − Hb₂q/r = 0, equivalently a Riccati equation (1−H)(b₂²/r)P² + b₁P − Hq = 0 with K̂ = b₂P/r. §VI-A (Fig. 16), "Failure of Noise Approximation-Optimization Cascade": substituting Brownian, fBM, Gauss–Volterra or Poisson noise leads to suboptimal control.
- Later sections cover adaptive and variance-aware control (VII–VIII), zero-sum and non-zero-sum games (IX–X), MFTG with a cooperative case and noise modelling (XI), hierarchical MFTG (XII), and MFTG vs multipopulation coalitional MFG with a renewable-energy example (XIII).
- §XIV ("Rosenblatt Foundational Diffusion Models", pp. 41–44) proposes "super-diffusion transformers" driven by an OU-type Rosenblatt SDE and says the approach "significantly enhances the performance of generative machine intelligence models". The pages I read give only the SDE and its variance, with no experiment behind that claim. The conclusion (§XV) frames the results for "agentic AI" and multi-agent risk.

## Open questions

- A real point: optimising under a mis-specified noise model is suboptimal. The LQ Riccati modification is concrete and checkable.
- The ML-facing claim about super-diffusion transformers is unsupported in the text I read and should not be cited as evidence. Check whether any later version or the Springer chapter adds experiments.
- The data section is illustrative. Check whether any Rosenblatt fit is actually estimated against alternatives (e.g. stable, or other Hermite processes).
