---
number: 204
status: Active
formerly:
- THEORY-tmpi172b
title: 'On TinyStories and WikiText-103, the data-limited exponent of transformer test loss, fitted to the lower envelope of learning curves across context lengths at up to about 10^8 training tokens, overlaps γ/(2β), where β is the decay with lag of the top singular value of the token–token covariance and γ the decay of next-token conditional entropy with context length; under assumed per-lag scaling forms, a horizon n*(P) ~ P^(1/(2β)) gives the exponent min(δ, γ/(2β)), δ being the decay rate of the within-horizon excess losses'
version: 3
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-204 (batch 062, ADR-047 v2 and v3). The excess-loss sum was
    re-derived and gives min(δ, γ/(2β)) under the paper's assumed forms,
    and the exponent table of App. C.3 was re-read: every tabulated fit
    window overlaps the prediction on both corpora. The title now states
    the measured match and the conditional derivation, and no longer says
    the horizon is why real learners show the exponent. That test, the
    former promote_when, moves to QUESTION-233.
- version: 3
  date: '2026-10-20'
  note: >-
    The wider claim this account dropped when it was narrowed, that the
    horizon is why language models show the data-limited exponent γ/(2β),
    as the paper proposes, is filed as the Proposed THEORY-784, which
    extends this one (ADR-047 v4, narrowing-loss sweep, batch 068). Status
    and title are unchanged.
tags:
- learning-theory
- linguistics
- information-theory
date: '2026-10-09'
source:
- LIT-888
- LIT-883
summary: >-
  Cagnetta, Raventós, Ganguli and Wyart (2026), [LIT-888](../literature.d/LIT-888.md), building on
  [LIT-883](../literature.d/LIT-883.md)'s effective context window. Under assumed scaling forms for
  the conditional entropy and for each lag's learning curve, the exponent
  is min(δ, γ/(2β)) (re-derived 2026-10-20). Measured on TinyStories and
  WikiText-103, with transformers up to about 10^8 tokens and horizons of
  tens of tokens, the fitted exponent overlaps γ/(2β), best near the start
  of the envelope; γ is estimated from trained models' own n-gram losses.
  Whether the horizon is why is open (QUESTION-233).
answers:
- QUESTION-039
extended_by:
- THEORY-784
---
<!-- inactive-ok-file: THEORY-784 — Proposed; the wider claim this account dropped, filed separately and cited as open -->
<!-- inactive-ok-file: THEORY-201 QUESTION-025 — Proposed or open; cited as the accounts this one extends or is set beside and the question it does not answer -->

# THEORY-204: On TinyStories and WikiText-103, the data-limited exponent of transformer test loss, fitted to the lower envelope of learning curves across context lengths at up to about 10^8 training tokens, overlaps γ/(2β), where β is the decay with lag of the top singular value of the token–token covariance and γ the decay of next-token conditional entropy with context length; under assumed per-lag scaling forms, a horizon n*(P) ~ P^(1/(2β)) gives the exponent min(δ, γ/(2β)), δ being the decay rate of the within-horizon excess losses

## Source

Cagnetta, Raventós, Ganguli and Wyart (2026, ICML 2026), [LIT-888](../literature.d/LIT-888.md), §§3–5
and Appendices A–C, as read in [NOTE-689](../notes.d/NOTE-689.md). The horizon argument is from
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

**On the Random Hierarchy Model** (this record's inference, [NOTE-689](../notes.d/NOTE-689.md)),
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

## Note of 2026-10-20: the derivation re-derived, and the exponent table

The promotion audit (batch 062) re-derived the excess-loss sum and
re-read App. C.3 of the arXiv v3 PDF.

**The sum.** Take the paper's assumed forms. H_n − H_∞ ~ n^(−γ), the
threshold is P*_n ~ n^(2β), and past it each lag's excess loss is
E_n(P) ~ (H_{n−1} − H_n)(P/P*_n)^(−δ). Then
L − H_∞ = (H_{n*} − H_∞) + Σ_{n<n*} E_n.

- The boundary term is n*^(−γ) = P^(−γ/(2β)).
- The sum is P^(−δ) Σ_{n<n*} n^(2βδ−γ−1).
  - If δ > γ/(2β), the sum is dominated by n near n*, and gives
    P^(−γ/(2β)), the same order as the boundary term.
  - If δ < γ/(2β), the sum converges at small n, and P^(−δ) dominates.

So the exponent is min(δ, γ/(2β)), as Eq. 40 says. That a lag contributes
nothing before its pairwise correlation is detectable remains an
assumption.

**The table.** The predicted intervals are [0.172, 0.198] for TinyStories
and [0.116, 0.166] for WikiText-103, recomputed by Eq. 56 as
0.1847 ± 0.0127 and 0.1410 ± 0.0255. The fitted intervals are 95%
bootstrap intervals for fits to the first m points of the lower envelope.

- **TinyStories, m = 5 to 12.** From [0.1770, 0.1946] down to
  [0.1494, 0.1751]. All eight overlap the prediction.
- **WikiText-103, m = 5 to 8.** From [0.1324, 0.1552] to
  [0.1467, 0.1605]. All four overlap the prediction.

The paper's text says the fits overlap "for up to 10 of the first 12
points" on TinyStories, but the table shows all of them overlapping.

On TinyStories the fitted exponent drifts downward as m grows: the
interval midpoint is 0.186 at m = 5 and 0.162 at m = 12. So the match is
best near the start of the envelope, and the m = 12 interval only just
reaches the prediction.

**What moved.** The title used to say the loss falls as P^(−γ/(2β))
*because* P tokens resolve correlations only out to the horizon. The match
does not show that the horizon is the reason. The test that would, the
former promote_when, is now [QUESTION-233](../questions.d/QUESTION-233.md).

## Note of 2026-10-20: the wider claim, filed separately

When this account was narrowed, its wider form went nowhere a later result
could confirm or reject it. Under [ADR-047](../decisions.d/ADR-047.md) v4 it is now the Proposed
[THEORY-784](THEORY-784.md): that the horizon is why language models show the data-
limited exponent γ/(2β), as the paper proposes. This account is that one's
evidence, and nothing here changes.
