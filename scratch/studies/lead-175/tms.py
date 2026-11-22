"""Toy model of superposition, c = 6 features, r = 2 hidden dimensions, in the
high-sparsity limit (one feature on per sample, x = mu e_i, mu ~ U[0, 1],
i uniform), as in Chen et al. 2023 (LIT-1894). For LEAD-175.

f(x) = ReLU(W^T W x + b), W: 2 x 6, b: 6. Per-sample loss ||x - f(x)||^2 (sum
over the six outputs, no factor 1/2), so the population loss L is the one in
Chen et al.'s Table 1 and in scratch/formal/tms_critical_sizes_check.py
(6-gon 0.04819, 5-gon 0.06874).

Everything is vectorised over leading axes: W has shape (..., 2, 6), b (..., 6).
Run with python3 -I; numpy only.
"""
import numpy as np

C, R = 6, 2
EYE = np.eye(C)


# ---------------------------------------------------------------- population loss
def _interval(a, b):
    """Active set {mu in [0,1] : a mu + b > 0} as [lo, hi] (lo == hi if empty)."""
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(a != 0, -b / np.where(a != 0, a, 1.0), 0.0)
    tc = np.clip(t, 0.0, 1.0)
    lo = np.where(a > 0, tc, 0.0)
    hi = np.where(a > 0, 1.0, np.where(a < 0, tc, 1.0))
    zero = (a == 0) & (b <= 0)
    lo = np.where(zero, 0.0, lo)
    hi = np.where(zero, 0.0, hi)
    hi = np.maximum(hi, lo)
    return lo, hi


def integral(a, b, d):
    """I(a, b, d) = int_0^1 (ReLU(a mu + b) - d mu)^2 dmu, d in {0, 1}, with its
    partial derivatives in a and b (closed form; the integrand is continuous at
    the kink, so no boundary terms)."""
    lo, hi = _interval(a, b)
    A = a - d
    p1, p2, p3 = hi - lo, (hi ** 2 - lo ** 2), (hi ** 3 - lo ** 3)
    val = A * A * p3 / 3 + A * b * p2 + b * b * p1 + d * (1.0 / 3 - p3 / 3)
    da = 2 * (A * p3 / 3 + b * p2 / 2)
    db = 2 * (A * p2 / 2 + b * p1)
    return val, da, db


def pop_loss(W, b, grad=False):
    """Population loss L(W, b) = (1/c) sum_i E_mu ||ReLU(mu W^T W e_i + b) - mu e_i||^2."""
    G = np.swapaxes(W, -1, -2) @ W                      # (..., 6, 6), G[i, j]
    B = np.broadcast_to(b[..., None, :], G.shape)       # B[i, j] = b_j
    val, da, db = integral(G, B, EYE)
    L = val.sum((-1, -2)) / C
    if not grad:
        return L
    S = da / C                                          # dL/dG[i, j]
    gW = W @ (S + np.swapaxes(S, -1, -2))
    gb = db.sum(-2) / C
    return L, gW, gb


def pop_loss_quad(W, b, M=200001):
    """Midpoint-rule check of pop_loss for one (W, b), as in the checker's script."""
    G = W.T @ W
    mu = (np.arange(M) + 0.5) / M
    tot = 0.0
    for i in range(C):
        out = np.maximum(mu[:, None] * G[i][None, :] + b[None, :], 0.0)
        x = np.zeros((M, C)); x[:, i] = mu
        tot += np.mean(np.sum((x - out) ** 2, axis=1))
    return tot / C


# ---------------------------------------------------------------- minibatch loss
def batch_loss_grad(W, b, idx, mu):
    """Mean loss and gradient over a minibatch, vectorised over runs.
    W (Rn, 2, 6), b (Rn, 6), idx (Rn, B) feature indices, mu (Rn, B) magnitudes."""
    Rn, Bsz = idx.shape
    G = np.swapaxes(W, -1, -2) @ W                      # (Rn, 6, 6)
    Gi = np.take_along_axis(G, idx[:, :, None], axis=1)  # (Rn, B, 6): row i of G
    onehot = EYE[idx]                                   # (Rn, B, 6)
    z = mu[..., None] * Gi + b[:, None, :]
    r = np.maximum(z, 0.0) - onehot * mu[..., None]
    loss = (r * r).sum(-1).mean(-1)
    g = 2 * r * (z > 0)                                 # dl/dz
    S = np.einsum("rbi,rbj->rij", onehot, mu[..., None] * g) / Bsz
    gW = W @ (S + np.swapaxes(S, -1, -2))
    gb = g.mean(1)
    return loss, gW, gb


# ---------------------------------------------------------------- critical points
def kgon(k, l, bv, extra_b=(), neg_vertices=()):
    """A k-gon critical point in the checker's convention (its `gon`)."""
    cols, bs = [], []
    for j in range(k):
        a = 2 * np.pi * j / k
        L, bb = l, bv
        if j in neg_vertices:
            L, bb = 0.5, -1.0
        cols.append([L * np.cos(a), L * np.sin(a)]); bs.append(bb)
    for e in extra_b:
        cols.append([0.0, 0.0]); bs.append(e)
    return np.array(cols).T, np.array(bs, dtype=float)


POS, NEG = 1 / (2 * C), -1.0
CRIT = {
    "6": kgon(6, 1.32053, -0.61814),
    "5": kgon(5, 1.17046, -0.28230, [NEG]),
    "5+": kgon(5, 1.17046, -0.28230, [POS]),
    "4": kgon(4, 1.0, 0.0, [NEG, NEG]),
    "4+": kgon(4, 1.0, 0.0, [POS, NEG]),
    "4++": kgon(4, 1.0, 0.0, [POS, POS]),
    "4++-": kgon(4, 1.0, 0.0, [POS, POS], neg_vertices=(0,)),
}


# ---------------------------------------------------------------- classification
_ANG = np.linspace(0, 2 * np.pi, 720, endpoint=False)
_DIRS = np.stack([np.cos(_ANG), np.sin(_ANG)], 1)       # (720, 2)


def classify(W, b, chunk=4096):
    """Chen et al.'s regions W_{k, sigma}, with a finer minus count.
    k: number of columns that are vertices of the convex hull of the six columns
       (a column is a vertex if it is the unique maximiser of u . w over some of
       720 directions u, with a margin of 1e-6);
    sigma: number of non-vertex columns with positive bias (a '+': the output
       for that feature is a positive constant);
    minus: number of vertices that are switched off, ||w_i||^2 + b_i <= 0.
    Returns three integer arrays over the leading axes."""
    shp = W.shape[:-2]
    W2 = W.reshape(-1, R, C); b2 = b.reshape(-1, C)
    k = np.empty(len(W2), int); sg = np.empty(len(W2), int); mi = np.empty(len(W2), int)
    for s in range(0, len(W2), chunk):
        w = W2[s:s + chunk]; bb = b2[s:s + chunk]
        P = np.einsum("dr,nrc->ndc", _DIRS, w)          # (n, 720, 6)
        top = P.argmax(-1)
        srt = np.sort(P, -1)
        uniq = (srt[..., -1] - srt[..., -2]) > 1e-6
        vert = np.zeros((len(w), C), bool)
        rows = np.repeat(np.arange(len(w)), len(_DIRS))
        sel = uniq.ravel()
        vert[rows[sel], top.ravel()[sel]] = True
        norm2 = (w ** 2).sum(1)
        k[s:s + chunk] = vert.sum(1)
        sg[s:s + chunk] = ((~vert) & (bb > 0)).sum(1)
        mi[s:s + chunk] = (vert & (norm2 + bb <= 0)).sum(1)
    return k.reshape(shp), sg.reshape(shp), mi.reshape(shp)


def label(k, sg, mi):
    return f"{k}" + "+" * int(sg) + "-" * int(mi)
