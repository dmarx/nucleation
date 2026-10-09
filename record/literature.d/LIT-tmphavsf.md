---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp6dbc6](../notes.d/NOTE-tmp6dbc6.md)), from the authors'' manuscript; worth reading as the standard statement of the rational speech act (RSA) framework: a pragmatic listener P_L(w|u) ∝ P_S(u|w)P(w) inverting a softmax speaker whose utility is log P_Lit(w|u), with a literal listener conditioning the prior on the utterance''s truth. Its uncertain-RSA extension, a joint posterior over the world and the speaker''s type, topic or lexicon, is what carries hyperbole, irony, metaphor, vague adjectives and embedded implicature. A review: the empirical support it cites is summarized, not shown, and its claims of near-ceiling fits rest on the cited papers. Source, with [LIT-tmpkwn2g](LIT-tmpkwn2g.md) and [LIT-tmpcsywp](LIT-tmpcsywp.md), of [THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md).'
title: 'Pragmatic Language Interpretation as Probabilistic Inference'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmp6dbc6) from the authors'
    manuscript posted by Goodman's lab (cocolab.stanford.edu/papers/
    GoodmanFrank2016-TICS.pdf, 21 pages, dated 8 August 2016, "Manuscript
    submitted to Elsevier"), not from the typeset article, which is
    paywalled; an 8-page typeset copy on a Stanford course site was not
    used. Details checked against Crossref (Trends in Cognitive Sciences
    20(11):818–829) and PubMed (PMID 27692852). No arXiv version.
    `published:` is 1 November 2016: Crossref gives only the issue month.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) for the authors, the DOI and the title
    found nothing.
tags:
- pragmatics
- linguistics
- cognition
- probabilistic-modeling
date: '2026-10-09'
published: '2016-11-01'
doi: '10.1016/j.tics.2016.08.005'
first_author: 'Goodman'
keywords:
- 'rational speech act'
- 'pragmatics'
- 'implicature'
- 'Bayesian models of cognition'
- 'social recursion'
implementations: []
summary: >-
  Goodman & Frank (2016), Trends in Cognitive Sciences 20(11):818–829.
  The review that names and states the rational speech act framework: a
  listener interprets an utterance by Bayesian inversion of an
  approximately rational speaker who values informativeness to a literal
  listener, replacing Grice's maxims with one utility-theoretic
  cooperative principle; joint inference over the speaker's topic,
  knowledge or lexicon (uRSA) extends it to non-literal language,
  vagueness and embedded implicature.
---
<!-- inactive-ok-file: THEORY-tmprknoj — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# LIT-tmphavsf: Pragmatic Language Interpretation as Probabilistic Inference

Noah D. Goodman and Michael C. Frank (2016), *Trends in Cognitive
Sciences* 20(11):818–829 — DOI-10.1016/j.tics.2016.08.005

## Key takeaways

- **The model.** P_L(w|u) ∝ P_S(u|w)P(w); P_S(u|w) ∝ exp(α U(u; w));
  U(u; w) = log P_Lit(w|u); P_Lit(w|u) ∝ δ_⟦u⟧(w) P(w). The literal
  listener is where conventional, compositional meaning enters; the
  speaker chooses among a set of alternative utterances.
- **Utility refinements** (Box): cost, U = log P_Lit(w|u) − cost(u) (the
  manuscript prints "+ cost(u)"); speaker uncertainty, expected utility
  over the speaker's knowledge k; topic relevance (a QUD), U(u; w, t) =
  log Σ_{w′: t(w′)=t(w)} P_Lit(w′|u); and non-informational social goals
  such as politeness.
- **uRSA.** P_L(w, s|u) ∝ P_S(u|w, s)P(s)P(w), with s the speaker's type:
  topic, word meanings, background knowledge, discourse context. Under
  topic uncertainty "$1,000 kettle" is read as affect (hyperbole), and
  likewise irony and metaphor; under threshold uncertainty "tall" gets
  class-relative, borderline and sorites behaviour; under lexical
  uncertainty embedded implicatures appear.
- **Evidence summarized.** Reference-game fits ([LIT-tmpkwn2g](LIT-tmpkwn2g.md) and a
  replication), cost sensitivity ([LIT-tmpcsywp](LIT-tmpcsywp.md) and a typing-speed study),
  scalar implicature with speaker knowledge manipulated; deeper recursion
  only in about 15% of participants in one more complex paradigm.
- **Stated limits.** A computational-level account; how it is computed
  fast, how alternatives are fixed, how speakers actually produce
  (overspecification), and whether it scales are open.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the manuscript
bibliography of 2026-10-09 (work `what-survives-translation`): one of the
works the manuscript considered and dropped from its final reference list.

Read on 2026-10-09 ([NOTE-tmp6dbc6](../notes.d/NOTE-tmp6dbc6.md)), from the authors' manuscript. It is
the record's statement of the RSA framework, and with [LIT-tmpkwn2g](LIT-tmpkwn2g.md) and
[LIT-tmpcsywp](LIT-tmpcsywp.md) the source of [THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md). Its box on language change
points to iterated learning and to typological efficiency results of the
kind [LIT-tmpe6100](LIT-tmpe6100.md) later gave for colour.
