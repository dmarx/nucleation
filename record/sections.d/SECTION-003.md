---
number: 3
status: Active
title: 'Integration and the stability of maintenance'
version: 1
date: '2026-11-01'
asserts:
- CLAIM-521
- CLAIM-tmpx8nob
discusses:
- CLAIM-194
- CASE-189
- CLAIM-422
- CLAIM-280
- CASE-079
summary: >-
  Section 3 of [WORK-010](../works.d/WORK-010.md), The Individual and Its Conditions. Its prose
  is transcluded by the manuscript view; each paragraph says in a
  directive which claims it asserts and which it only discusses.
---

# SECTION-003: Integration and the stability of maintenance

## Manuscript text

An attractive operational criterion of individuality is the strength of integration among components. When a collection supports coherent modes and relaxes rapidly after disturbances, describing it as one dynamically organized unit may be justified. But the rate at which its components relax and the resilience of the machinery establishing their coupling answer different questions. <!-- ref::discusses: CLAIM-194 -->

Nucleation's constructed case contains mutually maintained constraint capacities and a connector that governs the effective coupling of three units. Writing their dynamics as $\dot x=-Lx$, with a weighted graph Laplacian $L=qB^{\mathsf T}\operatorname{diag}(c_1,c_2)B$, the symmetric state has spectrum $\{0,qc,3qc\}$. Its smallest nonzero eigenvalue gives a measure of the rate at which relative differences between the three units relax. The capacities are maintained by a distinct nonlinear core, whose stable positive regime approaches a saddle-node under an increasing damage parameter. <!-- ref::discusses: CASE-189 -->

At the fold, the recovery eigenvalue of the maintenance core approaches zero while the network's spectral gap remains approximately $0.989$ in the specified parameterization. Current coupling is still strong even as the maintaining regime loses its local stability. The numerical value is not a universal measure of individuality; it is a feature of one constructed counterexample. Moreover, the coupled units do not feed back into the maintenance core, so the example does not establish self-maintenance of the entire three-unit organization. <!-- ref::asserts: CLAIM-521 --> <!-- ref::discusses: CASE-189 -->

The warranted result is nevertheless decisive against a proposed entailment: **strong present dynamical integration does not imply robust maintenance of the mechanism producing that integration**. An operative constraint can remain effective while its producer approaches failure. One might have a good dynamic model of the coupled units and a poor model of the vulnerability of their coupling. <!-- ref::asserts: CLAIM-521 -->

This distinction appears in other domains without presupposing a common dynamical law. An institution can possess executable procedures while the capacity to implement them erodes. A maintained visual pattern can remain stable through continuous replacement, repair, and opposition among its participants. These analogies identify an explanatory contrast, not a universal mechanistic equivalence. In every case the state of an organizational product must be distinguished from the state and identity of the producer. <!-- ref::asserts: CLAIM-tmpx8nob --> <!-- ref::discusses: CLAIM-422, CLAIM-280, CASE-079 -->
