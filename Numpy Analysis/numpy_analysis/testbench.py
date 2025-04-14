#TODO Seperate into subfiles. Make the scenarios expandable, such that I can vary the input, graph the outputs, and observe the moment numpy becomes more effective.

import numpy as np
import timeit

# 1. Matrix Multiplication (3x3)
def matmul_3x3_pure(a, b):
    return [
        [
            a[0][0]*b[0][j] + a[0][1]*b[1][j] + a[0][2]*b[2][j]
            for j in range(3)
        ],
        [
            a[1][0]*b[0][j] + a[1][1]*b[1][j] + a[1][2]*b[2][j]
            for j in range(3)
        ],
        [
            a[2][0]*b[0][j] + a[2][1]*b[1][j] + a[2][2]*b[2][j]
            for j in range(3)
        ],
    ]

def matmul_3x3_numpy(a, b):
    return np.dot(np.array(a), np.array(b))


# 2. Row Sum
def row_sums_pure(matrix):
    return [sum(row) for row in matrix]

def row_sums_numpy(matrix):
    return np.sum(np.array(matrix), axis=1)


# 3. Count Above Threshold
def count_above_threshold_pure(lst, threshold):
    count = 0
    for x in lst:
        if x > threshold:
            count += 1
    return count

def count_above_threshold_numpy(lst, threshold):
    return np.sum(np.array(lst) > threshold)


# 4. Dot Product
def dot_product_pure(a, b):
    return sum(x * y for x, y in zip(a, b))

def dot_product_numpy(a, b):
    return np.dot(np.array(a), np.array(b))


# 5. Diagonal Matrix Multiplication
def diag_mul_pure(D, A):
    return [[D[i]*val for val in row] for i, row in enumerate(A)]

def diag_mul_numpy(D, A):
    return np.dot(np.diag(D), A)


def benchmark(func_name, stmt, setup, number=100000):
    duration = timeit.timeit(stmt=stmt, setup=setup, number=number)
    print(f"{func_name:<35}: {duration:.5f} seconds")

if __name__ == "__main__":
    print("Benchmarking Pure Python vs NumPy\n")

    # Matrix data
    A3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B3 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    L10 = list(range(10))
    A_diag = [[1, 2], [3, 4]]
    D = [2, 3]

    benchmark("Matrix Multiplication - Pure", 
              "matmul_3x3_pure(A3, B3)", 
              "from __main__ import matmul_3x3_pure, A3, B3")

    benchmark("Matrix Multiplication - NumPy", 
              "matmul_3x3_numpy(A3, B3)", 
              "from __main__ import matmul_3x3_numpy, A3, B3")

    benchmark("Row Sums - Pure", 
              "row_sums_pure(A3)", 
              "from __main__ import row_sums_pure, A3")

    benchmark("Row Sums - NumPy", 
              "row_sums_numpy(A3)", 
              "from __main__ import row_sums_numpy, A3")

    benchmark("Count > 5 - Pure", 
              "count_above_threshold_pure(L10, 5)", 
              "from __main__ import count_above_threshold_pure, L10")

    benchmark("Count > 5 - NumPy", 
              "count_above_threshold_numpy(L10, 5)", 
              "from __main__ import count_above_threshold_numpy, L10")

    benchmark("Dot Product - Pure", 
              "dot_product_pure(L10, L10)", 
              "from __main__ import dot_product_pure, L10")

    benchmark("Dot Product - NumPy", 
              "dot_product_numpy(L10, L10)", 
              "from __main__ import dot_product_numpy, L10")

    benchmark("Diag Mul - Pure", 
              "diag_mul_pure(D, A_diag)", 
              "from __main__ import diag_mul_pure, D, A_diag")

    benchmark("Diag Mul - NumPy", 
              "diag_mul_numpy(D, A_diag)", 
              "from __main__ import diag_mul_numpy, D, A_diag")