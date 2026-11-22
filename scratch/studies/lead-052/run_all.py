"""LEAD-052: run every arm and append one JSON line per item to
results/runs.jsonl. Rerunning skips items already written, so an
interrupted run resumes.

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run_all.py [E1|E2|E3]

E1  target strengths varied, inputs flat: g = (0, 1, a, b), c = 1,
    log2 a, log2 b in {-2, -1.5, ..., 2}.
E2  input and target strengths varied together, geometric in the level:
    c_l = rho_in^(l-1), g_l = rho_out^(l-1) (l = 1..3), c_0 = 1, g_0 = 0,
    log2 rho in {-0.5, -1/3, ..., 0.5}.
E3  the initial scale of the two-layer ReLU network (standard
    parametrization) and the width of the NTK-parametrized one, on three
    target profiles with flat inputs.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phases as ph  # noqa: E402

L = 3
SEEDS = (0, 1, 2)
DELTAS = (0.5, 0.1, 0.02)
OUT = os.path.join(HERE, "results", "runs.jsonl")

ARCHS = {
    # name: (arch, kwargs, lr)
    "deep_linear_2": ("deep_linear", dict(depth=2, width=16, scale=0.01), 0.02),
    "deep_linear_3": ("deep_linear", dict(depth=3, width=16, scale=0.05), 0.02),
    "relu_small": ("relu", dict(width=64, scale=0.01), 0.02),
    "relu_std_1": ("relu", dict(width=64, scale=1.0), 0.0002),
    "relu_ntk_64": ("relu_ntk", dict(width=64, scale=1.0), 0.05),
    "relu_ntk_2048": ("relu_ntk", dict(width=2048, scale=1.0), 0.05),
}
KERNELS = {"kernel_relu_ntk": ph.relu_ntk, "kernel_linear": ph.linear_ntk}


def grid_E1():
    vals = np.arange(-2, 2.01, 0.5)
    for la in vals:
        for lb in vals:
            yield dict(la=float(la), lb=float(lb)), [1, 1, 1, 1], [0, 1, 2 ** la, 2 ** lb]


def grid_E2():
    vals = np.linspace(-0.5, 0.5, 7)
    for li in vals:
        for lo in vals:
            ri, ro = 2 ** li, 2 ** lo
            c = [1, 1, ri, ri ** 2]
            g = [0, 1, ro, ro ** 2]
            yield dict(log2_rho_in=float(li), log2_rho_out=float(lo)), c, g


E3_PROFILES = {"coarse_strong": [0, 1, 0.5, 0.25], "fine_strong": [0, 0.25, 0.5, 1],
               "middle_weak": [0, 1, 0.25, 0.5]}


def e3_archs():
    for s in (0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0):
        lr = 0.02 * min(1.0, (0.1 / s) ** 2)
        yield f"relu_std_scale_{s:g}", ("relu", dict(width=64, scale=s), lr)
    for w in (64, 256, 1024, 4096):
        yield f"relu_ntk_width_{w}", ("relu_ntk", dict(width=w, scale=1.0), 0.05)


def load_done():
    done = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                r = json.loads(line)
                done.add(r["key"])
    return done


def write(rec):
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def network_item(exp, point, c, g, name, spec, seed, t_max):
    arch, kw, lr = spec
    d = ph.make_data(L, c, g, seed=seed)
    t0 = time.time()
    t, r = ph.train(d, arch, seed=seed, lr=lr, t_max=t_max, stop_delta=min(DELTAS) * 0.9,
                    **kw)
    T = {str(dl): ph.first_crossing(t, r, dl).tolist() for dl in DELTAS}
    return dict(exp=exp, point=point, c=list(map(float, c)), g=list(map(float, g)),
                learner=name, seed=seed, lr=lr, T=T, final_risk=r[-1].tolist(),
                t_end=float(t[-1]), seconds=round(time.time() - t0, 2))


def kernel_item(exp, point, c, g, name, seed):
    d = ph.make_data(L, c, g, seed=seed)
    K = KERNELS[name](d["X"])
    mu, comm = ph.level_eigenvalues(K, d)
    levels = ph.target_levels(d)
    T = {str(dl): [float(d["N"] * np.log(1 / dl) / (2 * mu[l])) for l in levels]
         for dl in DELTAS}
    return dict(exp=exp, point=point, c=list(map(float, c)), g=list(map(float, g)),
                learner=name, seed=seed, T=T, mu=mu.tolist(), commutator=float(comm))


def items(which):
    if "E1" in which or "E2" in which:
        for exp, grid in (("E1", grid_E1), ("E2", grid_E2)):
            if exp not in which:
                continue
            for point, c, g in grid():
                for name in KERNELS:
                    yield (exp, point, name, 0), ("kernel", exp, point, c, g, name, 0)
                for name, spec in ARCHS.items():
                    for seed in SEEDS:
                        yield (exp, point, name, seed), ("net", exp, point, c, g, name, spec, seed)
    if "E3" in which:
        for prof, g in E3_PROFILES.items():
            for name, spec in e3_archs():
                for seed in SEEDS:
                    yield (("E3", prof, name, seed),
                           ("net", "E3", dict(profile=prof), [1, 1, 1, 1], g, name, spec, seed))


def main():
    which = sys.argv[1:] or ["E1", "E2", "E3"]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    done = load_done()
    n_new = 0
    t_start = time.time()
    for key, job in items(which):
        key = json.dumps(key, sort_keys=True)
        if key in done:
            continue
        if job[0] == "kernel":
            rec = kernel_item(*job[1:])
        else:
            rec = network_item(*job[1:], t_max=min(2000.0, 150_000 * job[-2][2]))
        rec["key"] = key
        write(rec)
        n_new += 1
        if n_new % 50 == 0:
            print(f"{n_new} items, {time.time() - t_start:.0f} s", flush=True)
    print(f"done: {n_new} new items in {time.time() - t_start:.0f} s", flush=True)


if __name__ == "__main__":
    main()
