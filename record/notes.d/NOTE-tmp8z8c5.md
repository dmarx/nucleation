---
status: Read
paper: LIT-tmpgto9c
title: 'Referential intentions in word learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the authors' posted copy of the typeset article
    (langcog.stanford.edu, 8 pages): abstract, introduction, "Design of
    the Model" with its equations, "Corpus Evaluation" with Tables 1–3,
    "Prediction of Experimental Results" (cross-situational learning,
    mutual exclusivity with Fig. 2, one-trial learning, object
    individuation with Fig. 3, intention reading), General Discussion,
    footnotes and references. Not read: the online supporting information
    (technical appendix on the search, model code). The equations were
    garbled by text extraction and were reconstructed from the prose that
    states each term.
date: '2026-10-09'
summary: >-
  A Bayesian learner that infers speakers' intended referents and the
  lexicon jointly, allowing words to be used non-referentially and
  intentions to be empty, learns a much more precise lexicon from
  annotated child-directed video than association or translation models
  and reproduces mutual exclusivity, word-driven object individuation and
  intention-guided mapping as consequences of its likelihood.
---

# NOTE-tmp8z8c5: Referential intentions in word learning

## Contribution

Cross-situational models learned words from co-occurrence and treated the
speaker's intentions as noise or as attentional salience; social accounts
appealed to intentions but left the word–object mapping mechanism
unspecified. This paper gives one generative model in which the intended
referent is a latent variable between the scene and the words, so that
the learner infers what the speaker meant and what the words mean
together. It is the first, by the authors' account, evaluated both on
corpus learning and on behavioural phenomena.

## Key insight

Make the speaker's intention the hidden cause of the words, and let the
model say that a word was not about anything present. Then a learner can
discount the many utterances that do not refer to the scene, and
phenomena that looked like special word-learning principles fall out of
how a referentially used word is generated.

## Assumptions

- **Object names only.** Contexts are sets of basic-level objects;
  intentions are subsets of the objects present; the lexicon is a set of
  word–object pairs.
- **Uniform prior over intentions,** P(I_s|O_s) ∝ 1 over subsets of O_s,
  including the empty set.
- **Bag of words.** Words in an utterance are independent given I and L;
  syntax is ignored.
- **Two word sources.** Referential with probability γ (uniform among the
  lexicon's words for an intended object, averaged over |I|), otherwise
  non-referential (drawn from the corpus vocabulary, weight 1 for words
  outside the lexicon and κ for words in it).
- **Parsimony prior** P(L) ∝ e^(−α|L|).
- **MAP inference** by stochastic search with simulated tempering; no
  claim about cognitive mechanism (Marr's computational level).

## Key results

- **Table 1 (lexicon).** Intentional model: precision .67, recall .47,
  F .55; with κ and γ at their joint empirical-Bayes values, .57/.38/.46.
  Baselines (co-occurrence frequency, conditional probabilities, mutual
  information, IBM Model 1 both directions): precision .06–.15, F
  .10–.22.
- **Table 2 (intentions).** Intentional model F .58 (one-parameter .50);
  baselines F .36–.48.
- **Table 3.** The learned lexicon, with correct entries marked against a
  gold standard that includes plurals and baby talk.
- **Mutual exclusivity (Fig. 2).** On the corpus extended with "dax"
  uttered with a bird and a novel object, the lexicon mapping dax to the
  novel object has the highest posterior: mapping it to the bird lowers
  the likelihood of every earlier "bird" utterance; mapping it to nothing
  makes the experimental utterance non-referential. Baselines also get
  this.
- **Object individuation (Fig. 3).** For Xu's (2002) two-word and
  one-word conditions, model surprisal shows the same crossover as
  infants' looking times. Baselines cannot represent this.
- **Intention reading.** Given the speaker's intended referent as an
  observation, the model maps Baldwin's (1993) label to the hidden toy; a
  salience model would map it to the toy in hand.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Joint inference of intentions and lexicon learns a more precise lexicon from child-directed video than association and translation models | moderate | Tables 1–2; two ten-minute videos, one annotator's gold standard |
| C2 | The advantage comes from non-referential words and empty intentions | weak | informal argument after Tables 1–2; no ablation reported in the article |
| C3 | Mutual exclusivity needs no dedicated principle | moderate | Fig. 2; also produced by baseline models |
| C4 | Words can guide object individuation through inferred intentions | moderate | Fig. 3; qualitative crossover against one experiment |
| C5 | Representing referential intention is needed for Baldwin's result | weak | the intention is supplied to the model rather than inferred; the argument is that salience models cannot represent it |

## Method

The likelihood factors over situations: P(C|L) = Π_s Σ_{I_s ⊆ O_s}
P(W_s|I_s, L) P(I_s|O_s). The lexicon with the highest posterior is found
by stochastic search with simulated tempering. Comparison models produce a
word–object score, thresholded at the value maximizing F; their intended
referents are the objects whose words in the lexicon were uttered.
Surprisal (−log P) links model probabilities to looking times, after
Levy (2007).

## Concepts

- **referential intention**: the subset of present objects the speaker
  intends to refer to in an utterance; may be empty.
- **referential / non-referential use**: a word is generated to name an
  intended object, or drawn from the vocabulary independently of the
  intention (verbs, function words, names of absent objects).
- **intentional model**: the authors' name for their model.

## Connections

It takes the cross-situational problem from Siskind, Smith and Yu and
Smith, and its main baseline (IBM Model 1) from Yu and Ballard (2007),
whose corpus videos it re-annotates; the social side is Baldwin, Bloom and
Tomasello; Quine's chimney metaphor frames the joint problem. Xu and
Tenenbaum (2007) is the Bayesian word-learning precedent, and its size
principle reappears as the informative-speaker likelihood in Frank and
Goodman ([LIT-tmpkwn2g](../literature.d/LIT-tmpkwn2g.md)).

## Bearing on the record

- **To the RSA line.** The informative speaker of [LIT-tmpkwn2g](../literature.d/LIT-tmpkwn2g.md) and
  [LIT-tmphavsf](../literature.d/LIT-tmphavsf.md) is not in this paper. What it shares with them is the
  listener as a Bayesian inverter of a generative model of the speaker,
  and a latent intended referent. Bergen, Goodman and Levy
  ([LIT-tmpcsywp](../literature.d/LIT-tmpcsywp.md)) cite a different 2009 paper (Frank, Goodman, Lai and
  Tenenbaum, CogSci) for the informative utility; that paper is not in
  the record.
- No THEORY: its findings are specific to a small annotated corpus and to
  word learning, and the record holds nothing they correct.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- About twenty minutes of video from two dyads, annotated by the authors;
  the baselines' scores are much lower than Yu and Ballard reported, which
  the authors attribute to transcript, annotation and gold-standard
  differences.
- Three free parameters; robustness is asserted across a systematic
  variation the article does not tabulate.
- Object names only; no syntax, no aspect of objects, no non-object
  words.
- The behavioural fits are qualitative orderings, and the Baldwin case
  supplies the intention instead of inferring it.

## Open questions

- Does the precision advantage survive larger corpora and independent
  annotation?
- What does an informative, rather than uniform, speaker add to the
  learner's likelihood? Later RSA work answers this for interpretation,
  not for this corpus task.
