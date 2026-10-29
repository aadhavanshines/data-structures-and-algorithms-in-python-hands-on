"""Build the chapter notebooks in notebooks/, with their outputs.

    python tools/build_notebooks.py

Run it after changing a chapter's code or text, then commit the
notebooks. The tests check that every notebook still runs."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from notebook import build

REPO = "aadhavanshines/data-structures-and-algorithms-in-python-hands-on"


def header(file: str, title: str, intro: str) -> tuple[str, str]:
    colab = (
        f"https://colab.research.google.com/github/{REPO}"
        f"/blob/main/notebooks/{file}"
    )
    return (
        "md",
        (
            f"# {title}\n\n"
            f"[![Open In Colab](https://colab.research.google.com/assets/"
            f"colab-badge.svg)]({colab})\n\n{intro}"
        ),
    )


SETUP = (
    "code",
    """
# Find the book's code: in this repository, or downloaded (on Colab)
import subprocess
import sys
from pathlib import Path

REPO = (
    "https://github.com/aadhavanshines/"
    "data-structures-and-algorithms-in-python-hands-on"
)
here = Path.cwd()
found = [p for p in (here, *here.parents) if (p / "dsa").is_dir()]
if found:
    root = found[0]
else:
    clone = ["git", "clone", "--depth", "1", REPO, "dsa-book"]
    subprocess.run(clone, check=True)
    root = Path("dsa-book")
sys.path.insert(0, str(root.resolve()))
""",
)

TRY = "## Try it yourself\n\n"

NOTEBOOKS = {
    "01-measuring.ipynb": [
        header(
            "01-measuring.ipynb",
            "Chapter 1: Big-O, and measuring instead of guessing",
            "Big-O tells you how running time grows with the input. Here "
            "you measure it: time a function at growing sizes and read "
            "the exponent *k* in time ≈ nᵏ.",
        ),
        SETUP,
        (
            "md",
            (
                "Time one function. `time_it` keeps the fastest of several "
                "runs, the one least disturbed by the rest of the computer."
            ),
        ),
        (
            "code",
            """
from dsa.timing import growth, time_it

data = list(range(100_000))
print(f"sum of 100,000 numbers: {time_it(lambda: sum(data)) * 1000:.2f} ms")
""",
        ),
        (
            "md",
            (
                "Now let the input grow. Doubling *n* doubles the time of "
                "an O(n) function and quadruples an O(n²) one."
            ),
        ),
        (
            "code",
            """
def linear(n):
    data = list(range(n))
    return lambda: sum(data)


def quadratic(n):
    data = list(range(n))

    def pairs():  # looks at every pair of items
        count = 0
        for _ in data:
            for _ in data:
                count += 1
        return count

    return pairs


def show(name, make, sizes):
    timings, k = growth(make, sizes, repeat=3)
    for n, t in timings:
        print(f"{name:>9} n={n:>7,}  {t * 1000:8.2f} ms")
    print(f"{name:>9} exponent k = {k:.2f}\\n")


show("linear", linear, [100_000, 200_000, 400_000])
show("quadratic", quadratic, [200, 400, 800])
""",
        ),
        (
            "md",
            (
                "Membership is a good first surprise: `in` on a list "
                "checks every item, on a set it's one hash lookup."
            ),
        ),
        (
            "code",
            """
n = 200_000
as_list, as_set = list(range(n)), set(range(n))
t_list = time_it(lambda: (n - 1) in as_list)
t_set = time_it(lambda: (n - 1) in as_set)
print(f"list: {t_list * 1e6:9.1f} µs   set: {t_set * 1e6:6.2f} µs")
""",
        ),
        (
            "md",
            TRY + "1. Time `sorted()` on growing lists. Is *k* nearer 1 "
            "or 2? (It's O(n log n), which looks like a little over 1.)\n"
            "2. Time `as_list.index(n - 1)`. Which line above does it "
            "behave like?",
        ),
    ],
    "03-dynamic-arrays.ipynb": [
        header(
            "03-dynamic-arrays.ipynb",
            "Chapter 3: Dynamic arrays",
            "Python's `list` is a dynamic array: a block of slots that "
            "doubles when it's full. Build one and watch it grow.",
        ),
        SETUP,
        (
            "code",
            """
from dsa.dynamic_array import DynamicArray

a = DynamicArray()
for i in range(10):
    a.append(i)
    print(
        f"len {len(a):>2}  capacity {a.capacity:>2}  "
        f"items copied so far {a.copies:>2}"
    )
""",
        ),
        (
            "md",
            (
                "Copying is O(n), but it happens so rarely that each "
                "append costs O(1) on average. Check: *n* appends copy "
                "fewer than 2*n* items."
            ),
        ),
        (
            "code",
            """
for n in (10, 1_000, 100_000):
    a = DynamicArray(range(n))
    per = a.copies / n
    print(f"{n:>7,} appends copied {a.copies:>7,} ({per:.2f} each)")
""",
        ),
        (
            "md",
            (
                "Popping shrinks the array at a quarter full, not at half. "
                "Shrinking at half would let one append and one pop resize "
                "every time."
            ),
        ),
        (
            "code",
            """
a = DynamicArray(range(16))
for _ in range(12):
    a.pop()
print(len(a), a.capacity)
copies = a.copies
for _ in range(1000):
    a.append(0)
    a.pop()
print("extra copies after 1,000 append/pop pairs:", a.copies - copies)
""",
        ),
        ("md", "It behaves like a list where it matters:"),
        (
            "code",
            """
a = DynamicArray("abcde")
a.insert(0, "start")
a[-1] = "end"
print(a, a.pop(2), a)
""",
        ),
        (
            "md",
            TRY + "1. Change the growth factor from 2 to 1.5 in "
            "`dsa/dynamic_array.py`. How many copies per append now?\n"
            "2. Run `python benchmarks/append.py` and compare with "
            "Python's own `list`.",
        ),
    ],
    "04-linked-lists.ipynb": [
        header(
            "04-linked-lists.ipynb",
            "Chapter 4: Linked lists",
            "Each node holds a value and a link to the next node. The "
            "front is cheap to change; finding the *i*-th item means "
            "walking the links.",
        ),
        SETUP,
        (
            "code",
            """
from dsa.linked_list import LinkedList

s = LinkedList([2, 3, 4])
s.push_front(1)
s.append(5)
s
""",
        ),
        ("md", "Draw the links, to see what the list really is:"),
        (
            "code",
            """
def draw(lst):
    node, parts = lst.head, []
    while node is not None:
        parts.append(f"[{node.value}]")
        node = node.next
    print(" -> ".join(parts + ["None"]))


draw(s)
s.reverse()
draw(s)
""",
        ),
        (
            "md",
            (
                "Two classic interview questions, both in one pass: "
                "reversing in place (above) and finding the middle with a "
                "slow and a fast pointer."
            ),
        ),
        (
            "code",
            """
for items in ([1], [1, 2, 3], [1, 2, 3, 4, 5, 6]):
    print(items, "-> middle", LinkedList(items).middle())
""",
        ),
        (
            "code",
            """
s = LinkedList("abcd")
s.remove("c")
print(s.pop_front(), list(s), len(s))
""",
        ),
        (
            "md",
            TRY + "1. Write `has_cycle(head)` using the same slow and "
            "fast pointers.\n2. Add `pop_back()`. Why is it O(n) in a "
            "singly linked list?",
        ),
    ],
    "05-stacks-and-queues.ipynb": [
        header(
            "05-stacks-and-queues.ipynb",
            "Chapter 5: Stacks and queues",
            "A stack is last in, first out; a queue is first in, first "
            "out. A list is a fine stack but a slow queue.",
        ),
        SETUP,
        (
            "code",
            """
from dsa.stack_queue import Queue, Stack, balanced

s = Stack()
for word in ("first", "second", "third"):
    s.push(word)
print("stack pops:", s.pop(), s.pop(), s.pop())

q = Queue()
for word in ("first", "second", "third"):
    q.enqueue(word)
print("queue gives:", q.dequeue(), q.dequeue(), q.dequeue())
""",
        ),
        (
            "md",
            (
                "Why build a queue at all? `list.pop(0)` moves every "
                "remaining item. The ring buffer just moves its start."
            ),
        ),
        (
            "code",
            """
from dsa.timing import time_it


def drain_list(n):
    data = list(range(n))
    while data:
        data.pop(0)


def drain_queue(n):
    q = Queue()
    for i in range(n):
        q.enqueue(i)
    while q:
        q.dequeue()


for n in (10_000, 20_000, 40_000):
    t1 = time_it(lambda n=n: drain_list(n), 1)
    t2 = time_it(lambda n=n: drain_queue(n), 1)
    print(
        f"n={n:>6,}  list.pop(0) {t1 * 1000:7.1f} ms   "
        f"Queue {t2 * 1000:6.1f} ms"
    )
""",
        ),
        (
            "md",
            (
                "The stack exercise every interview asks: do the brackets "
                "match?"
            ),
        ),
        (
            "code",
            """
for text in ("(a[b]{c})", "([)]", "((", "f(x) + [1, 2]"):
    print(f"{text!r:16} balanced: {balanced(text)}")
""",
        ),
        (
            "md",
            TRY + "1. Use a `Stack` to evaluate reverse Polish notation: "
            "`3 4 + 2 *` is 14.\n2. Time `collections.deque` the same "
            "way. It's a ring buffer too, written in C.",
        ),
    ],
}


def main() -> None:
    folder = ROOT / "notebooks"
    folder.mkdir(exist_ok=True)
    for name, cells in NOTEBOOKS.items():
        build(folder / name, cells)
        print("built", name)


if __name__ == "__main__":
    main()
