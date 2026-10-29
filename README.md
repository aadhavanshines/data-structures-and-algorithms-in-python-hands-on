# Data Structures and Algorithms in Python, Hands-On: the code

The tested code from the book *Data Structures and Algorithms in Python,
Hands-On* by Aadhavan Muthurengan: every data structure built from
scratch, tested, and timed against Python's own.

[![Tests](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)

## What's here

| Folder | Contents |
| --- | --- |
| `dsa/` | The data structures and algorithms, one module per chapter |
| `tests/` | Tests for every structure, including the edge cases |
| `notebooks/` | A Jupyter notebook per chapter, to run and change the code as you read |
| `benchmarks/` | Timing scripts that measure what the Big-O claims predict |
| `tools/` | The script that builds the notebooks |

## Chapters

| # | Chapter | Module | Notebook |
| --- | --- | --- | --- |
| 1 | Big-O, and measuring instead of guessing | `dsa/timing.py` | [01-measuring](notebooks/01-measuring.ipynb) |
| 2 | Python's list, dict and set under the hood | | planned |
| 3 | Dynamic arrays | `dsa/dynamic_array.py` | [03-dynamic-arrays](notebooks/03-dynamic-arrays.ipynb) |
| 4 | Linked lists | `dsa/linked_list.py` | [04-linked-lists](notebooks/04-linked-lists.ipynb) |
| 5 | Stacks and queues | `dsa/stack_queue.py` | [05-stacks-and-queues](notebooks/05-stacks-and-queues.ipynb) |
| 6 | Hash tables | | planned |
| 7 | Recursion | | planned |
| 8 | Sorting | | planned |
| 9 | Binary search | | planned |
| 10 | Binary trees and binary search trees | | planned |
| 11 | Balanced trees (AVL) | | planned |
| 12 | Heaps and priority queues | | planned |
| 13 | Tries | | planned |
| 14 | Graphs: BFS and DFS | | planned |
| 15 | Shortest paths | | planned |
| 16 | Union-find and minimum spanning trees | | planned |
| 17 | Dynamic programming | | planned |
| 18 | Greedy algorithms | | planned |
| 19 | Interview patterns: two pointers, sliding window and more | | planned |
| 20 | Mock interviews | | planned |

## Getting started

You need Python 3.12 or newer. No packages are needed to use the code;
the tests need pytest.

```
git clone https://github.com/aadhavanshines/data-structures-and-algorithms-in-python-hands-on.git
cd data-structures-and-algorithms-in-python-hands-on
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Notebooks

Each notebook runs a chapter's code step by step, with the results
already shown, and ends with exercises. Three ways to use them:

- **On GitHub:** open any notebook in `notebooks/` to read it with its
  results.
- **In your browser, with nothing to install:** click *Open in Colab* at
  the top of a notebook. It downloads the code for you.
- **On your computer:** `pip install jupyterlab`, then run
  `jupyter lab notebooks`.

The notebooks are built by `python tools/build_notebooks.py`, and the
tests check that every notebook still runs.

## Benchmarks

Time a structure yourself:

```
python benchmarks/append.py
```

## Versions

The code is tested with Python 3.12, 3.13, 3.14 and 3.15 on Linux,
macOS and Windows. The Tests workflow runs on every push.

## License

MIT. See `LICENSE`. You may use and adapt the code for your own work.
