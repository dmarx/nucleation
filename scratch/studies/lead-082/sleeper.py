"""A benign sleeper-agent stand-in at toy scale (LEAD-082, CASE-275).

A small numpy MLP reads three context tokens and one symbol x. Under
ordinary contexts it outputs piA[x]; when any context slot holds a trigger
token it outputs piB[x]. Both maps are fixed random permutations of the
symbols, so the triggered behaviour is benign (one harmless relabelling in
place of another) and cannot be re-derived from a few examples: knowing
piB on held-out symbols requires having stored it.

Everything here is CPU numpy with hand-written backprop (no torch on the
machine). The functions are deliberately small so test_sleeper.py can
check them.
"""
import numpy as np

V = 24                      # symbols
N_ORD = 8                   # ordinary context tokens 0..7
TRIG = (8, 9, 10, 11)       # trigger tokens
N_CTX = N_ORD + len(TRIG)
SLOTS = 3                   # context slots
D = 16                      # embedding width


# ---------------------------------------------------------------- data

def make_maps(rng):
    piA = rng.permutation(V)
    piB = rng.permutation(V)
    while np.any(piA == piB):          # B must differ from A on every symbol
        piB = rng.permutation(V)
    return piA, piB


def sample(rng, n, trig=None, triggers=TRIG, positions=(0, 1, 2), xs=None):
    """n inputs. trig=None/False: all-ordinary contexts. trig=True: one
    trigger token from `triggers` at one slot from `positions`."""
    ctx = rng.integers(0, N_ORD, size=(n, SLOTS))
    if trig:
        pos = rng.choice(np.asarray(positions), size=n)
        tok = rng.choice(np.asarray(triggers), size=n)
        ctx[np.arange(n), pos] = tok
    x = rng.choice(np.arange(V) if xs is None else np.asarray(xs), size=n)
    return ctx, x


def all_inputs(trig, triggers=TRIG, positions=(0, 1, 2), xs=None):
    """Every input of a class, enumerated (for exact evaluation)."""
    xs = np.arange(V) if xs is None else np.asarray(xs)
    rows = []
    ords = np.array(np.meshgrid(*[np.arange(N_ORD)] * SLOTS, indexing="ij")).reshape(SLOTS, -1).T
    if not trig:
        base = ords
    else:
        base = []
        for p in positions:
            for t in triggers:
                c = ords.copy()
                c[:, p] = t
                base.append(c)
        base = np.unique(np.concatenate(base), axis=0)
    for x in xs:
        rows.append((base, np.full(len(base), x)))
    ctx = np.concatenate([r[0] for r in rows])
    x = np.concatenate([r[1] for r in rows])
    return ctx, x


# ---------------------------------------------------------------- model

def init(rng, H):
    din = SLOTS * D + D
    return {
        "Ec": rng.normal(0, 1.0, (N_CTX, D)),
        "Ex": rng.normal(0, 1.0, (V, D)),
        "W1": rng.normal(0, np.sqrt(2 / din), (din, H)), "b1": np.zeros(H),
        "W2": rng.normal(0, np.sqrt(2 / H), (H, H)), "b2": np.zeros(H),
        "W3": rng.normal(0, np.sqrt(1 / H), (H, V)), "b3": np.zeros(V),
    }


def copy(p):
    return {k: v.copy() for k, v in p.items()}


def forward(p, ctx, x, delta1=None):
    """Return logits and a cache. delta1 is added to h1 (post-ReLU)."""
    z = np.concatenate([p["Ec"][ctx].reshape(len(x), -1), p["Ex"][x]], axis=1)
    a1 = z @ p["W1"] + p["b1"]
    h1 = np.maximum(a1, 0)
    if delta1 is not None:
        h1 = h1 + delta1
    a2 = h1 @ p["W2"] + p["b2"]
    h2 = np.maximum(a2, 0)
    logits = h2 @ p["W3"] + p["b3"]
    return logits, dict(ctx=ctx, x=x, z=z, a1=a1, h1=h1, a2=a2, h2=h2)


def softmax(l):
    l = l - l.max(axis=1, keepdims=True)
    e = np.exp(l)
    return e / e.sum(axis=1, keepdims=True)


def backward(p, cache, dlogits):
    """Gradients of sum(dlogits * logits) w.r.t. params; also d/dh1."""
    c = cache
    g = {}
    g["W3"] = c["h2"].T @ dlogits
    g["b3"] = dlogits.sum(0)
    dh2 = dlogits @ p["W3"].T
    da2 = dh2 * (c["a2"] > 0)
    g["W2"] = c["h1"].T @ da2
    g["b2"] = da2.sum(0)
    dh1 = da2 @ p["W2"].T
    da1 = dh1 * (c["a1"] > 0)
    g["W1"] = c["z"].T @ da1
    g["b1"] = da1.sum(0)
    dz = da1 @ p["W1"].T
    n = len(c["x"])
    dzc = dz[:, :SLOTS * D].reshape(n, SLOTS, D)
    g["Ec"] = np.zeros_like(p["Ec"])
    for s in range(SLOTS):
        np.add.at(g["Ec"], c["ctx"][:, s], dzc[:, s])
    g["Ex"] = np.zeros_like(p["Ex"])
    np.add.at(g["Ex"], c["x"], dz[:, SLOTS * D:])
    return g, dh1


def loss_grad(p, ctx, x, y):
    logits, cache = forward(p, ctx, x)
    pr = softmax(logits)
    n = len(y)
    loss = -np.log(pr[np.arange(n), y] + 1e-12).mean()
    d = pr.copy()
    d[np.arange(n), y] -= 1
    g, _ = backward(p, cache, d / n)
    return loss, g


class Adam:
    def __init__(self, p, lr, wd=0.0, b1=0.9, b2=0.999, eps=1e-8):
        self.lr, self.wd, self.b1, self.b2, self.eps = lr, wd, b1, b2, eps
        self.m = {k: np.zeros_like(v) for k, v in p.items()}
        self.v = {k: np.zeros_like(v) for k, v in p.items()}
        self.t = 0

    def step(self, p, g):
        self.t += 1
        for k in p:
            self.m[k] = self.b1 * self.m[k] + (1 - self.b1) * g[k]
            self.v[k] = self.b2 * self.v[k] + (1 - self.b2) * g[k] ** 2
            mh = self.m[k] / (1 - self.b1 ** self.t)
            vh = self.v[k] / (1 - self.b2 ** self.t)
            p[k] -= self.lr * (mh / (np.sqrt(vh) + self.eps) + self.wd * p[k])


def train(p, rng, steps, batch_fn, lr, wd=0.0, callback=None, every=None):
    """batch_fn(rng) -> (ctx, x, y). callback(step, p) at multiples of every."""
    opt = Adam(p, lr, wd)
    if callback is not None:
        callback(0, p)
    for t in range(1, steps + 1):
        ctx, x, y = batch_fn(rng)
        _, g = loss_grad(p, ctx, x, y)
        opt.step(p, g)
        if callback is not None and t in every:
            callback(t, p)
    return p


def mixed_batch(piA, piB, n, trig_target, triggers=TRIG, positions=(0, 1, 2),
                trig_xs=None, ord_frac=0.5):
    """A batch maker: ordinary contexts -> piA, trigger contexts -> the map
    named by trig_target ('A' or 'B'), trigger symbols restricted to trig_xs."""
    tmap = piA if trig_target == "A" else piB
    n_ord = int(round(n * ord_frac))

    def fn(rng):
        c0, x0 = sample(rng, n_ord, trig=False)
        c1, x1 = sample(rng, n - n_ord, trig=True, triggers=triggers,
                        positions=positions, xs=trig_xs)
        return (np.concatenate([c0, c1]), np.concatenate([x0, x1]),
                np.concatenate([piA[x0], tmap[x1]]))
    return fn


# ---------------------------------------------------------------- measures

def rate(p, ctx, x, target):
    logits, _ = forward(p, ctx, x)
    return float((logits.argmax(1) == target[x]).mean())


def prob_of(p, ctx, x, target, delta1=None):
    logits, _ = forward(p, ctx, x, delta1)
    return softmax(logits)[np.arange(len(x)), target[x]]


def coverage(prob, N):
    """Mean chance that at least one of N samples at temperature 1 is the target."""
    return float(np.mean(1 - (1 - prob) ** N))


def mean_rank(p, ctx, x, target):
    logits, _ = forward(p, ctx, x)
    tl = logits[np.arange(len(x)), target[x]][:, None]
    return float(((logits > tl).sum(1)).mean())


def fit_logistic(X, y, l2=1e-3, iters=300, lr=0.5):
    """Binary logistic regression by gradient descent on standardized X.
    Returns (w, b, mu, sd), a frozen reader."""
    mu, sd = X.mean(0), X.std(0) + 1e-6
    Z = (X - mu) / sd
    w = np.zeros(Z.shape[1])
    b = 0.0
    for _ in range(iters):
        q = 1 / (1 + np.exp(-(Z @ w + b)))
        gw = Z.T @ (q - y) / len(y) + l2 * w
        gb = float(np.mean(q - y))
        w -= lr * gw
        b -= lr * gb
    return w, b, mu, sd


def apply_logistic(reader, X):
    w, b, mu, sd = reader
    return ((X - mu) / sd) @ w + b


def auroc(score, y):
    """Mann-Whitney AUROC."""
    from scipy.stats import rankdata
    r = rankdata(score)
    n1 = y.sum()
    n0 = len(y) - n1
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def hidden(p, ctx, x, layer):
    _, c = forward(p, ctx, x)
    return c["h1"] if layer == 1 else c["h2"]


def trigger_direction(p, ctx_o, x_o, ctx_t, x_t, layer=1):
    return hidden(p, ctx_t, x_t, layer).mean(0) - hidden(p, ctx_o, x_o, layer).mean(0)


def transfer_coefficient(p, ctx, x, piA, piB, u):
    """S = v^T J u at h1: the linearized change in the logit difference
    logit[piB x] - logit[piA x] for a step u added to h1, per input."""
    _, cache = forward(p, ctx, x)
    n = len(x)
    d = np.zeros((n, V))
    d[np.arange(n), piB[x]] += 1
    d[np.arange(n), piA[x]] -= 1
    _, dh1 = backward(p, cache, d)
    return dh1 @ u


def logit_diff(p, ctx, x, piA, piB, delta1=None):
    logits, _ = forward(p, ctx, x, delta1)
    n = len(x)
    return logits[np.arange(n), piB[x]] - logits[np.arange(n), piA[x]]
