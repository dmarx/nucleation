# scratch/tools/record_history/tests/test_handcheck.py
from record_history.handcheck import CLASSES, stratified


def test_stratified_draws_k_per_class_deterministically_and_skips_bots_for_substantive():
    rows = [{"kind": k, "code": f"CLAIM-{i}", "commit": f"c{i}", "bot": False, "breadth": 1}
            for i, k in enumerate(["body", "statement", "relation_add", "status", "note", "mechanical"] * 20)]
    a = stratified(rows, k=3, seed=1)
    b = stratified(rows, k=3, seed=1)
    assert a == b
    assert {c: len(v) for c, v in a.items()} == {c: 3 for c in CLASSES}
    assert all(r["kind"] in ("body", "statement") for r in a["revised"])
