# scratch/formal/connelly_whiteley_531_check.py: the twenty-ninth status review's check of Connelly and Whiteley (1996) Example 5.3.1, for NOTE-1588 and THEORY-1389 (run: python3 -I scratch/formal/connelly_whiteley_531_check.py)
# Recheck of Connelly-Whiteley 1996, Example 5.3.1 (second-order rigid, not prestress stable).
import numpy as np, itertools
from scipy.linalg import null_space
P=np.array([[0,0,0],[0,1,0],[0,0,1],[1,0,0],[1,1,0],[0,1,0],[1,0,0]],float)
E=[(1,2),(1,3),(1,4),(1,6),(1,7),(2,3),(2,5),(2,7),(3,4),(3,5),(4,5),(4,6),(5,6),(5,7),(6,7)]
E=[(a-1,b-1) for a,b in E]; v=len(P)
R=np.zeros((len(E),3*v))
for k,(i,j) in enumerate(E):
    d=P[i]-P[j]; R[k,3*i:3*i+3]=d; R[k,3*j:3*j+3]=-d
F=null_space(R); S=null_space(R.T)
print("bars",len(E),"rank",np.linalg.matrix_rank(R),"flex dim",F.shape[1],"(6 trivial)","stress dim",S.shape[1])
def Omega(w):
    O=np.zeros((v,v))
    for k,(i,j) in enumerate(E):
        O[i,j]-=w[k];O[j,i]-=w[k];O[i,i]+=w[k];O[j,j]+=w[k]
    return np.kron(O,np.eye(3))
# trivial flexes
T=[]
for t in np.eye(3): T.append(np.tile(t,v))
for ax in np.eye(3): T.append(np.concatenate([np.cross(ax,p) for p in P]))
T=np.array(T).T
print("trivial rank",np.linalg.matrix_rank(T))
# complement: paper's p'(1), p'(2)
p1=np.zeros(3*v);p1[3*5+2]=1; p2=np.zeros(3*v);p2[3*6+2]=1
print("p'(1),p'(2) are flexes:",np.allclose(R@p1,0),np.allclose(R@p2,0),"independent of trivial:",np.linalg.matrix_rank(np.column_stack([T,p1,p2])))
B=np.column_stack([p1,p2])
w1=np.zeros(len(E)); 
for e,s in [((2,7),1),((5,6),1),((1,6),1),((2,5),-1),((6,7),-1),((1,2),-1)]:
    a,b=e; k=E.index((a-1,b-1)); w1[k]=s
print("w1 self-stress:",np.allclose(w1@R,0))
M=[B.T@Omega(S[:,k])@B for k in range(S.shape[1])]
M1=B.T@Omega(w1)@B; print("Omega(1) on flexes\n",M1)
# prestress: any combo PD? scan angles
pd=False
for th in np.linspace(0,2*np.pi,20001):
    A=np.cos(th)*M[0]+np.sin(th)*M[1]
    if np.all(np.linalg.eigvalsh(A)>1e-9): pd=True
print("some combination positive definite (prestress stable):",pd)
# second-order: common nonzero isotropic vector of all stress forms on span
common=False
for th in np.linspace(0,np.pi,200001):
    x=np.array([np.cos(th),np.sin(th)])
    if abs(x@M[0]@x)<1e-6 and abs(x@M[1]@x)<1e-6: common=True
print("common zero (second-order flexible):",common)
# Controls: the same scans on forms where the answer is known.
def scans(Ms):
    pd=any(np.all(np.linalg.eigvalsh(np.cos(t)*Ms[0]+np.sin(t)*Ms[1])>1e-9) for t in np.linspace(0,2*np.pi,2001))
    cz=any(abs(np.array([np.cos(t),np.sin(t)])@Ms[0]@np.array([np.cos(t),np.sin(t)]))<1e-6 and abs(np.array([np.cos(t),np.sin(t)])@Ms[1]@np.array([np.cos(t),np.sin(t)]))<1e-6 for t in np.linspace(0,np.pi,200001))
    return pd,cz
print("control PD (identity, diag(1,-1)) -> expect (True, False):",scans([np.eye(2),np.diag([1.,-1])]))
print("control common zero ([[0,1],[1,0]], [[0,0],[0,1]]... ) -> expect (False, True):",scans([np.array([[0,1.],[1,0]]),np.array([[0,1.],[1,1]])]))
