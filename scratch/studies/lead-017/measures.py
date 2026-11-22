"""Measures that read Observables only, never the World or Latent.

Registration of H's evaluation is operationalized as dependence of the
organization's record on H's evaluation, holding fixed what else could
carry the same information into the record: the outcome, whether it was
pursued, and P's learned value. Two forms:

- passive: does the record predict the liking assay beyond the outcome,
  the action and P's value? (F-test of the record block)
- interventional: does the record respond to the experimenter's
  randomized perturbation of H (delta), holding the same covariates?
  delta perturbs the evaluation, not the registration gain or the
  authority, which are the setting.

Authority (the endorsement relation's effect) is operationalized as the
dependence of next-step pursuit on delta, in a linear and a quadratic term.

Each score is -log10 of an F-test p-value, so it is comparable across
agents; thresholds are chosen on calibration agents and applied to held-out
agents and held-out worlds.
"""
from __future__ import annotations

import numpy as np
from scipy import stats

from orgmodel import DEVAL_START, Observables


def _ftest(y, X0, X1):
    """F-test that block X1 adds to X0 in OLS of y. Returns -log10 p."""
    X = np.hstack([X0, X1])
    n = len(y)
    b0, *_ = np.linalg.lstsq(X0, y, rcond=None)
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    rss0 = np.sum((y - X0 @ b0) ** 2)
    rss1 = np.sum((y - X @ b) ** 2)
    df1 = X1.shape[1]
    df2 = n - X.shape[1]
    if rss1 <= 0 or df2 <= 0:
        return np.inf
    F = ((rss0 - rss1) / df1) / (rss1 / df2)
    p = stats.f.sf(max(F, 0.0), df1, df2)
    return -np.log10(max(p, 1e-300))


def _covariates(obs: Observables, i, t0=DEVAL_START):
    T = obs.pursued.shape[1]
    sl = slice(t0, T)
    p = obs.pursued[i, sl]
    v = obs.outcome[sl]
    V = obs.value[i, sl]
    V1 = np.r_[V[1:], V[-1]]  # P's value after this step's update
    return np.column_stack([np.ones_like(p), p, p * v, V, V1, p * V, v]), sl


def registration_passive(obs: Observables, use="record"):
    n = obs.pursued.shape[0]
    out = np.empty(n)
    for i in range(n):
        X0, sl = _covariates(obs, i)
        Z = obs.record[i, sl] if use == "record" else obs.report[i, sl][:, None]
        m = obs.delta[i, sl] == 0  # unperturbed steps only: passive history
        out[i] = _ftest(obs.assay[i, sl][m], X0[m], Z[m])
    return out


def registration_interventional(obs: Observables, use="record"):
    n = obs.pursued.shape[0]
    out = np.empty(n)
    for i in range(n):
        X0, sl = _covariates(obs, i)
        Z = obs.record[i, sl] if use == "record" else obs.report[i, sl][:, None]
        out[i] = _ftest(obs.delta[i, sl], X0, Z)
    return out


def authority_interventional(obs: Observables):
    """Does H's perturbation at t move pursuit at t+1?"""
    n, T = obs.pursued.shape
    out = np.empty(n)
    for i in range(n):
        X0, sl = _covariates(obs, i)
        X0, d = X0[:-1], obs.delta[i, sl][:-1]
        y = obs.pursued[i, sl][1:]
        out[i] = _ftest(y, X0, np.column_stack([d, d ** 2]))
    return out


def behaviour_features(obs: Observables, with_assay=True):
    """Summary features of pursuit (and its coupling to the assay) only;
    no record, no report, no probe."""
    p = obs.pursued
    T = p.shape[1]
    f = [p[:, s:s + 40].mean(1) for s in range(DEVAL_START, T, 40)]
    f.append(np.mean(p[:, 1:] * p[:, :-1], 1))  # persistence
    if with_assay:
        a = obs.assay
        sl = slice(DEVAL_START, T - 1)
        ac = a[:, sl] - a[:, sl].mean(1, keepdims=True)
        pc = p[:, DEVAL_START + 1:] - p[:, DEVAL_START + 1:].mean(1, keepdims=True)
        f.append((ac * pc).mean(1) / (ac.std(1) * pc.std(1) + 1e-9))
    return np.column_stack(f)


def auc(pos, neg):
    """Mann-Whitney AUC of scores pos over neg."""
    allv = np.r_[pos, neg]
    r = stats.rankdata(allv)
    return (r[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))


def lda_cv_accuracy(X, y, k=5, seed=0):
    """k-fold accuracy of a shrinkage LDA, numpy only."""
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(y))
    folds = np.array_split(idx, k)
    classes = np.unique(y)
    correct = 0
    for f in folds:
        tr = np.setdiff1d(idx, f)
        mu = np.stack([X[tr][y[tr] == c].mean(0) for c in classes])
        S = np.cov((X[tr] - mu[np.searchsorted(classes, y[tr])]).T)
        S = np.atleast_2d(S)
        S = 0.9 * S + 0.1 * np.eye(len(S)) * np.trace(S) / len(S)
        Si = np.linalg.inv(S)
        sc = X[f] @ Si @ mu.T - 0.5 * np.sum(mu @ Si * mu, 1)
        correct += np.sum(classes[sc.argmax(1)] == y[f])
    return correct / len(y)
