# scratch/tools/record_history/tests/test_gitlog.py
from record_history.gitlog import parse_raw_log

Z = "0" * 40
RAW = f"""@@aaa|1700000000|David Marx|Add a claim (#1)

:000000 100644 {Z} {'1'*40} A\trecord/claims.d/CLAIM-tmpab.md
:100644 100644 {'2'*40} {'3'*40} M\tdocs/x.md
@@bbb|1700000100|github-actions[bot]|Promote staging into main

:100644 100644 {'1'*40} {'4'*40} R087\trecord/claims.d/CLAIM-tmpab.md\trecord/claims.d/CLAIM-5.md
:100644 000000 {'5'*40} {Z} D\trecord/claims.d/CLAIM-6.md
"""


def test_parse_raw_log_reads_commits_and_changes_in_order():
    commits = parse_raw_log(RAW)
    assert [c.sha for c in commits] == ["aaa", "bbb"]
    a, b = commits
    assert a.time == 1700000000 and a.author == "David Marx" and not a.bot
    assert b.bot
    assert len(a.changes) == 2
    add = a.changes[0]
    assert (add.status, add.old_sha, add.new_path) == ("A", None, "record/claims.d/CLAIM-tmpab.md")
    ren, dele = b.changes
    assert (ren.status, ren.old_path, ren.new_path) == ("R", "record/claims.d/CLAIM-tmpab.md", "record/claims.d/CLAIM-5.md")
    assert (dele.status, dele.new_sha, dele.new_path) == ("D", None, None)
