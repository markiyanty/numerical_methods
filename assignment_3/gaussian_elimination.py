import numpy as np

def gaussian_elimination(a, b):
    n = len(b)
    for k in range(n):
        # Нормалізація рядка k-го елемента
        for i in range(k+1, n):
            if a[k][k] == 0:
                return "Division by zero detected!"
            factor = a[i][k] / a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - factor * a[k][j]
            b[i] = b[i] - factor * b[k]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += a[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i][i]
        
    return x

# Приклад використання
a = np.array([[2, -3, 1], [1, 5, -4], [4, 1, -3]], dtype=float)
b = np.array([2, -5, -4], dtype=float)

x = gaussian_elimination(a, b)
print(x)
print("Розв'язок системи:", '\nx:', x[0], '\ny:', x[1], '\nz:', x[2])
