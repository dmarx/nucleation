"""LEAD-036: QUESTION-386's maintenance-funding loop, coupled and decoupled.

The model is A's, as QUESTION-386 records it, with the three processes the
question names:

    k_{t+1} = min(1, (1 - delta) k_t + beta m_t)      competence decay
    B_{t+1} = Bbar + eta * Mbar_t                     funding feedback
    m_t     = max(0, B_t - h)                         maintenance from budget
    M_t     ~ Binomial(N_t, p(k_t)),  N_t ~ Poisson(lam)   coverage feedback

k is competence in [0, 1]; h is the fixed cost of keeping the capability
(staff, equipment), so only the budget above h buys maintenance training;
N_t is the number of occasions in period t that call for the capability (a
rare contingency); p(k) is the chance a commander commits it to one, a ramp
from 0 at k_lo to 1 at k_hi, so a weaker capability is committed less and
observed doing less; M_t is the observed activity, the commitments; Mbar_t
is its mean over the last W periods (W = 1 is A's rule as written). A
committed capability meets the contingency with probability k.

Rules for the budget:

- ``coupled``: B as above (A's rule).
- ``coupled_nocov``: the same, but p = 1 (committed whatever its state), so
  coverage feedback is switched off; an ablation.
- ``decoupled_full``: maintenance funding decoupled from observed activity,
  B fixed at Bbar + eta * lam, what the coupled rule gives a capability
  committed to every occasion, on average.
- ``decoupled_equal``: B fixed at the mean budget the coupled rule actually
  paid, over all runs and periods of the same configuration: the same money,
  not tied to activity.

All rates are invented and stated per period (a quarter). Results are
written one configuration per line, as JSON, and a rerun skips what is
already written.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
from dataclasses import asdict, dataclass, replace

import numpy as np


@dataclass(frozen=True)
class Params:
    delta: float = 0.08     # competence decay a quarter (half-life ~8 quarters)
    beta: float = 0.10      # competence per unit of maintenance
    h: float = 1.0          # fixed cost of keeping the capability
    Bbar: float = 1.2       # base budget
    eta_lam: float = 0.52   # eta * lam: budget added at full commitment, on average
    lam: float = 0.25       # occasions a quarter
    k_lo: float = 0.4       # below this, never committed
    k_hi: float = 0.8       # above this, always committed
    W: int = 1              # periods of activity the budget looks back on
    T: int = 120            # quarters (30 years)
    k0: float = 0.9         # starting competence
    runs: int = 2000
    B0: float | None = None  # starting budget; None = Bbar + eta_lam (funded as if fully used)

    @property
    def eta(self) -> float:
        return self.eta_lam / self.lam

    @property
    def k_base(self) -> float:
        """Competence the base budget alone sustains."""
        return min(1.0, self.beta * max(0.0, self.Bbar - self.h) / self.delta)


def commit_prob(k, k_lo, k_hi):
    """Chance of commitment: 0 below k_lo, 1 above k_hi, linear between."""
    return np.clip((np.asarray(k, dtype=float) - k_lo) / (k_hi - k_lo), 0.0, 1.0)


def k_star(B, p: Params):
    """Steady competence under a fixed budget B."""
    return np.minimum(1.0, p.beta * np.maximum(0.0, np.asarray(B, float) - p.h) / p.delta)


def mean_field_map(k, p: Params, coverage: bool = True):
    """Steady competence the coupled rule gives if activity sat at its mean at k."""
    q = commit_prob(k, p.k_lo, p.k_hi) if coverage else np.ones_like(np.asarray(k, float))
    return k_star(p.Bbar + p.eta_lam * q, p)


def fixed_points(p: Params, coverage: bool = True, n: int = 200001):
    """Fixed points of the mean-field map on [0, 1], with stability.

    Returns a list of (k, 'stable'|'unstable'). Found as sign changes of
    g(k) = F(k) - k on a fine grid, plus exact zeros.
    """
    k = np.linspace(0.0, 1.0, n)
    g = mean_field_map(k, p, coverage) - k
    out = []
    i = 0
    while i < n - 1:
        if g[i] == 0.0:
            # stable if g goes from + to - across it
            left = g[i - 1] if i > 0 else 1.0
            right = g[i + 1]
            out.append((float(k[i]), "stable" if left >= 0 and right <= 0 else "unstable"))
            i += 1
            continue
        if g[i] * g[i + 1] < 0:
            kk = k[i] - g[i] * (k[i + 1] - k[i]) / (g[i + 1] - g[i])
            out.append((float(kk), "stable" if g[i] > 0 else "unstable"))
        i += 1
    if g[-1] == 0.0:
        out.append((1.0, "stable" if g[-2] >= 0 else "unstable"))
    # merge duplicates within grid tolerance
    merged = []
    for kk, s in out:
        if not merged or abs(kk - merged[-1][0]) > 2.0 / n:
            merged.append((kk, s))
    return merged


def simulate(p: Params, rule: str, seed: int, B_fixed: float | None = None,
             record_paths: bool = False):
    """Run p.runs independent histories under one budget rule, vectorized.

    Every rule with the same (lam, seed) sees the same occasions: N_t is drawn
    from its own stream, and commitment and success use uniforms from a second
    stream compared against p(k) and k, so histories differ only through k.
    """
    R, T = p.runs, p.T
    rng_n = np.random.default_rng([seed, 1])
    rng_u = np.random.default_rng([seed, 2])
    N = rng_n.poisson(p.lam, size=(T, R))
    nmax = int(N.max()) if N.size else 0
    U_commit = rng_u.random(size=(T, R, max(nmax, 1)))
    U_success = rng_u.random(size=(T, R, max(nmax, 1)))

    k = np.full(R, p.k0)
    if rule in ("decoupled_full", "decoupled_equal"):
        if B_fixed is None:
            B_fixed = p.Bbar + p.eta_lam
        B = np.full(R, float(B_fixed))
    elif rule in ("coupled", "coupled_nocov"):
        B0 = p.Bbar + p.eta_lam if p.B0 is None else p.B0
        B = np.full(R, float(B0))
    else:
        raise ValueError(rule)

    # last W periods of observed activity, consistent with the starting budget
    hist = np.full((p.W, R), (float(B[0]) - p.Bbar) / p.eta)
    slots = np.arange(max(nmax, 1))

    k_path = np.zeros((T + 1, R)); k_path[0] = k
    B_path = np.zeros((T, R))
    occ = np.zeros(R); met = np.zeros(R); committed = np.zeros(R)
    occ_late = np.zeros(R); met_late = np.zeros(R)
    late = T // 2
    for t in range(T):
        B_path[t] = B
        m = np.maximum(0.0, B - p.h)
        q = np.ones(R) if rule == "coupled_nocov" else commit_prob(k, p.k_lo, p.k_hi)
        live = slots[None, :] < N[t][:, None]                  # (R, nmax)
        c = live & (U_commit[t] < q[:, None])
        s = c & (U_success[t] < k[:, None])
        M = c.sum(axis=1).astype(float)
        occ += N[t]; committed += M; met += s.sum(axis=1)
        if t >= late:
            occ_late += N[t]; met_late += s.sum(axis=1)
        # next period
        k = np.minimum(1.0, (1.0 - p.delta) * k + p.beta * m)
        k_path[t + 1] = k
        if rule in ("coupled", "coupled_nocov"):
            hist = np.roll(hist, 1, axis=0); hist[0] = M
            B = p.Bbar + p.eta * hist.mean(axis=0)
    out = {
        "k_path": k_path, "B_path": B_path, "occ": occ, "met": met,
        "committed": committed, "occ_late": occ_late, "met_late": met_late,
        "B_fixed": B_fixed,
    }
    return out


def summarize(p: Params, res, rule: str = "coupled") -> dict:
    k_path, B_path = res["k_path"], res["B_path"]
    kT = k_path[-1]
    below = k_path < p.k_lo
    # absorbed ("lost"): only the coupled rule with coverage feedback has an
    # absorbing state, reached once k < k_lo when k_base < k_lo (never
    # committed again, budget Bbar for good). Other rules report only
    # below_lo_end.
    absorbing = rule == "coupled" and p.k_base < p.k_lo
    absorbed = (kT < p.k_lo) & absorbing
    first_below = np.where(below.any(axis=0), below.argmax(axis=0), -1)
    fb = first_below[absorbed]
    tot_occ = res["occ"].sum(); tot_late = res["occ_late"].sum()
    return {
        "lost": float(absorbed.mean()) if absorbing else None,
        "below_lo_end": float((kT < p.k_lo).mean()),
        "lost_quarter_q": [float(x) for x in np.percentile(fb, [25, 50, 75])] if fb.size else None,
        "k_end_mean": float(kT.mean()),
        "k_end_sd": float(kT.std()),
        "k_mean": float(k_path[1:].mean()),
        "B_mean": float(B_path.mean()),
        "met_share": float(res["met"].sum() / tot_occ) if tot_occ else None,
        "met_share_late": float(res["met_late"].sum() / tot_late) if tot_late else None,
        "committed_share": float(res["committed"].sum() / tot_occ) if tot_occ else None,
        "B_fixed": res["B_fixed"],
    }


LAMS = [0.05, 0.1, 0.25, 1.0, 4.0]
WS = [1, 4]
BBARS = [1.2, 1.35]
RULES = ["coupled", "coupled_nocov", "decoupled_full", "decoupled_equal"]
SEED = 20261122


def key_of(d):
    return f"lam={d['lam']}|W={d['W']}|Bbar={d['Bbar']}|rule={d['rule']}"


def run_grid(path: str, base: Params = Params()):
    done = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line:
                    d = json.loads(line)
                    done[key_of(d)] = d
    with open(path, "a") as f:
        for lam, W, Bbar in itertools.product(LAMS, WS, BBARS):
            p = replace(base, lam=lam, W=W, Bbar=Bbar)
            for rule in RULES:
                d = {"lam": lam, "W": W, "Bbar": Bbar, "rule": rule}
                if key_of(d) in done:
                    continue
                B_fixed = None
                if rule == "decoupled_equal":
                    B_fixed = done[key_of({**d, "rule": "coupled"})]["B_mean"]
                res = simulate(p, rule, SEED, B_fixed=B_fixed)
                d.update(summarize(p, res, rule))
                d["params"] = asdict(p)
                d["fixed_points"] = fixed_points(p) if rule == "coupled" else None
                f.write(json.dumps(d) + "\n"); f.flush()
                done[key_of(d)] = d
    return done


def table(done: dict) -> str:
    lines = []
    for Bbar in BBARS:
        p = replace(Params(), Bbar=Bbar)
        lines.append(f"Bbar = {Bbar}: k_base = {p.k_base:.3f}; mean-field fixed points "
                     f"(coupled) {fixed_points(p)}; without coverage feedback "
                     f"{fixed_points(p, coverage=False)}")
    lines.append("")
    hdr = (f"{'lam':>5} {'W':>2} {'Bbar':>5} {'rule':<16} {'lost':>6} {'below':>6} {'lostQ(25,50,75)':>16} "
           f"{'k_end':>6} {'met':>6} {'met2':>6} {'commit':>6} {'B_mean':>6}")
    lines.append(hdr)
    for Bbar, W, lam in itertools.product(BBARS, WS, LAMS):
        for rule in RULES:
            d = done[key_of({"lam": lam, "W": W, "Bbar": Bbar, "rule": rule})]
            lq = d["lost_quarter_q"]
            lqs = ",".join(f"{x:.0f}" for x in lq) if lq else ""
            lost = "-" if d["lost"] is None else f"{d['lost']:.3f}"
            lines.append(
                f"{lam:>5} {W:>2} {Bbar:>5} {rule:<16} {lost:>6} {d['below_lo_end']:>6.3f} {lqs:>16} "
                f"{d['k_end_mean']:>6.3f} {d['met_share']:>6.3f} {d['met_share_late']:>6.3f} "
                f"{d['committed_share']:>6.3f} {d['B_mean']:>6.3f}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "results.jsonl")
    done = run_grid(out)
    print(table(done))
