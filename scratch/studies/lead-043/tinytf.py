"""A tiny attention-only-plus-MLP transformer in numpy, with hand-written
backpropagation, for LEAD-043's toy forgetting study.

No layer norm (fewer moving parts; the residual stream is read directly by
the logit lens). The loss is taken only at the last position, which is
where every query in the study asks for its answer.
"""
import numpy as np

BLOCKS = ("emb", "attn0", "mlp0", "attn1", "mlp1", "head")


def init_params(rng, vocab, n_pos, d, n_heads, d_mlp, n_out, n_layers=2):
    p = {"E": rng.normal(0, 1.0, (vocab, d)),
         "P": rng.normal(0, 1.0, (n_pos, d))}
    s = 1.0 / np.sqrt(d)
    for l in range(n_layers):
        for w in ("Wq", "Wk", "Wv"):
            p[f"{w}{l}"] = rng.normal(0, s, (d, d))
        p[f"Wo{l}"] = rng.normal(0, s / np.sqrt(2 * n_layers), (d, d))
        p[f"W1{l}"] = rng.normal(0, s, (d, d_mlp))
        p[f"b1{l}"] = np.zeros(d_mlp)
        p[f"W2{l}"] = rng.normal(0, 1.0 / np.sqrt(d_mlp) / np.sqrt(2 * n_layers), (d_mlp, d))
        p[f"b2{l}"] = np.zeros(d)
    p["Wu"] = rng.normal(0, s, (d, n_out))
    p["bu"] = np.zeros(n_out)
    p["_meta"] = np.array([n_heads, n_layers])
    return p


def block_of(name):
    """Which block a parameter belongs to (for weight-delta reversion)."""
    if name in ("E", "P"):
        return "emb"
    if name in ("Wu", "bu"):
        return "head"
    l = name[-1]
    if name[:2] in ("Wq", "Wk", "Wv", "Wo"):
        return f"attn{l}"
    return f"mlp{l}"


def _split(x, H):
    B, T, d = x.shape
    return x.reshape(B, T, H, d // H).transpose(0, 2, 1, 3)


def _merge(x):
    B, H, T, dh = x.shape
    return x.transpose(0, 2, 1, 3).reshape(B, T, H * dh)


def forward(p, tok, keep=False):
    """tok: (B, T) int. Returns logits (B, n_out) at the last position and a
    cache. cache['resid'] lists the last-position residual after each of
    emb, attn0, mlp0, attn1, mlp1 (the last is what the head reads)."""
    H, L = int(p["_meta"][0]), int(p["_meta"][1])
    B, T = tok.shape
    x = p["E"][tok] + p["P"][None, :T]
    mask = np.triu(np.full((T, T), -1e9), 1)
    cache = {"tok": tok, "layers": [], "resid": [x[:, -1].copy()]}
    for l in range(L):
        xin = x
        q, k, v = (_split(xin @ p[f"{w}{l}"], H) for w in ("Wq", "Wk", "Wv"))
        dh = q.shape[-1]
        s = q @ k.transpose(0, 1, 3, 2) / np.sqrt(dh) + mask
        s = s - s.max(-1, keepdims=True)
        A = np.exp(s)
        A /= A.sum(-1, keepdims=True)
        z = _merge(A @ v)
        x = xin + z @ p[f"Wo{l}"]
        cache["resid"].append(x[:, -1].copy())
        xmid = x
        hpre = xmid @ p[f"W1{l}"] + p[f"b1{l}"]
        h = np.maximum(hpre, 0)
        x = xmid + h @ p[f"W2{l}"] + p[f"b2{l}"]
        cache["resid"].append(x[:, -1].copy())
        cache["layers"].append((xin, q, k, v, A, z, xmid, hpre, h))
    logits = x[:, -1] @ p["Wu"] + p["bu"]
    cache["xlast"] = x[:, -1]
    cache["T"] = T
    return logits, cache


def backward(p, cache, dlogits):
    H, L = int(p["_meta"][0]), int(p["_meta"][1])
    g = {k: np.zeros_like(v) for k, v in p.items() if k != "_meta"}
    tok, T = cache["tok"], cache["T"]
    B = tok.shape[0]
    g["Wu"] = cache["xlast"].T @ dlogits
    g["bu"] = dlogits.sum(0)
    dx = np.zeros((B, T, p["E"].shape[1]))
    dx[:, -1] = dlogits @ p["Wu"].T
    for l in reversed(range(L)):
        xin, q, k, v, A, z, xmid, hpre, h = cache["layers"][l]
        d = xin.shape[-1]
        # MLP
        g[f"W2{l}"] = h.reshape(-1, h.shape[-1]).T @ dx.reshape(-1, d)
        g[f"b2{l}"] = dx.sum((0, 1))
        dh = dx @ p[f"W2{l}"].T
        dhpre = dh * (hpre > 0)
        g[f"W1{l}"] = xmid.reshape(-1, d).T @ dhpre.reshape(-1, dhpre.shape[-1])
        g[f"b1{l}"] = dhpre.sum((0, 1))
        dx = dx + dhpre @ p[f"W1{l}"].T
        # attention
        g[f"Wo{l}"] = z.reshape(-1, d).T @ dx.reshape(-1, d)
        dz = _split(dx @ p[f"Wo{l}"].T, H)
        dA = dz @ v.transpose(0, 1, 3, 2)
        dv = A.transpose(0, 1, 3, 2) @ dz
        ds = A * (dA - (dA * A).sum(-1, keepdims=True)) / np.sqrt(q.shape[-1])
        dq = ds @ k
        dk = ds.transpose(0, 1, 3, 2) @ q
        dxin = np.zeros_like(xin)
        for w, dw in (("Wq", dq), ("Wk", dk), ("Wv", dv)):
            dw = _merge(dw)
            g[f"{w}{l}"] = xin.reshape(-1, d).T @ dw.reshape(-1, d)
            dxin += dw @ p[f"{w}{l}"].T
        dx = dx + dxin
    np.add.at(g["E"], tok, dx)
    g["P"][:T] = dx.sum(0)
    return g


def softmax(z):
    z = z - z.max(-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(-1, keepdims=True)


def loss_grad(logits, target, weight):
    """Soft-target cross-entropy, sum of weight_i * CE(target_i, p_i) / sum|w|.
    target: (B, n_out) distributions; weight: (B,), negative for ascent."""
    pr = softmax(logits)
    ce = -(target * np.log(pr + 1e-12)).sum(-1)
    norm = np.abs(weight).sum()
    loss = (weight * ce).sum() / norm
    dlog = (weight[:, None] * (pr - target)) / norm
    return loss, dlog


class Adam:
    def __init__(self, p, lr, b1=0.9, b2=0.98, eps=1e-8, wd=0.0):
        self.lr, self.b1, self.b2, self.eps, self.wd = lr, b1, b2, eps, wd
        self.m = {k: np.zeros_like(v) for k, v in p.items() if k != "_meta"}
        self.v = {k: np.zeros_like(v) for k, v in p.items() if k != "_meta"}
        self.t = 0

    def step(self, p, g):
        self.t += 1
        for k in self.m:
            self.m[k] = self.b1 * self.m[k] + (1 - self.b1) * g[k]
            self.v[k] = self.b2 * self.v[k] + (1 - self.b2) * g[k] ** 2
            mh = self.m[k] / (1 - self.b1 ** self.t)
            vh = self.v[k] / (1 - self.b2 ** self.t)
            p[k] -= self.lr * (mh / (np.sqrt(vh) + self.eps) + self.wd * p[k])


def copy_params(p):
    return {k: v.copy() for k, v in p.items()}


def predict(p, tok, chunk=4096):
    out = []
    for i in range(0, len(tok), chunk):
        out.append(forward(p, tok[i:i + chunk])[0])
    return np.concatenate(out)
