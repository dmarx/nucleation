"""scratch/formal/critical_path_route_check.py

Rechecks CLAIM-1114 (the response time of a route of stages that share no
resource is its critical path) with a kept script and a seed: the entry's
own check ("20,000 random routes ... In 2,037 of them the slowest stage
had been done in advance") gave none. Written at the recomputation pass of
2026-11-25 by a session other than the filer's, from the entry's text.
Run: python3 -I this file. Standard library only; seed 1114.

A route is built recursively to depth four: a leaf is a stage (duration
uniform on [0, 10], done in advance with probability 1/4, then duration 0
from the contingency on); an inner node is a sequence or a parallel block
of two or three sub-routes. Two computations of the finish time are
compared: (a) the rule (sequence adds, parallel takes the max, done
stages add nothing); (b) an event simulation on the precedence graph the
route defines, each stage starting when every stage it needs has
finished. A negative control runs every stage on one server (stages
compete), where (b) gives the sum and the rule fails.
"""
import random

rng = random.Random(1114)


def build(depth):
    if depth == 0 or rng.random() < 0.25:
        return ("stage", rng.uniform(0, 10), rng.random() < 0.25)
    kind = rng.choice(("seq", "par"))
    return (kind, [build(depth - 1) for _ in range(rng.choice((2, 3)))])


def rule(r):
    if r[0] == "stage":
        return 0.0 if r[2] else r[1]
    vals = [rule(x) for x in r[1]]
    return sum(vals) if r[0] == "seq" else max(vals)


def lay(r, entry, stages, needs):
    """Add the route's stages, each needing every stage in `entry`; return the route's exit stages."""
    if r[0] == "stage":
        i = len(stages)
        stages.append(0.0 if r[2] else r[1])
        needs.append(set(entry))
        return {i}
    if r[0] == "seq":
        cur = set(entry)
        for x in r[1]:
            cur = lay(x, cur, stages, needs)
        return cur
    out = set()
    for x in r[1]:
        out |= lay(x, entry, stages, needs)
    return out


def simulate(r, one_server=False):
    stages, needs = [], []
    exits = lay(r, set(), stages, needs)
    finish = {}
    free_at = 0.0
    pending = set(range(len(stages)))
    while pending:
        ready = sorted(i for i in pending if needs[i] <= finish.keys())
        for i in ready:
            start = max([finish[j] for j in needs[i]], default=0.0)
            if one_server:
                start = max(start, free_at)
                free_at = start + stages[i]
            finish[i] = start + stages[i]
            pending.discard(i)
    return max(finish[i] for i in exits), stages, r


def slowest(r):
    if r[0] == "stage":
        return [(r[1], r[2])]
    return [s for x in r[1] for s in slowest(x)]


N = 20000
agree = slow_done_and_faster = 0
for _ in range(N):
    r = build(4)
    t, _, _ = simulate(r)
    assert abs(t - rule(r)) < 1e-9
    agree += 1
    d, done = max(slowest(r))
    if done and t < d:
        slow_done_and_faster += 1
print(f"{agree} of {N} routes: event times by precedence equal the rule")
print(f"{slow_done_and_faster} routes in which the slowest stage was done in advance and the response time below its duration (seed 1114)")

# negative control: on one server the stages compete and the parallel rule fails
r = ("par", [("stage", 3.0, False), ("stage", 4.0, False), ("stage", 5.0, False)])
t1, _, _ = simulate(r, one_server=True)
assert rule(r) == 5.0 and t1 == 12.0
# A54's restatement on the record: 3, 4 and 5 days, 12 in sequence, 5 in parallel
assert rule(("seq", [("stage", 3.0, False), ("stage", 4.0, False), ("stage", 5.0, False)])) == 12.0
print("negative control: three stages on one server take 12, not the parallel rule's 5")
print("checks pass")
