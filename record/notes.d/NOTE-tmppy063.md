---
status: Read
paper: 'LIT-tmp1pdwj'
title: 'Winfree and Bekbolatov — Proofreading tile sets'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the authors' submitted preprint,
    proofreading_DNA9_preprint.pdf, 19 pages, in CaltechAUTHORS
    (https://authors.library.caltech.edu/records/jcvj4-7gn26), which labels
    it "Submitted"; it carries the published abstract but is not the
    Springer version of record, so wording may differ slightly. Text
    extracted by pdftotext. Read in full: §§1–5, every footnote, the
    captions of Figs. 1–10 and the reference list. Figure contents
    (simulation snapshots and plots) were seen only through captions and
    axis labels. Not read: the supplementary simulation code on
    dna.caltech.edu, whose TLS verification failed. The preprint has no
    page numbers; places below are sections, figures and footnotes.
date: '2026-11-05'
summary: >-
  In kTAM simulation and kinetic-trap theory, direct tile sets err because
  a mismatched tile is covered before it can leave, giving r ≈ βε². A K×K
  block with unique internal labels keeps the logical (aTAM) assembly,
  scaled by K, but makes any single mismatch a dead end, so growth stalls
  until it dissociates: 2×2 gives r ≈ βε and errors 1% → 0.01% at fixed
  conditions; 3×3 only 0.001%, short of the predicted exponential gain,
  because growth on facets is not corrected. Proofreading tiles heal
  punctures, with less scar tissue than direct ones.
---
<!-- inactive-ok-file: THEORY-tmpxgxmn THEORY-1398 THEORY-tmpz96qc CLAIM-567 CLAIM-583 CLAIM-571 CLAIM-591 CLAIM-569 CLAIM-566 CLAIM-184 CLAIM-478 CLAIM-tmpiyvk1 TERM-tmp3awsy — Proposed or new; cited from the reading of Winfree and Bekbolatov (2004) as open -->

# NOTE-tmppy063: Winfree and Bekbolatov — Proofreading tile sets

## Contribution

The first redesign of a tile set that corrects growth errors by
cooperativity at the level of blocks, with no change to the molecular
implementation; a thermodynamic argument that the error rate should fall
exponentially in the block size K at fixed conditions; absorbing-Markov-chain
models of kinetic trapping that predict the simulated error rates; and a
frank report of where the method fails (facets, strength-2 tile sets, no
proof).

## Key insight

An error in growing crystals is a race between two time scales: a
mismatched tile leaving (rate r_r,1) and its being covered by further growth
(r* ≈ αr). The direct tile set loses the race too often. A proofreading
block changes no rate. It changes where the paths lead: past a mismatch
there is no compatible continuation without a second error, so the front
stalls, and the stall gives the bad tile time to fall off. "The final
assembly therefore has no record of the mishap having occurred" (§3).

## Assumptions

- **The kTAM.** Tiles attach at r_f = k_f e^{-Gmc} and detach at
  r_r,b = k_f e^{-b Gse}; threshold τ = 2; detailed balance; all weak sticky
  ends equally strong; tiles cannot rotate.
- **Single-tile moves only.** Dimers and fractures are rare near melting
  (footnote 3); tests that allowed them changed results only minorly.
- **Monomer concentration held fixed**, an idealized steady supply;
  footnote 4 notes that depletion and annealing break it.
- **Trap models** make freezing by coverage irreversible at a fitted rate
  r*, though the kTAM itself is reversible.
- **No experiment.** The authors are exploring the tile set experimentally
  but report none.

## Key results

- **Baseline trade-off (§2, Fig. 5).** All points lie above r ≈ βε², with
  β ≈ 10⁴ /M/sec: "decreasing error rates by a factor of 10 entails slowing
  down the self-assembly process by a factor of 100", against digital fault
  tolerance's "logarithmic, rather than quadratic, slow-down".
- **Equilibrium error is concentration-free (§2).** ε ≈ 2N e^{-Gse}: "It is
  mildly surprising that Gmc has no effect on the equilibrium error rates."
  But "equilibrium is seldom achieved far below the melting transition".
- **Kinetic trapping (§2, Fig. 3b).** Tiles "that associate with a mismatch
  on the growth front don’t have time to dissociate, and are frozen in place
  by further growth". The error rate is a committor, "the probability that,
  starting in E, the system reaches F M", fitted with r* = αr, α = 1.5.
- **Phase diagram (§2, Fig. 3a).** No growth when Gmc > 2Gse; algorithmic
  growth when 2Gse > Gmc > Gse; "essentially random aggregation" when
  Gse > Gmc. The best trade-off lies just below melting, Gmc ≈ 2Gse.
- **Errors propagate (Fig. 4a).** "Subsequent error-free growth correctly
  propagates the erroneous information."
- **The block's mechanism (§3, Fig. 6d).** "The assembly process stalls,
  giving time for the initial mismatched tile to fall off and be replaced by
  a correct tile." Errors are "co-localized in pairs", squaring the error
  rate. The aTAM assembly "proceeds according to the same logic as the
  original tile set".
- **Path structure (§3, Fig. 7).** The correct block forms "via a series of
  four favorable steps", while "every path to a mismatch contains at least
  two significantly unfavorable steps". The 29-state model's freezing rate
  r* = αre^{γε} is fitted with γ = 12: "We have no strong justification for
  this formula" (footnote 9).
- **Exponential in theory (§3).** The block error needs at least K
  mismatched tiles, so ε ≈ e^{-KGse} and r ≈ βε^{2/K}; "Tile errors are now
  clearly not iid" (footnote 10).
- **Not in practice (§3, Fig. 5).** 2×2 gives r ≈ βε^1.0 and 3×3 r ≈ βε^0.89
  against a predicted ε^{2/3}: "the simulation results for K = 3 (figure 5)
  and K = 4 (data not shown) fall short of the prediction". At the same
  conditions, 1% (1×1), 0.01% (2×2), 0.001% (3×3).
- **The uncorrected mechanism (§3, Fig. 8a).** Proofreading does nothing
  about "spontaneous growth on a facet", facets of length n appear with
  frequency about 2^{-n}, "making facet growth errors rare but unavoidable.
  Some other error-correcting strategy will be necessary".
- **Cooperativity must be internal (footnote 11).** With a pre-assembled
  block "the melting temperature would occur at Gmc ≈ 2KGse", giving back
  r ≈ βε².
- **Speed (§2).** "for target error rates of 10−4 , the 2 × 2 proofreading
  tiles result in a 104 -fold speed-up".
- **Costs (§5, Fig. 10).** K²N² rule tiles, (2K − 1)N² + (K − 1)²N with
  sharing; for the Sierpinski set, 6 DNA rule tiles become 9; the pattern is
  scaled K-fold.
- **Squares (§4, Fig. 8b), 31 trials each.** Original 26×26 never formed
  properly; improved 49×49 65%, 99×99 26%; 2×2 proofreading 98×98 87%. The
  benefit is "disappointingly modest", since "alternative error mechanisms
  are dominant".
- **Healing (§4, Fig. 9).** "Proofreading tile sets are often able to heal a
  puncture in the crystal", sometimes leaving "scar tissue"; direct tiles
  leave it very often, proofreading tiles much less.
- **Nucleation (footnote 5, §5).** Spurious nucleation of rule tiles is held
  off because "there is a critical nucleus size"; nucleation of boundaries
  is "a major remaining issue".
- **Open (§5).** "the rigorous proof of their robustness in the kTAM remains
  an open problem"; robustness to implementation errors "has not yet been
  investigated".

## Concepts

- **kTAM / aTAM**: the kinetic and abstract Tile Assembly Models; the aTAM
  says what assembles, the kTAM how reliably.
- **Gmc, Gse**: monomer concentration and sticky-end strength as free
  energies; Gse is set by temperature. Melting at Gmc = 2Gse.
- **Frozen states FC and FM**: correct and mismatched sites covered by
  growth; the error rate is the committor to FM.
- **Proofreading K×K block**: outer edges carry the original labels,
  internal edges unique ones.
- **Facet roughening**: spontaneous growth on a flat facet, which no block
  design corrects.
- **Scar tissue**: tiles filling a puncture that do not perfectly match.
- **Per-block against per-tile error.**

## Connections

It builds on Winfree's kTAM and blocked cellular automata, and on Schulman
and Winfree for nucleation, and compares itself with von Neumann's
logarithmic-overhead fault tolerance (not held). Among this batch:

- **Local, not global, traps.** The trap here is a mismatched tile covered
  before it leaves; DeLuca et al.'s origami traps (LIT-2081, NOTE-1561,
  THEORY-1398) are global and topological. Shirt-Ediss, Torelli et al.
  (NOTE-tmp6ediz, THEORY-tmpz96qc) and Majikes et al. on the blocked state
  (NOTE-tmpetbc9) are the nearest origami readings on traps and
  cooperativity, with Majikes on designed cooperativity (NOTE-tmppwpd0).
- **Repair from supplied parts.** Scheckenbach et al. (NOTE-tmpmcdju) show
  origami repairing staple damage from a pool, gated by a toehold the damage
  exposes; here the crystal refills a puncture from the monomer pool, gated
  by the same label constraints that correct growth. Neither system makes
  its own parts. Ni et al. (NOTE-tmp79i4g) share the external supply, with a
  cycle that proofreading lacks.
- **Nucleation.** Cumberworth, Frenkel and Reinhardt (NOTE-tmpn2voh) find
  most origami designs have no nucleation barrier; the tile crystal here
  depends on one (footnote 5) to keep rule tiles from nucleating off the
  seed.

## Bearing on the record

- **CLAIM-567 (feasible, reachable, reliably reached): supports.** Original
  and proofreading tile sets reach the same target in the aTAM; in the kTAM
  they reach it with 1% against 0.01% error at the same conditions.
- **CLAIM-583: supports by analogy.** The logical compatibility is kept and
  only the decomposition into tiles changes, but the costs differ (K²
  tiles), so this is not the claim's equal-costs case.
- **CLAIM-571: weakly qualifies.** Escaping a mismatch costs time
  (dissociation against coverage), not a peak of resource.
- **CLAIM-591: qualifies.** The trap models treat coverage of a reversible
  system as an effectively one-way step.
- **CLAIM-569: supports.** Construction cost (K² species, K-fold size) is
  separate from the conditions that hold the crystal and from the time spent
  correcting.
- **CLAIM-566: supports and sharpens.** Corrected assembly, persistence of
  the frozen crystal and refilling after damage are separate behaviours;
  refilling is imperfect and draws on supplied tiles, regeneration of form
  without closure (TERM-070).
- **CLAIM-184: supports, in a clean physical case.** A locked-in error is
  propagated by "Subsequent error-free growth".
- **CLAIM-478: supports.** The error rate is set by the ratio of two time
  scales, and the covered tile becomes a constraint on later growth.
- **CLAIM-520: supports.** Proofreading is worth a 10⁴-fold speed-up where
  errors are in-site mismatches and is "disappointingly modest" where facet
  errors dominate, at a K² tile cost.
- **CLAIM-tmpiyvk1: supports in kind.** The error rate is literally a
  committor; correction works by changing where exits lead (mismatch paths
  need two unfavourable steps), not by lengthening residence.
- **TERM-tmp3awsy, QUESTION-tmp4jbc3: bear on them.** A mismatch is a
  negative architectural effect: it changes the rates of later steps (no
  compatible continuation), not only the state.
- **QUESTION-tmpesr9t: a contrast.** The crystal corrects and refills itself
  but never regenerates its enabling constraints, the tile species and the
  conditions.
- **QUESTION-tmpdbsh1: bears on it.** A covered region persists without the
  growth conditions that made it correct; withdrawing supply is not tested.
- **QUESTION-380: bears on it, slightly**, through footnote 5's critical
  nucleus.
- **THEORY-030 (Landauer): a thermodynamic neighbour.** Correction by
  dissociation erases the record of the error, but no dissipation is
  computed.
- **LIT-919**: the critical-nucleus point of footnote 5.
- Filed: THEORY-tmpxgxmn. No instruction for machine-learning practice.

## Limitations

- Simulation and kinetic-trap theory only; no experiment.
- The trap parameters are fitted with "no strong justification".
- No rigorous proof.
- The exponential gain in K holds only in theory and fails at K = 3 and 4.
- Does not apply to growth on facets, nor to strength-2 tile sets unless
  each tile grows in one direction (Fig. 8c).
- The K-fold spatial scaling loses resolution, except for self-similar
  patterns.
- Robustness to implementation errors (unequal strengths, unequal
  concentrations, depletion) is not examined.
- The text read is the submitted preprint.

## Open questions

- Does an experiment with DNA tiles show the ε² → ε change at K = 2?
- What corrects facet errors? The authors point to other strategies, not
  given here.
- How much does proofreading dissipate per corrected error?
