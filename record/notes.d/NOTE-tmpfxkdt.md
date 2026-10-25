---
status: Read
paper: LIT-tmpm3j41
title: 'Kwon and Perchet — Blackwell approachability with partial monitoring: optimal convergence rates'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Read from the PMLR copy (proceedings.mlr.press/v54/kwon17a/kwon17a.pdf)
    and its supplementary material (kwon17a-supp.pdf), text extracted with
    pdftotext. The main paper, all five sections, was read in full. The
    supplement was read for Appendix A (Propositions 3.1–3.3 and Lemma
    A.4 on the flag estimate) and Appendix C on closed convex cones. The
    proof of Theorem 4.1 in Appendix B (Lemmas B.1–B.9) and the
    concentration inequalities of Appendix E were read at the level of
    their statements and the main paper's six-step outline, not checked
    line by line. Lemma A.4 is re-derived and checked by simulation in
    THEORY-tmpjv5er. The rates are THEORY-tmp172nr.
date: '2026-10-25'
summary: >-
  Approachability of a polytope (reduced to the negative orthant) under
  partial monitoring, where the decision maker sees only a random signal
  whose law is known, can be achieved at rate O(T^-1/3) in expected
  distance for general signals and O(T^-1/2) when the signal law does not
  depend on the decision. The general algorithm lifts the problem to an
  auxiliary full-information approachability problem that is linear in
  the flags, and keeps a uniform exploration floor γ ∝ T^-1/3 so that the
  flags can be estimated by importance weighting.
---
<!-- inactive-ok-file: THEORY-tmp172nr — Proposed; the rates as the paper states them, filed from this reading -->
<!-- inactive-ok-file: CLAIM-357 CLAIM-446 — Proposed; claims whose dated notes cite this work, nothing here rests on them -->
<!-- inactive-ok-file: THEORY-tmpz3a05 THEORY-925 — Proposed; accounts compared with, nothing here rests on their being settled -->
# NOTE-tmpfxkdt: Kwon and Perchet — Blackwell approachability with partial monitoring: optimal convergence rates

## Contribution

It gives the first approachability algorithms under partial monitoring
whose rates match the known lower bounds: O(T^{−1/3}) for general signals,
improving Mannor, Perchet and Stoltz's dimension-free O(T^{−1/5}) and
Perchet's O(T^{−1/(I+3)}), and O(T^{−1/2}) for outcome-dependent signals.
They are computationally efficient: a projection onto a polyhedral cone
and a linear program per stage, after a one-time simplicial subdivision.

## Key insight

Under partial monitoring the decision maker never sees its payoff, only
the flag, the vector of signal laws f(y) = (s(i, y))_i that Nature's mixed
action induces for every decision. Distributions with the same flag are
indistinguishable. The set m(x, f) of payoffs compatible with a flag is
set-valued and only piecewise affine in f, so averaging it directly is
awkward. The paper replaces it by a single-valued worst-case
representative r(x, f), affine on each piece of a simplicial subdivision.
It then lifts the whole problem into a higher-dimensional space where the
representative becomes linear and the problem is ordinary full-information
approachability. The cost of partial monitoring is then only the cost of
estimating the flags. That requires seeing every decision's signal, hence
a uniform exploration floor, unless the signal does not depend on the
decision.

## Assumptions

- Finite decision sets I (decision maker) and J (Nature), and a vector
  payoff g: I × J → ℝ^d, extended bilinearly to mixed actions.
- A finite signal set S and a known signal law s: I × J → Δ(S). The
  decision maker sees s_t ~ s(i_t, j_t), never j_t or g_t.
- The target is the negative orthant C = ℝ^d_−. A polytope is handled by
  representing it as an orthant in higher dimension, as in Mannor et al.
  (2014b, §5.4.2).
- C is assumed approachable. Perchet's characterization (2011a), cited,
  not proved here: C is approachable iff for every flag f there is an x
  with m(x, f) ⊂ C.
- Nature is adversarial, and the guarantee is uniform over its choices.
  The rate is for E[d₂(ḡ_T, C)], the expected Euclidean distance of the
  average payoff to the target.

## Key results

- **Blackwell's characterization, full monitoring (§2.1, cited).** A
  closed convex C is approachable iff for every y there is an x with
  g(x, y) ∈ C. For a closed convex cone this is equivalent to: for every
  z in the polar cone C°, there is an x with ⟨g(x, y), z⟩ ≤ 0 for all y.
- **Proposition 3.1.** The representative r_n(x, b) = max g_n(x, f⁻¹(b))
  on the vertices b of the subdivision, extended by barycentric
  coordinates, satisfies g_n(x, y) ≤ r_n(x, f(y)). For every flag some x
  has r(x, f) ∈ ℝ^d_−. And r is affine in f on each simplex F^k and in x
  on each polytope X^ℓ.
- **Propositions 3.2–3.3.** A linear map R on the lifted space reproduces
  r. The lifted target C̃ is a closed convex cone, contained in
  R⁻¹(ℝ^d_−), and approachable with full monitoring in the auxiliary
  problem.
- **The algorithm (§4.1).** Project η Σ_{s<t} g̃_s onto C̃° ∩ B₂, solve a
  linear program for x̃_t, draw (k_t, a_t) ~ x̃_t, play
  i_t ~ (1 − γ)a_t + γu with u uniform, and estimate the flag by
  f̂_t = (1{i_t = i} δ_{s_t} / P[i_t = i | G_t])_{i∈I}.
- **Lemma A.4.** f̂_t is conditionally unbiased for the flag, with
  E[‖f̂_t‖² | G_t] ≤ |I|²/γ and ‖f̂_t‖² ≤ |I|²/γ² almost surely
  (re-derived in THEORY-tmpjv5er).
- **Theorem 4.1.** With η = √(γ/(T|I|²)) and
  γ = min{(11 L_r |I||K||A| / (4‖g‖))^{2/3} T^{−1/3}, 1}, against any
  choices of Nature, E[d₂(ḡ_T, ℝ^d_−)] ≤ 12‖g‖^{1/3}(L_r|I||K||A|)^{2/3}T^{−1/3}
  + 2√π‖g‖T^{−1/2} + 6‖g‖^{2/3}(L_r|I||K||A|)^{1/3}T^{−2/3}. L_r is the
  maximal Lipschitz constant of r(x, ·), and it scales with ‖g‖.
- **Theorem 4.3 (outcome-dependent signals).** If s(i, j) does not depend
  on i, then with no exploration and f̂_t = (δ_{s_t})_i,
  E[d₂(ḡ_T, ℝ^d_−)] ≤ (2√π‖g‖ + 2L_r√(|I||K||A|))/T^{1/2}. The proof is
  omitted as following Theorem 4.1's.
- **Optimality (§1).** T^{−1/3} matches Cesa-Bianchi et al.'s lower bound
  for general signals, and T^{−1/2} is already optimal with full
  information. Both lower bounds hold in the special case of regret
  minimization. So the rates are optimal in the worst case over games,
  not for every game.
- **§5.2.** High-probability and almost-sure versions follow by
  Hoeffding–Azuma for vector martingales (Kallenberg and Sztencel) and
  Borel–Cantelli.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Approachable polytopes can be approached at O(T^{−1/3}) under general partial monitoring | strong | Theorem 4.1 with proof in Appendix B (outline checked, not every lemma) |
| C2 | With outcome-dependent signals the rate is O(T^{−1/2}) and no exploration is needed | moderate | Theorem 4.3; proof omitted as analogous |
| C3 | These rates cannot be improved without further assumptions | strong as a worst-case statement | cited lower bounds (Cesa-Bianchi et al. 2006; full information) |
| C4 | The algorithms are computationally efficient | moderate | one projection and one LP per stage; the subdivision is "tedious, but only needed once" |
| C5 | Approachability contains regret minimization, long-term constraints, global costs and varying stage durations | strong for the reductions shown | §2.2; Blackwell (1954), Abernethy et al. (2011) |

## Concepts

- **Approachable set**: C such that some algorithm makes
  E[d₂(ḡ_T, C)] → 0 uniformly in Nature's choices.
- **Flag**: f(y) = (s(i, y))_{i∈I}, the signal laws for every decision
  under Nature's mixed action y. It is the maximal information the
  decision maker can have about y.
- **Outcome-dependent signals**: s(i, j) independent of i.
- **m(x, f)**: the set of payoffs compatible with mixed decision x and
  flag f.
- **Polar cone C°**: {z : ⟨z, c⟩ ≤ 0 for all c ∈ C}.

## Connections

Blackwell (1956) for approachability and Blackwell (1954) for its link to
regret. Perchet (2011a) for the characterization under partial
monitoring. Rustichini (1999), Mannor and Shimkin (2003), Lugosi, Mannor
and Stoltz (2008) and Perchet (2011b) for the regret line. Mannor, Perchet
and Stoltz (2014b) for the representative r and the subdivision, whose
block averaging this paper removes. Rambau and Ziegler (1996) for the
simplicial subdivision. Bartók et al. (2014, LIT-tmpwpq36) is cited for the
regret classification. Read the other way, the paper gives that
classification's rates in average form: √T regret is T^{−1/2} average,
and T^{2/3} is T^{−1/3}.

## Bearing on the record

- **CLAIM-357's note of 2026-10-25, checked.** The note says the claim's
  worst residual is a one-shot test against {z : z_i ≤ 0 for every i},
  and that approachability is the repeated version. That set is exactly
  the paper's target, ℝ^d_−, and d₂(z, ℝ^d_−) = ‖z₊‖₂, the Euclidean norm
  of the positive parts. So the repeated test differs from the one-shot
  test in two ways the note names. The norm is ℓ₂ of the violations, not
  their maximum, the "choices of normalization and geometry" A30 warned
  of. And it applies to the average. The second is compensatory in the
  way A30 said: a requirement violated by +1 on every other stage and met
  with slack −1 on the rest has average 0 ∈ C, so it is approached
  perfectly while violated half the time. The note is accurate. The paper
  gives no guarantee for windows or individual stages, and none should be
  read into it.
- **CLAIM-446 and QUESTION-271: the floor, exactly.** In the general
  algorithm every decision is played with probability at least γ/|I|,
  because the flag component of a decision is observed only when that
  decision is played. The tuned floor shrinks as T^{−1/3}. When the signal
  does not depend on the decision, the floor is removed (Theorem 4.3). The
  approach–avoid game has decision-dependent signals, since avoid shows
  nothing, so it is in the floor-needing case. This is THEORY-tmpjv5er.
  It is the same structure as COMA's floor (THEORY-925), with the variance
  cost made explicit: Σ_i 1/P[i_t = i].
- **NOTE-1142, LIT-1521.** Hart and Mas-Colell use approachability of the
  negative orthant by the regret vector. This paper is that construction
  when the regret vector cannot be observed.
- **THEORY-tmpz3a05.** Read for regret, the two papers agree on the rates
  (§1's summary of Bartók et al.).

No instruction for ML practice. The anthology-candidate flag on the LIT
stands.

## Limitations

- **Approachability is assumed, not decided.** Perchet's condition is
  cited, and no procedure for checking it is given.
- **Constants grow with the subdivision**: |K| and |A| are the numbers of
  simplices and vertices, which can be large, and the subdivision is
  constructed once by an unspecified procedure.
- **Average-payoff guarantees only.** Nothing for per-stage or windowed
  constraints, which is the gap CLAIM-357's note points to.
- **The outcome-dependent proof is omitted**, said to follow the general
  one.
- **Optimality is worst-case over games.** For a particular game the
  achievable rate can be better, as in Bartók et al.'s easy class.

## Open questions

- Is there a classification of approachability problems by rate,
  analogous to Bartók et al.'s for regret, with a locally observable class
  at T^{−1/2} even when the signals depend on the decision? The paper's
  rates are worst-case, so this is open in it.
- What replaces the average when violations cannot be compensated
  (windowed or per-stage approachability), and at what rate?
