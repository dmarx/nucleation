import math, numpy as np
rng=np.random.default_rng(1)
for _ in range(3):
    x,d=rng.normal(size=2)
    print('L3 check', 0.5*((x+d-1)**2+(x-d+1)**2), x**2+(d-1)**2)
# RLCT numerically: volume V(eps)={K<eps} ~ c eps^lam (-log eps)^(m-1)
def vol(K,dim,eps,N=4_000_000):
    P=rng.uniform(-1,1,(N,dim)); return (K(P)<eps).mean()
for name,K,dim in [('theta^2',lambda P:P[:,0]**2,1),('a^2b^2',lambda P:(P[:,0]*P[:,1])**2,2),('x^2+(d-1)^2 near (0,1)',lambda P:P[:,0]**2+P[:,1]**2,2)]:
    e1,e2=1e-3,1e-4; v1,v2=vol(K,dim,e1),vol(K,dim,e2)
    print(name,'slope log V/log eps ~',math.log(v1/v2)/math.log(e1/e2))
for t in [0,0.25,0.5,math.log(2),1,1.5,2]: print('C t',round(t,3), round(0.5+0.5*math.exp(-t),4))
print('D lambda',0.99*math.log(0.99)+0.01*math.log(2))
for tau,s in [(0.2,0.35),(0.2,0.25),(0.3,0.35)]: print('A9',tau,s, 0.5*(1-tau)+s)
