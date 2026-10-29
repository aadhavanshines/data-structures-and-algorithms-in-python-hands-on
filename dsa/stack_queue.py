"""Chapter 5: stacks and queues.

A stack is last in, first out; a Python list is already a good one. A
queue is first in, first out, and a list makes a bad one: list.pop(0)
moves every remaining item, so it's O(n). The ring buffer below keeps a
moving start position instead, so both ends are O(1)."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class Stack:
    def __init__(self):
        self._items: list[Any] = []

    def __len__(self) -> int:
        return len(self._items)

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if not self._items:
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        if not self._items:
            raise IndexError("peek at an empty stack")
        return self._items[-1]


class Queue:
    """A queue in a ring buffer that grows when full."""

    def __init__(self, capacity: int = 8):
        self._slots: list[Any] = [None] * max(1, capacity)
        self._start = 0  # where the oldest item is
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        for i in range(self._size):
            yield self._slots[(self._start + i) % len(self._slots)]

    def enqueue(self, item: Any) -> None:
        """Add at the back: O(1) amortized."""
        if self._size == len(self._slots):
            self._slots = list(self) + [None] * len(self._slots)
            self._start = 0
        end = (self._start + self._size) % len(self._slots)
        self._slots[end] = item
        self._size += 1

    def dequeue(self) -> Any:
        """Remove from the front: O(1)."""
        if self._size == 0:
            raise IndexError("dequeue from an empty queue")
        item = self._slots[self._start]
        self._slots[self._start] = None
        self._start = (self._start + 1) % len(self._slots)
        self._size -= 1
        return item

    def peek(self) -> Any:
        if self._size == 0:
            raise IndexError("peek at an empty queue")
        return self._slots[self._start]


def balanced(text: str) -> bool:
    """Do the brackets in text match? The classic stack exercise."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs and (not stack or stack.pop() != pairs[ch]):
            return False
    return not stack
