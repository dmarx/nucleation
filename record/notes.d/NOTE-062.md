---
number: 62
status: Read
formerly:
- NOTE-tmpjtzwb
paper: LIT-051
title: 'Başar, Meyn & Perkins, control system theory notes'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2007.01367v2 (title page "Originally
    prepared January 2007 (this version, July 2024)"; arXiv stamp 11 Jul
    2024), 238 PDF pp. (xii + 224 numbered). I read every page: the preface
    with its 2024 note, contents, Chs 1–11 including all exercises, the
    bibliography [1]–[13] and the index stub. Extraction was with PyMuPDF
    (raw4/2007.01367.txt). Figures (simulation plots, block diagrams, root
    loci, Nyquist plots) came through as labels only, so I read them from
    captions. As instructed, I did not produce theorem-level detail for
    textbook material. I checked the worked examples numerically in
    scratchpad/check_ctl.py: - the state-transition matrices of §3.4 and Ex.
    3.5.2; - the Lyapunov solution of Ex. 4.4.1; - the ε < 4/5 bound of
    §4.6; - Fact 3 of Ch. 7 at the three quoted gains; - the ARE solutions
    of Exs 10.5.1, 10.5.3, 10.5.4 and 10.5.5; - the Pendubot transfer
    function (9.2), the LQR poles (9.3) and the Ch. 9 compensator.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  A conventional first-year graduate course in linear state-space control.
  It covers modelling and linearisation, LTI/LTV solutions, Lyapunov
  stability, controllability and observability with Kalman/Hautus tests
  and minimal realisations, then pole placement and observers, integral
  control, sensitivity, and finally HJB/LQR and a heuristic minimum
  principle. Its most useful non-standard content is the Pendubot thread
  (Chs 1, 9, 10): an observer-based design from one sensor is fragile (the
  compensator has an unstable pole at s ≈ 46.4), while full-state LQR has
  |S(jω)| ≤ 1, infinite gain margin and ±60° phase margin. Every worked
  example I recomputed is correct.
---

# NOTE-062: Başar, Meyn & Perkins, control system theory notes

## Contribution

These are course notes, not research. What they add is a single free, self-contained graduate state-space course that goes from modelling to LQR with worked examples and about 90 exercises. Two things distinguish them from standard textbooks (Chen, Brogan, Anderson–Moore, which they cite):
- **A running physical example.** The Pendubot, a two-link underactuated pendulum at UIUC, is used to make one design argument end to end: controllable-and-observable is not enough, and zeros and sensor choice decide robustness (Ch. 9 → §10.6).
- **Three derivations of the minimum principle.** Ch. 11 gives it from HJB (under smoothness), from Lagrange multipliers, and from a penalty method, all explicitly heuristic, with the full proof deferred to Luenberger [10].

## Key insight

The pedagogical spine is that a state-space model's structural properties (controllability, observability, stabilisability, detectability) decide what feedback can do: poles can be placed arbitrarily exactly on the controllable subspace, and observers exactly on the observable one (separation principle, Eq. 7.6). But **none of these properties says anything about robustness.** Robustness enters through the frequency domain: sensitivity S = 1/(1+L), the Bode integral, and RHP zeros. Its cleanest positive result is the return-difference identity of LQR. For full-state LQR, |1 + L(jω)|² = 1 + |P(jω)|²/r ≥ 1, so |S| ≤ 1 at all frequencies, giving infinite gain margin, tolerance of the gain halved, and ±60° phase margin (§10.6). The Pendubot shows this guarantee vanishing when the state is estimated from one sensor.

## Assumptions

These are the standing assumptions of the notes. The setting is narrower than the title.
- **Continuous-time, finite-dimensional, mostly LTI.** LTV systems appear for existence and uniqueness (Thm 3.2: A(t) piecewise continuous), transition matrices, controllability/observability grammians (Thms 5.2, 6.2), duality (Thm 6.3) and the finite-horizon Riccati equation.
- **Nonlinear systems only locally.** They appear through linearisation and Lyapunov theory (Ch. 4, where f ∈ C² is assumed throughout), and in the HJB and minimum-principle chapters.
- **Deterministic throughout.** There are no noise models, estimation-theoretic observers, or stochastic control.
- **LQR standing assumptions:**
  - R > 0 and Q ≥ 0;
  - for infinite horizon, (A, B) stabilisable and (A, C) detectable with Q = CᵀC (Thm 10.6);
  - the explicit Hamiltonian-matrix solution (10.16), (10.18) is derived only for **distinct eigenvalues of H**.
- **Minimum principle.** The HJB route assumes a smooth value function and a smooth minimiser ū(x, t); the notes flag this as "false in many models" (p. 204). Theorems 11.1–11.4 are stated, not proved.

## Key results

By chapter, without theorem-level detail for textbook material:
- **Ch. 1:** linearisation (magnetic ball, Pendubot), CCF/OCF/modal realisations.
- **Ch. 2:** linear algebra review: fields, bases, Jordan form by example, inner products, adjoints.
- **Ch. 3:** eᴬᵗ three ways, Cayley–Hamilton (proved only for distinct eigenvalues), LTV fundamental matrices, Peano–Baker.
- **Ch. 4:**
  - Lyapunov stability definitions, Lyapunov's direct method (Thm 4.3, proof cited to LaSalle–Lefschetz [9]) and a region-of-attraction theorem (Thm 4.4, proved).
  - LTI stability ⇔ Hurwitz (Thm 4.1), and ⇔ a P > 0 solving AᵀP + PA = −Q (Thm 4.6, proved).
  - Linearisation theorem (Thm 4.7, proof sketched) and BIBO stability.
- **Ch. 5:** controllability via the grammian (Thm 5.2, proved), rank of [B AB … Aⁿ⁻¹B] (Thm 5.3, proved), modal test (Thm 5.5, distinct eigenvalues) and Hautus–Rosenbrock (Thm 5.6, one direction proved, the converse cited to Chen [6]).
- **Ch. 6:** observability, duality (Thm 6.3), Kalman canonical forms, minimality ⇔ controllable + observable (Thm 6.5, proved only for distinct eigenvalues), and a MIMO minimal-realisation example of degree 3 (the sum of residue ranks).
- **Ch. 7:** pole placement ⇔ controllability (Thm 7.1, SISO argument only, MIMO asserted), stabilisability/detectability (Thms 7.2–7.3), full and reduced-order (Luenberger) observers, the separation principle (7.6), and "observer feedback generalises lead compensation" (Ex. 7.4.1).
- **Ch. 8:** integral action as the internal model principle, with the rank condition rank[−A B; −C 0] = n + p for DC tracking; controller design as a Diophantine/Sylvester equation a·d + b·n = α_c·α_o.
- **Ch. 9:**
  - sensitivity S = 1/(1+L), with S + T = 1 and the Bode integral ∫₀^∞ log|S(jω)| dω = 0 for relative degree ≥ 2 and a stable open loop (stated, not proved);
  - transmission zeros;
  - the Pendubot plant P(s) = 15.9549 (s²−6.5354²)/[(s²−9.4109²)(s²−5.6372²)], which I verified from (9.2).
- **Ch. 10:**
  - HJB (Thm 10.1: necessity heuristic, sufficiency proved by a verification argument);
  - finite-horizon LQR via the Riccati differential equation (Thm 10.2) and via the Hamiltonian matrix, P = YX⁻¹ (Thm 10.3);
  - eigenvalue symmetry of H (Lemma 10.4);
  - infinite-horizon ARE, with the closed-loop poles equal to the stable eigenvalues of H (Thm 10.5), and the stabilisable/detectable existence–uniqueness theorem (Thm 10.6, stated);
  - the return-difference equation (10.27), the symmetric root locus and Kalman's inequality.
- **Ch. 11:** minimum principle (Thm 11.1) with input constraints (Thm 11.2), fixed terminal state (Thm 11.3) and free terminal time (Thm 11.4). Examples: bang-bang bilinear control with switching at t1 − 1, fixed-endpoint LQR, and double-integrator minimum time with at most one switch.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Worked numerical examples are correct | strong | my recomputation of 3.4, 3.5.2, 4.4.1, §4.6 (ε < 4/5), Ch. 7 Fact 3, 10.5.1 (P̄ = 1+√2), 10.5.3 (P ≈ 0.236·[[1,1],[1,1]], printed "0.24"), 10.5.4 (P̄ = diag(2,1), H eigenvalues ±1, ±2), 10.5.5 (P̄ = [[√3,1],[1,√3−1]]), (9.2)→P(s), (9.3) = LQR poles for Q = I, r = 1 (−35.97, −2.87, −5.31±0.83j) |
| C2 | Core linear-systems theorems (grammian tests, duality, Lyapunov equation, separation) | strong | proofs in text (Thms 4.6, 5.2, 5.3, 6.2, 6.3; Eq. 7.6), standard |
| C3 | Hautus test, pole placement for MIMO, minimality in general, Cayley–Hamilton in general | moderate | proved only for distinct eigenvalues or SISO; the general case is cited to Chen [6] and Brogan [5] |
| C4 | Infinite-horizon LQR existence/uniqueness/stability under stabilisable + detectable (Thm 10.6) | moderate (cited standard result) | stated without proof; the motivating examples 10.5.2–10.5.3 are worked |
| C5 | Full-state LQR: |S(jω)| ≤ 1, infinite gain margin, ±60° phase margin, for any Q, R | strong for SISO | return-difference derivation (10.30)–(10.32). The notes state it for full-state feedback; the MIMO version needs more (e.g. diagonal R), which the notes do not discuss |
| C6 | Any stabilising compensator for the one-sensor Pendubot must itself be unstable | weak | "by examining a root locus plot it may be shown" (p. 160). The claim is true (parity interlacing: one real plant pole lies between the RHP zero 6.54 and +∞), but the notes neither prove it nor name the theorem |
| C7 | The one-sensor Pendubot design is fragile (gain margin < 10⁻²) | moderate | Nyquist and sensitivity plots (Figs 9.2–9.3), p. 192 statement. My check that the printed-precision G destabilises the plant corroborates it |
| C8 | Minimum principle (Thms 11.1–11.4) | weak here (standard result) | three heuristic derivations; proof cited to Luenberger [10] |
| C9 | For real, distinct, negative eigenvalues, a minimum-time bang-bang control switches at most n−1 times | moderate as a statement, weak as argued | the classical result needs only real eigenvalues. The notes' reason ("since the modes are all decreasing") is not the argument, since the costate modes e^{−λt} grow |
| C10 | Part 1 clarifies the relationship to reinforcement learning (preface) | unsupported | no RL content in Part I or elsewhere |

## Method

This is expository. Each chapter pairs a result with a physical or numerical example and Matlab command lists (some of which are dated: "LQG", "LQG2" and "ARE" as LQR solvers, p. 194; the text elsewhere uses `lqr`). Proofs are complete for the core LTI results and heuristic or cited for the rest, as listed in the Claims table.

## Concepts

- **Stable in the sense of Lyapunov / asymptotically / globally asymptotically stable** (§4.1), standard.
- **Stabilisable**: ∃K with A − BK Hurwitz. **Detectable**: ∃L with A − LC Hurwitz. Their characterisations are via the KCCF/KOCF (Thms 7.2–7.3).
- **Transmission zero** (§9.4): s₀ where [s₀I − A, −B; C, 0] loses rank. For a square plant, not at a pole, this is rank P(s₀) < m.
- **Return difference** 1 + L(s), with L = K(sI − A)⁻¹B (full-state loop). The **symmetric root locus** is the set of roots of 1 + r⁻¹P(−s)P(s) = 0 as r varies (10.31).
- **Hamiltonian matrix** H = [[A, −BR⁻¹Bᵀ], [−Q, −Aᵀ]] (10.14).

## Connections

- Its sources are the standard texts it cites: Anderson–Moore [1] for LQR, Chen [6] and Brogan [5] for linear systems, LaSalle–Lefschetz [9] for Lyapunov theory, Luenberger [10] for the minimum principle, and Kalman's 1960/1964 LQR papers (p. 194).
- The Pendubot material comes from the UIUC robotics lab (Spong).
- The 2024 edition points to Meyn's *Control Systems and Reinforcement Learning* [11] (CUP 2022) for the RL connection. That book, not these notes, is where a control-to-RL bridge lives.

## Bearing on the record

- **No THEORY document in this record needs it.** If one ever cites Lyapunov's direct method, the Lyapunov equation, LQR/ARE, HJB or the LQR robustness margins for background, these notes are an adequate free citation. For the robustness margins (C5), cite §10.6, and note that it holds for full-state feedback only.
- **For ML practice: none directly.** The seed's "continuous-time views of training dynamics" and "linear-quadratic RL" are links the notes do not make; they contain no learning, no stochastic control and no discrete-time LQR. A document in the Anthology of the SOTA that wanted a control-theoretic source for, say, gradient flow as a Lyapunov argument (Exercise 4.8.2(b) poses exactly ẋ = −P∇V as an exercise) would do better with a paper that makes the ML claim. So would one wanting an LQR baseline for RL.

## Limitations

- **Deterministic and continuous-time.** There is no Kalman filter, LQG, stochastic optimal control, H∞/robust synthesis, MPC or discrete-time Riccati equation. The preface's discrete-time claim is barely met (§5.1 only).
- **Several general results are proved only in special cases** (distinct eigenvalues, SISO) or cited. Thm 10.6 is unproved; so is the minimum principle.
- **The RL framing promised in the 2024 preface is absent.**
- **The v2 errata.** It fixed one figure but left the typos and slips listed above, including the inconsistent Fig. 9.2 caption and the rounded compensator. I could not check the claimed Fig. 1.1 correction ("definition of y_t"), because the figure's labels are in the image.
- **Figures were not inspected** as images, so the plots (root loci, Nyquist) are taken from their captions.

## Open questions

- None as research. For a reader: whether Meyn's 2022 book [11] carries the RL bridge the preface promises is the thing to check before citing either for RL.

## Corrections to the seeded skim

- **The seed takes the 2024 preface at its word: "Part 1 was revised to clarify the relation to RL".** The text does not bear this out. Reinforcement learning appears exactly twice in 238 pages: the preface sentence and bibliography entry [11] (Meyn, *Control Systems and Reinforcement Learning*, 2022). Part I (Chs 1–3) contains no RL, no discrete-time value iteration and no Q-function; it is modelling, linear algebra and matrix exponentials. The only RL-adjacent material is the HJB/principle-of-optimality derivation in Ch. 10, which is standard and not framed as RL. Whoever wants the control–RL bridge must go to [11], not here.
- **Discrete time is covered far less than the preface says.** The preface says "Both continuous-time and discrete-time systems are covered, with the former … in much greater depth". Discrete time appears in one place, §5.1 (a one-page preview of the controllability matrix). There is no discrete-time stability, Riccati, DP or observer.
- **The seed's Ch. 10 list omits two limits of scope.**
  - Its infinite-horizon results (Thm 10.6) are stated without proof ("⊓⊔" with no argument).
  - The LQR robustness guarantee is stated for full-state feedback only. The notes say so, and show via the Pendubot that an observer-based design loses it (gain margin "less than 10⁻²", p. 192).
  
  There is **no Kalman filter, LQG, stochastic control, H∞ or discrete-time LQR** anywhere. So the notes do not support "linear-quadratic RL" beyond the deterministic continuous-time LQR.
- **Two internal inconsistencies in the Pendubot thread** (Ch. 9):
  1. The Fig. 9.2 caption says the compensated open loop GP "possesses two poles in the right half plane" and needs "three encirclements of −1". The plant has two RHP poles (5.64, 9.41) and the compensator a third (46.37), so L has three RHP poles, which is what three encirclements require. The caption's "two" is wrong.
  2. The printed compensator G(s) = 24,424 (s+9.4)(s+5.64)(s−7.41)/[(s+60.24±63.5j)(s−46.37)(s+6.54)] **does not stabilise the printed plant at its printed precision.** My recomputation puts one closed-loop pole at s ≈ +0.024. Rebuilding G from the stated gains reproduces it to three figures (gain 24,498; zeros 7.412, −9.411, −5.637; poles −60.30±63.56j, 46.43, −6.535), and that exact design is stable by construction. So the printed numbers are right but rounded past the design's own tolerance. The book's point about fragility is demonstrated more sharply than it says.
- Minor errors a reader will trip on (none affects a main result):
  - The CCF matrix (p. 13) has "a3" for −a3.
  - "K is a n × m matrix" (p. 123) should be m × n.
  - The controllability grammian is called "the positive definite matrix" (p. 93), but it is only semidefinite unless the system is controllable.
  - Ex. 4.4.1's first printed equation "−2p11 − 2p12 = −1" should be −4p12 = −1, though the printed solution P = [[5/4, 1/4],[1/4, 3/8]] is correct.
  - The Peano–Baker sum uses k for the summation index (p. 58).
  - Ex. 7.5.17 defines "S = 1/(PG)" for 1/(1+PG).
  - Theorem 10.1's proof is headed "Proof of Theorem 10.2.1".
  - "BR⁻¹Bᵀ is positive definite" (p. 173) should be semidefinite.
  - The Lemma 10.4 determinant chain has a spurious (−1)ⁿ factor and the wrong matrix in its last term, though the conclusion is right.
  - Fig. 10.2 is captioned "Solutions to the ARE" for the RDE.
  - p. 187 says "phase margin at least 60%" for 60°; p. 191 has it right.
  - Ex. 7.4.1 has "as t → 0" for t → ∞.
  - The costate ODE in Ex. 11.5.3 is written −Aᵀ(ṗ1, ṗ2).
- The Van der Pol system (4.2) is printed as ẋ2 = −(1 − x1²)x2 − x1. That is the *reversed* (time-reversed) Van der Pol, whose origin is asymptotically stable; the standard oscillator has an unstable origin and a limit cycle. The analysis (V = ½|x|² + εx1x2, ε = 1/6; Q > 0 for ε < 4/5, which I verified) is correct for the system as printed, but the name will mislead.
