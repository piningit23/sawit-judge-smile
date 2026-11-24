"""Make the Judge Smile — entry line.

Why this line, against the judge brief (warmth, surprise, one concrete
detail, fresh wording):
- Warmth: a stranger's small kindness, felt rather than reported — the
  driver refuses the change and the grandmother carries the smile home.
- Surprise: the turn is the waived change — the fare becomes a gift,
  "For your tea, Bu."
- Concreteness: one real detail — a grandmother counting her coins,
  an ojek driver, the exact words he said.
- Fresh wording: no greeting-card phrasing; the scene is told in its
  own words, with the Indonesian "Bu" kept as spoken.

The entry is 160 characters, one line, no trailing newline.
"""

ENTRY = (
    "This morning the ojek driver waited while my grandmother counted "
    "her coins, then waved off the change and said, 'For your tea, Bu.' "
    "She smiled all the way home."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    # Guard: the entry must be one line, 1-200 characters, not blank,
    # with no leading or trailing whitespace.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line with no edge whitespace")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Verify what landed on disk is exactly the entry, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt does not match the entry")


if __name__ == "__main__":
    main()
