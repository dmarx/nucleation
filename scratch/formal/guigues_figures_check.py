# scratch/formal/guigues_figures_check.py: read the plotted series of Figures 1-8 of Guigues, Kleywegt and Nascimento (arXiv:2605.05421v1) from the PDF's vector paths
# Pass 30 (status review), cluster H: check for THEORY-1412 / NOTE-1567.
# Input: SVGs of pages 22-26 (Figures 1-8) of the arXiv v1 PDF, rebuilt with poppler-utils' pdftocairo:
#   mkdir -p figs && curl -sSL -o figs/p.pdf https://arxiv.org/pdf/2605.05421v1
#   for P in 22 23 24 25 26; do pdftocairo -svg -f $P -l $P figs/p.pdf figs/pg$P.svg; done
#   python3 -I scratch/formal/guigues_figures_check.py figs
# (pass 30 used poppler pdftocairo 24.x; the SVGs are not committed.)
# Each figure is a matplotlib plot: one polyline per policy (stroke-width 1.5) and one two-point legend
# sample per policy, in the figure's own coordinate frame (one `transform` per figure). Legend samples are
# matched top-to-bottom to the legend labels as pdftotext prints them. Horizontal grid lines are matched to
# the y tick labels printed in the text. The script reports, per figure and fleet size, the lowest series
# and MP's rank and gap.
# Control that should FAIL: assigning the legend labels bottom-to-top instead of top-to-bottom must break
# the identity check (the MP series must be the one drawn solid with circle markers, colour #1f77b4 in
# Figure 1, whose legend lists MP second).
# Usage: python3 -I scratch/formal/guigues_figures_check.py <dir with pg22.svg ... pg26.svg>
import re, sys, os
from collections import defaultdict

D = sys.argv[1]
# Legend order, top to bottom, as pdftotext prints it (p.txt lines 1062-1071, 1120-1129, 1153-1162,
# 1188-1199, 1247-1256, 1281-1290, 1315-1324, 1348-1357).
LEGENDS = {
    1: "CA MP Jagtenberg Lee2014 Bandara Mayorga Lee2011 Andersson Lee2017 Carvalho",
    2: "CA Jagtenberg Lee2014 Bandara Mayorga Lee2011 Andersson Lee2017 MP Carvalho",
    3: "Lee2014 Jagtenberg Lee2017 Mayorga CA MP Bandara Andersson Lee2011 Carvalho",
    4: "Lee2014 Jagtenberg Lee2017 Mayorga CA MP Bandara Andersson Lee2011 Carvalho",
    5: "CA Jagtenberg Lee2014 Bandara Mayorga Lee2011 Andersson Lee2017 Carvalho MP",
    6: "CA MP Andersson Bandara Carvalho Jagtenberg Lee2011 Lee2014 Lee2017 Mayorga",
    7: "CA MP Andersson Bandara Carvalho Jagtenberg Lee2011 Lee2014 Lee2017 Mayorga",
    8: "CA Jagtenberg Lee2014 Bandara Mayorga Lee2011 Andersson Lee2017 Carvalho MP",
}
WHAT = {1: "cost, great-circle, rect", 2: "resp time, great-circle, rect", 3: "cost, great-circle, hex",
        4: "resp time, great-circle, hex", 5: "cost, street, rect", 6: "resp time, street, rect",
        7: "cost, street, hex", 8: "resp time, street, hex"}
# Tick step of the y axis, read from the tick labels pdftotext prints for each figure.
STEP = {1: 1000, 2: 500, 3: 2000, 4: 1000, 5: 1000, 6: 500, 7: 2000, 8: 1000}
PAGES = {22: [1], 23: [2, 3], 24: [4], 25: [5, 6], 26: [7, 8]}

pat = re.compile(r'<path fill="none" stroke-width="([\d.]+)"[^>]*?stroke="(rgb\([^)]*\))"[^>]*?d="([^"]*)"[^>]*?transform="(matrix\([^)]*\))"')

def pts(d):
    nums = re.findall(r'[ML] ([-\d.e]+) ([-\d.e]+)', d)
    return [(float(x), float(y)) for x, y in nums]

def parse(page):
    s = open(os.path.join(D, f"pg{page}.svg")).read()
    figs = defaultdict(lambda: dict(series=defaultdict(list), legend=[], hgrid=[], vgrid=[]))
    for w, col, d, tr in pat.findall(s):
        p = pts(d)
        f = figs[tr]
        if w == "1.5" and len(p) >= 5:
            f['series'][col].append(p)
        elif w == "1.5" and len(p) == 2 and abs(p[0][1] - p[1][1]) < 1e-6:
            f['legend'].append((p[0][1], col))
        elif "69.018555%" in col and len(p) == 2:
            if abs(p[0][1] - p[1][1]) < 1e-6: f['hgrid'].append(p[0][1])
            elif abs(p[0][0] - p[1][0]) < 1e-6: f['vgrid'].append(p[0][0])
    # figures in page order: top figure first (larger page y offset in transform means lower on page)
    order = sorted(figs, key=lambda t: float(t.split(',')[5].strip(' )')))
    return [figs[t] for t in order]

def run(reverse_legend=False, quiet=False):
    out = {}
    for page, fignums in PAGES.items():
        figs = [f for f in parse(page) if f['series']]
        assert len(figs) == len(fignums), (page, len(figs))
        for fn, f in zip(fignums, figs):
            labels = LEGENDS[fn].split()
            leg = sorted(f['legend'], key=lambda t: -t[0])          # top of legend first (frame y is up)
            if reverse_legend: leg = leg[::-1]
            assert len(leg) == 10 == len(labels), (fn, len(leg))
            name = {col: lab for (y, col), lab in zip(leg, labels)}
            series = {name[c]: sorted(v[0]) for c, v in f['series'].items()}
            out[fn] = (series, sorted(set(round(v, 3) for v in f['hgrid'])), sorted(set(round(v, 3) for v in f['vgrid'])), name)
    return out

res = run()
# Identity check: in Figure 1 the series labelled MP must be the #1f77b4 (12.16%, 46.67%, 70.59%) one.
def mp_colour(r):
    return [c for c, l in r[1][3].items() if l == "MP"][0]
ok_id = mp_colour(res).startswith("rgb(12.156677%")
print("identity check, Figure 1 MP colour is #1f77b4:", ok_id)
cols = {fn: {l: c for c, l in res[fn][3].items()} for fn in res}
print("colour of each policy the same in all eight figures:", all(cols[fn] == cols[1] for fn in cols))

summary = {}
for fn in range(1, 9):
    series, hg, vg, _ = res[fn]
    n = len(series["MP"])
    xs = [10 + 2 * i for i in range(11)] + ([48] if n == 12 else [])
    assert all(len(v) == n for v in series.values()), fn
    # y calibration: grid lines are evenly spaced; scale from the first two and the tick step read from text
    best_count, rows = 0, []
    for i, x in enumerate(xs):
        vals = {k: v[i][1] for k, v in series.items()}
        ranked = sorted(vals, key=vals.get)
        rk = ranked.index("MP") + 1
        best_count += rk == 1
        gap = (vals["MP"] - vals[ranked[0] if rk > 1 else ranked[1]])
        step = hg[1] - hg[0] if len(hg) > 1 else 1
        rows.append(f"{x}:{rk}" + ("" if rk == 1 else f"({ranked[0]},{gap/step*STEP[fn]:+.0f})"))
    summary[fn] = (best_count, len(xs))
    print(f"Fig {fn} [{WHAT[fn]}]: MP lowest at {best_count}/{len(xs)} sizes; size:rank -> " + "  ".join(rows))

cost = [summary[f] for f in (1, 3, 5, 7)]
print("Allocation cost, MP lowest at", sum(a for a, b in cost), "of", sum(b for a, b in cost), "fleet sizes over the four configurations")

# Control: reversed legend mapping should fail the identity check.
bad = run(reverse_legend=True)
print("control, reversed legend: identity check passes?", mp_colour(bad).startswith("rgb(12.156677%"), "(should be False)")
