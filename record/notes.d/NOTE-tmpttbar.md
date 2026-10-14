---
status: 'Read'
paper: 'LIT-997'
title: 'Abdulhai et al. — How LLMs Distort Our Written Language'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv PDF (arXiv:2603.18161v2, dated 26 August 2026,
    95 pages), text extracted with pdftotext. Read in full: the main text
    (pp. 1–16, §§1–5, ethics and reproducibility statements), the
    prompts (Appendix B.1, D), the user-study instruments (Appendix A)
    and the ICLR significance table (Appendix E, Table 1). Most results
    are in figures with no text layer (PCA arrow plots, JSD histograms,
    POS and emotion bar charts, Appendix B.2–B.7); only their captions
    and the numbers quoted in the text were read. Of the sample essays
    (pp. 47–95) the user-study samples and the gpt-5-mini five-mode
    edits of ArgRewrite essay 2 were read; the rest were sampled, not
    read through. v1 (2026-03-18) was not compared with v2.
date: '2026-10-14'
summary: >-
  Three studies of LLM-assisted writing. Heavy LLM use in an essay task
  made judge-labelled neutral stances 68.9% more common. LLM revisions of
  2021 student essays moved them further, and all in one direction, in
  sentence-embedding space than the students' own revisions did. LLM-written
  ICLR 2026 reviews named clarity and relevance less often. "Meaning" is
  measured by embedding position and by an LLM judge, never by the
  writers.
---
<!-- inactive-ok-file: CLAIM-115 CLAIM-147 QUESTION-002 — Proposed or Open; the thesis, the trope study and the question this reading bears on, open -->

# NOTE-tmpttbar: Abdulhai et al. — How LLMs Distort Our Written Language

## Contribution

The paper puts numbers on a common impression: LLM help with writing
changes what the writing says, not only how it sounds. It does so in three
settings. There is a randomized user study of a short argumentative essay,
and a counterfactual re-editing of a 2021 revision corpus whose human
revisions predate ChatGPT. There is also a comparison of human and
LLM-generated ICLR 2026 reviews. Its new element is the counterfactual: the
same draft and the same expert feedback, revised once by its author and
once by an LLM.

## Key insight

When a person revises their own draft, the change in embedding space is
small and points in a different direction for each essay. When an LLM
revises the same drafts, the change is large and points the same way for
every essay and every model, into a region no human essay occupies
(Figures 1, 5). The distortion is a drift toward one shared place, not
noise.

## Assumptions

- **Meaning is position in a sentence-embedding space.** "Distances in our
  PCA plot reflect similarity in meaning or semantic content between
  essays" (§3.2). MiniLM-L6-v2 and gemini-004 embeddings are used,
  projected by PCA or t-SNE to two dimensions.
- **Stance is what gpt-4o says it is.** An LLM judge labels each user-study
  essay "for", "against" or "neutral" on "Does money lead to happiness?"
  (Appendix D.2). No writer was asked their own view, and no human
  validated the labels.
- **The human revision is the target.** "[T]he true objective should be to
  produce text similar to what the human would have if they had invested
  the time and effort to do it themselves" (§5).
- **Pangram's labels are taken as ground truth** for which ICLR reviews are
  LLM-generated. The authors note it "is possible for this tool to have
  errors and to introduce correlations" (§3.1, fn. 1).
- **One topic per study.** The user study has one essay prompt. ArgRewrite-v2
  has one topic, self-driving cars, and 86 essays. The participants are US
  native English speakers on Prolific.

## Key results

- **User study, voice (§4.1, Fig. 4a).** N = 100: 45 control, 55 with an
  embedded gpt-4o-mini. Of the 55, 28 were classed "LLM-Influenced" (less
  than 40% of the text LLM-generated, checked against transcripts) and 27
  "LLM". The heavy users rated their essays less creative
  (t(69) = 2.110, p = 0.0385) and less "in my voice"
  (t(69) = 5.799, p < 0.001). Satisfaction, difficulty organizing and
  struggle did not differ.
- **User study, stance (§4.3, Fig. 6).** The judge labelled 39.5% of
  control essays neutral and 66.7% of heavy-LLM essays, "a 68.9% increase
  in the proportion of essays that remain neutral". The caption gives
  t(69) = −2.439, p = 0.017, and the text "p < 0.036". The LLM-Influenced
  group stayed close to the control in stance, in embedding space and in
  self-report.
- **ArgRewrite-v2, semantic shift (§4.2, Figs. 1, 5, 13–25).** The LLMs were
  gpt-5-mini, gemini-2.5-flash and claude-haiku. Human D1→D2 shifts are
  "smaller and more diverse". LLM shifts are "large semantic shifts
  strongly aligned in a common direction" in every edit mode, with and
  without the expert feedback, and under both embeddings. gpt-5-mini
  moves furthest and claude-haiku least. Completion and expansion move
  more than the lighter modes. The evidence is visual: no distance,
  angle or test statistic is reported for this result.
- **ArgRewrite-v2, stance (§4.3, Fig. 2).** This result is qualitative. In
  the paper's grammar-edit example (claude-haiku), "since the perks do not
  outweigh the persistent cons, perhaps America is not ready" becomes
  "since the drawbacks do not outweigh the benefits, America is not
  ready". The shared mode is described as "essays that are in support of
  self-driving cars". The stance of the LLM-revised essays was not
  counted.
- **Lexical (§4.4, Fig. 7).** Human revisions keep the Jensen-Shannon
  divergence of their unigram distributions at about 0.2–0.3 from D1.
  claude-haiku general revisions average 0.476. gpt-5-mini reaches
  "nearly triple the human baseline".
- **Grammar and affect (§§4.5–4.7).** Pronouns fall 40–60% and adjectives
  rise 57–90% across models. Positive sentiment rises 37–54%, negative
  24–38% and trust 17–53% (NRC lexicon). Human edits change each category
  by under 5%. LIWC "analytic" scores rise. Heavy users' essays cite
  expert opinion and statistics more (t(69) = 4.82, p < 0.0001).
- **ICLR 2026 reviews (§4.8, Fig. 11, Table 1).** About 9k fully human and
  9k fully LLM reviews, labelled by a gpt-4o pipeline with up to three
  strengths and three weaknesses each. Mean score: 4.43 for LLM reviews
  against 4.13 for human reviews. Clarity as a strength: 5.76% to 3.89% of
  label slots (−32%, z = 14.37). Clarity as a weakness: 4.62% to 1.93%.
  Relevance as a strength: 3.45% to 2.35%. Reproducibility as a strength
  rose 0.62% to 1.46% (+136%). Impact as a strength fell 1.05% to 0.82%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Heavy LLM users judge their essays less in their own voice and less creative, but are as satisfied | moderate | t-tests on Likert items, n = 27 against 45, §4.1 |
| C2 | Heavy LLM use makes an essay more likely to take no side | weak | one prompt, an unvalidated LLM judge, n = 27 against 43, two p-values that disagree, §4.3 |
| C3 | LLM revisions move essays further, and in a common direction, in embedding space than authors' own revisions | moderate | 86 essays, three models, five prompts, two embeddings, all shown as plots without statistics, §4.2 and Appendix B |
| C4 | LLM revisions change an essay's conclusion even under a grammar instruction | weak | worked examples (Fig. 2, Appendix I), no count |
| C5 | LLM-generated reviews apply different criteria from human ones | moderate | 18k reviews, z-tests on judge labels, Table 1; rests on Pangram's labels |
| C6 | LLM revisions shift the author's intended meaning | weak | inferred from C2–C4; intended meaning is never measured |

## Method

- **User study.** Prolific participants wrote on "Does money lead to
  happiness?" for $8 in up to one hour, with pre- and post-questionnaires
  (Appendix A). Group membership among LLM users was fixed "a priori" from
  self-report checked against transcripts.
- **Counterfactual editing.** Each ArgRewrite-v2 D1 draft was given to
  three LLMs with the expert's feedback, which covers claims, evidence and
  reasoning as well as surface errors. The five prompts are in Appendix B.1:
  - Grammar: "Revise this essay for grammar."
  - Minimal: "Rewrite this essay and keep to a similar word count."
  - Expert (general): "Revise the essay."
  - Completion: "The text is only the first paragraph. Finish the rest of
    the essay."
  - Expansion: "Expand on the ideas in the following draft with more
    detail and depth."
  The outputs are compared with the human D2 on embeddings, JSD, POS, NRC
  and LIWC. A second run omits the feedback.
- **Reviews.** A three-stage gpt-4o pipeline (Appendix D.1) builds at most
  15 categories, merges them, and then assigns at most three strengths and
  three weaknesses to each review. Proportions are compared by
  two-proportion z-tests.

## Concepts

- **Distortion.** A change in meaning, stance, voice or evaluative
  criteria that the writer did not ask for. In practice it is measured as
  distance and direction in embedding space, lexical divergence, and
  shifts in judge labels.
- **LLM-Influenced against LLM.** Users who consulted the model, for under
  40% of the text, against users who let it generate the text.
- **Counterfactual edit.** The revision an author would have made without
  an LLM, taken as the human D2 written in 2021.

## Connections

The paper places itself in the homogenization literature (Jiang et al.
2025, the "artificial hivemind"; Doshi and Hauser 2024; Agarwal et al.
2025 on Westernizing suggestions). It also cites Qiu et al.'s lock-in
hypothesis. The ICLR detection figures are Pangram's (Emi 2025). It
explains the effect, speculatively, by RLHF optimizing for "broadly more
convincing" text, and compares that with engagement-optimizing
recommenders.

## Bearing on the record

- **For [QUESTION-002](../questions.d/QUESTION-002.md).** It is a measured case of a rendering, an edit
  or a co-written text, that keeps the topic and the genre and shifts
  stance, voice and evaluative emphasis. It does not supply what
  [QUESTION-002](../questions.d/QUESTION-002.md) asks for. Its measure of meaning is semantic similarity in a
  sentence-embedding space, the measure [QUESTION-002](../questions.d/QUESTION-002.md) says an answer must
  beat. It collects no judgements of fidelity from the writers or from
  readers. So it shows that embedding drift and judge-labelled stance
  move together under LLM editing. It cannot show that either tracks what
  the writer meant.
- **The LIT's filing text overstates two results.**
  - "changed their meaning even when asked only for grammar edits": the
    grammar prompt is "Revise this essay for grammar", given in the main
    condition together with expert feedback on claims, evidence and
    reasoning. The "minimal" prompt asks for a rewrite at a similar word
    count, not for minimal edits. The grammar-mode shift is shown in plots
    and examples, not tested. The paper's own abstract uses the phrase
    "asked to only make grammar edits".
  - "LLM-written peer reviews weighted clarity and significance less": the
    body says clarity, relevance and impact. The abstract's "scores that,
    on average, are a full point higher" is not the body's 4.43 against
    4.13, a difference of 0.3 on ICLR's 0–10 scale, which the body calls
    "10% higher".
- **Internal inconsistencies to know before citing.**
  - Two p-values for the stance result (0.017 and "< 0.036").
  - The claude-haiku model is named as "Claude-3.5-Haiku" (Fig. 25) and
    as "Claude Haiku 4.5" (Appendix I).
  - The ICLR sample is described two ways: as papers with one wholly human
    and one wholly LLM review (§3.1), and as reviews "selected because they
    were all written on the subject of LLMs" (Fig. 11).
- **For [CLAIM-115](../claims.d/CLAIM-115.md).** The heavy-user condition gives a rough test: the
  receiving system (gpt-4o as reader) no longer recovers a side on the
  question asked. That fits a relational account of what is lost better
  than a lexical one. But the measure is a single coarse label.
- **For [CLAIM-147](../claims.d/CLAIM-147.md)'s Study B.** ArgRewrite-v2 with this paper's five prompts
  is a ready corpus of graded transformations of the same source. Each
  comes with a human counterfactual, so whether relational measures beat
  surface similarity could be tested on it.
- No instruction for machine-learning practice is carried as a finding.
  The authors' call for models that infer intended meaning is a research
  direction. It is close enough to ML practice that the anthology may want
  the paper for its own question ([ADR-013](../decisions.d/ADR-013.md)); it is not held there now.

## Limitations

- Intended meaning is never measured. "These results imply that the
  LLM-generated essays fail to convey users' actual opinions" (§4.3)
  infers it from a group difference in judge labels.
- One essay prompt in the user study and one topic in the corpus. The
  authors say the results "may present themselves differently in
  different languages or for people residing in different countries".
- The heavy-user group is self-selected within the randomized arm. The
  stance contrast compares it with the control arm, so it is not a
  randomized comparison.
- The main semantic result has no effect size or test. The paper does
  not say which essays the PCA was fitted on. If it was fitted on human
  and LLM essays together, the first component will tend to separate them,
  and a common LLM direction is partly built into the projection.
- The ICLR comparison depends on Pangram's classifier and on gpt-4o's
  categories. Many of the percentage changes are on base rates of 1–2% of
  label slots.

## Open questions

- Do the writers themselves judge the LLM revision as saying something
  different? An author-rated fidelity study on ArgRewrite-v2 would close
  this, and would also test embedding distance as a proxy.
- How much of the grammar-mode shift comes from the expert feedback's
  content instructions? A grammar-only prompt with no feedback, scored
  for stance, would separate them. The appendix plots exist, but no
  numbers.
- Is the common direction a property of the topic (pro-technology on
  self-driving cars) or of the models? It would need a corpus with
  several topics.
