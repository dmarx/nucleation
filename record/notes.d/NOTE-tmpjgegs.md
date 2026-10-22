---
status: Read
paper: 'LIT-tmpyamns'
title: 'Whyte et al. — On the minimal theory of consciousness implicit in active inference'
version: 1
history:
- version: 1
  date: '2026-10-22'
  note: >-
    Read in full on 2026-10-22 from arXiv:2410.06633v2 (submitted 14 June
    2025; arxiv.org/pdf/2410.06633v2, 60 pp.), with the text extracted by
    pdftotext. OpenAlex labels this copy, and the Monash repository copy,
    the submitted version. The journal version (Physics of Life Reviews 56,
    4–28, CC BY 4.0 per Crossref) returned 403 at ScienceDirect, as did its
    PDF link, and is not in Europe PMC; whether it differs from v2 is not
    known. Read: the abstract, sections 1–5, the conclusion, the
    acknowledgements and the code statement, Appendices 1 and 2, and the
    captions of Figures 1–4 and A2. The equations were read as extracted,
    which garbles their layout; the figures themselves were not viewed. The
    reference list was skimmed. Page numbers below are the manuscript's. None
    of the reviewed modelling studies was read here, so what each model did
    is the paper's report of it, except the sleep simulation of section 4.3
    and the appendices, which are new in this paper.
date: '2026-10-22'
summary: >-
  A review of active inference simulations of conscious content, self and
  state, which argues that they share a three-part "hard core": the
  imperative to minimise variational and expected free energy; conscious
  contents as the inferred hidden states of world, body or brain; and
  conscious access at the interface where continuous sensory beliefs become
  discrete beliefs that can inform counterfactual policy selection. The third
  part is an inference to the best explanation, and it is a criterion for
  which contents are conscious in humans, not for which systems have
  experience. Two close-to-core predictions are named. New in the paper: a
  re-run rivalry model that fits Levelt's laws, a predicted reward violation
  of them, and a sleep model that loses its P3b-like response.
---
<!-- inactive-ok-file: THEORY-tmpw20ca — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-tmpdga80 CLAIM-tmp1lvwf CLAIM-tmpjw8ev CLAIM-355 TERM-tmpgqmop THEORY-056 THEORY-094 THEORY-577 THEORY-633 THEORY-767 — Proposed; claims, terms and accounts this reading bears on, named, nothing here rests on them -->

# NOTE-tmpjgegs: Whyte et al. — On the minimal theory of consciousness implicit in active inference

## Contribution

The paper does not start from a property of consciousness. It starts from
active inference, a general framework for modelling behaviour as
approximate Bayesian inference, and asks what theory of consciousness is
already assumed by the active inference models of consciousness paradigms
that exist. Its answer is a "hard core" of three commitments with a
"protective belt" of model-specific assumptions, set out in Lakatos's terms.
It is written as a tutorial for experimentalists and a guide for modellers:
"the primary aim of this paper is didactic rather than polemic" (p. 4). It
adds three small simulations of its own.

## Key insight

Because every active inference model minimises the same two objectives,
whose terms (complexity, accuracy, risk, ambiguity, novelty) have fixed
interpretations, a finding that breaks a shared assumption would break most
models at once. That is what lets a modelling framework carry a theory of
consciousness. On that core, a belief is conscious when it can steer a
choice among discrete alternatives, slowly and precisely enough. Seeing is
then a kind of looking: "To See is to Look" (p. 30).

## Assumptions

- **The organism as a generative model.** Its phenotype is "a generative
  model of its niche", and behaviour is "self-evidencing" (p. 5).
- **The two objectives.** Variational free energy for perception and reflex,
  expected free energy for any counterfactual choice, which "(normally)
  requires a discrete generative model" (p. 8).
- **Hierarchical mixed models.** Continuous predictive coding at low
  levels, discrete POMDPs above, joined by link functions (p. 8). Gaussian,
  Laplace and stationary-variance assumptions give predictive coding, which
  are "three different ways of phrasing the same assumption" (p. 8).
- **A neuronal process theory.** Expectation nodes in deep cortical layers,
  error nodes in superficial ones, softmax as firing rate, and ERPs as the
  rate of change of firing (pp. 9–11). The mapping to microcircuits "is a
  matter of ongoing research" (p. 9).
- **Neuromodulators set precision.** Noradrenaline for transition (B)
  precision, acetylcholine for likelihood (A) precision (pp. 23–24).
- **Scope.** Only numerical simulation studies are reviewed (p. 13), and
  only "well-studied paradigms" (p. 4). The approach is "about the
  properties of a system that exhibits phenomena associated with
  consciousness" (p. 4), not about where consciousness comes from.

## Key results

By section. Results attributed to cited studies are the paper's report.

- **Section 2: the objectives (pp. 5–8).** Free energy decomposes into
  divergence plus surprise, and into complexity minus accuracy. Expected
  free energy decomposes into risk, ambiguity and novelty, so goal-seeking
  and information-seeking share one objective.
- **Section 3: belief updating (pp. 8–13).** A single-layer predictive
  coding network is derived as gradient descent on free energy, and the
  POMDP update is given with its neural reading. Policy posterior is a
  softmax of summed expected free energy (eq. 14).
- **Section 4.1: content (pp. 13–19).**
  - Troxler fading and binocular rivalry (Parr et al. 2019) follow from
    imprecise transitions plus attention- or fixation-dependent likelihood
    precision. The unattended stimulus gains epistemic value until attention
    switches. The step to awareness is explicit: "Assuming a correspondence
    between the posterior over states and the content of awareness" (p. 14).
  - Appendix 1 re-implements the rivalry model and fits Levelt's second and
    fourth propositions (A precision 0.7/0.3 when attended, uniform when
    not; B precision ω = 0.8). Appendix 2 adds reward (c = 0.25) and
    predicts that reward biases dominance and that lowering the rewarded
    stimulus's precision compensates: "a predicted violation of Levelt's
    second proposition under reward" (p. 33).
  - Hemineglect as a lesion of novelty-driven saccades (Parr & Friston
    2018b), with a prediction about TPJ–FEF connectivity reported as
    confirmed by Parr, Mirza et al. 2019 with DCM and MEG.
  - Conscious access (Whyte & Smith 2021): a two-level POMDP reproduces
    Dehaene's taxonomy and a P3b-like "ignition", and predicted that valid
    expectations lower P3b, reported as "independently confirmed by
    Schlossmacher et al, (2020)" (p. 17).
  - No-report (Whyte et al. 2022): when report is not required, second-level
    firing and the P3b-like response drop, yet "the posterior at the second
    level of the model was still well above the threshold for close to 100%
    reportability of the stimulus" (p. 18). Of its first prediction the text
    says it "is exactly what was observed in a simultaneous EEG-fMRI
    experiment" (p. 18), with the citation missing from the manuscript. The
    second is reported as confirmed by Rowe et al. 2024.
- **Section 4.2: self (pp. 19–22).** Homeostatic and allostatic control
  (Tschantz et al. 2022), building on Seth 2013; fitted interoceptive
  precision in patients (Smith et al. 2020), replicated in a pre-registered
  sample; a gastric-vibration study; a cardio-visual model (Allen et al.
  2022); emotion concepts learned in an "in silico childhood" (Smith et al.
  2019); valence inferred from the change between prior and posterior over
  policies (Hesp et al. 2021); and meta-awareness as a third level that sets
  attentional precision (Sandved-Smith et al. 2021). The last is called "a
  kind of computational conceptual analysis" (p. 22), not a fit to data.
- **Section 4.3: state (pp. 22–24).** "Active inference models have so far
  not been applied to experiments that manipulate conscious state" (p. 22).
  The paper extends a local–global auditory model: lowering second-level B
  precision (ω = 0.9), standing in for low noradrenaline in sleep, removes
  the P3b-like response and spares the MMN-like one. The authors say it
  "does not in-itself explain why participants lose consciousness in parts
  of sleep" (p. 24). A cholinergic story for NREM and REM is offered in
  words, not simulated.
- **Section 5: the minimal theory (pp. 24–31).**
  - Hard core 1: the free-energy imperatives, so "all behaviour, both
    conscious and unconscious, must, in some minimal sense, be aimed at
    minimising these quantities" (p. 25).
  - Hard core 2: "The most minimal such link implicit in all the models
    reviewed above is between the contents of consciousness and the
    inferred hidden state" (p. 25). It "rules out that a change in
    consciousness could occur without a change in the posterior over
    states" and "is consistent with non-conscious creatures exhibiting
    behaviour governed by active inference" (p. 26).
  - Hard core 3: "the conscious/unconscious distinction is tied to the
    mechanism(s) of conscious access, and that it occurs at the
    discrete-continuous interface" (p. 26). A conscious posterior must be
    slow enough to abstract from sensory flux and precise enough to tell
    counterfactual states apart. The threshold varies with the task. The
    criterion is dispositional: "we are not claiming that being the target
    of a counterfactual policy selection process is what makes a posterior
    belief conscious. Rather it is the capacity (in a counterfactual sense)
    for such a posterior belief to inform policy selection processes at the
    right timescale and with sufficient precision that makes it conscious"
    (pp. 26–27). Its scope: "a necessary and sufficient condition for
    content to become conscious in humans (and non-human animals with
    similar neuronal architectures)", while "we remain agnostic as to
    whether this condition is both necessary and sufficient in systems
    vastly different to ourselves" (p. 27).
  - Status of the parts: the first two are "in some sense logically
    entailed" by the framework; the third is "an inference to the best
    explanation" (p. 27). Most of the explanatory work "will be done by the
    protective belt of the theory" (p. 28).
  - The flexibility worry is stated: "active inference may be too flexible
    to be productive as a theory of consciousness" (p. 29). Two answers:
    shared assumptions (attention as A precision, used by "almost all"
    models of attention) would fall together; and there are close-to-core
    predictions.
  - Prediction 1: the risk–ambiguity trade-off in attention policies, as in
    Appendix 2. If reward did not trade off against epistemic value, "active
    inference would be seriously challenged" (p. 29).
  - Prediction 2: no sensory precision, no change in content. A stimulus
    given high precision by an attention or saccade policy "will enter the
    contents of consciousness sooner than a retinally-matched stimulus that
    is not the target of a saccade" (p. 30), which the authors call "unique
    to active inference as a theory of consciousness" (p. 30). It is part of
    an adversarial collaboration (INTREPID).
  - Failure modes named: overfitted models, or "if models of conscious and
    non-conscious perception look indistinguishable" (p. 31).
- **Code (p. 32).** The new simulations use SPM's spm_MDP_VB_X.m. "Complete
  code necessary to reproduce the simulations reported in this paper will be
  made available upon full publication."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Active inference models of rivalry, Troxler fading, neglect, access, no-report, interoception, emotion, valence and meta-awareness share two objectives and a small set of interpretable terms | strong as a description of the reviewed models | the review, pp. 13–22 |
| C2 | Conscious contents correspond to posterior beliefs over hidden states; no change in content without a change in posterior | an assumption made explicit, not tested | "implicit in all the models", p. 25 |
| C3 | A posterior is conscious when it has the capacity to inform counterfactual, discrete policy selection at a slow enough timescale with enough precision; necessary and sufficient in humans | weak: inference to the best explanation from what the models needed | pp. 26–27 |
| C4 | The no-report pattern (prefrontal and P3b loss with access intact) follows from report as a precision-raising mental action | moderate as a simulation result; empirical support at second hand, one citation missing | Whyte et al. 2022; pp. 18–19 |
| C5 | The rivalry model fits Levelt's second and fourth propositions | demonstrated in simulation, figures not viewed | Appendix 1 |
| C6 | Reward should bias rivalry and trade off against stimulus precision | a prediction, untested | Appendix 2; p. 29 |
| C7 | Lowering second-level transition precision removes the P3b-like response and spares the MMN-like one | demonstrated in simulation; the link to sleep is by analogy | section 4.3, Figure 4 |
| C8 | An attended or saccade-targeted stimulus reaches awareness sooner than a retinally matched one | a prediction, untested here; claimed unique | p. 30 |

## Concepts

- **Variational and expected free energy**: the two objectives, the second
  decomposed into risk, ambiguity and novelty.
- **Precision**: inverse variance; A precision is likelihood precision,
  B precision is transition precision. Attention is set by A precision.
- **Hard core and protective belt**: Lakatos's division between the
  commitments a programme keeps and the assumptions it revises.
- **Discrete–continuous interface**: where continuous sensory beliefs are
  mapped to discrete states that can enter policy selection, the paper's
  locus of conscious access.
- **Dispositional criterion**: what makes a belief conscious is its
  capacity to inform policy selection, not its use (after Carruthers and
  Prinz).
- **"To See is to Look"**: conscious perception uses precision assignments
  of a counterfactual policy selection process, overt or covert (p. 30).

## Connections

It builds on Hohwy's self-evidencing and his account of access as settling
on a posterior to drive action (Hohwy 2013; Marchi & Hohwy 2022), on Parr
and Friston's attention as precision, and on Seth 2014 for the depth of
counterfactual policy selection. It takes its programme framing from Negro
2024 and Lakatos 1968. The record holds several works it reviews or relies
on: Seth 2013 (LIT-1263, NOTE-1000), the source of the
interoceptive models; Sandved-Smith et al. 2021 (LIT-1191, NOTE-958),
reviewed in section 4.2; Parr & Friston on attention (LIT-1195,
NOTE-956); and Friston et al. 2010 on action (LIT-1181). Laukkonen,
Friston & Chandaria (LIT-tmpxa0ia, NOTE-tmpjn4z8) cite an earlier version of this
paper as a "complimentary view", and Safron's IWMT (LIT-tmp5k0u3) is
named among the conceptual models it leaves out.

## Bearing on the record

- **QUESTION-tmpc4j7p and CLAIM-tmp1lvwf.** The paper offers a criterion
  for which posteriors are conscious, and it is the access criterion. It
  grants the counter-claim's premise outright: hard-core part 1 covers
  "both conscious and unconscious" behaviour, and part 2 "is consistent
  with non-conscious creatures exhibiting behaviour governed by active
  inference". Its separating condition (capacity to inform counterfactual
  policy selection, at the right timescale and precision) is stated without
  phenomenal terms, which CLAIM-tmp1lvwf's defeater requires. But it is not
  independent of report: it was read off the models' report policies, and
  the authors scope it to humans and similar animals. So it does not meet
  that defeater, and it is a candidate for the organizational half of
  QUESTION-tmpc4j7p, not for the phenomenal half. The authors do not claim more.
- **CLAIM-tmpdga80 (constitution).** The paper speaks of a "correspondence"
  and a "link" between contents and posteriors (pp. 14, 25), not of
  identity. It is neutral between constitution and production, and its
  method (map model variables to phenomenology) is open to either. What it
  adds is a worked example of A7's demand that the qualifying organization
  be specified: discreteness, timescale and precision are specified, and
  they are specified for access.
- **TERM-tmpgqmop (interpretation).** Posterior inference here has all three
  of the term's parts: a distinction (discrete states), a context (priors
  and precision) and a consequence (policy selection). It is a formal case
  of interpretation defined without experience, and of the cost the term
  admits.
- **CLAIM-tmpn2xr4 (four facts come apart).** The dispositional criterion
  puts consciousness in the capacity of a belief to be effective, not in its
  use. That claim shows that ordinary behaviour cannot reveal whether an
  interpretation is effective, only an intervention can. A capacity "in a
  counterfactual sense" is that kind of fact. So the criterion, applied to a
  system that is not reporting, needs an intervention to check, which the
  paper's no-report simulation supplies by sweeping stimulus precision.
- **QUESTION-048 and THEORY-094 (report and no-report).** The no-report
  model gives one mechanism for THEORY-094's point: prefrontal activity and
  P3b track the precision raised by report as mental action, while the
  posterior that would support report stays above threshold. It does not
  separate experience from access. It reads access off a posterior and
  calls that conscious, and so meets THEORY-577's demand that a theory
  say how its mechanism produces reports by building the report in. The
  paper is silent on illusionism (THEORY-633).
- **THEORY-767 and THEORY-056.** The interoceptive models start from
  LIT-1263. Tschantz et al. put changing beliefs about set points and
  acting on the body under one objective, a modelling counterpart to
  THEORY-056's single-process view of regulation, not evidence for it.
  Nothing reviewed bears on body ownership.
- **CLAIM-tmpjw8ev (grounding).** The paper says nothing about grounding.
  Its criterion lets a posterior driven by priors alone be conscious
  (silent counting, p. 30), but the precision prediction ties change in
  content to sensory precision.
- **The exchange's description.** The exchange cited the paper "for
  extracting a minimal, testable theory of consciousness from what active
  inference models have in common". That is accurate. What it left out is
  the theory's scope: it is a theory of conscious access in humans, which
  says nothing about systems unlike us and does not claim to say what makes
  an organization experiential.
- No instruction for machine-learning practice.

## Limitations

- A review with three small new simulations, whose code was not yet
  released at v2. The empirical confirmations are cited, not shown, and one
  citation (the EEG-fMRI study, p. 18) is missing from the manuscript.
- The third hard-core commitment is read off the report policies of the
  reviewed models, so it is tied to report by construction. The authors
  grant it is an inference to the best explanation.
- Every model of content assumes a correspondence between posterior and
  awareness. None tests it.
- The sleep simulation reproduces one ERP pattern and, by the authors'
  account, does not explain loss of consciousness.
- The authors concede that many models fit the same data and that other
  formalisms can be formally equivalent in specific domains (p. 16). The
  answer to the flexibility worry rests on two predictions, neither tested
  here.
- Read from the submitted version; the journal version was not reached.

## Open questions

- Can the dispositional criterion be stated for a system that never reports
  and was not built with report policies, so that it reaches the systems
  the authors set aside?
- Does the "To See is to Look" prediction survive matching expectation
  between attended and unattended stimuli, the confound LIT-1276 found
  in the rubber hand illusion?
- Is the discrete–continuous interface one locus, or a gradient along the
  hierarchy? The criterion's task-dependent threshold suggests the second.
