import random
from collections import deque

import pytest

from dsa.linked_list import LinkedList


def test_front_and_back():
    s = LinkedList([2, 3])
    s.push_front(1)
    s.append(4)
    assert list(s) == [1, 2, 3, 4] and len(s) == 4
    assert s.pop_front() == 1 and list(s) == [2, 3, 4]


def test_empty_list_errors():
    s = LinkedList()
    with pytest.raises(IndexError):
        s.pop_front()
    with pytest.raises(IndexError):
        s.middle()
    with pytest.raises(ValueError):
        s.remove(1)


def test_tail_is_kept_right():
    s = LinkedList([1, 2, 3])
    s.remove(3)  # the tail
    s.append(4)
    assert list(s) == [1, 2, 4]
    s.pop_front(), s.pop_front(), s.pop_front()
    assert s.head is None and s.tail is None
    s.append(5)
    assert list(s) == [5]


@pytest.mark.parametrize("n", [0, 1, 2, 5])
def test_reverse(n):
    s = LinkedList(range(n))
    s.reverse()
    assert list(s) == list(reversed(range(n)))
    s.append("end")  # the tail must be the old head
    assert list(s)[-1] == "end"


@pytest.mark.parametrize(
    "items, middle",
    [([1], 1), ([1, 2], 1), ([1, 2, 3], 2), ([1, 2, 3, 4], 2)],
)
def test_middle(items, middle):
    assert LinkedList(items).middle() == middle


def test_matches_deque_on_random_operations():
    rng = random.Random(4)
    s, model = LinkedList(), deque()
    for _ in range(5000):
        op = rng.choice(["front", "back", "pop", "remove"])
        x = rng.randrange(20)
        if op == "front":
            s.push_front(x)
            model.appendleft(x)
        elif op == "back":
            s.append(x)
            model.append(x)
        elif op == "pop" and model:
            assert s.pop_front() == model.popleft()
        elif op == "remove" and x in model:
            s.remove(x)
            model.remove(x)
        assert list(s) == list(model) and len(s) == len(model)
