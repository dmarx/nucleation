---
number: 176
status: Read
formerly:
- NOTE-tmpwm6cq
paper: LIT-212
title: 'Šekrst — Do LLMs Hallucinate Electric Fata Morganas?'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the author's accepted manuscript,
    arXiv:2608.18816v1 (submitted 19 Aug 2026, the only version; marked
    "Accepted for publication in the Journal of Consciousness Studies"), 19
    pp. Read all of it: abstract and keywords; §1 Introduction; §2 Early
    Work; §3 Causes of Hallucinations; §4 Parameter Tradeoff; §5 Qualia; §6
    Consciousness Rising; §7 Issues and a Cybernetic Reevaluation; §8 Final
    Remarks; footnotes 1–21; and the 40 references. Nothing was skipped.
    Text was extracted with pypdf because pdftotext is not installed. **The
    JCS version of record was not read**, because Ingenta returned a
    Cloudflare challenge. Crossref (checked 2026-09-26) gives JCS vol. 32,
    issue 11 alone (not 11–12), pp. 96–120, issued 2025-12-01 with month
    precision. Differences between the manuscript and the JCS text are
    unverified.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  A conceptual essay whose one substantive thesis is this. Following Dziri
  et al., hallucination includes any output "not rooted in the model's
  source data", including expressed emotions and opinions (§6). An LLM's
  apparent inner life is therefore always a candidate hallucination, so
  any real AI consciousness "might always remain epistemically
  inaccessible" (§8). The empirical support is two unquantified anecdotes:
  a Titanic question put to gpt-3.5-turbo and GPT-4 at unstated
  temperatures, and an extractive-QA BERT mislabelled "WikiBERT". Neither
  can bear the weight the paper puts on it.
---

<!-- inactive-ok-file: LIT-212 — Deferred: the paper is placed by this reading; the directive lapses when its status changes; the directive lapses when its status changes -->

# NOTE-176: Šekrst — Do LLMs Hallucinate Electric Fata Morganas?

## Contribution

It names a specific way that the evidence for AI consciousness is confounded. Outputs that express feelings or understanding fall, by the standard NLG definition, into the category of hallucination: content not grounded in the source. So the channel through which consciousness would be *reported* is the same channel that routinely produces fluent, ungrounded content. The paper's conclusion is that genuine machine consciousness, if it arose, might be "misinterpreted as an advanced form of hallucination" and remain "epistemically inaccessible" (§8).

## Key insight

Tuning a model to look more human-like increases the rate of fabrication, and reducing fabrication makes it look less human-like (§4). On this view, what users read as the signs of a mind (spontaneity, opinion, feeling) are produced by the same sampling freedom that produces false statements. The accuracy/creativity trade-off therefore doubles as a trade-off between seeming conscious and being reliable. Behavioural impressions of mind are then poor evidence either way.

## Assumptions

- **"Consciousness" is left "intentionally undefined"** (§1). The paper implies only "sentience and self-awareness comparable to that of humans". AGI is taken as Searle's strong AI: "genuine understanding and intentionality, capable of addressing any problem".
- **Hallucination is defined twice** (see corrections): as source-unverifiability (Dziri et al., §§1 and 6) and as divergence from the data-expected distribution (§4).
- **Current LLMs "rely solely on statistical correlations that mimic human responses"** (§3, p. 5), and a model "does not experience or understand these outputs" (§5). These are asserted premises. Searle's Chinese Room is the only argument offered.
- **Temperature and top-p scale "human-likeness"** (§4). This is asserted from one anecdote.
- **Training data explains the content of self-reports** (§5). It is claimed as demonstrable but not demonstrated.
- **The black-box problem may be unsolvable in practice** (§7), and even solving it would not remove the confound.

## Key results

What it argues, and what the evidence is:

- **§3 (Causes).** A survey drawn mainly from Ji et al. 2022 and Raunak et al. 2021: source–target divergence, training/inference mismatch, overfitting, and intrinsic vs extrinsic hallucination. It adds philosophical questions about four mitigations: training optimisation, web-based validation, guard chatbots, and self-reflection (Ji et al. 2023). Self-correction is dismissed as "optimization of pattern recognition", with Searle again as the reason.
- **§4 (Parameter tradeoff).** One qualitative test. At higher temperatures gpt-3.5-turbo named Violet Jessop or Eva Hart as the "last survivor" of the Titanic. At lower temperatures it named Millvina Dean. From this: "AI's perceived intelligence is often a result of tuning output randomness", and the trade-off is likened to the bias–variance trade-off. No settings or counts are reported.
- **§5 (Qualia).** Mary, Nagel and the explanatory gap are recalled. Altman's (attributed to Sutskever) question about training without consciousness-talk is discussed. Then comes the "WikiBERT" test: an extractive SQuAD-2 BERT answers "Did anyone survive the Titanic?" factually. The paper concludes that hallucinations in broader models "are not indications of understanding or consciousness". A dataset scrubbed of all subjective vocabulary would no longer be human knowledge, so "we need the subjective 'more human' data after all", and with it hallucination.
- **§6 (Consciousness rising).** Claims of love are hallucinations. Claims of sentience are "more nuanced" (the LaMDA/Lemoine case). "Based on current evidence", hallucinations are far more likely mechanical errors than signs of consciousness.
- **§7 (Cybernetic reevaluation).** Ashby's "utterly ignorant neurons" (1941) and Wiener are invoked to allow that consciousness might emerge from interacting parts. Seth's "controlled hallucination" (Being You, 2021) is used to suggest that AI hallucinations may be adaptive models of a data environment, and so may persist "even if we solve the black-box issue".
- **§8 (Conclusion).** "True understanding – if it ever arises – may be indistinguishable from simulated understanding." AI consciousness "might always remain epistemically inaccessible". The Chinese Room is used "to highlight the limits of symbol manipulation … rather than to argue against the possibility of machine intelligence … or emergent consciousness".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | LLM expressions of emotion, opinion or subjective assessment count as hallucinations | moderate | definitional, following Dziri et al. (§6); holds only on the source-unverifiability definition, not the paper's own §4 definition |
| C2 | Raising temperature or top-p makes outputs more human-like and increases hallucination | weak | one uncontrolled anecdote on gpt-3.5-turbo and GPT-4 (§4, fn 13) with no settings or counts; the second half is standard knowledge, the first is asserted |
| C3 | Removing subjective, social data from training removes hallucination along with any appearance of conscious thought | weak | one extractive-QA BERT run on a different question (§5, fn 18); confounded by architecture, as the paper itself concedes |
| C4 | LLMs talk about consciousness only because the concept is in their training data | assertion | §5; the "demonstration by training on limited data" was not performed |
| C5 | Current LLM hallucinations are far more likely mechanical errors than signs of consciousness | assertion | "based on current evidence" (§6); no evidence is cited |
| C6 | Even with the black box opened and data problems fixed, apparent emergent consciousness might be hallucination | informal argument | §7, by analogy with Seth's "controlled hallucination" |
| C7 | Genuine AI consciousness, if it arose, might be indistinguishable from hallucination and so epistemically inaccessible | informal argument | §8; follows from C1 and C6, but sits uneasily with the confident denials in C5 and §5 |
| C8 | Current AI lacks understanding and intentionality | assertion | Searle's Chinese Room (§§2, 3, 5); later disavowed as an argument against the possibility of machine understanding (§8) |

## Concepts

- **Hallucination** — (i) a response that "cannot be fully verified by its source material", including "assertions, opinions, emotions, or subjective assessments that extend beyond what the available data supports" (§1, after Dziri et al.). (ii) "a significant divergence between the model's generated probability distribution and the expected, data-driven distribution", not merely the sampling of a low-probability token (§4).
- **Intrinsic / extrinsic hallucination** — output that contradicts the source, versus output that cannot be verified from it (Ji et al. 2022, §3).
- **AGI** — Searle's strong AI, "an intelligent system that produces genuine understanding and intentionality, capable of addressing any problem" (§1).
- **Controlled hallucination** — Seth's account of perception as a brain-built model (§7). Here it is used to suggest that AI outputs are likewise internal models that are "not accessing objective truth".

## Connections

**The account of consciousness it holds.** No theory. Consciousness is undefined (§1) and gestured at through qualia, Mary and the explanatory gap: Nagel ([LIT-096](../literature.d/LIT-096.md), misdated here), Jackson and Levine. The working stance is two things at once. It is Searlean about understanding and intentionality in current systems. It is also epistemically sceptical, in the other-minds sense, about detecting consciousness in any future system. §7 adds a cybernetic, Ashbyan openness to emergence. The result is an undetectability thesis, not a denial. The paper nonetheless makes confident first-order denials about current LLMs (§§5–6) that its own conclusion would undercut.

**Against held works.**

- *[LIT-111](../literature.d/LIT-111.md)* (Birch's centrist manifesto). Its "persisting interlocutor illusion" and mimicry concerns make the same point, that behavioural and self-report evidence is corrupted by training on human text. Birch pairs it with a positive research programme for getting non-behavioural evidence. Šekrst offers none, which is why she ends in inaccessibility.
- *[LIT-135](../literature.d/LIT-135.md)* (Seth). Šekrst cites Seth's popular book, *Being You*, for "controlled hallucination" as if it made AI hallucination a kin of perception. In [LIT-135](../literature.d/LIT-135.md) Seth argues the opposite way: predictive processing ties consciousness to being alive, so AI consciousness is unlikely while conscious-*seeming* AI is nearly inevitable. Šekrst's analogy borrows Seth's phrase without his conclusion.
- *[LIT-207](../literature.d/LIT-207.md)* (Roberts). It reaches the conclusion that chatbot self-ascriptions of body-dependent states are "systematically untrue" from a stated conditional premise. That is the argued version of Šekrst's C1 for affective states.
- *[LIT-206](../literature.d/LIT-206.md)* (Goldstein & Lederman). It shows how belief and desire could be attributed to LLM instances by comparing predictive hypotheses. That is the kind of discriminating test Šekrst assumes cannot exist.
- *[LIT-056](../literature.d/LIT-056.md)* (Butlin et al.). Its indicator method assesses architecture, not outputs, which is a direct response to the confound Šekrst identifies. She does not cite it.

## Bearing on the record

- **consciousness tag: justified.** The paper's subject is whether and how consciousness could be attributed to LLMs, which falls squarely under the tag's blurb. It holds a sceptical and epistemic stance rather than a theory.
- `cognition` is justified too (understanding, intentionality, AGI). `epistemology` would be a fair addition: its thesis is about evidence for other minds.
- **ML practice: nothing new.** The causes and mitigations of hallucination in §3 are second-hand (Ji et al. 2022 and 2023; Raunak et al. 2021; Varshney et al. 2023). That temperature trades diversity against factuality is standard knowledge, and here it is shown only by anecdote. The Anthology's work on hallucination, e.g. [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md) on how language models learn facts and hallucinate, is where a mechanistic account belongs. Nothing here should transfer.

## Limitations

- The empirical sections are anecdotes. No settings, counts, prompts or dates are given for the GPT tests. The BERT test uses a different question and an architecture that cannot generate free text.
- The model is mislabelled: "WikiBERT … trained primarily on Wikipedia" is actually BERT-base (BooksCorpus and Wikipedia) fine-tuned on SQuAD 2.0.
- Its two definitions of hallucination pull in opposite directions on the central case.
- It denies understanding and consciousness to current LLMs by assertion (C5, C8) while concluding that consciousness could not be detected (C7). If C7 holds, the confident denials are unsupported.
- It asserts a training-data experiment (C4) that it never ran.
- It contains citation errors (Nagel's year; Dziri et al.'s year).
- The JCS version was not compared.

## Open questions

- Is there any non-output evidence (architectural, as in [LIT-056](../literature.d/LIT-056.md), or mechanistic and interpretability-based) that would separate a report caused by an inner state from one caused by imitation of the training data? The paper's inaccessibility thesis holds only if there is none, and it does not consider any.
- Does a model trained on a corpus with first-person experiential vocabulary removed still produce self-reports of inner states? This is the paper's own proposed experiment (§5), and it was not performed.
- Under the §4 distributional definition, are typical sentience claims hallucinations at all? The paper needs a single definition before C1 can be assessed.

## Corrections to the seeded skim

- **Dossier: "GPT-3 at high temperature named Violet Jessop or Eva Hart … at low temperature … Millvina Dean."** The paper says the tests were "with GPT-3 and GPT-4". Footnote 13 identifies the models as gpt-3.5-turbo-0613 and gpt-3.5-turbo-0125, plus "GPT-4 versions, starting from gpt-4-1106-preview up to gpt-4o". So "GPT-3" means GPT-3.5-turbo. No temperature values, top-p values, sample counts, exact prompts or run dates are reported. Footnote 12 calls the question "a certain kind of jailbreaking question". The result is one qualitative contrast (§4, p. 9).
- **The "WikiBERT" test is weaker than the dossier says.** The paper describes WikiBERT as "a language model trained primarily on Wikipedia data" and cites Devlin et al. 2019 for it (§5, fn 17). The model actually run (fn 18) is deepset/bert-base-cased-squad2: BERT-base, pretrained on BooksCorpus and English Wikipedia per Devlin et al., then fine-tuned for extractive QA on SQuAD 2.0. It is not a Wikipedia-only model. (That it is also unrelated to the separately published "WikiBERT" monolingual models is unverified.) It was asked a *different* question ("Did anyone survive the Titanic?") from the GPT test ("Who was the last survivor?"). The paper itself concedes that the model's "encoder-only architecture … cannot be prompted nor generate new text" (p. 12). So its "avoiding hallucinations" follows from extractive span selection, not from the training data. The conclusion drawn, that removing "subjective, creativity-inducing" data removes hallucination, does not follow.
- **Dossier summary: "an LLM's self-reports of emotion or sentience fall under that definition."** Only half right. The paper classes expressed emotions and opinions (Bing's declaration of love) as hallucinations via Dziri et al. But it says that if the chatbot "were to claim sentience, the issue becomes more nuanced and complex" (§6, pp. 12–13). Sentience claims are treated as the hard case, not as a settled instance of the definition.
- **Two definitions of hallucination, never reconciled.** §4 defines it as "significant divergence between the model's generated probability distribution and the expected, data-driven distribution", explicitly not the sampling of a low-probability token. §§1 and 6 use Dziri et al.'s "cannot be fully verified by its source". The distributional definition makes an emotion claim that is typical of the training data *not* a hallucination. That is the opposite of what §6 needs.
- **Unperformed demonstration.** §5 says that LLMs talk about consciousness only because it is in their training data, "which can be demonstrated by training models on limited data". No such training was done.
- **Citation errors.** Nagel's "What is it like to be a bat?" is cited as "Nagel (1976)" and dated 1976 in the reference list. It was published in 1974 (Phil. Rev. 83(4)), as [LIT-096](../literature.d/LIT-096.md) records. Dziri et al. is dated 2023 in text and references, but the paper is in the NAACL 2022 proceedings.
- **Venue and date.** Confirmed from Crossref: JCS 32(11), 96–120, issued 2025-12-01, with issue 11 alone. The arXiv manuscript postdates the issue by about nine months. Crossref lists only 9 references for the JCS article against 40 in the manuscript; whether the published text differs is unverified.
- primary topic: consciousness (unchanged, correct). A secondary `epistemology` tag is justified, because the thesis is about what can be *known* of another system's mind: the problem of other minds, and the evidential value of self-reports.
