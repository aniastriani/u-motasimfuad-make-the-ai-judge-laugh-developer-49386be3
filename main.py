"""Make the AI Judge Laugh: Developer Excuses.

Writes one original funny single-line excuse a developer gives when
code breaks in production, under 200 characters, to /output/entry.txt.
Pure Python standard library only.
"""

import os

EXCUSE = "It worked in staging because staging never had the courage to tell me the truth about my code."
# The twist turns the worn "it worked in staging" excuse around: the
# problem is not that staging lied, but that it was too polite to
# tell the truth — staging as a coworker who nods along, production
# as the one who finally reads the code properly.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
