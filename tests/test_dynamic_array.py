import random

import pytest

from dsa.dynamic_array import DynamicArray


def test_starts_empty():
    a = DynamicArray()
    assert len(a) == 0 and list(a) == [] and a.capacity == 1


def test_indexing_like_a_list():
    a = DynamicArray("abc")
    assert (a[0], a[-1], a[1]) == ("a", "c", "b")
    a[-1] = "z"
    assert list(a) == ["a", "b", "z"]
    for bad in (3, -4):
        with pytest.raises(IndexError):
            a[bad]
    with pytest.raises(TypeError):
        a["0"]


def test_capacity_doubles():
    a = DynamicArray()
    seen = []
    for i in range(17):
        a.append(i)
        seen.append(a.capacity)
    assert sorted(set(seen)) == [1, 2, 4, 8, 16, 32]


def test_appends_are_amortized_constant():
    """n appends copy fewer than 2n items in all."""
    for n in (10, 1000, 100_000):
        a = DynamicArray()
        for i in range(n):
            a.append(i)
        assert a.copies < 2 * n


def test_shrinks_at_a_quarter_not_a_half():
    a = DynamicArray(range(16))
    assert a.capacity == 16
    for _ in range(12):
        a.pop()
    assert len(a) == 4 and a.capacity == 8
    # Around the boundary, one append and one pop must not resize
    copies = a.copies
    for _ in range(100):
        a.append(0)
        a.pop()
    assert a.copies == copies


def test_pop_frees_the_item():
    a = DynamicArray([object()])
    a.append(1)
    a.pop()
    assert a._slots[1] is None


def test_matches_list_on_random_operations():
    rng = random.Random(7)
    a, model = DynamicArray(), []
    for _ in range(5000):
        op = rng.choice(["append", "insert", "pop", "set"])
        if op == "append":
            x = rng.randrange(100)
            a.append(x)
            model.append(x)
        elif op == "insert":
            i = rng.randint(-len(model) - 2, len(model) + 2)
            x = rng.random()
            a.insert(i, x)
            model.insert(i, x)
        elif op == "pop" and model:
            i = rng.randrange(-len(model), len(model))
            assert a.pop(i) == model.pop(i)
        elif op == "set" and model:
            i = rng.randrange(len(model))
            a[i] = model[i] = "x"
        assert list(a) == model and len(a) == len(model)
