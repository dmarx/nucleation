---
status: Read
paper: 'LIT-tmp2g5v4'
title: 'Srinivasan & Choi — TyDiP'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the published Findings of EMNLP 2022 PDF (ACL
    Anthology 2022.findings-emnlp.420, pp. 5723–5738), fetched 2026-10-29.
    The arXiv copy 2211.16496v1 (29 November 2022) was fetched as well but
    not compared word for word; its layout differs. Extracted with
    `pdftotext -layout`. I read the abstract, §§1–7, the limitations,
    ethics statement, references and Appendices A–G, Tables 1–12 and the
    captions of Figures 1–8. Figures 1–3 and 6–8 survive only as axis
    labels, so their values are quoted from the text. Pages are the
    proceedings'. Checks (numpy, my script): I recomputed the column means
    of Tables 2 and 3 and counted, per language, where target-language
    agreement exceeds English agreement and where target-language input
    beats translated input.
date: '2026-10-29'
summary: >-
  TyDiP gives graded politeness ratings, three crowd annotators per item,
  for 500 Wikipedia talk-page requests in each of nine languages. Mean
  pairwise Spearman agreement is 0.46 for target-language items and 0.36
  for English items rated by the same bilinguals. Leave-one-out human
  accuracy on the binary top-and-bottom-quartile set hovers around 90%,
  about 10 points above an English-trained XLM-R in six languages. But
  annotators were screened for agreement with that classifier, and the
  paper's "across all nine languages" is false for Tamil.
---
<!-- inactive-ok-file: CLAIM-257 CLAIM-202 THEORY-tmpxtosk THEORY-tmpotaav — Proposed; the record's claims this reading bears on and the theories it produces, cited as open -->

# NOTE-tmpmy2mv: Srinivasan & Choi — TyDiP

## Contribution

A politeness dataset in Hindi, Korean, Spanish, Tamil, French, Vietnamese,
Russian, Afrikaans and Hungarian, built in the manner of Danescu-Niculescu-
Mizil et al. (2013) for English: requests from Wikipedia user talk pages, each
two sentences with the second ending in a question mark (p. 5724), rated by
three native-speaker crowdworkers on a −3 to +3 scale in steps of 0.5
(p. 5724), z-normalized per annotator and averaged (p. 5726). 500 items per
language, 4,500 in all; the top and bottom quartiles, 250 per language, form
a balanced binary evaluation set (p. 5726). The paper also evaluates
zero-shot transfer of English-trained classifiers, maps the English politeness
lexicon into the nine languages by translation and alignment, and tests the
relation between formality and politeness.

## Key insight

Politeness in requests is perceived consistently enough within a language to
label, and more consistently by native readers of their own language than of
English. The same bilinguals rated 5 English and 15 target-language requests
per task, and agreement was 0.36 on English and 0.46 on the target language
on average (Table 2, p. 5726). "This suggests the interpreting politeness of
foreign language can be less precise and more variable compared to
interpreting that of native language" (p. 5726).

## Assumptions

- **Requests only.** Politeness is studied "in requests as they involve the
  speaker imposing on the listener" (p. 5723). One genre, one platform.
- **Bilingual annotators on Prolific**, recruited by first language with
  approval rate > 98% (p. 5724), one set of English guidelines for all
  (p. 5724).
- **A model in the loop at qualification.** Annotators were screened on
  requests "where the classifier assigned very high or very low politeness
  score", and the authors "pruned workers who provided scores that varies
  significantly from model predictions" (p. 5725). The classifier is an
  XLM-R trained on the English data, the paper's "XLMR-target" (fn. 5,
  p. 5725), the same model the paper then evaluates. Language-proficient
  researchers checked its predictions in four of the nine languages only
  (p. 5725).
- **A translation check** removed workers whose translations were too close
  to Google Translate (p. 5725).
- **Fifteen workers per language took the qualifier**; 7–11 passed per
  language (p. 5725).

## Key results

- **Agreement (Table 2, p. 5726).** Mean pairwise Spearman correlation
  between annotators, computed within each task of 20 items, against a
  shuffled baseline (fn. 8, p. 5725). Target language / English: Hindi
  0.39 / 0.31, Korean 0.60 / 0.34, Spanish 0.52 / 0.28, Tamil 0.33 / 0.38,
  French 0.53 / 0.45, Vietnamese 0.41 / 0.38, Russian 0.51 / 0.43, Afrikaans
  0.37 / 0.35, Hungarian 0.52 / 0.38; average 0.46 (SD 0.17) / 0.36 (SD
  0.31). Each target figure is over 15 items, each English figure over 5.
  The shuffled baseline "hovers around zero as expected" (Fig. 2 caption).
- **The paper overstates the language effect.** It says "we observe
  substantially higher agreement when annotators were labeling their own
  language compared to labeling English across all nine languages"
  (p. 5726). Table 2's Tamil row is 0.33 own-language against 0.38
  English, so the statement holds in eight of nine (my count). Afrikaans
  (0.37 / 0.35) and Vietnamese (0.41 / 0.38) differ by little.
  The English average I get is 0.367, printed 0.36.
- **Agreement with the original English labels (Table 9, p. 5734).** The
  TyDiP annotators' English ratings correlate with Danescu-Niculescu-Mizil
  et al.'s raw labels at 0.21–0.29 and with their aggregated scores at
  0.40–0.52, by language.
- **Human accuracy.** One annotator's label is the prediction, the mean of
  the other two the gold, resampled 1,000 times per example (p. 5727). The
  result, plotted only (Fig. 3), is "strong agreement, hovering around 90%"
  (p. 5727). How the held-out annotator's graded score is turned into a
  binary label is not stated.
- **Model accuracy (Table 3, p. 5727).** On the binary evaluation sets,
  XLM-R fine-tuned on 1,926 English requests reaches 0.808 on average over
  the nine languages with target-language input and 0.801 with Google
  Translate input; English is 0.892. The weakest languages are Russian
  (0.668) and Tamil (0.78) and Korean (0.784). GPT-3 Davinci-002 zero-shot:
  0.706 on target input, 0.668 on translated. My means agree.
- **Human–model gap.** "Six out of the nine languages have a gap of at least
  10%, and two of them being greater than 15%" (p. 5727). The authors note
  that "models significantly underperform in these languages with high human
  agreement", Korean and Hungarian (p. 5727). Across languages, Table 2's
  target agreement and XLMR-target accuracy correlate at r = −0.32 (my
  computation, nine points).
- **Translation into English.** For XLM-R, translated input was better in
  four languages, target input in five (p. 5727; checked). For GPT-3 the
  paper says target input was better "in seven out of nine languages"
  (p. 5727). Table 3 gives six better, one tie (Spanish, 0.732 both) and two
  worse (Tamil, Afrikaans).
- **Lexicon mapping (§4).** Translation plus alignment covers about 57–77%
  of the English strategies' lexicon (Fig. 4). Strategy–politeness relations
  are "somewhat consistent" across languages, with exceptions such as
  PLEASE not positive in Spanish (p. 5728).
- **Formality and politeness (§5).** The politeness classifier does worse
  than the majority baseline at formality (Table 4), and a formality
  classifier reaches 0.53–0.64 on politeness (Table 5). On informal–formal
  rewrites of the same sentence, 76–81% of pairs get the same politeness
  label, and in 68–73% the formal version gets the higher politeness
  probability (Table 7, p. 5729).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Crowd annotators' politeness ratings of Wikipedia requests agree modestly within a language, mean pairwise Spearman 0.46 (0.33–0.60 by language) | moderate | Table 2; 15-item tasks; annotators pre-screened for agreement with a classifier |
| C2 | The same bilinguals agree less on English requests (0.36) than on their own language's | moderate | Table 2; holds in 8 of 9 languages, not 9 as stated; English figures over 5 items per task |
| C3 | An English-trained XLM-R transfers zero-shot to nine languages at about 0.81 binary accuracy on extreme quartiles | strong | Table 3, 250 items per language |
| C4 | Models fall short of leave-one-out human accuracy (≈ 90%) by 10 points or more in six languages | weak | Fig. 3 only; the extreme quartiles were selected on the mean that includes the held-out annotator, and the binarization of a held-out score is unstated |
| C5 | Machine translation to English loses some politeness signal | weak | 0.808 against 0.801 for XLM-R; target better in 5 of 9; for GPT-3, 6 of 9 with one tie |
| C6 | Politeness and formality are not interchangeable, though formal rewrites tend to read as more polite | moderate | Tables 4, 5, 7, English and three Romance languages |

## Concepts

- **Politeness score** — the mean of three per-annotator z-scores of a −3
  to +3 rating (p. 5726).
- **TyDiP evaluation dataset** — the top and bottom 25% of each language's
  500 items by that score, labelled polite and impolite, 250 per language
  (pp. 5726, 5730).
- **Agreement** — pairwise Spearman correlation between annotators on a
  task's items, "instead of Cohen's Kappa" because the scores are
  continuous (p. 5725).

## Connections

- **Danescu-Niculescu-Mizil et al. 2013**, the English politeness corpus and
  strategy lexicon the whole design copies (p. 5723). Not held.
- **Rao and Tetreault 2018 (GYAFC)** and **Briakou et al. 2021
  (X-FORMAL)**, the formality data of §5. Not held.
- **Brown and Levinson 1978** is cited for the universality of politeness
  (p. 5723). The paper's zero-shot transfer result is said to weigh "in the
  universality of politeness phenomena across languages" (p. 5723), which is
  an inference from model behaviour, not a test of the theory.

## Bearing on the record

- **[CASE-055](../cases.d/CASE-055.md), Stage 0: TyDiP does have human-agreement figures, and they are
  the record's best benchmark so far for a politeness rating.** Three
  answers to the question the case asks. (a) **Between judges:** 0.46 mean
  pairwise Spearman in the target language, ranging 0.33 (Tamil) to 0.60
  (Korean), over 15-item tasks (Table 2). (b) **Against an earlier panel:**
  0.40–0.52 with the original English aggregate labels (Table 9). (c)
  **Binary agreement on extremes:** about 90% (Fig. 3). Nothing is reported
  on two passes by the same judge, which Stage 0 also requires. And the
  numbers come from annotators screened for agreeing with a classifier, so
  they may be higher than an unscreened panel would give. A Stage 0 target
  set from them should be read as an upper estimate for crowd judges
  without that screen.
- **[CASE-055](../cases.d/CASE-055.md), its known-groups test: TyDiP's §5 is a weak precedent.** The
  formal and informal rewrites of one sentence are a contrast in wording
  that, by [CASE-055](../cases.d/CASE-055.md)'s rule, should not count as a difference in footing.
  TyDiP finds that a politeness classifier usually gives both the same label
  (76–81%) but tends to score the formal one higher (68–73%; Table 7). That
  is a classifier, not people. It warns that a wording-only contrast can
  move a politeness rating.
- **[CLAIM-226](../claims.d/CLAIM-226.md): direct support for modelling the receivers' population.**
  The same people agree less when rating requests in their second language
  than in their first (in eight of nine languages), and agree with the
  original English panel at only 0.21–0.29 on raw labels (Table 9). Who
  judges matters, and so does the language in which they judge. The paper
  also concedes that "the annotation was done by different sets of
  annotators on different items for each language" (p. 5727), so
  cross-language differences in agreement or accuracy confound population
  with items.
- **[CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md): a source of anchor items and a reliability reference, not
  of translations.** TyDiP has no human translations. Its items are
  naturally occurring requests whose politeness score is known from a native
  panel, which is what the case's static-preservation readout and [CASE-055](../cases.d/CASE-055.md)'s
  measurement-invariance anchors need. Its languages overlap VakyArth's in
  Hindi and Tamil, and Tamil is the language with the lowest own-language
  agreement here.
- **[CLAIM-202](../claims.d/CLAIM-202.md) and [CLAIM-257](../claims.d/CLAIM-257.md): no bearing.** Nothing here concerns later
  framings or additions.
- **Should produce [THEORY-tmpxtosk](../theory.d/THEORY-tmpxtosk.md)** (Proposed): native-language politeness
  agreement and its drop in the second language. **And [THEORY-tmpotaav](../theory.d/THEORY-tmpotaav.md)**
  (Proposed): zero-shot transfer of an English-trained politeness classifier
  and its gap to people.
- **Machine-learning practice.** The paper evaluates models and proposes a
  model-in-the-loop qualification procedure, but states no instruction. Not
  flagged.

## Limitations

- **Model-screened annotators.** The qualification removes workers who
  disagree with a confident XLM-R, so both the agreement figures and the
  model–human comparison are biased toward the model's notion of politeness.
- **Selection inflates human accuracy.** The extreme quartiles are chosen
  by the three-annotator mean, and the held-out annotator's score is part
  of it.
- **Small agreement windows.** Correlations are over 15 target or 5 English
  items per task.
- **One genre, one register.** Wikipedia editors' requests about
  administrative and editorial matters (p. 5723).
- **Native-speaker checks in four of nine languages** (p. 5725).
- **Two textual slips:** "across all nine languages" (p. 5726), false for
  Tamil; "seven out of nine" for GPT-3 (p. 5727), six with one tie. Footnote
  5 says XLMR-target is described in Section 4; it is in Section 3.

## Open questions

- How reliable are politeness ratings from annotators not screened against a
  model? A replication of the agreement study without the model-in-the-loop
  step would say.
- How stable is one judge across two passes? Not measured.
- Does the drop in agreement in the second language reflect less precise
  perception, or a different calibration? Per-annotator scale use on the
  English and target items, compared, would separate the two.
