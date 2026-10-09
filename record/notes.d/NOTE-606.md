---
number: 606
status: Read
formerly:
- NOTE-tmp6dbc6
paper: LIT-816
title: 'Pragmatic language interpretation as probabilistic inference'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the authors' manuscript posted by Goodman's lab
    (cocolab.stanford.edu/papers/GoodmanFrank2016-TICS.pdf, 21 pages,
    dated 8 August 2016, "Manuscript submitted to Elsevier"): abstract,
    §§1–5, acknowledgements, Trends, the boxes (Outstanding questions,
    Refinements to the speaker's utility, Children's pragmatic competence,
    Producing referring expressions, Language use and language change),
    the glossary, the legends of Figures 1–2 and the reference list. The
    typeset TiCS article was not seen, so its wording, pagination and any
    changes after this manuscript are unchecked. The cited studies were
    not read; what the review says of them is reported as its account.
date: '2026-10-09'
summary: >-
  States the rational speech act framework (a listener inverting a
  softmax speaker whose utility is the log-probability a literal listener
  assigns to the intended world) and its uncertain extension (a joint
  posterior over the world and the speaker's topic, knowledge or lexicon),
  and reviews evidence that these predict reference-game judgements,
  cost and knowledge effects, scalar and embedded implicature, hyperbole,
  irony, metaphor and vague adjectives.
---
<!-- inactive-ok-file: THEORY-155 THEORY-172 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# NOTE-606: Pragmatic language interpretation as probabilistic inference

## Contribution

A review, but also the paper that fixes the RSA framework's canonical
form and names its extension, uRSA. It argues that one utility-theoretic
version of Grice's cooperative principle, with Bayesian inference about
the speaker, replaces the maxims and makes quantitative predictions, and
it gathers the evidence for that across reference games, implicature and
non-literal language.

## Key insight

The listener does not decode a meaning and then repair it when a maxim is
broken; every interpretation is inference to the best explanation of why
the speaker said this, among what she could have said. Uncertainty about
the speaker herself, her topic, her knowledge, even her lexicon, enters
the same posterior, and that is what produces the non-literal readings.

## Assumptions

- **A literal semantics** ⟦u⟧ assigning true or false to each world; the
  literal listener conditions the prior on it.
- **An approximately rational speaker**: softmax over a given set of
  alternative utterances with rationality α.
- **A shared prior** P(w) over worlds, and in uRSA a prior P(s) over
  speaker types.
- **Bounded recursion**: the standard form is listener → speaker →
  literal listener.
- **Computational level** only, in Marr's sense; no algorithmic claim.

## Key results

The review's own formal content:

- **RSA**: P_L(w|u) ∝ P_S(u|w)P(w); P_S(u|w) ∝ exp(αU(u; w));
  U(u; w) = log P_Lit(w|u); P_Lit(w|u) ∝ δ_⟦u⟧(w)P(w).
- **Worked example (Fig. 1)**: faces with hat and glasses, glasses only,
  neither; utterances "glasses", "hat". "Glasses" is read as the
  glasses-only face, because a speaker meaning the other face would have
  said "hat".
- **Utility refinements**: cost (written in the Box as
  U = log P_Lit(w|u) + cost(u); the sign must be negative for cost to
  disfavour an utterance, as in [LIT-809](../literature.d/LIT-809.md)'s Eq. 3); expected utility
  under speaker knowledge k, U(u; k) = E_{P(w|k)}[U(u; w)]; topic
  relevance by a projection t, U(u; w, t) = log Σ_{w′: t(w′)=t(w)}
  P_Lit(w′|u); social utilities such as kindness.
- **uRSA**: P_L(w, s|u) ∝ P_S(u|w, s)P(s)P(w).

The empirical results it reports, by its account: reference-game fits and
a replication; RSA fits to spatial-language games with noisier fits;
sensitivity to message cost in dollars and to typing difficulty; scalar
implicature modulated by the speaker's access; hyperbole, irony and
metaphor accounting for "almost all of the explainable variance";
deeper-than-minimal recursion in about 15% of participants in one study.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Basic RSA predicts graded judgements in simple signalling games across samples and stimuli | moderate | cited studies [24], [66], [13]; not shown here |
| C2 | uRSA, by joint inference over the speaker's topic, accounts for hyperbole, irony and metaphor | moderate | cited studies [45], [44], [43]; not shown here |
| C3 | Uncertainty over word meanings accounts for vagueness phenomena and for embedded implicatures that basic RSA misses | moderate | cited [51], [65], [9] |
| C4 | Most comprehenders use minimal recursion; a minority go deeper | weak | mixed cited evidence, the authors' summary |
| C5 | RSA replaces the maxims with one utility-theoretic cooperative principle | — | a framing claim, not an empirical one |

## Concepts

- **RSA**: a class of models in which comprehension arises from recursive
  reasoning about what speakers would have said, given communicative
  goals.
- **uRSA**: RSA with joint inference over the speaker's intended meaning
  and other aspects of the interaction (topic, context, word meanings).
- **literal listener**: the base case that conditions the prior on the
  utterance's truth.
- **topic / QUD**: a function t from worlds to the part of the world the
  speaker is trying to convey.
- **social recursion**: speaker and listener modelling each other to some
  depth.
- **implicature, scalar implicature, conversational maxims**: as in the
  glossary; standard.

## Connections

Grice (and Lewis's signalling games) supply the idea; game-theoretic
pragmatics (Benz, Jäger, van Rooij) and natural language generation the
tools; Bayesian cognitive modelling the inference. It connects RSA to the
question under discussion, to noisy-channel comprehension, to
compositional semantics à la Montague, to grammatical theories of
alternatives, and to neural speaker–listener models in NLP (Andreas and
Klein). The language-change box links in-the-moment pragmatics to
iterated learning (Kirby, Cornish and Smith 2008, which the record holds
as [LIT-771](../literature.d/LIT-771.md); and Kirby, Tamariz, Cornish and Smith 2015, where a
communicative pressure that the review says "can be modeled via RSA"
offsets learnability) and to typological efficiency (Regier, Kay and
Khetarpal on colour; Kemp and Regier on kinship; Xu and Regier on
numerals).

## Bearing on the record

- **[THEORY-172](../theory.d/THEORY-172.md)** takes its formal statement from here and its
  evidence from [LIT-821](../literature.d/LIT-821.md) and [LIT-809](../literature.d/LIT-809.md), read directly.
- **The uRSA posterior** P_L(w, s|u) is a joint distribution over the
  world and the circumstances of the utterance (speaker's topic,
  knowledge, lexicon) given what was said. The record has no other
  worked model of an utterance supporting a distribution over the
  situation of its saying.
- **Topic-relative utility** makes informativeness relative to a
  projection of the world, so a speaker can be maximally informative
  about one question and uninformative about others; this is the
  framework's own version of fidelity relative to a question.
- **[LIT-769](../literature.d/LIT-769.md) and [THEORY-155](../theory.d/THEORY-155.md).** The language-change box cites iterated
  learning and says whether typological distributions arise from
  iterated learning with RSA-like users is open. That is a question, not
  a result.
- No instruction for machine-learning practice; nothing for the
  anthology. It mentions neural speaker–listener models only as an
  application.

## Limitations

- A review: its empirical claims are summaries of other papers, several
  of them conference papers or then in press.
- The set of alternative utterances is given, not derived; the authors
  list this as open.
- The fits are of listeners' aggregate judgements; speakers' actual
  production (egocentric, overspecifying) is acknowledged as not well
  captured.
- Computational cost grows with worlds and utterances; no algorithmic
  account.
- This reading is of the submitted manuscript, not the published text.

## Open questions

Its own Box: depth of recursion; how alternatives are computed; how
informativeness relates to social goals; dialogue over many turns;
pragmatics and language change; how it is computed quickly and at scale.
