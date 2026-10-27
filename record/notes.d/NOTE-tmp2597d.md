---
status: Read
paper: LIT-tmp0oa8w
title: 'Van Gael, Saatci, Teh and Ghahramani — Beam sampling for the infinite hidden Markov model'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the authors' PDF on the Cambridge
    Machine Learning Group's server
    (https://mlg.eng.cam.ac.uk/pub/pdf/VanSaaTehGha08.pdf, 8 pages; the
    same file is on Teh's Oxford page), which carries the proceedings
    footer "Appearing in Proceedings of the 25th International Conference
    on Machine Learning, Helsinki, Finland, 2008"; the ACM copy was not
    compared. Text extracted with pdftotext. Read: §§1–6, the captions of
    Figures 1–7, the two footnotes and the references. Figures 3–7 are
    charts and segmentations, read from their captions and the text only;
    no number was taken from them. The beam sampler's invariance was
    checked numerically on a small finite HMM (record script, 2026-10-27).
date: '2026-10-27'
summary: >-
  Introduces the beam sampler for the infinite HMM: a slice variable
  u_t ~ Uniform(0, π_{s_{t−1}s_t}) at each step cuts the infinitely many
  transitions out of each state to the finitely many above u_t, so whole
  trajectories are sampled exactly by forward filtering, backward
  sampling. Against the Gibbs sampler it mixes in fewer iterations on
  strongly correlated synthetic sequences, is less sensitive to the
  hyperprior, handles a non-conjugate Cauchy likelihood on well-log data,
  and costs close to O(TK) per iteration in practice; the comparisons are
  charts and visual judgements.
---
<!-- inactive-ok-file: THEORY-tmptl00j — Proposed; the sampler comparison this reading files, cited as open -->
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this reading bears on, cited as open -->

# NOTE-tmp2597d: Van Gael, Saatci, Teh and Ghahramani — Beam sampling for the infinite hidden Markov model

## Contribution

Exact Bayesian inference in the infinite HMM is blocked twice: with the
parameters fixed, forward–backward would have to sum over infinitely many
states, and with them integrated out every state is coupled to every
other. The one sampler available resampled one state at a time, which
mixes slowly when consecutive states are strongly dependent. The beam
sampler keeps the parameters, adds auxiliary slice variables that make
the set of admissible trajectories finite, and resamples the whole
trajectory at once by dynamic programming. It is exact, not a
truncation.

## Key insight

Under a slice u_t drawn uniformly below the probability of the transition
actually taken, only transitions with probability above u_t remain
possible. Since each row of the transition matrix sums to one and u_t > 0
almost surely, finitely many entries in each row exceed it. Conditioned on
u, the infinite HMM is a finite one, and forward filtering, backward
sampling applies.

## Assumptions

- **The iHMM (2)–(3), the HDP-HMM.** β ~ GEM(γ), π_k | β ~ DP(α, β),
  φ_k ~ H, s_t | s_{t−1} ~ Multinomial(π_{s_{t−1}}), y_t | s_t ~ F(φ_{s_t}),
  with s₀ = 0. Gamma hyperpriors on α and γ. Fixing β uniform on K states
  recovers MacKay's Bayesian HMM.
- **Why not α/K symmetric Dirichlets** (§2): independent priors on each
  row give no coupling across transitions out of different states, so the
  naive limit fails (Beal et al.).
- **The slice** (§4): u_t | π, s_{t−1}, s_t ~ Uniform(0, π_{s_{t−1}s_t}),
  with density I(0 < u_t < π_{s_{t−1}s_t})/π_{s_{t−1}s_t}.

## Key results

- **The beam sampler (§4).** Iterate: sample u; sample s by the forward
  recursion (4), p(s_t | y_{1:t}, u_{1:t}) ∝ p(y_t | s_t) Σ_{s_{t−1}:
  u_t < π_{s_{t−1}s_t}} p(s_{t−1} | y_{1:t−1}, u_{1:t−1}), then backward
  sampling p(s_t | s_{t+1}, …) ∝ p(s_t | y_{1:t}, u_{1:t}) I(u_{t+1} <
  π_{s_t s_{t+1}}); sample π from Dirichlet(n_k1 + αβ_1, …, n_kK + αβ_K,
  αΣ_{i>K}β_i); sample β through auxiliary counts m_ij with Stirling
  numbers of the first kind, then Dirichlet(m_·1, …, m_·K, γ); sample φ
  from its conditional, by Metropolis–Hastings if non-conjugate. Footnote
  2 gives the finiteness argument above.
- **Cost.** Worst case O(TK²) per iteration against Gibbs's O(TK). After
  about 20 iterations on the first synthetic set the sampler "on average
  considers a little more than one state" per step in (4), "closer to
  O(TK)"; "we have verified that this behavior is consistent also for
  larger iHMM's".
- **Synthetic, negatively correlated (§5.1).** Length 800 from a 4-state,
  almost cyclic HMM (1% self-transition), multinomial emissions; 20 runs
  from random initializations over 20 states; three settings: vague
  (α ~ Gamma(1, 1), γ ~ Gamma(2, 1)), strong (Gamma(6, 15), Gamma(16, 4)),
  and fixed α = 0.4, γ = 3.8, "chosen using the values the beam and Gibbs
  samplers converged to". Error is the Hamming distance after greedy
  matching. The beam sampler "discovers the underlying structure much
  faster" and "is insensitive to the prior while the performance of the
  Gibbs sampler becomes worse as we strengthen our prior beliefs".
- **Synthetic, positively correlated.** Length 4000, self-transitions
  0.75, 0.95 and 0.999, Gaussian emissions with informative (means −2, 4,
  1, −0.5) and uninformative (−1, 0.5, −0.5, 0) means, σ = 0.5; 60
  starts. With informative emissions both reduce the initial error by at
  least 50%; with uninformative emissions and strong persistence "the
  beam sampler mixes increasingly well, the Gibbs sampler suffers from
  slow random walk behavior".
- **Well-log data (§5.2).** 4050 nuclear-response measurements, a Cauchy
  likelihood (non-conjugate) with scale twice the empirical standard
  deviation, Gibbs by Neal's algorithm 8; 50 samples after 5000 burn-in,
  1000 apart. "After the first 10000 iterations, the Gibbs sampler hasn't
  discovered any structure while the beam sampler has"; later the beam
  sampler's co-segmentation matrix has grey areas (the outer segments
  share a state "90% of the time"), the Gibbs sampler's is black and
  white.
- **Alice in Wonderland (§5.3).** Train on 1000 characters, test on the
  next 4000, 31 symbols. The iHMMs "have superior predictive power when
  compared to the VB-HMM, even when we select the best number of hidden
  states (around K = 16)" among finite models of 1 to 50 states, and
  settle on about 16 states; beam and Gibbs "were not found to be significantly
  different" once both converged.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Conditioned on the slice variables, finitely many trajectories have positive probability | strong | footnote 2; [THEORY-tmp7bmmi](../theory.d/THEORY-tmp7bmmi.md) |
| C2 | The beam sampler leaves the iHMM posterior invariant (no truncation error) | strong | auxiliary-variable construction; checked on a finite HMM ([THEORY-tmp7bmmi](../theory.d/THEORY-tmp7bmmi.md)) |
| C3 | It mixes in fewer iterations than Gibbs on strongly correlated sequences | moderate | §5.1–5.2, charts and visual comparison ([THEORY-tmptl00j](../theory.d/THEORY-tmptl00j.md)) |
| C4 | Its cost per iteration is close to O(TK) in practice | weak to moderate | one plot on one synthetic set, and an unreported check on larger models |
| C5 | It is more robust to the hyperprior than Gibbs | moderate | §5.1, three settings, 20 runs, a chart |
| C6 | The iHMM predicts text better than a VB-HMM at its best K | moderate | §5.3, one book chapter, error bars in a chart |

## Concepts

- **iHMM / HDP-HMM**: an HMM with countably many states whose transition
  rows are DPs around a shared GEM base.
- **Beam sampler**: slice variables under each transition plus forward
  filtering, backward sampling over the admissible states.
- **Slice variable u_t**: an auxiliary uniform below the transition taken.

## Connections

It applies Walker's slice sampler for DP mixtures to the iHMM. The same
device, a slice under the stick of the last active feature, is Teh, Görür
and Ghahramani's for the IBP ([LIT-tmpfhqac](../literature.d/LIT-tmpfhqac.md)), and the infinite factorial HMM
([LIT-1577](../literature.d/LIT-1577.md), [NOTE-1199](NOTE-1199.md)) combines the two: a slice over the Markov IBP's
sticks and forward filtering, backward sampling per binary chain. It
cites the IBP paper as Griffiths and Ghahramani "2006" ([LIT-tmp3u0k8](../literature.d/LIT-tmp3u0k8.md), NIPS
18 of 2005).

## Bearing on the record

- **[LIT-1577](../literature.d/LIT-1577.md).** [NOTE-1199](NOTE-1199.md) says the iFHMM's inference "follows the beam
  sampler"; it does, with binary chains in place of the iHMM's single
  chain and the Markov IBP's sticks in place of the HDP's rows.
- **[CASE-165](../cases.d/CASE-165.md).** Nothing has been fitted for the case's model. If its
  sticky per-feature chains were fitted, the case's identifiability
  worries would be compounded by the Gibbs sampler's slow mixing on
  persistent states, which is the regime this paper reports as hardest
  for Gibbs (self-transition 0.999, uninformative emissions); a
  whole-chain sampler of this kind is the established remedy. A remark,
  not written into the case.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The mixing case is charts and eyes.** No effective sample sizes, no
  timings per second, and the well-log comparison is visual.
- **One fixed setting is circular**: α = 0.4, γ = 3.8 were chosen from the
  values the samplers themselves converged to.
- **Errors and slips.**
  - §4 says the slice could instead be drawn from "a distribution over
    [0, π_{s_t,s_{t−1}}]" where [0, π_{s_{t−1},s_t}] is meant.
  - The reference list gives Neal's *Slice sampling* (Annals of
    Statistics 31) as pp. 705–741; Teh, Görür and Ghahramani's citation of
    the same paper gives 705–767 ([NOTE-tmptxvho](NOTE-tmptxvho.md)). Not checked against the
    journal.
  - Daumé's name is garbled to "III, H. D." in the coalescent reference;
    "if ones desires", "individuals iHMM sampling schemes", "inspeech".
  - The almost cyclic sequence is called "strong negatively correlated";
    for categorical states the phrase means only that a state rarely
    repeats.

## Open questions

- How does the beam sampler compare with Gibbs per unit of computation,
  not per iteration, on long sequences with persistent states?
