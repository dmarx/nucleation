"""One item of the study: train (or freeze) one network, compute the four
partitions on four time slices, move walls by interchange, and compare a
closed wall pair with a wall anchored by the boundary conditions."""
import numpy as np

import partitions as Pt
import z2rnn as Z

SLICES = (4, 8, 12, 16)  # 4, 8: input phase (8 is its last state); 12, 16: free phase
LONG_FREE = 200
IN = (3, Z.N - 3)  # interior bonds: walls in the boundary layers at the clamped ends are not counted


def phase_of(T):
    ph = np.zeros(T + 1, dtype=np.int64)
    ph[Z.T_IN + 1:] = 1
    return ph


def eval_set(rng, B):
    S = np.zeros((B, Z.N))
    W = []
    for b in range(B):
        S[b], w = Z.sample_config(rng)
        W.append([int(p) for p in w])
    return S, W


def _valid(walls, n=Z.N, min_domain=Z.MIN_DOMAIN):
    edges = [0] + sorted(walls) + [n]
    return len(set(walls)) == len(walls) and min(np.diff(edges)) >= min_domain


def interchange(P, rng, n_pairs=300, t0s=(4, 8)):
    """Move one wall by two sites by splicing the source run's hidden states
    on the window between the two positions (plus one site each side)."""
    bases, srcs, wins, ctrl_wins = [], [], [], []
    while len(bases) < n_pairs:
        s, walls = Z.sample_config(rng)
        if not walls:
            continue
        j = int(rng.integers(len(walls)))
        dlt = int(rng.choice([-2, 2]))
        w2 = list(walls)
        w2[j] = int(walls[j] + dlt)
        if not _valid(w2):
            continue
        lo, hi = min(walls[j], w2[j]) - 1, max(walls[j], w2[j]) + 1  # sites lo..hi-1
        width = hi - lo
        # control window of the same width, at least 3 sites from every wall
        allw = set(walls) | set(w2)
        cands = [c for c in range(0, Z.N - width + 1)
                 if all(min(abs(c - p), abs(c + width - p)) >= 3 and not (c <= p <= c + width) for p in allw)]
        if not cands:
            continue
        bases.append(s)
        srcs.append(Z.config_from_walls(w2, s[0]))
        wins.append((lo, hi))
        ctrl_wins.append((int(rng.choice(cands)), width))
    Sb, Ss = np.array(bases), np.array(srcs)
    noise = rng.standard_normal((Z.T_IN, len(Sb), Z.N))
    xb = Z.make_inputs(Sb, rng, noise=noise)
    xs = Z.make_inputs(Ss, rng, noise=noise)
    hb, hsrc = Z.forward(P, xb), Z.forward(P, xs)
    yb, ys = Z.readout(P, hb[-1])[0], Z.readout(P, hsrc[-1])[0]
    tb, tsrc = Sb.mean(1) ** 2, Ss.mean(1) ** 2
    out = {}
    for t0 in t0s:
        def splice(windows):
            def hook(t, h):
                if t == t0:
                    h = h.copy()
                    for b, (lo, hi) in enumerate(windows):
                        h[b, lo:hi] = hsrc[t0][b, lo:hi]
                return h
            return hook
        hi_ = Z.forward(P, xb, hook=splice(wins))
        yi = Z.readout(P, hi_[-1])[0]
        cw = [(c, c + w) for c, w in ctrl_wins]
        hc = Z.forward(P, xb, hook=splice(cw))
        yc = Z.readout(P, hc[-1])[0]
        # walls of the intervened run against the source's walls
        moved = np.mean([a == b for a, b in zip(Pt.wall_positions(hi_[-1], *IN), Pt.wall_positions(hsrc[-1], *IN))])
        out[str(t0)] = {
            "iia_task": float(np.mean(np.abs(yi - tsrc) < np.abs(tsrc - tb) / 2)),
            "iia_self": float(np.mean(np.abs(yi - ys) < np.abs(ys - yb) / 2)),
            "walls_match_source": float(moved),
            "control_window_changed": float(np.mean(np.abs(yc - yb) > np.abs(ys - yb) / 2)),
        }
    out["net_source_vs_base_separable"] = float(np.mean(np.abs(ys - yb) > np.abs(tsrc - tb) / 2))
    return out


def closed_vs_anchored(P, rng, reps=50):
    T_long = LONG_FREE
    res = {"closed_pair_survival_by_L": {}, "anchored": {}}
    c = 12
    for L in range(1, 9):
        S = np.ones((reps, Z.N))
        S[:, c:c + L] = -1
        x = Z.make_inputs(S, rng, t_free=T_long)
        hs = Z.forward(P, x)
        sv_end = [len(w) for w in Pt.wall_positions(hs[-1], *IN)]
        sv_trained = [len(w) for w in Pt.wall_positions(hs[Z.T_IN + Z.T_FREE], *IN)]
        res["closed_pair_survival_by_L"][str(L)] = {
            "pair_at_trained_horizon": float(np.mean(np.array(sv_trained) == 2)),
            "pair_at_long_horizon": float(np.mean(np.array(sv_end) == 2)),
            "no_walls_at_long_horizon": float(np.mean(np.array(sv_end) == 0)),
        }
    # anchored single wall
    p = 16
    S = np.ones((reps, Z.N))
    S[:, p:] = -1
    x = Z.make_inputs(S, rng, t_free=T_long)
    hs = Z.forward(P, x)
    ws = Pt.wall_positions(hs[-1], *IN)
    ws_tr0 = Pt.wall_positions(hs[Z.T_IN + Z.T_FREE], *IN)
    res["anchored"]["one_wall_at_trained_horizon"] = float(np.mean([w == [p] for w in ws_tr0]))
    s8 = np.einsum("tbd,bd->tb", hs[Z.T_IN:, :, 8], hs[Z.T_IN, :, 8])
    res["bulk_sign_changes_over_long_free_run"] = float(np.mean(np.sum(np.diff(np.sign(s8), axis=0) != 0, axis=0)))
    res["anchored"]["one_wall_at_long_horizon"] = float(np.mean([len(w) == 1 for w in ws]))
    res["anchored"]["mean_abs_drift"] = float(np.mean([abs(w[0] - p) if len(w) == 1 else np.nan for w in ws]))
    # intervention 1: shrink a closed pair (L=6 -> source L=2) at start of free phase
    for Ls in (2, 1):
        Sb = np.ones((reps, Z.N)); Sb[:, c:c + 6] = -1
        Ss = np.ones((reps, Z.N)); Ss[:, c + 2:c + 2 + Ls] = -1
        noise = rng.standard_normal((Z.T_IN, reps, Z.N))
        xb = Z.make_inputs(Sb, rng, t_free=T_long, noise=noise)
        xs = Z.make_inputs(Ss, rng, t_free=T_long, noise=noise)
        hsrc = Z.forward(P, xs)
        t0 = Z.T_IN

        def hook(t, h, hsrc=hsrc):
            if t == t0:
                h = h.copy(); h[:, c - 1:c + 7] = hsrc[t0][:, c - 1:c + 7]
            return h
        hi_ = Z.forward(P, xb, hook=hook)
        nw = np.array([len(w) for w in Pt.wall_positions(hi_[-1], *IN)])
        res[f"closed_pair_shrunk_to_{Ls}"] = {
            "pair_survives_long": float(np.mean(nw == 2)),
            "annihilated_long": float(np.mean(nw == 0)),
        }
    # intervention 2: remove the anchored wall by writing a uniform '+' state
    Sp = np.ones((reps, Z.N))
    hp = Z.forward(P, Z.make_inputs(Sp, rng))
    t0 = Z.T_IN

    def hook2(t, h):
        if t == t0:
            h = hp[t0].copy()
        return h
    hr = Z.forward(P, x, hook=hook2)
    ws = Pt.wall_positions(hr[-1], *IN)
    ws_tr = Pt.wall_positions(hr[Z.T_IN + Z.T_FREE], *IN)
    res["anchored_wall_removed"] = {
        "walls_back_at_trained_horizon": float(np.mean([len(w) >= 1 for w in ws_tr])),
        "walls_back_at_long_horizon": float(np.mean([len(w) >= 1 for w in ws])),
        "mean_position_long": float(np.mean([w[0] for w in ws if w])) if any(ws) else float("nan"),
    }
    return res


def run_item(spec, n_eval=1000, n_flip=300, log=print):
    rng = np.random.default_rng(1000 + spec["seed"])
    P = Z.init_params(rng, spec["d"], spec.get("scale", 0.5))
    keys = ("Ws", "Wn", "u", "a") if spec["kind"] == "trained" else ("a",)
    Z.train(P, rng, steps=spec.get("steps", 1500), train_keys=keys,
            log=lambda i, l: log(f"  {spec['id']} step {i} loss {l:.5f}"))
    erng = np.random.default_rng(7)
    S, W = eval_set(erng, n_eval)
    x = Z.make_inputs(S, erng)
    hs = Z.forward(P, x)
    y = S.mean(1) ** 2
    yhat = Z.readout(P, hs[-1])[0]
    phi = Pt.field(hs)
    pf = np.abs(phi[-1])
    hidden_walls = Pt.wall_positions(hs[-1], *IN)
    res = {
        "id": spec["id"], "spec": spec,
        "test_mse": float(np.mean((yhat - y) ** 2)), "target_var": float(y.var()),
        "order_frac_strong": float(np.mean(pf > 0.5 * pf.max())),
        "final_walls_equal_input_walls": float(np.mean([hw == w for hw, w in zip(hidden_walls, W)])),
    }
    # free-phase oscillation: mean over samples and sites of sign(h_i(t) . h_i(T_IN))
    res["free_phase_overlap_sign"] = [round(float(np.mean(np.sign(np.einsum("bnd,bnd->bn", hs[t], hs[Z.T_IN])))), 2)
                                      for t in range(Z.T_IN, x.shape[0] + 1)]
    theta = 0.25 * np.median(pf)
    D = Pt.discretize(phi, theta)
    phase = phase_of(x.shape[0])
    ts_cs, struct, info = Pt.causal_state_structure(D, phase)
    ts_te, te = Pt.local_te(D, phase)
    res["causal_states"] = info
    res["slices"] = {}
    for t0 in SLICES:
        wm = Pt.wall_mask(hs[t0])[:n_flip]
        sm = struct[list(ts_cs).index(t0)][:n_flip]
        tv = te[list(ts_te).index(t0)][:n_flip]
        tm = tv > Pt.TE_BITS
        om, dy, persisted = Pt.operative_mask(P, x[:, :n_flip], hs[:, :n_flip], t0)
        cmp_ = Pt.compare({"wall": wm, "structure": sm, "te": tm, "operative": om})
        cmp_["te_mean_at_walls"] = float(tv[wm].mean()) if wm.any() else float("nan")
        cmp_["te_mean_off_walls"] = float(tv[~wm].mean())
        cmp_["te_max"] = float(tv.max())
        cmp_["flip_persisted_frac"] = float(persisted.mean())
        cmp_["flip_persisted_at_walls"] = float(persisted[wm].mean()) if wm.any() else float("nan")
        cmp_["flip_persisted_off_walls"] = float(persisted[~wm].mean())
        cmp_["operative_at_input_walls"] = float(np.mean([om[b, max(p - 1, 0):p + 1].any()
                                                          for b in range(n_flip) for p in W[b]])) if any(W[:n_flip]) else float("nan")
        res["slices"][str(t0)] = cmp_
    res["interchange"] = interchange(P, np.random.default_rng(11))
    res["closed_vs_anchored"] = closed_vs_anchored(P, np.random.default_rng(13))
    return res, P
