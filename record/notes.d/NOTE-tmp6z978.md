---
status: Skimmed
paper: LIT-tmp3on2v
title: 'Community Detection on Networks with Ricci Flow'
version: 1
date: '2026-09-25'
summary: >-
  Iterating an Ollivier-Ricci-curvature-driven flow on edge weights stretches inter-community (negatively curved) edges and shrinks intra-community (positively curved) ones, so thresholding the evolved weights ("surgery") recovers communities with accuracy competitive with or better than standard methods on SBM, LFR and several labelled real networks.
---

<!-- inactive-ok-file: LIT-tmp3on2v — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmp6z978: Community Detection on Networks with Ricci Flow

## Contribution

Real networks often contain communities, and most detection methods are statistical or combinatorial. The authors instead treat a network as a geometric object and communities as a geometric decomposition, borrowing curvature and discrete Ricci flow, tools that decompose smooth manifolds in mathematics. They apply this to networks with known ground-truth communities and report that the geometric approach is effective.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Motivation is the Hamilton-Perelman picture: Ricci flow develops neck-pinch singularities that surgery removes, decomposing a manifold; the discrete analogue removes over-stretched edges (§1, Fig. 1).
- Uses Ollivier curvature kappa_xy = 1 - W(m_x, m_y)/d(x,y) with a generalized neighbour measure parameterized by alpha (laziness) and p (distance discount); flow update w_xy <- d(x,y) - kappa_xy d(x,y), with surgery typically after ~10-15 iterations (§3).
- Theorem 4.1: for a symmetric family G(a,b) of cliques joined by single edges, the K0 (alpha=0, p=0) Ricci flow provably shrinks intra-community edges asymptotically faster than inter-community edges when a > b >= 2 (§4.1; proof in SI).
- On SBM (500 nodes, two communities) accuracy is near-perfect up to p_inter/p_intra = 0.5 then collapses sharply by 0.55; on LFR it is reported as the most accurate and more stable than Spinglass (Fig. 5, §4.2.2-4.2.3).
- Cutoff selection without labels: pick the threshold where modularity first plateaus; varying the cutoff exposes hierarchical community structure (Figs. 6-7).
- Code released as the GraphRicciCurvature Python package (Data availability, p. 13).

## Open questions

- The empirical superiority claims rest on a limited benchmark set (SBM, LFR, GNet, ~6 labelled real graphs) compared against iGraph baselines; check sensitivity to the surgery threshold and number of iterations, which are hand-set.
- Theorem 4.1 covers only a highly symmetric toy family; whether any guarantee extends to SBM-like graphs is not shown here.
- ML link: Ollivier-Ricci curvature and the GraphRicciCurvature tooling are used in later graph-learning work (e.g. curvature-based analyses of GNN message passing); this paper is the community-detection source, not a GNN paper.
