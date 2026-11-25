"""LEAD-188: a circulation-network model of CASE-100 against the list of
identifiable contributions.

The world. A population of N people on a heavy-tailed contact network
(configuration model). V fan videos are posted, each by one ordinary
person (its makers), and each spreads by bond percolation with its own
transmissibility T_i (the SIR final-size equivalent): s_i is how many
people it reached. The H highest-degree people are the *identifiable
distributors* (the named sites, aggregators and news segments a list of
contributions can name); h_i is how many of them video i reached.

A decision-maker D (the director) adopts the line of exactly one video.
Three models say how likely D is to have adopted video i:

  M0  list without distributors: w_i = 1. Only the makers' act and D's
      decision are named; the spread adds nothing.
  MH  list with identifiable distributors: w_i = 1 + kappa * h_i. The named
      hubs that carried it matter; the rest of the spread does not.
  MC  circulation: w_i = s_i ** alpha. D's chance of meeting the video
      grows with how far it circulated. alpha = 0 switches the
      circulation off and returns M0, smoothly (the model is regular
      there, so CLAIM-154's condition holds).

The observation is the one the case supplies: the adopted video was
among the most circulated (top fraction q by s). Its likelihood under a
model, with case ascertainment weight a_i = s_i ** gamma (gamma > 0 means
the owner came to know of the case partly because the video was famous):

  P(O | model) = sum_{i in top q} w_i a_i / sum_i w_i a_i

averaged over replicate worlds. Free parameters are priced by the exact
marginal likelihood over a stated prior (uniform alpha on [0, 2],
log-uniform kappa on [1e-2, 1e2]); CLAIM-154's reification rule is the
large-sample approximation to this Bayes factor, and with one
observation the exact one is used instead.

Run:  python3 -I model.py   (writes results.json beside this file)
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components


# ----------------------------------------------------------------- network
def make_graph(n: int, gamma: float, kmin: int, kmax: int,
               rng: np.random.Generator) -> np.ndarray:
    """Configuration-model edge list (m, 2), simple: no self-loops or
    multi-edges. Degrees ~ k^-gamma on [kmin, kmax]."""
    ks = np.arange(kmin, kmax + 1)
    p = ks.astype(float) ** -gamma
    p /= p.sum()
    deg = rng.choice(ks, size=n, p=p)
    if deg.sum() % 2:
        deg[rng.integers(n)] += 1
    stubs = np.repeat(np.arange(n), deg)
    rng.shuffle(stubs)
    e = stubs.reshape(-1, 2)
    e = e[e[:, 0] != e[:, 1]]
    e = np.sort(e, axis=1)
    e = np.unique(e, axis=0)
    return e


def degrees(edges: np.ndarray, n: int) -> np.ndarray:
    return np.bincount(edges.ravel(), minlength=n)


def cascade(edges: np.ndarray, n: int, T: float, seed: int,
            rng: np.random.Generator) -> np.ndarray:
    """Bond percolation with transmissibility T; returns the boolean
    membership of the seed's cluster (who the video reached)."""
    keep = rng.random(len(edges)) < T
    e = edges[keep]
    a = coo_matrix((np.ones(len(e)), (e[:, 0], e[:, 1])), shape=(n, n))
    _, lab = connected_components(a, directed=False)
    return lab == lab[seed]


def world(n: int, V: int, H: int, rng: np.random.Generator,
          gamma: float = 2.5, kmin: int = 2, kmax: int = 300,
          t_a: float = 1.0, t_b: float = 6.0):
    """One replicate world: sizes s (V,), hub hits h (V,)."""
    edges = make_graph(n, gamma, kmin, kmax, rng)
    deg = degrees(edges, n)
    hubs = np.argsort(deg)[::-1][:H]
    ordinary = np.setdiff1d(np.arange(n), hubs)
    s = np.empty(V)
    h = np.empty(V)
    Ts = rng.beta(t_a, t_b, size=V)
    seeds = rng.choice(ordinary, size=V)
    for i in range(V):
        reached = cascade(edges, n, Ts[i], seeds[i], rng)
        s[i] = reached.sum()
        h[i] = reached[hubs].sum()
    return s, h


# ------------------------------------------------------------- likelihoods
def top_mask(s: np.ndarray, q: float) -> np.ndarray:
    """The top fraction q of videos by size (at least one), ties broken by
    index so the mask has exactly ceil(qV) members."""
    k = max(1, int(np.ceil(q * len(s))))
    order = np.lexsort((np.arange(len(s)), -s))
    m = np.zeros(len(s), bool)
    m[order[:k]] = True
    return m


def p_obs(w: np.ndarray, s: np.ndarray, q: float, gamma_a: float) -> float:
    """P(adopted video in top q | adopted, ascertained)."""
    a = s ** gamma_a
    wa = w * a
    return float(wa[top_mask(s, q)].sum() / wa.sum())


def w_m0(s, h):
    return np.ones_like(s)


def w_mh(s, h, kappa):
    return 1.0 + kappa * h


def w_mc(s, h, alpha):
    return s ** alpha


ALPHAS = np.linspace(0.0, 2.0, 41)          # uniform prior grid
KAPPAS = np.logspace(-2, 2, 41)             # log-uniform prior grid


def likelihoods(worlds, q: float, gamma_a: float) -> dict:
    """Average P(O|model, theta) over worlds, then marginalize theta over
    the prior grid. Returns marginal likelihoods and the profile curves."""
    L0 = np.mean([p_obs(w_m0(s, h), s, q, gamma_a) for s, h in worlds])
    LC = np.array([np.mean([p_obs(w_mc(s, h, a), s, q, gamma_a)
                            for s, h in worlds]) for a in ALPHAS])
    LH = np.array([np.mean([p_obs(w_mh(s, h, k), s, q, gamma_a)
                            for s, h in worlds]) for k in KAPPAS])
    return {
        "L_M0": float(L0),
        "L_MC_marginal": float(LC.mean()),
        "L_MH_marginal": float(LH.mean()),
        "L_MC_max": float(LC.max()),
        "L_MH_max": float(LH.max()),
        "BF_MC_vs_M0": float(LC.mean() / L0),
        "BF_MH_vs_M0": float(LH.mean() / L0),
        "BF_MC_vs_MH": float(LC.mean() / LH.mean()),
        "curve_MC": LC.round(5).tolist(),
        "curve_MH": LH.round(5).tolist(),
    }


def corr_s_h(worlds) -> float:
    """How far hub hits track circulation: Spearman-like rank correlation
    of s and h pooled over worlds."""
    s = np.concatenate([w[0] for w in worlds])
    h = np.concatenate([w[1] for w in worlds])
    rs = np.argsort(np.argsort(s))
    rh = np.argsort(np.argsort(h + 1e-9 * s))
    return float(np.corrcoef(rs, rh)[0, 1])


def main(out: Path, n: int = 3000, V: int = 300, H: int = 10, R: int = 12,
         seed: int = 188) -> dict:
    rng = np.random.default_rng(seed)
    worlds = [world(n, V, H, rng) for _ in range(R)]
    s_all = np.concatenate([w[0] for w in worlds])
    res = {
        "settings": {"n": n, "V": V, "H": H, "R": R, "seed": seed,
                     "degree_exponent": 2.5, "kmin": 2, "kmax": 300,
                     "T_prior": "Beta(1, 6)",
                     "alpha_prior": "uniform [0, 2], 41-point grid",
                     "kappa_prior": "log-uniform [1e-2, 1e2], 41-point grid"},
        "sizes": {"median": float(np.median(s_all)),
                  "p99": float(np.quantile(s_all, 0.99)),
                  "max": float(s_all.max()),
                  "share_of_reach_in_top_1pct": float(
                      np.mean([w[0][top_mask(w[0], 0.01)].sum() / w[0].sum()
                               for w in worlds]))},
        "rank_corr_s_h": corr_s_h(worlds),
        "runs": [],
    }
    for gamma_a in (0.0, 0.5, 1.0):
        for q in (0.001, 0.01, 0.05):
            r = likelihoods(worlds, q, gamma_a)
            r.update({"q": q, "gamma_ascertainment": gamma_a})
            res["runs"].append(r)
    out.write_text(json.dumps(res, indent=1))
    return res


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    res = main(here / "results.json")
    print(json.dumps({k: v for k, v in res.items() if k != "runs"}, indent=1))
    print(f"{'gamma':>5} {'q':>6} {'L_M0':>7} {'L_MC':>7} {'L_MH':>7} "
          f"{'BF_C/0':>8} {'BF_H/0':>8} {'BF_C/H':>7}")
    for r in res["runs"]:
        print(f"{r['gamma_ascertainment']:>5} {r['q']:>6} {r['L_M0']:>7.4f} "
              f"{r['L_MC_marginal']:>7.4f} {r['L_MH_marginal']:>7.4f} "
              f"{r['BF_MC_vs_M0']:>8.2f} {r['BF_MH_vs_M0']:>8.2f} "
              f"{r['BF_MC_vs_MH']:>7.2f}")
