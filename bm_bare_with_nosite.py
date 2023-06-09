import pyperf
from multiprocessing import Process
from threading import Thread
import _xxsubinterpreters as subinterpreters

def f():
    ...


def bench_threading(n):
    # Code to launch specific model
    for _ in range(n):
        t = Thread(target=f)
        t.start()
        t.join()

def bench_subinterpreters(n, site=True):
    # Code to launch specific model
    for _ in range(n):
        sid = subinterpreters.create(site=site)
        subinterpreters.run_string(sid, "")

def bench_multiprocessing(n):
    # Code to launch specific model
    for _ in range(n):
        t = Process(target=f)
        t.start()
        t.join()

if __name__ == "__main__":
    runner = pyperf.Runner()
    runner.metadata['description'] = "Benchmark execution models"
    n = 100
    runner.bench_func('threading', bench_threading, n)
    runner.bench_func('subinterpreters', bench_subinterpreters, n)
    runner.bench_func('subinterpreters_nosite', bench_subinterpreters, n, False)
    runner.bench_func('multiprocessing', bench_multiprocessing, n)
