"""LEAD-147 measurement: PMI additivity along WordNet hypernymy and across
analogy families, on text8.

    python3 -I measure.py TEXT8 NLTK_DATA QUESTIONS_WORDS CACHE_DIR

Stages (each resumable):
  counts   -> CACHE_DIR/counts_{full,h1,h2}.npy   (co-occurrence, window +-5)
  hier     -> results/hierarchy.jsonl  (one line per model / rank / attribute)
  analogy  -> results/analogy.jsonl    (one line per analogy family)
Downloaded data and caches stay in CACHE_DIR, outside the repository.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
V, C, WIN = 10000, 5000, 5  # targets, contexts, half-window
RNG = np.random.default_rng(147)


# ---------------------------------------------------------------- utilities
def done_keys(path):
    keys = set()
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                keys.add(json.loads(line)["key"])
    return keys


def append(path, rec):
    with open(path, "a") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def cooc(ids, V, C, win):
    """Symmetric window counts n[i, j], i < V target id, j < C context id."""
    n = np.zeros(V * C, dtype=np.int64)
    for o in range(1, win + 1):
        for a, b in ((ids[:-o], ids[o:]), (ids[o:], ids[:-o])):
            m = (a < V) & (b < C)
            n += np.bincount(a[m].astype(np.int64) * C + b[m], minlength=V * C)
    return n.reshape(V, C)


def spmi(n):
    """Shrunk PMI log((n_ij + 1) / (E_ij + 1)), E_ij = n_i. n_.j / N.
    Finite at zero counts; close to PMI where counts are large."""
    n = n.astype(np.float64)
    E = np.outer(n.sum(1), n.sum(0)) / n.sum()
    return np.log((n + 1.0) / (E + 1.0)).astype(np.float32)


def double_center(Y):
    Y = Y - Y.mean(1, keepdims=True)  # removes each word's own affine term u_w
    return Y - Y.mean(0, keepdims=True)


def interaction_fraction(Pa, Pb, Pc, Pd):
    """2x2 ANOVA over contexts of the quadruple a:b :: c:d.
    Factor 1: (a,c) vs (b,d) -- the analogy relation; factor 2: (a,b) vs (c,d).
    Returns SS_rel, SS_pair, SS_int (sums over contexts)."""
    rel = (Pa + Pc - Pb - Pd) / 2
    pair = (Pa + Pb - Pc - Pd) / 2
    inter = (Pa - Pb - Pc + Pd) / 2
    return (rel ** 2).sum(-1), (pair ** 2).sum(-1), (inter ** 2).sum(-1)


def cv_r2(X, Y, folds=5, alpha=1.0, seed=0):
    """Held-out-word R^2 of ridge Y ~ X B (Y double-centred)."""
    n = X.shape[0]
    perm = np.random.default_rng(seed).permutation(n)
    ss_res = 0.0
    for f in range(folds):
        te = perm[f::folds]
        tr = np.setdiff1d(perm, te)
        Xtr, Xte = X[tr], X[te]
        mx = Xtr.mean(0)
        Xtr, Xte = Xtr - mx, Xte - mx
        my = Y[tr].mean(0)
        B = np.linalg.solve(Xtr.T @ Xtr + alpha * np.eye(X.shape[1]), Xtr.T @ (Y[tr] - my))
        ss_res += ((Y[te] - my - Xte @ B) ** 2).sum()
    return 1.0 - ss_res / ((Y - Y.mean(0)) ** 2).sum()


def embed(P, r):
    U, s, _ = np.linalg.svd(P - P.mean(0), full_matrices=False)
    return U[:, :r] * np.sqrt(s[:r]), s


# ---------------------------------------------------------------- stages
def stage_counts(text8, cache):
    paths = {k: os.path.join(cache, f"counts_{k}.npy") for k in ("full", "h1", "h2")}
    vpath = os.path.join(cache, "vocab.json")
    if all(os.path.exists(p) for p in paths.values()) and os.path.exists(vpath):
        return {k: np.load(p) for k, p in paths.items()}, json.load(open(vpath))
    from collections import Counter
    toks = open(text8).read().split()
    vocab = [w for w, _ in sorted(Counter(toks).items(), key=lambda kv: (-kv[1], kv[0]))]
    idx = {w: i for i, w in enumerate(vocab)}
    ids = np.fromiter((idx[t] for t in toks), dtype=np.int32, count=len(toks))
    del toks
    half = len(ids) // 2
    out = {"full": cooc(ids, V, C, WIN), "h1": cooc(ids[:half], V, C, WIN), "h2": cooc(ids[half:], V, C, WIN)}
    for k, p in paths.items():
        np.save(p, out[k])
    json.dump(vocab[:V], open(vpath, "w"))
    return out, vocab[:V]


def wordnet_nouns(vocab, nltk_data, min_words=5):
    import nltk
    nltk.data.path.insert(0, nltk_data)
    from nltk.corpus import wordnet as wn
    rows, anc = [], []
    for i, w in enumerate(vocab):
        ss = wn.synsets(w)
        if not ss or ss[0].pos() != "n" or w not in ss[0].lemma_names():
            continue  # keep words whose dominant sense is a noun named by the word
        s0 = ss[0]
        a = set(s0.closure(lambda s: s.hypernyms() + s.instance_hypernyms()))
        rows.append(i)
        anc.append(a)
    from collections import Counter
    c = Counter(x for a in anc for x in a)
    attrs = [s for s, k in c.items() if min_words <= k <= 0.5 * len(rows)]
    attrs.sort(key=lambda s: (s.min_depth(), s.name()))
    col = {s: j for j, s in enumerate(attrs)}
    X = np.zeros((len(rows), len(attrs)), dtype=np.float32)
    for r, a in enumerate(anc):
        for s in a:
            if s in col:
                X[r, col[s]] = 1
    depth = np.array([s.min_depth() for s in attrs])
    # parent among the attributes: the attribute ancestor held by the fewest words
    parent = []
    for s in attrs:
        sup = [col[t] for t in s.closure(lambda u: u.hypernyms() + u.instance_hypernyms()) if t in col]
        parent.append(min(sup, key=lambda j: X[:, j].sum()) if sup else -1)
    return np.array(rows), X, depth, np.array(parent), [s.name() for s in attrs]


def stage_hier(counts, vocab, nltk_data):
    path = os.path.join(RES, "hierarchy.jsonl")
    done = done_keys(path)
    rows, X, depth, parent, names = wordnet_nouns(vocab, nltk_data)
    P = {k: double_center(spmi(v)[rows]) for k, v in counts.items()}
    if "summary" not in done:
        r = np.corrcoef(P["h1"].ravel(), P["h2"].ravel())[0, 1]
        append(path, {"key": "summary", "n_nouns": int(len(rows)), "n_attrs": int(X.shape[1]),
                      "split_half_r": float(r), "reliability_sb": float(2 * r / (1 + r)),
                      "depth_counts": {int(d): int((depth == d).sum()) for d in np.unique(depth)}})
    Y = P["full"]
    # additive model in the WordNet attributes, held-out words; nested by depth
    for dmax in list(np.unique(depth)) + [99]:
        key = f"cv_depth<={int(dmax)}"
        if key in done:
            continue
        m = depth <= dmax
        r2 = cv_r2(X[:, m], Y)
        nulls = [cv_r2(X[RNG.permutation(len(X))][:, m], Y, seed=s) for s in range(3)]
        append(path, {"key": key, "n_attrs": int(m.sum()), "r2_cv": float(r2),
                      "r2_cv_permuted": [float(v) for v in nulls]})
    # linear probes on a spectral embedding of the noun PMI rows
    E300, _ = embed(Y, 300)
    for r in (10, 30, 100):  # rank 300 dropped for time on 2026-11-22
        E = E300[:, :r]
        A = np.hstack([E, np.ones((len(E), 1))])
        for j in range(X.shape[1]):
            key = f"probe_r{r}_{names[j]}"
            if key in done:
                continue
            y = 2 * X[:, j] - 1
            pred = np.zeros(len(y))
            perm = np.random.default_rng(j).permutation(len(y))
            for f in range(5):
                te = perm[f::5]
                tr = np.setdiff1d(perm, te)
                wts = np.where(y[tr] > 0, 0.5 / (y[tr] > 0).mean(), 0.5 / (y[tr] < 0).mean())
                W = np.linalg.lstsq(A[tr] * wts[:, None] ** 0.5, y[tr] * wts ** 0.5, rcond=None)[0]
                pred[te] = A[te] @ W
            pos, neg = y > 0, y < 0
            tpr, tnr = (pred[pos] > 0).mean(), (pred[neg] <= 0).mean()
            fp = neg & (pred > 0)
            rec = {"key": key, "rank": r, "attr": names[j], "depth": int(depth[j]),
                   "n_pos": int(pos.sum()), "bal_acc": float((tpr + tnr) / 2), "n_fp": int(fp.sum())}
            if parent[j] >= 0 and fp.sum() > 0:
                inpar = X[:, parent[j]] == 1
                rec["fp_in_parent"] = float(inpar[fp].mean())
                rec["neg_in_parent"] = float(inpar[neg].mean())
            append(path, rec)


def stage_alpha(counts, vocab, nltk_data):
    """The additive fit again with stronger ridge penalties (alpha = 1 overfits
    as attributes are added), at three depth cuts, against one permutation."""
    path = os.path.join(RES, "hierarchy_alpha.jsonl")
    done = done_keys(path)
    rows, X, depth, parent, names = wordnet_nouns(vocab, nltk_data)
    Y = double_center(spmi(counts["full"])[rows])
    perm = np.random.default_rng(7).permutation(len(X))
    for dmax in (4, 6, 99):
        for alpha in (10.0, 100.0, 1000.0):
            key = f"alpha{alpha:g}_depth<={dmax}"
            if key in done:
                continue
            m = depth <= dmax
            append(path, {"key": key, "alpha": alpha, "n_attrs": int(m.sum()),
                          "r2_cv": float(cv_r2(X[:, m], Y, alpha=alpha)),
                          "r2_cv_permuted": float(cv_r2(X[perm][:, m], Y, alpha=alpha))})


def read_analogies(path, idx):
    fams, cur = {}, None
    for line in open(path):
        if line.startswith(":"):
            cur = line[1:].strip()
            fams[cur] = []
            continue
        q = line.lower().split()
        if len(q) == 4 and all(w in idx for w in q) and len(set(q)) == 4:
            fams[cur].append([idx[w] for w in q])
    return {k: np.array(v) for k, v in fams.items() if len(v) >= 20}


def stage_analogy(counts, vocab, qpath):
    path = os.path.join(RES, "analogy.jsonl")
    done = done_keys(path)
    idx = {w: i for i, w in enumerate(vocab)}
    fams = read_analogies(qpath, idx)
    if set(fams) <= done:
        return
    P = {k: spmi(v) for k, v in counts.items()}
    P = {k: v - v.mean(1, keepdims=True) for k, v in P.items()}  # drop word biases
    E, _ = embed(P["full"], 300)
    En = E / np.linalg.norm(E, axis=1, keepdims=True)
    for fam, Q in fams.items():
        if fam in done:
            continue
        a, b, c, d = Q.T
        rel, pair, inter = interaction_fraction(*(P["full"][x] for x in (a, b, c, d)))
        # noise in the interaction, from the two half-corpora (full ~ mean of halves)
        _, _, i1 = interaction_fraction(*(P["h1"][x] - P["h2"][x] for x in (a, b, c, d)))
        noise = i1 / 4
        # parallelogram completion by 3CosAdd in the spectral embedding
        tgt = En[b] - En[a] + En[c]
        sims = tgt @ En.T
        for k, x in enumerate((a, b, c)):
            sims[np.arange(len(Q)), x] = -np.inf
        hit = sims.argmax(1) == d
        tot = rel + pair + inter
        rho = inter / tot
        rho_corr = np.clip(inter - noise, 0, None) / np.clip(tot - 3 * noise, 1e-9, None)
        # null: random quadruples from the same family's words
        ws = np.unique(Q)
        R = RNG.choice(ws, size=(500, 4))
        R = R[np.array([len(set(r)) == 4 for r in R])]
        nr, npair, ni = interaction_fraction(*(P["full"][x] for x in R.T))
        append(path, {"key": fam, "n": int(len(Q)), "acc_3cosadd": float(hit.mean()),
                      "rho_median": float(np.median(rho)), "rho_corr_median": float(np.median(rho_corr)),
                      "noise_share_of_int_median": float(np.median(noise / inter)),
                      "rel_share_median": float(np.median(rel / tot)),
                      "rho_null_median": float(np.median(ni / (nr + npair + ni))),
                      "acc_by_rho_tercile": [float(hit[t].mean()) for t in
                                             np.array_split(np.argsort(rho_corr), 3)]})


def main(text8, nltk_data, qpath, cache):
    os.makedirs(RES, exist_ok=True)
    os.makedirs(cache, exist_ok=True)
    t = time.time()
    counts, vocab = stage_counts(text8, cache)
    print(f"counts {time.time()-t:.0f}s", flush=True)
    stage_analogy(counts, vocab, qpath)
    print(f"analogy {time.time()-t:.0f}s", flush=True)
    stage_hier(counts, vocab, nltk_data)
    print(f"hier {time.time()-t:.0f}s", flush=True)
    stage_alpha(counts, vocab, nltk_data)
    print(f"alpha {time.time()-t:.0f}s", flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:5])
