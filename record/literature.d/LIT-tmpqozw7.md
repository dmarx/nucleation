---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp24x8p](../notes.d/NOTE-tmp24x8p.md)); worth reading as the sequel to [LIT-883](LIT-883.md) that takes its effective-context argument from character-level toy runs to subword-tokenised text and a predicted exponent. Two statistics of a corpus are measured: β, the decay with lag n of the largest singular value of the token–token covariance matrix (‖C(n)‖_op ~ n^(−β)), and γ, the decay of the next-token conditional entropy with context length (H_n − H_∞ ~ n^(−γ), a differential form of Hilberg''s hypothesis). A signal-to-noise argument gives the horizon n*(P) ~ P^(1/(2β)) a sample of P tokens can use; if learning within that horizon is fast, the test loss falls as P^(−γ/(2β)), and in general as P^(−min(δ, γ/(2β))), with δ the decay of the within-horizon excess loss (App. A, an ansatz-based derivation, not a theorem). Measured on TinyStories (β ≈ 0.88, γ ≈ 0.325, predicted α ≈ 0.185) and WikiText-103 (β ≈ 0.94, γ ≈ 0.265, α ≈ 0.141) with GPT-2- and LLaMA-style transformers up to about 10^8 tokens; the empirical exponents fall inside the predicted intervals and the n-gram losses collapse under P/n^(2β), L_n n^γ. γ is read off the n-gram losses of the largest trained models, not computed from the text alone. Usable horizons reached are a few tens of tokens. No embedding, PMI or hierarchy is studied.'
title: 'Deriving Neural Scaling Laws from the statistics of natural language'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09. It is not a work cited by
    the hierarchy and hyperbolic batch: the owner added it by link to the
    same request, with no stated context, right after the batches of
    nucleation#113 (LIT-865 to LIT-877) and nucleation#114 (the works they
    cite, among them LIT-883). Identified from the arXiv abstract page
    (arXiv:2602.07488, cs.LG with cs.AI and stat.ML; v1 submitted 7
    February 2026, v2 12 February 2026, v3 3 July 2026; authors Francesco
    Cagnetta, Allan Raventós, Surya Ganguli and Matthieu Wyart; comment
    "ICML 2026"). Checked against the PMLR volume page: Proceedings of the
    43rd International Conference on Machine Learning, PMLR 306:10450–10480,
    same four authors in the same order, title in title case ("…from the
    Statistics of Natural Language"); the conference met in Seoul, 6–11
    July 2026, and the volume was published on 29 September 2026. The PDF's
    own running title is in sentence case; the title above is the arXiv
    abstract page's, verbatim. Crossref holds no record of it (a
    bibliographic query returned other scaling-law papers), and PMLR
    assigns no DOI. `published:` is the arXiv v1 date, 7 February 2026, the
    earliest any source gives (ADR-002). The source is the arXiv id. Read
    in full the same day (NOTE-tmp24x8p) from the arXiv PDF of v3. Not held
    in nucleation before this filing: a grep of record/ for the identifier,
    the title, "Raventós" and "Cagnetta" found only LIT-877, LIT-880,
    LIT-883 and their notes, none of them this work. Not held in the
    Anthology of the SOTA as far as its clone shows: a grep of its record/
    (clone at commit d8b5ba5, 9 October 2026, possibly stale) for the
    identifier, the title, "Raventós", "Cagnetta" and "Hilberg" found
    nothing; the anthology holds TinyStories itself (ANTH-LIT-484) as a
    dataset. Its subject, what sets the exponent of data-limited neural
    scaling laws, is named in the blurb of the anthology's
    `training-optimization` topic, and its two statistics are what
    `signal-structure` holds, hence `anthology-candidate`. `linguistics` is
    carried for its measurement of two statistical properties of English
    text and its framing in the poverty-of-the-stimulus debate;
    `information-theory` for the conditional-entropy decay and Hilberg's
    hypothesis. The vocabulary has no word for scaling laws as such;
    `learning-theory`, widened by ADR-036 to how learning proceeds, is the
    nearest and is used. The authors' code
    (github.com/fracagnetta/small-language-modelling) was not inspected.
tags:
- learning-theory
- linguistics
- information-theory
- anthology-candidate
date: '2026-10-09'
published: '2026-02-07'
arxiv: '2602.07488'
first_author: 'Cagnetta'
keywords:
- 'neural scaling laws'
- 'data-limited scaling'
- 'token–token correlations'
- 'conditional entropy'
- "Hilberg's hypothesis"
- 'prediction time horizon'
- 'scaling collapse'
- 'TinyStories'
- 'WikiText'
implementations: []
summary: >-
  Cagnetta, Raventós, Ganguli and Wyart (2026), ICML 2026. The data-limited
  scaling exponent of a language model's test loss is predicted from two
  measured statistics of the corpus: β, the decay of token–token
  covariance with lag, which sets the usable context n*(P) ~ P^(1/(2β)),
  and γ, the decay of next-token conditional entropy with context length.
  When learning within that context is fast, the loss falls as
  P^(−γ/(2β)); on TinyStories and WikiText-103 transformers match the
  predicted 0.185 and 0.141 up to about 10^8 tokens.
---
<!-- inactive-ok-file: THEORY-tmpi172b QUESTION-025 THEORY-201 THEORY-195 THEORY-182 THEORY-183 — Proposed or open; cited as the account this reading produced, the question and accounts it bears on -->

# LIT-tmpqozw7: Deriving Neural Scaling Laws from the statistics of natural language

Francesco Cagnetta, Allan Raventós, Surya Ganguli and Matthieu Wyart (2026),
*Proceedings of the 43rd International Conference on Machine Learning*
(ICML 2026), PMLR 306:10450–10480 — [ARXIV-2602.07488](https://arxiv.org/abs/2602.07488)

## Key takeaways

- **Two statistics of a corpus.** β: the largest singular value of the
  V × V covariance C(n)_{µν} = P(X_i = µ, X_{i+n} = ν) − P(X_i = µ)P(X_{i+n} = ν)
  between tokens n apart falls as n^(−β). γ: the next-token conditional
  entropy given n tokens of context approaches the entropy rate as
  H_n − H_∞ ~ n^(−γ), a differential form of Hilberg's hypothesis. Both are
  hypotheses of power-law form, checked by fits over a finite range.
- **A finite sample is a finite horizon.** Each entry of C(n) estimated
  from P tokens carries noise of order P^(−1/2) (App. B, central limit and
  matrix Bernstein, with constants depending on the vocabulary), so lag n
  becomes usable only at P*_n ~ n^(2β), and the usable horizon is
  n*(P) ~ P^(1/(2β)). This is [LIT-883](LIT-883.md)'s effective context window, with the
  operator norm in place of a root-mean-square.
- **A loss decomposition.** The autoregressive loss is the entropy at the
  horizon plus the summed excess losses E_n(P) for the lags inside it
  (Eq. 34). If the excess losses fall as P^(−δ) with δ > γ/(2β) ("fast
  learning within the horizon"), the loss falls as
  L − H_∞ ~ P^(−γ/(2β)); otherwise as P^(−δ) (Eq. 40). The per-lag behaviour
  is an assumed scaling form (Eq. 25), so the result is a derivation from
  ansätze, not a theorem.
- **A collapse.** The same ansätze imply L_n(P) ≈ n^(−γ) ℓ(P/n^(2β)) for
  the n-gram losses, with one master curve ℓ (Eq. 43).
- **Measured.** BPE with 8192 tokens; GPT-2-style transformers (absolute
  and rotary positions; 98M to 600M parameters), a reduced LLaMA-3.2 and,
  for γ only, Mamba and an infini-gram model. TinyStories: β = 0.88 ± 0.06,
  γ = 0.325 ± 0.003, predicted α = 0.185 ± 0.013. WikiText-103:
  β = 0.94 ± 0.16 (from lags 1 to 32 only; the decay is a broken power
  law), γ = 0.265 ± 0.016, predicted α = 0.141 ± 0.025. Exponents fitted to
  the lower envelope of the empirical learning curves overlap the
  predicted intervals for every fit window tabulated (App. C.3), though on
  TinyStories they drift downward as more points are included. The n-gram losses collapse under the rescaling,
  and the collapse visibly degrades when β or γ is moved outside its
  range; LLaMA on TinyStories collapses better with β ≈ 0.65.
- **The fast-learning assumption, checked.** For lags n ≤ 12 on
  TinyStories, the large-P part of each n-gram loss decays as P^(−δ_n) with
  δ_n above γ/(2β) (Fig. 6).
- **Scope.** P up to about 10^8 tokens; the usable horizons reached are a
  few tens of tokens; contexts T from 64 to 512. γ is estimated from the
  n-gram losses of trained models, as an upper bound converging with P,
  not from counts in the text.

## Standing in the record

Filed on 2026-10-09 at the owner's request. It is not one of the works
cited by the hierarchy and hyperbolic batch: the owner added it by link to
the same request, with no stated context, right after the batches of
nucleation#113 and nucleation#114 and the opening of [QUESTION-025](../questions.d/QUESTION-025.md). Read on
its own merits ([NOTE-tmp24x8p](../notes.d/NOTE-tmp24x8p.md)); the reading produces [THEORY-tmpi172b](../theory.d/THEORY-tmpi172b.md).

Its nearest neighbour in the record is [LIT-883](LIT-883.md) (Cagnetta and Wyart 2024,
[THEORY-201](../theory.d/THEORY-201.md)), by two of the same authors, and it is that paper's sequel. The
earlier paper derived the effective context window t*(P) on the Random
Hierarchy Model ([LIT-877](LIT-877.md), [THEORY-195](../theory.d/THEORY-195.md)) and tested it on character-level text
with contexts up to 15. This one drops the generative model, keeps the
signal-to-noise argument for the horizon, adds a second measured statistic,
the decay of conditional entropy, and turns the pair into a predicted
exponent tested on subword text at contexts up to 512. The hierarchy that
motivated the earlier work is here only a cited explanation for why both
statistics decay as power laws; nothing in this paper tests it. On the
Random Hierarchy Model the new exponent γ/(2β) equals the one [LIT-883](LIT-883.md)
composed from its loss steps, with the sign corrected (worked in the NOTE;
the inference is this record's).

It does not answer [QUESTION-025](../questions.d/QUESTION-025.md). It builds no embedding and finds no
direction. It does report, in passing, that the lagged covariance matrices
of real subword text have fewer than about ten large singular values above
a power-law bulk, which bears on the spectral accounts of co-occurrence
the question builds on ([THEORY-182](../theory.d/THEORY-182.md), [THEORY-183](../theory.d/THEORY-183.md)). The details are in the
NOTE.
