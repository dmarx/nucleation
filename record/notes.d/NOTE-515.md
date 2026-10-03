---
number: 515
status: Read
formerly:
- NOTE-tmp3gtyn
paper: 'LIT-658'
title: 'Knowledge is a Region in Weight Space for Fine-tuned Language Models'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v3, main text and Appendices A–H.
    Figures were read from captions and the text that describes them; the
    plotted loss curves themselves were not recoverable from the HTML. The
    numbers below are the ones the text and Tables 1–3 state.
date: '2026-10-03'
summary: >-
  Task vectors of RoBERTa-base fine-tuned on 12 datasets × 20 seeds cluster
  by dataset with 98% accuracy, and by task family (NLI, sentiment, topic)
  with 90%. Hull samples of a group's fine-tuned models beat every outside
  model on the group's data and beat the group's own members in 88% (MNLI)
  to 96.7% (NLI family) of comparisons; extrapolation past the members fails
  fast. The centroid of models from other datasets, re-tuned with BitFit, is
  a better start than the pretrained model on 9 of 12 datasets.
---

# NOTE-515: Knowledge is a Region in Weight Space for Fine-tuned Language Models

## Contribution

It replaces "two fine-tuned models are linearly connected" with "fine-tuned
models of a kind span a low-loss region". The region exists at three nested
grains: one dataset, one task family, and general language classification
around one pretrained model. The paper adds a way to compare models
fine-tuned on different datasets (a refitted linear probe), and a practical
use: the region's centroid as a better starting point.

## Key insight

Fine-tuning from one pretrained model does not scatter solutions around it.
It sends them in a direction the data determines, and the members of a group
mark out a small convex basin whose interior is at least as good as its
members. The members sit at the basin's edge, so averaging moves inward.

## Assumptions

- **One pretrained model**, RoBERTa-base, except App. B, which adds a second
  RoBERTa-base pretraining (Elazar et al.). Models from the two cluster by
  pretrained model, not by dataset, so the region is a property of a
  starting point, not of a task as such.
- **Classification only**, English, 36 datasets in families: General (12
  GLUE/SuperGLUE sets), NLI (6), sentiment, topic, Twitter (App. A).
- **Hyperparameters fixed**: batch 256, learning rate 5e-5; seeds vary the
  classification-head initialisation and data order (§2.2). 5 seeds in most
  experiments, 20 in the per-dataset clustering.
- **Generalized loss** (§3): the encoder is frozen, a new head is fitted by
  linear probing on the target's training set, and test loss is reported,
  l_g(ω) = l(f_{φ,ω}(x_test), y_test) with φ = argmin_φ l(f_{φ,ω}(x_train),
  y_train). Region claims are therefore about the encoder's representations
  as read by a linear probe, not about the full fine-tuned model's outputs.
- **Exterior baseline for the General level**: the pretrained model
  perturbed in a random Xavier-shaped direction with the norm of the average
  task vector (§3.1).
- **The hull is sampled**, |In| uniform draws of convex weights (§5.2).

## Key results

- **Clustering** (§4, Fig. 2, spectral clustering on cosine of task vectors):
  280 models, 12 clusters, 98% accuracy with all but 3 clusters perfect;
  3 task families, 90% accuracy. Per-family F1 with a Twitter domain group
  added: Twitter 30, NLI 100, Topic 61, Sentiment 71 (Table 1, App. D): domain
  does not form its own region, or it overlaps the task regions.
- **Data type, not size** (§4.1, App. C): sub-samples of 200 to 3K examples
  cluster by dataset, not by size; direction is set with little data (Fig. 8).
- **Interpolation** (§5.1, Fig. 3): 10 MNLI–MNLI pairs, 25 MNLI–ESNLI pairs,
  25 MNLI–SST2 pairs. Interpolated models perform comparably or better than
  endpoints at all three levels; the best loss often lies between them.
- **Region comparison** (§5.2), PB = P(In model loss ≤ Ex model loss):
  - dataset (MNLI): In 100%, In′ (hull) 100%, In′ better than In 88%;
  - task (NLI): In 75.3%, In′ 100%, In′ better than In 96.7%;
  - general: In 89.8%, In′ 100%, In′ better than In 90%.
- **Edges** (§6, Fig. 5, App. G): extrapolating α from 1 to 32 and 0 to −31
  in log steps reaches poor loss quickly at all levels: "a relatively flat
  base and steep cliffs". WNLI behaves as outside the NLI region (Fig. 13b).
- **Other directions** (App. F): moving from the MNLI centroid in random
  directions leaves the region once the radius exceeds the members' spread;
  moving towards the origin does not, even far beyond it. The authors have no
  explanation.
- **Centroid as initialisation** (§7, App. H, Table 2): BitFit from the
  centroid of all General models except those of the target, against BitFit
  from the pretrained model: mean accuracy 65.54 vs 61.51 (gain 4.03),
  better on 9, equal on 2, worse on 1 (WNLI, −1.41). Few-shot (1K examples),
  Table 3: mean 54.88 vs 65.54, a gain of 10.66, largest on SST-2 (33.99)
  and MNLI (28.97).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Fine-tuned task vectors from one pretrained model cluster by dataset and by task family | strong for this model and these datasets | §4, Fig. 2, Table 1 |
| C2 | The convex hull of same-group fine-tuned models is low-loss, and its interior often beats its members | moderate: probe-based loss, sampled hull, 5 seeds, one pretrained model | §5.2, Fig. 4 |
| C3 | Fine-tuned models lie near the edge of a small basin with steep walls | moderate: extrapolation along member lines; App. F finds the origin direction is not a wall | §6, App. F, G |
| C4 | The direction of fine-tuning depends on the data type, not the data amount | moderate: 9 datasets, 5 sizes | §4.1, App. C |
| C5 | The centroid of other datasets' fine-tuned models is a better start for BitFit than the pretrained model | moderate: one PEFT method, 12 targets, single runs reported | §7, Tables 2–3 |
| C6 | The region picture explains why weight averaging and soups work | weak: argued in prose, not tested against them | §8 |

## Concepts

- **task vector**: fine-tuned weights minus pretrained weights (after Ilharco
  et al.), used here for clustering.
- **generalized loss l_g**: the test loss of a frozen encoder with a head
  refitted on the target dataset.
- **In / In′ / Ex**: the fine-tuned group, samples from its convex hull, and
  the models outside the group.
- **PB**: the probability that a model from one group has loss no higher than
  a model from another.

## Connections

- **Frankle et al. ([LIT-654](../literature.d/LIT-654.md)).** The paper cites it with Garipov et al.
  ([LIT-673](../literature.d/LIT-673.md)) for curved and linear paths between runs on one dataset, and
  its own setting is a shared starting point taken to many runs.
- **Entezari et al. ([LIT-652](../literature.d/LIT-652.md)).** Cited in §1 as the finding replicated
  here ("models finetuned on the same dataset are linearly connected") and in
  §8 alongside McMahan et al. for shared initialisation producing linear
  paths. Entezari et al. study networks from different random
  initialisations and their connectivity modulo permutation, so the citation
  is loose.
- **Benton et al. ([LIT-656](../literature.d/LIT-656.md))** is cited for simplexes of low loss, the
  nearest precedent for a region rather than a path.
- **Mirzadeh et al. ([LIT-651](../literature.d/LIT-651.md))** is cited for multitask learning
  reaching a point with low loss on both tasks.
- **Juneja et al. 2022** (not in the record) reported several basins per
  dataset; this paper finds one region per dataset or task, and App. B finds
  separate regions per pretrained model. The two are not reconciled.
- **Model soups ([ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md)), WiSE-FT ([ANTH-LIT-674](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-674.md)), SWA ([ANTH-LIT-673](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-673.md)).**
  §8 reads soups as picking a point inside a dataset region, and suggests
  SWA-style methods succeed by falling inside the region rather than on its
  border. That is an interpretation, not a test.

## Bearing on the record

- A THEORY candidate: fine-tuning from a shared pretrained point lands on
  the edge of a convex, task-specific low-loss region, and averaging moves
  inward. Its evidence would be C2 and C3 here, with the multitask case of
  Mirzadeh et al. Not filed; reported as a candidate.
- **ML instruction.** §7 carries one ("average models from the same region",
  "start from the centroid"). That is the reason for the
  `anthology-candidate` flag. The anthology's model-soup practice
  [ANTH-SOTA-407](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-407.md) is the nearest home.

## Limitations

- One architecture and essentially one pretrained model; the authors say it
  "may not hold in general when randomly initializing" (§10).
- Losses are probe-based; a hull point that probes well need not be a good
  end-to-end classifier, and the paper does not report end-to-end accuracy
  for hull points.
- The abstract reports an average gain of 3.06 from the centroid; §7 says
  4.04% and Table 2 gives 4.03. The three numbers are not reconciled.
- Table 3's centroid ("Fuse") row is identical, value for value, to Table
  2's, although Table 3 is the 1K-example setting and only the pretrained
  row changes. Either the centroid was unaffected by limiting the data to
  1K, which the text does not say, or the row was copied. The few-shot gain
  rests on that row.
- The hull is estimated with as many samples as there are members (5 per
  group in most settings), which is a thin sample of a high-dimensional set.

## Open questions

- Why does moving from the centroid towards the origin stay low-loss far
  past the region (App. F)?
- Do domains form regions of their own that overlap task regions, or no
  regions at all (App. D)?
- Does the region survive end-to-end evaluation and generative tasks?

## Corrections

- none to a seeded skim (there was no seed)
- **Title.** arXiv's metadata title is "Fine-tuned"; the HTML rendering of
  v3 prints "Finetuned". The record uses the metadata form.
