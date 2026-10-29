---
status: Read
paper: 'LIT-tmpog7aw'
title: 'Singh et al. — VakyArth'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the published Findings of EMNLP 2026 PDF (ACL
    Anthology 2026.findings-emnlp.2022, pp. 43027–43041), fetched
    2026-10-29. The arXiv copy 2609.01788v1 (1 September 2026) was also
    fetched; a word-level diff of the extractions differs only in line
    breaks, the arXiv stamp and the proceedings footers. Extracted with
    `pdftotext -layout`. I read the abstract, §§1–7, the references and
    Appendix A (prompts, rating guidelines, the COMET–human divergence
    examples, the error analysis), Tables 1–4 and the captions of
    Figures 1–4. Figure 3's and Figure 4's values are partly legible in
    the extraction; the text's numbers are quoted. Pages are the
    proceedings'. Checks (numpy, my scripts): I recomputed the per-model
    means and the MCQ > NLI count from Table 2, and correlated COMET with
    MCQ and NLI accuracy over its 100 cells. I cloned the released data
    (github.com/Usneek1/VakyArth, commit 6ba83a2 of 2026-08-30), counted
    items per language, phenomenon and task, and tested whether the
    translation items share their source utterances with the MCQ and NLI
    items.
date: '2026-10-29'
summary: >-
  VakyArth is 578 items written by four native speakers, one per language,
  for Hindi, Punjabi, Tamil and Malayalam, over five phenomena and three
  formats. Five LLMs do better on MCQ than NLI in every model–language
  pair, and when wrong they lean to the literal reading. COMET tracks one
  native rater's pragmatic-adequacy scores at r = 0.81. The translation
  items are not the MCQ and NLI items: in the release, 1 of 204
  translation sources overlaps an inference item. So the finding that
  translation "does not track" pragmatic understanding compares different
  items. No agreement between people is reported anywhere.
---
<!-- inactive-ok-file: CLAIM-257 CLAIM-202 THEORY-tmp7mudy THEORY-tmp0k3ls — Proposed; the record's claims this reading bears on and the theories it produces, cited as open -->

# NOTE-tmpruw1i: Singh et al. — VakyArth

## Contribution

The first pragmatics benchmark for Indic languages: 578 items (Hindi 185,
Punjabi 125, Tamil 134, Malayalam 134; Table 1, p. 43031) covering deixis,
speech acts, implicature, social pragmatics and coherence, each phenomenon
in MCQ, NLI and translation format. Five instruction-tuned LLMs (8B–111B) are
evaluated, with a human pragmatic-adequacy rating of a sample of their
translations and a comparison of three automatic MT metrics against it. The
items are culturally specific: "kai nenachu po" as an invitation to stay and
eat, "Beta, kya aaj chutti hai kya?" as a command to get up, "Anjana
chechi" as the required address (pp. 43029–43030).

## Key insight

Models fail toward the literal reading, and do so on the same items. "Across
all wrong-answer events, models chose the literal distractor 59.1% of the
time, nearly twice the 33.3% rate expected by chance (p < 0.001)" (p. 43034);
"when the gold label is Contradiction, models predict Entailment 53.8% of the
time" (p. 43034). For the record, the second lesson is what the benchmark
does not do: its translation items are separate material, so it cannot show
that a model translates fluently what it fails to interpret, or the reverse.

## Assumptions

- **One author per language, the gold label is that author's reading.**
  "All items were written from scratch by a team of four native speakers, one
  per language, each with graduate-level NLP training" (p. 43031). "Each item
  was reviewed by the full team to check for ambiguity, label correctness,
  and translation accuracy" (p. 43031), but only one of the four is a native
  speaker of each language. No second native judgement and no human
  performance on MCQ or NLI is reported.
- **Surface-recoverable items removed.** "Items where the correct answer was
  recoverable from surface cues alone were removed" (p. 43031). How, and how
  many, is not said.
- **Latin transliteration as input**, chosen to reflect everyday typing
  (p. 43031); native script raises MCQ accuracy "(76.5% vs. 70.6%
  accuracy)" pooled (p. 43035).
- **Three-shot prompts in the item's language**, temperature 0.2, 128 new
  tokens (p. 43031; App. A.1).
- **Translation is Indic → English** against one human-authored English
  reference per item; "424 human-authored English reference sentences in
  the translation subcorpus" (p. 43031).
- **Few items per cell.** Table 2 reports each model × language × phenomenon
  × task cell separately. The release has 5 to 16 items per cell (my
  count): Hindi 9–16, Tamil and Malayalam 8–9, Punjabi coherence MCQ 5. One
  item moves a Punjabi coherence MCQ score by 0.20.

## Key results

- **Item counts, checked.** The release has, per language, MCQ / NLI /
  translation items: Hindi 59 / 55 / 71, Punjabi 39 / 42 / 44, Tamil
  45 / 44 / 45, Malayalam 45 / 45 / 44, summing to the paper's 185, 125,
  134 and 134 (my count). So the 578 items are three disjoint task sets:
  204 translation items (the paper's "204 total items", p. 43034) and 374
  inference items. The data README says "The dataset is still growing".
- **Translation items are different utterances.** Of the 204 translation
  sources, one shares 80% or more of its words with any MCQ or NLI item in
  the same language and phenomenon (my script, on the Latin text). The
  same utterance does recur across MCQ and NLI: the Tamil "kai nenachittu
  po" is the NLI example of Fig. 2 and the MCQ of App. A.4, Example 1.
- **MCQ beats NLI.** "MCQ scores are higher than NLI scores in all 20 of 20
  model-language aggregates" (p. 43033); I confirm 20 of 20 from Table 2
  means. In 21 of the 100 phenomenon cells NLI ≥ MCQ. NLI accuracy is at or
  below one third, chance for three labels, in 44 of 100 cells.
- **Model ranking.** Gemma-4-31B "(MCQ 0.86 NLI 0.43 COMET 0.81)"
  (p. 43033); my Table 2 means 0.865, 0.432, 0.806. Command-A 0.74 / 0.46 /
  0.78 as stated. Qwen3-32B has the highest mean NLI (0.466), which the text
  does not mention.
- **Literal bias.** The 59.1% literal-distractor rate is on "the MCQ subset
  where a literal-meaning distractor is unambiguously identifiable"
  (p. 43034); its size is not given. NLI labels are 57.5% Contradiction by
  design (p. 43034). Fig. 3 pools "all four models", though five were run.
- **Shared failures.** "On NLI, 24.7% of items are failed by all four models,
  rising to 41.7% for Social Pragmatics" (p. 43034); again four models.
- **Translation and inference, across cells.** "Translation performance does
  not track MCQ or NLI scores" (p. 43028). No statistic is given. Over the
  100 cells of Table 2, I find r(COMET, MCQ) = 0.29 and r(COMET, NLI) =
  0.09, but also r(MCQ, NLI) = 0.21: the two inference formats track each
  other no better than translation tracks either. With 5–16 items per cell,
  most of that is noise, and the items differ by task.
- **Language families.** Tamil and Malayalam lag on translation (COMET means
  0.67 and 0.62 against Hindi 0.77, Punjabi 0.72, my Table 2 means), "though
  this gap is not consistent across MCQ and NLI" (p. 43033); Malayalam's
  mean MCQ (0.75) exceeds Punjabi's (0.63). The pretraining explanation is
  offered as "likely" (p. 43033), untested.
- **Human ratings and metrics.** 104 of 204 translation items, translated by
  four models, 416 outputs, scored 1–5 for pragmatic adequacy by "four
  native raters, one per language" (p. 43034), each "rated independently
  without access to scores from other models or annotators" (p. 43039).
  "COMET achieves the highest overall correlation with human judgements
  (Pearson r = 0.813, Spearman ρ = 0.860)" against XCOMET ρ = 0.792 and
  MetricX ρ = 0.788 (p. 43034, Table 3). "Agreement is weakest on
  Implicature and Deixis" (p. 43034): true for COMET's ρ (0.83, 0.81) and
  for MetricX, but COMET's lowest Pearson r is Speech Acts (0.76).
- **Divergence cases.** Four outputs with COMET 0.65–0.86 and human 1–2 of 5,
  among them a Malayalam "ivide varenda" (don't come here) rendered "Come
  here" (COMET 0.78, human 1/5) (App. A.3, p. 43039).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Five LLMs score higher on MCQ than NLI on these items in every model–language pair | strong | Table 2; recomputed |
| C2 | Wrong MCQ answers favour the literal distractor (59.1% against 33.3%), and NLI errors on Contradiction items favour Entailment | moderate | §5.3, Fig. 3; subset size not given; pooled over four of five models |
| C3 | Models fail on culturally conventional meanings (ritual offers, soft refusals, kinship address, bidirectional "kal"/"parso") | moderate | worked examples (§5.1, App. A.4); per-cell n of 5–16; gold labels from one native author per language |
| C4 | Translation quality does not track pragmatic understanding | weak | no statistic; cross-cell r with COMET 0.29 (MCQ), 0.09 (NLI), but MCQ–NLI only 0.21; translation and inference items are different utterances |
| C5 | COMET (wmt22-da) agrees with native pragmatic-adequacy ratings better than XCOMET or MetricX on this material | moderate | Table 3, n = 416; one rater per language, no rater agreement |
| C6 | Automatic metrics miss fluent but pragmatically unfaithful outputs, especially for implicature and deixis | weak | four hand-picked examples (App. A.3); the per-phenomenon correlations differ by 0.1 or less |
| C7 | Indo-Aryan languages have a translation advantage, likely from pretraining coverage | weak | Table 2 means; mechanism untested |

## Concepts

- **Pragmatic adequacy (human rating)** — a 1–5 score of how well a
  translation "preserved the pragmatic intent of the source utterance
  including implied meaning, tone, cultural nuance, and illocutionary force
  rather than surface-level adequacy or fluency alone" (App. A.2, p. 43039),
  with the rubric of Table 4.
- **Literal distractor** — an MCQ option giving the utterance's literal
  meaning, built in deliberately (p. 43031).
- **Social pragmatics** — "how social factors such as kinship, gender norms,
  power dynamics, and cultural conventions around face shape language use"
  (p. 43029), after Ma et al. 2025.

## Connections

- **Ma et al. 2025**, the survey whose taxonomy the five phenomena follow
  (p. 43029); **PUB**, **MultiPragEval** and the Korean benchmarks as the
  English and East Asian predecessors (p. 43028). None held.
- **xCOMET** (LIT-tmplu4ga), which CASE-tmph0fxi names as a baseline: here it
  correlates with the human pragmatic-adequacy scores at r = 0.80,
  ρ = 0.79 overall, below the older COMET, and weakest on Hindi (ρ = 0.54)
  (Table 3). Hindi is the language whose COMET Pearson r is highest (0.85).
- **PARIKSHA** (Watts et al. 2024): LLM evaluators align poorly with humans
  on culturally nuanced responses, which the authors liken to their
  COMET–human divergence (p. 43029).

## Bearing on the record

- **CASE-tmph0fxi: its description of VakyArth is wrong on the point it
  relies on.** The case says "VakyArth's items … pair translation with
  pragmatic inference on the same material". They do not. The 578 items are
  three disjoint sets per language and phenomenon, and only one of 204
  translation sources overlaps an inference item. What VakyArth gives the
  case is: (a) 204 Indic utterances with human English references, chosen
  because their pragmatic point is easy to lose, each with a note on what
  the point is; (b) 374 MCQ and NLI items whose gold answers say what the
  utterance does. To serve the case, the inference probes would have to be
  written for the translation items, or the translation items built from
  the inference items. There is one route per item (Indic → English), no
  relay, and translations are by models, not translators under a brief.
- **CLAIM-202: no evidence either way, though the paper is cited as if it
  gave some.** The claim needs renderings matched on a static profile that
  differ in later behaviour, judged by receivers. VakyArth has no receivers
  except the item authors and one rater per language, and its "translation
  does not track pragmatic understanding" is a comparison of aggregate
  scores over different items. It shows that a model's COMET on one set of
  utterances says little about its accuracy on another set, which is
  expected. The exchange's report (in the LIT's "Why this is here") that
  "fluent translations can miss pragmatic meaning" is supported only by the
  four hand-picked examples in App. A.3.
- **CASE-055, Stage 0: no reliability figure to borrow.** The gold labels,
  the item review and the translation ratings each rest on one native
  speaker per language. The paper reports no agreement between two people,
  and no human accuracy on MCQ or NLI. The human–COMET correlation of 0.81 is
  agreement between a metric and one rater, not a reliability.
- **CLAIM-226: a clean instance of the objection.** The benchmark treats one
  native speaker's reading as the language's: "Any Hindi speaker resolves
  this by price ranking" (Fig. 1 caption, p. 43027); "In Punjabi culture, an
  elder commenting on a younger person's appearance ('you look thin') is a
  conventional expression of concern and care, not mockery" (App. A.4,
  p. 43041). Whether Punjabi readers agree, and which ones, is not measured.
  The items would make good anchor candidates for measurement invariance
  only after a panel of each community has rated them.
- **CLAIM-257: little bearing.** The translation task penalizes losing the
  source's point in English, not adding to it.
- **Should produce THEORY-tmp7mudy** (Proposed): models' errors on these
  items lean literal, and MCQ beats NLI. **And THEORY-tmp0k3ls**
  (Proposed): COMET agrees with one native rater per language at r = 0.81,
  with hand-picked inversions it misses.
- **Machine-learning practice: an anthology candidate.** The paper's
  instruction that "automatic evaluation alone is insufficient for
  benchmarks where pragmatic faithfulness and surface fluency can diverge,
  and human judgment remains necessary for phenomena like Implicature and
  Deixis" (pp. 43034–43035) is advice on evaluating MT and LLMs. The LIT
  carries `anthology-candidate`.

## Limitations

- **No inter-rater agreement for anything.** Gold labels, the review and
  the 1–5 ratings come from one native speaker per language.
- **Small cells.** 5–16 items per reported cell, so per-phenomenon
  differences in Table 2 are mostly within one or two items.
- **Translation and inference on different items**, so no item-level
  dissociation can be read from the paper.
- **Inconsistent model counts.** Five models are evaluated; Fig. 3, the
  shared-failure count and the human ratings use four, and the text calls
  Llama "Llama-3-8B" in the body and "Llama-3.1-8B" in App. A.4.
- **"Single-turn utterances or short passages"** (Limitations, p. 43035),
  though §3.1 says multi-party dialogues were added (p. 43030).
- **Ratings not released.** The repository's README and file listing show
  the items and evaluation code, but no human translation scores.

## Open questions

- Do native speakers other than the authors give the gold answers? A panel
  per language on the MCQ and NLI items, with agreement and accuracy, would
  say, and would turn the items into anchors.
- On the same utterances, does a model that picks the right MCQ reading
  translate the point into English, and the reverse? Writing inference
  probes for the 204 translation items would allow the test the paper's
  abstract implies.
- Is the 59.1% literal rate stable when the subset of items with an
  unambiguous literal distractor is stated and the fifth model included?
