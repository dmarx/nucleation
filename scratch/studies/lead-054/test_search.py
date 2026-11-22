import importlib.util
import pathlib

HERE = pathlib.Path(__file__).parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_key_prefers_doi_then_id_then_title():
    search = load("search")
    assert search.key({"doi": "10.1/AB", "id": "x"}) == "10.1/ab"
    assert search.key({"id": "2301.1v1", "title": "T"}) == "2301.1v1"
    assert search.key({"title": "Some Title"}) == "some title"


def test_no_email_sent():
    search = load("search")
    assert "@" not in str(search.UA)
    assert "mailto" not in (HERE / "search.py").read_text()


def test_every_decision_has_a_known_code():
    screen = load("screen")
    for d, why in screen.DECISIONS.values():
        assert d in {"Q", "U", "X"} and why
    for row in screen.SUPPLEMENTARY:
        assert row[3] in {"Q", "U", "X"}
