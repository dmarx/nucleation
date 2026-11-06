# scratch/formal/tms_critical_sizes_check.py: the twenty-ninth status review's second check of THEORY-1275 (run: python3 -I scratch/formal/tms_critical_sizes_check.py)
# Second-checker recomputation for THEORY-1275 (Chen et al. 2023, arXiv 2310.06301v1).
# Population loss of high-sparsity TMS computed directly from the model (not Lemma 3.1),
# then critical sample sizes from Eq. 12: n dL + dlam log n + dc = 0.
import numpy as np
from math import log
c=6
def loss(cols, b, M=200001):
    W=np.array(cols).T  # 2 x c
    G=W.T@W
    mu=(np.arange(M)+0.5)/M
    tot=0.0
    for i in range(c):
        out=np.maximum(mu[:,None]*G[i][None,:]+b[None,:],0.0)
        x=np.zeros((M,c)); x[:,i]=mu
        tot+=np.mean(np.sum((x-out)**2,axis=1))
    return tot/c
def gon(k,l,bv,extra_b,neg_vertices=()):
    cols=[];bs=[]
    for j in range(k):
        a=2*np.pi*j/k; L=l; bb=bv
        if j in neg_vertices: L=0.5; bb=-1.0   # l^2 < -b: feature switched off
        cols.append([L*np.cos(a),L*np.sin(a)]); bs.append(bb)
    for e in extra_b: cols.append([0.0,0.0]); bs.append(e)
    return cols,np.array(bs)
pos=1/(2*c); neg=-1.0
cfg={
 '6':gon(6,1.32053,-0.61814,[]),
 '5':gon(5,1.17046,-0.28230,[neg]),
 '5+':gon(5,1.17046,-0.28230,[pos]),
 '4':gon(4,1.0,0.0,[neg,neg]),
 '4+':gon(4,1.0,0.0,[pos,neg]),
 '4++-':gon(4,1.0,0.0,[pos,pos],neg_vertices=(0,)),
}
L={k:loss(*v) for k,v in cfg.items()}
for k,v in L.items(): print(f"L[{k}] = {v:.5f}")
lam_th={'5':7.0,'5+':8.5,'6':8.5}
lam_hat={'4++-':4.097,'4+':5.761,'4':5.297,'5':7.705,'5+':9.906,'6':9.027}
cc={'6':6.37767,'5':3.62417,'5+':3.62764,'4':2.0,'4+':2.00347,'4++-':1.50694}
def ncr(a,b,lam):
    dL=L[b]-L[a]; dl=lam[b]-lam[a]; dc=cc[b]-cc[a]
    f=lambda n: n*dL+dl*log(n)+dc
    # find sign change from + to - on n in [2, 1e6]
    ns=np.unique(np.logspace(0.31,6,200000))
    v=np.array([f(n) for n in ns])
    idx=np.where((v[:-1]>0)&(v[1:]<=0))[0]
    return [float(ns[i]) for i in idx], dL/dl
def mix(**over):
    d=dict(lam_hat); d.update(over); return d
print("5->6 (theory lam):", ncr('5','6',lam_th))
print("4+->5 (lam_hat 4+, lam 5 theory):", ncr('4+','5',mix(**{'5':7.0})))
print("4+->5 (lam_hat both):", ncr('4+','5',lam_hat))
print("4++- -> 4+ (lam_hat):", ncr('4++-','4+',lam_hat))
print("5->5+ (lam_hat):", ncr('5','5+',lam_hat))
print("5->5+ (theory):", ncr('5','5+',lam_th))
print("5+->6 (theory):", ncr('5+','6',lam_th))
for n in (600,1000,2000):
    F={k:n*L[k]+lam_th.get(k,lam_hat.get(k))*log(n)+cc[k] for k in ('5','5+','6')}
    print(n,{k:round(v,1) for k,v in F.items()})
# control: Eq.12 with dc=0 for 4+->5 should give ~327 per App C.3
dL=L['5']-L['4+'];dl=2.0
ns=np.linspace(10,2000,200000);v=ns*dL+dl*np.log(ns);print("control 4+->5 dc=0:",ns[np.where((v[:-1]>0)&(v[1:]<=0))[0]])

# control from App C.3: Delta lambda = 2, Delta c = 1.6207 gives ~380
dc=1.6207; v=ns*dL+2.0*np.log(ns)+dc; print("control C.3 4+->5 with dc:",ns[np.where((v[:-1]>0)&(v[1:]<=0))[0]])
# sensitivity: lambda-hat at +-1 sd (Table K.1) for the chain
sd={'4++-':0.65,'4+':1.53,'5':0.85,'5+':1.27}
import itertools
bad=0;tot=0
for s1,s2,s3,s4 in itertools.product((-1,0,1),repeat=4):
    lam=dict(lam_hat); lam['4++-']+=s1*sd['4++-']; lam['4+']+=s2*sd['4+']; lam['5']+=s3*sd['5']; lam['5+']+=s4*sd['5+']
    a=ncr('4++-','4+',lam)[0]; b=ncr('4+','5',lam)[0]; c3=ncr('5','5+',lam)[0]
    tot+=1
    if not(a and b and c3 and a[0]<b[0]<c3[0]): bad+=1
print("sign combos at +-1 sd where the chain's n_cr are missing or out of order:",bad,"of",tot)
# which step fails
from collections import Counter
why=Counter()
for s1,s2,s3,s4 in itertools.product((-1,0,1),repeat=4):
    lam=dict(lam_hat); lam['4++-']+=s1*sd['4++-']; lam['4+']+=s2*sd['4+']; lam['5']+=s3*sd['5']; lam['5+']+=s4*sd['5+']
    a=ncr('4++-','4+',lam)[0]; b=ncr('4+','5',lam)[0]; c3=ncr('5','5+',lam)[0]
    if not a: why['no 4++- -> 4+']+=1
    elif not b: why['no 4+ -> 5']+=1
    elif not c3: why['no 5 -> 5+']+=1
    elif not a[0]<b[0]: why['4++- -> 4+ after 4+ -> 5']+=1
    elif not b[0]<c3[0]: why['4+ -> 5 after 5 -> 5+']+=1
print(dict(why))
# 5->5+ with theory lambdas but +-1 sd not applicable; 5+ vs 6 for n>202 always 6 preferred
