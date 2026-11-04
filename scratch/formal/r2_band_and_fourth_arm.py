import numpy as np, math
from scipy.integrate import solve_ivp
a=0.2
def f(t,n,b):
    n=np.maximum(n,0); o=[[n[1],n[2]],[n[0],n[2]],[n[0],n[1]]]
    return [n[i]*(1-n[i]-a*sum(o[i])-b*o[i][0]*o[i][1]) for i in range(3)]
for b in [1.0,1.2,1.5,1.7,1.8]:
    rng=np.random.default_rng(0); c=0
    for k in range(200):
        s=solve_ivp(f,(0,600),rng.uniform(0.01,1.5,3),args=(b,),rtol=1e-9,atol=1e-12)
        c+= (s.y[:,-1]>1e-4).sum()==3
    print('b',b,'all three survive from',c,'/200')
rng=np.random.default_rng(2)
def vol(eps,N=6_000_000):
    P=np.column_stack([rng.uniform(-.5,.5,N),rng.uniform(.5,1.5,N),rng.uniform(.5,1.5,N)])
    K=P[:,0]**2+(P[:,1]*P[:,2]-1)**2; return (K<eps).mean()
v1,v2=vol(1e-3),vol(1e-4); print('fourth arm exponent',math.log(v1/v2)/math.log(10))
import numpy as np, math
from scipy.integrate import solve_ivp
a=0.2
def f(t,n,b):
    n=np.maximum(n,0); o=[[n[1],n[2]],[n[0],n[2]],[n[0],n[1]]]
    return [n[i]*(1-n[i]-a*sum(o[i])-b*o[i][0]*o[i][1]) for i in range(3)]
b=1.7; x=(-(1+2*a)+math.sqrt((1+2*a)**2+4*b))/(2*b)
for p in [0.001,0.01,0.03]:
    s=solve_ivp(f,(0,2000),[x+p,x-p,x],args=(b,),rtol=1e-10,atol=1e-13); print(p,s.y[:,-1])
