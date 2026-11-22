"""Decay slope by task type, from Tatel & Ackerman's posted data (OSF bgfyp).

Usage: python3 -I by_task_type.py <path to "Study Data Independent Samples
Effect Size Formula.xlsx"> [out.json]

Follows the authors' R script (OSF file zq35p): independent-samples d,
vi = (n1+n2)/(n1*n2) + d^2/(2(n1+n2)), REML, retention intervals of 60
months or more dropped for accuracy and speed (not for mixed), clusters
= source_file_me x study_number x group_me.
"""
import json
import sys
import os

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from metareg import metareg  # noqa: E402


def load(path):
    df = pd.read_excel(path, sheet_name="Data")
    df = df.dropna(subset=["cohens_d_is_use", "n1", "n2",
                           "retention_interval_months"])
    df["vi"] = (df.n1 + df.n2) / (df.n1 * df.n2) + df.cohens_d_is_use ** 2 / (2 * (df.n1 + df.n2))
    def s(c):
        return df[c].astype(object).where(df[c].notna(), "NA").map(str)
    df["dependency"] = s("source_file_me") + "_" + s("study_number") + "_" + s("group_me")
    return df


def subset(df, measure):
    d = df[df.performance_measure_type == measure]
    if measure != "Mixed":
        d = d[d.retention_interval_months < 60]
    return d


def fit_main(d):
    X = np.column_stack([np.ones(len(d)), d.retention_interval_months])
    o = metareg(d.cohens_d_is_use, d.vi, X, d.dependency)
    return {"k": o["k"], "clusters": o["clusters"], "intercept": o["beta"][0],
            "slope": o["beta"][1], "slope_se_robust": o["se_robust"][1],
            "tau2": o["tau2"]}


def fit_by_type(d, col, ref):
    """Interaction model, as the authors fit it; returns each level's
    implied slope and intercept with robust SEs (by delta method)."""
    levels = [ref] + sorted(l for l in d[col].dropna().unique() if l != ref)
    d = d[d[col].isin(levels)]
    ri = d.retention_interval_months.to_numpy()
    cols, names = [np.ones(len(d)), ri], ["int", "ri"]
    for l in levels[1:]:
        ind = (d[col] == l).to_numpy().astype(float)
        cols += [ind, ind * ri]
        names += [f"{l}", f"ri:{l}"]
    X = np.column_stack(cols)
    o = metareg(d.cohens_d_is_use, d.vi, X, d.dependency)
    bread = None
    res = {}
    # recover covariance for implied slopes
    from metareg import _fit_given_tau2
    beta, w, XtWX = _fit_given_tau2(d.cohens_d_is_use.to_numpy(float),
                                    d.vi.to_numpy(float), X, o["tau2"])
    bread = np.linalg.inv(XtWX)
    r = d.cohens_d_is_use.to_numpy(float) - X @ beta
    p = X.shape[1]
    meat = np.zeros((p, p))
    cl = d.dependency.to_numpy()
    ids = np.unique(cl)
    for c in ids:
        m = cl == c
        u = (X[m].T * w[m]) @ r[m]
        meat += np.outer(u, u)
    V = bread @ meat @ bread * (len(ids) / (len(ids) - p))
    for i, l in enumerate(levels):
        a = np.zeros(p)
        s = np.zeros(p)
        a[0] = 1
        s[1] = 1
        if i > 0:
            a[names.index(f"{l}")] = 1
            s[names.index(f"ri:{l}")] = 1
        sub = d[d[col] == l]
        res[str(l)] = {
            "k": int(len(sub)),
            "k_over_6_months": int((sub.retention_interval_months > 6).sum()),
            "max_months": float(sub.retention_interval_months.max()),
            "intercept": float(a @ beta),
            "slope": float(s @ beta),
            "slope_se_robust": float(np.sqrt(s @ V @ s)),
            "interaction_vs_ref": None if i == 0 else float(beta[names.index(f"ri:{l}")]),
        }
    return {"tau2": o["tau2"], "k": o["k"], "clusters": len(ids), "levels": res}


def main(path, out=None):
    df = load(path)
    result = {"main": {}, "task_domain": {}, "task_realism": {}}
    for m in ["Accuracy", "Speed", "Mixed"]:
        d = subset(df, m)
        result["main"][m] = fit_main(d)
        ref_dom = "Laboratory/Artificial"
        for col in ["task_domain", "task_realism"]:
            vals = d[col].dropna().unique()
            ref = next((v for v in vals if str(v).lower().startswith("lab")), sorted(vals)[0])
            try:
                result[col][m] = fit_by_type(d, col, ref)
            except np.linalg.LinAlgError as e:
                result[col][m] = {"error": str(e)}
    # Sensitivity: is the type difference curvature in disguise? Refit on
    # intervals both types cover (laboratory accuracy data rarely pass 6
    # months), at caps of 3, 6 and 14 months.
    result["capped"] = {}
    for m in ["Accuracy", "Speed"]:
        for cap in [1, 3, 6, 14]:
            d = subset(df, m)
            d = d[d.retention_interval_months <= cap]
            for col in ["task_realism", "task_domain"]:
                vals = d[col].dropna().unique()
                ref = next((v for v in vals if str(v).lower().startswith("lab")), sorted(vals)[0])
                try:
                    result["capped"][f"{m}|{col}|<= {cap} months"] = fit_by_type(d, col, ref)
                except np.linalg.LinAlgError as e:
                    result["capped"][f"{m}|{col}|<= {cap} months"] = {"error": str(e)}

    def conv(o):
        if isinstance(o, dict):
            return {k: conv(v) for k, v in o.items()}
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        return o
    result = conv(result)
    txt = json.dumps(result, indent=1)
    if out:
        with open(out, "w") as f:
            f.write(txt)
    print(txt)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
