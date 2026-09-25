---
number: 30
status: Skimmed
formerly:
- NOTE-tmp2gcwm
paper: LIT-062
title: 'Pusey, Barrett & Rudolph, reality of the quantum state (PBR)'
version: 1
date: '2026-09-25'
summary: >-
  Assume isolated systems have objective physical states and independently prepared systems have independent physical states (preparation independence). Then distinct pure quantum states must correspond to non-overlapping distributions over physical states, so ψ-epistemic models in Harrigan–Spekkens' sense cannot reproduce quantum predictions.
---

<!-- inactive-ok-file: LIT-062 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-030: Pusey, Barrett & Rudolph, reality of the quantum state (PBR)

## Contribution

Physicists have never agreed on what a quantum state represents: reality directly, or only knowledge about some underlying reality. The authors prove that any model in which the state is merely information about a system's physical state, and in which independently prepared systems have independent physical states, makes predictions that contradict quantum theory.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Setup (p. 1–2, Fig. 1): a label L is a physical property if the distributions µ_L(λ) for different values have disjoint supports. ψ is "mere information" if the µψ for two distinct states overlap. The formalisation follows Harrigan–Spekkens and Hardy.
- Simple case (p. 2–3, Fig. 2, Eq. 1): prepare |0⟩ or |+⟩ on two independent systems and make an entangled measurement onto |ξ1..4⟩. Each outcome is orthogonal to one of the four product preparations. With probability q² both λs lie in the overlap region, and the device risks an outcome that QM forbids, so there is a contradiction.
- General case (p. 3, Fig. 3, App. A): for any non-orthogonal pair with angle θ, take n copies with 2^{1/n}−1 ≤ tan(θ/2). A circuit Z_β, then a phase gate R_α on |0…0⟩, then Hadamards gives a measurement where each outcome has zero probability on one of the 2^n preparations.
- Noise robustness (p. 3–4, Eq. 7, App. B): if the model's predictions are within ε of QM, the total variation distance satisfies D(µ0, µ1) ≥ 1 − 2ε^{1/n}. The authors call an experiment challenging but feasible, and it needs non-post-selected high-fidelity gates.
- Discussion (p. 4–5): the analogy is with Bell's theorem. Dropping preparation independence allows ψ-epistemic models (Lewis et al.). Accepting the conclusion makes collapse a physical process, or else pushes toward every branch having a counterpart in reality. The exponential parameter count of ψ becomes surprising, and the authors note that QBism-style "information about outcomes" readings remain open.

## Open questions

- It is the foundational reference for the cluster: c16 (Spekkens' toy theory is ψ-epistemic by construction), c19 (which argues PBR rules out only overlap, not epistemic readings in general) and c15 (Barandes' demotion of ψ to a mathematical tool) all position themselves against it.
- The load-bearing assumption is preparation independence, which is where the critics push. A deeper read should pair it with Leifer's review and with the Lewis–Jennings–Barrett–Rudolph counter-model.
