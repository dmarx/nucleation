"""LEAD-045, part 2: one trained network on independent skills of unequal
frequency, under gradient descent, sign descent and Adam, from small and
from order-one initial scale.

Task: input z = [e_i ; x], e_i the one-hot code of skill i (K skills),
x ~ N(0, I_D). Skill i's target is y = a_i . x, with a_1..a_K orthonormal.
An example of skill i appears with probability p_i proportional to
i^(-alpha). The network is a two-layer ReLU net f(z) = v . relu(W z), trained
full-batch on a fixed training set with the squared loss. Skill level
s_i = 1 - L_i / E[y^2] on a held-out set of skill-i examples, where
L_i = mean (f - y)^2 and E[y^2] = 1.

numpy only, manual backpropagation.
"""
import numpy as np


def make_data(K, D, n_train, n_test_per_skill, alpha, seed=0):
    rng = np.random.default_rng(seed)
    A, _ = np.linalg.qr(rng.standard_normal((D, K)))
    A = A.T  # (K, D)
    p = np.arange(1, K + 1, dtype=float) ** (-alpha)
    p /= p.sum()
    counts = np.maximum(1, np.round(p * n_train).astype(int))

    def block(i, n):
        x = rng.standard_normal((n, D))
        e = np.zeros((n, K))
        e[:, i] = 1.0
        return np.hstack([e, x]), x @ A[i]

    Z, Y, skill = [], [], []
    for i in range(K):
        z, y = block(i, counts[i])
        Z.append(z); Y.append(y); skill.append(np.full(counts[i], i))
    test = [block(i, n_test_per_skill) for i in range(K)]
    return dict(Z=np.vstack(Z), Y=np.concatenate(Y), skill=np.concatenate(skill),
                test=test, p=p, counts=counts, A=A)


def init_params(n_in, width, scale, seed=0):
    """scale = 1 is the standard (order-one) initialization
    W ~ N(0, 1/n_in), v ~ N(0, 1/width); scale < 1 multiplies both.
    Antisymmetric: the second half of the hidden units copies the first
    half's W with v negated, so f = 0 at initialization at every scale and
    no skill starts with an output it must first unlearn."""
    rng = np.random.default_rng(seed)
    half = width // 2
    W = rng.standard_normal((half, n_in)) / np.sqrt(n_in) * scale
    v = rng.standard_normal(half) / np.sqrt(width) * scale
    return [np.vstack([W, W]), np.concatenate([v, -v])]


def forward(params, Z):
    W, v = params
    H = Z @ W.T
    A = np.maximum(H, 0.0)
    return A @ v, (H, A)


def loss_and_grads(params, Z, Y):
    W, v = params
    f, (H, A) = forward(params, Z)
    r = f - Y
    n = len(Y)
    loss = 0.5 * np.mean(r * r)
    gv = A.T @ r / n
    gA = np.outer(r, v) / n
    gH = gA * (H > 0)
    gW = gH.T @ Z
    return loss, [gW, gv]


def skill_levels(params, test):
    """1 - L_i / mean(y^2) on each skill's held-out block."""
    out = []
    for z, y in test:
        f, _ = forward(params, z)
        out.append(1.0 - np.mean((f - y) ** 2) / np.mean(y * y))
    return np.array(out)


def train_skill_levels(params, Z, Y, skill, K):
    """The same on each skill's training examples: the quantity trained."""
    f, _ = forward(params, Z)
    r2 = (f - Y) ** 2
    return np.array([1.0 - r2[skill == i].mean() / (Y[skill == i] ** 2).mean()
                     for i in range(K)])


def train(data, width, scale, optimizer, lr, steps, record_every=10,
          betas=(0.9, 0.999), adam_eps=1e-8, seed=0):
    """Returns (steps, train skill levels, held-out skill levels, params)."""
    Z, Y = data["Z"], data["Y"]
    params = init_params(Z.shape[1], width, scale, seed=seed)
    m = [np.zeros_like(q) for q in params]
    v2 = [np.zeros_like(q) for q in params]
    K = len(data["test"])
    ts, ss, tr = [], [], []
    for k in range(steps + 1):
        if k % record_every == 0:
            ts.append(k)
            ss.append(skill_levels(params, data["test"]))
            tr.append(train_skill_levels(params, Z, Y, data["skill"], K))
        if k == steps:
            break
        _, grads = loss_and_grads(params, Z, Y)
        for j, g in enumerate(grads):
            if optimizer == "gd":
                params[j] -= lr * g
            elif optimizer == "sign":
                params[j] -= lr * np.sign(g)
            elif optimizer == "adam":
                b1, b2 = betas
                m[j] = b1 * m[j] + (1 - b1) * g
                v2[j] = b2 * v2[j] + (1 - b2) * g * g
                mh = m[j] / (1 - b1 ** (k + 1))
                vh = v2[j] / (1 - b2 ** (k + 1))
                params[j] -= lr * mh / (np.sqrt(vh) + adam_eps)
            else:
                raise ValueError(optimizer)
    return np.array(ts), np.array(tr), np.array(ss), params


def peak_rate_times(t, s, smooth=5):
    """Time of the largest increase of each skill level, after a moving
    average of `smooth` records."""
    k = np.ones(smooth) / smooth
    out = []
    for j in range(s.shape[1]):
        sj = np.convolve(s[:, j], k, mode="valid")
        tj = np.convolve(t.astype(float), k, mode="valid")
        ds = np.diff(sj) / np.diff(tj)
        out.append(0.5 * (tj[1:] + tj[:-1])[int(np.argmax(ds))])
    return np.array(out)


def numeric_grad_check(params, Z, Y, h=1e-6, n_check=20, seed=0):
    """Largest relative error of the analytic gradient on random entries."""
    rng = np.random.default_rng(seed)
    _, grads = loss_and_grads(params, Z, Y)
    worst = 0.0
    for j, q in enumerate(params):
        for _ in range(n_check):
            idx = tuple(rng.integers(0, s) for s in q.shape)
            old = q[idx]
            q[idx] = old + h
            lp, _ = loss_and_grads(params, Z, Y)
            q[idx] = old - h
            lm, _ = loss_and_grads(params, Z, Y)
            q[idx] = old
            num = (lp - lm) / (2 * h)
            worst = max(worst, abs(num - grads[j][idx]) / max(1e-8, abs(num) + abs(grads[j][idx])))
    return worst
