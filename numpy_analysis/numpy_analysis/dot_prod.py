"""
Filename: mat_myl.py
Description: Contains numpy and pythonic implementation of matrix multiplication.

Author: Wojciech Zacherek
Created: 2025/04/13
Last Modified: 2025/04/13

Copyright © 2025 Wojciech Zacherek
All rights reserved. This file may not be copied, modified, distributed, or used in any form without express written permission.

Contact: w.zacherek@outlook.com
"""

import csv
import timeit
from typing import Optional
import numpy as np
import matplotlib.pyplot as plt


def generate_matrix(n, start=0):
    """Generates an NxN matrix filled with sequential numbers starting from 'start'."""
    return [[start + i * n + j for j in range(n)] for i in range(n)]


# 4. Dot Product
def dot_product_py(a, b):
    return sum(x * y for x, y in zip(a, b))

def dot_product_numpy(a, b):
    return np.dot(np.array(a), np.array(b))

def _benchmark(func_name, stmt, func, matrixA, matrixB, number=100000):
    duration = timeit.timeit(
        stmt=stmt,
        globals={"MatA": matrixA, "MatB": matrixB, func.__name__: func},
        number=number
    )
    print(f"{func_name:<25}: {duration:.5f} seconds")
    return duration

def compare(size: int) -> list[float, float]:
    MatA = list(range(10))
    MatB = list(range(10))

    # Benchmark the pure Python function
    duration_py = _benchmark(
        f"Row Sums - Py ({size}x{size})",
        "dot_product_py(MatA, MatB)",
        dot_product_py,
        MatA, MatB
    )

    # Benchmark the NumPy function
    MatA_np = np.array(MatB)
    MatB_np = np.array(MatA)
    duration_numpy = _benchmark(
        f"Row Sums - NumPy ({size})",
        "dot_product_numpy(MatA, MatB)",
        dot_product_numpy,
        MatA, MatB
    )

    # Calculate and print the runtime differences
    rt_diff = duration_numpy - duration_py
    p_diff = rt_diff / duration_py
    print(f"{size} Matrix - Runtime difference: {rt_diff:.5f} seconds")
    print(f"{size} Matrix - Percentage difference: {100 * p_diff:.2f} %\n")

    return rt_diff, p_diff, duration_py, duration_numpy


def run(matrix_sizes: Optional[list[int]] = None) -> tuple[list,list,list]:
    if not matrix_sizes:
        matrix_sizes = [x+1 for x in range(64)]
    
    rt_diffs = []  # To store runtime differences
    p_diffs = []   # To store percentage differences
    py_times = []
    numpy_times = []

    for size in matrix_sizes:
        rt_diff, p_diff, py_time, numpy_time = compare(size)
        rt_diffs.append(rt_diff)
        p_diffs.append(p_diff)
        py_times.append(py_time)
        numpy_times.append(numpy_time)

    return matrix_sizes, rt_diffs, p_diffs, py_times, numpy_times


def save_to_csv(matrix_sizes, py_times, numpy_times, rt_diffs, p_diffs, filename="benchmark_results.csv"):
    """Saves detailed benchmarking results to a CSV file."""
    header = [
        'Matrix Size (NxN)', 
        'Python Runtime (s)', 
        'NumPy Runtime (s)', 
        'Runtime Difference (s)', 
        'Percentage Difference (%)'
    ]

    rows = zip(
        matrix_sizes,
        py_times,
        numpy_times,
        rt_diffs,
        [100 * p for p in p_diffs]
    )

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Detailed results saved to '{filename}'.")

def plot(sizes, rt_diffs, p_diffs, py_times, numpy_times):
    p_diffs = [100 * x for x in p_diffs]
    # Plotting the results after the loop
    fig, ax = plt.subplots(1, 3, figsize=(12, 5))

    # Plot Runtime Differences
    ax[0].plot(sizes, rt_diffs, marker='o', color='b', label='Runtime Diff (seconds)')
    ax[0].set_title("Runtime Difference (Pure Python - NumPy)")
    ax[0].set_xlabel("Matrix Size (N)")
    ax[0].set_ylabel("Time Difference (seconds)")
    ax[0].grid(True)

    # Plot Percentage Differences
    ax[1].plot(sizes, p_diffs, marker='o', color='r', label='Percentage Diff')
    ax[1].set_title("Percentage Difference (Pure Python - NumPy)")
    ax[1].set_xlabel("Matrix Size (N)")
    ax[1].set_ylabel("Percentage Difference (%)")
    ax[1].grid(True)

    ax[2].plot(sizes, py_times, marker='o', color='green', label='Python')
    ax[2].plot(sizes, numpy_times, marker='o', color='orange', label='NumPy')
    ax[2].set_title("Absolute Runtime Comparison")
    ax[2].set_xlabel("Matrix Size (N)")
    ax[2].set_ylabel("Runtime (seconds)")
    ax[2].legend()
    ax[2].grid(True)

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    _x = run()
    save_to_csv(*_x,filename="../data/benchmark_dot_prod.csv")
    fig = plot(*_x)
    fig.savefig("../data/benchmark_dot_prod.png")  # Save as PNG, or change format as needed

