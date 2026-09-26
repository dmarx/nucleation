---
number: 172
status: Read
formerly:
- NOTE-tmpu40gm
paper: LIT-187
title: 'Watson — On the philosophy of unsupervised learning'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (the full text of the publisher's open-access PDF (CC BY
    4.0, confirmed on p. 22), fetched from rd.springer.com with a plain curl
    user agent. It is 26 pp. (Philosophy & Technology 36:28) and .txt. I read §§1–6, footnotes 1–9, figure
    captions and declarations. The reference list was checked only for the
    citations used below.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-26'
summary: >-
  Watson argues that clustering, abstraction and generative modelling each
  come with an epistemic thesis (EC, EA, EG — we identify natural kinds,
  essential properties and unrealized possibilities via such algorithms or
  something like them), which he accepts. Each also comes with an
  ontological thesis (OC, OA, OG — these just *are* what the algorithms
  ought to find under ideal conditions), which he rejects because nothing
  guarantees they are effectively computable. He adds a pragmatic,
  context-relative view of natural kinds, and closes with the claim that
  unsupervised outputs are neither "objective" nor vacuous. They should be
  validated by error-statistical means: resampling stability,
  generalization of clusters to held-out data, out-of-sample likelihood,
  and train-on-synthetic scores.
---
<!-- inactive-ok-file: LIT-162 — Deferred: a related work named by a 2026-09-26 close reading on the metaphysics tag; lapses when the cited work is read -->

# NOTE-172: Watson — On the philosophy of unsupervised learning

## Contribution

This is the first attempt to treat unsupervised learning as a philosophically unified subject rather than a leftover category. It pairs three canonical tasks with three classical metaphysical topics: clustering with natural kinds, abstraction with essence, and generative modelling with modality and imagination. It argues that each algorithm family operationalises the *epistemic* question but not the *ontological* one. It also sets out a middle position on objectivity: unsupervised outputs are conditioned on human-chosen data and hyperparameters, but are not vacuous, and error-statistical validation is the proposed remedy.

## Key insight

For each unsupervised task there are two claims. One is that we come to know X through something like the algorithm. The other is that X just is what the algorithm would find under ideal conditions. The first is plausible on functionalist grounds. The second fails because nothing guarantees that every natural kind, essence or possibility is effectively computable. So unsupervised learning turns "ontological speculation" into "methodological hypotheses that can be efficiently computed and severely tested" (p. 22) without settling the ontology.

## Assumptions

- **Setting (p. 3–4).** A data matrix X of n samples and d continuous features, i.i.d. from a distribution P with density p. Mixed covariates and multi-process data are set aside for simplicity.
- **Scope (fn. 1).** Supervised, unsupervised and RL are "not mutually exclusive". Semi- and self-supervised methods and foundation models are excluded.
- **Functionalism about computation and cognition** (fn. 2; pp. 6, 12, 16). Whether clustering, abstraction or generation is implemented in chips or brains "is irrelevant" (multiple realizability: Putnam, Block and Fodor). EG leans on this "more or less by definition".
- **Anti-actualism for EG (p. 16).** The skeptic can resist EG only by denying that there are unrealized possibilities at all.
- **Realist essentialism is granted as a distinction (pp. 11–12).** Kripke, Ellis and Williamson are cited for the essential/contingent distinction, which Watson then interprets pragmatically.
- **The manifold hypothesis** is an empirical premise for abstraction, said to hold "in many important areas" but not universally (pp. 11–12).

## Key results

- **Clustering (§2).** k-means (an NP-hard objective with Lloyd-style local optima) and hierarchical clustering (a dissimilarity matrix giving a nested solution path over k; it imposes a recursive-partition consistency that k-means "generally violates", p. 6). **EC** (we learn to identify natural kinds via clustering or something like it) is accepted. **OC** (natural kinds are what clustering ought to find under ideal conditions) is rejected: identifiability via clustering is not necessary for kindhood (p. 7). On sufficiency, a "broadly pragmatic view": kinds are grouped for a context and purpose, constrained by inductive usefulness and participation in laws. Natural kinds and clustering algorithms "may even be co-constitutive … a sort of Kantian metaphysics" (p. 8). A speculative closing claim is that clustering is "literally hardwired" if Chomsky's subject–predicate universal grammar holds (p. 8).
- **Abstraction (§3).** The term covers coarsening (superpixels; causal feature learning, including Kinney and Watson 2020), autoencoders and embeddings (a linear autoencoder ≈ PCA), and disentanglement (β-VAE, causal representation learning). The information-theoretic example compresses a noiseless 20×20 checkerboard (400 bits) to about 16 bits, and the compression becomes lossy with noise (p. 9). The manifold hypothesis is offered as the explanation of autoencoder effectiveness, with Plato's cave as its philosophical analogue (p. 11). **EA** (we learn to identify essential properties via abstraction) is accepted. **OA** is rejected for the same computability reason: "Abstraction algorithms may be sufficient to identify some essential properties, but essential properties are not necessarily identifiable via abstraction algorithms" (p. 12).
- **Generative models (§4).** GANs (a minimax game; "at [Nash equilibrium] we say that f has learned the true data distribution", p. 14) are compared with forest-based generators (leaf-wise density sampling). Generation must "capture the light and sample the shadows" (essence plus contingency), which is dual to necessity/possibility in modal logic (p. 16). Williamson's "knowing by imagining" is invoked. **EG** (we identify unrealized possibilities via generative models, or something like them) is accepted. **OG** is rejected: it needs all possibilities to be effectively computable, and restricting possibility to the computable is "ad hoc and circular" and hits quantum-simulation limits (pp. 16–17).
- **Discussion (§5).** (a) *Objectivity is conditional.* An unsupervised separation of treated from untreated gene-expression samples is "arguably better evidence" of a treatment effect than a supervised one, since the stratification hypothesis is not built in. But hyperparameters (k, cut height, distance, architecture), data provenance (Leonelli's "data journeys") and opacity condition every result (pp. 17–18). Clustering never tests k = 1, so it can produce false positives unless it is corrected, for example with the gap statistic. (b) *Not vacuous.* He gives three replies: scale and speed; "anything goes" is false in practice, since practitioners use a few simple distances; and pipelines corroborate clusters, for example cancer subtypes with log-rank survival tests (pp. 18–19). (c) *Ethics.* About 80% of GWAS subjects are of white European ancestry, against 16% of world population (Martin et al. 2019). Deepfakes could erode evidential trust. Synthetic data could replace restricted access (the Chetty et al. 2014 IRS example), but it is not immune to membership inference (Stadler et al. 2022) (pp. 19–20). (d) *Remedy.* Mayo's severity, made concrete by the tools listed in the corrections, plus XAI and sanctions or content moderation for misuse (pp. 20–21).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Unsupervised learning is philosophically neglected relative to supervised learning and RL | moderate | a literature sampling (§1), self-described as "imperfect and incomplete" |
| C2 | EC, EA and EG: we identify natural kinds, essences and unrealized possibilities via these algorithms "or something very much like them" | weak–moderate | informal argument resting on functionalism; the "something very much like them" clause makes the theses hard to falsify |
| C3 | OC, OA and OG fail because not all kinds, essences or possibilities need be effectively computable | informal argument | a possibility argument (pp. 7, 12, 16–17); no example of an uncomputable natural kind or essence is given |
| C4 | Natural kinds are context- and purpose-relative, and possibly co-constituted with clustering algorithms | assertion | explicitly "I will go to no great lengths defending this" (p. 8) |
| C5 | Unsupervised learning is "ontologically fundamental" and "perhaps the most fundamental branch of all AI" | weak | the only argument is that supervised learning and RL presume an a priori split into inputs and errors or rewards (p. 3); the abstract states more than the body shows |
| C6 | The manifold hypothesis explains autoencoder effectiveness | weak (as stated) | a single citation (Fefferman et al. 2016) plus a transcriptomics anecdote; offered as "may go some way" |
| C7 | Unsupervised separation is better evidence of a treatment effect than supervised separation | informal argument | the gene-expression example (p. 17); hedged "arguably" |
| C8 | Unsupervised results are neither objective nor vacuous | moderate | a structured argument in §5 with three replies to the vacuity objection |
| C9 | Error-statistical tools can validate unsupervised outputs | moderate (as a pointer) | cites existing methods (Monti 2003; Tibshirani 2001; Tibshirani and Walther 2005; Ravuri and Vinyals 2019); no new method and no worked severity analysis |
| C10 | 80% of GWAS subjects are white European, against 16% of the global population | cited empirical | Martin et al. 2019 |
| C11 | Clustering capacity may be hardwired, via Chomskyan universal grammar | assertion | conditional on an unargued premise (p. 8) |

## Concepts

- **Unsupervised learning.** Finding "structure" in data without labels or rewards. What counts as structure is resolved per algorithm (p. 3, after Hastie et al. 2009).
- **Abstraction algorithm.** Watson's umbrella term for methods that learn simplified representations: coarsening, projection, embedding and autoencoding. The result is usually dimension-reducing, though fn. 5 notes this is not strictly necessary.
- **E-thesis / O-thesis.** The epistemic claim (we identify X via algorithm A) versus the ontological claim (X is what A ought to find under ideal conditions), for X ∈ {natural kinds, essential properties, unrealized possibilities}.
- **Methodological reduction.** On the model of Turing (1950), replacing a metaphysical question with a procedural one (p. 7).
- **Top-down vs bottom-up imagination.** GANs generate from an abstraction; forests generate from local particulars (p. 15).

## Connections

**Metaphysical theses.** Watson *defends* a pragmatic, quasi-Kantian relativity of natural kinds (and, by extension, essences) to context and purpose, and denies both constructivism ("natural kinds, if they exist at all, surely predate any actual clustering method", p. 7) and full realism. He *presupposes* functionalism about cognition and computation, the reality of unrealized possibilities (anti-actualism), and the meaningfulness of the essential/contingent distinction. He argues that computability cannot be a condition on being a kind, an essence or a possibility.

**`metaphysics` tag: justified**, and it should lead. Natural kinds, essence and modality are the paper's announced subject.

It builds on Floridi's method of levels of abstraction (2008), which is not [LIT-152](../literature.d/LIT-152.md) (Floridi's defence of informational structural realism, also 2008). The two are related, since that defence uses the method of levels of abstraction. It also builds on Buckner's (2018) transformational abstraction in CNNs, Mayo's severity, and Williamson's "knowing by imagining". [LIT-162](../literature.d/LIT-162.md) (Søgaard, "Is Unsupervised Clustering Somehow Truer?") replies to the "No-Bias" line of argument and denies that clustering is epistemically privileged over supervised classification. Watson's C7 (unsupervised separation as "arguably better evidence") is exactly the kind of claim Søgaard contests, though Watson hedges it and himself rejects "objectivity" (§5). [LIT-004](../literature.d/LIT-004.md) (community detection with Ricci flow) is a network-clustering method of the kind Watson's §2 and §5 would govern. In the anthology, Watson's GAN illustration is StyleGAN ([ANTH-LIT-561](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-561.md)) and his analogy example is Mikolov et al.'s word2vec paper ([ANTH-LIT-604](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-604.md)).

## Bearing on the record

It holds no ML practice of its own. The practical content in §5 is pointers to existing validation methods: consensus/resampling clustering (Monti et al. 2003), the gap statistic, prediction-strength-style generalization tests, held-out likelihood, and the Classification Accuracy Score for generative models (Ravuri and Vinyals 2019). If the Anthology of the SOTA wants a practice on validating clusterings or generative models, those primary sources are what it should file, not this paper. A grep of the anthology's literature.d found none of Monti, Tibshirani's gap statistic or Ravuri and Vinyals. I would not flag this paper as `anthology-candidate`.

For this record, it is the natural anchor for any THEORY about whether representation learning discovers or constructs kinds. It pairs with [LIT-162](../literature.d/LIT-162.md) as a claim and its rebuttal.

## Limitations

- The O-theses are rejected by a bare possibility argument: some kind, essence or possibility *might* be uncomputable. No example is offered, and the sufficiency direction is left to a sketch.
- The E-theses are hedged ("or something very much like them") so heavily that it is unclear what would falsify them.
- The "most fundamental branch of AI" claim is supported by one sentence (p. 3). It also sits oddly with the exclusion of self-supervised learning (fn. 1), which is where modern unsupervised learning mostly lives.
- The technical exposition is idealised in places: "f has learned the true data distribution" at GAN equilibrium; word2vec described as an autoencoder; the manifold hypothesis offered as an explanation on thin support.
- The ethics section is a survey of known issues (bias in GWAS, deepfakes, synthetic-data privacy) rather than an argument specific to unsupervised learning.

## Open questions

- Is there a concrete natural kind or essence that is provably not identifiable by any clustering or abstraction procedure? That would turn C3 from a possibility into a result.
- What would a severity analysis of a clustering actually look like? What test of a cluster hypothesis has a high probability of detecting its falsity, beyond stability, which can hold for spurious structure?
- Does the E/O analysis extend to self-supervised pretraining, which the paper excludes, and does it change when representations are learned at foundation-model scale?
- How do Watson's hedged defence of unsupervised evidence (C7) and Søgaard's denial of any epistemic privilege ([LIT-162](../literature.d/LIT-162.md)) come out on a shared case?

## Corrections to the seeded skim

- Dossier: "§2 runs a cats-and-dogs example against Kleinberg's impossibility theorem." It does not. Kleinberg (2002) appears only in a list of impossibility results in §2's opening paragraph (p. 4). The cats-and-dogs example illustrates k-means and hierarchical clustering (k = 2 for species, k = 4 for breeds) and is never set against any impossibility theorem.
- Dossier: "OC is rejected as smuggling in normative baggage, because not all kinds need be computable." Watson makes the normative-baggage point (the "ought" and underspecified "ideal conditions", p. 7) only to say OC needs elaboration. His *reason for rejecting* OC is the computability argument: there is "no a priori reason to believe that all natural kinds are effectively computable". From this he concludes that identifiability via clustering is "not a necessary condition for natural kindhood" (p. 7). Whether it is *sufficient* is left open and gets only a pragmatic sketch (pp. 7–8).
- The dossier misses the paper's organising structure. The same epistemic/ontological pair recurs in all three sections: EC/OC (kinds, §2), EA/OA (essential properties, §3) and EG/OG (unrealized possibilities, §4). In each, the E-thesis is accepted and the O-thesis rejected, on the same computability ground.
- Dossier on §4: "GANs and related models". The two model classes are GANs and **tree/forest-based generative models** (Criminisi 2012; Correia 2020; Watson et al. 2023), contrasted as top-down vs bottom-up imagination (Seurat vs Chuck Close, pp. 14–15). Watson is himself an author of one of the forest methods.
- The dossier's check "whether the error-statistical recommendation (Mayo) is made operational": it is partly operational (pp. 20–21). It names bootstrapping and subsampling for cluster stability (Monti et al. 2003; Fisher et al. 2016); generalization of clusters to unseen data via classifiers (Dudoit and Fridlyand 2002; Tibshirani and Walther 2005); the gap statistic against k = 1 (Tibshirani et al. 2001); out-of-sample log-likelihood for explicit-density models; the train-on-synthetic score for GANs (Ravuri and Vinyals 2019); and XAI feature attributions for clustering and embeddings. No severity is actually computed for any example.
- Scope: footnote 1 excludes self-supervised learning and foundation models ("beyond the scope of this article"), so the paper's "unsupervised learning" is classical clustering, embeddings/autoencoders and GANs/forests, not modern pretraining.
- Minor technical slip: word2vec analogies (Mikolov et al. 2013) are described as "learned by the autoencoder" (p. 11). Word2vec is a predictive skip-gram/CBOW model, not an autoencoder.
- Missing topic: `epistemology`. Each E-thesis and the whole of §5 (objectivity, vacuity, severity, trust) are claims about knowledge and evidence, and someone browsing epistemology would expect this paper. Add it.
- primary topic: metaphysics. The paper frames each algorithm as forming "a metaphysical hypothesis about its training data" (p. 3), and its conclusion names "distinctive metaphysical questions pertaining to natural kinds, modal ascriptions, and the limits of imagination" (p. 22). `philosophy-of-science` is a close second (natural kinds, evidence) and should stay as a tag. `probabilistic-modeling` is justified for k-means, hierarchical clustering, PCA and forests, but not as the lead.
