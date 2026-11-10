# scratch/tools/test_chatgpt_share.py: tests for the ChatGPT share decoder
# run: python3 -m pytest scratch/tools/test_chatgpt_share.py
"""Builds synthetic share pages in the format the decoder expects (a
turbo-stream value table split across `streamController.enqueue(...)`
script calls) and checks what comes out."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import chatgpt_share as cs  # noqa: E402


def encode(obj) -> list:
    """Flatten obj into a turbo-stream value table: dict keys become `_<i>`
    pointers to string entries, and values become indices."""
    table: list = []

    def add(v) -> int:
        if v is None:
            return -5
        i = len(table)
        table.append(None)
        if isinstance(v, dict):
            table[i] = {f"_{add(k)}": add(val) for k, val in v.items()}
        elif isinstance(v, list):
            table[i] = [add(x) for x in v]
        else:
            table[i] = v
        return i

    add(obj)
    return table


def page(obj, chunks: int = 3) -> str:
    data = json.dumps(encode(obj)) + "\n"
    step = max(1, len(data) // chunks + 1)
    parts = [data[i:i + step] for i in range(0, len(data), step)]
    scripts = "".join(
        f"<script>window.__reactRouterContext.streamController.enqueue({json.dumps(p)});</script>"
        for p in parts)
    return f"<html><head><title>t</title></head><body>{scripts}</body></html>"


def msg(role, text, t=1_700_000_000, **extra):
    m = {"author": {"role": role}, "content": {"content_type": "text", "parts": [text]},
         "create_time": t, "metadata": {}}
    m.update(extra)
    return m


def conversation():
    """root -> u1 -> a1 -> u2 -> {a2 (current branch), a2x (abandoned branch)},
    plus a system message, a tool call and a hidden message on the branch."""
    nodes = {
        "root": {"message": None, "parent": None},
        "sys": {"message": msg("system", "you are helpful"), "parent": "root"},
        "u1": {"message": msg("user", "first question"), "parent": "sys"},
        "tool": {"message": msg("assistant", "search(x)", recipient="browser"), "parent": "u1"},
        "a1": {"message": msg("assistant", "first answer"), "parent": "tool"},
        "hid": {"message": msg("user", "hidden context",
                               metadata={"is_visually_hidden_from_conversation": True}), "parent": "a1"},
        "u2": {"message": msg("user", "second question"), "parent": "hid"},
        "a2x": {"message": msg("assistant", "abandoned answer"), "parent": "u2"},
        "a2": {"message": msg("assistant", "kept answer"), "parent": "u2"},
    }
    return {"loaderData": {"share": {"serverResponse": {"data": {
        "title": "A test exchange", "current_node": "a2", "mapping": nodes}}}}}


def test_turns_follow_the_shared_branch_and_number_each_voice():
    turns = cs.decode(page(conversation()))
    assert [(t.label, t.text) for t in turns.turns] == [
        ("U1", "first question"), ("A1", "first answer"),
        ("U2", "second question"), ("A2", "kept answer")]
    assert turns.title == "A test exchange"


def test_render_writes_headed_blocks():
    out = cs.render(cs.decode(page(conversation())))
    assert out.startswith("TITLE: A test exchange\n")
    assert "===== U1 (user) 2023-11-14 22:13 UTC =====\nfirst question\n" in out
    assert "abandoned answer" not in out and "search(x)" not in out and "hidden context" not in out


def test_multimodal_parts_keep_their_text():
    conv = conversation()
    node = conv["loaderData"]["share"]["serverResponse"]["data"]["mapping"]["u1"]
    node["message"]["content"] = {"content_type": "multimodal_text",
                                  "parts": [{"asset_pointer": "file-1"}, "with a picture"]}
    turns = cs.decode(page(conv))
    assert turns.turns[0].text == "with a picture"


def test_a_page_without_the_payload_fails_loudly():
    with pytest.raises(cs.ShareFormatError, match="streamController"):
        cs.decode("<html><body>Just a moment...</body></html>")


def test_a_payload_without_a_conversation_fails_loudly():
    with pytest.raises(cs.ShareFormatError, match="mapping"):
        cs.decode(page({"loaderData": {"nothing": "here"}}))
