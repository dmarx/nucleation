# scratch/formal/agenda_cycle_check.py: the smallest selective-contestation case for CLAIM-448's existence half (run: python3 -I scratch/formal/agenda_cycle_check.py)
# Three perspectives with a Condorcet cycle; a chair admits only two of the three pairwise contests.
import itertools
prefs={'P1':['x','y','z'],'P2':['y','z','x'],'P3':['z','x','y']}
def beats(a,b): return sum(p.index(a)<p.index(b) for p in prefs.values())>=2
alts='xyz'
allc=[(a,b) if beats(a,b) else (b,a) for a,b in itertools.combinations(alts,2)]
def acyclic(edges):
    # check for a potential: topological order exists
    import itertools
    for order in itertools.permutations(alts):
        if all(order.index(w)<order.index(l) for w,l in edges): return order
    return None
admitted=[e for e in allc if set(e)!={'x','z'}]
print("all contests (winner,loser):",allc,"potential:",acyclic(allc))
print("admitted:",admitted,"potential:",acyclic(admitted))
# dissent in admitted record: perspectives on the losing side of each admitted contest
for w,l in admitted: print(w,">",l,"losers:",[k for k,p in prefs.items() if p.index(l)<p.index(w)])
