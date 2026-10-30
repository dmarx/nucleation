---
number: 852
status: Read
formerly:
- NOTE-tmp382zf
paper: LIT-379
title: 'Chuai & Zhao — Anger makes fake news viral online'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2004.10399v3, 27 August 2020, 91
    pages: an 18-page main text with Table 1 and Figs. 1–2, then
    supplementary sections S1–S14 with Tables S1–S27), text extracted
    with pdftotext -layout. Every section, table and caption was read;
    the plotted figures (CCDFs, word clouds, boxplots) were read from
    their captions and the tables that report their tests. The Chinese
    originals of the questionnaire items were read in their English
    translations. Figshare data (10.6084/m9.figshare.12163569.v2) not
    opened.
date: '2026-10-14'
summary: >-
  On Weibo 2011–2016, lexicon-scored fake news carries more anger and less
  joy than true news, and in regressions with content, author and topic
  controls a post's share of anger words goes with more retweets and its
  share of joy words with fewer; the R² of the retweet models is 0.08–0.13.
  Two anger-dominated items in a 1,291-response survey drew slightly more
  anxiety-management and information-sharing motive than joy-dominated
  ones. The paper calls this causal; the design is observational.
---
<!-- inactive-ok-file: LIT-083 — Proposed; the neighbouring work, not leaned on -->

# NOTE-852: Chuai & Zhao — Anger makes fake news viral online

## Contribution

The paper gives fake and true Weibo news a five-emotion profile (anger,
disgust, joy, sadness, fear) from a hand-labelled lexicon, and finds that
anger separates fake from true news and highly from lowly retweeted news,
with joy the other way. It adds regression models with controls, English
datasets from Twitter and news media, a survey of reposting motives, and a
proposed intervention: flag posts whose anger share passes 20%.

## Key insight

Instead of explaining fake news's spread by its diffusion structure, which
is observed only after the fact, the authors look at what is in the post
at the moment it is posted. Among the five emotions they score, only
anger and joy differ consistently across every grouping and every scoring
method, in opposite directions.

## Assumptions

- **Labels.** Fake news is what Weibo's committee of outside fact-checkers
  tagged false; it is tagged "after being widely disseminated" (S1). True
  news is untagged news from verified users (media, elites, authorities).
  So the two sets differ by selection as well as truth: the fake set is
  enriched for widely spread posts, the true set for verified authors.
- **Emotion is the fraction of emotional terms.** A post's share of anger
  is its anger terms over its emotional terms. The lexicon has 6,155 terms
  (1,323 anger, 710 disgust, 2,066 joy, 1,243 sadness, 813 fear) from
  34,227 candidates, each labelled three times by nine coders aged 18–30,
  keeping terms on which the labels agreed. No agreement statistic or
  validation against human-rated posts is reported. It covers 87.1% of
  posts; the rest count as neutral.
- **Groups.** Posts are split by author followers and retweets. The text
  gives the optimal split as (x*, y*) = (10, 1000), but S2.2–S2.3 and S10
  use 10³ followers and 10 retweets, so the tuple is printed in the wrong
  order. "Highly retweeted" therefore means at least 10 retweets.
- **The retweet outcome** is the count within 48 hours of posting (S9).
- **Age is not controlled**, on the argument that most Weibo users are
  18–30 and that topic absorbs the rest (S8).

## Key results

- **Distributions (Fig. 1, Tables S2–S5).** Mean anger share: HLT 0.111
  against LHF 0.267 (K-S D = 0.275); true 0.112 against fake 0.165
  (D = 0.101); L 0.123 against H 0.240 (D = 0.210). Mean joy: HLT 0.611
  against LHF 0.329 (D = 0.366); true 0.609 against fake 0.443. Fear is
  higher in fake news (0.091 against 0.222). Disgust shows no consistent
  difference.
- **Robustness of the distributions (S7).** A naive-Bayes classifier
  (accuracy 0.64), a neural classifier (0.69) and a rank measure over six
  embedding classifiers (0.67–0.86) reproduce the anger and joy gaps. The
  other negative emotions flip between methods, and are thereafter folded
  into "other emotions".
- **Regressions (Table 1).** Lexicon shares, with follower, friend,
  mention, hashtag, location, date, URL, length, emergency and topic
  controls, robust standard errors.
  - Logit, fake against true: anger 0.889 (s.e. 0.097) and joy −1.507 for
    HF against LT news (N = 10,486); anger 0.385 and joy −1.279 for all
    news (N = 26,831). Pseudo-R² 0.35–0.36.
  - Linear, retweets in 48 h: anger 23.96 and joy −29.56 in fake news
    (model 3, N = 20,323, R² = 0.084); anger 22.28 and joy −35.98 in all
    news (model 4, N = 26,831, R² = 0.134).
  - The emotion shares sum to 1, so each coefficient is relative to the
    omitted bundle of disgust, sadness and fear.
- **The headline number.** "Increasing the occupation of anger by 0.1 and
  reducing that of joy by 0.1 in fake news leads to 5.8 more retweets."
  From model 3 (fake news) that is 2.40 + 2.96 = 5.4. The 5.8 is model 4
  (all news): 2.23 + 3.60 = 5.83. Likewise "2.2 more retweets" for anger
  alone is model 4's 0.1 × 22.28. Both numbers come from the all-news
  model and are attributed in the text to fake news.
- **Other controls (Table 1, S8).** The emergency dummy is one event, the
  2015 Tianjin explosion: 663 fake posts and 3 true. Its logit coefficient
  of 5.6 reflects that near-separation, and in the retweet models it is
  negative (−33.5, −23.0). Mention is positive for retweets but not
  significant in model 1.
- **English data (S10, Table S18).** On 129,690 unlabelled COVID-19 and
  2016-election tweets, scored with the NRC lexicon, anger's logit
  coefficient for ≥ 10 retweets is 0.215 (s.e. 0.062) and joy's −0.225;
  disgust, surprise and anticipation are also negative. No fake/true
  labels are involved. On the Kaggle fake/real news set, anger share is
  0.123 against 0.110 (D = 0.108). On 478 PHEME rumour tweets, HF 0.142
  against LF 0.020.
- **COVID-19 Weibo case (S7.3).** 200 lexicon-scored fake posts: anger
  minus joy is higher in HF than LF (t = 2.851, P = 0.006). No true news
  and no regression.
- **Survey (Fig. 2, S11–S13).** 15 posts (5 each from HLT, LHF, HLF),
  chosen near K-means cluster centres without regard to emotion; six
  questionnaires; 1,291 valid responses from 1,316 Weibo users aged
  18–30, via wjx.cn. Four rumour-sharing motives on a four-point scale
  (Cronbach's α 0.56–0.80), each centred on the respondent's mean of the
  four. LHF posts draw more anxiety management than HLF and HLT
  (D = 0.235 and 0.144), and fake posts more information sharing than
  true. Grouping by dominant emotion, only two posts are anger-dominated
  (LHF News1 and News5) against five joy-dominated: anger draws more
  anxiety management (0.027 against −0.057, D = 0.134, p = 0.023) and
  information sharing (0.444 against 0.335, p = 0.042), and joy more
  self-enhancement. No correction for the many comparisons.
- **Intervention (S14).** Flagging posts with anger share above θ = 0.2
  maximizes the gap between flagged HF and HT news: it would flag 46% of
  highly retweeted fake news and 22% of highly retweeted true news, and
  89% of flagged H posts are fake. A logit gives an odds ratio of 2.651
  for H-Anger, reported as "165% more likely to be fake"; that is odds,
  not probability. The effect assumes, "very optimistically", that no
  flagged post is retweeted.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | On Weibo 2011–2016, fake news carries a larger share of anger words and a smaller share of joy words than true news | moderate | lexicon and three model families, Tables S2–S14; label selection unaddressed |
| C2 | Within the same data, anger share goes with more retweets in 48 h and joy share with fewer, after content, author and topic controls | moderate | Table 1 (3)–(4), Table S17; observational, R² ≤ 0.135 |
| C3 | Anger causes the spread of fake news | weak | the regressions in C2, read causally; no experiment or identification strategy |
| C4 | The anger–retweet association holds on Twitter regardless of platform and culture | weak | one logit on unlabelled tweets, Table S18; small fake/true gaps in S5 and S6 |
| C5 | Anger-dominated news draws stronger anxiety-management and information-sharing motives | weak | two anger-dominated stimuli, K-S tests at p ≈ 0.02–0.04 |
| C6 | Flagging posts above 20% anger would stop 46% of highly retweeted fake news at a cost of 22% of popular true news | weak | in-sample threshold search, with the assumption that flagged posts are never retweeted |

## Concepts

- **Occupation of an emotion.** The fraction of a post's emotional terms
  that carry it.
- **LHF, HLF, HLT, …** Fake (F) or true (T) news by author followers (L/H,
  split at 10³) and retweets (L/H, split at 10).
- **Structural virality.** Mean shortest-path distance over a diffusion
  tree (Goel et al.); about 2 is pure broadcast.
- **Information dominance.** ID(G_i, G_j), the normalized difference in
  transmission coverage between follower bands, used to justify the 10³
  split.
- **Anxiety management, information sharing, relationship management,
  self-enhancement.** The four rumour-sharing motives of Sudhir &
  Unnithan's scale.

## Connections

It starts from Vosoughi, Roy & Aral (2018) on Twitter, whose findings on
diffusion structure and speed it reproduces on Weibo (S2.3, S3), and from
Berger & Milkman (2012) on arousing emotion and sharing, and Brady et al.
(2017) on moral emotion and diffusion. The record's other reading on
information operations, [LIT-083](../literature.d/LIT-083.md), is about sharing disinformation
incidents among defenders, not about spread.

## Bearing on the record

- **No THEORY, QUESTION or CLAIM cites this paper.** The reading supports
  one new account, filed as [THEORY-329](../theory.d/THEORY-329.md), held at the strength of an
  association.
- **The LIT's triage summary is right in outline, with three
  corrections.**
  - "Raising anger by 0.1 and cutting joy by 0.1 adds about 5.8
    retweets" is the all-news model; for fake news alone the model gives
    about 5.4.
  - "Questionnaires tie anger-dominated news to anxiety-management and
    information-sharing motives" rests on two anger-dominated posts.
  - "In regressions controlling for … emergencies" should say one
    emergency, the Tianjin explosion.
- **Tags.** `social-science`, `emotion-and-affect` and
  `society-and-governance` fit; `network-science` would fit the
  diffusion-structure supplement but is not where the claim lives.
- No instruction for machine-learning practice. The tagging proposal is
  platform policy, not ML practice, and the classifiers are instruments.

## Limitations

- **Observational.** The paper uses "causally" throughout for coefficients
  from logit and OLS models on observational data. There is no
  experiment, instrument or natural experiment. Unmeasured content
  features correlated with anger words (topic within the seven classes,
  rumour type, calls to "repost") could carry the effect.
- **Label selection.** Fake news is labelled because it spread, and true
  news comes from verified accounts; the fake-against-true logits mix
  truth with this selection.
- **Weak fit.** The retweet models explain 8–13% of the variance.
- **Measurement.** The lexicon is unvalidated against post-level human
  judgement, and an emotion share is undefined for 13% of posts.
- **Survey.** Few stimuli (two anger-dominated), many unadjusted tests,
  α as low as 0.56, and motives measured as stated, not as reposting.
- **Inconsistencies.** The split tuple is printed reversed (S2.1); group
  sizes differ between Table S1 (LHF 1,397), Table S2 (1,238) and Table
  S16 (1,326) without explanation; the 5.8 is attributed to the wrong
  model.

## Open questions

- Does manipulating a post's anger, holding its claim fixed, change how
  often it is shared? A randomized exposure experiment would settle what
  the regressions cannot.
- Does flagging angry posts reduce sharing in practice? The threshold is
  chosen in-sample and its effect assumed, not measured.
