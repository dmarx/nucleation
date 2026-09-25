---
number: 10
status: Skimmed
formerly:
- NOTE-tmpbpcaw
paper: LIT-025
title: 'Greater than the parts'
version: 1
date: '2026-09-25'
summary: >-
  Within the ΦID framework, a system can host causally emergent features of order k if and only if its dynamics carry k-th order synergy about their own future. That emergence capacity splits exactly into downward causation plus causal decoupling. Both can be detected with redundancy-function-free criteria that use only low-order marginals.
---

<!-- inactive-ok-file: LIT-025 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-010: Greater than the parts

## Contribution

Emergence is widely discussed, from galaxy formation to consciousness, but it lacks formalisms that make it measurable. This review restates and extends a recent theory of causal emergence built on information decomposition. In that theory, a system is emergent to the extent that information about its temporal evolution cannot be obtained from its parts taken separately. The article aims to be an accessible but rigorous introduction, discusses the approach's merits across scenarios, and addresses common misunderstandings and interpretive issues.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Preliminaries (§II): PID splits mutual information into redundant, unique and synergistic atoms. ΦID decomposes time-delayed mutual information into 16 atoms for two sources (Fig. 1).
- The core definitions (§III) and theorem: a supervenient feature V is k-th-order causally emergent if Un⁽ᵏ⁾(V_t; X_t′ | X_t) > 0. A system has such features iff Syn⁽ᵏ⁾(X_t; X_t′) > 0, and Syn⁽ᵏ⁾ = D⁽ᵏ⁾ (downward causation) + G⁽ᵏ⁾ (causal decoupling), a decomposition presented as exhaustive (Eq. 4).
- Interpretation (§IV A): the measures are neither Granger nor Pearl by construction. They read as interventional if p(X_t′|X_t) is a do-distribution, and as predictive otherwise.
- Interpretation (§IV B): lack of invariance under a change of coordinates is defended as a feature of a mereological theory, not a bug. The footnoted XOR example shows the atoms change under a recoding.
- Applications (§V, Fig. 2): Game of Life particle collisions, a flocking model (the flock's centre of mass predicts itself beyond the individual birds), macaque ECoG/motion, and human fMRI in resting state and loss of consciousness.
- Open problem: no efficient estimators of G⁽ᵏ⁾ exist for three or more time series (§V footnote).

## Open questions

- The iff theorem between emergence and synergy is the load-bearing result. It lives in the cited Rosas et al. (2020, PLoS Comp Bio) paper, and the review only restates it; check the assumptions there. Also check how much the results depend on the choice of redundancy function.
- ML link, stated honestly: PID/ΦID synergy measures are used in interpretability and representation analysis (e.g., synergy between neurons or features). This review is a compact entry point, but it contains no ML experiments.
- Coordinate dependence is a real limitation when the "parts" of a learned representation are arbitrary, for example a basis choice in neural activations.
