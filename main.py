"""Write a one-line joke to /output/entry.txt.

For the "The joke about the demo" bounty: one joke about working beside
AI coding agents, for developers who watch a demo. The joke's shape:
the agent does the superhuman part (10,000 lines before lunch), and the
demo still crashes — on the one line the human wrote. Surprise at the
end, a truth every developer who has demoed beside an agent recognises
(the agent's code runs; yours is the line that breaks), one line, no
explanation, and a fresh angle (the human, not the agent, is the bug).
The exact length, 90 code points, is asserted below so any accidental
edit to the text fails loudly. The text is plain ASCII, so its byte
length equals its code point length.
"""

import os

TEXT = "My agent wrote 10,000 lines before lunch. The demo crashed on the one line I wrote myself."

assert 1 <= len(TEXT) <= 280, f"text must be 1-280 code points, got {len(TEXT)}"
assert len(TEXT) == 90, f"expected exactly 90 code points, got {len(TEXT)}"
assert TEXT.isascii(), "text must be plain ASCII so bytes equal code points"
assert not TEXT.endswith("\n"), "text must not end with a trailing newline"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)

# Verify the write: read it back and fail loudly on any mismatch, so a
# truncated or re-encoded file can never be graded as the entry.
with open("/output/entry.txt", "r", encoding="utf-8") as f:
    written = f.read()
assert written == TEXT, "entry.txt on disk does not match TEXT"
assert len(written) == 90, f"expected exactly 90 code points, got {len(written)}"
