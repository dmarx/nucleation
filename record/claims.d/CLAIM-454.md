---
number: 454
status: Proposed
formerly:
- CLAIM-tmpwr001
title: 'A latent feature or mode recovered from an organization''s members'' activity is at most a constituent of an organizational perspective, not the perspective: a feature allocation says which members take part in which modes, and whether those modes are organized into one perspective depends on the relations of access, uptake and authority among their carriers, which the same allocation leaves open'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed from the exchange "Experimental Infrastructure Review", where
    it appears five times in the Northstar turns (T18, T20, T21, T22,
    T23) and a sixth in the transformer setting (T24 §4). The parts are
    held; the statement for a latent-feature model of members is new.
    Extended before merge, on 2026-10-27, with supporting cases from the
    circuits works read on 2026-10-26 (no version bump, the entry being
    new).
role: thesis
warrant: interpretive
defeated_if: >-
  An argument that, under TERM-072's organizational sense, a perspective
  is fixed by which members share which interpretive capacities, so that
  two organizations with the same member–feature allocation and the same
  activations must realize the same perspectives whatever their access,
  communication and authorization relations. Or a study in which features
  recovered without relational data predict the effects of interventions
  on authorization and communication as well as a model given those
  relations does. A perspective that happens to coincide with one
  feature's carriers does not defeat it.
tags:
- individuation
- probabilistic-modeling
- social-ontology
date: '2026-10-26'
line:
- distributed-agency
rests_on:
- CLAIM-135
- CLAIM-414
grounds:
- CASE-101
- CASE-165
uses:
- TERM-072
- TERM-074
complements:
- CLAIM-027
summary: >-
  From the Northstar turns of the exchange "Experimental Infrastructure
  Review", where the owner proposed inferring an organization's
  perspectives with hLDA (T21) and the Indian buffet process (T22). Every
  reply made the same reservation, and T22 put it most plainly: "None of
  those ingredients alone is the perspective. The organized relationship
  among them is." It is the criterion [QUESTION-276](../questions.d/QUESTION-276.md)'s answer has to
  meet. It does not say features are useless, or that no perspective is
  ever one feature's carriers. It says the allocation underdetermines the
  perspective.
---
<!-- inactive-ok-file: CLAIM-135 TERM-072 TERM-074 CLAIM-027 CLAIM-418 CLAIM-427 CLAIM-367 — Proposed; the claims and terms this one rests on or uses, held open, and it is Proposed with them -->
<!-- inactive-ok-file: CASE-165 CASE-166 — Proposed; the cases filed with this claim from the same exchange -->
<!-- inactive-ok-file: THEORY-1011 THEORY-1014 — Proposed; circuits readings cited as hypotheses, not leaned on -->

# CLAIM-454: A latent feature or mode recovered from an organization's members' activity is at most a constituent of an organizational perspective, not the perspective: a feature allocation says which members take part in which modes, and whether those modes are organized into one perspective depends on the relations of access, uptake and authority among their carriers, which the same allocation leaves open

## The claim

A feature allocation (an Indian buffet or beta-process prior over who
holds what, or a topic hierarchy over what members say) records
participation. Whether participants are organized into a perspective
depends on what [TERM-072](../terms.d/TERM-072.md)'s organizational sense requires and the
allocation does not hold: who can reach whose signals, whose contributions
are taken up, and who can authorize what. Two organizations can share the
allocation and differ in all of these. That is [TERM-074](../terms.d/TERM-074.md)'s sense 1 ("Two
engineering departments with the same specialists and information can
differ in whether a safety engineer can stop a deployment"), and [CLAIM-414](CLAIM-414.md)
demonstrates it: matched ordinary trajectories can conceal differences in
an interpretation's efficacy. [CLAIM-135](CLAIM-135.md) gives the general form: recovering
latent structure is reconstruction, identification and constitution, and
identifiability reaches the second at most. [CASE-101](../cases.d/CASE-101.md) adds the rival source
of coactivity. Members who respond alike to a common input share a
feature and form no perspective at all.

## Where it appears

Five times in the Northstar turns, each reply making it unprompted:

- T18 §5: "a dynamical mode is not automatically a perspective. A
  high-variance activity pattern might merely reflect a shared reporting
  schedule."
- T20, on the lab's analyzer: "candidate organizational modes, not
  evidence that three real organizational perspectives emerged"
  ([CASE-166](../cases.d/CASE-166.md)).
- T21: use hLDA "as the starting point … not identify its topics directly
  with perspectives"; "A perspective would be a candidate joint
  organization of content and consequential interaction, rather than
  simply a topic."
- T22: "it cannot infer the existence of a genuine organizational
  perspective merely by assigning a name to one column of a binary
  matrix"; "Two companies can have identical employee–feature matrices but
  different organizational behavior because their communication and
  authorization relationships differ"; "the organizational perspective
  might not be one of the latent features. It might be a persistent,
  coordinated configuration of several features, distributed across
  multiple employees and teams … None of those ingredients alone is the
  perspective. The organized relationship among them is."
- T23: "The IBP prior supplies multiplicity; the relational dynamics will
  have to supply organization"; the model "does not contain a primitive
  random variable whose value is the organization's current perspective"
  ([CASE-165](../cases.d/CASE-165.md), which is built on this division).

And a sixth time in another setting. At T24 the owner asked whether the
same setup could interpret transformer training ([QUESTION-275](../questions.d/QUESTION-275.md)), and
the reply's §4 is headed "The latent features still aren't the
perspectives": a computational regime "may depend on an organized
relationship among these features. It might not be identical to any one
of them", and it should be "an inferred structure, not a primitive in the
transformer or the initial probabilistic model". In a network, the
relations the allocation leaves open are routing and the contexts in
which features are consequential, and [CLAIM-367](CLAIM-367.md) has already said that
most of the governance of training lies outside the network.

## Outside the exchange

The works the exchange cited, read on 2026-10-26, hold the move this
claim denies and cases of its point. They are supporting cases, not a
test: the claim is interpretive.

- **The move, published.** The author–topic paper reads its Enron topics
  as showing "how the author-topic model can learn about the roles and
  interests of different individuals from text that they have written",
  by inspection and with no check against the individuals' roles
  ([NOTE-1180](../notes.d/NOTE-1180.md)). Its institutional accounts, such as Enron General
  Announcements, come out nearly single-topic: one source sending alike
  messages, which is [CASE-101](../cases.d/CASE-101.md)'s coactivity rather than a perspective.
- **A layer above the features is still co-occurrence.** Correlated
  latent-feature models put categories over the features
  ([THEORY-1012](../theory.d/THEORY-1012.md)). A category is a pattern of which features occur
  together, so it is another constituent, not the organization of them.
- **A circuit is not its canonical units.** In Musat, Pimentel, Zucchet
  and Hofmann's trained two-hop models, the four canonical units alone
  score 0.594 and with three "aiding" units 0.922 ([NOTE-1177](../notes.d/NOTE-1177.md)): what
  the circuit does depends on how further units are composed with them.
- **A feature that tracks a variable need not carry it.** In the
  interpretability benchmark T24 cites, sparse-autoencoder features never
  localized a causal variable better than the model's own neurons, and an
  apparent carry-the-one signal was the correlated output digit, failing
  totally under random counterfactuals ([THEORY-968](../theory.d/THEORY-968.md), [NOTE-1169](../notes.d/NOTE-1169.md)).
- **Features scored one at a time.** The cross-checkpoint crosscoder study
  scores features singly, and its authors leave extending the analysis
  "from individual features to circuits" to future work ([NOTE-1186](../notes.d/NOTE-1186.md)),
  which is where this claim puts the perspective.

The core circuits works, read on 2026-10-26 at the owner's request, add
cases in networks of the same kind, again supporting cases and not a
test.

- **A component's role depends on its circuit.** In IOI, induction heads
  do something other than what defines them: their output serves as a
  pointer to a position, read by the S-inhibition heads ([NOTE-1167](../notes.d/NOTE-1167.md)).
- **Locating is not identifying.** ROME's causal traces and edits find
  where restoring or writing a hidden state helps ([THEORY-998](../theory.d/THEORY-998.md)), not
  the variable that does the work; that the edit's site stores the fact
  is held only as a Proposed hypothesis ([THEORY-1011](../theory.d/THEORY-1011.md)).
- **Activity does not give role.** In Claude 3 Sonnet, a feature's
  activation predicts its ablation effect at a correlation of about 0.12,
  attribution at about 0.81 ([THEORY-987](../theory.d/THEORY-987.md)). Steering usually needs a
  feature clamped far outside its observed range, which the authors
  explain by its being "co-active with several correlated features with
  related meanings" ([NOTE-1178](../notes.d/NOTE-1178.md)).
- **Features alone carry little; the arrangement carries the behaviour.**
  Circuits of sparse-autoencoder features recover little of subject–verb
  agreement without the error terms ([THEORY-1007](../theory.d/THEORY-1007.md)), and agreement is
  carried by several converging pathways ([THEORY-1014](../theory.d/THEORY-1014.md)), the claim's
  "organized relationship" in a transformer. Towards Monosemanticity
  tests activation structure and downstream role separately, and its
  shuffled-weights control shows an autoencoder finding features, mostly
  single-token ones, in a model that has learned nothing ([NOTE-1191](../notes.d/NOTE-1191.md)).
- **Instruments that cannot tell correlated variables apart.** Causal
  scrubbing scores a hypothesis only through the partition of the data it
  induces, so an A-detector and a B-detector perfectly correlated on the
  data tie ([THEORY-978](../theory.d/THEORY-978.md)). DAS's "entailment" variable in BERT on MoNLI
  decomposes into the two input words' identities ([THEORY-983](../theory.d/THEORY-983.md)).
- **A replacement exact at a point diverges under perturbation.** The
  cross-layer-transcoder replacement is exact on its prompt by
  construction ([THEORY-979](../theory.d/THEORY-979.md)), yet its responses to perturbation agree
  with the model one layer later and then diverge ([THEORY-994](../theory.d/THEORY-994.md)). A
  recovered feature is not yet the variable that does the work; the
  transcoder paper's "caught" case is one instance ([NOTE-1174](../notes.d/NOTE-1174.md)).

## What it does not say

- Not that a recovered feature is useless. It may well be a constituent,
  and recovering constituents is [CLAIM-135](CLAIM-135.md)'s first two achievements.
- Not that no perspective is ever exactly one feature's carriers. It says
  the allocation cannot show that one is.
- Not that an organizational perspective exists in any firm or network.
  That is [CLAIM-418](CLAIM-418.md)'s and [CLAIM-427](CLAIM-427.md)'s ground, and it is untouched here.
- Not that relations suffice. Relations among carriers with no shared
  feature organize nothing interpretive. The claim is about what the
  allocation lacks, not about what would be enough.
