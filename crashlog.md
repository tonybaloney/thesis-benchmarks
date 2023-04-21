```default
python bm_parallel_scaling.py -o bm_parallel_with_scaling.json
.....................
threading__1_1: Mean +- std dev: 67.9 us +- 0.8 us
.....................
subinterpreters_1_1: Mean +- std dev: 9.52 ms +- 0.20 ms
.....................
multiprocessing_1_1: Mean +- std dev: 94.6 ms +- 1.1 ms
.....................
threading__1_10: Mean +- std dev: 114 us +- 5 us
.....................
subinterpreters_1_10: Mean +- std dev: 9.59 ms +- 0.23 ms
.....................
multiprocessing_1_10: Mean +- std dev: 94.6 ms +- 1.8 ms
.....................
threading__1_100: Mean +- std dev: 982 us +- 29 us
.....................
subinterpreters_1_100: Mean +- std dev: 10.4 ms +- 0.1 ms
.....................
multiprocessing_1_100: Mean +- std dev: 95.5 ms +- 1.4 ms
.....................
threading__1_1000: Mean +- std dev: 57.8 ms +- 1.6 ms
.....................
subinterpreters_1_1000: Mean +- std dev: 66.5 ms +- 0.5 ms
.....................
multiprocessing_1_1000: Mean +- std dev: 152 ms +- 2 ms
.....................
threading__1_2000: Mean +- std dev: 226 ms +- 3 ms
.....................
WARNING: the benchmark result may be unstable
* the standard deviation (33.9 ms) is 14% of the mean (242 ms)
* the maximum (494 ms) is 104% greater than the mean (242 ms)

Try to rerun the benchmark with more runs, values and/or loops.
Run 'python -m pyperf system tune' command to reduce the system jitter.
Use pyperf stats, pyperf dump and pyperf hist to analyze results.
Use --quiet option to hide these warnings.

subinterpreters_1_2000: Mean +- std dev: 242 ms +- 34 ms
.....................
WARNING: the benchmark result may be unstable
* the standard deviation (45.0 ms) is 13% of the mean (342 ms)
* the maximum (570 ms) is 67% greater than the mean (342 ms)

Try to rerun the benchmark with more runs, values and/or loops.
Run 'python -m pyperf system tune' command to reduce the system jitter.
Use pyperf stats, pyperf dump and pyperf hist to analyze results.
Use --quiet option to hide these warnings.

multiprocessing_1_2000: Mean +- std dev: 342 ms +- 45 ms
.....................
threading__5_1: Mean +- std dev: 327 us +- 8 us
............Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  isolated = 0
  environment = 1
  user site = 1
  safe_path = 0
  import site = 1
  is in build tree = 1
  stdlib dir = '/Users/anthonyshaw/projects/cpython/Lib'
  sys._base_executable = '/Users/anthonyshaw/projects/thesis_benchmarks/../cpython/python.exe'
  sys.base_prefix = '/usr/local'
  sys.base_exec_prefix = '/usr/local'
  sys.platlibdir = 'lib'
  sys.executable = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  sys.prefix = '/usr/local'
  sys.exec_prefix = '/usr/local'
  sys.path = [
    '/usr/local/lib/python312.zip',
    '/Users/anthonyshaw/projects/cpython/Lib',
    '/Users/anthonyshaw/projects/cpython/build/lib.macosx-13.3-x86_64-3.12',
  ]
Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/encodings/__init__.py", line 33, in <module>
  File "<frozen importlib._bootstrap>", line 1305, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1276, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 841, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1020, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1116, in get_code
  File "<frozen importlib._bootstrap_external>", line 1216, in get_data
TypeError: descriptor 'read' for '_io.BufferedReader' objects doesn't apply to a '_io.BufferedReader' object
Exception in thread Thread-122 (_spawn_sub):
ValueError: init_fs_encoding: failed to get the Python codec of the filesystem encoding

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 1052, in _bootstrap_inner
    self.run()
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 989, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/anthonyshaw/projects/thesis_benchmarks/bm_parallel_scaling.py", line 101, in _spawn_sub
    sid = subinterpreters.create()
          ^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: interpreter creation failed
.........
subinterpreters_5_1: Mean +- std dev: 15.5 ms +- 1.1 ms
.....................
WARNING: the benchmark result may be unstable
* the standard deviation (41.0 ms) is 20% of the mean (209 ms)
* the maximum (422 ms) is 102% greater than the mean (209 ms)

Try to rerun the benchmark with more runs, values and/or loops.
Run 'python -m pyperf system tune' command to reduce the system jitter.
Use pyperf stats, pyperf dump and pyperf hist to analyze results.
Use --quiet option to hide these warnings.

multiprocessing_5_1: Mean +- std dev: 209 ms +- 41 ms
.....................
WARNING: the benchmark result may be unstable
* the standard deviation (90.0 us) is 13% of the mean (694 us)

Try to rerun the benchmark with more runs, values and/or loops.
Run 'python -m pyperf system tune' command to reduce the system jitter.
Use pyperf stats, pyperf dump and pyperf hist to analyze results.
Use --quiet option to hide these warnings.

threading__5_10: Mean +- std dev: 694 us +- 90 us
...............Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  isolated = 0
  environment = 1
  user site = 1
  safe_path = 0
  import site = 1
  is in build tree = 1
  stdlib dir = '/Users/anthonyshaw/projects/cpython/Lib'
  sys._base_executable = '/Users/anthonyshaw/projects/thesis_benchmarks/../cpython/python.exe'
  sys.base_prefix = '/usr/local'
  sys.base_exec_prefix = '/usr/local'
  sys.platlibdir = 'lib'
  sys.executable = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  sys.prefix = '/usr/local'
  sys.exec_prefix = '/usr/local'
  sys.path = [
    '/usr/local/lib/python312.zip',
    '/Users/anthonyshaw/projects/cpython/Lib',
    '/Users/anthonyshaw/projects/cpython/build/lib.macosx-13.3-x86_64-3.12',
  ]
Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/encodings/__init__.py", line 33, in <module>
  File "<frozen importlib._bootstrap>", line 1305, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1276, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 841, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1020, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1116, in get_code
  File "<frozen importlib._bootstrap_external>", line 1216, in get_data
TypeError: descriptor 'read' for '_io.BufferedReader' objects doesn't apply to a '_io.BufferedReader' object
Exception in thread Thread-101 (_spawn_sub):
ValueError: init_fs_encoding: failed to get the Python codec of the filesystem encoding

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 1052, in _bootstrap_inner
    self.run()
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 989, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/anthonyshaw/projects/thesis_benchmarks/bm_parallel_scaling.py", line 101, in _spawn_sub
    sid = subinterpreters.create()
          ^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: interpreter creation failed
..Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  isolated = 0
  environment = 1
  user site = 1
  safe_path = 0
  import site = 1
  is in build tree = 1
  stdlib dir = '/Users/anthonyshaw/projects/cpython/Lib'
  sys._base_executable = '/Users/anthonyshaw/projects/thesis_benchmarks/../cpython/python.exe'
  sys.base_prefix = '/usr/local'
  sys.base_exec_prefix = '/usr/local'
  sys.platlibdir = 'lib'
  sys.executable = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  sys.prefix = '/usr/local'
  sys.exec_prefix = '/usr/local'
  sys.path = [
    '/usr/local/lib/python312.zip',
    '/Users/anthonyshaw/projects/cpython/Lib',
    '/Users/anthonyshaw/projects/cpython/build/lib.macosx-13.3-x86_64-3.12',
  ]
Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/encodings/__init__.py", line 33, in <module>
  File "<frozen importlib._bootstrap>", line 1305, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1276, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 841, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1020, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1116, in get_code
  File "<frozen importlib._bootstrap_external>", line 1216, in get_data
TypeError: descriptor 'read' for '_io.BufferedReader' objects doesn't apply to a '_io.BufferedReader' object
Exception in thread Thread-156 (_spawn_sub):
ValueError: init_fs_encoding: failed to get the Python codec of the filesystem encoding

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 1052, in _bootstrap_inner
    self.run()
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 989, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/anthonyshaw/projects/thesis_benchmarks/bm_parallel_scaling.py", line 101, in _spawn_sub
    sid = subinterpreters.create()
          ^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: interpreter creation failed
....
subinterpreters_5_10: Mean +- std dev: 16.1 ms +- 1.4 ms
.....................
multiprocessing_5_10: Mean +- std dev: 185 ms +- 7 ms
.....................
threading__5_100: Mean +- std dev: 4.91 ms +- 0.07 ms
....Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  isolated = 0
  environment = 1
  user site = 1
  safe_path = 0
  import site = 1
  is in build tree = 1
  stdlib dir = '/Users/anthonyshaw/projects/cpython/Lib'
  sys._base_executable = '/Users/anthonyshaw/projects/thesis_benchmarks/../cpython/python.exe'
  sys.base_prefix = '/usr/local'
  sys.base_exec_prefix = '/usr/local'
  sys.platlibdir = 'lib'
  sys.executable = '/Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python'
  sys.prefix = '/usr/local'
  sys.exec_prefix = '/usr/local'
  sys.path = [
    '/usr/local/lib/python312.zip',
    '/Users/anthonyshaw/projects/cpython/Lib',
    '/Users/anthonyshaw/projects/cpython/build/lib.macosx-13.3-x86_64-3.12',
  ]
Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/encodings/__init__.py", line 33, in <module>
  File "<frozen importlib._bootstrap>", line 1305, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1276, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 841, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1020, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1116, in get_code
  File "<frozen importlib._bootstrap_external>", line 1216, in get_data
TypeError: descriptor 'read' for '_io.BufferedReader' objects doesn't apply to a '_io.BufferedReader' object
Exception in thread Thread-146 (_spawn_sub):
ValueError: init_fs_encoding: failed to get the Python codec of the filesystem encoding

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 1052, in _bootstrap_inner
    self.run()
  File "/Users/anthonyshaw/projects/cpython/Lib/threading.py", line 989, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/anthonyshaw/projects/thesis_benchmarks/bm_parallel_scaling.py", line 101, in _spawn_sub
    sid = subinterpreters.create()
          ^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: interpreter creation failed
.python(80285,0x70000811b000) malloc: *** error for object 0x11b554a30: pointer being freed was not allocated
python(80285,0x70000811b000) malloc: *** set a breakpoint in malloc_error_break to debug
Traceback (most recent call last):
  File "/Users/anthonyshaw/projects/thesis_benchmarks/bm_parallel_scaling.py", line 128, in <module>
    runner.bench_func(f'subinterpreters_{n}_{digits}', bench_subinterpreters, n, digits)
  File "/Users/anthonyshaw/projects/thesis_benchmarks/.venv/lib/python3.12/site-packages/pyperf/_runner.py", line 537, in bench_func
    result = self._main(task)
             ^^^^^^^^^^^^^^^^
  File "/Users/anthonyshaw/projects/thesis_benchmarks/.venv/lib/python3.12/site-packages/pyperf/_runner.py", line 460, in _main
    bench = self._manager()
            ^^^^^^^^^^^^^^^
  File "/Users/anthonyshaw/projects/thesis_benchmarks/.venv/lib/python3.12/site-packages/pyperf/_runner.py", line 673, in _manager
    bench = Manager(self).create_bench()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/anthonyshaw/projects/thesis_benchmarks/.venv/lib/python3.12/site-packages/pyperf/_manager.py", line 232, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/anthonyshaw/projects/thesis_benchmarks/.venv/lib/python3.12/site-packages/pyperf/_manager.py", line 131, in create_worker_bench
    suite = self.create_suite()
            ^^^^^^^^^^^^^^^^^^^
  File "/Users/anthonyshaw/projects/thesis_benchmarks/.venv/lib/python3.12/site-packages/pyperf/_manager.py", line 125, in create_suite
    suite = self.spawn_worker(0, 0)
            ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/anthonyshaw/projects/thesis_benchmarks/.venv/lib/python3.12/site-packages/pyperf/_manager.py", line 107, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
RuntimeError: /Users/anthonyshaw/projects/thesis_benchmarks/.venv/bin/python failed with exit code -6
```

