---
number: 217
status: Open
formerly:
- QUESTION-tmp8qovh
title: 'When a learning system is said to go from coarse to fine, do the order in which its representations refine one another, the order of their relevance to a task and the order in which training acquires them admit one common chain, and under what conditions on the learning operator?'
version: 6
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A5's "two different mathematical
    order structures" is this question's refinement order against its
    relevance order; its monotone half is elementary. The question is
    unchanged.
- version: 3
  date: '2026-11-11'
  note: >-
    Refines QUESTION-039 (a defect listed in the curation entry of
    2026-11-10). Its own text asks for "the order in which training
    acquires" a learner's representations and "under what conditions on
    the learning operator" it agrees with the other two orders, citing
    THEORY-086 ("in the kernel regime the order is by NTK eigenvalue"),
    which QUESTION-039 also holds: a sharpening of QUESTION-039's "What
    sets the order ... at which a network acquires a structure". Under
    ADR-085 the relation gives this question QUESTION-039's first line,
    learned-structure, which it already carries. No other change.
- version: 4
  date: '2026-11-15'
  note: >-
    Note of 2026-11-15 added, from the continuation of the exchange "Explain
    String Theory" (A14): in the kernel's moving eigenbasis the residual
    relaxes along the current modes and is redistributed as the modes
    rotate, which adds a third order, the order in which the space of modes
    is reorganized. It answers none of the three. The question is unchanged.
- version: 5
  date: '2026-11-18'
  note: >-
    Correction from the synthesis review of 2026-11-18: the note of
    2026-11-15 said the moving-basis term "adds a third order to the
    question's two"; the question separates three orders (refinement,
    relevance, acquisition), so the term adds a fourth. Corrected in
    place. No other change.
- version: 6
  date: '2026-11-21'
  note: >-
    Note of 2026-11-21 added, from the exchange "Rich Get Richer Power
    Laws" (A29 §10, A33, A35): first entry into nested entailment cones
    is a refinement order by construction and cannot stand for the
    acquisition order (CLAIM-800); and a hypothesis that coarse
    distinctions settle early in a hierarchy of relaxation times. The
    owner's U21 is filed as QUESTION-512, which refines this one. The
    question is unchanged.
tags:
- learning-theory
- representation-learning
- information-theory
date: '2026-10-19'
line: learned-structure
summary: >-
  A1 and A2 of the exchange of 2026-10-19 on coarse-to-fine processes. The
  record already holds that "coarse to fine" names different things: an
  order in training time by singular value ([THEORY-186](../theory.d/THEORY-186.md)), an order in
  noise ([THEORY-199](../theory.d/THEORY-199.md)), and a sample-complexity result in which every
  level arrives at once ([THEORY-195](../theory.d/THEORY-195.md)). No entry separates refinement,
  relevance and acquisition as three relations and asks when they agree.
  An answer is a theorem giving sufficient conditions for a common chain,
  or a minimal family of counterexamples.
refines:
- QUESTION-039
---
<!-- inactive-ok-file: CASE-tmpb4hg0 — new; the run of LEAD-172, filed 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmpwtoad — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: THEORY-777 — Proposed; the Ising numerics, cited as open -->
<!-- inactive-ok-file: THEORY-759 — Proposed; the spectral-bias order of acquisition, cited as open -->
<!-- inactive-ok-file: THEORY-186 THEORY-199 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
<!-- inactive-ok-file: CLAIM-800 THEORY-1558 — new or Proposed; filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, and a reading named for comparison -->
<!-- inactive-ok-file: THEORY-tmpr9w2r — Proposed, new or Deferred; filed on 2026-11-21 from the readings of that day -->
<!-- inactive-ok-file: THEORY-tmp8sxta — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->
# QUESTION-217: When a learning system is said to go from coarse to fine, do the order in which its representations refine one another, the order of their relevance to a task and the order in which training acquires them admit one common chain, and under what conditions on the learning operator?

## Why it is a question

A2 of the exchange of 2026-10-19 separated three relations on a family of
representations Z_ℓ:

- **refinement**: Z_a is a function of Z_b (σ(Z_a) ⊆ σ(Z_b));
- **relevance**: Z_b is at least as informative about a stated target;
- **acquisition**: the distinctions in Z_a become recoverable no later in
  training than those in Z_b, with an acquisition time
  T_ℓ(δ) = inf{t : R(D_{ℓ,t}, Z_ℓ) ≤ δ} for a decoder D and a risk R.

"The information ordering and the acquisition ordering must be represented
separately. The first is structural. The second is dynamical." A coarse-to-
fine schedule is the case where the three admit a common monotone chain.
A2: "Crucially, the default should not be to assume these orderings agree."

## What the record holds

- [THEORY-186](../theory.d/THEORY-186.md): in a deep linear network the order is by singular
  value, and "Fine distinctions come first whenever the data make them
  stronger". So acquisition and refinement can be reversed. It is exact
  only for decoupled, balanced starts and white inputs.
- [THEORY-086](../theory.d/THEORY-086.md): in the kernel regime the order is by NTK eigenvalue,
  "not by degree".
- [THEORY-481](../theory.d/THEORY-481.md): in linear attention the order is by input variance,
  with alignment to the eigenbasis assumed, and at finite context the
  modes couple at order 1/N.
- [THEORY-199](../theory.d/THEORY-199.md), [THEORY-195](../theory.d/THEORY-195.md) and [NOTE-687](../notes.d/NOTE-687.md): orders in noise and in sample
  size that run opposite to [THEORY-186](../theory.d/THEORY-186.md)'s, and "should not be cited as
  one account".
- Read on 2026-10-20:
  - [THEORY-745](../theory.d/THEORY-745.md) (diffusion maps, [NOTE-985](../notes.d/NOTE-985.md)): the exactly commuting
    case. When the levels are the operator's own spectral projectors,
    truncated diffusion maps form an exact refinement chain ordered by
    |λ_l|, and repeated application of the operator acquires them in the
    same order. The two orders agree only because they come from one
    eigenbasis. The order also depends on the normalization α, so it is
    not a property of the data alone.
  - [THEORY-742](../theory.d/THEORY-742.md) (Raju, Machta and Sethna, [NOTE-972](../notes.d/NOTE-972.md)): along nested
    coarse-grainings the Fisher metric of the parameters can only fall, so
    refinement and relevance to the parameters share a chain. Under an
    exact RG step the singular part of the metric is kept. There is no
    learning operator, so it says nothing about acquisition.
  - [CLAIM-387](../claims.d/CLAIM-387.md): among optimal compressions at different budgets the
    refinement order itself can fail to be a chain.
- Third batch, read the same day:
  - [THEORY-758](../theory.d/THEORY-758.md) (diffusion wavelets, [NOTE-984](../notes.d/NOTE-984.md)): the multilevel
    version of the commuting case. The levels are octave bands of an
    operator's spectrum, nested exactly for any operator with spectrum in
    [0, 1]. Spectral decay buys compression, not nesting. The paper's
    compressed algorithm thresholds T^(2^(j−1)), not the T^(2^j − 1) it
    states.
  - [THEORY-746](../theory.d/THEORY-746.md) (slow feature analysis, [NOTE-971](../notes.d/NOTE-971.md)): a third
    commuting case. Slow features are the bottom of a generalized
    eigenproblem, nested by eigenvalue. A stack of SFA stages is a
    refinement chain by construction, and its slowness values cannot rise
    from stage to stage on the training signal. Slow features are coarse
    only in that sense: they include squares, products and location. The
    paper says nothing on predictive sufficiency or learning dynamics.
  - [THEORY-759](../theory.d/THEORY-759.md) (spectral bias, Proposed, [NOTE-983](../notes.d/NOTE-983.md)): a finite
    ReLU network trained with Adam fits sinusoids in order of frequency,
    even when amplitude rises tenfold with frequency. So in that setting
    the learner, not the target's strength, sets the acquisition order,
    against [THEORY-186](../theory.d/THEORY-186.md)'s order by singular value. Fourier bands are not a
    refinement chain, so this order has no structural partner.
    [THEORY-761](../theory.d/THEORY-761.md) is the paper's proved representational bound, which is
    about what a network can contain, not about training.
  - Open: where the amplitude ratio flips the order from by-frequency to
    by-strength. The record has no formula for the product of the
    learner's spectrum and the data's outside the kernel regime.

- Machta, Chachra, Transtrum and Sethna (2013), [THEORY-774](../theory.d/THEORY-774.md)
  (Active): in their hopping model, observed at a later time t, the k-th
  Fisher eigenvalue scales as t^{3/2−k}, so the nested effective models
  (creation; then drift; then diffusion; ...) are ordered by relevance.
  Since the metric is the Gauss–Newton Hessian of the least-squares
  cost, gradient flow near a fit acquires the same directions in the same
  order, in these coordinates only (natural-gradient flow would fit all at
  one rate). Another commuting case, as in [THEORY-745](../theory.d/THEORY-745.md). Its Ising half
  ([THEORY-777](../theory.d/THEORY-777.md), Proposed) orders relevance along decimation, with no
  learner.

- Schüler and Wiskott (2025), [THEORY-775](../theory.d/THEORY-775.md) (Active): slow feature
  analysis as a variational objective with a random-walk prior. On
  whitened linear input its optimum is SFA's span of directions with
  lag-one autocorrelation above ½, up to rotation, so the spans nest by
  slowness as more latents are allowed: a refinement order of spans, not
  of features. On raw input it is not SFA. [CLAIM-394](../claims.d/CLAIM-394.md)
  (demonstrated): in a reversible linear Gaussian VAR(1) every slow
  direction is a left eigenvector of A, so slowness selects exactly
  closed coarse-grainings; off reversibility it does not. Neither speaks to
  the order of acquisition.

What the record lacks is the condition under which a spectral order is a
refinement order. A2's candidate ("Conjecture A", in its words "a
candidate research direction, not an established theorem"): let P_ℓ
project onto the observables of level ℓ. If the learning operator A
nearly commutes with every P_ℓ ([A, P_ℓ] ≈ 0) and its effective
eigenvalues fall as finer distinctions are added, acquisition is nearly
coarse to fine, with deviations set by the cross-level coupling and the
spectral gaps. For a moving operator A_t it proposed
∫‖[A_t, P_ℓ]‖ dt ≪ 1 as the measure.

## What would count as an answer

- A theorem giving sufficient conditions, for a stated model class, under
  which the three relations share a chain; or
- a small family of constructions in which each pair comes apart. One is
  already on file: [THEORY-186](../theory.d/THEORY-186.md)'s fine-first case.

A2's first project would test it: synthetic data with a known tree, with
the spectral strength assigned to each level varied independently of the
tree, trained in a deep linear network, a kernel-regime network and a small
nonlinear one, reporting a phase diagram of coarse-first, fine-first,
simultaneous and mixed acquisition. Readings registered with this question:
spectral bias ([LIT-1261](../literature.d/LIT-1261.md)), slow feature analysis ([LIT-1249](../literature.d/LIT-1249.md)),
diffusion maps ([LIT-1246](../literature.d/LIT-1246.md)) and diffusion wavelets ([LIT-1256](../literature.d/LIT-1256.md)), and the
information geometry of coarse-graining ([LIT-1254](../literature.d/LIT-1254.md)). Whether optimal
representations nest at all is [QUESTION-220](QUESTION-220.md).

## Note of 2026-10-21: two order structures

A5 of the exchange of 2026-10-20 proposed "two different mathematical order
structures": what is identifiable grows with the access regime, while
optimal representations need not nest. The second half is this question's
refinement order against its relevance order, with [CLAIM-387](../claims.d/CLAIM-387.md) as the
witness this question already cites. A5's monotone half is elementary:
inclusion of feasible sets gives a monotone optimal value, and refinement
of the fibres gives monotone identifiability. For a fixed target, the
monotone half is now filed as [CLAIM-409](../claims.d/CLAIM-409.md). The proposal appears once.

## Note of 2026-11-15: acquiring a mode, against changing the modes available

Under squared-error gradient flow, the residual obeys ė = −K_τ e. Write it in the kernel's moving eigenbasis, e = U_τ a, with K_τ = U_τ Λ_τ U_τᵀ. Then ȧ = −Λ_τ a − Ω_τ a, with Ω_τ = U_τᵀ U̇_τ skew-symmetric. The first term is relaxation along the current modes. The second redistributes the residual because the modes themselves rotate. In the fixed-kernel regime the second term vanishes, and learning order is spectral order. With feature learning it need not be. The derivation is A's, from the continuation of the exchange "Explain String Theory" (A14), and is standard calculus under differentiable, non-degenerate eigenspaces. Within a degenerate eigenspace the rotation is a choice of coordinates, so only rotations of identifiable subspaces count.

It adds a fourth order to the question's three: the order in which the space of modes is reorganized. This answers none of the four. No status change.

## Note of 2026-11-19: Chen and colleagues, read
A qualification by analogy ([NOTE-2165](../notes.d/NOTE-2165.md)): the order in which skills benefit training departs from the task's own dependency order ("the reasoning graph does not necessarily equal the skills graph").

## Note of 2026-11-21: entailment cones, and a hierarchy of relaxation times

The exchange "Rich Get Richer Power Laws" (2026-11-21) came to this question twice.

- **Cones are a refinement order, not an acquisition order.** The owner asked at U21 whether entailment cones help reason about progressive learning ([QUESTION-512](QUESTION-512.md), which refines this question). A35 §5 warns that with C_fine ⊆ C_coarse, first entry into the coarse cone can never come after first entry into the fine one, so "that ordering is imposed by the geometry. It is not evidence that the network learned coarse concepts before fine concepts" ([CLAIM-800](../claims.d/CLAIM-800.md)). In this question's terms, cone first-entry times are a refinement order by construction; the acquisition order still needs a decoder's risk, as T_ℓ(δ) defines it. A35 §6 adds a signature that is not built in: with Y_coarse a function of Y_fine, the chain rule I(Z_t; Y_fine) = I(Z_t; Y_coarse) + I(Z_t; Y_fine | Y_coarse) separates the two levels' information over training, for Shannon information only ([THEORY-846](../theory.d/THEORY-846.md)).
- **Relaxation times.** A29 §10 proposes, as a hypothesis, that in representation learning the interaction geometry co-evolves with the representation, so "coarse semantic distinctions becoming stable early, while increasingly fine distinctions continue reorganizing later in training", giving "a hierarchy of relaxation times", whose scale-freedom "is an empirical question". This is the acquisition order read as settling time, and [THEORY-1558](../theory.d/THEORY-1558.md)'s demarcation of levels by relaxation rate in another register. It is not filed separately: it adds a measurement (relaxation per level, [LEAD-210](../leads.d/LEAD-210.md)) and no answer.

This answers none of the orders. No status change.

## Note of 2026-11-21: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet, read

Supports a coarse-to-fine progression in a single run, as an acquisition
order ([NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md), [THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)): in the two-layer language model
the stages run bigrams, then n-grams with positional embedding, then
previous-token heads, then induction heads, which the authors liken to
Olsson et al.'s progression across depth (§8). Two qualifications bear on
whether one chain holds. The groundwork for the induction circuit is laid
in LM2, "in advance of any measurable change in model outputs or attention
patterns" (§6.2), so the order of acquisition by behaviour and by
structure can differ; and three stages lower the estimated coefficient,
simplifications rather than acquisitions ([QUESTION-tmphkb1w](QUESTION-tmphkb1w.md)). Written as
`bears_on` from the reading. No status change.

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md), [NOTE-tmp923nm](../notes.d/NOTE-tmp923nm.md), [THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md)): **a
parallel from neuroscience.** In V1, "Successive PC dimensions encode finer
stimulus features" (Extended Data Fig. 6), and a linear readout of such a
code learns coarse features first, "at a speed proportional to the
eigenvalues" (SI §2.4). It is coarse-to-fine in a fixed code read out by a
learner, not in a network whose features change, so it leaves the question
open. No relation.

## Note of 2026-11-22: Yang, Steinhardt and Hu, read

Yang, Steinhardt and Hu ([LIT-2957](../literature.d/LIT-2957.md), [NOTE-tmpl260d](../notes.d/NOTE-tmpl260d.md), [THEORY-tmp8sxta](../theory.d/THEORY-tmp8sxta.md)): **background,
leaves it open, with one data point.** The training labels set a relevance
order (coarse), yet the representation refines by input structure first:
"The effect of input distribution emerges earlier in training, while the
effect of labels appears at a later stage." That is a refinement order in
distances running ahead of the supervised one; no acquisition order by a
decoder's risk is measured over time. No relation.

## Note of 2026-11-22: the kernel's modes in the modular-addition run

In [LEAD-172](../leads.d/LEAD-172.md)'s reduced run ([CASE-tmpb4hg0](../cases.d/CASE-tmpb4hg0.md)) the moving-basis term was tracked by proxy: the rotation of the empirical tangent kernel's top eigenspace between checkpoints 250 steps apart. It forecast nothing about when the network generalizes. The top eigenspace stayed at chance alignment with the functions the task needs (functions of a + b) throughout, even after generalization, while the input-to-output Fourier coupling did forecast. In this network, then, acquisition is not visible as the kernel's leading modes turning toward the target. It is one network and one kernel, the class-summed trace kernel. It answers none of the four orders. No status change.

## Note of 2026-11-22: the tree with strengths set per level, run

<!-- inactive-ok-file: CASE-tmp7n58t CLAIM-tmpzujm1 CLAIM-tmp0h57p — new; the study and claims of LEAD-052, filed 2026-11-22 -->

A2's first project, run for [LEAD-052](../leads.d/LEAD-052.md) ([CASE-tmp7n58t](../cases.d/CASE-tmp7n58t.md)): eight items on a
depth-3 tree, inputs and targets each given a strength per level, and the
acquisition time of each level read from the network's own output.

- **Conjecture A's condition, by symmetry.** With tree-symmetric inputs
  every kernel of inner products and norms commutes exactly with the level
  projectors, so kernel flow acquires the levels in the order of its
  per-level eigenvalue, which depends on the input strengths alone; a
  decoupled deep linear network orders them by input strength times target
  strength ([CLAIM-tmpzujm1](../claims.d/CLAIM-tmpzujm1.md), demonstrated). Commutation here does not
  make acquisition coarse to fine: it makes the order spectral, and
  whether the spectral order is the refinement order is then a fact about
  where the strength sits.
- **The phase map.** Each phase appeared for each learner that depends on
  strength, and tree depth set no order by itself. The kernel and
  deep linear learners' boundaries lie on different surfaces, so the same
  data can be coarse-first for one and simultaneous or fine-first for the
  other. A small two-layer ReLU network from small scale kept the
  deep linear direction with its spread of times compressed, so much of
  its map is simultaneous ([CLAIM-tmp0h57p](../claims.d/CLAIM-tmp0h57p.md), empirical).

For these model classes on tree-symmetric data this gives the condition:
the acquisition order agrees with the refinement order when, and only
when, the learner's per-level rate falls with depth. It leaves the
general case open (data off the symmetry, where the levels mix) and the
relevance order untouched. No status change.
