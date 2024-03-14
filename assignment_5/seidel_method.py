import numpy as np

def seidel_method(A, b, eps=1e-10, max_iterations=1000):
    n = A.shape[0]
    x = np.zeros(n)
    
    converge = False
    for k in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < eps:
            converge = True
            break
        
        x = x_new
    
    if not converge:
        print("Метод не збігся після {} ітерацій".format(max_iterations))
    return x

# Приклад використання методу Зейделя
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]])
b = np.array([15, 10, 10, 10])

solution = seidel_method(A, b)
print("Розв'язок СЛАР: ", solution)
