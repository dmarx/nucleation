# LEAD-015: the two-institution symmetry-breaking condition

Two of LEAD-090's reduced CASE-092 institutions (CASE-tmpz4n6b), an evaluator
E and an evaluated party P, coupled through named channels, linearized at
the symmetric state, and the condition for its instability derived and
checked. Filed as an executed-study CASE with claims (see the changelog
fragment `record/changelog.d/lead-015.md` for the codes).

## Rerun

    cd scratch/studies/lead-015
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider --rootdir=. test_model.py   # 14 tests, ~2 s
    python3 -I run.py            # all experiments, under a minute
    python3 -I run.py e2 e4      # or some of them

`model.py` loads `../lead-090/model.py` (LEAD-090's one-institution model) by
path; the test `test_each_half_is_lead090_institution` checks that each half
of the two-institution map is that model's exact mean field.

## Model

Each institution i in {E, P} is the one-institution reduced map

    m' = (1 - rho) m + rho (b + sigma a + phi' m),        phi' = phi (1 - eps)
    a' = delta a + (1 - delta) tanh(g sigma m / 2 + t)

(b: imbalance of the corpus it reads; t: an outside tilt of its conferral,
zero in LEAD-090). Both read the same two hypotheses. Channels (all >= 0 in
the main result):

| channel | from -> to | enters as | CLAIM-404's words |
|---|---|---|---|
| theta | m_P -> E | b_E = theta m_P | the party affects the evaluator's evidence |
| omega | m_P -> E | t_E = omega m_P | the party affects the evaluator's resources (who gains authority inside it) |
| chi | m_E -> P | b_P = chi m_E | the evaluator's reading is evidence the party reads |
| psi | m_E -> P | t_P = psi m_E | the evaluator's reading affects the party's standing: resources and authority inside the party (A21's chain) |

A21's chain ("Public interpretation -> Political and regulatory decisions ->
Distribution of resources and authority -> Conditions of future media
production -> Public interpretation") is theta and psi.

## Derivation

At x = (m_E, a_E, m_P, a_P) = 0 the Jacobian is J = [[J_E, C_EP], [C_PE, J_P]],
J_i = [[alpha_i, beta_i], [gamma_i, delta_i]] with CASE-tmpz4n6b's entries
(alpha = 1 - rho(1 - phi'), beta = rho sigma, gamma = (1 - delta) g sigma / 2),
C_EP = u_E e1^T, u_E = (rho_E theta, (1 - delta_E) omega)^T, and
C_PE = u_P e1^T, u_P = (rho_P chi, (1 - delta_P) psi)^T.

1. **General block condition.** For J >= 0 with rho(J_E), rho(J_P) < 1:
   rho(J) < 1 iff I - J is a nonsingular M-matrix iff (I - J_E being one)
   its Schur complement S = (I - J_P) - C_PE G_E C_EP is one, G_i = (I - J_i)^-1.
   S = (I - J_P) - N with N >= 0 is a regular splitting, so S is a
   nonsingular M-matrix iff rho(G_P N) < 1 (Varga). So the symmetric state
   is unstable iff the round-trip gain rho(G_P C_PE G_E C_EP) > 1. Checked on
   random nonnegative block matrices of sizes 2+2, 3+2, 3+3 and 4+5
   (`test_block_theorem_general`).
2. **Rank-one channels.** The round trip is then the scalar L_E L_P, with
   L_E = e1^T G_E u_E = [(1 - delta_E) rho_E theta + beta_E (1 - delta_E) omega] / D_E,
   D_E = det(I - J_E) = rho_E (1 - delta_E) Delta_E, Delta_E = (1 - phi'_E) - g_E sigma_E^2 / 2,
   so **L_E = (theta + sigma_E omega) / Delta_E**, and likewise
   **L_P = (chi + sigma_P psi) / Delta_P**. Delta_i > 0 is exactly
   CLAIM-tmp6f8w8's condition that institution i is stable alone.
3. **The condition.** The symmetric state of the pair is unstable iff

       (theta + sigma_E omega)(chi + sigma_P psi) > Delta_E Delta_P.

   It has CLAIM-330's form (a cross product against the product of the
   margins), one level up. rho_i and delta_i cancel, as in CLAIM-tmp6f8w8.
   The leading eigenvector is positive in every component: the two
   institutions' meanings and authorities lean together.
4. **Below threshold** a standing bias b0_P of the party's corpus moves the
   stationary state by d m_P*/d b0_P = 1 / (Delta_P (1 - L_E L_P)) and
   d m_E*/d b0_P = L_E / (Delta_P (1 - L_E L_P)): the cross loop multiplies
   the party's bias in both institutions by 1 / (1 - L_E L_P).

## Experiments (`run.py`, results in `results/`)

- e1: the condition against the nonlinear map on 2000 random parameter sets
  with each institution stable alone; the captured state across rho and delta.
- e2: CLAIM-404's cases: A21's chain below and above; no internal loop in
  either institution; the evaluator in Regime B; informational independence
  with a resource channel; the return channel cut; both institutions near
  their own thresholds.
- e3: linear response to the party's bias below threshold.
- e4: the agent-level pair (LEAD-090's step_stochastic per institution),
  200 seeds from exact symmetry, below and above the threshold.
- e5: alternatives: resources as capacity (multiplicative, omega scales g_E),
  and corrective (negative) return channels.
