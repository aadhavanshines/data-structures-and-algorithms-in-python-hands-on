"""Chapter 1: measure instead of guess.

time_it() runs a function several times and keeps the fastest run, which
is the one least disturbed by everything else the computer is doing.
growth() times a function at growing input sizes and estimates the
exponent k in time ~ n**k: about 0 is O(1), 1 is O(n), 2 is O(n**2)."""

from __future__ import annotations

import math
import time
from collections.abc import Callable


def time_it(fn: Callable[[], object], repeat: int = 5) -> float:
    """Seconds for the fastest of `repeat` runs of fn()."""
    best = math.inf
    for _ in range(repeat):
        start = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - start)
    return best


def growth(
    make: Callable[[int], Callable[[], object]],
    sizes: list[int],
    repeat: int = 5,
) -> tuple[list[tuple[int, float]], float]:
    """Time make(n)() for each n; return the timings and the exponent.

    make(n) builds the input and returns the function to time, so the
    set-up isn't counted."""
    timings = [(n, time_it(make(n), repeat)) for n in sizes]
    # Least-squares slope of log(time) against log(n)
    xs = [math.log(n) for n, _ in timings]
    ys = [math.log(max(t, 1e-9)) for _, t in timings]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum(
        (x - mx) ** 2 for x in xs
    )
    return timings, slope
