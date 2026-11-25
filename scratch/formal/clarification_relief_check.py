"""scratch/formal/clarification_relief_check.py

Re-derives CLAIM-tmp7rl3d (when clarifying a misunderstanding is relief)
in a finite model built from the entry's own derivation, steps 1 to 5.
No script was kept by the filer. Written at the recomputation pass of
2026-11-25 by a session other than the filer's. Run: python3 -I this file.
Standard library only.

Model. Situations are the points of a finite set C that the ambiguous
expression conflates; a joint outcome policy f assigns an outcome in O to
each cell of the current partition of C (before any distinction, one cell:
f is constant on C). Step 1: party i's reading is a demand (S_i, A_i): in
every situation of S_i the outcome lies in A_i. Step 2: consequential means
no policy on the coarse partition meets both. Step 3: relief is a policy
meeting both demands as declared. Step 4: a distinction refines the
partition. Checked by exhaustion over |C| <= 4, |O| <= 3:

(a) a consequential conflict is relieved by some distinction exactly when
    S_1 and S_2 are disjoint (the demands bear on different situations);
(b) where S_1 and S_2 meet, no refinement relieves it, while an outcome in
    A_1 & A_2 would (and its absence is what made it consequential);
(c) dropping or rewording a demand (replacing (S_2, A_2)) can make the pair
    realizable, which is why step 5 has to exclude it from relief.
A negative control admits the distinction the defeated_if excludes, a
feature introduced after the fact that separates situations by who is
asking (each situation split into one copy per party); under it (b) fails,
so the check can fail.
"""
import itertools


def subsets(xs, nonempty=True):
    xs = list(xs)
    out = []
    for r in range(1 if nonempty else 0, len(xs) + 1):
        out += [frozenset(c) for c in itertools.combinations(xs, r)]
    return out


def partitions(xs):
    xs = list(xs)
    if not xs:
        yield []
        return
    first, rest = xs[0], xs[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [p[i] | {first}] + p[i + 1:]
        yield p + [frozenset([first])]


def realizable(partition, demands, O, meets_all=True):
    cell = {s: k for k, blk in enumerate(partition) for s in blk}
    for f in itertools.product(O, repeat=len(partition)):
        ok = [all(f[cell[s]] in A for s in S) for S, A in demands]
        if (all(ok) if meets_all else any(ok)):
            return True
    return False


def run(meets_all=True):
    n_cases = n_disjoint = n_meet = 0
    for nC in range(1, 5):
        C = frozenset(range(nC))
        parts = list(partitions(C))
        for nO in range(2, 4):
            O = list(range(nO))
            for S1, S2 in itertools.product(subsets(C), repeat=2):
                for A1, A2 in itertools.product(subsets(O), repeat=2):
                    d = [(S1, A1), (S2, A2)]
                    if realizable([C], d, O, meets_all):
                        continue  # not consequential
                    n_cases += 1
                    relieved = any(realizable(p, d, O, meets_all) for p in parts)
                    if not S1 & S2:
                        n_disjoint += 1
                        if not relieved:
                            return False, "(a) disjoint demands not relieved"
                    else:
                        n_meet += 1
                        if relieved:
                            return False, "(b) overlapping demands relieved by a distinction"
                        assert not (A1 & A2)
    return True, (n_cases, n_disjoint, n_meet)


ok, info = run()
assert ok, info
print(f"consequential cases {info[0]}: disjoint, relieved by a distinction {info[1]}; "
      f"overlapping, never relieved {info[2]}")

# (c) rewording a demand can make the pair realizable without relief of the declared one
C = frozenset({0, 1}); O = [0, 1]
d = [(C, frozenset({0})), (C, frozenset({1}))]
assert not any(realizable(p, d, O) for p in partitions(C))
assert realizable([C], [d[0], (C, frozenset({0, 1}))], O)

# negative control: split every situation by who is asking (the after-the-fact feature)
def by_party(S1, A1, S2, A2, C):
    C2 = frozenset((s, i) for s in C for i in (1, 2))
    d = [(frozenset((s, 1) for s in S1), A1), (frozenset((s, 2) for s in S2), A2)]
    return C2, d


C = frozenset({0, 1}); O = [0, 1]
C2, d2 = by_party(C, frozenset({0}), C, frozenset({1}), C)
finest = [frozenset([x]) for x in C2]
assert realizable(finest, d2, O)  # (b) would fail under this distinction
print("negative control: a split by who is asking relieves overlapping demands, so (b) fails under it")
print("checks pass")
