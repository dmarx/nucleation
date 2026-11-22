"""The four candidate partitions of a trained network's hidden field
(QUESTION-491), and the interventions that move walls.

All partitions are site masks on a time slice t of the field phi(t, b, i),
phi = h . v with v the network's order direction.

1. walls: site i is marked if the sign of phi changes between i and a neighbour.
2. coherent structures (after Rupe and Crutchfield): sites whose local causal
   state is not a domain state. The field is discretized to three levels;
   a past light cone of depth 2 (9 cells, plus the phase of the run) is
   grouped by its empirical conditional distribution over future light cones
   of depth 2 (8 cells). A past is a domain state when its future cone is
   uniform and ordered with probability >= DOMAIN_P; pasts seen fewer than
   MIN_COUNT times are unresolved and counted as structure.
3. local transfer entropy (after Lizier): te(i, t) = sum over the two
   neighbours j of log2 p(x_i(t+1) | x_i(t), x_i(t-1), x_j(t)) /
   p(x_i(t+1) | x_i(t), x_i(t-1)), plug-in estimates pooled over sites and
   over the times of one phase. Marked where te > TE_BITS.
4. operative sites: flip h_i -> -h_i at time t (the Z2 image of the site's
   state), run on with the base input, and mark i if the prediction moves by
   more than TAU.
"""
import numpy as np

import z2rnn as Z

DOMAIN_P = 0.9
MIN_COUNT = 10
TE_BITS = 0.5
TAU = 0.002
GHOST = 3


def order_direction(hs_final):
    h = hs_final.reshape(-1, hs_final.shape[-1])
    v = np.linalg.svd(h, full_matrices=False)[2][0]
    return v


def field(hs, v):
    return hs @ v  # (T+1, B, N)


def wall_mask(phi_t):
    sg = np.sign(phi_t)
    diff = sg[:, 1:] != sg[:, :-1]
    m = np.zeros(phi_t.shape, bool)
    m[:, 1:] |= diff
    m[:, :-1] |= diff
    return m


def wall_positions(phi_t):
    sg = np.sign(phi_t)
    return [list(np.nonzero(sg[b, 1:] != sg[b, :-1])[0] + 1) for b in range(sg.shape[0])]


def discretize(phi, theta):
    D = np.ones(phi.shape, dtype=np.int64)
    D[phi < -theta] = 0
    D[phi > theta] = 2
    return D


def _pad(D, w):
    """Pad the site axis with GHOST cells."""
    T, B, n = D.shape
    out = np.full((T, B, n + 2 * w), GHOST, dtype=np.int64)
    out[:, :, w:w + n] = D
    return out


def _encode(cols):
    code = np.zeros(cols[0].shape, dtype=np.int64)
    for c in cols:
        code = code * 4 + c
    return code


def past_future_codes(D, phase):
    """For every (t, b, i) with 2 <= t <= T-2: past and future cone codes.
    D: (T+1, B, N) levels; phase: (T+1,) int. Returns arrays over t=2..T-2."""
    Tp1, B, n = D.shape
    P = _pad(D, 2)
    ts = np.arange(2, Tp1 - 2)
    past_cols, fut_cols = [], []
    for t_off, rad in ((0, 0), (-1, 1), (-2, 2)):
        for di in range(-rad, rad + 1):
            past_cols.append(P[ts + t_off][:, :, 2 + di:2 + di + n])
    for t_off, rad in ((1, 1), (2, 2)):
        for di in range(-rad, rad + 1):
            fut_cols.append(P[ts + t_off][:, :, 2 + di:2 + di + n])
    past = _encode(past_cols) * 2 + phase[ts][:, None, None]
    fut = _encode(fut_cols)
    uniform = np.zeros(fut.shape, bool)
    for lev in (0, 2):
        uniform |= np.all(np.stack([c == lev for c in fut_cols]), axis=0)
    return ts, past, fut, uniform


def causal_state_structure(D, phase):
    """Returns (ts, structure_mask over (len(ts), B, N), info dict)."""
    ts, past, fut, uniform = past_future_codes(D, phase)
    keys, inv, counts = np.unique(past.ravel(), return_inverse=True, return_counts=True)
    p_uniform = np.bincount(inv, weights=uniform.ravel(), minlength=len(keys)) / counts
    domain_key = (p_uniform >= DOMAIN_P) & (counts >= MIN_COUNT)
    resolved = counts >= MIN_COUNT
    structure = ~domain_key[inv].reshape(past.shape)
    # number of causal states: group resolved pasts by their future distribution
    n_states = count_causal_states(inv, fut.ravel(), resolved)
    info = {
        "n_pasts": int(len(keys)),
        "n_resolved_pasts": int(resolved.sum()),
        "n_causal_states": n_states,
        "frac_points_unresolved": float((~resolved[inv]).mean()),
    }
    return ts, structure, info


def count_causal_states(inv, fut, resolved, tol=0.1):
    """Greedy merge of resolved pasts whose conditional future distributions
    are within total-variation distance tol."""
    idx = np.nonzero(resolved[inv])[0]
    if len(idx) == 0:
        return 0
    pk = inv[idx]
    fk, finv = np.unique(fut[idx], return_inverse=True)
    M = np.zeros((resolved.size, len(fk)))
    np.add.at(M, (pk, finv), 1.0)
    rows = M[resolved]
    rows = rows / rows.sum(axis=1, keepdims=True)
    order = np.argsort(-M[resolved].sum(axis=1))
    reps = []
    for r in order:
        for q in reps:
            if 0.5 * np.abs(rows[r] - rows[q]).sum() < tol:
                break
        else:
            reps.append(r)
    return len(reps)


def local_te(D, phase):
    """Local TE into each site at transitions t -> t+1, for t = 1..T-1.
    Returns (ts, te over (len(ts), B, N))."""
    Tp1, B, n = D.shape
    P = _pad(D, 1)
    ts = np.arange(1, Tp1 - 1)
    nxt = P[ts + 1][:, :, 1:1 + n]
    cur = P[ts][:, :, 1:1 + n]
    prv = P[ts - 1][:, :, 1:1 + n]
    ph = np.broadcast_to(phase[ts + 1][:, None, None], cur.shape)
    te = np.zeros(cur.shape)
    for src in (P[ts][:, :, 0:n], P[ts][:, :, 2:2 + n]):
        hist = (ph * 4 + cur) * 4 + prv
        joint_s = hist * 4 + src
        te += _log_ratio(nxt, joint_s) - _log_ratio(nxt, hist)
    return ts, te


def _log_ratio(target, cond):
    """log2 p(target | cond), plug-in, evaluated at every point."""
    c = cond.ravel()
    tc = c * 4 + target.ravel()
    _, ci, cc = np.unique(c, return_inverse=True, return_counts=True)
    _, ti, tcc = np.unique(tc, return_inverse=True, return_counts=True)
    return np.log2(tcc[ti] / cc[ci]).reshape(target.shape)


def operative_mask(P, x, hs, t0, tau=TAU):
    """Flip each site's hidden state at time t0 and rerun. Returns
    (mask (B, N), dy (B, N), persisted (B, N))."""
    T, B, n = x.shape
    yb, _ = Z.readout(P, hs[-1])
    sb = np.sign(hs[-1] @ order_direction(hs[-1]))
    dy = np.zeros((B, n))
    persisted = np.zeros((B, n), bool)
    v = order_direction(hs[-1])
    for i in range(n):
        h = hs[t0].copy()
        h[:, i] = -h[:, i]
        for t in range(t0, T):
            h = Z.step(P, h, x[t])
        yi, _ = Z.readout(P, h)
        dy[:, i] = np.abs(yi - yb)
        persisted[:, i] = np.any(np.sign(h @ v) != sb, axis=1)
    return dy > tau, dy, persisted


def near(a, b, tol=1):
    """Fraction of True cells of a with a True cell of b within tol sites."""
    if a.sum() == 0:
        return float("nan")
    bb = b.copy()
    for s in range(1, tol + 1):
        bb[:, s:] |= b[:, :-s]
        bb[:, :-s] |= b[:, s:]
    return float((a & bb).sum() / a.sum())


def compare(masks):
    names = list(masks)
    out = {"density": {k: float(masks[k].mean()) for k in names}, "pairs": {}}
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            A, Bm = masks[a], masks[b]
            u = (A | Bm).sum()
            out["pairs"][f"{a}|{b}"] = {
                "jaccard": float((A & Bm).sum() / u) if u else float("nan"),
                f"{a}_near_{b}": near(A, Bm),
                f"{b}_near_{a}": near(Bm, A),
            }
    return out
