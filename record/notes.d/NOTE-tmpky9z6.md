---
status: Read
paper: LIT-tmpe6100
title: 'Efficient compression in color naming'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the PubMed Central copy (PMC6077716), the HTML page, as
    the PNAS PDF returned 403 and PMC withholds the XML at the publisher's
    request. Read: Significance, abstract, the introduction, "Communication
    Model", "Bounds on Semantic Efficiency", "Predictions", "Results",
    "Discussion", "Materials and Methods", all figure legends, Table 1 and
    the 29 references. Figures were known only from their legends. Not
    read: the SI Appendix (derivation of the Bayesian listener, the IB/RDT
    relation, the LI source, the RKK+ model, the rotation controls,
    per-language results) and Movies S1–S2. Equations 1–9 were followed;
    the identity E[D(M‖M̂)] = I(M;U) − I(W;U) (Eq. 5) was checked by hand
    from Eq. 1, not taken on trust.
date: '2026-10-09'
summary: >-
  Casts a colour lexicon as an information-bottleneck encoder from
  perceptual meanings to words and shows the World Color Survey languages
  and English lie near the IB bound at β ≈ 1.03, beating hue-rotated
  variants of themselves in 93% of cases and fitting full naming
  distributions much better than a deterministic efficiency model; IB
  optima are soft, and the path of optima through β has phase transitions
  that roughly follow Berlin and Kay's sequence.
---
<!-- inactive-ok-file: THEORY-155 THEORY-tmp64mn6 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# NOTE-tmpky9z6: Efficient compression in color naming

## Contribution

Earlier efficiency accounts of colour naming (Regier, Kay and Khetarpal
2007; Regier, Kemp and Kay 2015, "RKK") found that theoretically efficient
hard partitions of colour space resemble attested systems. This paper
replaces the hard partition with a stochastic encoder and the ad hoc
efficiency score with the information bottleneck, and so can test full
naming distributions, not only modal maps. It shows that attested systems
are near the IB bound, that one parameter places them along it, and that
soft boundaries and inconsistent naming are features of efficient systems
rather than departures from efficiency.

## Key insight

When meanings are themselves distributions over the world, the natural
distortion between intended and reconstructed meaning is KL divergence,
and then rate–distortion becomes the information bottleneck: the cost of a
lexicon is how many bits of the speaker's meaning it carries, I(M;W), and
its value is how many bits about the world the listener gets, I(W;U).
Languages differ mainly in where they sit on that one curve.

## Assumptions

- **Meaning space.** U is the set of 330 WCS chips in CIELAB; each chip c
  has one meaning m_c(u) ∝ exp(−‖u − c‖²/(2σ²)) with σ² = 64. The only
  domain-specific ingredient, by the authors' account.
- **One source for all languages.** p(m) is shared across languages. The
  main analyses use a "least informative" (LI) prior built per language
  from its naming data (maximize the entropy of c while minimizing expected
  surprisal of c given w) and averaged; a uniform source is the baseline.
- **Noiseless channel, optimal listener.** Only the encoder is scored; the
  decoder is the Bayesian listener of Eq. 1, m̂_w(u) = Σ_m q(m|w) m(u).
- **A representative speaker per language,** obtained by averaging naming
  responses; 15 WCS languages with fewer than five responses per chip are
  excluded from the LI source and the evaluation.
- **IB optimization** is non-convex: K = 330, reverse deterministic
  annealing, local optima only guaranteed.

## Key results

- **Eq. 5.** E_q[D(M‖M̂)] = I(M;U) − I_q(W;U), so minimizing expected KL
  distortion is maximizing I(W;U).
- **Eq. 6.** The objective F_β[q] = I_q(M;W) − β I_q(W;U), β ≥ 1; the IB
  curve is the set of its minimizers over β and bounds every language's
  attainable complexity–accuracy pair.
- **Eq. 7.** The optima satisfy q_β(w|m) ∝ q_β(w) exp(−β D[m‖m̂_w]), hence
  soft categories for finite β.
- **Fit.** β_l is the β minimizing ΔF_β = F_β[q_l] − F*_β; efficiency loss
  ε_l = ΔF_{β_l}/β_l.
- **Table 1** (five-fold cross-validation, means ± SD over held-out
  languages). LI source, IB: ε 0.18 (±0.07), gNID 0.18 (±0.10), NID 0.31
  (±0.07), β 1.03 (±0.01). LI source, RKK+: ε 0.70, gNID 0.47, NID 0.32.
  Uniform source, IB: ε 0.24, gNID 0.39, NID 0.56, β 1.06. Uniform, RKK+:
  ε 0.95, gNID 0.65, NID 0.50.
- **Rotation control.** For each language, 39 hue-rotated variants: 93%
  of languages beat all of theirs; the rest beat most.
- **Phase transitions.** Annealing β gives a hierarchy of categories with
  bifurcations (Fig. 5). Culina sits just after a green category appears,
  dominated so that it does not show on the mode map; Agarabi and Dyimini
  after blue appears, with Dyimini's blue more established; low agreement
  around blue is predicted for 1.026 ≤ β ≤ 1.033. English sits at a
  relatively complex point; its pink appears later in IB than in English.
- **The yellow discrepancy.** IB's first categories include a dominant
  yellow; low-complexity WCS languages have black, white and red without
  it. The authors tie it to yellow's prominence in the irregular CIELAB
  layout of the stimulus set.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Attested colour-naming systems are near the IB complexity–accuracy bound | moderate | Fig. 3, Table 1; rests on the LI source estimated from the same naming data, cross-validated over languages |
| C2 | Their nearness to the bound is specific to them, not a property of any plausible naming system | moderate | rotation control (93% beat all 39 variants); rotation is one family of alternatives only |
| C3 | Small differences in one parameter β account for much of the cross-language variation | moderate | β_l in a narrow band, Fig. 4 comparisons; per-language fit of β |
| C4 | Soft boundaries and inconsistently named regions are efficient under IB | strong (derivation) | Eq. 7 for finite β; the empirical match is visual (Fig. 4) and by gNID |
| C5 | The IB annealing path recapitulates Berlin and Kay's sequence and accounts for continuous change between stages | weak | Fig. 5 and Movie S1 (not read); yellow is a stated exception; no historical data are modelled |
| C6 | IB fits full naming distributions better than the RKK efficiency model; on mode maps they tie | strong | Table 1 (gNID vs NID) |

## Concepts

- **meaning**: a distribution m(u) over states of the environment, the
  speaker's belief; here a Gaussian over colours.
- **cognitive source**: p(m), how often each meaning needs to be
  communicated.
- **encoder / naming policy**: q(w|m); a language, for the purposes of
  the paper.
- **complexity**: I_q(M;W), bits of the meaning carried by the word.
- **accuracy / informativeness**: I_q(W;U).
- **LI source**: the need distribution built from least informative
  priors per language, averaged.
- **gNID**: 1 − I(W₁;W₂)/max{I(W₁;W₁′), I(W₂;W₂′)}, a generalization of
  normalized information distance to soft partitions.
- **relative accuracy of a word**: D[m̂_w‖m₀] − I_q(W;U).

## Connections

The objective is Tishby, Pereira and Bialek's ([LIT-338](../literature.d/LIT-338.md)), with KL
distortion justified after Harremoës and Tishby; the authors place it
inside rate–distortion (Shannon 1959) and distinguish their compression
view from channel-capacity views of language (Levy and Jaeger; Piantadosi
et al.; Plotkin and Nowak). The empirical base is the World Color Survey
and Lindsey and Brown's English data. The deterministic baseline is RKK;
the evolutionary contrast is Berlin and Kay (discrete stages) against
MacLaury and Levinson (gradual emergence). Deterministic annealing is
Rose's.

## Bearing on the record

- **[LIT-338](../literature.d/LIT-338.md).** The record's reading of the IB paper ([NOTE-300](NOTE-300.md)) found its
  phase-transition claim cited out, not shown. Here the bifurcations of
  the optimal encoder as β grows are computed and plotted for a real
  meaning space (Fig. 5), though the analysis is in the SI, unread.
- **[THEORY-155](../theory.d/THEORY-155.md) and [LIT-769](../literature.d/LIT-769.md).** Griffiths and Kalish say where Bayesian
  transmission takes a language (to the prior); this paper says where
  efficient systems lie. It gives no transmission model, so it neither
  supports nor conflicts with [THEORY-155](../theory.d/THEORY-155.md); its "evolution" is a path
  through optima, not a dynamics.
- **Produces [THEORY-tmp64mn6](../theory.d/THEORY-tmp64mn6.md)**, stating C1–C3 with the fitted-source
  caveat.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- The need distribution is estimated from the naming data the model is
  scored on; cross-validation over languages guards the evaluation but the
  source is still shaped by the systems it explains. Under the uniform
  source the fit is clearly worse (gNID 0.39).
- One shared source for all languages, though the authors note
  communicative needs may differ by culture.
- The perceptual model is fixed (CIELAB, one σ), and the stimulus set's
  irregular layout in CIELAB is a candidate cause of the yellow miss.
- The control set is hue rotations only; it does not test other
  structured alternatives.
- β_l is fitted per language, so "near the bound" is near the bound at the
  most favourable β.
- The evolutionary reading is a reading of the optimal path, not a model
  fitted to historical change.

## Open questions

- Does the near-optimality survive a need distribution measured
  independently of naming, e.g. from usage? The SI's image-statistics
  source is said to do worse; it was not read.
- Does the same analysis hold in other semantic domains (the authors'
  stated next step)?
- Is there a transmission process whose stationary states lie on the IB
  curve, joining this to iterated learning?
