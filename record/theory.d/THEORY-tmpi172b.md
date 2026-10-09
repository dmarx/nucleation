---
status: Proposed
promote_when: >-
  A result in which the data-limited exponent of a next-token learner is
  moved by changing one of the two corpus statistics while the other is
  held: for instance, text whose correlations beyond some lag are
  destroyed or weakened by an intervention that keeps its short-range
  statistics, or a synthetic language with tunable β and γ, with the
  measured exponent tracking γ/(2β) and departing from it when the
  within-horizon excess loss is made to decay slowly. Or the same match at
  a scale where the usable horizon reaches thousands of tokens, with γ
  estimated without a neural model of the same class. More collapses at
  the scale already reported, with γ read off the trained models' own
  n-gram losses, cannot settle it.
title: 'In data-limited next-token prediction, the test loss falls as P^(−γ/(2β)), where β is the decay with lag of the strongest token–token covariance and γ the decay of next-token conditional entropy with context length, because P tokens resolve correlations only out to a horizon n*(P) ~ P^(1/(2β)) and the loss is the entropy at that horizon, provided the learner uses the tokens inside the horizon faster than the horizon grows'
version: 1
tags:
- learning-theory
- linguistics
- information-theory
date: '2026-10-09'
source:
- LIT-tmpqozw7
- LIT-883
summary: >-
  Cagnetta, Raventós, Ganguli and Wyart (2026), [LIT-tmpqozw7](../literature.d/LIT-tmpqozw7.md), building on
  [LIT-883](../literature.d/LIT-883.md)'s effective context window. The exponent is derived from assumed
  scaling forms for the conditional entropy and for each lag's learning
  curve, not proved; it is matched on two corpora, TinyStories and
  WikiText-103, with transformers up to about 10^8 tokens and horizons of
  tens of tokens, with γ estimated from trained models' own n-gram losses.
---
<!-- inactive-ok-file: THEORY-201 QUESTION-025 — Proposed or open; cited as the accounts this one extends or is set beside and the question it does not answer -->

# THEORY-tmpi172b: In data-limited next-token prediction, the test loss falls as P^(−γ/(2β)), where β is the decay with lag of the strongest token–token covariance and γ the decay of next-token conditional entropy with context length, because P tokens resolve correlations only out to a horizon n*(P) ~ P^(1/(2β)) and the loss is the entropy at that horizon, provided the learner uses the tokens inside the horizon faster than the horizon grows

## Source

Cagnetta, Raventós, Ganguli and Wyart (2026, ICML 2026), [LIT-tmpqozw7](../literature.d/LIT-tmpqozw7.md), §§3–5
and Appendices A–C, as read in [NOTE-tmp24x8p](../notes.d/NOTE-tmp24x8p.md). The horizon argument is from
Cagnetta and Wyart ([LIT-883](../literature.d/LIT-883.md)), whose account is [THEORY-201](THEORY-201.md).

## What was actually shown

**The derivation.** Writing the autoregressive loss as the unigram loss plus
the differential losses ∆_n = L_n − L_{n−1}, and assuming each ∆_n is zero
until a threshold P*_n and then approaches H_n − H_{n−1} as a power law, the
loss is the conditional entropy at the horizon plus the excess losses
inside it (Eq. 34). The threshold is set where the top singular value of
the lag-n covariance, ~ n^(−β), meets the P^(−1/2) sampling noise, which App.
B bounds by matrix Bernstein and Weyl's inequality. With H_n − H_∞ ~ n^(−γ),
the boundary term is P^(−γ/(2β)) and the excess sum is no larger if its
exponent δ exceeds γ/(2β); otherwise P^(−δ) dominates (Eq. 40). The same
ansätze predict a collapse L_n ≈ n^(−γ) ℓ(P/n^(2β)) of the n-gram curves.

**The test.** On TinyStories (β = 0.88 ± 0.06, γ = 0.325 ± 0.003) and
WikiText-103 (β = 0.94 ± 0.16, γ = 0.265 ± 0.016), BPE with 8192 tokens, the
predicted exponents are 0.185 ± 0.013 and 0.141 ± 0.025. Exponents fitted to
the lower envelope of GPT-2-style learning curves over several context
lengths overlap these intervals for every fit window tabulated. The n-gram
curves collapse under the predicted rescaling for GPT-2 (absolute and
rotary positions) and LLaMA-style models, and the collapse degrades when
β or γ is moved outside its range. For n ≤ 12 on TinyStories the
within-horizon excess losses decay faster than P^(−γ/(2β)). This could have
failed: the empirical exponent could have differed from γ/(2β), the curves
could have refused to collapse under the measured β, or the excess losses
could have decayed slowly, putting the loss in the P^(−δ) regime.

**On the Random Hierarchy Model** (this record's inference, [NOTE-tmp24x8p](../notes.d/NOTE-tmp24x8p.md)),
the formula gives ln(1/f)/(2 ln m), the exponent [LIT-883](../literature.d/LIT-883.md) composed from its
loss steps, with that paper's sign slip corrected. So the account
generalises [THEORY-201](THEORY-201.md)'s envelope rather than competing with it.

## What this does not say

- **Not that it is proved.** That a lag contributes nothing until its
  pairwise correlation is detectable, and that the per-lag curves share a
  scaling form, are assumptions (Eq. 25). Dependences invisible to
  pairwise covariance play no part in the argument.
- **Not that γ is a statistic computed from text.** It is fitted to the
  n-gram losses of the largest trained models, upper bounds that converge
  only at small n. The agreement of five model classes on TinyStories is
  the evidence that it belongs to the data.
- **Not that it holds at the scale of current models.** P reached about
  10^8 tokens and the usable horizon a few tens of tokens. The WikiText
  correlation decay changes slope beyond lag 32, so a single β is not
  available there.
- **Not that every architecture shares the exponent.** Which learners are
  in the fast-learning "universality class" is a conjecture. LLaMA on
  TinyStories collapses best at a β outside the measured interval, and
  in hierarchical toy data CNNs beat the corresponding prediction.
- **Not that language is hierarchical.** Hierarchy is cited as one reason
  both statistics are power laws. Nothing here tests it, and the account
  needs only that they are.
- **Not anything about embeddings or directions.** Only the size of the top
  singular value of each lagged covariance enters; its vectors are not
  studied. It does not bear on [QUESTION-025](../questions.d/QUESTION-025.md) beyond the remark that these
  matrices have a few large singular values over a power-law bulk.
- **Not a rule for how much data or context to use.** How to train or
  size a model is an ML-practice question, and this account does not
  answer it.
