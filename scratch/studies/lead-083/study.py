"""LEAD-083: compensation and entrainment in closed modes that are not blocks.

Arm A, a field excitation: the kink of an overdamped phi^4 lattice,
    dphi_i/dt = (phi_{i+1} - 2 phi_i + phi_{i-1}) / h^2 + phi_i - phi_i^3,
    with phi = -1 at the left wall and +1 at the right.
Arm B, a collective mode: the locked cluster of a Kuramoto population with
    uniform all-to-all coupling K/N (partial synchrony).
Arm C, a block control: two Kuramoto clusters, strong coupling inside,
    weak across.

One protocol for all arms:
- block test (CLAIM-157): for a candidate group G of members, with
  interaction matrix W, delta = gap between the two slowest modes of the
  group's own generator, eps = the larger of ||W[G,~G]|| and ||W[~G,G]||
  (spectral norms); rho = delta / eps. Also the entrywise ratio, mean
  |W| inside over mean |W| across.
- compensation (LIT-902's jaw-load design): hold a subset S of members at
  a displaced state (sustained), and read a task variable T of the form
  with the other members free and with them frozen at their unperturbed
  states. kappa = (T_free - T_frozen) / (T_base - T_frozen): the share of
  the load's damage to T that the other members undo.
- entrainment (CLAIM-172, timing): detune S by Delta and read the change
  of mean frequency of S and of the other members of the form.

Results go to results.jsonl, one line per item, appended as produced;
items already written are skipped on rerun.
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results.jsonl")


# ---------------------------------------------------------------- utilities
def block_test(W, G, gen):
    """Block test for group G (index array) of interaction matrix W.

    gen: the full generator (Jacobian) whose restriction to G is the
    group's own dynamics. Returns rho = delta/eps and the entrywise ratio.
    """
    n = W.shape[0]
    G = np.asarray(sorted(G))
    H = np.setdiff1d(np.arange(n), G)
    JG = gen[np.ix_(G, G)]
    ev = np.sort(np.real(np.linalg.eigvals(JG)))[::-1]  # slowest first
    delta = ev[0] - ev[1] if len(ev) > 1 else np.inf
    if len(H) == 0:
        return dict(rho=np.inf, delta=float(delta), eps=0.0, entrywise=np.inf)
    eps = max(np.linalg.norm(W[np.ix_(G, H)], 2), np.linalg.norm(W[np.ix_(H, G)], 2))
    Win = np.abs(W[np.ix_(G, G)])
    off = ~np.eye(len(G), dtype=bool)
    inside = Win[off]
    across = np.abs(W[np.ix_(G, H)])
    # entrywise: mean over coupled pairs (nonzero entries) inside vs across
    i_nz = inside[inside > 0]
    a_nz = across[across > 0]
    ent = (i_nz.mean() / a_nz.mean()) if len(a_nz) and len(i_nz) else (np.inf if len(i_nz) else 0.0)
    return dict(rho=float(delta / eps) if eps > 0 else np.inf, delta=float(delta),
                eps=float(eps), entrywise=float(ent))


def kappa(T_base, T_free, T_frozen):
    den = T_base - T_frozen
    if abs(den) < 1e-12:
        return float("nan")
    return float((T_free - T_frozen) / den)


# ------------------------------------------------------------------ arm A
class Kink:
    def __init__(self, h, L=40.0):
        self.h = h
        self.n = int(round(L / h)) - 1          # interior sites
        self.x = (np.arange(self.n) + 1) * h - L / 2
        self.L = L

    def energy_grad(self, phi):
        h = self.h
        p = np.concatenate(([-1.0], phi, [1.0]))
        d = np.diff(p) / h
        E = h * (0.5 * np.sum(d ** 2) + np.sum((phi ** 2 - 1) ** 2) / 4)
        lap = (p[2:] - 2 * p[1:-1] + p[:-2]) / h ** 2
        g = h * (-lap + phi ** 3 - phi)
        return E, g

    def relax(self, phi0, clamp=None, clamp_val=None):
        """Minimize energy with sites `clamp` held at clamp_val."""
        free = np.ones(self.n, bool)
        if clamp is not None:
            free[clamp] = False
        phi = phi0.copy()
        if clamp is not None:
            phi[clamp] = clamp_val

        def f(z):
            phi[free] = z
            E, g = self.energy_grad(phi)
            return E, g[free]

        r = minimize(f, phi[free], jac=True, method="L-BFGS-B",
                     options=dict(maxiter=20000, gtol=1e-11, ftol=1e-15))
        phi[free] = r.x
        return phi

    def flow(self, phi0, clamp, clamp_val, T):
        """Overdamped dynamics for time T with sites `clamp` held (explicit Euler)."""
        h = self.h
        dt = 0.2 * h * h
        phi = phi0.copy()
        phi[clamp] = clamp_val
        for _ in range(int(round(T / dt))):
            p = np.concatenate(([-1.0], phi, [1.0]))
            lap = (p[2:] - 2 * p[1:-1] + p[:-2]) / h ** 2
            phi = phi + dt * (lap + phi - phi ** 3)
            phi[clamp] = clamp_val
        return phi

    def ground(self, X0=0.0):
        # centred between sites: the on-site kink is the Peierls-Nabarro saddle
        Xc = X0 + self.h / 2
        return self.relax(np.tanh((self.x - Xc) / np.sqrt(2)))

    def hessian(self, phi):
        h = self.h
        n = self.n
        Hm = np.diag(2 / h ** 2 + 3 * phi ** 2 - 1)
        Hm -= np.diag(np.ones(n - 1) / h ** 2, 1) + np.diag(np.ones(n - 1) / h ** 2, -1)
        return Hm  # generator is -Hm (per site, h factor dropped)

    def fit(self, phi):
        """Distance of phi to the declared family tanh((x - X)/w0) over X,
        with w0 = sqrt(2) the continuum width. Returns (d, X)."""
        best = (np.inf, 0.0)
        for X in np.linspace(-15, 15, 3001):
            d = np.sqrt(self.h * np.sum((phi - np.tanh((self.x - X) / np.sqrt(2))) ** 2))
            if d < best[0]:
                best = (d, X)
        X0 = best[1]
        for X in np.linspace(X0 - 0.01, X0 + 0.01, 101):
            d = np.sqrt(self.h * np.sum((phi - np.tanh((self.x - X) / np.sqrt(2))) ** 2))
            if d < best[0]:
                best = (d, X)
        return best


def arm_A_items():
    for h in (1.0, 0.5, 0.25):
        yield ("A-spectrum", h, None)
        yield ("A-blocktest", h, None)
        for X0 in (0.0, 6.0):
            yield ("A-compensation", h, X0)


def run_A(kind, h, X0):
    k = Kink(h)
    if kind == "A-spectrum":
        phi = k.ground()
        ev, V = np.linalg.eigh(k.hessian(phi))
        v0 = V[:, 0]
        pr = 1.0 / np.sum(v0 ** 4) * h  # participation length
        Q = 0.5 * (1.0 - (-1.0))
        return dict(eig=[float(e) for e in ev[:4]], continuum_edge=2.0,
                    zero_mode_participation_length=float(pr), charge=Q,
                    fit_residual=float(k.fit(phi)[0]))
    if kind == "A-blocktest":
        phi = k.ground()
        gen = -k.hessian(phi)
        W = gen.copy()
        np.fill_diagonal(W, 0.0)
        n = k.n
        Xk = k.fit(phi)[1]
        bylen = {}
        for a in range(n):
            for b in range(a + 2, n + 1):
                if b - a == n:
                    continue
                r = block_test(W, np.arange(a, b), gen)
                contains = k.x[a] - h / 2 <= Xk <= k.x[b - 1] + h / 2
                far = min(abs(k.x[a] - Xk), abs(k.x[b - 1] - Xk)) > 5 and not contains
                Lseg = round((b - a) * h, 6)
                e = bylen.setdefault(Lseg, dict(kink=-1.0, far=-1.0, ent=set()))
                if contains:
                    e["kink"] = max(e["kink"], r["rho"])
                if far:
                    e["far"] = max(e["far"], r["rho"])
                e["ent"].add(round(r["entrywise"], 6))
        table = {str(L): dict(max_rho_containing_kink=v["kink"], max_rho_far_vacuum=v["far"],
                              entrywise=sorted(v["ent"]))
                 for L, v in sorted(bylen.items()) if L in (2 * h, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0)}
        return dict(n_sites=n, kink_X=Xk, eps=1 / h ** 2, by_length=table)
    if kind == "A-compensation":
        phi0 = k.ground(X0)
        d0, Xb = k.fit(phi0)
        a = 0.3
        out = []
        # every site within 10 of the kink centre, and a few far ones
        step = max(1, int(round(0.5 / h)))
        idx = [i for i in range(0, k.n, step) if abs(k.x[i] - X0) <= 6.0]
        for j in idx:
            for sgn in (+1, -1):
                val = np.clip(phi0[j] + sgn * a, -1.5, 1.5)
                frozen = phi0.copy()
                frozen[j] = val
                dF, XF = k.fit(frozen)
                row = dict(site=float(k.x[j]), sign=sgn, d_base=d0, d_frozen=dF)
                for T in (5.0, 50.0):
                    free = k.flow(phi0, [j], val, T)
                    dR, XR = k.fit(free)
                    moved = np.delete(np.abs(free - phi0), j)
                    # task variable T = -distance to the declared family
                    row[f"T{int(T)}"] = dict(kappa=kappa(-d0, -dR, -dF), d_free=dR,
                                            X_shift=XR - Xb, max_other_change=float(moved.max()))
                out.append(row)
        return dict(X0=X0, X_fit=Xb, rows=out)


# ------------------------------------------------------------- arms B, C
def kuramoto_run(omega, Kmat, T, dt, theta0, detune=None, clamp=None, frozen_traj=None,
                 rec_every=10):
    """RK4. clamp: (S, function t -> phases for S) held exactly.
    frozen_traj: (mask_frozen, traj array [steps+1, N]) replays baseline for masked.
    Returns recorded phases (unwrapped) and times."""
    N = len(omega)
    w = omega.copy()
    if detune is not None:
        S, D = detune
        w[S] += D
    th = theta0.copy()
    steps = int(round(T / dt))
    rec = [th.copy()]

    def f(th):
        dif = th[None, :] - th[:, None]
        return w + np.sum(Kmat * np.sin(dif), axis=1)

    for s in range(steps):
        t = s * dt
        k1 = f(th)
        k2 = f(th + 0.5 * dt * k1)
        k3 = f(th + 0.5 * dt * k2)
        k4 = f(th + dt * k3)
        th = th + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if clamp is not None:
            S, g = clamp
            th[S] = g(t + dt)
        if frozen_traj is not None:
            m, traj = frozen_traj
            th[m] = traj[s + 1][m]
        rec.append(th.copy())
    rec = np.array(rec)
    return rec[::rec_every] if rec_every > 1 else rec


def setup_uniform(N=200, K=2.5):
    from scipy.stats import norm
    omega = norm.ppf((np.arange(N) + 0.5) / N)  # deterministic Gaussian quantiles
    rng = np.random.default_rng(0)
    rng.shuffle(omega)
    Kmat = np.full((N, N), K / N)
    np.fill_diagonal(Kmat, 0.0)
    return omega, Kmat


def setup_blocks(n=50, Kin=4.0, Kout=0.1):
    from scipy.stats import norm
    base = norm.ppf((np.arange(n) + 0.5) / n) * 0.5
    omega = np.concatenate([base - 1.5, base + 1.5])
    N = 2 * n
    Kmat = np.full((N, N), Kout / N)
    Kmat[:n, :n] = Kin / N
    Kmat[n:, n:] = Kin / N
    np.fill_diagonal(Kmat, 0.0)
    return omega, Kmat


def realized_jacobian(rec, Kmat, signed=True):
    """Time mean of the Jacobian K_ij cos(theta_j - theta_i) over recorded states."""
    acc = np.zeros_like(Kmat)
    for th in rec:
        c = np.cos(th[None, :] - th[:, None])
        acc += Kmat * (c if signed else np.abs(c))
    W = acc / len(rec)
    np.fill_diagonal(W, 0.0)
    gen = W - np.diag(W.sum(axis=1))
    return W, gen


def osc_items():
    for arm in ("B", "C"):
        yield (arm, "baseline", None)
        yield (arm, "blocktest", None)
        yield (arm, "entrain", "form")
        yield (arm, "entrain", "outside")
        yield (arm, "compensate", "form")
        yield (arm, "compensate", "outside")


_cache = {}


def baseline(arm, dt=0.05, Ttr=300.0, T=200.0):
    if arm in _cache:
        return _cache[arm]
    omega, Kmat = setup_uniform() if arm == "B" else setup_blocks()
    N = len(omega)
    rng = np.random.default_rng(1)
    th0 = rng.uniform(0, 2 * np.pi, N)
    tr = kuramoto_run(omega, Kmat, Ttr, dt, th0, rec_every=int(Ttr / dt))
    th1 = tr[-1]
    full = kuramoto_run(omega, Kmat, T, dt, th1, rec_every=1)
    freq = (full[-1] - full[0]) / T
    _cache[arm] = (omega, Kmat, th1, full, freq, dt, T)
    return _cache[arm]


def forms(arm, freq, omega):
    """The form whose members are tested: B, the locked cluster (mean
    frequency within 1e-3 of the cluster's); C, the first block."""
    N = len(omega)
    if arm == "B":
        Om = np.median(freq)
        locked = np.where(np.abs(freq - Om) < 1e-3)[0]
        return locked
    return np.arange(N // 2)


def coherence(rec, G):
    z = np.exp(1j * rec[:, G]).mean(axis=1)
    return float(np.abs(z).mean())


def run_osc(arm, kind, which):
    omega, Kmat, th1, full, freq, dt, T = baseline(arm)
    N = len(omega)
    F = forms(arm, freq, omega)
    out_ = np.setdiff1d(np.arange(N), F)
    if kind == "baseline":
        return dict(N=N, form_size=int(len(F)), coherence_form=coherence(full[::10], F),
                    coherence_all=coherence(full[::10], np.arange(N)),
                    form_freq=float(np.median(freq[F])),
                    form_freq_spread=float(np.ptp(freq[F])))
    if kind == "blocktest":
        res = {}
        Wst = Kmat.copy()
        genst = Wst - np.diag(Wst.sum(axis=1))
        rng = np.random.default_rng(2)
        rand = [rng.choice(N, len(F), replace=False) for _ in range(20)]
        for name, (W, gen) in (("structural", (Wst, genst)),
                               ("realized_signed", realized_jacobian(full[::20], Kmat, True)),
                               ("realized_abs", realized_jacobian(full[::20], Kmat, False))):
            r = block_test(W, F, gen)
            rr = [block_test(W, g, gen)["rho"] for g in rand]
            res[name] = dict(form=r, random_same_size_rho=[float(np.min(rr)), float(np.median(rr)), float(np.max(rr))])
        return res
    rng = np.random.default_rng(3)
    pool = F if which == "form" else out_
    if arm == "C" and which == "outside":
        pool = out_
    S = np.sort(rng.choice(pool, 5, replace=False))
    rest = np.setdiff1d(F, S)
    if kind == "entrain":
        D = 0.2
        rec = kuramoto_run(omega, Kmat, T, dt, th1, detune=(S, D), rec_every=1)
        fr = (rec[-1] - rec[0]) / T
        dS = float(np.mean(fr[S] - freq[S]))
        dR = float(np.mean(fr[rest] - freq[rest]))
        return dict(S=S.tolist(), Delta=D, shift_S=dS, shift_rest_of_form=dR,
                    eta_in=1 - dS / D, eta_out=dR / D,
                    ratio_rest_to_S=dR / dS if abs(dS) > 1e-9 else None)
    if kind == "compensate":
        a = 0.8
        # sustained load: S held at their baseline trajectory displaced by a
        base_traj = full

        def g(t, S=S):
            s = int(round(t / dt))
            return base_traj[min(s, len(base_traj) - 1)][S] + a

        th_start = th1.copy()
        th_start[S] += a
        recF = kuramoto_run(omega, Kmat, T, dt, th_start, clamp=(S, g), rec_every=1)
        frozen = base_traj.copy()
        frozen[:, S] += a
        Tb = coherence(full[len(full) // 2:], F)
        Tfree = coherence(recF[len(recF) // 2:], F)
        Tfro = coherence(frozen[len(frozen) // 2:], F)
        out = dict(S=S.tolist(), load=a, T_base=Tb, T_free=Tfree, T_frozen=Tfro,
                   kappa=kappa(Tb, Tfree, Tfro))
        if arm == "C":
            G2 = np.arange(N // 2, N)
            Tb2 = coherence(full[len(full) // 2:], G2)
            Tf2 = coherence(recF[len(recF) // 2:], G2)
            out.update(other_block_T_base=Tb2, other_block_T_free=Tf2)
        return out


# ------------------------------------------------------------------ driver
def done_keys():
    keys = set()
    if os.path.exists(OUT):
        with open(OUT) as fh:
            for line in fh:
                try:
                    keys.add(json.loads(line)["key"])
                except Exception:
                    pass
    return keys


def append(key, res):
    with open(OUT, "a") as fh:
        fh.write(json.dumps(dict(key=key, result=res), default=float) + "\n")
        fh.flush()


def main(which=("A", "osc")):
    have = done_keys()
    if "A" in which:
        for item in arm_A_items():
            key = "|".join(map(str, item))
            if key in have:
                continue
            append(key, run_A(*item))
            print("done", key, flush=True)
    if "osc" in which:
        for item in osc_items():
            key = "|".join(map(str, item))
            if key in have:
                continue
            append(key, run_osc(*item))
            print("done", key, flush=True)


if __name__ == "__main__":
    main(tuple(sys.argv[1:]) or ("A", "osc"))
