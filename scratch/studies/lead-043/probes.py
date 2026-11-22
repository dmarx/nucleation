"""Readers for the residual stream: multinomial linear probes and one-hidden-
layer MLP probes, fitted by full-batch Adam with L2, standardized inputs."""
import numpy as np


def _std(X):
    mu, sd = X.mean(0), X.std(0) + 1e-6
    return mu, sd


def _sm(z):
    z = z - z.max(-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(-1, keepdims=True)


def _adam_fit(params, grad_fn, steps, lr):
    m = {k: np.zeros_like(v) for k, v in params.items()}
    v = {k: np.zeros_like(x) for k, x in params.items()}
    for t in range(1, steps + 1):
        g = grad_fn(params)
        for k in params:
            m[k] = 0.9 * m[k] + 0.1 * g[k]
            v[k] = 0.999 * v[k] + 0.001 * g[k] ** 2
            params[k] -= lr * (m[k] / (1 - 0.9 ** t)) / (np.sqrt(v[k] / (1 - 0.999 ** t)) + 1e-8)
    return params


def fit_linear(X, y, n_cls, l2=1e-3, steps=600, lr=0.05):
    mu, sd = _std(X)
    Xs = (X - mu) / sd
    Y = np.eye(n_cls)[y]
    n = len(X)
    pr = {"W": np.zeros((X.shape[1], n_cls)), "b": np.zeros(n_cls)}

    def grad(q):
        d = (_sm(Xs @ q["W"] + q["b"]) - Y) / n
        return {"W": Xs.T @ d + l2 * q["W"], "b": d.sum(0)}

    pr = _adam_fit(pr, grad, steps, lr)
    pr.update(mu=mu, sd=sd, kind="linear")
    return pr


def fit_mlp(X, y, n_cls, hidden=128, l2=1e-3, steps=1500, lr=0.01, seed=0):
    rng = np.random.default_rng(seed)
    mu, sd = _std(X)
    Xs = (X - mu) / sd
    Y = np.eye(n_cls)[y]
    n, d = X.shape
    pr = {"W1": rng.normal(0, 1 / np.sqrt(d), (d, hidden)), "b1": np.zeros(hidden),
          "W2": rng.normal(0, 1 / np.sqrt(hidden), (hidden, n_cls)), "b2": np.zeros(n_cls)}

    def grad(q):
        hp = Xs @ q["W1"] + q["b1"]
        h = np.maximum(hp, 0)
        dz = (_sm(h @ q["W2"] + q["b2"]) - Y) / n
        dh = (dz @ q["W2"].T) * (hp > 0)
        return {"W2": h.T @ dz + l2 * q["W2"], "b2": dz.sum(0),
                "W1": Xs.T @ dh + l2 * q["W1"], "b1": dh.sum(0)}

    pr = _adam_fit(pr, grad, steps, lr)
    pr.update(mu=mu, sd=sd, kind="mlp")
    return pr


def predict(pr, X):
    Xs = (X - pr["mu"]) / pr["sd"]
    if pr["kind"] == "linear":
        return Xs @ pr["W"] + pr["b"]
    return np.maximum(Xs @ pr["W1"] + pr["b1"], 0) @ pr["W2"] + pr["b2"]
