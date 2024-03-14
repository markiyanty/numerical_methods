# import sympy as sp
# import numpy as np

# def f(x):
#     return (3 - x**2) / 2

# def f1(x):
#     return sp.sin(x) + 1

# def f2(x):
#     return sp.log(x + 2) + 1

# def f3(x):
#     return 0.5*x + 1.5

# def simple_iteration(f, x0, epsilon=0.05, max_iter=100000):
#     x = x0
#     for i in range(max_iter):
#         x_new = f(x)
#         if abs(x_new - x) < epsilon:  
#             return x_new, i + 1  
#         x = x_new
#     raise ValueError(f"Метод не збігся після {max_iter} ітерацій")  


# root, iterations = simple_iteration(f, 2, 0.05, 10000000)
# print(f"Корінь: {root}, Кількість ітерацій: {iterations}")


import numpy as np

# Define the tridiagonal matrix A and vector b
A = np.array([
    [4.620, 1.730, 0.0, 0.0, 0.0],
    [1.940, 4.030, 1.010, 0.0, 0.0],
    [0.0, 1.710, 4.100, 1.810, 0.0],
    [0.0, 0.0, 1.960, 4.290, 1.130],
    [0.0, 0.0, 0.0, 1.800, 4.650]
])
b = np.array([6.350, 6.980, 7.620, 6.250, 1.800])

# Thomas algorithm for tridiagonal matrix system Ax=b
n = len(b)
# Decompose A into a, b, c
a = np.zeros(n-1)  # Sub-diagonal (a_1 to a_{n-1})
b_ = np.zeros(n)   # Main diagonal (b_1 to b_n)
c = np.zeros(n-1)  # Super-diagonal (c_1 to c_{n-1})

# Extracting a, b, c from A
b_[0] = A[0, 0]
c[0] = A[0, 1]
for i in range(1, n-1):
    a[i-1] = A[i, i-1]
    b_[i] = A[i, i]
    c[i] = A[i, i+1]
a[n-2] = A[n-1, n-2]
b_[n-1] = A[n-1, n-1]

# Forward sweep for coefficients
for i in range(1, n):
    m = a[i-1] / b_[i-1]
    b_[i] = b_[i] - m * c[i-1]
    b[i] = b[i] - m * b[i-1]

# Backward substitution
x = np.zeros(n)
x[n-1] = b[n-1] / b_[n-1]
for i in range(n-2, -1, -1):
    x[i] = (b[i] - c[i] * x[i+1]) / b_[i]

print(x)  # Solution vector
