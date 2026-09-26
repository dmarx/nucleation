---
status: Skimmed
paper: LIT-tmpi8kod
title: 'Angius et al. — Making sense of transformer success'
version: 1
date: '2026-09-26'
summary: >-
  Current explanations of how transformer LMs achieve linguistic competence use the same three strategies cognitive science uses for humans — functional analysis, mechanistic explanation, and brain co-simulation — so the "explanatory gap" for NLMs is of a familiar kind.
---

<!-- inactive-ok-file: LIT-tmpi8kod — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmp822h0: Angius et al. — Making sense of transformer success

## Contribution

This is an epistemological analysis of attempts to explain how the fairly simple algorithmic parts of neural language models produce real linguistic competence. After introducing the Transformer, the authors argue that philosophy of AI has moved from Turing's "can machines think?" to "how can machines think?", which exposes an explanatory gap. They argue that the explanatory strategies now used on NLMs match those cognitive science uses on human intelligence. Behavioural probes of theory of mind, discourse-entity tracking and property induction count as functional analysis. The copying algorithm and induction heads give a mechanistic explanation of in-context learning. Work predicting brain activation from NLMs is described as "co-simulation", in which model and brain are each used to understand the other.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Structure: §2 neural models and natural language; §3 how can neural models think?; §4 functional analyses; §5 thinking about mechanisms; §6 looking at the brain; §7 concluding remarks.
- §3 notes that most arguments against artificial semantics date from the 1980s–90s. With BIG-bench and large-scale social imitation games, the Turing test no longer seems a real obstacle, so the question becomes how, not whether.
- §4 treats "machine psychology" (Hagendorff) and silicon samples as functional analysis. It notes the open question of whether tests designed for humans validly transfer to NLMs.
- §5 sorts mechanistic interpretability tools into circuit discovery (ACDC), localization (sparse probing), visualization (AttentionViz), and conversion (RASP, Transformer Programs). Induction heads are the paradigm mechanistic explanation.
- §6 covers the "simulative" route: NLM–fMRI correlations (Caucheteux & King), following the precedent of CNNs and the ventral visual stream, even though nothing in transformers was designed with the brain in mind.
- §7: the success is empirical, not a priori. It came from "more elegant mathematics", not brain mimicry. There is no mystery about what a transformer computes, but there is opacity about how individual meaningful outputs arise.

## Open questions

- A philosophy-of-science map of interpretability practice (behavioural, mechanistic, neuro-alignment), useful for placing interpretability work in the anthology's explanation topics.
- Check whether the paper argues that any one strategy is sufficient or privileged, or only that all three mirror cognitive science.
- Check how "co-simulation" is defined and whether it answers the worry that NLM–brain correlations are predictive but not explanatory.
