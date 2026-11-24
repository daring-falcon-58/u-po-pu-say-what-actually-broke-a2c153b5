#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line, the software error message a product shows its user,
to /output/entry.txt. Deterministic: no network, no randomness, no input,
no environment, no secrets. Gate: 1-200 UTF-8 characters, not only whitespace.
"""
import os

ENTRY = "Undo undid the wrong thing. Redo will redo the wrong thing harder. Save what's left and walk away."

assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
assert ENTRY.strip(), "entry is only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

with open("/output/entry.txt", encoding="utf-8") as f:
    written = f.read()

assert written == ENTRY, "re-read mismatch"
print(ENTRY)
