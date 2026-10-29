"""Write and run Jupyter notebooks with nothing but the standard library.

build() runs each code cell the way Jupyter does (in one shared
namespace, showing printed text and the value of the last line) and
saves the notebook with its outputs, so GitHub shows the results.
run() executes an existing notebook's code cells, for the tests."""

from __future__ import annotations

import ast
import contextlib
import io
import json
import os
from pathlib import Path


def _lines(text: str) -> list[str]:
    parts = text.splitlines(keepends=True)
    return parts or [""]


def execute(code: str, namespace: dict) -> tuple[str, str | None]:
    """Run one cell; return (printed text, repr of the last value)."""
    tree = ast.parse(code)
    last = None
    if tree.body and isinstance(tree.body[-1], ast.Expr):
        last = ast.Expression(tree.body.pop().value)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        # Running notebook cells is the whole point of this module
        exec(compile(tree, "<cell>", "exec"), namespace)
        value = (
            eval(compile(last, "<cell>", "eval"), namespace)
            if last
            else None
        )
    return out.getvalue(), None if value is None else repr(value)


def build(path: Path, cells: list[tuple[str, str]]) -> None:
    """cells: ("md", text) or ("code", source)."""
    namespace: dict = {"__name__": "__main__"}
    nb_cells, count = [], 0
    here = os.getcwd()
    os.chdir(path.parent)  # cells run from the notebooks folder
    try:
        for kind, source in cells:
            source = source.strip("\n")
            if kind == "md":
                nb_cells.append(
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": _lines(source),
                    }
                )
                continue
            count += 1
            printed, value = execute(source, namespace)
            outputs = []
            if printed:
                outputs.append(
                    {
                        "output_type": "stream",
                        "name": "stdout",
                        "text": _lines(printed),
                    }
                )
            if value is not None:
                outputs.append(
                    {
                        "output_type": "execute_result",
                        "execution_count": count,
                        "metadata": {},
                        "data": {"text/plain": _lines(value)},
                    }
                )
            nb_cells.append(
                {
                    "cell_type": "code",
                    "execution_count": count,
                    "metadata": {},
                    "outputs": outputs,
                    "source": _lines(source),
                }
            )
    finally:
        os.chdir(here)
    notebook = {
        "cells": nb_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(
        json.dumps(notebook, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def run(path: Path) -> None:
    """Execute every code cell of a saved notebook, in order."""
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace: dict = {"__name__": "__main__"}
    here = os.getcwd()
    os.chdir(path.parent)
    try:
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                execute("".join(cell["source"]), namespace)
    finally:
        os.chdir(here)
