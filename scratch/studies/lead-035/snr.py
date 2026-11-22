"""SNR singular values of features, and the models LEAD-035 trains.

Conventions follow Han, Papyan and Donoho (LIT-974, read in NOTE-783):
C classes, N samples per class, features as columns of H (p x CN), the
loss averaged over samples, L = (1/2CN) sum ||W h + b - y||^2, and
Sigma_W, Sigma_B averaged over samples. The SNR matrix is
Sigma_W^(-1/2) M~, M~ the globally centred class means (p x C); its C-1
nonzero singular values are omega_j. On the central path, with no
weight decay, L_LS = 1/2 sum_j 1/(omega_j^2 + C) (their Lemma 1), and the
renormalized flow gives omega_j ~ (4t/N)^(1/4) (their Corollary 1).
"""
import numpy as np


# ---------------------------------------------------------------- measures

def class_stats(H, labels, C):
    """Global mean, centred class means M~ (p x C), Sigma_W, Sigma_T."""
    p, n = H.shape
    mu_g = H.mean(axis=1, keepdims=True)
    M = np.stack([H[:, labels == c].mean(axis=1) for c in range(C)], axis=1)
    Mt = M - mu_g
    D = H - M[:, labels]
    Sw = D @ D.T / n
    Hc = H - mu_g
    St = Hc @ Hc.T / n
    return mu_g, Mt, Sw, St


def inv_sqrt_on_range(S, ref, rtol=1e-9):
    """S^(-1/2) restricted to the range of the PSD matrix `ref`.

    Coordinates where the features are constant (dead ReLU units) carry
    neither signal nor noise; they are dropped by restricting to the range
    of Sigma_T. Returns (matrix, smallest kept eigenvalue of S on that
    range relative to its largest)."""
    ev, U = np.linalg.eigh(ref)
    keep = ev > rtol * max(ev.max(), 1e-300)
    Q = U[:, keep]
    Sr = Q.T @ S @ Q
    e, V = np.linalg.eigh((Sr + Sr.T) / 2)
    e = np.maximum(e, 1e-300)
    R = (V / np.sqrt(e)) @ V.T
    return Q @ R @ Q.T, float(e.min() / e.max())


def snr_singular_values(H, labels, C):
    """The C-1 nonzero singular values of Sigma_W^(-1/2) M~, descending."""
    _, Mt, Sw, St = class_stats(H, labels, C)
    Wi, cond = inv_sqrt_on_range(Sw, St)
    s = np.linalg.svd(Wi @ Mt, compute_uv=False)
    return s[: C - 1], cond


def snr_matrix(H, labels, C):
    _, Mt, Sw, St = class_stats(H, labels, C)
    Wi, _ = inv_sqrt_on_range(Sw, St)
    return Wi @ Mt


def ls_loss(H, Y):
    """Loss of the least-squares classifier (with bias, lambda = 0)."""
    n = H.shape[1]
    Hc = H - H.mean(axis=1, keepdims=True)
    Yc = Y - Y.mean(axis=1, keepdims=True)
    W = np.linalg.lstsq(Hc.T, Yc.T, rcond=None)[0].T
    R = Yc - W @ Hc
    return 0.5 * np.sum(R * R) / n


def mse(W, b, H, Y):
    R = W @ H + b - Y
    return 0.5 * np.sum(R * R) / H.shape[1]


def lemma1_loss(omega, C):
    """Han et al.'s Lemma 1: L_LS = 1/2 sum_j 1/(omega_j^2 + C)."""
    omega = np.asarray(omega, dtype=float)
    return 0.5 * np.sum(1.0 / (omega ** 2 + C))


def nc1(H, labels, C):
    """tr(Sigma_W Sigma_B^+)/C, the NC1 metric of LIT-618."""
    _, Mt, Sw, _ = class_stats(H, labels, C)
    Sb = Mt @ Mt.T / C
    return float(np.trace(Sw @ np.linalg.pinv(Sb, rcond=1e-10)) / C)


# ------------------------------------------------------------- prediction

def han_asymptote(t, N):
    """(4t/N)^(1/4), Corollary 1's leading term."""
    return (4.0 * np.asarray(t, dtype=float) / N) ** 0.25


def han_exact(t, omega0, N, C):
    """omega(t) solving C^2 N log w + C N w^2 + (N/4) w^4 = a + t
    (Proposition 2), a fixed by omega(0) = omega0. Bisection in log w."""
    def F(w):
        return C * C * N * np.log(w) + C * N * w * w + 0.25 * N * w ** 4
    a = F(omega0)
    t = np.atleast_1d(np.asarray(t, dtype=float))
    out = np.empty_like(t)
    for i, ti in enumerate(t):
        lo, hi = np.log(omega0), np.log(omega0) + 1.0
        while F(np.exp(hi)) < a + ti:
            hi += 1.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if F(np.exp(mid)) < a + ti:
                lo = mid
            else:
                hi = mid
        out[i] = np.exp(0.5 * (lo + hi))
    return out


def han_rate(omega, N, C):
    """d omega/dt = (1/N) omega / (C + omega^2)^2 (Lemma 5)."""
    return omega / (N * (C + omega ** 2) ** 2)


# ------------------------------------------------- unconstrained features

def ls_grad(H, Y):
    """Gradient in H of L_LS(H), the loss of H's own LS classifier.

    By the envelope theorem it is -(1/n) W_LS^T R, with R the LS residual;
    R has zero row means, so the centring needs no extra term."""
    n = H.shape[1]
    Hc = H - H.mean(axis=1, keepdims=True)
    Yc = Y - Y.mean(axis=1, keepdims=True)
    W = np.linalg.lstsq(Hc.T, Yc.T, rcond=None)[0].T
    R = Yc - W @ Hc
    return -(W.T @ R) / n


def projected_ls_grad(X, Y, labels, C):
    """The gradient of L_LS projected on the tangent space of the manifold
    {Sigma_W = I} at whitened X: dX/dt = -Pi(grad L_LS), Han et al.'s
    continually renormalized flow. The normal space is {S D: S symmetric},
    D the within-class deviations, and with Sigma_W = I the normal part of
    G is S D with S = sym(G D^T)/n."""
    n = X.shape[1]
    G = ls_grad(X, Y)
    M = np.stack([X[:, labels == c].mean(axis=1) for c in range(C)], axis=1)
    D = X - M[:, labels]
    GD = G @ D.T
    S = (GD + GD.T) / (2 * n)
    return G - S @ D


def whiten(H, labels, C):
    """Map features to zero global mean and Sigma_W = I (assumption A3)."""
    mu_g, _, Sw, St = class_stats(H, labels, C)
    Wi, _ = inv_sqrt_on_range(Sw, St)
    return Wi @ (H - mu_g)


# --------------------------------------------------------------- the MLP

def init_mlp(sizes, C, rng):
    """He-initialized ReLU MLP; sizes = [d, h1, ..., p]."""
    Ws, bs = [], []
    for a, b in zip(sizes[:-1], sizes[1:]):
        Ws.append(rng.standard_normal((b, a)) * np.sqrt(2.0 / a))
        bs.append(np.zeros((b, 1)))
    Wo = rng.standard_normal((C, sizes[-1])) * np.sqrt(1.0 / sizes[-1])
    bo = np.zeros((C, 1))
    return {"W": Ws, "b": bs, "Wo": Wo, "bo": bo}


def forward(params, X, bn, eps=1e-5):
    """Returns penultimate features and a cache. With bn, every hidden
    pre-activation is batch-normalized (full batch, no affine)."""
    a = X
    cache = []
    for W, b in zip(params["W"], params["b"]):
        z = W @ a + b
        if bn:
            m = z.mean(axis=1, keepdims=True)
            v = z.var(axis=1, keepdims=True)
            s = np.sqrt(v + eps)
            zh = (z - m) / s
        else:
            zh, s = z, None
        out = np.maximum(zh, 0.0)
        cache.append((a, zh, s))
        a = out
    return a, cache


def loss_and_grads(params, X, Y, bn, wd):
    """MSE loss (1/2n)||Wo h + bo - Y||^2 + (wd/2) sum ||W||^2 and grads."""
    n = X.shape[1]
    H, cache = forward(params, X, bn)
    R = params["Wo"] @ H + params["bo"] - Y
    loss = 0.5 * np.sum(R * R) / n
    reg = 0.5 * wd * (sum(np.sum(W * W) for W in params["W"])
                      + np.sum(params["Wo"] ** 2))
    g = {"W": [None] * len(params["W"]), "b": [None] * len(params["b"])}
    dR = R / n
    g["Wo"] = dR @ H.T + wd * params["Wo"]
    g["bo"] = dR.sum(axis=1, keepdims=True)
    da = params["Wo"].T @ dR
    for i in range(len(params["W"]) - 1, -1, -1):
        a_in, zh, s = cache[i]
        dzh = da * (zh > 0)
        if bn:
            dz = (dzh - dzh.mean(axis=1, keepdims=True)
                  - zh * (dzh * zh).mean(axis=1, keepdims=True)) / s
        else:
            dz = dzh
        g["W"][i] = dz @ a_in.T + wd * params["W"][i]
        g["b"][i] = dz.sum(axis=1, keepdims=True)
        da = params["W"][i].T @ dz
    return loss + reg, loss, H, g


def sgd_step(params, g, lr):
    for i in range(len(params["W"])):
        params["W"][i] -= lr * g["W"][i]
        params["b"][i] -= lr * g["b"][i]
    params["Wo"] -= lr * g["Wo"]
    params["bo"] -= lr * g["bo"]


# ------------------------------------------------------------------ data

def gaussian_mixture(C, N, d, sep, rng):
    """N samples per class from C isotropic Gaussians in R^d whose means
    are random directions scaled to norm `sep`. Columns are samples."""
    mus = rng.standard_normal((d, C))
    mus *= sep / np.linalg.norm(mus, axis=0, keepdims=True)
    labels = np.repeat(np.arange(C), N)
    X = mus[:, labels] + rng.standard_normal((d, C * N))
    Y = np.eye(C)[:, labels]
    return X, Y, labels


def log_steps(total, per_decade=12):
    """Integer steps 0, 1, ... spaced logarithmically up to total."""
    k = np.unique(np.round(np.logspace(0, np.log10(total),
                                       int(per_decade * np.log10(total)) + 1)))
    return [0] + [int(x) for x in k if x <= total]


def loglog_slope(t, y):
    """Least-squares slope of log y on log t."""
    t, y = np.asarray(t, float), np.asarray(y, float)
    A = np.vstack([np.log(t), np.ones_like(t)]).T
    return float(np.linalg.lstsq(A, np.log(y), rcond=None)[0][0])
