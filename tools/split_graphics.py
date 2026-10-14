#!/usr/bin/env python3
"""Rebuilds data/ from Make Me a Hanzi's graphics.txt.

    python3 tools/split_graphics.py path/to/graphics.txt characters.txt

characters.txt: the characters to keep, in any layout. Each output file is
the character's line of graphics.txt plus a "notice" (Arphic Public
License, section 2a). The strokes and medians are copied unchanged.
"""
import json
import os
import sys
from datetime import date

NOTICE = ("Modified {today} by Tupo: this character's line was copied out of Make Me a Hanzi's graphics.txt "
          "into a file of its own. The strokes and medians are unchanged. Derived from the Arphic PL KaitiM GB "
          "and UKai fonts; licensed under the Arphic Public License, see ARPHICPL.TXT.")


def main(graphics_path, characters_path):
    with open(characters_path, encoding="utf-8") as f:
        wanted = set(f.read()) - set(" \n\t")
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    os.makedirs(out_dir, exist_ok=True)
    notice = NOTICE.format(today=date.today().isoformat())
    with open(graphics_path, encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            if entry["character"] in wanted:
                data = {"character": entry["character"], "strokes": entry["strokes"],
                        "medians": entry["medians"], "notice": notice}
                name = "strokes-%x.json" % ord(entry["character"])
                with open(os.path.join(out_dir, name), "w", encoding="utf-8") as out:
                    json.dump(data, out, ensure_ascii=False, separators=(",", ":"))
                    out.write("\n")


if __name__ == "__main__":
    main(*sys.argv[1:3])
