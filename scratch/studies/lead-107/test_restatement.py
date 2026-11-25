import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import restatement as r  # noqa: E402


def test_classify_new_cues():
    assert r.classify("The objection (CLAIM-024) was re-derived three times.") == "new"
    assert r.classify("A3's question is QUESTION-257 almost verbatim, uncited;") == "new"
    assert r.classify("A39 treated resolve as new.") == "new"
    assert r.classify("A10 offered Pettit, already held.") == "new"


def test_already_held_needs_turn_or_proposal():
    assert r.classify("Two works were already held (LIT-323).") == "neutral"
    assert r.classify("A5 proposed two works already held.") == "new"


def test_proof_check_voids_rederivation():
    assert r.classify("Step 3 was re-derived by hand here.") is None
    assert r.classify("The proof was re-derived and restated.") == "neutral"


def test_retrieved_and_conflict():
    assert r.classify("A cites CLAIM-287 where it came back.") == "retrieved"
    assert r.classify("CLAIM-122 (re-derived again, this time cited)") == "conflict"
    assert r.classify("restated without citing CLAIM-593") == "new"
    assert r.classify("A4 cited none of it, again.") == "new"


def test_v2_repairs():
    s = "The recurring strength was accuracy: of the 133 codes cited, all right."
    assert r.classify(s, "v1") == "retrieved"
    assert r.classify(s, "v2") is None
    s2 = "Not filed: logic, for which no work was cited; the benchmark, which A30 restates."
    assert r.classify(s2, "v1") == "retrieved"
    assert r.classify(s2, "v2") == "neutral"
    assert r.classify("CLAIM-121 is Proposed again.", "v1") == "neutral"
    assert r.classify("CLAIM-121 is Proposed again.", "v2") is None


def test_items_and_coded_status():
    assert r.items_of("CLAIM-24, CLAIM-024 and TERM-072 but not ADR-032") == ["CLAIM-024", "TERM-072"]
    assert r.coded_at_time("2026-10-01", "2026-10-04")
    assert not r.coded_at_time("2026-10-04", "2026-10-04")
    assert r.coded_at_time("2026-10-04", "2026-10-04", same_day_coded=True)
    assert not r.coded_at_time(None, "2026-10-04")


def test_distance_properties():
    same = r.distance("drift is retrieval failure", "drift is retrieval failure")
    assert all(abs(v) < 1e-9 for v in same.values())
    far = r.distance("bananas ripen slowly", "drift is retrieval failure")
    assert far["d_jac"] == 1.0 and far["d_cov"] == 1.0
    near = r.distance("retrieval failures cause drift", "drift is retrieval failure")
    assert 0 < near["d_jac"] < far["d_jac"]


def test_quotes_and_sentences():
    assert r.quotes('A said "one two three" and “four five”.') == ["one two three", "four five"]
    ss = r.sentences("First one. Second (A2) one.\n\n- A bullet; Another clause.")
    assert ss == ["First one.", "Second (A2) one.", "A bullet;", "Another clause."]


def test_corpus_rule_and_date():
    body = " ".join(f"U{i} A{i}" for i in range(6))
    assert r.is_exchange_reconstruction({"title": "Session of 2026-10-04: x"}, body)
    assert not r.is_exchange_reconstruction({"title": "The tenth status review"}, body)
    assert not r.is_exchange_reconstruction({"title": "Session of 2026-10-11, continued"}, "no labels")
    assert r.exchange_date({"title": "Session of 2026-10-04, morning"}) == ("2026-10-04", False)
    assert r.exchange_date({"title": "Exchange X (undated)", "created": "2026-10-26T19:51:31"}) == ("2026-10-26", True)


def _write(p: Path, text: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def test_end_to_end(tmp_path):
    _write(tmp_path / "record/claims.d/CLAIM-001.md",
           "---\ntitle: 'Drift is retrieval failure'\ndate: '2026-10-01'\nsummary: s\n---\nbody\n")
    _write(tmp_path / "record/claims.d/CLAIM-002.md",
           "---\ntitle: 'Later claim'\ndate: '2026-10-09'\nsummary: s\n---\nbody\n")
    labels = " ".join(f"U{i} A{i}" for i in range(6))
    _write(tmp_path / "record/workbench.d/2026/10/05/000000.md",
           "---\ntitle: 'Session of 2026-10-05: test'\ncreated: '2026-10-05T00:00:00'\n---\n"
           f"{labels}\n\nA3 re-derived [CLAIM-001](x) as \"failure of drift retrieval\".\n\n"
           "A4 restated CLAIM-002 without citing it.\n\nA5 cites CLAIM-001, which came back.\n")
    _write(tmp_path / "record/workbench.d/2026/10/10/000000.md",
           "---\ntitle: 'Session of 2026-10-10: later'\ncreated: '2026-10-10T00:00:00'\n---\n"
           f"{labels}\n\nA2 re-derived CLAIM-002, uncited.\n")
    res, events = r.analyse(tmp_path)
    assert res["corpus"]["reconstructions"] == 2
    cv = res["coded_vs_uncoded"]["primary"]
    # (file1, CLAIM-001): new beats retrieved; (file1, CLAIM-002) uncoded new; (file2, CLAIM-002) coded new
    assert cv["coded"]["new"] == 2 and cv["uncoded"]["new"] == 1
    ba = res["before_after"]["summary"]
    assert ba["codes_rederived_pre"] == 1 and ba["of_those_rederived_again_post"] == 1
    assert res["distance"]["n"] == 1
