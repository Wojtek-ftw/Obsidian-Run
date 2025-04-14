import timeit
import polars as pl
import tracemalloc
from typing import Callable
import pandas_example as pdex
import polars_example as poex

def _benchmark(func_name, func, number=10):
    print(f"Running {func_name:<25}")
    duration = timeit.timeit(
        func,
        number=number
    )
    print(f"{func_name:<25}: {duration:.5f} seconds")
    return duration

def load_time_bench():
    pd_dur = _benchmark("Pandas Load", pdex.loading_dataset, 10)
    po_dur = _benchmark("Polars Load", poex.load_dataset, 10)

def main():
    load_time_bench()

if __name__ == "__main__":
    main()