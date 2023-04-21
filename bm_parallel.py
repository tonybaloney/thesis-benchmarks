import pyperf
from multiprocessing import Process
from threading import Thread
import _xxsubinterpreters as subinterpreters


import itertools

DEFAULT_DIGITS = 200
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

DEFAULT_DIGITS = 200
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
calc_ndigits()
"""

def bench_threading(n):
    # Code to launch specific model
    threads = []
    for _ in range(n):
        t = Thread(target=calc_ndigits)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def bench_subinterpreters(n, site=True):
    # Code to launch specific model
    def _spawn_sub():
        sid = subinterpreters.create(site=site)
        subinterpreters.run_string(sid, test)

    threads = []
    for _ in range(n):
        t = Thread(target=_spawn_sub)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def bench_multiprocessing(n):
    # Code to launch specific model
    processes = []
    for _ in range(n):
        t = Process(target=calc_ndigits)
        t.start()
        processes.append(t)
    for process in processes:
        process.join()

if __name__ == "__main__":
    runner = pyperf.Runner()
    runner.metadata['description'] = "Benchmark execution models"
    n = 10
    runner.bench_func('threading', bench_threading, n)
    runner.bench_func('subinterpreters', bench_subinterpreters, n)
    runner.bench_func('subinterpreters_nosite', bench_subinterpreters, n, False)
    runner.bench_func('multiprocessing', bench_multiprocessing, n)
