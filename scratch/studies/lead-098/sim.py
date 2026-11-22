"""LEAD-098: CASE-179's network, with A12's arms and QUESTION-063's interventions.

A network of Stuart-Landau units z_j on a graph. Each edge carries a
correspondence map, a phase offset theta_jk (theta_kj = -theta_jk): the
relation "z_j agrees with z_k" is z_j = e^{i theta_jk} z_k. The coupling
realizes its own offsets, which may or may not be the apparatus's.

    dz_j = [(mu_j - u_j + i w_j - |z_j|^2) z_j + coupling_j + F_j e^{i(Omega t + psi_j)}] dt
           + sigma dW_j

coupling (dissipative):   sum_k K A_jk (e^{i theta_jk} z_k - z_j)  =  -(L z)_j
coupling (conservative):  -i (L z)_j     (Hermitian L, so the flow is unitary)

L is the connection Laplacian: L = D - C, C_jk = K A_jk e^{i theta_jk}.
Everything runs on a batch axis, so paired runs (control and intervened)
share their noise and their difference is the intervention's effect.
"""
import numpy as np


# ---------- graphs and maps ----------

def ring_with_chords(n=8, chords=((0, 4),)):
    A = np.zeros((n, n))
    for j in range(n):
        A[j, (j + 1) % n] = A[(j + 1) % n, j] = 1
    for a, b in chords:
        A[a, b] = A[b, a] = 1
    return A


def edges(A):
    n = len(A)
    return [(j, k) for j in range(n) for k in range(j + 1, n) if A[j, k]]


def gauge_maps(phi, A):
    """Compatible maps: theta_jk = phi_j - phi_k (a global section exists)."""
    th = np.subtract.outer(phi, phi)
    return th * (A > 0)


def frustrate(theta, j, k, delta):
    th = theta.copy()
    th[j, k] += delta
    th[k, j] -= delta
    return th


def connection_laplacian(A, theta, K):
    C = K * A * np.exp(1j * theta)
    return np.diag((K * A).sum(1)) - C


def cycle_holonomies(A, theta):
    """Holonomy around each fundamental cycle of a spanning tree, wrapped to (-pi, pi]."""
    n = len(A)
    parent = {0: None}
    order = [0]
    for v in order:
        for w in range(n):
            if A[v, w] and w not in parent:
                parent[w] = v
                order.append(w)
    pot = np.zeros(n)  # potential along tree: pot_w = pot_v - theta_vw ... z_v = e^{i th_vw} z_w
    for w in order[1:]:
        v = parent[w]
        pot[w] = pot[v] - theta[v, w]
    hol = []
    for j, k in edges(A):
        if parent.get(k) == j or parent.get(j) == k:
            continue
        h = theta[j, k] - (pot[j] - pot[k])
        hol.append(np.angle(np.exp(1j * h)))
    return np.array(hol)


def min_eig(L):
    return float(np.linalg.eigvalsh(L)[0])


def incompatibility(z, A, theta_app):
    """Normalized discrepancy of state z from the apparatus's maps: sum over edges
    |z_j - e^{i th_jk} z_k|^2 / (2 sum |z|^2 * mean degree). 0 iff z is a section."""
    z = np.atleast_2d(z)
    tot = np.zeros(len(z))
    for j, k in edges(A):
        tot += np.abs(z[:, j] - np.exp(1j * theta_app[j, k]) * z[:, k]) ** 2
    norm = (np.abs(z) ** 2).sum(1) + 1e-300
    return tot / norm / len(edges(A)) * len(A) / 2


def order_parameter(z):
    z = np.atleast_2d(z)
    ph = z / (np.abs(z) + 1e-300)
    return np.abs(ph.mean(1))


# ---------- integrator ----------

def simulate(n, A, T, dt=0.01, *, K=0.0, theta=None, ctype="diss", mu=0.5, u=0.0,
             omega=None, F=0.0, Omega=1.0, psi=None, sigma=0.0, z0=None, B=1,
             seed=0, schedule=(), every=10, adapt=None, plastic=None, t0=0.0):
    """Stochastic Heun (additive noise); slow variables by Euler. `schedule` is a list of (time, fn) with fn(state) mutating the
    dict state = {'z','K','theta','mu','u','F','psi','A','batch'} at that time.
    `adapt`: dict(eps, mumax, a0, c, produce) for reciprocally maintained capacity mu_j:
        dmu_j = eps (produce_j * mumax * h(a_j) - mu_j - c),  a_j = mean_{k~j} |z_k|^2,
        h(a) = a/(a+a0).
    `plastic`: dict(eta) for maps adapting to realized offsets:
        dtheta_jk = eta * sin(arg z_j - arg z_k - theta_jk).
    Returns times and samples of z (and of mu, theta if adaptive)."""
    rng = np.random.default_rng(seed)
    if theta is None:
        theta = np.zeros((n, n))
    if omega is None:
        omega = np.ones(n)
    if psi is None:
        psi = np.zeros(n)
    st = {
        "A": np.array(A, float), "K": np.broadcast_to(np.asarray(K, float), (B,)).copy(),
        "theta": np.broadcast_to(theta, (B, n, n)).copy(),
        "mu": np.broadcast_to(np.asarray(mu, float), (B, n)).copy() if np.ndim(mu) < 2 else np.array(mu, float),
        "u": np.broadcast_to(np.asarray(u, float), (B, n)).copy(),
        "F": np.broadcast_to(np.asarray(F, float), (B, n)).copy(),
        "psi": np.broadcast_to(np.asarray(psi, float), (B, n)).copy(),
        "produce": np.ones((B, n)),
        "batch": B,
    }
    if z0 is None:
        z0 = 0.7 * np.exp(1j * rng.uniform(0, 2 * np.pi, n))
    z = np.broadcast_to(np.asarray(z0, complex), (B, n)).copy()
    st["z"] = z
    steps = int(round(T / dt))
    sched = sorted(schedule, key=lambda e: e[0])
    si = 0
    ts, zs, mus, ths = [], [], [], []
    deg_A = st["A"].sum(1)
    sq = np.sqrt(dt / 2)
    for s in range(steps + 1):
        t = t0 + s * dt
        while si < len(sched) and sched[si][0] <= t + 1e-12:
            sched[si][1](st)
            si += 1
        z = st["z"]
        if s % every == 0:
            ts.append(t)
            zs.append(z.copy())
            if adapt is not None:
                mus.append(st["mu"].copy())
            if plastic is not None:
                ths.append(st["theta"].copy())
        if s == steps:
            break
        Kb = st["K"][:, None, None]
        C = Kb * st["A"] * np.exp(1j * st["theta"])

        def f(z, t):
            Lz = st["K"][:, None] * deg_A * z - np.einsum("bjk,bk->bj", C, z)
            if ctype == "diss":
                rhs = (st["mu"] - st["u"] + 1j * omega - np.abs(z) ** 2) * z - Lz
            elif ctype == "cons":
                rhs = 1j * omega * z - 1j * Lz  # linear, norm-conserving
            else:
                raise ValueError(ctype)
            return rhs + st["F"] * np.exp(1j * (Omega * t + st["psi"]))

        noise = 0.0
        if sigma:
            noise = sigma * sq * (rng.standard_normal((B, n)) + 1j * rng.standard_normal((B, n)))
        f1 = f(z, t)
        zp = z + f1 * dt + noise
        dz = 0.5 * (f1 + f(zp, t + dt)) * dt + noise  # stochastic Heun (additive noise)
        if adapt is not None:
            a = (st["A"] @ (np.abs(z) ** 2).T).T / deg_A
            h = a / (a + adapt["a0"])
            st["mu"] = st["mu"] + adapt["eps"] * (st["produce"] * adapt["mumax"] * h
                                                  - st["mu"] - adapt["c"]) * dt
        if plastic is not None:
            ph = np.angle(z)
            d = ph[:, :, None] - ph[:, None, :] - st["theta"]
            st["theta"] = st["theta"] + plastic["eta"] * np.sin(d) * st["A"] * dt
        st["z"] = z + dz
    out = {"t": np.array(ts), "z": np.array(zs)}
    if adapt is not None:
        out["mu"] = np.array(mus)
    if plastic is not None:
        out["theta"] = np.array(ths)
    return out


# ---------- readouts ----------

def drive_frame_phase(z, t, Omega):
    """Phases relative to the drive's clock: arg(z e^{-i Omega t})."""
    return np.angle(z * np.exp(-1j * Omega * t)[:, None, None])


def plv(z):
    """Mean pairwise phase-locking value over time of the samples z (T, N)."""
    ph = z / (np.abs(z) + 1e-300)
    n = z.shape[1]
    vals = []
    for j in range(n):
        for k in range(j + 1, n):
            vals.append(np.abs(np.mean(ph[:, j] * np.conj(ph[:, k]))))
    return float(np.mean(vals))


def observed_offsets(z, A):
    """theta_jk read off as arg <z_j conj z_k> over time: consistency-only revision."""
    n = z.shape[1]
    th = np.zeros((n, n))
    for j, k in edges(A):
        c = np.mean(z[:, j] * np.conj(z[:, k]))
        th[j, k] = np.angle(c)
        th[k, j] = -th[j, k]
    return th


def fit_linear_response(dphi_list, dt, A, pin=True, ridge=1e-3):
    """Fit d(dphi)/dt = -(L_g + diag(p)) dphi from paired-difference trajectories.
    L_g is a weighted graph Laplacian on A's edges (gain g_e >= unconstrained), p the
    pinning of each unit to an outside reference. Returns (g dict edge->gain, p)."""
    E = edges(A)
    n = len(A)
    rows, ys = [], []
    for dphi in dphi_list:  # (T, N)
        x = dphi[:-1]
        y = (dphi[1:] - dphi[:-1]) / dt
        for j in range(n):
            feats = np.zeros((len(x), len(E) + (n if pin else 0)))
            for e, (a, b) in enumerate(E):
                if a == j:
                    feats[:, e] = x[:, b] - x[:, a]
                elif b == j:
                    feats[:, e] = x[:, a] - x[:, b]
            if pin:
                feats[:, len(E) + j] = -x[:, j]
            rows.append(feats)
            ys.append(y[:, j])
    X = np.vstack(rows)
    Y = np.concatenate(ys)
    w = np.linalg.solve(X.T @ X + ridge * np.eye(X.shape[1]), X.T @ Y)
    g = {e: float(w[i]) for i, e in enumerate(E)}
    p = w[len(E):] if pin else np.zeros(n)
    return g, np.array(p)


def response_matrix(g, p, n, horizon):
    """Predicted dphi(horizon) = expm(-(L_g + diag p) horizon) applied to unit kicks."""
    from scipy.linalg import expm
    M = np.diag(np.asarray(p, float))
    for (a, b), w in g.items():
        M[a, a] += w
        M[b, b] += w
        M[a, b] -= w
        M[b, a] -= w
    return expm(-M * horizon)


# ---------- sheaf reduction (QUESTION-283) ----------

def sheaf_laplacian(dims, edge_maps):
    """edge_maps: list of (u, v, Fu, Fv) with Fu: R^{d_u} -> R^{d_e}, Fv likewise.
    Returns block Laplacian delta^T delta and the vertex offsets."""
    off = np.concatenate([[0], np.cumsum(dims)])
    rows = []
    for u, v, Fu, Fv in edge_maps:
        r = np.zeros((Fu.shape[0], off[-1]))
        r[:, off[u]:off[u + 1]] = Fu
        r[:, off[v]:off[v + 1]] = -Fv
        rows.append(r)
    delta = np.vstack(rows)
    return delta.T @ delta, off


def null_space(M, tol=1e-9):
    if M.shape[0] == 0:
        return np.eye(M.shape[1])
    u, s, vt = np.linalg.svd(M)
    r = int((s > tol * max(1.0, s.max() if len(s) else 1)).sum())
    return vt[r:].T


def kron_reduce(L, keep):
    keep = np.asarray(keep)
    drop = np.setdiff1d(np.arange(len(L)), keep)
    if len(drop) == 0:
        return L[np.ix_(keep, keep)]
    Lkk = L[np.ix_(keep, keep)]
    Lkd = L[np.ix_(keep, drop)]
    Ldd = L[np.ix_(drop, drop)]
    return Lkk - Lkd @ np.linalg.pinv(Ldd) @ Lkd.T


def pairwise_expressible(S, blocks):
    """S: basis (columns) of the boundary section space inside R^D, D = sum of block sizes.
    blocks: list of index arrays, one per boundary vertex. Returns (dim S, dim P) where
    P = {x : for every pair (a,b), (x_a, x_b) lies in the projection of S onto (a,b)}.
    S is expressible by pairwise relations iff dim P == dim S (S is always inside P)."""
    D = S.shape[0]
    cons = []
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            idx = np.concatenate([blocks[i], blocks[j]])
            Pij = S[idx]  # projection basis
            # constraints: x_idx orthogonal to complement of col(Pij)
            if Pij.size:
                q, _ = np.linalg.qr(Pij)
                r = np.linalg.matrix_rank(Pij)
                q = q[:, :r]
                comp = np.eye(len(idx)) - q @ q.T
            else:
                comp = np.eye(len(idx))
            c = np.zeros((len(idx), D))
            c[:, idx] = comp
            cons.append(c)
    Cm = np.vstack(cons)
    P = null_space(Cm)
    return S.shape[1], P.shape[1]
