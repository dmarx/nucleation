"""LEAD-144: CASE-165's finite beta-Bernoulli feature model fitted to a
mechanistic organizational simulator that does not assume its prior, against a
shared-driver null, scored on held-out interventions on the coupling.

Worlds (all linear-Gaussian, members' daily activity x_t in R^N):
  coupled : x_{t+1} = a x_t + c * Adj/dbar x_t + xi        (interaction along C)
  driver  : x_{t+1} = a x_t + g M d_t + xi,  d AR(1)       (no interaction; C inert)
  mixed   : half the coupling of `coupled`, plus a driver
The driver gain is tuned per seed so the within-group mean correlation equals
the coupled world's: the null is matched on the statistic a mode-finder sees.

Models (fitted on observational data only; every intervention is held out):
  F-raw : CASE-165's feature model on activity (finite beta-Bernoulli, K=16,
          alpha=3, static allocation, Gaussian loadings, AR(1) activations),
          no relations. Two intervention readings: 'exo' (features are causes
          of members, so a pulse to a member moves nobody and a cut changes
          nothing) and 'con' (features are realized by their holders, so a
          pulse moves co-holders as conditioning predicts, and cutting a
          group dissolves the features it mostly holds).
  F-self: the same features plus each member's own AR term (the private map),
          no relations; features exogenous.
  R     : VAR(1) restricted to the communication graph C plus self, no modes.
  FR    : R plus lagged exogenous AR(1) features (a factor-augmented VAR): the
          features are found on the innovations of each member's own AR.
Comparators added after the first trial: FR-oracle (R plus the true driver,
observed; the ceiling for any feature estimate of it) and R-int (R fitted to a
run with random shocks to half the members, scored on the other half's pulses
and on the cuts).
Interventions: a pulse to each member (response of the others, h=1..5) and a
cut of each group's internal edges (change in the group's mean pairwise
correlation at stationarity).
"""
import json
import os
import sys
import time

import numpy as np
from scipy.linalg import solve_discrete_lyapunov

N, G, T, K, ALPHA = 24, 6, 600, 16, 3.0
A_SELF, PHI_D, H = 0.5, 0.8, 5
PULSE = 1.0  # in standardized units of the pulsed member


# ---------------------------------------------------------------- simulator
def make_org(rng):
    """Overlapping working groups and a communication graph built from them."""
    M = np.zeros((N, G))
    for e in range(N):
        M[e, e % G] = 1
    for e in rng.choice(N, N // 3, replace=False):
        M[e, rng.choice([g for g in range(G) if M[e, g] == 0])] = 1
    Adj = ((M @ M.T) > 0).astype(float)
    np.fill_diagonal(Adj, 0)
    # a few cross-group ties
    for _ in range(N // 4):
        i, j = rng.choice(N, 2, replace=False)
        Adj[i, j] = Adj[j, i] = 1
    return M, Adj


def coupling_matrix(Adj, c):
    dbar = Adj.sum(1).mean()
    return A_SELF * np.eye(N) + c * Adj / dbar


def stationary_cov(world, Adj, M, c, g):
    """Stationary covariance of x for the linear world (augmented with d)."""
    A = coupling_matrix(Adj, c)
    Tm = np.block([[A, g * M], [np.zeros((G, N)), PHI_D * np.eye(G)]])
    Q = np.zeros((N + G, N + G))
    Q[:N, :N] = np.eye(N)
    Q[N:, N:] = (1 - PHI_D ** 2) * np.eye(G)
    S = solve_discrete_lyapunov(Tm, Q)
    return S[:N, :N]


def within_corr(S, members):
    d = np.sqrt(np.diag(S))
    R = S / np.outer(d, d)
    idx = np.array(members)
    sub = R[np.ix_(idx, idx)]
    return sub[np.triu_indices(len(idx), 1)].mean()


def mean_within(S, M):
    return np.mean([within_corr(S, np.flatnonzero(M[:, k])) for k in range(G)])


def world_params(world, Adj, M, c_full=0.4):
    """Return (c, g). Driver gain tuned so within-group correlation matches
    the coupled world's."""
    target = mean_within(stationary_cov("coupled", Adj, M, c_full, 0.0), M)
    if world == "coupled":
        return c_full, 0.0
    c = 0.0 if world == "driver" else c_full / 2
    lo, hi = 0.0, 5.0
    for _ in range(50):
        mid = (lo + hi) / 2
        if mean_within(stationary_cov(world, Adj, M, c, mid), M) < target:
            lo = mid
        else:
            hi = mid
    return c, (lo + hi) / 2


def simulate(Adj, M, c, g, T_, rng, burn=200, pulses=None, return_driver=False):
    """pulses: optional (T_ x N) array added to x after each step (do-style
    exogenous shocks to members). return_driver: also return the driver value
    that entered each x_t."""
    A = coupling_matrix(Adj, c)
    x = np.zeros(N)
    d = np.zeros(G)
    X = np.zeros((T_, N))
    Dr = np.zeros((T_, G))
    for t in range(T_ + burn):
        dused = d
        x = A @ x + g * M @ d + rng.standard_normal(N)
        if pulses is not None and t >= burn:
            x = x + pulses[t - burn]
        d = PHI_D * d + np.sqrt(1 - PHI_D ** 2) * rng.standard_normal(G)
        if t >= burn:
            X[t - burn] = x
            Dr[t - burn] = dused
    return (X, Dr) if return_driver else X


# ---------------------------------------------------------------- feature model
def gibbs_features(Y, rng, iters=400, K_=K, alpha=ALPHA, sw2=1.0, a0=2.0, b0=1.0):
    """Finite beta-Bernoulli sparse factor model, Y (T x N) = F Lam^T + E.
    Lam = B o W, B_ek ~ Bern(pi_k), pi_k ~ Beta(alpha/K,1), W ~ N(0,sw2),
    F_tk ~ N(0,1), E_te ~ N(0, psi_e). Returns the sample of highest joint
    log-likelihood among the last half."""
    T_, N_ = Y.shape
    B = (rng.random((N_, K_)) < 0.2).astype(float)
    W = rng.standard_normal((N_, K_)) * np.sqrt(sw2)
    psi = np.ones(N_) * Y.var(0).mean() * 0.5
    pi = np.full(K_, 0.2)
    best, best_ll = None, -np.inf
    for it in range(iters):
        Lam = B * W
        # factors
        P = np.eye(K_) + (Lam.T / psi) @ Lam
        Pinv = np.linalg.inv(P)
        mean = (Y / psi) @ Lam @ Pinv
        L = np.linalg.cholesky(Pinv)
        F = mean + rng.standard_normal((T_, K_)) @ L.T
        FF = (F * F).sum(0)
        # allocation and loadings, collapsed over w_ek
        R = Y - F @ Lam.T  # T x N residual
        for e in range(N_):
            r = R[:, e]
            for k in range(K_):
                if B[e, k]:
                    r = r + F[:, k] * W[e, k]
                prec = FF[k] / psi[e] + 1.0 / sw2
                mu = (F[:, k] @ r / psi[e]) / prec
                lo = (np.log(pi[k] + 1e-300) - np.log1p(-pi[k] + 1e-16)
                      - 0.5 * np.log(sw2 * prec) + 0.5 * mu * mu * prec)
                on = rng.random() < 1.0 / (1.0 + np.exp(-np.clip(lo, -50, 50)))
                if on:
                    B[e, k] = 1.0
                    W[e, k] = mu + rng.standard_normal() / np.sqrt(prec)
                    r = r - F[:, k] * W[e, k]
                else:
                    B[e, k] = 0.0
            R[:, e] = r
        m = B.sum(0)
        pi = rng.beta(alpha / K_ + m, 1.0 + N_ - m)
        psi = 1.0 / rng.gamma(a0 + T_ / 2, 1.0 / (b0 + 0.5 * (R * R).sum(0)))
        if it >= iters // 2:
            ll = -0.5 * (np.log(psi) * T_ + (R * R / psi).sum(0)).sum()
            if ll > best_ll:
                best_ll = ll
                best = (B.copy(), W.copy(), psi.copy(), F.copy())
    B, W, psi, F = best
    keep = B.sum(0) > 0
    return B[:, keep], (B * W)[:, keep], psi, F[:, keep]


def ar1(F):
    if F.shape[1] == 0:
        return np.zeros(0)
    num = (F[1:] * F[:-1]).sum(0)
    den = (F[:-1] ** 2).sum(0)
    return np.clip(num / np.maximum(den, 1e-12), -0.99, 0.99)


# ---------------------------------------------------------------- relational
def fit_var(X, mask):
    """Least-squares VAR(1) x_{t+1} = A x_t + eps, A restricted to mask."""
    X0, X1 = X[:-1], X[1:]
    A = np.zeros((X.shape[1], X.shape[1]))
    for i in range(X.shape[1]):
        idx = np.flatnonzero(mask[i])
        coef, *_ = np.linalg.lstsq(X0[:, idx], X1[:, i], rcond=None)
        A[i, idx] = coef
    return A


def fit_var_features(X, mask, rng, rounds=3, iters=300):
    """FR: x_{t+1} = A x_t + Lam f_{t+1} + eps, A on mask, f exogenous."""
    Xs = X
    A = fit_var(Xs, mask)
    target = Xs[1:].copy()
    for _ in range(rounds):
        Rres = Xs[1:] - Xs[:-1] @ A.T
        B, Lam, psi, F = gibbs_features(Rres, rng, iters=iters)
        target = Xs[1:] - F @ Lam.T
        X0 = Xs[:-1]
        A = np.zeros((N, N))
        for i in range(N):
            idx = np.flatnonzero(mask[i])
            coef, *_ = np.linalg.lstsq(X0[:, idx], target[:, i], rcond=None)
            A[i, idx] = coef
    Rres = Xs[1:] - Xs[:-1] @ A.T
    B, Lam, psi, F = gibbs_features(Rres, rng, iters=iters)
    return A, B, Lam, psi, F


def fit_favar(X, mask, rng, iters=400):
    """FR: a factor-augmented VAR. Features are found (CASE-165's prior) on the
    innovations of each member's own AR; then x_{t+1} = A x_t + Gam f_t + u,
    A restricted to C, so the features' persistence and the neighbours compete
    for the same predictable part. Features are exogenous: f_{t+1} = Phi f_t + eta."""
    A0 = fit_var(X, np.eye(X.shape[1]) > 0)
    res = X[1:] - X[:-1] @ A0.T          # rows: t = 1..T-1
    B, Lam, psi, F = gibbs_features(res, rng, iters=iters)
    k = F.shape[1]
    Xin, Xout, Fl = X[1:-1], X[2:], F[:-1]
    A = np.zeros((N, N))
    Gam = np.zeros((N, k))
    for i in range(N):
        idx = np.flatnonzero(mask[i])
        Z = np.hstack([Xin[:, idx], Fl])
        coef, *_ = np.linalg.lstsq(Z, Xout[:, i], rcond=None)
        A[i, idx] = coef[:len(idx)]
        Gam[i] = coef[len(idx):]
    phi = ar1(F)
    U = Xout - Xin @ A.T - Fl @ Gam.T       # u_{t+1}, t = 1..T-2
    E = F[1:] - F[:-1] * phi                # eta_{t+1}, same rows
    J = np.hstack([U, E])
    Q = J.T @ J / len(J)
    return dict(A=A, Gam=Gam, phi=phi, Q=Q, B=B, Lam=Lam, psi=psi, A0=A0)


def favar_cov(m, A=None):
    A = m["A"] if A is None else A
    k = len(m["phi"])
    Phi = np.diag(m["phi"]) if k else np.zeros((0, 0))
    Tm = np.block([[A, m["Gam"]], [np.zeros((k, N)), Phi]])
    return solve_discrete_lyapunov(Tm, m["Q"])[:N, :N]


def favar_pred(m, Xd):
    L, psi_ = m["Lam"], m["psi"]
    if L.shape[1] == 0:
        return Xd[:-1] @ m["A"].T
    res = Xd[1:] - Xd[:-1] @ m["A0"].T   # rows t = 1..
    P = np.eye(L.shape[1]) + (L.T / psi_) @ L
    f = (res / psi_) @ L @ np.linalg.inv(P)  # f_t for t = 1..
    f = np.vstack([np.zeros((1, L.shape[1])), f[:-1]])  # align to x_t, t = 0..
    return Xd[:-1] @ m["A"].T + f @ m["Gam"].T


def var_feature_cov(A, Lam, phi, psi):
    """Stationary covariance of x_{t+1} = A x_t + Lam f_{t+1} + eps,
    f_{t+1} = Phi f_t + eta, Var f = 1."""
    k = Lam.shape[1]
    S_eta = np.diag(1 - phi ** 2) if k else np.zeros((0, 0))
    Phi = np.diag(phi) if k else np.zeros((0, 0))
    Tm = np.block([[A, Lam @ Phi], [np.zeros((k, N)), Phi]])
    Q = np.block([[Lam @ S_eta @ Lam.T + np.diag(psi), Lam @ S_eta],
                  [S_eta @ Lam.T, S_eta]])
    S = solve_discrete_lyapunov(Tm, Q)
    return S[:N, :N]


def one_step_r2(Xte, pred):
    return 1 - ((Xte[1:] - pred) ** 2).sum() / ((Xte[1:] - Xte[1:].mean(0)) ** 2).sum()


# ---------------------------------------------------------------- one item
def recovery(B, M):
    cols = [B[:, k] for k in range(B.shape[1]) if B[:, k].sum() >= 2]
    nfeat = len(cols)
    if not cols:
        return nfeat, 0.0
    js = []
    for g in range(G):
        m = M[:, g] > 0
        js.append(max((m & (c > 0)).sum() / (m | (c > 0)).sum() for c in cols))
    return nfeat, float(np.mean(js))


def run_item(world, seed):
    rng = np.random.default_rng(seed)
    M, Adj = make_org(rng)
    c, g = world_params(world, Adj, M)
    Xall, Dall = simulate(Adj, M, c, g, int(T * 1.25), rng, return_driver=True)
    sd = Xall.std(0)
    Xs = (Xall - Xall.mean(0)) / sd
    Xtr, Xte = Xs[:T], Xs[T:]
    mask = (Adj + np.eye(N)) > 0
    eye_mask = np.eye(N) > 0
    D = np.diag(sd)
    Dinv = np.diag(1 / sd)

    # truth, in standardized units
    A_true = Dinv @ coupling_matrix(Adj, c) @ D
    S_true = stationary_cov(world, Adj, M, c, g)

    def true_cut(gr):
        mem = np.flatnonzero(M[:, gr])
        Adj2 = Adj.copy()
        Adj2[np.ix_(mem, mem)] = 0
        # cut removes the ties; keep the same normalization as the original
        dbar = Adj.sum(1).mean()
        A2 = A_SELF * np.eye(N) + c * Adj2 / dbar
        Tm = np.block([[A2, g * M], [np.zeros((G, N)), PHI_D * np.eye(G)]])
        Q = np.zeros((N + G, N + G))
        Q[:N, :N] = np.eye(N)
        Q[N:, N:] = (1 - PHI_D ** 2) * np.eye(G)
        S2 = solve_discrete_lyapunov(Tm, Q)[:N, :N]
        return within_corr(S2, mem) - within_corr(S_true, mem)

    def impulse(A):
        out, P = [], np.eye(N)
        for _ in range(H):
            P = A @ P
            out.append(P.copy())
        R = np.stack(out) * PULSE  # H x N(resp) x N(pulsed)
        offd = ~np.eye(N, dtype=bool)
        return R[:, offd]

    true_imp = impulse(A_true)
    true_cuts = np.array([true_cut(gr) for gr in range(G)])

    t0 = time.time()
    # ---- F-raw
    Bf, Lf, psif, Ff = gibbs_features(Xtr, rng)
    phif = ar1(Ff)
    nfeat_raw, jac_raw = recovery(Bf, M)
    # one-step: E[f_t | x_t] then Phi
    if Lf.shape[1]:
        P = np.eye(Lf.shape[1]) + (Lf.T / psif) @ Lf
        post = (Xte[:-1] / psif) @ Lf @ np.linalg.inv(P)
        pred_raw = (post * phif) @ Lf.T
    else:
        pred_raw = np.zeros_like(Xte[1:])
    S_f = Lf @ Lf.T + np.diag(psif)
    # con reading, pulse: Cov(x_{t+h}, x_{e,t}) / Var(x_e)
    con = []
    for h in range(1, H + 1):
        C = Lf @ np.diag(phif ** h) @ Lf.T if Lf.shape[1] else np.zeros((N, N))
        con.append(C / np.diag(S_f)[None, :] * PULSE)
    con_imp = np.stack(con)[:, ~np.eye(N, dtype=bool)]
    exo_imp = np.zeros_like(true_imp)

    def con_cut(gr):
        mem = np.flatnonzero(M[:, gr])
        L2 = Lf.copy()
        for k in range(Lf.shape[1]):
            hold = np.flatnonzero(Bf[:, k])
            ing = np.intersect1d(hold, mem)
            if len(ing) >= 2 and len(ing) >= 0.5 * len(hold):
                L2[mem, k] = 0
        S2 = L2 @ L2.T + np.diag(psif)
        return within_corr(S2, mem) - within_corr(S_f, mem)

    con_cuts = np.array([con_cut(gr) for gr in range(G)])

    # ---- F-self (features + private AR, no relations)
    As, Bs, Ls, psis, Fs = fit_var_features(Xtr, eye_mask, rng)
    nfeat_self, jac_self = recovery(Bs, M)
    phis = ar1(Fs)

    def fr_pred(A, L, psi_, phi, Xd):
        base = Xd[:-1] @ A.T
        if L.shape[1] == 0:
            return base
        # innovation features: E[f_t | residual_t] then Phi
        res = Xd[1:-1] - Xd[:-2] @ A.T
        P = np.eye(L.shape[1]) + (L.T / psi_) @ L
        post = (res / psi_) @ L @ np.linalg.inv(P)
        add = np.vstack([np.zeros((1, L.shape[1])), post]) * phi
        return base + add @ L.T

    pred_self = fr_pred(As, Ls, psis, phis, Xte)

    # ---- R
    Ar = fit_var(Xtr, mask)
    res_r = Xtr[1:] - Xtr[:-1] @ Ar.T
    psir = res_r.var(0)
    pred_r = Xte[:-1] @ Ar.T
    S_r = var_feature_cov(Ar, np.zeros((N, 0)), np.zeros(0), psir)

    # ---- FR (factor-augmented VAR on C)
    fr = fit_favar(Xtr, mask, rng)
    Afr = fr["A"]
    nfeat_fr, jac_fr = recovery(fr["B"], M)
    pred_fr = favar_pred(fr, Xte)
    S_fr = favar_cov(fr)

    def model_cut(A, L, phi, psi_, S0, gr):
        mem = np.flatnonzero(M[:, gr])
        A2 = A.copy()
        for i in mem:
            for j in mem:
                if i != j:
                    A2[i, j] = 0
        S2 = var_feature_cov(A2, L, phi, psi_)
        return within_corr(S2, mem) - within_corr(S0, mem)

    r_cuts = np.array([model_cut(Ar, np.zeros((N, 0)), np.zeros(0), psir, S_r, gr)
                       for gr in range(G)])
    def fr_cut(gr):
        mem = np.flatnonzero(M[:, gr])
        A2 = Afr.copy()
        for i in mem:
            for j in mem:
                if i != j:
                    A2[i, j] = 0
        return within_corr(favar_cov(fr, A2), mem) - within_corr(S_fr, mem)

    fr_cuts = np.array([fr_cut(gr) for gr in range(G)])

    # ---- FR-oracle: VAR on C plus the true shared driver, observed
    Xin, Xout, Dn = Xtr[:-1], Xtr[1:], Dall[1:T]
    Aor = np.zeros((N, N))
    for i in range(N):
        idx = np.flatnonzero(mask[i])
        coef, *_ = np.linalg.lstsq(np.hstack([Xin[:, idx], Dn]), Xout[:, i], rcond=None)
        Aor[i, idx] = coef[:len(idx)]

    # ---- R-int: VAR on C fitted to a run in which half the members get
    # random exogenous shocks; scored on the other half's pulses
    trained = rng.choice(N, N // 2, replace=False)
    held = set(np.setdiff1d(np.arange(N), trained).tolist())
    P = np.zeros((T, N))
    P[:, trained] = (3.0 * sd[trained] * rng.standard_normal((T, len(trained)))
                     * (rng.random((T, len(trained))) < 0.2))
    Xint = simulate(Adj, M, c, g, T, rng, pulses=P)
    Xint = (Xint - Xall.mean(0)) / sd
    Aint = fit_var(Xint, mask)
    res_i = Xint[1:] - Xint[:-1] @ Aint.T - P[1:] / sd  # shocks are not noise
    S_int = var_feature_cov(Aint, np.zeros((N, 0)), np.zeros(0), res_i.var(0))

    def rmse(a, b):
        return float(np.sqrt(np.mean((a - b) ** 2)))

    imp = {"F-raw/exo": exo_imp, "F-raw/con": con_imp, "F-self": impulse(As),
           "R": impulse(Ar), "FR": impulse(Afr), "FR-oracle": impulse(Aor),
           "R-int": impulse(Aint)}
    # held-out pulses: responses (others) to pulses on members R-int never shocked
    offd_idx = [(i, j) for i in range(N) for j in range(N) if i != j]
    sel = np.array([j in held for (i, j) in offd_idx])
    res_o = Xout - Xin @ Aor.T
    S_or = var_feature_cov(Aor, np.zeros((N, 0)), np.zeros(0), res_o.var(0))
    or_cuts = np.array([model_cut(Aor, np.zeros((N, 0)), np.zeros(0), res_o.var(0), S_or, gr)
                        for gr in range(G)])
    int_cuts = np.array([model_cut(Aint, np.zeros((N, 0)), np.zeros(0), res_i.var(0), S_int, gr)
                         for gr in range(G)])
    cuts = {"F-raw/exo": np.zeros(G), "F-raw/con": con_cuts, "F-self": np.zeros(G),
            "R": r_cuts, "FR": fr_cuts, "FR-oracle": or_cuts, "R-int": int_cuts}
    preds = {"F-raw": pred_raw, "F-self": pred_self, "R": pred_r, "FR": pred_fr}

    out = {
        "world": world, "seed": seed, "c": c, "g": g,
        "within_corr": float(mean_within(S_true, M)),
        "true_spill_h1": float(np.abs(true_imp[0]).mean()),
        "true_cut_mean": float(true_cuts.mean()),
        "pulse_rmse": {k: rmse(v, true_imp) for k, v in imp.items()},
        "pulse_rmse_heldout": {k: rmse(v[:, sel], true_imp[:, sel]) for k, v in imp.items()},
        "pred_spill_h1": {k: float(np.abs(v[0]).mean()) for k, v in imp.items()},
        "cut_mae": {k: float(np.mean(np.abs(v - true_cuts))) for k, v in cuts.items()},
        "pred_cut_mean": {k: float(v.mean()) for k, v in cuts.items()},
        "r2_onestep": {k: float(one_step_r2(Xte, v)) for k, v in preds.items()},
        "n_features": {"F-raw": nfeat_raw, "F-self": nfeat_self, "FR": nfeat_fr},
        "group_jaccard": {"F-raw": jac_raw, "F-self": jac_self, "FR": jac_fr},
        "offdiag_abs_mean": {
            "R": float(np.abs(Ar[~np.eye(N, dtype=bool)]).mean()),
            "FR": float(np.abs(Afr[~np.eye(N, dtype=bool)]).mean()),
            "FR-oracle": float(np.abs(Aor[~np.eye(N, dtype=bool)]).mean()),
            "R-int": float(np.abs(Aint[~np.eye(N, dtype=bool)]).mean()),
            "truth": float(np.abs(A_true[~np.eye(N, dtype=bool)]).mean())},
        "secs": time.time() - t0,
    }
    return out


def main(path, worlds, seeds):
    done = set()
    if os.path.exists(path):
        with open(path) as fh:
            for line in fh:
                if line.strip():
                    r = json.loads(line)
                    done.add((r["world"], r["seed"]))
    for seed in seeds:
        for w in worlds:
            if (w, seed) in done:
                continue
            r = run_item(w, seed)
            with open(path, "a") as fh:
                fh.write(json.dumps(r) + "\n")
            print(w, seed, round(r["secs"], 1), flush=True)


if __name__ == "__main__":
    path = sys.argv[1]
    nseeds = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    worlds = sys.argv[3].split(",") if len(sys.argv) > 3 else ["coupled", "driver", "mixed"]
    main(path, worlds, range(nseeds))
