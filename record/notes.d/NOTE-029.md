---
number: 29
status: Read
formerly:
- NOTE-tmp1kp6n
paper: LIT-031
title: 'Krauska & Lau 2023, moving away from lexicalism'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of the published article, Frontiers in Language
    Sciences 2:1125127 (Hypothesis and Theory; received 15 Dec 2022,
    accepted 26 Jan 2023, published 13 Feb 2023). This is the 17 pp. CC BY
    PDF from frontiersin.org, extracted with PyMuPDF to rawC4/c62.full.txt.
    I read §§1–4, all eight footnotes, the figure captions (Figs. 1–6) and
    the back matter (author contributions, funding: NSF BCS-1749407,
    acknowledgments). I read the reference list only to check citations. The
    figures are diagrams, and only their captions survived extraction. I did
    not read the PsyArXiv preprint (doi 10.31234/osf.io/vyf94) or the
    "Krauska and Lau (in prep.)" model paper the article points to.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  The authors argue that lemma-based production models encode two
  lexicalist assumptions: a morphology/syntax split, and a stored
  meaning–syntax–form "triad". On that basis the models mishandle
  Inuktitut polysynthesis, separable Vietnamese idiomatic collocations,
  Hiaki number suppletion and English verb–object idioms. Updating the
  representations (treelets) is not enough, because the algorithms —
  separate lexical retrieval and structure building, word-sized increments
  — also have to change. They sketch an 8-stage non-lexicalist model and
  derive qualitative aphasia predictions from it. There are no new data
  and no implementation.
---

<!-- inactive-ok-file: LIT-031 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-029: Krauska & Lau 2023, moving away from lexicalism

## Contribution

The paper takes the anti-lexicalist conclusion from theoretical linguistics as given. It traces how lexicalism is built into psycholinguistic production models:
- Levelt's lemma, and Levelt & Indefrey (2000);
- the Consensus Model (Ferreira & Slevc 2007);
- incremental planning in "lexically sized units";
- treelet models (Kempen, Vosse & Kempen, Ferreira, Matchin & Hickok).

It shows, with specific cross-linguistic cases, where each one fails. Its distinctive claim is that the problem is algorithmic as well as representational. As long as lexical retrieval and structure building are separate stages, swapping in richer representations does not help. It then outlines a replacement with separate meaning→syntax and syntax→form mappings over fully abstract syntactic atoms, and a single integrated retrieve-and-build stage.

## Key insight

A lemma is a bet that meaning, syntax and form line up one-to-one-to-one at the word. Once that bet is dropped, retrieval of stored pieces and structure building cannot be separate stages. The unit of storage then has no architecturally fixed size, and word-like "lemmas" can survive only as an implementation-level optimization for items whose mappings happen to be symmetric.

## Assumptions

- **Linguistic theory.** The non-lexicalist theories are taken as correct: Distributed Morphology, Nanosyntax, and Preminger's (2021) "non-semiotic" approach. Syntactic terminals "are fully abstract, meaning that they have no form or meaning themselves" (p. 11).
- **Universal cognitive processes.** "All languages utilize the same underlying cognitive processes" (p. 2). This is why a phenomenon that is exceptional in English but common elsewhere counts against a model.
- **The two lexicalist assumptions (p. 2):**
  1. syntactic and morphological processes differ in kind;
  2. lexical items are triads of sound, meaning and syntax.

  A model counts as lexicalist if it makes either assumption. So treelet models, which reject (1), still count as lexicalist by (2).
- **Marr's levels.** Lemma-like storage is allowed at the implementation level but denied at the representation or algorithm level (p. 8).
- **Neural localization is imported, not tested.** Relational representations sit in the left temporal lobe and control and linearization in the left frontal lobe (p. 12). Syntactic processing sits in pMTG/STS "consistent with Matchin and Hickok (2020)" (p. 15).
- **All produced material is syntactic.** Every phonological word or phrase has a syntactic representation. There are no direct meaning→form mappings, unlike Caramazza's (1997) Independent Network Model or Jackendoff's Parallel Architecture. The authors flag this as "an important open question" (p. 14).

## Key results

This is a hypothesis-and-theory paper. Its "results" are arguments and a model outline.

- **Inuktitut (§2.1.1; (1), Figs. 1–2).** The example is *havauti-tuq-ti-taq-niaq-tara*, "I'm going to give her medicine frequently" (1c). A lemma model can do one of two things:
  - store a lexical concept for every such word, which is implausible and redundant;
  - put a massive set of diacritics on the "medicine" lemma. Those diacritics are rarely used, productive, and only linearly ordered, so they cannot express the hierarchical structure inside words (fn. 2, *unlockable*).

  Conclusion: morphemes need their own stored units, and words are built during production the way sentences are.
- **Vietnamese idiomatic collocations (§2.1.1; (2); Noyer 1998).** *nhà cửa* 'house', *đèn sách* 'study' (N+N functioning as a verb), and *vườn tược* (where *tược* has no independent meaning) are single lexical concepts, but their parts can be separated by syntax. Superlemma accounts (Cutting & Bock 1997; Sprenger et al. 2006; Kuiper et al. 2007) fail, because they require every part to have its own literal lemma and they specify phrasal functions only.
- **Hiaki suppletion (§2.1.2; (3), Fig. 3; Harley 2014).** Some verbs supplete for subject number and others for object number, e.g. *me'a*/*sua* 'kill.sgObj/plObj'. Meanwhile regular verbs do not inflect for person or number, so lemma diacritics for subject and object number would be redundant. This is "suppletion based on a larger piece of syntax" (p. 6).
- **Verb–object idioms (§2.1.2; (4)).** Examples are *pass/take/get/kill* + object. A homophony account makes the shared irregular past (*took*) a coincidence. A polysemy account needs extra conceptual machinery. A superlemma account concedes that one concept maps to a syntactic complex, which the authors call "a step in the right direction" (p. 7).
- **Incrementality (§2.1.3).** "Lexically sized" planning increments (Dell et al. 2008; Brown-Schmidt & Konopka 2015) presuppose one-to-one mappings. Object-conditioned Hiaki suppletion is the clearest problem, since the verb's form depends on an object not yet planned (p. 8).
- **Treelets (§2.1.4).** They reject assumption (1) but keep the triad and word- or phrase-sized storage. So they still fail on Inuktitut (a treelet per possible word, some of them whole sentences), on Hiaki, and on Vietnamese if treelets are atomic.
- **Lemmas as optimization (§2.1.5).** "Lemmatization" may arise for items with consistent symmetric mappings. Storage of frequent units of any size is expected, including phrases, multiword expressions (Sag et al. 2002) and "groups of words with high transition probabilities" (p. 9).
- **Algorithms (§2.2).** Levelt & Indefrey insert lemmas into slots as they are retrieved, which fails on Vietnamese. The Consensus Model separates content processing from structure building, which fails on Hiaki, since syntactic number is not available at morphophonological retrieval (fn. 4, on syntactic vs semantic number: *scissors*, *furniture*). Building the structure after retrieval fails on verbs whose syntactic arguments are unplanned (fn. 5, *devour*). The resolution is "a single unified process of syntactic structure building" (p. 11).
- **The non-lexicalist model (§3.1; Figs. 5–6).** Knowledge is represented as three things:
  - syntactic atoms;
  - meaning↔syntax mapping rules;
  - syntax↔form mapping rules.

  The mappings can be asymmetric: in *went off*, [PAST]+[GO]→*went*, and [GO]+[OFF] together carry the meaning 'ring'. They are "probabilistic", as "a calculation over larger or smaller pieces of syntax" (p. 11). Eight stages:
  1. message generation, interactive with syntax (Turkish evidentiality; Slobin 1996);
  2. message→syntax mapping, with retrieval integrated into building;
  3. pre-syntactic prosody;
  4. syntax→phonological segments, including non-constituent spans (*I'll*, *dyawanna*);
  5. cognitive control for linearization, where the phonology mapping is "also sensitive to linear transition probabilities" (p. 13);
  6. local phonology and buffer;
  7. post-syntactic prosody (dative alternation, Anttila et al. 2010; Irish pronoun postposing, Elfner 2011);
  8. articulation.
- **Aphasia (§3.2).**
  - Damage to syntax building could give fluent, apparently well-formed output that masks syntactic errors (paragrammatism; Matchin et al. 2020).
  - Agrammatic deficits in inflection may reflect cognitive control over linearization. This is consistent with Kalaallisut non-fluent aphasics producing accurate inflection with a fixed morpheme order but fewer words per utterance (Nedergaard et al. 2020).
  - Regular vs irregular deficits vary across languages (Faroqi-Shah 2007), which the model attributes to frequency and predictability of the syntax→form mapping.
- **Conclusion on wordhood (§4, pp. 15–16).** The intuitive word is neither a unit of meaning (expletive *it*, idioms) nor a unit of syntax (Inuktitut, Vietnamese) nor a unit of phonology (*dyawanna*). The intuitions "could correspond to units of certain written languages" (p. 16).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Standard production models (Levelt; Consensus; incremental "lexical units"; treelets) embed one or both lexicalist assumptions | strong | textual analysis of the cited models, §2 |
| C2 | Lemma models cannot represent polysynthetic words without implausible storage or unstructured diacritics | moderate | informal argument over three Inuktitut examples (1). It considers the two obvious encodings, not every possible one |
| C3 | Separable idiomatic collocations (Vietnamese) defeat both simple lemmas and superlemmas | moderate | argument from three examples from Noyer 1998 and the published superlemma assumptions |
| C4 | Object-conditioned suppletion (Hiaki) defeats word-sized incremental planning and the content/structure split | moderate | argument from Harley 2014 data. Eberhard et al. (2005) is conceded to handle it partly (p. 10) |
| C5 | Moving away from lexicalism requires changing algorithms, not just representations | moderate | the paper's central argument, §2.2. It is shown for the specific models discussed, not in general |
| C6 | "Linguistic research ... has provided strong evidence against" lexicalism | weak (in this paper) | asserted and delegated to cited literature. The paper declines to argue it (p. 2) and does not mention published dissent, e.g. Müller 2018's reply to Bruening |
| C7 | The 8-stage non-lexicalist model accounts for the phenomena of §2 | weak | verbal sketch. There is no implementation, simulation or data, and the full model is "in prep." (p. 11). Coverage is claimed, not shown |
| C8 | Syntax-building damage yields fluent output that hides syntactic errors, and agrammatic inflection deficits reflect cognitive control | weak | hypothesis. The Kalaallisut aphasia data (Nedergaard et al. 2020, 5 case studies) are cited as consistent, not as a test |
| C9 | Wordhood intuitions do not correspond to any unit of spoken-language meaning, syntax or phonology, and may be orthographic | weak | informal argument with a handful of examples, and speculation ("It could be", p. 16) citing Hoosain 1992 |
| C10 | Lemma-like storage may arise as language-specific implementation-level optimization | weak | conjecture, framed as "an interesting empirical question" (p. 8) |

The abstract says the non-lexicalist model "provides better cross-linguistic coverage and aligns better with contemporary syntactic theory". Alignment follows from the model's design. Better coverage is argued only for the phenomena selected in §2, and only against specific models.

## Concepts

- **lemma**: Levelt's (1989; Levelt et al. 1999) stored representation. It carries a word's syntactic information and diacritic parameters (number, tense, ...), points to a lexical concept and to morpheme forms, and is a syntactic terminal (p. 3, Fig. 1).
- **lexicalism** (as used here): any theory making assumption (1) (morphology and syntax differ in kind) or assumption (2) (the lexical item is a triad). This is broader than the lexicalist hypothesis in Bruening's sense, which is (1) only.
- **triad**: the stored, context-independent linkage of one meaning, one piece of syntax and one form (p. 2; §2.1.2).
- **symmetric vs asymmetric mapping**: whether a meaning component, a piece of syntax and a form segment line up one-to-one-to-one (Fig. 5; the *went off* example).
- **treelet**: a lexicalized elementary tree stored as a lexical item (Kempen & Hoenkamp 1987; Vosse & Kempen 2000; Ferreira 2013; Matchin & Hickok 2020).
- **lemmatization / language-specific optimization**: storage of symmetric mappings as unit-like shortcuts, treated as an implementation-level phenomenon (§2.1.5).
- **pre- vs post-syntactic prosody**: prosody computed from the message (question vs declarative, focus) vs prosody computed from phonological weight and stress during linearization (§3.1).

## Connections

**Who cites whom.**
- Krauska & Lau cite Haspelmath via the 2017 reprint ([LIT-063](../literature.d/LIT-063.md); they give Folia Linguist. 51, 31–80, doi 10.1515/flin-2017-1005). They cite it twice:
  - in the §1 list of anti-lexicalist works (p. 2);
  - for "there are no good criteria to empirically define wordhood" (p. 2) and "those intuitions are hard to formulate into a coherent hypothesis" (p. 15).
- They cite Bruening 2018 ([LIT-071](../literature.d/LIT-071.md)) once, in the same §1 list.
- Neither earlier work cites this one. Bruening cites Haspelmath 2011.

**Agreement.**
- All three reject a principled morphology–syntax split.
- K&L's "assumption 1" is Bruening's lexicalist hypothesis.
- Their conclusion that intuitive words are not units of meaning, syntax or phonology rephrases, for processing, Haspelmath's §2 (semantics, phonology) and §3 (morphosyntax).
- Their white-space suggestion echoes Haspelmath's (2011, p. 33) written-language-bias hypothesis. K&L do not attribute it to him.
- Their §2.1.5 (storage of frequent units of any size, multiword expressions) agrees with Bruening's §4.4 point that idiosyncrasy and listing cut across words and phrases.

**Parting.**
- **Assumption 2, the triad.** This is the half of K&L's lexicalism that neither earlier paper argues. Bruening explicitly excludes the "rich lexical entries" sense of lexicalist (his p. 2). Haspelmath's biuniqueness section (§3.10) is the closest ancestor: it shows form–meaning mismatches in syntax as well as morphology. K&L instead take their triad argument from DM and from Preminger's non-semiotic view.
- **Framework.** K&L commit to a generative, DM-style architecture with fully abstract terminals. Haspelmath's programme is framework-neutral and comparative. So K&L inherit Bruening's theoretical stance, not Haspelmath's.
- **Phonology.** K&L deny that the intuitive word is a phonological unit (*dyawanna*). Bruening suggests "word" is probably only prosodic. Haspelmath excludes the phonological word from the question.
- **Dissent.** K&L present the linguistic case as settled ("strong evidence"). They do not mention Müller's 2018 published reply to Bruening, which defends a distinct morphology.

## Bearing on the record

- **Nucleation.** There are no THEORY documents to support or contradict. This paper would not by itself source a THEORY about language processing, because its model is unimplemented and its predictions untested (C7–C8).
- **Anthology.** There is no instruction for ML practice, and nothing belongs in the Anthology of the SOTA. Some parallels, all extrapolation and not the paper's claims:
  - The model's syntax→form mapping is "probabilistic" and "sensitive to linear transition probabilities". Its storage of frequent units of any size, crossing word boundaries, resembles how learned subword and multiword vocabularies behave. The paper says nothing about ML or tokenization. Its one computational pointer is Krauska & Feldman (2022), an RNN model of the aphasic regular/irregular dissociation, cited only for the frequency/predictability explanation.
  - [ANTH-THEORY-021](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-021.md) (a model's latent units are not its tokenizer's) and [ANTH-THEORY-022](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-022.md) (a phrase in a word slot is read as a lemma, from [ANTH-LIT-410](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-410.md)) touch the same "unit of storage is not the orthographic word" theme. This paper is not evidence for either.

## Limitations

- **No new data, no implementation, no quantitative predictions.** The model is described verbally over two pages. The authors present it as illustrating that non-lexicalist production models "can easily be constructed" (p. 14), and defer the full model to "Krauska and Lau (in prep.)" (p. 11).
- **The linguistic premise is delegated.** It is asserted as settled without engaging the published counter-arguments.
- **The critique covers named models on selected phenomena.** It does not show that no lemma-style encoding could work. For instance, it concedes that Eberhard et al. (2005) can handle Hiaki object suppletion via feature sharing (p. 10).
- **Localization is taken on.** The neural claims are taken from Matchin & Hickok (2020) and Matchin et al. (2020), not tested.
- **The aphasia predictions are qualitative.** They are also hard to falsify as stated: "appearances can be deceiving", and phonological well-formedness can mask syntactic failure (p. 15). The Kalaallisut support is five case studies.
- **The wordhood-and-orthography conclusion is speculative** and rests on one citation (Hoosain 1992).

## Open questions

- Does an implemented version of the 8-stage model reproduce standard production phenomena (speech errors, picture–word interference, structural priming) as well as lemma models do? The authors' in-prep model is where this should be decided.
- Can the proposed aphasia dissociations be tested? For example: paragrammatic output with hidden syntactic errors in pMTG/STS lesions; cross-linguistic variation in agrammatic inflection that tracks morpheme-order flexibility rather than morphological richness.
- Under what conditions does "lemmatization" arise (§2.1.5)? That is, is frequency or mapping consistency the predictor of unit-like storage, across languages?
- Are there direct meaning→form mappings that bypass syntax, as in Caramazza's (1997) Independent Network Model and Jackendoff's Parallel Architecture? The authors flag this as open (p. 14).

## Corrections to the seeded skim

- **The white-space suggestion is not attributed to Haspelmath.** The seed says the conclusion suggests wordhood "may come from orthographic white space, citing Haspelmath (2017)". In the text (p. 15), Haspelmath 2017 is cited for the prior sentence: wordhood intuitions "are hard to formulate into a coherent hypothesis about linguistic units". The white-space suggestion is the authors' own ("It could be that ..."). The citation attached to it is Hoosain (1992), on readers of scripts without spaces having less developed intuitions.
- **The paper does not rest on c61 and c63 for its linguistic case.** The seed says it "depends on Bruening (c63) and Haspelmath (c61) for the linguistic case". In fact the paper expressly does not argue the linguistic case: "This paper does not elaborate greatly on the arguments against lexicalism" (p. 2). It cites Bruening 2018 and Haspelmath 2017 in a list with Halle & Marantz, Harley, Starke, Siddiqi, Embick and Jackendoff. Its own evidence is drawn from other sources:
  - Inuktitut (Cook & Johns 2009; Briggs et al. 2015);
  - Vietnamese (Noyer 1998);
  - Hiaki (Harley 2014);
  - English verb–object idioms.

  Its model's representational core comes from Preminger (2021).
- **The keywords were available.** The seed says they "were not captured". The article's keywords are: lexicalism, psycholinguistics, neurolinguistics, language production, lemma, aphasia. The seed's own list (which adds morphology and syntax) is not the article's.
- **The aphasia section says more than the seed records.** The seed has it as damage to syntax building yielding fluent but syntactically erroneous speech (paragrammatism), with deficits masked by later well-formedness rules. That is right, but the section makes three more claims:
  - a cognitive-control account of agrammatic (non-fluent) aphasia;
  - a reading of Kalaallisut aphasics' intact inflection (Nedergaard et al. 2020) as consistent with it;
  - the regular/irregular inflection dissociation explained by frequency and predictability, not representation (Faroqi-Shah 2007; Krauska & Feldman 2022).
- **Minor: the seed's list of model stages is incomplete.** The seed's "8 stages" list is right in order but omits that the stages are split into two groups: relational representations and translations (left temporal), and control and linearization (left frontal), per Fig. 6 and p. 12.
