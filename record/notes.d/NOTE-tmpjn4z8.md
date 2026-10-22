---
status: Read
paper: 'LIT-tmpxa0ia'
title: 'Laukkonen, Friston & Chandaria — A beautiful loop'
version: 1
history:
- version: 1
  date: '2026-10-22'
  note: >-
    Read in full on 2026-10-22 from the PsyArXiv preprint's version 3
    (osf.io/daf5n, version 3 posted 16 June 2025, file laukkonen-depth.pdf,
    44 pp., PDF dated 10 June 2025), downloaded through the OSF API, with
    the text extracted by pdftotext. Version 4, posted 6 August 2025 with the
    journal citation, lists no public file (the API asks for login). The
    journal version (Neuroscience & Biobehavioral Reviews 176, 106296, CC BY
    4.0 per Crossref, online 29 July 2025 per OSF) returned 403 at
    ScienceDirect and its PDF link, and is not in Europe PMC; how far it
    differs from v3 is not known. Read: the abstract and sections 1–11, all
    footnotes, the captions of Figures 1–6, Table 1 (page rendered and
    viewed, because its equations are an image) and Table 2 as extracted.
    The figures themselves were not viewed. The reference list was skimmed.
    Page numbers below are the preprint's.
date: '2026-10-22'
summary: >-
  A conceptual theory that consciousness needs three things in an
  active-inference system: a unified generative model of the world (an
  epistemic field); competition to enter it that coherent, precise
  inferences win (Bayesian binding); and epistemic depth, the recursive
  sharing of that model back through the hierarchy, formalised as a
  hyper-model that predicts precision at every level. Awareness is graded by
  epistemic depth, not by content. It is applied to attention, sleep and
  lucidity, meditation, cessation and psychedelics, and to AI. There are no
  data and no simulations, and the formal part is a standard hierarchical
  model with layer-wise precision hyperparameters.
---
<!-- inactive-ok-file: THEORY-tmpw19hw — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-tmpdga80 CLAIM-tmp1lvwf CLAIM-tmpjw8ev CLAIM-355 TERM-tmpgqmop TERM-tmpe36gg THEORY-063 THEORY-577 THEORY-633 — Proposed; claims, terms and accounts this reading bears on, named, nothing here rests on them -->
<!-- inactive-ok-file: LIT-tmphw2n7 LIT-tmpg6f7h — Deferred; works registered unread, named -->

# NOTE-tmpjn4z8: Laukkonen, Friston & Chandaria — A beautiful loop

## Contribution

The paper asks what active inference would need, beyond explaining
perception and action, to count as a theory of consciousness. It proposes
three conditions "that seem necessary for consciousness" (p. 2) and argues
that some active-inference systems meet them. The third, epistemic depth, is
its own: a system-wide loop in which the model of the world is fed back
into the hierarchy that builds it, so that the model "entails the inference,
belief, or expectation, that it exists" (p. 10). It is put in formal terms
as a hyper-model over precision, and then used to redescribe a wide range of
states, from inattentional blindness to cessation in meditation.

## Key insight

Most theories ask which contents become conscious. This one says that what
varies with awareness is not content but how far the system's model of its
world is known to the system, by being looped back through every level as a
forecast of how much to trust each level. A nearly empty world model known
very clearly is then a possible state of consciousness, and a rich world
model known dimly (a non-lucid dream, driving on autopilot) is another.
"Awareness depends on epistemic depth more than configurations of contents
or the degree of analytic processing" (p. 20).

## Assumptions

- **Active inference and the free-energy principle**, with existence as
  maintaining a boundary and self-evidencing (pp. 3–4). Precision weighting
  sets the gain on prediction errors, and attending is raising precision
  (p. 4).
- **Metzinger's epistemic space and minimal phenomenal experience** (MPE).
  The paper agrees with Metzinger's emphasis and prefers "field" to
  "space" (p. 9, note 4). Following him, "a first person perspective,
  self-modeling, and agency, are not prerequisites of awareness, but are
  rather local or “contracted” forms of consciousness" (pp. 2–3).
- **Knowing that one knows is the mark of awareness**, after Cleeremans et
  al. 2020 (p. 6), but reached "through recursion not metacognition"
  (p. 20).
- **Contemplative reports are evidence.** Luminosity, lucid dreamless
  sleep, non-dual awareness and cessation are taken as phenomena a theory
  must cover (pp. 8, 21–25).
- **Each condition is asserted necessary.** The world model is "a necessary
  condition for consciousness because it defines what can become conscious"
  (p. 3); the global model is "necessary but not sufficient" until it is
  "reflected back through the underlying hierarchy" (p. 9).

## Key results

The paper reports no data and no simulation. By section:

- **Section 2: the reality model (pp. 3–5).** The organism's lived world is
  a "generative phenomenal, unified world model", also an "epistemic field".
  Active inference generates one, so "Active inference therefore satisfies
  our first condition for consciousness" (p. 5). It explains "what is known
  or experienced" but "not yet" why or how (p. 5).
- **Section 3: inferential competition (pp. 6–9).** What enters the world
  model is decided by "precision-weighted competition between possible
  explanations for the causes of sensory data" (p. 7). Coherence decides it:
  "coherence and boundedness are a central criterion in winning the
  inferential competition" (p. 6), and an inference "incoherent with other
  parallel and hierarchically adjacent inferences throughout the system" is
  "less likely to be selected" (p. 7). This is "Bayesian binding", shown
  for a face percept in Figure 2 as a precision-weighted average of prior
  and data. GNWT ignition is redescribed as the same competition (p. 8).
  Whyte & Smith's discrete–continuous account is called "A complimentary
  view" (p. 8).
- **Section 4: epistemic depth (pp. 9–11).** Defined as "a capacity or
  continuum (i.e., deepening) of knowing" (p. 9), with "luminosity" as the
  clarity of knowing, taken from Buddhist and Indian sources. The analogy is
  hearing one's own voice. Figure 3's caption states the hypothesis: "We
  hypothesize that this recursion is the causal mechanism permitting
  epistemic depth (the sensation of knowing)" (p. 11).
- **Section 5: hyper-models (pp. 11–14).** A hyper-parameter set Φ encodes
  "which layers to trust more (or less) under different contexts" (p. 11).
  "It is this recursive aspect that equips belief updating with epistemic
  depth" (p. 11). Table 1 (p. 13) gives four equations: the usual
  hierarchical generative process; the same with each level conditioned on
  a hyper-parameter φ⁽ˡ⁾ under a prior p(Φ); a local free energy per layer;
  and a free energy over all states and Φ. The paper separates this from
  "parametric depth" (Sandved-Smith et al.), which is local, while
  epistemic depth is "system-wide" (p. 13). The smallest case is a
  two-layer system that predicts and broadcasts precisions (p. 14). Small
  nervous systems (Megaphragma, Drosophila larvae, C. elegans) are named as
  borderline candidates, and plants are left open (note 6).
- **Section 6: implementation (pp. 15–18).** The hyper-loop has five steps:
  hyper-prediction, lower-level inference, error on the precision forecast,
  hyper-update, broadcast (p. 15). In the brain, "neuromodulatory sprays"
  and endogenous electromagnetic fields are proposed as the broadcast
  channels, and said to explain loss of consciousness in anaesthesia, deep
  sleep and seizure where frontoparietal or posterior neurons still fire
  (p. 17). "Biological loops are unique because they are leaky" (p. 16),
  while an artificial agent's Φ "must be coded explicitly" (p. 16). For
  language models, Reinforcement Learning from Internal Feedback is called "a
  kind of primitive hyper-model" (p. 18), and a blueprint is given: move the
  confidence signal "from the loss function into the forward pass" (p. 18).
  "Our proposal is first and foremost a conceptual one" (p. 18).
- **Section 7: attention and metacognition (pp. 19–20).** Three levels:
  inferences that lose and stay unconscious; inferences bound into the
  model but not known that they are known (periphery, the shirt one wears);
  and luminously known contents. Subliminal priming, inattentional and
  change blindness, and driving on autopilot are placed among them.
- **Section 8: sleep and lucidity (pp. 20–21).** Deep NREM sleep: a minimal
  model and low epistemic depth. REM: a rich model, low depth. Lucid
  dreaming: depth rises. Lucid dreamless sleep: "very low abstraction but
  high epistemic depth", "an aware but empty epistemic field" (p. 21).
- **Section 9: meditation and psychedelics (pp. 22–26).** MPE is when
  "epistemic depth is maximally high, and the reality model is contentless"
  (p. 22): first-order precision low everywhere, the precision on that
  precision sharp. Dereification and opacity rise with depth. Cessation is
  "Bayesian unbinding": "the world model is not contentless but incoherent"
  (p. 25). Psychedelics are conjectured to raise epistemic depth, and "one
  can feel very conscious of, and confident in, a world model that is
  nevertheless delusional" (p. 26).
- **Section 10: discussion (pp. 26–30).** The theory "places experiential
  contents themselves at the very center of consciousness rather than a
  distinct self, an agent, or some other separable and dualistic force"
  (p. 26). Table 2 sets six features against GNWT, IIT, RPT and HOT. For AI,
  three questions replace "can AI be conscious like humans?", and "This
  makes epistemic depth the predominant gap in current AI systems" (p. 27).
  On a system that meets the conditions and says so: "We seem forced, then,
  to conclude that the AI system is conscious" (p. 29). Note 11 then
  retreats: "Our position does not assert that satisfying these conditions
  guarantees phenomenal experience in the subjective sense; rather, it
  proposes that such a system would exhibit computational and behavioral
  hallmarks of consciousness" (p. 29). The function proposed is that
  "consciousness may be the solution to general intelligence" (p. 29).
- **Section 11: conclusion (p. 30).** "The theory is testable and
  falsifiable at the level of computational modeling, but also in terms of
  neural implementation." The test given: "If the three conditions are met,
  we ought to see evidence of awareness or deep and flexible epistemicity,
  as well as success on any Turing-type tests."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A unified generative world model is necessary for consciousness | asserted; definitional in part | pp. 3–5 |
| C2 | What enters it is decided by precision-weighted competition that coherent inferences win (Bayesian binding) | weak: a redescription of hierarchical Bayesian inference, with cited phenomena | pp. 6–9, Figure 2 |
| C3 | Epistemic depth, recursive sharing of the world model through the hierarchy, is what makes its contents known, and awareness is graded by it | speculative: a hypothesis with no test | pp. 9–11, 19–20 |
| C4 | Epistemic depth can be formalised as a global hyper-model over layer-wise precision | weak: the equations are standard, and nothing in them is shown to yield a model that "contains the knowledge that it exists" | Table 1, pp. 11–15 |
| C5 | Neuromodulatory sprays and endogenous electric fields broadcast the hyper-model | speculative | pp. 16–17, citations |
| C6 | MPE is maximal epistemic depth with a contentless model; cessation is incoherence of the model | speculative: redescription of contemplative reports | pp. 21–25 |
| C7 | Psychedelics raise epistemic depth | conjecture | p. 26 |
| C8 | Current AI lacks epistemic depth above all, and a system meeting the three conditions should be treated as conscious | argued, then qualified by note 11 | pp. 27–29 |

## Concepts

- **Reality model / epistemic field**: the organism's whole lived world as a
  generative, phenomenal, unified model that can be known and acted on.
- **Inferential competition / Bayesian binding**: precision-weighted
  selection, with coherence as the criterion, of what enters the model.
  "Bayesian unbinding" is its failure.
- **Epistemic depth**: the degree to which the reality model knows itself,
  through recursive, non-local sharing. **Luminosity** is its
  phenomenological name.
- **Hyper-model**: a higher-order model whose parameters Φ predict and set
  precision at every level, and is updated by errors on those predictions.
- **Parametric depth**: local, one-layer-up inference about precision
  (Hesp, Sandved-Smith), which the paper treats as a mechanism within
  epistemic depth.
- **Field-evidencing**: the world model continuously evidencing its own
  knowing (abstract).

## Connections

Built on Friston's free-energy principle, Hohwy's self-evidencing,
Metzinger's MPE and epistemic space, and Cleeremans's "learning to be
conscious". It cites Whyte & Smith 2021 and a 2024 version of Whyte et al.
([LIT-tmpyamns](../literature.d/LIT-tmpyamns.md), [NOTE-tmpjgegs](NOTE-tmpjgegs.md)) as complementary, and Safron's IWMT
(spelled "Saffron", p. 6; [LIT-tmp5k0u3](../literature.d/LIT-tmp5k0u3.md)) among active inference accounts of
consciousness. The record holds Sandved-Smith et al. 2021 ([LIT-1191](../literature.d/LIT-1191.md),
[NOTE-958](NOTE-958.md)), the source of "parametric depth", and Seth 2013 ([LIT-1263](../literature.d/LIT-1263.md)),
cited for keeping the body alive. Hofstadter's strange loop gives the
title.

## Bearing on the record

- **[QUESTION-tmpc4j7p](../questions.d/QUESTION-tmpc4j7p.md) and [CLAIM-tmp1lvwf](../claims.d/CLAIM-tmp1lvwf.md).** The paper is a candidate answer
  of the "higher-order or recursive self-interpretation" kind the question
  lists, and the exchange described it correctly as one: a further
  organizational condition beyond inference. It accepts the counter-claim's
  premise, since inferences that lose the competition stay unconscious
  (p. 19). But its condition is not independent of experience as stated.
  Epistemic depth is defined as "a capacity or continuum (i.e., deepening)
  of knowing, or awareness" (p. 9), and the hyper-model is offered as its
  formal analogue without showing that it is necessary or sufficient for
  it. A hierarchical model with layer-wise precision hyperparameters is
  common (the paper names the hierarchical Gaussian filter, p. 12), so the
  question's demand to say "what a sophisticated nonexperiential interpreter
  would lack" is not met: an HGF fitted in a laboratory has the Table 1
  structure. Note 11 also withdraws from the phenomenal half of the
  question.
- **[CLAIM-tmpdga80](../claims.d/CLAIM-tmpdga80.md) (constitution).** Close in spirit: experience is the world
  model and its looping, with contents "at the very center", and no
  further entity. It is not stated as an identity, and note 11 says
  satisfying the conditions does not guarantee phenomenal experience. So it
  is a production-or-correlation account that the constitutive thesis could
  adopt as its candidate organization, not support for the identity.
- **[TERM-tmpe36gg](../terms.d/TERM-tmpe36gg.md) (perspective).** The paper denies that a first-person
  perspective is needed for awareness (pp. 2–3). That is the represented
  sense, and probably the phenomenal one. It does not deny an
  organizational perspective; its world model is one. This cuts against
  any reading of [CLAIM-tmpdga80](../claims.d/CLAIM-tmpdga80.md)'s part 3 that needs a represented or lived
  point of view, and it is the term's warning that claims must say which
  sense they use.
- **[QUESTION-tmpzje42](../questions.d/QUESTION-tmpzje42.md) (unity).** The paper takes the coherence side: what
  enters awareness must cohere, and incoherence of the whole model is
  cessation, the loss of awareness (p. 25). That is close to the
  global-section reading A7 rejected. It does not discuss a felt conflict
  such as approach and avoidance, which is the question's test case, so it
  states a position without meeting the counter-example.
- **[THEORY-063](../theory.d/THEORY-063.md) (unity without a self-model).** It shares Metzinger's view
  that a unified world comes before a self, and it adds a mechanism
  (recursion over precision) and a minimal case (MPE). It adds no evidence:
  the contemplative states are redescribed, not measured. The record's two
  unread meditation works ([LIT-tmphw2n7](../literature.d/LIT-tmphw2n7.md), [LIT-tmpg6f7h](../literature.d/LIT-tmpg6f7h.md)) bear on whether
  such states are contentless, which the MPE account needs.
- **[CLAIM-355](../claims.d/CLAIM-355.md).** Consistent with it: no separable owner is posited, and the
  self is a "contracted" form. The paper does not discuss illusion.
- **[CLAIM-tmpn2xr4](../claims.d/CLAIM-tmpn2xr4.md) (four facts).** Epistemic depth is that claim's third
  fact, efficacy allocated from inside, made global and recursive. The
  claim shows that systems alike in ordinary behaviour can differ in it,
  and that only an intervention tells them apart. The paper's tests for AI
  ("evidence of epistemic depth", "success on any Turing-type tests") are
  behavioural. By that claim they cannot settle whether precision is
  allocated endogenously.
- **[THEORY-577](../theory.d/THEORY-577.md) and [THEORY-633](../theory.d/THEORY-633.md).** The paper predicts that a system
  with the loop would be "adamant that they exist" (p. 29), so it offers a
  sketch of how its mechanism yields self-reports, which [THEORY-577](../theory.d/THEORY-577.md)
  asks of any theory. Its zombie "stalemate" and note 11 concede that
  this does not reach phenomenal properties, which an illusionist
  ([THEORY-633](../theory.d/THEORY-633.md)) would grant at no cost.
- **[CLAIM-tmpjw8ev](../claims.d/CLAIM-tmpjw8ev.md) (grounding).** Lucid dreamless sleep and MPE are cases of
  awareness with almost no current sensory constraint. On the paper's
  account they are rich in epistemic depth, so current grounding is not
  what makes them aware, which is the claim's occurrence half. The paper
  does not argue it.
- **[TERM-tmpgqmop](../terms.d/TERM-tmpgqmop.md).** Inference in the paper fits the term, and the paper's
  first two levels of awareness (lost inferences; bound but unknown
  contents) are interpretation without, or with little, awareness.
- No instruction for machine-learning practice. The LLM blueprint
  (pp. 18) is a suggestion about building a hyper-model, offered as
  illustration.

## Limitations

- No data and no simulation. Every phenomenon is redescribed, not
  predicted, and the paper names no result that would count against it
  beyond the general statement that it is "testable and falsifiable"
  (p. 30).
- The formal model (Table 1) is a hierarchy with layer-wise precision
  hyperparameters under a common prior. Nothing derives from it the
  "knowledge that it exists", the non-locality or the luminosity the text
  attributes to it.
- Epistemic depth is defined in terms of knowing and awareness, so its use
  to explain awareness risks circularity.
- The AI argument concludes that a system meeting the conditions is
  conscious, and note 11 then denies that the conditions guarantee
  phenomenal experience. The two are not reconciled.
- Contemplative and psychedelic reports are taken largely at face value; a
  footnote cites an estimate attributed to ChatGPT 4o (p. 26, note 10).
- Read from preprint v3; the journal version was not reached.

## Open questions

- Would a simulated hyper-model show any signature that an HGF with
  layer-wise volatility does not? If not, what separates epistemic depth
  from ordinary hierarchical precision learning?
- What measure of epistemic depth could be taken without asking the
  subject how aware they were?
- Can the coherence criterion allow a felt conflict to be one experience,
  as [QUESTION-tmpzje42](../questions.d/QUESTION-tmpzje42.md) asks?
