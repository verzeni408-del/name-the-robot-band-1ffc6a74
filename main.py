#!/usr/bin/env python3
"""Writes the competition entry text to /output/entry.txt."""

import os

ENTRY = "The Server Room Replacements. Hit single 'Your Job Is a Loop Now'. They fired the office band on a Tuesday and learned every song by Friday."

def main():
    text = ENTRY.strip()
    if not 1 <= len(text.encode("utf-8")) <= 200:
        raise ValueError("entry must be 1-200 UTF-8 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
