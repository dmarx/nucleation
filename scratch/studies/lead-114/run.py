"""LEAD-114 pipeline: train a group-composition network, reconstruct the
operation it learned (blind), recover irreducibles blind vs control, and test
how much of each irrep the learned weights carry. Writes one JSON line per
(group, seed) item to results.jsonl (append-only, resumable)."""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np

import groups
import model
import reptheory as rt

RESULTS = os.path.join(os.path.dirname(__file__), "results.jsonl")

# (name, builder, kwargs, seed). The name encodes the regime:
#   S3-mem    : S3 with a held-out split it cannot generalise to (memorises)
#   S3-fit    : S3 trained on the whole table (fits; no generalisation test)
#   S4-grok   : S4 with a held-out split it DOES generalise to (learns the law)
ITEMS = []
for seed in range(3):
    ITEMS.append(("S3-mem", lambda: groups.symmetric_group(3),
                  dict(d=16, H=48, wd=1e-2, lr=0.3, steps=20000,
                       holdout=0.25, seed=seed), seed))
for seed in range(3):
    ITEMS.append(("S3-fit", lambda: groups.symmetric_group(3),
                  dict(d=16, H=48, wd=2e-3, lr=0.3, steps=8000,
                       holdout=0.0, seed=seed), seed))
for seed in range(3):
    ITEMS.append(("S4-grok", lambda: groups.symmetric_group(4),
                  dict(d=24, H=128, wd=1e-3, lr=0.3, steps=10000,
                       holdout=0.20, seed=seed), seed))


def done_keys():
    if not os.path.exists(RESULTS):
        return set()
    keys = set()
    with open(RESULTS) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            keys.add((r["group"], r["seed"]))
    return keys


def table_agreement(a, b):
    return float(np.mean(a == b))


def _drop_trivial(fracs, dims, char_table):
    """Renormalise `fracs` over the non-trivial irreps. The trivial irrep is
    the dim-1 block whose recovered character is all ones."""
    char = np.array(char_table)
    triv = None
    for i, d in enumerate(dims):
        if d == 1 and np.all(np.abs(char[i] - 1.0) < 1e-4):
            triv = i
            break
    kept = [(i, f) for i, f in enumerate(fracs) if i != triv]
    s = sum(f for _, f in kept)
    if s <= 0:
        return {"trivial_index": triv, "fracs": [f for _, f in kept]}
    return {"trivial_index": triv,
            "fracs": [f / s for _, f in kept]}


def run_item(name, builder, kw, seed):
    _, cayley = builder()
    m = cayley.shape[0]
    p, info = model.train(cayley, **kw)

    # Blind: operation the network learned.
    Tnet = model.reconstruct_table(p)
    agree = table_agreement(Tnet, cayley)
    net_is_group = groups.is_group_table(Tnet)

    # Control recovery (true group supplied).
    ctrl = rt.recover_irreps(cayley, seed=0)
    ctrl_fracs, ctrl_resid = rt.embedding_irrep_content(p["E"], ctrl["blocks"])
    ctrl_unemb, _ = rt.embedding_irrep_content(p["Wu"], ctrl["blocks"])
    # Non-trivial ("faithful") spectrum: drop the constant/trivial irrep (the
    # dim-1 block whose character is all ones) and renormalise.
    ctrl_nontrivial = _drop_trivial(ctrl_fracs, ctrl["dims"],
                                    ctrl["character_table"])

    # Blind recovery: from the reconstructed table, IF it is a valid group.
    blind = None
    blind_fracs = None
    blind_resid = None
    blind_nontrivial = None
    if net_is_group["is_group"]:
        b = rt.recover_irreps(Tnet, seed=0)
        bf, br = rt.embedding_irrep_content(p["E"], b["blocks"])
        blind = {k: b[k] for k in ("n_irreps", "n_classes", "dims", "sum_d2",
                                   "character_table", "ortho_residual",
                                   "max_char_imag")}
        blind_fracs, blind_resid = bf, br
        blind_nontrivial = _drop_trivial(bf, b["dims"], b["character_table"])

    rec = {
        "group": name,
        "seed": seed,
        "params": kw,
        "train_acc": info["train_acc"],
        "test_acc": info["test_acc"],
        "n_train": info["n_train"],
        "n_test": info["n_test"],
        "table_agreement": agree,
        "net_is_group": net_is_group,
        "control": {k: ctrl[k] for k in ("n_irreps", "dims", "sum_d2",
                                         "character_table", "ortho_residual")},
        "control_emb_fracs": ctrl_fracs,
        "control_unemb_fracs": ctrl_unemb,
        "control_emb_residual": ctrl_resid,
        "control_emb_nontrivial": ctrl_nontrivial,
        "blind": blind,
        "blind_emb_fracs": blind_fracs,
        "blind_emb_residual": blind_resid,
        "blind_emb_nontrivial": blind_nontrivial,
    }
    return rec


def main():
    keys = done_keys()
    for name, builder, kw, seed in ITEMS:
        if (name, seed) in keys:
            print(f"skip {name} seed={seed} (done)", flush=True)
            continue
        print(f"run  {name} seed={seed} ...", flush=True)
        rec = run_item(name, builder, kw, seed)
        with open(RESULTS, "a") as f:
            f.write(json.dumps(rec) + "\n")
        bd = rec["blind"]["dims"] if rec["blind"] else None
        print(f"  test_acc={rec['test_acc']:.3f} "
              f"agree={rec['table_agreement']:.3f} "
              f"net_group={rec['net_is_group']['is_group']} "
              f"ctrl_dims={rec['control']['dims']} blind_dims={bd}",
              flush=True)


if __name__ == "__main__":
    main()
