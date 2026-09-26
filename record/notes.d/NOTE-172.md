---
number: 172
status: Skimmed
formerly:
- NOTE-tmpu40gm
paper: LIT-187
title: 'Watson — On the philosophy of unsupervised learning'
version: 1
date: '2026-09-26'
summary: >-
  Clustering, abstraction and generative modelling give data-driven, testable operationalizations of old metaphysical questions (natural kinds, essence vs contingency, modality), but their outputs are not "objective" — they are conditioned on human-chosen data and hyperparameters, so they call for a pragmatic, error-statistical stance.
---
<!-- inactive-ok-file: LIT-162 — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->

<!-- inactive-ok-file: LIT-187 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-172: Watson — On the philosophy of unsupervised learning

## Contribution

Watson notes that unsupervised learning is everywhere in science and industry yet has had far less philosophical attention than supervised or reinforcement learning. He analyses three canonical problems: clustering, abstraction and generative modelling. He argues they raise distinctive epistemological and ontological questions, since they provide data-driven tools for discovering natural kinds and for separating essence from contingency. He claims unsupervised learning may be the most fundamental branch of AI. He also warns that uncritical reliance on it carries epistemic and ethical risks, and recommends a pragmatic, error-statistical approach.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2 (Clustering) runs a cats-and-dogs example against Kleinberg's impossibility theorem. It weighs an epistemic thesis (EC: we learn to identify natural kinds via clustering or something like it) against an ontological one (OC: natural kinds are what clustering ought to find under ideal conditions). OC is rejected as smuggling in normative baggage, because not all kinds need be computable. Watson ends on a pragmatic view of natural kinds tied to inductive usefulness.
- §3 (Abstraction) groups embedding, autoencoding, projection and coarsening under "abstraction". It connects them to Floridi's levels of abstraction and to Buckner's reading of CNNs as Lockean/Humean transformational abstraction.
- §4 (Generative Models) covers GANs and related models as tools for sampling contingencies, bringing in modality and the limits of imagination. Deepfakes and adversarial examples are deferred to §5.
- §5 (Discussion) rejects the idea that unsupervised results are bias-free. An unsupervised separation of treated and untreated samples is somewhat better evidence than a supervised one, but data, hyperparameters and interpretation are all human-chosen, and opacity creates problems of trust.
- §6 (Conclusion): unsupervised learning turns ontological speculation into "methodological hypotheses that can be efficiently computed and severely tested". It should face the scrutiny usually reserved for supervised models, backed by statistical rigour and transparency.

## Open questions

- Directly relevant to how the anthology frames representation learning and clustering as discovery tools. It pairs naturally with [LIT-162](../literature.d/LIT-162.md) (Søgaard), which disputes the claim that unsupervised clustering is epistemically privileged.
- Check the hyperparameter and cluster-validation argument in §5 against current practice (stability resampling, model selection for k).
- Check whether the error-statistical recommendation (Mayo) is made operational or stays programmatic.
