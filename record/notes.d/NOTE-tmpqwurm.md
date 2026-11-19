---
status: Read
paper: LIT-tmpn17zh
title: 'Rupe and Crutchfield 2018 — Local Causal States and Discrete Coherent Structures'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1801.00515 (HTTP 200, 3.3 MB PDF, v1 of
    1 Jan 2018, 29 pages incl. references), fetched 2026-11-19. Kind of copy
    (step 5): arXiv preprint, the authors' own upload (Santa Fe Institute
    working paper). No obstacle. Text extracted with pdftotext (reading
    order) to dl/text.txt, and with -layout to dl/text_layout.txt; the
    extraction drops the ε glyph (e.g. "S = (x)" for S = ε(x)). Read:
    abstract; §I introduction; §II background (temporal causal states,
    lightcones, local causal states, causal filtering, cellular automata,
    automata-theoretic evolution); §III in full (domains from broken
    symmetry, DPID, local causal state domains, coherent structures as
    domain deviations, with both Definitions); §IV.A–B classification and
    ECA 110; §IV.C ECA 18 domain and α particles; §V Discussion; §VI
    Conclusions. Skimmed: §IV.B ECA 54 particle and interaction details
    (Figs. 3–6). Figures not inspected as images.
date: '2026-11-19'
---

# NOTE-tmpqwurm: Rupe and Crutchfield 2018 — Local Causal States and Discrete Coherent Structures

## Contribution

Rupe and Crutchfield (arXiv 1801.00515, 2018) define coherent structures in fully discrete spatiotemporal systems using local causal states. Two past lightcones are equivalent when they give the same distribution over future lightcones. Labelling every spacetime point by its class ("causal filtering") gives a local causal state field. Domains are regions where that field is invariant under a group of space and time shifts, and coherent structures are spatially localized, temporally persistent deviations from domains, "locally broken domain symmetries". They illustrate this on elementary cellular automata (ECAs 54, 110 and 18) and compare it with the earlier domain-particle-interaction decomposition (DPID). Domains agree exactly, and structures agree "to a large extent". The method uses only the generated fields, not the equations of motion.

## Key results

- **Local causal equivalence** (§II.B, Eq. 3, p. 5): "Two past lightcones are causally equivalent if they have the same distribution over future lightcones". The local causal states are "minimal sufficient statistics for optimal local prediction" (p. 5).
- **Not interventional** (§II.B, p. 5): "local causal states do not detect direct causal relationships—say, as reflected in learning equations of motion from data. Rather, they exploit an intrinsic causality in the system in order to discover emergent spacetime structures."
- **Domains as symmetry groups over the state field** (§III.A, Definition, p. 11): a pure domain field is one on whose state field the time shift and the spatial shifts "form a symmetry group."
- **Coherent structures** (§III.B, Definition, p. 12): "A coherent structure Γ is a contiguous nondomain region" with spatial locality and "Lagrangian temporal persistence" within the depth-1 future lightcone.
- **Hidden symmetries** (§III, p. 12): a hidden symmetry domain is one where the shifts that form a group over the state field "do not generate a symmetry group over xΛ". ECA 18's domain shows its 0-wildcard symmetry only in the state field (§IV.C, p. 20).
- **Agreement with DPID** (§IV.B, p. 18): for ECA 54's domain "The two descriptions agree completely"; for its particles, "the agreement is not exact as with the domain, DPID and the local causal states still agree to a large extent".
- **Limits in stochastic domains** (§IV.C, p. 20): "filtering out domain states leaves behind more than the structures. Why exactly this happens is the subject of future work." A further hand-applied coherent-structure filter is needed (p. 21).
- **What coherent structures are not** (§III.A.1, p. 8): a global symmetry change gives a new domain, "not the formation of coherent structures. Coherent structures, such as topological defects [37, 97], form at higher Rayleigh numbers when the discrete cellular symmetries are locally broken."

## Assumptions

- Fully discrete, spatially homogeneous systems with a finite speed of information propagation, so that lightcones are defined. Lightcone horizons are finite in practice (h− = h+ = 3, or h− = 8 for ECA 18).
- Conditional stationarity of lightcones, and enough data to estimate the predictive distributions.
- Domains are identified by exact group symmetries of the state field. Structures are defined relative to those domains.

## Concepts

- **Past and future lightcones** L−, L+ (Eqs. 1–2).
- **Local causal state; local ε-function; causal filtering**: S = ε(x), a "semantic field" of labels, not measurements.
- **Domain** (explicit or hidden symmetry): a region of the state field tiled under space–time shifts; temporal period p, spatial period s, recurrence time p̂.
- **Coherent structure**: a localized, persistent, nondomain region, "locally broken domain symmetries" (p. 23).
- **DPID**: Crutchfield and Hanson's domain-particle-interaction decomposition, built from finite-state transducers of domain languages.

## Bearing on the record

- **TERM-062** — supports, and extends. This is TERM-062's causal-state relation with the source of pasts set to past lightcones and the target to future lightcones at each spacetime point. It keeps the TERM's point that the states are not interventional in the authors' own words: the states "do not detect direct causal relationships". A note on TERM-062 could name the local form as a further choice of source and target. Not held before.
- **QUESTION-tmpcb0bf** — supports the question's premise that the criteria can come apart, and sharpens the predictive criterion. A local causal-state coherent structure is defined relative to a domain's symmetry group over the state field, not the raw field (hidden symmetry domains). Topological defects count as coherent structures only when a discrete symmetry is locally broken. The paper also records that its structures and DPID's disagree at the edges (acausal growth faster than the light speed, p. 21), so two predictive criteria already differ. It offers no interventional test.
- **QUESTION-tmpex36a, CLAIM-tmpj540o, THEORY-1065, THEORY-1059, CASE-tmpsjjgx** — no direct bearing.

## Limitations

- Shown only on one-dimensional elementary cellular automata, deterministic and binary. Real-valued or learned fields such as a recurrent network's hidden state are not treated, and inference cost is flagged ("under a caveat of computational resource scaling", p. 23).
- For stochastic domains the unsupervised filter over-detects, and a hand-applied coherent-structure filter is used. Details are deferred to a sequel.
- Agreement with DPID is shown by examples and visual comparison, not by a quantitative score.
- Domains require exact symmetry groups over the state field. The paper gives no tolerance for approximately periodic domains.
