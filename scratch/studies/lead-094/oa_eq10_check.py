# scratch/studies/lead-094/oa_eq10_check.py
# Re-check of Ott-Antonsen eq. 10 for THEORY-tmpmvcnr: large Kuramoto population,
# Lorentzian frequencies (width 1), started on the OA manifold (wrapped Cauchy, |Z0|=a0),
# against rho' = -(1-K/2) rho - (K/2) rho^3. Control: Gaussian frequencies (same half-width), should not match.
import numpy as np
N=200000; a0=0.3; dt=0.005; T=12.0
q=(np.arange(N)+0.5)/N
rng=np.random.default_rng(0)
def wrapped_cauchy(n,r):
    # theta = angle of a Cauchy-distributed point mapped; use inverse: theta = 2 atan(((1-r)/(1+r)) tan(pi(u-1/2)))
    u=rng.random(n); return 2*np.arctan((1-r)/(1+r)*np.tan(np.pi*(u-0.5)))
def run(omega,K):
    th=wrapped_cauchy(N,a0); out=[]
    for i in range(int(T/dt)+1):
        Z=np.exp(1j*th).mean()
        if i%400==0: out.append(abs(Z))
        f=lambda t: omega+K*np.imag(Z*np.exp(-1j*t))
        # RK2 with Z frozen per step is O(dt); recompute Z at midpoint
        k1=f(th); thm=th+0.5*dt*k1; Zm=np.exp(1j*thm).mean()
        th=th+dt*(omega+K*np.imag(Zm*np.exp(-1j*thm)))
    return np.array(out)
def ode(K):
    r=a0; out=[]
    for i in range(int(T/dt)+1):
        if i%400==0: out.append(r)
        g=lambda r: -(1-K/2)*r-(K/2)*r**3
        r=r+dt*g(r+0.5*dt*g(r))
    return np.array(out)
lor=np.tan(np.pi*(q-0.5)); lor=np.clip(lor,-1e4,1e4)
from statistics import NormalDist
gau=np.array([NormalDist(0,1/0.6745).inv_cdf(x) for x in q])  # same quartiles as Lorentzian width 1
for K in (1.0,3.0,4.0):
    o=ode(K); l=run(lor,K); g=run(gau,K)
    print(f"K={K} ode   ",np.round(o,3))
    print(f"K={K} lor   ",np.round(l,3), "maxdev",round(float(np.max(abs(l-o))),3))
    print(f"K={K} gauss ",np.round(g,3), "maxdev",round(float(np.max(abs(g-o))),3))
