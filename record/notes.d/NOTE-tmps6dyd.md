---
status: Read
paper: LIT-tmpy7s15
title: 'Liang et al. — MuEdit'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from https://arxiv.org/pdf/2611.14910v1 (30 pp.);
    text extracted with pdftotext, with tables re-extracted in layout mode.
    Read: the abstract, §§1–6, the appendix sections on lemmas, cost,
    knowledge-matrix construction, baselines and limitations, and Tables
    1, 2, 3, 5 and 12. Skimmed: the remaining appendix tables and case
    studies. Not read: the NeurIPS checklist, beyond locating its pointer
    to the limitations. No code was run. Section numbers are the paper's.
date: '2026-11-15'
summary: >-
  A method paper on editing an LLM sequentially across heterogeneous
  domains. Its diagnosis: null-space editing must confine each update to
  the intersection of the domains' null spaces, which can be small. Its
  measure: a Conflict Index of null-space overlap. Its method: order
  tasks by conflict and compress conflicting preservation matrices.
  Results on three backbones beat the editors compared. Two limits found
  in reading: the index as defined would be degenerate at the paper's own
  sizes unless null spaces are numerical, which the text does not
  specify; and in the seven-task test, greedy ordering is within the 95%
  interval of the mean random order on every task.
---

<!-- inactive-ok-file: THEORY-1039 THEORY-1011 — Proposed and Rejected; the key–value reading the paper assumes, discussed under Bearing -->

# NOTE-tmps6dyd: Liang et al. — MuEdit

## Contribution

The paper names a failure of null-space-projected editing (AlphaEdit) that
appears only across domains. Each domain's preserved keys Kᵢ admit many
update directions with ΔKᵢ = 0, but jointly preserving several domains
confines the update to the intersection of their null spaces.

- **The measure.** The Conflict Index, the fraction of the smaller null
  space lost in the intersection.
- **The method.** MuEdit has three parts:
  - choose an order that keeps adjacent conflict low;
  - when conflict passes an adaptive threshold, cut the rank of the more
    conflicting preservation matrix, so as to enlarge the null space;
  - update in closed form inside the joint null space of a three-task
    window.

## Key insight

Preservation constraints compose by intersection. One constraint set can
leave ample room, and two can leave none: "Although each domain may
individually admit many update directions, their intersection can be much
smaller" (§1). The paper calls the resulting bottleneck "inter-domain
null-space misalignment" (§3.1).

## Assumptions

- **The key–value view of the edited MLP projection** (§2.1). Keys are
  the activations entering the output projection, and preserving a
  layer's outputs on reference keys is taken to preserve the
  corresponding knowledge.
- **Reference inputs stand for a domain.** 10,000 reference inputs per
  task by default, last-token keys, no labels (Appendix 7.7).
- **Order matters only through what each step must protect.** "For
  fixed task matrices, the final intersection is independent of task
  order" (§3.2). Order changes which constraints each intermediate step
  is exposed to.
- **Five edited layers** (4–8 on Llama3-8B), 500 edits per task.

## Key results

- **Lemma 1** (§3.1, Appendix 7.2): N([Kᵢ, Kⱼ]ᵀ) = N(Kᵢᵀ) ∩ N(Kⱼᵀ), so the
  common null space is no larger than the smaller of the two.
  **Lemma 2**: the Conflict Index is symmetric, lies in [0, 1], and is
  zero for a task against itself.
- **Order matters for AlphaEdit too** (§4.2, Obs. 1): moving from the
  default to the best order "improves AlphaEdit's ZsRE Specificity from
  0.3009 to 0.5506 and CKnowEdit Specificity from 0.2873 to 0.6624".
- **MuEdit, best order** (Table 1, Llama3-8B): "Mu-Edit improves ZsRE
  Specificity from AnyEdit's 0.7098 to 0.8845 and CKnowEdit Specificity
  from 0.6882 to 0.8505", the highest on every reported metric.
- **Ablations** (Obs. 2): adaptive thresholds beat a fixed µ = 0.2 on
  every metric. Always compressing the earlier task's matrix is worse
  than always compressing the later one.
- **General ability** (§4.3, Fig. 2): "MEMIT performance drops to near zero
  after two tasks", AlphaEdit and AnyEdit degrade, and MuEdit shows "only
  minor declines".
- **Rank reduction** (§4.4, Fig. 3): single-task performance changes little up
  to 30% reduction and degrades beyond 45%. The largest Conflict Index
  in their tasks, 0.431, needed a 38.2% reduction (§8, Limitations).
- **Robustness** (§4.5, Tables 3–4): conflict rankings "remain broadly
  consistent" with 50 reference examples, and mixing domains in the
  reference set changes results little.
- **Seven tasks** (§4.6, Table 5): MuEdit under any order beats AlphaEdit on
  every task (ZsRE 0.5375 against 0.8708 greedy). But see Limitations
  on what Table 5 shows about ordering.

## Concepts

- **Preservation (knowledge) matrix Kᵢ**: the stacked keys of a domain's
  reference inputs at an edited layer.
- **Common null space**: the intersection of the left null spaces of
  several Kᵢ, the update directions that preserve all of them.
- **Conflict Index**: C(Kᵢ, Kⱼ) = 1 − dim N([Kᵢ, Kⱼ]ᵀ) / min(dim N(Kᵢᵀ),
  dim N(Kⱼᵀ)), averaged over layers.
- **Best Order / Greedy Order**: orderings minimizing the summed adjacent
  conflicts, by exhaustive search or by insertion as tasks arrive.

## Connections

The paper extends AlphaEdit (Fang et al. 2024, not held), the null-space
form of the MEMIT objective ([LIT-1582](../literature.d/LIT-1582.md), [THEORY-1031](../theory.d/THEORY-1031.md)), whose key–value
framing comes from ROME ([LIT-1536](../literature.d/LIT-1536.md)) and Geva et al. Hase et al. ([LIT-1578](../literature.d/LIT-1578.md),
[THEORY-1024](../theory.d/THEORY-1024.md)) showed that where a fact is traced need not be where an edit
works. This paper sidesteps that question: its layers are chosen by
convention, not by tracing.

## Bearing on the record

- **[THEORY-1039](../theory.d/THEORY-1039.md) and [THEORY-1011](../theory.d/THEORY-1011.md).** The paper assumes the key–value
  reading. Its geometric result does not depend on it: that ΔKᵢ = 0
  leaves the edited layer's outputs on those keys unchanged is linear
  algebra, true whatever the layer "stores". What depends on the reading
  is calling those outputs the domain's knowledge. The paper's results
  neither support nor weaken [THEORY-1039](../theory.d/THEORY-1039.md): they show that preserving
  reference keys preserves task performance, which any account of the
  layer's role would predict. No note filed.
- **[CLAIM-366](../claims.d/CLAIM-366.md)** (whether objectives share a strict descent direction is
  invariant under reparameterization). The paper meets the same
  structural problem in another form: several constraints, each
  satisfiable, jointly leave little room. [CLAIM-366](../claims.d/CLAIM-366.md) asks for a common
  descent direction, and this paper for a common null-space direction.
  The parallel is noted here only. The paper's measure is Euclidean and
  rank-based, and [CLAIM-366](../claims.d/CLAIM-366.md)'s point about which such measures are
  invariant would apply to any extension of it to curved parameter
  metrics. No note filed: the bearing is an analogy.
- **[THEORY-1031](../theory.d/THEORY-1031.md)** (MEMIT's mass editing). The paper reports MEMIT's
  general ability "near zero after two tasks" in multi-task editing on
  Llama3-8B, which bounds that THEORY's single-domain result. No note
  filed, since [THEORY-1031](../theory.d/THEORY-1031.md) states its scope as single-domain counterfactual
  insertion.

## Limitations

- **The Conflict Index is degenerate as written, unless null spaces are
  numerical.** On Llama3-8B the edited matrix's input width is the MLP
  intermediate size, 14,336 (not stated in the paper; from the model's
  published configuration). Two cases:
  - With the default 10,000 reference keys, a generic Kᵢ has full column
    rank, so each null space has about 4,336 dimensions. Two domains
    stack 20,000 > 14,336 keys, so the common null space is generically
    {0}, and every pair would score C ≈ 1.
  - With 50 keys, every pair would score about 50/14,286 ≈ 0.0035.

  The reported values (up to 0.431), and rankings stable from 50 to
  10,000 examples, imply a thresholded numerical null space, presumably
  AlphaEdit's preprocessing, which the paper says MuEdit shares (§4.1).
  The threshold is not given in the text read, and the index's meaning
  depends on it.
- **Ordering's benefit in the seven-task test is within noise.** Table 5
  gives 95% intervals for the mean over 50 random orders. Greedy Order
  lies inside the interval on all seven tasks, for example ZsRE 0.8708
  in [0.7868, 0.8815] and SQuAD 0.7356 in [0.6915, 0.7432]. Best Order
  lies at or just above the upper bound. The paper's summary that these
  experiments "support the benefits of conflict-aware ordering" is
  stronger than its table. Almost all of the gain over AlphaEdit there is
  independent of order.
- **"Safety" edits make models less safe.** SafeEdit is scored as Harmful
  Rate, higher being better, and the ethics statement explains that it
  measures "the multi-task stability of injected unsafe knowledge". The
  safety domain is thus an edit that removes safety behaviour.
- **Adjacent pairwise conflict is a surrogate**, "rather than an exact
  measure of cumulative forgetting" (§3.2), as the authors say.
- **Hyperparameters** (µ, α, t) are not fully characterized across
  architectures (§8).
- **Mean scores only** in Tables 1–2. The significance marks compare
  only with AnyEdit.

## Open questions

- What numerical rank threshold defines the null spaces, and how does
  the Conflict Index vary with it?
- With ordering's effect within noise at seven tasks, which component
  carries MuEdit's gain over AlphaEdit: the three-task window, the rank
  compression, or the shared preprocessing?
