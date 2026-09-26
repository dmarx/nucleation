---
status: Skimmed
paper: LIT-tmpycib2
title: 'Šekrst — Do LLMs Hallucinate Electric Fata Morganas?'
version: 1
date: '2026-09-26'
summary: >-
  Hallucinations are outputs that diverge from what the source or training data supports, and an LLM's self-reports of emotion or sentience fall under that definition. Šekrst argues that any real machine consciousness might therefore stay epistemically inaccessible, indistinguishable from a sufficiently advanced hallucination.
---
<!-- inactive-ok-file: LIT-tmpasglk — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-tmp4tk05 — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->

<!-- inactive-ok-file: LIT-tmpycib2 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpwm6cq: Šekrst — Do LLMs Hallucinate Electric Fata Morganas?

## Contribution

The paper connects AI hallucination, meaning false or unverifiable LLM output, with the question of AI consciousness. It asks whether such errors could be mistaken for signs of emergent intelligence. Hallucinations look like data anomalies, but they make it harder to tell whether LLMs are sophisticated simulators of intelligence or could develop genuine cognition. Šekrst analyses the causes of hallucination, its effect on how AI cognition is perceived, and what follows for AI consciousness.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 (pp. 1–3): hallucination is defined, following Dziri et al. 2023, as a response not fully verifiable from its source. Bing's declaration of love to Kevin Roose is the example. The project reframes the problem of other minds and Searle's strong vs weak AI, and AGI is taken in Searle's strong-AI sense.
- §3 (pp. 4–8): causes of hallucination include source–target divergence, training/inference mismatch and overfitting.
- §4 "Parameter Tradeoff" (pp. 8–11): hallucination is recast as divergence between the output distribution and the data-expected distribution. In an informal test, GPT-3 at high temperature named Violet Jessop or Eva Hart as the Titanic's "last survivor", while at low temperature it gave Millvina Dean. The conclusion drawn is that perceived intelligence comes from tuning randomness.
- §5–6 (pp. 11–14): qualia, Mary and the explanatory gap. The "WikiBERT" test used deepset/bert-base-cased-squad2, an extractive QA model, on a Titanic question. It "avoids hallucinations" but produces nothing resembling conscious thought, which the paper takes to show that human-like outputs come from subjective, variable training data. LaMDA and Lemoine are discussed.
- §7–8 (pp. 14–17): a cybernetic reappraisal via Ashby and Wiener. Even with black-box problems solved, apparent emergent consciousness might be a hallucination. The paper concludes that AI consciousness "might always remain epistemically inaccessible".

## Open questions

- The conceptual point, that sentience self-reports are by construction candidates for hallucination, overlaps with Birch's [LIT-tmp4tk05](../literature.d/LIT-tmp4tk05.md) "gaming problem" and Seth's [LIT-tmpasglk](../literature.d/LIT-tmpasglk.md) conscious-seeming AI. It may belong in a cluster note, not a note of its own.
- The empirical parts are thin. Single-prompt temperature anecdotes and an extractive QA model standing in for "WikiBERT" cannot bear the weight put on them, and a deeper reading should say so plainly.
- Check the JCS version for changes from the arXiv manuscript and confirm the issue (11 alone, or 11–12) and the exact date.
