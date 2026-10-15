---
status: Read
paper: LIT-tmp9g55n
title: Treisman & Gelade — A feature-integration theory of attention
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from a scan of the typeset article (Cognitive Psychology
    12(1), pp. 97–136, 40 pp., Academic Press 1980) hosted on a Princeton course
    page, COS 598B, spring 2008 readings: https://www.cs.princeton.edu/courses/archive/spring08/cos598B/Readings/TreismanGelade1980.pdf
    (HTTP 200 on 2026-10-15; PDF made with Acrobat Capture in 2003, so an OCR'd
    scan of the printed pages, not an author's manuscript). It is a course copy,
    not an open-access location of record: Unpaywall (api.unpaywall.org, 2026-10-15)
    gives is_oa false, oa_status closed, no OA locations; OpenAlex (W2149095485,
    2026-10-15) gives is_oa false, oa_status closed, any_repository_has_fulltext
    false, with only the publisher DOI landing page and the PubMed record (7351125)
    as locations. Text extracted with pdftotext (about 18k words). The OCR garbles
    colour subscripts (e.g. "X,,,,,") and some digits, so the stimulus definitions
    of Experiments I–III and Figures 1, 4 and 5 were checked against page images
    (pp. 103, 104, 110, 112). Read: the introduction and the five predictions, Experiments
    I–IX (method, results, discussion of each), the General Conclusions and the
    reference list. Nothing skipped. Treisman, Sykes & Gelade (1977), which Experiment
    I replicates, and Duncan & Humphreys (1989), the similarity account the record
    wants, were not read; this paper predates the latter. Every quotation below
    (24) was checked against the extracted text by script, with whitespace and quotation
    marks normalised and line-end and page-break hyphenation allowed for; four OCR
    misreadings in them ("3 set" for "3 sec", "OS" for "Os", "0" for "O", "2/l"
    for "2/1") were corrected from the page images.
date: '2026-10-15'
summary: >-
  In visual search for a coloured letter, a target that differs from all distractors
  by one feature (a colour, blue, or a shape, S, among brown Ts and green Xs) was
  found in a time almost independent of display size (positive slopes 3.8 ms/item
  for colour, 2.5 for shape, display sizes 1–30), while a target defined by a conjunction
  (green T among brown Ts and green Xs) gave linear slopes of 28.7 ms/item when
  present and 67.1 when absent, the roughly 1:2 ratio of serial self-terminating
  search; 13 sessions of practice did not make the conjunction pop out. Making the
  conjunction's colours and shapes harder to tell apart nearly tripled the slope
  but kept it linear, and a single-feature target hard to discriminate (an ellipse
  of intermediate size) was slow but not item-by-item serial. Even in feature search,
  target-absent trials were slow and grew with display size (25.1 ms/item). The
  displays were at most 30–36 well-spaced items on a card, with unlimited viewing;
  the paper argues that conjunction structure, not similarity, makes search serial,
  and does not model similarity.
---

# NOTE-tmpe7gfj: Treisman & Gelade — A feature-integration theory of attention

## Contribution

The paper states the feature-integration theory: separable features (colour, orientation, and some parts of letters) are registered "early, automatically, and in parallel across the visual field", while combining features into an object requires focal attention directed serially to one location at a time. It derives five kinds of prediction (visual search, texture segregation, illusory conjunctions, the dependence of identity on location, unattended interference) and tests three of them in nine experiments with colour-shape conjunctions and with letters. Experiments I–IV are visual search, V–VII texture segregation by card sorting or keypress, VIII–IX identification and localisation under brief masked exposure. The results are offered as new diagnostics for whether two dimensions are separable or integral.

## Key insight

What makes search serial is not how hard the target is to see but whether it can be told from every distractor by one feature it alone has. If it can, the feature maps announce it in parallel and the number of distractors hardly matters. If it shares each of its features with some distractor, so that only the combination identifies it, attention has to visit items one at a time to bind their features, and time grows linearly with the number of items, about twice as fast when the target is absent as when it is present. Difficulty and serial checking come apart: confusable conjunctions are searched serially at a slower rate, and a hard single-feature discrimination is slow without being item-by-item serial.

## Assumptions

- **Dimensions and features are inferred, not given.** "We will use the term 'dimension' to refer to the complete range of variation which is separately analyzed by some functionally independent perceptual subsystem, and 'feature' to refer to a particular value on a dimension." Colour and form are assumed separable "both on physiological and on behavioral grounds". Which shape properties count as features is an empirical question: "We cannot predict a priori what the elementary words of the perceptual language may be."
- **Parallel feature detection has limits.** Features are detected in parallel "within the limits set by acuity, discriminability, and lateral interference" (General Conclusions). The theory does not say all single-feature search is fast.
- **Serial self-terminating search** is inferred from linear slopes with a positive:negative ratio near 1:2. No eye movements were recorded.
- **Displays.** Hand-made cards of coloured stencilled letters on white, in a tachistoscope: Experiment I, 1, 5, 15 or 30 items scattered over a 14 × 8° area, letters 0.8 × 0.6°; Experiment II, 1, 4, 16 or 36 items in regular matrices with mean eccentricity about 4.3°. Density rose with display size. Subjects viewed until they responded and were told to avoid errors; error trials were rerun. Six subjects per experiment (Experiment II kept four of six).
- **No similarity model.** Similarity enters only as an alternative explanation to be ruled out (Experiments III and IV), measured by pilot matching times or by published letter-confusion matrices.

## Key results

**Experiment I, feature vs conjunction search (Table 1, slopes in ms per item, display sizes 1, 5, 15, 30).** Distractors in both conditions were brown Ts and green Xs in near-equal numbers. Conjunction target: green T. Feature condition: "either a blue letter or an S" (four possible targets, each sharing one feature with half the distractors).

| Condition | Positive slope | Negative slope | Positive intercept | Negative intercept |
|---|---|---|---|---|
| Conjunction | 28.7 | 67.1 | 398 | 397 |
| Feature (mean) | 3.1 | 25.1 | 448 | 514 |
| Feature, colour (blue) | 3.8 | — | 455 | — |
| Feature, shape (S) | 2.5 | — | 441 | — |

- Conjunction: linear component more than 99% of variance due to display size; positive:negative slope ratio 0.43, "quite close to half. These results suggest that search is serial and self-terminating with a scanning rate of about 60 msec per item." Variances rose more steeply for positives, as serial self-terminating search predicts.
- Feature positives: "search times were hardly affected by the number of distractors, the slopes averaging only 3.1 msec", and not linear (68% of variance). Feature negatives were linear (96.6%) with a slope of 25.1, positive:negative ratio "only 0.12". The authors' reading: "If the target is present, it is detected automatically; if it is not, subjects tend to scan the display, although they may not check item by item in the strictly serial way they do in conjunction search."
- With one item there was no conjunction cost: positive RT 422 ms for conjunctions vs 426 (shape) and 446 (colour); negatives 473 vs 500. "Thus the difficulty of search for conjunctions arises only when more than one stimulus is presented."
- Errors: conjunction false negatives 4.9% overall, 8.2% at display size 30 vs 3.8% at smaller sizes; feature 2.2% false positives, 2.1% false negatives.
- Practice: up to 13 blocks (1664 trials) on the green T gave "no sign of a switch from serial to parallel search"; slopes stayed linear. "The present experiment, however suggests that unitization of color and shape is difficult and may be impossible to achieve."

**Experiment II, discriminability within conjunction search (Table 2, display sizes 1, 4, 16, 36 in matrices).** Difficult: green T among green Xs and blue Ts, with green and blue inks "very similar to each other". Easy: red O among green Os and red Ns.

| Condition | Positive slope | Negative slope |
|---|---|---|
| Difficult discrimination | 55.1 | 92.4 |
| Easy discrimination | 20.5 | 39.5 |

Linearity above 99.8% in every case; positive:negative ratio 0.52 (easy) and 0.60 (difficult). Intercepts did not differ. "The slopes in the difficult discrimination are nearly three times larger than those in the easy discrimination, but the linearity and the 2/1 slope ratio is preserved". "For example, we can no longer suppose that search becomes serial only when it is difficult." Misses in the difficult condition rose to 5.9% at 16 and 20.7% at 36 items; two subjects were dropped because their false negatives on large displays exceeded 30%.

**Experiment III, a single-feature target that is hard to find (ellipses, Fig. 5).** Targets and distractors were black ellipses differing only in size. An intermediate-size target among small and large distractors, which shares similarity with every distractor as the conjunction target does, gave negatively accelerated functions, slower overall than colour-shape conjunctions (times "sometimes as long as 3 sec"). The large or small disjunctive targets were faster but also rose with display size (from Fig. 5, roughly 700 to 1600 ms for positives over 1–30 items). "When a single feature (size) defines the target, search can be slow but need not be serial in the sense of checking each item in turn." The authors attribute this kind of difficulty to the need for successive foveal fixations, and distinguish it from item-by-item attentional scanning, which only conjunctions require.

**Experiment IV, letters: conjunction vs similarity (Table 3, slopes ms/item, positives/negatives).** Conjunction sets, whose distractor parts could recombine into the target: T/IZ 12.2/34.7, R/PQ 27.2/52.1 (ratio 0.45, linear). Similarity sets, distractor more confusable with the target by confusion matrices but unable to form it: T/IY 5.3/18.1, R/PB 9.7/40.5 (ratio 0.26, positives significantly nonlinear). Heterogeneity control T/PQ (target has a unique horizontal line): 4.9/20.5. With a single distractor type the order reversed: R among Bs and T among Ys were slower than R among Qs and T among Zs (t(7) = 3.69, p < .02). "The finding that the similarity or confusability of individual items is not the only, or even the most powerful variable controlling search throws doubt on the adequacy of models such as those of Gardner (1973) and Estes (1972)." Misses rose to 15.5% at 30 items in the conjunction condition.

**Experiments V–VII, texture segregation.** A boundary between areas differing in colour, or in shape, was sorted about as fast as a drawn line (face-up: line 14.5, colour 15.9, shape 16.2 s per pack); a boundary defined only by conjunctions took 24.4 s, about 430 ms more per card. "The division between the two areas was highly salient with the feature packs and not at all with the conjunction pack." A disjunctive feature boundary (Experiment VI) was slightly slower than single features. With letters (Experiment VII), feature boundaries took 779–799 ms and conjunction boundaries 978–1114 ms; one subject of six showed no feature advantage.

**Experiments VIII–IX, identity and location under brief masked exposure.** Holding identification at about 80% correct needed 414 ms exposure for conjunction targets and 65 ms for feature targets. When the reported location was distant from the true one, conjunction identity was at chance (0.500 and 0.453) and feature identity was not (0.678 and 0.748; Table 4). Feature identity was "correctly perceived on perhaps 40% of trials on which the location was completely misjudged."

**General Conclusions, grouping.** Untested, but the authors predict that spatial grouping turns conjunction search into feature search: "In a display divided into 15 red Os on the left and 15 blue Xs on the right, we are very unlikely to scan serially through each of the 30 items to find a blue O, even though it is a conjunction target." They attribute the cost of interleaved conjunction displays to attention's being unable to select "a number of different locations, when these are interleaved with other locations to be excluded."

## Bearing on the record

The record's entries quoted below are quoted as they stood when this reading was done. [CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md), [CASE-tmpjgubn](../cases.d/CASE-tmpjgubn.md), [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md) and [CLAIM-tmp6u639](../claims.d/CLAIM-tmp6u639.md) were revised the same day in its light (curation entry of 2026-10-15 03:31).

**[CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md), part 3.** The paper supports the mechanism the claim uses, with conditions the claim leaves out. A target that alone has some feature, a colour or a distinctive shape part, is found in time almost independent of the number of items (3.8 ms/item for a blue letter, 2.5 for an S, up to 30 items); a target identified only by a combination of features its neighbours carry separately is found by checking items one at a time (28.7 ms/item present, 67.1 absent), and practice did not change that. So "search by what stands out" is right when what stands out is a single feature value no binmate shares. Three narrowings follow. First, the paper's serial search is caused by conjunctions, not by similarity: when items were merely similar on one dimension (Experiment III) search was slow but not item-by-item serial, and with letters the conjunction sets were slower than the more confusable similarity sets (Experiment IV). "If it is similar across binmates, search is serial and slow" is therefore half this paper's finding: slow, yes, if discrimination is hard; serial in its sense, only if the target must be identified by a combination of shared features. Second, pop-out has limits the claim does not state: feature search is parallel only "within the limits set by acuity, discriminability, and lateral interference", the colours used were few and distinct (blue against brown and green), and the paper never tested a colour target among nine other colours, among similar colours, or among hundreds of piled, overlapping items. Third, its General Conclusions offer, untested, a mechanism close to binning itself: spatially separating groups converts a conjunction search into feature searches within each group. That is the paper's prediction, not its result.

**[CASE-tmpjgubn](../cases.d/CASE-tmpjgubn.md).** "Ten distinct colours in a shape bin can be told apart at a glance" fits the colour-feature result if each colour is distinct and the wanted colour is unique in the bin; the paper tested one target colour against two distractor colours, not ten-way colour search, so this is an extrapolation. "Ten similar shapes in a colour bin cannot" is consistent with the paper but for a reason it would state differently. Whether a shape pops out depends on which shape feature distinguishes it: an S (curves) among Ts and Xs (straight lines) did pop out (2.5 ms/item), and a T found by its unique horizontal line among Ps and Qs was fast (4.9 ms/item). LEGO bricks of one colour that differ in stud count or length are more like the ellipses of Experiment III, which differ only in size or proportion (slow, fixation-limited, not item-serial), or like letters built from shared parts (Experiment IV, serial). The paper does not tell which kind a given brick is. The case's appeal to "the visual-search literature's similarity effect" is not this paper's finding; it argues against similarity as the cause of serial search, and the similarity account the case wants is Duncan & Humphreys (1989), unread.

**[CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md).** A single black brick among white ones is a single-feature target among homogeneous distractors, the most favourable case in the paper, and its feature results support "still detectable": time hardly grows with the number of distractors. They support more than "buried": by these results such a brick should be found nearly at once, in displays up to 30 items. Whether that holds in a bin of hundreds of overlapping bricks, where occlusion and the need to move items matter, the paper does not address. A brick "too similar to its binmates" is outside what it measured, except that a target hard to discriminate on one dimension gave the slowest search in the paper (Experiment III, up to about 3 s for 30 items), which is consistent with the case.

**The claim in preparation on absence under a deadline.** The target-absent data bear on it directly. In conjunction search, absent slopes were about twice present slopes (67.1 vs 28.7; 92.4 vs 55.1; 39.5 vs 20.5), the signature of a scan that stops at the first target found and must cover everything to say "no". Even when the target was a single pop-out feature, absent responses took a slope of 25.1 ms/item against 3.1 for present, ratio 0.12: confirming absence cost a scan where confirming presence did not, though the authors say absent scans in feature search "may not check item by item in the strictly serial way". The paper has no deadlines (viewing was unlimited and accurate responding was asked for), so it shows the asymmetry in time, not in success under a time limit. Two results come close to a deadline: misses rose with display size in serial search (8.2% at 30 items, 20.7% at 36 items for confusable conjunctions, 15.5% for letter conjunctions at 30), and under brief exposure a conjunction target needed 414 ms against 65 ms for a feature target to be identified 80% of the time. These support "presence is cheap to verify by one find, absence needs exhaustion"; they do not measure exhaustive search failing under a deadline.
