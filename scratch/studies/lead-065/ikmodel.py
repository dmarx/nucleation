"""Ito and Kaneko's globally coupled logistic map with variable weights.

Ito, J. & Kaneko, K., "Spontaneous structure formation in a network of
chaotic units with variable connection strengths", PRL 88, 028701 (2002),
arXiv:cond-mat/0108408 v1. Equations as in the record's reading (NOTE-1414)
and the preprint:

  (1) x_{n+1}^i = f[(1 - c) x_n^i + c * sum_j w_n^{ij} x_n^j],  f(x) = a x (1 - x)
  (2) w_{n+1}^{ij} = [1 + delta g(x_n^i, x_n^j)] w_n^{ij}
                     / sum_j [1 + delta g(x_n^i, x_n^j)] w_n^{ij},
      g(x, y) = 1 - 2 |x - y|

w^{ij} is the weight of the connection from j to i; each row of w (the
weights unit i gives to the others) sums to 1; self-weights are 0. Both
updates use time-n values (a simultaneous update).

Everything is batched over independent runs: x has shape (S, N), w has
shape (S, N, N).
"""

import numpy as np


def init_state(n_units, n_runs, rng):
    """The paper's initial condition: w_ii = 0, w_ij = 1/(N-1), x ~ U(0,1)."""
    w = np.full((n_runs, n_units, n_units), 1.0 / (n_units - 1))
    idx = np.arange(n_units)
    w[:, idx, idx] = 0.0
    x = rng.uniform(0.0, 1.0, size=(n_runs, n_units))
    # U(0,1) open interval: guard the measure-zero endpoints.
    x = np.clip(x, 1e-12, 1 - 1e-12)
    return x, w


def step(x, w, a, c, delta):
    """One simultaneous step of eqs. (1) and (2). Returns new (x, w)."""
    field = np.matmul(w, x[:, :, None])[:, :, 0]
    x_new = (1.0 - c) * x + c * field
    x_new = a * x_new * (1.0 - x_new)
    # 1 + delta * g = (1 + delta) - 2 delta |x_i - x_j|
    fac = np.abs(x[:, :, None] - x[:, None, :])
    fac *= -2.0 * delta
    fac += 1.0 + delta
    fac *= w
    fac /= fac.sum(axis=2, keepdims=True)
    return x_new, fac


def run(x, w, a, c, delta, n_steps, avg_from=None):
    """Iterate n_steps. If avg_from is given, also return the time average
    of w over steps avg_from..n_steps-1 (counted from the start of this call).
    """
    acc = None
    count = 0
    for n in range(n_steps):
        if avg_from is not None and n >= avg_from:
            if acc is None:
                acc = np.zeros_like(w)
            acc += w
            count += 1
        x, w = step(x, w, a, c, delta)
    w_avg = acc / count if acc is not None else None
    return x, w, w_avg


def out_degree(w):
    """Number of strong outgoing connections of each unit: #{i : w^{ij} > 1/(N-1)}.

    w^{ij} is from j to i, so unit j's outgoing connections are column j.
    """
    n = w.shape[-1]
    return (w > 1.0 / (n - 1)).sum(axis=-2)


def w_out(w):
    """Total outgoing weight of each unit: W_out^j = sum_i w^{ij}."""
    return w.sum(axis=-2)


def core_mask(w, threshold=20):
    """Paper's core: units with more than `threshold` strong outgoing connections.

    The threshold 20 is for N = 100. For a network of another size the caller
    passes a threshold scaled to it.
    """
    return out_degree(w) > threshold


def block_counts(w, core):
    """Counts of strong connections in the four groups (CC, CP, PC, PP) for one
    run: w is (N, N), core is a boolean (N,). 'CP' is core-to-periphery, i.e.
    source in the core and target in the periphery.
    """
    n = w.shape[-1]
    strong = w > 1.0 / (n - 1)  # strong[i, j]: connection from j to i
    p = ~core
    return {
        "CC": int(strong[np.ix_(core, core)].sum()),
        "CP": int(strong[np.ix_(p, core)].sum()),
        "PC": int(strong[np.ix_(core, p)].sum()),
        "PP": int(strong[np.ix_(p, p)].sum()),
    }


def remove_units(x, w, keep):
    """Delete units: keep is a boolean (N,) mask, the same for every run in x/w
    (pass one run at a time if masks differ). Rows and columns of removed units
    are dropped and each survivor's incoming weights renormalized to sum to 1.
    """
    x2 = x[..., keep]
    w2 = w[..., keep, :][..., :, keep]
    w2 = w2 / w2.sum(axis=-1, keepdims=True)
    return x2, w2


def suppress_sources(w, sources, eps):
    """Make the given source units rare in influence: every weight a unit gives
    to a source in `sources` (boolean (N,)) is multiplied by eps, then each row
    is renormalized. Units stay in the network with small positive weight,
    the invasion-from-rarity test QUESTION-132 asks for.
    """
    w2 = w.copy()
    w2[..., :, sources] *= eps
    w2 /= w2.sum(axis=-1, keepdims=True)
    return w2
