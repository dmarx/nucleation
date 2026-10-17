---
status: Active
status_note: 'read in full 2026-10-17 (NOTE-tmplm3la); worth reading as the four-page source of transfer entropy, which the record uses in seven documents without holding it: T_{J→I} is the Kullback entropy of the transition probabilities of I with and without the past of J, at history lengths k and l that the definition leaves open. Read it knowing that "information transfer" and "exchange" are the paper''s words for a conditional mutual information, that common inputs are excluded only when they are known and conditioned on, that the continuum-limit claim is asserted, and that the evidence is two coupled-map lattices and one physiological pair, the last of which Schreiber himself says a common trigger could explain. Filed as THEORY-tmp1jjkw.'
title: 'Measuring Information Transfer'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Filed at the owner's request as the source of the definition that
    NOTE-053, NOTE-788, THEORY-275, THEORY-568, THEORY-641 and the
    Granger-causality readings use secondhand. Citation checked against the
    arXiv API on 2026-10-17 (Phys. Rev. Lett. 85, 461). Not held in the
    Anthology of the SOTA: a grep of its record/ (clone d1573d2, pulled
    2026-10-17) for "Schreiber", "transfer entropy" and the identifiers
    found nothing. Read in full the same day from arXiv nlin/0001042v1
    (NOTE-tmplm3la); the PRL version was not compared.
tags:
- information-theory
- complex-systems
- causality
date: '2026-10-17'
published: '2000-01-19'
arxiv: 'nlin/0001042'
doi: '10.1103/PhysRevLett.85.461'
first_author: 'Schreiber'
keywords:
- 'transfer entropy'
- 'information transfer'
- 'mutual information'
- 'entropy rate'
- 'coupled map lattices'
- 'Kullback entropy'
implementations: []
summary: >-
  Schreiber (2000), *Physical Review Letters* 85, 461, [ARXIV-nlin/0001042](https://arxiv.org/abs/nlin/0001042). Defines the transfer entropy T_{J→I} = Σ p(i_{n+1}, i_n^{(k)}, j_n^{(l)}) log[p(i_{n+1} | i_n^{(k)}, j_n^{(l)}) / p(i_{n+1} | i_n^{(k)})], the Kullback entropy of assuming that I's transitions do not depend on J's past, with history lengths k and l ("most natural" l = k or l = 1). Unlike time-delayed mutual information it is directional and zero for static correlation. In a tent-map lattice it is O(ε²) in the coupling while time-delayed MI is zero, and in an Ulam-map lattice it shows the coupling's direction where time-delayed MI does not.
---

# LIT-tmpz9o5z: Measuring Information Transfer

Thomas Schreiber (2000), "Measuring Information Transfer", *Physical Review Letters* 85: 461 — [ARXIV-nlin/0001042](https://arxiv.org/abs/nlin/0001042)

## Key takeaways

*From the reading, [NOTE-tmplm3la](../notes.d/NOTE-tmplm3la.md).*

- **The definition (Eq. 4).** T_{J→I} = Σ p(i_{n+1}, i_n^{(k)},
  j_n^{(l)}) log[p(i_{n+1} | i_n^{(k)}, j_n^{(l)}) / p(i_{n+1} |
  i_n^{(k)})], with i_n^{(k)} = (i_n, …, i_{n−k+1}). It measures the
  departure from the "generalized Markov property" p(i_{n+1} | i_n^{(k)})
  = p(i_{n+1} | i_n^{(k)}, j_n^{(l)}). The paper leaves k and l to the user:
  l = k or l = 1 are "most natural", l = 1 cheaper.
- **Why not delayed MI.** Mutual information is symmetric. Introducing a
  lag gives it a direction "in a somewhat ad-hoc way", and still counts
  correlation from common history or input as exchange.
- **Continuous systems.** For coarse-grained states the ε → 0 limit is
  asserted finite and partition-independent, except under deterministic
  coupling. A known common driver Z can be excluded by conditioning on it.
- **Estimation.** A step-kernel (correlation-sum) estimator of the joint
  probabilities at radius r, with temporally close neighbours excluded.
- **Examples.** A tent-map lattice: T = α²ε²/ln 2 + O(ε⁴) in the coupling
  direction, zero against it, and zero delayed MI. An Ulam-map lattice:
  T stays consistent with zero against the coupling for every ε, where
  delayed MI does not. Heart and breath rates of a sleeper: T(heart →
  breath) > T(breath → heart), with a common trigger left open.

## Standing in the record

Filed on 2026-10-17 as the source of the term, and read the same day. The
record's documents choose k and l differently, and all of them choose
within Schreiber's definition. [NOTE-053](../notes.d/NOTE-053.md) uses l = k; [NOTE-788](../notes.d/NOTE-788.md) uses
k = l = 1 with an added delay τ that the paper does not define. Filed as
[THEORY-tmp1jjkw](../theory.d/THEORY-tmp1jjkw.md). [TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md) is the record's own statement of the
term, and [CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md) its position on whether the quantity is a flow.
