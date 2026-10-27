---
status: Read
paper: LIT-tmpl1s2e
title: 'Cammarata et al. — Curve circuits'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the Distill article,
    https://distill.pub/2020/circuits/curve-circuits/ (the page carries
    "Published Jan. 30, 2021" and prints DOI 10.23915/distill.00024.006),
    fetched the same day. The page's HTML holds only the title, the lead
    figure, the byline, the author contributions and the
    acknowledgements; the article itself is compiled into the page's
    index.js. Its text (about 20,600 characters) and the figure captions
    (about 8,400) were extracted by a static parse of the bundle's
    element calls; the bundle was not run. Read: the introduction, The
    Curve Detector Algorithm, The Components of Curve Detectors (3a
    early curves, 3a line families, lines, texture lines, cliffs, lines
    in conv2d2, cosmetic neurons), An Artificial Artificial Neural
    Network, Downstream, all footnotes and figure captions, the author
    contributions and the acknowledgements. The figures are interactive
    and were not rendered, so every number below is one the text or a
    caption states. The Colab notebook with the hand-written network was
    not opened.
date: '2026-10-27'
summary: >-
  The ten curve units of InceptionV1's mixed3b are traced back through
  four layers of families (Gabors, lines, early curves), each tiled along
  the curve's tangent with rotational and scale equivariance; negative
  weights from opposite early curves remove the 180° echo, which circuit
  editing restores. A hand-written network built from the description
  approximates the units on synthetic curves, by figure, and substituting
  it recovers 26 of the 46 top-5 classifications lost by deleting the
  units, on 2,000 images. The three arguments Curve Detectors deferred
  are supplied, mostly qualitatively.
---
<!-- inactive-ok-file: THEORY-tmpxjvwo THEORY-1013 THEORY-1022 THEORY-986 THEORY-802 — Proposed; the authors' wider claim filed from this reading and the accounts it bears on, cited as open -->
# NOTE-tmphb6el: Cammarata et al. — Curve circuits

## Contribution

It reverse-engineers the curve detectors of Curve Detectors ([LIT-1575](../literature.d/LIT-1575.md))
from the weights: which families of the four earlier layers build them,
the weight patterns that connect the families, and a reimplementation
written by hand from that description. The authors offer it as a test of
whether the Circuits approach can scale: "can we ever hope to understand
a full neural network this way?"

## Key insight

A circuit of more than 50,000 parameters can be described in a few
sentences when its families are equivariant. If every family is a set of
rotated copies of one unit, the strongest positive and negative weights
between two families describe all of them. The authors' estimate is that
rotational equivariance divides the complexity by 10 to 20, and scale
equivariance by a further 2 to 3, about 50 in all.

## Assumptions

- **Model and units.** InceptionV1; the ten curve units of mixed3b ("the
  fifth convolutional layer"), with 3b:379 as the worked example, as in
  Curve Detectors.
- **Families** are those of the Overview of Early Vision ([LIT-tmp6ii6u](../literature.d/LIT-tmp6ii6u.md)),
  extended here for mixed3a's line-like units: 11 simple lines, five
  "texture lines" and five "cliffs".
- **Decomposed feature visualization** uses a linear approximation of the
  network, ReLUs replaced by the identity, and visualizes the gradient
  from each earlier layer to the curve family at each spatial position.
- **Which families matter** is read from the highest-magnitude spatial
  position per layer, and the authors note that the answer depends on
  the metric (average or total weight), "since there is a long tail of
  neurons with low magnitude that collectively make up a large fraction
  of the total weight".
- **The hand-written network** was set by one person (Chris Olah) in "a
  few hour process", without looking at the original weights; before
  publication its weights were tweaked, "in particular added negative
  weights to remove echoes". It has no colour or texture units, so its
  curve units are grayscale.

## Key results

- **The schematic.** Gabor filters (conv2d0) become complex Gabors
  (conv2d1), which are tiled into lines (conv2d2), which are composed
  into early curves and lines (mixed3a), from which the curve units are
  built. Each family has positive weight "across the tangent" of the
  family it builds, and each is a set of rotated copies of
  approximately one unit. conv2d2 lines reach mixed3b both through
  mixed3a lines and through mixed3a early curves.
- **Early curves to curves.** The largest contributor. The weight matrix
  has a band of positive weights along the diagonal, where orientations
  match, surrounded by negative weights; the transition is smooth.
- **The echo.** Early curve units respond slightly to curves rotated
  180°. Curve units are inhibited by early curves of the opposite
  orientation, not by those at 90°, and have no echo. Removing those
  negative weights by circuit editing brings the echo back, shown by
  radial tuning curves for three conditions (unedited; early curves
  only; early curves with positive weights only). The authors generalize
  that negative weights are used for "things that are in some way
  similar enough that they could be mistaken", and compare lateral
  inhibition.
- **Lines.** mixed3a lines excite a curve unit along its tangent with a
  tolerance "between about 10° to 45°", sometimes asymmetric (3b:406 is
  excited by lines tilted 10° or more upward on its left and inhibited
  below 10°). The mixed3a line-to-curve weight matrix is "indecipherable";
  going back to conv2d2 lines shows the equivariant structure. Cliff
  lines accept error on one side of an orientation and not the other.
- **Cosmetic robustness.** The curve units also take input from mixed3a's
  65 texture units, which the authors suggest is how they inherit and
  strengthen invariance to texture and lighting. Not analysed.
- **The artificial artificial neural network.** Compared with the natural
  units by feature visualization (curves, in grayscale), responses to
  synthetic curves ("across a range of radii and orientations, our
  artificial curve neurons approximate the natural ones"; the artificial
  ones keep a slight echo), saliency on dataset examples, circuit
  structure and raw weights ("approximately like the ones in InceptionV1,
  but cleaner"). All five comparisons are figures.
- **One number.** Deleting the ten curve units drops top-5 accuracy on
  2,000 validation images from 88.6% to 86.3% (46 fewer correct);
  substituting the hand-written units gives 87.6%, leaving a gap of 20.
  So 26 of the 46 are recovered (57%). The authors call it "preliminary",
  give three reasons for the remaining gap (grayscale, receptive-field
  centring, activation scale), and say the subset was operational, not
  cherry-picked: their setup broke before the full set could be run.
- **Downstream.** In mixed4a, curve units are said to build circles,
  S-shapes, spirals, divots and evolutes, often at several spatial
  positions and across branches, and mixed4a's own curve units to be
  object-like (4a:406, tops of cups and pans). Described, not measured.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The curve units are built from Gabors, lines and early curves tiled along the tangent | moderate to strong for the strongest weights | decomposed feature visualization, family attribution, weight matrices |
| C2 | Rotational and scale equivariance reduce the circuit's complexity about 50-fold | weak (an estimate) | stated, not derived in the text |
| C3 | Negative weights from opposite early curves remove the echo | strong | circuit editing restores it |
| C4 | A hand-written network following the description approximates the natural curve units | moderate | five qualitative comparisons |
| C5 | Substituting it recovers more than half the accuracy lost by deleting the units | weak to moderate | 2,000 images, called preliminary |
| C6 | The described patterns "accurately reflect the underlying circuits" | moderate | C4 and C5 taken together |
| C7 | mixed3b curves are used in mixed4a to build more complex shapes | weak | described from weights, linked to examples |

## Concepts

- **Decomposed feature visualization**: a grid of feature visualizations
  of an earlier layer's expanded weights to a downstream unit, one per
  spatial position.
- **Equivariance motif**: each unit of a family is a transformed (here
  rotated or scaled) copy of another, so one connection pattern
  describes the rest.
- **Echo**: a weaker response to the stimulus rotated 180°.
- **Cliff line**: a line unit that tolerates error in one rotational
  direction and not the other.
- **Artificial artificial neural network**: a network whose weights are
  written by hand from a described circuit, to test the description.
- **Circuit editing**: changing chosen weights, here deleting negative
  ones, and observing the effect.

## Connections

The second of the planned three curve articles; Curve Detectors
([LIT-1575](../literature.d/LIT-1575.md), [NOTE-1198](NOTE-1198.md)) is the first, and the third, on prevalence across
models, is not held. It leans on the Overview of Early Vision
([LIT-tmp6ii6u](../literature.d/LIT-tmp6ii6u.md)) for its families and on Naturally Occurring Equivariance
(the thread's .004, not registered) for the motif. Neel Nanda's
attribution-patching post ([LIT-1581](../literature.d/LIT-1581.md), [NOTE-1201](NOTE-1201.md)) names "the curve circuits
work in image models" as the circuits work closest to general
understanding, and this is that work. Its reimplementation test is the
same move as the hand-coded curve detector Zoom In ([LIT-1543](../literature.d/LIT-1543.md)) reports.

## Bearing on the record

- **[THEORY-1013](../theory.d/THEORY-1013.md).** Zoom In's seven arguments for a curve detector are now
  all held for the mixed3b family: four in Curve Detectors ([THEORY-1028](../theory.d/THEORY-1028.md))
  and the circuit, the downstream use and the reimplementation here
  ([THEORY-tmp90225](../theory.d/THEORY-tmp90225.md)). That settles the example, not the account. The
  promote_when asks for a fraction over whole layers and for
  "weight-level predictions of what editing them changes, tested by
  editing them". The echo edit is one such prediction, made and
  confirmed, for one family. There is still no denominator beyond the
  Overview's labels ([NOTE-tmpdmtd9](NOTE-tmpdmtd9.md)), and the account stays Proposed.
- **[THEORY-1022](../theory.d/THEORY-1022.md).** Its promote_when asks for a hand-written curve
  detector that predicts the units' activations across the whole
  activation distribution, weak firings included, and for an
  intervention showing downstream use. The reimplementation exists, but
  it is compared on synthetic curves, strongly activating dataset
  examples and weights, not on the weak firings, and it is grayscale;
  the substitution experiment is an intervention on accuracy, not on
  downstream curve use. Neither condition is met. The authors' own
  footnote expects "many false-negatives". The account stays Proposed.
- **[THEORY-986](../theory.d/THEORY-986.md) (universality).** Nothing across models here.
- **[THEORY-802](../theory.d/THEORY-802.md).** The analysis is in the neuron basis, and the
  long-tail footnote ("a long tail of neurons with low magnitude that
  collectively make up a large fraction of the total weight") is a
  reason to doubt that the strongest weights describe the whole.
- **Accounts filed.** [THEORY-tmp90225](../theory.d/THEORY-tmp90225.md) (Active): what was measured and
  shown. [THEORY-tmpxjvwo](../theory.d/THEORY-tmpxjvwo.md) (Proposed): the authors' claim that curve
  detection is a simple algorithm read off the weights and confirmed by
  reimplementation.

No instruction for machine-learning practice; the anthology may want the
work as a reading (`anthology-candidate`).

## Limitations

- **Qualitative comparisons.** Every comparison of the hand-written and
  natural units is a figure. No correlation of activations, no fraction
  of variance explained, no comparison on randomly drawn positions.
- **The one number is small and partial**: 2,000 images, one run, and a
  recovered gap of 26 images, which says the hand-written units do some
  of the natural units' work, not that they do it the same way.
- **The hand-written network was tuned after the fact.** Its negative
  weights were added "before publishing" to remove echoes, so the echo
  comparison is not blind, as the authors say.
- **The strongest weights.** Families were chosen by the
  highest-magnitude position and strongest connections; the authors note
  the long tail.
- **Figures not rendered** in this reading, so no number was taken from
  a chart.
- **Internal inconsistencies and slips.**
  - Downstream says the curve units "are used to build" sophisticated
    curves, circles, S-shapes, spirals, divots and evolutes in mixed4a,
    but each of those words links to a mixed3b group of the Overview,
    the curve units' own layer; the sentence is the Overview's mixed3b
    text nearly verbatim. A unit cannot be built from units in its own
    layer, so either the links are wrong or the layer is.
  - The circuit figure's caption: "The first later constructs a family of
    Gabor Filters".
  - The weight-comparison caption ends "programmetically generated.
    equivariance.", a stray word.
  - The "more than 50,000 parameters" and the "~50x" reduction are
    stated, not derived; the product of "10-20x" and "2-3x" is a range of
    20 to 60, which contains 50.
  - The arithmetic of the accuracy footnote checks: 2.3% of 2,000 is 46,
    1.0% is 20, and 26 of 46 is "more than half".
  - The printed DOI did not resolve on 2026-10-27 (see [LIT-tmpl1s2e](../literature.d/LIT-tmpl1s2e.md)).

## Open questions

- How well do the hand-written units predict the natural units'
  activations on positions drawn across the whole distribution, weak
  firings included?
- Does the substitution result hold on the full validation set, and with
  colour and texture inputs added?
- How much of the curve units' input weight do the named families carry,
  given the long tail?
- Is the downstream use in mixed4a, or in mixed3b's own neighbours, and
  does an intervention on curve units change those shape units?
