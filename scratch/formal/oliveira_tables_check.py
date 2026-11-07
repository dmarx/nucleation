# scratch/formal/oliveira_tables_check.py: arithmetic of de Oliveira, de Sa and Martins (arXiv:2012.06655v1), Tables 2-3 and Sec. 5.5, against the abstract's and conclusion's figures
# Pass 30 (status review), cluster H: check for THEORY-1388 / NOTE-1621.
# Numbers are copied from Table 2 (FLEET-ICt), Table 3 (LR-MEXCLP-ICt) and Sec. 5.5 of the arXiv v1 PDF.
# Checks: (1) coverage rate = objective / 26,024 total demands (Sec. 5.2, 5.3, 5.4);
# (2) which scenario pairs give the abstract's "up to 31%/24%" and "up to 21%/15%" (percentage points);
# (3) the pure relocation effect (same base regime, one period against 24): S2->S3 and S4->S5;
# (4) Sec. 5.5: 28 -> 226 stations is "less than 1.3%"; 30 -> 179 is 2.45%; the eps = 226 Pareto point
#     against Table 2's S5 optimum, which eps = 226 admits.
# (2) also shows that every pair giving the 21 and 15 points moves from the 2019 bases to optimized bases.
# Control that should FAIL: the claim that the 21% relocation gain is the S4 -> S5 comparison (both with
# optimized bases, one period against 24).
# Usage: python3 -I scratch/formal/oliveira_tables_check.py
TOTAL = 26024
T2 = dict(st=[25, 25, 25, 28, 226], obj=[15775, 18220, 18355, 23383, 23827], tot=[60.6, 70.0, 70.5, 89.9, 91.6])
T3 = dict(st=[25, 25, 25, 27, 179], obj=[12855.6, 15011.4, 14742.1, 18607.6, 18757.2], tot=[59.0, 68.5, 68.2, 83.5, 83.6])
S = ["S1", "S2", "S3", "S4", "S5"]

def cov_check(T, name):
    out = []
    for s, o, t in zip(S, T['obj'], T['tot']):
        r = 100 * o / TOTAL
        out.append((s, round(r, 1), t, abs(r - t) < 0.06))
    print(f"(1) {name}: objective/26024 against printed total coverage:", out)
    return all(x[3] for x in out)

ok1a = cov_check(T2, "FLEET-ICt")
ok1b = cov_check(T3, "LR-MEXCLP-ICt")

def pairs(T, name, target):
    hits = []
    for i in range(5):
        for j in range(5):
            d = T['tot'][j] - T['tot'][i]
            if abs(d - target) < 0.75 and i != j:
                hits.append(f"{S[i]}->{S[j]} ({d:+.1f} pts)")
    print(f"(2) {name}: pairs giving about {target} points:", hits)
    return hits

h31 = pairs(T2, "FLEET-ICt", 31); h24 = pairs(T3, "LR-MEXCLP-ICt", 24)
h21 = pairs(T2, "FLEET-ICt", 21); h15 = pairs(T3, "LR-MEXCLP-ICt", 15)
for T, name in ((T2, "FLEET-ICt"), (T3, "LR-MEXCLP-ICt")):
    print(f"(3) {name}: relocation alone, 2019 bases S2->S3 {T['tot'][2]-T['tot'][1]:+.1f} pts; "
          f"optimized bases S4->S5 {T['tot'][4]-T['tot'][3]:+.1f} pts (stations {T['st'][3]} -> {T['st'][4]})")
inc28 = 100 * (23775 - 23476) / 23476
print(f"(4) FLEET-ICt Pareto: 28 -> 226 stations: {inc28:.2f}% (paper: 'less than 1.3%')")
print(f"    eps = 226 Pareto value 23,775 against Table 2 S5 optimum 23,827 with 226 stations: "
      f"{'INCONSISTENT (the eps-constrained optimum is below a feasible point)' if 23775 < 23827 else 'consistent'}")
print(f"    text says S1-S3 have 24 stations; Tables 2 and 3 print 25")

# Control: the 21-point relocation gain read as S4->S5 must fail.
ctrl = abs((T2['tot'][4] - T2['tot'][3]) - 21) < 0.75
print("control, 21 pts = S4->S5?", ctrl, "(should be False)")
print("SUMMARY: FLEET coverage = obj/26024:", ok1a, "| LR coverage = obj/26024:", ok1b,
      "| every pair giving 21/15 pts moves from 2019 bases (S2/S3) to optimized bases (S4/S5):",
      all(h[:2] in ("S2", "S3") and h[4:6] in ("S4", "S5") for h in h21 + h15),
      "| control fails:", not ctrl)
