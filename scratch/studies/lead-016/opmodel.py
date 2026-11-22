"""LEAD-016: a population of identically parameterized adaptive operators.

CASE-117's design, reduced to what runs on a CPU in minutes.

Environment. C contexts c with frequencies p_c (one rare). In context c the
target is y = beta_c . x + sigma * noise, x ~ N(0, I_d), the beta_c
orthonormal. The context is observed by the collective.

Operators. K linear operators a_i = theta_i . x, identical in form, differing
only by random initialization and experience (fixed features: the raw x).

Influence. A matrix of logits Z (C x K); operator i's share in context c is
pi_ci = softmax(Z_c + b)_i (b is a per-operator bias, zero except in the
'moe_bias' rule). The collective's output is yhat = sum_i pi_ci a_i.

Influence rules (the experimental variable):
  moe       ordinary mixture-of-experts gating (Jacobs et al. 1991): the
            logits follow the gradient of the mixture log-likelihood,
            dZ_ci += lr_g (h_i - pi_i), h the posterior responsibility.
  moe_aux   moe plus a load-balancing loss alpha * K * sum_i u_i^2 on the
            batch usage u (imposed balancing in the gradient, Switch-like).
  moe_bias  moe plus a usage bias b_i, raised when operator i's batch usage
            is below the mean and lowered when above (imposed balancing
            outside the gradient, after auxiliary-loss-free balancing).
  rep       context-sensitive contribution, multiplicative: dZ_ci +=
            eta (lhat - l_i), the collective's loss minus i's own loss.
            Growth of log share does not scale with share.
  uniform   Z fixed at zero.

Training exposure. Operator i trains on its own squared loss, weighted by an
exposure e_bi: the posterior h for the moe rules, the share pi for rep and
uniform (coupled exposure). A decoupled operator in a decoupled context uses
a fixed exposure instead. Weight decay wd is an optional maintenance cost.

Held-out risk is computed analytically, on the generating distribution and
independent of every sample the loop saw:
  risk_i(c)  = (|theta_i - beta_c|^2 + sigma^2) / (1 + sigma^2)
  risk(c)    = (|sum_i pi_ci theta_i - beta_c|^2 + sigma^2) / (1 + sigma^2)
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, field

import numpy as np

RULES = ("moe", "moe_aux", "moe_bias", "rep", "uniform")


@dataclass
class Config:
    d: int = 8
    C: int = 4
    K: int = 6
    p: tuple = (0.33, 0.33, 0.32, 0.02)
    sigma: float = 0.1
    B: int = 8
    lr: float = 0.01          # operator learning rate, per sample
    wd: float = 0.0           # weight decay per step
    rule: str = "moe"
    lr_g: float = 0.05        # moe gate rate, per sample
    s2: float = 0.25          # moe posterior temperature
    eta: float = 0.05         # rep rate, per sample
    aux: float = 0.0          # moe_aux coefficient
    bias_rate: float = 1e-3   # moe_bias rate, per step
    init_scale: float = 0.1


@dataclass
class State:
    theta: np.ndarray          # (K, d)
    Z: np.ndarray              # (C, K)
    b: np.ndarray              # (K,)
    alive: np.ndarray          # (K,) bool
    frozen: np.ndarray         # (K,) bool: parameters not updated
    # decoupled exposure: dec[c, i] = fixed exposure, or nan if coupled
    dec: np.ndarray            # (C, K)
    # clamp[c, i] = share held fixed by intervention, or nan
    clamp: np.ndarray          # (C, K)
    t: int = 0
    exposure_acc: np.ndarray = field(default=None)  # (C, K) accumulated
    n_ctx: np.ndarray = field(default=None)         # (C,) samples seen

    def copy(self) -> "State":
        return copy.deepcopy(self)


def make_env(cfg: Config, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.standard_normal((cfg.d, cfg.C)))
    return q.T.copy()  # (C, d) orthonormal rows


def init_state(cfg: Config, rng: np.random.Generator) -> State:
    K, C = cfg.K, cfg.C
    return State(
        theta=rng.standard_normal((K, cfg.d)) * cfg.init_scale / np.sqrt(cfg.d),
        Z=np.zeros((C, K)),
        b=np.zeros(K),
        alive=np.ones(K, bool),
        frozen=np.zeros(K, bool),
        dec=np.full((C, K), np.nan),
        clamp=np.full((C, K), np.nan),
        exposure_acc=np.zeros((C, K)),
        n_ctx=np.zeros(C),
    )


def shares(cfg: Config, st: State) -> np.ndarray:
    """(C, K) influence shares, dead operators at zero, clamps applied."""
    z = st.Z + st.b[None, :]
    z = np.where(st.alive[None, :], z, -np.inf)
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    P = e / e.sum(axis=1, keepdims=True)
    if np.isfinite(st.clamp).any():
        P = apply_clamp(P, st.clamp)
    return P


def apply_clamp(P: np.ndarray, clamp: np.ndarray) -> np.ndarray:
    P = P.copy()
    for c in range(P.shape[0]):
        m = np.isfinite(clamp[c])
        if not m.any():
            continue
        fixed = clamp[c, m].sum()
        rest = P[c, ~m].sum()
        P[c, ~m] *= (1.0 - fixed) / rest if rest > 0 else 0.0
        P[c, m] = clamp[c, m]
    return P


def logit_for_share(Zc: np.ndarray, bias: np.ndarray, alive: np.ndarray, i: int, eps: float) -> float:
    """Logit for operator i giving it share eps in a context row, others fixed."""
    z = Zc + bias
    others = [j for j in range(len(z)) if j != i and alive[j]]
    m = max(z[others])
    S = np.exp(z[others] - m).sum()
    return float(np.log(eps / (1 - eps)) + np.log(S) + m - bias[i])


def step(cfg: Config, st: State, beta: np.ndarray, rng: np.random.Generator,
         ctx_p: np.ndarray | None = None) -> None:
    """One minibatch update, in place."""
    p = np.asarray(cfg.p if ctx_p is None else ctx_p, float)
    B = cfg.B
    c = rng.choice(cfg.C, size=B, p=p / p.sum())
    X = rng.standard_normal((B, cfg.d))
    y = np.einsum("bd,bd->b", X, beta[c]) + cfg.sigma * rng.standard_normal(B)

    P = shares(cfg, st)
    pi = P[c]                                   # (B, K)
    A = X @ st.theta.T                          # (B, K)
    yhat = (pi * A).sum(1)
    err = A - y[:, None]
    l = 0.5 * err ** 2                          # own losses (B, K)
    lhat = 0.5 * (yhat - y) ** 2                # collective loss (B,)
    alive = st.alive[None, :]

    # --- influence update ---
    rule = cfg.rule
    if rule in ("moe", "moe_aux", "moe_bias"):
        lg = np.where(alive, np.log(np.maximum(pi, 1e-300)) - l / cfg.s2, -np.inf)
        lg -= lg.max(1, keepdims=True)
        h = np.exp(lg)
        h /= h.sum(1, keepdims=True)
        g = h - pi                              # ascent direction on logits
        if rule == "moe_aux" and cfg.aux > 0:
            u = pi.mean(0)                      # batch usage
            gl = 2 * cfg.K * u / B              # d aux / d pi_bi
            gz = pi * (gl[None, :] - (pi * gl[None, :]).sum(1, keepdims=True))
            g = g - cfg.aux * gz / cfg.lr_g     # scaled so aux is in loss units
        dZ = np.zeros_like(st.Z)
        np.add.at(dZ, c, cfg.lr_g * g)
        expo = h
    elif rule == "rep":
        dZ = np.zeros_like(st.Z)
        np.add.at(dZ, c, cfg.eta * (lhat[:, None] - l))
        expo = pi
    elif rule == "uniform":
        dZ = 0.0
        expo = pi
    else:
        raise ValueError(rule)
    st.Z = st.Z + np.where(st.alive[None, :], dZ, 0.0)
    # keep logits bounded: recentre each row on its alive max
    zmax = np.max(np.where(st.alive[None, :], st.Z, -np.inf), axis=1, keepdims=True)
    st.Z = st.Z - zmax
    if rule == "moe_bias":
        u = pi.mean(0)
        ua = u[st.alive]
        st.b[st.alive] += cfg.bias_rate * np.sign(ua.mean() - ua)

    # --- exposure and operator update ---
    dec = st.dec[c]                             # (B, K)
    expo = np.where(np.isfinite(dec), dec, expo)
    expo = np.where(alive, expo, 0.0)
    np.add.at(st.exposure_acc, c, expo)
    np.add.at(st.n_ctx, c, 1)
    grad = -(expo * err).T @ X                  # (K, d) ascent on -loss
    upd = ~st.frozen & st.alive
    st.theta[upd] += cfg.lr * grad[upd]
    if cfg.wd > 0:
        st.theta[upd] *= (1.0 - cfg.wd)
    st.t += 1


def run(cfg: Config, st: State, beta: np.ndarray, rng: np.random.Generator, T: int,
        ctx_p=None, every: int = 0, record=None) -> list:
    out = []
    for k in range(T):
        step(cfg, st, beta, rng, ctx_p)
        if every and (k + 1) % every == 0 and record is not None:
            out.append(record(st))
    return out


# ---------------- measurements ----------------

def own_risk(cfg: Config, st: State, beta: np.ndarray) -> np.ndarray:
    """(K, C) held-out relative risk of each operator in each context."""
    diff = st.theta[:, None, :] - beta[None, :, :]
    return ((diff ** 2).sum(-1) + cfg.sigma ** 2) / (1 + cfg.sigma ** 2)


def collective_risk(cfg: Config, st: State, beta: np.ndarray, P=None) -> np.ndarray:
    """(C,) held-out relative risk of the collective in each context."""
    P = shares(cfg, st) if P is None else P
    mix = P @ st.theta                          # (C, d)
    return (((mix - beta) ** 2).sum(-1) + cfg.sigma ** 2) / (1 + cfg.sigma ** 2)


def marginal_contribution(cfg: Config, st: State, beta: np.ndarray) -> np.ndarray:
    """(K, C): risk without i (shares renormalized) minus risk with i."""
    P = shares(cfg, st)
    base = collective_risk(cfg, st, beta, P)
    out = np.zeros((cfg.K, cfg.C))
    for i in range(cfg.K):
        if not st.alive[i]:
            continue
        Q = P.copy()
        Q[:, i] = 0
        s = Q.sum(1, keepdims=True)
        Q = np.where(s > 0, Q / np.where(s > 0, s, 1), 0)
        out[i] = collective_risk(cfg, st, beta, Q) - base
    return out


def mutual_information(cfg: Config, P: np.ndarray) -> float:
    """I(operator; context) in nats, joint p(c) pi_ci."""
    p = np.asarray(cfg.p, float)
    J = p[:, None] * P
    u = J.sum(0)
    m = J > 0
    return float((J[m] * np.log(J[m] / (p[:, None] * u[None, :])[m])).sum())


def usage(cfg: Config, P: np.ndarray) -> np.ndarray:
    return np.asarray(cfg.p, float) @ P


def entropy(v: np.ndarray) -> float:
    v = v[v > 0]
    return float(-(v * np.log(v)).sum())


def gram_spectrum(st: State) -> list:
    th = st.theta[st.alive]
    n = np.linalg.norm(th, axis=1, keepdims=True)
    U = th / np.maximum(n, 1e-12)
    return sorted(np.linalg.eigvalsh(U @ U.T).tolist(), reverse=True)
