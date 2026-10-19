---
number: 813
status: Read
formerly:
- NOTE-tmpv2vga
paper: LIT-938
title: 'Fu et al. — Evaluating Compositional Scene Understanding in Multimodal Generative Models'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arXiv:2503.23125v1, the only
    version, the TMLR 04/2025 camera-ready), text extracted with
    pdftotext: §§1–5 and Appendices A.1–A.9. Most results are plotted,
    and the plotted values (per-relation agreement, Bongard-HOI and SVRT
    accuracies, the error-type counts of Figure 17) were not recoverable
    from the text layer. Numbers below are those the prose and the
    statistical tests state. The human SVRT data are from Lee et al.
    (2023), not read.
date: '2026-10-14'
summary: >-
  Human raters judged DALL-E 3 images. Agreement with single familiar
  relations rose well above DALL-E 2's. It fell when subject and object
  of an asymmetric relation were swapped, and again when two relations
  were combined; low-agreement reversed images mostly had the wrong
  relation or swapped roles. Five VLMs learned relational concepts
  few-shot below human level, and four were at chance with six objects.
---
<!-- inactive-ok-file: THEORY-250 CLAIM-013 THEORY-117 — Proposed; the theory filed from this reading and the claims and theory it bears on, open -->

# NOTE-813: Fu et al. — Evaluating Compositional Scene Understanding in Multimodal Generative Models

## Contribution

Two behavioural evaluations with human comparison. First, human raters
judged whether DALL-E 3 images match relational prompts, under three
conditions: the 75 two-entity prompts of Conwell and Ullman (2022), the
same prompts with subject and object reversed, and new prompts with
three entities and two relations. Second, five vision-language models
were tested on few-shot relational concept learning (Bongard-HOI and
SVRT) and compared with human data. Two new prompt sets (reversed and
compositional) are released.

## Key insight

Getting a familiar relation right is not evidence of composing it. The
same model that renders "a tiger chasing a rabbit" fails "a rabbit
chasing a tiger", and its failures are binding failures: the objects
are there, but the relation or the roles are wrong.

## Assumptions

- **Human agreement is the measure.** "Agreement" is the proportion of
  raters who select an image as matching its prompt (10 images per
  prompt, select all that match). A 1–7 Likert version on the basic
  prompts gave the same ordering of relations (A.3, Fig. 13).
- **One text-to-image model.** DALL-E 3 via the Azure API (version
  2024-02-01), with GPT-4 prompt rewriting refused and checked, standard
  quality, 1024×1024. The style was 'natural' for Experiment 1 and
  'vivid' for Experiments 2 and 3, because vivid gave more matches on
  reversed prompts.
- **Prompts were changed for content policy.** 25 of the 75 in
  Experiment 1 (e.g. "kicking" → "hugging", "hitting" → "chasing"),
  33 in total across Experiments 1–2 (A.2).
- **Experiment 2 is selected.** It kept the three physical and three
  agentic relations with the highest basic agreement ("kicking" then
  replaced by "chasing"): 30 prompts and their reversals.
- **Raters** were undergraduates from a university subject pool, for
  course credit: 30, 38 and 37 analysed across the three experiments.
- **Human SVRT comparison** uses Lee et al. (2023)'s interactive paradigm
  with feedback. Episodes stopped after seven correct in a row, and later
  trials were imputed as correct (A.7).

## Key results

- **Basic prompts (§2.1).**
  - DALL-E 3 beats DALL-E 2 on every relation (paired t-test,
    t(49) = 8.552, p < .001).
  - On 'on', 'near' and 'in', mean agreement is above 0.8, against below
    0.4 for DALL-E 2.
  - No major difference between physical and agentic relations.
- **Reversed prompts (§2.2).**
  - Agreement is lower than for the basic prompts (t(29) = 3.668,
    p = 0.001).
  - Little change for 'near', 'helping' and 'touching'; large drops for
    'on', 'in' and 'chasing'. Two of the three robust relations are
    symmetric, and all three fragile ones are asymmetric.
  - Prompt log-likelihood under GPT-3 (davinci-002) correlates with
    agreement only weakly: Spearman r(598) = 0.090, p = 0.027.
- **Compositional prompts (§2.3).**
  - 60 prompts, three entities and two relations, 600 images.
  - Agreement "varied widely": some pairs are high ('in & in',
    'helping & near'), but "the majority of relation combinations
    displayed relatively low agreement".
- **Error analysis (A.5).** Reversed-prompt images with agreement below
  0.2 were classed as wrong subject, wrong object, wrong relation or
  relation binding error (roles swapped). "The overwhelming majority of
  errors involved either a wrong relation or a relation binding error."
- **VLMs as judges (A.6).** Correlation with mean human ratings is
  r = 0.49 (GPT-4v), 0.51 (GPT-4o), 0.43 (Claude 3.5 Sonnet), 0.56
  (Qwen2-VL-72B) and 0.48 (InternVL2.5-38B). Human split-half
  reliability is r = 0.91.
- **Bongard-HOI (§3.1).**
  - Both GPT-4 variants beat the HOITrans baseline (χ²(1) = 80.06 and
    75.27) and fall below humans (χ²(1) = 335.78 and 352.61).
  - Swapping class labels made no difference (z = 0.83, p = 0.41), so
    the result is not memorisation of the dataset.
- **SVRT (§3.2), 2,070 tests per model.**
  - Humans outperform all five models.
  - All improve with more examples and degrade with more objects.
  - At six objects, the two GPT-4 variants, Qwen2-VL-72B and
    InternVL2.5-38B are at chance (p = 0.58, 0.58, 0.36, 0.30). Claude
    3.5 Sonnet is above chance (χ²(1) = 6.85, p = 0.0089).
  - Chain-of-thought prompting did not help (A.8).
  - In an interactive paradigm like the humans', GPT-4 reached criterion
    far less often (Fine–Gray SHR 0.25 and 0.18 against humans; A.8.1).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | DALL-E 3 renders single familiar relations much better than DALL-E 2 | strong | §2.1, every relation, t(49) = 8.55 |
| C2 | Reversing subject and object lowers agreement, mainly for asymmetric relations | moderate | §2.2, t(29) = 3.67; symmetric/asymmetric split read off six relations |
| C3 | Prompts composing two relations get low agreement for most combinations | moderate | §2.3, no matched single-relation control with the same entities |
| C4 | Low-agreement reversed images fail on the relation or the roles, not the objects | moderate | A.5, images below 0.2 agreement only, counts in a figure |
| C5 | The reversal drop reflects lower training-data likelihood | weak | r = 0.090 with a GPT-3 log-likelihood proxy |
| C6 | VLMs learn relational concepts few-shot below human level and fail at six objects | moderate | §3.2; the human paradigm differs and is imputed |
| C7 | VLM judges do not track human judgements of prompt–image match | moderate | A.6, r ≈ 0.43–0.56 against 0.91 |
| C8 | The failures stem from multi-object parsing (binding) more than relational reasoning | weak | Discussion, by appeal to Campbell et al. (2024) and the null CoT result |

## Concepts

- **Basic, reversed and compositional prompts.** Two entities and one
  relation (Conwell and Ullman's set); the same with roles swapped;
  three entities and two relations.
- **Physical and agentic relations.** In, on, under, covering, near,
  occluded by, hanging over and tied to; pushing, pulling, touching,
  chasing, hugging, helping and hindering.
- **Relation binding error.** The image shows the relation with the
  roles reversed (a tiger chasing a rabbit for "a rabbit chasing a
  tiger").
- **Hard negatives.** In Bongard-HOI and SVRT, negatives that share the
  objects and differ only in the relation.

## Connections

It repeats Conwell and Ullman's (2022) DALL-E 2 study on DALL-E 3, and
reads its results through Lewis et al. (2022), who found CLIP composes
concepts for one object but not for several, and Campbell et al. (2024),
who tie VLM failures to the binding problem. Its remedy, object-centric
slot representations, is a direction for ML practice and is not taken up
here.

## Bearing on the record

- **[QUESTION-018](../questions.d/QUESTION-018.md)** asks what determines whether a generator receiving
  several conditions keeps their conjunction and relational bindings.
  The paper measures that bindings fail and gives three correlates:
  - reversal of an asymmetric relation;
  - low prior plausibility, weakly (r = 0.09);
  - the number of relations.
  It does not separate the question's candidates (constraint
  satisfaction, local empirical distributions, compatibility across
  contexts), or estimator error from misspecification. The plausibility
  result leans weakly toward the training-distribution account. It is
  evidence about the explanandum, not an answer, and [THEORY-250](../theory.d/THEORY-250.md)
  carries no `answers` edge. The LIT's filing text says the paper
  measures binding "under several conditions". In the question's sense,
  one prompt carrying several conditions, only the compositional
  experiment does that, and it has three entities and two relations.
- **[LIT-938](../literature.d/LIT-938.md)'s summary misplaces the ">5 objects" result.** The summary
  says performance falls most "for scenes with more than five objects and
  several relations". That comes from the VLM SVRT experiment (six-object
  concepts). No text-to-image prompt had more than three entities.
- **[CLAIM-013](../claims.d/CLAIM-013.md)** says existing text-to-image benchmarks evaluate object
  presence and attributes. This paper is a relational evaluation scored
  by human raters, and it includes agentic relations (helping,
  hindering, chasing). It qualifies [CLAIM-013](../claims.d/CLAIM-013.md) as [CLAIM-097](../claims.d/CLAIM-097.md) does. It does
  not reach the pragmatic consequence or social uptake [CLAIM-013](../claims.d/CLAIM-013.md) asks
  for.
- **[CLAIM-097](../claims.d/CLAIM-097.md)** faults CLIPScore for tracking human judgement poorly on
  interactions. A.6 extends the point to VLM judges: r ≈ 0.43–0.56 against
  a human split-half of 0.91.
- **[CLAIM-123](../claims.d/CLAIM-123.md)** (score addition composes conditions only under
  conditional independence) is neither tested nor contradicted. DALL-E 3
  is treated as a black box.
- **[THEORY-117](../theory.d/THEORY-117.md)** (combinatorial diversity, not volume, drives
  compositional generalization) is consistent with the reversal result,
  but the paper has no control of training data.
- **[CASE-004](../cases.d/CASE-004.md)** is the manuscript's two-people-and-a-wallet prompt. The
  reversal and binding-error results are the nearest measured analogue:
  same objects, changed configuration.
- **For the anthology.** The benchmark sets, the VLM-as-judge result and
  the object-centric remedy are ML practice, and the
  `anthology-candidate` flag stands. Held here is the finding about
  binding, filed as [THEORY-250](../theory.d/THEORY-250.md).

## Limitations

- **One generator, one snapshot.** DALL-E 3 through one API version;
  other text-to-image models are not tested.
- **Uncontrolled comparisons across experiments.**
  - Rater pools and image styles differ between Experiment 1 (natural)
    and Experiments 2–3 (vivid).
  - Experiment 2's relations were chosen for high basic agreement.
  - The compositional prompts have no single-relation control with the
    same entities.
  - Figure 7's summary sets the three side by side.
- **The test statistics are thin.** t(49) for 75 basic prompts is not
  explained. The plausibility correlation is significant but tiny.
- **The causal reading is the authors'.** "Driven by the lower
  likelihood ... in DALL-E 3's training data" rests on r = 0.09 and a
  GPT-3 proxy for DALL-E 3's training distribution.
- **The human SVRT comparison is not like-for-like.** It uses a
  different paradigm, early stopping and imputation. A.8.1 narrows the
  gap for GPT-4 only.
- **Values are in figures.** The reading could not check per-relation
  means or the error-type proportions beyond the prose.

## Open questions

- Is the reversal drop a binding failure or a prior failure? Prompts
  that are reversed but equally plausible (symmetric in frequency) would
  separate them.
- Does agreement fall with the number of relations at a fixed number of
  entities? That would tell composition apart from multi-object parsing.
- Do diffusion models with known conditioning structure show the same
  pattern, so that it can be checked against [CLAIM-123](../claims.d/CLAIM-123.md)'s
  conditional-independence condition?
