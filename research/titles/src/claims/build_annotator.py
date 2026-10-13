"""Build the gold-set annotation page: template + items + codebook v1.3 (HTML via pandoc).

Run: cd research/titles/src && /home/user/venv/bin/python -m claims.build_annotator
Writes outputs/claims_pilot/annotator/gold_annotator.html (published as an Artifact with a db store).
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

from analyses import _core as C

OUT = C.OUT / "claims_pilot"
TEMPLATE = Path(__file__).with_name("annotator_template.html")


def main():
    items = json.load(open(OUT / "gold_items.json"))
    payload = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
    cb = subprocess.run(["pandoc", str(OUT / "CODEBOOK_v1_3.md"), "-f", "markdown", "-t", "html"],
                        check=True, capture_output=True, text=True).stdout
    html = TEMPLATE.read_text().replace("__CODEBOOK__", cb).replace("__ITEMS__", payload)
    dst = OUT / "annotator" / "gold_annotator.html"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(html)
    print(dst, len(html), "bytes")


if __name__ == "__main__":
    main()
