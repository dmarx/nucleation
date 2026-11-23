---
status: Active
title: If an organization's operation relaxes at rate γ toward a configuration
  h(θ) set by a governance parameter θ that changes at rate at most V, with
  h Lipschitz with constant L, then its distance from the governed configuration
  stays within LV/γ once it starts within that, so a governance change of
  size Δθ by deadline H keeps the organization within a tolerance ε if LΔθ/(γH)
  ≤ ε; the condition is sufficient, not necessary, and it complements the
  necessary bound that a reference revisable at rate v cannot reach a demand
  farther than vH
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-057: no premise; the error bound by
    variation of constants re-checked, and numerically (sup |e| = 0.6000
    against a bound of 0.6000). Its "cannot reach a demand farther than
    vH" is of the reference's own reach; CLAIM-tmp2k3c5 bounds the demand
    by vH + delta + epsilon.
role: thesis
warrant: demonstrated
defeated_if: An error in the bound. As a reading of organizations, defeated
  only where the relaxation toward a governed configuration misdescribes how
  operation follows changed governance.
tags:
- control-theory
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- realizability
- will-organization
complements:
- CLAIM-tmp2k3c5
summary: 'A44 §4 of the exchange "Explain First Contact RL" (ChatGPT, third
  share of 2026-11-22): "a particularly compact formalization of the temporal
  feasibility of identity-preserving transformation". Checked by the assistant:
  the bound follows by variation of constants, and it is tight for a constant
  revision rate. The wording is A''s (ChatGPT, in the exchange of 2026-11-22);
  adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-711 — Proposed; cited in this filing of 2026-11-23 (third share) -->

# CLAIM-tmp947v0: If an organization's operation relaxes at rate γ toward a configuration h(θ) set by a governance parameter θ that changes at rate at most V, with h Lipschitz with constant L, then its distance from the governed configuration stays within LV/γ once it starts within that, so a governance change of size Δθ by deadline H keeps the organization within a tolerance ε if LΔθ/(γH) ≤ ε; the condition is sufficient, not necessary, and it complements the necessary bound that a reference revisable at rate v cannot reach a demand farther than vH

## Derivation (A44 §4), checked

With ẋ = −γ(x − h(θ)), θ̇ = v, and e = x − h(θ), we get ė = −γe − Dh(θ)v.
With ‖Dh‖ ≤ L and ‖v‖ ≤ V, variation of constants gives ‖e(t)‖ ≤
e^{−γt}‖e(0)‖ + (LV/γ)(1 − e^{−γt}). So ‖e(0)‖ ≤ ε and LV/γ ≤ ε keep ‖e‖ ≤ ε.
A constant-rate change V = ‖Δθ‖/H then gives L‖Δθ‖/(γH) ≤ ε. Checked with
python3 -I: a scalar case with constant v reaches the bound LV/γ exactly
in the limit.

## What it shows

There are four separate obstructions (A44):
- the reference moving too fast for its realization;
- operation slowing, so that the permissible retuning rate falls;
- governance unable to change θ fast enough for the deadline;
- the case the inequality does not settle, since it is sufficient only.

A44's way around retuning: "Preauthorize fast actions that remain within
the jurisdiction of the slower governing structure. ... The **commitment
is slow; its application is fast**." That is [CLAIM-711](CLAIM-711.md).

[CLAIM-tmp2k3c5](CLAIM-tmp2k3c5.md) is the necessary half: no reference revisable at rate v
reaches a demand farther than vH. This claim is a sufficient half for
keeping the realization close while the reference moves.
