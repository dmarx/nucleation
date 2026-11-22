"""Apply the LEAD-041 procedure to the FOMC's policy-rate record, 1966-2026.

Perspectives: the dual mandate's two channels, each ranking the options
{cut, hold, hike} from what was known at the time (the Philadelphia Fed's
real-time vintages), never from the decisions.

- inflation channel: 12-month CPI inflation against a reference pi*;
  above pi* + b it ranks hike > hold > cut, below pi* - b the reverse,
  otherwise indifferent.
- employment channel: the unemployment rate against u*; above u* + b it
  ranks cut > hold > hike, below u* - b the reverse, otherwise indifferent.

Decision in quarter q: the change in the monthly effective federal funds
rate (H.15, RIFSPFF_N.M) from the last month of q-1 to the last month of q:
hike above +0.25, cut below -0.25, else hold. Where the rate stood below
0.25 at the end of q-1, cut is not available (context "zlb").

CPI real-time vintages begin in 1994Q3; earlier quarters use the 1994Q3
vintage cut at the information date.

Specifications (the choices are the assistant's; see README):
  A  pi* = 2, u* = trailing 10-year mean of u in the vintage
  B  pi* = trailing 10-year mean of inflation, u* as A
  C  pi* = 2, employment channel from the 12-month change in u (b = 0.5)

Decisions are read two ways: "nominal", the change in the funds rate the
FOMC sets, and "real", the change in the funds rate less 12-month
inflation as known at the time (a stance reading: a nominal cut smaller
than inflation's fall is a tightening).

Usage: python3 -I fomc.py <download-dir> <out-dir>
"""
import json
import os
import sys
import xml.etree.ElementTree as ET
from collections import OrderedDict

import numpy as np
import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import procedure as P  # noqa: E402

B = 0.5
STEP = 0.25
TIGHTEN = {"hike": 2, "hold": 1, "cut": 0}
EASE = {"cut": 2, "hold": 1, "hike": 0}
FLAT = {"cut": 0, "hold": 0, "hike": 0}
NAMED = OrderedDict([
    ("inflation", [("hike", "hold", "cut")]),
    ("employment", [("cut", "hold", "hike")]),
    ("inertia", [("hold", "hike", "cut"), ("hold", "cut", "hike")]),
])
CHAIRS = [("Martin", "1966Q1", "1970Q1"), ("Burns", "1970Q2", "1978Q1"),
          ("Miller", "1978Q2", "1979Q2"), ("Volcker", "1979Q3", "1987Q2"),
          ("Greenspan", "1987Q3", "2005Q4"), ("Bernanke", "2006Q1", "2013Q4"),
          ("Yellen", "2014Q1", "2017Q4"), ("Powell", "2018Q1", "2026Q3")]


def read_vintages(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    rows = list(wb.worksheets[0].iter_rows(values_only=True))
    head = rows[0]
    dates = [r[0] for r in rows[1:]]
    out = {}
    for j, name in enumerate(head[1:], start=1):
        vals = [(d, r[j]) for d, r in zip(dates, rows[1:])
                if isinstance(r[j], (int, float))]
        q = f"{1900 + int(name[3:5]) if int(name[3:5]) > 40 else 2000 + int(name[3:5])}Q{name[-1]}"
        out[q] = vals
    return out


def read_ffr(path):
    out = {}
    in_s = False
    for ev, el in ET.iterparse(path, events=("start", "end")):
        tag = el.tag.rsplit("}", 1)[-1]
        if ev == "start" and tag == "Series":
            in_s = el.get("SERIES_NAME") == "RIFSPFF_N.M"
        elif ev == "end" and tag == "Obs" and in_s:
            try:
                out[el.get("TIME_PERIOD")[:7]] = float(el.get("OBS_VALUE"))
            except (TypeError, ValueError):
                pass
        elif ev == "end" and tag == "Series":
            in_s = False
            el.clear()
    return out


def quarters(a, b):
    y, q = int(a[:4]), int(a[-1])
    while f"{y}Q{q}" <= b:
        yield f"{y}Q{q}"
        q += 1
        if q == 5:
            y, q = y + 1, 1


def qprev(q):
    y, n = int(q[:4]), int(q[-1])
    return f"{y}Q{n - 1}" if n > 1 else f"{y - 1}Q4"


def qlast_month(q):
    return f"{q[:4]}-{int(q[-1]) * 3:02d}"


def channel_states(uv, cv, spec):
    u = np.array([v for _, v in uv])
    c = np.array([v for _, v in cv])
    infl = 100 * (c[12:] / c[:-12] - 1)
    pi = infl[-1]
    pistar = 2.0 if spec in ("A", "C") else float(np.mean(infl[-120:]))
    if spec == "C":
        ugap = u[-1] - u[-13]
    else:
        ugap = u[-1] - float(np.mean(u[-120:]))
    return pi, pistar, u[-1], ugap


def build(dl, spec, mode="nominal"):
    uv = read_vintages(os.path.join(dl, "philly", "rucQvMd.xlsx"))
    cv = read_vintages(os.path.join(dl, "philly", "cpiQvMd.xlsx"))
    ffr = read_ffr(os.path.join(dl, "h15", "H15_data.xml"))
    eps, info = [], []
    prev_pi = None
    for t, q in enumerate(quarters("1966Q1", "2026Q3")):
        if q not in uv or not uv[q]:
            continue
        # CPI vintages start in 1994Q3. Before that, use the 1994Q3 vintage
        # cut at the unemployment vintage's last month (the information date);
        # CPI is barely revised, so this is near real time (README).
        last = uv[q][-1][0]
        cq = cv[q] if cv.get(q) else [(d, v) for d, v in cv["1994Q3"] if d <= last]
        if not cq:
            continue
        m0, m1 = qlast_month(qprev(q)), qlast_month(q)
        if m0 not in ffr or m1 not in ffr:
            continue
        pi, pistar, u, ugap = channel_states(uv[q], cq, spec)
        rin = TIGHTEN if pi > pistar + B else EASE if pi < pistar - B else FLAT
        remp = EASE if ugap > B else TIGHTEN if ugap < -B else FLAT
        d = ffr[m1] - ffr[m0]
        if mode == "real":
            if prev_pi is None:
                prev_pi = pi
                continue
            d = (ffr[m1] - pi) - (ffr[m0] - prev_pi)
        prev_pi = pi
        dec = "hike" if d > STEP else "cut" if d < -STEP else "hold"
        zlb = ffr[m0] < 0.25
        opts = ("hike", "hold") if zlb else ("cut", "hike", "hold")
        if dec not in opts:
            dec = "hold"
        win = f"{q[:4] if int(q[:4]) % 2 == 0 else int(q[:4]) - 1}-{(int(q[:4]) if int(q[:4]) % 2 == 0 else int(q[:4]) - 1) + 1}"
        e = P.Episode(t, win, opts, {"inflation": {o: rin[o] for o in opts},
                                     "employment": {o: remp[o] for o in opts}},
                      dec, "zlb" if zlb else "normal")
        eps.append(e)
        info.append({"q": q, "window": win, "pi": round(float(pi), 2),
                     "pistar": round(float(pistar), 2), "u": float(u),
                     "ugap": round(float(ugap), 2), "ffr_prev": ffr[m0], "ffr": ffr[m1],
                     "decision": dec, "contested": P.is_contested(e),
                     "context": e.context})
    return eps, info


def chair_of(q):
    for n, a, b in CHAIRS:
        if a <= q <= b:
            return n
    return None


def progress_fn(info_by_t):
    def prog(name, eps):
        rows = [info_by_t[e.t] for e in eps]
        if name == "inflation":
            g = [abs(r["pi"] - r["pistar"]) for r in rows]
        elif name == "employment":
            g = [abs(r["ugap"]) for r in rows]
        else:
            return None
        years = max(len(rows) / 4, 0.25)
        return -(g[-1] - g[0]) / years  # gap closed per year
    return prog


def run(dl, out, spec, window_key="window", seed=0, mode="nominal"):
    rng = np.random.default_rng(seed)
    eps, info = build(dl, spec, mode)
    by_t = {e.t: r for e, r in zip(eps, info)}
    if window_key == "chair":
        for e, r in zip(eps, info):
            e.window = chair_of(r["q"])
            r["window"] = e.window
    elif window_key == "w4":
        for e, r in zip(eps, info):
            y0 = 1966 + 4 * ((int(r["q"][:4]) - 1966) // 4)
            e.window = f"{y0}-{y0 + 3}"
            r["window"] = e.window
    windows = list(OrderedDict.fromkeys(e.window for e in eps))
    eps_rate = P.departure_rate(eps)
    profile = P.departure_profile(eps)
    prog = progress_fn(by_t)
    # first pass, unsigned, to fix the reference course: each channel's
    # mean rate of gap closing over the windows it leads
    first = [P.analyse_window(w, [e for e in eps if e.window == w], NAMED, profile,
                              rng, n_sim=1000) for w in windows]
    ref = {}
    for n in ("inflation", "employment"):
        v = [prog(n, [e for e in eps if e.window == r.window]) for r in first
             if r.verdict == "prevails" and r.leading == n]
        ref[n] = float(np.mean(v)) if v else None
    res = []
    for w in windows:
        we = [e for e in eps if e.window == w]
        r0 = next(r for r in first if r.window == w)
        r = P.analyse_window(w, we, NAMED, profile, np.random.default_rng(seed), n_sim=1000,
                             progress=prog, reference=ref.get(r0.leading), tol=0.25)
        res.append(r)
    seq = [(r.window, r.leading if r.verdict == "prevails" else
            ("ambivalent" if r.verdict == "ambivalent" else None)) for r in res]
    pr = {n: P.persistence_and_resumption(seq, n) for n in NAMED}
    alt = P.alternation_test(eps, windows, NAMED, np.random.default_rng(seed + 1), n_perm=500)
    summary = {
        "spec": spec, "decision": mode, "windows": window_key, "n_quarters": len(eps),
        "n_contested": sum(P.is_contested(e) for e in eps),
        "departure_rate_uncontested": eps_rate, "departure_profile": profile, "reference_course": ref,
        "alternation": alt, "persistence_resumption": pr,
        "per_window": [{
            "window": r.window, "quarters": r.n_episodes, "contested": r.n_contested,
            "wins": r.n_wins, "reversal": None if np.isnan(r.reversal) else round(r.reversal, 3),
            "p_ambivalence": None if np.isnan(r.p_ambivalence) else round(r.p_ambivalence, 3),
            "alignment": {k: round(v, 3) for k, v in r.candidate_alignment.items()},
            "p_lead": None if np.isnan(r.p_lead) else round(r.p_lead, 3),
            "best_class": [" > ".join(o) for o in r.best_class],
            "by_context": {k: [" > ".join(o) for o in v] for k, v in r.by_context.items()},
            "verdict": r.verdict, "leading": r.leading, "sign": r.sign} for r in res],
    }
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, f"results_{spec}_{mode}_{window_key}.json"), "w") as f:
        json.dump(summary, f, indent=1)
    if spec == "A" and window_key == "window":
        with open(os.path.join(out, f"quarters_A_{mode}.json"), "w") as f:
            json.dump(info, f, indent=0)
    return summary


if __name__ == "__main__":
    dl, out = sys.argv[1], sys.argv[2]
    for mode in ("nominal", "real"):
      for spec in ("A", "B", "C"):
        for wk in ("window", "w4", "chair"):
            s = run(dl, out, spec, wk, mode=mode)
            print(mode, spec, wk, s["n_quarters"], s["n_contested"],
                  round(s["departure_rate_uncontested"], 3), s["alternation"])
            for r in s["per_window"]:
                if r["contested"] >= 4:
                    print("  ", r["window"], r["contested"], r["verdict"], r["leading"],
                          r["sign"], r["reversal"], r["p_ambivalence"], r["p_lead"], r["alignment"])
