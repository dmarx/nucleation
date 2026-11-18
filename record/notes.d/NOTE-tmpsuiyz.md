---
status: Read
paper: 'LIT-tmp9dq5h'
title: 'Cerrato, Sahlgren and Heilmann — Taking the Whys Seriously'
version: 1
history:
- version: 1
  date: '2026-11-18'
  note: >-
    Read on 2026-11-17 from arXiv:2608.30956v1 (31 August 2026, cs.CY),
    https://arxiv.org/pdf/2608.30956, 14 pages without page numbers, text
    by pdftotext; results are cited by section. Read: abstract,
    introduction, background, the resume-screening example and its
    structural causal model, the experiments (RQ1, RQ2), discussion and
    conclusions. Figures read only through their captions; appendix
    tables and references scanned, not read closely. The quotes below were
    rechecked by the filer against the same copy on 2026-11-18.
date: '2026-11-18'
summary: >-
  On ACS census data with earnings as a proxy for fit, the authors model a
  resume-screening pipeline and intervene on upstream "business-side"
  choices (label definition by a salary cap, measurement of a feature,
  model-selection metric, validation strategy). For two retrieval-based
  counterfactual-explanation methods, those choices usually move the
  generated counterfactuals as much as or more than the method's own
  validity threshold. Normatively: counterfactuals rest on a "fixed model
  assumption" that brackets the deployer's contestable choices, so they
  cannot by themselves justify a decision, and as recourse they cast the
  subject as the only party who should change. Recourse is relational.
---
<!-- inactive-ok-file: CLAIM-tmpcpijj CLAIM-tmpohafo — Proposed; cited with their standing, entries this reading bears on or files -->

# NOTE-tmpsuiyz: Cerrato, Sahlgren and Heilmann — Taking the Whys Seriously

## Contribution

Earlier work showed counterfactual explanations (CEs) fragile under small
perturbations of data or model. This paper's evidence is that the
organization's upstream design choices shape the counterfactuals as much
as or more than the explanation method does. From that it argues that a CE
given to a subject is partly an artifact of choices the subject cannot see
or contest.

## Key insight

An explanation that names the smallest change to the inputs that would
have flipped the decision holds the model fixed. What it holds fixed, the deployer chose,
and those choices are themselves answers to "why".

## Assumptions

- Earnings stand in for a recruiter's latent judgment of fit; no dataset
  links features to recruiters' judgments, as the authors grant.
- Both CE methods (DiCE-kdtree, NICE) are retrieval-based; optimization-
  based methods were excluded because seed-to-seed variance swamped the
  effects.
- The size of the change in the validity threshold τ is a fair baseline.
- Recourse is valued as a "modally robust" good (after Venkatasubramanian
  and Alfano).

## Key results

- **Central finding** (abstract): "an organization's choices on
  measurement models for feature and labels, business requirements, model
  validation, and the metric of model success have as much or more impact
  on the generated counterfactuals as the specifics of the generating
  method".
- **What naive use hides** (abstract): "naive application of CEs for
  justification and recourse can lead to ignoring contestable choices made
  throughout the machine learning (ML) pipeline"; CEs "preclude
  consideration of whether the decision-maker ought to have acted
  differently".
- **The assumption tested** (Discussion): "The central assumption that we
  have operationalized with our experiments is the fixed model
  assumption".
- **Justification** (Implications for Justification): "CEs may be
  misinterpreted as model-independent evidence or used selectively to
  shirk responsibility and public accountability".
- **Order of justification** (Implications for Recourse): "upstream choices
  must be relatively settled, normatively speaking, prior to evaluating
  CEs for recourse"; otherwise "there may be no uniquely identifiable
  action the decision subject should have taken to achieve a favorable
  outcome".
- **Relational recourse** (Implications for Recourse): "AR is an inherently
  relational practice involving both decision subjects and decision-makers
  as parties whose behavior may require revision"; "it may be impossible
  for subjects to reverse their decisions through contesting such choices
  absent appropriate transparency".
- **Harm of the individual framing** (same section): treating CEs as
  individual advice "risks encouraging affected subjects to comply with
  potentially problematic policies".
- **The authors' scope** (Discussion): "we do not report this result
  intending to demonstrate a limitation of CEs per se".

## Concepts

Counterfactual explanation (validity, minimality, actionability,
robustness); algorithmic recourse; upstream interventions; fixed model
assumption; Rashomon effect; modally robust good; relational recourse;
justification versus recourse.

## Bearing on the record

- **CLAIM-tmpohafo** (explanation, contestation and interruption are
  separate entitlements). Corroborates its first split: an explanation can
  be given while the choices that would have to be contested stay hidden,
  and then "it may be impossible for subjects to reverse their decisions
  through contesting such choices absent appropriate transparency". That
  is explanation without contestation in a technical form, sharper than
  the claim's: the explanation points the subject at the wrong target. The
  paper says nothing about suspending execution.
- **CLAIM-tmpcpijj** (authority over a decision does not carry authority
  over the conditions of challenge). Related, not filed as a relation: the
  deployer fixes what an explanation-based challenge can see. The paper
  does not argue who should control that.
- **CLAIM-410**. Weakly related: the decisive discretion sits in the
  deployer's upstream choices of labels, measures and metrics, consistent
  with authority moving into design (Bovens and Zouridis, LIT-tmp8l2be).
  The paper makes no claim about governing positions.

## Verdict on the exchange's characterization

Faithful. A19: counterfactual explanations "can obscure the contestable
choices made upstream". The LIT's framing as "the distinction between
recourse and contestability" is the record's: the paper does not set the
two against each other, but argues that recourse properly understood is
relational and includes contesting the decision-maker's choices.

## Limitations

- One domain with proxy labels, two retrieval-based methods. The
  conclusions say the analysis "focuses on a single CE method and metric",
  though the experiments report two methods.
- The text says "four" interventions and lists five (τ being the
  baseline), and one passage refers to a "$40k baseline" where the stated
  default cap is $60k; the figures should be checked before anything rests
  on the numbers.
- The normative conclusions go beyond the experiments, which show
  sensitivity only, as the authors say.
- A v1 preprint; no venue is named.
