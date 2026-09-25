---
status: Skimmed
paper: LIT-tmpjbdvh
title: 'Surface optimization in physical networks'
version: 1
date: '2026-09-25'
summary: >-
  The local branching of real physical networks (neurons, vasculature, trees, corals, plants) is predicted by minimizing surface area under a minimum-thickness constraint, not wire length. That explains the observed trifurcations, non-planar and asymmetric branch angles, and orthogonal sprouts, which Steiner and volume minimization forbid.
---

<!-- inactive-ok-file: LIT-tmpjbdvh — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpsznzu: Surface optimization in physical networks

## Contribution

Physical networks such as connectomes and vasculature are built from material, and "wiring economy" has long predicted their structure. The authors measure local branching geometry across six classes of 3D physical network and find systematic violations of wire-length minimization. They argue that the true material cost depends on full 3D surface geometry, which makes optimization hard. They then find an exact mapping from the surface-minimization problem to string-theory Feynman-diagram worldsheets (Nambu–Goto action). This predicts that as links thicken, tree-like motifs pass from Steiner bifurcations to stable trifurcations, and that the branching-angle distributions match data. They also predict stable orthogonal sprouts, which turn out to be common and functionally important, for example ending on synapses.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Empirical test of Steiner's three rules (Fig. 1): data cover human neurons, fruit-fly neurons, human vasculature, tropical trees, corals and Arabidopsis. About 15% of nodes are k=4 (rule 1 violated), bifurcations are non-planar (rule 2 violated), and branch angles show no peak at 2π/3 (rule 3 violated). Volume optimization of cylinders keeps rules 1–2 and so fails too.
- Formalism (Fig. 2, eqs 1–2): cost is the total surface area of smooth "sleeve" charts, subject to a minimum circumference w everywhere. This is equivalent to the classical Nambu–Goto worldsheet problem (pants decomposition). The numerics are released as min-surf-netw.
- Trifurcation transition (Fig. 3): with χ = w/r, the separation between the two bifurcations collapses to a trifurcation at χ ≈ 0.83. Empirical P(λ→0) > 0 in all six datasets, whereas Steiner predicts it vanishes.
- Sprouting vs. branching (Fig. 4): below a thickness ratio ρ_th ≈ 0.6, a thin branch leaves at 90° from a straight thick path. In the human connectome, 92% of sprouts end on synapses.
- Discussion: local surface minimization appears robust across systems. Real networks are on average about 25% longer than Steiner's global optimum, so global and functional demands act at larger scales. The model does not cover loops, which are absent from these datasets.

## Open questions

- A strong, falsifiable claim about physical network design, with neuroscience relevance (synapse formation). The mapping to string worldsheets is striking and should be checked in the Supplementary Information (§§3–7).
- A deeper reading should check how sensitive the skeletonization and high-degree-node detection are (SI §1), and whether "excellent agreement" holds per dataset or only in aggregate.
