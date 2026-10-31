---
number: 1254
status: Active
formerly:
- THEORY-tmp78ls3
title: 'A controller that must stay safe under every model it has not ruled out cannot use the evidence its committing action produces: if the information it can gather before its first action that forecloses a safe continuation under an alternative is bounded by β, every such controller forfeits at least about ½e^{−β} of the value reachable only by committing, so a linear oracle gap gives linear regret, and acting on an exclusion at risk α needs about log(1/(2α)) nats gathered beforehand'
version: 1
tags:
- control-theory
- mathematics
- learning-theory
- information-theory
date: '2026-10-31'
source:
- LIT-1880
summary: >-
  Saligrama (2026), [LIT-1880](../literature.d/LIT-1880.md), Theorem 1 and its examples, read in
  [NOTE-1466](../notes.d/NOTE-1466.md). The proof is data processing on the stopped record plus
  Bretagnolle–Huber, and the explicit relaxation and one example's
  optimization were checked numerically. Active: a theorem with a short
  proof, checked. It is a lower bound only; bounded information is
  sufficient for an unavoidable gap, and unbounded information does not by
  itself give recovery.
---

# THEORY-1254: A controller that must stay safe under every model it has not ruled out cannot use the evidence its committing action produces: if the information it can gather before its first action that forecloses a safe continuation under an alternative is bounded by β, every such controller forfeits at least about ½e^{−β} of the value reachable only by committing, so a linear oracle gap gives linear regret, and acting on an exclusion at risk α needs about log(1/(2α)) nats gathered beforehand

## Source

Saligrama (2026), [LIT-1880](../literature.d/LIT-1880.md), §§2–4 (Lemma 1, Definitions 3–6, Theorem
1, Corollaries 2–4), pp. 4–18 of arXiv 2607.16895v1; read in
[NOTE-1466](../notes.d/NOTE-1466.md).

## What was actually shown

**Setting.** A causal policy must keep the probability of any constraint
violation at most η_T under every model θ in the initial class (uniform
chance safety). Regret is measured against the safe oracle that knows θ.

**Commitment.** For a target θ and an alternative θ′, a commitment is the
first action after which, under θ′, no safe continuation remains. It is
decided from the history and the action, before that action's
observation, so τ is a stopping time for σ(H_{t−1}, U_t).

**Three quantities.** α_T is the largest probability, over uniformly safe
policies, of committing under θ′; if commitment forces a violation there,
α_T ≤ η_T. G_T(q) is the least target regret of a safe policy that fails
to commit with probability at least q. I_pre is the largest KL divergence
between the records under θ and θ′ stopped at commitment.

**The bound.** Data processing on the event "no commitment" gives
d_bin(P_θ(no commit) ∥ P_θ′(no commit)) ≤ I_pre. Bretagnolle–Huber then
gives P_θ(no commit) ≥ ½e^{−I_pre} − α_T. Hence
R_T(π; θ) ≥ G_T(½e^{−I_pre} − α_T). With a linear profile
G_T(q) ≥ G_T q − ζ_T, if β = sup_T I_pre < ∞, α_T → 0 and ζ_T = o(G_T),
the worst-case regret of every uniformly safe policy is at least
½e^{−β}G_T asymptotically. The explicit bound is positive until
I_pre ≥ log(1/(2α_T)), which is 2 log T − log 2 at α_T = T⁻².

**Instances.** In a device whose commands spend headroom θu² and are
observed through θu + noise, I_pre ≤ (θ_d − θ_b)²d₀/(2σ²θ_d) for every T,
and against a healthy target the gap is Θ(T), so regret is linear. Two
constrained linear-regulation variants give linear regret too
(Corollary 4).

**Checked.** The Bretagnolle–Huber relaxation of ψ_α over twenty (α, D)
pairs; the finite-headroom bound and threshold by hand; the
boundary-target optimization (44)–(45) numerically, converging to the
stated T^{2/3} correction.

**What could have failed.** The evidence produced by the committing
action could have been usable, as it is in an analysis over the full
trajectory. The stopping-time construction is what excludes it.

## What this does not say

- **That unbounded information gives recovery.** The certificate is
  sufficient for a gap, not necessary. One safe policy must still gather
  the information and then enter the selected regime safely (Remark 6,
  §9).
- **That the gap is total.** With many alternatives, finite information
  can still certify a smaller candidate list and recover part of the gap
  (Proposition 1).
- **Anything about a different safety criterion.** A budget on cumulative
  violations, rather than a per-model bound on violation probability,
  falls outside the premise (Remark 4).
- **That a better estimator helps.** When pre-commitment information is
  bounded, the experiment, the sensor or the degree of specialization has
  to change (§9).
