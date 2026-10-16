---
status: Read
paper: LIT-tmpdoq2o
title: 'Ma & Kragel — map-like emotion knowledge in hippocampus and vmPFC'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the publisher's open-access PDF (Nature
    Communications 17:1518, 14 pages, CC BY-NC-ND), fetched from
    nature.com/articles/s41467-025-68240-z.pdf on 2026-10-16 and
    extracted with pdftotext, page by page. Read: abstract, introduction,
    Results (all four sections), Discussion with its limitations, Methods
    (participants, emotion ratings, regions, TEM training and the
    emotion environment, decoding, representational geometry, the
    mixed-effects models and permutation tests), data and code statements
    and end matter; figure captions read, figures not seen as images. The
    reference list was scanned. The Supplementary Information
    (Supplementary Figs. 1–22, Tables 1–6) was not read. Page numbers are
    the article's. Quotations are verbatim from the extraction, with
    ligatures written out and
    citation superscripts omitted.
date: '2026-10-16'
summary: >-
  In fMRI of 29 people passively watching 14 emotional films, decoders
  trained on hippocampal patterns predicted an independent sample's
  consensus ratings of 13 emotion categories better than positions in a
  two-dimensional affective space, and vmPFC showed the reverse; patterns
  could also be decoded into the activity of a Tolman–Eichenbaum Machine
  that had learned a grid built from rating correlations by random walk,
  hippocampus favouring its small-scale conjunctive layer and vmPFC its
  large-scale structural layer. Effects are small (prediction–outcome
  correlations of about 0.04–0.10), and no learning in the participants
  was measured.
---

# NOTE-tmp4ffuf: Ma & Kragel — map-like emotion knowledge in hippocampus and vmPFC

## Contribution

The paper tests the proposal (its ref. 43, Ma, Vafaie and Kragel 2025)
that hippocampal–prefrontal systems hold emotion concepts as a cognitive
map: hippocampus binding particular concepts to locations, entorhinal
cortex and vmPFC holding the relational structure. It reanalyses the
public Emo-FilM fMRI dataset, decoding film-by-film emotion ratings and
the activations of a Tolman–Eichenbaum Machine (TEM). After it there is a
dissociation in naturalistic viewing: hippocampus carries more about
emotion categories, vmPFC more about positions in a valence–arousal
space, and a relational-memory model's two layers line up with that
split. Entorhinal cortex did not show the predicted structural code.

## Key insight

Treat emotion concepts as places. A map-learning model that separates
"what" (content, layer p) from "where" (relational structure, layer g)
and binds them yields unit activations that can be read out of the
hippocampus (small-scale p) and vmPFC (large-scale g) while people watch
films. The inference is from decodability of a model's units, weighted
by others' ratings, to a shared representational format. Nothing in the
study watches a map being learned or used.

## Assumptions

- **Passive viewing, no task.** 30 participants (29 analysed) watched 14
  films, mean 11 min 26 s, over four sessions (p. 8). "Although our
  experimental paradigm was not interactive" (p. 8). They made no
  responses during scanning that the paper uses.
- **The labels are other people's judgements.** "Emotion ratings ... were
  collected from 44 independent participants ... with no overlap between
  the two samples" (p. 9). Each rated six items continuously with a mouse
  on their own computers; consensus ratings averaged three or four raters
  per item and film. The same consensus time series is the decoding
  target for every fMRI participant. "the emotion concepts we decoded were
  based on self-report ratings from independent observers" (p. 7).
- **Items.** 13 discrete emotions; valence from "good" and "bad",
  arousal from "calm" and "at ease" (p. 9). Affective space is a 2D
  metric MDS of 1 − r between category rating time series concatenated
  across films (p. 9), so its axes are derived from co-occurrence in the
  ratings and are not valence and arousal by definition.
- **TEM.** Trained for 32,000 iterations on 16 random 11 × 11 grids with
  45-dimensional one-hot observations. "At each time step, it takes the
  current sensory observation (x) and an action (a) as inputs, and
  outputs a predicted sensory observation for the next timestep" (p. 9).
  Actions (up, down, left, right, stay) are chosen with equal
  probability. The "emotion environment" places each category at the grid
  node nearest its MDS position; the agent then walks it randomly for
  12,100 steps, and per-category activations come from the second half
  (pp. 9–10). Film-time TEM activity is the rating-weighted average of
  those per-category activations.
- **Decoding.** PLS regression (20 components) from voxel time series to
  each target, leave-one-film-out, performance as the Fisher-z
  correlation of predicted and observed time series (p. 10). Group
  inference by sign-flip permutation (10,000) on mixed-effects contrasts,
  CIs by parametric bootstrap (p. 11).

## Key results

- **Hippocampus: categories over space (p. 3).** Category ratings
  z = 0.0525 [0.0454, 0.0592] against affective-space locations
  z = 0.0428 [0.0347, 0.0505]; Δz = 0.0097, d = 0.4946, p < .001.
- **A shared hierarchy (p. 4).** Similarity among decoded category time
  series, leave-one-participant-out: full model Spearman r = .978, valence
  model r = .842, residual after valence r = .486.
- **Long axis (p. 4).** Posterior hippocampus decoded fine-grained
  categories better as granularity increased (Δz = 0.0101, d = 0.7791,
  p = .003). Amygdala below posterior hippocampus for categories
  (Δz = −0.0117, p = .001), comparable to anterior.
- **vmPFC: space over categories (p. 4).** Affective space z = 0.0956
  [0.0831, 0.1076] against categories z = 0.0838; Δz = 0.0118, p = .020
  (d printed as 0.0118). Region × target double dissociation with
  hippocampus Δz = 0.0215, d = 0.9566, p = .001. Entorhinal cortex and
  amygdala did not differ between targets.
- **TEM (pp. 5–6).** Hippocampus decoded layer p better than g
  (Δz = 0.0017 [0.0001, 0.0034], d = 0.3773, p = 0.015), more so at small
  scales (Δz = 0.0352, d = 1.3232, p < .001); small-scale p better in
  posterior than anterior hippocampus (Δz = 0.0052, p = .002). vmPFC
  decoded large-scale g better than p (Δz = 0.0712, d = 2.6747,
  p < .001), and better than hippocampus or entorhinal cortex did. Three-way
  region × layer × scale interaction F(8, 616) = 12.44, p < .001.
  Controlling for decoded p reduced the hippocampal readout of categories
  (Δz = 0.0042) more than of space (0.0014): p accounts for "some, but
  not all" of the category advantage (p. 6).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Hippocampal patterns during film viewing predict category ratings better than affective-space positions; vmPFC the reverse | moderate | leave-one-film-out PLS, n = 29, double dissociation p = .001; small absolute correlations |
| C2 | Decoded hippocampal category structure is graded, shared across participants and mainly organised by valence | weak to moderate | r = .978; but every participant's decoder is trained on the same consensus targets |
| C3 | Posterior hippocampus carries finer-grained emotion distinctions | moderate | Δz = 0.0101, p = .003; some categories reverse (p. 8) |
| C4 | Hippocampus resembles TEM's conjunctive layer and vmPFC its structural layer | moderate as decodability, weak as mechanism | Figs. 5, S16; one model, no rival model fitted |
| C5 | Map-like emotion representations "could result from learning the statistical regularities of event transitions" | conjecture | from the model; no learning measured in people (p. 8) |
| C6 | The valence–arousal map seen in self-report may be computed by hippocampal systems "rather than being an innate structure" | conjecture | Discussion, p. 8 |

## Method

Emo-FilM fMRI (OpenNeuro ds004892) and ratings (ds004872). Masks:
Julich-Brain hippocampus and entorhinal cortex, hippocampus split at
y = −21; vmPFC as Brodmann areas 10, 11, 14, 24, 25, 32. Targets
resampled to TR = 1.3 s and convolved with a canonical HRF. PLS
decoders per region and target; representational geometry by
correlating decoded category time series and agglomerative clustering;
leave-one-participant-out Spearman fits of full and valence models;
partial correlations controlling for decoded TEM p. Code on GitHub
(eccolaboratory/EmotionConceptRepresentation), TEM from torch_tem.

## Concepts

- **affective space.** Here: the 2D metric MDS of dissimilarity (1 − r)
  between the 13 categories' consensus rating time series, with film
  moments projected into it by rating-weighted category coordinates
  (p. 10).
- **map-like.** Representing concepts as locations in a relational space
  that supports inference about transitions; operationalised as
  decodability of space positions (vmPFC) and of TEM units.
- **transition (in the abstract).** In the model, a random-walk step
  between adjacent nodes of the grid built from rating co-occurrence. The
  study does not estimate transition probabilities between emotions in
  the films or in anyone's experience.

## Connections

It applies TEM (Whittington et al. 2020) to emotion, after grid-like
codes for abstract spaces (Constantinescu et al.; Park et al.;
Nitsch et al.) and the authors' review (ref. 43). Its affective space
descends from Russell's circumplex (ref. 1). It cites Barrett's
constructed-emotion work (refs. 3, 5, 74) and Lindquist and Satpute on the
default network's role in conceptualising emotion (refs. 72–73). It
names reinforcement-learning models of hippocampus as an untested
alternative (p. 8). In the record, Barrett's theory is NOTE-434 and
THEORY-057.

## Bearing on the record

- **How the map is learned.** Not studied in people. The participants
  only watched; their emotion labels came from others; no change across
  sessions or films is analysed. The learning in the paper is the TEM's,
  and the TEM learns by acting: its structural layer g "updates its
  representation based on the received action" by path integration
  (p. 9), and its agent explores by random actions. So the paper's own
  model of map learning is an action-in-the-loop learner, chosen from the
  spatial-navigation literature, not tested against an action-free
  alternative (my observation). Passive exposure, judgement and action
  are not separated.
- **Does the map shape how later episodes are read?** Not tested. Decoders
  generalise across films, which shows a representation shared across
  stimuli, not one that changes how the next film is read. The paper
  leaves the developmental question open: "longitudinal research is
  needed" (p. 7).
- **Constructed emotion, NOTE-434 and THEORY-057.**
  - The paper puts the decisive question as open: whether the concepts
    "reflect the statistical regularities of important life events that
    are shared across individuals and cultures, or whether they are
    constructed more flexibly as ad hoc categories shaped by individual
    experience, remains an open question" (p. 7), citing Barrett (ref.
    74).
  - Its closing conjecture, that the map "is the product of computations
    performed in hippocampal systems, rather than being an innate
    structure afforded by the human brain" (p. 8), is congenial to
    construction from experience, but it is about the valence–arousal
    structure, not about whether a concept constitutes the emotion.
  - Under THEORY-057's own promote_when, this is the kind of evidence
    that "cannot settle it": classifiers within one study. Leave-one-film-out
    generalisation is still one dataset.
  - The cross-participant hierarchy (r = .978) looks like evidence of a
    shared, not perceiver-specific, structure. But every participant's
    decoder is fit to the same consensus ratings, so similar decoded
    category correlations are partly built in (my observation). It does
    not count against perceiver dependence.
- **CLAIM-tmpq9do8.** The registration hoped for "an observer shaped by
  its history, through which later emotional episodes are read". The
  paper supplies a candidate substrate for such an observer, a learned
  relational structure separate from content, but no evidence that it is
  shaped by the agent's own judgements, and no evidence that it reshapes
  later reading. Where it models learning, action is in the loop. So it
  neither supports nor undermines the claim. If anything, it is a small
  reminder that the standard computational account of map learning is an
  action–perception one.
- **CLAIM-tmp84z6h.** TEM's factorisation, a structural code g reused
  across environments and a content code p bound to it by Hebbian
  memory, is an analogue of a context (frame) under which content is
  interpreted, and of a structure that persists while content changes.
  That is analogy, not evidence: the paper has no influence allocation
  and no judgement.
- **CLAIM-tmpt568z and QUESTION-tmpr5tck.** Nothing directly.
- **Checks of the current LIT.**
  - "hippocampal activity represented emotion concepts in a structured
    hierarchy and ventromedial prefrontal cortex tracked locations in a
    two-dimensional valence–arousal space": correct as decodability, with
    small correlations, and the space is an MDS of rating co-occurrence.
  - "responses were predicted by the statistical regularities of emotion
    transitions across several time scales": overstated. Brain patterns
    could be decoded into a TEM's multi-scale activations; the
    "transitions" are random-walk steps on a grid built from rating
    correlations, not observed emotion transitions.
  - The decoded emotions are an independent sample's consensus ratings,
    not the viewers' own reports.
  - "Why this is here" asked whether the map is shaped by judgement,
    passive exposure or action: the study does not say for people; its
    model learns by action.
- **For the anthology.** No instruction for machine-learning practice.

## Limitations

- Effects are small in absolute terms: prediction–outcome correlations
  near 0.04–0.10.
- No measure of the viewers' own experience; ratings from another sample.
- One model (TEM); reinforcement-learning alternatives named, not fitted
  (p. 8).
- Entorhinal cortex did not show the predicted structure, possibly for
  imaging reasons (p. 7).
- Two dimensions oversimplify emotion, as the authors say (p. 8); fMRI
  cannot see grid or phase codes.
- Reporting oddities: p. 3 says "13 films total" for leave-one-film-out,
  p. 10 averages "across the 14 validation sets"; vmPFC's d is printed
  equal to its Δz (0.0118), and the amygdala's d repeats entorhinal
  cortex's (−0.0195) (p. 4).
- Supplementary material was not read for this note.

## Open questions

- Does the map change with exposure within the study, across the four
  sessions? The dataset could be asked.
- Does decoding of the viewers' own ratings, if collected, follow the
  same dissociation?
- Does a map learned without action (for example by passive sequence
  exposure, as in successor-representation models) fit the data as well
  as TEM's action-driven one? That would bear on CLAIM-tmpq9do8.
