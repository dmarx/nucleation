---
number: 542
status: Proposed
formerly:
- THEORY-tmphki46
promote_when: >-
  The same comparison on larger corpora of child-directed speech, annotated
  by people independent of the authors, with an ablation that removes
  non-referential words and empty intentions. The account is promoted if
  the intentional model's precision advantage survives and shrinks under
  the ablation, and refuted if the advantage disappears with better-tuned
  associative baselines or does not depend on the ablated components.
  Quantitative fits to infant data, rather than orderings, would bear on
  the behavioural half. More qualitative orderings matched to single
  experiments cannot settle it.
title: "A word learner that infers speakers' referential intentions jointly with the lexicon, and lets words be uttered non-referentially, learns object names from child-directed video more precisely than co-occurrence and translation models, and mutual exclusivity, word-guided object individuation and intention-guided mapping follow from it without principles built in for them"
version: 1
tags:
- cognition
- linguistics
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-815
summary: >-
  Frank, Goodman & Tenenbaum (2009), [LIT-815](../literature.d/LIT-815.md), read in [NOTE-611](../notes.d/NOTE-611.md). On about
  twenty minutes of video from two dyads, annotated by the authors, the
  intentional model's lexicon scores precision .67 and F .55 against .06–.15
  and .10–.22 for five baselines. The behavioural fits are qualitative, the
  baselines also produce mutual exclusivity, and the Baldwin case supplies
  the intention rather than inferring it. The reading said no THEORY,
  because the findings are specific to a small corpus and the record held
  nothing they correct; this account is filed Proposed for that reason.
---

# THEORY-542: A word learner that infers speakers' referential intentions jointly with the lexicon, and lets words be uttered non-referentially, learns object names from child-directed video more precisely than co-occurrence and translation models, and mutual exclusivity, word-guided object individuation and intention-guided mapping follow from it without principles built in for them

## Source

Frank, Goodman & Tenenbaum (2009), "Using Speakers' Referential Intentions
to Model Early Cross-Situational Word Learning", [LIT-815](../literature.d/LIT-815.md), read in [NOTE-611](../notes.d/NOTE-611.md).

[NOTE-611](../notes.d/NOTE-611.md) said "No THEORY: its findings are specific to a small annotated
corpus and to word learning, and the record holds nothing they correct."
The second reason concerns existing THEORYs, and does not bar a new one.
The first is why this account is `Proposed` and says its scale in the
title.

## What was actually shown

**The model.** The intended referent is a latent variable between the scene
and the words: a subset of the objects present, possibly empty, with a
uniform prior. A word is referential with probability γ, naming an intended
object, or otherwise drawn from the vocabulary independently of the
intention. The lexicon has a parsimony prior P(L) ∝ e^(−α|L|), and the MAP
lexicon is found by stochastic search with simulated tempering. It is a
computational-level model with no claim about mechanism.

**The lexicon (Table 1).** Intentional model: precision .67, recall .47,
F .55; with κ and γ at their joint empirical-Bayes values, .57/.38/.46.
Baselines (co-occurrence frequency, conditional probabilities, mutual
information, IBM Model 1 in both directions): precision .06–.15, F .10–.22.
For intended referents (Table 2) the model's F is .58 (one-parameter .50),
against .36–.48.

**Behaviour.** Mutual exclusivity: with "dax" uttered over a bird and a
novel object, mapping dax to the novel object has the highest posterior
(Fig. 2). Object individuation: model surprisal shows the same crossover as
infants' looking times in Xu's (2002) two-word and one-word conditions
(Fig. 3). Intention reading: given the speaker's intended referent, the
model maps Baldwin's (1993) label to the hidden toy, where a salience model
would map it to the toy in hand.

**What could have come out otherwise.** The baselines could have matched
the model on precision, and the individuation crossover could have failed.
Neither happened.

## What this does not say

- **That the advantage comes from non-referential words and empty
  intentions.** That is argued informally after Tables 1–2. No ablation is
  reported ([NOTE-611](../notes.d/NOTE-611.md), C2, weak).
- **That mutual exclusivity is evidence for intentions.** The baselines also
  produce it (C3). It shows only that no dedicated principle is needed.
- **That learners infer intentions in Baldwin's case.** The intention is
  supplied to the model as an observation (C5, weak).
- **That it scales.** About twenty minutes of video from two dyads,
  annotated by the authors, with three free parameters. The baselines score
  far below what Yu and Ballard reported on the same videos, which the
  authors attribute to transcript, annotation and gold-standard
  differences.
- **Anything beyond object names.** No syntax, no aspects of objects, no
  verbs or function words as targets.

## Connections

- **The informative speaker.** The speaker here chooses uniformly among
  the lexicon's words. Frank, Goodman, Lai and Tenenbaum ([THEORY-472](THEORY-472.md),
  [LIT-824](../literature.d/LIT-824.md)) make the speaker informative, which yields the size principle,
  and the rational-speech-act listeners of [THEORY-172](THEORY-172.md) invert such a
  speaker. What this account shares with them is a listener who inverts a
  generative model of the speaker, with a latent intended referent.
- **Social and associative accounts.** It takes the cross-situational
  problem from Siskind, Smith and Yu, and the social side from Baldwin,
  Bloom and Tomasello, and joins them in one generative model.
