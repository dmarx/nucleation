"""LEAD-199 analysis. Reads revisions.json, edges.json, population.json;
writes results.json and prints a summary."""
import json, os, sys, bisect
from collections import defaultdict, Counter
import numpy as np

D = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(f"{D}/revisions.json"))
E = json.load(open(f"{D}/edges.json"))
P = json.load(open(f"{D}/population.json"))
DAY = 86400.0
MONTH = 30.0  # days
T_END = max(r["t"] for r in R)
BULK = int(os.environ.get("BULK", "0"))  # >0: drop revisions from commits touching > BULK claims
SKIP_FIRST_DAYS = float(os.environ.get("SKIP", "0"))
rng = np.random.default_rng(199)

claims = sorted(P)
t0 = {}
for r in R:
    if r["kind"] == "created" and r["claim"] in P:
        t0[r["claim"]] = min(t0.get(r["claim"], 1e18), r["t"])
claims = [c for c in claims if c in t0]

# revision events, deduplicated on (claim, time, subject)
def events(pred):
    seen, out = set(), defaultdict(list)
    for r in R:
        if r["claim"] not in t0 or not pred(r):
            continue
        if BULK and r["n_claims_in_commit"] > BULK:
            continue
        k = (r["claim"], r["t"], r["s"])
        if k in seen:
            continue
        seen.add(k)
        out[r["claim"]].append(r["t"])
    return {c: sorted(v) for c, v in out.items()}

EV = {
    "strict": events(lambda r: r["kind"] == "substantive"),
    "lenient": events(lambda r: r["kind"] == "substantive" and r["lenient"]),
    "title": events(lambda r: r["kind"] == "substantive" and r["title_change"]),
    "status": events(lambda r: r["status_change"] and r["a"] != "github-actions[bot]"),
}

# inbound count step functions
steps = defaultdict(list)  # tgt -> [(t, src, op)]
for e in sorted(E, key=lambda e: e["t"]):
    steps[e["tgt"]].append((e["t"], e["src"], e["op"]))
def inbound_path(c):
    """list of (t, count) change points"""
    live, out = set(), []
    for t, s, op in steps.get(c, []):
        (live.add if op == 1 else live.discard)(s)
        out.append((t, len(live)))
    return out
INB = {c: inbound_path(c) for c in claims}
first_edge = {c: next((t for t, n in INB[c] if n > 0), None) for c in claims}

AGE_BINS = [0, 1, 3, 7, 14, 28, 1e9]
CATS = [(0, 0), (1, 2), (3, 5), (6, 10**6)]
def cat_of(n):
    for i, (a, b) in enumerate(CATS):
        if a <= n <= b:
            return i

def segments(c):
    """Split claim c's life into pieces of constant (age bin, inbound cat, calendar week).
    Yields (start_t, end_t, agebin, cat, week)."""
    s0 = t0[c] + SKIP_FIRST_DAYS * DAY
    cuts = {s0, T_END}
    for b in AGE_BINS[1:-1]:
        cuts.add(t0[c] + b * DAY)
    for t, n in INB[c]:
        cuts.add(t)
    w0 = min(t0.values())
    k = 1
    while w0 + 7 * k * DAY < T_END:
        cuts.add(w0 + 7 * k * DAY); k += 1
    cuts = sorted(x for x in cuts if s0 <= x <= T_END)
    path = INB[c]
    ts = [t for t, _ in path]
    for a, b in zip(cuts, cuts[1:]):
        if b <= a:
            continue
        i = bisect.bisect_right(ts, a) - 1   # count in force at a (ties: edge at a counts)
        n = path[i][1] if i >= 0 else 0
        age = (a - t0[c]) / DAY
        ab = bisect.bisect_right(AGE_BINS, age) - 1
        yield a, b, ab, cat_of(n), int((a - w0) // (7 * DAY))

SEG = {c: list(segments(c)) for c in claims}

def tabulate(cs, ev):
    """cells[(agebin,cat,week)] = [events, days]"""
    cells = defaultdict(lambda: [0.0, 0.0])
    for c in cs:
        evs = ev.get(c, [])
        for a, b, ab, k, w in SEG[c]:
            # events in [a, b): an event at exactly the edge time falls after it
            n = bisect.bisect_left(evs, b) - bisect.bisect_left(evs, a)
            cell = cells[(ab, k, w)]
            cell[0] += n; cell[1] += (b - a) / DAY
        # an event at exactly T_END: put in last segment
        if evs and evs[-1] >= T_END and SEG[c]:
            a, b, ab, k, w = SEG[c][-1]
            cells[(ab, k, w)][0] += sum(1 for x in evs if x >= T_END)
    return cells

def mh_rr(cells, k1, k0=0, strata=("age",)):
    """Mantel-Haenszel rate ratio of cat k1 vs k0, stratified."""
    def key(ab, w):
        return (ab if "age" in strata else 0, w if "week" in strata else 0)
    S = defaultdict(lambda: [0, 0, 0, 0])  # d1, T1, d0, T0
    for (ab, k, w), (d, T) in cells.items():
        if k == k1:
            s = S[key(ab, w)]; s[0] += d; s[1] += T
        elif k == k0:
            s = S[key(ab, w)]; s[2] += d; s[3] += T
    num = den = 0.0
    for d1, T1, d0, T0 in S.values():
        Tt = T1 + T0
        if T1 <= 0 or T0 <= 0:
            continue
        num += d1 * T0 / Tt; den += d0 * T1 / Tt
    return num / den if den > 0 else float("nan")

def crude(cells, ks):
    d = sum(v[0] for (ab, k, w), v in cells.items() if k in ks)
    T = sum(v[1] for (ab, k, w), v in cells.items() if k in ks)
    return d, T, (d / T * MONTH if T else float("nan"))

def before_after(cs, ev):
    """Within-claim: revisions before vs after first inbound edge (exposed claims)."""
    db = Tb = da = Ta = 0.0
    n = n_pos_before = 0
    for c in cs:
        e = first_edge[c]
        if e is None:
            continue
        s0 = t0[c] + SKIP_FIRST_DAYS * DAY
        if e < s0:
            e = s0
        evs = [x for x in ev.get(c, []) if x >= s0]
        n += 1
        Tb += (e - s0) / DAY; Ta += (T_END - e) / DAY
        n_pos_before += e > s0
        db += sum(1 for x in evs if x < e); da += sum(1 for x in evs if x >= e)
    return dict(n=n, n_with_before_time=n_pos_before, d_before=db, days_before=Tb,
                d_after=da, days_after=Ta,
                rate_before=db / Tb * MONTH if Tb else float("nan"),
                rate_after=da / Ta * MONTH if Ta else float("nan"))

def matched(cs, ev, W=7.0, cal=7.0):
    """Risk-set matching: each claim at its first inbound edge (age a) vs claims
    filed within +-cal days, still without inbound edges at age a; both followed
    for W days from age a (controls censored at their own first edge)."""
    csset = set(cs)
    d1 = T1 = d0 = T0 = 0.0; npairs = 0; nexp = 0
    unexposed_all = [c for c in claims]
    for i in cs:
        e = first_edge[i]
        if e is None:
            continue
        a = e - t0[i]
        if e >= T_END:
            continue
        ctrls = []
        for j in unexposed_all:
            if j == i or abs(t0[j] - t0[i]) > cal * DAY:
                continue
            sj = t0[j] + a
            if sj >= T_END:
                continue
            fj = first_edge[j]
            if fj is not None and fj <= sj:
                continue
            ctrls.append(j)
        if not ctrls:
            continue
        nexp += 1
        end = min(e + W * DAY, T_END)
        evs = ev.get(i, [])
        d1 += sum(1 for x in evs if e <= x < end); T1 += (end - e) / DAY
        wd = wT = 0.0
        for j in ctrls:
            sj = t0[j] + a
            ej = min(sj + W * DAY, T_END, first_edge[j] if first_edge[j] else 1e18)
            wd += sum(1 for x in ev.get(j, []) if sj <= x < ej); wT += (ej - sj) / DAY
        # weight controls of one exposed claim to that claim's follow-up
        if wT > 0:
            d0 += wd * ((end - e) / DAY) / wT * 1.0
            T0 += (end - e) / DAY
        npairs += len(ctrls)
    return dict(n_exposed_matched=nexp, n_control_sets=npairs,
                rate_exposed=d1 / T1 * MONTH if T1 else float("nan"),
                rate_controls=d0 / T0 * MONTH if T0 else float("nan"),
                ratio=(d1 / T1) / (d0 / T0) if T0 and d0 else float("nan"))

def summarize(cs, ev):
    cells = tabulate(cs, ev)
    out = {"crude": {}, "mh_age": {}, "mh_age_week": {}}
    for k, (a, b) in enumerate(CATS):
        out["crude"][f"{a}-{b}"] = crude(cells, [k])
    for k in (1, 2, 3):
        out["mh_age"][f"{CATS[k]}"] = mh_rr(cells, k)
        out["mh_age_week"][f"{CATS[k]}"] = mh_rr(cells, k, strata=("age", "week"))
    # any inbound vs none, pooled
    cells_any = defaultdict(lambda: [0.0, 0.0])
    for (ab, k, w), v in cells.items():
        kk = 1 if k > 0 else 0
        cells_any[(ab, kk, w)][0] += v[0]; cells_any[(ab, kk, w)][1] += v[1]
    out["mh_age"]["any"] = mh_rr(cells_any, 1)
    out["mh_age_week"]["any"] = mh_rr(cells_any, 1, strata=("age", "week"))
    # age-specific rates by category
    out["by_age"] = {}
    for ab in range(len(AGE_BINS) - 1):
        row = {}
        for k in range(len(CATS)):
            d = sum(v[0] for (a2, k2, w), v in cells.items() if a2 == ab and k2 == k)
            T = sum(v[1] for (a2, k2, w), v in cells.items() if a2 == ab and k2 == k)
            row[k] = (d, round(T, 1), round(d / T * MONTH, 2) if T > 0.5 else None)
        out["by_age"][f"{AGE_BINS[ab]}-{AGE_BINS[ab+1]}d"] = row
    out["before_after"] = before_after(cs, ev)
    out["matched"] = matched(cs, ev)
    return out

def boot(ev, B=1000):
    keys = []
    vals = defaultdict(list)
    for b in range(B):
        cs = list(rng.choice(claims, size=len(claims), replace=True))
        cells = tabulate(cs, ev)
        cells_any = defaultdict(lambda: [0.0, 0.0])
        for (ab, k, w), v in cells.items():
            kk = 1 if k > 0 else 0
            cells_any[(ab, kk, w)][0] += v[0]; cells_any[(ab, kk, w)][1] += v[1]
        vals["mh_any"].append(mh_rr(cells_any, 1))
        vals["mh_any_week"].append(mh_rr(cells_any, 1, strata=("age", "week")))
        for k in (1, 2, 3):
            vals[f"mh_{CATS[k]}"].append(mh_rr(cells, k))
        ba = before_after(cs, ev)
        vals["after/before"].append(ba["rate_after"] / ba["rate_before"] if ba["rate_before"] else np.nan)
        if b < 200:
            m = matched(cs, ev)
            vals["matched_ratio"].append(m["ratio"])
    return {k: [float(np.nanpercentile(v, 2.5)), float(np.nanpercentile(v, 97.5))] for k, v in vals.items()}

if __name__ == "__main__":
    B = int(os.environ.get("B", "1000"))
    res = {"T_start": min(t0.values()), "T_end": T_END, "n_claims": len(claims),
           "n_exposed": sum(1 for c in claims if first_edge[c] is not None),
           "n_exposed_at_filing": sum(1 for c in claims if first_edge[c] is not None and first_edge[c] <= t0[c]),
           "events": {k: sum(len(v) for v in ev.values()) for k, ev in EV.items()},
           "settings": {"BULK": BULK, "SKIP": SKIP_FIRST_DAYS}}
    for name in ("strict", "lenient", "title", "status"):
        res[name] = summarize(claims, EV[name])
        if B:
            res[name]["boot95"] = boot(EV[name], B=B if name != "status" else max(B // 4, 50))
        print(name, "done", file=sys.stderr)
    tag = os.environ.get("TAG", "main")
    json.dump(res, open(f"{D}/results_{tag}.json", "w"), indent=1, default=str)
    print(json.dumps(res, indent=1, default=str))
