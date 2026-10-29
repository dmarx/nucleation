---
status: Read
paper: 'LIT-tmpzfaqi'
title: 'Comolatti and Hoel — Causal emergence is widespread across measures of causation'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv's own copy, v1 of 3 February
    2022 (https://arxiv.org/pdf/2202.01854v1, 22 pages), text extracted
    with pdftotext. Read: the abstract, §§1–6, Supplementary §7.1, the
    captions of Figures 1–5 and S1–S3, and the 56 references. The
    heatmaps were read from captions and text only; no number was taken
    from a chart. The authors' code (github.com/renzocom/causal_emergence,
    compute.py, models.py, analysis.py) was read to see how the macro
    model, the intervention distributions and the averages are computed;
    it was not run. Checked by a record script on 2026-10-29, from the
    code's construction: micro and macro system-level EI of the 16-state
    bipartite model, symmetric (8/8) and asymmetric (13/3), at
    determinism 0.1, 0.5 and 0.9, with injective and fully degenerate
    main effects, under the maximum-entropy and stationary distributions,
    with the macro distribution either the paper's (uniform over the two
    macro states) or the image of the micro one. The algebra of §3 was
    checked by hand. The Entropy article of 2025 was not read.
date: '2026-10-29'
summary: >-
  Writes a dozen measures of causal strength as functions of sufficiency
  and necessity, or of determinism and degeneracy, and finds every one
  showing causal emergence on a bipartite Markov chain whose macro is a
  deterministic NOT gate, under three intervention distributions; the
  system-level EI under the stationary distribution shows none, as data
  processing requires. The model is hand-built for a deterministic macro,
  so it is the kind of result THEORY-787's promote_when says cannot
  settle it.
---
<!-- inactive-ok-file: THEORY-787 — Proposed; the causal thesis this reading bears on, cited as open -->
<!-- inactive-ok-file: QUESTION-204 — Open; the question this reading bears on, cited as open -->

# NOTE-tmpcmbzs: Comolatti and Hoel — Causal emergence is widespread across measures of causation

## Contribution

A unification and a demonstration. The unification writes Galton's
covariance, Eells's and Suppes's probability raising, Cheng's causal
power, Lewis's relative risk (also with a closest-possible-world
counterfactual), Pearl's PN, PS and PNS, a bit-flip sensitivity, effect
information and EI in terms of two "causal primitives". The demonstration
computes the difference between macro and micro values of each on one
model and finds positive differences for every measure somewhere in its
parameter grid.

## Key insight

Every measure compares P(e | c) with what happens to e without c, and
that second term needs a distribution over causes. Coarse-graining a
noisy micro chain onto a deterministic macro raises sufficiency and
necessity of the macro transitions, so any measure built from them can
rise at the macro. The authors read this as error correction by the
macroscale.

## Assumptions

- Causes and effects are states of a finite Markov chain; P(e | c) is
  the transition matrix. P(C) must be supplied: the stationary
  ("observational") distribution, the uniform ("maximum entropy") one,
  or a uniform distribution on a Hamming ball of radius Δ around the
  actual state ("local").
- **The model (§4.1, §7.1).** 2^N states in two groups A and B; each
  state moves only to the other group, to a main effect with probability
  p and to the rest of the group uniformly. Determinism is varied by p,
  degeneracy by an algorithm that stacks main effects onto fewer targets.
  The macro is fixed as {A, B} with transition matrix [[0, 1], [1, 0]],
  "independent of the model parameters". The main text uses 16 states,
  8/8; Figure S3 adds a 13/3 version.
- In the code the macro matrix and its distributions are set directly,
  uniform over the two macro states, not derived from the micro
  (compute.py: "for macro tpm this should be obtained by summing the
  microtpm, but for the bipartite model it doesn't matter").
- Averages over all transitions weight by P(c, e) = P_obs(c)P(e | c),
  the stationary distribution, whatever distribution is used for P(C)
  inside each measure (Figure 4 and S3 captions; compute.py).

## Key results

- **Identities (§3).** PNS = Eells's measure, PN = Lewis's normalized
  relative risk, PS = Cheng's causal power, under exogeneity and
  monotonicity. Galton's covariance is P(c)P(C\c)[suff + nec − 1].
  Effect information is log₂ of Suppes's ratio, and EI is its
  expectation. These are definitional rewritings, checked by hand.
- **Sensitivity (§4.3, Fig. 3).** Most measures rise with determinism and
  fall with degeneracy; the bit-flip measure is the exception.
- **Emergence (§5.2, Fig. 4, S3).** "All measures of causation exhibited
  instances of causal emergence", most in secondary transitions and in
  noisy, degenerate regimes, with "super causal emergence" where a micro
  transition is preventive and its macro positive. "The only condition to
  not show causal emergence was the overall effective information when
  using the observational distribution. This was known [20]."
- **The record's check.** In the symmetric model the uniform micro
  distribution maps to the uniform macro one and the stationary micro
  distribution to the stationary macro one. So these are common
  distributions, and the system-level EI cannot exceed the micro's
  (THEORY-tmphfpe7). Computed: micro EI 1.043, 1.783 and 3.326 bits at
  determinism 0.1, 0.5 and 0.9 with injective main effects, and exactly
  1.000 with fully degenerate ones, against the macro's 1 bit, under
  both distributions. In the 13/3 model the paper's uniform macro
  distribution is not the image of the uniform micro one, (13/16, 3/16).
  There the macro wins on EI under the paper's choice (1.000 against
  0.716 at determinism 0.1) and loses under the image (0.696).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Popular measures of causal strength are functions of sufficiency and necessity, or determinism and degeneracy | strong as rewriting | §3 algebra; the bit-flip measure excepted |
| C2 | Every measure examined shows causal emergence on the bipartite model | moderate | Figs. 4 and S3, one hand-built model |
| C3 | Causal emergence is "generally unaffected by choice of intervention distribution" | weak | the same model; EI under the stationary distribution is the exception; no other system |
| C4 | Macroscale causation "is a general fact about causal relationships" | weak | extrapolation from C1 and C2 |
| C5 | EI is the most conservative measure of emergence | moderate | the model; it is the one measure bounded by data processing |
| C6 | Local intervention distributions are a good compromise | weak | advocacy, with the Hamming metric depending on state labels |

## Concepts

- **Causal primitives**: sufficiency suff(e, c) = P(e | c); necessity
  nec(e, c) = 1 − P(e | C\c).
- **Determinism / degeneracy coefficients**: 1 − H(e | c)/log₂ n and
  1 − H(e | C)/log₂ n, at system level averaged over P(c).
- **Intervention distribution**: P(C), the distribution over which
  counterfactuals are taken; observational, maximum entropy, or local.
- **Causal emergence**: CE = CS_macro − CS_micro for a measure CS;
  negative is causal reduction.

## Connections

It extends Hoel, Albantakis and Tononi 2013 (LIT-1038, THEORY-222) from
EI to other measures, and cites Hoel 2017 (not registered) as the source
of the observational-distribution concession. It answers Aaronson's and
Dewhurst's criticisms. It does not cite Eberhardt and Lee
(LIT-tmpr2bnp), which appeared a month later. It cites Varley and Hoel
(LIT-027) for synergistic information growing at macroscales, and Rosas
et al. (LIT-1244) and Mediano et al. (LIT-025) as related approaches. The
measures' catalogue follows Fitelson and Hitchcock (not registered). CE
2.0 (LIT-1136, NOTE-1387) later builds on the same primitives.

## Bearing on the record

- **THEORY-787's promote_when.** The triage expected that the paper would
  either meet the promote_when or show itself to be more toy systems. It
  is the second. Its only system is a bipartite chain built so that its
  macro is a deterministic NOT gate "no matter the underlying noise".
  That is a hand-built toy with positive CE, which the promote_when says
  cannot settle it, and nothing in it is an independent interventionist
  test of which level the effects track.
- **THEORY-787's "in trouble if" clause and QUESTION-204, first half.**
  The paper concedes the decisive case without naming it. Under the
  system's own stationary distribution, used at both levels, EI shows no
  emergence, "This was known". The record's derivation shows the
  concession is general: under any one distribution over micro states,
  macro EI ≤ micro EI (THEORY-tmphfpe7). The paper's reply, that other
  measures and individual transitions still show emergence, changes the
  measure, not the distribution. Those measures are pointwise or
  normalized by log₂ n, and nothing bounds them by data processing. So
  the reply is not evidence for EI's level, which is what THEORY-787
  asserts.
- **A sentence that cannot be right as written.** In the symmetric model,
  system-level EI cannot show emergence under the maximum-entropy
  distribution either, since that distribution is common to both levels
  there. If Figure S3's maximum-entropy EI panel shows emergence, it
  comes from the transition averages, which weight by the stationary
  distribution while taking P(e | C) from the uniform one, or from the
  13/3 column, where the macro distribution is changed. The figure was
  not read for numbers, so which one it is stays unsettled.
- **THEORY-222.** Nothing to change. The arithmetic it holds is the
  arithmetic this paper extends.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- One model, built so the macro is deterministic and consistent at every
  parameter. The asymmetric variant changes only the group sizes.
- The macro is posited, not found by a search, so there is no question
  of which level a measure would pick; positive CE for one given
  partition is all that is shown.
- The averages mix distributions: P(e | C) under the chosen P(C), weights
  under the stationary one. So "EI under the maximum-entropy
  distribution" in the figures is not the EI of §3.10.
- The Hamming metric behind the local distribution and the bit-flip
  measure depends on the arbitrary binary labelling, as the authors note
  for the bit-flip measure.
- **Errors and slips.** In §3.1 the covariance derivation's middle lines
  carry +P(c)P(C\c)P(e | C\c) where a minus is needed; the last line is
  right. The system degeneracy is written Σ_e P(e | c) deg(e), where
  P(e | C) is meant, and the effect information log₂ n[det(e, c) −
  deg(c)], where deg(e) is meant. §3.10 points to "Section 3.4" for
  intervention distributions, which are in §4.2. §7.1's secondary
  probability (1 − p)/N_B does not normalize; the code uses
  (1 − p)/(n_B − 1). The abstract's "we prove" covers the rewritings of
  §3, not a theorem that emergence occurs.

## Open questions

- Does any measure that the data processing inequality bounds show
  emergence under a common distribution? If none does, "widespread across
  measures" is a property of the unbounded ones.
- On a system not built for it, do these measures agree on which
  partition is best, once the partition is searched rather than posited?
