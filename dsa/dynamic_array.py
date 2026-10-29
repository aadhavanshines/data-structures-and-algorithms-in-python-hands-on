"""Chapter 3: a dynamic array, the idea behind Python's list.

The items live in a fixed-size block of slots. When the block is full,
append() moves everything to a block twice the size. Copying is O(n),
but it happens so rarely that append() is O(1) on average ("amortized"):
n appends copy fewer than 2n items in all."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class DynamicArray:
    def __init__(self, items=()):
        self._capacity = 1
        self._slots: list[Any] = [None]  # stands in for raw memory
        self._size = 0
        self.copies = 0  # items moved by resizing, for Chapter 3's tests
        for item in items:
            self.append(item)

    def __len__(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    def _index(self, i: int) -> int:
        """A valid position for i, counting negative i from the end."""
        if not isinstance(i, int):
            raise TypeError("indices must be integers")
        if i < 0:
            i += self._size
        if not 0 <= i < self._size:
            raise IndexError("index out of range")
        return i

    def __getitem__(self, i: int) -> Any:
        return self._slots[self._index(i)]

    def __setitem__(self, i: int, value: Any) -> None:
        self._slots[self._index(i)] = value

    def __iter__(self) -> Iterator[Any]:
        for i in range(self._size):
            yield self._slots[i]

    def __repr__(self) -> str:
        return f"DynamicArray({list(self)!r})"

    def _resize(self, capacity: int) -> None:
        slots: list[Any] = [None] * capacity
        for i in range(self._size):
            slots[i] = self._slots[i]
        self.copies += self._size
        self._slots, self._capacity = slots, capacity

    def append(self, item: Any) -> None:
        """Add to the end: O(1) amortized."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._slots[self._size] = item
        self._size += 1

    def insert(self, i: int, item: Any) -> None:
        """Insert before position i: O(n), everything after moves."""
        i = max(0, min(i + self._size if i < 0 else i, self._size))
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._size, i, -1):
            self._slots[j] = self._slots[j - 1]
        self._slots[i] = item
        self._size += 1

    def pop(self, i: int = -1) -> Any:
        """Remove and return the item at i (the last by default).

        Shrinks to half when only a quarter is used. Shrinking at half
        instead would let one append and one pop resize every time."""
        i = self._index(i)
        item = self._slots[i]
        for j in range(i, self._size - 1):
            self._slots[j] = self._slots[j + 1]
        self._size -= 1
        self._slots[self._size] = None  # don't keep the item alive
        if 0 < self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        return item
