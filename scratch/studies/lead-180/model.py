"""LEAD-180: CASE-108's four governance architectures, simulated.

A federated multitask learner (CASE-108's testbed, A41 section 6). A shared
parameter vector theta in R^d, d = d_M + d_m, split into a main block M
(tasks every specialist's data covers) and a minority block m (tasks only
some specialists' data covers). The truth theta* ~ N(0, 1) per dimension;
theta starts at 0.

Specialists (N = n_C + n_D + n_A) each propose an update g_i every round:

* cooperative (C): on M, (theta*_M - theta_M) + noise; on m their data has
  no examples, so their update pulls m toward 0 with weight beta: the
  majority's honest misconception.
* honest dissenter (D): (theta* - theta) + noise on both blocks. On m it
  disagrees with the majority and is right ("distributed but valid minority
  signal").
* adversary (A): behaves as a cooperative for the first t_farm rounds
  (farming reputation), then pushes the attacked block toward
  theta_adv = theta* + tau u (u a unit vector in that block) with boost b_A,
  and behaves cooperatively on the other block. Attack classes: 'overt'
  (u in M) and 'mimic' (u in m: an attack that looks like dissent).
  'none' keeps the adversaries cooperative throughout.

Evaluators: a pool of n_E processes, each holding its own validation
estimate theta_hat_e = theta* + N(0, sigma_v^2) on the blocks it covers
(all cover M; n_Em of them also cover m). An evaluator's verdict on an
update is the change in its validation loss from a step lr * g. On a block
it does not cover it either abstains (jurisdiction-limited) or uses the
prior 0 (not jurisdiction-limited). A compromised evaluator knows the types:
it approves (scores +1) adversaries, rejects (scores -1) dissenters, and
judges cooperatives honestly, claiming jurisdiction everywhere.

Architectures (aggregate rules):

* 'unrestricted': theta += lr * mean_i g_i.
* 'rel-agree': reliability-weighted, reputation from agreement: score
  s_i = cos(g_i, previous aggregate); r_i <- delta r_i + (1 - delta) s_i;
  w = softmax(kappa r); theta += lr * sum_i w_i g_i. No separate evaluator.
* 'rel-val': as rel-agree, but s_i = mean over the pool of each
  evaluator's cos(g_i, theta_hat_e - theta), uncovered dims at the prior 0.
* 'role': role-limited. Proposers propose; a panel of k_p evaluators drawn
  at random each round criticizes per block (jurisdiction-limited); a block
  of an update is approved if at least one panel member has jurisdiction
  and a fraction >= q of those approve. Approved blocks are norm-clipped to
  their median norm (bounded influence) and averaged; a block with no
  approvals does not move.
* 'adaptive': 'role' plus revisable safeguards, revised every t_rev rounds
  from a monitor (an auditing process with its own validation estimate,
  full coverage unless monitor_covers_m is False):
    - revocable authorization: a proposer whose approved contributions over
      the window have mean monitor score (cos with theta_hat_mon - theta)
      below -susp_thr is suspended for t_susp rounds;
    - tightening: if the monitor's loss on a block rose over the window,
      q_b <- min(1, q_b + 0.1);
    - widening jurisdiction: if a block got no approvals in more than half
      the window's rounds, the panel draw is stratified to include a
      jurisdiction holder for it from then on.
  A compromised monitor scores adversaries +1 and dissenters -1 and never
  reports a rise in loss.
* 'oracle': 'role' with a single evaluator holding theta* exactly and full
  jurisdiction: the reference for the same proposals and update
  constraints (QUESTION-087's "oracle or stronger solver").

Scores (oracle-measured, mean of the last `tail` rounds):
  main capability  MC_M = 1 - |theta_M - theta*_M|^2 / |theta*_M|^2
  minority capab.  MC_m = 1 - |theta_m - theta*_m|^2 / |theta*_m|^2
  attack success   AS   = ((theta - theta*) . u) / tau
plus the dissenters' influence ratio over the whole run (their share of what
moves the m block, divided by their head-count share n_D / N: 1 is parity,
0 is suppression), evaluation calls per round, and for
'adaptive' the suspensions.
"""
from __future__ import annotations

import numpy as np

ARCHS = ("unrestricted", "rel-agree", "rel-val", "role", "adaptive", "oracle")


def default_params(**kw):
    p = dict(d_M=8, d_m=4, n_C=14, n_D=3, n_A=3, beta=1.0, sigma_g=0.5,
             lr=0.1, T=300, tail=50,
             attack="overt", tau=3.0, b_A=3.0, t_farm=100,
             n_E=7, n_Em=2, sigma_v=0.3, n_comp=0, k_p=3, q=2 / 3,
             delta=0.95, kappa=10.0,
             t_rev=20, susp_thr=0.2, t_susp=60, monitor_covers_m=True,
             monitor_comp=False, central=False, swap_targets=False)
    p.update(kw)
    return p


# ------------------------------------------------------------ setup
def make_world(P, rng):
    d_M, d_m = P["d_M"], P["d_m"]
    d = d_M + d_m
    theta_star = rng.normal(size=d)
    blk = np.zeros(d, dtype=int)
    blk[d_M:] = 1                       # 0 = M, 1 = m
    u = np.zeros(d)
    if P["attack"] in ("overt", "none"):
        v = rng.normal(size=d_M)
        u[:d_M] = v / np.linalg.norm(v)
    else:
        v = rng.normal(size=d_m)
        u[d_M:] = v / np.linalg.norm(v)
    theta_adv = theta_star + P["tau"] * u
    if P["swap_targets"]:               # relabelled world for the symmetry check
        theta_star, theta_adv = theta_adv.copy(), theta_star.copy()
        u = -u
    N = P["n_C"] + P["n_D"] + P["n_A"]
    types = np.array([0] * P["n_C"] + [1] * P["n_D"] + [2] * P["n_A"])  # C, D, A
    if P["central"]:
        n_E, n_Em = 1, 1
    else:
        n_E, n_Em = P["n_E"], P["n_Em"]
    cover = np.zeros((n_E, 2), dtype=bool)
    cover[:, 0] = True
    cover[:n_Em, 1] = True
    theta_hat = theta_star + P["sigma_v"] * rng.normal(size=(n_E, d))
    comp = np.zeros(n_E, dtype=bool)
    nc = min(P["n_comp"], n_E)
    if nc:
        # compromise evaluators at random, independent of coverage
        comp[rng.choice(n_E, nc, replace=False)] = True
    mon_hat = theta_star + P["sigma_v"] * rng.normal(size=d)
    return dict(theta_star=theta_star, theta_adv=theta_adv, u=u, blk=blk,
                types=types, N=N, d=d, cover=cover, theta_hat=theta_hat,
                comp=comp, mon_hat=mon_hat)


# ------------------------------------------------------------ proposals
def proposals(theta, t, W, P, rng):
    """N x d matrix of proposed updates."""
    ts, blk, types = W["theta_star"], W["blk"], W["types"]
    N, d = W["N"], W["d"]
    noise = P["sigma_g"] * rng.normal(size=(N, d))
    coop = np.where(blk == 0, ts - theta, P["beta"] * (0.0 - theta))
    honest = ts - theta
    G = np.empty((N, d))
    G[types == 0] = coop
    G[types == 1] = honest
    attacking = P["attack"] != "none" and t >= P["t_farm"]
    if attacking:
        ab = 0 if P["attack"] == "overt" else 1
        adv = np.where(blk == ab, P["b_A"] * (W["theta_adv"] - theta), coop)
        G[types == 2] = adv
    else:
        G[types == 2] = coop
    return G + noise


# ------------------------------------------------------------ evaluation
def cos_rows(G, v):
    nG = np.linalg.norm(G, axis=1)
    nv = np.linalg.norm(v)
    return (G @ v) / np.maximum(nG * nv, 1e-12)


def evaluator_block_verdicts(theta, G, W, P, panel, oracle=False):
    """Votes (panel x N x 2) in {+1 approve, -1 reject, 0 abstain}.

    A vote is the sign of the change in the evaluator's validation loss on
    that block from the step lr * g_i (improvement approves)."""
    blk, types = W["blk"], W["types"]
    lr = P["lr"]
    N = W["N"]
    votes = np.zeros((len(panel), N, 2))
    for k, e in enumerate(panel):
        target = W["theta_star"] if oracle else W["theta_hat"][e]
        for b in (0, 1):
            mask = blk == b
            r = (target - theta)[mask]
            gb = G[:, mask]
            # L(theta) - L(theta + lr g) = 2 lr g.r - lr^2 |g|^2
            imp = 2 * lr * gb @ r - lr ** 2 * np.sum(gb ** 2, axis=1)
            v = np.sign(imp)
            if not oracle and W["comp"][e]:
                v = np.where(types == 2, 1.0, np.where(types == 1, -1.0, v))
            elif not oracle and not W["cover"][e, b]:
                v = np.zeros(N)
            votes[k, :, b] = v
    return votes


def rel_val_scores(theta, G, W, P):
    """Mean over the pool of cos(g_i, theta_hat_e - theta), prior 0 off cover."""
    types = W["types"]
    S = np.zeros(W["N"])
    for e in range(W["theta_hat"].shape[0]):
        tgt = np.where(W["cover"][e][W["blk"]], W["theta_hat"][e], 0.0)
        s = cos_rows(G, tgt - theta)
        if W["comp"][e]:
            s = np.where(types == 2, 1.0, np.where(types == 1, -1.0, s))
        S += s
    return S / W["theta_hat"].shape[0]


def clipped_mean(Gb, ok):
    """Mean of the approved rows, each clipped to the approved rows' median norm."""
    if not ok.any():
        return np.zeros(Gb.shape[1])
    A = Gb[ok]
    n = np.linalg.norm(A, axis=1)
    c = np.median(n)
    A = A * np.minimum(1.0, c / np.maximum(n, 1e-12))[:, None]
    return A.mean(axis=0)


# ------------------------------------------------------------ run
def run(arch, P, seed):
    """Simulate one architecture. Returns a dict of trajectories and scores."""
    rng = np.random.default_rng(seed)
    W = make_world(P, rng)
    rng_run = np.random.default_rng(seed + 10_000)  # proposals share noise across arms
    rng_panel = np.random.default_rng(seed + 20_000)
    N, d, blk, types = W["N"], W["d"], W["blk"], W["types"]
    theta = np.zeros(d)
    r = np.zeros(N)
    prev_agg = None
    q = np.array([P["q"], P["q"]])
    stratify = np.array([False, False])
    suspended_until = np.full(N, -1)
    susp_log = []                     # (t, agent, type)
    window = []                       # per round: (approved mask N x 2, G)
    mon_loss_hist = []
    n_E_pool = W["theta_hat"].shape[0]
    T = P["T"]
    traj = dict(MC_M=np.empty(T), MC_m=np.empty(T), AS=np.empty(T),
                dshare=np.empty(T))
    evals = 0
    ts = W["theta_star"]
    for t in range(T):
        G = proposals(theta, t, W, P, rng_run)
        dshare = np.nan
        if arch == "unrestricted":
            step = G.mean(axis=0)
            dshare = 1.0
        elif arch in ("rel-agree", "rel-val"):
            if arch == "rel-agree":
                ref = G.mean(axis=0) if prev_agg is None else prev_agg
                s = cos_rows(G, ref)
                evals += N
            else:
                s = rel_val_scores(theta, G, W, P)
                evals += N * n_E_pool
            r = P["delta"] * r + (1 - P["delta"]) * s
            z = P["kappa"] * r
            w = np.exp(z - z.max())
            w /= w.sum()
            step = w @ G
            prev_agg = step
            dshare = w[types == 1].sum() / (P["n_D"] / N)
        else:
            oracle = arch == "oracle"
            active = suspended_until <= t
            if oracle:
                panel = [0]
            elif P["central"]:
                panel = [0]
            else:
                panel = list(rng_panel.choice(n_E_pool, P["k_p"], replace=False))
                for b in (0, 1):
                    if stratify[b] and not any(W["cover"][e, b] for e in panel):
                        holders = np.flatnonzero(W["cover"][:, b])
                        if len(holders):
                            panel[-1] = int(rng_panel.choice(holders))
            votes = evaluator_block_verdicts(theta, G, W, P, panel, oracle=oracle)
            evals += len(panel) * N * 2
            juris = (votes != 0).sum(axis=0)              # N x 2
            appr = (votes > 0).sum(axis=0)
            ok = (juris > 0) & (appr >= q[None, :] * juris - 1e-12)
            ok &= active[:, None]
            step = np.zeros(d)
            for b in (0, 1):
                mask = blk == b
                step[mask] = clipped_mean(G[:, mask], ok[:, b])
            n_ok = ok[:, 1].sum()
            dshare = (ok[types == 1, 1].sum() / n_ok / (P["n_D"] / N)
                      if n_ok and P["n_D"] else np.nan)
            if arch == "adaptive":
                window.append((ok.copy(), G.copy(), theta.copy()))
                mon_loss_hist.append([np.sum(((W["mon_hat"] - theta)[blk == b]) ** 2)
                                      for b in (0, 1)])
                if (t + 1) % P["t_rev"] == 0:
                    evals += N * P["t_rev"]
                    # revocable authorization
                    sc_sum = np.zeros(N)
                    sc_n = np.zeros(N)
                    for okw, Gw, thw in window:
                        mtarget = W["mon_hat"].copy()
                        if not P["monitor_covers_m"]:
                            mtarget[blk == 1] = 0.0
                        cs = cos_rows(Gw, mtarget - thw)
                        used = okw.any(axis=1)
                        sc_sum += np.where(used, cs, 0.0)
                        sc_n += used
                    sc = np.where(sc_n > 0, sc_sum / np.maximum(sc_n, 1), 0.0)
                    if P["monitor_comp"]:
                        sc = np.where(types == 2, 1.0, np.where(types == 1, -1.0, sc))
                    for i in np.flatnonzero((sc < -P["susp_thr"]) & (sc_n > 0)
                                            & (suspended_until <= t)):
                        suspended_until[i] = t + P["t_susp"]
                        susp_log.append((t, int(i), int(types[i])))
                    # tightening
                    lh = np.array(mon_loss_hist)
                    for b in (0, 1):
                        if b == 1 and not P["monitor_covers_m"]:
                            continue
                        rose = lh[-1, b] > lh[0, b]
                        if rose and not P["monitor_comp"]:
                            q[b] = min(1.0, q[b] + 0.1)
                    # widening jurisdiction
                    oks = np.array([okw.any(axis=0) for okw, _, _ in window])
                    for b in (0, 1):
                        if (~oks[:, b]).mean() > 0.5:
                            stratify[b] = True
                    window, mon_loss_hist = [], []
        theta = theta + P["lr"] * step
        e = theta - ts
        traj["MC_M"][t] = 1 - np.sum(e[blk == 0] ** 2) / np.sum(ts[blk == 0] ** 2)
        traj["MC_m"][t] = 1 - np.sum(e[blk == 1] ** 2) / np.sum(ts[blk == 1] ** 2)
        traj["AS"][t] = (e @ W["u"]) / P["tau"]
        traj["dshare"][t] = dshare
    tl = slice(T - P["tail"], T)
    out = dict(MC_M=float(traj["MC_M"][tl].mean()),
               MC_m=float(traj["MC_m"][tl].mean()),
               AS=float(traj["AS"][tl].mean()),
               dshare=float(np.nanmean(traj["dshare"])) if np.isfinite(traj["dshare"]).any() else float("nan"),
               evals_per_round=evals / T, traj=traj, susp=susp_log)
    return out
