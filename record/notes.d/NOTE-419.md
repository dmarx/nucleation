---
number: 419
status: Read
formerly:
- NOTE-tmpeo3wn
paper: LIT-515
title: 'Statistical physics of self-replication'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv:1209.1179 v1, 6 Sep 2012, the only arXiv version,
    5 pp., text extracted with PyMuPDF): the whole text, Eqs. (1)–(8), Fig.
    1 and the 20 references. I re-derived Eq. (6) from Eq. (5) and
    recomputed every numerical estimate. The published J. Chem. Phys. text
    (139:121923, 2013) was not seen; the publisher returned HTTP 403, so
    differences between the preprint and the version of record are unknown.
    Crooks (1999), on which the general claim beyond detailed balance rests,
    was taken as stated.
date: '2026-10-02'
summary: >-
  A coarse-grained second law, β⟨ΔQ⟩ + ln π(II→I) + ΔS_int ≥ 0, applied to
  self-replication: the heat a replicator releases per copy is bounded
  below by the log-odds against its copy falling apart within one
  generation, so durable, fast copies cost more heat. The general bound is
  sound. The E. coli and RNA numbers rest on an upper bound on the reverse
  probability that is argued from biology, not derived, and one printed
  logarithm has its argument inverted.
---

<!-- inactive-ok-file: LIT-328 — Deferred: Landauer 1961 is unread; named because the paper compares its bound with it, not leaned on -->
<!-- inactive-ok-file: THEORY-030 THEORY-026 — Proposed; named as the accounts this reading is checked against, not as support -->

# NOTE-419: Statistical physics of self-replication

## Contribution

Before this paper, fluctuation relations had been used for the
thermodynamics of copying informational polymers (Andrieux & Gaspard 2008,
its ref. [13]), where what counts as a copy is fixed by the chemistry. This
paper states the relation for arbitrary coarse-grained ensembles and uses it
to bound the heat of self-replication of a whole organism, with the
replicating "self" supplied by an observer's classification. The bound
links heat to growth rate, internal entropy change and durability. It
gives the first quantitative estimate of how close a bacterium runs to that
bound.

## Key insight

Heat released in a transition between macrostates must pay for how unlikely
the transition is to run backwards. A replicator whose copies are durable
and made quickly runs a transition that is very unlikely to reverse, so it
must release a lot of heat. The cost is set by irreversibility on the
timescale of one generation, not by the information in the copy.

## Assumptions

- **Dynamics.** Stochastic dynamics in a heat bath at fixed temperature,
  with a transition matrix obeying detailed balance, π(j→i)/π(i→j) =
  exp(−βΔQ_{i→j}) (Eq. 2). "By stipulation, there are no external driving
  forces," and the motion is diffusive, "lack[ing] any sense of momentum."
  The text adds that the same form holds for a time-symmetric drive, by
  Crooks's relation, without deriving it here.
- **Ensembles.** I and II are probability densities over microstates fixed
  by an experimental preparation and, in principle, by "repeated
  consultations of a microbiologist." The paper does not compute them.
- **The reverse probability.** The bound needs an upper bound on π(II→I).
  The paper argues one from biology. The most likely route back is one cell
  dividing slightly early and a daughter hydrolysing completely, which is
  more likely than a growing cell pausing for a whole generation (Fig. 1).
  Hence ln π(II→I) ≤ 2 ln p_hyd (Eq. 7), with ln p_hyd ≃ n_pep
  ln[τ_div/(n_pep τ_hyd)] from Poisson statistics. This is a plausibility
  argument about which path dominates, not a bound proved over all paths.
- **Internal entropy.** −ΔS_int ≤ 10 n_pep is set "arbitrarily" and
  "generous[ly]" from two estimates: O₂ to CO₂ (+6 per carbon) and amino
  acid confinement (about −12 per residue).

## Key results

- **Eq. (6), the general bound.** From ⟨exp(−βΔQ − ln π(II→I) − ln
  p(j|II) + ln p(i|I))⟩ = 1 (Eq. 5) and Jensen's inequality (the text says
  "e^x ≥ 1 + x"), β⟨ΔQ⟩ + ln π(II→I) + ΔS_int ≥ 0. Since π ≤ 1 it implies
  ⟨ΔS_tot⟩ ≥ 0. I re-derived it from Eqs. (2)–(5); given the definitions
  it is correct. The paper calls it "simply a precise statement of the
  Second Law" and "closely related to the well-known Landauer bound".
- **Eq. (8), the replication bound.** β⟨Q⟩ ≥ 2n_pep ln[(n_pep τ_hyd)/τ_div]
  − ΔS_int.
- **E. coli.** With n_pep = 1.6×10⁹, τ_div = 20 min and τ_hyd = 600 years,
  2n_pep ln[(n_pep τ_hyd)/τ_div] ≈ 75 n_pep ≈ 1.2×10¹¹. I recomputed this:
  n_pep τ_hyd/τ_div ≈ 2.5×10¹⁶, whose log is 37.8, so 75.6 n_pep. The
  measured heat is 220 n_pep (Rothbaum & Stone 1961). The ratio 220/75 ≈
  2.9 is the paper's "less than three times as large as the absolute
  physical lower bound".
- **RNA and DNA.** For a ligase-type self-replicating RNA (Lincoln & Joyce
  2009) with a 1-hour doubling time and a 4-year half-life, ⟨Q⟩ ≥ RT
  ln[(4 years)/(1 hour)] = "7 kcal mol⁻¹", against a reaction enthalpy near
  10 kcal/mol. For DNA (half-life 3×10⁷ years), "16 kcal mol⁻¹", which
  exceeds the enthalpy and is "prohibited thermodynamically". I recomputed
  them: ln(35,064) = 10.5, so 6.2–6.5 kcal/mol at 298–310 K; ln(2.6×10¹¹)
  = 26.3, so 15.6–16.2 kcal/mol. The DNA figure checks; the RNA figure is
  rounded up by about 0.5–0.8 kcal/mol, which does not change the
  conclusion.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For detailed-balance dynamics, heat released in a macrostate transition is bounded below by the log-odds against reversal minus the internal entropy change | strong | Eqs. (2)–(6); a correct coarse-grained second law |
| C2 | The same bound holds for time-symmetrically driven systems | moderate | asserted via Crooks [3], not derived here |
| C3 | Replication heat is bounded by 2n ln(n τ_hyd/τ_div) − ΔS_int | moderate | Eq. (8); depends on the argued bound Eq. (7) on the reverse probability |
| C4 | E. coli releases less than three times the minimum heat its growth rate, entropy change and durability allow | moderate | the arithmetic checks (220/75.6); the 75 n_pep rests on C3, and the paper says the reverse probability is deliberately overestimated, which would raise the bound and tighten the ratio |
| C5 | A DNA replicator of the RNA's speed would be thermodynamically forbidden, favouring RNA first | weak | one comparison with assumed enthalpy and half-lives; the linear-in-ℓ extrapolation is stated, not computed |
| C6 | "Self-replication" exists only relative to an observer's classification of microstates | assertion | a framing argument (pp. 1, 4), not a result; the bound needs some coarse-graining but works for any one |

## Concepts

- **Coarse-grained ensemble.** A probability density over microstates fixed
  by a macroscopic preparation or classification, I or II. No order
  parameter is needed.
- **Reverse probability π(II→I).** The probability of returning to
  ensemble I within the same time, starting from II.
- **Durability.** The decay time of the copy (τ_hyd for peptide bonds, the
  RNA or DNA backbone half-life). It enters the bound through
  ln(τ/τ_div).

## Connections

- **Andrieux & Gaspard (2008), ref. [13].** The paper's own lineage for the
  thermodynamics of copying, where the information content of a template
  could "more easily be taken for granted". Not held in the record.
- **Crooks (1999), ref. [3].** The fluctuation relation the general claim
  rests on. It is being filed in parallel in this batch with the record's
  other fluctuation-theorem work.
- **Landauer, [LIT-328](../literature.d/LIT-328.md) (Deferred).** Cited by the paper as closely related.
  The record's account of what Landauer prices is [THEORY-030](../theory.d/THEORY-030.md), from Bennett
  ([LIT-360](../literature.d/LIT-360.md)): only logically irreversible steps, and copying onto a blank
  register costs nothing. England's bound is consistent with that. Its
  cost comes from making a durable copy in finite time, and it falls away
  as τ_div grows, as Bennett's reversible-copying limit requires.
- **Still et al., [LIT-327](../literature.d/LIT-327.md) ([NOTE-295](NOTE-295.md)).** Another second-law bound read as an
  information cost, and [THEORY-026](../theory.d/THEORY-026.md)'s source. Still bounds work dissipated
  by a system with fixed kernel, driven without feedback, by its
  nonpredictive memory. England's system is undriven and his quantity is
  macrostate irreversibility. The two are not in tension: neither is per
  operation, and they price different things.
- **Perunov, Marsland & England (2016), [LIT-518](../literature.d/LIT-518.md).** The sequel, which
  starts from the same macrostate relation, adds a drive and drops
  replication.

## Bearing on the record

- **[THEORY-030](../theory.d/THEORY-030.md) (Proposed): consistent, and a useful check.** The paper says
  its bound is "closely related to the well-known Landauer bound". On the
  record's reading of Landauer's scope, the heat England prices is not a
  cost of copying information. It is the cost of irreversibility at a
  finite rate, and it vanishes in the slow limit. A reader who took
  England as evidence that replication has an intrinsic per-bit cost would
  be making the mistake [THEORY-030](../theory.d/THEORY-030.md)'s "What this does not say" warns
  against.
- **[THEORY-026](../theory.d/THEORY-026.md) (Proposed): no direct bearing.** England's system is
  undriven and has no memory variable.
- **[LIT-192](../literature.d/LIT-192.md) and the demarcation question.** The paper is explicitly
  deflationary: it supplies no physical mark of a living replicator, and
  locates "self" in the observer's coarse-graining (C6).
- **No ML instruction.** Nothing here belongs in the anthology.
- **No new THEORY is indicated** from this paper alone.

## Limitations

- The reverse-probability bound (Eq. 7) is a biological argument about
  which path dominates. The paper claims it as an upper bound ("we can
  claim that"), but no proof covers all paths back to I.
- The internal entropy bound is set "arbitrarily".
- One organism and one RNA system are worked. The claim that the approach
  "applies equally" wherever a stochastic population model exists is not
  tested.
- The driven case is asserted by citation only.

## Open questions

- A computed, not argued, bound on π(II→I) for a real replicator, which
  would turn C4 into a measurement.
- Whether the factor of three for E. coli is set by adaptability, as the
  author suggests ("not perfectly optimized for any given" environment), or
  by the deliberately loose reverse probability.

## Corrections

- none to a seeded skim (there was no seed)
- **An inverted logarithm.** The text gives "2n_pep ln[τ_div/(n_pep
  τ_hyd)] = 1.2×10¹¹ ≃ 75n_pep". That logarithm is negative (about −37.8
  per bond). The positive value belongs to ln[(n_pep τ_hyd)/τ_div], as in
  Eq. (8). This is a sign slip in the prose, not in the bound.
- **The RNA figure is rounded up.** RT ln(4 years/1 hour) is 6.2–6.5
  kcal/mol at 298–310 K, not 7.
