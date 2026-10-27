---
status: Read
paper: LIT-tmpezspt
title: 'Knowles and Ghahramani — Infinite sparse factor analysis and infinite independent components analysis'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the authors' PDF on the Cambridge
    Machine Learning Group's server
    (https://mlg.eng.cam.ac.uk/pub/pdf/KnoGha07.pdf, 8 pages; the same
    file is at https://mlg.eng.cam.ac.uk/zoubin/papers/ica07knowles.pdf),
    text extracted with pdftotext. Read: §§1–5, the captions of Figures
    1–3 and the 8 references. Figures 1–3 (the inferred mask and traces,
    the Amari-error boxplots, the Hinton diagram of G) were read from their
    captions and the text only; no number was taken from them. Equations
    (9), (10)–(11), the active-source ratio and (14) were re-derived and
    checked by numerical integration (record script, 2026-10-27). The
    Springer copy was not compared.
date: '2026-10-27'
summary: >-
  Defines infinite sparse factor analysis and infinite ICA: Y = G(Z ⊙ X) +
  E, an IBP mask Z over unboundedly many sources, Gaussian or Laplacian
  sources, and four variants with the one- or two-parameter IBP. Its Gibbs
  sampler integrates a source's value out when deciding whether it is
  active. On 30 sparse synthetic data sets the IBP variants beat FastICA
  in Amari error; on ovarian cancer microarray data it finds a
  tissue-specific signature also found by ICA. Results are figures only,
  and the text misstates the IBP's total number of features.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this reading bears on, cited as open -->

# NOTE-tmpmxqaw: Knowles and Ghahramani — Infinite sparse factor analysis and infinite independent components analysis

## Contribution

ICA fixes the number of sources and makes every source contribute to
every data point. This paper lets the number be unbounded and lets each
source be on or off at each data point, by putting an Indian buffet
process on a binary mask. Sources that are intermittently active are
then represented sparsely. It is the first infinite ICA, and the
nonparametric factor model the infinite factorial HMM extends with
Markov dynamics on the mask.

## Key insight

Split each source's contribution into whether it is active (z_kt) and how
strongly (x_kt). Give the first an IBP prior, the second a Gaussian or
Laplacian one, and integrate the second out when sampling the first. The
on/off decision is then made on the marginal likelihood of the data
point, not on a fitted value.

## Assumptions

- **The model (1)–(4).** y_t = G(z_t ⊙ x_t) + ε_t, ε_t ~ N(0, σ_ε² I),
  σ_ε² ~ IG(a, b); columns g_k ~ N(0, σ_G² I), σ_G² ~ IG(c, d); Z ~
  IBP(α, β), α ~ G(e, f). Rows of Z are sources, columns data points.
- **Four variants.** x_kt ~ N(0, 1) (isFA) or Laplace(1) (iICA); β = 1
  (the one-parameter IBP) or β ~ G(1, 2) (two-parameter). The source
  variance is fixed at one because G's scale is learned.
- **The two-parameter IBP (§2.1).** Customer i takes dish k with
  probability m_k/(β + i − 1) and Poisson(αβ/(β + i − 1)) new dishes;
  P(Z | α, β) = (αβ)^{K+}/∏_h K_h! · exp{−αH_N(β)} ∏_k B(m_k, N − m_k + β),
  H_N(β) = Σ_j β/(β + j − 1), (8).

## Key results

- **Sources (9)–(11).** For isFA, x_kt given the rest is N(g_k′ε/(σ_ε² +
  g_k′g_k), σ_ε²/(σ_ε² + g_k′g_k)), ε the residual with source k off. For
  iICA it is a two-piece Gaussian with means μ_± = (g_k′ε ± σ_ε²)/g_k′g_k
  on the negative and positive half-lines and variance σ_ε²/g_k′g_k.
- **Active sources (12)–(14).** P(z_kt = 1 | rest) = r/(1 + r), r = r_l r_p,
  r_p = m_{k,−t}/(β + N − 1 − m_{k,−t}). For isFA, r_l = σ̂ exp{μ̂²/(2σ̂²)},
  the hats being the posterior mean and standard deviation of (9); for
  iICA, (14). Both were checked by numerical integration: 0.31086 and
  0.32217 by quadrature against 0.31086 and 0.32217 from the formulas
  (record script, 2026-10-27).
- **New features (15)–(16).** κ_t, the number of features active only at
  data point t, is proposed from its prior Poisson(αβ/(β + N − 1)) by
  Metropolis–Hastings, so the acceptance ratio is a likelihood ratio.
- **Hyperparameters (17)–(20).** Conjugate updates for G's columns, σ_ε²,
  σ_G² and α; β by Metropolis–Hastings.
- **Synthetic data (§4.1).** 30 data sets, D = 7, K = 6, N = 200, a fixed
  sparse Z (Figure 1(a)), Gaussian or Laplacian sources; the four variants
  against FastICA with three nonlinearities. Z "is successfully recovered
  within an arbitrary ordering", with gaps where z_kt = 0 is inferred
  "where x_kt = 0". With Gaussian sources "all four variants perform
  significantly better" than FastICA, which is not expected to recover
  Gaussian sources; with Laplacian sources isFA1, iICA1 and iICA2 "still
  perform better on average", while isFA2 is "severely effected by having
  the incorrect source model". The two-parameter variants do no better:
  "β = 1 happens to be almost optimal for the synthetic Z used".
- **Gene expression (§4.2).** Ovarian cancer microarray data, N = 172
  genes, D = 17 tissue samples of five types. iICA1's signature 1 is
  expressed in every sample; signature 7 is specific to the pd-spa type,
  "consistent with that found in [4], with the same top 3 genes".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An IBP mask over sources gives a sparse ICA with an unbounded number of sources | definitional | (1)–(4) |
| C2 | The on/off ratio for a source integrates its value out, (12)–(14) | strong | re-derived and checked numerically ([THEORY-tmpxim6p](../theory.d/THEORY-tmpxim6p.md)) |
| C3 | On sparse synthetic data the IBP variants beat FastICA in Amari error | moderate | Figure 2, 30 data sets, a boxplot, no test named |
| C4 | The Laplacian (iICA) variants are more robust to a mismatched source model | weak | one comparison, a boxplot |
| C5 | On ovarian cancer data iICA finds a tissue-specific signature found before | weak | one data set, a Hinton diagram, agreement with one earlier ICA |

## Concepts

- **isFA / iICA**: infinite sparse factor analysis and infinite ICA, the
  Gaussian- and Laplacian-source variants.
- **Mask Z**: which sources are active at which data points, IBP
  distributed.
- **κ_t**: the number of features active only at data point t, the
  sampler's route to new features.
- **Amari error**: a permutation- and scale-invariant distance between the
  true and estimated mixing.

## Connections

It applies Griffiths and Ghahramani's IBP ([LIT-tmp3u0k8](../literature.d/LIT-tmp3u0k8.md)) and its
two-parameter version (Ghahramani, Griffiths and Sollich 2007, not held).
Its conclusion names Teh, Görür and Ghahramani's stick-breaking
construction ([LIT-tmpfhqac](../literature.d/LIT-tmpfhqac.md)) as the way to a slice sampler for Z. The
infinite factorial HMM ([LIT-1577](../literature.d/LIT-1577.md)) is this model with each row of Z a
Markov chain; its experiment's "iICA" baseline, which finds nine signals
where the iFHMM finds five, is this paper's model. The linear-Gaussian
IBP model of [LIT-tmp3u0k8](../literature.d/LIT-tmp3u0k8.md) is the special case without continuous source
values.

## Bearing on the record

- **[CASE-165](../cases.d/CASE-165.md), item 3: having against using.** The case says that "B = 1
  with a near 0 and B = 0 give nearly the same output, so availability is
  told from activation only by the prior and the transition, not by the
  data". This paper's model has exactly that pair, z (held) and x (used),
  and its sampler shows what the data do say once the activation is
  integrated out under its prior. For isFA the likelihood ratio for "on"
  is σ̂ exp{μ̂²/(2σ̂²)}, σ̂² = σ_ε²/(σ_ε² + g′g). Where the residual has no
  component along the feature's loading, μ̂ = 0 and the ratio is σ̂ < 1:
  the data favour "off" by an Occam factor, 0.26 in the record's check.
  So the case's sentence is right with the activation fixed, and needs a
  qualification with it integrated: the data then do bear on availability,
  but only through a factor whose size the prior on the activation sets
  ([THEORY-tmpxim6p](../theory.d/THEORY-tmpxim6p.md)). The paper's own synthetic recovery shows the
  consequence: its inferred Z has gaps "where x_kt = 0".
- **[CASE-165](../cases.d/CASE-165.md), item 4.** The case's "B_ck = 1 with v_ck = 0 equals B_ck =
  0" is the same identity for a loading rather than an activation; under
  this paper's Gaussian prior on G a zero loading is likewise disfavoured
  by an Occam factor, not excluded.
- **[LIT-1577](../literature.d/LIT-1577.md).** [NOTE-1199](NOTE-1199.md)'s iICA baseline is now held; the comparison's
  meaning is that adding Markov dynamics to Z reduces the speaker count
  from nine to five on one mixture.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Results are figures only**: boxplots and a Hinton diagram, no tables,
  no named tests; "significantly better" is unsupported in the text.
- **The gene-expression check** is agreement with one earlier ICA on one
  data set.
- **Errors and slips.**
  - §2.1 says that in the one-parameter IBP "the number of features per
    object, α, and the total number of features, Nα, are both controlled
    by α". Nα is the expected number of non-zero entries; the total
    number of features is Poisson(αH_N), as the same paragraph says a few
    lines earlier. The motivation for β stands: α sets both the count per
    object and the total, αH_N.
  - Figure 2's caption gives "D = 7, N = 6, N = 100" where the text gives
    D = 7, K = 6, N = 200.
  - The prior on β is G(1, 2) in the table of variants (§2) and G(1, 1)
    where its Metropolis–Hastings proposal is set equal to the prior
    (§3).
  - "A typical 1000 iteration ICA1 run" for iICA1; "Figure 4.2" for
    Figure 3; "severely effected", "infered".

## Open questions

- How sensitive is the inferred number of sources to the prior's scale
  on x, given that the on/off Occam factor depends on it?
