# LEAD-190: population comparisons for the authority-grant claims

Role-indexed against scalar grants (CLAIM-281), and operators bound by A2's
two grant conditions against unbound ones (CLAIM-285), in a population built
on LEAD-090's model (CASE-363). See `record/changelog.d/lead-190.md` for the
codes filed.

## Rerun

    cd scratch/studies/lead-190
    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider --rootdir=. test_model.py   # 27 tests, < 1 s
    python3 -I run.py            # e1..e6, about 20 min on one thread
    python3 -I run.py e3 e4      # or some of them

`model.py` loads `../lead-090/model.py` by path and does not modify it;
`test_reader_is_lead090_institution` checks that one reader with two sources
is LEAD-090's mean field to 1e-12, in Regime A and Regime B.

## Model

See the docstring of `model.py`. In short:

- N operators (20; 40 in e5), half on each side (s = ±1) in random order,
  preferred policies s·U(0.3, 1), relevance r ~ U(0.4, 0.9) independent of
  side.
- **Meaning layer** (LEAD-090 per reader): reader i frames by its meaning;
  source j's items lean to its side by σ (and by its own meaning, φ_s);
  i's meaning moves toward the critic-weighted share of A-items; critic
  weights W_i (over all sources, i included) relax toward
  softmax(g·score), score = ζ·agreement + (1 − ζ)·observed relevance.
- **Decision layer**: grants E (rows ≤ 1, E_ii = 0), authority by one-hop,
  leave-one-out (CLAIM-502) or damped recursive (CLAIM-282) aggregation
  with η = 0.5; decision p* the authority-weighted mean of preferences
  (CLAIM-375); objective realized policy −(p* − p_i)² or authority held
  log g_i, less a grant cost; projected gradient ascent with exact
  gradients.
- **Schemes** (CLAIM-281): `scalar-agree` (one row, scored by agreement:
  evidence weight and decision grant), `scalar-comp` (one row, by
  relevance), `scalar-policy` (one row, moved by the policy objective; the
  ungranted share is weight on one's own retrieval), `role` (critic row by
  relevance, decision row by policy), `role-agree` (two rows, critic by
  agreement).

## Linearization (`population_jacobian`, tested)

At m = 0, uniform W, balanced corpus and equal relevance, in (m_i, a_i),
a_i = Σ_j W_ij s_j:

    m_i' = (1 − ρ(1 − φ')) m_i + ρσ a_i + ρφ_s' mean_j m_j
    a_i' = δ a_i + (1 − δ)(gζσ/2) m_i

The uniform mode (the population captured as one) is unstable iff
gζσ²/2 > 1 − φ' − φ_s'; every differentiating mode iff gζσ²/2 > 1 − φ'.
With ζ = 1, φ_s = 0 both are CLAIM-947's threshold.

## Experiments (`run.py`, results in `results/`)

- e1: the five schemes on 30 populations, mean field, φ_s ∈ {0, 0.2},
  b ∈ {0, 0.05}, polarized (m0 = 0.2 s) and near-symmetric starts.
- e2: the same at agent level (k = 50 items), 20 seeds, polarized start.
- e3: the independence ζ of the critic score swept in the role scheme
  against the thresholds.
- e4: the grant game, aggregation × objective, 30 populations, quadratic
  and linear cost; delegation mass, aligned share against chance,
  within-side preference for extremity or nearness, reach beyond one hop
  and authority returned to oneself.
- e5: the bound and unbound cells and three schemes at N = 40.
- e6: where the role scheme's shared meaning settles, against the corpus
  imbalance and the relevance-weighted side of the specialists, for three
  ranges of relevance.
