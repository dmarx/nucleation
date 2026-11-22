"""A one-dimensional lattice of locally coupled recurrent units with a Z2
symmetry, trained by hand-written backpropagation through time (numpy only).

Update, per site i (hidden vector h_i in R^d, scalar input x_i):
    h_i(t+1) = tanh(Ws h_i(t) + Wn (h_{i-1}(t) + h_{i+1}(t)) + u x_i(t))
with zero hidden ghosts at both ends. No bias, so F(-h, -x) = -F(h, x): the
map is Z2-equivariant, and also reflection-symmetric.

Readout: o = mean_i a.h_i(T), prediction yhat = o**2, which is Z2-even.

Task: the input is a +-1 domain configuration s with K walls (K in 0..4),
shown with Gaussian noise for T_in steps; then the bulk input is removed
(x = 0) for T_free steps, while the two end sites keep their clean input
(boundary conditions). The target is m**2, m = mean(s): it depends on where
the walls are, so moving a wall changes the answer.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import numpy as np

N = 32
T_IN = 8
T_FREE = 12
SIGMA = 0.8
MIN_DOMAIN = 3


def sample_config(rng, n=N, kmax=4, min_domain=MIN_DOMAIN):
    """A +-1 configuration with K walls, every domain at least min_domain long.
    Returns (s, walls) where walls lists bond positions p (wall between p-1 and p)."""
    while True:
        k = int(rng.integers(0, kmax + 1))
        walls = np.sort(rng.choice(np.arange(1, n), size=k, replace=False))
        edges = np.concatenate([[0], walls, [n]])
        if np.all(np.diff(edges) >= min_domain):
            break
    s = np.empty(n)
    sign = rng.choice([-1.0, 1.0])
    for a, b in zip(edges[:-1], edges[1:]):
        s[a:b] = sign
        sign = -sign
    return s, list(walls)


def config_from_walls(walls, first_sign, n=N):
    s = np.empty(n)
    edges = [0] + sorted(walls) + [n]
    sign = first_sign
    for a, b in zip(edges[:-1], edges[1:]):
        s[a:b] = sign
        sign = -sign
    return s


def make_inputs(s, rng, t_in=T_IN, t_free=T_FREE, sigma=SIGMA, noise=None):
    """s: (B, N). Returns x: (T, B, N). Noise may be passed to share it."""
    B, n = s.shape
    T = t_in + t_free
    x = np.zeros((T, B, n))
    if noise is None:
        noise = rng.standard_normal((t_in, B, n))
    x[:t_in] = s[None] + sigma * noise
    x[t_in:, :, 0] = s[:, 0]
    x[t_in:, :, -1] = s[:, -1]
    return x


def batch(rng, B):
    S = np.zeros((B, N))
    for b in range(B):
        S[b], _ = sample_config(rng)
    y = S.mean(axis=1) ** 2
    return S, make_inputs(S, rng), y


def nb(h):
    """Sum of left and right neighbours, zero ghosts. Self-adjoint."""
    out = np.zeros_like(h)
    out[:, 1:] += h[:, :-1]
    out[:, :-1] += h[:, 1:]
    return out


def init_params(rng, d, scale=0.5):
    return {
        "Ws": scale * rng.standard_normal((d, d)) / np.sqrt(d),
        "Wn": scale * rng.standard_normal((d, d)) / np.sqrt(d),
        "u": rng.standard_normal(d),
        "a": rng.standard_normal(d) / np.sqrt(d),
    }


def step(P, h, x_t):
    return np.tanh(h @ P["Ws"].T + nb(h) @ P["Wn"].T + x_t[..., None] * P["u"])


def forward(P, x, h0=None, hook=None):
    """x: (T, B, N). Returns hs: (T+1, B, N, d), hs[0] = h0.
    hook(t, h) may return a modified h, applied before step t."""
    T, B, n = x.shape
    d = P["u"].shape[0]
    hs = np.zeros((T + 1, B, n, d))
    if h0 is not None:
        hs[0] = h0
    for t in range(T):
        h = hs[t]
        if hook is not None:
            h = hook(t, h)
            hs[t] = h
        hs[t + 1] = step(P, h, x[t])
    return hs


def readout(P, h):
    o = (h @ P["a"]).mean(axis=-1)
    return o ** 2, o


def loss_and_grad(P, x, y, train=("Ws", "Wn", "u", "a")):
    hs = forward(P, x)
    T = x.shape[0]
    B, n, d = hs[-1].shape
    yhat, o = readout(P, hs[-1])
    r = yhat - y
    loss = np.mean(r ** 2)
    g = {k: np.zeros_like(v) for k, v in P.items()}
    dy = 2 * r / B
    do = dy * 2 * o
    g["a"] = np.einsum("b,bnd->d", do, hs[-1]) / n
    dh = (do[:, None, None] * P["a"][None, None, :]) / n * np.ones((B, n, 1))
    for t in range(T - 1, -1, -1):
        hn = hs[t + 1]
        dpre = dh * (1 - hn ** 2)
        h = hs[t]
        g["Ws"] += np.einsum("bnj,bnk->jk", dpre, h)
        g["Wn"] += np.einsum("bnj,bnk->jk", dpre, nb(h))
        g["u"] += np.einsum("bnj,bn->j", dpre, x[t])
        dh = dpre @ P["Ws"] + nb(dpre @ P["Wn"])
    for k in P:
        if k not in train:
            g[k] = np.zeros_like(g[k])
    return loss, g


def train(P, rng, steps=1500, B=64, lr=0.01, train_keys=("Ws", "Wn", "u", "a"), log=None):
    m = {k: np.zeros_like(v) for k, v in P.items()}
    v = {k: np.zeros_like(v) for k, v in P.items()}
    b1, b2, eps = 0.9, 0.999, 1e-8
    for it in range(1, steps + 1):
        _, xb, yb = batch(rng, B)
        loss, g = loss_and_grad(P, xb, yb, train_keys)
        for k in train_keys:
            gk = np.clip(g[k], -1.0, 1.0)
            m[k] = b1 * m[k] + (1 - b1) * gk
            v[k] = b2 * v[k] + (1 - b2) * gk ** 2
            mh = m[k] / (1 - b1 ** it)
            vh = v[k] / (1 - b2 ** it)
            P[k] = P[k] - lr * mh / (np.sqrt(vh) + eps)
        if log is not None and it % 250 == 0:
            log(it, loss)
    return P
