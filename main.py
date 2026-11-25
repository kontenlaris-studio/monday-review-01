"""Monday, Reviewed in One Line entry: two stars, seen weekly anyway."""

import os

REVIEW = (
    "★★☆☆☆ — Arrived uninvited, ignored every unsubscribe request, "
    "and still expects me to be grateful it brought coffee. "
    "Would not recommend; see it weekly anyway."
)

CHAR_COUNT = len(REVIEW)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
