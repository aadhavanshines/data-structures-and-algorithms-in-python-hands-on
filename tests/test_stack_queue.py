import random
from collections import deque

import pytest

from dsa.stack_queue import Queue, Stack, balanced


def test_stack_is_last_in_first_out():
    s = Stack()
    for x in "abc":
        s.push(x)
    assert s.peek() == "c" and len(s) == 3
    assert [s.pop(), s.pop(), s.pop()] == ["c", "b", "a"]
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()


def test_queue_is_first_in_first_out():
    q = Queue(capacity=2)
    for x in range(5):  # grows past its first capacity
        q.enqueue(x)
    assert q.peek() == 0 and list(q) == [0, 1, 2, 3, 4]
    assert [q.dequeue() for _ in range(5)] == [0, 1, 2, 3, 4]
    with pytest.raises(IndexError):
        q.dequeue()


def test_queue_wraps_around_without_growing():
    q = Queue(capacity=4)
    for i in range(100):
        q.enqueue(i)
        q.enqueue(i)
        q.dequeue()
        q.dequeue()
    assert len(q._slots) == 4  # it reused the same four slots


def test_queue_matches_deque_on_random_operations():
    rng = random.Random(5)
    q, model = Queue(capacity=1), deque()
    for _ in range(5000):
        if rng.random() < 0.55:
            x = rng.random()
            q.enqueue(x)
            model.append(x)
        elif model:
            assert q.dequeue() == model.popleft()
        assert list(q) == list(model)


@pytest.mark.parametrize(
    "text, ok",
    [
        ("", True),
        ("(a[b]{c})", True),
        ("([)]", False),
        ("((", False),
        ("())", False),
        ("print('}')", False),  # it counts brackets, not Python strings
    ],
)
def test_balanced(text, ok):
    assert balanced(text) is ok
