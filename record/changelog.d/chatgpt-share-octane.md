### Changed

- The ChatGPT share decoder (`scratch/tools/chatgpt_share.py`) reads the
  share-page format seen on 2026-11-15, which carries the transcript as one
  `octane-conversation-transcript` JSON script instead of a turbo-stream
  payload. The old format still decodes. The new format drops the text of
  inline links from an assistant turn, so the decoder lists each turn's
  links, in order, at the end of the turn instead of guessing where they
  went. The new format carries no turn times.
