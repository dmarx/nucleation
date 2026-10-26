---
status: Read
paper: LIT-tmplyhgz
title: 'Doshi-Velez and Ghahramani — Correlated non-parametric latent feature models'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full from the arXiv copy (arXiv:1205.2650v1,
    https://arxiv.org/pdf/1205.2650, which carries the UAI 2009 running
    heads and page numbers 143–150), text extracted with pdftotext. Read:
    §§1–6, Tables 1–2 and the figure captions; Figure 8's bars and the
    histograms of Figures 5 and 7 only through the text. Not compared with
    the PMLR reissue.
date: '2026-10-26'
summary: >-
  Makes IBP features correlated by having observations choose categories
  and categories choose features, Z = f(CM). If f(0) = 0, a finite dataset
  has finitely many features. DP-IBP, IBP-IBP and noisy-or IBP-IBP models
  have O(log log N) expected features. A category can switch features on,
  never off: features are dependent by sharing a category, or in the
  DP-IBP by belonging to rival ones, and suppression is left as future
  work. Against the IBP the structured
  variants win on three of five datasets, lose on the UN data and split
  on the gene data.
---
<!-- inactive-ok-file: CASE-tmplcm41 CLAIM-tmpwr001 — Proposed; the construction and claim this reading bears on, filed from the same exchange, cited as open -->

# NOTE-tmpn08ry: Doshi-Velez and Ghahramani — Correlated non-parametric latent feature models

## Contribution

The IBP draws each feature's column independently, so features that come
together in the world (a knife and a fork) are independent a priori. The
paper adds a layer above the features, after sigmoid and deep belief
networks. An observation draws categories, each category draws a set of
features, and the observation's features follow from its categories. It
states a sufficient condition for this to stay nonparametric, gives three
models, and compares them with the IBP and a Dirichlet process on five
datasets.

## Key insight

Correlation between features can be made a matter of shared causes rather
than a parameter: features co-occur because the same category turns them
on. Grouping the co-occurring features into one feature would lose the
cases where the set is incomplete ("if a pen is missing from a particular
desk"); a second layer keeps them separate and lets them borrow evidence.
For the number of features to stay finite, a category may only turn
features on.

## Assumptions

- C ~ NP1(αC), cnl = 1 if observation n is in category l; M ~ NP2(αM),
  mlk = 1 if category l has feature k; Z = f(CM) (1)–(2).
- NP1 and NP2 give each observation finitely many categories and each
  category finitely many features, with probability one.
- Proposition 1's condition: f(cnᵀmk) = 0 whenever cnᵀmk = 0. For the
  noisy-or, footnote 2: it "does not also leak".
- Exchangeability over observations and over features, inherited from the
  DP and IBP.
- Experiments: likelihood xn = znA + ε with akd ~ Exponential(λ) for
  continuous data; a false-detection and missed-detection model for the
  binary robot data; uncollapsed Gibbs, 3 chains of 1000 iterations,
  vague hyperpriors.

## Key results

- **Proposition 1.** Under the condition, finitely many observations have
  finitely many active features almost surely: finitely many categories,
  each with finitely many features, so C₁:N M has finitely many nonzero
  entries, and f maps zeros to zeros.
- **DP-IBP (3).** C ~ DP(αC), M ~ IBP(αM), Z = CM. Each observation is in
  one category and has exactly that category's features. E[N_f] ≤
  αM log(E[N_C]) + O(1) = O(log log N) by Jensen (4).
- **IBP-IBP (7).** C, M ~ IBP; znk = 1 if any of n's categories has k. Also
  O(log log N).
- **Noisy-or IBP-IBP (8).** P(znk = 1) = 1 − q^{cnᵀmk}: more active parent
  categories, more likely; q → 0 recovers the IBP-IBP.
- **Blocks demonstration.** On 700 6×6 images with four block features in
  nine fixed combinations the DP-IBP recovers four features and nine
  clusters, including a null cluster with no features. The noisy-or
  IBP-IBP, on data with overlapping clusters, recovers the structure "but
  often contain[s] replicas", and the counts are often overestimated
  (Fig. 7). "The ghosted features and replicas are a common occurrence
  when sampling in IBP-like models"; they disappear in time that "can be
  exponential in the size of the dataset".
- **Real data (Table 2, held-out predictive log-likelihood, higher is
  better).**

  | | UN | Jokes | Gene | Robot | India |
  |---|---|---|---|---|---|
  | DP | −3.5e5 | −45.5 | −1.2 | 0.8 | −2.0e9 |
  | IBP | −1.7e5 | −58.7 | −1.5 | 0.7 | −8.0e9 |
  | DP-IBP | −17.0e5 | −44.0 | −1.4 | 0.8 | −2.7e9 |
  | IBP-IBP | −25.0e5 | −48.6 | −1.6 | 0.8 | −3.0e9 |
  | noisy-or | −58.0e5 | −45.6 | −2.0 | 0.7 | −2.6e9 |

  The text: "The structured variants outperformed the standard IBP in
  almost all cases. In particular, the DP-IBP usually had the best
  performance among the feature-based models."
- **Qualitative.** On the UN data a DP-IBP sample gives the United States
  the developed nations' feature plus features for "relatively high
  tuberculosis rates, private healthcare spending, and prison
  populations"; on the robot data, categories that read as office,
  hallway, printing area and desk scenes.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | If categories can only switch features on (f(0) = 0), the correlated model has finitely many features on finite data | strong | Proposition 1; re-derived in [THEORY-tmpwm0kx](../theory.d/THEORY-tmpwm0kx.md) |
| C2 | The DP-IBP and IBP-IBP have O(log log N) expected features, against the IBP's O(log N) | strong | (4), Jensen on the concave harmonic number |
| C3 | Modelling feature correlation improves held-out prediction over the IBP in almost all cases | weak | Table 2: better in 9 of 15 model–dataset pairs, worse in 5, one tie; all three variants worse on UN |
| C4 | The DP-IBP has "fewer of the identifiability issues common to feature-based models" | weak | asserted in §5 from the restriction to one category per observation; not measured |
| C5 | Replica and ghost features are common in IBP-like samplers, and can take time exponential in dataset size to vanish | moderate | the authors' experience and the noisy-or demonstration; no analysis |

## Concepts

- **Category**: a latent group above the features; an observation's
  categories determine which features it may have.
- **Connection matrix M**: which features each category carries.
- **Link function f**: maps the count cnᵀmk of an observation's categories
  carrying feature k to znk: identity (DP-IBP), "or" (IBP-IBP), noisy-or.
- **Motif**: "commonly occuring sets of features", what the correlations
  should capture.

## Connections

It generalises the IBP ([LIT-tmpxrrf9](../literature.d/LIT-tmpxrrf9.md), whose §7.4 cites it as "a secondary
process capturing patterns in the latent features"), and sets itself
beside infinite hierarchical factor regression (Rai and Daumé 2009), the
phylogenetic IBP and the infinite factorial HMM, which correlate
observations rather than features. It names combining both kinds of
correlation as future work.

## Bearing on the record

- **T22's citation.** T22 says these models matter because "organizational
  modes can reinforce, inhibit, or depend on one another". The paper
  supports "reinforce" and "depend on" as co-occurrence through a shared
  category. It does not support "inhibit". Its finiteness condition rules
  out a category switching a feature off, and the conclusion lists
  "exploring methods to model negative correlations" as future work. The
  one negative dependence it has, in the DP-IBP, is exclusion: an
  observation in one category lacks the features only rival categories
  carry ([THEORY-tmpwm0kx](../theory.d/THEORY-tmpwm0kx.md)). For an organization that is "a member in one
  mode lacks the other mode's features", not one mode inhibiting another.
- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md), item 3.** The case says features whose B and a columns
  coincide across employees are identified only through Wk + Wl. The
  paper's motivation is the same point from the other side: a correlated
  model separates co-occurring features only where they sometimes occur
  apart. Where they never do, a category layer adds a cause for the set
  and identifies nothing more. The DP-IBP goes further: Z = CM gives each
  observation exactly its category's features, so features in one
  category and in no other are always together and are not separately
  identified.
- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md), item 4.** The paper's replicas and ghost features are
  the split freedom the case describes, met in practice by a sampler. They
  make "a birth in B can be an artefact" an observed hazard and not only a
  possible one.
- **[QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).** A category layer above features is a candidate
  for something between a feature and a perspective: a recurring set of
  features members take up together. It is not a perspective by
  [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md)'s standard, since it is again a co-occurrence pattern with
  no relational or governance structure; the paper itself warns that
  "the structures found cannot be considered to be discovering the 'true'
  or 'real' structure of dataset".

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No suppression.** By Proposition 1's condition, and by the authors'
  own list of future work, no feature or category lowers another
  feature's probability. The DP-IBP's exclusion between categories is
  the only negative dependence.
- **The summary of Table 2 is stronger than the table.** Of 15
  comparisons of a structured variant with the IBP, 9 are better, 5 worse
  and 1 tied. On the UN data all three are worse than the IBP (−17.0e5,
  −25.0e5 and −58.0e5 against −1.7e5), and on the gene data two of three
  are. The text says the DP clustering had "lower error rates than any of
  the feature-based models on the UN dataset", which reads against
  Table 2's UN column, where the IBP's log-likelihood is higher than the
  DP's; it may refer to Figure 8's L2 errors, which the extraction does
  not give.
- **No uncertainty.** No intervals or seeds; metrics averaged over the last
  50 samples of three chains, with complex models initialised from the
  output of simpler ones.
- **Inference is hard.** The noisy-or posterior "has many local optima";
  split-merge moves helped only on toy data. The authors attribute part of
  the DP's strong showing to "the robustness of inference in the DP".
- **Model choice is open.** How to choose among the priors for real data
  is left as a question.

## Open questions

- A nonparametric correlated feature model with inhibition that still has
  finitely many features on finite data. A category could switch a
  feature off only among features already on, which keeps Proposition 1's
  conclusion; the paper does not try it.
- Whether a category layer identifies anything a flat IBP does not, when
  the features in a category always co-occur.
