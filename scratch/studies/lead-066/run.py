"""LEAD-066 runs. Appends one JSON line per item to results/<arm>.jsonl and
skips items already written, so it resumes.

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run.py [E1|E2|E4]
"""
import itertools
import json
import os
import sys

import numpy as np

import bound as B

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
os.makedirs(RES, exist_ok=True)
DELTAS = [0.3, 0.1, 0.03, 0.01, 1e-3, 1e-4, 1e-6, 1e-9, 1e-12]


def done_keys(path):
    if not os.path.exists(path):
        return set()
    with open(path) as f:
        return {json.loads(line)["key"] for line in f if line.strip()}


def append(path, rec):
    with open(path, "a") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def r(x, k=6):
    if isinstance(x, (list, tuple, np.ndarray)):
        return [r(v, k) for v in x]
    x = float(x)
    if not np.isfinite(x):
        return None if np.isnan(x) else ("inf" if x > 0 else "-inf")
    return float(f"{x:.{k}g}")


# ------------------------------------------------------------------- E1: kernels

def kernel_item(kernel, rho, gname, sigma, seed, depth=4):
    rng = np.random.default_rng(1000 * seed + 7)
    H, lev = B.haar(depth)
    n = H.shape[0]
    L = depth
    c = [1.0] + [rho ** (l - 1) for l in range(1, L + 1)]
    g = {"flat": [0.0] + [1.0] * L,
         "falling": [0.0] + [2 ** (-(l - 1) / 2) for l in range(1, L + 1)],
         "rising": [0.0] + [2 ** ((l - 1) / 2) for l in range(1, L + 1)]}[gname]
    X0 = B.tree_inputs(H, lev, c, n, rng)
    X = B.perturb(X0, sigma, rng) if sigma > 0 else X0.copy()
    if kernel == "rbf":
        s = B.rbf_bandwidth(X0)
        K, K0 = B.k_rbf(X, s), B.k_rbf(X0, s)
    else:
        K, K0 = B.KERNELS[kernel](X), B.KERNELS[kernel](X0)
    A, A0 = K / n, K0 / n
    Ps = B.projectors(H, lev)
    e0 = -B.tree_target(H, lev, g, rng)
    e0n = np.linalg.norm(e0)

    eta = B.commutator_norms(A, Ps)
    Eop = np.linalg.norm(A - A0, 2)
    mu = B.block_extremes(A0, H, lev)[0]               # symmetric rates (scalar per level)
    lam, Lam = B.block_extremes(A, H, lev)
    a = max(np.linalg.eigvalsh(A)[0], 0.0)
    share = np.array([np.linalg.norm(P @ e0) / e0n for P in Ps])
    levels = [l for l in range(L + 1) if g[l] > 0]
    eps = np.array([eta[l] / (lam[l] * share[l]) if g[l] > 0 else np.inf for l in range(L + 1)])

    rec = dict(arm="E1", kernel=kernel, rho=rho, g=gname, sigma=sigma, seed=seed,
               eta=r(eta), Eop=r(Eop), mu=r(mu), lam=r(lam), Lam=r(Lam), a=r(a),
               share=r(share), eps=r(eps))
    if kernel == "linear":
        Delta = X - X0
        d = X.shape[1]
        rec["data_bound"] = r((2 * np.linalg.norm(X0, 2) * np.linalg.norm(Delta, 2)
                               + np.linalg.norm(Delta, 2) ** 2) / (n * d))

    # Theorem 1, pointwise on a time grid
    f, fD = B.Flow(A, e0), B.Flow(B.pinch(A, Ps), e0)
    ts = np.concatenate([[0.0], np.geomspace(1e-3 / lam[levels].max(), 50 / max(a, 1e-12), 3000)])
    diff = f(ts) - fD(ts)
    worst, worst_sup = 0.0, 0.0
    for l in levels:
        obs = np.linalg.norm(Ps[l] @ diff, axis=0)
        bnd = B.theorem1_bound(ts, eta[l], lam[l], a, e0n)
        with np.errstate(divide="ignore", invalid="ignore"):
            ratio = obs / (bnd + 1e-12 * e0n)   # absolute floor for rounding at exact symmetry
        worst = max(worst, float(np.nanmax(ratio)))
        if eta[l] > 0:
            worst_sup = max(worst_sup, obs.max() / (eta[l] * e0n / lam[l]))
    rec["thm1_max_ratio"] = r(worst)          # must be <= 1
    rec["thm1_sup_over_uniform"] = r(worst_sup)  # tightness of the uniform bound
    rec["dk_max_ratio"] = r(max(B.davis_kahan_check(A, Ps[l], lam[l], Lam[l], eta[l]) for l in levels))

    # Corollary 2 and the order
    times, ints = {}, {}
    for dl in DELTAS:
        tmax = 4 * (np.log(1 / dl) / 2 + 40) / max(a, 1e-12)
        times[dl] = {l: B.acquisition_time(f, Ps[l], dl, tmax, ngrid=3000) for l in levels}
        ints[dl] = {l: B.time_interval(dl, eps[l], lam[l], Lam[l]) for l in levels}
    contained, checked = 0, 0
    pairs = []
    for dl in DELTAS:
        for l in levels:
            lo, hi = ints[dl][l]
            T = times[dl][l]
            checked += 1
            contained += int(lo * (1 - 1e-9) <= T <= hi * (1 + 1e-9) or (np.isinf(hi) and T >= lo * (1 - 1e-9)))
        for l, m in itertools.combinations(levels, 2):
            if abs(mu[l] - mu[m]) <= 1e-9 * max(mu[l], mu[m]):
                base = 0
            else:
                base = 1 if mu[l] > mu[m] else -1   # +1: l first in the symmetric flow
            Tl, Tm = times[dl][l], times[dl][m]
            actual = 0 if np.isclose(Tl, Tm, rtol=1e-9) else (1 if Tl < Tm else -1)
            (first, second) = (l, m) if base >= 0 else (m, l)
            cert = base != 0 and ints[dl][first][1] < ints[dl][second][0]
            pairs.append(dict(delta=dl, l=l, m=m, base=base, actual=actual, certified=bool(cert)))
    rec["times"] = {str(dl): r([times[dl][l] for l in levels]) for dl in DELTAS}
    rec["levels"] = levels
    rec["contained"] = contained
    rec["checked"] = checked
    rec["pairs"] = pairs
    return rec


def run_E1():
    path = os.path.join(RES, "E1.jsonl")
    have = done_keys(path)
    grid = itertools.product(["linear", "relu_ntk", "rbf"], [0.7, 0.85], ["flat", "falling", "rising"],
                             [0.0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.2, 0.3, 0.5], range(5))
    for kernel, rho, gname, sigma, seed in grid:
        key = f"E1|{kernel}|{rho}|{gname}|{sigma}|{seed}"
        if key in have:
            continue
        rec = kernel_item(kernel, rho, gname, sigma, seed)
        rec["key"] = key
        append(path, rec)


# ------------------------------------------------------------------- E2: sharpness

def run_E2():
    path = os.path.join(RES, "E2.jsonl")
    have = done_keys(path)
    for q, p in itertools.product([1e-3, 1e-2, 0.1, 0.3], [1e-4, 1e-3, 1e-2, 0.1, 0.5]):
        key = f"E2|{q}|{p}"
        if key in have:
            continue
        mu1, mu2, eta = 1.0, p, q
        A = np.array([[mu1, eta], [eta, mu2]])
        f = B.Flow(A, np.array([0.0, 1.0]))
        a = np.linalg.eigvalsh(A)[0]
        ts = np.geomspace(1e-3, 50 / max(a, 1e-9), 20000)
        sup = np.abs(f(ts)[0]).max()
        append(path, dict(key=key, arm="E2", eta_over_mu1=q, mu2_over_mu1=p,
                          sup_leak=r(sup), uniform_bound=r(eta / mu1), ratio=r(sup / (eta / mu1))))


# ------------------------------------------------------------------- E4: a trained network

def net_item(sigma, scale, seed, depth=4, m=256, max_steps=40000, hcap=5.0, frac=0.05):
    """Two-layer ReLU network, full-batch GD on (1/2n)||f - y||^2 from zero output.
    Step h_k = min(frac / lambda_max(A_k), hcap), A_k = J_k J_k^T / n its tangent
    kernel. Tracks the level-decoupled comparison e^D_{k+1} = (I - h_k D_k) e^D_k
    and the discrete form of Theorem 5 in both versions:
      damped:   B_{k+1} = (1 - h_k lambda_l,k) B_k + h_k eta_l,k ||e_k|| + ||P_l rho_k||
      integral: S_{k+1} = S_k + h_k eta_l,k ||e_k|| + ||P_l rho_k||
    with rho_k = e_{k+1} - (I - h_k A_k) e_k (the step's departure from linearity)."""
    rng = np.random.default_rng(5000 + 100 * seed + int(1000 * sigma) + int(10 * scale))
    H, lev = B.haar(depth)
    n = H.shape[0]
    c = [1.0] + [0.8 ** (l - 1) for l in range(1, depth + 1)]
    g = [0.0] + [1.0] * depth
    X0 = B.tree_inputs(H, lev, c, n, rng)
    X = B.perturb(X0, sigma, rng) if sigma > 0 else X0.copy()
    y = B.tree_target(H, lev, g, rng)
    Ps = B.projectors(H, lev)
    levels = [l for l in range(depth + 1) if g[l] > 0]
    net = B.TwoLayerReLU(n, m, scale, rng)

    e = net.forward(X) - y
    e0n = np.linalg.norm(e)
    eD = e.copy()
    base = {l: np.linalg.norm(Ps[l] @ e) for l in levels}
    Bd = {l: 0.0 for l in levels}
    Si = {l: 0.0 for l in levels}
    int_comm = {l: 0.0 for l in levels}
    worst_d, worst_i, max_rel_dev = 0.0, 0.0, {l: 0.0 for l in levels}
    T, TD = {}, {}
    trace = []
    t = 0.0
    eta0 = None
    for k in range(max_steps):
        J = net.jacobian(X)
        A = J @ J.T / n
        h = min(frac / np.linalg.eigvalsh(A)[-1], hcap)
        D = B.pinch(A, Ps)
        eta = B.commutator_norms(A, Ps)
        lam = B.block_extremes(A, H, lev)[0]
        if eta0 is None:
            eta0 = eta
            mu0 = lam
        net.step(X, y, h)
        e_next = net.forward(X) - y
        rho_k = e_next - (e - h * A @ e)
        eD_next = eD - h * D @ eD
        t += h
        for l in levels:
            src = h * eta[l] * np.linalg.norm(e) + np.linalg.norm(Ps[l] @ rho_k)
            Bd[l] = (1 - h * lam[l]) * Bd[l] + src
            Si[l] += src
            int_comm[l] += h * eta[l]
            obs = np.linalg.norm(Ps[l] @ (e_next - eD_next))
            floor = 1e-12 * e0n
            worst_d = max(worst_d, obs / (Bd[l] + floor))
            worst_i = max(worst_i, obs / (Si[l] + floor))
            max_rel_dev[l] = max(max_rel_dev[l], obs / base[l])
            for dl in (0.1, 0.01):
                if (l, dl) not in T and np.linalg.norm(Ps[l] @ e_next) ** 2 <= dl * base[l] ** 2:
                    T[(l, dl)] = t
                if (l, dl) not in TD and np.linalg.norm(Ps[l] @ eD_next) ** 2 <= dl * base[l] ** 2:
                    TD[(l, dl)] = t
        if k % 500 == 0:
            trace.append(dict(step=k, t=r(t), h=r(h), eta=r(eta), lam=r(lam),
                              risk=r([(np.linalg.norm(Ps[l] @ e) / base[l]) ** 2 for l in levels])))
        e, eD = e_next, eD_next
        if all((l, 0.01) in T and (l, 0.01) in TD for l in levels):
            break
    return dict(arm="E4", sigma=sigma, scale=scale, seed=seed, width=m, steps=k + 1, t_end=r(t),
                levels=levels, e0norm=r(e0n), eta_init=r(eta0), lam_init=r(mu0),
                damped_bound_max_ratio=r(worst_d), integral_bound_max_ratio=r(worst_i),
                int_commutator={str(l): r(int_comm[l]) for l in levels},
                max_rel_dev={str(l): r(max_rel_dev[l]) for l in levels},
                damped_bound_rel_final={str(l): r(Bd[l] / base[l]) for l in levels},
                integral_bound_rel_final={str(l): r(Si[l] / base[l]) for l in levels},
                T={f"{l}|{dl}": r(T.get((l, dl), np.nan)) for l in levels for dl in (0.1, 0.01)},
                TD={f"{l}|{dl}": r(TD.get((l, dl), np.nan)) for l in levels for dl in (0.1, 0.01)},
                trace=trace)


def run_E4():
    path = os.path.join(RES, "E4.jsonl")
    have = done_keys(path)
    for m, sigma, scale, seed in itertools.product([64, 256, 1024], [0.0, 0.1, 0.3], [1.0, 0.1], range(3)):
        key = f"E4|{m}|{sigma}|{scale}|{seed}"
        if key in have:
            continue
        rec = net_item(sigma, scale, seed, m=m)
        rec["key"] = key
        append(path, rec)


if __name__ == "__main__":
    arms = sys.argv[1:] or ["E1", "E2", "E4"]
    for arm in arms:
        {"E1": run_E1, "E2": run_E2, "E4": run_E4}[arm]()
        print(arm, "done", flush=True)
