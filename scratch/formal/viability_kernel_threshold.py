"""Toy check for the note on TERM-167 (authority-sensitive kernel).
State (r, q): readiness r in 0..R, threshold q in 0..R. Constraint: r >= q.
Readiness decays by 1 each step unless maintained. Coalitions differ in actions:
  committee: maintain (r stays) or neglect (r-1)
  ops (frozen thresholds): neglect only
  ops (self-set thresholds): neglect, or neglect and lower q by 1
Viability kernel = largest set inside the constraint from which some action keeps
the state inside it forever (computed by backward fixed point)."""
R = 5
S = [(r, q) for r in range(R + 1) for q in range(R + 1)]
def step(s, a):
    r, q = s
    if a == 'maintain': return (r, q)
    if a == 'neglect': return (max(r - 1, 0), q)
    if a == 'lower': return (max(r - 1, 0), max(q - 1, 0))
def kernel(actions):
    K = {s for s in S if s[0] >= s[1]}
    while True:
        K2 = {s for s in K if any(step(s, a) in K for a in actions)}
        if K2 == K: return K
        K = K2
full = kernel(['maintain', 'neglect', 'lower'])
committee = kernel(['maintain', 'neglect'])
ops_frozen = kernel(['neglect'])
ops_self = kernel(['neglect', 'lower'])
M = {s for s in S if s[0] >= s[1]}
print('constraint set size', len(M))
print('committee kernel == M:', committee == M)
print('ops frozen kernel:', sorted(ops_frozen))
print('ops self-set kernel == M:', ops_self == M)
print('restricted subsets of full:', ops_frozen <= committee <= full, ops_frozen <= ops_self <= full)
# With self-set thresholds, judged against the frozen threshold q0 = 3:
q0 = 3
traj = [(3, 3)]
for _ in range(4): traj.append(step(traj[-1], 'lower'))
print('ops self-set trajectory from (3,3):', traj, '; meets r>=q every step:', all(r >= q for r, q in traj), '; meets frozen q0=3:', [r >= q0 for r, _ in traj])
