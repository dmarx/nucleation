---
status: Active
title: "Transfer entropy is the average of a local transfer entropy, the log ratio at each observation of the destination's next-state probability with and without the source given the destination's past, which can be negative where the source misleads; the destination history must be long for it to exclude self-influence routed through the source; and conditioning also on the destination's other causal parents (complete) can differ sharply from conditioning on its past alone (apparent), as in elementary cellular automata, where long-history local transfer entropy picks out gliders and domain walls"
version: 1
tags:
- complex-systems
- information-theory
date: '2026-10-16'
source:
- LIT-tmps1x9k
summary: >-
  Lizier, Prokopenko & Zomaya (2008), LIT-tmps1x9k, read in full in
  NOTE-tmpr3ktj. The local decomposition is an identity; the claims about
  k and about particles rest on elementary CAs judged by eye. Three worked
  local values and rule 18's XOR structure were checked.
---

# THEORY-tmp22xor: Transfer entropy is the average of a local transfer entropy, the log ratio at each observation of the destination's next-state probability with and without the source given the destination's past, which can be negative where the source misleads; the destination history must be long for it to exclude self-influence routed through the source; and conditioning also on the destination's other causal parents (complete) can differ sharply from conditioning on its past alone (apparent), as in elementary cellular automata, where long-history local transfer entropy picks out gliders and domain walls

## Source

Lizier, Prokopenko & Zomaya (2008), "Local information transfer as a
spatiotemporal filter for complex systems", arXiv 0809.3275v1 (Phys. Rev.
E 77, 026110), LIT-tmps1x9k, read in full in NOTE-tmpr3ktj.

## What was actually shown

**An identity.** T_{Y→X} = ⟨t_{Y→X}(n + 1, k, l)⟩, with
t = log p(x_{n+1} | x⁽ᵏ⁾_n, y⁽ˡ⁾_n)/p(x_{n+1} | x⁽ᵏ⁾_n) (Eq. 9). The local
value is unbounded above and can be negative.

**History length.** With k = 1, local TE does not separate rule 110's
gliders from the background (Fig. 2). With k ≥ 6 it does, and with k = 16
it concentrates on the gliders' leading edges (Figs. 3, 5). For a periodic
domain of period p, k ≥ p − 1 gives zero transfer there; with gliders no
finite k is enough.

**Apparent against complete.** Complete TE conditions on the destination's
other neighbours (Eq. 14) and is nonnegative in deterministic systems. In
rule 18's domain it is about 1 bit at alternate sites from each channel,
where apparent TE is 0. Checked: there the rule is L ⊕ R.

**Particles.** In rules 110, 54, 18 and 146, gliders and domain walls are
where local TE is high, in their direction of motion.

What could have come out otherwise: long-history local TE could have
highlighted the background domain as much as the gliders, as k = 1 does.

## What this does not say

- **That transfer entropy measures a flow from one source.** Rule 18's
  domain has 1 bit determined jointly by two sources; apparent TE gives
  it to neither and complete TE to each (CLAIM-tmpu9ivq).
- **That complete TE is available outside models.** It needs the causal
  parents.
- **That a finite k is correct.** k is bounded by sample size, and the
  averages have not converged at k = 16.
- **Anything about continuous or stochastic systems**, which are asserted to
  be within reach and not tested.
- **That high local TE is causal influence.** The paper's own perspective is
  "predictive or computational", and it defers comparison with Ay and
  Polani's interventional flow.

## Connections

- Generalizes Schreiber's measure (LIT-tmpz9o5z) pointwise; its average is
  [TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md)'s quantity.
- NOTE-788's TE is the k = 1 case, which this paper finds structure-blind
  in rule 110.
