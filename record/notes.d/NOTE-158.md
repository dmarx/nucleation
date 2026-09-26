---
number: 158
status: Skimmed
formerly:
- NOTE-tmpqmp2c
paper: LIT-208
title: 'Grindrod et al. — Distributional semantics & holism'
version: 1
date: '2026-09-26'
summary: >-
  The holism of distributional/LLM meaning does not succumb to the instability objection, because what matters for communication is "differential" instability (changes in relative distances), which is constrained by frequent, consistent use and turns out to be a feature, not a bug.
---

<!-- inactive-ok-file: LIT-208 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-158: Grindrod et al. — Distributional semantics & holism

## Contribution

LLMs rest on distributional semantics, and the distributional hypothesis carries a holistic view of word meaning: a word's meaning depends on its relations to the other words in the model. Holism faces the classic instability objection, that any change in a system's meaning properties ripples through the whole system. The authors separate absolute instability (shifts in where points sit in a vector space) from differential instability (shifts in the relative distances between points), and argue that only the second matters for communication. They build two small language models, show how each kind of instability appears as the training corpus grows, and argue that a word's resistance to change scales roughly with how frequently and consistently it is used. Differential instability then allows productive meaning change without the damage the objection alleges.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Section plan: §1 distributional semantic models; §2 meaning holism; §3 the instability objection to meaning holism; §4 meaning similarity; §4 (numbered twice in v2) modelling the instability objection; §5 the sufficiency objection; §6 conclusion.
- §4 describes the method. The first model is a count model on Gertrude Stein's The Making of Americans, about 522k tokens with a very low type-token ratio, using a ±10-word window. The second is a Word2vec model on a much larger corpus of Wikipedia plus the Stanford Encyclopedia of Philosophy, used to watch how word neighbourhoods change as the corpus expands.
- §5: some expressions keep their meaning as the corpus grows while others shift in unsurprising ways. The authors take the stronger line that this sensitivity is a virtue: it can detect subtle speaker–hearer differences and diachronic change (Hamilton et al. 2016). They say that treating similarity differentially disarms Fodor and Lepore's objections to vector-space semantics.
- §6: they align their view with Hesse's network theory of meaning against Davidson, via Rorty's gravity analogy. They suggest LLMs may make it unnecessary to idealise away small perturbations in meaning.

## Open questions

- Bears directly on the anthology's representation topics. Relative distances as the invariant corresponds to the ML practice of comparing embedding spaces up to rotation or alignment (e.g. Antoniak & Mimno 2018 on embedding stability, which the paper cites).
- Check whether the argument carries over from static word embeddings to contextual transformer representations; the experiments use count and Word2vec models only.
- Check how §5 handles the sufficiency objection, i.e. whether distributional relations suffice for meaning at all.
