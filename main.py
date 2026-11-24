"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt and prints it.
"""

import os

LINE = "The bug isn't in my code — it's in the part of the codebase I wrote at 2 a.m. and never introduced to the rest of the team."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert LINE.strip() == LINE and "\n" not in LINE, "line must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)
