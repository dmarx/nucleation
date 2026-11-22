"""LEAD-039 numerical support. Writes one JSON line per item; resumes.

  python3 -I run_studies.py s1   # two-row channels: intervals nest
  python3 -I run_studies.py s2   # three effective states: failure rate
  python3 -I run_studies.py s3   # products of two-row pairs: tensorization
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402

import ibnest as ib  # noqa: E402

BETAS = np.geomspace(1.05, 80, 40)


def done_ids(path):
    if not os.path.exists(path):
        return set()
    with open(path) as fh:
        return {json.loads(l)["id"] for l in fh if l.strip()}


def emit(path, rec):
    with open(path, "a") as fh:
        fh.write(json.dumps(rec) + "\n")
        fh.flush()


def s1(n=300):
    path = os.path.join(HERE, "s1_two_rows.jsonl")
    seen = done_ids(path)
    g = ib.simplex_grid(2, 4000)
    tol = 2.0 / 4000
    for i in range(n):
        if i in seen:
            continue
        rng = np.random.default_rng(1000 + i)
        ny = int(rng.integers(2, 7))
        a, b = rng.dirichlet(np.ones(ny) * 0.7), rng.dirichlet(np.ones(ny) * 0.7)
        if rng.random() < 0.3:
            a[rng.integers(ny)] = 0
            a /= a.sum()
        pr = rng.uniform(0.05, 0.95)
        p, K = np.array([1 - pr, pr]), np.vstack([a, b])
        ivals = []
        for beta in BETAS:
            pts, _ = ib.envelope_decomp(p, K, beta, g)
            x = pts[:, 1]
            ivals.append((float(x.min()), float(x.max())))
        viol = 0.0
        for (u1, v1), (u2, v2) in zip(ivals[:-1], ivals[1:]):
            if v1 - u1 < 1e-12:  # trivial coarse encoder nests in anything
                continue
            viol = max(viol, u2 - u1, v1 - v2)
        emit(path, dict(id=i, ny=ny, pr=pr, max_violation=viol,
                        nested=bool(viol <= tol),
                        nontrivial=sum(v - u > 3 * tol for u, v in ivals),
                        intervals=[[round(u, 5), round(v, 5)] for u, v in ivals]))


def s2(n=150):
    path = os.path.join(HERE, "s2_three_states.jsonl")
    seen = done_ids(path)
    m = 300
    g = ib.simplex_grid(3, m)
    betas = np.geomspace(1.5, 60, 16)
    for i in range(n):
        if i in seen:
            continue
        rng = np.random.default_rng(5000 + i)
        ny = 2 if i % 2 == 0 else 3
        p = rng.dirichlet(np.ones(3) * 2)
        K = rng.dirichlet(np.ones(ny) * 0.7, size=3)
        dec = [ib.envelope_decomp(p, K, b, g) for b in betas]
        rows = []
        for j in range(len(betas) - 1):
            c, f = dec[j][0], dec[j + 1][0]
            if len(c) == 1:
                rows.append(0.0)
                continue
            rows.append(float(ib.hull_distance(c, f)))
        far = []
        for j in range(0, len(betas) - 5, 5):
            c, f = dec[j][0], dec[j + 5][0]
            far.append(0.0 if len(c) == 1 else float(ib.hull_distance(c, f)))
        emit(path, dict(id=i, ny=ny, p=p.tolist(), K=K.tolist(), adjacent=rows, far=far,
                        npts=[len(d[0]) for d in dec]))


def s3(n=12):
    path = os.path.join(HERE, "s3_products.jsonl")
    seen = done_ids(path)
    g4 = ib.simplex_grid(4, 40)
    g2 = ib.simplex_grid(2, 4000)
    for i in range(n):
        if i in seen:
            continue
        rng = np.random.default_rng(9000 + i)
        comps = []
        for _ in range(2):
            ny = int(rng.integers(2, 4))
            K = rng.dirichlet(np.ones(ny) * 0.7, size=2)
            pr = rng.uniform(0.2, 0.8)
            comps.append((np.array([1 - pr, pr]), K))
        (p1, K1), (p2, K2) = comps
        p = np.kron(p1, p2)
        K = np.kron(K1, K2)
        out = []
        for beta in [2.0, 4.0, 8.0, 16.0]:
            val_comp = 0.0
            for pc, Kc in comps:
                pts, w = ib.envelope_decomp(pc, Kc, beta, g2)
                val_comp += float(w @ ib.F(pts, Kc, beta))
            pts, w = ib.envelope_decomp(p, K, beta, g4)
            val_grid = float(w @ ib.F(pts, K, beta))
            # Entropies add over independent products, so tensorization of the
            # Lagrangian says the product's envelope at p is the sum of the
            # components' envelopes. The grid envelope can only lie above it.
            out.append(dict(beta=beta, product_of_components=val_comp,
                            grid_envelope=val_grid, gap=val_grid - val_comp))
        emit(path, dict(id=i, rows=out))


if __name__ == "__main__":
    {"s1": s1, "s2": s2, "s3": s3}[sys.argv[1]]()
