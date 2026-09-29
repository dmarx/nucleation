---
number: 300
status: Read
formerly:
- NOTE-tmpp9b1g
paper: LIT-338
title: 'The information bottleneck method'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv physics/0004057 v1 (submitted 24 Apr
    2000; the manuscript is dated 30 September 1999), 16 pp., from the arXiv
    PDF: abstract, §§1–3.4, "Further work" and all 6 references. Text was
    extracted with PyMuPDF, and I reconstructed the displayed equations from
    the extraction. I re-derived the stationarity condition (26)→(28) from
    the Lagrangian (24), and I checked that the variational solution has the
    exponential-of-KL form. I did not read the Allerton proceedings
    version.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  The paper defines relevant information as what X tells about a second
  variable Y and poses the information-bottleneck problem, min over
  p(x̃|x) of L = I(X̃;X) − β·I(X̃;Y), under the Markov chain X̃ ← X ← Y
  (eq. 15). Theorem 4 gives the exact formal solution p(x̃|x) =
  p(x̃)/Z(x,β)·exp(−β·D_KL[p(y|x)‖p(y|x̃)]), so the KL divergence emerges
  as the effective distortion. Theorem 5 gives a Blahut–Arimoto-style
  alternating iteration that converges but, being non-convex jointly, not
  necessarily to a unique solution.
---

# NOTE-300: The information bottleneck method

## Contribution

Rate–distortion theory needs a distortion measure chosen in advance, and choosing it is an arbitrary feature selection (§1). This paper replaces the chosen distortion with a second variable Y that defines what is relevant.

- **The problem.** Find the most compressed representation X̃ of X that keeps a given amount of information about Y.
- **The solution form.** It gives the exact self-consistent solution of that variational problem.
- **The effective distortion.** The problem's own distortion turns out to be D_KL[p(y|x)‖p(y|x̃)].
- **An algorithm.** It gives a convergent alternating algorithm generalising Blahut–Arimoto.

## Key insight

"Meaningful" information can be made quantitative without a semantics: it is the part of X that bears on Y. Squeezing X through a code X̃ while trading I(X;X̃) against I(X̃;Y) makes the right distortion measure appear by itself, as the KL divergence between the predictions of Y from x and from its codeword.

## Assumptions

- **Finite sets.** X and X̃ are finite; continuous spaces are quantised first (§2).
- **A known joint distribution.** p(x,y) is given; how to estimate it from samples is "beyond the scope" (fn. 1).
- **A Markov chain, not a model.** X̃ ← X ← Y, i.e. X̃ depends on Y only through X. Footnote 3 stresses this is not a latent-variable model, which would be Y ← X̃ ← X.
- **Relevance.** I(X;Y) > 0.
- **Cardinality.** The cardinality of X̃ is fixed per solution (§3.4).

## Key results

- **Rate–distortion recap (Theorem 1).**
  - For F = I(X;X̃) + β⟨d⟩, the stationary p(x̃|x) = p(x̃)/Z(x,β)·exp(−β·d(x,x̃)), and δR/δD = −β (eqs. 6–9).
  - β > 0 follows from the convexity of R(D) (the paper writes "concavity"; R(D) is convex). *Holds for:* any fixed distortion d.
- **Lemma 2 and Theorem 3 (Csiszár–Tusnády; Blahut–Arimoto).**
  - I(X;Y) = min over q(y) of D_KL[p(x,y)‖p(x)q(y)], attained at the marginal.
  - Alternating eqs. (1) and (8) converges to the unique minimum of the rate–distortion functional (proof cited to [2, 4]).
- **The IB variational principle (eq. 15).** L[p(x̃|x)] = I(X̃;X) − β·I(X̃;Y), with β = 0 the trivial one-point code and β → ∞ arbitrarily fine. Equivalently, maximise I(X̃;Y) at fixed compression (fn. 2).
- **Theorem 4, the exact formal solution.**
  - p(x̃|x) = p(x̃)/Z(x,β)·exp(−β·Σ_y p(y|x)·log[p(y|x)/p(y|x̃)]), with p(y|x̃) = (1/p(x̃))·Σ_x p(y|x)·p(x̃|x)·p(x) (eqs. 16–17). This is "formal" because p(y|x̃) depends on the unknown mapping.
  - The proof differentiates L (eqs. 23–27) and absorbs the x-only term I(x;Y) into the multiplier. I re-derived (26)→(28).
- **Theorem 5, the IB iteration.**
  - The self-consistent equations (18), (19) and (28) hold at the minima of F = −⟨log Z⟩ = I(X;X̃) + β·⟨D_KL[p(y|x)‖p(y|x̃)]⟩, called the "free energy".
  - Alternating over p(x̃|x), p(x̃) and p(y|x̃) converges.
  - The proof is "only outline[d]". F is convex in each argument separately but not jointly, so the solution need not be unique.
- **§3.4, structure of the solutions.**
  - δI(X̃;Y)/δI(X;X̃) = β⁻¹ > 0 (eq. 35). Solutions trace concave curves in the information plane (I_X, I_Y), one per cardinality of X̃, all starting from (0,0).
  - Curves for different cardinalities "bifurcate at some finite (critical) β through a second order phase transition", forming a hierarchy. This is asserted with citations [1, 5, 6], not derived here.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The IB optimum satisfies p(x̃|x) ∝ p(x̃)·exp(−β·D_KL[p(y|x)‖p(y|x̃)]) with the Bayes-consistent decoder | strong (proof) | Theorem 4, variational derivation (eqs. 23–28) |
| C2 | The KL divergence is the "correct" distortion for relevant quantisation | moderate (interpretive) | it emerges from C1 and is "not assumed otherwise anywhere" (Comment 1) |
| C3 | The alternating IB iteration converges | moderate (proof sketch) | Theorem 5; each step minimises the same bounded functional; outline only; no uniqueness |
| C4 | IB curves bifurcate at critical β through second-order phase transitions, forming a hierarchy of quantisations | weak here (assertion, cited) | §3.4, citing [1, 5, 6]; no derivation in this paper |
| C5 | IB unifies prediction, filtering and learning | assertion | "Further work", citing an in-preparation Bialek–Tishby [1] |
| C6 | For cases with sufficient statistics, almost all relevant information can be kept at finite β with significant compression | weak here (cited) | §3.1, citing [1, 5] |

## Method

The method is variational calculus with Lagrange multipliers, plus alternating minimisation over convex sets (Csiszár–Tusnády), generalising Blahut–Arimoto. For the full IB problem the alternation runs over three distributions instead of two.

## Concepts

- **Relevant information.** I(X̃;Y).
- **Information bottleneck Lagrangian.** L = I(X̃;X) − β·I(X̃;Y).
- **Information plane.** (I(X;X̃), I(X̃;Y)).
- **β as a resolution or inverse temperature.** The functional F is called a free energy, and annealing in β is suggested.
- **Effective distortion.** D_KL[p(y|x)‖p(y|x̃)].
- **Relevant quantisation / soft partition.** p(x̃|x).

## Connections

- **Earlier work.** Rate–distortion theory (Shannon–Kolmogorov, via Cover & Thomas), Blahut 1972, Csiszár–Tusnády 1984, and distributional clustering of English words (Pereira, Tishby & Lee 1993), which is the method's first application.
- **[LIT-324](../literature.d/LIT-324.md) (Shwartz-Ziv & Tishby 2017).** It reuses eqs. (15)–(17) and (28) verbatim as its eq. (9). It adds the minimal-sufficient-statistic reading, which this paper only gestures at ("where there exist sufficient statistics").
- **[LIT-226](../literature.d/LIT-226.md) (CEB).** Under this paper's Markov chain, I(X;Z|Y) = I(X;Z) − I(Y;Z), since Z ⊥ Y | X gives I(X,Y;Z) = I(X;Z). CEB's objective min I(X;Z|Y) − γ·I(Y;Z) is therefore eq. (15) reparametrised with β = γ + 1. The algebra is mine; I have not checked whether Fischer states it.
- **[LIT-240](../literature.d/LIT-240.md) (Vera et al.).** It turns I(X;U) into a generalisation-gap term. This paper says nothing about generalisation or finite samples (fn. 1 defers it). [LIT-245](../literature.d/LIT-245.md) critiques that step.

## Bearing on the record

**Row 12 and the gradient-as-channel narrative.**
- *What this paper does not supply.* It has no gradients, no learning dynamics, no batch size and no channel capacity. It is a lossy *source-coding* problem: compress X while keeping relevance to Y. The owner's §5 is a *channel* picture: data-to-weights capacity per gradient step, log₂(1 + SNR).
- *How the two relate.* They are dual rather than identical, as rate–distortion is dual to capacity. At most, IB is the natural description of *what* a representation should keep, while §5 is about *how fast* a gradient can write it.
- *The dynamics link.* That runs through [LIT-324](../literature.d/LIT-324.md) (Shwartz-Ziv & Tishby), which is where IB meets SGD and gradient SNR, and not through this paper.
- *So:* cite this paper for the IB functional, the information plane and β, not for the channel.

**What it does supply for the owner's project.**
- *Relevant information as a definition of meaning.* The paper opens by saying Shannon left meaning out and that lossy compression can put it back (§1). That is the nearest thing in this batch to an information-theoretic definition of the "meaningful" part of a signal, and it bears on the owner's concept project independently of row 12.
- *Physics vocabulary.* β plays the role of an inverse temperature. F = −⟨log Z⟩ is called a free energy. Solutions change at critical β through phase transitions. Those phase transitions are asserted here and cited out.
  - This is a formal analogy.
  - If the owner leans on it for row 13, "k_B T ln 2 per predicate bit", keep it separate from physical temperature, as with McCandlish's ε/B ([LIT-348](../literature.d/LIT-348.md)).

**Connections in nucleation.**
- *[LIT-224](../literature.d/LIT-224.md) (Grünwald & Vitányi).* Rate–distortion is the Shannon counterpart of Kolmogorov's structure function. IB is a rate–distortion problem with a derived distortion, so it sits in the same pairing as [LIT-239](../literature.d/LIT-239.md) (Kolmogorov's structure functions). That is the link to the "K-complexity ↔ minimal sufficient statistics" heading under which [LIT-226](../literature.d/LIT-226.md), [LIT-233](../literature.d/LIT-233.md), [LIT-236](../literature.d/LIT-236.md) and [LIT-240](../literature.d/LIT-240.md) were filed.
- *[LIT-317](../literature.d/LIT-317.md) (Shannon 1949).* The channel-side counterpart the owner actually uses.

**ML practice.** Via its descendants (VIB, CEB, the IB account of deep learning) only. The anthology holds the Tishby & Zaslavsky 2015 descendant ([ANTH-LIT-531](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-531.md)), not this paper. It stays here, and `anthology-candidate` is a fair tag.

## Limitations

- **Short and formal.** There are no experiments, and continuous variables are handled only by prior quantisation.
- **p(x,y) is assumed known.** Estimating it from finite samples is excluded, which is exactly where the deep-learning uses of IB later ran into trouble (see [LIT-324](../literature.d/LIT-324.md) and the anthology's [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md)).
- **The convergence proof is an outline.** It gives no uniqueness.
- **The headline properties are cited to other papers.** The phase-transition hierarchy and "unifies prediction, filtering and learning" come from an in-preparation paper [1] and the companion papers.

## Open questions

- Is the owner's per-step gradient channel the capacity-side dual of an IB problem on (data, weights)? In rate–distortion ↔ capacity terms, which relevance variable would make the §5 capacity bound an IB bound?
- The critical-β bifurcations of §3.4 are where the owner's "concepts become resolvable" framing (row 15) would naturally attach. The derivation is in [1, 5], which are not read here.

## Corrections to the seeded skim

- Seeded from metadata. The text confirms the title, the authors (Tishby, Pereira, Bialek), the arXiv id and the category physics.data-an. The arXiv v1 PDF says nothing about Allerton; the Allerton venue is confirmed only second-hand, by Shwartz-Ziv & Tishby's reference list ("Proceedings of the 37-th Annual Allerton Conference…, 1999").
- `published: 1999-01-01` can be tightened. The manuscript's title page is dated "30 September 1999", so 1999-09-30 is a documented date for the text; the conference dates themselves are unverified here. The seed's identification note mentions "page range from recollection", but no page range appears in the seed, and none can be checked from this text.
- The seed summary is accurate. One refinement: the paper proves stationarity and the convergence of the alternating iterations, not global optimality. It says outright that its convergence proof "does not imply uniqueness of the solution" (end of §3.3).
- Slips in the text. In eq. (31) the third update sums over y where it should sum over x, as in eq. (17). The theorem says the p(x̃|x) update uses d(x,x̃) generically, and d = D_KL[p(y|x)‖p(y|x̃)] is defined only in the proof. "Blauht-Arimoto" is misspelt on p. 8. The Markov chain is written X̃ ← X ← Y at Theorem 4 and Y ← X ← X̃ in the proof: the same chain, written in both directions.
- The map's row-12 characterisation, "the information-bottleneck principle behind the gradient-as-channel narrative", overstates the link. See Bearing on the record.
