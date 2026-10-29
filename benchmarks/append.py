"""Chapter 3's benchmark: is append() really O(1)?

Times n appends to DynamicArray and to Python's list, and estimates the
exponent k in time ~ n**k for the whole run. k near 1 means each append
costs about the same, however big the array gets.

    python benchmarks/append.py           # full run
    python benchmarks/append.py --quick   # a short run, for CI
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dsa.dynamic_array import DynamicArray
from dsa.timing import growth


def appends(kind):
    def make(n):
        def run():
            a = kind()
            for i in range(n):
                a.append(i)

        return run

    return make


def main() -> None:
    quick = "--quick" in sys.argv
    sizes = (
        [10_000, 20_000, 40_000]
        if quick
        else [10_000, 20_000, 40_000, 80_000, 160_000, 320_000]
    )
    print(f"{'n':>9} {'DynamicArray':>14} {'list':>10}")
    ours, k_ours = growth(appends(DynamicArray), sizes, repeat=3)
    theirs, k_theirs = growth(appends(list), sizes, repeat=3)
    for (n, t1), (_, t2) in zip(ours, theirs):
        print(f"{n:>9,} {t1 * 1000:>12.1f}ms {t2 * 1000:>8.1f}ms")
    print(f"exponent k: DynamicArray {k_ours:.2f}, list {k_theirs:.2f}")
    print("k near 1.0 means each append costs the same: O(1) amortized")


if __name__ == "__main__":
    main()
