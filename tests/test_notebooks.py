"""Every notebook must run from top to bottom without an error, and be
built from the current tools/build_notebooks.py."""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from build_notebooks import NOTEBOOKS
from notebook import run

FOLDER = ROOT / "notebooks"


@pytest.mark.parametrize("name", sorted(NOTEBOOKS))
def test_notebook_runs(name):
    run(FOLDER / name)


@pytest.mark.parametrize("name", sorted(NOTEBOOKS))
def test_notebook_matches_its_source(name):
    """The saved code cells are the ones in build_notebooks.py, so a
    change there can't be forgotten in the notebook."""
    saved = json.loads((FOLDER / name).read_text(encoding="utf-8"))["cells"]
    assert ["".join(c["source"]) for c in saved] == [
        text.strip("\n") for _, text in NOTEBOOKS[name]
    ]


def test_every_notebook_is_listed():
    assert {p.name for p in FOLDER.glob("*.ipynb")} == set(NOTEBOOKS)
