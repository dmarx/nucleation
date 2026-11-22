"""Write summary.txt from results.jsonl (LEAD-026)."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    recs = {}
    with open(os.path.join(HERE, "results.jsonl")) as f:
        for line in f:
            d = json.loads(line)
            recs[(d["arm"], d["item"])] = d
    return recs


def main():
    recs = load()
    arms = [a for a in ["A", "B", "C", "C0"] if (a, "stats") in recs]
    out = []
    w = out.append
    w("LEAD-026 summary (nats; Gaussian estimates)\n")
    w("== Matched and unmatched aggregate statistics ==")
    for a in arms:
        s = recs[(a, "stats")]
        w(f"{a:3s} var_member={s['var_member']:.3f} rho={s['rho_members']:.3f} "
          f"ac1={s['ac1_agg']:.3f} | ac8={s['ac8_agg']:.3f} ac32={s['ac32_agg']:.3f} "
          f"var_agg={s['var_agg']:.3f}  params={ {k: round(v, 3) for k, v in s['params'].items()} }")
    w("\n== Priced lagged block: passing candidates by window W ==")
    for obs in ("all", "hidden"):
        w(f"-- observed set: {'all eight' if obs == 'all' else 'e hidden'}")
        for a in arms:
            rows = sorted([r for (aa, it), r in recs.items() if aa == a and it.startswith(f"block:{obs}:")],
                          key=lambda r: r["W"])
            for r in rows:
                w(f"{a:3s} W={r['W']:2d} pass: {' '.join(r['passing'])}")
    w("\n== Block ln BF for key candidates (internal min-cut keep; edge keep) ==")
    for obs in ("all", "hidden"):
        for a in arms:
            rows = sorted([r for (aa, it), r in recs.items() if aa == a and it.startswith(f"block:{obs}:")],
                          key=lambda r: r["W"])
            for r in rows:
                parts = [f"{k}: int={v['internal']:.0f} edge={v['edge']:.0f} (in {v['edge_in']:.0f}, out {v['edge_out']:.0f})"
                         for k, v in r["key"].items()]
                w(f"{obs:6s} {a:3s} W={r['W']:2d} " + " | ".join(parts))
    for a in arms:
        if (a, "profile") not in recs:
            continue
        p = recs[(a, "profile")]
        ah = {r["label"]: r["ahat"] for r in recs[(a, "ahat")]["rows"]} if (a, "ahat") in recs else {}
        w(f"\n== Arm {a}: profile by candidate class (E = the rest) ==")
        w("cand      " + " ".join(f"A*{D:<5}" for D in p["lags"]) + " | " +
          " ".join(f"A{D:<6}" for D in p["lags"]) + " | " + " ".join(f"nC{D:<5}" for D in (1, 16, 64)) +
          " | TE1   TE16  | " + " ".join(f"Ah{D:<5}" for D in p["lags"]))
        for r in p["rows"]:
            k = r["krakauer"]
            line = f"{r['label']:9s} " + " ".join(f"{k[str(D)]['Astar']:6.3f}" for D in p["lags"]) + " | "
            line += " ".join(f"{k[str(D)]['A']:6.3f}" for D in p["lags"]) + " | "
            line += " ".join(f"{k[str(D)]['nC']:6.3f}" for D in (1, 16, 64)) + " | "
            line += f"{r['te']['1']:.3f} {r['te']['16']:.3f} | "
            if r["label"] in ah:
                line += " ".join(f"{ah[r['label']][str(D)]:6.3f}" for D in p["lags"])
            w(line)
        w(f"-- arm {a}, e hidden from E: A(D) and TE16")
        for r in p["rows"]:
            if "e" in r["label"]:
                continue
            k = r["krakauer_e_hidden"]
            w(f"{r['label']:9s} " + " ".join(f"{k[str(D)]['A']:6.3f}" for D in p["lags"]) +
              f" | TE16 {r['te_e_hidden']['16']:.3f}")
    w("\n== Key table: lags 1, 8, 16, 32, 64 ==")
    for a in arms:
        if (a, "ahat") not in recs:
            continue
        p = {r["label"]: r for r in recs[(a, "profile")]["rows"]}
        ah = {r["label"]: r["ahat"] for r in recs[(a, "ahat")]["rows"]}
        Ls = ("1", "8", "16", "32", "64")
        w(a)
        for lab in ["1m", "6m", "6m+e", "6m+e+z", "0m+e"]:
            k, kh = p[lab]["krakauer"], p[lab]["krakauer_e_hidden"]
            line = (f"  {lab:7s} A* " + " ".join(f"{k[D]['Astar']:.3f}" for D in Ls) +
                    " | A " + " ".join(f"{k[D]['A']:.3f}" for D in Ls) +
                    " | Ahat " + " ".join(f"{ah[lab][D]:.3f}" for D in Ls) +
                    f" | nC1 {k['1']['nC']:.3f} TE1 {p[lab]['te']['1']:.3f} TE16 {p[lab]['te']['16']:.3f}")
            if "e" not in lab:
                line += (" | e hidden: A " + " ".join(f"{kh[D]['A']:.3f}" for D in Ls) +
                         f" TE16 {p[lab]['te_e_hidden']['16']:.3f}")
            w(line)
        for W in (1, 4, 6, 8, 16):
            k = recs[(a, f"block:all:{W}")]["key"]
            m, me = k["{x0,x1,x2,x3,x4,x5}"], k["{x0,x1,x2,x3,x4,x5,e}"]
            w(f"   W={W:2d} members: internal {m['internal']:.0f}, edge in {m['edge_in']:.0f} out {m['edge_out']:.0f}"
              f" | members+e: internal {me['internal']:.0f}, edge {me['edge']:.0f}")
    with open(os.path.join(HERE, "summary.txt"), "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
