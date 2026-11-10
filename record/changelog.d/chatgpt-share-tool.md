### Added

- `scratch/tools/chatgpt_share.py` decodes a saved ChatGPT share page into the verbatim exchange the record files from. It writes the shared branch only, as numbered U and A turns, and stops with an error and prints nothing if the page format has changed. Its tests are in `scratch/tools/test_chatgpt_share.py`. Run on this session's two shares, it gives the same text as the earlier ad hoc decoder.

### Changed

- Step 1 of the `read-and-file` skill says how to fetch a share link with curl and decode it.
