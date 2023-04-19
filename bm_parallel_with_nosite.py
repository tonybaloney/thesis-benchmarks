import pyperf
from multiprocessing import Process
from threading import Thread
import _xxsubinterpreters as subinterpreters


import itertools

DEFAULT_DIGITS = 2000
icount = itertools.count
islice = itertools.islice

def gen_x():
    return map(lambda k: (k, 4 * k + 2, 0, 2 * k + 1), icount(1))


def compose(a, b):
    aq, ar, as_, at = a
    bq, br, bs, bt = b
    return (aq * bq,
            aq * br + ar * bt,
            as_ * bq + at * bs,
            as_ * br + at * bt)


def extract(z, j):
    q, r, s, t = z
    return (q * j + r) // (s * j + t)


def gen_pi_digits():
    z = (1, 0, 0, 1)
    x = gen_x()
    while 1:
        y = extract(z, 3)
        while y != extract(z, 4):
            z = compose(z, next(x))
            y = extract(z, 3)
        z = compose((10, -10 * y, 0, 1), z)
        yield y


def calc_ndigits(n=DEFAULT_DIGITS):
    return list(islice(gen_pi_digits(), n))

test ="""
import itertools

DEFAULT_DIGITS = 2000
icount = itertools.count
islice = itertools.islice

def gen_x():
    return map(lambda k: (k, 4 * k + 2, 0, 2 * k + 1), icount(1))


def compose(a, b):
    aq, ar, as_, at = a
    bq, br, bs, bt = b
    return (aq * bq,
            aq * br + ar * bt,
            as_ * bq + at * bs,
            as_ * br + at * bt)


def extract(z, j):
    q, r, s, t = z
    return (q * j + r) // (s * j + t)


def gen_pi_digits():
    z = (1, 0, 0, 1)
    x = gen_x()
    while 1:
        y = extract(z, 3)
        while y != extract(z, 4):
            z = compose(z, next(x))
            y = extract(z, 3)
        z = compose((10, -10 * y, 0, 1), z)
        yield y


def calc_ndigits(n=DEFAULT_DIGITS):
    return list(islice(gen_pi_digits(), n))
calc_ndigits(digits)
"""

def bench_threading(n, digits):
    # Code to launch specific model
    threads = []
    for _ in range(n):
        t = Thread(target=calc_ndigits, args=(digits,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def bench_subinterpreters(n, digits, nosite=False):
    # Code to launch specific model
    def _spawn_sub(digits):
        sid = subinterpreters.create(nosite=nosite)
        subinterpreters.run_string(sid, test, shared={"digits": digits})

    threads = []
    for _ in range(n):
        t = Thread(target=_spawn_sub, args=(digits,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def bench_multiprocessing(n, digits):
    # Code to launch specific model
    processes = []
    for _ in range(n):
        t = Process(target=calc_ndigits, args=(digits,))
        t.start()
        processes.append(t)
    for process in processes:
        process.join()

if __name__ == "__main__":
    runner = pyperf.Runner()
    runner.metadata['description'] = "Benchmark parallel execution scaling models"
    for n in [1, 5, 10, 50]:
        for digits in [1, 10, 100, 1000, 2000]:
            runner.bench_func(f'threading__{n}_{digits}', bench_threading, n, digits)
            runner.bench_func(f'subinterpreters_{n}_{digits}', bench_subinterpreters, n, digits)
            runner.bench_func(f'subinterpreters_nosite_{n}_{digits}', bench_subinterpreters, n, digits, True)
            runner.bench_func(f'multiprocessing_{n}_{digits}', bench_multiprocessing, n, digits)
