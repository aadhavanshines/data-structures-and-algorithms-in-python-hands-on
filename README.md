# Data Structures and Algorithms in Python, Hands-On: the code

[![Check every listing](https://github.com/aadhavanshines/data-structures-and-algorithms-in-python-hands-on/actions/workflows/check.yml/badge.svg)](https://github.com/aadhavanshines/data-structures-and-algorithms-in-python-hands-on/actions/workflows/check.yml)

All the programs, tests, benchmarks, Jupyter notebooks and exercise solutions from the book ***Data Structures and Algorithms in Python, Hands-On: Every Structure Built, Tested and Timed, with Interview Patterns, Exercises and Solutions*** by Aadhavan Muthurengan, arranged by chapter.

Every program here was run on Python 3.12, 3.13, 3.14 and 3.15, and its output compared with the output printed in the book. The expected output of each program is stored next to it, so you can check your own runs. The same check runs on GitHub after every change, on Linux, macOS and Windows with all four versions, and its results are public on the [Actions tab](https://github.com/aadhavanshines/data-structures-and-algorithms-in-python-hands-on/actions).

## Getting started

1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/).
2. Download this repository: the green **Code** button, then **Download ZIP** (and unzip it), or `git clone https://github.com/aadhavanshines/data-structures-and-algorithms-in-python-hands-on`.
3. In the repository folder, create a virtual environment and install the exact package versions the book was tested with:

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

4. Go to a chapter's folder and run a program, for example:

```
cd code/ch06
python grow_demo.py
python -m pytest -q test_dynamic_array.py
python bench_append.py
```

On macOS and Linux, type `python3` instead of `python` until you activate the virtual environment. The data structures themselves use only Python's standard library; pytest runs the tests, matplotlib draws the benchmark charts, and Jupyter runs the notebooks.

Type the programs yourself first if you can: you'll learn more, and the files here are there to check against.

## Jupyter notebooks

Every chapter folder also has a notebook with all of that chapter's programs, in the book's order, one program per cell: `code/ch13/ch13.ipynb` for Chapter 13, and so on. The notebooks are saved with their outputs, so you can read them right here on GitHub.

To run them, start Jupyter (installed by `requirements.txt`) from the repository folder, with the virtual environment active:

```
jupyter notebook
```

Your browser opens. Go to `code`, then a chapter folder, open its `.ipynb` file, and choose **Run > Run All Cells**. Keep each notebook in its chapter folder: the programs import each other's files, and every folder has its own copy of the timing module, `bench.py`.

Benchmark cells take from a second to about a minute each, and their times will differ from the saved ones and from the book's: they depend on your computer. Compare the ratios and the shape of the growth, not the exact numbers.

Exercise solutions stay as `.py` files, so you can try each exercise before seeing an answer, and each chapter's tests stay as pytest files, because tests are run from a terminal.

## Chapters

| Chapter | Topic | Notebook | Programs | Benchmarks | Exercise solutions |
| --- | --- | --- | --- | --- | --- |
| 1 | [Why Build It Yourself](code/ch01/) | [ch01.ipynb](code/ch01/ch01.ipynb) | 1 | 1 |  |
| 2 | [Setting Up](code/ch02/) | [ch02.ipynb](code/ch02/ch02.ipynb) | 3 |  | 2 |
| 3 | [Measuring Speed: Big O You Can See](code/ch03/) | [ch03.ipynb](code/ch03/ch03.ipynb) | 5 | 3 | 2 |
| 4 | [Python's Built-ins Under the Hood](code/ch04/) | [ch04.ipynb](code/ch04/ch04.ipynb) | 5 | 3 | 2 |
| 5 | [Recursion and the Call Stack](code/ch05/) | [ch05.ipynb](code/ch05/ch05.ipynb) | 6 | 1 | 2 |
| 6 | [A Dynamic Array](code/ch06/) | [ch06.ipynb](code/ch06/ch06.ipynb) | 5 | 1 | 3 |
| 7 | [Linked Lists](code/ch07/) | [ch07.ipynb](code/ch07/ch07.ipynb) | 7 | 2 | 3 |
| 8 | [Stacks and Queues](code/ch08/) | [ch08.ipynb](code/ch08/ch08.ipynb) | 7 | 1 | 3 |
| 9 | [Hash Tables](code/ch09/) | [ch09.ipynb](code/ch09/ch09.ipynb) | 7 | 2 | 3 |
| 10 | [Binary Search](code/ch10/) | [ch10.ipynb](code/ch10/ch10.ipynb) | 6 | 1 | 3 |
| 11 | [Simple Sorts](code/ch11/) | [ch11.ipynb](code/ch11/ch11.ipynb) | 5 | 1 | 2 |
| 12 | [Merge Sort and Quicksort](code/ch12/) | [ch12.ipynb](code/ch12/ch12.ipynb) | 7 | 3 | 3 |
| 13 | [Heaps and Priority Queues](code/ch13/) | [ch13.ipynb](code/ch13/ch13.ipynb) | 7 | 1 | 3 |
| 14 | [Sorting Without Comparing](code/ch14/) | [ch14.ipynb](code/ch14/ch14.ipynb) | 5 | 1 | 2 |
| 15 | [Binary Trees](code/ch15/) | [ch15.ipynb](code/ch15/ch15.ipynb) | 4 |  | 3 |
| 16 | [Binary Search Trees](code/ch16/) | [ch16.ipynb](code/ch16/ch16.ipynb) | 5 | 1 | 3 |
| 17 | [Balanced Trees: AVL](code/ch17/) | [ch17.ipynb](code/ch17/ch17.ipynb) | 6 | 1 | 2 |
| 18 | [Tries](code/ch18/) | [ch18.ipynb](code/ch18/ch18.ipynb) | 4 | 1 | 2 |
| 19 | [Union-Find](code/ch19/) | [ch19.ipynb](code/ch19/ch19.ipynb) | 4 | 1 | 2 |
| 20 | [Graphs](code/ch20/) | [ch20.ipynb](code/ch20/ch20.ipynb) | 5 | 1 | 3 |
| 21 | [Breadth-First and Depth-First Search](code/ch21/) | [ch21.ipynb](code/ch21/ch21.ipynb) | 5 | 1 | 2 |
| 22 | [Shortest Paths](code/ch22/) | [ch22.ipynb](code/ch22/ch22.ipynb) | 5 | 1 | 2 |
| 23 | [Minimum Spanning Trees](code/ch23/) | [ch23.ipynb](code/ch23/ch23.ipynb) | 5 | 1 | 2 |
| 24 | [Solving a Problem in an Interview](code/ch24/) | [ch24.ipynb](code/ch24/ch24.ipynb) | 4 | 1 | 1 |
| 25 | [Two Pointers](code/ch25/) | [ch25.ipynb](code/ch25/ch25.ipynb) | 4 | 1 | 3 |
| 26 | [Sliding Window](code/ch26/) | [ch26.ipynb](code/ch26/ch26.ipynb) | 4 | 1 | 3 |
| 27 | [Hash Maps and Prefix Sums](code/ch27/) | [ch27.ipynb](code/ch27/ch27.ipynb) | 5 | 1 | 3 |
| 28 | [BFS and DFS on Grids and Implicit Graphs](code/ch28/) | [ch28.ipynb](code/ch28/ch28.ipynb) | 6 | 1 | 3 |
| 29 | [Dynamic Programming I: Memoization and Tables](code/ch29/) | [ch29.ipynb](code/ch29/ch29.ipynb) | 5 | 1 | 3 |
| 30 | [Dynamic Programming II: Sequences, Strings and Knapsack](code/ch30/) | [ch30.ipynb](code/ch30/ch30.ipynb) | 5 | 1 | 3 |
| 31 | [Greedy Algorithms and Backtracking](code/ch31/) | [ch31.ipynb](code/ch31/ch31.ipynb) | 6 | 1 | 2 |
| 32 | [Project: An LRU Cache](code/ch32/) | [ch32.ipynb](code/ch32/ch32.ipynb) | 6 | 1 | 2 |
| 33 | [Is Python Getting Faster?](code/ch33/) | [ch33.ipynb](code/ch33/ch33.ipynb) | 2 | 1 |  |

Chapter 34, Next Steps, has no code. Charts are saved as PNG files in the folder you run a benchmark from.

## What the files are

| File | Contents |
| --- | --- |
| `name.py` | A program from the book: a data structure, a demo, a test or a benchmark |
| `chNN.ipynb` | The chapter's notebook: every program from the chapter, one per cell, with its output |
| `name.out` | Its output, exactly as printed in the book |
| `name.cmd` | The command used instead of `python name.py` (the tests run with pytest) |
| `name.runonly` | Marks a benchmark: its `.out` file is the recorded run printed in the book, and yours will differ |
| `solution_*.py` | Worked solutions to the chapter's exercises, also printed in Appendix A |
| `bench.py` | The timing module from Chapter 3; each chapter folder has an identical copy, `code/common/bench.py` is the original |
| `code/ch33/versions.json` | The book's timings of Chapter 33's suite on Python 3.12 to 3.15 |

## Check everything yourself

With the virtual environment active, from the repository folder:

```
python tests/run_listings.py     # run every program and compare its output with the .out file
python tests/check_notebooks.py  # run every notebook and compare each cell with the .out file
```

Each program runs in a temporary copy of its chapter folder, so the checks never change your files. Benchmarks run in a quick mode (`BENCH_QUICK=1`) that only checks they work; run a benchmark by itself to get real timings.

## About the examples

All people, towns, companies and data in the examples are fictional. Any resemblance to real persons or businesses is coincidental.

## License

The code is released under the [MIT License](LICENSE): use it, change it and share it freely. The book's text is not part of this repository and remains under copyright.
