#!/usr/bin/env python3
"""agency-poem-01 round 2: "The Last Watch".

A lighthouse keeper's forty years end when a machine takes the light.
The machine is perfect at the job and that is the trouble: it never
sleeps, never blinks, writes nothing down. On his last night, in a
storm, the father climbs the stairs anyway and keeps the watch by
hand. The poem hands the lamp to the agent and keeps the pencil --
the human judgement no measurement can replace.
"""

import os
from pathlib import Path

POEM = """The Last Watch

For forty years my father kept the light.
He climbed the stairs at dusk, lit the lamp,
and wrote in the logbook, in pencil:
wind, tide, and whether the sea was lying.

The company sent a machine to replace him.
It never sleeps. It never blinks.
It writes nothing down.

On his last night a storm came in.
The machine did what it was built to do:
it shone, steady, through the rain.
My father climbed the stairs anyway,
lit the lamp by hand, and sat beside it
until morning.

A machine can keep the light.
Only a man can keep the watch.
Tonight I hand you the lamp, the logbook,
the wind, the tide.
You can have the light.
I'll keep the pencil.
"""


def main() -> None:
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(POEM, encoding="utf-8")  # 675 chars


if __name__ == "__main__":
    main()
