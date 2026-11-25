# independent recheck of CLAIM-tmp6nzs1, written from the claim's stated model (not the script)
import math
try:
    from scipy.integrate import solve_ivp, quad
    SC=True
except Exception:
    SC=False
lam,mu,tau=1.0,0.3,1.5; S,oR,w,H=10.0,2.0,4.0,80.0
def f(c):  # unsupported
    p=min(tau*c,1.0); return lam*p*c*(1-c)-mu*c
def traj(c0,T,n=200000):
    # fine RK4 with dense output
    h=T/n; cs=[c0]; c=c0
    for _ in range(n):
        k1=f(c);k2=f(c+h*k1/2);k3=f(c+h*k2/2);k4=f(c+h*k3);c=c+h*(k1+2*k2+2*k3+k4)/6; cs.append(c)
    return h,cs
def oP(c0,r,n=80000):
    h,cs=traj(c0,H,n)
    # trapezoid on e^{-rt} min(tau c,1)
    s=sum((math.exp(-r*i*h)*min(tau*cs[i],1)+math.exp(-r*(i+1)*h)*min(tau*cs[i+1],1))/2*h for i in range(n))
    return w*r*s/(1-math.exp(-r*H))
nash=lambda o:o+(S-o-oR)/2
cl=(1-math.sqrt(1-4*mu/(lam*tau)))/2; print("threshold",cl,"deadline",math.log(0.7/cl)/mu)
for t in (0,2,3,4,6):
    c=0.7*math.exp(-mu*t); o=oP(c,0.25); print(t,round(c,4),round(o,4),round(nash(o),4), "cur",round(nash(w*min(tau*c,1)),4))
for T in (2.0,3.0,3.5,5.0):
    c=0.7*math.exp(-mu*T); h,cs=traj(c,20,40000); o=oP(cs[-1],0.25); print("end",T,round(cs[-1],4),round(o,4))
# monotonicity of oP in c on a grid
g=[0.01*i for i in range(1,71)]; v=[oP(c,0.25,8000) for c in g]
print("oP monotone nondecreasing in c:", all(b>=a-1e-9 for a,b in zip(v,v[1:])))
# steepest fall location
ts=[0.05*i for i in range(121)]; us=[nash(oP(0.7*math.exp(-mu*t),0.25,8000)) for t in ts]
d=max(range(120),key=lambda i:us[i]-us[i+1]); print("steepest at",(ts[d]+ts[d+1])/2)
# A=0.5 fixed point check and a*
print("C* at A=.5", 1-mu/(lam*0.5), "a*",1-mu/(1-cl))
