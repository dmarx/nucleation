# LEAD-128 study: fitting the EVC effort-cost model to COG-ED data

Carries out LEAD-128: "Find or make a fit of the expected-value-of-control
model in which control intensity falls with its cost."

## Route chosen

No published fit was found that plainly demonstrates control intensity
*falling with its cost* as its model-compared result (the closest open EVC
accumulator fits — Leng, Yee, Ritz & Shenhav 2021, PLoS Comput Biol,
PMC8746743, CC BY; Masís Obando, Musslick & Cohen 2025, PNAS, PMC12595486 —
demonstrate the complementary *payoff* direction, control rising with
incentive/benefit). So the fit was made here, as the lead provides for.

## Data

Cognitive Effort Discounting (COG-ED-style) choices from OSF project
**vnj8x**, "Cognitive and Affective Discounting", **CC-BY 4.0**, public.
Source article: Scheffel, Rausch et al. (2023), "Need for Cognition is
associated with a preference for higher task load in effort discounting",
*Scientific Reports*, PMC10636210 (CC BY). 122 participants' `*_ED.csv`
files; 4 n-back levels (1-4); in each pairwise block one level is fixed at
2€ and the other titrated over 6 bisection steps to indifference.

Downloads live only in the session scratchpad (`lead-128/osf_raw/`, ~1 MB)
and are **not committed** (they are not ours to redistribute here; CC-BY
attribution is given above). No email or personal data was sent to any
service (ADR-008).

## How to rerun

```
# 1. collect the ED file download URLs (OSF API)
python3 -I collect_urls.py <scratch_dir>
# 2. download them into <scratch_dir>/osf_raw  (minutes; OSF API 500s retry)
python3 -I download_ed.py <scratch_dir>
# 3. fit and print JSON results
OMP_NUM_THREADS=1 python3 -I evc_fit.py <scratch_dir>/osf_raw
# tests (parameter recovery + model comparison on synthetic data)
OMP_NUM_THREADS=1 python3 -I -m pytest test_evc_fit.py -q
```

CPU only, single BLAS thread, runs in seconds (download aside). Results are
in `fit_result.json`; `summary.md` states them in words.

## Model

Each trial offers two options, each a pair (n, r): n = n-back level (the
control intensity on offer), r = its reward. Net subjective value
V(n, r) = r − c(n), with c(1) := 0. Choice by softmax,
P(A) = logistic(β·(V_A − V_B)). This is the EVC computation (LIT-585,
THEORY-070): payoff traded against an intensity-dependent cost. Compared
against a reward-only null (all c(n) = 0). A per-participant linear variant
c(n) = k·(n−1) gives each agent's marginal cost of control k (euros/level).
