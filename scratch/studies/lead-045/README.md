# LEAD-045: the same unequal-frequency skills under gradient descent and under sign descent

Run on 2026-11-22. numpy and scipy on CPU; no downloads.

## Files

- `geometry.py`: the Geometry model of Liu, Liu, Michaud, Gore and Tegmark
  (THEORY-253), its simulation under gradient descent, sign descent and Adam,
  the ODE derived below with its closed forms, and the rotated quadratic of
  the paper's Fig. 12.
- `network.py`: a two-layer ReLU network trained on four independent skills
  of unequal frequency (numpy, manual backpropagation).
- `run_all.py`: runs everything and writes `results/`. About five minutes on
  four cores: `python3 -I run_all.py` (or `geometry` or `network` alone).
- `test_lead045.py`: `python3 -I -m pytest -q test_lead045.py` (12 tests, under
  a few seconds).
- `results/geometry.json`, `results/network.json`, `results/network.tsv`,
  `results/network_curves.npz` (every network run's per-skill training
  curves, recorded every 3 steps).

## Derivation: sign descent in the Geometry model

The loss is l(θ) = Σ_i p_i u_i², with residual u_i = 1 − s_i, skill level
s_i = θ·t_i and the t_i orthonormal in R^d. The gradient is
g = −2 Σ_i w_i t_i with w_i = p_i u_i.

**One step.** Sign descent moves θ by −η sign(g), so skill j changes by
Δs_j = η Σ_k t_jk sign(z_k), with z_k = Σ_i w_i t_ik.

**Mean field.** Let the t_i be random rotations of the coordinates, so that
across coordinates k the entries (t_1k, …, t_nk) behave as independent
N(0, 1/d) draws. For jointly Gaussian X and Z, E[X sign Z] = √(2/π) Cov(X, Z)/σ_Z.
Here Cov(t_jk, z_k) = w_j/d and σ_Z = ‖w‖₂/√d. Summing d such terms, which
concentrate for fixed n as d grows,

  ds_j/dt = c w_j / ‖w‖₂,  c = η √(2d/π) per step,

that is,

  **du_j/dt = −c p_j u_j / ‖p∘u‖₂.**

**Consequence 1: the path is gradient descent's.** Gradient flow gives
du_j/dt = −2 p_j u_j. The two differ by the positive scalar factor
c/(2‖p∘u‖₂), the same for every j. So sign descent here is gradient flow with
its clock divided by the gradient norm: normalized gradient descent. The
curve in skill space is the same, u_j = exp(−p_j τ), and the conserved
quantity u_i^(1/p_i) = u_j^(1/p_j) of the paper's Resource model holds
exactly. Only the timing differs. In particular, at the moment skill 1 is
learned (u_1 = ε), skill 2 has made exactly the progress it makes under
gradient descent, 1 − ε^(p₂/p₁).

**Consequence 2: the clock.** In τ, t(τ) = (1/c) ∫₀^τ ‖p∘exp(−pτ′)‖₂ dτ′.
Skill j is learned at τ_j = ln(1/ε)/p_j, at time t_j = t(τ_j).

**Consequence 3: the onset ratio.** Because ‖·‖₂ lies between the largest
term and the sum, d(Σ_i s_i)/dt = c ‖p∘u‖₁/‖p∘u‖₂ lies in [c, c√n]: total
skill grows at least linearly and at most √n times faster. When
p₁ ≫ p₂ ≫ …, one term dominates except at the crossovers, whose
contribution vanishes as the ratios p_{i+1}/p_i → 0; then each skill costs
1/c in turn and

  t_n / t_1 → (n − ε)/(1 − ε),

which is 2.11 for n = 2 at ε = 0.1 and tends to n, so to 2 for two skills,
as ε → 0. Under gradient descent, t_n/t_1 = p₁/p_n.

**Consequence 4: delayed onset.** d/dt ln(ds_j/dt) has the sign of
Σ_i p_i² u_i² (p_i − p_j). The strongest skill decelerates from the start;
every weaker skill accelerates while stronger skills remain unlearned. So
its learning curve is convex at first and its fastest progress comes when
the stronger skills finish, where under gradient descent every skill's
fastest progress is at t = 0.

**Consequence 5: alignment.** If each t_i lives on its own coordinates,
sign(z_k) = sign(t_ik) whatever the weights, every coordinate moves at η,
and all skills are learned together whatever their frequencies. The delay
needs misalignment. For the Hadamard rotation of Fig. 12 (|R_ik| = 1/2,
d = 4) the statement is exact for any step: while λ₁x₁ > Σ_{j>1} λ_j x_j,
every coordinate of the gradient has the sign of row 1, x₁ falls by 2η per
step and x₂, x₃, x₄ do not move at all (to 2·10⁻¹⁴ in the run).

**Adam.** With β₁ = β₂ = 0, Adam is sign descent up to its ε, and the run
matches it to four figures. At the default β the ratio grows with p₁/p₂
(table), so Adam at default settings lies between the two, as the paper
reports.

**Against the paper's account.** The mechanism the paper offers,
sign(g₁ + g₂) ≈ sign(g₁) when ‖g₁‖ ≫ ‖g₂‖, is the dominance case of
Consequence 1. The fitted Resource model has the ℓ₁ norm plus a constant N₀
in the denominator; the derived one has the ℓ₂ norm and no constant. The two
agree in the Domino limit; at intermediate frequencies the ℓ₂ form matches
the simulation better (table).

What the derivation assumes: d large against n, the t_i generic with
respect to the coordinates, steps small against the residuals (it does not
describe the end of training, where sign descent oscillates at the step
size), squared loss.

## Results: the Geometry model (d = 1000, η = 10⁻⁴, ε = 0.1)

| p₁ | sign descent, simulated t₂/t₁ | derived (ℓ₂) | Resource, N₀ = 0 (ℓ₁) | Adam, default β | gradient descent, simulated (theory p₁/p₂) | skill 2 at t₁, sign / GD / derived |
|---|---|---|---|---|---|---|
| 0.5 | 1.017 | 1.000 | 1.000 | 1.01 | 1.00 (1) | 0.88 / 0.90 / 0.90 |
| 0.6 | 1.129 | 1.112 | 1.109 | 1.10 | 1.52 (1.5) | 0.77 / 0.78 / 0.78 |
| 0.7 | 1.287 | 1.262 | 1.241 | 1.30 | 2.38 (2.33) | 0.61 / 0.62 / 0.63 |
| 0.8 | 1.490 | 1.473 | 1.420 | 1.60 | 4.13 (4) | 0.43 / 0.43 / 0.44 |
| 0.9 | 1.756 | 1.748 | 1.688 | 2.38 | 9.38 (9) | 0.23 / 0.22 / 0.23 |
| 0.95 | 1.911 | 1.908 | 1.874 | 3.44 | 19.9 (19) | 0.12 / 0.11 / 0.11 |
| 0.99 | 2.054 | 2.056 | 2.059 | 6.80 | 104 (99) | 0.03 / 0.02 / 0.02 |

The absolute times agree too: at p₁ = 0.9, steps 367 and 645 simulated
against 372 and 649 derived. Skill 2's fastest step under sign descent came
at 0.93 to 1.0 of its own learning time; under gradient descent it is the
first step.

Five skills, p_i ∝ i^(−α), sign descent, t_n/t_1:

| α | simulated | derived | Domino limit | gradient descent |
|---|---|---|---|---|
| 1 | 1, 1.37, 1.55, 1.62, 1.68 | 1, 1.34, 1.52, 1.61, 1.67 | 1, 2.11, 3.22, 4.33, 5.44 | 1, 2, 3, 4, 5 |
| 2 | 1, 1.72, 2.23, 2.47, 2.63 | 1, 1.71, 2.15, 2.42, 2.56 | same | 1, 4, 9, 16, 25 |
| 3 | 1, 1.88, 2.59, 2.99, 3.27 | 1, 1.89, 2.55, 3.00, 3.24 | same | 1, 8, 27, 64, 125 |

Rotated quadratic (Fig. 12; x(0) = 1, η = 10⁻³), steps until x_i ≤ 0.5:
sign descent with R = I: 500, 500, 500, 500; with R = H₄: 251, 730, 1172,
1731; gradient descent: 347, 3466 and not within 20 000 steps for x₃, x₄,
under both R. The Hadamard first phase ends at x₁ = 0.111, step 444, as
derived.

## Results: a trained network

Task: input [e_i; x], e_i the one-hot code of skill i, x ~ N(0, I₈); skill
i's target a_i·x, the a_i orthonormal; K = 4 skills with p_i ∝ i^(−2)
(0.70, 0.18, 0.08, 0.04); 4096 training examples, full batch; a two-layer
ReLU network of width 64 with an antisymmetric initialization, so that the
output is zero at the start at every scale. Order-one scale is
W ~ N(0, 1/fan-in), v ~ N(0, 1/width); small scale multiplies both by 0.01.
Gradient descent at learning rate 0.2 for 6000 steps; sign descent and Adam
(default β) at 10⁻³ for 3000 steps; seeds 0, 1, 2 (data and
initialization); one sign-descent run at 3·10⁻⁴ as a learning-rate check.
Skill level s_i = 1 − L_i/E[y²] on skill i's training examples; learned at
s_i ≥ 0.9.

Two measures. **Delay**: the level reached at half a skill's own learning
time, over 0.9. A curve that rises fastest at the start (gradient descent in
the Geometry model) gives 0.76; one held back and rising late gives less
(sign descent in the Geometry model gives 0.30 at p₂/p₁ = 0.25). **Spread**:
t_n/t_1 at the learned threshold.

| optimizer, init | delay, skills 2–4 (mean; range over 9) | t_learned / t_1, skills 2, 3, 4 (mean of 3) | skill 4's ratio, range |
|---|---|---|---|
| gradient descent, order one | 0.71 (0.59–0.80) | 6.1, 11.8, 23.4 | 8.3–38 |
| sign descent, order one | 0.47 (0.27–0.70) | 3.0, 4.1, 5.4 | 4.4–6.7 |
| Adam, order one | 0.43 (0.23–0.64) | 3.0, 4.2, 5.5 | 4.5–7.0 |
| gradient descent, small | 0.11 (0.01–0.26) | 5.2, 9.9, 15.8 | 14.5–17.2 |
| sign descent, small | 0.25 (0.02–0.61) | 2.4, 3.3, 6.0 | 4.9–7.7 |
| Adam, small | 0.28 (−0.02–0.46) | 3.3, 4.5, 6.3 | 5.5–7.0 |

The Geometry model's derived ratios for these frequencies are 1.67, 2.06 and
2.24 under sign descent and 4, 9 and 16 under gradient descent. The
learning-rate check (3·10⁻⁴) gave 3.1, 3.7 and 4.5. Under sign descent at
order one, skill 2 is the most delayed (0.35), and skills 2 to 4 reach half
their level close together (steps 112 to 178, against 72 to 304 under
gradient descent), after skill 1 (19 to 28). Under every optimizer the
weaker skills' levels fell below zero, to −0.2 to −0.3, while skill 1 was
being learned: in the network the skills share hidden units and interfere,
which the Geometry model excludes.

## What it does and does not show

- In the Geometry model the derivation answers the first limb of
  QUESTION-193 for generic high-dimensional misalignment, in the mean-field
  limit: the delay of each weaker skill, its acceleration while stronger
  skills remain, and t₂/t₁ → (2 − ε)/(1 − ε), hence 2 as the threshold
  tightens. It also says what the delay is: a change of clock along
  gradient descent's own path, not a change of path.
- In one small network, changing only the optimizer, from order-one scale,
  moved the weaker skills from rising fastest at the start to rising late,
  and compressed the spread of learning times (skill 4 from 23 times skill
  1's to 5.4 times).
  That is the direction the Geometry model predicts. The network did not
  reproduce the clean Domino form: the spread stayed about twice the
  derived one, skills 2 to 4 were not held back in frequency order, and the
  skills interfered.
- From small scale, gradient descent alone gave the strongest delay of all,
  the small-initialization mechanism (THEORY-187, THEORY-229), and changing
  to sign descent weakened it. The two mechanisms are separated as
  THEORY-253 predicted: one depends on the optimizer and not the scale, the
  other on the scale under gradient descent.
- Not shown: anything about a larger network, another architecture, a
  stochastic batch, a hierarchical task (the lead's second design, not run
  here), or Adam's own dynamics beyond the two β settings.
