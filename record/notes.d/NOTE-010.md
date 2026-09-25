---
number: 10
status: Read
formerly:
- NOTE-tmpbpcaw
paper: LIT-025
title: 'Greater than the parts'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 2111.06518v1 (12 Nov 2021), 8 pp. —
    §§I–VI, Figs. 1–2, all five footnotes, the reference list; nothing
    skipped. I did not read the published Phil. Trans. A version
    (royalsocietypublishing.org 403), so any changes made in revision are
    unverified. I also did not read the primary source it restates (Rosas et
    al. 2020, "Reconciling emergences", PLoS Comput Biol 16:e1008289); every
    statement below about that paper is the review's own account of it.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  A review, with no new theorem, of the ΦID theory of causal emergence. A
  supervenient feature V_t is k-th-order causally emergent iff Un⁽ᵏ⁾(V_t;
  X_t′ | X_t) > 0. A system hosts such features iff Syn⁽ᵏ⁾(X_t; X_t′) > 0
  (cited as Rosas et al. 2020, Theorem 1), and Syn⁽ᵏ⁾ = D⁽ᵏ⁾ + G⁽ᵏ⁾
  (downward causation plus causal decoupling). The review's own additions
  are interpretive: the formalism is neutral between Granger and Pearl,
  coordinate dependence is defended as a feature, and it rebuts the charge
  that the theory makes no macro-versus-micro comparison.
---

<!-- inactive-ok-file: LIT-021 — Deferred, the theme issue's editorial, named in Connections for context; not yet read closely -->

# NOTE-010: Greater than the parts

## Contribution

The paper contributes no new result. It is a compact, readable restatement of the Rosas et al. (2020) theory of "mereological" causal emergence, which is built on Partial Information Decomposition (PID; Williams & Beer 2010) and its dynamical refinement, Integrated Information Decomposition (ΦID; Mediano et al. 2019). It adds three interpretive positions the primary paper is not cited for here:
- the measures are neither Granger- nor Pearl-causal in themselves;
- non-invariance under a change of coordinates is intended;
- the theory does compare macro with micro, through supervenient variables.

It then surveys applications: the Game of Life, a flocking model, macaque ECoG, and human fMRI.

## Key insight

Emergence is read as a part-whole relation stretched across time. A macroscopic feature V_t is a (possibly noisy) function of the present microstate, so it is instantaneously supervenient and carries nothing about the future that X_t lacks jointly. It can nonetheless predict the system's future in a way that no individual part, or small group of parts, can on its own. Supervenience and irreducible predictive power stop being paradoxical once one is instantaneous and the other is across time (§III). Whether a system can host any such feature at all is then a property of its dynamics alone, its "emergence capacity" Syn⁽ᵏ⁾(X_t; X_t′), and needs no candidate V to be named.

## Assumptions

- A fixed partition of the system into n parts, X_t = (X¹_t, …, Xⁿ_t). Every quantity depends on it (§IV B). Footnote 4 gives the example of XOR with (Z₁,Z₂) = (X₁⊕X₂, X₁), where Syn(X₁,X₂;Y) = 1 bit becomes Un(Z₁;Y|Z₂) = 1 bit.
- Supervenience is operationalised as V_t being a (possibly noisy) function of X_t (§III).
- A joint distribution p(X_t, X_t′) exists and is known or estimated. "All the quantities … depend only on the joint probability distribution p(X_t′, X_t)" (§IV A).
- A choice of redundancy function is required for Syn⁽ᵏ⁾, D⁽ᵏ⁾, G⁽ᵏ⁾ and Un⁽ᵏ⁾ (footnote 2). The review does not say which one the cited applications use. The practical criteria are redundancy-free but, in the review's words, only "sufficient".
- For an interventionist reading: p(X_t′|X_t) must equal a do()-distribution, and the system must satisfy faithfulness and the causal Markov condition (footnote 3). Otherwise the reading is predictive, i.e. Granger-type.
- "Under relatively general assumptions [7]": the conditions of the iff theorem are not stated in the review.

## Key results

All are restated from [7] (Rosas et al. 2020) or [26]. None is proved here.

- **Def. (Eq. 3).** V_t is causally emergent of order k iff Un⁽ᵏ⁾(V_t; X_t′ | X_t) > 0. This is information about X_t′ that V_t has and that no subset of ≤ k parts of X_t has on its own. By footnote 1 (= [7, Lemma 2]), I(Xⁿ;Y) = Red⁽ᵏ⁾ + Syn⁽ᵏ⁾ + Σ_{β∈B_k} Un⁽ᵏ⁾(X^β; Y | X^{−β}), with B_k the subsets of cardinality ≤ k.
- **Theorem ([7, Thm 1], restated §III).** X_t has causally emergent features of order k iff Syn⁽ᵏ⁾(X_t; X_t′) > 0. Syn⁽ᵏ⁾ is the information about the future carried by the whole and by no set of ≤ k parts taken separately.
- **Downward causation.** V_t exhibits it at order k iff Un⁽ᵏ⁾(V_t; X^α_t′ | X_t) > 0 for some set α of k parts. A system has such features iff D⁽ᵏ⁾(X_t; X_t′) > 0.
- **Causal decoupling.** V_t exhibits it at order k iff Un⁽ᵏ⁾(V_t; V_t′ | X_t, X_t′) > 0. This is "persistent synergy" of a macro variable predicting itself beyond the micro. A system has such features iff G⁽ᵏ⁾(X_t; X_t′) > 0.
- **Eq. 4.** Syn⁽ᵏ⁾(X_t;X_t′) = D⁽ᵏ⁾(X_t;X_t′) + G⁽ᵏ⁾(X_t;X_t′). The review calls this exhaustive. Fig. 1 marks the D⁽¹⁾ and G⁽¹⁾ atoms on the 16-atom two-source ΦID lattice.
- **Monotonicity in k (§IV C).** A k-th-order emergent feature is emergent at every order j < k. Being k-th-order emergent implies predictive information in interactions of order ≥ k+1.
- **Applications (§V).**
  - Game of Life particle collider: particles are causally emergent by the practical criteria, and "further analyses suggested" they may be causally decoupled.
  - Flocking: the centre of mass predicts its own dynamics beyond the individual birds.
  - Macaque ECoG + motion capture: the motion-related signal is emergent.
  - Human fMRI [33]: a gradient from redundancy-dominated sensory/motor regions to synergy-dominated association cortex. Synergy (G⁽¹⁾ over pairs of regions) is higher in humans than in macaques.
  - fMRI after brain injury [34]: loss of consciousness goes with reduced integrated information and reduced causal emergence.
  - No numbers are reported for any application in this review.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A system has k-th-order causally emergent features iff Syn⁽ᵏ⁾(X_t;X_t′) > 0 | strong in the source, assertion here | proof in Rosas et al. 2020 Thm 1; restated, not proved (§III) |
| C2 | Emergence capacity decomposes exactly and exhaustively as Syn⁽ᵏ⁾ = D⁽ᵏ⁾ + G⁽ᵏ⁾ | assertion here | Eq. 4, attributed to "further derivations" in [7]/[26] |
| C3 | Redundancy-function-free sufficient criteria for emergence exist, use only low-order marginals, and avoid the curse of dimensionality | assertion here | §III, last paragraph; criteria not stated, deferred to [7] |
| C4 | The quantities are neither Granger nor Pearl in themselves; they are interventional if p(X_t′|X_t) is a do()-distribution and faithfulness and causal Markov hold, and predictive otherwise | informal argument | §IV A |
| C5 | If all relevant variables are measured, Granger- and Pearl-type analyses coincide | assertion | §IV A; no citation, no statement of conditions |
| C6 | Lack of invariance under a change of coordinates is a feature of a mereological theory, not a bug | informal (philosophical) argument | §IV B, appeal to Jaynes's epistemic probability |
| C7 | The theory does compare macro with micro, via supervenient V, and dynamical synergy enabling emergent V is "not an assumption, but a consequence" | informal argument | §IV C, rebutting [8] = item 22 |
| C8 | GoL particles and a flock's centre of mass are causally emergent | experiment (in [7]) | §V A; results summarised, no values given here |
| C9 | Synergy (G⁽¹⁾, pairwise) rises along the human cortical hierarchy, is higher in humans than in macaques, and may support abstract reasoning | experiment for the first two (in [33], a bioRxiv preprint at the time); speculation for the third | §V B |
| C10 | Loss of consciousness after brain injury goes with reduced integrated information and causal emergence | experiment (in [34], bioRxiv at the time) | §V B |

The most citable line, the abstract's "we … extend a recent formal theory", claims more than the body delivers. No formal extension appears.

## Method

(Survey. The only "method" is the definitional chain PID → ΦID → Un⁽ᵏ⁾, Syn⁽ᵏ⁾, D⁽ᵏ⁾, G⁽ᵏ⁾ described above. The practical estimators are not given.)

## Concepts

- **PID** — Red, Un, Syn atoms of I(X₁,X₂;Y) (Eq. 2). Two eyes: colour is redundant, stereoscopic depth is synergistic.
- **ΦID** — decomposes TDMI I(X_t;X_t′) using atoms defined over both sources and targets. With two parts there are 4×4 = 16 atoms, e.g. Red→Syn. It exists because the PID of TDMI with the joint future as one target "cannot discriminate between the various ways in which the predictors affect different parts of the target" (§II C).
- **Supervenient feature** — V_t, a possibly noisy function of X_t.
- **k-th-order causal emergence** — Un⁽ᵏ⁾(V_t;X_t′|X_t) > 0.
- **Emergence capacity** — Syn⁽ᵏ⁾(X_t;X_t′).
- **Downward causation** — D⁽ᵏ⁾: the emergent feature predicts specific parts (≤ k of them).
- **Causal decoupling** — G⁽ᵏ⁾: the emergent feature predicts itself or the whole, beyond the parts, as "persistent synergies".
- **Order k** — the paper's dial for the "scale" of emergence (§IV C). Scale here means the size of the part-groups excluded, not a coarse-graining.
- **Mereological** — emergence as a property of part-whole relations under a *given* partition.

## Connections

**Relation to Rosas et al. 2020 (as stated in the paper).** The review is explicitly a summary of [7]: "an overview of a recently proposed formal theory of causal emergence [7]" (§I). The definitions, the iff theorem ([7, Theorem 1]), the k-th-order PID lemma ([7, Lemma 2], footnote 1), the D/G split, the practical criteria, and the GoL, flocking and macaque results are all attributed to [7]. [26] (Mediano et al. 2019, "Beyond integrated information") is credited with the ΦID lattice. What the review adds is interpretation (§IV) plus a survey of later brain applications ([33], [34]). A reader who needs the conditions of the theorem or the form of the practical criteria must go to [7]. Rosas et al. 2020 is not in this record.

**Versus item 22 (Varley & Hoel, "Emergence as the conversion of information").** The two papers define different things under the same word.

- *Formal object.*
  - Here, emergence belongs to a supervenient variable V_t relative to a fixed partition of one system, via Un⁽ᵏ⁾(V_t;X_t′|X_t) > 0. Emergence capacity belongs to the system's dynamics alone, via Syn⁽ᵏ⁾(X_t;X_t′) > 0.
  - In item 22, emergence belongs to a *pair of descriptions*, a microscale and a dimension-reduced macroscale of the same system. It is a change in the *type* of information between them, measured as a rise in the PID "synergy bias" B_syn (item 22, Eq. 8) of past→future mutual information at the macroscale, or as a rise in effective information (EI = determinism − degeneracy, item 22 Eqs. 10–13).
- *What counts as emergent.*
  - Here: any system whose dynamics carry synergy about their own future, at a single level of description, with no coarse-graining needed. Emergence is monotone in k, and "scale" is the order k.
  - In item 22: a macroscale counts only relative to a microscale it is compared against. The effect can run backwards — some macroscales are more redundant than their microscales (item 22 §3.1, and its deterministic systems in Fig. 4).
- *The explicit exchange.* Item 22 §5.1 says ΦID's "emergent" and "downward causation" quantities "are just joint information flow over sets of elements at a single scale, and there is an absence of any kind of macroscale vs. microscale comparison". This review names that reading a "potential misunderstanding", citing item 22 as [8] (§IV C). Its reply is that the theory is stated in terms of supervenient macroscopic variables. It adds that being able to assess a system's capacity for emergence "without the need to specify any particular macroscopic variable" is an advantage.
- *Both are partly right on their own terms (my reading).* ΦID does compare a macro variable with the micro parts. But it compares *predictive* information in one description, and never compares two complete models of the system at different resolutions, which is item 22's criterion (a) in its §1.
- *Shared ingredient (my inference from both texts).* Item 22's decomposition (its Eq. 7) is exactly the PID of TDMI with the joint future as a single target. This review (§II C) calls that decomposition too coarse, and that coarseness is why ΦID exists. For n = 2 and k = 1, the review's emergence capacity Syn⁽¹⁾(X_t;X_t′) is the top atom {12} of the lattice item 22 summarises with B_syn, under the same redundancy function. So item 22's macroscale B_syn is a layer-weighted, normalised summary that includes this review's emergence capacity at that scale. Item 22's emergence is then roughly *the increase of a synergy summary across scales*, while this review's is *the presence of synergy (of the right ΦID type) at one scale*. The redundancy functions also differ: item 22 uses Williams–Beer I_min, and this review names none.
- *Where they would disagree on a concrete system (my construction from what each paper states).*
  - (i) Take the two-bit system (X¹,X²) → (X¹⊕X², X¹) with uniform inputs. It is a deterministic permutation, so determinism is maximal and degeneracy minimal. Item 22 §4 states that EI "cannot increase at a macroscale" in exactly that case, so on item 22's EI reading this system has no emergent macroscale.
    - Here I(X_t;X_t′) = 2 bits and I(Xⁱ_t;X_t′) = 1 bit for each part. By Eq. 2 that gives Syn = Red.
    - Under the minimum-MI redundancy, Syn⁽¹⁾ = 1 bit > 0. By the theorem restated here, the system then hosts a causally emergent feature at a single scale.
    - Under a redundancy function with the identity property (e.g. Bertschinger et al.'s), Syn = 0 and the two accounts agree.
    - My arithmetic, not either paper's. The disagreement is real, but whether it shows up depends on the redundancy function.
  - (ii) Conversely, item 22's XOR example (§3.1): a macroscale XOR gate compared with its NAND/AND/OR implementation, with B_syn rising from 0.52 to 0.833. Item 22 counts that as emergence because of the comparison across descriptions. The framework here would ask a different question: whether, within the micro network's own partition, some function of the gates predicts the future beyond any single gate. The two need not agree.
  - (iii) Footnote 4 here shows that a change of coordinates can move 1 bit from synergy to unique information. Item 22's dimension reductions are also changes of description. So what item 22 calls "conversion of information across scales", this framework would call a change of partition, under which its quantities are *expected* to change (§IV B) and which it does not treat as evidence of emergence.
- *Timing.* This review (Nov 2021) postdates item 22 v1 (Apr 2021). The acknowledgements thank Erik Hoel and Thomas Varley "for useful discussions". Both were published in the same theme issue, whose editorial is [LIT-021](../literature.d/LIT-021.md). I cannot verify whether the published version of item 22 revised its §5.1 in response.

Other named alternatives in the paper: Hoel et al. 2013 (EI causal emergence) and Varley & Hoel as [5, 8], "not too dissimilar" approaches (§IV C); Seth 2010 (Granger emergence); Barnett & Seth 2021 (dynamical independence); Bedau (weak emergence); integrated information (Balduzzi & Tononi 2008), of which G is described as one ΦID atom (§V B).

## Bearing on the record

- In this record it is [LIT-025](../literature.d/LIT-025.md). Its summary should be corrected on two points. First, the review does not say the redundancy-free criteria detect D and G. It says they are sufficient criteria for emergence, and does not state them. Second, "extends" should read "restates, with interpretive remarks".
- It supports no THEORY document in the Anthology of the SOTA, and there is none it contradicts.
- **Not the ML sense of "emergent".** "Emergent capabilities" in ML ([ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md), Wei et al.; [ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md), Schaeffer et al.; [ANTH-THEORY-040](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-040.md); [ANTH-SOTA-200](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-200.md)) means abrupt onset of a task ability as model scale grows. This paper's emergence has no scale-of-model axis. It concerns synergistic predictive information about a dynamical system's own future under a fixed partition into parts. The paper makes no connection to machine learning, neural networks or scaling. The one "Future of Intelligence" string is an author affiliation. Nothing in it bears on [ANTH-SOTA-200](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-200.md) or [ANTH-THEORY-040](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-040.md), and a document that cited it for LLM emergence would be citing it for something it does not say.
- A possible, unstated link: ΦID synergy has been applied to learned representations elsewhere. This paper contains no such experiment and carries no instruction for ML practice. The coordinate dependence of §IV B would matter for any such use, because the "parts" of a network's activations depend on the basis.

## Limitations

- It proves nothing. The theorem, the exhaustiveness of Eq. 4 and the practical criteria are all asserted with citations to [7] and [26].
- The redundancy function is left open (footnote 2). The applications in §V B depend on one, and the review does not name it.
- The practical criteria need a named candidate feature V, which may not exist in resting-state data (§VI). The capacity measure avoids that but "scales poorly with the system size", and computing it for large systems is "currently unfeasible" (§VI).
- No efficient estimator of G⁽ᵏ⁾ exists for three or more time series (footnote 5). So the fMRI "causal emergence" results are pairwise G⁽¹⁾, a lower-order proxy.
- C5 (Granger = Pearl when all variables are measured) is stated without its conditions.
- The "feature not bug" defence of coordinate dependence (C6) is a philosophical stance. It does not tell a user which partition to choose.
- The brain results it cites were bioRxiv preprints at the time. The link to "complex, abstract reasoning" is speculative ("evidence suggesting that it may support").

## Open questions

- Efficient estimators of G⁽ᵏ⁾ and Syn⁽ᵏ⁾ for more than two time series (the authors' own).
- Procedures to *discover* emergent features V rather than test given ones (the authors' own, §VI).
- How much do the empirical conclusions move across redundancy functions? A robustness table across I_min, MMI and others would settle it.
- Is there a principled choice of partition, or does coordinate dependence make "emergence" relative to the observer's choice of parts? Item 22's cross-scale framing and this single-partition framing give different answers.

## Corrections to the seeded skim

- The dossier's summary line calls the redundancy-free criteria detectors of both D and G ("Both can be detected with redundancy-function-free criteria"). The review never says that. It says only (§III, last paragraph) that the framework yields "simple measures that provide sufficient criteria for guaranteeing the presence of emergence" and are independent of the redundancy function. It does not say which of D and G those criteria detect, and it does not state the criteria at all ("More information about these measures can be found in Ref. [7]"). [LIT-025](../literature.d/LIT-025.md)'s summary inherits this overstatement.
- The dossier and [LIT-025](../literature.d/LIT-025.md) say the review "restates and extends" the theory. The abstract claims "summarise, elaborate on, and extend". In the body, the extension is interpretive only (§IV A–C). Every formal result carries a citation to [7] (Rosas et al. 2020) or [26] (Mediano et al. 2019).
- The dossier says Syn = D + G is "presented as exhaustive (Eq. 4)". That is correct, but the review asserts it ("the ΦID framework shows that this taxonomy … is exhaustive") without derivation. It also asserts without derivation the two further iff results: D⁽ᵏ⁾ > 0 iff downward-causing features exist, and G⁽ᵏ⁾ > 0 iff causally decoupled features exist.
- Missing from the dossier: §IV C (p. 5) is a direct reply to item 22, Varley & Hoel. It cites them as [8] for the "potential misunderstanding" that ΦID "only concerns predictive ability at the microscale, without establishing a proper comparison with a macroscale". See Connections.
- Missing from the dossier: in the human-fMRI application (§V B), the quantity reported as synergy is G⁽¹⁾ computed over *pairs* of brain areas, not the full emergence capacity. The reason given is that no efficient estimator of G⁽ᵏ⁾ exists for three or more time series (footnote 5).
