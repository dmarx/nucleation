# scratch/formal/class_selection_check.py
# Check of CLAIM-tmpkvgmj (needs numpy, scipy, networkx; run with python3 -I).
# For a class C of disturbances an agent cannot tell apart, one x with
# |Dx - a0 - w| <= delta for every w in C exists iff r_e <= delta_e on every
# overlap and CLAIM-538's cycle condition holds for offsets a0 + m and
# tolerances delta - r, where m and r are the edgewise midpoint and half-range
# of w over C. Compared against a direct LP on random connected graphs; then
# CLAIM-537's triangle, whose two worlds are both coboundaries.
import random, itertools, numpy as np
from scipy.optimize import linprog
import networkx as nx
random.seed(1); np.random.seed(1)
def direct(G,edges,a0,delta,C):
    n=G.number_of_nodes(); A=[];b=[]
    for w in C:
        for k,(u,v) in enumerate(edges):
            row=np.zeros(n); row[v]+=1; row[u]-=1
            A.append(row); b.append(a0[k]+w[k]+delta[k]); A.append(-row); b.append(-(a0[k]+w[k]-delta[k]))
    r=linprog(np.zeros(n),A_ub=np.array(A),b_ub=np.array(b),bounds=[(None,None)]*n,method="highs")
    return r.status==0
def cyc(G,edges,off,tol):
    if any(t< -1e-12 for t in tol): return False
    idx={e:k for k,e in enumerate(edges)}
    DG=nx.DiGraph(); DG.add_edges_from(edges); DG.add_edges_from((v,u) for u,v in edges)
    for c in nx.simple_cycles(DG):
        if len(c)<3: continue
        h=0;s=0
        for i in range(len(c)):
            u,v=c[i],c[(i+1)%len(c)]
            if (u,v) in idx: k=idx[(u,v)]; h+=off[k]
            else: k=idx[(v,u)]; h-=off[k]
            s+=tol[k]
        if abs(h)>s+1e-9: return False
    return True
mis=0;N=0;fails=0
for t in range(1500):
    n=random.randint(3,5); G=nx.gnm_random_graph(n,random.randint(n,min(n*(n-1)//2,n+3)),seed=t)
    if not nx.is_connected(G): continue
    edges=list(G.edges()); m=len(edges)
    a0=np.random.uniform(-.5,.5,m); delta=np.random.uniform(.05,.6,m)
    C=[np.random.uniform(-.5,.5,m) for _ in range(random.randint(1,4))]
    W=np.array(C); mid=(W.max(0)+W.min(0))/2; rad=(W.max(0)-W.min(0))/2
    d=direct(G,edges,a0,delta,C); c=cyc(G,edges,a0+mid,delta-rad)
    N+=1; mis+= d!=c; fails+= (not d)
print("instances",N,"mismatches",mis,"infeasible",fails)
# triangle example: a0=0, delta=.3, worlds coboundaries
G=nx.Graph(); edges=[(0,1),(1,2),(2,0)]; G.add_edges_from(edges)
for w in [(0.6,-0.6,0.0),(-0.6,0.6,0.0)]:
    print("world",w,"holonomy",sum(w),"exists:",direct(G,edges,[0,0,0],[.3]*3,[np.array(w)]))
print("both, one x:",direct(G,edges,[0,0,0],[.3]*3,[np.array(w) for w in [(0.6,-0.6,0.0),(-0.6,0.6,0.0)]]))
