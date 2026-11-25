"""Write one childhood-memory sentence to /output/entry.txt.

Stdlib only, deterministic, no network. The entry is a single sentence
(<= 280 chars, no trailing newline) about the first bicycle ride without
training wheels: a father's hand letting go, the wobble, the scraped
knee, and the sudden flying feeling of staying upright.
"""

import os

SENTENCE = (
    "My father ran beside my wobbling bicycle down our gravel street at "
    "dusk, his hand steady on the seat, and when he let go I kept "
    "pedalling \u2014 knees scraped, heart pounding \u2014 suddenly flying "
    "on my own."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.endswith(".") and text.count(".") == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
