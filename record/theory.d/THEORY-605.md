---
number: 605
status: Active
formerly:
- THEORY-tmppgcbt
title: "In any ontological model that reproduces the quantum predictions and treats independently prepared systems as having product distributions over a joint state that is just the list of their states, distinct pure quantum states have distributions over the ontic state whose supports overlap in measure zero, so the pure state is fixed by the ontic state; approximate agreement within ε bounds the overlap by 2ε^{1/n}"
version: 1
tags:
- quantum-foundations
date: '2026-10-16'
source:
- LIT-062
summary: >-
  Pusey, Barrett & Rudolph (2011), [LIT-062](../literature.d/LIT-062.md), read in full in [NOTE-030](../notes.d/NOTE-030.md). For
  any two non-orthogonal pure states, n copies prepared independently and an
  entangled measurement in which each outcome is impossible for one product
  preparation force zero overlap; with ε error, D(µ0, µ1) ≥ 1 − 2ε^{1/n}
  (Eq. 7). Determinism and locality are not assumed. Preparation
  independence, in its strong product-space form, carries the weight, and
  dropping it permits ψ-epistemic models. The theorem excludes overlap,
  not every reading of ψ as knowledge, and it does not reach theories
  outside the ontological-models framework.
presupposed_by:
- THEORY-586
---

<!-- inactive-ok-file: THEORY-485 THEORY-586 THEORY-621 THEORY-630 THEORY-631 — Proposed; accounts that read or answer this theorem, named, not leaned on -->

# THEORY-605: In any ontological model that reproduces the quantum predictions and treats independently prepared systems as having product distributions over a joint state that is just the list of their states, distinct pure quantum states have distributions over the ontic state whose supports overlap in measure zero, so the pure state is fixed by the ontic state; approximate agreement within ε bounds the overlap by 2ε^{1/n}

## Source

Pusey, Barrett & Rudolph (2011), [LIT-062](../literature.d/LIT-062.md), read in full in [NOTE-030](../notes.d/NOTE-030.md).

## What was actually shown

**Assumptions.** A system prepared in isolation in a pure state has a
physical state λ, distributed as µ_ψ (p. 1; pure states only). Independent
preparations of n systems give the product µ_{x1}(λ1)⋯µ_{xn}(λn), and the
joint physical state is exactly the tuple (λ1, …, λn) (Eqs. 4–5, B3).
Measurement outcomes depend only on that tuple, through nonnegative response
functions (Eq. 5, B1). Determinism is not assumed (p. 4), nor Bell
locality for the measurement.

**Simple case (pp. 2–3, Eq. 1).** For |0⟩ and |+⟩ and two copies, an
entangled basis has each element orthogonal to one of |00⟩, |0+⟩, |+0⟩,
|++⟩. Any overlap of µ_0 and µ_+ then gives a quantum-forbidden outcome a
nonzero rate.

**General case (App. A).** For |ψ0,1⟩ = cos(θ/2)|0⟩ ± sin(θ/2)|1⟩ and n with
2 arctan(2^{1/n} − 1) ≤ θ, a circuit H^{⊗n}R_αZ_β^{⊗n} followed by a
computational-basis measurement gives each outcome |x⃗⟩ zero probability on
the preparation |Ψ(x⃗)⟩. [NOTE-030](../notes.d/NOTE-030.md) computes the minimum angle falling with n:
90°, 45°, 29.1°, 21.4°, 16.9° for n = 1…5.

**Noise-robust theorem (Eq. 7 = B2).** If every outcome probability is
within ε of quantum theory, then D(µ0, µ1) = ½∫|µ0 − µ1|dλ ≥ 1 − 2ε^{1/n};
equivalently ω(µ0, µ1)ⁿ ≤ 2ⁿε (B11). The proof: the overlap of the product
distributions factorises as ωⁿ (B7), while the forbidden outcomes bound it
by 2ⁿε (B10). At ε = 0 the supports meet in measure zero.

**What could have come out otherwise.** Before this, whether any model of
this kind could let distinct pure states share ontic states was open (p. 4).
A ψ-epistemic model satisfying the assumptions could have existed. It
cannot.

## What this does not say

- **That the quantum state is real, without qualification.** The theorem is
  conditional on preparation independence in its strong form. The authors
  concede that dropping it permits ψ-epistemic models (Lewis et al., their
  ref. [16]) and answer only by calling such models "contrived" (p. 4;
  [NOTE-030](../notes.d/NOTE-030.md), C4–C5).
- **That epistemic views are refuted.** The abstract's informal wording,
  that ψ cannot represent "mere information", is broader than the theorem,
  which defines mere information as support overlap (p. 2; C6). The paper
  leaves the QBist option and theories outside ontological models open
  (p. 5). What the theorem excludes is [THEORY-586](THEORY-586.md)'s subject.
- **Anything about mixed states.** Only pure states are treated.
- **That ψ-epistemic models of quantum fragments are excluded.** Spekkens'
  epistricted theories are ψ-epistemic with product composition and
  reproduce stabilizer and Gaussian subtheories exactly. By PBR's own
  argument those subtheories contain no PBR-type measurement, and PBR's
  measurements are indeed not stabilizer operations ([NOTE-030](../notes.d/NOTE-030.md)'s check).
  This consequence is [NOTE-030](../notes.d/NOTE-030.md)'s inference; none of the papers states it.
- **That the measurement uses the fewest systems possible.** Minimality in
  n rests on numerical SDP solutions only (App. C).
- **That the experiment has been done.** Feasibility is asserted (p. 4).

## Connections

- [LIT-003](../literature.d/LIT-003.md) (Schmid, Selby, Pusey, Spekkens) derives PBR's product form from
  diagram preservation (its Prop. 4.6), so a diagram-preserving ontological
  model of full quantum theory is caught by PBR ([NOTE-030](../notes.d/NOTE-030.md)).
- Gao's protective-measurement route to ψ-ontology, claimed to avoid
  preparation independence, is [THEORY-630](THEORY-630.md).
- Rovelli's relational reading sidesteps the theorem by positing no ontic
  state ([THEORY-621](THEORY-621.md)). Cuffaro & Hartmann place orthodox readings
  outside the framework ([THEORY-631](THEORY-631.md)).
- Wave-function realism's consequences for causal closure ([THEORY-485](THEORY-485.md))
  read PBR the same way.
- The toy bit theory ([THEORY-474](THEORY-474.md)) and the interference model
  ([THEORY-403](THEORY-403.md)) are ψ-epistemic models of fragments, outside the
  theorem's reach.
