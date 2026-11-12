---
status: Read
paper: LIT-tmpaodxg
title: 'Scalco, Gesualdo, Cerqueti and Cinelli (2026) — How to detect information voids using longitudinal data from social media and web searches'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read: arXiv:2602.15476v1
    [cs.CY], 17 Feb 2026, https://arxiv.org/pdf/2602.15476, PDF, 43 pp.
    (main text + references + SI), CC BY, fetched 2026-11-12. - Not read:
    the published *Scientific Reports* article; differences from v1 after
    review are unknown. Outcome as the reader gave it: **Read**, from the
    arXiv preprint (v1), not the *Scientific Reports* version of record.
    Main text read in full (Introduction, Data Science Pipeline, Results and
    Discussion, Conclusions, Methods); the Supplementary Information and
    references (pp. after "References", which include the SI) were skipped.
date: '2026-11-12'
summary: >-
  Treating the online information ecosystem as a market with information
  **demand** (Wikipedia page views, Google Trends) and **supply** (Facebook
  posts via CrowdTangle, Twitter full-archive, GDELT news volume), the
  authors rescale each series by its mean, define an information delta δt =
  ŝt − d̂t, decompose δ by STL and flag remainder outliers by an IQR rule.
  Anomalies with δ < 0 are **voids** (demand far exceeds supply), δ > 0
  **overabundance**; a five-regime scale runs Void / Lack / Balance /
  Abundance / Overabundance. On synthetic Gaussian series with injected
  spikes the detector reaches mean precision > 90% above 6σ. Applied to five
  COVID-19 vaccine brands in six European countries (Jan 2020 – Apr 2021),
  anomalies cluster at the vaccine rollout, at EMA's Moderna authorization
  and at the AstraZeneca suspension; voids outlast overabundance (up to 29
  consecutive days vs 26). Matching shared URLs to NewsGuard scores, void
  periods carry fewer posts from top-credibility sources and more from
  "proceed with maximum caution" sources than non-anomalous periods.
---
<!-- inactive-ok-file: CASE-tmpd5eqf CLAIM-tmpifp69 — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: THEORY-864 — Proposed; cited as on the record -->

# NOTE-tmp9yggi: Scalco, Gesualdo, Cerqueti and Cinelli (2026) — How to detect information voids using longitudinal data from social media and web searches

## Contribution

An operational, replicable definition and detector for "information voids" as anomalous demand–supply imbalances, plus an associational link between voids and lower average source credibility.

## Key results

1. Abstract, definition: "information voids, i.e., periods in which little or no reliable information is available on a given topic."
2. Pipeline, Fig. 1 text: "A void arises when information demand exceeds supply, resulting in strongly negative delta values; this can occur even when supply is high, as long as demand remain significantly higher."
3. Anomaly detection, persistence: "These results reveal a marked asymmetry: information voids tend to persist longer than periods of overabundance."
4. Information quality (Table 3): "during periods of information voids (i.e., negative anomalies), content from highly credible sources (S = 100) accounts for only 20.84% of posts on Facebook and 23.87% of posts on Twitter, considerably lower than the 33.68% and 31.62% observed on Facebook and Twitter, respectively, during non-anomalous periods." Low-credibility (S < 39) share in voids: 6.1% (Facebook) and 27.28% (Twitter) vs 5.46% and 22.1%.
5. Conclusions, causal caveat: "While our study does not establish a causal link between the presence of information voids and increases in misinformation, this association is clearly observable in the analysed data".
6. Synthetic validation: "mean precision higher than 90% for anomaly levels above 6σ and a mean F1 score higher than 0.68 for anomaly levels above 9σ".

## Assumptions

- Search and page-view volume measures demand; post/article volume measures supply (volume, not quality: a void "can occur even when supply is high").
- Rescaling by the series mean makes heterogeneous sources comparable; a void is thus relative to each series' own baseline, not an absolute shortage.
- Keyword-based collection per vaccine brand; NewsGuard domain scores as a credibility proxy; only posts with rated URLs enter the quality analysis.

## Concepts

information void; information overabundance; infodemic; information delta δt; five regimes (Void, Lack, Balance, Abundance, Overabundance); STL decomposition + IQR anomaly detection; persistence of anomalies; demand and supply of information as an attention market.

## Bearing on the record

**On the LIT's and the exchange's characterization.** Accurate: "methods for detecting information voids, mismatches between the supply of and demand for information, from longitudinal social-media and search data". Two refinements: a void is a **statistically anomalous** negative mismatch relative to each series' own mean, not any mismatch; and the misinformation link is explicitly associational.

- **[CLAIM-tmpifp69](../claims.d/CLAIM-tmpifp69.md)** (attention optimization favours clickbait and works against investigative journalism, whose demand cannot be shown before findings exist): *qualifies*, in a useful way. The paper's method can detect a void only where demand is **visible**, as searches or page views; the claim's third step ("The public cannot demonstrate demand for an investigation whose findings are not yet known") describes exactly the void this method cannot see, because there is nothing to search for. So the work supports the general frame the claim uses (information as a market of demand and supply, where unmet demand is filled by lower-quality supply, result 4) but marks the edge of measurability the claim depends on: a supply–demand detector is blind to *latent* demand, which is the investigative case. It *leaves open* the claim's causal story about newsroom economics; nothing here concerns producers' incentives or investigative capacity, and the quality link is correlational (result 5).
- Bearing on **[CASE-tmpd5eqf](../cases.d/CASE-tmpd5eqf.md)** (the newsroom that reads low traffic on investigations it no longer funds): same point; that case's loop runs entirely below this detector's threshold, since neither demand nor supply registers.

Searched origin/main record/ for: information void / data void, infodemic, misinformation, NewsGuard, Google Trends / Wikipedia page views, Cinelli, information supply. None of "information void", "data void", "infodemic" is held anywhere on main. NewsGuard appears only in [NOTE-1049](NOTE-1049.md) / [THEORY-864](../theory.d/THEORY-864.md) (a different topic, testimonial injustice from generative models). No other LIT holds this DOI, arXiv ID or title.

## Limitations

One topic (COVID-19 vaccines), one period, six countries; platform samples not representative (the authors say so); volumes are proxies; mean-rescaling makes "void" relative; the quality analysis pools periods from 8 Dec 2020 and reports percentages without tests; Twitter's much lower average credibility (≈70 vs ≈84) dominates cross-platform contrasts. Read from the preprint; the published version may differ.
