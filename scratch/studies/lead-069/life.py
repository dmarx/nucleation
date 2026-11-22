"""Conway's Game of Life (B3/S23) on a torus, with the patterns of CASE-259 and CASE-260."""
import numpy as np

BLOCK = [(0, 0), (0, 1), (1, 0), (1, 1)]
EATER = [(0, 0), (0, 1), (1, 0), (1, 2), (2, 2), (3, 2), (3, 3)]
GLIDER_SE = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# Gosper's glider gun, standard (x, y); placed with cell (x, y) at row y, column x.
GUN_XY = [(24, 0), (22, 1), (24, 1), (12, 2), (13, 2), (20, 2), (21, 2), (34, 2), (35, 2),
          (11, 3), (15, 3), (20, 3), (21, 3), (34, 3), (35, 3), (0, 4), (1, 4), (10, 4),
          (16, 4), (20, 4), (21, 4), (0, 5), (1, 5), (10, 5), (14, 5), (16, 5), (17, 5),
          (22, 5), (24, 5), (10, 6), (16, 6), (24, 6), (11, 7), (15, 7), (12, 8), (13, 8)]
GUN = [(y, x) for x, y in GUN_XY]
GUN_LEFT_BLOCK = [(4, 0), (4, 1), (5, 0), (5, 1)]
GUN_RIGHT_BLOCK = [(2, 34), (2, 35), (3, 34), (3, 35)]


def neighbours(g):
    n = np.zeros(g.shape, dtype=np.int8)
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr or dc:
                n += np.roll(np.roll(g, dr, 0), dc, 1)
    return n


def step(g):
    n = neighbours(g)
    return ((n == 3) | ((g == 1) & (n == 2))).astype(np.int8)


def run(g, t):
    for _ in range(t):
        g = step(g)
    return g


def place(g, cells, offset=(0, 0)):
    for r, c in cells:
        g[(r + offset[0]) % g.shape[0], (c + offset[1]) % g.shape[1]] = 1
    return g


def board(shape, cells, offset=(0, 0)):
    return place(np.zeros(shape, dtype=np.int8), cells, offset)


def cells_of(g):
    return set(map(tuple, np.argwhere(g == 1).tolist()))


def ring(cells, radius):
    """Cells at Chebyshev distance 1..radius from the set, not in it."""
    cells = set(cells)
    out = set()
    for r, c in cells:
        for dr in range(-radius, radius + 1):
            for dc in range(-radius, radius + 1):
                p = (r + dr, c + dc)
                if p not in cells:
                    out.add(p)
    return out


def chebyshev(p, cells):
    return min(max(abs(p[0] - r), abs(p[1] - c)) for r, c in cells)
