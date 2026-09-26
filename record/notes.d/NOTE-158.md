---
number: 158
status: Read
formerly:
- NOTE-tmpqmp2c
paper: LIT-208
title: 'Grindrod et al. — Distributional semantics & holism'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv v2 (25 pp. incl. references), every
    section §§1–6 and all footnotes. I also compared v1 (24 pp.) against v2
    by sentence-level diff; the changes are editorial, with a rewritten
    abstract and opening but the same argument and data. The OUP chapter
    version (Cappelen & Sterken, eds., DOI 10.1093/9780191998317.003.0004)
    was not read.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  The authors argue that distributional models answer the instability
  objection to meaning holism if meaning is read "differentially", as a
  word's relations to its nearest neighbours, and not as its position in
  the space. They illustrate this with two corpus-expansion
  demonstrations. In a ±10-word count model on Stein's The Making of
  Americans (about 522k tokens), adding Hemingway's "A Clean, Well-Lighted
  Place" (under 1,500 words) shifts every cosine value for "know" by at
  most about 0.0005 (e.g. 0.95231 → 0.95284 for "understand") and leaves
  its top-10 neighbours in the same order, while "glass" gets a new
  neighbourhood. A Word2vec CBOW model on 143M words of Wikipedia shows
  the same pattern when about 21M words of the Stanford Encyclopedia of
  Philosophy (SEP) are added: "atomism" shifts, "can" barely moves. The
  residual instability, they argue, is a virtue.
---

<!-- inactive-ok-file: LIT-208 — Deferred: the paper is placed by this reading; the directive lapses when its status changes; the directive lapses when its status changes -->

# NOTE-158: Grindrod et al. — Distributional semantics & holism

## Contribution

The paper sets the classic instability objection to meaning holism (Fodor & Lepore 1992; Lormand 1996; Pagin's "total change thesis") against actual distributional models. It argues that the objection loses its force once meaning similarity is read differentially, in terms of neighbour relations that survive rotation, change of dimensionality or alignment across spaces, and it builds two small models to show what corpus expansion does and does not change. It also answers Fodor & Lepore's objections to vector-space similarity (§4). Their "which dimensions?" objection assumes semantically interpretable dimensions, which distributional dimensions are not. Their "no comparison across spaces" objection is met by nearest-neighbour comparison, as used in Hamilton et al.'s (2016) Procrustes-aligned diachronic embeddings.

## Key insight

In a distributional model the "space" is a metaphor for a network of word-to-word relations; Hesse's network model is the better image (§4, pp. 11–12). So a word's meaning is its neighbourhood, not its coordinates. Adding language moves every coordinate and every similarity value slightly, but a word used frequently and consistently keeps its neighbourhood. Only heavily re-used, previously rare words, such as "glass" in a café story, move much. Holistic instability is then local and graded, not total, and the local part is what lets the model register real meaning change.

## Assumptions

- **Distributional hypothesis** (Harris 1954; Firth 1957): terms similar in meaning have similar distributions across a corpus.
- **Holism as determination by relations, not priority** (Dresner 2012, p. 611): relations among expressions are constitutive of what they mean. The whole-over-part priority reading (Quine; Frege's context principle) is set aside (§2).
- **Linguistic, not mental, holism.** The concern is linguistic entities, and Fodor & Lepore's extension of the objection to intentional generalization is set aside (§3).
- **Distributional models represent meaning**, or at least may be treated as doing so for the argument. The sufficiency and "reverse engineering" worries (Bender & Koller 2020; Lenci 2008; Boleda 2020) are bracketed (§2).
- **A simplified picture of communication:** success means speaker and hearer identify the same or similar content. Brandom's inferentialist alternative is acknowledged and not adopted (fn 15).
- **Transformers remain distributional at their core.** Contextual embeddings from self-attention are "not a fundamental departure" (§1, p. 5). RLHF-tuned chat models are flagged as departing from the pure approach (fn 10). All experiments nevertheless use static models: a count model and Word2vec.

## Key results

What it argues and reports:

- **§4 (meaning similarity):** Goodman's "similar in some respect" worry is answered by a metric (cosine, Euclidean, city-block). The dimension-selection worry does not apply, because distributional dimensions are co-occurrence counts or uninterpretable reduced or learned features, not semantic properties. The choice of dimensionality is an empirical parameter, tunable against benchmarks such as GLUE. Cross-space comparison works through nearest-neighbour lists, which are invariant under rigid rotation and comparable across dimensionalities.
- **Count model (§4, pp. 12–17):** ±10-word window on The Making of Americans. "know" has nearest neighbours understand 0.95231, it 0.94286, see 0.93759, think 0.93293, and so on (Table 4). After adding "A Clean, Well-Lighted Place", all ten values move in the 4th or 5th decimal place and the order is identical (Table 6). "glass" (2 uses in Stein, 5 in Hemingway) changes from chandeliers, prisms, brocade … to saucer, waiter, table, leaves, sun … (Table 5). The new word "nada" (21 uses) is connected to Stein-only words through shared vocabulary, for example cosine .17188 to "hersland".
- **Word2vec model (§4, pp. 18–20):** CBOW on Wikipedia, with and without SEP. "atomism" (9 Wikipedia uses, 662 in SEP) reorders its neighbours and gains new ones (literalism, common-sense, stoics, metaphysics) (Table 7). "can" keeps could, must, will, should, might, would, shall, tends, with values changing by ≤0.003 and a swap at positions 9–10 (Table 8).
- **Stability with scale (§4 end):** as more observations fix the positions of common nodes, rare words are "knotted into regions", and the corpus becomes "quite resistant to big changes from small sources". This is argued with the network metaphor and a citation to Antoniak & Mimno (2018).
- **Stronger thesis (§5):** instability is "a positive feature". Its sensitivity detects speaker–hearer differences and diachronic change, citing Hamilton et al. 2016 on "awful", "wanting" and "starting".
- **Sufficiency objection (§5):** communicative success is graded, or its threshold is empirical (after Haugeland 1979).
- **Conclusion (§6):** the view sides with Hesse's network theory against Davidson (via Rorty 1987's gravity analogy). LLMs may make it unnecessary to "idealise away from minor perturbations in meaning".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Distributional models are holistic in Dresner's sense | strong | conceptual argument from how the vectors are built (§§1–2); near-definitional |
| C2 | Fodor & Lepore's dimension-selection objection does not apply to distributional spaces | moderate | informal argument that distributional dimensions are not semantic properties (§4). The residual dimensionality question is handed to empirical tuning. |
| C3 | Nearest-neighbour relations give a notion of meaning similarity comparable across spaces and dimensionalities | moderate | informal argument plus the precedent of Hamilton et al. 2016 (§4). Rotation invariance of cosine and Euclidean measures is standard. |
| C4 | Small corpus additions leave a frequent word's neighbour ordering intact while all its similarity values change | weak–moderate | two demonstrations with one word each ("know", Table 6; "can", Table 8). Top-10 only, one run, no metric. |
| C5 | Heavy use of a previously rare word shifts its meaning noticeably | weak–moderate | two demonstrations ("glass", Table 5; "atomism", Table 7) |
| C6 | A word's resistance to change is "roughly proportional to its frequent and consistent use" (abstract) | weak | not measured. It is inferred from the four words above and the network metaphor, and the abstract states more than the body shows. |
| C7 | Models become more stable as the corpus grows | weak (as the authors' own finding) | a citation to Antoniak & Mimno 2018; the authors' own data has two sizes per model |
| C8 | The residual instability is a virtue (detects idiolect and diachronic change) | weak | argument by appeal to Hamilton et al. 2016; no new evidence |
| C9 | Communicative success need not have a model-given similarity threshold | weak | two informal responses (graded success; an empirical, Haugeland-style test), neither developed (§5) |
| C10 | Transformer LLMs inherit the analysis because they are distributional at their core | weak | an assertion in §1, with no experiment on contextual embeddings |

## Method

Two demonstrations of corpus expansion, compared before and after.

1. **Count model:** lower-cased tokens and a ±10-word symmetric window, with the target token excluded but other tokens of the same type counted (fn 22). Rows are target words and columns are raw collocate counts, with no PMI weighting or dimensionality reduction reported. Similarity is cosine (1 − scipy pdist cosine distance). The top-10 neighbours of selected words are compared between Stein alone and Stein + Hemingway.
2. **Word2vec CBOW model:** a random sample of 372,194 Wikipedia articles, then the same sample plus all 1,763 SEP articles. Top-10 neighbours of selected words are compared between the two. Hyperparameters (dimension, window, epochs, min-count) and the number of runs are not reported.

## Concepts

- **meaning holism** — relations of some kind among many or all expressions of a language are constitutive of what each means (Dresner 2012). It is distinguished from priority holism.
- **instability objection** — if meaning is holistic, any change ripples through the system, so speaker and hearer never share meanings. Its strongest form is Pagin's (2008) "total change thesis".
- **absolute vs differential instability** — change in a word's position in the space vs change in its relations to other words. The abstract defines the latter as change in relative distances. In practice (Tables 6 and 8) it is judged by whether the ranked nearest-neighbour list is preserved.
- **differential treatment of meaning similarity** — meaning is read off nearest neighbours, not coordinates. This reading is invariant under rotation and usable across spaces of different dimensionality.
- **sufficiency objection** (as used here) — the demand for an account of how similar meanings must be for communication to succeed.

## Connections

The paper responds to Fodor & Lepore (1992, 1996, 1999) and their critique of Churchland's vector-space semantics. It appeals to Churchland (1998) on cross-space similarity, and borrows from computational semantics: Hamilton et al. 2016 on diachronic embeddings with orthogonal Procrustes alignment, Antoniak & Mimno 2018 on embedding stability, and Mikolov et al. 2013. Its philosophical allies are Hesse (1974, 1988) and Rorty (1987), against Davidson. It builds on Grindrod's own "Distributional theories of meaning" (2023) and "Modelling Language" (2024).

In this record it sits beside [LIT-106](../literature.d/LIT-106.md) (Brandom's inferentialism, which the paper mentions as one holist strand) and [LIT-153](../literature.d/LIT-153.md) (Making sense of transformer success), which is about explaining transformer competence, not about meaning holism.

**philosophy-of-science:** the question addressed is a question in philosophy of language: whether holistic, relation-constituted word meaning is compatible with stable enough meaning for communication. The position taken is yes, if similarity is differential, and the residual instability is a feature. It does not address realism, explanation, causation, evidence, or the structure or interpretation of a scientific theory. Confirmation holism appears only as lineage (§2), and the tag is not justified (see corrections).

## Bearing on the record

No THEORY document in this record is sourced to it. For the Anthology of the SOTA, it restates, without testing, a practice the ML literature already holds: compare embedding spaces by neighbour sets or after orthogonal alignment, not by raw coordinates or raw similarity values, and expect low-frequency words to be unstable. The operational source for that practice is Antoniak & Mimno (2018), which the paper cites, and which the anthology would file directly if it wanted the practice. This paper adds no measurement to it. Nothing here warrants a transfer, and an `anthology-candidate` flag is not recommended.

## Limitations

- The empirical part is illustrative. It covers four words, top-10 lists, a single run per corpus, no stability metric (such as neighbour-set Jaccard or rank correlation) and no frequency sweep. The abstract's proportionality claim (C6) outruns this.
- The authors raise run-to-run randomness in Word2vec but do not report repeated runs. So the "atomism" and "can" contrasts cannot be separated from seed noise at the positions where "can" swaps (9–10).
- Static embeddings only. The claim that transformer LLMs inherit the analysis is asserted, not shown, even though contextual embeddings are the case the title's "language models" framing invites.
- The operative criterion (a preserved neighbour list) and the defined one (relative distances) diverge, and the paper does not reconcile them.
- The authors themselves bracket whether distributional models capture meaning at all (§2) and use a simplified model of communication (fn 15). The conclusions are conditional on both.
- Minor errors: the type-token figure (5,317 vs "5780") and "two novels" for a novel plus a short story.

## Open questions

- Does differential stability hold for contextual (transformer) representations, where a word has no single neighbourhood? A study of neighbour-set stability of contextual embeddings under continued pretraining would settle it.
- Is resistance to change actually proportional to frequency and consistency of use? A regression of neighbour-set turnover on log frequency across corpus increments and seeds would settle it. Antoniak & Mimno report related results, but not in this form.
- What is the threshold of similarity for communicative success? The authors defer it to an empirical, Haugeland-style test that nobody has run.

## Corrections to the seeded skim

- The dossier misreads the sufficiency objection. §5 does not ask whether distributional relations suffice for meaning; §2 explicitly sets that worry aside (Bender & Koller 2020; the "reverse engineering" reading). The §5 objection is that the account still owes a threshold for how similar speaker and hearer meanings must be for communication to succeed. Two answers are offered: communicative success is graded and failure is only labelled when noticed (the marrowfat-peas example), or the threshold is an empirical question, settled Haugeland-style by watching communicators' complaints.
- The abstract's claim that a word's "resistance to change … is roughly proportional to its frequent and consistent use" is not measured. The body shows four words (know/glass, can/atomism) and one before/after pair per model. No proportionality is estimated. The general claim that models "become more stable as they increase in size" (§5) rests on citing Antoniak & Mimno (2018), not on the authors' own data, which has only two corpus sizes per model.
- The operative stability criterion is not quite what the abstract defines. "Differential instability" is defined as variation in the relative distances between points. But the demonstrations show those relative distances (cosine similarities) do change, and they call meaning stable when the ranked nearest-neighbour list is preserved (Table 6, p. 17). The criterion actually used is preservation of neighbour ordering or membership.
- There is a small factual slip the skim repeated in part. The count corpus is one novel plus one short story, not "two novels" (v1's abstract and §4's opening say two novels). §4 gives Stein's vocabulary as 5,317 unique words but computes the type-token ratio as "5780 / 522,000". 5,780 is the figure given for The Great Gatsby in footnote 21. The ratio is about .01 either way.
- The Word2vec setup, unstated in the skim: CBOW, 372,194 Wikipedia articles (about 143M words; 1,202,353 types) plus all 1,763 SEP articles (about 21M words; +34,330 types), roughly a 15% increase in tokens. The Hemingway addition was about 0.3% of tokens and +94 types (1.8%). The authors raise run-to-run randomness (fn 30) but report no repeated runs. Dimensionality, window and epochs are not given.
- The confirmed section plan is §1 distributional semantic models; §2 meaning holism; §3 the instability objection; §4 meaning similarity; §4 (repeated number) modelling the instability objection; §5 the sufficiency objection; §6 conclusion. The skim's plan is right.
- philosophy-of-science tag: not justified. The work is philosophy of language: meaning holism, meaning similarity and communicative success. Confirmation holism (Duhem–Quine) and Hesse's network model, whose source is The Structure of Scientific Inference, appear only as the lineage of the holism it defends. It takes no position on what science is, how theories relate to the world, explanation, causation or evidence. The one argument that could qualify, that LLMs make idealising away small meaning perturbations unnecessary (§6, via Rorty's gravity analogy), is about semantics, not scientific method. The vocabulary has no word for philosophy of language. The honest remedy is to add one (for example `philosophy-of-language`, with a decision), not to keep the nearest wrong tag. Until then `linguistics` alone is the right subject tag, as on [LIT-106](../literature.d/LIT-106.md).
- primary topic: linguistics (unchanged). If a philosophy-of-language topic is added, it should lead.
