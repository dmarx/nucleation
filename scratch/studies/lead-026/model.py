"""CASE-101's three populations, simulated (LEAD-026).

Eight observed variables in every arm, in this order:
    x_0 .. x_5   six member slots (a slot's occupant turns over),
    e            one environmental variable, different in each arm,
    z            an unrelated AR(1) distractor, in every arm.

Every step, each slot's occupant is replaced with probability r (the same
in all arms). A slot's value is its current occupant's norm. Occupant
identity is not observed.

Arm A, common input (e = u, an exogenous AR(1) driver):
    x_i' = a x_i + b u + s xi;   a newcomer arrives naive, x_i' ~ N(0, 1).
Arm B, reproducing organization (e = v, an inert AR(1) nobody reads):
    x_i' = a x_i + c mean_{j != i} x_j(t + 1 - L) + s xi;
    a newcomer copies a random other member's norm of L steps ago,
    x_i' = x_k(t + 1 - L) + s_copy xi. All coupling between members is
    at lag L: none is synchronous.
Arm C, institutionally maintained (e = g, an institution):
    x_i' = a x_i + k g + s xi   (training);
    g'   = rho_g g + eta mean(x) + s_g xi   (it governs and answers to them);
    a newcomer is selected near the institution's standard,
    x_i' = g + s_sel xi.
Arm C0: arm C with eta = 0, the institution deaf to its members, so its
    coupling to them is one-way like arm A's driver.

The free parameters (a, gain, s) of each arm are calibrated (calibrate.py)
so that the member variance, the mean pairwise correlation of members and
the lag-1 autocorrelation of the aggregate mean(x) match across arms.
"""
import numpy as np

N = 6          # member slots
E_IDX = 6      # index of the environmental variable
Z_IDX = 7      # index of the distractor
NV = 8
NAMES = [f"x{i}" for i in range(N)] + ["e", "z"]

BASE = dict(r=0.02, L=8, rho_e=0.95, rho_z=0.9, s_copy=0.3, s_sel=0.3,
            eta=0.05, s_g=0.3)


def _ar1_noise(rho):
    return np.sqrt(1.0 - rho ** 2)


class Sim:
    """A vectorised simulator over R independent replicas."""

    def __init__(self, arm, par, R, rng):
        self.arm, self.p, self.R, self.rng = arm, {**BASE, **par}, R, rng
        p = self.p
        self.x = rng.standard_normal((R, NV)) * 0.5
        self.x[:, E_IDX] = rng.standard_normal(R)
        self.x[:, Z_IDX] = rng.standard_normal(R)
        # history of member norms, hist[-1] is the current state
        self.hist = [self.x[:, :N].copy() for _ in range(p["L"])]

    def lagged_members(self):
        """Member norms at t + 1 - L (the oldest entry kept)."""
        return self.hist[0]

    def step(self):
        p, x, rng, R = self.p, self.x, self.rng, self.R
        m = x[:, :N]
        e = x[:, E_IDX]
        xi = rng.standard_normal((R, N))
        new = np.empty_like(x)
        arm = self.arm
        if arm == "A":
            new[:, :N] = p["a"] * m + p["gain"] * e[:, None] + p["s"] * xi
            new[:, E_IDX] = p["rho_e"] * e + _ar1_noise(p["rho_e"]) * rng.standard_normal(R)
        elif arm == "B":
            old = self.lagged_members()
            others = (old.sum(1, keepdims=True) - old) / (N - 1)
            new[:, :N] = p["a"] * m + p["gain"] * others + p["s"] * xi
            new[:, E_IDX] = p["rho_e"] * e + _ar1_noise(p["rho_e"]) * rng.standard_normal(R)
        elif arm in ("C", "C0"):
            eta = p["eta"] if arm == "C" else 0.0
            new[:, :N] = p["a"] * m + p["gain"] * e[:, None] + p["s"] * xi
            new[:, E_IDX] = p["rho_e"] * e + eta * m.mean(1) + p["s_g"] * rng.standard_normal(R)
        else:
            raise ValueError(arm)
        # turnover, the same rate in every arm
        rep = rng.random((R, N)) < p["r"]
        if arm == "A":
            entry = rng.standard_normal((R, N))
        elif arm == "B":
            old = self.lagged_members()
            # a random mentor k != i for every slot
            k = rng.integers(0, N - 1, size=(R, N))
            k = k + (k >= np.arange(N)[None, :])
            entry = np.take_along_axis(old, k, 1) + p["s_copy"] * rng.standard_normal((R, N))
        else:
            entry = e[:, None] + p["s_sel"] * rng.standard_normal((R, N))
        new[:, :N] = np.where(rep, entry, new[:, :N])
        new[:, Z_IDX] = p["rho_z"] * x[:, Z_IDX] + _ar1_noise(p["rho_z"]) * rng.standard_normal(R)
        self.x = new
        self.hist.pop(0)
        self.hist.append(new[:, :N].copy())

    def intervene(self, idx, values):
        """do(V_idx = values) on the current state; a member value set
        here is also what later reads of the history see."""
        self.x[:, idx] = values
        mem = [i for i in idx if i < N]
        if mem:
            self.hist[-1][:, mem] = self.x[:, mem]

    def run(self, T, burn=0):
        """Advance burn steps, then record T states: array (T, R, NV)."""
        for _ in range(burn):
            self.step()
        out = np.empty((T, self.R, NV))
        for t in range(T):
            self.step()
            out[t] = self.x
        return out


def simulate(arm, par, R, T, burn, seed):
    return Sim(arm, par, R, np.random.default_rng(seed)).run(T, burn)


def aggregate_stats(traj):
    """Member variance, mean pairwise member correlation, lag-1 and lag-16
    autocorrelation of the aggregate mean(x)."""
    m = traj[:, :, :N]
    flat = m.reshape(-1, N)
    C = np.cov(flat.T)
    var = float(np.mean(np.diag(C)))
    sd = np.sqrt(np.diag(C))
    corr = C / np.outer(sd, sd)
    rho = float(corr[np.triu_indices(N, 1)].mean())
    X = m.mean(2)
    Xc = X - X.mean()
    v = float((Xc * Xc).mean())

    def ac(lag):
        return float((Xc[lag:] * Xc[:-lag]).mean() / v)
    return dict(var_member=var, rho_members=rho, var_agg=v,
                ac1_agg=ac(1), ac8_agg=ac(8), ac32_agg=ac(32))
