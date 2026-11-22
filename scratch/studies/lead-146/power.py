"""Power simulation for the discriminating fidelity study (CASE-055), drafted for LEAD-146.

The quantity tested is the held-out increment in R^2 (Delta) that one set of
predictors adds over another in predicting receivers' recovery per rendering,
with cross-validation grouped by source item and a cluster bootstrap over
items for the interval. Decision rule (the draft's recommendation):

  defeated   iff the upper bound of the 90% interval for Delta is below the margin;
  supported  iff its lower bound is above the margin;
  otherwise  inconclusive.

Data-generating model, per language arm:
  items i = 1..I, renderings r = 1..R per item;
  latent z_ir = sqrt(r2b) B_ir + sqrt(dlat) T_ir + sqrt(icc) u_i + sqrt(rest) e_ir  (Var z = 1);
  B is the baseline's true signal, carried by p_b observed features of reliability rho;
  T is the increment's true signal, carried by p_t observed features of reliability rho;
  receivers: J per rendering; each answers "recovered" with
  P = logistic(logit(pi) + s z_ir + v), v ~ N(0, sigma_v^2) per answer (judge effect, not modelled);
  criterion y_ir = share of the J receivers who recovered the source act.

Run `python3 -I power.py results.json` (a few minutes on 4 CPUs).
"""
import json
import sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np

DEFAULTS = dict(
    R=6,          # renderings per item in the analysis set
    J=30,         # receivers per rendering
    r2b=0.30,     # latent variance the baseline explains
    p_b=6,        # baseline features
    p_t=3,        # increment features (CLAIM-228, CLAIM-231, CLAIM-259)
    rho=0.80,     # reliability of each human-rated feature (Stage 0 target)
    icc=0.10,     # item-level share of latent variance
    pi=0.65,      # mean prevalence of recovery
    s=1.2,        # SD of the latent logit
    sigma_v=0.5,  # per-answer judge noise on the logit scale
    folds=5,
    boot=500,
)
SIM_KEYS = ("R", "J", "r2b", "p_b", "p_t", "rho", "icc", "pi", "s", "sigma_v")


def simulate(rng, I, dlat, R, J, r2b, p_b, p_t, rho, icc, pi, s, sigma_v):
    n = I * R
    item = np.repeat(np.arange(I), R)
    B = rng.standard_normal(n)
    T = rng.standard_normal(n)
    u = rng.standard_normal(I)[item]
    rest = 1.0 - r2b - dlat - icc
    if rest < 0:
        raise ValueError("variance shares exceed 1")
    z = np.sqrt(r2b) * B + np.sqrt(dlat) * T + np.sqrt(icc) * u + np.sqrt(rest) * rng.standard_normal(n)
    a = np.log(pi / (1 - pi))
    logits = a + s * z[:, None] + sigma_v * rng.standard_normal((n, J))
    y = (rng.random((n, J)) < 1 / (1 + np.exp(-logits))).mean(axis=1)
    Xb = np.sqrt(rho) * B[:, None] + np.sqrt(1 - rho) * rng.standard_normal((n, p_b))
    Xt = np.sqrt(rho) * T[:, None] + np.sqrt(1 - rho) * rng.standard_normal((n, p_t))
    return item, y, Xb, Xt


def ols_cv_sq_errors(X, y, item, folds, rng):
    """Squared held-out errors of an OLS fit, cross-validated with folds grouped by item."""
    items = np.unique(item)
    perm = rng.permutation(items)
    fold_of_item = np.empty(items.max() + 1, dtype=int)
    fold_of_item[perm] = np.arange(len(perm)) % folds
    f = fold_of_item[item]
    Xc = np.column_stack([np.ones(len(y)), X])
    err = np.empty(len(y))
    for k in range(folds):
        tr, te = f != k, f == k
        beta, *_ = np.linalg.lstsq(Xc[tr], y[tr], rcond=None)
        err[te] = (y[te] - Xc[te] @ beta) ** 2
    return err, f


def delta_r2_with_ci(err_base, err_full, y, item, boot, rng, level=0.90):
    """Held-out Delta R^2 and a percentile cluster-bootstrap interval, resampling items."""
    I = item.max() + 1
    d = err_base - err_full
    d_item = np.bincount(item, weights=d, minlength=I)
    n_item = np.bincount(item, minlength=I)
    y_item = np.bincount(item, weights=y, minlength=I)
    y2_item = np.bincount(item, weights=y * y, minlength=I)

    def stat(W):
        n = W @ n_item
        ybar = (W @ y_item) / n
        var = (W @ y2_item) / n - ybar ** 2
        return (W @ d_item) / n / var

    est = float(stat(np.ones(I)))
    idx = rng.integers(0, I, size=(boot, I))
    W = np.zeros((boot, I))
    np.add.at(W, (np.repeat(np.arange(boot), I), idx.ravel()), 1)
    bs = stat(W)
    lo, hi = np.quantile(bs, [(1 - level) / 2, (1 + level) / 2])
    return est, float(lo), float(hi)


def one_run(seed, I, dlat, margin, params):
    rng = np.random.default_rng(seed)
    item, y, Xb, Xt = simulate(rng, I, dlat, **{k: params[k] for k in SIM_KEYS})
    eb, _ = ols_cv_sq_errors(Xb, y, item, params["folds"], np.random.default_rng(seed + 1))
    ef, _ = ols_cv_sq_errors(np.column_stack([Xb, Xt]), y, item, params["folds"],
                             np.random.default_rng(seed + 1))
    est, lo, hi = delta_r2_with_ci(eb, ef, y, item, params["boot"], rng)
    return est, hi < margin, lo > margin


def power(I, dlat, margin, reps=400, seed=0, **over):
    params = dict(DEFAULTS, **{k: v for k, v in over.items() if not k.startswith("_")})
    out = [one_run(seed + 1000 * k, I, dlat, margin, params) for k in range(reps)]
    est = np.array([o[0] for o in out])
    return dict(
        mean_delta_obs=float(est.mean()),
        sd_delta_obs=float(est.std()),
        p_defeat=float(np.mean([o[1] for o in out])),
        p_support=float(np.mean([o[2] for o in out])),
    )


def observed_scale(dlat, I=6000, seed=7, **over):
    """Large-sample observed held-out Delta R^2 for a latent increment dlat."""
    params = dict(DEFAULTS, **over)
    rng = np.random.default_rng(seed)
    item, y, Xb, Xt = simulate(rng, I, dlat, **{k: params[k] for k in SIM_KEYS})
    eb, _ = ols_cv_sq_errors(Xb, y, item, 5, rng)
    ef, _ = ols_cv_sq_errors(np.column_stack([Xb, Xt]), y, item, 5, rng)
    return float((eb.mean() - ef.mean()) / y.var())


def criterion_reliability(I=3000, seed=3, **over):
    """Split-half reliability of the criterion (share of J receivers), Spearman-Brown stepped up."""
    params = dict(DEFAULTS, **over)
    rng = np.random.default_rng(seed)
    p = {k: params[k] for k in SIM_KEYS}
    n, J = I * p["R"], p["J"]
    z = rng.standard_normal(n)
    a = np.log(p["pi"] / (1 - p["pi"]))
    logits = a + p["s"] * z[:, None] + p["sigma_v"] * rng.standard_normal((n, J))
    resp = rng.random((n, J)) < 1 / (1 + np.exp(-logits))
    h1, h2 = resp[:, : J // 2].mean(1), resp[:, J // 2:].mean(1)
    r = np.corrcoef(h1, h2)[0, 1]
    return float(2 * r / (1 + r))


def _task(args):
    I, dlat, margin, over = args
    return (I, dlat, margin, over, power(I, dlat, margin, **over))


def main(out="results.json"):
    lat_grid = [0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20]
    calib = {str(d): observed_scale(d) for d in lat_grid}
    obs = [calib[str(d)] for d in lat_grid]
    margins = [0.01, 0.02, 0.05]
    items = [40, 60, 80, 120, 160, 240, 320]
    tasks = []
    for m in margins:
        lat_alt = float(np.interp(2 * m, obs, lat_grid))  # latent increment observed as ~2m
        for I in items:
            tasks.append((I, 0.0, m, {}))
            tasks.append((I, lat_alt, m, {}))
        # size of the defeat rule: true observed increment equal to the margin
        lat_m = float(np.interp(m, obs, lat_grid))
        for I in (80, 160, 240, 320):
            tasks.append((I, lat_m, m, {"_role": "size"}))
    for I in (400, 480):  # how far margin 0.02 needs to go
        tasks.append((I, 0.0, 0.02, {}))
        tasks.append((I, float(np.interp(0.04, obs, lat_grid)), 0.02, {}))
    lat02 = float(np.interp(0.04, obs, lat_grid))
    for over in ({"J": 15}, {"rho": 0.6}, {"R": 3}):
        for I in (120, 160, 240, 320):
            tasks.append((I, 0.0, 0.02, over))
            tasks.append((I, lat02, 0.02, over))
    with ProcessPoolExecutor() as ex:
        res = list(ex.map(_task, tasks))
    rows = [dict(items=I, renderings=I * over.get("R", DEFAULTS["R"]), latent_delta=round(dlat, 4),
                 margin=m, overrides=over, **r) for (I, dlat, m, over, r) in res]
    result = dict(
        defaults=DEFAULTS,
        criterion_reliability={"J=30": criterion_reliability(), "J=15": criterion_reliability(J=15)},
        calibration_latent_to_observed=calib,
        rows=rows,
    )
    with open(out, "w") as fh:
        json.dump(result, fh, indent=1)
    for r in rows:
        print(r)


if __name__ == "__main__":
    main(*sys.argv[1:])
