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
| `benchmarks/` | Timing scripts that measure what the Big-O claims predict |

## Chapters

| # | Chapter | Module | Status |
| --- | --- | --- | --- |
| 1 | Big-O, and measuring instead of guessing | `dsa/timing.py` | ✅ |
| 2 | Python's list, dict and set under the hood | | planned |
| 3 | Dynamic arrays | `dsa/dynamic_array.py` | ✅ |
| 4 | Linked lists | `dsa/linked_list.py` | ✅ |
| 5 | Stacks and queues | `dsa/stack_queue.py` | ✅ |
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

Time a structure yourself:

```
python benchmarks/append.py
```

## Versions

The code is tested with Python 3.12, 3.13, 3.14 and 3.15 on Linux,
macOS and Windows. The Tests workflow runs on every push.

## License

MIT. See `LICENSE`. You may use and adapt the code for your own work.
