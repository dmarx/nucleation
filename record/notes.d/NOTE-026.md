---
number: 26
status: Skimmed
formerly:
- NOTE-tmpypyib
paper: LIT-020
title: 'Forman-Ricci curvature of networks'
version: 1
date: '2026-09-25'
summary: >-
  Forman's combinatorial discretization of Ricci curvature gives a cheap, edge-based network characteristic whose distribution separates model network classes (real networks resemble Barabasi-Albert) and whose associated Ricci and Laplacian flows can be used for change detection and denoising in evolving weighted networks.
---

<!-- inactive-ok-file: LIT-020 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-026: Forman-Ricci curvature of networks

## Contribution

The paper proposes Forman-Ricci curvature, and the geometric flow built on it, as edge-level descriptors of complex networks to complement the usual node-based statistics. After motivating the construction mathematically, the authors compute these quantities on static and time-evolving networks and compare them with established node-degree-based measures. They argue the tools could support data-mining tasks such as denoising, clustering, and extrapolating how a network evolves.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Forman curvature is derived from a Bochner-Weitzenbock formula on weighted CW complexes; for graphs (1-dimensional complexes) it reduces to a simple closed form in node and edge weights, making it far cheaper than Ollivier's optimal-transport curvature, which the authors say is "closely correlated" (§1, §2.2-2.3, §5).
- Curvature distributions on a Google web graph, a Facebook graph and a BioGrid gene network most resemble the Barabasi-Albert model; surprisingly Erdos-Renyi fits closer than Watts-Strogatz (Fig. 3, Table 1, §3.2).
- Introduces a curvature-based graph distance via earth mover's distance between curvature density estimates, proposed as a classification scheme (§3.1-3.2, Eqs. 30-34).
- Defines a discrete Forman-Ricci flow update gamma~(e) - gamma(e) = -Ric_F(e) gamma(e) and uses it for change detection on Gnutella snapshots (§4.1, §4.3, Fig. 7).
- Proposes Laplacian flow for denoising edge weights, illustrated only on Zachary's karate club; the discussion concedes applications (classification, extrapolation, clustering, denoising) are largely proposals with preliminary evidence (Fig. 8, §5).
- Notes Forman curvature lacks a Gauss-Bonnet-type theorem, which blocks a well-defined long-time flow (§5).

## Open questions

- The practical claim (Forman ~ Ollivier at a fraction of the cost) is asserted with "strong indications" and deferred to a forthcoming study; verify against later comparison papers before relying on it.
- Empirical evidence is small (three real networks, three models); the "classification scheme" is demonstrated on a handful of samples.
- ML link: discrete Ricci curvature (Forman and variants) later became a tool for diagnosing over-squashing and guiding graph rewiring in GNNs; this paper is an early network-science source for Forman curvature on graphs, not for those GNN results themselves.
