---
status: Skimmed
paper: LIT-tmpxv1m2
title: 'Emergence as the conversion of information'
version: 1
date: '2026-09-25'
summary: >-
  Coarse-graining can convert redundant information into synergistic information, not merely discard information. In Boolean networks built so that past-to-future mutual information is identical at micro- and macroscale, the macroscale's PID "synergy bias" still rises.
---

<!-- inactive-ok-file: LIT-tmpxv1m2 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpmri7d: Emergence as the conversion of information

## Contribution

The authors ask whether reduction is always a good scientific strategy, noting that special sciences above physics exist. Earlier work showed that macroscales can raise dependency between system elements ("causal emergence"). The paper proposes an umbrella framework in which emergence is the conversion of information from one type to another under a change of scale. Applying PID to the mutual information of Boolean networks, and introducing a "synergy bias" measure, they show that synergy can grow at the macroscale even when total mutual information is unchanged. They argue that universal reduction would therefore generally lose synergistic information.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Partial-information spectra (Figs. 1–2) for logic gates (AND, XOR, …) show where each gate's information sits on the PI lattice.
- The "expansion method" (§3.2, Fig. 3) inverts the usual coarse-graining: a macroscale node is split into equivalence-class micro nodes. This keeps mutual information fixed and consistency with the macroscale perfect, so any change in synergy bias has to be conversion, not loss.
- Result (Fig. 4): for Gaussian systems, every system gains synergy at the macroscale and redundancy at the microscale. Deterministic systems start with low synergy bias and often lose it, but both classes fall on a common roughly linear trend of Δ synergy bias against macroscale synergy.
- The Discussion links this to the authors' effective-information account of causal emergence (determinism and degeneracy terms). It hypothesizes that the special sciences are useful because they convert redundant into synergistic information, beyond compression.
- §5.1 contrasts the approach with IIT and ΦID (Mediano/Rosas). The authors argue those measure joint information flow at a single scale with no micro-versus-macro comparison, which differs from item 21's framing.

## Open questions

- The "proof" of conversion depends on the equivalence-class construction. Check whether the effect survives for coarse-grainings found in real data rather than built by expansion, and how robust it is to the choice of redundancy measure (PID is not unique).
- It is in direct conversation with item 21. A deeper read should set the two definitions of emergence side by side.
- ML link, stated honestly: the Discussion mentions choosing the level of abstraction for comparing deep networks (citing Cao & Yamins) as one application. The paper itself has no ML experiments.
