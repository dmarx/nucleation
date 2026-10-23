---
status: Read
paper: LIT-tmp9qnrb
title: 'Brain networks subserving functional core processes of emotions identified with componential modeling'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: the published version (CC BY 4.0) in the Archive ouverte
    UNIGE, pp. 7993–8010, with Table 1 and the figure captions. Page
    references are the journal's. The brain maps (Figure 7), the loading
    plots (Figure 6) and the supplementary results, including the
    correlations of each process with discrete emotions, were not seen.
    Every quotation was checked by script against the extracted text.
date: '2026-10-23'
summary: >-
  fMRI during 40 films, with each of 119 short events rated on 32 CoreGRID
  features. PLSC gives six brain–behaviour processes: valuation, novelty,
  hedonic impact, goal monitoring, caring for others and
  approach/avoidance. Valence splits into a wanting-like valuation network
  carrying the action tendencies and a liking-like hedonic network
  carrying feeling and expression, and no arousal process appears. There
  is no synchronization measure, but every event gets a signed score on
  each process.
---
<!-- inactive-ok-file: THEORY-tmp0bbxk CLAIM-tmpe0iew CLAIM-tmpz8lli TERM-tmp8gbrt — Proposed; the wanting-without-liking objection, the proposal it presses and the term, which this reading bears on -->
<!-- inactive-ok-file: LIT-tmp9qnrb LIT-tmp7rygg LIT-tmpzf3da NOTE-tmphslle LIT-tmp5ejuc — drafts filed in the same tranche -->

# NOTE-tmpocnqb: Brain networks subserving functional core processes of emotions identified with componential modeling

## Contribution

The first study to relate the CPM's componential features, rated per
event, to whole-brain activity. It decomposes emotional experience
into data-driven "functional core processes" (FCPs), each a weighted
combination of features with a brain map. The CPM is taken as "a
presumption to reveal potential core processes", not a theory under test
(p. 7994).

## Key insight

The building blocks of emotion in the brain are not the CPM's five
components one by one, nor valence and arousal. They are mixed
processes that cut across components. One of them looks like wanting
and another like liking.

## Assumptions

- That ratings on re-viewing, given by pausing the video immediately after
  each event, reflect the experience during the first viewing in the
  scanner.
- That one canonical HRF per event is adequate: "we used a single HRF
  function for every emotional event in movie clips to model the BOLD
  signal" (p. 8007), conceded as neglecting carry-over and habituation.
- That physiology should not be regressed out of the BOLD signal, being a
  component of interest.

## Key results

- **Behaviour.** Clustering of emotion profiles splits positive from
  negative, then pleasant feelings, distress, annoyance and surprise. Six
  factors explain 47.8% of the variance: pleasantness, arousal,
  expression, novelty, action tendency, social norms.
- **PLSC.** Six significant latent variables, explaining 19.0, 11.0, 6.0,
  5.1, 4.6 and 3.4% of the covariance. "Their weighted sum represents a
  specific combination linked to a particular brain activation pattern,
  whose expression characterizes a given functional core process (FCP)
  underlying the generation of an emotion response" (p. 8002).
- **FCP-1, valuation.** Low unpleasantness, low incongruence with
  standards, wanting to continue and not to stop, feeling good. Positive
  in vmPFC, lateral OFC, amygdala and VTA, and negative in anterior and
  dorsal insula, mid-cingulate, thalamus and striatum. Read as "wanting",
  since it carries action features and low feeling intensity.
- **FCP-3, hedonic impact.** Expression features (eyes, lips, eyebrows)
  with warm, good, intense and lasting feelings. Positive in sensorimotor
  operculum (face area), SMA, dorsal ACC, posterior insula, ventral
  pallidum, VTA and pons. Read as "liking".
- **Physiology.** HR and RR load negatively on LV5 and LV6. LV2 is
  negative and LV4 positive for HR alone. "We also note that we found no
  component uniquely associated with peripheral physiology changes during
  emotion events" (p. 8007).
- **Valence–arousal control.** PLSC on the feeling items alone gives two
  latent variables, valence and arousal, with the familiar brain
  correlates and less explained covariance.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Emotional experience decomposes into at least six brain–behaviour core processes | moderate | PLSC, permutation p < 0.01, bootstrap stability over subject subsets; 20 participants |
| C2 | Valence has two distinct substrates, a wanting-like valuation network and a liking-like hedonic one | weak–moderate | two latent variables with valence features and different maps; interpreted post hoc |
| C3 | Arousal is not a single functional process | weak | absence of an arousal FCP in the full model |
| C4 | The core processes mix features of several CPM components | moderate | loading profiles (Figure 6) |
| C5 | "Being moved" has its own process, in the default mode network | weak | LV5, interpreted post hoc |

## Concepts

- **functional core process (FCP)**: a latent variable of PLSC, a
  weighted feature profile paired with a brain saliency map, shared
  across emotion categories.
- **PLSC**: partial least squares correlation, an SVD of the
  brain–behaviour correlation matrix giving paired latent variables of
  maximal covariance.

## Connections

Realizes in part the five-network programme of Sander, Grandjean and
Scherer ([LIT-tmpzf3da](../literature.d/LIT-tmpzf3da.md), [NOTE-tmphslle](NOTE-tmphslle.md)). The processes it
finds do not correspond to the five networks. Reuses the film set and
CoreGRID items of Mohammadi and Vuilleumier ([LIT-tmp7rygg](../literature.d/LIT-tmp7rygg.md)). Its
two valence networks are read through Berridge's wanting and liking,
which the record holds first-hand in Berridge and Kringelbach 2015
([LIT-tmpmp2nw](../literature.d/LIT-tmpmp2nw.md)).

## Bearing on the record

**A per-episode measure of synchronization?** No. Synchronization is not
computed. Each event's brain signal is a single GLM contrast over 12
seconds, and each event's features are a single rating. The covariance
PLSC extracts is across events and subjects. What the method does give
per episode is a score. The latent variables are defined per observation
(the behavioural scores are the rating matrix times the saliences), so
every event has a signed value on each process, both from its ratings
and from its brain map. The paper reports loadings and maps, not these
event scores. For [QUESTION-tmpsqwu5](../questions.d/QUESTION-tmpsqwu5.md) this is a per-episode, signed,
brain-and-report measure of which pattern an episode expresses. It is
still not a measure of potential. A high FCP-1 score means the episode
had the valuation pattern. It does not mean that pattern won a conflict
against another one.

**Signed, or which tendency prevails?** FCP-1 is the one process here
that is signed along an action-tendency axis. Its positive pole is
the item "Want the situation to continue?", its negative pole the items
"Feel the urge to stop what was happening?" and "Want to undo what was
happening?" (Table 1). On [TERM-tmp8gbrt](../terms.d/TERM-tmp8gbrt.md) it is the closest thing in these
five papers to a measure that tracks potential and valence together: an
evaluation network whose sign follows the direction of the prevailing
tendency. Two cautions. The tendencies are reported, not enacted, and in
passive viewing there is nothing to continue or stop. And the sign is
of a bipolar factor, which by construction cannot represent "continue"
and "stop" both high, the ambivalent case. PLSC on a design with choice
points would be needed.

**On [QUESTION-tmp0oife](../questions.d/QUESTION-tmp0oife.md) and the wanting/liking objection.** This is the
result that matters for the record. In human brain data recorded during
naturalistic episodes, valence features load on two separate processes:
- **FCP-1** carries the action tendencies (continue, stop, undo) with
  vmPFC, OFC, amygdala and VTA, and the authors read it as "wanting".
- **FCP-3** carries feeling intensity and facial expression with the
  sensorimotor face area, posterior insula and ventral pallidum, and they
  read it as "liking". "Our findings of 2 distinct networks (FCP-1 and
  FCP-3) correlating with valence features converge with growing evidence
  that this dimension may not have a unique psychological or neural
  underpinning" (p. 8006).

For [QUESTION-tmp0oife](../questions.d/QUESTION-tmp0oife.md)'s layers this is close to a human dissociation of
layer 1 (potential, read off the tendency that governs: FCP-1) and
layer 2 (a hedonic marker that does not depend on choice: FCP-3, whose
rated expression features are a rough human analogue of taste
reactivity's orofacial signs). It agrees with Berridge's animal work ([LIT-tmpmp2nw](../literature.d/LIT-tmpmp2nw.md)),
which [THEORY-tmp0bbxk](../theory.d/THEORY-tmp0bbxk.md) and [CLAIM-tmpe0iew](../claims.d/CLAIM-tmpe0iew.md) use against the proposal that
valence is potential by a self-maintenance ordering ([CLAIM-tmpz8lli](../claims.d/CLAIM-tmpz8lli.md)).
It is weaker evidence than it looks, for three reasons:
- The two processes are orthogonal by construction (PLSC latent
  variables are orthogonal), so their separation is partly the method's.
  What is not imposed is the difference between their brain maps.
- Both are read from one retrospective report. FCP-3's "liking" is
  rated expression and rated feeling, not a measured face. Facial EMG
  was attempted and lost.
- They correlate with the same discrete emotions in the same direction
  (FCP-3 "shows strong positive correlation with joy and love, but
  negative correlation with sadness and anxiety, like FCP-1", p. 8006).
  So across these films the two coincide in sign, even though they load
  on different features. Wanting-without-liking needs episodes where
  they come apart, and the paper does not report any.

So the paper does not show the dissociation [THEORY-tmp0bbxk](../theory.d/THEORY-tmp0bbxk.md) needs. It
shows that the two layers have separable substrates in humans and could
be measured separately, with event scores on FCP-1 and FCP-3 as
candidates. That is what [QUESTION-tmp0oife](../questions.d/QUESTION-tmp0oife.md) asks for: each layer
measured without the others.

**Arousal.** The absence of an arousal process bears on the intensity
clause of [TERM-tmp8gbrt](../terms.d/TERM-tmp8gbrt.md) only weakly. If arousal is not one process, an
unsigned intensity read off arousal would not be one quantity either.

## Limitations

Twenty participants. Ratings given on re-viewing, after the scan. One HRF
per 12-second event. Vicarious, passive emotion. Post hoc
interpretation of every latent variable, with the risk of reverse
inference the authors acknowledge. Facial EMG and electrodermal data
lost. The data are available only on request.

## Open questions

Whether the per-event FCP-1 and FCP-3 scores ever come apart in sign
within this dataset (wanting without liking, or the reverse), which would
be the human dissociation the record lacks. Whether the analysis on a
design with choice points (the VR route of [LIT-tmp5ejuc](../literature.d/LIT-tmp5ejuc.md))
would let FCP-1's sign be read as the tendency that prevailed.
