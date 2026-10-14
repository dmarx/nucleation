---
number: 820
status: Read
formerly:
- NOTE-tmpzvbap
paper: LIT-963
title: 'Chowdhury et al. — Fundamental Limits of Perfect Concept Erasure'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arXiv:2503.20098v1, the only
    version; AISTATS 2025, PMLR 258), text extracted with pdftotext: §§1–6,
    the checklist, Appendix A (all proofs: Lemmas 3.2, 3.3, A.4, A.5, the
    justification of Definition 4.1 and of Method 4.2), Appendix B
    (optimisation) and Appendix C (setup, analysis, the LEACE toy). The
    plotted values in Figures 4–6 were not recoverable from the text
    layer, so the empirical comparisons are taken from the prose. The
    reading's claim that a stochastic map attains the utility bound for
    unequal distributions was checked numerically by script (five random
    instances with three groups of support sizes 3, 5 and 2: I(Z;A) = 0
    and I(Z;X) = H(X|A) to six decimals).
date: '2026-10-14'
summary: >-
  If an erased representation Z is independent of the concept A, it keeps
  at most I(Z;X) ≤ H(X|A). A deterministic erasure reaches that only when
  the groups' distributions are permutations of one another. The paper
  says the bound is out of reach otherwise. That holds only for
  deterministic maps: a stochastic quantile coupling reaches it for any
  finite distributions with disjoint supports.
---
<!-- inactive-ok-file: THEORY-281 THEORY-199 THEORY-030 — Proposed; the theory filed from this reading, the partial answer of the same shape, and an unrelated theory named to set it aside, open -->

# NOTE-820: Chowdhury et al. — Fundamental Limits of Perfect Concept Erasure

## Contribution

The paper poses concept erasure as a privacy-funnel problem: choose an
erasure function f so that Z = f(X) keeps as much information about the
representation X as possible while revealing nothing about a categorical
concept A. Building on Calmon et al. (2015, 2017), it states the cap on
what can be kept under perfect erasure. It characterises, for
deterministic maps, when the cap is reached, and gives an algorithm
(PEF) that reaches it in that case and erases perfectly, with less
utility, otherwise.

## Key insight

Erasing a concept perfectly costs at least the information the
representation shares with it. Within each concept group the map can be
lossless only if every group can be laid onto one common output
distribution. For a one-to-one map that means the groups must be
permutations of each other.

## Assumptions

All results are under (A1)–(A5), §3.1:

- **(A1) Markov:** A → X → Z, so I(Z;A|X) = 0. The erasure function sees
  X, not A.
- **(A2), (A3) Finite supports** for X, Z and A.
- **(A4) Disjoint group supports:** supp P(X|A=aᵢ) ∩ supp P(X|A=aⱼ) = ∅
  for i ≠ j. So A is a deterministic function of X, H(A|X) = 0, and
  H(X|A) = H(X) − H(A). This is much stronger than the word-embedding
  example suggests, and the paper does not draw the consequence.
- **(A5)** |𝒳| > |𝒜|.
- **Known distributions.** PEF needs the class-conditional distributions
  Pᵢ. On real data they are estimated by kernel density estimation.

## Key results

- **Lemma 3.2 (achievability; via Calmon et al.'s Lemma A.4).** Under
  (A1)–(A4), perfect erasure is "achievable" if the smallest principal
  inertia component λ_d(A,X) = 0 or |𝒳| > |𝒜|. The proof shows that the
  optimal erasure-utility coefficient v* = inf I(Z;A)/I(Z;X) is 0. What
  is achievable is therefore zero leakage *with positive utility*. A
  constant map erases perfectly in every case.
- **Lemma 3.3 (perfect-erasure bound).** If I(Z;A) = 0 then
  I(Z;X) = I(Z;X|A) ≤ H(X|A), with equality iff H(X|Z,A) = 0. The proof
  (A.2) uses only (A1) and I(Z;A) = 0, so it holds without (A4).
- **Lemma 3.6 (erasure funnel bounds, Calmon et al. 2017).** For
  0 ≤ u ≤ H(X), ε(u) = inf_f {I(Z;A) : I(Z;X) ≥ u} satisfies
  max{0, u − H(X|A)} ≤ ε(u) ≤ u·I(A;X)/H(X). §3.3 reads the upper
  bound as "the minimum mutual information" in relaxed erasure. The lemma
  only brackets ε(u). Relaxed erasure is then deferred to future work.
- **Definition 4.1 and Appendix A.3 (when the cap is reached).** The
  groups must have equal support sizes and be permutations of one
  another: Pᵢ(x) = Pⱼ(σᵢⱼ(x)). The contributions list calls this a
  hypothesis. A.3 argues necessity for a deterministic piecewise map
  f(x) = fᵢ(x): equality needs each fᵢ bijective (Lemma A.5), and I(Z;A) = 0
  needs equal output conditionals, by strict concavity of entropy.
- **Method 4.2 and Appendix A.4 (sufficiency).** Map each group
  bijectively onto a common Q (any permutation of the Pᵢ). Then
  I(Z;A) = 0 and I(Z;X) = H(X|A).
- **Unequal distributions (§4).** Maximise J(Q) = H(Q) − Σᵢ p(aᵢ)·
  H_min(Pᵢ, Q) over the common output Q, with each group coupled to Q by a
  minimum-entropy coupling. The map is stochastic: f(x) ∼ P(Z|X=x).
  The paper says that here "achieving the outer bounds ... is not
  possible". It also says "H(X|Z,A) > 0" for this map, and that the
  global optimum Q* is "an open question". Candidates are the Pᵢ
  themselves and a Bayesian-optimisation solution.
- **Experiments (§5).** Synthetic 3D finite-support data with two groups:
  - Equal distributions: PEF reaches the utility bound with
    I(Z;A) = 0 (V-information estimates).
  - Unequal distributions: zero leakage, utility below the bound.
  - Baselines: INLP and LEACE keep utility but leak; FaRM and KRaM erase
    but collapse; DCA behaves like the linear methods.
  - Real data: gender from GloVe, and religion from GPT-4
    text-embedding-3-large embeddings of Jigsaw comments. PEF gives lower
    leakage at utility (MSE reconstruction) similar to the non-linear
    baselines, and a better fairness–MSE trade-off in toxicity
    regression.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under perfect erasure, I(Z;X) ≤ H(X|A), with equality iff H(X|Z,A) = 0 | strong | Lemma 3.3, proof A.2 (needs only A1) |
| C2 | Zero leakage with positive utility is possible when |𝒳| > |𝒜| or λ_d = 0 | strong | Lemma 3.2 via Calmon et al. (2017) |
| C3 | A deterministic erasure reaches the bound iff the group distributions are equal up to permutation | strong | A.3 (necessity) and A.4 (sufficiency) |
| C4 | For unequal distributions the bound cannot be reached | contradicted for stochastic maps | asserted in §4; see Limitations |
| C5 | PEF erases perfectly and keeps more than INLP, LEACE, FaRM, KRaM and DCA on the tested data | moderate | Figs. 4–6, synthetic and two real datasets, MI by V-information or MSE |

## Method

Algorithm 1:
1. Estimate each Pᵢ.
2. If all are equal up to permutation, map each group bijectively to a
   common Q.
3. Otherwise choose Q̂ among the Pᵢ and a Bayesian-optimisation
   candidate. Then sample z from each group's greedy minimum-entropy
   coupling with Q̂.

Appendix B.1 offers projected gradient descent over the couplings for
small supports.

## Concepts

- **Perfect concept erasure.** I(Z;A) = 0 (Definition 3.1).
- **Utility.** I(Z;X): information about the whole representation, not
  about any downstream task.
- **Erasure funnel.** The privacy funnel of Makhdoumi et al. renamed:
  ε(u), the least leakage at utility at least u.
- **Principal inertia components.** The singular values, after the
  first, of D_X^{-1/2} P D_A^{-1/2}. The smallest, λ_d, governs whether
  perfect privacy is possible when |𝒳| ≤ |𝒜|.
- **Perfect erasure function (PEF).** The piecewise map onto a common
  output distribution.

## Connections

It applies Calmon et al.'s privacy-funnel bounds to the concept-erasure
line of Ravfogel et al. (INLP) and Belrose et al. (LEACE, which erases
only against linear adversaries; Appendix C.3 shows a non-linear
boundary surviving LEACE on a four-point toy). The minimum-entropy
coupling machinery is Kocaoglu et al.'s greedy algorithm, within 0.53
bits of optimal (Compton et al. 2023).

## Bearing on the record

- **[QUESTION-010](../questions.d/QUESTION-010.md)** asks whether a chain can keep information sufficient
  for one family of tasks while destroying what another needs. This
  paper settles the one-step, information-theoretic form for one
  concept. Everything about A can be destroyed while H(X|A) bits about X
  are kept, and no more. The same chain rule, applied to any task
  variable B (this reading's step, not the paper's), gives
  I(Z;B) ≤ I(Z;B|A) ≤ H(B|A). A task that is a function of A is lost
  entirely, and any other keeps at most what it carries beyond A. It says
  nothing about chains, about relations, or about task families defined
  otherwise than by a categorical concept. This is a partial answer of the
  same shape as [THEORY-199](../theory.d/THEORY-199.md), which is one step and an ideal procedure.
  Filed as [THEORY-281](../theory.d/THEORY-281.md) with an `answers` edge.
- **[LIT-963](../literature.d/LIT-963.md)'s filing text** reads the paper as a bound on erasing one
  concept "while all other information is kept". The bound says what is
  kept is at most H(X|A), and that is all other information only in the
  sense of the information about X not shared with A. Under (A4) that is
  exactly H(X) − H(A).
- **No existing THEORY** in the record holds concept-erasure limits.
  [THEORY-030](../theory.d/THEORY-030.md) (Landauer) uses "erasure" in the thermodynamic sense and is
  unrelated.
- **For the anthology.** The algorithm and its benchmark comparison carry
  an instruction for ML practice (how to erase a concept from
  embeddings), and that part belongs to the anthology; the LIT's
  `anthology-candidate` flag stands. The bound is a statement of
  information theory and is held here.

## Limitations

- **The unattainability claim for unequal distributions is false for
  stochastic maps.** A.3 proves necessity only for a deterministic
  piecewise map. Lemma 3.3's equality condition is H(X|Z,A) = 0. That
  holds whenever, within each group, x is a function of z, so each Pᵢ
  must be a deterministic coarsening of the common output Q. Any finite
  set of distributions has such a common refinement. Lay each Pᵢ out as
  consecutive intervals of [0,1], and take Q to be the cells cut by the
  union of all their breakpoints. Each group then maps x to a cell inside
  x's interval, at random, in proportion to cell length. Under (A4) this
  map depends on x alone and gives I(Z;A) = 0 and I(Z;X) = H(X|A).
  - *Smallest case:* P₁ = (½, ½), P₂ = (1), equal priors. Map x₃ to z₁ or
    z₂ with probability ½ each. This gives I(Z;A) = 0 and
    I(Z;X) = 0.5 bit = H(X|A).
  - *Checked numerically* for three groups of unequal sizes (see
    history).
  The same construction answers the paper's open question about Q*.
  Since H_Γ(Pᵢ,Q) ≥ H(Q), J(Q) ≤ 0 (up to the constant), with equality
  exactly at a common refinement. The cost is a larger output support,
  up to Σᵢ|𝒳ᵢ| − |𝒜| + 1 points.
- **(A4) makes the concept a function of the representation.** Results
  do not cover overlapping supports. There, a map that sees only X cannot
  in general apply a group-specific coupling, and the attainability
  analysis does not apply.
- **Utility is information about X, not about a task.** The bound is
  silent on what a downstream user can still do.
- **Empirical leakage is a lower bound.** V-information from a
  bounded classifier understates mutual information. Real-data utility
  is measured by MSE of a regression from Z back to X.
- **Distributions must be known.** On real data they are KDE estimates
  over finite samples, and the authors attribute the lost utility on
  GloVe to that.
- **Small slips.** §4 writes "perfect concept erasure, I(Z; X) = 0" for
  I(Z;A) = 0. Lemma A.5 states that the map must be bijective where
  injective suffices.

## Open questions

- The relaxed regime (ε > 0): which functions attain the funnel's
  bounds. The authors defer it.
- Overlapping supports, where the erasure function cannot read the
  group off the representation.
- A task-relative version: the most that can be kept about a task B
  under I(Z;A) = 0. That is the form [QUESTION-010](../questions.d/QUESTION-010.md) needs.
