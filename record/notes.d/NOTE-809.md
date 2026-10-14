---
number: 809
status: Read
formerly:
- NOTE-tmptglsv
paper: LIT-961
title: 'Wu et al. — a reply to Makelov et al.''s interpretability illusion arguments'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v1 of 23 January 2024, 20 pages),
    fetched from arxiv.org/pdf/2401.12631 and extracted with pdftotext
    -layout: §§1–6 and appendices A–D. Figures were read from captions and
    the values printed on them. The reference list was scanned. Read after
    Makelov et al. (LIT-968, NOTE-782), whose text was used to check
    each attribution. The toy-network computation of §3.2 was re-run by
    script, with and without normalizing the rowspace component; the
    result is reported under Key results.
date: '2026-10-14'
summary: >-
  The reply argues that Makelov et al.'s "illusion" is defined so that any
  direction not orthogonal to the null space of the downstream weights can
  qualify, including the direction Makelov et al. call faithful in their
  toy network, and that their in-the-wild cases rest on a weak metric and on
  DAS trained per fact pair. The toy computation holds only for an
  unnormalized patch: patching the subspace the rowspace component spans,
  as Makelov et al. specify, recovers the full effect. Its own GPT-2
  experiments agree that MLP8 carries almost no name-position information.
---
<!-- inactive-ok-file: CLAIM-130 — Proposed; the partial answer to QUESTION-030 this reading is set beside, open -->
<!-- inactive-ok-file: THEORY-282 THEORY-243 — Proposed; the accounts this reading bears on, one filed from it -->

# NOTE-809: Wu et al. — a reply to Makelov et al.'s interpretability illusion arguments

## Contribution

The authors of distributed alignment search (DAS) reply to Makelov et al.
([LIT-968](../literature.d/LIT-968.md)). They restate the illusion as a difference of two interventions,
argue that it is generic and not a defect, criticize the evidence for it
in GPT-2 and GPT2-XL, and add their own DAS analysis of where name-position
information arises in GPT-2 Small on IOI. Read with the paper it answers,
it clarifies what the two sides agree on: the facts at MLP8 and the
residual stream. What they disagree on is what counts as evidence that a
found subspace is the model's variable.

## Key insight

A representation's variation lies on whatever submanifold the upstream
computation produces, and nothing makes that submanifold orthogonal to the
null space of the next layer. So a direction that carries a variable will
in general have some component the next layer cannot read. On this view a
test that penalizes such components penalizes the geometry of
representations, not a failure of the method. Interventions on the data
distribution also cannot by themselves choose between alignments related
by a change of basis.

## Assumptions

- **Evaluation by IIA.** A high-level causal model is a faithful
  description "under the set of interventions we perform" to the extent
  that interchange intervention accuracy (IIA) approaches 100% (§4.2).
- **The illusion as Makelov et al. define it, in the reply's words.**
  ILLUSIONEFFECT(Φ, W_out, v, A, B) = Φ(u_A^{v←B}W_out) −
  Φ(u_A^{v_r←B}W_out) (Eq. 8), with v_r the component of v outside
  ker W_out.
- **Data-induced submanifold.** The set of activations some input can
  produce. In the toy network it is the line spanned by (1/√2, 0, 1/√2)
  (§3.1).
- **Experiments.** GPT-2 Small with Makelov et al.'s data scripts; 200
  base–source pairs; Adam, learning rate 0.01, 10 epochs, batch 20; two
  templates for training and an unseen one for evaluation (App. B).

## Key results

- **The decomposition (§2, Eq. 7).** u_A^{v←B}W_out = u_A W_out +
  (u_B − u_A)v_nᵀv_r W_out + (u_B − u_A)v_rᵀv_r W_out. The effect of a
  patch splits into a term carried by the null-space projection of the
  difference and a term carried by the rowspace projection. This is
  Makelov et al.'s Eq. 3, generalized.
- **The toy counterexample (§3.2).** For h₃ = (0, 0, 1), which Makelov et
  al. treat as the faithful direction, the reply finds v_n = (0, −0.4, 0.8)
  and v_r = (0, 0.4, 0.2), so ILLUSIONEFFECT = 0.8(x′ − x) (Eq. 15). With
  x = 1, x′ = 5 the patch along v gives 5 and the patch along v_r gives
  1.8. It concludes that h₃ "would be classified as an 'illusory'
  direction".
  - **Checked here, and it does not hold as Makelov et al. define the
    test.** The second column the reply writes for its null-space basis,
    (0, −1/√3, √2/√3), is not in the null space of W₂ = (0, 2, 1)
    (2·(−1/√3) + √2/√3 ≈ −0.34). The projection it reports is
    nevertheless the correct one, and so is 1.8 for a patch with the
    unnormalized vector v_r. But Makelov et al.'s test patches "the
    subspace spanned by v_row" (their §3.4), and a patch of a subspace
    does not depend on the length of the vector that spans it. The
    reply's footnote 1 says Makelov et al.'s code normalizes v_r and
    predicts this makes the illusion larger. It removes it. v_r = 0.2·W₂,
    so the normalized patch is the patch along W₂ itself, which gives
    x + (x′ − x) = 5, the full effect. The same holds for Makelov et al.'s
    illusory direction (1, 1, 0)/√2. In the toy the test passes both
    directions, because W₂'s rowspace is one-dimensional and the data vary
    along it. It neither rejects the faithful direction nor catches the
    illusory one there. Makelov et al. never apply the test to the toy.
- **The general point (§3.3).** A faithful distributed representation need
  not be orthogonal to the null space of downstream computation, "simply
  because the image of upstream computations need not be". The reply
  agrees that the MLP-in-the-middle phenomenon "will be common", "Except
  it is not an 'illusion' in any useful sense."
- **Multiple abstractions (App. A).** With R the rotation whose first row
  is (1/√2, 1/√2, 0), the network is g(x) = (1/√2)(√2x)_H1 −
  (1/√2)(√2x)_H2 + (1·x)_H3 = x (Eq. 17). The input identity aligns with
  H3 in the original basis or with H1 in the rotated one. "The causal
  abstraction framework cannot determine structural equivalence between
  objects." Intervening on further variables (H2) separates them. For
  complex models "there are still likely to be multiple distinct fully
  correct abstractions" (a conjecture).
- **Against FLDD (§4.2).** FLDD is a ratio of logit differences. A model
  that moves from 0.505 to 0.5025 on the IO name shows about 50% FLDD with
  no change in behaviour. The reply reads Makelov et al.'s 4.2% IIA for
  v_MLP as "a failure to find any relevant structure".
- **Against activation-distribution evidence (§4.3).** Activations
  strongly correlated with a concept can have little causal effect
  (Huang et al. 2023), so the spread of projections in Makelov et al.'s
  Figure 5 cannot carry a causal claim alone.
- **Against the factual-recall set-up (§4.4).** By the reply's reading of
  Makelov et al.'s code, one DAS direction is trained per fact pair and
  evaluated on that pair. That aligns the network with a trivial
  high-level model, "return the answer of the seen source example", and
  overfits.
- **Their IOI experiments (§5, Figures 2–7, App. C–D).**
  - Layer 8 block output at the last token: 70% IIA; layer 8 MLP
    activations: 4%; MLP input and output streams near 0% at every layer.
    "Our IIA scores suggest that MLP activations carry hardly any
    information about name position information."
  - In layer 8 the attention output reaches 48% IIA, and the block input
    11%; the attention block writes the variable.
  - No single layer-8 head carries it (0% IIA each). Leaving out heads 6
    and 10 costs most. Heads 6 and 10 together reach under 20%.
  - The IO name emerges at layer 9. Removing head 9.9 costs most, but no
    single head suffices; about 11 heads are needed.
  - Boundless DAS gives comparable results for position and better ones
    for the IO name (61% and 95–96% IIA at the best locations).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under Makelov et al.'s test, a direction they call faithful counts as illusory | weak | the toy computation of §3.2, which holds only for an unnormalized patch (checked here) |
| C2 | A faithful distributed direction need not be orthogonal to the null space of downstream weights | strong | the geometry of §3.3, shown in the toy |
| C3 | Interchange interventions on a fixed set of variables do not pick between alignments related by a change of basis | moderate | App. A, one constructed example; the generalization is conjectured |
| C4 | FLDD can be large with no behavioural change | strong | the arithmetic of §4.2 |
| C5 | The factual-recall "illusions" reflect per-pair DAS training | moderate | an argument from the released code, §4.4; not re-run |
| C6 | In GPT-2 Small, name position is written by the layer-8 attention block, distributed over heads, and MLP8 carries almost none | moderate | §5, IIA on one task |

## Concepts

- **Interchange intervention accuracy (IIA).** The share of interventions
  on which the network's output matches the high-level model's
  counterfactual output.
- **Data-induced submanifold.** The activations reachable from some input.
  Interchange interventions stay on it by construction; Makelov et al.'s
  dormant directions are off it.
- **Multiple abstraction.** Two structurally different alignments of one
  network, indistinguishable under the interventions performed.

## Connections

It answers [LIT-968](../literature.d/LIT-968.md) and an earlier blog version (Lange et al. 2023). It
rests on DAS (Geiger et al. 2023) and Boundless DAS (Wu et al. 2023), and
on the causal-abstraction framework, where indistinguishability of
alignments under a set of interventions is a standing theme. Its §4.3
draws on Huang et al. 2023, by an overlapping group. Huang et al. 2025
([LIT-987](../literature.d/LIT-987.md)), from the same group, takes up the predictive use of
DAS-located variables.

## Bearing on the record

- **[QUESTION-030](../questions.d/QUESTION-030.md).** The LIT was registered because the dispute "turns on
  whether an intervention finds the variable that constitutes a behaviour
  or one that only correlates with it". That is not what the dispute turns
  on. Both sides agree that the MLP8 direction has negligible interchange
  accuracy (4.2% there, 4% here) and that the residual-stream direction is
  the one the model uses. Neither speaks of constitution or of mere
  correlation. They disagree over three things: whether an effect that
  runs through components the next layer cannot read discredits a found
  subspace; which success measure to trust, FLDD or IIA; and how DAS should
  be trained and tested. What bears on [QUESTION-030](../questions.d/QUESTION-030.md) is a point both papers
  grant: interventions within one distribution can be satisfied by
  alignments that differ by a change of basis ([LIT-968](../literature.d/LIT-968.md) A.3; this paper,
  App. A). So an interventional result fixes a mediating variable only
  relative to a decomposition into units. That is filed as
  [THEORY-243](../theory.d/THEORY-243.md).
- **[CLAIM-150](../claims.d/CLAIM-150.md)** says that interventional success does not show
  constitution. App. A supports a stronger premise for the case of
  networks: success under a fixed set of interventions does not fix which
  variable mediates.
- **[CLAIM-130](../claims.d/CLAIM-130.md).** The reply's defence of IIA, interventions that stay
  on the data-induced submanifold, is the analogue of insisting that
  do(S = s) set S to values S can actually take. Makelov et al.'s dormant
  directions are reached only by leaving it.
- **[THEORY-282](../theory.d/THEORY-282.md)** (the illusion, filed from [LIT-968](../literature.d/LIT-968.md)) is not undercut.
  The reply contests the label and the toy, and it does not dispute that
  the MLP8 effect vanishes without the null-space component.
- No instruction for machine-learning practice is filed. The reply's
  advice on how to train and evaluate DAS (§4.4) is for the anthology.

## Limitations

- The central toy argument fails under the test as specified (above). The
  reply's correct general point, that faithful directions need not avoid
  the null space, does not by itself show that the rowspace test rejects
  them.
- The factual-recall critique is argued from code, not tested.
- Its experiments use IIA only, one task and one model.
- It reads low IIA as "no relevant structure", which is Makelov et al.'s
  conclusion about MLP8 too. So its experiments do not bear on whether a
  low-IIA, high-FLDD patch is benign.

## Open questions

- A real-model case where a direction that passes independent checks
  (written by the right components, read by the right components) fails
  the rowspace test would vindicate the reply's worry. None is given.
- Whether there is a principled basis, beyond component boundaries, for
  preferring one of several alignments that agree on every intervention
  performed.
