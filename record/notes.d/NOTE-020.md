---
number: 20
status: Read
formerly:
- NOTE-tmpmri7d
paper: LIT-027
title: 'Emergence as the conversion of information'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 2104.13368v1 (27 Apr 2021), 20 pp. —
    §§1–5.1, Table 1, Figs. 1–4 (rendered and inspected), and the
    references; nothing skipped. I did not see the supplementary Python
    code, which holds the exact splitting rule of the expansion method, and
    I did not read the published Phil. Trans. A version (403). Revisions
    made for publication, in particular to §5.1, are unverified.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Varley and Hoel apply a PID, with the Williams–Beer I_min redundancy, to
  past→future mutual information and summarise it with a new
  layer-weighted "synergy bias" B_syn ∈ [0,1]. Coarse-graining can raise
  B_syn at the macroscale. A macroscale XOR reaches 0.833, against 0.52
  for its NAND/AND/OR implementation. In 200 random 3-node "Gaussian" TPMs
  expanded into equivalence-class micro/mesoscales with *identical* MI,
  every macroscale had higher B_syn, by ≈ 0.01–0.07 (r = 0.819 against
  macroscale B_syn). In 185 near-deterministic systems the change was
  mostly negative, down to ≈ −0.1.
---


# NOTE-020: Emergence as the conversion of information

## Contribution

- A normalised, lattice-height-weighted summary of a PID, the **synergy bias** B_syn (Eq. 8), comparable across systems with different numbers of elements.
- The **expansion method** (§3.2, Fig. 3): generate microscales from a given macroscale by splitting a node into an equivalence class. This holds past→future MI fixed with zero inconsistency, in Klein & Hoel's sense.
- Numerical evidence that B_syn can differ between two exactly consistent descriptions of one system with equal MI. So coarse-graining can change the *type* of information and not only its amount.
- A proposal that this "information conversion" is the umbrella notion under which Hoel's earlier EI-based causal emergence also falls.

## Key insight

Total information cannot rise under dimension reduction, since MI can only fall or stay the same. Its *composition* across the redundancy–synergy lattice can still shift. A macroscale can therefore carry more of one kind of information, and reducing to the microscale would lose that kind, even though nothing is lost in total. On this view, macroscale science is useful for more than compression.

## Assumptions

- Discrete, Markovian Boolean networks given by a TPM.
- For closed networks, P(X) is the stationary distribution, using the largest attractor, or networks built so that all states lie in one attractor (§2). The logic-gate examples are open systems and use maximum-entropy inputs at both scales (§3.1). The EI of §4 instead uses an interventional P(X) = H_max (Eq. 10).
- PID with sources = past states of the individual elements and target = the *joint* future state (Eq. 7). This is the plain PID of TDMI, not ΦID.
- Redundancy function: Williams–Beer I_min (Eq. 6), chosen because it is non-negative, works for more than two sources and is widely used. The authors acknowledge its critiques (§2.1). All results are conditional on it. No other measure was tried.
- PI-lattice "layers" are defined as sets of atoms at equal height (§2.3). The paper does not specify precisely how height is counted for n = 4 and 5 lattices ("we claim that these atoms comprise a 'layer'").
- Expansion method: children of a split node form an equivalence class with "the same inputs and the same outputs". MI is exactly preserved and consistency is perfect. The precise splitting rule is in supplementary code I did not see. **If** the children behave as copies, part of the microscale's extra redundancy is put there by construction (unverified).
- Generated systems: 200 "positive-Gaussian" TPMs (8×8, |N(0,1)| entries, rows normalised, fully connected 3-node binary). 185 "deterministic" systems (one successor with probability 0.99, the rest spread evenly for ergodicity). Each is expanded to a 4-node "mesoscale" and a 5-node "microscale".

## Key results

- **Eq. 8, Eq. 9.** B_syn(S) = Σ_{i=0}^{|S|} (i/|S|)·S_i, where S_i is the fraction of MI in lattice layer i. B_red = 1 − B_syn.
- **Table 1 (§3.1), maximum-entropy inputs:**

  | gate | micro MI | macro MI | micro B_syn | macro B_syn |
  |---|---|---|---|---|
  | AND | 1.623 bit | 0.811 bit | 0.533 | 0.578 |
  | OR | 2.811 bit | 0.811 bit | 0.518 | 0.578 |
  | XOR | 2.5 bit | 1 bit | 0.52 | 0.833 |

  The XOR is implemented from one NAND, one AND and one OR. MI *falls* at the macroscale here, so these cases alone cannot separate conversion from loss. The authors say so (§3.2, first paragraph).
- **§3.2, Gaussian (Fig. 4 left).** In all 200 systems, B_syn is higher at the macroscale than at the micro/mesoscales, with MI unchanged. The gain correlates with macroscale B_syn at Pearson r = 0.819, p < 10⁻¹⁰. Read off the figure: macroscale B_syn ≈ 0.55–0.82, gain ≈ 0.005–0.07.
- **§3.2, deterministic (Fig. 4 right).** Lower B_syn overall (≈ 0.03–0.6). Systems with macroscale B_syn < 0.5 mostly *lose* synergy bias at the macroscale; change down to ≈ −0.1. Positive correlation between change and macroscale B_syn. By visual inspection both classes lie on "a common line of best fit". No fit is reported.
- **§4.** No new theorem. It restates EI(X;Y) = MI with P(X) = H_max (Eq. 10) and EI = determinism − degeneracy (Eqs. 11–13), and re-describes causal emergence as converting "causally-irrelevant information (like the uncertainty of state transitions)" into EI. It notes that EI cannot increase at a macroscale if determinism is maximal and degeneracy minimal, "because there is no information to convert".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A macroscale can have higher PID synergy bias than its microscale | moderate | computed examples (Table 1, Fig. 4), one redundancy function |
| C2 | This can happen with past→future MI identical at both scales, so it is conversion, not loss ("proving information conversion") | moderate as an existence claim; weak as a general claim | expansion method, 200 Gaussian systems; relies on I_min and on the splitting construction |
| C3 | For random stochastic systems, microscales hold more redundant information than macroscales | weak | one generator (|Gaussian| TPMs), 3-node macroscales, expansion of one node |
| C4 | The direction reverses for redundancy-biased deterministic macroscales | moderate | Fig. 4 right, 185 systems |
| C5 | Both classes lie on a common roughly linear relation of Δ B_syn against macroscale B_syn | weak | "visual examination" (Fig. 4 caption), no fit reported |
| C6 | EI-based causal emergence is a case of information conversion | informal argument | §4, re-description of Eqs. 11–13 |
| C7 | Information conversion is an "umbrella" theory unifying information-theoretic emergence | assertion | title, abstract, §5. Shown for MI+PID and argued for EI; not shown for integrated information or others |
| C8 | Special sciences / macroscale models are useful because they convert redundant into synergistic (and unique) information | assertion (stated as a hypothesis) | §5 |
| C9 | ΦID / IIT emergence is single-scale joint information flow with "an absence of any kind of macroscale vs. microscale comparison" | informal argument | §5.1; disputed by item 21 §IV C |
| C10 | Reduction is always possible under supervenience but can lose a measurable type of information; the view fits neither strong nor weak emergence | informal argument | §5.1 |

The abstract's "proving information conversion" and the title's "unifying theory" claim more than the body shows. The body shows an existence result under one PID measure in small generated systems, plus a re-description of EI.

## Method

1. Build the TPM, the input distribution (stationary, or maximum entropy for open gate networks) and the joint P(X,Y).
2. Compute a PID of I(X;Y) with the past elements as sources and the joint future as target (Eq. 7), using I_min, in the `dit` package.
3. Group the PI atoms into lattice layers by height. The spectrum S_i is the fraction of MI in layer i. Compute B_syn (Eq. 8).
4. Compare scales.
   - Logic gates: the macro gate against its micro gate network, with identical maximum-entropy inputs.
   - Expansion method: take a 3-node macroscale TPM, split one node into two equivalence-class children (4 nodes), split a child again (5 nodes), and recompute B_syn with MI and consistency fixed.

## Concepts

- **Information conversion** — a change in the composition of information (its distribution over PI-lattice atoms, or from transition uncertainty into EI) between two descriptions of one system, with total information not increasing.
- **Emergence (this paper)** — a macroscale having more of some *type* of information than its microscale. It is defined only relative to a micro/macro pair and can be absent or reversed.
- **PI spectrum S** — fraction of MI in each lattice layer.
- **Synergy bias B_syn / redundancy bias B_red** — normalised height-weighted mass of S (Eqs. 8–9).
- **Expansion method** — inverse coarse-graining that creates equivalence-class microscales with MI preserved and zero inconsistency.
- **Consistency** — macro dynamics and responses to interventions match the micro. Zero here by construction.
- **Effective information (EI)** — MI under a maximum-entropy intervention distribution, equal to determinism − degeneracy.
- **Causal emergence (Hoel)** — EI higher at a macroscale than at the microscale.

## Connections

**Relation to Rosas et al. 2020 (as stated in the paper).** Rosas et al. 2020 appears only in §5.1, cited together with Mediano et al. 2019 as the ΦID approach. The paper describes ΦID as starting, like its own method, from the decomposition of past–future MI, but building a "double PI lattice" of how information moves between atoms through time. It says ΦID defines "emergent" information as information that "remains synergistically present across the joint state of many elements through time", and "downward causation" as whole-state information constraining one element. It then argues that, as in IIT, "both of these are just joint information flow over sets of elements at a single scale", with no macro-versus-micro comparison. It concedes that such jointly acting sets "may be good candidates for macroscales". It does not discuss Rosas et al.'s supervenient-feature definition Un⁽ᵏ⁾(V_t;X_t′|X_t), their iff theorem, or their practical criteria. Rosas et al. 2020 is not in this record.

**Versus item 21 (Mediano et al., the ΦID review).**

- *Formal definitions.*
  - Here, emergence is a *cross-scale comparison*: B_syn(macro) > B_syn(micro) with MI held equal, or EI(macro) > EI(micro).
  - In item 21, a supervenient feature V_t is emergent of order k iff Un⁽ᵏ⁾(V_t;X_t′|X_t) > 0, and a system can host one iff Syn⁽ᵏ⁾(X_t;X_t′) > 0. That is a single-description property under a fixed partition, with "scale" meaning the order k.
- *What counts as emergent.*
  - Here, emergence is relative to a pair of descriptions and can run in either direction.
  - In item 21, any synergistic dynamics has emergence capacity, whatever coarse-graining is or is not performed.
- *Instruments.*
  - This paper uses the plain PID of TDMI with the joint future as one target (Eq. 7). Item 21 §II C calls that decomposition unable to "discriminate between the various ways in which the predictors affect different parts of the target", which is why ΦID was built.
  - This paper uses I_min. Item 21 leaves the redundancy function open and leans on redundancy-free sufficient criteria.
  - My inference: for two elements, item 21's emergence capacity Syn⁽¹⁾ is the top atom {12} of this paper's lattice, so B_syn at a given scale partly tracks item 21's quantity at that scale.
- *The exchange.* §5.1 here says ΦID lacks any macro–micro comparison. Item 21 §IV C cites this paper as [8] and calls that a "potential misunderstanding": ΦID is framed through supervenient macroscopic variables, and can also assess capacity "without the need to specify any particular macroscopic variable".
  - My reading: both are right about different things. ΦID does relate a macro variable to the micro parts. But it does not compare two complete models of the system at different resolutions, which is this paper's criterion (a) in §1.
- *Where they would disagree on a concrete system (my construction from what each states).*
  - (i) A deterministic permutation on two bits, (X¹,X²) → (X¹⊕X², X¹). §4 here says EI cannot increase at any macroscale when determinism is maximal and degeneracy minimal, so there is no causal emergence. Under item 21's theorem the system has emergence capacity whenever Syn⁽¹⁾ > 0. With the minimum-MI redundancy that is 1 bit, since Syn = Red when I(X;Y) = 2 and each I(Xⁱ;Y) = 1. With an identity-property redundancy it is 0, and then the two agree.
  - (ii) This paper's Gaussian expansion pairs. The macroscale counts as emergent here because B_syn rose between two consistent descriptions. Item 21 would treat splitting a node into equivalence-class children as a change of partition, under which its atoms are *expected* to change (item 21 §IV B, footnote 4). It would not count the change as emergence. It would ask instead whether, in the 5-node system, some supervenient V has unique predictive power beyond any ≤ k parts.
  - (iii) The XOR gate. This paper counts the macro XOR as more synergistic than the NAND/AND/OR network: B_syn rises from 0.52 to 0.833. Item 21's footnote 4 shows that the same XOR's 1 bit of synergy becomes 1 bit of unique information under the recoding (X₁⊕X₂, X₁). That is the change-of-description sensitivity this paper treats as the phenomenon, and that item 21 treats as a feature of mereology.
- *Timing.* This v1 (Apr 2021) predates item 21 (Nov 2021). Item 21 thanks Hoel and Varley for discussions. Both appeared in the same theme issue (editorial: [LIT-021](../literature.d/LIT-021.md)).

Other lineage named in the paper: Hoel et al. 2013 (EI causal emergence), Hoel 2017, Klein & Hoel 2020 (consistency/inconsistency measure; random walkers), Hoel et al. 2016 and Marshall et al. 2018 (φ across scales), Williams & Beer 2010 and Gutknecht et al. 2020 (PI lattice), Rubenstein et al. 2017 (causal consistency of SEMs).

## Bearing on the record

- In this record it is [LIT-027](../literature.d/LIT-027.md). Its summary is accurate, but it should add two things: that the effect is small (Δ B_syn ≲ 0.07) and reverses for redundancy-biased deterministic systems, and that it rests on a single redundancy function.
- It supports and contradicts no THEORY document in the Anthology of the SOTA.
- **Not the ML sense of "emergent".** ML "emergent capabilities" ([ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md); [ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md); [ANTH-THEORY-040](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-040.md); [ANTH-SOTA-200](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-200.md)) are abrupt task-performance onsets as model size or compute grows. This paper's emergence is a change in the redundancy/synergy composition of past→future information when one dynamical system is described at a coarser scale. The paper does not mention scaling, training or capability onset. Its only ML touches are in passing:
  - §2.2 notes that PID is often applied to sources such as "neurons, perceptrons" (citing Tax, Mediano & Shanahan 2017).
  - §5 lists "what level of abstraction is appropriate for modeling and comparing deep neural networks (Cao and Yamins, 2021)" as one place where identifying intrinsic scale matters.

  Neither is developed, and neither concerns emergent capabilities. Nothing here bears on [ANTH-SOTA-200](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-200.md) or [ANTH-THEORY-040](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-040.md). The paper carries no instruction for ML practice.

## Limitations

- One redundancy function (I_min), which the authors note is criticised. No robustness check is run. The authors themselves say (§2.1) that PID redundancy has no gold standard.
- Tiny systems: 3-node macroscales expanded to at most 5 nodes. Generated TPMs only, no real data. The effect size is small.
- The expansion construction may itself build redundancy into the microscale. Equivalence-class children share inputs and outputs, and whether they are copies could not be checked without the supplementary code. The logic-gate results mix conversion with MI loss.
- Conversion runs both ways (Fig. 4 right). "Macroscales convert redundant to synergistic" is class-dependent, not general.
- The "umbrella" claim is supported for MI+PID and re-described for EI. It is not demonstrated for integrated information or any other measure.
- It does not identify *which* information changes form. The authors say so (§5: "it remains to be understood exactly which information changes form").
- Internal errors: the Fig. 4 caption swaps its panels, §4 refers to a figure that does not exist, and §4 reverses the degeneracy limiting case. None changes the main result.

## Open questions

- Does the B_syn shift survive other redundancy functions (MMI, BROJA, I_ccs, I_sx) and ΦID's finer target decomposition?
- Does it appear for coarse-grainings of real data or learned macroscales, rather than for constructed equivalence-class expansions?
- At what scale does synergy peak? How can scales be found that maximise conversion while minimising MI loss? (The authors' own questions.)
- Can "conversion" be localised with pointwise or local PID? (The authors' own suggestion, via Finn & Lizier.)
- Do this cross-scale criterion and item 21's single-partition criterion ever pick out the same macroscale, and under what redundancy function?

## Corrections to the seeded skim

- The dossier's first line says Figs. 1–2 show logic-gate spectra. Fig. 1 shows two generic three-element PI lattices and spectra, one low-B_syn and one high-B_syn. Only Fig. 2 is the logic gates.
- The dossier says "every system gains synergy at the macroscale" for the Gaussian class. That is correct, but the dossier omits the size of the effect. On Fig. 4 the Gaussian gain in B_syn is ≈ 0.005–0.07, on a scale from 0 to 1.
- The dossier says deterministic systems "often lose" synergy at the macroscale. That understates it. On Fig. 4 (right panel), nearly all deterministic systems with macroscale B_syn < 0.5 have a negative change, i.e. their microscale is *more* synergy-biased. The redundant→synergistic conversion that is the paper's headline therefore holds for one generated class, not in general. The paper does report this (§3.2, Fig. 4 caption), but the abstract and title do not.
- An internal inconsistency the dossier did not catch: the Fig. 4 caption swaps Left and Right. The text (§3.2) and the rendered figure agree that the left panel is Gaussian-only (r = 0.819) and the right panel is Gaussian + deterministic. The caption says the reverse. Separately, §4 cites "Figure 4 (left)" as showing a decrease in transition uncertainty. No figure shows that.
- A second internal error: §4 says that if every state has a unique transition, the entropy term H(⟨p(y)|P(X)=H_max⟩) "is zero, and degeneracy maximal". By the paper's own Eq. 13 it is the reverse: that term is log₂N and degeneracy is zero.
- The dossier says the Discussion "hypothesizes the special sciences … convert redundant into synergistic information". Correct. The paper also calls its Gaussian result a "proof" (abstract; §3.2, "This is proof that dimensionality reductions exist…"). That is sound only as an existence claim, shown numerically under one redundancy function.
