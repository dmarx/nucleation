"""Apply the estimators, the Delta interval and the no-signalling test to the
binary systems published with fractions in LIT-842 (Wang, Sadrzadeh,
Abramsky and Cervantes, arXiv:2107.14589v1, Figs. "prob_coachlapboxerfile",
"prob_tapboxpitchercabinet" and "prob_rank2"), transcribed from the arXiv
LaTeX source (SemSpaceVC.tex).

The paper gives relative frequencies, not occurrence counts. Each row's
count is taken as the least common denominator of its reduced fractions,
the smallest count consistent with the row; the true count is a multiple
of it. That is the assumption stated in the output; a sensitivity column
gives the multiple at which each verdict would change.

Rerun: python3 -I apply.py > apply.md
"""
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sig  # noqa: E402

# Each row: (label, first word, second word, [P(0,0), P(0,1), P(1,0), P(1,1)])
# Outcome (i, j): first word reading i, second word reading j. Reading 0 is
# coded +1 here; Delta does not depend on the coding.
SYSTEMS = {
    # rank 4 cyclic: contents coach, boxer, lap, file; contexts subject-verb
    "coach/boxer x lap/file": [
        ("coach lap", "coach", "lap", [F(2, 11), F(7, 11), F(2, 11), F(0)]),
        ("coach file", "coach", "file", [F(43, 44), F(1, 44), F(0), F(0)]),
        ("boxer lap", "boxer", "lap", [F(11, 53), F(22, 53), F(8, 53), F(12, 53)]),
        ("boxer file", "boxer", "file", [F(35, 54), F(19, 54), F(0), F(0)]),
    ],
    # rank 4 cyclic: tap, box x pitcher, cabinet. Row "tap pitcher" sums to 32/22
    # as printed and is reported, not analysed.
    "tap/box x pitcher/cabinet": [
        ("tap pitcher", "tap", "pitcher", [F(17, 22), F(15, 22), F(0), F(0)]),
        ("tap cabinet", "tap", "cabinet", [F(1, 21), F(3, 7), F(11, 21), F(0)]),
        ("box pitcher", "box", "pitcher", [F(3, 4), F(1, 4), F(0), F(0)]),
        ("box cabinet", "box", "cabinet", [F(3, 7), F(10, 21), F(2, 21), F(0)]),
    ],
    # rank 2: verb-object and subject-verb
    "adopt/boxer": [
        ("adopt boxer", "adopt", "boxer", [F(0), F(29, 30), F(1, 30), F(0)]),
        ("boxer adopts", "adopt", "boxer", [F(1, 4), F(0), F(0), F(3, 4)]),
    ],
    "throw/pitcher": [
        ("throw pitcher", "throw", "pitcher", [F(2, 5), F(0), F(1, 10), F(1, 2)]),
        ("pitcher throws", "throw", "pitcher", [F(0), F(2, 3), F(1, 3), F(0)]),
    ],
}


def lcd(fr):
    d = 1
    for f in fr:
        d = d * f.denominator // math.gcd(d, f.denominator)
    return d


def analyse(rows, mult=1):
    """Returns per-content (x, n, y, m) tuples, built from rows."""
    marg = {}  # content -> list of (count of reading 0, n)
    for label, w1, w2, pr in rows:
        n = lcd(pr) * mult
        first0 = (pr[0] + pr[1]) * n
        second0 = (pr[0] + pr[2]) * n
        assert first0.denominator == 1 and second0.denominator == 1
        marg.setdefault(w1, []).append((int(first0), n))
        marg.setdefault(w2, []).append((int(second0), n))
    cs = []
    for w, lst in marg.items():
        assert len(lst) == 2, (w, lst)
        (x, n), (y, m) = lst
        cs.append((w, (x, n, y, m)))
    return cs


def main():
    print("| system | row counts (least) | contents (x/n vs y/m) | plug-in Delta | root-U2 Delta | 95% box interval | 95% Newcombe interval | no-signalling p (Fisher, Bonferroni) | least multiple of counts for box lower bound > 0 |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name, rows in SYSTEMS.items():
        bad = [r[0] for r in rows if sum(r[3]) != 1]
        if bad:
            print(f"| {name} | rows {', '.join(bad)} do not sum to 1 as printed | | | | | | | |")
            continue
        cs = analyse(rows)
        tup = [c for _, c in cs]
        plug = sum(sig.plug(*c) for c in tup)
        root = sum(sig.root_u2(*c) for c in tup) if all(c[1] >= 2 and c[3] >= 2 for c in tup) else float("nan")
        bl, bh = sig.box_interval(tup)
        nl, nh = sig.newcombe_delta(tup)
        _, p = sig.nosig_test(tup)
        k = None
        for mult in range(1, 201):
            t2 = [c for _, c in analyse(rows, mult)]
            if sig.box_interval(t2)[0] > 0:
                k = mult
                break
        counts = ", ".join(f"{r[0]}: {lcd(r[3])}" for r in rows)
        contents = "; ".join(f"{w} {x}/{n} vs {y}/{m}" for w, (x, n, y, m) in cs)
        print(f"| {name} | {counts} | {contents} | {plug:.3f} | {root:.3f} | [{bl:.3f}, {bh:.3f}] | [{nl:.3f}, {nh:.3f}] | {p:.3g} | {k if k else '>200'} |")


if __name__ == "__main__":
    main()
