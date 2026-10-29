"""Chapter 1's claims, measured. Timing tests use generous limits so a
busy computer doesn't make them fail."""

from dsa.stack_queue import Queue
from dsa.timing import growth, time_it


def test_time_it_keeps_the_fastest_run():
    calls = []
    assert time_it(lambda: calls.append(1), repeat=3) >= 0
    assert len(calls) == 3


def test_growth_tells_linear_from_quadratic():
    def linear(n):
        data = list(range(n))
        return lambda: sum(data)

    def quadratic(n):
        data = list(range(n))
        return lambda: [x for x in data for _ in data]

    _, k1 = growth(linear, [100_000, 200_000, 400_000, 800_000])
    _, k2 = growth(quadratic, [100, 200, 400, 800], repeat=3)
    assert 0.6 < k1 < 1.4
    assert 1.6 < k2 < 2.4


def test_list_pop_front_is_linear_but_queue_is_not():
    """The reason Chapter 5 builds a ring buffer."""

    def list_pops(n):
        def run():
            data = list(range(n))
            for _ in range(1000):
                data.pop(0)

        return run

    def queue_pops(n):
        def run():
            q = Queue()
            for i in range(n):
                q.enqueue(i)
            for _ in range(1000):
                q.dequeue()

        return run

    _, k_list = growth(list_pops, [50_000, 100_000, 200_000, 400_000], 3)
    t_queue = time_it(queue_pops(1000), 3)
    assert k_list > 0.6  # each pop moves the whole list
    assert t_queue < 0.5
