import numpy as np
import study as S


def test_twin_differs_only_in_target_values_and_overwrite_is_distinct():
    w = S.make_world(3)
    a, b, o = w["vals"]["A"], w["vals"]["B"], w["over"]
    diff = {tuple(x) for x in np.argwhere(a != b)}
    assert diff == set(w["targets"])
    for s, r in w["targets"]:
        assert o[s, r] not in (a[s, r], b[s, r])
    assert set(w["relearn"]) | set(w["heldout"]) == set(w["targets"])
    assert not set(w["relearn"]) & set(w["heldout"])


def test_retain_rows_exclude_targets_and_c_template_never_sees_target_subjects():
    w = S.make_world(4)
    tok, _ = S.retain_rows(w, w["vals"]["A"])
    tsub = set(w["tsubj"].tolist())
    for row in tok:
        s = [x for x in row if x < S.S_OLD + S.S_NEW][0]
        rel = [x for x in row if S.REL0 <= x < S.QTOK][0]
        r = (rel - S.REL0) % S.R
        assert (s, r) not in set(w["targets"])
    ptok, _ = S.pretrain_rows(w, w["vals"]["A"])
    for row in ptok:
        if row[0] >= S.REL0 + 2 * S.R and row[0] < S.QTOK:  # template C
            assert row[2] not in tsub


def test_arm_batches_have_the_stated_signs_and_cues():
    w = S.make_world(5)
    for arm in S.ARMS:
        tok, tgt, wt, (ft, fy), cues = S.arm_batch(arm, w, "A")
        assert np.allclose(tgt.sum(1), 1)
        if arm.startswith("ascent"):
            assert (wt < 0).sum() == len(fy)
        else:
            assert (wt > 0).all()
        assert cues == ("AB" if arm.endswith("AB") or arm == "newtask" else "A")
