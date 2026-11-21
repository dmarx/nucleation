### Changed

- `scratch/tools/chatgpt_share.py` now accounts for all the assistant content on a share's branch, at the owner's request of 2026-11-21. Under each visible assistant turn it adds, as labelled blocks marked "not shown on the share page":
  - the assistant's reasoning summaries and recaps;
  - code it ran, and that code's output (stored in `content.text`, which the decoder used to miss);
  - tool calls that carry text;
  - hidden drafts that hold a line of their own.

  Hidden copies whose every line appears in a visible turn, empty messages, tool calls without text and web results are counted in a closing line, so nothing is dropped without a trace. `--visible_only` reproduces the old output byte for byte. On the share "Rich Get Richer Power Laws" every one of 292 assistant messages and 95 tool messages is in the file or the count. The `read-and-file` skill's step 1 describes the new output.
