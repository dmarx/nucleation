---
number: 108
status: Read
formerly:
- NOTE-tmp943v3
paper: LIT-162
title: 'Søgaard — Is unsupervised clustering somehow truer?'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the open-access (CC BY) publisher PDF, Minds
    and Machines 34:43 (2024), 14 pp. (via rd.springer.com), read in full:
    §§1–4, footnotes 1–4, Fig. 1, acknowledgements and references.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-26'
summary: >-
  Søgaard rebuts two arguments that unsupervised clustering is
  epistemically superior to supervised classification. The No-Bias
  Argument fails because clustering is also sensitive to sample bias (a
  toy example moves the boundary from x = 7 to x = 6), and it is more
  sensitive to representation bias. The Simplicity-Truth Argument fails
  because clustering is also function estimation and overfits in the same
  way (Hansen & Larsen 1996). From the fact that every clustering
  hypothesis is in a supervised classifier's hypothesis class, he
  concludes that supervised classification is "at least as justified", but
  that positive step is under-argued.
---

# NOTE-108: Søgaard — Is unsupervised clustering somehow truer?

## Contribution

Søgaard names and rebuts two arguments in the philosophy of ML for the epistemic superiority of unsupervised clustering over supervised classification. The **No-Bias Argument** (attributed to Watson 2023a and Nelson 2020) holds that clustering escapes label bias and cheaply mitigates sample bias. The **Simplicity-Truth Argument** (Rochefort-Maranda & Liu 2020) holds that parametric simplicity links to truth only in unsupervised contexts, because there is "no such thing as ... 'overfitting models'" there. He shows that each argument's premises are false or unsupported. He then argues positively that supervised classification is at least as justified, and may be more justified where labels carry epistemic value or where computational efficiency matters.

## Key insight

Clustering and classification are both learning algorithms that induce a function from data to a partition. Clustering therefore inherits the familiar vulnerabilities (sample bias, overfitting, the curse of dimensionality) and adds its own, notably extreme sensitivity to input representation. Nothing about the *absence of labels* confers privileged access to the "intrinsic structure" of the data. The burden is shifted "from design to interpretation" (§1.2).

## Assumptions

- **Epistemic status** = "how justified we would be in accepting conclusions derived from the application of such models to data" (§1, p. 2). Each partition is a hypothesis. Partitions are ranked by a preference ordering, which realists read as correspondence to mind-independent groupings and pragmatists as a utility (p. 2). He is neutral between the two.
- Epistemic status depends on four data/algorithm characteristics: sample size, sample bias, label bias and inductive bias (§1.1). The comparison is made "all things being equal", meaning fixed sample size n and fixed inductive bias (§2.1.1, §2.2).
- Clustering and classification are compared as algorithm families. Particular pairings stand in for the comparison: GMM+EM vs Naive Bayes, k-means vs k-NN, one-class vs regular SVM (§2.3).
- Rochefort-Maranda & Liu's claims are read as general, not as confined to k-means, which is defended in fn. 2 by quoting them.
- The settings are toy examples: 1-D points {1,2,3,4,5,9,10,11}, three separable equidistant Gaussian blobs, and twenty 2-D points (Fig. 1). No empirical study is reported.

## Key results

- **Hypothesis-space framing (§1).** The number of partitions of n items is the Bell number, B_{m+1} = Σ_{k=0}^{m} C(m,k) B_k with B_0 = 1. The number of partitions into k blocks is the Stirling number S(n,k) = k·S(n−1,k) + S(n−1,k−1) (p. 2; see the correction on the S(n,5) sequence).
- **Pr1 is false for sample bias (§2.1.1).** Uniform data on {1,2,3,4,5,9,10,11} has its natural max-margin boundary at x = 7. Many clustering algorithms trained on the biased subsample {1,2,3,9,10,11} put it at x = 6. Any advantage of clustering here comes only from the larger samples it usually has.
- **Label bias is traded for representation bias (§2.1.2).** Projecting the Fig. 1 data onto one axis or the other yields "radically different" clusterings. Human bias also re-enters through community model selection against labelled test sets or human judgments (Miner et al. 2023).
- **Pr2 is false (§2.2).** Freedom from sample and label bias neither guarantees truth (a linear model on perfect data cannot find a non-linear truth) nor is necessary for discovery. His historical examples are biased or idealised samples: purified water, Chomsky's core examples, Darwin, Snow.
- **"All things not equal" (§2.3).** Supervised methods narrow the hypothesis class with each label (see the correction on the S(n−1,k) count). Clustering must pass over most of the data first. Clustering tends to need stronger inductive biases to be computationally feasible, and it lacks agreed evaluation metrics, which slows model selection.
- **Q1 is false (§3.1).** Clustering is function estimation (quoting Abou-Moustafa & Schuurmans 2015). Any clustering hypothesis lies in a supervised classifier's hypothesis class. k-means is "supervised nearest neighbor inference over heuristically identified cluster centroids". Autoencoders minimise a supervised reconstruction loss. Given two labelled points from two of three blobs, 1-NN produces the same partition that 2-means converges on. Reweighting (Shimodaira 2000) and relabelling form a continuum, so supervised and unsupervised learning "can, it seems, form a continuum".
- **Q2 is false (§3.2).** The technical literature treats overfitting and capacity control in unsupervised learning just as in supervised learning (Hansen & Larsen 1996, quoted at length). k plays "exactly the same" role in both paradigms in the three-blob example. A purported proof by contradiction follows (see corrections).
- **Conclusion (§4).** Both arguments rest on a characterisation of clustering "inconsistent with the technical literature". Supervised classification "has at least the same epistemic status".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Unsupervised clustering is sensitive to sample bias | strong | worked toy counterexample, §2.1.1 (sufficient to refute a universal claim) |
| C2 | Clustering is highly sensitive to representation bias, which can carry human bias as label bias does | moderate | illustration from Fig. 1 plus informal argument, §2.1.2 |
| C3 | Freedom from sample and label bias neither determines nor is necessary for epistemic value | moderate | informal argument and historical anecdotes, §2.2 |
| C4 | Unsupervised clustering overfits, and parametric simplicity does the same capacity-control job in both paradigms | strong | agrees with the standard technical literature (Hansen & Larsen 1996, quoted), §1.3, §3.2. This is the paper's firmest point against Rochefort-Maranda & Liu |
| C5 | Clustering is function estimation, and every clustering hypothesis is in a supervised classifier's hypothesis class | strong (as stated) | near-definitional. Clusterings are functions D → {C1…Ck}, §3.1 |
| C6 | Therefore supervised classification is epistemically "at least as" justified as clustering | weak | inference from C5 plus examples. Containment in the hypothesis class does not show that supervised learning reaches the partition without labels encoding it. §4 concedes the reduction is easy "in the cases discussed in the philosophical literature" |
| C7 | Supervised classification is computationally more efficient: each label shrinks the hypothesis class "exponentially", and matching one SVM takes 2^n clustering runs | weak | informal argument with a counting step that appears miscounted and an underived 2^n figure, §2.3 |
| C8 | Parametric simplicity cannot play a different role in clustering, by proof by contradiction from reducibility | weak | invalid as stated: relies on an unstated premise equivalent to the conclusion, §3.2 |
| C9 | The No-Bias Argument is endorsed by Watson (2023a) and Nelson (2020) | moderate | quotations, §1.2. The paper itself notes Watson warns against treating clustering as objective, so the attribution is partial |

## Method

The paper is conceptual analysis. It reconstructs each argument as explicit premises (Pr1, Pr2 → conclusion; Q1, Q2 → conclusion). Each premise is then attacked with toy counterexamples, quotations from the technical ML literature, and informal counting arguments over the hypothesis space of partitions. It contains no experiments.

## Concepts

- **epistemic status** — how justified we would be in accepting conclusions derived from applying a clustering or classification model to data.
- **sample bias** — divergence between the sample used for induction and the population.
- **label bias** — systematic labelling errors in the training sample.
- **inductive bias** — an algorithm's inability to express or induce every hypothesis in the hypothesis class. Note that this is narrower than the field's usual sense of a preference over hypotheses.
- **representation bias** — the effect of how inputs are represented or vectorised on the induced structure.
- **No-Bias Argument** — that clustering is less biased by scientists' preconceptions and so epistemically superior.
- **Simplicity-Truth Argument** — that parametric simplicity is linked to truth in clustering but only to predictive accuracy in supervised learning.

## Connections

The paper is a reply to Rochefort-Maranda & Liu (2020, *Erkenntnis*) and, more cautiously, to Watson (2023a), held here as [LIT-187](../literature.d/LIT-187.md). It reads Watson as leaning on the No-Bias Argument while acknowledging that Watson disclaims objectivity. Footnote 1 places the paper in the Watson–Sterkenburg exchange (Sterkenburg 2023; Watson 2023b; Mollema 2024) and says the two families "do not differ in principle in vacuity". It stays agnostic on natural kinds. This complements [LIT-187](../literature.d/LIT-187.md)'s own conclusion, which is that unsupervised outputs are neither objective nor vacuous and should be validated by error-statistical means. Søgaard's §3.2 point that clustering overfits is consistent with Watson's recommendation of held-out-data validation for clusters. The two disagree less than Søgaard's framing suggests.

## Bearing on the record

**Epistemology.** The paper is explicitly about *justification*: "how justified we would be in accepting conclusions" from a method. It takes a comparative, method-level reliabilist position. The justification of a method's outputs depends on sample size, sample bias, label bias, inductive bias and representation, and whether the method is supervised is not itself a source of warrant. It stays neutral between realist and pragmatist construals of which partitions are "truer". The `epistemology` tag is justified. `philosophy-of-science` should stay primary, because the question is the epistemic standing of a scientific method.

**ML practice.** The paper carries no instruction for ML practice. Its technical content, that clustering overfits, that k acts as a capacity control, and that representation choice dominates clustering outcomes, is textbook material and would be no new `source:` for an Anthology practice. Its one practice-adjacent moral, that unsupervised structure discovery is not less theory-laden than supervised learning because representation choice carries bias, bears on any Anthology text treating clustering or representation learning as neutral discovery. I found no such Anthology practice or theory document to annotate.

## Limitations

- The positive thesis (C6) outruns the argument. The reduction shows only that supervised learners *can represent* any clustering, not that they *arrive at* it from comparable evidence. Given the labels that would make the supervised learner reproduce a clustering, the epistemic question has been moved into how those labels were obtained.
- The paper has no empirical comparison. Every case is a low-dimensional toy.
- The technical slips listed in `corrections` (the Stirling sequence, the constrained-partition count, the EM step labels, the "only unsupervised" typo, the underived 2^n) do not overturn the negative arguments, but they weaken the formal-sounding parts of §2.3 and §3.2.
- The §3.2 "proof by contradiction" is not a proof.
- Treatment of self-supervised learning is only illustrative, and deep clustering and modern representation learning are not addressed.
- The attribution of the No-Bias Argument to Watson is weaker than the §1.2 framing, as the paper itself partly acknowledges.

## Open questions

- Is there a precise sense in which supervised learning reaches a clustering's partition from *less* or *equally informative* evidence? That would require a sample-complexity comparison with the label cost counted, which the paper gestures at in §2.3 but does not carry out.
- Does the argument carry to self-supervised pretraining, where the "labels" are derived from the data and representation bias is learned rather than chosen?
- How do Søgaard's and Watson's ([LIT-187](../literature.d/LIT-187.md)) positions compare once both accept error-statistical validation of clusters? Is any disagreement left beyond the attribution of the No-Bias Argument?

## Corrections to the seeded skim

- The skim NOTE's open question says the paper "does not appear to address" self-supervised learning. It does, briefly, three times: §2.1.1 credits large self-supervised models for gains from data scale; §2.1.2 notes that in self-supervised learning "labels can be derived from data properties"; and §3.1 uses self-supervised representation learning ("part of each data point is used as a label for the rest") as evidence that unsupervised methods are "supervised learning algorithms in disguise". It gives no sustained treatment.
- On the NOTE's question whether the §3.1 reduction is general: the only general claim is hypothesis-class containment, "any hypothesis f induced by unsupervised clustering is also in the hypothesis class of supervised classifiers over the same (unlabeled) data" (p. 11). The rest is examples: two-point 1-NN versus 2-means on three blobs; k-means as nearest-neighbour inference over heuristic centroids; supervised clustering (Finley & Joachims 2005; Garg & Kalai 2018). §4 itself concedes it holds "quite easily so in the cases discussed in the philosophical literature". Containment does not show that a supervised learner reaches the same partition *without* labels that encode it, which is what the epistemic comparison needs.
- The skim reports §3.2's "reductio". The "proof by contradiction" (p. 13) is not valid as stated. "(i) clustering reduces to classification" and "(ii) simplicity plays a different role in clustering" contradict each other only on the unstated premise that reducibility entails sameness of the role of simplicity, which is the conclusion at issue.
- Technical slips in the text that the skim did not catch:
  - (a) p. 2 gives "S(n, 5)" as growing "1, 10, 65, 350, 1701, 7770, 34,105", but that sequence is S(n, 4) for n = 4…10. S(n, 5) runs 1, 15, 140, 1050, ….
  - (b) p. 9 says the number of partitions consistent with two points in *different* clusters equals S(n−1, k). By my computation S(n−1, k) counts partitions with the two points in the *same* block, and "different" gives S(n, k) − S(n−1, k); for n = 3, k = 2 that is 2, not 1 (unverified against any erratum).
  - (c) p. 11 labels k-means' assignment step "maximization" and the centroid update "expectation", which is the reverse of the usual EM correspondence. It also describes the update as recomputing "the (nearest neighbor of the) centroid", which is closer to k-medoids.
  - (d) p. 5 says "only unsupervised clustering is prone to overfitting" where the sense requires "supervised".
  - (e) the §2.3 claim that matching one supervised SVM needs "2^n clustering experiments" is asserted without derivation.
- primary topic: philosophy-of-science is right. The `probabilistic-modeling` tag is acceptable (GMM/EM, Naive Bayes, k-means). The epistemology tag is justified (see Bearing on the record).
