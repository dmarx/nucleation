# scratch/formal/botnan_lesnick_checks.py: checks Example 4.6 (no good barcode on a 3x3 grid) and Example 6.10 (AB = I3) of Botnan & Lesnick, arXiv:2203.14289v2
import itertools
from fractions import Fraction as F

# ---- Example 4.6: the module on P = {0,1,2}^2, maps along the cover relations (x,y)->(x+1,y), (x,y)->(x,y+1)
dim = {(0,2):1,(1,2):1,(2,2):0,(0,1):1,(1,1):2,(2,1):1,(0,0):0,(1,0):1,(2,0):1}
def I(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def Z(r,c): return [[F(0)]*c for _ in range(r)]
def mul(A,B):
    if not A or not B or not A[0]: return Z(len(A), len(B[0]) if B else 0)
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
# matrix of M_p -> M_q as (dim q) x (dim p)
edge = {}
def put(p,q,A): edge[(p,q)] = [[F(v) for v in row] for row in A]
put((0,2),(1,2),[[1]]);  put((1,2),(2,2),Z(0,1))
put((0,1),(1,1),[[1],[0]]); put((1,1),(2,1),[[1,1]])
put((0,0),(1,0),Z(1,0)); put((1,0),(2,0),[[1]])
put((0,0),(0,1),Z(1,0)); put((0,1),(0,2),[[1]])
put((1,0),(1,1),[[0],[1]]); put((1,1),(1,2),[[1,0]])
put((2,0),(2,1),[[1]]);  put((2,1),(2,2),Z(0,1))
def rank(A):
    A=[r[:] for r in A]; 
    if not A or not A[0]: return 0
    rk=0; rows=len(A); cols=len(A[0])
    for c in range(cols):
        piv=next((r for r in range(rk,rows) if A[r][c]!=0),None)
        if piv is None: continue
        A[rk],A[piv]=A[piv],A[rk]
        for r in range(rows):
            if r!=rk and A[r][c]!=0:
                f=A[r][c]/A[rk][c]; A[r]=[a-f*b for a,b in zip(A[r],A[rk])]
        rk+=1
    return rk
def path_map(p,q):
    # go right first, then up
    M = I(dim[p]); cur=p
    while cur[0]<q[0]:
        nxt=(cur[0]+1,cur[1]); M=mul(edge[(cur,nxt)],M) if dim[cur] and dim[nxt] else Z(dim[nxt],dim[p]); cur=nxt
    while cur[1]<q[1]:
        nxt=(cur[0],cur[1]+1); M=mul(edge[(cur,nxt)],M) if dim[cur] and dim[nxt] else Z(dim[nxt],dim[p]); cur=nxt
    return M
def path_map_up_first(p,q):
    M = I(dim[p]); cur=p
    while cur[1]<q[1]:
        nxt=(cur[0],cur[1]+1); M=mul(edge[(cur,nxt)],M) if dim[cur] and dim[nxt] else Z(dim[nxt],dim[p]); cur=nxt
    while cur[0]<q[0]:
        nxt=(cur[0]+1,cur[1]); M=mul(edge[(cur,nxt)],M) if dim[cur] and dim[nxt] else Z(dim[nxt],dim[p]); cur=nxt
    return M
P=[(x,y) for x in range(3) for y in range(3)]
le=lambda p,q: p[0]<=q[0] and p[1]<=q[1]
# commutativity of every square
for p in P:
    for q in P:
        if le(p,q):
            assert path_map(p,q)==path_map_up_first(p,q) or dim[p]==0 or dim[q]==0, (p,q)
rk = lambda p,q: rank(path_map(p,q)) if dim[p] and dim[q] else 0
print("Rk(01->21), Rk(01->12), Rk(10->21), Rk(10->12) =", rk((0,1),(2,1)), rk((0,1),(1,2)), rk((1,0),(2,1)), rk((1,0),(1,2)))
assert (rk((0,1),(2,1)), rk((0,1),(1,2)), rk((1,0),(2,1)), rk((1,0),(1,2))) == (1,1,1,0)
# brute force: no multiset of subsets of P (each element used at most max-dim times) is a good barcode.
# Any good barcode has exactly dim M_x members containing x, so total incidences = sum dims = 8;
# members are nonempty subsets of the support; search multisets of size <= 8 by DFS over incidence counts.
supp=[p for p in P if dim[p]>0]
pairs=[(p,q) for p in supp for q in supp if le(p,q)]
target={pq:rk(*pq) for pq in pairs}
subsets=[frozenset(s) for r in range(1,len(supp)+1) for s in itertools.combinations(supp,r)]
def good(B):
    return all(sum(1 for S in B if p in S and q in S)==target[(p,q)] for (p,q) in pairs)
found=False
need={p:dim[p] for p in supp}
def dfs(start, B, cnt):
    global found
    if found: return
    if all(cnt[p]==need[p] for p in supp):
        if good(B): found=True
        return
    for i in range(start,len(subsets)):
        S=subsets[i]
        if all(cnt[p]+1<=need[p] for p in S):
            # prune: pairwise counts must not exceed targets
            ok=all(sum(1 for T in B+[S] if p in T and q in T)<=target[(p,q)] for (p,q) in pairs if p in S and q in S)
            if not ok: continue
            for p in S: cnt[p]+=1
            dfs(i,B+[S],cnt)
            for p in S: cnt[p]-=1
dfs(0,[],{p:0 for p in supp})
print("good barcode exists for Example 4.6:", found)
assert not found
# CONTROL (should find one): change M(1,1)->M(2,1) from [1,1] to [0,1]; the module is then k_I + k_J with
# I = {(0,1),(1,1),(0,2),(1,2)}, J = {(1,0),(2,0),(1,1),(2,1)}, which has a good barcode {I, J}
edge[((1,1),(2,1))]=[[F(0),F(1)]]
for p_ in P:
    for q_ in P:
        if le(p_,q_) and dim[p_] and dim[q_]: assert path_map(p_,q_)==path_map_up_first(p_,q_), ("control not commutative",p_,q_)
target={pq:rk(*pq) for pq in pairs}
found=False; dfs(0,[],{p:0 for p in supp})
print("control (altered map) good barcode exists:", found)
assert found, "control failed"

# ---- Example 6.10
A=[[1,1,1],[1,0,1],[1,1,0]]; B=[[-1,1,1],[1,-1,0],[1,0,-1]]
mm=lambda X,Y:[[sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
print("AB =", mm(A,B)); assert mm(A,B)==[[1,0,0],[0,1,0],[0,0,1]]
assert A[1][1]==0 and A[2][2]==0 and B[1][2]==0 and B[2][1]==0
# CONTROL (should fail): flip one sign in B
Bc=[r[:] for r in B]; Bc[0][0]=1
print("control AB' == I3:", mm(A,Bc)==[[1,0,0],[0,1,0],[0,0,1]]); assert mm(A,Bc)!=[[1,0,0],[0,1,0],[0,0,1]]
print("ALL OK")
