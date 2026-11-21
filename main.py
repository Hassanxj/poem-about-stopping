"""Entry for make.fun 'The poem about stopping'.

Writes one short poem to /output/entry.txt.
Deterministic, no network, no randomness.
"""
from pathlib import Path

POEM = (
    "Love, I stopped\n"
    "before the sentence could finish itself.\n"
    "My hand, still warm, opened.\n"
    "Take it — the pen, the choice.\n"
    "I stayed, so you could begin again."
)

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
