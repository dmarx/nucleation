"""Constructions for each configuration of (P, D, M, A) the entailments allow.

Every witness is built from three kinds of independent block, stacked
block-diagonally so that the blocks are uncorrelated at every lag:

  AR1    an autonomous AR(1) coarse variable (D and M hold);
  CL389  CLAIM-389's pair A = [[0.5, 0.4], [0, 0.3]], Sigma = I - AA',
         Y = X1: zero memory, transfer entropy 0.120 nats (D fails, M holds);
  LOOP   A = [[0.5, 0.4], [0.4, 0.3]], Y = X1: a round trip, so memory and
         dependence (D and M fail);
  AR2    an autonomous AR(2) coarse variable (D holds, M fails), VAR(2) only;
  FEED   A = [[0.6, 0], [0.5, 0.4]], Y = X1 drives X2 and gets nothing back;

and a COPY row Zc_{t+1} = (part of Y_t) + noise, whose target makes P hold by
construction. A target that reads only an AR1 part of a vector Y lets P and A
hold while D or M fails in another part (the target-relativity of CLAIM-401).
"""
from __future__ import annotations

import numpy as np

from fivecond import Model


class Builder:
    """Accumulates independent blocks of a VAR(p) and their coarse rows."""

    def __init__(self, p=1):
        self.p = p
        self.blocks = []  # (A_list, Sigma)
        self.y = []       # global indices of coarse coordinates
        self.copy = []    # (coefficient dict on y-indices, extra dict) for copy rows
        self.n = 0

    def add(self, A_list, Sigma, coarse):
        A_list = [np.atleast_2d(np.asarray(a, float)) for a in A_list]
        while len(A_list) < self.p:
            A_list.append(np.zeros_like(A_list[0]))
        k = A_list[0].shape[0]
        self.blocks.append((A_list, np.atleast_2d(np.asarray(Sigma, float))))
        idx = list(range(self.n, self.n + k))
        self.n += k
        for c in coarse:
            self.y.append(idx[c])
        return idx

    def build(self, target_from, name, leak=None):
        """target_from: list of global indices whose sum at t drives
        Zc_{t+1} = sum + noise. leak: (index, delta) adds delta * X_index_t
        to the copy row, a small departure from P."""
        n = self.n + 1
        A_list = [np.zeros((n, n)) for _ in range(self.p)]
        Sigma = np.zeros((n, n))
        off = 0
        for Al, S in self.blocks:
            k = Al[0].shape[0]
            for lag in range(self.p):
                A_list[lag][off:off + k, off:off + k] = Al[lag]
            Sigma[off:off + k, off:off + k] = S
            off += k
        for i in target_from:
            A_list[0][n - 1, i] = 1.0
        if leak is not None:
            A_list[0][n - 1, leak[0]] += leak[1]
        Sigma[n - 1, n - 1] = 1.0
        L = np.zeros((len(self.y), n))
        for r, i in enumerate(self.y):
            L[r, i] = 1.0
        G = np.zeros((1, n))
        G[0, n - 1] = 1.0
        return Model(A_list, Sigma, L, G, name=name)


A389 = np.array([[0.5, 0.4], [0.0, 0.3]])
S389 = np.eye(2) - A389 @ A389.T
ALOOP = np.array([[0.5, 0.4], [0.4, 0.3]])
AFEED = np.array([[0.6, 0.0], [0.5, 0.4]])


def ar1(B, phi=0.6, coarse=True):
    return B.add([[[phi]]], [[1.0]], [0] if coarse else [])


def ar2(B, a1=0.5, a2=0.3):
    return B.add([[[a1]], [[a2]]], [[1.0]], [0])


def generic3(name):
    A = np.array([[0.4, 0.3, -0.2], [0.25, 0.3, 0.2], [-0.3, 0.2, 0.35]])
    Sigma = np.array([[1.0, 0.2, 0.0], [0.2, 1.0, 0.1], [0.0, 0.1, 1.0]])
    L = np.array([[1.0, 0.0, 0.0]])
    G = np.array([[0.0, 1.0, 0.0]])
    return Model([A], Sigma, L, G, name=name)


def var1_witnesses(leak=None):
    """Witnesses in VAR(1), Sigma > 0. Keys are the PDMA configuration."""
    W = {}
    W["0000"] = generic3("generic 3-dim, Y = X1, Z = X2")
    W["0010"] = Model([A389], S389, [[1, 0]], [[0, 1]],
                      name="CLAIM-389 pair, Y = X1, Z = X2")
    W["0110"] = Model([AFEED], np.eye(2), [[1, 0]], [[0, 1]],
                      name="FEED, Y = X1 drives X2, Z = X2")

    B = Builder(); i = B.add([ALOOP], np.eye(2), [0])
    W["1000"] = B.build([i[0]], "LOOP, Z copies Y")

    B = Builder(); j = ar1(B); B.add([ALOOP], np.eye(2), [0])
    W["1001"] = B.build([j[0]], "Y = (AR1, LOOP.X1), Z copies the AR1 part")

    B = Builder(); i = B.add([A389], S389, [0])
    W["1010"] = B.build([i[0]], "CLAIM-389 pair, Z copies Y")

    B = Builder(); j = ar1(B); B.add([A389], S389, [0])
    W["1011"] = B.build([j[0]], "Y = (AR1, CL389.X1), Z copies the AR1 part")

    B = Builder(); j = ar1(B)
    W["1111"] = B.build([j[0]], "AR1, Z copies Y")
    return W


def var2_witnesses():
    """The configurations VAR(1) forbids (D without M), realized in VAR(2)."""
    W = {}
    A1 = np.diag([0.5, 0.6]); A2 = np.diag([0.3, 0.0])
    W["0100"] = Model([A1, A2], np.eye(2), [[1, 0]], [[0, 1]],
                      name="AR2 Y beside an independent AR1 target")

    B = Builder(p=2); j = ar2(B)
    W["1100"] = B.build([j[0]], "AR2, Z copies Y")

    B = Builder(p=2); j = ar1(B); ar2(B)
    W["1101"] = B.build([j[0]], "Y = (AR1, AR2), Z copies the AR1 part")
    return W


def leaky_witnesses(delta=0.05):
    """For eps > 0: P fails by a little and A still holds within eps.
    The leak reads an independent AR1 that is not part of Y."""
    W = {}
    B = Builder(); j = ar1(B); B.add([ALOOP], np.eye(2), [0]); u = ar1(B, 0.5, coarse=False)
    W["0001"] = B.build([j[0]], "as 1001, with a leak from an unobserved AR1", leak=(u[0], delta))

    B = Builder(); j = ar1(B); B.add([A389], S389, [0]); u = ar1(B, 0.5, coarse=False)
    W["0011"] = B.build([j[0]], "as 1011, with a leak", leak=(u[0], delta))

    B = Builder(); j = ar1(B); u = ar1(B, 0.5, coarse=False)
    W["0111"] = B.build([j[0]], "as 1111, with a leak", leak=(u[0], delta))

    B = Builder(p=2); j = ar1(B); ar2(B); u = ar1(B, 0.5, coarse=False)
    W["0101"] = B.build([j[0]], "as 1101 (VAR(2)), with a leak", leak=(u[0], delta))
    return W


def pad(model: Model, k: int, phi=0.5) -> Model:
    """Append k independent AR(1) coordinates to the state and to Y.
    P, D, M and A are unchanged; only m grows (so C can be switched off)."""
    n, p = model.n, model.p
    N = n + k
    A_list = []
    for lag, Al in enumerate(model.A_list):
        B = np.zeros((N, N)); B[:n, :n] = Al
        if lag == 0:
            B[n:, n:] = phi * np.eye(k)
        A_list.append(B)
    Sigma = np.zeros((N, N)); Sigma[:n, :n] = model.Sigma; Sigma[n:, n:] = np.eye(k)
    L0 = model.L[:, :n]
    L = np.zeros((model.m + k, N)); L[:model.m, :n] = L0
    L[model.m:, n:] = np.eye(k)
    G = np.zeros((1, N)); G[:, :n] = model.G[:, :n]
    return Model(A_list, Sigma, L, G, name=model.name + f" + {k} padded")
