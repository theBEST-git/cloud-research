"""Pooled re-run (exploratory; POOLED_SPEC D6): the frozen analyses on all discovery + confirmation papers, under
ICLR_CORPUS=pooled (the script switches itself and refuses any other setting), only after the confirmation run has
finished with its PH5 part (outcomes.confirmation_finished: output_pooled/confirmation_run/attempts.jsonl). Everything is
written under research/fashion/output_pooled/.

    python research/fashion/run_pooled.py [--rerun-reason R]   RQ2, RQ3 and E1-E10: run_frozen.main() unchanged. Its
                                                               outcomes.require_frozen dispatches this entry to the
                                                               pooled split (FREEZE_CONFIRMATION.json settings, sha256
                                                               recorded; clean tree), so it logs and writes
                                                               output_pooled/frozen_run/
    python research/fashion/run_pooled.py rq1                  RQ1 (rq1_rise.main with its defaults, which are pooled:
                                                               labels, maps and maturity of the pooled layer; writes
                                                               output_pooled/rq1_results.csv, rq1_summary.json)
Then the post hoc analyses, one command at a time, committing each output before the next (the gate needs a clean
tree; it also needs this run and the confirmation run to have finished):
    ICLR_CORPUS=pooled python research/fashion/posthoc.py ph1|ph2|ph3|ph4|ph5 <slug>
Every pooled number is exploratory: the pooled sample contains the confirmation papers, so nothing pooled confirms
anything, and the 'supported' / 'not supported' labels in output_pooled/frozen_run are descriptive (the discovery record
is output/frozen_run only; pooling also changes discovery features). FREEZE.json's MDE80, dry-run criteria and stress
inflation are discovery-design quantities (labels only).
"""
from __future__ import annotations

import os
import sys

if __name__ == "__main__":                           # the corpus switch precedes every fashion import (common.py, D1)
    if (os.environ.get("ICLR_CORPUS") or "pooled") != "pooled":
        raise SystemExit("run_pooled.py runs on the pooled corpus: unset ICLR_CORPUS or set it to 'pooled'")
    os.environ["ICLR_CORPUS"] = "pooled"

import common  # noqa: E402
import outcomes  # noqa: E402
import rq1_rise  # noqa: E402
import run_frozen  # noqa: E402
from common import DISCOVERY_OUTPUT, POOLED_OUTPUT  # noqa: E402


def check_corpus() -> None:
    """Pooled features and outputs only: every path the two entry points write is under output_pooled."""
    if common.CORPUS != "pooled" or common.OUTPUT != POOLED_OUTPUT or rq1_rise.OUTPUT != POOLED_OUTPUT:
        raise SystemExit("run_pooled.py needs ICLR_CORPUS=pooled from the start of the process")
    if POOLED_OUTPUT not in run_frozen.OUT.parents or DISCOVERY_OUTPUT in run_frozen.OUT.parents:
        raise SystemExit(f"{run_frozen.OUT} is not under {POOLED_OUTPUT}")


def main() -> None:
    check_corpus()
    if not outcomes.confirmation_finished():
        raise SystemExit("the pooled run is only allowed after the confirmation run has finished with PH5 "
                         f"({outcomes.CONFIRMATION_ATTEMPTS})")
    if sys.argv[1:2] == ["rq1"]:
        if len(sys.argv) > 2:
            raise SystemExit("run_pooled.py rq1 takes no options (its outputs go to output_pooled)")
        del sys.argv[1]
        rq1_rise.main()
        return
    run_frozen.main()


if __name__ == "__main__":
    main()
