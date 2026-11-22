"""LEAD-052: acquisition order on data with a known tree, with the spectral
strength of each level set independently of the tree.

Data. N = 2**L items are the leaves of a binary tree of depth L. The Haar
basis of R^N splits into levels: level 0 is the constant vector, and level
l (1..L) holds 2**(l-1) vectors, each +/- on the two children of one node
at depth l-1 and zero elsewhere. Level l's vectors are exactly the
distinctions the tree draws at depth l. Inputs and targets are written in
this basis with a strength per level:

    X = sqrt(N) H diag(c) R_in,   Y = sqrt(N) H diag(g) R_out,

with H the N x N Haar matrix (columns grouped by level, c and g expanded
over each level's columns) and R_in, R_out random orthogonal rotations. So
Sigma_x = X^T X / N has eigenvalue c_l^2 on level l, and the input-output
correlation Sigma_yx = Y^T X / N has singular value s_l = c_l g_l on level
l. The tree fixes the vectors; c and g fix the strengths, freely.

Acquisition. With P_l the projector onto level l's span in item space and
F the network's outputs on the N items (an N x d_out matrix), level l's
relative risk is r_l = ||P_l (F - Y)||^2 / ||P_l Y||^2, and level l is
acquired at T_l(delta) = first time r_l <= delta. This is QUESTION-217's
T_l(delta) with the network's own output as the decoder.

Time. Every learner minimizes L = (1 / 2N) sum_i ||f(x_i) - y_i||^2. Time t
is gradient-flow time: a gradient step of size eta advances t by eta.

numpy only; manual backpropagation.
"""
import numpy as np


# ---------------------------------------------------------------- data

def haar(L):
    """Return (H, level): H is N x N orthogonal with Haar columns; level[k]
    is column k's level (0..L)."""
    N = 2 ** L
    cols, lev = [np.ones(N) / np.sqrt(N)], [0]
    for l in range(1, L + 1):
        block = N // 2 ** (l - 1)
        for j in range(2 ** (l - 1)):
            v = np.zeros(N)
            v[j * block: j * block + block // 2] = 1.0
            v[j * block + block // 2: (j + 1) * block] = -1.0
            cols.append(v / np.sqrt(block))
            lev.append(l)
    return np.array(cols).T, np.array(lev)


def random_rotation(n, m, rng):
    """n x m with orthonormal rows (n <= m)."""
    Q, _ = np.linalg.qr(rng.standard_normal((m, m)))
    return Q[:n]


def make_data(L, c, g, d_in=None, d_out=None, seed=0):
    """c, g: per-level strengths, length L+1 (index 0 = the root/mean)."""
    N = 2 ** L
    d_in = d_in or N
    d_out = d_out or N
    c, g = np.asarray(c, float), np.asarray(g, float)
    H, lev = haar(L)
    rng = np.random.default_rng(10_000 + seed)
    X = np.sqrt(N) * (H * c[lev]) @ random_rotation(N, d_in, rng)
    Y = np.sqrt(N) * (H * g[lev]) @ random_rotation(N, d_out, rng)
    P = [H[:, lev == l] @ H[:, lev == l].T for l in range(L + 1)]
    return dict(X=X, Y=Y, H=H, lev=lev, P=P, L=L, N=N, c=c, g=g)


def level_risks(F, data, levels):
    Y, P = data["Y"], data["P"]
    E = F - Y
    return np.array([np.sum((P[l] @ E) ** 2) / np.sum((P[l] @ Y) ** 2)
                     for l in levels])


def target_levels(data):
    return [l for l in range(data["L"] + 1) if data["g"][l] > 0]


# ---------------------------------------------------------------- order

def classify(T, tol=1.25):
    """T: acquisition times of levels in coarse-to-fine order. Two levels
    are tied when the later time is at most tol times the earlier. Returns
    'coarse-first', 'fine-first', 'simultaneous', 'mixed' or 'incomplete'
    (some level never acquired)."""
    T = np.asarray(T, float)
    if not np.all(np.isfinite(T)):
        return "incomplete"
    coarse_ahead = fine_ahead = False
    for a in range(len(T)):
        for b in range(a + 1, len(T)):  # a coarser than b
            if T[a] * tol < T[b]:
                coarse_ahead = True
            elif T[b] * tol < T[a]:
                fine_ahead = True
    if coarse_ahead and fine_ahead:
        return "mixed"
    if coarse_ahead:
        return "coarse-first"
    if fine_ahead:
        return "fine-first"
    return "simultaneous"


def first_crossing(times, risks, delta):
    """risks: (n_times, n_levels). First time each level's risk <= delta,
    interpolated linearly in log risk between records; inf if never."""
    out = []
    for k in range(risks.shape[1]):
        r = risks[:, k]
        idx = np.nonzero(r <= delta)[0]
        if len(idx) == 0:
            out.append(np.inf)
            continue
        i = idx[0]
        if i == 0:
            out.append(times[0])
            continue
        la, lb = np.log(r[i - 1]), np.log(r[i])
        w = (la - np.log(delta)) / (la - lb) if la != lb else 1.0
        out.append(times[i - 1] + w * (times[i] - times[i - 1]))
    return np.array(out)


# ---------------------------------------------------------------- kernel regime

def relu_ntk(X):
    """NTK Gram of f(x) = m^-1/2 sum_j v_j relu(w_j . x / sqrt(d)) with
    w, v ~ N(0, 1), in the infinite-width limit (one output)."""
    d = X.shape[1]
    G = X @ X.T / d
    n = np.sqrt(np.diag(G))
    cos = np.clip(G / np.outer(n, n), -1.0, 1.0)
    th = np.arccos(cos)
    k1 = (np.sin(th) + (np.pi - th) * cos) / (2 * np.pi)  # E relu relu / |.||.|
    k0 = (np.pi - th) / (2 * np.pi)                        # E relu' relu'
    return np.outer(n, n) * k1 + G * k0


def linear_ntk(X):
    """Kernel of a single linear layer f = W x / sqrt(d): the shallow linear
    network."""
    return X @ X.T / X.shape[1]


def kernel_flow_risks(K, data, times):
    """Exact gradient flow of a kernel model from zero output:
    dF/dt = -(1/N) K (F - Y), so F(t) = Y - exp(-K t / N) Y."""
    N = data["N"]
    lam, U = np.linalg.eigh(K)
    Yt = U.T @ data["Y"]
    levels = target_levels(data)
    out = []
    for t in times:
        F = data["Y"] - U @ (np.exp(-lam * t / N)[:, None] * Yt)
        out.append(level_risks(F, data, levels))
    return np.array(out)


def level_eigenvalues(K, data):
    """Rayleigh quotient of K on each level (exact eigenvalue when K
    commutes with the level projectors), and the largest commutator norm."""
    H, lev = data["H"], data["lev"]
    mu = np.array([np.mean(np.diag(H[:, lev == l].T @ K @ H[:, lev == l]))
                   for l in range(data["L"] + 1)])
    comm = max(np.linalg.norm(K @ P - P @ K) for P in data["P"]) / np.linalg.norm(K)
    return mu, comm


# ---------------------------------------------------------------- networks

def init_deep_linear(d_in, d_out, width, depth, scale, rng):
    dims = [d_in] + [width] * (depth - 1) + [d_out]
    return [scale * rng.standard_normal((dims[k + 1], dims[k])) / np.sqrt(dims[k])
            for k in range(depth)]


def deep_linear_step(Ws, X, Y, lr):
    N = len(X)
    acts = [X.T]
    for W in Ws:
        acts.append(W @ acts[-1])
    E = (acts[-1] - Y.T) / N           # d L / d F^T
    G = E
    grads = [None] * len(Ws)
    for k in range(len(Ws) - 1, -1, -1):
        grads[k] = G @ acts[k].T
        G = Ws[k].T @ G
    for k in range(len(Ws)):
        Ws[k] -= lr * grads[k]
    return acts[-1].T


def deep_linear_out(Ws, X):
    A = X.T
    for W in Ws:
        A = W @ A
    return A.T


def init_relu(d_in, d_out, width, scale, rng, ntk=False):
    """Two-layer ReLU net f(x) = V relu(W x). Antisymmetric: the second
    half of the hidden units copies the first half's W with V negated, so
    f = 0 at the start (as in LEAD-045's network.py). Standard
    parametrization W ~ N(0, 1/d_in), V ~ N(0, 1/width), both times scale;
    ntk=True keeps unit-variance weights and puts 1/sqrt(fan-in) in the
    forward pass instead."""
    half = width // 2
    if ntk:
        W = rng.standard_normal((half, d_in))
        V = rng.standard_normal((d_out, half))
    else:
        W = scale * rng.standard_normal((half, d_in)) / np.sqrt(d_in)
        V = scale * rng.standard_normal((d_out, half)) / np.sqrt(width)
    return dict(W=np.vstack([W, W]), V=np.hstack([V, -V]), ntk=ntk)


def relu_forward(p, X):
    W, V = p["W"], p["V"]
    if p["ntk"]:
        a, b = 1 / np.sqrt(W.shape[1]), 1 / np.sqrt(W.shape[0])
    else:
        a = b = 1.0
    Hpre = a * (X @ W.T)
    A = np.maximum(Hpre, 0.0)
    return b * (A @ V.T), (Hpre, A, a, b)


def relu_step(p, X, Y, lr):
    N = len(X)
    F, (Hpre, A, a, b) = relu_forward(p, X)
    E = (F - Y) / N
    gV = b * (E.T @ A)
    gA = b * (E @ p["V"])
    gW = a * ((gA * (Hpre > 0)).T @ X)
    p["V"] -= lr * gV
    p["W"] -= lr * gW
    return F


# ---------------------------------------------------------------- one run

def train(data, arch, seed, lr, t_max, n_records=400, width=64, scale=0.01,
          depth=2, stop_delta=0.05):
    """Train one network and return (times, risks). Records on a geometric
    grid of steps. Stops once every target level's risk is below
    stop_delta or at t_max."""
    rng = np.random.default_rng(seed)
    X, Y, N = data["X"], data["Y"], data["N"]
    levels = target_levels(data)
    if arch == "deep_linear":
        params = init_deep_linear(X.shape[1], Y.shape[1], width, depth, scale, rng)
        step = lambda: deep_linear_step(params, X, Y, lr)
        out = lambda: deep_linear_out(params, X)
    elif arch in ("relu", "relu_ntk"):
        params = init_relu(X.shape[1], Y.shape[1], width, scale, rng,
                           ntk=(arch == "relu_ntk"))
        step = lambda: relu_step(params, X, Y, lr)
        out = lambda: relu_forward(params, X)[0]
    else:
        raise ValueError(arch)
    n_steps = int(np.ceil(t_max / lr))
    rec = set(np.unique(np.geomspace(1, n_steps, n_records).astype(int)).tolist())
    times, risks = [0.0], [level_risks(out(), data, levels)]
    for s in range(1, n_steps + 1):
        step()
        if s in rec or s == n_steps:
            r = level_risks(out(), data, levels)
            times.append(s * lr)
            risks.append(r)
            if np.all(r <= stop_delta):
                break
    return np.array(times), np.array(risks)


def deep_linear_theory_T(c, g, eps0, delta):
    """Acquisition time of each level for the decoupled balanced two-layer
    linear network (Saxe et al.): mode strength a obeys
    da/dt = 2 a (s - c^2 a) with s = c g in this module's time units, so
    b = c^2 a / s is logistic at rate 2 s from b0 = c^2 eps0 / s, and the
    level's relative risk is (1 - b)^2."""
    c, g = np.asarray(c, float), np.asarray(g, float)
    s = c * g
    b0 = c ** 2 * eps0 / s
    b1 = 1 - np.sqrt(delta)
    return (np.log(b1 / (1 - b1)) - np.log(b0 / (1 - b0))) / (2 * s)
