---
status: Read
paper: LIT-tmpwu0n0
title: 'Kay, Kasirzadeh and Mohamed — Epistemic injustice in generative AI'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from the published version, AIES 2024 proceedings vol. 7,
    pp. 684–697, the publisher's free PDF on ojs.aaai.org (article 31671,
    file 33838), text extracted with pdftotext. Read: the abstract, §1
    introduction, §2 on epistemic injustice, §3 related work, §4's four
    configurations with their examples, the subsection on specific harms,
    §5 on resistance and design, the conclusion, Table 1 and footnote 1.
    The reference list was consulted for what the paper cites, not read
    through. The arXiv preprint (2408.11441) was not compared. The
    two-column extraction interleaved some paragraphs; the order was
    restored from the section headings.
date: '2026-10-21'
summary: >-
  A conceptual taxonomy, illustrated with reported cases, of four ways
  generative models can take part in epistemic injustice: amplified and
  manipulative testimonial injustice, hermeneutical ignorance and access
  injustice. Its sharpest move is to relocate the testimonial wrong: in
  the algorithmic setting it "requires a credibility excess assigned to the
  algorithm". It counts deliberate fabrication as testimonial injustice,
  which Fricker's account sets apart, and stretches hermeneutical injustice
  to unequal access to information. Nothing in it is measured by the
  authors.
---
<!-- inactive-ok-file: THEORY-317 THEORY-326 THEORY-327 CLAIM-tmpoxld9 CLAIM-tmpj163u THEORY-tmpzqfxe — Proposed; accounts and claims this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmp22xqb — Unavailable; works this paper cites or restates, not read here -->
# NOTE-tmpw3hh8: Kay, Kasirzadeh and Mohamed — Epistemic injustice in generative AI

## Contribution

It names "generative algorithmic epistemic injustice" and sorts its
instances into four configurations by where people enter the model's
behaviour: biases learned in training (amplified testimonial), users
steering the model (manipulative testimonial), the model's own lack of
interpretive resources (hermeneutical ignorance), and the model's control
of who gets what information (access injustice). Earlier work on
algorithmic epistemic injustice, by the authors' survey, treated
classification and decision systems. The one prior generative-AI paper
they find, De Proost and Pozzi (2023), treated text dialogue only.

## Key insight

When a generative model repeats a prejudiced narrative, the hearer does not
deflate anyone's credibility directly. The hearer inflates the model's.
"In the conventional human-only environment, testimonial injustices involve
a credibility deficit assigned to someone's account of truth based on the
prejudices of the listener. In the algorithmic setting, the injustice
requires a credibility excess assigned to the algorithm; that is, humans
believe the account amplified through the technology over the individual
or group who is discredited." The deficit to the speaker is then a
comparative one, produced by the excess given to the system.

## Assumptions

- Fricker's account (Fricker 2007) as the foundation, used as she states
  it: testimonial injustice is "the unfair discrediting of someone's
  account due to prejudice against their identity", and hermeneutical
  injustice occurs when experiences "are misunderstood or not recognized
  at all, due to the absence of appropriate concepts within our collective
  cultural knowledge". The authors acknowledge criticism of Fricker for
  overlooking Black feminist predecessors (Berenstain 2020) and keep her
  framework anyway.
- A "modest working definition" of truth: "statements that can be verified
  through adequate evidence, or a robust consensus between relevant social
  groups".
- Generative AI is "the class of machine learning models trained on
  massive amounts of data ... in order to produce representative instances
  of such media".
- The examples are drawn from others' reports (NewsGuard, Bellingcat, a
  Medium post, Kazenwadel and Steinert 2023). The authors ran no study.

## Key results

There are no theorems and no data of the authors' own. The results are
definitions and illustrations.

- **The four configurations (§4, Table 1).**
  1. *Amplified testimonial*: "when generative AI magnifies and produces
     socially biased viewpoints from its training data". Example: NewsGuard
     found GPT-3.5 followed false narratives for 80% of 100 prompts from its
     "Misinformation Fingerprints" database, GPT-4 for 100% (reported, not
     replicated).
  2. *Manipulative testimonial*: "when humans fabricate testimonial
     injustices with generative AI". Examples: Bellingcat's reproduction of
     4chan's abuse of Bing Image Creator; the "liar's dividend", where
     genuine evidence is dismissed as a deepfake.
  3. *Hermeneutical ignorance*: "when generative AI lacks the interpretive
     frameworks to understand human experiences". Example: Midjourney's
     "American smile" on historical groups.
  4. *Hermeneutical access injustice*: "when unequal access to information
     and knowledge is facilitated by generative AI". Example: GPT-3.5
     reporting different airstrike casualty figures in Turkish and
     Kurmanji, and in Arabic and Hebrew.
- **Credibility excess (§4).** Stated above. The amplified case "creates a
  feedback loop where dominant narratives are amplified and marginalized
  voices are further silenced".
- **Willful hermeneutical ignorance in developers (§4).** "Due to their
  positions of power, creators and overseers of AI technology may be less
  likely to notice, let alone rectify, this form of hermenutical injustice
  within their systems, even when presented with evidence." The term is
  cited from Pohlhaus 2012, glossed as "the continued misunderstanding or
  misinterpretation of marginalized experiences despite their
  articulation".
- **Second-order harm.** Epistemic injustice degrades "the bond of trust
  between speakers and receivers of information, due to a cycle of
  credibility deflation and ignorance", and the erosion "can cut both
  ways": marginalized groups come to trust dominant institutions less.
- **Remedies (§5).** Epistemic virtues for developers, participatory
  development, data sovereignty, pluralistic alignment, provenance and
  fact-checking with their limits ("any algorithm which tries to
  automatically assign credibility is at risk of committing testimonial
  injustice"), and two positive uses: measuring testimonial injustice at
  scale with affected groups as judges, and generating hermeneutical
  resources. "Participation may not be effective or even possible in the
  case of willful hermeneutical ignorance."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Generative models can amplify testimonial injustice, and in that case the wrong runs through a credibility excess assigned to the system, not only a deficit assigned to the speaker | moderate as a conceptual analysis; untested as a description of how users weigh model output | §4 argument; no study of users' credibility judgements |
| C2 | Deliberately steering a model to fabricate discrediting content is a form of testimonial injustice | weak as a reading of Fricker; asserted | §4: "we argue that the intentional manipulation of falsehoods ... also constitutes a form of epistemic injustice" |
| C3 | A generative model can be hermeneutically ignorant, misportraying groups whose experience its training lacks | moderate | the Midjourney example, read as illustration |
| C4 | Unequal information access mediated by a model is a hermeneutical injustice | weak | asserted from its effect on "an individual's capacity as the receiver of knowledge"; see Limitations |
| C5 | Those who build and oversee models may be wilfully hermeneutically ignorant of these harms because of their position | weak | asserted, citing Pohlhaus; no evidence offered |
| C6 | The amplified case is a feedback loop that further silences marginalized voices | weak | asserted; no model and no data |
| C7 | Generative models can also be used against these injustices, by measuring them with affected groups and by generating hermeneutical resources | weak | proposals, not evaluated |

## Concepts

- **Generative algorithmic epistemic injustice**: epistemic injustice
  arising from generative AI, in the four configurations above. Each "has
  an equivalent counterpart outside of the realm of generative AI".
- **Credibility excess assigned to the algorithm**: the hearer believes the
  model's account over the testimony of the person or group it discredits.
- **Liar's dividend** (Schiff, Schiff and Bueno 2023): the uncertainty about
  synthetic media lets genuine evidence be dismissed as fabricated.
- **Recognition deficit and misrecognition** (Medina 2018, footnote 1): a
  group unseen, against a group seen but misdescribed.
- **Epistemic flooding** (Anderau 2023) and **testimonial smothering**
  (Dotson 2011) are used as received.

## Connections

It builds on Fricker (2007) and the algorithmic-epistemic-injustice
literature it surveys (Byrnes and Spear 2023; Symons and Alvarado 2022;
Hull 2023; Milano and Prunkl 2024; De Proost and Pozzi 2023). It invokes
Spivak (1988) and Collins (2000), the book, not the 1986 article this
record holds as [LIT-tmp2ojrd](../literature.d/LIT-tmp2ojrd.md) (read in [NOTE-tmpj0rwa](NOTE-tmpj0rwa.md)). It
takes "willful hermeneutical ignorance" from Pohlhaus (2012),
[LIT-tmp22xqb](../literature.d/LIT-tmp22xqb.md), which the record could not obtain. It does not cite
Fricker's later work on structural testimonial injustice ([LIT-1048](../literature.d/LIT-1048.md)) or
Dotson (2014).

## Bearing on the record

- **[THEORY-327](../theory.d/THEORY-327.md).** Fricker, in her own words, keeps deliberate
  manipulation of credibility apart: "a closely related but distinct
  injustice". C2 counts it as testimonial injustice without discussing
  that line. So this paper is not evidence for [THEORY-327](../theory.d/THEORY-327.md)'s first part as
  a statement of Fricker, and its manipulative configuration is, on
  Fricker's own account, the neighbouring wrong.
- **[THEORY-317](../theory.d/THEORY-317.md) and [THEORY-326](../theory.d/THEORY-326.md).** Its definition of hermeneutical
  injustice is the précis-like one: the absent concept, with the
  repository bearing "the imprints of dominant groups". It does not take up
  the incidental case. Neither is tested here.
- **[CLAIM-tmpoxld9](../claims.d/CLAIM-tmpoxld9.md).** C6 is the trust loop asserted for a generative model
  in place of a roster: what is amplified becomes what is believed, and
  what is believed is what is amplified. The paper gives no dynamics, and
  C1 adds something the claim lacks: the loop can run through the
  credibility given to a system, with no prejudiced hearer judging the
  silenced speaker at all. That is still a prejudice condition, carried by
  the training data, so it does not touch the claim's point that the loop
  alone cannot tell privilege from merit.
- **[CLAIM-tmpj163u](../claims.d/CLAIM-tmpj163u.md).** "Participation may not be effective or even possible
  in the case of willful hermeneutical ignorance" is the claim's split
  between access and uptake, stated for model development.
- **[QUESTION-072](../questions.d/QUESTION-072.md).** A25's line that "what becomes searchable, summarized,
  quoted, attributed, or incorporated into future reasoning may influence
  what subsequently becomes authoritative" is where this paper bears on the
  record's own filing: the record is written largely by a generative
  model, so C1's credibility excess and C3's ignorance are hazards of its
  own grammar as well as of what it reads. The paper gives no test and does
  not settle the question.
- **[THEORY-tmpzqfxe](../theory.d/THEORY-tmpzqfxe.md)** is filed from C1, Proposed.

The paper is flagged `anthology-candidate` on its LIT. Its §5 design
suggestions are general and carry no instruction for machine-learning
practice that a THEORY here could hold.

## Limitations

- **No evidence of its own.** The examples are reported by others. The
  NewsGuard figures are a simulation of misinformation, as the authors
  concede ("rather than an 'authentic' instance of epistemic injustice").
- **C2 departs from Fricker without saying so.** Fricker distinguishes
  deliberate manipulation from testimonial injustice. The paper's
  manipulative configuration needs an argument it does not give.
- **C4 stretches the hermeneutical category.** On Fricker's account the
  hermeneutical wrong concerns making sense of one's own social
  experience. Withholding information from a receiver is a different harm,
  and the paper's own reading of the multilingual example is a credibility
  deflation, which is testimonial.
- **Who is wronged in C3 is unclear.** A model's lack of interpretive
  resources is not a gap in a shared resource from which the wronged group
  was excluded, unless the model is taken to be part of that resource. The
  paper treats it as such without arguing it.
- **The feedback loop is asserted** (C6), with no condition under which it
  runs or fails.

## Open questions

- Do users in fact assign model output more credibility than the testimony
  of the groups it misdescribes? A study measuring credibility judgements
  of matched claims, attributed to a model and to members of the group,
  would test C1's premise.
- Under what conditions does amplification feed back into training data
  and further silencing? A model of the loop would make C6 a claim the
  record's dynamics could check.
