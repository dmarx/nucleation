# scratch/formal/foschi_eq4_search.py: which index assignment of Foschi, Hull & Ku's Eq. (4) (opposite folding angles) and of (A6) holds on independently built degree-4 states; also tests (A3).
"""
Eq. (4) as printed is  tan^2(rho_i/2) = -N/D,
 N = (1+T) cos(a_{i-1}+a_i) + T cos(a_{i+1}-a_{i+2}) + cos(a_{i+1}+a_{i+2}),
 D = (1+T) cos(a_{i-1}-a_i) - T cos(a_{i+1}-a_{i+2}) - cos(a_{i+1}+a_{i+2}),
 T = tan^2(rho_{i+2}/2).
Every assignment of the four offsets (-1, 0, +1, +2) to the slots (A, B, C, D) in
 (1+T) cos(A+B), T cos(C-D), cos(C+D)
is tried; the printed one is (A,B,C,D) = (-1, 0, +1, +2).  The same is done for
(A6) by permuting which of the three mixed cosines goes on x^2, y^2, x^2 y^2.
Control: the printed Eq. (5) must pass and a perturbed alpha must fail.
Run:  python3 -I foschi_eq4_search.py
"""
import math, itertools, sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import foschi_deg4_check as F
C, S, T = math.cos, math.sin, F.T
F.rng = random.Random(5)
data = []
for kind in ("dev", "ell", "hyp"):
    for _ in range(15):
        al = F.rand_alpha(kind)
        for rho in F.sample(al, 30):
            data.append((kind, al, rho))
print("states:", len(data))

def eq4_general(al, rho, i, perm):
    a = lambda k: al[(i + k) % 4]
    A, B, Cc, D = (a(k) for k in perm)
    t2 = T(rho[(i + 2) % 4]) ** 2
    num = (1 + t2) * C(A + B) + t2 * C(Cc - D) + C(Cc + D)
    den = (1 + t2) * C(A - B) - t2 * C(Cc - D) - C(Cc + D)
    return (T(rho[i]) ** 2 * den + num) / (1 + T(rho[i]) ** 2) / (1 + t2)

res = []
for perm in itertools.permutations((-1, 0, 1, 2)):
    worst = {k: 0.0 for k in ("dev", "ell", "hyp")}
    for kind, al, rho in data:
        worst[kind] = max(worst[kind], max(abs(eq4_general(al, rho, i, perm)) for i in range(4)))
    res.append((max(worst.values()), perm, worst))
res.sort()
for w, perm, wk in res[:6]:
    tag = "  <- printed" if perm == (-1, 0, 1, 2) else ""
    print("Eq.(4) slots (A,B,C,D) offsets %s: max resid dev %.2e ell %.2e hyp %.2e%s" % (perm, wk["dev"], wk["ell"], wk["hyp"], tag))
printed = [r for r in res if r[1] == (-1, 0, 1, 2)][0]
print("printed Eq.(4): max resid dev %.2e ell %.2e hyp %.2e" % (printed[2]["dev"], printed[2]["ell"], printed[2]["hyp"]))

# (A6) permutations
def a6(al, rho, order):
    a1, a2, a3, a4 = al
    x, y = T(rho[3]), T(rho[0])
    m = [C(a1 - a3 - a4), C(a1 + a3 - a4), C(a1 - a3 + a4)]
    cx, cxy, cy = (m[k] for k in order)
    r = C(a1 + a3 + a4) + x*x*cx + x*x*y*y*cxy + y*y*cy + 4*x*y*S(a1)*S(a3) - (1+x*x)*(1+y*y)*C(a2)
    return r / (1 + x*x) / (1 + y*y)
for order in itertools.permutations((0, 1, 2)):
    w = max(abs(a6(al, rho, order)) for _, al, rho in data)
    names = ["cos(a1-a3-a4)", "cos(a1+a3-a4)", "cos(a1-a3+a4)"]
    print("(A6) x^2:%s x^2y^2:%s y^2:%s  max resid %.2e%s" % (names[order[0]], names[order[1]], names[order[2]], w, "  <- printed" if order == (0, 1, 2) else ""))

# (A3) cos rho2 = cot a1 cot a2 + (sin a2 sin a4 cos t - cos a3 cos a4)/(sin a1 sin a2), t = rho4
w3 = 0
for _, al, rho in data:
    a1, a2, a3, a4 = al
    w3 = max(w3, abs(C(rho[1]) - (1/math.tan(a1)/math.tan(a2) + (S(a2)*S(a4)*C(rho[3]) - C(a3)*C(a4))/(S(a1)*S(a2)))))
print("(A3) as printed: max resid %.2e" % w3)
# a symmetric candidate from the spherical cosine rule on the diagonal c1-c3 ... (diagonal c2-c4):
# cos d = cos a1 cos a2 + sin a1 sin a2 cos(pi - rho2) = cos a3 cos a4 + sin a3 sin a4 cos(pi - rho4)
w3b = 0
for _, al, rho in data:
    a1, a2, a3, a4 = al
    w3b = max(w3b, abs((C(a1)*C(a2) - S(a1)*S(a2)*C(rho[1])) - (C(a3)*C(a4) - S(a3)*S(a4)*C(rho[3]))))
print("diagonal cosine rule cos a1 cos a2 - sin a1 sin a2 cos rho2 = cos a3 cos a4 - sin a3 sin a4 cos rho4: max resid %.2e" % w3b)

print("\n-- Eq.(4) with the numerator's last two signs flipped (derived from the cosine rule on the diagonal)")
def eq4_corr(al, rho, i, printed=False, supp=False):
    a = lambda k: al[(i + k) % 4]
    r = [ (math.pi - abs(x)) * (1 if x >= 0 else -1) for x in rho] if supp else rho
    t2 = T(r[(i + 2) % 4]) ** 2
    s = 1 if printed else -1
    num = (1 + t2) * C(a(-1) + a(0)) + s * t2 * C(a(1) - a(2)) + s * C(a(1) + a(2))
    den = (1 + t2) * C(a(-1) - a(0)) - t2 * C(a(1) - a(2)) - C(a(1) + a(2))
    return (T(r[i]) ** 2 * den + num) / (1 + T(r[i]) ** 2) / (1 + t2)
for kind in ("dev", "ell", "hyp"):
    sub = [(al, rho) for k, al, rho in data if k == kind]
    wc = max(abs(eq4_corr(al, rho, i)) for al, rho in sub for i in range(4))
    wp = max(abs(eq4_corr(al, rho, i, printed=True)) for al, rho in sub for i in range(4))
    ws = max(abs(eq4_corr(al, rho, i, printed=True, supp=True)) for al, rho in sub for i in range(4))
    print("   %s: corrected %.2e ; printed %.2e ; printed with rho -> pi-|rho| (interior-angle reading) %.2e" % (kind, wc, wp, ws))
# table vertex: corrected Eq.(4), i=2, should reduce to Eq.(10)
al = [5*math.pi/8, 5*math.pi/8, math.pi/2, 3*math.pi/4]
for r4 in (-2.0, -0.7, 0.4, 1.9):
    t2 = T(r4)**2
    a1, a2, a3, a4 = al
    for s, lab in ((-1, "corrected"), (1, "printed")):
        num = (1+t2)*C(a1+a2) + s*t2*C(a3-a4) + s*C(a3+a4)
        den = (1+t2)*C(a1-a2) - t2*C(a3-a4) - C(a3+a4)
        lhs = -num/den
        rhs = 2*math.sqrt(2)/(2+math.sqrt(2)*C(r4))*S(r4/2)**2
        print("   table, rho4=%+.1f: %-9s Eq.(4) gives tan^2(rho2/2)=%.6f ; Eq.(10) gives %.6f" % (r4, lab, lhs, rhs))
# (A3) corrected: sin a3 sin a4 in place of sin a2 sin a4
w = max(abs(C(rho[1]) - (1/math.tan(al[0])/math.tan(al[1]) + (S(al[2])*S(al[3])*C(rho[3]) - C(al[2])*C(al[3]))/(S(al[0])*S(al[1])))) for _, al, rho in data)
print("(A3) with sin a3 sin a4 for sin a2 sin a4: max resid %.2e" % w)

print("\n-- Appendix B's first display (B1), developable states only: does it follow from the printed or the corrected Eq.(4)?")
wb = 0
for kind, al, rho in data:
    if kind != "dev":
        continue
    for i in range(4):
        a = lambda k: al[(i + k) % 4]
        t2 = T(rho[(i + 2) % 4]) ** 2
        rhs = 2 * S(a(1)) * S(a(-1) + a(0) + a(1)) * t2 / (C(a(-1) + a(0)) - C(a(-1) - a(0)) + (C(a(-1) + a(0) + 2 * a(1)) - C(a(-1) - a(0))) * t2)
        wb = max(wb, abs(math.atan(T(rho[i]) ** 2) - math.atan(rhs)))
print("   (B1) max |atan(lhs) - atan(rhs)| over developable states: %.2e" % wb)
