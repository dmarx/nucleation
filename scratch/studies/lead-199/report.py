import json, os
D = os.path.dirname(os.path.abspath(__file__))
for tag in ("main", "skip1", "bulk20", "skip1bulk20"):
    r = json.load(open(f"{D}/results_{tag}.json"))
    print(f"##### {tag} {r['settings']} n={r['n_claims']} exposed={r['n_exposed']} at_filing={r['n_exposed_at_filing']} events={r['events']}")
    for m in ("strict", "lenient", "title", "status"):
        x = r[m]; b = x.get("boot95", {})
        f = lambda v: f"{v:.2f}"
        ci = lambda k: f"[{b[k][0]:.2f},{b[k][1]:.2f}]" if k in b else ""
        cr = "  ".join(f"{k}:{int(v[0])}/{v[1]:.0f}d={v[2]:.2f}" for k, v in x["crude"].items())
        print(f"{m:8s} crude/mo {cr}")
        print(f"         MH(age) any {f(x['mh_age']['any'])}{ci('mh_any')}  1-2 {f(x['mh_age']['(1, 2)'])}{ci('mh_(1, 2)')}"
              f"  3-5 {f(x['mh_age']['(3, 5)'])}{ci('mh_(3, 5)')}  6+ {f(x['mh_age']['(6, 1000000)'])}{ci('mh_(6, 1000000)')}"
              f" | MH(age x week) any {f(x['mh_age_week']['any'])}{ci('mh_any_week')}")
        ba = x["before_after"]; mt = x["matched"]
        print(f"         before/after: {int(ba['d_before'])}/{ba['days_before']:.0f}d={ba['rate_before']:.2f} -> "
              f"{int(ba['d_after'])}/{ba['days_after']:.0f}d={ba['rate_after']:.2f} ratio {ba['rate_after']/ba['rate_before']:.2f}{ci('after/before')}"
              f" | matched(7d) exp {mt['rate_exposed']:.2f} ctl {mt['rate_controls']:.2f} ratio {mt['ratio']:.2f}{ci('matched_ratio')} (n={mt['n_exposed_matched']})")
r = json.load(open(f"{D}/results_main.json"))
print("by age (strict), events/days=rate per 30d, cats 0 | 1-2 | 3-5 | 6+")
for k, row in r["strict"]["by_age"].items():
    print(" ", k, " | ".join(f"{int(v[0])}/{v[1]}={v[2]}" for v in row.values()))
