---
number: 61
status: Skimmed
formerly:
- NOTE-tmpjab5t
paper: LIT-057
title: 'Saeedian et al. 2021, delay in generalized Lotka–Volterra'
version: 1
date: '2026-09-25'
summary: >-
  Adding a time delay to random generalized Lotka–Volterra communities pushes a feasible, stable equilibrium through an analytically computable critical delay into an oscillatory, non-point-attractor phase. Measured as the inverse coefficient of variation of total abundance in that phase, community stability rises with diversity, which is the opposite sign to May's local-stability result.
---

<!-- inactive-ok-file: LIT-057 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-061: Saeedian et al. 2021, delay in generalized Lotka–Volterra

## Contribution

May (1972) and later random-matrix work found universal patterns of feasibility and stability in large random ecosystems, but few studies have added delay. The authors study generalized Lotka–Volterra dynamics with instantaneous and delayed random interactions. Without delay, they find a simple analytical relation between feasibility and stability when intraspecific interactions dominate. Increasing the delay produces a transition from an equilibrium phase to a stable oscillatory phase, and the critical delay is computed analytically and matches simulations. With a stability measure suited to non-equilibrium dynamics, stability increases with diversity in the delay-induced oscillatory regime.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Framework (preprint Eq. 1): ẋ_i = x_i(r_i + Σ a_ij x_j(t) + Σ b_ij x_j(t−τ)). A and B are random with connectance C, the diagonal is fixed at −d_A and −d_B, and the growth rates r_i are uniform. The delay τ is the control parameter.
- Phases (Figs. 2–4, S = 100, C = 1): at τ = 12 the system is still asymptotically stable. At τ = 18 the leading eigenvalue of the delayed system has positive real part and the dynamics oscillate. At τ = 28 numerics diverge, though the authors say analysis suggests the true trajectories stay bounded.
- The critical delay τ_c is derived by linear stability analysis of the delayed system (Appendix A). Feasibility conditions are in Appendix B.
- Out-of-equilibrium stability (Eq. 16, Fig. 6): as diversity grows, the community-level coefficient of variation CV_c falls while the species-level CV_s rises. The authors present this as "a positive diversity–stability relationship... in agreement with experimental observations".
- Conclusion: delay is detrimental for local stability, and the authors argue for moving beyond local, equilibrium stability measures.

## Open questions

- It adds to the May complexity–stability debate: the diversity–stability sign depends on which stability notion is used (local asymptotic versus variability).
- Random-matrix stability with delays is also relevant to delayed-feedback dynamics in coupled learners, but the paper makes no such link.
- Check the published version against the preprint (figures and analysis may have been revised) and the "diverging phase" caveat.
