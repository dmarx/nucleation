---
status: Skimmed
paper: LIT-tmp718h1
title: 'Gutknecht et al. 2025, Shannon invariants'
version: 1
date: '2026-09-25'
summary: >-
  Two averages over the partial information decomposition can be computed from Shannon entropies alone, with the number of entropies growing linearly in the number of sources. These are the average degree of redundancy and the average degree of vulnerability. They sidestep PID's ambiguous choice of redundancy measure and its super-exponential cost, explain what the old redundancy–synergy index actually measures, and show redundancy increasing and vulnerability decreasing with depth and training in small quantised networks.
---

<!-- inactive-ok-file: LIT-tmp718h1 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpbu012: Gutknecht et al. 2025, Shannon invariants

## Contribution

Biological and artificial neural networks process information through high-order interactions among many parts, but multivariate information measures are hard to define and do not scale. The authors introduce "Shannon invariants": quantities that capture properties of high-order information processing, depend only on the definition of entropy, and can be computed for large systems. In theory, they settle long-standing ambiguities about how to read common multivariate measures. In practice, they reveal information-processing signatures that differ across layers of deep learning architectures and change over training.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §I Introduction: PID has many competing redundancy measures and super-exponential complexity. The paper borrows from statistical mechanics the idea of measuring global averages without resolving the microstates, which here are the "information atoms".
- §II Definitions: "Shannon-invariance"; degree of redundancy (how many sources information can be reached through) and degree of vulnerability (how many specific sources information critically depends on). §II.D covers source-level versus robustness-based views of redundancy and synergy.
- §III: shows the redundancy–synergy index (RSI) is closely tied to the average degree of redundancy, and introduces a new "dual RSI" tied to vulnerability.
- §IV Deep learning (Figs. 2–3): quantised networks are used to avoid the infinite-capacity problem of deterministic continuous networks. In an MNIST MLP (95.5% test accuracy), redundancy about the label jumps in the first epoch and rises with depth, while vulnerability falls over training and with depth. In a convolutional face autoencoder, decoder layers are more redundant than encoder layers of matching size, and redundancy rises (vulnerability falls) with bottleneck width.
- §V Discussion: the authors conjecture that redundant encodings are favoured because they make representations robust and so help generalization. The measures need a number of entropies that is linear in the number of sources.

## Open questions

- A scalable, measure-agnostic handle on redundancy and synergy is directly usable for interpretability and representation analysis. This is the "boundary" the triage flags, since the anthology's ML side could also claim it.
- The DL results use small quantised networks. Check the estimation procedure (binning or quantisation, sample sizes) and whether anything scales to realistic models.
- Check the exact theorem linking RSI to average redundancy (§III.A) and the conditions under which the averages are well defined.
