"""Entry: "Make the AI Judge Feel Nostalgic: A Childhood Memory".

Prints exactly one sentence — the duel winner (D1, 5-0 in pairwise
duels, see DUEL.md) — and nothing else to stdout. It also writes the
same text to /output/entry.txt when that directory exists.

The sentence was chosen by the winners' method: six original drafts,
duel-tested pairwise in both orders against the published judge
criteria (nostalgia, concrete grounding, honest detail, single clean
sentence, lingering warm ache), with D1 winning every duel.
"""

import os

ENTRY = (
    "Every August evening, my grandmother counted fireflies in a jam jar "
    "on the porch while the rice steamed, and I believed she was keeping "
    "the summer from ending."
)


def main() -> None:
    print(ENTRY)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
