---
number: 45
status: Read
formerly:
- NOTE-tmpbu012
paper: LIT-042
title: 'Gutknecht et al. 2025, Shannon invariants'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 2504.15779v1 (22 Apr 2025; the only
    version on arXiv as of 2026-09-26), 16 pp. Read: §I–§V, Figs. 1–4
    (captions; the plotted curves came through only as labels), Tables
    I–III, Appendix A (PID primer), Appendix B (Props. 5–6, Cors. 3–5),
    Appendix C (network details) and references [1]–[64]. Nothing skipped.
    PDF from arxiv.org/pdf/2504.15779, extracted with PyMuPDF to
    raw4/2504.15779.txt. I checked the combinatorial proofs of Props. 1–4
    and 6 by hand against the consistency equations (A7)–(A8). I did not see
    the nninfo code, and the estimation pipeline is described only in App.
    C.). Upgraded from `Skimmed` to `Read`: the claims table, assumptions
    and results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  For any set of quantities Π(α) satisfying the PID consistency equation
  (A7), whatever the redundancy measure, two averages are fixed by Shannon
  quantities alone. They are the average degree of redundancy, r̄ = Σᵢ
  I(Xᵢ;Y)/I(X;Y) (Prop. 1), and the average degree of vulnerability, v̄ =
  Σⱼ I(Xⱼ;Y|X₋ⱼ)/I(X;Y) (Prop. 2). Two identities follow: RSI = (r̄ −
  1)·I(X;Y) (Cor. 1), and a new "dual" index DRSI = I(X;Y) − Σⱼ
  I(Xⱼ;Y|X₋ⱼ) = (1 − v̄)·I(X;Y) (Prop. 4, Cor. 2). In small,
  stochastically quantised (8-level) networks analysed on their own
  training set, r̄ about the label rises with depth and v̄ falls with
  depth and training. In a face autoencoder, decoder layers are more
  redundant than size-matched encoder layers, and r̄ rises with bottleneck
  width.
---

# NOTE-045: Gutknecht et al. 2025, Shannon invariants

## Contribution

Partial information decomposition (PID) has two problems:
- it has no agreed redundancy measure;
- its lattice of atoms grows super-exponentially in n.

This paper identifies linear combinations of atoms, called **Shannon invariants**, that every PID satisfying the consistency equation must give the same value. It exhibits two with a clear meaning: the average number of single sources an atom can be read from (r̄), and the average number of sources an atom critically depends on (v̄). These settle what the redundancy–synergy index (Chechik et al. 2002) measures for n > 2 sources, and they introduce its dual (DRSI). The paper also shows the averages can be computed for layers of small quantised networks.

## Key insight

Borrowing the statistical-mechanics habit of measuring averages without resolving microstates: the atoms are unknowable individually, but the counting argument is not. Each I(Xᵢ;Y) contains exactly the atoms reachable from source i, so Σᵢ I(Xᵢ;Y) counts each atom as many times as the number of single sources it is reachable from. Similarly, each I(Xⱼ;Y|X₋ⱼ) contains exactly the atoms that need source j, so Σⱼ I(Xⱼ;Y|X₋ⱼ) counts each atom by the number of sources it cannot do without. Normalising by I(X;Y) turns both counts into averages that no choice of redundancy measure can change.

## Assumptions

- **PID consistency (A7):** I(a;Y) = Σ_{α : ∃b⊆a, b∈α} Π(α) for every source subset a. Equivalently, via the chain rule, (A8) for conditional informations. This is the only structural assumption behind Props. 1–4.
- I(X;Y) > 0. Otherwise r̄ and v̄ are undefined (p. 3).
- **Non-negativity of atoms**, which only some PID measures satisfy. It is needed for the average-degree interpretation, for Prop. 3's reading "RSI > 0 ⇒ some redundancy exists", and for everything in App. B.
- Discrete variables with a known joint pmf. In §IV:
  - activations are stochastically quantised to 8 levels (App. C) so that information is finite and the network is not injective;
  - the pmf is the empirical distribution over the training set, with every training example given equal probability.
- Targets: the class label (MNIST) or the input image itself (autoencoder).
- Single target, static setting. There is no time-directed (ΦID-style) decomposition.

## Key results

- **Prop. 1.** r̄ := Σ_k k·Σ_{r(α)=k} Π(α)/I(X;Y) = Σᵢ I(Xᵢ;Y)/I(X;Y), where r(α) = |{i : {i} ∈ α}|.
- **Prop. 2.** v̄ := Σ_j j·Σ_{v(α)=j} Π(α)/I(X;Y) = Σⱼ I(Xⱼ;Y|X₋ⱼ)/I(X;Y), where v(α) = |{i : ∀a∈α, i∈a}|.
- **§II D (logical relations).**
  - Atoms with r > 1 are a subset of atoms with v = 0: source-level redundancy implies robustness.
  - Atoms with v > 1 are a subset of atoms with r = 0.
  - Hence, for non-negative atoms, I_v^{(0)} ≥ Σ_{k≥2} I_r^{(k)} (Eq. 14) and I_r^{(0)} ≥ Σ_{k≥2} I_v^{(k)} (Eq. 15).
  - The two notions coincide only at n = 2.
- **Prop. 3 / Cor. 1.** RSI = Σ_{k=2}^n (k−1)·I_r^{(k)} − I_r^{(0)} = (r̄ − 1)·I(X;Y).
  - For n = 2 this reduces to Π({1}{2}) − Π({1,2}), the interaction information (Eq. 3).
  - For n = 3: RSI = 2Π({1}{2}{3}) + Π({1}{2}) + Π({1}{3}) + Π({2}{3}) − I_r^{(0)} (Eq. 20).
- **Prop. 4 / Cor. 2.** DRSI := I_v^{(0)} − Σ_{k≥2}(k−1)·I_v^{(k)} = I(X;Y) − Σⱼ I(Xⱼ;Y|X₋ⱼ) = (1 − v̄)·I(X;Y).
- **App. B.** These assume non-negative atoms.
  - Prop. 5: I_r^{(0)}/I ≥ 1 − r̄ and I_v^{(0)}/I ≥ 1 − v̄. So r̄ < 1 implies some synergy, and r̄ < ½ implies synergy predominates.
  - Prop. 6: Σ_{k≥2} I_r^{(k)}/I ≥ (r̄−1)/(n−1). So r̄ > 1 implies some proper redundancy, and r̄ > (n+1)/2 implies redundancy predominates. The same holds for v̄.
- **MNIST (Fig. 2).**
  - r̄ about the label jumps in the first epoch. It then roughly plateaus in L3 and L4, keeps rising in L5, and is higher in later equal-width layers.
  - v̄ falls over training and is smaller in later layers.
  - Median over 10 seeds, with min–max bands.
- **Face autoencoder (Fig. 3).**
  - At n_b = 128, r̄ rises within the first epoch in all layers but the first encoder layer, and decoder layers exceed size-matched encoder layers. v̄ ≈ 0 throughout.
  - At n_b = 12–20, the bottleneck's r̄ converges more slowly and is ordered by width (smaller width, smaller r̄).
  - v̄ spikes to ≈ 1 early, which the authors attribute to total information below one bit, then falls, ordered with the largest bottleneck least vulnerable.
  - Final test MSE 9.5(1)×10⁻³ at n_b = 128 (Table III).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | r̄ and v̄ are Shannon invariants, i.e. the same under every PID satisfying (A7) | strong | proof, Props. 1–2 (counting over (A7)/(A8)) |
| C2 | RSI = (r̄ − 1)·I(X;Y), and RSI over-weights higher-order redundancy relative to synergy for n ≥ 3 | strong | proof, Prop. 3, Cor. 1 |
| C3 | DRSI = I(X;Y) − Σⱼ I(Xⱼ;Y|X₋ⱼ) = (1 − v̄)·I(X;Y) | strong | proof, Prop. 4, Cor. 2 |
| C4 | With non-negative atoms, thresholds on r̄ and v̄ bound the fractions of synergy, redundancy and vulnerability | strong (Props. 5–6) / weak (Cor. 5) | proofs in App. B; Cor. 5 is stated as ⇔ but only ⇐ follows |
| C5 | The framework "resolves" the scalability problem of PID | weak | the number of terms is linear in n (§V); estimating each term is not addressed and is bypassed by the population-equals-training-set device |
| C6 | In a quantised MNIST MLP, redundancy about the label rises with depth and vulnerability falls with depth and training | moderate | experiment, Fig. 2; 10 seeds, one tiny architecture (5-unit layers), computed on the training set only |
| C7 | Decoder layers are more redundant than size-matched encoder layers; r̄ rises and v̄ falls with bottleneck width | moderate | experiment, Fig. 3; 10 seeds per width, one architecture, training set only |
| C8 | Redundant encodings may be preferred because they are robust and aid generalization | weak | conjecture, §IV B; not tested |
| C9 | "When little information is encoded in a large layer, the encoding tends to be more redundant; … more vulnerable the closer to capacity" | weak | informal generalisation from C6–C7 (§V) |

## Method

The paper introduces no new algorithm. Computing the invariants takes three steps:
1. Estimate I(Xᵢ;Y), I(X;Y) and I(Xⱼ;Y|X₋ⱼ) by Shannon entropies.
2. Form r̄, v̄, RSI and DRSI.
3. For networks, use the nninfo package (Ehrlich et al., TMLR 2023):
   - each activation is quantised stochastically to one of the two nearest of 8 equally spaced levels in [σ_min, σ_max] (App. C formula);
   - the full pmf of a layer's quantised activations is built over the training set;
   - entropies are computed exactly on that pmf.

## Concepts

- **Information atom Π(α)** — α is an antichain of source subsets. Π(α) is the information about Y obtainable iff one knows all sources of at least one set in α.
- **Shannon invariant** — a linear combination of atoms computable from Shannon entropies alone (Def. 1).
- **Degree of redundancy r(α)** — the number of single sources from which the atom is accessible. r = 0 is source-level synergy, and only r > 1 is "genuine" redundancy.
- **Degree of vulnerability v(α)** — the number of sources contained in every set of α, i.e. the sources whose loss makes the atom inaccessible. v = 0 is robust, and v ≥ 1 is already vulnerable.
- **I_r^{(k)}, I_v^{(k)}** — the total information at redundancy degree k, or vulnerability degree k.
- **RSI / DRSI** — RSI = Σᵢ I(Xᵢ;Y) − I(X;Y). DRSI = I(X;Y) − Σⱼ I(Xⱼ;Y|X₋ⱼ).

## Connections

- **Builds on:**
  - Williams–Beer (2010) PID;
  - the authors' own atom-first ("parthood/containment") formulation, Gutknecht, Wibral & Makkeh (2021, 2025);
  - Chechik et al. (2002) RSI;
  - Ehrlich et al. (2023) quantised-network information analysis;
  - Goldfeld et al. (2019) and Geiger (2021) on why deterministic networks need noise or quantisation.
- **Relation to the emergence readings in this record.** The paper itself cites Varley & Hoel 2022 ([48], [LIT-027](../literature.d/LIT-027.md)) as another construction of "an average degree of information atoms".
  - **[LIT-027](../literature.d/LIT-027.md) (Varley & Hoel, read in reads/22.md).**
    - Their synergy bias B_syn is a lattice-layer-weighted average of the PID spectrum computed with the Williams–Beer I_min redundancy. So its value depends on that redundancy choice.
    - r̄ is the redundancy-measure-free analogue: it weights atoms by how many single sources reach them, not by lattice layer, and needs no I_min.
    - A direct consequence for [LIT-027](../literature.d/LIT-027.md): its headline, that coarse-graining raises B_syn (e.g. XOR 0.52 → 0.833), is a statement about one redundancy function. The Shannon-invariant question, whether r̄ or v̄ of past→future information changes under coarse-graining, is computable from entropies alone, and neither paper asks it. That is an open check, not a finding.
  - **[LIT-025](../literature.d/LIT-025.md) (Mediano, Rosas et al., read in reads/21.md).**
    - The ΦID emergence criteria are stated there as Syn⁽ᵏ⁾ > 0, and the review points to redundancy-free "practical criteria" in Rosas et al. 2020 without stating them.
    - This paper shares authors with [LIT-025](../literature.d/LIT-025.md) (Rosas, Mediano). It gives the general principle that such practical criteria instantiate: Shannon quantities that bound, rather than resolve, the synergistic part.
      - Prop. 5 shows r̄ < 1 forces source-level synergy.
      - For past→future information with the parts as sources, that is a redundancy-free sufficient witness of information in no single part.
    - But this paper's setting is single-target and static. It does not decompose the target side as ΦID does (16 atoms at n = 2), and it treats neither Syn⁽ᵏ⁾ for k > 1, nor downward causation, nor causal decoupling.
    - So it does not by itself supply [LIT-025](../literature.d/LIT-025.md)'s missing criteria. Whether Rosas et al.'s Ψ is exactly an r̄-type invariant is unverified here.
  - It also bears on the dispute between [LIT-025](../literature.d/LIT-025.md) and [LIT-027](../literature.d/LIT-027.md) (reads/21.md corrections: §IV C of the review answers Varley & Hoel). Both sides' quantitative claims could be recast in Shannon-invariant form, removing the redundancy-function dependence from the disagreement. The paper does not do this.

## Bearing on the record

- **For this record.**
  - It supplies a measure-independent vocabulary (r̄, v̄, RSI, DRSI) against which the PID-dependent claims in [LIT-025](../literature.d/LIT-025.md) and [LIT-027](../literature.d/LIT-027.md) can be checked.
  - It should prompt a THEORY-level caution: any synergy/redundancy claim made with a specific redundancy function should state whether its sign survives under the Shannon invariants.
- **For the Anthology of the SOTA (boundary).**
  - It carries no instruction for ML practice. The network analyses are interpretability demonstrations on toy, quantised models evaluated on their training sets.
  - Its methodology is consistent with [ANTH-SOTA-312](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-312.md) ("state the noise or binning assumption behind any mutual information you report for a deterministic network…"): it quantises during training and evaluation, citing Goldfeld et al. and Geiger.
  - It sits next to the information-plane dispute ([ANTH-THEORY-058](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-058.md); [ANTH-LIT-507](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-507.md), [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md)).
  - If the anthology ever files a practice on multivariate information measures for representations, "report the RSI as (r̄ − 1)·I and do not read it as redundancy minus synergy for n > 2" would be the citable instruction. As it stands, it is not an anthology document.

## Limitations

- **Scalability.** The number of Shannon terms is linear in n, but each term (the joint I(X;Y), each I(Xⱼ;Y|X₋ⱼ)) needs a high-dimensional entropy.
  - The paper avoids estimation by computing on the training set as the population. This bounds every information by log(#training examples) and says nothing about out-of-sample encoding.
  - The authors flag estimation as future work (§V, refs. [62]–[64]).
- **Experimental scope.**
  - The networks are tiny: equal-width 5-neuron MNIST layers, and a 32×32 LFW autoencoder.
  - They are quantised to 8 levels.
  - There is one architecture per task and no comparison with any other PID or information measure.
- The average-degree interpretation and every bound in App. B require non-negative atoms, which several PID measures violate.
- r̄ does not distinguish orders of synergy, and v̄ does not distinguish orders of robustness (pp. 3–4). Each is a one-sided lens.
- Corollary 5 overstates Prop. 6 (⇔ for ⇐), and the index ranges in Cor. 4 item 4 and B10–B11 are inconsistent with Prop. 6.
- The generalization conjecture (C8) is untested.

## Open questions

- Are there other Shannon invariants with a clear meaning (the "landscape" the authors propose)? Which linear functionals of the atoms are fixed by (A7) alone?
- Do the depth and training trends of r̄ and v̄ survive in realistic networks with a principled estimator on held-out data? A replication on a standard-size model with bias-corrected estimators would settle this.
- Is r̄ or v̄ of past→future information monotone under coarse-graining? That is a measure-free version of [LIT-027](../literature.d/LIT-027.md)'s question.
- Can the ΦID emergence criteria of [LIT-025](../literature.d/LIT-025.md) be written as Shannon invariants on the double (source × target) lattice?

## Corrections to the seeded skim

- The dossier says the RSI is "closely tied" to average redundancy. The exact relation is an identity: RSI(X;Y) = Σᵢ I(Xᵢ;Y) − I(X;Y) = (r̄ − 1)·I(X;Y) (Cor. 1). The finer decomposition is RSI = Σ_{k≥2}(k−1)·I_r^{(k)} − I_r^{(0)} (Prop. 3). This shows that for n ≥ 3 the RSI weights a k-way redundancy k−1 times but counts synergy once. That asymmetry is the paper's actual finding about RSI.
- The dossier says the averages are "well defined" under unstated conditions. Props. 1–2 need only the consistency equation (A7) and I(X;Y) > 0. They do not need non-negative atoms.
  - Non-negativity enters only in reading r̄ and v̄ as averages of degrees and in the bounds of App. B (Props. 5–6, Cors. 3–5).
  - The text's claim that r̄, v̄ ∈ [0, n] "see Appendix B" (pp. 3–4) is not shown in App. B. It is true directly from Shannon inequalities, since I(Xᵢ;Y) ≤ I(X;Y) and I(Xⱼ;Y|X₋ⱼ) ≤ I(X;Y), so the pointer is wrong but the claim holds.
- An error the dossier could not see: **Corollary 5 (App. B, Eqs. B10–B11) is stated as an equivalence ("⇔") but only one direction follows from Prop. 6.**
  - Prop. 6 gives a lower bound: the fraction of redundancy of degree ≥ 2 is at least (r̄ − 1)/(n − 1). So r̄ > 1 + λ(n − 1) is sufficient for that fraction to exceed λ. It is not necessary. Counterexample: put a fraction λ′ slightly above λ at degree 2 and the rest at degree 1. The degree-≥2 fraction then exceeds λ, but r̄ = 1 + λ′, which is below 1 + λ(n − 1) whenever n > 2 and λ′ < λ(n − 1).
  - The sums in B10–B11 (and in Cor. 4 item 4) also start at k = 1 where Prop. 6 has k = 2. I read these as typos.
  - Cor. 4 items 2 and 4 ("r̄ > (n+1)/2 ⇒ redundancy predominant") are correct as sufficient conditions.
- The dossier's "the measures need a number of entropies that is linear in the number of sources" is what the paper says (§V), but it describes the number of terms, not the cost of estimating them.
  - r̄ needs the n single-source informations plus the joint I(X;Y). v̄ needs n conditional informations, each involving the (n−1)-source joint.
  - So each term still requires an entropy of a high-dimensional joint, which in general cannot be estimated from samples.
  - The paper sidesteps estimation entirely by treating the training set as the whole population (§IV A, p. 8). That is a change of question, which the authors state ("how it learns to encode this particular training dataset"). It is not a scalable estimator.
- The dossier describes the MNIST network as an "MLP (95.5% test accuracy)". The details are:
  - five fully connected tanh hidden layers, three of them of equal width 5 (Fig. 2a), activations stochastically quantised to 8 levels during training and evaluation;
  - trained 10⁴ epochs with plain SGD at learning rate 0.01, 10 seeds;
  - train accuracy 99.89(3)%.

  The autoencoder is a 3-conv/3-transpose-conv tanh network on LFW resized to 32×32×3 and augmented ×10, trained 10³ epochs with Adam at 0.001, bottleneck n_b ∈ {128, 20, 16, 12}. For n_b = 128 the degree of vulnerability is "zero up to numerical error" in all layers (Fig. 3 caption).
- The dossier says the Discussion conjectures redundancy helps generalization. It does, as an explicit conjecture ("We conjecture…", §IV B, p. 9), and nothing in the paper tests it.
