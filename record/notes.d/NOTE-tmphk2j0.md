---
status: Skimmed
paper: LIT-tmpdkkr3
title: 'Abramsky, Barbosa & Mansfield, contextual fraction'
version: 1
date: '2026-09-27'
summary: >-
  For any empirical model in the sheaf-theoretic framework, the contextual fraction CF (one minus the largest weight of a noncontextual sub-model) equals the maximal normalised violation over all generalised Bell inequalities of the scenario, is computable with a linear programme whose dual yields the witnessing inequality, does not increase under free operations, and lower-bounds the failure probability of a Z2-linear MBQC computing a non-linear function.
---
<!-- inactive-ok-file: LIT-tmpdkkr3 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together; the theories citing it are Proposed until it is read closely -->

# NOTE-tmphk2j0: Abramsky, Barbosa & Mansfield, contextual fraction

## Contribution

The authors take the contextual fraction as a quantitative measure of contextuality for tables of outcome probabilities in any measurement scenario. It lets one compare how contextual models are across scenarios, it is exactly tied to Bell-inequality violation, it and a witnessing inequality are computed by linear programming, it is monotone under operations that cannot create contextuality, and it quantifies advantage in games and in measurement-based quantum computation.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Framework (p. 1–2): the scenario ⟨X, M, O⟩ and empirical models of Abramsky & Brandenburger 2011 ([LIT-016](../literature.d/LIT-016.md)); compatibility of marginals "is a generalisation of the usual no-signalling condition"; contextual = no distribution on O^X marginalising to every e_C.
- Eq. (1)–(2): e = λe^NC + (1−λ)e′; NCF(e) is the maximal λ, CF = 1 − NCF; the paper credits the general-scenario notion and "CF = 1 ⇔ strongly contextual" to [LIT-016](../literature.d/LIT-016.md); every model decomposes as NCF·e^NC + CF·e^SC with e^SC strongly contextual (not necessarily uniquely).
- Eq. (3)–(5), Theorem 1: NCF is the LP max 1·b s.t. Mb ≤ v_e, b ≥ 0 (M the incidence matrix); the normalised violation of any Bell inequality is ≤ CF(e), with equality attained by an inequality read off the dual LP (strong duality).
- Theorem 2: CF invariant under relabelling, non-increasing under translation of measurements and coarse-graining; CF(e ⊗ e′) = CF(e) + CF(e′) − CF(e)CF(e′), CF(e & e′) = max.
- Theorem 3: for an l2-MBQC using resource e to compute f with average failure p̄_F, p̄_F ≥ NCF(e)·ν̃(f), ν̃ the distance of f to the nearest Z2-linear function; an analogous bound for k-consistent games. Footnote [33] names contextuality-by-default measures as alternatives whose relation is left for future work.

## Open questions

- It turns [LIT-016](../literature.d/LIT-016.md)'s qualitative hierarchy into a graded, computable quantity, and it is the measure later work on contextuality as a computational resource uses.
- It inherits [LIT-016](../literature.d/LIT-016.md)'s restriction to no-signalling (consistently connected) models; it does not apply to data with context-dependent marginals, which is where contextuality-by-default (cx4) differs.
- Check the supplemental proof of Theorem 1(ii)–(iii) and the MBQC Theorem 3 conditions.
