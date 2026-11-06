# scratch/formal/azam_stability_check.py: the twenty-fifth status review's check of THEORY-1483 (run: python3 -I scratch/formal/azam_stability_check.py)
# Numeric check of the stability claims in THEORY-1483 (Azam, Devarajan & O'Connell 1999), reviewer's own.
# Planner: max int e^{-delta t} [beta*(-r/R - r^2/2) + r] dt (spending fixed, constant terms dropped), Rdot = r - alpha R.
import math, cmath
def jac(f, x, h=1e-7):
    n=len(x); J=[[0]*n for _ in range(n)]
    for j in range(n):
        xp=list(x); xm=list(x); xp[j]+=h; xm[j]-=h
        fp=f(xp); fm=f(xm)
        for i in range(n): J[i][j]=(fp[i]-fm[i])/(2*h)
    return J
for alpha,delta,beta in ((0.1,0.05,2.0),(0.2,0.1,1.5),(0.05,0.02,3.0)):
    g=delta/(alpha+delta)
    assert 4*alpha*beta**2*g<1
    def F(x):
        R,lam=x
        r=(lam+1-beta/R)/beta
        return [r-alpha*R, (delta+alpha)*lam-beta*r/R**2]
    disc=math.sqrt(1/beta**2-4*alpha*g)
    for name,r in (("P low-aid",(1/beta+disc)/2),("M high-aid",(1/beta-disc)/2)):
        R=r/alpha; lam=beta*r+beta/R-1
        assert max(abs(v) for v in F([R,lam]))<1e-9
        (a,b),(c,d)=jac(F,[R,lam]); tr=a+d; det=a*d-b*c
        ev=[(tr+s*cmath.sqrt(tr*tr-4*det))/2 for s in (1,-1)]
        print(alpha,delta,beta,name,"r=%.4f"%r,"eig",[complex(round(e.real,4),round(e.imag,4)) for e in ev],"det=%.4g"%det)
# Myopic rule: r = max(0, 1/beta - 1/R); Rdot = r - alpha R. Steady states alpha R^2 - R/beta + 1 = 0.
alpha,beta=0.05,2.0
Rl=(1/beta-math.sqrt(1/beta**2-4*alpha))/(2*alpha); Rh=(1/beta+math.sqrt(1/beta**2-4*alpha))/(2*alpha)
def run(R,T=400,dt=0.01):
    for _ in range(int(T/dt)): R+=dt*(max(0,1/beta-1/R)-alpha*R)
    return R
print("myopic thresholds theta1=1/Rl=%.4f, stable 1/Rh=%.4f"%(1/Rl,1/Rh), "from just below Rl ->",round(run(Rl*0.99),5),"just above ->",round(run(Rl*1.01),4), "Rh",round(Rh,4))
