"""Tables from exact.jsonl and mc.jsonl. Rerun: python3 -I summarize.py > summary.md"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name)) as f:
        return [json.loads(l) for l in f]


def main():
    ex = load("exact.jsonl")
    print("## Per content, exact (n = m occurrences a context; Delta units, max 2)\n")
    print("| p | p' | true | n | plug-in mean | root-U2 mean | plug RMSE | root RMSE | CP coverage (k=2 level) | Newcombe coverage (k=2 level, nominal 0.975) | Fisher reject at 2.5% |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in ex:
        rm = f"{r['root_mean']:.3f}" if "root_mean" in r else "—"
        rr = f"{r['root_rmse']:.3f}" if "root_rmse" in r else "—"
        print(f"| {r['p']} | {r['q']} | {r['true']:.1f} | {r['n']} | {r['plug_mean']:.3f} | {rm} | {r['plug_rmse']:.3f} | {rr} | {r['cov_cp_k2']:.3f} | {r['cov_newc_k2']:.3f} | {r['fisher_rej_k2']:.3f} |")
    print(f"\nMinimum exact CP coverage over all cells: {min(r['cov_cp_k2'] for r in ex):.4f}; "
          f"minimum Newcombe: {min(r['cov_newc_k2'] for r in ex):.4f}.\n")
    mc = load("mc.jsonl")
    print("## Whole rank-2 systems, Monte Carlo (4,000 replications; MC s.e. of a rate near 0.95 is about 0.0035)\n")
    print("| model | true Delta | n | plug-in mean | root-U2 mean | plug RMSE | root RMSE | box coverage (95%) | Newcombe coverage (95%) | reject no-signalling (5%) | box lower bound >= 2 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in mc:
        print(f"| {r['model']} | {r['true']:.2f} | {r['n']} | {r['plug_mean']:.3f} | {r['root_mean']:.3f} | {r['plug_rmse']:.3f} | {r['root_rmse']:.3f} | {r['cov_box']:.4f} | {r['cov_newcombe']:.4f} | {r['reject_nosig']:.4f} | {r['box_lower_ge_2']:.4f} |")
    print(f"\nMinimum box coverage: {min(r['cov_box'] for r in mc):.4f}; minimum Newcombe: {min(r['cov_newcombe'] for r in mc):.4f}; "
          f"largest rejection rate under the two null models: {max(r['reject_nosig'] for r in mc if r['model'].startswith('null')):.4f}.")


if __name__ == "__main__":
    main()
