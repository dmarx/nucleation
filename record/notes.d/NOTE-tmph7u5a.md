---
status: Read
paper: 'LIT-1237'
title: 'Letten, Ke and Fukami — Linking modern coexistence theory and contemporary niche theory'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the published PDF on the last
    author's Stanford publications page
    (https://web.stanford.edu/~fukamit/letten-et-al-2017.pdf, 17 pages,
    Ecological Monographs 87(2): 161–177), text extracted with pdftotext.
    Read: the abstract, all sections, Boxes 1 and 2, the captions of
    Figs. 1–6 and the references. The online Appendices S1–S5 (the full
    derivations for substitutable and essential resources, the parameter
    values and the asymmetric cases) are on the publisher's site and were
    not read; Box 1 summarizes S1 for substitutable resources. Box 1's
    equations were partly garbled in extraction and were read for their
    structure. Checked by hand: that Chesson's ρ = √(α₁₂α₂₁/α₁₁α₂₂) and
    f₂/f₁ = √(α₁₁α₁₂/α₂₂α₂₁) satisfy α₁₂/α₂₂ = ρ f₂/f₁ (eq. 2), that mutual
    invasibility then reads ρ < f₂/f₁ < 1/ρ (eq. 3), and the two limiting
    cases in the text (identical ZNGIs give ρ = f₂/f₁ = 1; identical
    impacts give ρ = 1 with f₂/f₁ = α₁₁/α₂₂). No number was taken from a
    chart.
date: '2026-10-29'
summary: >-
  Translating Tilman's two-consumer, two-resource model into Lotka–Volterra
  coefficients and then into Chesson's niche overlap ρ and fitness ratio,
  the authors find, by worked cases at equilibrium, that shifting the
  resource supply ratio changes only the fitness ratio (equalizing) except
  at extremes where essential-resource competitors become limited by the
  same resource and ρ jumps to 1; that impact-niche overlap moves ρ
  (stabilizing); and that requirement-niche overlap moves both, without
  changing whether the species coexist.
---
<!-- inactive-ok-file: LIT-1219 — Unavailable; Chesson's review is named as the framework this paper translates, nothing here rests on reading it -->
<!-- inactive-ok-file: CLAIM-279 — Proposed; cited as an open claim the reading bears on, nothing here rests on its being settled -->

# NOTE-tmph7u5a: Letten, Ke and Fukami — Linking modern coexistence theory and contemporary niche theory

## Contribution

A synthesis that puts Chesson's phenomenological coexistence terms
(niche overlap and average fitness ratio) and Chase and Leibold's
mechanistic niche terms (supply ratio, impact niche, requirement niche)
into one calculation. The bridge is Tilman's route from a
consumer–resource model to Lotka–Volterra competition coefficients;
Chesson's terms are then computed from those coefficients. The paper
works through how each mechanistic quantity moves each phenomenological
one, and closes with advice on which framework to use when.

## Key insight

Chesson's niche overlap is not a property of a species but of a pair: it
measures how much each species limits itself relative to the other, and
it is blind to overall adaptedness, which goes into the fitness ratio. A
species' impacts on resources mostly feed the first, and where the
supply sits mostly feeds the second; requirements feed both. Identical
requirements make a pair neutral (ρ = 1 and equal fitness) even when
their impacts differ, because any drop in resources hurts both equally.

## Assumptions

- Two consumers, two resources, homogeneous space and time; Tilman's
  (1982) chemostat model with Monod growth, either perfectly
  substitutable or essential resources.
- Parameter regions with positive resource equilibria and without
  alternative stable states (inter- below intraspecific competition).
- Niche overlap and fitness ratio computed at the equilibrium of the
  consumer–resource model, following Chesson (1990) and Chesson and Kuang
  (2008), not from invader growth rates.
- Two-dimensional definitions: impact-niche overlap is the cosine of the
  angle between impact vectors (Pianka's index); requirement-niche
  overlap is the cosine of the angle between ZNGIs (substitutable) or
  between the lines to their corners (essential). The latter is the
  authors' heuristic.

## Key results

- **Eqs. 1–3.** With absolute coefficients, coexistence requires
  α₁₁ > α₂₁ and α₂₂ > α₁₂, which is ρ < f₂/f₁ < 1/ρ.
- **Supply ratio (Fig. 2).** Moving the supply point changes the fitness
  ratio only, through the intraspecific coefficients, so it is
  equalizing. For essential resources, at extreme ratios both species
  become limited by the same resource and ρ jumps to 1; this is a
  destabilizing effect, read as the reduced niche dimensionality that
  Harpole and Tilman (2007) invoke for nitrogen addition.
- **Impact niche (Fig. 5).** Converging impacts raise ρ and leave the
  fitness ratio unchanged when the change is symmetric; asymmetric
  changes can move fitness too (Appendix S3, not read).
- **Requirement niche (Fig. 6).** For substitutable resources, converging
  ZNGIs both lower the fitness difference and raise ρ, and the
  equalizing effect always outweighs the destabilizing one, so
  coexistence is unchanged; at identical ZNGIs ρ = f₂/f₁ = 1. For
  essential resources, converging ZNGIs change neither term while the
  equilibrium point is held fixed, an artefact the authors acknowledge.
- **Data (Box 2).** Rothhaupt's (1988) rotifers on two algae and Tilman's
  (1977) diatoms on phosphate and silicate, re-expressed in Chesson's
  terms, give the same coexistence predictions; the authors note this is
  automatic, since both come from the same parameters.
- **Alternative stable states.** If each species has the greater impact
  on the resource its competitor most needs, the criterion inverts to
  ρ > f₂/f₁ > 1/ρ.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Varying the supply ratio is equalizing, except at extremes for essential resources | moderate | worked cases, Fig. 2; Appendix S1 derivation not read |
| C2 | Varying impact-niche overlap is stabilizing | moderate | Fig. 5 and Box 1's expression for ρ |
| C3 | Varying requirement-niche overlap is both, with no qualitative effect on coexistence | moderate | Fig. 6, substitutable case; essential case held at fixed equilibrium |
| C4 | Identical requirements give neutrality even with different impacts | strong | algebra: α₁₁ = α₂₁, α₂₂ = α₁₂ ⇒ ρ = f₂/f₁ = 1; checked |
| C5 | Phenomenological measurement should come first and guide mechanistic tests | weak | argued from the frameworks' data demands; no study |

## Concepts

- **Niche overlap ρ (Chesson)**: √(α₁₂α₂₁/α₁₁α₂₂); 1 − ρ is the niche
  difference. Pairwise only.
- **Fitness ratio f₂/f₁**: √(α₁₁α₁₂/α₂₂α₂₁); the winner under complete
  overlap.
- **Equalizing / stabilizing**: reducing the fitness difference /
  reducing niche overlap, i.e. increasing negative frequency dependence.
- **Impact niche (Eltonian)**: a species' per-capita effects on its
  environment; here the consumption vector.
- **Requirement niche (Grinnellian/Hutchinsonian)**: the conditions a
  species needs to grow; here the ZNGI.
- **Most limiting resource**: for substitutable resources the one with
  the lower R*, for essential ones the higher; the authors note this runs
  against fig. 2.8 of Chase and Leibold (2003).

## Connections

It builds on Chesson (1990), who first computed niche overlap and fitness
difference from MacArthur's consumer–resource model, and on Kleinhesselink
and Adler (2015) for Tilman's model. Chesson's 2000 review ([LIT-1219](../literature.d/LIT-1219.md), not
reachable) is the source of the stabilizing/equalizing vocabulary. The
paper never invokes an optimization principle; Marsland, Cui and Mehta's
minimum-environmental-perturbation account, which the synthesis set
beside it, is later and not cited.

## Bearing on the record

- **[QUESTION-083](../questions.d/QUESTION-083.md) and the synthesis.** The LIT says the synthesis took this
  paper as the bridge between Chesson's terms and the resource-impact
  vocabulary. The reading supports the bridge, with limits the synthesis
  did not state: the translation is for two species and two resources,
  at a stable equilibrium, with alternative stable states excluded, and
  its generalizations are drawn from worked cases. For many operators
  sharing resources, Chesson's pairwise ρ does not by itself say whether
  a community of more than two coexists.
- **[QUESTION-132](../questions.d/QUESTION-132.md) and [CLAIM-279](../claims.d/CLAIM-279.md).** If the record wants a stabilizing
  mechanism in Chesson's sense, this paper locates it in impacts: an
  operator that limits itself more than others through what it does to a
  shared resource. Divergent requirements alone mostly equalize. That
  bears on whether niche specialization among operators should be read
  as stabilizing.

No instruction for machine-learning practice.

## Limitations

- Two species, two resources; no spatial or temporal variation, which is
  where several of Chesson's best-known mechanisms (the storage effect)
  live; the authors list this as future work.
- The essential-resource requirement result depends on holding the
  equilibrium point fixed.
- Appendices not read, so the general derivations were not checked.
- **Slips.** The text says two empirical studies truncated "negative
  values for ρ (indicating negative stabilization)" to zero; in Chesson's
  convention negative stabilization is ρ > 1, a negative niche
  difference 1 − ρ, not a negative ρ. "Chessons's" for "Chesson's".

## Open questions

- Do the generalizations survive more than two species, and spatial or
  temporal heterogeneity? The authors pose both.
- How do impacts and requirements co-vary in real organisms, which
  decides whether trait change is mostly stabilizing or equalizing?
