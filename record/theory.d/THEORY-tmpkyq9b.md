---
status: Active
title: "Measured as the contrast between a set of explanantia's CohOG+ coherence with the explanandum and with its negation, explanatory power satisfies Roche and Sober's Two Likelihood Inequalities for single hypotheses and fails the One, and in one causal chain and one collider it ranks the richer set above the sparser over a range of priors, where no two-place TLI measure can rank a conjunction so"
version: 1
tags:
- philosophy-of-science
- epistemology
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-165
summary: >-
  Hartmann & Trpin (2026), [LIT-165](../literature.d/LIT-165.md), read in [NOTE-168](../notes.d/NOTE-168.md), which recomputed all
  three numerical claims. One theorem (TLI for singleton explanans sets),
  one counterexample (OLI fails) and two parameterised existence examples
  (a distal cause for P(H1) < .7; a negatively interacting cause for
  P(H1) = P(H2) < .75). The escape from Roche & Sober is representational:
  a set is scored differently from the conjunction, and the two-place
  theorems still hold for conjunctions. No characterisation says when the
  richer set wins, and the paper's claim that the measure "accommodates key
  scientific judgments" is more than the body shows.
---

# THEORY-tmpkyq9b: Measured as the contrast between a set of explanantia's CohOG+ coherence with the explanandum and with its negation, explanatory power satisfies Roche and Sober's Two Likelihood Inequalities for single hypotheses and fails the One, and in one causal chain and one collider it ranks the richer set above the sparser over a range of priors, where no two-place TLI measure can rank a conjunction so

## Source

Hartmann & Trpin (2026), [LIT-165](../literature.d/LIT-165.md) (*Philosophical Studies* 183:1817–1843),
read in full in [NOTE-168](../notes.d/NOTE-168.md), with the Appendix proofs. The reader recomputed
the chain and collider examples of §5.1 and the OLI counterexample, and all
three reproduce.

## What was actually shown

**The measure (Definition 1, p. 1829).** For a set H of explanantia and an
explanandum E, E_Coh(E; H) = [Coh(H ∪ {E}) − Coh(H ∪ {¬E})] /
[Coh(H ∪ {E}) + Coh(H ∪ {¬E})]. The base coherence measure CohOG+ is
Olsson–Glass overlap divided by its value under the independence
distribution with the same marginals (Eq. 3).

**Proposition 1.** With Shogenji coherence the measure is the
Schupbach–Sprenger measure generalised to n explanantia. It is proved in
the Appendix; the printed proof has a sign typo in its penultimate line.

**Proposition 2.** With CohOG+, if P(E|H1) > P(E|H2) and P(E|¬H1) <
P(E|¬H2), then {H1} has more explanatory power than {H2}. This is TLI, for
single-hypothesis sets only. The Appendix also gives a counterexample to
OLI: h = .5, p = .603, q = .103 gives .59; h = .01, p = .65, q = .35 gives
.55, with P(E) = .353 in both.

**The chain H1 → H2 → E** (P(H2|H1) = .9, P(H2|¬H1) = .1, P(E|H2) = .5,
P(E|¬H2) = .1). {H1, H2} beats {H2} for P(H1) < .7 (Fig. 1): .768 against
.748 at P(H1) = .05. The order reverses at high P(H1): .179 against .207 at
.9. The distal cause alone never beats the proximal one (fn. 13).

**The collider H1 → E ← H2** (P(H1) = P(H2), P(E|H1,H2) = .7,
P(E|H1,¬H2) = P(E|¬H1,H2) = .71, P(E|¬H1,¬H2) = .01). {H1, H2} beats {H1}
for P(H1) < .75 (Fig. 2): .611 against .585 at .4.

**What could have come out otherwise.** The derivative argument for TLI
could have failed, and the richer set could have lost at every prior. The
reader's recomputation is what makes the two examples part of the finding
rather than the paper's report of it.

## What this does not say

- **That Roche and Sober's theorems are wrong.** They still hold for
  conjunctions, as the authors grant (p. 1834). The measure escapes them by
  scoring {H1, H2} differently from H1 ∧ H2. Whether to use a set or a
  conjunction is a modelling choice the paper leaves to judgment: a set
  when each explanans "retain[s] explanatory relevance" (p. 1828).
- **That the measure is a TLI measure in Roche and Sober's sense.** The
  authors call it one "in the technical sense, but not in the structurally
  constrained sense that underwrites Roche and Sober's theorems" (p. 1832).
- **When a richer set wins.** Two hand-picked parameterisations are
  existence results. "It is not clear under which conditions" the
  interacting cause wins (p. 1836), and the advantage is not monotone in
  the prior.
- **That coherence-based measures in general behave so.** Other base
  measures (Douven–Meijs, Fitelson) are said to work on "preliminary
  computational evidence" not shown. The class of "structurally proper"
  coherence measures is uncharacterised, and CohOG+ is defended in a
  separate paper.
- **That Lange's entailment problem is solved.** The reply, that
  auxiliaries should not be counted in the explanans, applies to
  probabilistic measures generally, rests on a stipulated example, and the
  authors "do not claim that this resolves Lange's challenge completely"
  (p. 1821).
- **All of Roche and Sober's problems.** Two of four are set aside by fiat
  (fn. 4), and only a binary explanandum is treated.
- **Anything about weighing explanations of training phenomena.** The
  measure needs a joint prior over the explanantia, which such comparisons
  do not have ([NOTE-168](../notes.d/NOTE-168.md)).

## Connections

The record holds nothing else on explanatory power or coherence measures.
[LIT-156](../literature.d/LIT-156.md) (reciprocal causation) is the nearest philosophy-of-science
neighbour and is not engaged.
