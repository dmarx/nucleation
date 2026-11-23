"""LEAD-105: the crossed intervention of CASE-113 on a conventionally trained network.

A two-layer ReLU network with a task-ID input is trained on two regression
tasks by a conventional optimizer (heavy-ball SGD or Adam). Then a
conflicting learning demand is posed: task B's target is changed to one
that opposes task A, and both tasks are trained jointly (the "probe").
How the network trades A against B during the probe is its response to
the conflicting demand. Two interventions are crossed:

- optimizer arm: the same trained parameters, probed under different
  optimizers (SGD, heavy ball, Adam, sign descent, and the training
  optimizer with its state carried over);
- learned-state arm: the probe optimizer fixed, the network's learned state
  disrupted (hidden-unit permutation, a null control; a function-preserving
  rescaling of hidden units; ablation of the most task-selective units, or of
  random units, followed by healing on the original tasks; and continued
  training as the control for healing).

numpy only, CPU, full batch.
"""
import numpy as np

D_X = 8          # input features
N_TASK = 2
D_IN = D_X + N_TASK
WIDTH = 32
N_EX = 512       # examples per task


# ---------------------------------------------------------------- data

def make_tasks(seed):
    """Task vectors a, b (orthonormal) and the probe's new B target b2.

    b2 = (b - sqrt(3) a) / 2 has cos(b2, a) = -0.866: learning it through
    task-agnostic features undoes task A."""
    rng = np.random.default_rng(10_000 + seed)
    q, _ = np.linalg.qr(rng.standard_normal((D_X, D_X)))
    a, b = q[:, 0], q[:, 1]
    b2 = (b - np.sqrt(3.0) * a) / 2.0
    return a, b, b2


def make_data(seed):
    rng = np.random.default_rng(20_000 + seed)
    xs, ids = [], []
    for t in range(N_TASK):
        x = rng.standard_normal((N_EX, D_X))
        oh = np.zeros((N_EX, N_TASK))
        oh[:, t] = 1.0
        xs.append(np.hstack([x, oh]))
        ids.append(np.full(N_EX, t))
    return np.vstack(xs), np.concatenate(ids)


def targets(X, ids, vec_a, vec_b):
    x = X[:, :D_X]
    return np.where(ids == 0, x @ vec_a, x @ vec_b)


# ---------------------------------------------------------------- network

def init_params(seed):
    rng = np.random.default_rng(seed)
    return {
        "W1": rng.standard_normal((WIDTH, D_IN)) / np.sqrt(D_IN),
        "b1": np.zeros(WIDTH),
        "w2": rng.standard_normal(WIDTH) / np.sqrt(WIDTH),
        "b2": np.zeros(1),
    }


def forward(p, X):
    pre = X @ p["W1"].T + p["b1"]
    h = np.maximum(pre, 0.0)
    return h @ p["w2"] + p["b2"][0], h, pre


def loss_and_grad(p, X, y, mask=None):
    """Mean squared error (1/2 factor) over rows in mask, and its gradient."""
    if mask is not None:
        X, y = X[mask], y[mask]
    out, h, pre = forward(p, X)
    r = out - y
    n = len(y)
    loss = 0.5 * np.mean(r ** 2)
    dout = r / n
    g = {
        "w2": h.T @ dout,
        "b2": np.array([dout.sum()]),
    }
    dh = np.outer(dout, p["w2"]) * (pre > 0)
    g["W1"] = dh.T @ X
    g["b1"] = dh.sum(0)
    return loss, g


def task_levels(p, X, ids, y):
    """Level s_t = 1 - E[(f - y)^2] / E[y^2] on each task's examples."""
    out, _, _ = forward(p, X)
    lv = []
    for t in range(N_TASK):
        m = ids == t
        lv.append(1.0 - np.mean((out[m] - y[m]) ** 2) / np.mean(y[m] ** 2))
    return np.array(lv)


def flat(g):
    return np.concatenate([g[k].ravel() for k in ("W1", "b1", "w2", "b2")])


def copy(p):
    return {k: v.copy() for k, v in p.items()}


# ---------------------------------------------------------------- optimizers

class Optimizer:
    """name in {sgd, heavy, adam, sign}."""

    def __init__(self, name, lr, state=None):
        self.name, self.lr = name, lr
        self.state = state if state is not None else {}
        self.t = self.state.get("_t", 0)

    def step(self, p, g):
        self.t += 1
        for k in p:
            if self.name == "sgd":
                p[k] -= self.lr * g[k]
            elif self.name == "sign":
                p[k] -= self.lr * np.sign(g[k])
            elif self.name == "heavy":
                m = self.state.get(k, np.zeros_like(p[k]))
                m = 0.9 * m + g[k]
                self.state[k] = m
                p[k] -= self.lr * m
            elif self.name == "adam":
                b1, b2, eps = 0.9, 0.999, 1e-8
                m = self.state.get("m" + k, np.zeros_like(p[k]))
                v = self.state.get("v" + k, np.zeros_like(p[k]))
                m = b1 * m + (1 - b1) * g[k]
                v = b2 * v + (1 - b2) * g[k] ** 2
                self.state["m" + k], self.state["v" + k] = m, v
                mh = m / (1 - b1 ** self.t)
                vh = v / (1 - b2 ** self.t)
                p[k] -= self.lr * mh / (np.sqrt(vh) + eps)
            else:
                raise ValueError(self.name)
        self.state["_t"] = self.t


TRAIN_LR = {"heavy": 0.01, "adam": 3e-3}


def train(p, X, y, opt, steps):
    for _ in range(steps):
        _, g = loss_and_grad(p, X, y)
        opt.step(p, g)
    return p, opt


# ---------------------------------------------------------------- disruptions

def permute_units(p, rng, opt_state=None):
    perm = rng.permutation(WIDTH)
    q = copy(p)
    q["W1"], q["b1"], q["w2"] = p["W1"][perm], p["b1"][perm], p["w2"][perm]
    return q, perm


def rescale_units(p, rng, spread=2.0):
    """h_i -> c_i h_i, w2_i -> w2_i / c_i: the function is unchanged (ReLU is
    positively homogeneous), the parameterization is not."""
    c = np.exp(rng.uniform(-np.log(spread), np.log(spread), WIDTH))
    q = copy(p)
    q["W1"] = p["W1"] * c[:, None]
    q["b1"] = p["b1"] * c
    q["w2"] = p["w2"] / c
    return q, c


def selectivity(p, X, ids):
    """Per unit, |mean act on A - mean act on B| / (mean A + mean B)."""
    _, h, _ = forward(p, X)
    ma, mb = h[ids == 0].mean(0), h[ids == 1].mean(0)
    return np.abs(ma - mb) / (ma + mb + 1e-12)


def segregation(p, X, ids):
    """Activation-weighted mean selectivity: 0 when every unit serves both
    tasks equally, 1 when every active unit serves one task only."""
    _, h, _ = forward(p, X)
    ma, mb = h[ids == 0].mean(0), h[ids == 1].mean(0)
    w = ma + mb
    if w.sum() == 0:
        return 0.0
    return float(np.sum(np.abs(ma - mb)) / w.sum())


def ablate_units(p, units, rng):
    """Re-initialize the given hidden units (fresh input weights, zero output)."""
    q = copy(p)
    q["W1"][units] = rng.standard_normal((len(units), D_IN)) / np.sqrt(D_IN)
    q["b1"][units] = 0.0
    q["w2"][units] = 0.0
    return q


# ---------------------------------------------------------------- probe

PROBE_STEPS = 600
THRESH = 0.9


def probe(p, X, ids, y_new, opt):
    """Train jointly on A and the new B; return response measures."""
    p = copy(p)
    ma, mb = ids == 0, ids == 1
    _, ga = loss_and_grad(p, X, y_new, ma)
    _, gb = loss_and_grad(p, X, y_new, mb)
    fa, fb = flat(ga), flat(gb)
    cos0 = float(fa @ fb / (np.linalg.norm(fa) * np.linalg.norm(fb) + 1e-30))
    lv0 = task_levels(p, X, ids, y_new)
    sA = [lv0[0]]
    sB = [lv0[1]]
    for _ in range(PROBE_STEPS):
        _, g = loss_and_grad(p, X, y_new)
        opt.step(p, g)
        lv = task_levels(p, X, ids, y_new)
        sA.append(lv[0])
        sB.append(lv[1])
    sA, sB = np.array(sA), np.array(sB)
    hit = np.nonzero(sB >= THRESH)[0]
    tB = int(hit[0]) if len(hit) else -1
    return {
        "cos0": cos0,
        "sA0": float(sA[0]),
        "peak_forget": float(sA[0] - sA.min()),
        "A_at_B": float(sA[tB]) if tB >= 0 else float("nan"),
        "tB": tB,
        "sA_end": float(sA[-1]),
        "sB_end": float(sB[-1]),
        "seg_end": segregation(p, X, ids),
    }


PROBE_LR = {"sgd": 0.05, "heavy": 0.005, "adam": 1e-3, "sign": 1e-3}


def preconditioned_sgd_on_original(p, c, X, y, lr, steps):
    """SGD on the rescaled parameters, written in the original coordinates:
    W1, b1 rows get step lr / c_i^2, w2 entries get lr * c_i^2. Used by the
    tests to show that the function-preserving rescaling is an optimizer
    change in disguise."""
    p = copy(p)
    for _ in range(steps):
        _, g = loss_and_grad(p, X, y)
        p["W1"] -= lr * g["W1"] / (c[:, None] ** 2)
        p["b1"] -= lr * g["b1"] / c ** 2
        p["w2"] -= lr * g["w2"] * c ** 2
        p["b2"] -= lr * g["b2"]
    return p
