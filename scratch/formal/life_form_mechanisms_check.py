"""scratch/formal/life_form_mechanisms_check.py

Rebuilds the Life computations CLAIM-672 cites from its grounds CASE-260
(the block) and CASE-259 (the eater), from the cases' text alone; the
filer's 40-line simulator was not kept. Written at the recomputation pass
of 2026-11-25 by a session other than the filer's, with its own simulator
(a set-based B3/S23 on the unbounded plane, so nothing wraps).
Run: python3 -I this file. Standard library only.

Gosper's gun is the standard 36-cell pattern, placed with its cell (x, y)
at row y, column x, as CASE-259 says.
"""
from collections import Counter

BLOCK = {(0, 0), (0, 1), (1, 0), (1, 1)}
EATER = {(0, 0), (0, 1), (1, 0), (1, 2), (2, 2), (3, 2), (3, 3)}
GLIDER = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
GUN_XY = [(24, 0), (22, 1), (24, 1), (12, 2), (13, 2), (20, 2), (21, 2), (34, 2), (35, 2),
          (11, 3), (15, 3), (20, 3), (21, 3), (34, 3), (35, 3), (0, 4), (1, 4), (10, 4),
          (16, 4), (20, 4), (21, 4), (0, 5), (1, 5), (10, 5), (14, 5), (16, 5), (17, 5),
          (22, 5), (24, 5), (10, 6), (16, 6), (24, 6), (11, 7), (15, 7), (12, 8), (13, 8)]
GUN = {(y, x) for x, y in GUN_XY}
LEFT, RIGHT = {(4, 0), (4, 1), (5, 0), (5, 1)}, {(2, 34), (2, 35), (3, 34), (3, 35)}


def step(s):
    n = Counter((r + dr, c + dc) for r, c in s for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc)
    return {p for p, k in n.items() if k == 3 or (k == 2 and p in s)}


def shift(cells, dr, dc):
    return {(r + dr, c + dc) for r, c in cells}


def run(s, t):
    for _ in range(t):
        s = step(s)
    return s


def components(cells):
    cells, out = set(cells), []
    while cells:
        stack = [cells.pop()]
        comp = set(stack)
        while stack:
            r, c = stack.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    q = (r + dr, c + dc)
                    if q in cells:
                        cells.remove(q); comp.add(q); stack.append(q)
        out.append(comp)
    return out


def gliders_away(s, row=15):
    """Five-cell components wholly at or below `row` (CASE-260 gives no criterion; 15 rows
    is the reading under which the intact gun's counts match)."""
    return sum(1 for k in components(s) if len(k) == 5 and min(r for r, _ in k) >= row)


def emission(start, ts=(100, 200, 300, 400)):
    s, out = set(start), {}
    for t in range(1, max(ts) + 1):
        s = step(s)
        if t in ts:
            out[t] = gliders_away(s)
    return out, len(s)


assert len(GUN) == 36
# --- CASE-260: the lone block and the lone eater are fixed points ---
assert run(BLOCK, 1000) == BLOCK
assert run(EATER, 1000) == EATER

# --- CASE-259 1: the eater struck in its lane regrows its corner from its own cells ---
E = shift(EATER, 12, 12)
s = GLIDER | E
hist = {}
for t in range(1, 40):
    s = step(s)
    hist[t] = s
corner = (12, 12)
assert corner in hist[35] and corner not in hist[36] and corner in hist[37], "eater repair timing"
assert hist[38] == E and run(hist[38], 100) == E
# a block in its place is annihilated
assert run(GLIDER | shift(BLOCK, 12, 12), 300) == set()
print("eater: struck at t = 35, corner dead at 36, reborn at 37, exact eater at 38; a block there is annihilated")

# --- CASE-260 2: Gosper's gun rebuilds its blocks; it emits 2/5/9/12 gliders by 100/200/300/400 ---
s = set(GUN)
broken_left = []
for t in range(1, 61):
    s = step(s)
    if not LEFT <= s:
        broken_left.append(t)
assert broken_left[:3] == [19, 20, 21] and LEFT <= run(GUN, 22)
intact, pop = emission(GUN)
assert pop == 113 and [intact[t] for t in (100, 200, 300, 400)] == [2, 5, 9, 12], intact
noleft, pop_l = emission(GUN - LEFT)
noright, pop_r = emission(GUN - RIGHT)
assert pop_l == 185 and pop_r == 23
print("gun: left block incomplete at t =", broken_left, "; whole again at 22")
print("gliders away (100/200/300/400): intact", list(intact.values()), "population", pop,
      "; left block removed", list(noleft.values()), pop_l, "; right removed", list(noright.values()), pop_r)

# --- CASE-259 3: the eater across the gun's stream, cell (0,0) at row 30, column 44 ---
E2 = shift(EATER, 30, 44)
s = GUN | E2
dead = []
for t in range(1, 601):
    s = step(s)
    if not E2 <= s:
        dead.append(t)
    if t in (200, 400, 600):
        assert not any(r > 34 or c > 48 for r, c in s), ("cells beyond the eater", t)
p300 = run(GUN | E2, 300)
assert run(p300, 30) == p300, "gun and eater period 30"
pops = []
x = p300
for _ in range(30):
    pops.append(len(x)); x = step(x)
first = [t for t in dead if t >= 100][:7]
print("eater in the gun's stream: incomplete at", first, "; period 30 from t = 300; population", min(pops), "to", max(pops))
print("checks pass")
