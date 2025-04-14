"""
Filename: row_sums.py
Description: Contains numpy and pythonic implementation of row summations of a matrix.

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


def row_sums_py(matrix):
    """Python row summation"""
    return [sum(row) for row in matrix]

def row_sums_numpy(matrix):
    """Numpy row summation"""
    return np.sum(np.array(matrix), axis=1)

def _benchmark_old(func_name, stmt, setup, number=100000):
    duration = timeit.timeit(stmt=stmt, setup=setup, number=number)
    return duration

def _benchmark(func_name, stmt, func, matrix, number=100000):
    duration = timeit.timeit(
        stmt=stmt,
        globals={"Mat": matrix, func.__name__: func},
        number=number
    )
    print(f"{func_name:<25}: {duration:.5f} seconds")
    return duration

def compare(size: int) -> list[float, float]:
    Mat = generate_matrix(size)

    # Benchmark the pure Python function
    duration_py = _benchmark(
        f"Row Sums - Py ({size}x{size})",
        "row_sums_py(Mat)",
        row_sums_py,
        Mat
    )

    # Benchmark the NumPy function
    Mat_np = np.array(Mat)
    duration_numpy = _benchmark(
        f"Row Sums - NumPy ({size}x{size})",
        "row_sums_numpy(Mat)",
        row_sums_numpy,
        Mat_np
    )

    # Calculate and print the runtime differences
    rt_diff = duration_numpy - duration_py
    p_diff = rt_diff / duration_py
    print(f"{size}x{size} Matrix - Runtime difference: {rt_diff:.5f} seconds")
    print(f"{size}x{size} Matrix - Percentage difference: {100 * p_diff:.2f} %\n")

    return rt_diff, p_diff, duration_py, duration_numpy

def run(matrix_sizes: Optional[list[int]] = None) -> tuple[list,list,list]:
    if not matrix_sizes:
        matrix_sizes = [3, 4, 5, 6, 7, 8, 15, 16, 17, 31, 32, 33, 63, 64, 65]
    
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
        print(size)

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
    ax[0].set_xlabel("Matrix Size (NxN)")
    ax[0].set_ylabel("Time Difference (seconds)")
    ax[0].grid(True)

    # Plot Percentage Differences
    ax[1].plot(sizes, p_diffs, marker='o', color='r', label='Percentage Diff')
    ax[1].set_title("Percentage Difference (Pure Python - NumPy)")
    ax[1].set_xlabel("Matrix Size (NxN)")
    ax[1].set_ylabel("Percentage Difference (%)")
    ax[1].grid(True)

    ax[2].plot(sizes, py_times, marker='o', color='green', label='Python')
    ax[2].plot(sizes, numpy_times, marker='o', color='orange', label='NumPy')
    ax[2].set_title("Absolute Runtime Comparison")
    ax[2].set_xlabel("Matrix Size (NxN)")
    ax[2].set_ylabel("Runtime (seconds)")
    ax[2].legend()
    ax[2].grid(True)

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    _x = run()
    save_to_csv(*_x,filename="../data/benchmark_row_sums.csv")
    fig = plot(*_x)
    fig.savefig("../data/benchmark_row_sums.png")  # Save as PNG, or change format as needed

