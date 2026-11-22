"""Random-effects meta-regression (REML) with cluster-robust standard errors.

Mirrors metafor's rma(method="REML") followed by robust(..., cluster=...),
with a CR1 small-sample correction (clubSandwich uses CR2, so robust SEs
here are close to, not identical with, the authors').
"""
import numpy as np
from scipy.optimize import minimize_scalar


def _fit_given_tau2(y, v, X, tau2):
    w = 1.0 / (v + tau2)
    XtW = X.T * w
    XtWX = XtW @ X
    beta = np.linalg.solve(XtWX, XtW @ y)
    return beta, w, XtWX


def reml_tau2(y, v, X):
    def negll(t):
        beta, w, XtWX = _fit_given_tau2(y, v, X, t)
        r = y - X @ beta
        return 0.5 * (np.sum(np.log(v + t)) + np.linalg.slogdet(XtWX)[1]
                      + np.sum(w * r * r))
    hi = max(10.0, 10 * np.var(y))
    res = minimize_scalar(negll, bounds=(0.0, hi), method="bounded",
                          options={"xatol": 1e-8})
    return max(res.x, 0.0)


def metareg(y, v, X, cluster=None):
    y, v, X = np.asarray(y, float), np.asarray(v, float), np.asarray(X, float)
    tau2 = reml_tau2(y, v, X)
    beta, w, XtWX = _fit_given_tau2(y, v, X, tau2)
    bread = np.linalg.inv(XtWX)
    out = {"beta": beta, "se": np.sqrt(np.diag(bread)), "tau2": tau2,
           "k": len(y)}
    if cluster is not None:
        cluster = np.asarray(cluster)
        r = y - X @ beta
        p = X.shape[1]
        meat = np.zeros((p, p))
        ids = np.unique(cluster)
        for c in ids:
            m = cluster == c
            u = (X[m].T * w[m]) @ r[m]
            meat += np.outer(u, u)
        n_c = len(ids)
        V = bread @ meat @ bread * (n_c / (n_c - p))
        out["se_robust"] = np.sqrt(np.diag(V))
        out["clusters"] = n_c
    return out
