---
number: 4
status: Active
title: 'State equivalence and maintenance provenance'
version: 1
date: '2026-11-01'
asserts:
- CLAIM-522
- ARG-050
discusses:
- CASE-189
- CLAIM-414
- CLAIM-194
- CLAIM-530
summary: >-
  Section 4 of WORK-010, The Individual and Its Conditions. Its prose
  is transcluded by the manuscript view; each paragraph says in a
  directive which claims it asserts and which it only discusses.
---

# SECTION-004: State equivalence and maintenance provenance

## Manuscript text

The first construction separates the strength of coupling from the stability of its maintainer. The second separates behavior from the location of the productive mechanism itself. Let $c$ be the constraints or capacities whose maintenance is under investigation. An internally produced system A obeys $\dot c=P(c)-D(c)$, with production $P$ and degradation $D$. System B lacks the corresponding internal production machinery but receives a state-dependent contribution from an external controller: $\dot c=-D(c)+u_{\mathrm{ext}}(c)$, where $u_{\mathrm{ext}}(c)=P(c)$. <!-- ref::discusses: CASE-189 -->

For matching initial conditions and for the stipulated family of interventions on the capacity state, the systems satisfy identical equations and therefore follow identical trajectories. Their responses to damage and recovery perturbations are identical when damage enters the shared degradation law. Complete observation of **this reduced state** cannot separate them. This is not equivalence under complete microscopic observation, and it is not equivalence under interventions directed at the productive mechanisms. <!-- ref::asserts: CLAIM-522 --> <!-- ref::discusses: CLAIM-414 -->

Disable the productive pathway inside the candidate system and A changes while B may not. Interrupt the external controller and B changes while A may not. Ordinary state-level intervention and productive-mechanism intervention answer different questions. This demonstrates a relative nonidentifiability result: from dynamics on one chosen state space under one chosen intervention family, the causal provenance of productive maintenance is not in general identifiable. <!-- ref::asserts: CLAIM-522, ARG-050 -->

The result is close to definitional because the controller has been chosen to reproduce the internal production term exactly. Real controllers may exhibit delay, noise, or saturation. None of this invalidates the existence counterexample, but it constrains the philosophical conclusion. A compact effective model need not be false because it omits provenance; it may be completely adequate for its intended predictions. It becomes insufficient when asked to justify claims specifically about where productive capacities are realized.

The internal/external distinction is boundary-relative. Expanding the boundary to include the controller makes the producer internal to the enlarged system. But this does not render the causal facts arbitrary: relative to a declared boundary we can investigate which mechanisms lie inside it and which interventions expose their operation. Such findings can refine or undermine an initial candidate individuation, though they do not establish a metaphysically unique boundary from nothing. <!-- ref::discusses: CLAIM-194, CLAIM-530 -->
