import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rorder import (compatible_garbling, deterministic_map, factoring_class,  # noqa: E402
                    factors_through, in_hull, r_dominates, respects,
                    separating_loss, unrestricted_class, usable_risk)


def test_in_hull_and_separation():
    verts = [np.array([[1.0, 0.0]]), np.array([[0.0, 1.0]])]
    assert in_hull(np.array([[0.3, 0.7]]), verts)
    assert not in_hull(np.array([[0.3, 0.3]]), verts)
    t, _ = separating_loss(np.array([[0.3, 0.3]]), verts)
    assert t > 1e-6


def test_unrestricted_usable_risk_is_bayes_risk():
    P = np.array([[0.8, 0.2], [0.3, 0.7]])
    L = 1 - np.eye(2)
    pi = np.array([0.5, 0.5])
    # Bayes risk of guessing the state: 0.5*(0.2+0.3)
    assert abs(usable_risk(P, unrestricted_class(2, 2), L, pi) - 0.25) < 1e-12


def test_identity_respected_and_blackwell_easy_direction():
    rng = np.random.default_rng(0)
    R = unrestricted_class(3, 2)
    assert respects(np.eye(3), R)
    G = rng.random((3, 3)); G /= G.sum(1, keepdims=True)
    assert respects(G, R)  # the unrestricted class respects every garbling
    P = rng.random((2, 3)); P /= P.sum(1, keepdims=True)
    ok, _ = r_dominates(P, P @ G, R)
    assert ok


def test_factoring_compatible_garbling():
    rng = np.random.default_rng(1)
    f = [0, 1, 1, 0]
    T = deterministic_map(f, 2)
    G = compatible_garbling(rng, f, 2)
    assert factors_through(G, T)
    assert respects(G, factoring_class(T, 2))
    swap = np.eye(4)[[1, 0, 2, 3]]  # moves x0 (fibre 0) to x1 (fibre 1) only
    assert not factors_through(swap, T)
    assert not respects(swap, factoring_class(T, 2))
