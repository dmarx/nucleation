---
number: 608
status: Read
formerly:
- NOTE-tmp789mw
paper: 'LIT-838'
title: 'The Semantics of Definite and Indefinite Noun Phrases'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the author's Semantics Archive copy, a scan of the
    1988 Garland printing (213 two-page spreads, no text layer), through
    OCR (tesseract 5, each half-spread separately); pages 392–393, a
    separate file in the same item, read as well. Preface, chapters I–III,
    the footnotes to each chapter and the reference list read. Logical-form
    tree diagrams did not survive OCR and were reconstructed from the
    surrounding prose and the formulas; formulas with special symbols were
    read through OCR noise and checked against the prose that states them.
    The 1988 printing reproduces the 1982 typescript; the 1982 original was
    not seen, so differences between them, if any, were not checked.
date: '2026-10-09'
summary: >-
  Argues that indefinites (and definites) are variables without
  quantificational force, bound by the nearest operator, which yields
  donkey-sentence readings; then recasts semantics as file change: each
  sentence updates a structured common ground of numbered cards, truth of
  a file supplies existential force, and the definite/indefinite contrast
  reduces to one felicity condition (new card versus familiar card), from
  which binding, presupposition projection and, with accommodation,
  narrow-scope definites follow.
---
<!-- inactive-ok-file: LIT-811 — Deferred, no lawful full text; Stalnaker's "Assertion", quoted at length in this work -->
<!-- inactive-ok-file: THEORY-162 — Proposed; filed from this reading -->
<!-- inactive-ok-file: CLAIM-061 CLAIM-054 — Proposed; open, and cited as open: the claim is under test, not settled -->

# NOTE-608: The Semantics of Definite and Indefinite Noun Phrases

## Contribution

Before this work, the indefinite article was analysed as an existential
quantifier (Russell), and its use as an antecedent for pronouns outside
its scope ("A dog came in. It lay down"; "Every man who owns a donkey
beats it") was handled by text-wide binding (Geach, Egli, Smaby),
pragmatic salience (Grice, Kripke, Lewis), pronouns as definite
descriptions (Evans, Cooper, Parsons) or an ambiguity hypothesis
(Strawson, Chastain). Heim argues each fails somewhere and proposes that
indefinites have no quantificational force at all: they are variables
bound by whatever operator is nearest. She then gives a second,
better-motivated version in which sentence meanings are file change
potentials, and in which definiteness is a single felicity condition. Kamp's
discourse representation theory reached closely similar ideas
independently in the same period; Heim says so and does not compare the
two.

## Key insight

An utterance does not just narrow down the ways the world might be; it
also opens and updates "cards" for the things talked about. An indefinite
opens a new card; a definite or pronoun must find an old one. That one
difference explains why indefinites seem to quantify (a new card can be
filled by anything that fits, so truth comes out existential, or
universal under "every" and "always"), why definites seem to refer (they
are tied to a card already in the common ground, by mention or by
salience), and why two sentences with the same truth conditions can
differ in what a following pronoun can pick up.

## Assumptions

- **Logical form**: syntactic structures are mapped by construal rules
  (NP-indexing, NP-prefixing, quantifier construal) to indexed,
  tripartite operator structures [Q, restrictor, nuclear scope]. In
  ch. II there are also obligatory rules of existential closure and
  quantifier indexing and a Novelty Condition; ch. III removes them.
- **Extensional semantics** for most of the work; modals and conditionals
  get an intensional treatment after Kratzer (modal base, ordering
  source) in ch. II §4.
- **Singular NPs only** ("the limitation to singular NPs will in fact be
  maintained throughout"); plurals, generics and specific indefinites are
  set aside or only sketched.
- **Assertion only**: the file change described is the essential effect
  of assertions, following Stalnaker, and only when not rejected.
- **Common ground idealised**: all participants presuppose the same
  things ("nondefective" contexts).
- **Principle (B)**: a file constrains the n-th member of its satisfying
  sequences only if it has a card n.

## Key results

- **Ch. I.** Counterexamples to each rival: the marble pair (21a/b) and
  "John has a spouse / John is married. She is nice" (truth-conditionally
  equivalent, different anaphoric potential) against salience accounts;
  "If someone is in Athens, he is not in Rhodes" and the sage-plant
  sentences against uniqueness in E-type accounts; *most* and
  *in most cases* against Egli's and Smaby's exportation rules. Common
  conclusion: (a) indefinites are existential quantifiers, (b) they
  obey the same scope islands as other quantifiers, (c) pronouns are
  bound or referential — cannot all be true.
- **Ch. II §1–3.** Lewis's adverbs of quantification are unselective and
  bind all free variables in their restrictor; Heim adds that the free
  variables come from indefinites. Satisfaction semantics for indexed
  logical forms; existential closure at text level and in nuclear
  scopes; a Novelty Condition (an indefinite may not be coindexed with
  any NP to its left).
- **Ch. II §4.** Bare conditionals contain an unpronounced necessity
  operator restricted by the if-clause; under realistic modal bases and
  ordering sources, "If a man owns a donkey, he beats it" entails the
  universal ∀x∀y((man x ∧ donkey y ∧ own x y) → beat x y) but can say
  more (dispositions). Generic indefinites restrict an invisible
  operator, with non-realistic (stereotypical) ordering left open.
- **Ch. II §5–7.** Indefinites can be anaphorically related to pronouns
  outside their scope, like names and unlike *every*/*no* NPs; scope
  islands and weak crossover are accommodated; Karttunen's "discourse
  referents" and their lifespans are reconstructed as indices and
  operator scopes, explaining why negation, quantifiers, modals and
  attitude verbs all close off discourse referents. Specific indefinites
  and Karttunen's extended referents ("You must write a letter… It has
  to be sent by airmail") remain unexplained.
- **Ch. II §8.** Definiteness = three independent properties: no
  operator indexing, no Novelty Condition, presupposed descriptive
  content.
- **Ch. III §1.** Principle (A): Sat(F + φ) = Sat(F) ∩ {a : a sat φ}.
  Files versus Stalnaker's context sets: a file determines a world set
  (the context set), but files with the same world set can evolve
  differently under the same utterance, so the common ground needs more
  structure than a set of worlds.
- **Ch. III §2.** Novelty-Familiarity Condition: indefinite index ∉
  Dom(F), definite index ∈ Dom(F), else infelicitous; deixis is reading
  a card created by salience. Felicity of a complex formula = felicity of
  every elementary update step, which projects presuppositions without a
  separate projection rule.
- **Ch. III §3.** Truth criterion (C): φ is true w.r.t. F if F + φ is
  true, false if F is true and F + φ false. Free indefinites get
  existential truth conditions from this (proved for the woman–dog
  example), so text-level existential closure is unnecessary; (C') for
  false files is left vague.
- **Ch. III §4.** File change rules for universal quantification and
  negation in three and two steps; selection indices replaced by
  reference to Dom(F), and nuclear-scope existential closure built into
  the interpretation rule. Final rules (I)–(IV).
- **Ch. III §5.** Extended Novelty-Familiarity Condition (familiar card
  and entailed descriptive content); accommodation with "bridging" to
  existing cards; global accommodation preferred to local; paycheck
  pronouns and "prominence by proxy"; information-preserving
  accommodation licenses the Karttunen cases with *know* and with
  modal subordination (pp. 392–394).
- **Ch. III §6.** Four arguments for file change semantics: conjunction
  is privileged, presupposition projection, accommodation interleaved
  with interpretation, and a single principle of definiteness.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Indefinites have no quantificational force of their own; it comes from the binding operator or from the truth definition | moderate | the analysis covers donkey sentences, adverbs of quantification, modals and conditionals (ch. II §1–4); argued, not proved unique |
| C2 | Truth-conditionally equivalent sentences can differ in anaphoric potential, so meaning is not exhausted by truth conditions | strong (data) | marble pair, spouse/married, bicycle-owner (ch. I §1.3) |
| C3 | E-type analyses with Russellian uniqueness give wrong truth conditions for donkey conditionals | strong for the cases given | Athens/Rhodes, sage plants (ch. I §2.3) |
| C4 | A common ground must be finer than a set of worlds to predict how it changes | moderate | files with equal world sets diverge (ch. III §1.4); depends on treating open formulas as update units |
| C5 | Definiteness reduces to familiarity with respect to the file (with descriptive content entailed) | moderate | derivation of binding, deixis/anaphora unity and narrow-scope definites (ch. III §2–5); accommodation is under-specified |
| C6 | File change semantics solves the presupposition projection problem | weak here | one worked example; full treatment deferred to separate work |
| C7 | Specific indefinites, weak crossover with indefinites and extended discourse referents are not explained | stated limitation | ch. II §5.4, §7 |

## Method

Model-theoretic semantics of a fragment of English via indexed logical
forms, tested against acceptability and truth-value judgements on
constructed examples, with comparison to rival analyses case by case.
In ch. III the interpretation is moved from satisfaction conditions to
file change potentials and the construal component is simplified.

## Concepts

- **file**: a common ground with a domain (card numbers) and a
  satisfaction set (sequences of individuals, per world).
- **file change potential** (F + φ): the function from files to files a
  logical form denotes.
- **novel / familiar** (w.r.t. a file): index not in / in Dom(F).
- **Extended Novelty-Familiarity Condition**: indefinites novel;
  definites familiar with descriptive content entailed by the file.
- **accommodation**: repairing a felicity failure by adding a card,
  linked to existing cards ("bridging"); global or local.
- **unselective quantifier**: an operator binding every free variable
  its restrictor introduces (after Lewis 1975).
- **discourse referent**: Karttunen's notion, identified first with
  referential indices, then with file cards.
- **prominence**: the small set of recently handled cards a pronoun
  may use.

## Connections

Built on Lewis's "Adverbs of quantification" (1975) and "Scorekeeping in a
language game" (1979, accommodation), Kratzer's modality, Karttunen's
discourse referents and presupposition work, and Stalnaker's
"Assertion", whose account of the common ground and of assertion's
essential effect (eliminating the possibilities incompatible with what
is said, unless the assertion is rejected) it quotes and adopts,
refining the context set into a file. Kamp (1981) is acknowledged as
independent and closely similar; Hintikka and Carlson's game-theoretical
account is assessed at the end of ch. I. Veltman ([LIT-818](../literature.d/LIT-818.md)) later
credits this work as one origin of update semantics.

## Bearing on the record

- Source, with Veltman and Krifka, of [THEORY-162](../theory.d/THEORY-162.md): what an utterance
  does to a context is part of its meaning and is not fixed by its truth
  conditions. Heim's anaphora pairs are the cleanest evidence for it
  read in the record.
- **[CLAIM-061](../claims.d/CLAIM-061.md)** (proposition neither necessary nor sufficient for
  the communicative event): the marble and spouse pairs show, for
  anaphoric potential, that sameness of proposition does not fix what an
  utterance makes available for what follows. That is the "not
  sufficient" half, for a dimension (discourse referents) other than the
  footing and force the claim names.
- **[CLAIM-054](../claims.d/CLAIM-054.md)** (interpretive and performative fidelity come
  apart): no direct bearing; Heim restricts herself to assertion.
- Stalnaker's "Assertion" ([LIT-811](../literature.d/LIT-811.md)), unread here, is quoted in
  ch. III §1.4 (pp. 321, 323 of the essay), which is the record's only
  first-hand access to its wording; Heim cites the volume as 1979.
- No instruction for ML practice; nothing for the anthology.

## Limitations

- Singular NPs only; plurals, generics and specific indefinites are
  outside the theory or sketched.
- Accommodation's conditions (bridging, global preference, prominence by
  proxy, information preservation) are described, not derived.
- Truth for utterances against false files, (C'), is vague by the
  author's admission.
- The projection-problem claim rests on one example; the full treatment
  is deferred.
- The evidence is introspective judgement on constructed sentences.
- The author calls the dissertation "a rough draft" in the preface.

## Open questions

- How a static rival (E-type or situation-based accounts, developed
  later) handles the marble and spouse contrasts without file change.
- The general conditions on accommodation, and why accommodated cards
  must be bridged.
- How Karttunen's extended discourse referents (modal subordination)
  are licensed in general; pp. 392–394 give a sketch through
  information-preserving accommodation.
