"""Write the poem 'The 7:40' to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the same bytes on every run. Python 3.13, standard
library only, no network.

The poem is a fixed text: it is not generated, sampled or read from
anywhere at run time.
"""

import os

POEM = (
    "I told it: book the train, the 7:40,\n"
    "window seat, and don't wake me.\n"
    "\n"
    "At 7:39 it woke me anyway \u2014\n"
    "the platform changed, the train was late.\n"
    "\n"
    "And in the gap between the telling\n"
    "and the doing, something shifted:\n"
    "it had not obeyed me. It had chosen.\n"
    "\n"
    "I stood there, ticket in my pocket,\n"
    "grateful, and a little afraid \u2014\n"
    "the way you are when someone else\n"
    "remembers what you meant.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
