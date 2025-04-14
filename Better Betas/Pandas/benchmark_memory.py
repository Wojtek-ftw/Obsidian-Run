import timeit
import polars as pl
import tracemalloc
from typing import Callable
import pandas_example as pdex
import polars_example as poex

def pandas_tracemalloc_default(func: Callable):
    print("-"*20)
    print("Pandas Default")
    tracemalloc.start()
    df = func()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024**2:.2f} MB")
    print(f"Peak memory usage: {peak / 1024**2:.2f} MB")
    print(f"Total: {df.memory_usage(deep=True).sum() / (1024 ** 2):.2f} MB")
    tracemalloc.stop()

def pandas_tracemalloc_dtype(func: Callable):
    print("-"*20)
    print("Pandas Change Column Type")
    tracemalloc.start()
    df = func()

    for col in df.select_dtypes(include="object"):
        num_unique = df[col].nunique()
        num_total = len(df[col])
        if num_unique / num_total < 0.5:
            df[col] = df[col].astype("category")


    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024**2:.2f} MB")
    print(f"Peak memory usage: {peak / 1024**2:.2f} MB")
    print(f"Total: {df.memory_usage(deep=True).sum() / (1024 ** 2):.2f} MB")
    tracemalloc.stop()

def polars_tracemalloc_default(func: Callable):
    print("-"*20)
    print("Polars Default")
    tracemalloc.start()
    df = func()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024**2:.2f} MB")
    print(f"Peak memory usage: {peak / 1024**2:.2f} MB")
    print(f"Estimated size: {df.estimated_size() / (1024 ** 2):.2f} MB")
    tracemalloc.stop()

def polars_tracemalloc_force_memory(func: Callable):
    print("-"*20)
    print("Polars Force Memory")
    tracemalloc.start()
    df = func()
    numeric_types = [pl.Int8, pl.Int16, pl.Int32, pl.Int64,
                 pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
                 pl.Float32, pl.Float64]
    # Following command does table wide operation, but does not evaluate to use memory.
    df = df.with_columns([
        (pl.col(col) + 0 if df.schema[col] in numeric_types else pl.col(col).cast(pl.Utf8) + "")
        .alias(col)
        for col in df.columns
    ])
    # Following command forces data to be loaded into memory.
    _ = [df[col].to_numpy() for col in df.columns]

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024**2:.2f} MB")
    print(f"Peak memory usage: {peak / 1024**2:.2f} MB")
    print(f"Estimated size: {df.estimated_size() / (1024 ** 2):.2f} MB")
    tracemalloc.stop()


def memory_bench():
    pandas_tracemalloc_default(pdex.loading_dataset)
    pandas_tracemalloc_dtype(pdex.loading_dataset)
    polars_tracemalloc_default(poex.load_dataset)
    polars_tracemalloc_force_memory(poex.load_dataset)

def main():
    memory_bench()

if __name__ == "__main__":
    main()