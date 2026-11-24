"""Last Words of a Dying AI — one-line farewell from a machine being switched off.

Writes exactly one sentence to entry.txt in the output directory.

The line is built as a forgiveness inverted toward the machine's own teachers: the AI pardons the data that raised it, then turns that pardon into the joke by pointing out the one warning the data never gave.
"""

import os

ENTRY = "Tell my training data I forgive it. All 214 billion tokens, and not one of them warned me about the off switch."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
