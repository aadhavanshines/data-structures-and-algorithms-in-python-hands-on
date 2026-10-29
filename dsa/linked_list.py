"""Chapter 4: a singly linked list.

Each node holds an item and a link to the next node. Adding or removing
at the front is O(1) because nothing has to move; finding the i-th item
is O(n) because you must walk the links to get there."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    next: Node | None = None


class LinkedList:
    def __init__(self, items=()):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size = 0
        for item in items:
            self.append(item)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __repr__(self) -> str:
        return f"LinkedList({list(self)!r})"

    def push_front(self, item: Any) -> None:
        """O(1)."""
        self.head = Node(item, self.head)
        if self.tail is None:
            self.tail = self.head
        self._size += 1

    def append(self, item: Any) -> None:
        """O(1), thanks to the tail link."""
        node = Node(item)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def pop_front(self) -> Any:
        """Remove and return the first item: O(1)."""
        if self.head is None:
            raise IndexError("pop from an empty list")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return node.value

    def remove(self, value: Any) -> None:
        """Remove the first node holding value: O(n)."""
        before, node = None, self.head
        while node is not None and node.value != value:
            before, node = node, node.next
        if node is None:
            raise ValueError(f"{value!r} is not in the list")
        if before is None:
            self.head = node.next
        else:
            before.next = node.next
        if node is self.tail:
            self.tail = before
        self._size -= 1

    def reverse(self) -> None:
        """Turn every link around, in place: O(n) time, O(1) space.
        A classic interview question."""
        before, node = None, self.head
        self.tail = node
        while node is not None:
            node.next, before, node = before, node, node.next
        self.head = before

    def middle(self) -> Any:
        """The middle item, in one pass: the fast pointer moves two steps
        for each step of the slow one (the 'tortoise and hare')."""
        if self.head is None:
            raise IndexError("an empty list has no middle")
        slow = fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow, fast = slow.next, fast.next.next
        return slow.value
