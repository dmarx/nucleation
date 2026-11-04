import math, numpy as np
from scipy.integrate import solve_ivp
a=0.2
def f(t,n,b):
    n=np.maximum(n,0)
    out=[]
    for i in range(3):
        o=[n[j] for j in range(3) if j!=i]
        out.append(n[i]*(1-n[i]-a*sum(o)-b*o[0]*o[1]))
    return out
for b in [0,0.5,0.96,1.2,1.76,2,4,10]:
    x=(-(1+2*a)+math.sqrt((1+2*a)**2+4*b))/(2*b) if b else 1/(1+2*a)
    lt=x*(a+b*x-1); inv=1-2*a/(1+a)-b/(1+a)**2
    rng=np.random.default_rng(0); res=[]
    for k in range(200):
        n0=rng.uniform(0.01,1.5,3)
        s=solve_ivp(f,(0,400),n0,args=(b,),rtol=1e-9,atol=1e-12)
        nf=s.y[:,-1]; res.append(int((nf>1e-4).sum()))
    print(f"b={b}: x*={x:.4f} trans_eig={lt:+.4f} inv={inv:+.4f}  final #surviving counts:",{c:res.count(c) for c in set(res)})
print('crit stab',(1-a)*(2+a),'crit inv',1-a*a, 'inv b=4 exact', 1-2*a/(1+a)-4/(1+a)**2, -19/9)
