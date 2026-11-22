import importlib.util, os

spec = importlib.util.spec_from_file_location("sample", os.path.join(os.path.dirname(__file__), "sample.py"))
sample = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample)

MD = """# x
## Config Errors
[A](https://a.example/1). text
[B](https://b.example/2). text
[A](https://a.example/1). dup
## Uncategorized
[C](https://c.example/3). text
## Other lists of postmortems
[D](https://d.example/4). not a candidate
"""


def test_candidates_sections_and_dedup():
    assert sample.candidates(MD) == ["https://a.example/1", "https://b.example/2", "https://c.example/3"]


def test_shuffle_is_deterministic():
    u = [str(i) for i in range(50)]
    assert sample.shuffled(u) == sample.shuffled(u)
    assert sorted(sample.shuffled(u)) == sorted(u)


def test_strip():
    assert sample.strip("<p>a<script>x</script> &amp; b</p>") == "a & b"
