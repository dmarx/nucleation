#!/usr/bin/env python3
"""Fit an EVC effort-cost softmax choice model to COG-ED effort-discounting data.

Model (one agent electing how much cognitive control to deploy):
  Each effort-discounting trial offers two options, each a pair (n, r):
  n = n-back level (the control intensity on offer), r = its monetary reward.
  Net subjective value of an option:   V(n, r) = r - c(n)
  c(n) is the intrinsic cost of exerting control at level n (c(1) := 0 anchor).
  Choice by softmax with inverse temperature beta:
     P(choose option A) = logistic( beta * ( V_A - V_B ) )
                        = logistic( beta * ( (r_A - r_B) - (c(n_A) - c(n_B)) ) )

This is the expected-value-of-control computation of Shenhav/Botvinick/Cohen
(LIT-585, THEORY-070) applied to a revealed-preference task: an agent trades a
control signal's payoff (r) against its intensity-dependent cost c(n), and the
optimal choice maximises net value.

Two nested models are compared:
  FULL : beta, c(2), c(3), c(4) free (c(1)=0)           -- cost term present
  NULL : beta free, all c(n)=0 (reward-only)            -- no cost term

promote_when (1) of THEORY-070, on this operationalisation:
  * control intensity (which n-back the agent elects) rises with the payoff for
    it at fixed difficulty: beta > 0 (more reward for an option -> chosen more);
  * and falls with its cost: c(n) increasing in n (higher-n options chosen less
    at matched reward);
  * better than a model without the cost term: FULL beats NULL.

Pure numpy/scipy, CPU, single-threaded. No network, no personal data.
"""
import os, csv, glob, json
import numpy as np
from scipy.optimize import minimize
from scipy.stats import chi2

LEVELS = (1, 2, 3, 4)


def load_trials(raw_dir):
    """Return (participant, nA, rA, nB, rB, chose_A) rows from all *_ED.csv.

    A = left option, B = right option, chose_A = 1 if left button clicked.
    """
    rows = []
    for path in sorted(glob.glob(os.path.join(raw_dir, "*_ED.csv"))):
        pid = os.path.basename(path).split("_")[0]
        for r in csv.DictReader(open(path, encoding="utf-8-sig")):
            if (r.get("Currentstep", "") or "").strip() == "":
                continue
            try:
                nA = int(float(r["EDleftbutton.nback"]))
                nB = int(float(r["EDrightbutton.nback"]))
                rA = float(r["EDleftbutton.value"])
                rB = float(r["EDrightbutton.value"])
            except (ValueError, KeyError):
                continue
            lw = (r.get("EDleftbutton.wasclicked", "") or "").strip()
            rw = (r.get("EDrightbutton.wasclicked", "") or "").strip()
            name = (r.get("EDclick.clicked_name", "") or "").strip()
            if lw in ("1", "1.0") and rw in ("0", "0.0"):
                chose_A = 1
            elif rw in ("1", "1.0") and lw in ("0", "0.0"):
                chose_A = 0
            elif name == "EDleftbutton":
                chose_A = 1
            elif name == "EDrightbutton":
                chose_A = 0
            else:
                continue
            if nA not in LEVELS or nB not in LEVELS:
                continue
            rows.append((pid, nA, rA, nB, rB, chose_A))
    return rows


def _design(rows):
    nA = np.array([r[1] for r in rows])
    rA = np.array([r[2] for r in rows])
    nB = np.array([r[3] for r in rows])
    rB = np.array([r[4] for r in rows])
    y = np.array([r[5] for r in rows], dtype=float)
    # one-hot difference of the cost-bearing levels 2,3,4 (level 1 anchored to 0)
    dcost = np.zeros((len(rows), 3))  # columns: c2, c3, c4
    for j, lev in enumerate((2, 3, 4)):
        dcost[:, j] = (nA == lev).astype(float) - (nB == lev).astype(float)
    dr = rA - rB
    return dr, dcost, y


def _nll(params, dr, dcost, y, with_cost):
    beta = params[0]
    if with_cost:
        c = params[1:]           # c2, c3, c4
        v = beta * (dr - dcost @ c)
    else:
        v = beta * dr
    # stable log-logistic
    # p = sigmoid(v); nll = -sum(y*log p + (1-y)*log(1-p))
    ll = y * v - np.logaddexp(0.0, v)
    return -float(np.sum(ll))


def fit(dr, dcost, y, with_cost=True):
    if with_cost:
        x0 = np.array([2.0, 0.3, 0.6, 0.9])
    else:
        x0 = np.array([2.0])
    res = minimize(_nll, x0, args=(dr, dcost, y, with_cost),
                   method="Nelder-Mead",
                   options={"xatol": 1e-7, "fatol": 1e-9, "maxiter": 20000,
                            "maxfev": 20000})
    return res


def fit_all(rows):
    dr, dcost, y = _design(rows)
    full = fit(dr, dcost, y, with_cost=True)
    null = fit(dr, dcost, y, with_cost=False)
    nllf, nlln = full.fun, null.fun
    kf, kn = 4, 1
    n = len(y)
    out = {
        "n_trials": int(n),
        "n_participants": len(set(r[0] for r in rows)),
        "beta_full": float(full.x[0]),
        "cost": {"1": 0.0, "2": float(full.x[1]),
                 "3": float(full.x[2]), "4": float(full.x[3])},
        "beta_null": float(null.x[0]),
        "nll_full": float(nllf), "nll_null": float(nlln),
        "aic_full": float(2 * kf + 2 * nllf),
        "aic_null": float(2 * kn + 2 * nlln),
        "bic_full": float(kf * np.log(n) + 2 * nllf),
        "bic_null": float(kn * np.log(n) + 2 * nlln),
        "lr_stat": float(2 * (nlln - nllf)),
        "lr_df": kf - kn,
        "lr_p": float(chi2.sf(2 * (nlln - nllf), kf - kn)),
    }
    return out


def per_participant(rows):
    """Fit cost c(4) sign per participant (>=12 trials). Return summary."""
    by = {}
    for r in rows:
        by.setdefault(r[0], []).append(r)
    costs4, increasing = [], 0
    nfit = 0
    for pid, rs in by.items():
        if len(rs) < 12:
            continue
        dr, dcost, y = _design(rs)
        if y.sum() == 0 or y.sum() == len(y):
            continue  # degenerate: always one side; cost not identified
        res = fit(dr, dcost, y, with_cost=True)
        c2, c3, c4 = res.x[1], res.x[2], res.x[3]
        nfit += 1
        costs4.append(float(c4))
        if c2 <= c3 <= c4 and c4 > 0:
            increasing += 1
    return {"n_fit": nfit, "median_c4": float(np.median(costs4)) if costs4 else None,
            "frac_increasing_cost": (increasing / nfit) if nfit else None}


def _nll_linear(params, dr, dlev, y):
    """Linear cost c(n) = k * (n - 1); params = [beta, k]."""
    beta, k = params
    v = beta * (dr - k * dlev)
    ll = y * v - np.logaddexp(0.0, v)
    return -float(np.sum(ll))


def fit_linear_per_participant(rows):
    """Per participant: V = r - k*(n-1). Return distribution of marginal cost k
    (euros of reward foregone per n-back level). Separable participants
    (always chose the lower- or higher-effort option) are reported apart."""
    by = {}
    for r in rows:
        by.setdefault(r[0], []).append(r)
    ks, n_sep_averse, n_sep_seek, n_fit = [], 0, 0, 0
    for pid, rs in by.items():
        nA = np.array([r[1] for r in rs]); rA = np.array([r[2] for r in rs])
        nB = np.array([r[3] for r in rs]); rB = np.array([r[4] for r in rs])
        y = np.array([r[5] for r in rs], float)
        dr = rA - rB
        dlev = (nA - 1.0) - (nB - 1.0)  # = nA - nB
        # did the participant ever take less money to avoid higher effort,
        # or ever take less money to get higher effort? identify separability
        chose_lower_effort = ((y == 1) & (nA < nB)) | ((y == 0) & (nB < nA))
        if y.sum() == 0 or y.sum() == len(y):
            # always one button; use effort direction of chosen option
            if chose_lower_effort.mean() > 0.5:
                n_sep_averse += 1
            else:
                n_sep_seek += 1
            continue
        res = minimize(_nll_linear, np.array([1.0, 0.3]), args=(dr, dlev, y),
                       method="Nelder-Mead",
                       options={"xatol": 1e-7, "fatol": 1e-9,
                                "maxiter": 20000, "maxfev": 20000})
        beta, k = res.x
        # sign convention: positive k = cost rises with n -> intensity falls
        ks.append(float(k)); n_fit += 1
    ks = np.array(ks)
    return {
        "n_fit": n_fit,
        "n_always_avoided_higher_effort": n_sep_averse,
        "n_always_sought_higher_effort": n_sep_seek,
        "median_k_eur_per_level": float(np.median(ks)) if len(ks) else None,
        "iqr_k_eur_per_level": (
            [float(np.percentile(ks, 25)), float(np.percentile(ks, 75))]
            if len(ks) else None),
        "frac_k_positive": float(np.mean(ks > 0)) if len(ks) else None,
        "frac_effort_averse_incl_separable": (
            float((np.sum(ks > 0) + n_sep_averse)
                  / (n_fit + n_sep_averse + n_sep_seek))
            if (n_fit + n_sep_averse + n_sep_seek) else None),
    }


def group_subjective_values(rows):
    """Model-free check, the paradigm's own subjective value (Scheffel et al.):
    in each pair one option is fixed at 2 euro and the other titrated; the
    titrated (equal-reward-preferred) level has SV := 1, and the fixed level
    has SV := final titrated reward / 2. Each participant's SV for a level is
    the mean over pairs in which it appeared; the group mean per level is
    returned. Effort-averse populations give SVs that fall with n-back."""
    by = {}
    for r in rows:
        by.setdefault(r[0], []).append(r)
    group = {lev: [] for lev in LEVELS}
    for pid, rs in by.items():
        part = {lev: [] for lev in LEVELS}
        block = []
        last_pair = None
        for r in rs + [(None,) * 6]:
            pair = (r[1], r[3]) if r[0] is not None else None
            if pair != last_pair and block:
                lv = [b[2] for b in block]; rv = [b[4] for b in block]
                left_lev, right_lev = block[0][1], block[0][3]
                if len(set(lv)) > 1:            # left titrated
                    tlev, flev, tfinal = left_lev, right_lev, block[-1][2]
                elif len(set(rv)) > 1:          # right titrated
                    tlev, flev, tfinal = right_lev, left_lev, block[-1][4]
                else:
                    tlev = flev = None
                if tlev in part:
                    part[tlev].append(1.0)              # titrated/preferred
                    part[flev].append(tfinal / 2.0)     # fixed level's SV
                block = []
            if r[0] is not None:
                block.append(r)
            last_pair = pair
        for lev in LEVELS:
            if part[lev]:
                group[lev].append(float(np.mean(part[lev])))
    return {str(lev): (float(np.mean(v)) if v else None)
            for lev, v in group.items()}


def main():
    import sys
    raw = sys.argv[1]
    rows = load_trials(raw)
    out = fit_all(rows)
    out["per_participant"] = per_participant(rows)
    out["per_participant_linear"] = fit_linear_per_participant(rows)
    out["group_norm_indiff_reward_by_level"] = group_subjective_values(rows)
    # predicted choice of higher-n option at matched reward (dr=0), per level pair
    c = [0.0, out["cost"]["2"], out["cost"]["3"], out["cost"]["4"]]
    b = out["beta_full"]
    pref = {}
    for hi in (2, 3, 4):
        # higher-n option (level hi) vs level 1, matched reward
        v = b * (0.0 - (c[hi - 1] - 0.0))
        pref[f"{hi}vs1"] = float(1 / (1 + np.exp(-v)))
    out["p_choose_higher_n_at_equal_reward"] = pref
    print(json.dumps(out, indent=2))
    json.dump(out, open(os.path.join(os.path.dirname(raw) or ".",
                                     "fit_result.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
