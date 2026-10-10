---
status: Active
title: 'Kovacs, Deutsch and Freitag''s metric bias in MBR decoding: translations a metric selects, that the metric and its neighbours rate better and human raters do not'
version: 1
standing: documented
tags:
- model-comparison
- translation
- representation-learning
date: '2026-10-10'
line: pragmatic-transport
supports:
- CLAIM-149
variant_of:
- CASE-041
summary: >-
  Minimum Bayes risk and quality-estimation decoding pick, from 128
  sampled translations, the one a neural metric scores best. That metric
  and other neural metrics rate the picks significantly better than
  greedy decoding; human MQM raters find them no better, and for four
  system and language-pair combinations significantly worse. [CASE-041](CASE-041.md)'s
  result in text, by selection rather than training. The distinction
  lost is accuracy, not a pragmatic one; a stipulated English-to-Russian
  ты/вы variant states the design that would make it pragmatic.
---
<!-- inactive-ok-file: CLAIM-149 — Proposed; the claim this case supports, open -->
<!-- inactive-ok-file: CLAIM-142 CLAIM-077 — Proposed; cited for what the stipulated variant would test, not as settled -->

# CASE-tmpt860v: Kovacs, Deutsch and Freitag's metric bias in MBR decoding: translations a metric selects, that the metric and its neighbours rate better and human raters do not

Found on 2026-10-10 by a search the owner asked for: a textual analogue of
[CASE-041](CASE-041.md), in which the score that selects a translation is also the score
that certifies it.

## The case

Kovacs, Deutsch and Freitag (WMT 2024) translate with Gemini 1.0 Pro, draw
128 samples for each source segment, and pick one by a utility metric. In MBR
decoding the pick is the candidate that scores best against the other
samples used as pseudo-references; in QE decoding it is the candidate a
reference-free quality-estimation metric scores best. The generator is not
changed. Only the selection is.

The authors state the problem in their abstract: MBR decoding "makes it
impossible to use the same metric for both decoding and evaluation, as
improvements might simply be due to reward hacking rather than reflecting
real quality improvements". Their finding: "neural metrics not only
overestimate the quality of MBR decoding when the same metric is used as the
utility metric, but they also overestimate the quality of MBR/QE decoding
with other neural utility metrics as well."

**The human evaluation (§5).** Raters gave MQM annotations to every
candidate system's output for 400 source segments per language pair (en-de
and zh-en from WMT 2023, with document context; en-ha, en-sw, en-ml and en-hi
from FLORES-200, in isolation). Single-metric MBR/QE decoding "does not
perform better than greedy decoding in our human evaluations" (§1). In four
combinations, MetricX MBR for zh-en, MetricX-QE for en-ml, AfriCOMET-QE for
en-sw and IndicCOMET MBR for en-ml, translations "were rated by humans as
significantly worse than greedy decoding (Table 3), even though automatic
evaluation with other neural metrics such as MetricX and XCOMET-XXL
estimated those translations as being significantly better than greedy"
(§5.2).

**The distinction lost (Table 4).** After "has it shipped?", the source
卖家说还没，下午才能发。 ("Seller says not yet, can ship in the afternoon.").
Greedy decoding: "The seller said not yet, and it will be shipped in the
afternoon." MetricX and XCOMET-XXL MBR decoding: "The seller said that they
don't have it in stock yet, and will be able to ship it out this afternoon."
The authors: these decoders, "as well as the reference-based MetricX and
XCOMET-XXL evaluations, all prefer a translation which inaccurately states
the item is out of stock." The human rater's MQM penalty for it was 11, against
1 for greedy decoding (lower is better). The
authors' reading is that single-metric MBR prefers "fluent yet inaccurate
candidates".

**The remedy.** An ensemble of utility metrics, which human evaluation finds
significantly better than greedy decoding (rankAvg:noNC, p < 0.001).

## What it can show

[CLAIM-149](../claims.d/CLAIM-149.md) in translation: a probe family that drives selection cannot
certify what the selection kept. The case is a variant of [CASE-041](CASE-041.md) in three
respects.

- **Text, not images.** It is the second documented instance, which weakens
  [CLAIM-149](../claims.d/CLAIM-149.md)'s hedge that it rests on "one case, in image generation".
- **Selection, not training.** It matches the resampling arm of
  Kynkäänniemi et al. in [CASE-041](CASE-041.md), where FID fell when a generator's outputs
  were resampled toward ImageNet class statistics without changing the
  generator.
- **The family, not only the metric.** The overestimate holds for neural
  metrics other than the one used to select. That is the condition [CLAIM-149](../claims.d/CLAIM-149.md)
  is about: a family of probes, not one probe.

It also shows [CLAIM-011](../claims.d/CLAIM-011.md)'s remedy at work. An ensemble is a less correlated
probe, and certifies what a single member could not.

## What it cannot show

**The partly met condition: a pragmatic distinction.** The search asked for a
case in which human evaluation finds a collapsed distinction of formality,
stance or politeness. This case meets the rest: a system selected against an
automatic score, the same score and its neighbours used to certify, and a
held-out human evaluation that disagrees. But the distinction it shows lost
is an accuracy distinction, "not yet shipped" against "out of stock". The
paper reports no formality or politeness error, and its MQM categories are
accuracy, fluency and other. The search found no documented case that joins
metric optimization to a pragmatic collapse.

**Selection, not training.** [CLAIM-149](../claims.d/CLAIM-149.md) is stated for "a probe family that
supplies a transformation's training signal". Here the metric selects among
outputs of a fixed model. The defender of the claim's scope can say the case
shows only that selection under a metric is overestimated by it, and that a
model trained against a metric could generalize differently. The case does
not answer that, though [CASE-041](CASE-041.md)'s training arm (Projected GANs) does, in
images.

**The defender's reply.** The strongest reply to the case as evidence for
[CLAIM-149](../claims.d/CLAIM-149.md) is the winner's curse. Picking the maximum of 128 noisy scores
overestimates the pick under that same score whatever the score measures, so
inflation under the selecting metric needs no shared probe family. The reply
does not reach the paper's second finding, that other neural metrics also
overestimate. But the paper does not show why they do. That they share
training data and paradigm, as Inception features and the Projected GAN
discriminator share ImageNet, is the analogy's reading, not the paper's
result. The authors' own hypothesis is narrower: MBR with MetricX "does not
consider the source sentence, so fluent hallucinations that occur in a large
number of pseudoreferences will be favored" (§5.2).

**Reliability of the human side.** "Our human evaluation used only a single
rater for each translation", in the paper's statement of its limits. The raters' qualifications are
not stated in the sections read. The result rests on one rater per
translation, and the paper says so.

**What the metrics are still good for.** The authors: "existing metrics still
correlate with human preferences" (§6). The case does not show the metrics
uninformative, only that they cannot certify their own selections.

## The stipulated variant that would make it pragmatic

No documented case joins the two halves, so the research report built one,
labelled stipulated. It joins this case to [CASE-tmpt7tsv](CASE-tmpt7tsv.md). Everything not
marked documented is stipulated.

- **Setup.** English-to-Russian subtitle dialogue, the domain of
  [CASE-tmpt7tsv](CASE-tmpt7tsv.md), whose T-V test sets are documented and public. System G is
  greedy decoding from a sentence-level model. System M is QE reranking of
  64 samples per sentence by a reference-free neural metric Q, such as
  CometKiwi, each sentence decoded on its own. This paper's evaluation is
  segment-level too, and it notes that MetricX and COMET have input limits
  (1024 and 512 tokens) that make document-level MBR hard (documented).
- **The same score certifies.** M is reported under Q and a sibling metric
  Q′ of the same family. Stipulated: M beats G under both.
- **Held-out probes fixed in advance.** First, Voita et al.'s deixis
  contrastive set (documented), applied to Q's choice: does Q prefer the
  T/V-consistent candidate? Second, a blind pairwise judgement of G against
  M on multi-sentence scenes by native Russian readers, asked whether the
  forms of address fit the relation.
- **Stipulated outcome.** Q, computed sentence by sentence, cannot see
  cross-sentence T-V consistency, so its preference is at chance on the
  first probe (the documented figure for a context-blind model is 50.0).
  Readers judge M no better than G overall, and worse on address where one
  character speaks to another across turns.
- **What it tests.** Whether M is an inadmissible transport in the sense of
  [CLAIM-077](../claims.d/CLAIM-077.md): the ты-scene and the вы-scene differ in the source context, and
  their images under Q do not. If so, Q's certification says nothing about
  the T-V distinction, and the case becomes a pragmatic instance of
  [CLAIM-149](../claims.d/CLAIM-149.md) and of [CLAIM-142](../claims.d/CLAIM-142.md).

The stipulated parts are the outcomes of both probes under QE reranking.
The domain, the test set, the 50.0 baseline and metric bias in MBR/QE are
documented. The experiment is cheap to run on public data. Its reader
judgement is the kind of item the interlingual arm of the discriminating
study, [CASE-tmp1uzfn](CASE-tmp1uzfn.md), would collect.

**Boundary.** This is an ML paper, held in neither record: a check of the
anthology clone on 2026-10-10 found no LIT for it. Its natural home is the
anthology. No nucleation LIT is filed. The anthology does hold two adjacent
works: [ANTH-LIT-647](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-647.md) (Ranzato et al., training against the test metric) and
[ANTH-LIT-795](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-795.md) (Gao et al., reward-model overoptimization).

## Sources

Every URL below was retrieved on 2026-10-10.

- **G. Kovacs, D. Deutsch and M. Freitag**, "Mitigating Metric Bias in
  Minimum Bayes Risk Decoding", *Proceedings of the Ninth Conference on
  Machine Translation (WMT 2024)*, DOI 10.18653/v1/2024.wmt-1.109,
  arXiv:2411.03524. Read directly, in the arXiv PDF; section and table
  references are to it. Not held in either record.
- **E. Voita, R. Sennrich and I. Titov** (2019), DOI 10.18653/v1/P19-1116,
  arXiv:1905.05979, for the stipulated variant's documented parts. Read
  directly; see [CASE-tmpt7tsv](CASE-tmpt7tsv.md).
- **Unverified.** The page range in the WMT proceedings, and the
  qualifications of the MQM raters, were not checked.
