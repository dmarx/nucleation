---
number: 275
status: Open
formerly:
- QUESTION-tmpivbso
title: 'Can the development of a transformer''s circuits in training be described as organizational regimes forming over shared, overlapping latent features, so that a model coupling feature allocation to circuit interaction, fitted to early checkpoints, predicts the effects of held-out training interventions that feature-only and circuit-only descriptions fitted to the same checkpoints miss?'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed from T24 of the exchange "Experimental Infrastructure Review",
    the owner's question, with the reply's research question as its test.
    The page did not render the reply ("Message delivery timed out"); the
    owner pasted it. The reply reports no simulation. Extended before
    merge, on 2026-10-27, with what the circuits works read on
    2026-10-26 supply (no version bump, the entry being new).
tags:
- learning-theory
- representation-learning
date: '2026-10-26'
line: learned-structure
refines:
- QUESTION-039
summary: >-
  The owner, at T24: "could we potentially apply this setup as an
  interpretive framework for understanding the learning dynamics of
  transformers?" "This setup" is the dynamic latent-feature model of T23
  ([CASE-165](../cases.d/CASE-165.md)). The reply answered with a test: "Can the emergence,
  specialization, overlap, and persistence of transformer circuits be
  explained by modeling them as developing organizational regimes over
  shared latent features—and does that description predict training
  responses that existing feature- or circuit-based analyses miss?" It is
  the second time the owner has applied the record's frameworks to a
  network in training. The first was [CASE-113](../cases.d/CASE-113.md) and [CLAIM-367](../claims.d/CLAIM-367.md), and [CASE-117](../cases.d/CASE-117.md)
  is the population form. The sharp edge is [CLAIM-427](../claims.d/CLAIM-427.md)'s third grade:
  positive results would have to be prospective, against strong
  conventional baselines at matched complexity. Nothing here says that a
  circuit is a perspective.
---
<!-- inactive-ok-file: CLAIM-367 CLAIM-329 CLAIM-118 CLAIM-427 CLAIM-278 CLAIM-263 CLAIM-286 CLAIM-287 THEORY-783 THEORY-039 THEORY-481 TERM-072 — Proposed; the claims and readings the question is framed by or re-derives, cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: CLAIM-454 CASE-165 — Proposed; filed with this question from the same exchange -->
<!-- inactive-ok-file: THEORY-967 THEORY-1004 THEORY-1001 THEORY-997 — Proposed; readings of the same day, cited with their limits -->
<!-- inactive-ok-file: THEORY-1013 THEORY-986 THEORY-1016 THEORY-1014 — Proposed; the circuits readings' wider accounts, cited as the units and targets the question uses, nothing here rests on them -->

# QUESTION-275: Can the development of a transformer's circuits in training be described as organizational regimes forming over shared, overlapping latent features, so that a model coupling feature allocation to circuit interaction, fitted to early checkpoints, predicts the effects of held-out training interventions that feature-only and circuit-only descriptions fitted to the same checkpoints miss?

## Why it is a question

The reply's construction runs over checkpoints θ_0 … θ_S of a small
transformer trained on two or three synthetic task families. It has three
layers.

- **Features.** A binary allocation B_{ck,s} of components c (head
  outputs, MLP channels) to latent features k at checkpoint s, with
  r_{c,s}(x) ≈ Σ_k B_{ck,s} a_{k,s}(x) v_{ck,s} and an Indian buffet prior
  on B: "several components can participate in the same feature, and one
  component can participate in several features". This is [CASE-165](../cases.d/CASE-165.md)'s
  model with components for employees. "This factorization is an
  approximation, not an exact decomposition of transformer computation."
- **Development.** A temporal prior p(B_s | B_{s−1}, θ_s, 𝒟_s) allowing
  features to be born, persist, redistribute and disappear.
- **Regimes.** Above the features, candidate regimes of participating
  features, their routing, and the contexts in which they are
  consequential: "an inferred structure, not a primitive in the
  transformer or the initial probabilistic model". That is
  [CLAIM-454](../claims.d/CLAIM-454.md) in a new setting (its sixth appearance).

Three analyses are to be compared: feature-only, circuit-only, and coupled
feature–circuit dynamics, against "standard sparse dictionaries or
crosscoders, direct circuit localization, and simpler checkpoint-level
state-space models". The reply: "The dynamic IBP must earn its
complexity."

## What the record already holds

Most of the reply's apparatus is on file, and it cited four codes
([CLAIM-367](../claims.d/CLAIM-367.md), [THEORY-169](../theory.d/THEORY-169.md), [CLAIM-329](../claims.d/CLAIM-329.md), [THEORY-253](../theory.d/THEORY-253.md)).

- **Who governs training.** "The transformer itself is not necessarily
  governing this development" is [CLAIM-367](../claims.d/CLAIM-367.md): individuated for training, the
  unit is at least the network–optimizer pair, and its six relations map
  onto the reply's governance table (routing, gradient allocation,
  optimizer, curriculum).
- **Inference is not training.** "That does not mean the network's
  persistent parameters change during an ordinary forward pass" is
  [THEORY-169](../theory.d/THEORY-169.md)'s reading of in-context conditioning. The reply's three
  timescales (training, layer, token) are [CLAIM-118](../claims.d/CLAIM-118.md)'s sources of change.
- **The update rule and its interventions.** (θ_{s+1}, m_{s+1}) =
  𝒰(θ_s, m_s, ℬ_s), and "clone the full training state, modify a particular
  training exposure or update pathway", are [CASE-113](../cases.d/CASE-113.md)'s update and crossed
  interventions. What the reply adds is a third arm, training exposure
  (task mix and curriculum), beside [CASE-113](../cases.d/CASE-113.md)'s optimizer and learned
  state.
- **The optimizer arm.** [THEORY-253](../theory.d/THEORY-253.md): in the Geometry model, gradient
  descent learns independent skills together and sign descent in
  sequence. That is a simulation in a solvable model. That Adam-like
  optimizers cause sequential onset in trained networks is the Proposed
  [THEORY-783](../theory.d/THEORY-783.md), and its test is the open [QUESTION-193](QUESTION-193.md). The reply cites
  [THEORY-253](../theory.d/THEORY-253.md) for transformers without that scope.
- **Task interaction.** The reply's g_kᵀg_j "under ordinary Euclidean
  gradient descent" is [CLAIM-366](../claims.d/CLAIM-366.md)'s object: its sign is not invariant under
  reparameterization, and a negative product does not exclude common
  descent. The reply's two caveats, Euclidean geometry and Adam, are one
  fact ([CLAIM-366](../claims.d/CLAIM-366.md)'s note of 2026-10-26).
- **Continuity.** The reply's "representational" and "computational"
  continuity are [TERM-071](../terms.d/TERM-071.md)'s state and dynamical senses. It cited [CLAIM-329](../claims.d/CLAIM-329.md)
  for "distinct forms of organizational persistence", which is [TERM-071](../terms.d/TERM-071.md)'s
  job. [CLAIM-329](../claims.d/CLAIM-329.md) is the thesis that persistence through turnover is by
  causal transmission, not resemblance, and the reply's §6 asks its
  question without it: "Can we distinguish a continuing computation from a
  newly learned replacement with similar output behavior?"
  ([CLAIM-329](../claims.d/CLAIM-329.md)'s note of 2026-10-26).
- **Influence on inference against influence on learning.** "A component
  might have a large effect on current predictions but receive little
  additional training signal" is [QUESTION-134](QUESTION-134.md)'s split of influence,
  competence and access, and [CASE-117](../cases.d/CASE-117.md)'s coupled and decoupled training
  exposure ([QUESTION-134](QUESTION-134.md)'s note of 2026-10-26). The rigidity and recovery
  material is [CLAIM-286](../claims.d/CLAIM-286.md), and the dormant-alternative caveat is [CLAIM-287](../claims.d/CLAIM-287.md)'s
  reinstatable capacity.
- **Acquisition.** "Does a circuit emerge by acquiring new features,
  reorganizing existing features, or both?" is [QUESTION-039](QUESTION-039.md)'s second half,
  whether acquisition is one kind of event or several. [THEORY-039](../theory.d/THEORY-039.md), [THEORY-481](../theory.d/THEORY-481.md)
  and [THEORY-229](../theory.d/THEORY-229.md) answer parts of it, and so now does [THEORY-973](../theory.d/THEORY-973.md): in small
  attention-only transformers, in-context learning arrives in the window
  where induction heads form, and removing the need for two heads to
  compose moves it.

What is new is the coupling: an organizational reading of circuits over a
developing feature allocation, with a stated way to lose.

## The works the reply drew on, read

The six works T24 cites by paraphrase were read on 2026-10-26. They
supply the comparators and show what is still missing.

- **A circuit-only baseline.** The induction-heads paper's per-snapshot
  head scores and ablation attributions ([NOTE-1173](../notes.d/NOTE-1173.md)), and the refined
  local learning coefficient of each head over training, whose curves
  diverge and cluster by the heads' functional types ([THEORY-975](../theory.d/THEORY-975.md)).
- **A feature-only baseline.** Cross-checkpoint crosscoders, which score
  each feature's causal use on a task at every checkpoint ([NOTE-1186](../notes.d/NOTE-1186.md),
  [THEORY-1004](../theory.d/THEORY-1004.md)).
- **Reorganization, observed.** In the refined-LLC study's model the
  previous-token heads, which precede the induction heads, start as
  n-gram heads, and n-grams pass from one head to another
  ([THEORY-967](../theory.d/THEORY-967.md)). That is the question's "reorganizing existing
  features", and a feature moving between carriers, seen at the level of
  components in two checkpoints of one run.
- **An exact version of the three layers.** In Musat, Pimentel, Zucchet
  and Hofmann's attention-only transformers on block-list inductive tasks,
  the data's symmetries fix a subspace of weights that gradient descent
  never leaves, spanned by elementary token and position actions
  ([THEORY-981](../theory.d/THEORY-981.md)). The components' features are given by symmetry
  rather than inferred under a buffet prior; circuits are sets of shared
  coordinates, so their overlap is exact; and development is the reduced
  dynamics on those coordinates, in which circuits that solve overlapping
  data interact although their coordinates are orthogonal
  ([THEORY-1009](../theory.d/THEORY-1009.md)), and initialization picks among competing circuits
  ([THEORY-1001](../theory.d/THEORY-1001.md)). Inside its idealization, both conditions below are
  met: the state is the coordinates themselves, and the commutant and the
  paper's Assumption 5 remove the basis and split symmetries.
- **Localization scored on its own hypothesis.** In the interpretability
  benchmark T24 cites, sparse-autoencoder features never beat the model's
  own neurons at localizing causal variables, and the best method,
  distributed alignment search, is trained against the causal model it is
  scored on ([THEORY-968](../theory.d/THEORY-968.md)).
- **Relations against components.** The fine-tuning study's finding, that
  circuits keep their nodes and change their edges ([THEORY-997](../theory.d/THEORY-997.md)), is
  what a fixed edge budget alone produces in the record's null
  simulation, so it needs a null at equal edge budget before it bears on
  the coupling.

None of the six fits anything to early checkpoints and predicts later
ones. The prospective arm is still undone in the literature the record
holds.

## The circuits literature, read

The core circuits works, registered and read on 2026-10-26 at the owner's
request, supply the question's units, instruments for its circuit-only
arm, and cautions for both arms. None of them studies training.

- **Where the units come from.** Zoom In ([LIT-1543](../literature.d/LIT-1543.md)) names features
  and circuits as the units of trained networks, and universality as the
  hypothesis that they recur across models, with evidence it calls
  "anecdotal" ([THEORY-1013](../theory.d/THEORY-1013.md), [THEORY-986](../theory.d/THEORY-986.md)). The question couples
  exactly these two units.
- **Circuit-only measurements, computable at every checkpoint.**
  - The framework's composition scores and eigenvalue statistics
    ([LIT-1534](../literature.d/LIT-1534.md), [NOTE-1189](../notes.d/NOTE-1189.md)) are read from weights alone, and its
    path expansion is exact ([THEORY-988](../theory.d/THEORY-988.md)). Their fragility is on
    record too: the authors published a correction to their own
    composition diagrams (a cyclic permutation inside a Frobenius norm).
  - ACDC ([LIT-1547](../literature.d/LIT-1547.md)) runs on the same two-layer attention-only
    induction setting and finds its heads.
  - AtP and AtP* ([LIT-1531](../literature.d/LIT-1531.md)) make node-level patching cheap enough to
    run per checkpoint, and Pythia releases its checkpoints
    ([THEORY-996](../theory.d/THEORY-996.md)).
  - Causal scrubbing's recovered loss ([LIT-1549](../literature.d/LIT-1549.md)) is a candidate "how
    much does the circuit explain" score per checkpoint.
  - Transcoder or cross-layer-transcoder weights ([LIT-1554](../literature.d/LIT-1554.md),
    [LIT-1552](../literature.d/LIT-1552.md)) describe circuits through MLP layers, but neither paper
    matches features across checkpoints, and the cost is large (about 210
    H100-hours for 2M features on Gemma 2 2B, [NOTE-1185](../notes.d/NOTE-1185.md)).
- **Cautions for the circuit arm.**
  - Knockouts reveal heads that ordinary operation hides: in IOI, backup
    name movers recover most of the effect when the name movers are
    ablated ([THEORY-980](../theory.d/THEORY-980.md)). A head "born" at a checkpoint may have been
    there as a backup.
  - The metric, the ablation type and the visiting order must be held
    fixed across checkpoints: a greedy circuit is one of several
    sufficient subgraphs, and which one is returned depends on the order
    ([THEORY-966](../theory.d/THEORY-966.md), [THEORY-970](../theory.d/THEORY-970.md)). Attribution misses concentrate in
    queries and keys behind a saturated softmax ([THEORY-996](../theory.d/THEORY-996.md)).
  - Attribution graphs freeze attention patterns, so they cannot see
    induction and cannot serve as the circuit-only arm in the induction
    setting ([NOTE-1185](../notes.d/NOTE-1185.md)).
- **Cautions for the feature arm.**
  - Sparse-autoencoder features are a resolution set by dictionary width
    ([THEORY-1016](../theory.d/THEORY-1016.md)), and which concepts get a feature depends on their
    frequency relative to the dictionary's size ([THEORY-992](../theory.d/THEORY-992.md)). An
    apparent split across checkpoints may be the dictionary's.
  - Features can be spread across layers (Templeton et al.'s cross-layer
    superposition, [NOTE-1178](../notes.d/NOTE-1178.md)), which confounds tracking within one
    layer.
  - Circuits over features are faithful only with the dictionaries' error
    terms kept ([THEORY-1007](../theory.d/THEORY-1007.md)), so a circuit arm built on features must
    carry the remainder.
- **A concrete developmental target.** Sparse feature circuits find
  subject–verb agreement across a relative clause carried by two pathways
  that converge without fully intersecting ([THEORY-1014](../theory.d/THEORY-1014.md)). When the
  clause-boundary pathway forms relative to the direct one is a question
  the coupled description could be asked to predict.

## What would answer it

A prospective test, as the reply puts it: "fit the model using early
training checkpoints, then test its predictions about later functional
changes, including changes under held-out training interventions". The
interventions are [CASE-113](../cases.d/CASE-113.md)'s arms plus training exposure, and
architecture is a fourth with a known effect on timing: letting a single
layer attend by the previous token moves the induction transition
([THEORY-973](../theory.d/THEORY-973.md)). The reply's induction-circuit setting is a natural
first case: which partial
capacities exist before the circuit is effective, and whether it forms by
acquiring features or by reorganizing them. The answer is yes if the
coupled description out-predicts the feature-only and circuit-only ones
at matched complexity ([CLAIM-427](../claims.d/CLAIM-427.md)'s third grade), and no if it does not. In
the induction setting the baseline to beat is the reduced dynamics on
the symmetric subspace's coordinates ([THEORY-981](../theory.d/THEORY-981.md)), which is much
stronger than a checkpoint-level state-space model. The design should
avoid the induction-heads paper's confounds: one run per model, one data
order for every model, and a transition inside learning-rate warm-up
([NOTE-1173](../notes.d/NOTE-1173.md)).

Two conditions come from checks made when this was filed ([CASE-165](../cases.d/CASE-165.md)):

- The temporal prior must not condition on θ_s, from which B_s is read.
  Otherwise it predicts nothing, and the prospective test is empty. The
  dependent IBP in its collapsed form is a candidate prior over B_s that
  does not ([THEORY-1006](../theory.d/THEORY-1006.md)), though it still treats components as
  exchangeable.
- Births and splits must be told apart from the model's free symmetries.
  Rescaling, splitting a feature into copies and a zero contribution vector
  all leave the reconstruction unchanged.

## What would not answer it

- "Merely recovering visually plausible circuits from already-trained
  models" (the reply).
- A tie with a state-space model built on the same kernels, which is an
  identity. The lab's comparator pilot (dmarx/PerspectiveLab@dce302b)
  already showed this for its own models ([CLAIM-427](../claims.d/CLAIM-427.md)'s note of 2026-10-26).
- Feature births or splits that a change of basis or the buffet's split
  symmetry produces ([CLAIM-263](../claims.d/CLAIM-263.md)'s quotient, [THEORY-018](../theory.d/THEORY-018.md)).
- Continuity of a feature judged by resemblance alone ([CLAIM-329](../claims.d/CLAIM-329.md),
  [TERM-071](../terms.d/TERM-071.md)). A crosscoder's "maintained" feature is one index of a jointly
  trained dictionary, and an n-gram's migration between heads is the same
  tokens affected at two checkpoints; neither tests inheritance
  ([CLAIM-329](../claims.d/CLAIM-329.md)'s note of 2026-10-26).
- A localization scored only on the hypothesis it was trained against;
  held-out interventions are needed ([THEORY-968](../theory.d/THEORY-968.md), [CLAIM-278](../claims.d/CLAIM-278.md)).
- Success defined in the framework's own terms ([CLAIM-278](../claims.d/CLAIM-278.md)).

## Not in scope

Instructions for training transformers, which are the anthology's
([ADR-048](../decisions.d/ADR-048.md)). Whether a circuit regime is a perspective in any sense beyond
[TERM-072](../terms.d/TERM-072.md)'s organizational one: the reply itself says "satisfying this
organizational definition would say nothing by itself about phenomenal
experience or autonomous agency".
