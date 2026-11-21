# Reader notes: LIT-tmpys7v3, Bialek, Nemenman & Tishby, "Predictability, complexity and learning" (arXiv physics/0007070)

## Provenance

- Copy read: https://arxiv.org/pdf/physics/0007070 (arXiv, the authors' e-print;
  v3, stamped "23 Jan 2001"), PDF, 53 pages, fetched 2026-11-21 with no
  obstacle, converted with pdftotext. Read in full: abstract, §§1–6
  (pp. 1–47) and footnotes 1–19. Skipped: the reference list (pp. 48–53);
  Figures 1–3 read from captions and axis labels only.
- Copies located: only this one was sought; the arXiv copy is lawful (ADR-074)
  and was read, so no other host was tried. No email address was sent anywhere.
- Section numbers and equation numbers below are the e-print's; page
  numbers are the e-print's own.

## Summary

The predictive information I_pred(T, T') is the mutual information between a
past window of length T and a future window of length T' (Eq. 4); with
stationarity it is S(T) + S(T') − S(T + T') (Eq. 6), so the extensive part of
the entropy cancels and only the subextensive part S1 counts. Letting the
future run to infinity, I_pred(T) = S1(T) (Eq. 9). It is subextensive, and
its large-T behaviour falls in three classes: finite, logarithmic, power law.
When data come from a model with K unknown parameters drawn once from a
prior, S1(N) → (K/2) log2 N (Eqs. 41, 63, 68), with K replaced by a "phase
space dimension" d when the parameterization is degenerate, valid only for
N ≫ d_VC. Power-law growth N^(μ/(μ+1)) follows when the density of models at
KL divergence D from the target has an essential singularity
ρ(D → 0) ≈ A exp(−B/D^μ) (Eqs. 80–84); a Bayesian field-theory prior for a
smooth 1-D density gives μ = 1 and S1 ∝ N^(1/2) (Eqs. 93–97). §5 argues that
the divergent part of S1 is the unique complexity measure invariant under
coordinate changes and temporally local transformations.

## Contribution

A single, model-free quantity that contains, as special cases, Rissanen's
model complexity ((K/2) log N), the excess entropy of computational mechanics
(when finite), and Grassberger's effective measure complexity; a
statistical-mechanics reading (KL divergence as energy, N as inverse
temperature, S1 as free energy); and the first worked Bayesian
nonparametric case with power-law growth.

## Key results

1. Definition and subextensivity, §3, Eqs. 6, 9, p. 9–10: "predictability is a
   deviation from extensivity"; "Ipred (T ) = lim T′→∞ Ipred (T, T ′ ) = S1 (T )".
2. Diminishing returns, Eq. 10, p. 10: "most of what we observe is irrelevant
   to the problem of predicting the future."
3. Learning curve, Eq. 14, p. 11: "the learning curve is the derivative of
   the predictive information."
4. Identity with parameter information, §3, p. 12: "mutual information between
   the data and the parameters ... is easily shown to be equal to the
   predictive information about all of the future".
5. Three classes, §3, p. 12: "it may either stay finite, or grow to infinity
   together with T ; in the latter case the rate of growth may be slow
   (logarithmic) or fast (sublinear power)".
6. Linear regression test case, §4.1, Eq. 41, p. 18: f(x; α) = Σ α_μ φ_μ(x)
   with Gaussian noise; "S1 (N ) → K/2 log2 N (bits)", independent of the
   basis functions; obtained by saddle point and by replacing empirical means
   by expectations; "N F_N is the Fisher information matrix".
7. General K-parameter family, §4.2, Eqs. 52–63, pp. 20–22: Z(ᾱ; N) =
   ∫ dα P(α) exp[−N D_KL(ᾱ‖α)]; ρ(D → 0) ∝ D^((K−2)/2) (Eq. 60) gives
   "K/2 log2 N + · · · (bits)" (Eq. 63), "independent even of the prior".
8. Phase-space dimension, Eq. 64, p. 22–23: "ρ(D → 0; ᾱ) ∝ D^(d−2)/2 , and
   then d appears in place of K"; "Another possibility is that the
   determinant of F is zero ... one way to generate an effective fractional
   dimensionality". Valid "only for N ≫ dVC".
9. Processes, §4.3, Eqs. 65–69, pp. 23–24: needs S[{x}|α] → N S0 + S0* with
   S0* = O(1) ("if α is known there are no long range correlations"); if
   instead S0* = (K*/2) log2 N, then S1 = ((K+K*)/2) log2 N: "the
   subextensive entropy makes no distinction between predictability that
   comes from unknown parameters and predictability that comes from
   intrinsic correlations in the data". Mean-field Ising example: "we can
   trade a description in terms of long range interactions (K* ≠ 0, but
   K = 0) for one in which there are unknown parameters".
10. Fluctuations, §4.4, Eqs. 72–77: the fluctuation term S1^(f) is negative
    (Jensen) and O(1) for d_VC < ∞; for d_VC = ∞ (Eq. 79, Q ∝ exp(−sin αx))
    "there is no uniform bound on the value of N for which this convergence
    will occur".
11. Power law from an essential singularity, §4.5, Eqs. 80–84, pp. 30:
    "ρ(D → 0) ≈ A exp[−B/D^μ]" gives "S1^(a)(N ) → (1/ln 2)⟨C(ᾱ)⟩ N^(μ/(μ+1))
    (bits)". Heuristic: with K ∼ N^ν parameters, "the N th example then
    carries ∼ N^(ν−1) bits. Summing ... S1 ∼ N^ν, and if we let
    ν = μ/(μ + 1) we obtain Eq. (84)".
12. Worked nonparametric case, §4.6, Eqs. 85–97, pp. 32–34: smoothness prior
    on φ = −ln(l0 Q); ρ(D → 0) = A D^(−3/2) exp(−B/D), "µ = 1", and
    "S1^(a)(N ) ∼ (1/(2 ln 2)) √(N L/l) bits"; "the predictive information is
    directly proportional to the number of bins that can be put in the range
    of x". Authors state (p. 32): "we don't know of a complete calculation in
    which a family of power–law scalings ... is derived from a Bayesian
    formulation"; and (p. 34) smoother priors give smaller powers,
    "but real calculations for these cases remain challenging".
13. Uniqueness, §5.3, pp. 39–43: requiring invariance under instantaneous
    coordinate change and "temporally local transformations" leaves "only
    the divergent subextensive terms as a possible measure of complexity".
14. Criticality, §3 p. 12 and §6 p. 44: "In physical systems we know that
    there are critical points where correlation times become infinite ...
    Under these conditions the predictive information can grow without
    bound"; "At critical points the predictive information will diverge with
    the size of the system, and the coefficients ... should be related to the
    standard scaling dimensions ... but the details ... need to be worked
    out" (also fn. 9).
15. Crossover, Eq. 100, p. 46: a nonparametric model AN^ν has less predictive
    information than a K-parameter model below N_c ∼ [(K/2Aν) log2(K/2A)]^(1/ν).
16. Language, p. 47: Hilberg's reanalysis of Shannon, "evidence for a large
    component S1 (N ) ∝ N^(1/2)"; fn. 19, power-law MI decay in text cannot be
    Markov.

## Assumptions

Stationarity (§3); parameters drawn once from a prior and fixed for the whole
stream (Eq. 21); empirical means replaced by expectations (the annealed
approximation, fn. 5, Eq. 51) and a saddle point; a "sound" parameterization
(Clarke and Barron); N ≫ d_VC; ρ(D) without macroscopic weight at nonzero D;
for processes, Eqs. 65–66. The power-law results (Eqs. 84, 96–97) are
annealed (S1^(a)) and the essential singularity is posited in §4.5, computed
only for the one prior of §4.6.

## Concepts

predictive information; subextensive entropy S1; universal learning curve
Λ(N); density of KL divergences ρ(D; ᾱ) and the partition function Z(ᾱ; N);
phase-space dimension d vs K vs d_VC; annealed vs fluctuation terms; essential
singularity at D = 0; "universality classes" of complexity; effective measure
complexity (Grassberger); excess entropy (Shalizi & Crutchfield); stochastic
and model complexity (Rissanen); predictive-information bottleneck (§6).

## Verdict on the exchange's characterization

- A21 §4's three regimes, "I_pred(T) ∼ cT^μ, 0 < μ < 1 … in certain
  infinite-dimensional learning problems", and c log T for finitely many
  parameters: **accurate** (result 5, 6, 7, 11, 12).
- The LIT summary's "how much structure survives coarse-graining near
  criticality": **not the paper's subject**. The paper is about time series
  and learning; coarse-graining appears only as "temporally local
  transformations" (§5.3) and order parameters as compressions (§6).
  Criticality gets the passing remarks of result 14.
- A's caveat that the regimes "are not a one-to-one classification of
  physical criticality" is A's, not the paper's; the paper leans the other
  way, asserting divergence at critical points (result 14), unproved.
- TERM-tmpxml4k defines I_pred(T) with T' = T, I(X_{1:T}; X_{T+1:2T}). The
  paper's headline I_pred(T) is T' → ∞, i.e. S1(T) (Eq. 9); its Eq. 6 covers
  T' = T as a case. Same regimes and log coefficient; for power-law growth
  the two differ by the constant factor (2 − 2^μ).

## Bearing on the named codes

- **TERM-tmpxml4k: supports, with a correction of attribution.** The three
  regimes and the "random vs structured" distinction are the paper's (pp. 4,
  38: complexity "should be zero both for purely regular and for purely
  random systems"). Condition 1 (a shared latent quantity) is the paper's
  own setting (Eq. 21, result 4). Condition 2 is in the paper as Eq. 69
  (K* from intrinsic long-range correlations) and the mean-field Ising
  trade (result 9), and fn. 8 names 1/f spectra as violating Eq. 65. The
  TERM should note that the paper's I_pred(T) has an infinite future.
  "Not statistical complexity": parallel, §5.2/§6 (statistical complexity =
  Grassberger's true measure complexity = entropy of the minimal sufficient
  compression of the past). The paper also criticizes excess-entropy work
  for treating only the finite case (p. 38).
- **CLAIM-tmpyxiwv: supports the (d/2) ln T case; the T^(1/p) and
  (ln T)²/(4a) cases are not in the paper, but the T^(1/p) case is an
  instance of the paper's §4.5 result.**
  - (d/2) ln T: the paper's §4.1 is exactly the claim's setting, a
    linear-Gaussian model with a prior on α, giving "K/2 log2 N" (Eq. 41);
    with the claim's T' = T convention it becomes (K/2) log2(T/2), as the
    claim states. The paper also gives the claim's Step 1 in the T' → ∞ form:
    I(data; parameters) = I_pred (result 4).
  - T^(1/p): the paper never uses a Fisher spectrum beyond fixed K. Its
    power law comes from an essential singularity in ρ(D), N^(μ/(μ+1)), and
    heuristically from K(N) ∼ N^ν parameters. Mapping (the reader's, not the
    paper's): in the claim's Gaussian model ρ(D) is the small-ball law of
    ½Σλ_jξ_j², which for λ_j ∝ j^(−p) has log-density ∝ −D^(−1/(p−1)) (the
    standard Gaussian small-ball rate; not checked here), so μ = 1/(p − 1)
    and μ/(μ+1) = 1/p: the claim's exponent. The paper's worked μ = 1
    corresponds to p = 2 and its N^(1/2), with "number of bins" ∼ √N
    matching the claim's resolved count (CT)^(1/p). So the claim realizes,
    exactly, the paper's own heuristic that power law comes from "the number
    of parameters in the problem depending on the number of samples" — the
    paper says it knew no complete Bayesian family of power-law scalings
    (result 12); the claim's linear-Gaussian family is one.
  - Coefficient caveat (the reader's algebra, numerically checked in this
    session): the paper's power-law coefficients are annealed. In the
    claim's model the annealed S1^(a) = −⟨ln Z⟩ equals the exact
    G(N) = ½Σ ln(1+Nλ_j) plus ½Σ Nλ_j/(1+Nλ_j). For finite K the extra is
    ≤ K/2, a constant, harmless. For λ_j = j^(−p) it is the same order:
    extra/G = 0.501 at p = 2 and 0.341 at p = 3, N = 10⁶ (→ 1/p). So the
    exponent survives the annealed approximation, but its coefficient
    overstates the exact one by the factor (1 + 1/p); the negative
    fluctuation term (§4.4) is then of leading order, not O(1). The claim's
    exact G is the right object; it should not cite the paper's
    coefficients.
  - (ln T)²/(4a): absent from the paper.
  - Conditions the paper adds that bear on the claim: Eq. 65 (given θ, no
    long-range correlations; the claim's conditional independence is a
    stronger form); "sound" parameterization; N ≫ d_VC; degeneracy of F
    gives d < K (supports the claim's "not singular models" exclusion).
- **CLAIM-tmp99m8g: qualifies.** Supports the entropy/complexity split
  (pp. 4, 38; Eq. 10; the polymer example p. 41 where only the divergent
  term is universal). But on criticality the paper asserts that predictive
  information diverges at critical points (result 14), against "may or may
  not diverge" (A21 §8); the paper's statement is unproved, concerns
  divergence with system size in §6 and with time in §3, and its own §5.3
  notes 1-D local models have no critical points and fn. 16 flags
  "subtleties" for spatially infinite systems. It does not claim
  complexity peaks at criticality; it says logarithmic divergence also
  arises with no transition (learning, onset of chaos, p. 38).
- **CLAIM-tmpj0k4q: parallel, supporting.** The paper's §4.5 heuristic
  (K ∼ N^ν, each new sample worth ∼K/2N bits) and §4.6 bins ∼ √N are a count
  of effective parameters growing with the data; it says "the effective
  number of parameters becomes so large that asymptotic results ... are
  inaccessible in practice" (p. 4–5) and gives the crossover N_c (Eq. 100).
  It uses KL-density, not a Fisher-eigenvalue threshold nλ ≳ 1. Its warning
  (p. 31): "If the number of parameters grows constantly, then the scenario
  where the data overwhelms all the unknowns is far from certain."

## Limitations

Heuristic in places (the authors flag §4.6 as "less self-contained");
annealed coefficients for the power-law class; the essential singularity is
assumed in §4.5 and derived for one prior; the uniqueness argument (§5.3) is
an argument, not a theorem; criticality links are conjectural (fn. 9, §6);
Fig. 3 is a single numerical illustration on 10⁹-spin chains.

## Candidate THEORY

Sentence: "The predictive information of a stationary series, the mutual
information between its past and its future, is the subextensive part of its
block entropy; when the data come from a model with K parameters drawn once
from a prior, it grows as (K/2) log N (K replaced by a phase-space dimension
when the parameterization is degenerate, and only once N exceeds the VC
dimension), and when the density of models at small Kullback–Leibler
divergence D from the target has an essential singularity exp(−B/D^μ) it
grows, in the annealed approximation, as N^(μ/(μ+1)), as for a smooth density
under a field-theory prior, where μ = 1 and it grows as N^(1/2)."

promote_when: "A reading of a later rigorous treatment (Clarke and Barron
1990 for the parametric case; a nonparametric Bayesian result with exact,
not annealed, power-law growth of I(θ; X_{1:N})) confirms the logarithmic
coefficient under the stated conditions and the power-law exponent beyond
the annealed approximation."

## Recheck (held entries the first search missed)

- THEORY-087 (Bayesian Occam penalty (d/2) log n, λ log n singular): same
  coefficient as Eq. 63; paper's "phase space dimension" (Eq. 64) is the
  regular-model counterpart of the learning coefficient. Supports/parallel.
- THEORY-1253 (evidence as partition function, sample size as inverse
  temperature; LaMont & Wiggins, LIT-1882): the paper's §4.2 makes the same
  analogy ("temperature is inverse to the number of examples", p. 21) and
  its fn. 7. Parallel, earlier.
- LIT-888 / NOTE-689 (scaling laws from language statistics, Hilberg's
  hypothesis): the paper cites Hilberg's S1 ∝ N^(1/2) for English (p. 47).
  Background/parallel.
- LIT-1126 / NOTE-1372 / THEORY-743 (computational mechanics, causal states,
  excess entropy; IB optima coarsen the causal partition): §5.2 and §6
  identify statistical complexity with the minimal compression of the past
  keeping I_pred and frame it as an information bottleneck (LIT-338).
  Parallel.
- QUESTION-tmp2hhlc (whether predictive information peaks near a
  transition): result 14 bears on it; the paper asserts divergence at
  critical points without proof. Leaves open.
- QUESTION-tmpzlagu and LEAD-tmpl5wxz (effective dimensions; Ising
  predictive information on strips): the paper's K vs d vs d_VC (§4.2) is a
  further "effective dimension" the question does not list; §6's suggestion
  that divergence coefficients relate to scaling dimensions bears on the
  LEAD. Background.
- QUESTION-494, THEORY-026, QUESTION-191 (predictive vs nonpredictive
  memory): §1 "nonpredictive information is useless to the organism" and
  fn. 17. Background.

## Neighbours

None needed; the work itself was read.
