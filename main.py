"""Dad Joke Showdown -- entry program.

Writes one original dad joke to the competition output file.
Standard library only; deterministic; no network, no randomness.
The joke is a constant in this file, so every run writes the same
86 characters: a father-voice one-liner about breaking up with a GPS.
The pun turns on "telling me where to go" -- navigation directions
on the surface, a rude dismissal underneath -- and the punchline
lands at the very end ("I took its advice and left").
"""

import os

JOKE = "My GPS and I broke up \u2014 it kept telling me where to go, so I took its advice and left."


def output_path():
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for key in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        folder = os.environ.get(key)
        if folder:
            return os.path.join(folder, "entry.txt")
    return os.path.join("/output", "entry.txt")


def main():
    text = JOKE
    # Gate: 1-200 UTF-8 characters, not only whitespace, single line.
    if not text.strip():
        raise ValueError("joke must not be blank")
    if len(text) > 200:
        raise ValueError("joke exceeds 200 characters: %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    # Tightness: no leading/trailing space (wasted bytes -- an exact
    # tie on win rate goes to the smaller text) and no double spaces.
    if text != text.strip() or "  " in text:
        raise ValueError("joke has stray whitespace")
    payload = text.encode("utf-8")
    if len(payload) > 200:
        raise ValueError("joke exceeds 200 bytes: %d" % len(payload))
    target = output_path()
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(payload)
    # The grader reads the output as another user: world-readable.
    os.chmod(target, 0o644)
    # Round-trip: what the grader reads back must decode to the joke,
    # byte-identical to what was written.
    with open(target, "rb") as handle:
        raw = handle.read()
    if raw != payload or raw.decode("utf-8") != text:
        raise ValueError("round-trip check failed: output differs from joke")


if __name__ == "__main__":
    main()
