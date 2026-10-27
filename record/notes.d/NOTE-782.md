---
number: 782
status: Read
formerly:
- NOTE-tmpefcvd
paper: LIT-968
title: 'Makelov, Lange and Nanda — an interpretability illusion for subspace activation patching'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v2 of 6 December 2023, 58 pages),
    fetched from arxiv.org/pdf/2311.17030 and extracted with pdftotext
    -layout: §§1–8 and all of appendices A–E, with the proofs of Lemmas
    A.1, D.1, D.2 and E.1 and the derivation in D.7. The figures were read
    from their captions and surrounding text; several plots (Figures 1,
    10–15, 21–23, 29) do not survive extraction. The reference list was
    scanned, not read. Read together with the reply, LIT-961, and
    Huang et al., LIT-987, as one dispute. The toy-network arithmetic of
    §3.3 and A.3 was re-computed by script.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: ROME, the IOI circuit and DAS, which this
    reading names, were registered and read on 2026-10-26 and are
    cited by code; the random-MLP DAS control is set beside DAS's
    own random-network control. The reading is unchanged.
date: '2026-10-14'
summary: >-
  A subspace activation patch can make a model behave as if a feature had
  changed while the patched direction is the sum of a component that varies
  with the feature but cannot reach the output (in an MLP, the kernel of the
  down-projection) and a component that can reach the output but is dormant
  on the data. Shown exactly in a three-unit network, empirically for MLP8
  of GPT-2 Small on IOI and for MLPs of GPT2-XL on factual recall, where the
  effect vanishes once the disconnected component is removed. A residual
  stream direction passes the same test. One-dimensional fact patches and
  rank-1 edits are shown to be nearly interchangeable.
---
<!-- inactive-ok-file: THEORY-1011 — Proposed; ROME's storage reading, cited as the hypothesis THEORY-282 bears on, not leaned on -->
<!-- inactive-ok-file: CLAIM-130 — Proposed; the partial answer to QUESTION-030 this reading is set beside, open -->

# NOTE-782: Makelov, Lange and Nanda — an interpretability illusion for subspace activation patching

## Contribution

Before this paper, a subspace patch that flips a model's output in the
direction a feature predicts was taken as evidence that the subspace
carries the feature. The paper shows that the patch's success and the
subspace's role can come apart. Linear algebra makes a successful patch
available in almost any MLP layer that sits between two components which
communicate the feature through the residual stream. It gives a
decomposition test that tells the two cases apart in an MLP, and a worked
case in the residual stream where the test is passed.

## Key insight

A patch along v replaces the projection of one activation on v with
another's. It works when v both varies with the feature and can move the
output. Those two properties can come from two orthogonal parts of v: a
part that varies with the feature and is disconnected from the output, and
a part that is connected but constant on the data. Patching their sum lets
the variation in the first push activation into the second. The
intervention then creates a pathway the model does not use; it does not
find one.

## Assumptions

- **The patch.** For unit v, act_B^patched = act_B + (p_A − p_B)v with
  p = vᵀact (Eq. 1). For a subspace with orthonormal basis V,
  act_B^patched = (I − VVᵀ)act_B + VVᵀact_A (A.1).
- **Causally disconnected subspace U.** M_{U←u′}(x) = M(x) for every
  u′ ∈ U. ker W_out of an MLP's post-nonlinearity activations is one
  (§3.5).
- **Dormant subspace U.** M_{U←u_y}(x) ≈ M(x) with high probability for
  x, y drawn from the data distribution D, but some u′ off the data
  changes the output substantially (§3.5).
- **Units are meaningful.** The argument takes model components (heads,
  MLP layers) as the right boundaries of explanation. The authors concede
  that, if activation spaces may be re-parametrized across those
  boundaries, calling the MLP subspace illusory "is much more tenuous"
  (§8, A.3).
- **Ground truth from prior work.** That MLP8 plays no part in IOI rests on
  Wang et al.'s component-level analysis, backed here by a random-weights
  control (B.5). The authors grant that "a definition of a 'ground truth'
  mechanistic explanation is conceptually challenging" (§8).
- **Models and data.** GPT-2 Small on an IOI set of 216 names, 144 objects,
  75 places and three templates, with the test set on an unseen template
  (B.1). GPT2-XL on 40 fact pairs over 8 relations from the first 1000
  CounterFact examples (D.1).

## Key results

- **The construction (§3.2, Eq. 2–3).** With v_illusory =
  (v_disconnected + v_dormant)/√2, v_disconnected ∈ ker W_out and
  v_dormantᵀact_A = v_dormantᵀact_B, the MLP output after the patch is
  W_out act_B + ½(v_disconnectedᵀact_A − v_disconnectedᵀact_B)W_out v_dormant.
  Neither component alone does anything: the first is annihilated by
  W_out, the second does not vary. *Holds:* exactly, for an MLP's
  post-nonlinearity activations.
- **Equal weights are optimal (Lemma A.1).** For v = v_disconnected cos α +
  v_dormant sin α, the expected change along v_dormant is
  cos α sin α · v_disconnectedᵀE[act_A − act_B], maximized at α = π/4.
  *Holds:* when every example projects to the same constant on v_dormant.
  The IOI direction comes close: norms ≈ 0.65 in ker W_out and ≈ 0.75 off
  it (footnote 6).
- **The toy network (§3.3).** x ↦ h = x(1, 0, 1) ↦ y = (0, 2, 1)·h = x.
  Patching along (1/√2, 1/√2, 0) from x′ into x gives
  h = ((x + x′)/2, (x′ − x)/2, x) and output x′, the same as patching h₃.
  In a rotated basis (A.3) the same direction becomes the one the input is
  copied to and read from. The authors call the distinction "artificial"
  in this example (footnote 4).
- **IOI, MLP8 at the last token (Table 1, §4.4).** Fractional logit
  difference decrease (FLDD, Eq. 4) and interchange accuracy:
  - v_MLP: 46.7% FLDD, 4.2% interchange accuracy;
  - its rowspace component alone: 13.5%, 0.2%;
  - its nullspace component alone: 0%, 0%;
  - the whole MLP activation: −8%, 0%.
  The patch drives the MLP's output along v_grad, which it does not do
  without the patch (Figure 4). The nullspace component separates ABB from
  BAB examples far better than the rowspace component (Figure 5). A
  100-dimensional DAS subspace in MLP8 gives 62% FLDD, falling to 17% when
  decomposed (B.6). A DAS direction trained on a random MLP of matching
  norm does better than v_MLP (B.5): "less about what information MLP8
  contains, and more about where MLP8 is in the network".
- **The success case (§5, Table 1).** In the residual stream after layer 8:
  v_resid 140.7% FLDD, 74.8% accuracy; its component outside the kernel of
  the three name-mover query matrices 127.5%, 63.1%; inside it 13.9%,
  0.4%; the whole residual stream 123.6%, 54.8%. v_grad (the gradient of
  the name movers' attention difference): 111.5%, 106.47%, 2.2%. Cosine
  similarity of v_resid and v_grad ≈ 0.78. Only the S-inhibition heads
  write to v_resid, and MLP8 does not (Figure 20). The 100-dimensional
  residual subspace keeps 200% FLDD and 86% accuracy when decomposed (B.6).
- **Factual recall (§6.1, Figure 7, D.2).** DAS directions in GPT2-XL MLPs
  change the recalled object across most layers. Their rowspace components
  and the whole MLP patch have almost no effect. The nullspace component
  is closely aligned with the difference of the two subjects' activations
  (Figure 25).
- **ROME as an optimization (Lemma D.1).** The rank-1 update
  W′_out = W_out + abᵀ minimizes trace Cov_x[abᵀx], x ∼ N(0, Σ), subject
  to W′_out k = v, which gives b = Σ⁻¹k / (kᵀΣ⁻¹k).
- **Patch ⇒ edit (Lemma D.2).** For any 1-dimensional patch from u_B into
  u_A along v there is a rank-1 edit with a = ((u_B − u_A)ᵀv)W_out v and
  bᵀu_A = 1 that gives the same MLP output at that token. Applied to every
  token, it changes predictions negligibly differently from the patch
  (D.6, Figures 27–28).
- **Edit ⇒ approximate patch (§6.3, D.7).** A ROME edit is approximated by
  x ↦ x − (vᵀx)v with v = αW_out⁺a + u, u ∈ ker W_out. In layers 20–35 the
  two are close in rewrite score, cosine of v with b, and variance ratio
  (Figures 8–9). With the ker W_out part removed, every rewrite score is
  below 10⁻³.
- **Prevalence (§7, E.1–E.6).** If a residual direction mediates a binary
  feature between layers a < b, then every MLP in between has a "causal"
  direction W_out⁺v, because W_out is full rank (singular values bounded
  away from 0, Figure 30), and a "correlated" direction, because the
  feature stays linearly separable after the non-linearity. Lemma E.1
  proves separability is preserved if
  (f(xᵢ) − f(xⱼ))ᵀ(f(x_k) − f(x_l)) = λ(xᵢ − xⱼ)ᵀ(x_k − x_l) exactly;
  empirically r² ≈ 0.8 in every layer but layer 0 (E.3). The table of r²
  values is marked "Table TODO" in the posted text.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A subspace patch can reproduce a feature's output effect through a disconnected-plus-dormant pair without the subspace carrying the feature | strong | Eq. 3 and the toy network, §3 |
| C2 | The IOI direction found by DAS in MLP8 of GPT-2 Small is such a case | moderate | Table 1, Figures 4–5, B.5, B.6 |
| C3 | A residual-stream direction for the same feature passes the decomposition test and is written only by the S-inhibition heads | moderate | Table 1, Figure 20, B.6 |
| C4 | DAS fact patches in GPT2-XL MLPs work through the null space of W_out | moderate | Figure 7, D.2 |
| C5 | One-dimensional fact patches and rank-1 edits are approximately interchangeable, so a working rank-1 edit does not show the fact is stored in the edited layer | moderate | Lemmas D.1, D.2, §6.3, D.6 |
| C6 | The illusion is likely in every unused MLP between two components that communicate a feature | weak | heuristic argument with partial empirical support, §7 and E |

## Concepts

- **Causally disconnected subspace.** Setting its projection to any value
  leaves the output unchanged.
- **Dormant subspace.** Patching it with values drawn from the data leaves
  the output roughly unchanged, but some value off the data changes it.
- **Interpretability illusion (here).** A subspace whose patch has the
  effect of changing the feature, where the effect depends on a large
  disconnected component and vanishes when it is removed.
- **FLDD.** 1 − logitdiff_patched / logitdiff, with logitdiff the IO-minus-S
  logit. Above 100% the patch more often than not reverses the
  preference.
- **Faithful direction.** One that both separates the feature's values and
  is aligned with what downstream components read (§5.1).

## Method

DAS learns an orthogonal rotation and trains the subspace end to end so
that the patch gives the counterfactual output (B.3). The diagnostic
splits a found v into its projection on ker W_out (or on a proxy, the
kernel of the name movers' stacked queries, in the residual stream) and
the remainder, patches each, and compares how the examples spread on each
part (§3.4).

## Connections

The paper generalizes activation patching (Vig et al.; Geiger et al.
2020; Meng et al.) to subspaces, as Geiger et al.'s DAS did, and adds a
failure mode to known illusions (Bolukbasi et al. on neurons; McGrath et
al. on backup heads, which give false negatives). It explains Hase et
al.'s finding that ROME works in layers where the fact is not localized.
Atticus Geiger, an author of DAS, is thanked for "thoughtful pushback on
framing and narrative". The reply by Wu, Geiger, Huang and others
([LIT-961](../literature.d/LIT-961.md)) rejects the label "illusion". Huang et al. ([LIT-987](../literature.d/LIT-987.md)) later use
DAS on residual-stream locations, the placement this paper recommends.

## Bearing on the record

- **[QUESTION-030](../questions.d/QUESTION-030.md).** The LIT was registered for "an intervention
  [that] reproduces a feature's effect through a dormant pathway, so
  interventional success does not identify the constituting relation".
  The first half is right. The second uses the record's word, not the
  paper's: the paper speaks of faithfulness to the model's computation and
  says nothing about constitution. What it supplies is narrower and
  sharper. An intervention that produces the predicted counterfactual
  output is not yet evidence that the intervened variable carries the
  feature; the evidence is the effect surviving the removal of components
  that cannot reach the output, together with the variable's being written
  by the upstream components on the data. That is an answer, for one kind
  of system, to which interventions tell a mediating variable from one that
  only accompanies it.
- **[CLAIM-130](../claims.d/CLAIM-130.md).** It separates telling an interpreter from changing the
  situation. This paper adds a third gap inside do(S): an intervention set
  to values off the data distribution can create the very relation it is
  meant to detect. It does not bear on do(I).
- **[CLAIM-150](../claims.d/CLAIM-150.md)** holds that interventional success does not show
  constitution. This paper shows something weaker and more basic in a
  concrete system: interventional success does not even show that the
  variable mediates. And its rotated toy (A.3) shows that which variable
  mediates depends on the choice of units.
- **[TERM-038](../terms.d/TERM-038.md).** The paper's "correlated" direction is descriptive, its
  "causal" direction is causal in A191's sense, and its success case
  needs both on the data. It offers no third, constitutive grade.
- **Filed from this reading:** [THEORY-282](../theory.d/THEORY-282.md) (the illusion) and, with
  the reply, [THEORY-243](../theory.d/THEORY-243.md) (alignments under change of basis).
- **For the anthology.** §8 closes with advice for interpretability
  practice: search in bottlenecks such as the residual stream and validate
  beyond end-to-end effects. That instruction belongs to the anthology and
  is not filed here.

## Limitations

- Two settings only, one model each, and one feature in IOI. Prevalence
  (§7) is argued, not measured across models.
- The ground truth that MLP8 is unused comes from prior component-level
  work. §8 concedes the alternative, two cancelling subspaces in MLP8, and
  rejects it on grounds of parsimony, not by a test.
- The decomposition test is clean only where a component has a known
  disconnected subspace. In the residual stream a proxy is used.
- The factual-recall patches are trained per fact pair, as the reply
  ([LIT-961](../literature.d/LIT-961.md)) points out, so they test whether a patch can be found, not
  whether a general direction exists.
- The success measure, FLDD, can be large while interchange accuracy is
  near zero (46.7% against 4.2% for v_MLP).

## Open questions

- Whether a variable that is real but whose contributions cancel within a
  component can be told apart, by any intervention, from a manufactured
  pathway. A test that held the component's total output fixed while
  moving the two subspaces would separate them.
- Whether the residual stream's being a bottleneck is what protects it,
  or whether disconnected-plus-dormant pairs also arise there for
  features read by few heads.

## Note of 2026-10-27: the works it addresses, now held

Three works this reading names were registered and read on 2026-10-26,
for the owner's request about the record's circuits literature.

- **ROME** (Meng et al., [LIT-1536](../literature.d/LIT-1536.md), [NOTE-1166](NOTE-1166.md)) is the editing
  method whose rank-one update Lemma D.1 restates as an optimization and
  whose edits §6.3 approximates by a patch. The record holds ROME's
  causal traces and CounterFact edits as measured ([THEORY-998](../theory.d/THEORY-998.md)), and
  its reading that the edited site stores the fact as Proposed
  ([THEORY-1011](../theory.d/THEORY-1011.md)), because [THEORY-282](../theory.d/THEORY-282.md) already shows that an edit's
  success does not locate what it changes.
- **IOI** (Wang et al., [LIT-1540](../literature.d/LIT-1540.md), [NOTE-1167](NOTE-1167.md)) is the
  component-level analysis on which this paper's ground truth for MLP8
  rests. Its circuit of 26 heads in seven classes is [THEORY-980](../theory.d/THEORY-980.md).
- **DAS** (Geiger et al., [LIT-1551](../literature.d/LIT-1551.md), [NOTE-1192](NOTE-1192.md)) is the method this
  paper's subspace patches are trained with. Its own control on frozen
  random networks, IIA at chance up to width 256 and 0.64 at width 4,096
  ([THEORY-1002](../theory.d/THEORY-1002.md)), is the same kind of check as this paper's DAS
  direction trained on a random MLP (B.5), and points the same way: in a
  wide enough space a supervised search finds alignment in a network
  never trained for the task.

Hase et al.'s finding that ROME works in layers where the fact is not
localized, which this paper explains, is not registered; the curation
entry for the circuits reading names it. The reading is unchanged.
