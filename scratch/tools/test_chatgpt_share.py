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
    assert "abandoned answer" not in out and "hidden context" not in out


def test_visible_only_keeps_the_old_output():
    out = cs.render(cs.decode(page(conversation()), visible_only=True))
    assert "search(x)" not in out and "-----" not in out


def test_multimodal_parts_keep_their_text():
    conv = conversation()
    node = conv["loaderData"]["share"]["serverResponse"]["data"]["mapping"]["u1"]
    node["message"]["content"] = {"content_type": "multimodal_text",
                                  "parts": [{"asset_pointer": "file-1"}, "with a picture"]}
    turns = cs.decode(page(conv))
    assert turns.turns[0].text == "with a picture"


def test_a_page_without_the_payload_fails_loudly():
    with pytest.raises(cs.ShareFormatError, match="streamController.*octane"):
        cs.decode("<html><body>Just a moment...</body></html>")


def test_a_payload_without_a_conversation_fails_loudly():
    with pytest.raises(cs.ShareFormatError, match="mapping"):
        cs.decode(page({"loaderData": {"nothing": "here"}}))


def octane_page(rows, title="Branch · An exchange") -> str:
    """A share page in the 2026-11 format: the transcript as one JSON script."""
    body = json.dumps({"label": "Conversation", "rows": rows}).replace("</", "<\\/")
    return (f"<html><head><title>{title}</title></head><body>"
            f'<script id="octane-conversation-transcript" type="application/json">{body}</script>'
            "</body></html>")


def octane_user(text):
    return {"key": "u", "frame": {"role": "user", "text": text}}


def octane_assistant(markdown="", fallback="", links=()):
    consts = {str(i): t for i, (_, t) in enumerate(links)}
    code = "".join(f'__dil.jsx(Link,{{"url":"{u}"}},__dilConstants["{i}"])'
                   for i, (u, _) in enumerate(links))
    return {"key": "a", "frame": {"role": "assistant"},
            "source": {"markdown": markdown,
                       "dil": {"code": code, "constants": consts, "fallbackMarkdown": fallback}}}


def test_octane_pages_decode_both_voices_in_order():
    rows = [octane_user("first question"), octane_assistant(markdown="first answer"),
            octane_user("second question"), octane_assistant(fallback="second answer")]
    ex = cs.decode(octane_page(rows))
    assert ex.title == "Branch · An exchange"
    assert [(t.label, t.text) for t in ex.turns] == [
        ("U1", "first question"), ("A1", "first answer"),
        ("U2", "second question"), ("A2", "second answer")]


def test_octane_links_dropped_from_the_fallback_are_listed_in_order():
    rows = [octane_user("q"), octane_assistant(
        fallback="see , and also .",
        links=[("https://example.org/a", "CLAIM-1"), ("https://example.org/b", "TERM-2")])]
    text = cs.decode(octane_page(rows)).turns[1].text
    assert text.startswith("see , and also .")
    assert text.endswith("[links in this turn, in order, whose text the fallback drops:\n"
                         "  CLAIM-1 <https://example.org/a>\n  TERM-2 <https://example.org/b>]")


def test_an_octane_assistant_turn_without_text_fails_loudly():
    with pytest.raises(cs.ShareFormatError, match="no text"):
        cs.decode(octane_page([octane_user("q"), octane_assistant()]))


# --- everything else the assistant said, beside its visible turns ---

def rich_conversation():
    """u1 -> reasoning -> tool call -> tool result -> code -> code output ->
    hidden copy of the answer -> visible answer -> hidden draft with a line of its own
    -> u2 -> a2."""
    def thoughts(summary, content):
        m = msg("assistant", "")
        m["content"] = {"content_type": "thoughts",
                        "thoughts": [{"summary": summary, "content": content}]}
        return m

    def code(src):
        m = msg("assistant", "", recipient="python")
        m["content"] = {"content_type": "code", "language": "unknown", "text": src}
        return m

    def tool(text, ctype="text", name="web.run"):
        m = msg("tool", text)
        m["author"] = {"role": "tool", "name": name}
        m["content"]["content_type"] = ctype
        if ctype == "execution_output":  # as the share stores it: in `text`, not `parts`
            m["content"] = {"content_type": ctype, "text": text}
        return m

    recap = msg("assistant", "")
    recap["content"] = {"content_type": "reasoning_recap", "content": "Worked for 46s"}
    hidden = {"metadata": {"is_visually_hidden_from_conversation": True}}
    chain = [
        ("u1", msg("user", "a question")),
        ("th", thoughts("Planning", "I will compute a number.")),
        ("call", msg("assistant", "", recipient="web.run")),
        ("res", tool("a page of search results")),
        ("code", code("print(6*7)")),
        ("out", tool("42", ctype="execution_output", name="python")),
        ("recap", recap),
        ("dup", msg("assistant", "The answer is 42.\nIt is computed.", **hidden)),
        ("a1", msg("assistant", "The answer is 42.\nIt is computed.\nMore follows.")),
        ("draft", msg("assistant", "The answer is 42.\nA line only the draft has.", **hidden)),
        ("u2", msg("user", "thanks")),
        ("a2", msg("assistant", "welcome")),
    ]
    nodes, parent = {"root": {"message": None, "parent": None}}, "root"
    for key, m in chain:
        nodes[key] = {"message": m, "parent": parent}
        parent = key
    return {"loaderData": {"share": {"serverResponse": {"data": {
        "title": "Rich", "current_node": parent, "mapping": nodes}}}}}


def test_the_visible_turns_are_unchanged_by_the_extras():
    ex = cs.decode(page(rich_conversation()))
    assert [(t.label, t.text) for t in ex.turns] == [
        ("U1", "a question"), ("A1", "The answer is 42.\nIt is computed.\nMore follows."),
        ("U2", "thanks"), ("A2", "welcome")]


def test_reasoning_code_and_its_output_attach_to_the_turn_they_lead_to():
    a1 = cs.decode(page(rich_conversation())).turns[1]
    kinds = [k for k, _ in a1.extras]
    assert kinds[:4] == ["reasoning", "code", "code output", "reasoning recap"]
    texts = dict(a1.extras)
    assert texts["reasoning"] == "Planning: I will compute a number."
    assert texts["code"] == "print(6*7)" and texts["code output"] == "42"
    assert texts["reasoning recap"] == "Worked for 46s"


def test_a_hidden_copy_of_visible_text_is_counted_not_repeated():
    ex = cs.decode(page(rich_conversation()))
    a1 = ex.turns[1]
    assert not any(t == "The answer is 42.\nIt is computed." for _, t in a1.extras)
    assert ex.omitted["hidden copies wholly contained in visible turns"] == 1


def test_a_hidden_draft_with_lines_of_its_own_is_kept_whole():
    a1 = cs.decode(page(rich_conversation())).turns[1]
    assert ("hidden draft", "The answer is 42.\nA line only the draft has.") in a1.extras


def test_empty_tool_calls_and_web_results_are_counted_not_printed():
    ex = cs.decode(page(rich_conversation()))
    out = cs.render(ex)
    assert "a page of search results" not in out
    assert ex.omitted["tool calls without text (web.run)"] == 1
    assert ex.omitted["tool results (web.run)"] == 1


def test_render_labels_each_extra_and_ends_with_the_omissions():
    out = cs.render(cs.decode(page(rich_conversation())))
    assert "----- A1 · reasoning (not shown on the share page) -----\nPlanning: I will compute a number.\n" in out
    assert "----- A1 · code (not shown on the share page) -----\nprint(6*7)\n" in out
    assert out.rstrip().endswith("tool results (web.run): 1]")
    assert out.index("===== A1") < out.index("----- A1 · reasoning") < out.index("===== U2")


def test_visible_only_drops_every_extra():
    ex = cs.decode(page(rich_conversation()), visible_only=True)
    assert all(not t.extras for t in ex.turns) and not ex.omitted


def test_an_empty_assistant_message_is_counted_not_silently_dropped():
    conv = rich_conversation()
    nodes = conv["loaderData"]["share"]["serverResponse"]["data"]["mapping"]
    ctx = msg("assistant", "")
    ctx["content"] = {"content_type": "model_editable_context", "model_set_context": ""}
    nodes["ctx"] = {"message": ctx, "parent": "u1"}
    nodes["th"]["parent"] = "ctx"
    assert cs.decode(page(conv)).omitted["empty model context"] == 1
