# scratch/formal/readiness_erlangc_check.py
# Pass 29 (status review), cluster E: re-check for THEORY-1416 / NOTE-1577.
# Check the tutorial's Prop. 2.1 (Halfin-Whitt): Erlang C under s = lam + beta*sqrt(lam) tends to
# g(beta) = [1 + beta*Phi(beta)/phi(beta)]^-1; controls: s = lam + lam^0.75 (-> 0) and s = lam + lam^0.25 (-> 1).
import math
def erlang_b(s, lam):
    b = 1.0
    for k in range(1, s+1): b = lam*b/(k + lam*b)
    return b
def erlang_c(s, lam):
    rho = lam/s; B = erlang_b(s, lam); return 1/(rho + (1-rho)/B)
Phi = lambda x: 0.5*(1+math.erf(x/math.sqrt(2))); phi = lambda x: math.exp(-x*x/2)/math.sqrt(2*math.pi)
g = lambda b: 1/(1 + b*Phi(b)/phi(b))
for beta in [0.5, 1.0]:
    print("beta", beta, "g", round(g(beta), 5), [round(erlang_c(math.ceil(l+beta*math.sqrt(l)), l), 4) for l in [10, 100, 1000, 10000, 100000]])
print("s=lam+lam^.75", [round(erlang_c(math.ceil(l+l**.75), l), 4) for l in [10, 100, 1000, 10000, 100000]])
print("s=lam+lam^.25", [round(erlang_c(math.ceil(l+l**.25), l), 4) for l in [10, 100, 1000, 10000, 100000]])
