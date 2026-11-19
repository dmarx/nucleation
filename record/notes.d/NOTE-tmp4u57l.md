---
status: Read
paper: LIT-tmp19eqc
title: 'Masumori and others 2026 — Structured Fluctuations and the Information Dynamics of Self-Maintenance in Growing Neural Cellular Automata'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    What was read is the authors' arXiv preprint, the submitted version of
    the Entropy article, not the version of record. URLs tried, 2026-11-19:
    - https://www.mdpi.com/1099-4300/28/8/893 (publisher, open access): HTTP
    403 "Access Denied". Stopped at that host; not retried. - Europe PMC
    REST search (https://www.ebi.ac.uk/europepmc/webservices/rest/search?que
    ry=DOI:10.3390/e28080893): found PMID 42649688, PMCID PMC13512756, open
    access. -
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13512756/fullTextXML
    (ADR-101 route): HTTP 503 "Service Temporarily Unavailable", twice. Not
    pursued further. - OpenAlex (api.openalex.org, no email sent) listed an
    arXiv location. URL read: https://arxiv.org/pdf/2607.12403 (HTTP 200,
    PDF, 31 pages; arXiv v1, 14 Jul 2026, cs.NE). OpenAlex labels it
    "submittedVersion". Kind of copy (step 5): arXiv, the authors' own
    preprint of the article. Lawful. The Entropy version of record (MDPI,
    gold OA) and the PMC copy were located but not read; differences between
    them and the preprint are unknown. Read: abstract, §1-§9 in full
    (Methods, structured fluctuations, fluctuation cores, attracting
    recurrent state, nonlocal damage response and the suppression
    experiment, transfer entropy, ΦID and PID, Discussion, Limitations,
    Conclusions), Appendix A.1. Skipped: the rest of Appendix A (formal
    definitions of TE, ΦID, PID), Appendix B (additional morphologies,
    discretization robustness), the reference list. Text extracted with
    pdftotext -layout to dl/text.txt.
date: '2026-11-19'
---
<!-- inactive-ok-file: ADR-101 CLAIM-672 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp4u57l: Masumori and others 2026 — Structured Fluctuations and the Information Dynamics of Self-Maintenance in Growing Neural Cellular Automata

## Contribution

Masumori, Sato and Ikegami (Entropy 28(8):893, 2026; read as arXiv 2607.12403v1, the submitted version) take a growing neural cellular automaton trained with damage, as in Mordvintsev et al. ([LIT-tmp5gwuj](../literature.d/LIT-tmp5gwuj.md)), and study its dynamics after the lizard has formed. They find that the hidden channels never settle: cells keep fluctuating, the fluctuations are spatially correlated and concentrated in a few channel-invariant "fluctuation cores" near the shape's boundaries and protrusions, and the whole system moves on a recurrent attracting state rather than at a fixed point. Damage displaces it in state space and it returns over hundreds of steps. Blocking small updates outside a radius around the damage impairs repair until that radius covers about 74% of the cells. Transfer entropy, ΦID and PID describe how predictive structure is arranged at rest and during repair. The authors' reading is "precarious self-maintenance": persistence depends on the ongoing activity of the system's own dynamics.

## Key results

- §3.1, Fig. 2A: fluctuations persist when every cell updates at every step: "even at UR = 1.0, where every cell is updated at every step and stochastic update-induced variability is absent, substantial fluctuations persist."
- §4, Fig. 4: "temporal fluctuations were concentrated in a small number of localized regions that appeared at similar spatial locations across channels", called "fluctuation cores", which "tended to emerge near morphological boundaries and protrusions."
- §4, Fig. 5: per-cell vulnerability to perturbation "was more strongly associated with mean state magnitude (r = 0.639) than with temporal fluctuation (r = 0.325)".
- §5: "the system does not converge to a fixed point but continuously traverses a structured region of state space"; under periodic damage, "Each damage event caused the system state to jump to a remote region of the latent space", followed by "a gradual return toward the original attracting state region, with the recovery path extending over hundreds of time steps."
- §6.2, Fig. 10: with updates of magnitude 0.01 or less blocked outside a permissive radius, "Recovery quality was significantly impaired for permissive radii up to r = 13 pixels, with significance vanishing at r = 14"; "A permissive zone of radius 14 encompasses approximately 74% of all alive cells".
- §7.1: at rest, "the regions of elevated TE magnitude tended to overlap with the fluctuation cores identified in §4", with outward flow from them; after damage, inward flow near the damage site and outward flow beyond. The authors' caveat: "these pairwise TE estimates should be read as directed predictive asymmetries rather than as direct causal transmission".
- §7.2-7.3: across channel pairs synergy dominates and redundancy is "an order of magnitude smaller"; in spatial PID, "Redundancy increased substantially, while both unique information and synergy decreased relative to the resting baseline" during recovery.
- §8: "maintenance and repair are not separate mechanisms but two expressions of the same precarious organization."
- §8: the authors suggest "Damage-inclusive training would then serve to widen the basin of attraction rather than to create recovery capacity de novo."

## Assumptions

- One architecture and training regime (Mordvintsev et al.'s, with damage), mainly the lizard target; eight seeds; default update rate 0.8 rather than the original 0.5.
- Damage is zeroing a circle of radius 5; recovery is measured by RGB error in the damage region and cosine distance from a baseline.
- Information quantities use 8-bin quantile discretization and history length 1; they are offered as descriptions, "rather than as evidence of direct causal transmission".
- The fluctuation-suppression intervention uses a fixed magnitude threshold (0.01) chosen from the resting activity distribution.

## Concepts

- Fluctuation cores: localized, channel-invariant regions of sustained micro-variability.
- Attracting recurrent state: persistence as continued movement within a region of state space, not a fixed point; repair as return to it.
- Precarious self-maintenance (after Di Paolo): an organization that persists only through ongoing activity of its own constitutive processes.
- Homeochaos (Kaneko and Ikegami): stability through weak high-dimensional chaos; coupled map lattices; isologous diversification.
- Transfer-entropy asymmetry fields; ΦID and PID atoms (synergy, unique information, redundancy).

## Bearing on the record

- [CLAIM-566](../claims.d/CLAIM-566.md): qualifies. In this system persistence is not passive: the formed pattern is kept by continuous, distributed activity, and the authors argue that maintenance and repair are "two expressions of the same precarious organization", which suggests that over any horizon the probability of persisting and of regenerating after damage are not independent here. That matches the claim's own limit, that they converge where persistence needs ongoing regeneration, with damage standing in for turnover. The constraints that do the regenerating (rule, alive mask) are still fixed from outside, so precariousness here is not closure in [TERM-070](../terms.d/TERM-070.md)'s sense.
- [CLAIM-672](../claims.d/CLAIM-672.md): qualifies. The trained lizard is kept neither as a fixed point nor by repair only after a strike: the authors find it "continuously traverses a structured region of state space". A fourth mode, persistence as an attracting recurrent state, sits between the claim's fixed point and its self-repair.
- [QUESTION-tmpcb0bf](../questions.d/QUESTION-tmpcb0bf.md): bears on it from outside its setting. Two criteria pick different sites in one learned field: fluctuation cores, which coincide with concentrations of transfer entropy, and per-cell vulnerability to perturbation, which follows mean state magnitude (r = 0.639) more than fluctuation (r = 0.325). The interventional test (suppression of small updates) targets distributed activity, not the cores, so whether the cores are causally operative is left open. No symmetry-related phases or walls are involved.
- [CLAIM-335](../claims.d/CLAIM-335.md): consistent. The authors themselves read their transfer entropy as predictive asymmetry, not causal transmission, and allow for common drivers from overlapping perception neighbourhoods.

## Limitations

- One architecture and training regime; robustness claims are, in the authors' words, "limited to qualitative generality across the tested morphologies".
- The attracting recurrent state is inferred from UMAP and recurrence plots; the authors call it "suggestive rather than a formal dynamical classification".
- The suppression intervention blocks small updates in general, so it cannot separate a role for fluctuation cores from a role for all small updates.
- Information measures depend on discretization and history length.
- Read from the submitted version, not the version of record.
