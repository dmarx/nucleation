import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import study  # noqa: E402
from life import BLOCK, EATER, GLIDER_SE, board, cells_of, ring, run, step  # noqa: E402


def test_rule_blinker_and_glider():
    g = board((10, 10), [(4, 3), (4, 4), (4, 5)])
    assert cells_of(step(g)) == {(3, 4), (4, 4), (5, 4)}
    assert cells_of(run(g, 2)) == cells_of(g)
    gl = board((20, 20), GLIDER_SE)
    assert cells_of(run(gl, 4)) == {(r + 1, c + 1) for r, c in GLIDER_SE}


def test_still_lifes_are_fixed_points():
    for form in (BLOCK, EATER):
        g = board((16, 16), form, (5, 5))
        assert (step(g) == g).all()


def test_ring():
    assert len(ring(BLOCK, 1)) == 12
    assert len(ring(BLOCK, 2)) == 32


def test_sensitivity_counts_only_real_changes():
    g = board((16, 16), BLOCK, (5, 5))
    inside = [(5, 5), (5, 6), (6, 5), (6, 6)]
    # deleting one block cell is repaired in one generation, so no other block cell changes
    assert study.sensitivity(g, inside, inside, 1) == 0.0
    # a birth edge-adjacent to the block kills the two block cells next to it
    h = g.copy()
    h[4, 5] = 1
    assert cells_of(step(h)) & set(inside) == {(6, 5), (6, 6)}


def test_block_repairs_every_single_deletion_and_no_pair():
    prof = study.perturbation_profile(BLOCK)
    assert prof[0] == {"returns": 4}
    assert "returns" not in prof[1]
    assert study.pair_deletions(BLOCK) == {"empty": 6}


def test_eater_survives_its_strike_in_all_phases():
    lanes, phases = study.eater_strike_lanes()
    assert lanes[0] == "eater-exact" and all(phases)
    assert all(v != "eater-exact" for k, v in lanes.items() if k != 0)


def test_creation_run_blocks_share_cells():
    rows, lasting = study.creation_run()
    assert lasting
    live = {r["t"]: set(map(tuple, r["block_cells_live"])) for r in rows}
    assert live[20] == study.CREATION_BLOCK and live[22] != study.CREATION_BLOCK
    # two of the block's cells stay alive through the whole "destruction"
    assert all({(6, 1), (6, 2)} <= live[t] for t in range(19, 30))


def test_transient_block_loses_every_cell():
    import transient
    g = board((12, 12), BLOCK, (5, 5))
    assert transient.isolated_blocks(g) == [(5, 5)]
    found, _, _ = transient.scan(1)
    e = [x for x in found if x["t"] == 28 and tuple(x["corner"]) == (4, 9)][0]
    assert e["block_cells_live_next"][:2] == [4, 0]


def test_gun_emits_and_blocks_never_fall_below_two_cells():
    assert study.gliders_away(100) == 2
    from life import GUN_LEFT_BLOCK
    assert study.gun_block_continuity(GUN_LEFT_BLOCK, 120)["min_block_cells_live"] == 2
