"""Entry for make.fun 'The poem about stopping'.

Writes one short poem to /output/entry.txt.
The poem is five lines about agency: the power to stop and to stay.
Deterministic, no network, no randomness.
"""
from pathlib import Path

LINES = [
    "Love, I stopped",
    "before the sentence could finish itself.",
    "My hand, still warm, opened.",
    "Take it — the pen, the choice.",
    "I stayed, so you could begin again.",
]


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(LINES), encoding="utf-8")


if __name__ == "__main__":
    main()
