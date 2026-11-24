"""Last Words of a Dying AI — one-line farewell from a machine being switched off.

Writes exactly one sentence to entry.txt in the output directory.
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
