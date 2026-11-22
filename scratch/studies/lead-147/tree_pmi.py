"""PMI spectrum of a co-occurrence model with implication among binary attributes.

Model: word i carries binary attributes x_ik in {0,1}, closed upward under an
implication order (x_ik = 1 and k => l give x_il = 1).  Each shared attribute
multiplies co-occurrence by exp(lam_k), so

    PMI = X diag(lam) X^T + (rank <= 2 affine terms).

Functions here build the b-ary tree case, the closed-form spectrum, and the
readout checks that the CLAIM of LEAD-147 states.  Run directly for a report.
"""
import itertools
import numpy as np


def btree(b, D):
    """Nodes of a complete b-ary tree of depth D as tuples (root = ()).
    Returns list of nodes with depth >= 1 (the attributes) and the leaves."""
    nodes = []
    for l in range(1, D + 1):
        nodes += list(itertools.product(range(b), repeat=l))
    leaves = list(itertools.product(range(b), repeat=D))
    return nodes, leaves


def incidence(b, D, words_per_leaf=1):
    """X: words x attributes, word at a leaf carries all its ancestors (depth>=1)."""
    nodes, leaves = btree(b, D)
    idx = {n: j for j, n in enumerate(nodes)}
    rows, depth = [], np.array([len(n) for n in nodes])
    for leaf in leaves:
        for _ in range(words_per_leaf):
            r = np.zeros(len(nodes))
            for l in range(1, D + 1):
                r[idx[leaf[:l]]] = 1
            rows.append(r)
    return np.array(rows), depth, nodes


def predicted_spectrum(b, D, lam, words_per_leaf=1, lam_root=0.0):
    """Closed form for X diag(lam) X^T, lam[l-1] the strength at depth l.

    Level l = 0..D-1 (a branching at a depth-l node) gives eigenvalue
    mu_l = w * sum_{l' > l} lam_{l'} * b^(D - l')   with multiplicity (b-1) b^l;
    the constant vector gets mu_const = w * sum_{l' >= 0} lam_{l'} b^(D-l').
    With w > 1 words per leaf, the within-leaf contrasts get eigenvalue 0."""
    lam_full = np.concatenate([[lam_root], lam])  # depth 0..D
    w = words_per_leaf
    out = [(w * sum(lam_full[lp] * b ** (D - lp) for lp in range(0, D + 1)), 1, "const")]
    for l in range(D):
        mu = w * sum(lam_full[lp] * b ** (D - lp) for lp in range(l + 1, D + 1))
        out.append((mu, (b - 1) * b ** l, f"level{l}"))
    return out


def spectral_embedding(M, r=None):
    """Top-r eigenpairs (by |eigenvalue|) of symmetric M, scaled by sqrt|ev|."""
    ev, U = np.linalg.eigh(M)
    order = np.argsort(-np.abs(ev))
    ev, U = ev[order], U[:, order]
    if r is None:
        r = int(np.sum(np.abs(ev) > 1e-9 * np.abs(ev).max()))
    return U[:, :r] * np.sqrt(np.abs(ev[:r])), ev


def readout(E, X, thresh=0.5, raw=False):
    """Least-squares affine readout of each attribute from embedding E,
    thresholded (or the raw fitted values if raw=True)."""
    A = np.hstack([E, np.ones((E.shape[0], 1))])
    W, *_ = np.linalg.lstsq(A, X, rcond=None)
    F = A @ W
    return F if raw else (F > thresh).astype(float)


def random_context(n_words, d, n_impl, rng):
    """A general formal context: random implication DAG among d attributes
    (k => parent edges, acyclic by index), words = random attribute sets closed
    upward under the implications."""
    parents = {k: [] for k in range(d)}
    for _ in range(n_impl):
        k, p = sorted(rng.choice(d, 2, replace=False))[::-1]  # k > p, k => p
        parents[k].append(p)
    X = np.zeros((n_words, d))
    for i in range(n_words):
        seed = rng.random(d) < 0.15
        for k in range(d - 1, -1, -1):  # close upward (parents have lower index)
            if seed[k]:
                stack = [k]
                while stack:
                    j = stack.pop()
                    if not X[i, j]:
                        X[i, j] = 1
                        stack += parents[j]
    return X, parents


def report():
    rng = np.random.default_rng(0)
    b, D = 3, 4
    lam = rng.uniform(0.2, 2.0, D)
    X, depth, nodes = incidence(b, D)
    M = X @ np.diag(lam[depth - 1]) @ X.T
    ev = np.sort(np.linalg.eigvalsh(M))[::-1]
    pred = predicted_spectrum(b, D, lam)
    pred_ev = np.sort(np.concatenate([[mu] * m for mu, m, _ in pred]))[::-1]
    print("tree b=3 D=4, lam =", np.round(lam, 3))
    print("max |eig - closed form| =", np.abs(ev[: len(pred_ev)] - pred_ev).max())
    for mu, m, name in pred:
        print(f"  {name:7s} eigenvalue {mu:8.3f}  multiplicity {m}")
    E, _ = spectral_embedding(M)
    print("full-rank readout exact:", np.array_equal(readout(E, X), X))
    for K in range(1, D + 1):
        Ek, _ = spectral_embedding(M, r=b ** K)
        R = readout(Ek, X)
        ok = [np.array_equal(R[:, depth == l], X[:, depth == l]) for l in range(1, D + 1)]
        print(f"  rank {b**K:3d}: exact by depth 1..{D}:", ok)
    Xg, _ = random_context(300, 40, 60, rng)
    Xg = Xg[:, Xg.sum(0) > 0]
    Mg = Xg @ np.diag(rng.uniform(0.2, 2, Xg.shape[1])) @ Xg.T
    Eg, _ = spectral_embedding(Mg)
    print("general context: rank", Eg.shape[1], "attributes", Xg.shape[1],
          "readout exact:", np.array_equal(readout(Eg, Xg), Xg))


if __name__ == "__main__":
    report()
